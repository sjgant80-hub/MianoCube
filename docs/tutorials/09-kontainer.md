# Tutorial 9: Kontainer Deployment

**Running MianoCube as microservices**

## Architecture

Three services, three ports:

| Service | Port | CPU  | Memory | Role              |
|---------|------|------|--------|-------------------|
| api     | 3001 | 1    | 1Gi    | REST BlockArray   |
| web     | 3000 | 0.5  | 512Mi  | GitHub Pages app  |
| ws      | 3002 | 0.5  | 512Mi  | WebSocket Cube    |

## Running Locally

```bash
docker-compose -f src/kontainer/docker-compose.yml up
```

## Services Explained

- **api** — handles all REST endpoints for BlockArray
  operations (create, get, set, LLM process)
- **web** — serves the static 3D visualization from `app/`
- **ws** — handles WebSocket connections for real-time
  Cube operations (initialize, process, connect)

## Environment Variables

```
DB_URL=postgresql://localhost:5432/konomi
REDIS_URL=redis://localhost:6379
```

These are optional — the core system works without
external databases. Add them when you need persistence.

## Scaling

Each service scales independently. Need more Cube
processing? Scale the `ws` service. Need more grid
reads? Scale the `api` service.
