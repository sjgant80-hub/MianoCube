/**
 * animate.js — Main animation loop.
 *
 * Handles auto-rotation, glow pulsing,
 * and camera zoom per level.
 */

const clock = new THREE.Clock();

function animate() {
  requestAnimationFrame(animate);
  const t = clock.getElapsedTime();

  // Auto-rotate when not dragging
  if (!isDrag) rY += 0.002;

  // Smooth rotation interpolation
  grp.rotation.y += (rY - grp.rotation.y) * 0.04;
  grp.rotation.x += (rX - grp.rotation.x) * 0.04;

  // Pulse glow on mesh nodes
  grp.children.forEach((child, i) => {
    if (child.isMesh && child.material) {
      child.material.opacity = Math.max(
        0.1,
        child.material.opacity + Math.sin(t * 3 + i * 0.2) * 0.02
      );
    }
  });

  // Camera zoom based on current level
  const camZ = cur <= 1 ? 20 : cur <= 4 ? 28 : 35;
  camera.position.z += (camZ - camera.position.z) * 0.02;
  camera.position.y += (6 + cur * 0.5 - camera.position.y) * 0.02;
  camera.lookAt(0, 0, 0);

  renderer.render(scene, camera);
}

animate();
