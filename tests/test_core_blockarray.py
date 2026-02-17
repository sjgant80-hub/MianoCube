"""Dynamic BlockArray tests — PERFORMANCE metric.

Parameterized across grid sizes and coordinate patterns.
"""

import pytest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from core import BlockArray

DIMS = [(3, 3, 3), (5, 5, 5), (10, 10, 10), (1, 1, 1)]
COORDS = [(0, 0, 0), (1, 2, 3), (4, 4, 4)]


@pytest.mark.parametrize("dims", DIMS, ids=[f"{d[0]}x{d[1]}x{d[2]}" for d in DIMS])
def test_create_various_sizes(dims):
    """BlockArray initializes at different dimensions."""
    ba = BlockArray(dims)
    assert ba.arr.shape == dims
    assert ba.active_count == 0


@pytest.mark.parametrize("x,y,z", COORDS)
def test_set_get_roundtrip(blockarray, x, y, z):
    """Values survive a set/get cycle."""
    blockarray.set(x, y, z, 42.0)
    assert blockarray.get(x, y, z) == 42.0


def test_active_count(blockarray):
    """Active count tracks non-zero cells."""
    assert blockarray.active_count == 0
    blockarray.set(0, 0, 0, 1.0)
    blockarray.set(1, 1, 1, 2.0)
    assert blockarray.active_count == 2


def test_llm_at_creates_lazily(blockarray):
    """LLM is created on first access at a coordinate."""
    assert len(blockarray.llms) == 0
    llm = blockarray.llm_at(0, 0, 0)
    assert len(blockarray.llms) == 1
    # Same coord returns same instance
    assert blockarray.llm_at(0, 0, 0) is llm


def test_llm_at_different_coords(blockarray):
    """Different coords get different LLM instances."""
    a = blockarray.llm_at(0, 0, 0)
    b = blockarray.llm_at(1, 1, 1)
    assert a is not b
