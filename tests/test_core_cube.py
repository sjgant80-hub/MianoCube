"""Dynamic Cube tests — PERFORMANCE metric.

Parameterized across all 8 vertices and edge patterns.
"""

import pytest
import asyncio
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from core.cube import VERTICES

ALL_EDGES = [
    ("NEU", "SWD"),  # diagonal
    ("NED", "SWU"),  # diagonal
    ("NEU", "NED"),  # same face
    ("SEU", "SWU"),  # same face
]


def test_cube_has_all_vertices(cube):
    """Cube must have all 8 vertex LLMs."""
    assert len(cube.verts) == 8
    for v in VERTICES:
        assert v in cube.verts


def test_cube_has_central(cube):
    """Cube must have a central LLM."""
    assert cube.central is not None


@pytest.mark.parametrize("src,dst", ALL_EDGES)
def test_connect_bidirectional(cube, src, dst):
    """Connecting two vertices creates edges both ways."""
    cube.connect(src, dst)
    assert dst in cube.neighbors(src)
    assert src in cube.neighbors(dst)


@pytest.mark.parametrize("vertex", VERTICES)
def test_process_all_vertices(cube, vertex):
    """Every vertex processes text without error."""
    result = asyncio.get_event_loop().run_until_complete(
        cube.process_vertex(vertex, f"Hello from {vertex}")
    )
    assert isinstance(result, str)


def test_neighbors_empty_default(cube):
    """Unconnected vertex has no neighbors."""
    assert cube.neighbors("NEU") == []


def test_multiple_connections(cube):
    """A vertex can connect to many others."""
    cube.connect("NEU", "NED")
    cube.connect("NEU", "SEU")
    cube.connect("NEU", "SWD")
    assert len(cube.neighbors("NEU")) == 3
