# Tutorial 4: The Cube

**9 nodes = 8 vertices + 1 center**

## The Idea

A cube has 8 corners. Each corner runs a FemtoLLM.
A 9th LLM sits at the center. Vertices connect via edges.

Labels use compass + altitude:
- N/S = North/South, E/W = East/West, U/D = Up/Down
- NEU = North-East-Up, SWD = South-West-Down, etc.

## Key Code (`src/core/cube.py`)

```python
from src.core import Cube
import asyncio

cube = Cube("c1")

# Connect two vertices
cube.connect("NEU", "SWD")  # diagonal link
print(cube.neighbors("NEU"))  # ['SWD']

# Process text at a vertex
result = asyncio.run(cube.process_vertex("NEU", "Hello"))
print(result)
```

## What to Notice

- 8 vertex labels cover all 3D corners
- `edges` is a dict of lists (adjacency list)
- Connections are bidirectional
- Each vertex is an independent FemtoLLM

## Brain Connection

At nesting depth 1, 8 cubes = 1 microcircuit.
That's 8 neurons that can "vote" together.
The cube IS the neuron at depth 0.

## Try It

Connect all 8 vertices to the center. Process text
at every vertex. What would a "consensus" look like?
