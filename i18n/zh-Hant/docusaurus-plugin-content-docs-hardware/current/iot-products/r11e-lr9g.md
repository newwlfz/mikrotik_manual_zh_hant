---
title: "R11e-LR9G"
slug: /r11e-lr9g
source: https://manual.mikrotik.com/hardware/r11e-lr9g
captured_at: '2026-11-04T09:59:11+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可下載為 <a href="/assets/files/r11e-lr9g-53967cbc5df54a2266a0515317a062b3.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/271bd67e61e17ec9.jpg)

R11e-LR9G - LR mPCIe 閘道器模組。它可以整合到帶有 mPCIe 插槽的 RouterBOARD 產品中。需要在 RouterOS 中安裝 LR 軟體包才能進行配置。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品不帶外殼，需由經過培訓的合格人員安裝到 MikroTik 主機裝置中。有關安裝說明，請參閱所選 MikroTik 主機產品的快速指南。請勿嘗試拆卸、修理或改裝本裝置。
- 請在開始安裝前仔細閱讀安裝說明。使用錯誤的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用本裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 請讓這張 mini PCIe 卡遠離水、火、潮溼或高溫環境。
- 客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置應與您的身體、職業使用者或公眾保持不少於 20 釐米的距離。

## 規格 {#specifications}

低功耗，採用 mini PCIe 介面，適用於遠距離資料傳輸，發射：

- 介面 – Mini-PCIe；
- 工作溫度 -40 / +70；
- 支援 Class A 和 C；
- 頻率 - 902-928MHz（美國）；
- 射頻輸出功率 - 902-928MHz（美國）最高 27dBm；
- *最大接收靈敏度 - 141 dB @ SF12，取決於所使用的天線；*
- *最大功耗 1.3 W。*
- GPS 接收器 U.FL 插槽（用於連線外部 GPS 天線）。支援 GPS（不支援 GLONASS、BeiDou、Galileo）。

## 將模組安裝到您的裝置中 {#installing-the-module-in-your-device}

R11e-LR9G 供專業使用。每張卡均採用 ESD 防護包裝。處理電氣裝置時，請遵守以下安全預防措施：

-

拆包和處理電氣元件時，請使用腕部接地帶，以避免靜電放電（ESD）損壞；

-

拆包後，請將卡放置在防靜電墊上；

-

安裝時，請確保沒有可能損壞或接觸 PCB 板的物體；

-

可以使用 PCB 板上出廠預留的螺絲孔，將卡安裝到您所需的裝置中；*圖片僅用於示意，裝置配置和 miniPCIe 卡的位置可能有所不同。*

-

在您的裝置上找到 miniPCIe 插槽；

-

擰下兩顆出廠時已安裝的螺絲；

![](/img/201e1c747cc5cacc.webp)

![](/img/fa01a2e5438f417c.webp)

- 您也可以選用導熱墊，將其放置在卡的下方，導熱墊不包含在包裝內；
- 將模組安裝到 miniPCIe 插槽中，並用之前拆下的螺絲固定。擰緊力矩為 0,3 Nm。

![](/img/92b6604db87307db.webp)

## 連線到天線 {#connecting-to-the-antenna}

如果您的裝置沒有內建天線，可以透過新增線纜轉接頭連線到外部天線，產品型號 — [ACSMAUFL](https://mikrotik.com/product/acsmaufl)。請在裝置關閉時連線和斷開天線！

將 LoRa 天線線纜連線到標有 "RFIO" 的聯結器以使用 LoRa，將 GPS 天線線纜連線到標有 "GPS" 的聯結器以使用 GPS：

![](/img/6c286454f503a4a7.webp)

在戶外安裝時，請確保裝置外殼防水且專為戶外使用而設計。本裝置的 IP 防護等級為 IP0。*本裝置的安裝和配置應由合格人員完成。*

## RouterOS 配置 {#configuration-for-routeros}

要為 LR 設定配置，請連線到裝置並使用網頁瀏覽器、WinBox 或移動應用程式登入。按照以下兩個簡單步驟操作：**第一步：**

-

登入後，將預設選中 Quick Set，請切換到螢幕右側的 WebFig。如果透過移動應用程式進行配置，請點選螢幕右側的齒輪圖示以開啟高階選單。

-

在左側選單中找到並選擇 "IoT&gt;Lora" 部分。

-

在 newly 開啟的視窗中選擇 Servers 標籤頁。

-

點選 + 新增新的伺服器配置。

-

將出現一個新視窗，您需要輸入：Name：（伺服器名稱）Address：（伺服器地址）Up port：（用於 LoRa UDP，1700）Down port：（用於 LoRa UDP，1700）

-

點選 OK 儲存。**第二步：**

-

在之前的視窗中選擇 Device 標籤頁。

-

雙擊或點按該行進行配置。

-

在下拉選單中選擇先前輸入的網路。

-

點選 Enable 按鈕以啟用閘道器。

-

點選 OK 儲存。

-

配置完成。

## 規格 {#specifications-1}

該模組可以安裝到 miniPCIe 轉 USB 介面卡上，並用於我們任何帶有 USB 插槽且已安裝 Lora 軟體包的裝置中。

**要在其他裝置中使用該模組，需要 Semtech 的 packet forwarder：** [packet_forwarder](https://github.com/Lora-net/packet_forwarder)

此警告僅適用於已預裝在 MikroTik 閘道器裝置（如 WAP LR9）中的 mPCIe 卡。這裡需要特別注意的是，必須使用 **引腳 39** 和 **引腳 41**。如果您想在其他地方使用該卡，請注意某些 USB 轉 mPCIe 介面卡並未連線上述引腳，缺少這些引腳時 LoRa 卡將無法工作。有關更詳細的 **引腳定義**，請檢視下面的章節。

## 引腳定義 {#pinout}

![](/img/6df4c73924b16c0d.webp)

## 框圖 {#block-diagram}

![](/img/584644264f82120d.webp)

## 作業系統支援 {#operating-system-support}

該模組支援 RouterOS 軟體版本 v7。其他作業系統尚未經過測試。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解您所在地區將裝置妥善運送至指定處置場所的相關程式。
