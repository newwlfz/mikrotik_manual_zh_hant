---
title: "hAP mini"
slug: /hap-mini
source: https://manual.mikrotik.com/hardware/hap-mini
captured_at: '2026-11-04T05:58:30+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/91ff4ed7ddac7300.webp" alt="" width={746} height={800} /></p>

## [hAP mini](https://mikrotik.com/product/RB931-2nD) (RB931-2nD) {#hap-mini-rb931-2nd}

hAP 是一款簡單的家用無線接入點。它已完成初始配置，您只需插上 ISP 線纜即可開始使用無線網路上網。我們建議您設定密碼以保護裝置安全。完整規格和宣傳冊請參見 [hAP mini 產品頁面](https://mikrotik.com/product/RB931-2nD)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於機架安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座上拔下電源插頭。
- 客戶有責任遵守當地國家法規，包括在法律許可的頻段內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置應與您的身體、職業使用者或公眾保持不少於 20 釐米的距離。

## 設定 {#setup}

- 選擇您的供電方案，可能的方案請參見“供電”部分。
- 將網際網路線纜連線到第一個埠，如有有線裝置，將其連線到其他埠。
- 將計算機的 IP 配置設定為自動（DHCP）。
- 從您的 PC 或智慧手機連線名稱以“MikroTik”開頭的無線網路。
- 連線無線網路後，在 Web 瀏覽器中開啟 192.168.88.1 開始配置，使用者名稱為 **admin**，預設沒有密碼（某些型號請在貼紙上檢視使用者名稱和無線密碼）。
- 使用移動應用程式時請選擇 Quick Setup，它將在六個簡單步驟中引導您完成所有必要配置。
- 我們建議點選“Check for updates”按鈕，將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。
- 在載入的介面上選擇您所在的國家/地區，以應用國家法規設定並設定密碼。

## 供電 {#powering}

裝置可從 microUSB 埠供電。該埠本身並不作為標準 microUSB 資料埠使用，僅用於供電。您可以使用通常隨智慧手機附帶的標準 0.5 - 2A USB 介面卡。包裝盒內附有一個 5V 0.7A USB 充電器。最大負載下的功耗可達 3.5W。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

<p><Img src="/img/9bcba09a7b6a0d53.webp" alt="" width={249} height={246} /></p>

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟應用程式。
- 預設情況下，IP 地址和使用者名稱已自動填入。
- 點選 Connect，透過無線網路與裝置建立連線。
- 選擇 Quick setup，應用程式將在幾個簡單步驟中引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要設定。

## 配置 {#configuration}

除了本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側透過裝置的 MAC 地址進行連線（預設情況下，來自網際網路埠的所有訪問均被阻止）。出於恢復目的，可以引導裝置進行重新安裝，請參見“按鈕和跳線”。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 乙太網埠透過交換晶片連線，可單獨配置，並支援自動交叉/直通線纜糾正（Auto MDI/X），因此您可以使用直通線或交叉線連線其他網路裝置。
- 整合無線模組，支援 AP/CPE/P2P/Repeater 模式。

## 安裝 {#mounting}

本裝置設計用於室內使用，可放置在平坦表面上，所需線纜均連線在裝置後部。本裝置的 IPX 等級為 IPX0。我們建議使用 Cat6 遮蔽線纜。警告！本裝置的安裝和執行位置應與您的身體保持至少 20 釐米的距離。在住宅環境中執行本裝置可能會造成無線電干擾。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三種功能：

- 在啟動過程中按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議同時驗證這兩種選項，以防其中一種無法使用。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電後等待 1–2 秒，然後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。視型號不同，這可能由 **USR、USER、System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置上電之前按下按鈕，系統將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置工作在上述法規之外的頻段，則需要由製造商/供應商提供定製的韌體版本並應用到終端使用者裝置上，同時防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料手冊均可在製造商官方網站上獲取。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限制在 2.400 – 2.4835 GHz，發射功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限制在 5.150 – 5.250 GHz，發射功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限制在 5.250 – 5.350 GHz，發射功率限制為 20dBm（EIRP）。

請確保裝置具有 lock 軟體包（來自制造商的韌體版本），該韌體需要應用到終端使用者裝置上，以防止終端使用者重新配置。產品將標註國家程式碼“-EG”。本裝置需要升級到最新版本，以確保符合當地主管部門的法規！終端使用者有責任遵守當地國家法規，包括在法律許可的頻段內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢棄物處置場所。請了解將裝置正確運送到您所在地區指定處置場所的流程。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID:TV7931-2ND 本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的有害干擾防護。本裝置會產生、使用並輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉再開啟裝置來確定），建議使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整或移動接收天線。
- 增大裝置與接收器之間的間距。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。**FCC 警告：** 未經負責合規的一方明確批准的任何更改或修改，都可能導致使用者操作本裝置的許可權失效。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致不良操作的干擾。本裝置及其天線不得與其他任何天線或發射機位於同一位置或聯合執行。**重要提示：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置的安裝和執行位置應使輻射體與您身體的任何部位之間保持至少 20 釐米的距離。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC:7442A-9312ND 本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置操作異常的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要提示：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和執行位置應使輻射體與您身體的任何部位之間保持至少 20 釐米的距離。Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射機功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證情況而有所不同。

有關裝置生產日期的資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

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

工作頻率（最大輸出功率）：2400-2483.5 МГц（20 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需要按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議（2013 年 1 月 3 日在烏克蘭司法部登記，編號 № 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RB931-2nD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>可在所有歐盟成員國無任何限制地使用</td></tr></tbody></table>

** 遵守當地國家法規是客戶的責任，包括在法律許可的通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上文的符合性宣告。
