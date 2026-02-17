"""Dynamic REST API tests — PERFORMANCE metric.

Tests every route handler with parameterized inputs.
"""

import pytest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

DIMS_CASES = [
    ("small", (3, 3, 3)),
    ("medium", (10, 10, 10)),
    ("tiny", (1, 1, 1)),
]


@pytest.fixture
def routes(system):
    from api import create_rest_app
    return create_rest_app(system)


@pytest.mark.parametrize("name,dims", DIMS_CASES, ids=[c[0] for c in DIMS_CASES])
def test_template_create(routes, name, dims):
    """Create templates of various sizes."""
    result = routes["POST /template/create"](name, dims)
    assert result["status"] == "created"
    assert result["dims"] == dims


def test_value_get_missing_array(routes):
    """Getting from non-existent array returns error."""
    result = routes["GET /value"]("nope", 0, 0, 0)
    assert "error" in result


def test_value_set_and_get(routes):
    """Set then get round-trip through REST."""
    routes["POST /template/create"]("rest_test", (5, 5, 5))
    routes["POST /value"]("rest_test", 1, 2, 3, 99.0)
    result = routes["GET /value"]("rest_test", 1, 2, 3)
    assert result["value"] == 99.0


def test_value_set_missing_array(routes):
    """Setting on non-existent array returns error."""
    result = routes["POST /value"]("nope", 0, 0, 0, 1.0)
    assert "error" in result


@pytest.mark.asyncio
async def test_llm_process(routes, system):
    """LLM process route runs without error."""
    system.create_block_array("llm_test", (5, 5, 5))
    result = await routes["POST /llm/process"]("llm_test", 0, 0, 0, "hi")
    assert "result" in result
