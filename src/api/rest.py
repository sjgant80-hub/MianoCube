"""REST API for BlockArray operations.

Endpoints:
  POST /template/create  — create a new template
  POST /instance/create  — instantiate from template
  GET  /value            — read value at (x, y, z)
  POST /value            — write value at (x, y, z)
  POST /llm/process      — run LLM at coordinate

Tutorial:
    app = create_rest_app(system)
    # Then run with: uvicorn or similar
"""

try:
    from ..core.system import KonomiSystem
except ImportError:
    from core.system import KonomiSystem


def create_rest_app(system: KonomiSystem):
    """Create a REST application dict (framework-agnostic).

    Returns route definitions. Plug into Flask, FastAPI, etc.
    """
    routes = {}

    def template_create(name: str, dims: tuple):
        ba = system.create_block_array(name, dims)
        return {"status": "created", "name": name, "dims": dims}

    def value_get(array: str, x: int, y: int, z: int):
        ba = system.arrays.get(array)
        if not ba:
            return {"error": "array not found"}
        return {"value": ba.get(x, y, z)}

    def value_set(array: str, x: int, y: int, z: int, v: float):
        ba = system.arrays.get(array)
        if not ba:
            return {"error": "array not found"}
        ba.set(x, y, z, v)
        return {"status": "ok"}

    async def llm_process(array: str, x: int, y: int, z: int, text: str):
        ba = system.arrays.get(array)
        if not ba:
            return {"error": "array not found"}
        llm = ba.llm_at(x, y, z)
        result = await llm.process(text)
        return {"result": result}

    routes["POST /template/create"] = template_create
    routes["GET /value"] = value_get
    routes["POST /value"] = value_set
    routes["POST /llm/process"] = llm_process
    return routes
