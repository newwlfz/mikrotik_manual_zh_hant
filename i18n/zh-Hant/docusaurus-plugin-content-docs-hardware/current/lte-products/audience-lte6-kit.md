---
title: "Audience LTE6 套件"
slug: /audience-lte6-kit
source: https://manual.mikrotik.com/hardware/audience-lte6-kit
captured_at: '2026-11-04T09:43:11+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/3a70e73b88a06312.webp)

## [Audience LTE6 kit](https://mikrotik.com/product/audience_lte6_kit)（RBD25GR-5HPacQD2HPnD&R11e-LTE6） {#audience-lte6-kit-rbd25gr-5hpacqd2hpndr11e-lte6}

Audience LTE6 kit 是一款內建 LTE 調變解調器的家庭接入點。你可以透過向網路中新增更多 Audience 裝置來擴充套件無線覆蓋範圍——這些裝置會組成一個使用相同 SSID 的單一網路，因此你的裝置可以在其覆蓋範圍內自由漫遊。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家和地區的法律與法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置預期安裝在機架中。開始安裝之前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能導致對人員造成危險的情況並損壞系統。
- 本產品預期在室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。
- 這是 A 類裝置。在居住環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的射頻輻射暴露限值。本 MikroTik 裝置安裝和執行時，應與你的身體、職業使用者或普通公眾保持不小於 20 釐米的距離。

## 連線 {#connecting}

- 插入 Micro SIM 卡，參見（SIM 卡槽使用）。
- 將隨附的電源介面卡插入以啟動裝置（見 ""）。
- 裝置將啟動，前面板 LED 指示燈將常亮藍色，無線網路將可供連線。
- 在你的 PC、手機或其他裝置上開啟網路連線，搜尋 MikroTik 無線網路並連線到它。
- 連線到無線網路後，在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始配置，由於預設沒有密碼，你將自動登入（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）。手機請使用該應用程式（見 ""）。
- 選擇 "Check for updates" 按鈕並將你的 RouterOS 軟體更新到最新版本，需要有效的 SIM 卡。
- 選擇 WebFig 標籤頁，在左側選單中選擇 CAPsMAN。
- 選擇 Security Cfg。
- 選擇新增新的：選擇 Authentication Type：WPA PSK、WPA2 PSK；Encryption：aes ccm；Passphrase：strongwirelesspassword；

![](/img/447b6a0d58621531.webp)

- 選擇 OK。
- 選擇 Configurations 標籤頁。
- 選擇一個介面示例：cfg-2ghz。
- 找到 Security 並選擇之前建立的配置檔案：security1。
- 找到 Country 並設定你所在的國家。
- 選擇 OK。
- 對 cfg-5ghz-ac 介面執行相同的操作。
- 在左側選單中選擇 System&gt;Password。
- 為裝置輸入密碼並選擇 Change。要向網路中新增另一臺 Audience 裝置（見 ""）。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇你偏好的作業系統。
- 安裝並開啟應用程式。
- 預設情況下，IP 地址和使用者名稱將已預先填寫。
- 選擇 Connect 以透過無線網路與你的裝置建立連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導你完成所有基本配置設定。
- 還提供了高階選單，可完整配置所有必要的設定。

## 供電 {#powering}

裝置可透過電源插孔或乙太網埠供電：

-

所提供的直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 12-57 V DC ⎓。

-

乙太網 1 埠接受 Passive PoE 24-57 V DC ⎓。最大負載下的功耗可達 30 W。**連線到 POE 介面卡。** 包裝中不包含 POE 介面卡，如果你考慮使用它，請按以下步驟操作：

-

將乙太網線從 Audience 連線到 POE 介面卡的 POE 埠。

-

將乙太網線從你的 LAN 連線到 POE 介面卡的 LAN 埠，注意資料與電源流向的箭頭。

-

將電源線連線到介面卡，然後將電源線插入電源插座。

## 安裝 {#mounting}

本裝置設計用於室內，可放置在平整表面上，所有需要的線纜都連線到裝置的背面。IPX 防護等級為 IPX0。Audience 裝置應使用 Cat6 遮蔽電纜。*警告！本裝置安裝和執行時，裝置與你的身體之間應保持至少 50 釐米的距離。本裝置在居住環境中執行可能造成無線電干擾。*

## 配置 {#configuration}

登入後，你應在 QuickSet 選單中選擇 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳的效能和穩定性。對於無線型號，請確保已選擇裝置將要使用的國家，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問都被阻止）。出於恢復目的，可以啟動裝置以進行重新安裝，參見章節 。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 兩個千兆乙太網埠。
- 整合無線 2.4 GHz 802.11b/g/n，天線增益 3.5 dBi。
- 整合無線 5.0 GHz 802.11a/n/ac，天線增益 4.5 dBi。5180 – 5320 MHz。
- 整合無線 5.0 GHz 802.11a/n/ac，天線增益 4.5 dBi。5500 – 5825 MHz。
- Audience LTE6 kit - MiniPCIe 插槽，出廠預裝 R11e-LTE6 卡和 SIM 卡槽。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕的功能如下所述：

- 在接通電源之前按住此按鈕，通電三秒後鬆開，以載入備份 boot loader。如果裝置因 RouterBOOT 升級失敗而無法執行，這可能是有必要的。在使用備份 loader 啟動裝置後，你可以設定 RouterOS 在 RouterBOARD 設定中強制使用備份 loader，或者有機會從 fwf 檔案重新安裝失敗的 RouterBOOT（共 3 秒）。
- 如果你繼續按住此按鈕 2 秒直到綠色 LED 燈開始閃爍，鬆開按鈕即可將 RouterOS 配置重設為預設值（共 5 秒）。
- 要將此裝置連線到由 CAPsMAN 管理的無線網路，請繼續按住按鈕 5 秒，LED 變為常亮綠色，此時鬆開即可開啟 CAPs 模式（共 10 秒）。
- 或者繼續按住按鈕 5 秒直到綠色 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器。你也可以一直按住按鈕，直到裝置出現在 Windows 上的 Netinstall 程式中（共 15 秒）。無論使用上述哪種方式，如果在裝置通電之前按鈕已被按下，系統將載入備份 RouterBOOT loader。這對 RouterBOOT 偵錯和恢復很有用。

### WPS 同步按鈕 {#wps-sync-button}

使用 WPS 同步按鈕，透過向網路中新增多臺 Audience 裝置來擴充套件你的無線中繼網路覆蓋範圍。

- 在選定的 Audience AP 上，按一次 "WPS-Sync" 按鈕，即可開啟 WPS 模式兩分鐘，使其等待 Audience 中繼裝置。狀態 LED 將閃爍綠色。
- Audience 中繼裝置需要在按住 "WPS-Sync" 按鈕的情況下啟動，以便裝置根據 "WPS-Sync" 模式自行配置並連線到 Audience AP。當狀態 LED 閃爍琥珀色時，鬆開 "WPS-Sync" 按鈕。
- 如果 Audience 中繼裝置無法連線到 Audience AP，則可以透過 RouterOS 重試連線，或按下 "WPS-Sync" 按鈕並在 5 秒後鬆開，裝置將開啟 "WPS-Sync" 模式兩分鐘並搜尋 Audience AP。狀態 LED 將閃爍琥珀色。
- 要向網路中新增第三臺 Audience 中繼裝置，請在你的網路中第二臺 Audience 上按下 "WPS-Sync" 按鈕，然後在按住 "WPS-Sync" 按鈕的情況下啟動第三臺裝置。根據需要新增更多裝置，重複此操作。

## 前面板狀態 LED 行為 {#front-status-led-behavior}

- 常亮藍色 – 裝置已通電。
- 閃爍綠色 – 裝置處於 Access Point 模式，正在等待另一臺 Audience 裝置連線。
- 閃爍琥珀色（紅色 + 綠色）– 裝置正在搜尋並嘗試連線到另一臺 Audience 裝置。
- 常亮綠色 – 裝置已在 Audience 網路中建立連線。
- 閃爍紅色 – 裝置正在執行用於動態頻率選擇（DFS）的雷達檢測。

## SIM 卡槽使用 {#sim-slot-usage}

SIM 卡槽設計用於 Micro SIM 卡。

- Nano SIM 卡厚度不同，不建議配合轉接卡使用。

![](/img/a0db691ac4861274.webp)

## 配件 {#accessories}

![](/img/39548a32b05e93fa.webp)

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/audience_lte6_kit](https://mikrotik.com/product/audience_lte6_kit)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未經過測試。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置的工作範圍與上述規定不同，則需要將由製造商/供應商提供的定製韌體版本應用於終端使用者裝置，並同時防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料手冊均可在製造商官方網站上獲取。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，發射功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，發射功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，發射功率限制為 20dBm（EIRP）。

請確保裝置具有鎖包（來自制造商的韌體版本），該韌體需要應用於終端使用者裝置，以防止終端使用者重新配置。產品將標註國家程式碼 "-EG"。本裝置需要升級到最新版本以確保符合當地主管部門的法規！終端使用者有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全方式處置，例如送往指定的廢物處置場所。請了解你所在地區將裝置妥善運送到指定處置場所的相關流程。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th><th>包含 FCC ID</th></tr></thead><tbody><tr><td>RBD25GR-5HPacQD2HPnD-US&R11e-LTE6</td><td>TV7D25-5HPQ2HP</td><td>TV7R11ELTE6</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為居住環境中的安裝提供合理的有害干擾防護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。然而，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉再開啟裝置來確定），則鼓勵使用者嘗試透過以下一項或多項措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。FCC 注意：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的授權。

本裝置符合 FCC 規則第 15 部分。其執行受以下兩個條件約束：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受收到的任何干擾，包括可能導致意外執行的干擾。

注：本裝置已使用遮蔽電纜與外圍裝置一起進行測試。為確保合規，必須使用遮蔽電纜與裝置配合。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th><th>包含 IC</th></tr></thead><tbody><tr><td>RBD25GR-5HPacQD2HPnD-US&R11e-LTE6</td><td>7442A-D255HPQ2HP</td><td>7442A-R11ELTE6</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 標準的免許可發射器/接收器。其執行受以下兩個條件約束：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。

本裝置內含的免許可證發射器/接收器符合加拿大創新、科學與經濟發展部（ISED）針對免許可證無線電裝置適用的 CNR 標準。允許在以下兩個條件下執行：1）裝置不得產生干擾；2）裝置必須接受任何接收到的無線電干擾，即使該干擾可能導致裝置執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

工作在 5150–5250 MHz 頻段的裝置僅限室內使用，以減少對同頻道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射機功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證而異。

關於裝置製造日期的資訊，標註在其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 МГц (20 дБм)、5150-5250 МГц (23 дБм)、5250-5350 МГц (20 дБм)、5470-5725 МГц (27 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 NCCIR 2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）所批准的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBD25GR-5HPacQD2HPnD&R11e-LTE6 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/product/audience_lte6_kit](https://mikrotik.com/product/audience_lte6_kit)

### WLAN / WCDMA / LTE / 5G {#wlan--wcdma--lte--5g}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>WLAN</th><th>2400-2483.5 MHz / 20 dBm</th></tr></thead><tbody><tr><td>5150-5250 MHz / 23 dBm</td><td></td><td></td></tr><tr><td>5250-5350 MHz / 20 dBm</td><td></td><td></td></tr><tr><td>5470-5725 MHz / 27 dBm</td><td></td><td></td></tr><tr><td>E-GSM-900</td><td>900 MHz / 33 dBm</td><td></td></tr><tr><td>DCS-1800</td><td>1800 MHz 30 dBm</td><td></td></tr><tr><td>WCDMA Band I</td><td>1922.4 MHz / 24 dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>882.4 MHz / 24 dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1</td><td>2100 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8</td><td>900 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dBm ± 2.7 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 規定對 WLAN 和 LTE 最大發射功率的限值。更多詳細資訊請參見上文的符合性宣告。

![](/img/0561b3ba8c95a35c.webp)

在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限於室內使用。
