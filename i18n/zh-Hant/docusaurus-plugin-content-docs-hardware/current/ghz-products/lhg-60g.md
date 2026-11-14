---
title: "LHG 60G"
slug: /lhg-60g
source: https://manual.mikrotik.com/hardware/lhg-60g
captured_at: '2026-11-04T09:54:12+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可以下載為 <a href="/assets/files/lhg-60g-d834c6f77e358b33f6d3fd47663765b4.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/bec66097fc732862.jpg)

## [LHG 60G](https://mikrotik.com/product/lhg_60g) (RBLHGG-60ad) {#lhg-60g-rblhgg-60ad}

LHG 60G 裝置工作在 60 GHz 無線頻段，這些裝置的工作溫度範圍為 -40°C 至 +70°C。每臺裝置具有一個千兆乙太網埠，可透過 PoE 供電。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律法規。
- 在任意牆面上安裝接入點的所有安裝方法均須獲得當地主管部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於戶外安裝在立柱上。開始安裝前，請仔細閱讀安裝說明。未使用正確的硬體和配置，或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因裝置使用不當而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座上拔下。
- 客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線裝置必須由專業人員進行安裝。
- 這是 A 類裝置。在居住環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

## 快速開始 {#quickstart}

- 組裝裝置。有關安裝說明，請參閱 [LHG 60G 產品頁面](https://mikrotik.com/product/lhg_60g)；裝置包含一個接地連線（標記為 ⏚），應將其連線到裝置使用所在塔架或建築的接地裝置。這可大幅降低靜電放電和雷擊損壞的風險。包裝內含接地聯結器。

警告！本裝置的安裝和操作應確保裝置與人體之間保持至少 95 cm 的距離。在居住環境中操作本裝置可能造成無線電干擾。本裝置的 IP 防護等級為 IP54。*本裝置的安裝和配置應由合格人員完成。*

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個乙太網埠，支援自動交叉/直通線纜校正 (Auto MDI/X)，因此您可以使用直通線或交叉線連線到其他網路裝置。
- WiGig, 802.11ad.

## 供電 {#powering}

裝置可透過乙太網埠供電。乙太網埠接受 12-57 V DC 的 PoE 輸入（無源和 802.3af/at）。包裝盒內包含電源介面卡和無源 PoE 注入器。使用 PoE 注入器時，請務必使用 "Power + Data" 聯結器連線裝置，使用 "Data" 聯結器連線您的 PC、路由器或交換器。**連線到 POE 介面卡：**

- 將來自裝置的乙太網電纜連線到 POE 介面卡的 POE+DATA 埠。
- 將來自本地網路 (LAN) 的乙太網電纜連線到 POE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。最大功耗 5 W。

## 配置 {#configuration}

我們建議點選 "Check for updates" 按鈕，並將您的 RouterOS 軟體更新到最新版本，以確保最佳的效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法透過 IP 連線，可以使用 WinBox 工具 ([https://mt.lv/winbox](https://mt.lv/winbox)) 從 LAN 側連線到裝置的 MAC 地址。請熟悉 [W60G 介面](/docs/wireless/w60g) 的附加資訊。出於恢復目的，可以引導裝置進行重新安裝，請參閱 章節 。

## 按鈕和跳線 {#buttons-and-jumpers}

routerBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，以將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，以清除所有配置並恢復預設值。
- 當 LED 熄滅後（約 20 秒）鬆開按鈕，使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。無論使用上述哪種選項，如果在裝置接通電源之前按下按鈕，系統將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## LED 狀態 {#led-status}

裝置包含使用 LED 的精確對準引導。如果從天線後方朝鏈路另一端看去，燈光會用箭頭指示轉動天線的方向。當對準 LED 熄滅，僅保留 "link established" LED 時，表示對準完成。各 LED 燈為：

![](/img/81b844d3fdf5b5cd.webp)

- 向上傾斜。
- 向下傾斜。
- 向右旋轉。
- 向左旋轉。
- 鏈路建立時 LED 亮起。
- 乙太網連線時 LED 亮起。
- 使用者可配置 LED。
- 電源狀態開啟。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的附件：

- K-LHG 螺絲套裝/緊固套裝。
- 千兆 POE 注入器。
- LHG-5G-390 mm 天線盤（網孔尺寸 0.5 t x1.0 wx1.4 mm ）。
- 歐盟/美國開關電源 24 V ⎓，0.38 A，9 W，Level VI，線纜：1.5 m。
- 軟管卡箍 SUS304（十字型；夾緊直徑範圍 35-70 mm）。
- BRAC1_ LHG 安裝元件。
- DynaDish U 型螺栓 M8（A2 不鏽鋼）。
- QuickMount AIM。

## 規格 {#specifications}

有關 LHG 產品、規格和圖片的更多資訊，請訪問我們的網頁：[https://mikrotik.com/product/lhg_60g](https://mikrotik.com/product/lhg_60g)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列在 /system resource 中。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用在現場配置您的路由器，或為您的 MikroTik 家庭接入點應用最基本的初始設定。掃描二維條碼並選擇您首選的作業系統。

![](/img/9bcba09a7b6a0d53.webp)

![](/img/8d294e5cd375c591.webp)

本裝置符合 ETSI 法規規定的最大發射功率限制。歐盟的頻率和最大發射功率如下：57-66GHz：34.92 dBm。60 GHz 頻段的工作模式：58.32 GHz、60.48 GHz、62.64 GHz。本裝置已獲認證可用於點對多點應用的戶外使用。在以下國家，本裝置不能用於固定點對點應用：

![](/img/01438e2d9209ce7d.webp)

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCCID</th></tr></thead><tbody><tr><td>RBLHGG-60ad</td><td>TV7LHGG60AD</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝環境提供合理的有害干擾保護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在居住區域操作本裝置很可能造成有害干擾，此時使用者需要自行承擔費用來糾正干擾。

![](/img/ce6fc3eb10b9a1e6.webp)

**FCC 警告：** 任何未經負責合規的一方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共址或聯合執行。

**重要：射頻輻射暴露。** 天線與職業使用者/公眾之間必須保持至少 95 cm 的距離。在此配置下，可滿足 FCC 針對一般人群/非受控環境規定的輻射暴露限值。

**天線安裝。警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用經本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，明確禁止使用任何未經本產品認證的天線。安裝人員應根據國家法規和天線型別配置天線的輸出功率水平。帶聯結器的裝置需要專業安裝，以確保符合健康與安全要求。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBLHGG-60ad</td><td>7442A-LHGG60AD</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，並且 (2) 本裝置必須接受任何干擾，包括可能導致裝置執行不正常的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

本裝置不得在飛機上操作，ISED RSS-210 附錄 J.1 所列條件除外。Cet appareil ne doit pas être utilisé sur un avion, sauf dans les conditions énumérées ISED RSS-210 Annex J.1.

**重要說明：IC 輻射暴露宣告：** 本裝置符合 IC RSS-102 針對非受控環境規定的輻射暴露限值。本裝置的安裝和操作應確保輻射體與人體之間保持至少 95 cm 的距離。Cet équipement est conforme aux limites d'exposition aux rayonnements IC établies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé avec un minimum de 95 cm de distance entre la source de rayonnement et votre corps.

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期資訊標註在其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用本裝置，須按照烏克蘭國家通訊與資訊化監管委員會 2012 年 11 月 1 日第 559 號決定（2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBLHGG-60ad 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WiGig {#wigig}

<table><thead><tr><th>工作通道 / 最大輸出功率 Betriebskanäle / maximale Ausgangsleistung Canaux opérationnels / puissance de sortie maximale Canali operativi / massima potenza di uscita Canales operacionales / potencia de salida máxima Операционные каналы / максимальная выходная мощность</th><th>58.32 GHz / &lt;40 dBm</th></tr></thead><tbody><tr><td>60.48 GHz / &lt;40 dBm</td><td></td></tr><tr><td>62.64 GHz / &lt;40 dBm</td><td></td></tr></tbody></table>
