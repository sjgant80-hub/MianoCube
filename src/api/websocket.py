"""WebSocket API for Cube operations.

Actions:
  initialize — set up a cube
  process    — run LLM at a vertex
  connect    — link two vertices
  status     — get all vertex states

Tutorial:
    server = create_ws_server(system)
    # Handles JSON messages over ws://host:6789
"""

import json
from ..core.system import KonomiSystem


def create_ws_server(system: KonomiSystem):
    """Create a WebSocket message handler.

    Returns an async handler function.
    """

    async def handle_message(raw: str) -> str:
        msg = json.loads(raw)
        action = msg.get("action")

        if action == "initialize":
            cube_id = msg.get("cube_id", "default")
            system.create_cube(cube_id)
            return json.dumps({"status": "initialized", "cube": cube_id})

        if action == "process":
            cube_id = msg.get("cube_id", "default")
            vertex = msg["vertex"]
            text = msg["text"]
            cube = system.cubes.get(cube_id)
            if not cube:
                return json.dumps({"error": "cube not found"})
            result = await cube.process_vertex(vertex, text)
            return json.dumps({"result": result})

        if action == "connect":
            cube_id = msg.get("cube_id", "default")
            cube = system.cubes.get(cube_id)
            if not cube:
                return json.dumps({"error": "cube not found"})
            cube.connect(msg["source"], msg["target"])
            return json.dumps({"status": "connected"})

        if action == "status":
            cube_id = msg.get("cube_id", "default")
            cube = system.cubes.get(cube_id)
            if not cube:
                return json.dumps({"error": "cube not found"})
            states = {v: llm.state for v, llm in cube.verts.items()}
            return json.dumps({"vertices": states})

        return json.dumps({"error": f"unknown action: {action}"})

    return handle_message
