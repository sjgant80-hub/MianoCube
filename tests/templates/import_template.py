"""Import Test Template — verify every module is importable.

Dynamically discovers all .py files under src/ and generates
one test case per module. This measures AVAILABILITY.

Usage:
    cases = ImportTestTemplate.discover("src")
    # Returns: [("core.evgpu", "src/core/evgpu.py"), ...]
"""

import os
import importlib


class ImportTestTemplate:
    """Generate import test cases for all source modules."""

    @staticmethod
    def discover(src_root: str) -> list[tuple[str, str]]:
        """Find all .py modules under src_root.

        Returns (module_dotpath, file_path) pairs.
        """
        cases = []
        for dirpath, _, filenames in os.walk(src_root):
            for f in sorted(filenames):
                if not f.endswith('.py') or f.startswith('__'):
                    continue
                filepath = os.path.join(dirpath, f)
                rel = os.path.relpath(filepath, src_root)
                dotpath = rel.replace(os.sep, '.').removesuffix('.py')
                cases.append((dotpath, filepath))
        return cases

    @staticmethod
    def try_import(dotpath: str, src_root: str) -> tuple[bool, str]:
        """Attempt to import a module. Returns (success, error)."""
        import sys
        if src_root not in sys.path:
            sys.path.insert(0, src_root)
        try:
            importlib.import_module(dotpath)
            return True, ""
        except Exception as e:
            return False, str(e)
