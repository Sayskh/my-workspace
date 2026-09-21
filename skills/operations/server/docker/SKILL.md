---
name: server-docker
description: any task related to docker, containers, swarm, compose, images
metadata:
  hermes:
    tags: [server, homelab, devops, sysadmin, docker]
    category: server
---

# docker
version: 29.x
os: linux
loaded_when: any task related to docker, containers, swarm, compose, images

## Detection
```bash
docker version
docker info
docker node ls 2>/dev/null && echo "SWARM ACTIVE"
```

## Containers
```bash
docker ps
docker ps -a
docker logs <container> --tail 30
docker logs <container> -f
docker inspect <container>
docker exec -it <container> bash
docker stats --no-stream
```

## Images
```bash
docker images
docker build -t <name>:<tag> -f <Dockerfile> <context>
# IMPORTANT: context = parent directory of all files referenced in Dockerfile
# Correct: cd ~/.argos && docker build -t argos:latest -f docker/Dockerfile .
docker rmi <image>
docker image prune -f
```

## Compose (non-Swarm)
```bash
docker compose -f <path>/docker-compose.yml up -d
docker compose -f <path>/docker-compose.yml up -d --force-recreate
docker compose -f <path>/docker-compose.yml down
docker compose -f <path>/docker-compose.yml logs --tail 30
```

## Swarm
```bash
# Init manager
docker swarm init --advertise-addr <IP>
# Join worker
docker swarm join --token <token> <manager-IP>:2377
# Recover join token
docker swarm join-token worker
# Node status
docker node ls
# Deploy stack
docker stack deploy -c swarm-stack.yml <stack-name>
docker stack ls
docker stack ps <stack-name>
docker stack rm <stack-name>
docker service ls
docker service logs <service> --tail 30
docker service ps <service> --no-trunc
# Update image in Swarm
docker service update --image <registry>/<image>:<tag> <service>
```

## Swarm - required open ports on MANAGER
- TCP <published port> (e.g. 666)
- TCP 2377 — cluster management
- TCP/UDP 7946 — node communication
- UDP 4789 — overlay network

## Local Registry (multi-node Swarm)
```bash
# Start registry
docker run -d --name argos-registry --restart unless-stopped -p 5000:5000 -v registry-data:/var/lib/registry registry:2
# Tag and push
docker tag <image>:latest <IP>:5000/<image>:latest
docker push <IP>:5000/<image>:latest
# Insecure registry on NixOS (configuration.nix):
# daemon.settings = { insecure-registries = [ "<IP>:5000" ]; };
# Insecure registry on Debian (/etc/docker/daemon.json):
# {"insecure-registries":["<IP>:5000"]}
# then: systemctl restart docker
```

## Volumes
```bash
docker volume ls
docker volume inspect <volume>
docker volume rm <volume>
```

## Secrets (Swarm)
```bash
printf 'value' | docker secret create <name> -
docker secret ls
docker secret rm <name>
```

## Postgres in container
```bash
# Dump from container
docker exec <container> pg_dump -U <user> <db> | gzip > backup.sql.gz
# Dump from external postgres (NixOS requires nix-shell)
nix-shell -p postgresql --run "pg_dump -h <host> -U <user> -d <db>" | gzip > backup.sql.gz
# Restore into container
gunzip -c backup.sql.gz | docker exec -i <container> psql -U <user> -d <db>
# Direct psql access
docker exec -it <container> psql -U <user> -d <db>
# PG version upgrade (e.g. 16->17): dump old container, rm container+volume, new container, restore
```

## Nvidia GPU in container (NixOS)
```bash
# In configuration.nix:
# virtualisation.docker.enableNvidia = true;
# hardware.nvidia-container-toolkit.enable = true;
# Test:
docker run --rm --gpus all ubuntu nvidia-smi
# Container with GPU:
docker run -d --gpus all --name <container> <image>
```

## CRITICAL Gotchas
- depends_on with condition: and container_name = incompatible with Swarm — use only for classic compose
- version: in docker-compose.yml = obsolete in new versions — remove it
- expanduser("~") in container = home of user INSIDE container, not host user — use ABSOLUTE PATH
- Wrong build context = "file not found" — context must be parent of all files in Dockerfile
- Port already in use on host = container fails to start — check with ss -tlnp | grep <port>
- Swarm ports blocked by NixOS firewall by default — add explicitly
- Swarm ingress does not respond on localhost — use real machine IP
- DB_HOST in Swarm overlay = real host IP (e.g. 11.11.11.111), NOT 172.17.0.1
- 172.17.0.1 works only for classic compose (bridge network)
- Swarm join timeout = firewall blocking port 2377, not a network issue
- /etc/nixos does not exist in container — do not include in WATCHED_FILES without explicit mount
- Bind-mount volumes must exist physically on EVERY Swarm node where container runs
- NFS mounted on host = Docker sees it as normal bind mount — works transparently
- WORKDIR in Dockerfile must be the ABSOLUTE PATH of the code, not generic /app
- working_dir in compose/stack overrides WORKDIR from Dockerfile
- Swarm overlay network: containers on different nodes communicate via overlay, not bridge

## Reference Multi-Node Cluster Architecture
### Node 1 — Swarm Manager (e.g., NixOS / Debian)
- `app-server` — Main application replica
- `db-server` — PostgreSQL 17 primary instance
- `ollama-gpu` — Ollama GPU inference service
- `local-registry` — Private container registry on port 5000

### Node 2 — Swarm Worker (e.g., Debian / Ubuntu)
- `app-server` — Secondary application replica
- `db-standby` — PostgreSQL 17 standby replica (streaming replication)

