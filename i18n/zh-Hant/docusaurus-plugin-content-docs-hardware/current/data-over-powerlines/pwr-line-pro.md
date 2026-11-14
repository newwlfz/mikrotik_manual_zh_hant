---
title: "PWR-LINE PRO"
slug: /pwr-line-pro
source: https://manual.mikrotik.com/hardware/pwr-line-pro
captured_at: '2026-11-04T06:03:03+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/c6317f884010cbd7.webp" alt="" width={800} height={800} /></p>

PWR-LINE PRO 允許受支援的裝置之間透過普通電力線實現類似乙太網的連線。當插入同一電路時，該裝置將使用 HomePlug AV 2 標準建立乙太網連線。該裝置支援 802.1q。PWR-LINE PRO 不需要任何系統軟體或配置，開箱即用。

## 連線 {#connecting}

- 將一個 PWR-LINE PRO 裝置插入電源插座。
- 將 MikroTik 路由器的某個 LAN 埠連線到 PWR-LINE PRO 的乙太網埠。
- 將另一個 PWR-LINE PRO 單元（或任何其他相容裝置）插入同一電路中的某個位置。
- 使用 sync 按鈕連線裝置，本地網路將自動擴充套件。請參閱有關如何配對額外 PWR-LINE PRO 裝置的章節。
- PWR-LINE PRO 支援從乙太網埠輸出 PoE，用於為另一臺 MikroTik 裝置供電，可透過開關啟用，請參閱相關章節。

## 安裝 {#mounting}

PWR-LINE PRO 可以使用隨附的四顆螺釘安裝在牆上：

- 要接觸到安裝點，請使用 PH2 螺絲刀拆下固定頂蓋的中心螺釘。

<p><Img src="/img/6b90a23121ae4347.webp" alt="" width={379} height={301} /></p>

- 在牆上所需位置為 PWR-LINE PRO 標記四個螺釘孔位。
- 使用 5 mm 鑽頭鑽出膨脹螺栓孔，如有必要，輕輕敲入膨脹螺栓。
- 安裝 PWR-LINE PRO 併合上頂蓋，中心螺釘擰緊力矩為 0.5 – 0.7 Nm，將隨附的 3M 貼紙貼到中心螺釘的蓋子上。

## 供電 {#powering}

該裝置從所插入的牆壁插座取電。100-240 V AC ⏦，~50/60 Hz。最大負載下的功耗可達 5 W。啟用 PoE-Out 時的最大功耗為 14 W。

*為達到 600 Mbps 的速度，您的電源插座需要接地。* *要與另一臺 PWR-LINE 裝置連線，兩者必須位於同一電相位上。*

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個千兆乙太網埠，支援 24 V PoE 輸出，預設設定下為關閉狀態。

## 按鈕和跳線 {#buttons-and-jumpers}

### PWR 連線按鈕（sync） {#pwr-connection-button-sync}

<p><Img src="/img/894ee9f81b48c6fb.webp" alt="" width={719} height={205} /></p>

- 按住 0.5 – 3 秒。裝置將在 120 秒內嘗試與另一臺 PWR-LINE PRO 裝置通訊。琥珀色 LED 閃爍表示裝置處於搜尋模式。您必須在另一臺 PWR 裝置上執行相同操作，這樣它們才能同步。再次按下按鈕可取消搜尋。
- 按住 5 – 8 秒。將生成新的安全金鑰。這是將 PWR-LINE PRO 裝置從現有 PWR 網路中移除所必需的。
- 按住 10 – 15 秒。重設所有與 PWR 相關的設定。
- 如果配對裝置時遇到問題，請按住 SYNC 按鈕 5 - 8 秒以生成新的網路金鑰，然後再次按住 SYNC 按鈕 0.5 – 3 秒，重新嘗試將其配對到 PWR-LINE PRO 網路中。

## LED 指示燈與 PoE 開關 {#led-lights-and-poe-switch}

<p><Img src="/img/87211f2b58117550.webp" alt="" width={720} height={237} /></p>

- 藍色 LED 表示裝置已通電。
- 琥珀色 LED 表示裝置已配對，琥珀色閃爍表示裝置處於搜尋模式。可透過 sync 按鈕啟用。請參閱相關章節。
- 綠色 LED 表示乙太網埠已連線。
- 紅色 LED 表示 PoE 已啟用。
- PoE 開關預設位置為 OFF。可使用標準圓珠筆來切換位置。紅燈表示 PoE 已啟用。

## 配件 {#accessories}

包裝內含以下隨裝置提供的附件：

- K-62 緊固套件。
- EU/US 電源線，D03+QT1 H03VV-F 0x0.75 mm2，30 cm RoHS，白色。

## 規格 {#specifications}

如需瞭解有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/pl7510gi](https://mikrotik.com/product/pl7510gi)

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的規定。操作須滿足以下兩個條件：(1) 本裝置不得產生有害干擾，並且 (2) 本裝置必須接受所收到的任何干擾，包括可能導致意外操作的干擾。注意：本單元已使用外圍裝置上的遮蔽電纜進行測試。必須在本單元上使用遮蔽電纜以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部的免許可證 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得產生干擾，並且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。本裝置符合加拿大工業部適用於免許可證無線電裝置的相關 CNR 規定。操作須滿足以下兩個條件：(1) 裝置不得產生干擾，並且 (2) 使用者必須接受裝置所受到的任何無線電干擾，即使該干擾可能影響其正常執行。

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置生產日期的資訊標註在其標籤上序列號的末尾，用斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後面兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
