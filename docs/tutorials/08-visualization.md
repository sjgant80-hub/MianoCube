# Tutorial 8: Cubes Are Neurons

**The 3D brain visualization (GitHub Pages app)**

## What It Shows

9 levels of nesting — from 1 neuron to 86 billion.
Each level is 8x the previous (cube corners).

| Level | Cubes  | Brain Part        |
|-------|--------|-------------------|
| 0     | 1      | Single neuron     |
| 1     | 8      | Microcircuit      |
| 2     | 64     | Minicolumn        |
| 3     | 512    | Macrocolumn       |
| 4     | 4,096  | Cortical area     |
| 5     | 32K    | Brain region      |
| 6     | 262K   | Functional network|
| 7     | 2M     | Hemisphere        |
| 8     | 86B    | Full brain        |

## How the App Works

Files in `app/`:
- `index.html` — loads all scripts
- `css/style.css` — dark theme styling
- `data/levels.json` — level descriptions
- `js/scene.js` — Three.js setup
- `js/controls.js` — mouse drag rotation
- `js/viz.js` — box/dot/line builders
- `js/rebuild.js` — per-level visualization
- `js/levels.js` — nav and level switching
- `js/animate.js` — render loop

## Controls

- Click nav tabs to switch levels
- Arrow keys: Left/Right to browse
- Click and drag to rotate the 3D scene

## The Key Insight

**12 nesting depths** get you to 86 billion.
128 connections per neuron (2^7).
The connection layer nests 2 depths deeper
than the neuron layer.
