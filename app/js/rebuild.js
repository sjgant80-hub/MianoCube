/**
 * rebuild.js — Rebuilds 3D visualization per level.
 *
 * Called by setLevel() whenever the user switches.
 * Each level has a unique visual representation.
 */

function rebuildViz(idx) {
  while (grp.children.length) grp.remove(grp.children[0]);
  const l = levels[idx];

  if (idx === 0) {
    addBox(0, 0, 0, 6, l.color, 0.8);
    const ax0 = new THREE.Vector3(0, -3, 0);
    const ax1 = new THREE.Vector3(0, -8, 0);
    addLine(ax0, ax1, 0xff6600, 0.5);
    addDot(0, -8, 0, 0.3, 0xff6600, 0.8);
    for (let d = 0; d < 5; d++) {
      const a = (d / 5) * Math.PI * 2;
      const tip = new THREE.Vector3(
        Math.cos(a) * 5, 3 + Math.sin(d) * 2, Math.sin(a) * 5
      );
      addLine(new THREE.Vector3(0, 3, 0), tip, 0x00ff88, 0.3);
      addDot(tip.x, tip.y, tip.z, 0.2, 0x00ff88, 0.6);
    }
    addDot(0, 0, 0, 0.5, 0xffffff, 0.4);
  } else if (idx <= 3) {
    nestCubes(0, 0, 0, 8, 0, Math.min(idx, 3));
  } else if (idx <= 6) {
    nestCubes(0, 0, 0, 10, 0, 4);
    const dotCount = Math.min(Math.pow(8, idx - 4), 60);
    for (let r = 0; r < dotCount; r++) {
      addDot(
        (Math.random() - 0.5) * 18,
        (Math.random() - 0.5) * 18,
        (Math.random() - 0.5) * 18,
        0.12, l.color, 0.4
      );
    }
  } else if (idx === 7) {
    nestCubes(-5.5, 0, 0, 7, 0, 3);
    nestCubes(5.5, 0, 0, 7, 0, 3);
    for (let b = 0; b < 8; b++) {
      const y = (b / 7 - 0.5) * 5;
      addLine(
        new THREE.Vector3(-2, y, 0),
        new THREE.Vector3(2, y, 0),
        0xffff00, 0.2
      );
    }
  } else {
    nestCubes(-5, 0, 0, 6.5, 0, 3);
    nestCubes(5, 0, 0, 6.5, 0, 3);
    for (let b = 0; b < 10; b++) {
      const y = (b / 9 - 0.5) * 5;
      addLine(
        new THREE.Vector3(-1.5, y, 0),
        new THREE.Vector3(1.5, y, 0),
        0xffff00, 0.15
      );
    }
    for (let s = 0; s < 150; s++) {
      const p1 = new THREE.Vector3(
        (Math.random()-0.5)*16,
        (Math.random()-0.5)*12,
        (Math.random()-0.5)*12
      );
      const p2 = p1.clone().add(new THREE.Vector3(
        (Math.random()-0.5)*3,
        (Math.random()-0.5)*3,
        (Math.random()-0.5)*3
      ));
      addLine(p1, p2, 0xff00ff, 0.04);
    }
    for (let t = 0; t < 10; t++) {
      const a = (t / 10) * Math.PI * 2;
      addDot(Math.cos(a)*9, Math.sin(a)*6, 0, 0.3, 0xff00ff, 0.5);
    }
    addDot(Math.cos(10/12*Math.PI*2)*9, Math.sin(10/12*Math.PI*2)*6, 0, 0.3, 0x330000, 0.3);
    addDot(Math.cos(11/12*Math.PI*2)*9, Math.sin(11/12*Math.PI*2)*6, 0, 0.3, 0x330000, 0.3);
  }
}
