"""Dynamic crosswalk tests — QUALITY metric.

Parameterized across all defined crosswalk mappings.
"""

import pytest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from standard.crosswalks import crosswalk, list_crosswalks, CROSSWALK_TABLE

ALL_MAPPINGS = [
    (f, e, t, info["entity"], info["mapping"])
    for (f, e, t), info in CROSSWALK_TABLE.items()
]


@pytest.mark.parametrize(
    "from_std,entity,to_std,expected_entity,mapping_type",
    ALL_MAPPINGS,
    ids=[f"{f}.{e}->{t}" for f, e, t, _, _ in ALL_MAPPINGS]
)
def test_crosswalk_lookup(from_std, entity, to_std, expected_entity, mapping_type):
    """Every defined crosswalk must resolve correctly."""
    result = crosswalk(from_std, entity, to_std)
    assert result is not None
    assert result["entity"] == expected_entity
    assert result["mapping"] == mapping_type


def test_crosswalk_missing():
    """Non-existent crosswalks return None."""
    result = crosswalk("FAKE", "nothing", "NOPE")
    assert result is None


def test_list_all():
    """List all crosswalks returns correct count."""
    all_cw = list_crosswalks()
    assert len(all_cw) == len(CROSSWALK_TABLE)


def test_list_filtered():
    """List filtered by source standard works."""
    isa95 = list_crosswalks("ISA-95")
    assert all(c["from"] == "ISA-95" for c in isa95)
    assert len(isa95) >= 1
