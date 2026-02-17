"""Dynamic WebSocket API tests — PERFORMANCE metric.

Tests every action type with parameterized inputs.
"""

import pytest
import json
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

ACTIONS = ["initialize", "process", "connect", "status"]


@pytest.fixture
def handler(system):
    from api import create_ws_server
    return create_ws_server(system)


@pytest.mark.asyncio
async def test_initialize(handler):
    """Initialize action creates a cube."""
    resp = await handler(json.dumps({
        "action": "initialize", "cube_id": "ws1"
    }))
    data = json.loads(resp)
    assert data["status"] == "initialized"


@pytest.mark.asyncio
async def test_process_vertex(handler):
    """Process action runs LLM at vertex."""
    await handler(json.dumps({"action": "initialize", "cube_id": "ws2"}))
    resp = await handler(json.dumps({
        "action": "process", "cube_id": "ws2",
        "vertex": "NEU", "text": "hello"
    }))
    data = json.loads(resp)
    assert "result" in data


@pytest.mark.asyncio
async def test_connect(handler):
    """Connect action links two vertices."""
    await handler(json.dumps({"action": "initialize", "cube_id": "ws3"}))
    resp = await handler(json.dumps({
        "action": "connect", "cube_id": "ws3",
        "source": "NEU", "target": "SWD"
    }))
    data = json.loads(resp)
    assert data["status"] == "connected"


@pytest.mark.asyncio
async def test_status(handler):
    """Status action returns vertex states."""
    await handler(json.dumps({"action": "initialize", "cube_id": "ws4"}))
    resp = await handler(json.dumps({"action": "status", "cube_id": "ws4"}))
    data = json.loads(resp)
    assert "vertices" in data
    assert len(data["vertices"]) == 8


@pytest.mark.asyncio
async def test_unknown_action(handler):
    """Unknown actions return error."""
    resp = await handler(json.dumps({"action": "explode"}))
    data = json.loads(resp)
    assert "error" in data


@pytest.mark.asyncio
async def test_missing_cube(handler):
    """Operations on non-existent cubes return error."""
    resp = await handler(json.dumps({
        "action": "status", "cube_id": "ghost"
    }))
    data = json.loads(resp)
    assert "error" in data
