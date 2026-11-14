---
title: "PWR-LINE AP"
slug: /pwr-line-ap
source: https://manual.mikrotik.com/hardware/pwr-line-ap
captured_at: '2026-11-04T06:02:52+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/ed0b0664d647ce4c.webp" alt="" width={751} height={768} /></p>

PWR-LINE 系列裝置允許受支援的裝置之間透過普通電力線實現類似乙太網的連線。當插入同一個電路時，PWR 裝置將使用 HomePlug AV 標準建立乙太網連線。PWR-LINE AP 是一款無線接入點，具有一個乙太網埠、內建 802.11b/g/n WiFi 接入點以及整合的 PWR-LINE 支援。只需將此裝置直接插入 MikroTik 路由器的其中一個 LAN 埠，並在您場所中的更遠處再新增一臺，即可擴充套件無線網路覆蓋範圍，而無需安裝任何 LAN 線纜。您可以安裝更多 PWR-LINE 裝置來進一步構建網路，最多支援八臺裝置。

## 連線 {#connecting}

- 將一臺 PWR-LINE AP 裝置插入電源插座。
- 主裝置應插入路由器的其中一個 LAN 埠。
- 其他 PWR-LINE AP 裝置可以放置在同一電力電路中的任意插座上的任意位置。
- 使用 WinBox 的 "Neighbors" 標籤頁來發現 PWR LINE 單元的地址。
- 由於預設沒有密碼，您將自動登入（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。請設定您的 wifi 密碼和您所在的國家/地區，以確保遵守當地法規。
- 要新增更多透過電力線連線的裝置，請在同一電力電路中的某處新增相容裝置。有關如何配對單個 PWR-LINE 裝置的資訊，請參見“按鈕和跳線”一節。重要提示！該裝置被配置為網橋，用於擴充套件您的 LAN 網路。預設情況下，它沒有密碼或防火牆，在未進行相應配置的情況下不應直接連線到網際網路。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下來自網際網路埠的所有訪問均被阻止）。出於恢復目的，可以從網路啟動裝置，請參見章節（連結）。

## 供電 {#powering}

該裝置可直接由其插入的 100-240 V ~50/60Hz 牆壁插座供電。最大負載下的功耗可達 7 W。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個 10/100 乙太網埠，支援自動交叉/直通線纜修正（Auto MDI/X），因此您可以使用直通或交叉線纜連線其他網路裝置。
- 整合 2.4 GHz 802.11b/g/n 無線，帶板載 PIF 天線，最大增益 1.5 dBi。

## 按鈕和跳線 {#buttons-and-jumpers}

PWR-LINE AP 具有以下按鈕：

### 復位按鈕 {#reset-button}

- 在裝置上電前按住按鈕，上電時該按鈕將強制載入備份引導載入程式。繼續按住該按鈕以使用此按鈕的另外兩項功能。
- 當綠色 LED 開始閃爍時鬆開按鈕，以重設 RouterOS 配置。若不想載入備份引導載入程式，您可以在已經通電後再開始按住按鈕。
- 在 LED 不再閃爍後（約 20 秒）鬆開按鈕，使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 所需）。無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

### Sync 按鈕 {#sync-button}

- 按住 0.5 – 3 秒。裝置將在 120 秒內嘗試與另一臺 PWR-LINE 裝置通訊。橙色 LED 閃爍表示它處於搜尋模式。您還必須對另一臺 PWR 裝置執行相同操作，以便它們能夠同步。再次按按鈕可取消搜尋。您也可以在 RouterOS 設定中手動設定安全金鑰。
- 按住 5 – 8 秒。將生成新的安全金鑰。這用於將 PWR-LINE 裝置從現有 PWR 網路中移除。
- 按住 10 – 15 秒。重設所有與 PWR 相關的設定。

### Mode 按鈕 {#mode-button}

可以透過 RouterOS 軟體配置此按鈕來執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置的工作範圍與上述規定不同，則必須對終端使用者裝置應用來自制造商/供應商的定製韌體版本，並防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料表均可在製造商官方網站上獲取。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限於 2.400 – 2.4835 GHz，發射功率限於 20dBm（EIRP）。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限於 5.150 – 5.250 GHz，發射功率限於 23dBm（EIRP）。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限於 5.250 – 5.350 GHz，發射功率限於 20dBm（EIRP）。

請確保裝置具有鎖定包（來自制造商的韌體版本），必須將其應用於終端使用者裝置，以防止終端使用者重新配置。產品將標記國家程式碼“-EG”。本裝置需要升級到最新版本，以確保符合當地主管機構的規定！終端使用者有責任遵守當地國家/地區法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝。

## 作業系統支援 {#operating-system-support}

該裝置支援版本號等於或高於 RouterOS 選單 /system resource 中所指示版本的 RouterOS 軟體。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置場所處置。請熟悉您所在地區將裝置正確運輸到指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID: TV7PL64112ND 本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的有害干擾防護。

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉再開啟裝置來確定），則建議使用者嘗試透過以下一項或多項措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。**FCC 警告：** 任何未經合規責任方明確批准的更改或修改都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的規定。其操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器同地放置或共同操作。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

IC: 7442A-PL64112ND 本裝置符合加拿大工業部免許可 RSS 標準。其操作須符合以下兩個條件：(1) 本裝置不得造成干擾，並且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射機功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

有關裝置製造日期的資訊，以其標籤上序列號末尾、用斜槓分隔的數字表示。第一位數字表示年份編號（年份的最後一位數字），隨後兩位數字表示周編號。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準（Norma Oficial Mexicana） {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2480-2483.5 МГц（20 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需要按照 NCRFI 2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 PWR-LINE AP 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝！*
