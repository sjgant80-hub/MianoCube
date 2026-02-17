"""Cube — 9-node processing unit.

8 vertices (compass+altitude labels) + 1 central node.
Each node runs a FemtoLLM. Vertices connect via edges.

Vertex labels:
  NEU=NorthEastUp  NED=NorthEastDown
  NWU=NorthWestUp  NWD=NorthWestDown
  SEU=SouthEastUp  SED=SouthEastDown
  SWU=SouthWestUp  SWD=SouthWestDown

Tutorial:
    cube = Cube("c1")
    cube.connect("NEU", "SWD")  # diagonal
    result = await cube.process_vertex("NEU", "Hello")
"""

from collections import defaultdict
from .femtollm import FemtoLLM

VERTICES = [
    "NEU", "NED", "NWU", "NWD",
    "SEU", "SED", "SWU", "SWD",
]


class Cube:
    """9-node LLM processing unit."""

    def __init__(self, cube_id: str):
        self.id = cube_id
        self.verts = {v: FemtoLLM() for v in VERTICES}
        self.central = FemtoLLM()
        self.edges: dict[str, list[str]] = defaultdict(list)

    def connect(self, src: str, dst: str):
        """Create an edge between two vertices."""
        self.edges[src].append(dst)
        self.edges[dst].append(src)

    async def process_vertex(self, vertex: str, text: str) -> str:
        """Run text through a vertex LLM."""
        llm = self.verts[vertex]
        return await llm.process(text)

    def neighbors(self, vertex: str) -> list[str]:
        """List connected vertices."""
        return self.edges.get(vertex, [])
