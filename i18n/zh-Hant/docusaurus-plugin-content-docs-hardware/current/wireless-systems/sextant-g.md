---
title: "SEXTANT G"
slug: /sextant-g
source: https://manual.mikrotik.com/hardware/sextant-g
captured_at: '2026-11-04T10:03:49+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/69bc768aa04e219f.webp)

## [SEXTANT G](https://mikrotik.com/product/RBSEXTANTG-5HPnD) (RBSEXTANTG-5HPnD) {#sextant-g-rbsextantg-5hpnd}

RouterBOARD SEXTANT G 以完整套裝形式提供，內建 802.11n 雙鏈無線裝置和雙極化 18 dBi 天線。它配有一個支援 MDI-X 自動檢測的千兆乙太網介面。包裝內含 SEXTANT G 裝置、電源介面卡、千兆 PoE 注入器以及兩個軟管卡箍。完整規格和宣傳冊請參見 [SEXTANT G 產品頁面](https://mikrotik.com/product/RBSEXTANTG-5HPnD)。

## 首次使用 {#first-use}

- 將乙太網線連線到小塑膠門後的埠
- SEXTANT G 透過 *千兆 PoE 注入器* 接受 24 V 被動 PoE
- 用於配置的 LAN 預設 IP 地址為 192.168.88.1
- 使用者名稱為 **admin**，且沒有密碼（對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）
- 選擇您所在的國家/地區，以應用該國家/地區的法規設定。

## 供電 {#powering}

該板卡可透過乙太網埠（被動 PoE）接受 8-30 V DC 供電。包裝內含 24V 介面卡。裝置的最大功耗為 13.8 W。

## 安裝 {#mounting}

將卡扣朝前，把安裝支架滑入機殼底部的導軌，直到卡扣咔噠一聲到位。裝置隨附一個軟管卡箍——將卡箍穿入支架上的開口，並環繞在將要安裝的立杆上。對齊完成後擰緊軟管卡箍的螺絲。另設有兩個螺絲孔，作為防止支架意外移動的額外保障。裝置帶有一個滑動門，乙太網埠和復位跳線位於其後。該門也可以用螺絲固定在所提供的螺絲孔中。內建天線的連線方式如下：chain0 = 水平極化，chain1 = 垂直極化。本裝置安裝和執行時，輻射體與您身體的任何部位之間應保持至少 30 cm 的距離。

## 配置 {#configuration}

登入後，我們建議您點選 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳的效能和穩定性。對於無線型號，請務必選擇裝置將要使用的國家/地區，以符合當地法規。除了本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始，熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參閱相關章節 。

## 復位按鈕 {#reset-button}

復位按鈕具有以下功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可復位 RouterOS 配置（總共 5 秒）。
- 或者繼續按住按鈕 5 秒鐘，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總共 15 秒）。無論使用上述哪種方式，如果在裝置通電之前按住按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統未經測試。

## 聯邦通訊委員會 (FCC) 干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID: TV7RB912G-5HPNDM

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的保護，防止有害干擾。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則建議使用者嘗試透過以下措施之一來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改都可能使使用者操作本裝置的許可權失效。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾，(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器放置在同一位置，也不得與其協同操作。**重要：射頻輻射暴露。** 本裝置符合 FCC 針對不受控環境所規定的射頻輻射暴露限值。本裝置安裝和執行時，輻射體與您身體的任何部位之間應保持至少 20 cm 的距離。本裝置及其天線不得與任何其他天線或發射器放置在同一位置，也不得與其協同操作。**天線安裝。警告**：安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用經授權的天線時，僅使用經本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，明確禁止使用任何未經本產品認證的天線。安裝人員應根據國家/地區法規並按照天線型別配置天線的輸出功率水平。帶有聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。操作須符合以下兩個條件：(1) 本裝置不得造成干擾，(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

在 5150–5250 MHz 頻段內工作的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный диапазон</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

Робоча частота (Максимальна вихідна потужність): 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

### CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相關型號）**</th><th>**使用的通道**</th><th>**最大輸出功率 (EIRP)**</th><th>**限制**</th></tr></thead><tbody><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家/地區的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置必須由專業人員安裝！**
