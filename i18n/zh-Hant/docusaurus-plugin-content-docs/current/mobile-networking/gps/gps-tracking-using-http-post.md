---
sidebar_key: "mobile-networking/gps/gps-tracking-using-http-post"
sidebar_position: 1
title: "使用 HTTP POST 進行 GPS 跟蹤"
sidebar_label: "使用 HTTP POST 進行 GPS 跟蹤"
description: "本頁說明如何使用 MikroTik RouterOS 的 GPS 功能並透過 HTTP POST 設定車輛跟蹤系統，將座標傳送到 Web 伺服器，再由該伺服器將其儲存到 SQLite3 資料庫中，以便使用 Leaflet.js 進行視覺化。"
tags:
  - 'fetch'
  - 'scripting'
  - 'sqlite3'
source: https://manual.mikrotik.com/docs/mobile-networking/gps/gps-tracking-using-http-post
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本文介紹如何使用 RouterOS 的 GPS 功能和指令碼建立一個簡單的車輛跟蹤系統。

## 方法 {#method}

此方法使用 RouterOS Fetch 工具的 HTTP POST 能力。它允許你直接從 RouterOS 命令列向 Web 伺服器 POST 任意型別的資料。當然，你可以使用指令碼用變數填充 POST 資料。提交的資料將被寫入 SQLITE3 資料庫（如果檔案不存在則會建立），然後從資料庫中讀取並傳入 Leaflet.js 的 Polyline 陣列。這是一個概念驗證示例；沒有身份驗證、安全保護或錯誤處理。

## 要求 {#requirements}

- 你選擇的 Web 伺服器。
- PHP。
- 用於 PHP 的 SQLite3 模組。
- 帶有可用 GPS 模組的 RouterOS 裝置。
- RouterOS。
- 在 RouterOS 中將 GPS 格式設定為 **dd**。

## RouterOS 指令碼 {#routeros-script}

你可以在 Scheduler 工具中以 1s 的間隔執行此指令碼，以便每秒傳送一次座標。

```ros
{
:global lat
:global lon
/system/gps/monitor once do={
:set $lat $("latitude")
:set $lon $("longitude")
}
/tool/fetch mode=http url="http://YOURSERVER.com/index.php" port=80 http-method=post http-data=("{\"lat\":\"" . $lat . "\",\"lon\":\"" . $lon . "\"}") http-header-field="Content-Type: application/json" 
:put ("{\"lat\":\"" . $lat . "\",\"lon\":\"" . $lon . "\"}")
}
```

## index.php 檔案 {#indexphp-file}

在 index.php 檔案旁邊建立一個名為 **sqlite\_db** 的空目錄。確保使用 **chmod -R a+w sqlite\_db/** 使該目錄和檔案可被組寫入。

```ros
<?php
$loc = dirname(__FILE__).'/sqlite_db/coord.db';
$db = new SQLite3($loc,SQLITE3_OPEN_READWRITE | SQLITE3_OPEN_CREATE);
$raw = file_get_contents('php://input');
$raw = preg_replace('/\\x00/','',$raw);
$data = json_decode($raw);

if (!empty($data) && is_object($data) && property_exists($data,'lat') && property_exists($data,'lon')){
    if(file_exists($loc)) echo 'exists!'.chr(0xa);
    $src = 'SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'coordinates\'';
    $res = $db->querySingle($src);
    if ($res === false){
            $db->exec('CREATE TABLE coordinates (latitude TEXT, longitude TEXT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, added TIMESTAMP DEFAULT CURRENT_TIMESTAMP ) ');
    }
    
$regex = '/^(|\-)([0-9]{2,3}\.[0-9]{0,8})$/';

if (preg_match($regex,$data->lat) && preg_match($regex,$data->lon) )
	{
		$lat = $data->lat;
		$lon = $data->lon;
	}
	$ins = 'INSERT INTO coordinates (latitude,longitude) VALUES (\''.SQLite3::escapeString($lat).'\',\''.SQLite3::escapeString($lon).'\')';
	$db->exec($ins);
	die();
}
?>

<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css" integrity="sha512-Rksm5RenBEKSKFjgI3a41vrjkw4EVPlJ3+OiI65vTjIdo9brlAacEuKOiQ5OFh7cOI1bkDwLqdLw3Zg0cRJAAQ==" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js" integrity="sha512-/Nsx9X4HebavoBvEBuyp3I7od5tA0UzAxs+j83KgC8PU0kgB4XiK4Lfe4y4cgBtaRJQEIFCW+oC506aPT2L1zw==" crossorigin=""></script>
</head>
<body>

<script>
var map = L.map('map').setView([0,0], 4);
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {attribution: 'OSM'}).addTo(map);

<?php
    if($result = $db->query('SELECT latitude,longitude FROM coordinates')){
    echo ' var latlngs = [ ';
    while($obj = $result->fetchArray()){
    	if (!is_array($obj) || !isset($obj['latitude']) || !isset($obj['longitude']) || empty($obj['latitude']) || empty($obj['longitude'])) continue;
    	echo '["'. $obj['latitude'].'","'.$obj['longitude'].'"],';
    }
    echo ']; ';
    } else
     echo('//'.$db->lastErrorMsg().chr(0xa));  

?>
var polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);
map.fitBounds(polyline.getBounds());
</script>
</body>
</html>
```

## 結果 {#result}

![](/img/9bd20a259fa32856.webp)
