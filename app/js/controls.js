/**
 * controls.js — Mouse drag rotation.
 *
 * Click and drag to rotate the cube group.
 * Rotation is smoothly interpolated in the animation loop.
 */

let rY = 0.3, rX = 0.3;
let isDrag = false, px = 0, py = 0;

renderer.domElement.addEventListener('mousedown', e => {
  isDrag = true;
  px = e.clientX;
  py = e.clientY;
});

document.addEventListener('mouseup', () => {
  isDrag = false;
});

document.addEventListener('mousemove', e => {
  if (!isDrag) return;
  rY += (e.clientX - px) * 0.004;
  rX += (e.clientY - py) * 0.004;
  rX = Math.max(-1, Math.min(1.5, rX));
  px = e.clientX;
  py = e.clientY;
});
