import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/loaders/GLTFLoader.js';

let camera, scene, renderer;
let carModel;
const canvas = document.getElementById('bg-canvas');

// Init
init();
animate();

function init() {
  renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(window.devicePixelRatio);

  scene = new THREE.Scene();

  camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 100);
  camera.position.set(0, 2, 5);
  targetPosition.copy(camera.position);

  const light = new THREE.HemisphereLight(0xffffff, 0x444444, 1.2);
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

// Camera control
const targetPosition = new THREE.Vector3();
const lookAtTarget = new THREE.Vector3(0, 1, 0); // adjust for car center

// Animate
function animate() {
  requestAnimationFrame(animate);
  camera.position.lerp(targetPosition, 0.05);
  camera.lookAt(lookAtTarget);
  renderer.render(scene, camera);
}

// Camera movement
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
      targetPosition.set(0, dist + 1, 0.01);
      break;
    case 'reset':
    default:
      targetPosition.set(0, 2, 5);
      break;
  }
};
