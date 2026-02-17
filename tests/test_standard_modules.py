"""Dynamic module contract tests — PERFORMANCE metric.

Uses ModuleTestTemplate to verify every class instance
has the expected methods and attributes.
"""

import pytest
import sys, os
import numpy as np

_here = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(_here, '..', 'src'))
sys.path.insert(0, _here)

from templates import ModuleTestTemplate
from core import eVGPU, FemtoLLM, BlockArray, Cube, KonomiSystem
from standard.isa95 import Equipment
from standard.isa88 import Batch
from standard.isa18_2 import Alarm
from standard.kpis import OEE

# Build instances so we can check instance attributes too
INSTANCE_CONTRACTS = [
    (eVGPU(cores=2), ["tensor", "activate", "OPS", "cores"]),
    (FemtoLLM(), ["encode", "forward", "process", "HIDDEN", "state"]),
    (BlockArray((3, 3, 3)), ["set", "get", "llm_at", "active_count", "dims"]),
    (Cube("t"), ["connect", "process_vertex", "neighbors", "verts", "central"]),
    (KonomiSystem(), ["create_block_array", "create_cube", "status", "evgpu"]),
    (Equipment(id="E1", name="Test"), ["activate", "fault", "state", "mode"]),
    (Batch(id="B1", recipe="test"), ["start", "transition", "state", "events"]),
    (Alarm(tag="T1", type="HI"), ["activate", "acknowledge", "clear", "state"]),
    (OEE(run=100, down=0, actual=100, ideal=100, good=100, total=100),
     ["availability", "performance", "quality", "oee"]),
]

ALL_CHECKS = []
for instance, attrs in INSTANCE_CONTRACTS:
    cls_name = type(instance).__name__
    for attr in attrs:
        found = hasattr(instance, attr)
        ALL_CHECKS.append((cls_name, attr, found))


@pytest.mark.parametrize(
    "cls_name,attr,found", ALL_CHECKS,
    ids=[f"{c}.{a}" for c, a, _ in ALL_CHECKS]
)
def test_class_has_attribute(cls_name, attr, found):
    """Every class instance exposes its contracted attributes."""
    assert found, f"{cls_name} missing attribute: {attr}"
