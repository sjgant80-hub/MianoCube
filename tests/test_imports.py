"""Dynamic import tests — AVAILABILITY metric.

Auto-discovers every .py module under src/ and verifies
it imports without errors. One test per module.
"""

import os
import sys
import pytest

TESTS = os.path.dirname(__file__)
SRC = os.path.join(TESTS, '..', 'src')
sys.path.insert(0, SRC)
sys.path.insert(0, TESTS)

from templates import ImportTestTemplate

MODULES = ImportTestTemplate.discover(SRC)


@pytest.mark.parametrize("dotpath,filepath", MODULES, ids=[m[0] for m in MODULES])
def test_module_imports(dotpath, filepath):
    """Each source module must import cleanly."""
    ok, err = ImportTestTemplate.try_import(dotpath, SRC)
    assert ok, f"Failed to import {dotpath}: {err}"
