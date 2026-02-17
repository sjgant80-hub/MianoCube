"""Shared fixtures for all MianoCube tests.

Provides pre-built instances of every core component
so tests stay DRY and consistent.
"""

import sys, os
import pytest
import numpy as np

# Ensure src is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


@pytest.fixture
def system():
    from core import KonomiSystem
    return KonomiSystem(cores=2)


@pytest.fixture
def evgpu():
    from core import eVGPU
    return eVGPU(cores=2)


@pytest.fixture
def femtollm():
    from core import FemtoLLM
    return FemtoLLM(seed=42)


@pytest.fixture
def blockarray():
    from core import BlockArray
    return BlockArray((5, 5, 5))


@pytest.fixture
def cube():
    from core import Cube
    return Cube("test-cube")


@pytest.fixture
def matrix_pair():
    rng = np.random.RandomState(99)
    return rng.randn(4, 4), rng.randn(4, 4)
