---
title: "Disc Lite5"
slug: /disc-lite5
source: https://manual.mikrotik.com/hardware/disc-lite5
captured_at: '2026-11-04T09:47:47+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/65562c26cccc0768.webp)

## [DISC Lite5](https://mikrotik.com/product/rbdisc_5nd) (RBDisc-5nD) {#disc-lite5-rbdisc-5nd}

DISC 是一款內建定向天線的室外無線系統。它可以用作 CPE，也可用於點對點鏈路。完整的規格引數和宣傳資料請參閱 [Disc Lite5 產品頁面](https://mikrotik.com/product/rbdisc_5nd)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適合安裝在室外的立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置，或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 只能使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝與執行應使其與您的身體、職業使用者或公眾的距離不小於 45 釐米。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 使用乙太網線將裝置連線到隨附的 PoE 注入器的 data+power 端；
- 將 PoE 注入器的 data 端連線到電腦；
- 將電源介面卡連線到 PoE 注入器；
- 使用網頁瀏覽器透過 **WebFig** 或 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）配置您的裝置。**提供多種配置方式以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 即可訪問 **WebFig**；若使用 **WinBox**，請下載該工具，切換到 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本可確保獲得最佳的效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家，以應用該國家的法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 供電 {#powering}

本裝置僅接受來自 Passive PoE 注入器的 10-30 V 供電（隨附一個電源和一個 PoE 注入器）。

## 啟動過程 {#booting-process}

本裝置被配置為無線用戶端。配置必須透過乙太網埠完成。除本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的所有訪問都會被阻止）。出於恢復目的，可以從網路啟動裝置，請參閱相關章節。

## 組裝與安裝 {#assembly-and-mounting}

本裝置隨附一個金屬安裝環，可用於產品的任一側（有兩個安裝槽）。第三個中央安裝點與 quickMount Pro（不包含）相容。

![](/img/0f4a04fecd600831.webp)

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個 10/100 乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X），因此您可以使用直通線或交叉線連線到其他網路裝置。
- 一個整合無線 5GHz 802.11a/n 或 ac（取決於型號），2x2 MIMO，內建定向天線，最大增益 21 dBi。

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置將開始尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒直到 LED 熄滅，然後鬆開，使 RBDisc-5nD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，如果在裝置通電之前按下該按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復非常有用。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列在 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢棄物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBDisc-5nD</td><td>TV7LHG5NDM</td></tr></tbody></table>

本裝置已經過測試，並確認符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝中的有害干擾提供合理防護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來判斷），建議使用者嘗試透過以下措施之一來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者無權操作本裝置。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，(2) 本裝置必須接受任何接收到的干擾，包括可能導致非預期操作的干擾。本裝置及其天線不得與任何其他天線或發射器處於同一位置，也不得與其共同工作。**重要：射頻輻射暴露。** 天線與職業使用者之間必須保持至少 13 釐米的距離，與公眾之間必須保持至少 28 釐米的距離。在此配置下，即可滿足 FCC 針對人群/非受控環境所規定的輻射暴露限值。**天線安裝。警告：** 安裝者有責任確保在美國（或適用 FCC 規則的地區）使用經授權的天線時，僅使用經過產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，嚴禁使用任何未經產品認證的天線。安裝者應根據國家法規和天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBDisc-5nD</td><td>7442A-LHG5NDM</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 標準。其使用須滿足以下兩個條件：(1) 裝置不得產生干擾，(2) 使用者必須接受裝置所受到的任何無線電干擾，即使該干擾可能影響其正常執行。

在 5150–5250 MHz 頻段內工作的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>5650-5850 MHz</td><td>≤100 mW</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證情況而有所不同。

裝置的製造日期資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），隨後的兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 (Norma Oficial Mexicana) {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5470-5725 MHz（27 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議規定的程式取得使用許可，該決議已於 2013 年 1 月 3 日在烏克蘭司法部登記，編號為 57/22589。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBDisc-5nD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

**頻段使用條款**

<table><thead><tr><th>頻率範圍（適用於相應型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家的法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所設定的最大 WLAN 發射功率限值。更多資訊請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上方的符合性宣告。
