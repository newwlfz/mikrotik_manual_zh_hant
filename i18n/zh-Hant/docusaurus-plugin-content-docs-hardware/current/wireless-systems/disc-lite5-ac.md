---
title: "Disc Lite5 ac"
slug: /disc-lite5-ac
source: https://manual.mikrotik.com/hardware/disc-lite5-ac
captured_at: '2026-11-04T09:47:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/f42faeb29b5f71d4.webp)

## [DISC Lite5 ac](https://mikrotik.com/product/disc_lite5_ac) (RBDiscG-5acD) {#disc-lite5-ac-rbdiscg-5acd}

DISC 是一款內建定向天線的室外無線系統。它可用作 CPE，也可用於點對點鏈路。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於安裝在室外的立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會給人員帶來危險並損壞系統。
- 請僅使用製造商認可的電源和附件，這些電源和附件可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請先閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻段內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 本裝置為 A 類裝置。在住宅環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 以及歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 使用乙太網線將裝置連線到隨附 PoE 供電器的 data+power 端；
- 將 PoE 供電器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 供電器；
- 透過 **WebFig** 或 **WinBox** 工具使用網頁瀏覽器配置您的裝置，地址為 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 可訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為 "**admin**"，無密碼（某些型號的使用者名稱和無線密碼請檢視標籤貼紙）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。

## 供電 {#powering}

本裝置僅接受來自無源 PoE 供電器的 10-30 V 電源（隨附一個電源和一個 PoE 供電器）。

## 啟動過程 {#booting-process}

本裝置配置為無線用戶端。配置必須透過乙太網埠完成。除本文件所述內容外，RouterOS 還包含許多配置選項。建議從這裡開始瞭解各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的所有訪問均被阻止）。出於恢復目的，可以從網路啟動裝置，請參閱相關章節。

## 組裝與安裝 {#assembly-and-mounting}

本裝置隨附一個金屬安裝環，可安裝在產品的任一側（有兩個安裝槽位）。第三個中央安裝點與 quickMount Pro 相容（不含在內）。

![](/img/0f4a04fecd600831.webp)

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個 10/100 乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通線或交叉線連線到其他網路裝置。
- 一個整合 5GHz 802.11a/n 或 ac 無線（取決於型號），2x2 MIMO，內建定向天線，最大增益 21 dBi。

## 復位按鈕 {#reset-button}

復位按鈕具有三種功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置將開始尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統都將載入備份的 RouterBOOT 載入器。這對 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中隨裝置附帶以下配件：

- DC ⎓ EU/US 開關電源 24 V，0.38 A，9 W，Level VI，線纜：1.5 m。
- POE 供電器線纜（POE）/ 千兆 POE 供電器（GPOE）。
- 軟管卡箍 40/60 w2 A2 9 mm。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/disc_lite5_ac](https://mikrotik.com/product/disc_lite5_ac)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

![](/img/8d294e5cd375c591.webp)

![](/img/25f50553ffd86eaf.webp)

![](/img/b0984aa3ad3c6d58.webp)

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置妥善運送至指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

![](/img/ce6fc3eb10b9a1e6.webp)

<table><thead><tr><th>型號</th><th>FCCID</th></tr></thead><tbody><tr><td>RBDiscG-5acD</td><td>TV7LHG5ACD</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝環境中的有害干擾提供合理保護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能造成有害干擾，此時使用者需自費糾正干擾。

FCC 警告：未經合規負責方明確批准的任何更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其操作須遵循以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受所收到的任何干擾，包括可能導致意外操作的干擾。注：本裝置在測試時對外圍裝置使用了遮蔽線纜。為確保合規，必須使用遮蔽線纜與本裝置配合使用。

本裝置及其天線不得與任何其他天線或發射器處於同一位置或聯合工作。重要提示：射頻輻射暴露。本 MikroTik 裝置符合 FCC、IC 以及歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

**天線安裝。警告：** 安裝者有責任確保在美國（或適用 FCC 規則的地區）使用經授權的天線時，僅使用經本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分的規定，嚴禁使用任何未經本產品認證的天線。安裝者應根據國家法規和天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBDiscG-5acD</td><td>7442A-LHG5ACD</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。其操作須遵循以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 要求。其使用須滿足以下兩個條件：(1) 裝置不得產生干擾；(2) 使用者必須接受所受到的任何無線電干擾，即使該干擾可能影響裝置的正常執行。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證而有所不同。

有關裝置生產日期的資訊標註在裝置標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5470-5725 MHz（27 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用須按照 NKRZI 2012 年 11 月 1 日第 559 號決議（已於 2013 年 1 月 3 日在烏克蘭司法部登記，登記號 57/22589）規定的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBDiscG-5acD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相關型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家法規，包括在合法頻段內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。欲瞭解更多詳細資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所設定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告。
