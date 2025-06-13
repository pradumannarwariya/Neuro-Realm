import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/loaders/GLTFLoader.js';

let camera, scene, renderer;
let carModel;
let targetPosition = new THREE.Vector3();
let lookAtTarget = new THREE.Vector3(0, 0, 0); // Default look-at point

init();
animate();

function init() {
  const canvas = document.getElementById('bg-canvas');
  renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(window.devicePixelRatio);

  scene = new THREE.Scene();

  camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 100);
  camera.position.set(0, 2, 5);
  targetPosition.copy(camera.position); // Start position

  const light = new THREE.HemisphereLight(0xffffff, 0x444444);
  scene.add(light);

  const loader = new GLTFLoader();
  loader.load('car.glb', (gltf) => {
    carModel = gltf.scene;
    carModel.scale.set(1, 1, 1);
    scene.add(carModel);
  });

  window.addEventListener('resize', onWindowResize);
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
  requestAnimationFrame(animate);

  // Smooth camera movement
  camera.position.lerp(targetPosition, 0.05);
  camera.lookAt(lookAtTarget);

  renderer.render(scene, camera);
}

// Move camera to predefined views
window.moveCamera = function(view) {
  const dist = 5;
  switch(view) {
    case 'front':
      targetPosition.set(0, 2, dist);
      break;
    case 'back':
      targetPosition.set(0, 2, -dist);
      break;
    case 'left':
      targetPosition.set(-dist, 2, 0);
      break;
    case 'right':
      targetPosition.set(dist, 2, 0);
      break;
    case 'top':
      targetPosition.set(0, dist + 1, 0.01); // 0.01 to avoid lookAt jump
      break;
    case 'reset':
    default:
      targetPosition.set(0, 2, 5);
      break;
  }
};
