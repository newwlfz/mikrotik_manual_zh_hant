---
title: "cAP lite"
slug: /cap-lite
source: https://manual.mikrotik.com/hardware/cap-lite
captured_at: '2026-11-04T05:55:23+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/54e3094058df4d34.jpg" alt="" width={799} height={739} /></p>

## [cAP lite](https://mikrotik.com/product/RBcAPL-2nD-307) (RBcAPL-2nD) {#cap-lite-rbcapl-2nd}

產品附帶兩種不同的外殼，可以輕鬆更換；或者，如果您希望設計與環境更加協調，我們還提供適合 3D 列印的設計檔案。有關完整規格和宣傳冊，請參見 [cAP lite 產品頁面](https://mikrotik.com/product/RBcAPL-2nD-307)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置旨在安裝於機架中。開始安裝前，請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確程式可能會對人員造成危險情況，並損壞系統。
- 本產品旨在室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座中拔出電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境設定的輻射暴露限值。本 MikroTik 裝置安裝和操作時，應與您的身體、職業使用者或公眾保持不少於 20 釐米的距離。

## 設定 {#setup}

- 確保您的網際網路服務提供商 (ISP) 允許硬體更改並自動分配 IP 地址；
- 將 ISP 線纜連線到乙太網埠；
- 將裝置連線到電源；
- 透過無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在 Web 瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具：[https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方法以確保可訪問性；**
- 使用預設 IP 地址 192.168.88.1 在所選工具中開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 單擊 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 若要手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，並重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 復位按鈕 {#reset-button}

復位按鈕具有三個功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請將裝置置於 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議驗證兩個選項，以防其中一個無法使用。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。根據型號不同，這可能由 **USR、USER、System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個 10/100 乙太網埠，支援自動交叉/直通線纜校正 (Auto MDI/X)。可以使用直通或交叉線纜連線到其他網路裝置。
- 一個整合無線 2.4 GHz 802.11b/g/n。
- 一個 USB AB 型插槽。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

- DC ⎓ EU/US 開關電源 24 V，0.2 A，4.8 W，Level VI，線纜：1.5m）。
- 帶遮蔽乙太網線纜/聯結器的 POE 注入器 (RBPOE)。
- K-49 緊固套件。
- Map 牆面蓋板。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

<p><Img src="/img/8d294e5cd375c591.webp" alt="" width={247} height={244} /></p>

<p><Img src="/img/25f50553ffd86eaf.webp" alt="" width={241} height={80} /></p>

<p><Img src="/img/b0984aa3ad3c6d58.webp" alt="" width={239} height={81} /></p>

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

## 安裝 {#mounting}

<p><Img src="/img/1e6c830dab17a8df.webp" alt="" width={735} height={1042} /></p>

## 注意 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置使用的範圍與上述法規不同，則需要將製造商/供應商提供的定製韌體版本應用到終端使用者裝置，並防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可證。
- 任何裝置的資料表可在製造商官方網站上獲取。
- 序列號末尾帶有字母 “EG” 的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，TX 功率限制為 20dBm (EIRP)。
- 序列號末尾帶有字母 “EG” 的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，TX 功率限制為 23dBm (EIRP)。
- 序列號末尾帶有字母 “EG” 的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，TX 功率限制為 20dBm (EIRP)。

請確保裝置具有鎖定軟體包（製造商提供的韌體版本），必須將其應用到終端使用者裝置以防止終端使用者重新配置。產品將標有國家程式碼 “-EG”。本裝置需要升級到最新版本，以確保符合當地法規！終端使用者有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線裝置必須由專業人員安裝。

為避免環境汙染，請將裝置與生活垃圾分開，並以安全方式處置，例如送到指定的廢物處置場所。請熟悉您所在地區將裝置正確運輸到指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID: TV7MAPL2ND

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理保護，防止有害干擾。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整或移動接收天線。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改都可能使使用者操作本裝置的許可權失效。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾，以及 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器放在一起，也不得與其一起執行。**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境設定的 RF 輻射暴露限值。本裝置安裝和操作時，輻射器與您身體的任何部分之間應保持至少 20 釐米的距離。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC:7442A-MAPL2ND 本裝置符合加拿大工業部免許可證 RSS 標準。操作須符合以下兩個條件：(1) 本裝置不得造成干擾，以及 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement. **重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境設定的輻射暴露限值。本裝置安裝和操作時，輻射器與您身體的任何部分之間應保持至少 20 釐米的距離。Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射器功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊位於其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 МГц (20 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需要按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定（2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBcAPL-2nD 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相關型號）**</th><th>**使用的通道**</th><th>**最大輸出功率 (EIRP)**</th><th>**限制**</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告。
