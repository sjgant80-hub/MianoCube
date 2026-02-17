/**
 * scene.js — Three.js scene setup.
 *
 * Creates the renderer, camera, and main group.
 * Handles window resize events.
 */

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  50, innerWidth / innerHeight, 0.1, 500
);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight);
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
document.body.appendChild(renderer.domElement);

const grp = new THREE.Group();
scene.add(grp);

camera.position.set(0, 8, 25);

window.addEventListener('resize', () => {
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});
