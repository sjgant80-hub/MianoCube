/**
 * viz.js — 3D visualization builders.
 *
 * Adds wireframe boxes, glowing dots, and connection lines.
 * Builds nested cube structures per level.
 */

function addBox(x, y, z, size, color, opacity) {
  const edges = new THREE.EdgesGeometry(
    new THREE.BoxGeometry(size, size, size)
  );
  const wire = new THREE.LineSegments(edges,
    new THREE.LineBasicMaterial({
      color, transparent: true, opacity
    })
  );
  wire.position.set(x, y, z);
  grp.add(wire);
}

function addDot(x, y, z, size, color, opacity) {
  const dot = new THREE.Mesh(
    new THREE.SphereGeometry(size, 6, 6),
    new THREE.MeshBasicMaterial({
      color, transparent: true, opacity,
      blending: THREE.AdditiveBlending
    })
  );
  dot.position.set(x, y, z);
  grp.add(dot);
}

function addLine(p1, p2, color, opacity) {
  const geo = new THREE.BufferGeometry().setFromPoints([p1, p2]);
  grp.add(new THREE.Line(geo,
    new THREE.LineBasicMaterial({
      color, transparent: true, opacity
    })
  ));
}

function nestCubes(x, y, z, size, depth, maxDepth) {
  const color = levels[Math.min(depth, levels.length - 1)].color;
  const opacity = Math.max(0.08, 0.6 - depth * 0.12);
  addBox(x, y, z, size, color, opacity);

  if (depth >= maxDepth) {
    addDot(x, y, z, size * 0.06, color, 0.5);
    return;
  }

  const childSize = size * 0.38;
  const offset = size * 0.27;
  const corners = [
    [-1,-1,-1],[1,-1,-1],[-1,1,-1],[1,1,-1],
    [-1,-1,1],[1,-1,1],[-1,1,1],[1,1,1]
  ];
  corners.forEach(([cx, cy, cz]) => {
    nestCubes(
      x + cx * offset, y + cy * offset, z + cz * offset,
      childSize, depth + 1, maxDepth
    );
  });
}
