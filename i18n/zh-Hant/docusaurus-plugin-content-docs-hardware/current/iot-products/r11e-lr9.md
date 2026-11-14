---
title: "R11e-LR9"
slug: /r11e-lr9
source: https://manual.mikrotik.com/hardware/r11e-lr9
captured_at: '2026-11-04T09:59:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可下載為 <a href="/assets/files/r11e-lr9-43501007f1481be9eb0a4d0e5cd6fec0.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/154687456007685e.webp)

R11e-LR9 - LR mPCIe 閘道器模組。它可以整合到帶 mPCIe 插槽的 RouterBOARD 產品中。需要在 RouterOS 中安裝 Lora 軟體包才能進行配置。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 客戶有責任遵守當地國家的法規，包括在法律允許的頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 針對非受控環境規定的射頻輻射暴露限值。本 MikroTik 裝置安裝和操作時，與您的身體、職業使用者或公眾的距離不得小於 29 釐米。

## 規格 {#specifications}

低功耗，採用 mini PCIe 介面，用於長距離資料傳輸，發射：

- 介面 – Mini-PCIe；
- 工作溫度 -40 / +70；
- 支援 Class A 和 C；
- 頻率 - 902-928MHz (US)；
- 射頻輸出功率 - 902-928MHz (US) @ 20dBm；
- *接收最大靈敏度 - 137 dB @ SF12，取決於所使用的天線；*
- *最大功耗 2 W。*

## 在您的裝置中安裝模組 {#installing-the-module-in-your-device}

R11e-LR9 供專業使用。每塊卡都採用 ESD 防護包裝。在處理電氣裝置時，請遵守以下安全注意事項：

-

拆包和處理電氣元件時，請使用腕部接地帶，以避免靜電放電（ESD）損壞；

-

拆包後，請將卡放在防靜電墊上；

-

安裝時，請確保沒有可能損壞或接觸 PCB 板的物體；

-

可使用 PCB 板上出廠提供的螺絲孔將卡安裝到您所需的裝置中；*圖片僅用於示意，裝置配置和 miniPCIe 卡的安裝位置可能有所不同。*

-

在您的裝置上找到 miniPCIe 插槽；

-

擰下兩顆出廠時安裝的螺絲；

![](/img/201e1c747cc5cacc.webp)

![](/img/fa01a2e5438f417c.webp)

- 您也可以選擇在卡下方放置導熱墊，導熱墊不包含在包裝內；
- 將模組安裝到 miniPCIe 插槽中，並用先前拆下的螺絲固定。擰緊扭矩為 0,3 Nm。

![](/img/92b6604db87307db.webp)

## 連線天線 {#connecting-to-the-antenna}

如果您的裝置沒有內建天線，可以透過新增線纜聯結器（產品程式碼 — [ACSMAUFL](https://mikrotik.com/product/acsmaufl)）來連線外接天線。請在裝置關閉時連線和斷開天線！

![](/img/3d8604c8a69b38c9.webp)

- 將天線線纜連線到模組上的聯結器：

在戶外安裝時，請確保裝置外殼防水且專為戶外使用而設計。本裝置的 IP 等級為 IP0。*本裝置的安裝和配置應由合格人員完成。*

## RouterOS 配置 {#configuration-for-routeros}

要為 LR 設定配置，請連線到裝置並使用 Web 瀏覽器、WinBox 或移動應用程式登入。只需兩個簡單步驟：**第一步：**

-

登入後，將預設選中 Quick Set，請切換到螢幕右側的 WebFig。如果是透過移動應用程式進行配置，請點選螢幕右側的齒輪圖示以開啟高階選單。

-

在左側選單中，找到並選擇 "Lora" 選項。

-

在新開啟的視窗中，選擇 ers 標籤頁。

-

點選 + 新增 w 伺服器配置。

-

將出現一個新視窗，您需要輸入：Name：（伺服器名稱）Address：（伺服器地址）Up port：（通常為 1700）Down port：（通常為 1700）

-

點選 OK 儲存。**第二步：**

-

在上一個視窗中選擇 Device 標籤頁。

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

該模組可安裝在 miniPCIe 轉 USB 介面卡上，並在我們任何帶 USB 插槽且已安裝 Lora 軟體包的裝置中使用。

**要在其他裝置中使用它，需要 Semtech 的 packet forwarder：** [packet_forwarder](https://github.com/Lora-net/packet_forwarder)

## 引腳定義 {#pinout}

<table><thead><tr><th>引腳編號</th><th>值</th></tr></thead><tbody><tr><td>2</td><td>3V3</td></tr><tr><td>4</td><td>GND</td></tr><tr><td>9</td><td>GND</td></tr><tr><td>15</td><td>GND</td></tr><tr><td>18</td><td>GND</td></tr><tr><td>21</td><td>GND</td></tr><tr><td>22</td><td>PERST#（在 RouterOS 中未使用）</td></tr><tr><td>24</td><td>3V3</td></tr><tr><td>26</td><td>GND</td></tr><tr><td>27</td><td>GND</td></tr><tr><td>29</td><td>GND</td></tr><tr><td>34</td><td>GND</td></tr><tr><td>35</td><td>GND</td></tr><tr><td>36</td><td>USB_D-</td></tr><tr><td>37</td><td>GND</td></tr><tr><td>38</td><td>USB_D+</td></tr><tr><td>39</td><td>3V3</td></tr><tr><td>40</td><td>GND</td></tr><tr><td>41</td><td>3V3</td></tr><tr><td>43</td><td>GND</td></tr><tr><td>50</td><td>GND</td></tr><tr><td>51</td><td>保留</td></tr><tr><td>52</td><td>3V3</td></tr></tbody></table>

## 作業系統支援 {#operating-system-support}

該模組支援 RouterOS 軟體版本 v6 和 v7。其他作業系統尚未經過測試。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全方式處置，例如送往指定的廢物處理場所。請了解將裝置妥善運送至您所在地區指定處置場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝環境中的有害干擾提供合理防護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝環境中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），建議使用者嘗試透過以下措施之一來消除干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。**FCC 警告：** 未經合規負責方明確批准的任何更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須遵守以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共址或協同執行。

**重要：射頻輻射暴露。**

天線與職業使用者之間必須保持至少 0,29m 的距離，與公眾之間必須保持 0,64m 的距離。在此配置下，可滿足 FCC 針對人群/非受控環境規定的射頻輻射暴露限值。

**天線安裝警告**

安裝人員有責任確保在美國（或適用 FCC 規則的地方）使用授權天線時，僅使用經本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，明確禁止使用任何未經本產品認證的天線。安裝人員應根據國家法規和天線型別配置天線的輸出功率電平。

## OEM 宣告 {#oem-statement}

本模組僅供 OEM 安裝使用。因此，OEM 整合商有責任確保終端使用者未獲得拆卸、安裝或改裝該模組的手冊說明。本模組僅限於在移動或固定應用中安裝。OEM 整合商可使用增益等於或小於本文件列表中所示值的天線（有關此主題的更多資訊，請參閱 47 CFR 第 15.204(c)(4) 段）。MikroTik OEM 射頻模組符合 FCC 規則和法規第 15 部分。受讓人將向主機裝置製造商提供指導，以確保符合第 15 部分 B 子部分的要求。OEM 模組已獲得 FCC 認證，可用於其他產品而無需進一步認證（依據 FCC 第 2.1091 節）。對於其他執行配置，包括涉及 47CFR 第 2.1093 段的行動式配置以及不同的天線配置，需要單獨批准。OEM 必須遵守所有 47CFR 標籤說明以及成品的要求。未經 MikroTik 明確批准的更改或修改可能會使 OEM 失去安裝或操作本裝置的許可權。OEM 必須測試其最終產品，以符合非故意輻射體要求（FCC 第 15.107 和 15.109 節），然後才能宣告其最終產品符合 FCC 規則第 15 部分。**警告：** OEM 必須確保滿足 FCC 標籤要求。這包括在 OEM 外殼外側貼上一個清晰可見的標籤，標明本產品適用的 MikroTik OEM 射頻模組 FCC 識別符號，以及下文列出的任何其他必需的 FCC 宣告。本內含裝置符合 FCC 規則和法規 47CFR 第 15 C 段。操作須遵守以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。標籤和文字資訊應使用足夠大的字號，以便與裝置及標籤的尺寸相稱且易於辨認。**警告：** 本裝置已使用 MMCX 聯結器和下表所列天線進行測試。整合到 OEM 產品中時，這些固定天線需要專業安裝。防止終端使用者將其更換為不合規的天線。在符合認證要求的情況下，可使用與上述型別相同且增益更低的天線。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。操作須遵守以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, mźme si le brouillage est susceptible d'en compromettre le fonctionnement.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## LE-LAN 裝置限制 {#le-lan-device-restriction}

LE-LAN 裝置在 5150-5250 MHz 頻段僅限室內使用。但是，由車輛製造商安裝在車輛中的原始裝置製造商（OEM）裝置是允許的；還應告知使用者，大功率雷達被分配為 5250-5350 MHz 和 5650-5850 MHz 頻段的主要使用者（即優先使用者），這些雷達可能會對 LE-LAN 裝置造成干擾和/或損壞。les dispositifs fonctionnant dans la bande de 5 150 ą 5 250 MHz sont réservés uniquement pour une utilisation ą l'intérieur afin de réduire les risques de brouillage préjudiciable aux systčmes de satellites mobiles utilisant les mźmes canaux Les utilisateurs devraient aussi źtre avisés, d'une part, que les utilisateurs de radars de haute puissance sont désignés utilisateurs principaux (c.-ą-d., qu'ils ont la priorité) des bandes de 5 250 ą 5 350 MHz et de 5 650 ą 5 850 MHz et, d'autre part, que ces radars pourraient causer du brouillage et/ou des dommages aux dispositifs de RL-EL This radio transmitter (identify the device by certification number or model number if Category II) has been approved by Industry Canada to operate with the antenna types listed below with the maximum permissible gain indicated. Antenna types not included in this list, having a gain greater than the maximum gain indicated for that type, are strictly prohibited for use with this device.
