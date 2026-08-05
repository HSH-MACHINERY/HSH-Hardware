<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>遥控割草机 - 三列展示</title>

<style>

body {
  font-family: Arial, sans-serif;
  background: radial-gradient(circle at top, #2b2000 0%, #111 35%, #000 100%);
  margin: 0;
  padding: 20px;
  color: #f5f5f5;
}

.container {
  max-width: 1200px;
  margin: auto;
}

h1 {
  text-align: center;
  color: #ffd700;
  margin-bottom: 30px;
  text-shadow: 0 0 10px rgba(255,215,0,0.45);
}

/* 表格 */
table.info-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  background: linear-gradient(145deg,#1a1a1a,#050505);
  border-radius: 10px;
  border: 1px solid rgba(255,215,0,0.2);
  box-shadow: 0 4px 15px rgba(0,0,0,0.45);
  margin-bottom: 20px;
  overflow: hidden;
}

table.info-table td {
  padding: 15px 10px;
  vertical-align: top;
  color: #f0f0f0;
}

table.info-table tr:nth-child(even) {
  background-color: rgba(255,255,255,0.03);
}

table.info-table td strong {
  color: #ffd700;
}

/* 产品区 */
.product-row {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin: 30px 0;
}

.product {
  flex: 1 1 calc(33.333% - 20px);
  background: linear-gradient(145deg,#1a1a1a,#050505);
  border-radius: 10px;
  padding: 20px;
  text-align: center;
  cursor: pointer;
  border: 1px solid rgba(255,215,0,0.2);
  box-shadow: 0 4px 15px rgba(0,0,0,0.45);
  transition: 0.3s;
}

.product:hover {
  transform: scale(1.03);
  border-color: rgba(255,215,0,0.55);
  box-shadow: 0 0 22px rgba(255,215,0,0.18);
}

.product img {
  width: 100%;
  height: 220px;
  object-fit: contain;
  border-radius: 8px;
  margin-bottom: 10px;
}

.product-info h2 {
  color: #ffd700;
  font-size: 20px;
  margin: 0;
}

/* 按钮 */
.back-button {
  display: block;
  width: fit-content;
  margin: 40px auto 0;
  padding: 12px 24px;
  background: linear-gradient(145deg,#111,#000);
  color: #ffd700;
  border-radius: 8px;
  border: 1px solid #ffd700;
  text-decoration: none;
}

.back-button:hover {
  background: linear-gradient(90deg,#000,#7a5a00,#000);
  color: #fff;
}

/* 手机 */
@media (max-width: 768px) {
  .product {
    flex: 1 1 100%;
  }
}

/* 视频弹窗 */
#videoModal {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.85);
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

#videoModal.active {
  display: flex;
}

#videoModal video {
  max-width: 90%;
  max-height: 80%;
  border-radius: 10px;
  border: 2px solid rgba(255,215,0,0.4);
}

.close-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  font-size: 30px;
  color: #ffd700;
  cursor: pointer;
  width: 45px;
  height: 45px;
  text-align: center;
  line-height: 45px;
  background: rgba(0,0,0,0.6);
  border-radius: 50%;
}

</style>
</head>

<body>

<div class="container">

<h1>ROBOTIC LAWN MOWER</h1>

  <table class="info-table">
    <tr>
      <td><strong>马力 Power / Kuasa</strong></td>
      <td>9.0 HP/12.0 HP</td>
    </tr>
    <tr>
      <td><strong>适合地形 Terrain Sesuai / Suitable Terrain</strong></td>
      <td>
        厚草、斜坡、崎岖地形、工程地<br>
        Rumput tebal, cerun, tanah kasar, projek<br>
        Thick grass, slopes, rugged terrain, project sites
      </td>
    </tr>
    <tr>
      <td><strong>特点 / Ciri / Features</strong></td>
      <td>
        ✅ 底盘结实，极度耐用 /  Rangka kukuh & sangat tahan lasak / Strong chassis, highly durable<br>
        ✅ 专业承包商首选 / Pilihan utama kontraktor profesional / Top choice for contractors<br>
        ✅ 高马力，适合极端环境 /  Kuasa tinggi, sesuai untuk keadaan ekstrem / High power, built for extreme conditions
      </td>
    </tr>
    <!-- 白色表格（参数表） -->
    <table class="info-table">
      <tr><td><strong>型号 / Model</strong></td><td>HSH-S950-P / HSH-S1260-D</td></tr>
      <tr><td><strong>发动机功率 (马力) / Engine Power (HP) / Kuasa Enjin (HP)</strong></td><td>9.0 HP/12.0 HP</td></tr>
      <tr><td><strong>发动机类型 / Engine Type / Jenis Enjin</strong></td><td>LONCIN</td></tr>
      <tr><td><strong>割幅宽度 / Cutting Width / Lebar Potongan</strong></td><td>(P)500 mm / (D)600 mm</td></tr>
      <tr><td><strong>割草高度调节范围 / Cutting Height Adjustment / Pelarasan Tinggi Potongan</strong></td><td>20mm-200mm</td></tr>
      <tr><td><strong>行走方式 / Drive Type / Jenis Gerakan</strong></td><td>Track</td></tr>
      <tr><td><strong>最大爬坡能力 / Max Climbing Ability / Keupayaan Mendaki Maksimum</strong></td><td>40°</td></tr>
      <tr><td><strong>油箱容量 / Fuel Tank Capacity / Kapasiti Tangki Minyak</strong></td><td>(P)4L  /  (D)5.5L</td></tr>
      <tr><td><strong>适用作业面积 / Suitable Working Area  / Kawasan Kerja Sesuai</strong></td><td>(P)1 to 3 acre <br>  (D)1 to 4 acre</td></tr>
      <tr><td><strong>遥控距离 / Remote Control Range / Jarak Kawalan Jauh</strong></td><td>200m</td></tr>
      <tr><td><strong>机器重量 / Machine Weight / Berat Mesin</strong></td><td>(P)180kg  /  (D)280kg</td></tr>
      <tr><td><strong>外形尺寸 (长×宽×高) / Dimensions (L×W×H) / Dimensi (P×L×H)</strong></td><td>(P)1140mm X 970mm X 730mm <br>  (D)1260mm X 1020mm X 700mm  </td></tr>
    </table>

  </table>

<!-- 产品 -->
<div class="product-row">

<div class="product" onclick="openVideo('video1.mp4')">
  <img src="HSH-S950-P (Petrol Version) 9HP.JPG">
  <div class="product-info"><h2>9.0 HP （P）etrol Version</h2></div>
</div>

<div class="product" onclick="openVideo('video2.mp4')">
  <img src="HSH-S1260-D (Diesel Low Spec Version) 12HP.JPG">
  <div class="product-info"><h2>12.0 HP （D）iesel Low Spec Version</h2></div>
</div>



</div>

<a class="back-button" href="index.html">← 返回总览</a>

</div>

<!-- 视频弹窗 -->
<div id="videoModal" onclick="closeVideo(event)">
  <div class="close-btn" onclick="closeVideo(event)">×</div>
  <video id="videoPlayer" controls></video>
</div>

<script>
function openVideo(src){
  const modal = document.getElementById('videoModal');
  const player = document.getElementById('videoPlayer');
  player.src = src;
  modal.classList.add('active');
}

function closeVideo(e){
  if(e.target.id === 'videoModal' || e.target.classList.contains('close-btn')){
    const modal = document.getElementById('videoModal');
    const player = document.getElementById('videoPlayer');
    player.pause();
    player.src = '';
    modal.classList.remove('active');
  }
}
</script>

</body>
</html>