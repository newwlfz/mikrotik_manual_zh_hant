---
title: "GPeRx4"
slug: /gperx4
source: https://manual.mikrotik.com/hardware/gperx4
captured_at: '2026-11-04T09:49:07+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/9723c1c72c350da8.jpg)

使用緊湊耐用的 GPeR14i，輕鬆將單個高功率 PoE 埠拆分為多個標準 PoE 連線。輕鬆擴充套件、延伸併為您的網路供電！

## 安全警告 {#safety-warnings}

在操作任何 MikroTik 裝置之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。僅使用製造商批准且可在本產品原包裝中找到的電源和配件。本裝置應由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責確保裝置安裝符合當地和國家電氣規範。請勿嘗試拆卸、維修或改裝裝置。本產品適用於戶外。開始安裝前，請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的程式，可能會對人員造成危險情況並損壞系統。我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！如果裝置發生故障，請將其斷電。最快的方法是將電源介面卡從電源插座中拔出。

## 連線 {#connecting}

- 同時按下下殼體兩側的按鈕以解鎖外殼，然後取下裝置蓋板；
- 將線纜穿過殼體底部的橡膠密封圈；
- 將帶有供電的所需網線連線到 PoE in 乙太網埠，並透過 PoE out 埠延伸；
- 將線纜連線到下一臺裝置或另一臺 GPER14i 裝置；

## 供電 {#powering}

本裝置提供兩種不同的供電選項：

- 第一個乙太網埠是 PoE-in，支援 802.3bt，並接受 48 至 57V⎓ 範圍內的直流電壓。
- 兩針聯結器相容 24 至 57V⎓ 範圍內的直流電壓。
- 您可以使用兩針聯結器為另一臺 GPER14i 裝置供電。為此，請將本裝置連線到另一臺 GPER14i 裝置的兩針聯結器，並確保 SwOS Lite 系統的 "Power I/O" 選項配置為 "Output"。要啟用此操作，本裝置本身必須透過 PoE-in 供電。輸出功率警告：請確保裝置的功耗不超過供電裝置的輸入功率容量，並考慮其當前負載。

最大功耗：115W。需要注意的是，所有其他埠的功耗限制為 30W

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

-

將裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠。

-

將乙太網線從本地網路（LAN）連線到 PoE 介面卡。

-

將電源線連線到介面卡，然後將電源線插入電源插座。連線兩針聯結器：

-

將正極線連線到 + 插槽。

-

將負極線連線到 - 插槽。

## 接地 {#grounding}

接地線應連線到 RouterBOARD 接地線連線點。然後，該線應連線到安裝位置的基座，確保連線符合接地標準。不包含 M4 接地螺絲。

## 安裝 {#mounting}

本裝置專為戶外使用而設計，其 IP 防護等級為 IP68。可使用裝置安裝支架上提供的螺孔將裝置固定在立柱上。

建議使用 Cat5/6 線纜。*本裝置的安裝和配置應由合格人員完成。*

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 1 個 PoE-in 802.3bt 千兆乙太網埠。
- 3 個 PoE-out 802.3af/at 千兆乙太網埠。
- 1 個兩針聯結器直流電源電壓插槽，範圍為 24 至 57V⎓。

## LED 狀態 {#led-status}

只有在開啟殼體時才能看到裝置的 LED 指示。

- DC-in 狀態 LED。
- DC-out 狀態 LED。
- 乙太網埠活動狀態 LED。
- PoE-out 狀態 LED

## 復位按鈕 {#the-reset-button}

復位按鈕位於面板上，可在開啟殼體的情況下使用。按住此按鈕，直到 DC-in LED 燈開始閃爍，鬆開按鈕即可將配置重設為預設值。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的配件：

- 帶螺絲和膨脹管的安裝支架。

## 規格 {#specifications}

尺寸：高 x 寬 x 深，mm：280 x 75 x 70 mm

![](/img/38e5784c8f7d0478.webp)

![](/img/e45facbeb60bb470.webp)

![](/img/7b92052359fcdf3b.webp)

有關本產品、規格和圖片的更多資訊，請訪問我們的網頁：[https://mikrotik.com/product/gper](https://mikrotik.com/product/gper)

## 配置 {#configuration}

本裝置執行 SwOS Lite 作業系統。

- 將 PC 的 IP 設定為 192.168.88.2/24；
- 將 PC 連線到任意未使用的乙太網埠；
- 開啟 Web 瀏覽器，預設 IP 管理地址為 192.168.88.1，使用者名稱為 **admin**，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 從 [https://mikrotik.com/download](https://mikrotik.com/download) 下載最新版本的 SwitchOS Lite 軟體；
- 在 Web 瀏覽器的 Upgrade 標籤頁中上傳檔案，升級後設備將重啟；
- 設定密碼以保護裝置。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝環境中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，不能保證在特定安裝環境中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一項或多項措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。

注意：本裝置已使用外圍裝置上的遮蔽電纜進行測試。必須將遮蔽電纜與本裝置一起使用以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：(1) 本裝置不得產生干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置內含的免許可證發射器/接收器符合加拿大創新、科學與經濟發展部（ISED）針對免許可證無線電裝置適用的 CNR 標準。允許在以下兩個條件下執行：1）裝置不得產生干擾；2）裝置必須接受任何接收到的無線電干擾，即使該干擾可能導致裝置執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置製造日期資訊以其標籤上序列號末尾的斜槓後數字表示。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡賣家。

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其非預期執行的干擾。製造商：MikroTikls SIA, Unijas iela 2, Riga, LV-1039, 拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
