"""KonomiSystem — Top-level orchestrator.

Wires together eVGPU, BlockArrays, and Cubes.
This is the entry point for the quick-start tutorial.

Tutorial:
    K = KonomiSystem()
    ba = K.create_block_array("main", (10, 10, 10))
    cube = K.create_cube("c1")
"""

from .evgpu import eVGPU
from .blockarray import BlockArray
from .cube import Cube


class KonomiSystem:
    """Top-level Konomi orchestrator."""

    def __init__(self, cores: int = 4):
        self.evgpu = eVGPU(cores=cores)
        self.arrays: dict[str, BlockArray] = {}
        self.cubes: dict[str, Cube] = {}

    def create_block_array(
        self, name: str, dims: tuple = (10, 10, 10)
    ) -> BlockArray:
        """Create and register a BlockArray."""
        ba = BlockArray(dims)
        self.arrays[name] = ba
        return ba

    def create_cube(self, cube_id: str) -> Cube:
        """Create and register a Cube."""
        cube = Cube(cube_id)
        self.cubes[cube_id] = cube
        return cube

    def status(self) -> dict:
        """System status summary."""
        return {
            "arrays": list(self.arrays.keys()),
            "cubes": list(self.cubes.keys()),
            "evgpu_cores": self.evgpu.cores,
        }
