# MianoCube

**Konomi Cube Tutorial for Stephen Miano**
*By Thomas Frumkin*

An enterprise-scaled, modular tutorial repo teaching the Konomi Cube
architecture — from eVGPU tensor ops to 86-billion-neuron brain
simulations. Every source file is under 250 tokens.

## Live Demo

Enable GitHub Pages (Settings > Pages > Source: main) to see the
interactive 3D "Cubes Are Neurons" visualization.

## Quick Start

```bash
pip install numpy
cd src
python -c "
from core import KonomiSystem
import numpy as np, asyncio

K = KonomiSystem()
ba = K.create_block_array('main', (10,10,10))
ba.set(0,0,0, 1.0)
cube = K.create_cube('c1')
cube.connect('NEU', 'SWD')
a, b = np.random.randn(4,4), np.random.randn(4,4)
print('Tensor result shape:', K.evgpu.tensor(a, b, '@').shape)
print('Status:', K.status())
print('LLM:', asyncio.run(cube.process_vertex('NEU', 'Hello Stephen')))
"
```

## Repository Structure

```
MianoCube/
├── app/                    # GitHub Pages 3D visualization
│   ├── index.html          #   entry point
│   ├── css/style.css       #   dark theme
│   ├── data/levels.json    #   9 brain nesting levels
│   └── js/                 #   modular Three.js scripts
│       ├── scene.js        #     renderer + camera
│       ├── controls.js     #     mouse drag rotation
│       ├── viz.js          #     box/dot/line builders
│       ├── rebuild.js      #     per-level 3D visuals
│       ├── levels.js       #     nav + level switching
│       └── animate.js      #     render loop
│
├── src/                    # Python source (enterprise-scaled)
│   ├── core/               #   4 building blocks
│   │   ├── evgpu.py        #     CPU tensor processor
│   │   ├── femtollm.py     #     16-dim nano LLM
│   │   ├── blockarray.py   #     3D compute grid
│   │   ├── cube.py         #     9-node processor
│   │   └── system.py       #     top-level orchestrator
│   ├── api/                #   interface layer
│   │   ├── rest.py         #     REST for BlockArrays
│   │   └── websocket.py    #     WebSocket for Cubes
│   ├── standard/           #   Konomi Standard (10 layers)
│   │   ├── meta.py         #     Layer 0: meta-standard
│   │   ├── base_udts.py    #     Layer 1: shared types
│   │   ├── isa95.py        #     Layer 2: enterprise
│   │   ├── isa88.py        #     Layer 3: batch control
│   │   ├── isa101.py       #     Layer 4: HMI design
│   │   ├── isa18_2.py      #     Layer 5: alarms
│   │   ├── opcua.py        #     Layer 6: OPC-UA
│   │   ├── sparkplug.py    #     Layer 7: MQTT
│   │   ├── modbus.py       #     Layer 8: field protocol
│   │   ├── kpis.py         #     Layer 9: OEE metrics
│   │   └── crosswalks.py   #     standard-to-standard maps
│   └── kontainer/          #   deployment configs
│       ├── docker-compose.yml
│       ├── Dockerfile.api
│       └── Dockerfile.ws
│
├── prompts/                # Original build prompts
│   ├── 01-konomi-build-spec.md
│   ├── 02-cubes-are-neurons.md
│   └── 03-konomi-standard.md
│
├── docs/tutorials/         # Step-by-step tutorials
│   ├── 00-overview.md      #   start here
│   ├── 01-evgpu.md         #   electronic virtual GPU
│   ├── 02-femtollm.md      #   nano language model
│   ├── 03-blockarray.md    #   3D compute grid
│   ├── 04-cube.md          #   9-node processor
│   ├── 05-system.md        #   orchestrator
│   ├── 06-apis.md          #   REST + WebSocket
│   ├── 07-standard.md      #   Konomi Standard overview
│   ├── 08-visualization.md #   3D brain app
│   └── 09-kontainer.md     #   deployment
│
└── .github/workflows/
    └── pages.yml           # auto-deploy to GitHub Pages
```

## Tutorials

Start at `docs/tutorials/00-overview.md` and work through each file
in order. Every tutorial has runnable code examples.

| # | Topic           | File                   |
|---|-----------------|------------------------|
| 0 | Overview        | `00-overview.md`       |
| 1 | eVGPU           | `01-evgpu.md`          |
| 2 | FemtoLLM        | `02-femtollm.md`       |
| 3 | BlockArray      | `03-blockarray.md`     |
| 4 | Cube            | `04-cube.md`           |
| 5 | KonomiSystem    | `05-system.md`         |
| 6 | APIs            | `06-apis.md`           |
| 7 | Konomi Standard | `07-standard.md`       |
| 8 | Visualization   | `08-visualization.md`  |
| 9 | Kontainer       | `09-kontainer.md`      |

## The Core Idea

**A cube is a neuron.** 8 cubes nest inside a bigger cube.
Repeat 12 times and you have 86 billion — a human brain.
Each cube runs a tiny LLM. The eVGPU does tensor math on
CPU. No GPU needed. The Konomi Standard maps this to
real industrial systems (factories, control rooms, SCADA).

## Kontainer Deployment

```bash
docker-compose -f src/kontainer/docker-compose.yml up
```

| Service | Port | Role                |
|---------|------|---------------------|
| web     | 3000 | 3D visualization    |
| api     | 3001 | REST BlockArray API |
| ws      | 3002 | WebSocket Cube API  |
