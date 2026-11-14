---
title: "GPERx6"
slug: /gperx6
source: https://manual.mikrotik.com/hardware/gperx6
captured_at: '2026-11-04T09:49:11+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/aee53463176c788e.jpg)

### GPERx6 (CSS606-1G-2Gi-3S+OUT) {#gperx6-css606-1g-2gi-3sout}

用一根混合線纜擺脫雜亂的佈線——在任何地方同時延長供電和光纖。在遠端，GPERx6 將這一切整齊分流：SFP+ 用於進一步的長距離上聯，PoE-out 用於為其他交換器或接入點供電，DC 輸出用於 IoT 裝置或專用裝置。完整規格和宣傳冊請參見 [GPERx6 產品頁面](https://mikrotik.com/product/gperx6)。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 從 [https://mikrotik.com/download](https://mikrotik.com/download) 下載最新版本的 SwOS Lite 軟體；
- 將您的計算機連線到其中一個乙太網埠；
- 將裝置連線到電源；
- 將計算機的 IP 地址設定為 192.168.88.2；
- 開啟您的網頁瀏覽器，預設 IP 管理地址為 192.168.88.1，使用者名稱為 **admin**，無密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 在 Upgrade 標籤頁中透過網頁瀏覽器上傳檔案，升級後設備將重啟；
- 設定您的密碼以保護您的裝置。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<table><thead><tr><th>**引數**</th><th>**值**</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>CSS606‑1G‑2Gi‑3S+OUT</td></tr><tr><td>**交換晶片型號**</td><td>88E6193X</td></tr><tr><td>**作業系統**</td><td>SwOS</td></tr><tr><td>**MTBF**</td><td>25 °C 下約 200,000 小時</td></tr><tr><td>**測試環境溫度**</td><td>‑40 °C 至 +70 °C</td></tr><tr><td>**10/100/1000 乙太網埠**</td><td>3</td></tr><tr><td>**帶 PoE‑IN 的 1G 乙太網**</td><td>一個，Ether1 802.3 bt</td></tr><tr><td>**PoE-In 輸入電壓 42-57 V**</td><td>42-57 V</td></tr><tr><td>**帶 PoE‑OUT 的 1G 乙太網**</td><td>無源 PoE，最高 57V（Ether2- Ether3）</td></tr><tr><td>**10G SFP+ 埠**</td><td>3</td></tr><tr><td>**DC 輸入數量**</td><td>2（2 針螺釘端子，PoE-In）</td></tr><tr><td>**2 針螺釘端子輸入電壓 **</td><td>12-57 V</td></tr><tr><td>**DC 輸出埠數量**</td><td>3，DC1-DC3，最大總輸出 3.6 A</td></tr><tr><td>**最大功耗（不含附件） **</td><td>6 W</td></tr><tr><td>**最大功耗**</td><td>160 W</td></tr><tr><td>**CPU 溫度監控**</td><td>是</td></tr><tr><td>**防護等級**</td><td>IP66</td></tr><tr><td>**尺寸**</td><td>406 × 116 × 76 mm</td></tr></tbody></table>

## 配置 {#configuration}

SwOS 的完整文件請參見：[https://mt.lv/help](https://mt.lv/help)。可以透過 WinBox 工具在 Neighbors 列表中點選來發現該裝置。預設管理地址為 192.168.88.1。請參閱 [CSS610 系列 SwOS 手冊](/docs/bridging-and-switching/swos/css610)，以熟悉其各項功能。出於恢復目的，可以引導裝置進行重新安裝，參見章節 。

## 按鈕和跳線 {#buttons-and-jumpers}

在啟動期間按住 Reset 按鈕，直到 LED 燈開始閃爍。鬆開按鈕即可重設 SwOS 配置，並載入備份軟體以便重新安裝和升級。

## 安裝 {#mounting}

GPERx6 專為戶外使用而設計，可安裝在牆壁或立柱上。請按照**安裝方向標記**（標有“UP”的箭頭）對齊裝置，以確保方向正確。

### 將 GPERx6 安裝到牆壁上： {#to-mount-the-gperx6-on-the-wall}

-

#### 將支架安裝到裝置上 {#attach-brackets-to-the-device}

使用 **K‑93 安裝套件**中的螺釘，將**三個金屬支架**安裝到 GPERx6 的背面。

- 調整支架的位置，使其與裝置的安裝孔對齊。
- 確保**頂部支架**的**較薄部分朝上**，以便正確安裝到牆壁。
-

![](/img/6522977240101f81.webp)

-

#### 將裝置安裝到牆壁上 {#mount-the-device-on-the-wall}

按照**安裝方向標記（“UP”箭頭）**對齊裝置。

- 使用適合您牆壁型別的螺釘或膨脹螺栓將裝置固定到牆上，並讓三個支架都受力以保證穩定。

### 將 GPERx6 安裝到立柱上： {#to-mount-the-gperx6-on-a-pole}

-

#### 將支架安裝到裝置上 {#attach-brackets-to-the-device-1}

使用 **K‑93 安裝套件**中的螺釘，將兩個金屬支架安裝到 GPERx6 的背面。

- 確保支架上的**卡箍孔**朝向裝置**背面**。
-

![](/img/e8454f9f9e377961.webp)

-

#### 安裝到立柱上 {#mounting-on-the-pole}

將**軟管卡箍**穿過支架上的孔。

- 將 GPERx6 放置到立柱周圍，並把卡箍繞到立柱上。
- 擰緊卡箍，將裝置牢固固定。

## 配件 {#accessories}

![](/img/6f79a405ce455e36.webp)

## 作業系統支援 {#operating-system-support}

該裝置支援 SwOS 軟體。其他作業系統尚未經過測試。
