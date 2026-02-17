# Tutorial Overview

**Hey Stephen!** Welcome to MianoCube.

This repo teaches you the Konomi Cube system step by step.
Built by Thomas Frumkin for you to learn at your own pace.

## What You'll Learn

1. **eVGPU** — Run AI tensor ops on CPU (no GPU needed)
2. **FemtoLLM** — A tiny 16-dimension language model
3. **BlockArray** — A 3D grid of compute cells
4. **Cube** — A 9-node processing unit (8 vertices + center)
5. **APIs** — REST and WebSocket interfaces
6. **Konomi Standard** — Industrial standards (ISA-95, 88, etc.)
7. **Cubes Are Neurons** — The 3D brain visualization

## How to Navigate

- `src/core/` — Python source code for each component
- `src/standard/` — The Konomi Standard implementations
- `src/api/` — REST and WebSocket API layers
- `app/` — GitHub Pages 3D visualization
- `prompts/` — The original build prompts
- `docs/tutorials/` — You are here! Start with `01-evgpu.md`

## Quick Run

```bash
cd src && python -c "from core import KonomiSystem; print(KonomiSystem().status())"
```
