---
title: "R11e-LR2"
slug: /r11e-lr2
source: https://manual.mikrotik.com/hardware/r11e-lr2
captured_at: '2026-11-04T09:58:51+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可作為 <a href="/assets/files/r11e-lr2-31679419e5e4a56e1f4d2b5566cb004f.pdf" target="_blank" rel="noopener">PDF 檔案</a>下載。

![](/img/f55649d189098c83.jpg)

R11e-LR2 - LR mPCIe 閘道器模組。它可以整合到帶有 mPCIe 插槽的 RouterBOARD 產品中。在 RouterOS 中進行配置需要安裝 LR 軟體包。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應依照所有國家法律法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 30 釐米。

## 規格 {#specifications}

note請注意，並非所有伺服器都支援 2.4 GHz LoRa 通訊。截至目前，2.4 GHz LoRa 由 TTN 和 ChirpStack 伺服器提供支援。

低功耗，採用 mini PCIe 介面，用於遠距離資料傳輸：

- 產品程式碼 R11e-LR2
- LoRa 頻段 2.4 GHz
- Tx 鏈路數量 1
- Rx 鏈路數量 4
- TX/RX 通道 2403 MHz, 2425 MHz, 2450 MHz, 2479 MHz
- RF 輸出功率 10 dBm
- 工作溫度 -40°C 至 +70°C

## 在裝置中安裝模組 {#installing-the-module-in-your-device}

R11e-LR2 供專業使用。每張卡均採用 ESD 防護包裝。處理電氣裝置時，請遵守以下安全注意事項：

-

拆包和處理電氣元件時，請使用腕部接地帶，以避免靜電放電（ESD）損壞；

-

拆包後，請將卡放在防靜電墊上；

-

安裝時，請確保沒有可能損壞或接觸 PCB 板的物體；

-

可使用 PCB 板上出廠提供的螺絲孔將卡安裝到您所需的裝置中；*圖片僅用於說明目的，裝置配置和 miniPCIe 卡的安裝位置可能有所不同。*

-

找到裝置上的 miniPCIe 插槽；

-

擰下兩顆出廠時已安裝的螺絲；

![](/img/201e1c747cc5cacc.webp)

![](/img/fa01a2e5438f417c.webp)

- 將模組安裝到 miniPCIe 插槽中，並用之前拆下的螺絲固定。擰緊力矩為 0,3 Nm。

![](/img/92b6604db87307db.webp)

## 連線到天線 {#connecting-to-the-antenna}

在戶外安裝時，請確保裝置外殼防水且專為戶外使用而設計。本裝置的 IP 防護等級為 IP0。*本裝置的安裝和配置應由合格人員完成。*

您可以使用 UFL 或 MMCX 聯結器。

如果您的裝置沒有內建天線，可以透過新增電纜轉接頭連線到外接天線，產品程式碼 — [ACSMAUFL](https://mikrotik.com/product/acsmaufl)。請在裝置關閉時連線和斷開天線！

我們建議使用 TOF-2400-8V-4 Omni 天線

使用 UFL 聯結器時，請將天線電纜連線到下圖所示的聯結器：

![](/img/a2e4120f6227e87d.webp)

使用 MMCX 聯結器時，請將天線電纜連線到下圖所示的聯結器：

![](/img/6c68e7ab1acb3909.webp)

連線天線後，即可開啟裝置。請確保在軟體設定中模組使用的是正確的聯結器。

為此，請進入裝置的 GUI，在 **LoRa* → *Devices* → 雙擊閘道器 → 在 "**Antenna**" 部分下檢視使用的是哪個聯結器：

![](/img/4f432620cfebced0.webp)

## RouterOS 配置 {#configuration-for-routeros}

要設定 LR 的配置，請連線到裝置並使用網頁瀏覽器、WinBox 或移動應用登入。只需完成兩個簡單步驟：**第一步：**

-

登入後，將預設選中 Quick Set，請切換到螢幕右側的 WebFig。如果透過移動應用進行配置，請點選螢幕右側的齒輪圖示以開啟高階選單。

-

在左側選單中，找到並選擇 "Lora" 部分。

-

在 newly opened 視窗中，選擇 Servers 標籤頁。

-

點選 + 新增新的伺服器配置。

-

將出現一個新視窗，您需要輸入：Name：（伺服器名稱）Address：（伺服器地址）Up port：（通常為 1700）Down port：（通常為 1700）

-

點選 OK 儲存。**第二步：**

-

在上一個視窗中選擇 Device 標籤頁。

-

雙擊或點選該行進行配置。

-

在下拉選單中選擇之前輸入的網路。

-

點選 Enable 按鈕以啟用閘道器。

-

點選 OK 儲存。

-

配置完成。

## 規格 {#specifications-1}

該模組可以安裝在 miniPCIe 轉 USB 介面卡上，並用於我們任何帶有 USB 插槽且已安裝 Lora 軟體包的裝置中。

**要在其他裝置中使用該模組，需要使用 Semtech 的 packet forwarder：** [packet_forwarder](https://github.com/Lora-net/gateway_2g4_hal/tree/master/packet_forwarder)

## 作業系統支援 {#operating-system-support}

該模組支援 RouterOS 軟體版本 v6。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解當地將裝置運送至指定處置場所的正確程式。

## UKCA 標誌 {#ukca-marking}

![](/img/387853c20d5a4c82.gif)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期的資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## Norma Oficial Mexicana {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用本裝置，須按照烏克蘭國家通訊與資訊化監管委員會 2012 年 11 月 1 日第 559 號決議批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記（編號 57/22589）的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 R11e-LR2 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### LR {#lr}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>2403-2479 MHz / 20 dBm</th></tr></thead></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。有關更詳細的資訊，請參閱上文的符合性宣告。
