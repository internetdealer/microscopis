/**
 * Seeded floating triangles background (Three.js, no React).
 * Matches microscopis triangle-background.tsx behavior with stable layout.
 */
(function () {
  function init() {
  var container = document.getElementById("triangle-bg-container");
  if (!container || typeof THREE === "undefined") {
    if (typeof console !== "undefined" && console.warn) {
      console.warn("triangle-background: missing container or THREE");
    }
    return;
  }

  function mulberry32(seed) {
    return function () {
      var t = (seed += 0x6d2b79f5);
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  var rand = mulberry32(42);

  var width = Math.max(container.clientWidth || 0, window.innerWidth || 1);
  var height = Math.max(container.clientHeight || 0, window.innerHeight || 1);

  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(60, width / height, 0.1, 1000);
  camera.position.set(0, 0, 10);

  var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.setSize(width, height, false);
  renderer.setClearColor(0xffffff, 1);
  var canvas = renderer.domElement;
  canvas.style.display = "block";
  canvas.style.position = "absolute";
  canvas.style.left = "0";
  canvas.style.top = "0";
  canvas.style.width = "100%";
  canvas.style.height = "100%";
  container.appendChild(canvas);

  scene.add(new THREE.AmbientLight(0xffffff, 0.8));
  var d1 = new THREE.DirectionalLight(0xffffff, 0.5);
  d1.position.set(10, 10, 5);
  scene.add(d1);
  var d2 = new THREE.DirectionalLight(0xffffff, 0.3);
  d2.position.set(-10, -10, -5);
  scene.add(d2);

  function createExtrudedTriangleGeometry() {
    var shape = new THREE.Shape();
    shape.moveTo(0, 1);
    shape.lineTo(-0.866, -0.5);
    shape.lineTo(0.866, -0.5);
    shape.lineTo(0, 1);
    return new THREE.ExtrudeGeometry(shape, {
      depth: 0.1,
      bevelEnabled: true,
      bevelThickness: 0.02,
      bevelSize: 0.02,
      bevelSegments: 2,
    });
  }

  var solidGeo = createExtrudedTriangleGeometry();
  /* MeshBasicMaterial: visible without relying on lights / tone mapping */
  var solidMat = new THREE.MeshBasicMaterial({
    color: 0xf0f0f0,
    transparent: true,
    opacity: 0.78,
    side: THREE.DoubleSide,
    depthWrite: true,
  });

  var outlinePoints = [
    new THREE.Vector3(0, 1, 0),
    new THREE.Vector3(-0.866, -0.5, 0),
    new THREE.Vector3(0.866, -0.5, 0),
    new THREE.Vector3(0, 1, 0),
  ];
  var outlineGeo = new THREE.BufferGeometry().setFromPoints(outlinePoints);
  var outlineMat = new THREE.LineBasicMaterial({
    color: 0x000000,
    transparent: true,
    opacity: 0.15,
  });

  var meshes = [];

  function rndRange(a, b) {
    return a + rand() * (b - a);
  }

  for (var i = 0; i < 12; i++) {
    var mesh = new THREE.Mesh(solidGeo, solidMat);
    var px = rndRange(-10, 10);
    var py = rndRange(-6, 6);
    var pz = rndRange(-10, 0);
    mesh.position.set(px, py, pz);
    mesh.rotation.set(
      rndRange(0, Math.PI),
      rndRange(0, Math.PI),
      rndRange(0, Math.PI)
    );
    var sc = 0.3 + rand() * 0.8;
    mesh.scale.setScalar(sc);
    mesh.userData.initialY = py;
    mesh.userData.speed = 0.3 + rand() * 0.5;
    mesh.userData.delay = rand() * 10;
    mesh.userData.rot = [
      mesh.rotation.x,
      mesh.rotation.y,
      mesh.rotation.z,
    ];
    mesh.userData.kind = "solid";
    scene.add(mesh);
    meshes.push(mesh);
  }

  for (var j = 0; j < 20; j++) {
    var line = new THREE.LineSegments(outlineGeo, outlineMat);
    var lx = rndRange(-12.5, 12.5);
    var ly = rndRange(-7.5, 7.5);
    var lz = rndRange(-7, -1);
    line.position.set(lx, ly, lz);
    line.rotation.set(
      rndRange(0, Math.PI),
      rndRange(0, Math.PI),
      rndRange(0, Math.PI)
    );
    var ls = 0.5 + rand() * 1.5;
    line.scale.setScalar(ls);
    line.userData.initialY = ly;
    line.userData.speed = 0.2 + rand() * 0.4;
    line.userData.delay = rand() * 10;
    line.userData.rot = [
      line.rotation.x,
      line.rotation.y,
      line.rotation.z,
    ];
    line.userData.kind = "outline";
    scene.add(line);
    meshes.push(line);
  }

  var clock = new THREE.Clock();

  function animate() {
    requestAnimationFrame(animate);
    var elapsed = clock.getElapsedTime();

    for (var k = 0; k < meshes.length; k++) {
      var obj = meshes[k];
      var t = elapsed + obj.userData.delay;
      var sp = obj.userData.speed;
      var ry = obj.userData.rot[1];
      var ix = obj.userData.initialY;

      if (obj.userData.kind === "solid") {
        obj.rotation.x =
          obj.userData.rot[0] + Math.sin(t * sp * 0.5) * 0.3;
        obj.rotation.y = ry + t * sp * 0.2;
        obj.rotation.z =
          obj.userData.rot[2] + Math.cos(t * sp * 0.3) * 0.2;
        obj.position.y = ix + Math.sin(t * sp * 0.4) * 0.5;
      } else {
        obj.rotation.x =
          obj.userData.rot[0] + Math.sin(t * sp * 0.6) * 0.4;
        obj.rotation.y = ry + t * sp * 0.15;
        obj.rotation.z =
          obj.userData.rot[2] + Math.cos(t * sp * 0.4) * 0.3;
        obj.position.y = ix + Math.sin(t * sp * 0.5) * 0.3;
      }
    }

    renderer.render(scene, camera);
  }

  animate();

  window.addEventListener("resize", function () {
    width = Math.max(container.clientWidth || 0, window.innerWidth || 1);
    height = Math.max(container.clientHeight || 0, window.innerHeight || 1);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
  });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
