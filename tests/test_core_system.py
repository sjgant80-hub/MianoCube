"""Dynamic KonomiSystem tests — PERFORMANCE metric.

Tests the orchestrator's ability to manage components.
"""

import pytest
import numpy as np


def test_system_creates_with_evgpu(system):
    """System initializes with an eVGPU."""
    assert system.evgpu is not None
    assert system.evgpu.cores == 2


def test_create_block_array(system):
    """System registers block arrays by name."""
    ba = system.create_block_array("test", (3, 3, 3))
    assert "test" in system.arrays
    assert ba.arr.shape == (3, 3, 3)


def test_create_cube(system):
    """System registers cubes by id."""
    c = system.create_cube("c1")
    assert "c1" in system.cubes
    assert len(c.verts) == 8


def test_status_empty(system):
    """Empty system reports no arrays or cubes."""
    s = system.status()
    assert s["arrays"] == []
    assert s["cubes"] == []
    assert s["evgpu_cores"] == 2


def test_status_populated(system):
    """Status reflects created components."""
    system.create_block_array("a1", (2, 2, 2))
    system.create_block_array("a2", (3, 3, 3))
    system.create_cube("c1")
    s = system.status()
    assert len(s["arrays"]) == 2
    assert len(s["cubes"]) == 1


def test_evgpu_through_system(system):
    """eVGPU tensor ops work through the system."""
    a = np.eye(4)
    b = np.ones((4, 4))
    result = system.evgpu.tensor(a, b, "@")
    np.testing.assert_array_equal(result, b)
