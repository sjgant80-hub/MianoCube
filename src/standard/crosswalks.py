"""Crosswalks — Mappings between standards.

Maps entities from one standard to their equivalents in another.
Mapping types: exact, partial, semantic.

Tutorial:
    result = crosswalk("ISA-95", "WorkCenter", "ISA-88")
    # Returns: {"entity": "ProcessCell", "mapping": "exact"}
"""

CROSSWALK_TABLE = {
    ("ISA-95", "WorkCenter", "ISA-88"): {
        "entity": "ProcessCell", "mapping": "exact",
    },
    ("ISA-95", "WorkUnit", "ISA-88"): {
        "entity": "Unit", "mapping": "exact",
    },
    ("ISA-95", "ProcessSegment", "ISA-88"): {
        "entity": "Operation", "mapping": "exact",
    },
    ("ISA-95", "Equipment", "OPC-UA"): {
        "entity": "Object", "mapping": "exact",
    },
    ("ISA-95", "Property", "OPC-UA"): {
        "entity": "Variable", "mapping": "exact",
    },
    ("ISA-88", "Phase.RUNNING", "PackML"): {
        "entity": "EXECUTE", "mapping": "exact",
    },
    ("ISA-88", "Phase.HELD", "PackML"): {
        "entity": "HELD", "mapping": "exact",
    },
    ("OPC-UA", "Variable", "Sparkplug"): {
        "entity": "Metric", "mapping": "exact",
    },
    ("OPC-UA", "Method", "Sparkplug"): {
        "entity": "CMD", "mapping": "partial",
    },
}


def crosswalk(from_std: str, entity: str, to_std: str) -> dict | None:
    """Look up a crosswalk mapping."""
    return CROSSWALK_TABLE.get((from_std, entity, to_std))


def list_crosswalks(from_std: str = "") -> list[dict]:
    """List all crosswalk entries, optionally filtered."""
    results = []
    for (f_std, ent, t_std), info in CROSSWALK_TABLE.items():
        if from_std and f_std != from_std:
            continue
        results.append({
            "from": f_std, "entity": ent,
            "to": t_std, **info,
        })
    return results
