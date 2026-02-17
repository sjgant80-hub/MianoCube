# Tutorial 6: APIs

**REST for BlockArrays, WebSocket for Cubes**

## REST API (`src/api/rest.py`)

BlockArray operations over HTTP:

```
POST /template/create   — make a new 3D grid
GET  /value?x,y,z      — read a cell value
POST /value             — write a cell value
POST /llm/process       — run LLM at coordinate
```

```python
from src.core import KonomiSystem
from src.api import create_rest_app

system = KonomiSystem()
routes = create_rest_app(system)

# Simulate a request
routes["POST /template/create"]("main", (10,10,10))
result = routes["GET /value"]("main", 0, 0, 0)
```

## WebSocket API (`src/api/websocket.py`)

Cube operations over ws://

```json
{"action": "initialize", "cube_id": "c1"}
{"action": "process", "cube_id": "c1", "vertex": "NEU", "text": "Hi"}
{"action": "connect", "cube_id": "c1", "source": "NEU", "target": "SWD"}
{"action": "status", "cube_id": "c1"}
```

## Why Two Protocols?

- REST: stateless, good for grid reads/writes
- WebSocket: persistent connection, good for real-time vertex processing

## Try It

Call every REST route in sequence. Initialize a cube
over WebSocket, then connect and process.
