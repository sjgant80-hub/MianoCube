"""BlockArray — 3D compute grid with LLM at coordinates.

Default shape is 1000x1000x1000 (1 billion cells).
Each cell can hold a value and optionally an LLM instance.

Tutorial:
    ba = BlockArray((10, 10, 10))  # demo size
    ba.set(0, 0, 0, 1.0)
    llm = ba.llm_at(0, 0, 0)
"""

import numpy as np
from .femtollm import FemtoLLM


class BlockArray:
    """3D grid that maps coordinates to values and LLMs."""

    def __init__(self, dims: tuple = (10, 10, 10)):
        self.dims = dims
        self.arr = np.zeros(dims, dtype=np.float32)
        self.llms: dict[tuple, FemtoLLM] = {}

    def set(self, x: int, y: int, z: int, value: float):
        """Set a value at (x, y, z)."""
        self.arr[x, y, z] = value

    def get(self, x: int, y: int, z: int) -> float:
        """Get the value at (x, y, z)."""
        return float(self.arr[x, y, z])

    def llm_at(self, x: int, y: int, z: int) -> FemtoLLM:
        """Get or create an LLM at the coordinate."""
        key = (x, y, z)
        if key not in self.llms:
            self.llms[key] = FemtoLLM()
        return self.llms[key]

    @property
    def active_count(self) -> int:
        """Number of non-zero cells."""
        return int(np.count_nonzero(self.arr))
