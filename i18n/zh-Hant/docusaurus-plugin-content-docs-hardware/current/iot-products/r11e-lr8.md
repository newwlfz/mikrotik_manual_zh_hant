---
title: "R11e-LR8"
slug: /r11e-lr8
source: https://manual.mikrotik.com/hardware/r11e-lr8
captured_at: '2026-11-04T09:58:46+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可以下載為 <a href="/assets/files/r11e-lr8-d0ac4256b0bb1ec57c362648c9c7ec3a.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

R11e-LR8 - LR mPCIe 閘道器模組。它可以整合到帶 mPCIe 插槽的 RouterBOARD 產品中。需要在 RouterOS 中安裝 LR 軟體包才能進行配置。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或一般公眾的距離不得小於 20 釐米。

## 規格 {#specifications}

低功耗，採用 mini PCIe 介面，用於長距離資料傳輸，發射：

- 介面 – Mini-PCIe；
- 工作溫度 -40 / +70；
- 支援 Class A 和 C；
- 頻率 - 863-870MHz (EU)；
- 射頻輸出功率 - 862-870MHz (EU) @ 14dBm；
- *最大接收靈敏度 - 137 dB @ SF12，取決於所使用的天線；*
- *最大功耗 2 W。*

## 將模組安裝到您的裝置中 {#installing-the-module-in-your-device}

R11e-LR8 供專業使用。每張卡都採用 ESD 保護包裝。處理電氣裝置時，請遵守以下安全預防措施：

-

拆包和處理電氣元件時，請使用手腕接地帶，以避免靜電放電（ESD）損壞；

-

拆包後請將卡放在防靜電墊上；

-

安裝時請確保沒有可能損壞或觸碰 PCB 板的物體；

-

可以使用 PCB 板上出廠提供的螺絲孔將卡安裝到您想要的裝置中；*圖片僅用於說明目的，裝置配置和 miniPCIe 卡的位置可能有所不同。*

-

找到裝置上的 miniPCIe 插槽；

-

擰下兩顆出廠時已安裝的螺絲；

![](/img/154687456007685e.webp)

![](/img/fa01a2e5438f417c.webp)

- 可選地，您可以將散熱墊放在卡下方使用，散熱墊不包含在包裝中；
- 將模組安裝到 miniPCIe 插槽，並用之前拆下的螺絲固定。擰緊扭矩為 0,3 Nm。

![](/img/92b6604db87307db.webp)

## 連線到天線 {#connecting-to-the-antenna}

如果您的裝置沒有內建天線，可以透過新增電纜聯結器連線到外部天線，產品程式碼 — [ACSMAUFL](https://mikrotik.com/product/acsmaufl)。請在裝置關閉時連線和斷開天線！

- 將天線電纜連線到模組上的聯結器：

![](/img/32c6221fae70fa2d.webp)

在戶外安裝時，請確保裝置外殼防水且專為戶外使用而設計。本裝置的 IP 等級為 IP0。*本裝置的安裝和配置應由合格人員完成。*

## RouterOS 配置 {#configuration-for-routeros}

要設定 LR 的配置，請連線到裝置並使用網頁瀏覽器、WinBox 或移動應用程式登入。按以下兩個簡單步驟操作：**第一步：**

-

登入後，將選中 Quick Set，請切換到螢幕右側的 WebFig。如果透過移動應用程式進行配置，則點選螢幕右側的齒輪圖示以開啟高階選單。

-

在左側選單中，找到並選擇 "Lora" 部分。

-

在新開啟的視窗中選擇 Servers 標籤頁。

-

點選 + 新增新的伺服器配置。

-

將出現一個新視窗，您需要輸入：名稱：（伺服器名稱）地址：（伺服器地址）上行埠：（通常為 1700）下行埠：（通常為 1700）

-

點選 OK 儲存。**第二步：**

-

在之前的視窗中選擇 Device 標籤頁。

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

該模組可以安裝在 miniPCIe 轉 USB 介面卡上，並可在我們任何帶 USB 插槽且已安裝 Lora 軟體包的裝置中使用。

**要在其他裝置中使用該模組，需要來自 Semtech 的 packet forwarder：** [packet_forwarder](https://github.com/Lora-net/packet_forwarder)

## 引腳定義 {#pinout}

<table><thead><tr><th>引腳編號</th><th>數值</th></tr></thead><tbody><tr><td>2</td><td>3V3</td></tr><tr><td>4</td><td>GND</td></tr><tr><td>9</td><td>GND</td></tr><tr><td>15</td><td>GND</td></tr><tr><td>18</td><td>GND</td></tr><tr><td>21</td><td>GND</td></tr><tr><td>22</td><td>PERST#（RouterOS 中未使用）</td></tr><tr><td>24</td><td>3V3</td></tr><tr><td>26</td><td>GND</td></tr><tr><td>27</td><td>GND</td></tr><tr><td>29</td><td>GND</td></tr><tr><td>34</td><td>GND</td></tr><tr><td>35</td><td>GND</td></tr><tr><td>36</td><td>USB_D-</td></tr><tr><td>37</td><td>GND</td></tr><tr><td>38</td><td>USB_D+</td></tr><tr><td>39</td><td>3V3</td></tr><tr><td>40</td><td>GND</td></tr><tr><td>41</td><td>3V3</td></tr><tr><td>43</td><td>GND</td></tr><tr><td>50</td><td>GND</td></tr><tr><td>51</td><td>保留</td></tr><tr><td>52</td><td>3V3</td></tr></tbody></table>

## 作業系統支援 {#operating-system-support}

該模組支援 RouterOS 軟體版本 v6 和 v7。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置場所進行處置。請了解您所在地區將裝置正確運輸到指定處置場所的程式。

## UKCA 標誌 {#ukca-marking}

![](/img/387853c20d5a4c82.gif)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置製造日期的資訊標註在其標籤上的序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），接下來的兩位數字表示週數。

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

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定（2013 年 1 月 3 日在烏克蘭司法部註冊，編號 57/22589）所規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 R11e-LR8 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### LR {#lr}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>863 - 870 MHz / 14 dBm</th></tr></thead></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。有關更多詳細資訊，請參閱上文的符合性宣告。
