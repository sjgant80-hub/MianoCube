# 🧊 CUBES ARE NEURONS — Visualization Prompt

## Overview

Interactive Three.js visualization showing how cubes map to brain
structures across 9 nesting levels — from 1 neuron to 86 billion.

## Levels

| Level | Cubes          | Brain Structure     |
|-------|----------------|---------------------|
| 0     | 1              | Single Neuron       |
| 1     | 8              | Microcircuit        |
| 2     | 64             | Minicolumn          |
| 3     | 512            | Macrocolumn         |
| 4     | 4,096          | Cortical Area       |
| 5     | 32,768         | Brain Region        |
| 6     | 262,144        | Functional Network  |
| 7     | 2,097,152      | Hemisphere          |
| 8     | 86,000,000,000 | Full Brain          |

## Key Concepts

- **1 Cube = 1 Neuron**: 6 faces = connection points
- **8x Nesting**: Each level nests 8 of the previous
- **Depth 12**: Full brain = 10 x 8^11 cubes
- **128 Connections**: 2^7 connections per neuron (Raphael's number)
- **2 Empty Corners**: Room to grow at the top level

## Tech Stack

- Three.js r128 for 3D rendering
- Wireframe cubes with additive blending
- Mouse drag rotation + arrow key navigation
- Responsive camera zoom per level

## Features

- Click navigation tabs to switch levels
- Arrow keys for sequential browsing
- Drag to rotate the 3D scene
- Scale bar shows logarithmic progression
- Pulsing glow on mesh nodes

## Source

The full HTML source is deployed at `app/index.html` in this repo
and served via GitHub Pages.
