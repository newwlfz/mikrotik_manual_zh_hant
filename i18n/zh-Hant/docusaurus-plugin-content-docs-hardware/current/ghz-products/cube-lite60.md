---
title: "Cube Lite60"
slug: /cube-lite60
source: https://manual.mikrotik.com/hardware/cube-lite60
captured_at: '2026-11-04T09:48:02+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可下載為 <a href="/assets/files/cube-lite60-4d7ed9c7f2202d7a7a4f5a01d2a625ea.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/e1fbe52194fa5d7e.webp)

## [Cube Lite60](https://mikrotik.com/product/cube_lite60) (RBCube-60ad) {#cube-lite60-rbcube-60ad}

Cube Lite60 是一款室外無線路由器，內建定向天線，工作在 60 GHz 頻段。為確保符合當地監管機構的規定，此裝置需要升級到 RouterOS v6.46 或最新版本。

客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律法規進行處理。
- 在任何牆面上安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品旨在室外安裝在立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險情況並損壞系統。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置出現故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。
- 這是 A 類裝置。在居住環境中，本產品可能會造成無線電干擾，在這種情況下，使用者可能需要採取適當的措施。

## 快速開始 {#quickstart}

- 開啟乙太網艙門，將乙太網線纜連線到乙太網埠，將乙太網線纜的另一端連線到隨附的 PoE 供電器；
- 將 PoE 供電器插入您的網路交換器或計算機；
- 將隨附的電源插入 PoE 供電器以啟動裝置；
- 將 LAN 計算機的 IP 配置設定為自動 (DHCP)；
- 裝置的預設 IP 地址為 192.168.88.1，在網頁瀏覽器中開啟該地址即可開始配置；
- 使用者名稱：admin，預設沒有密碼，您將自動登入到 Quick Set 介面（對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 我們建議點選右側的 "Check for updates" 按鈕，並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性；
- 要個性化您的無線網路，可以在 "Network Name" 欄位中更改 SSID；
- 在螢幕左側的 "Country" 欄位中選擇您所在的國家/地區，以應用國家/地區法規設定；
- 在 "WiFi Password" 欄位中設定您的無線網路密碼，密碼必須至少包含八個字元；
- 在右側底部的 "Password" 欄位中設定路由器密碼，並在 "Confirm Password" 欄位中重複輸入，該密碼將在下次登入時使用；
- 點選 "Apply Configuration" 儲存更改。*如果裝置發生了 RX 阻塞情況，裝置將在幾秒鐘後恢復訊號。*

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

- 掃描二維條碼並選擇您喜歡的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱將會自動填入。
- 點選 Connect 透過無線網路與您的裝置建立連線。
- 選擇 Quick setup，應用將通過幾個簡單的步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

## 配置 {#configuration}

登入後，我們建議在 QuickSet 選單中點選 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將要使用的國家/地區，以符合當地法規。除本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法進行 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置（參見 ）。如果裝置失去連線，請等待幾秒鐘，裝置將自動恢復連線。

## 組裝與安裝 {#assembly-and-mounting}

該裝置可以安裝在垂直或水平立杆上，如圖 A 和圖 B 所示。請注意，裝置安裝時底部卡扣必須朝下。立杆最大直徑為 51 mm。

本裝置的安裝和配置應由經過認證的人員完成。

選擇您想要的位置，裝置需要進行精確調整以獲得最佳效能。

- 使用 ph0 螺絲刀和隨附的螺絲將隨附的支架固定到裝置背面。
- 使用 8 mm 棘輪扳手，透過 U 型螺栓支架安裝到立杆上。
- 將螺栓放入三個位置之一，它們可實現微調，放在中間位置時可在 23 度範圍內調節，如果調節需要超出該範圍，請將螺絲更換到其他位置。

![](/img/acd1ca316e8c01cd.webp)

本裝置的防護等級為 IP54。在室外安裝時，請確保所有線纜開口朝下。我們建議使用 PoE 供電器以及具有正確接地的 Cat6 遮蔽線纜。使用和安裝本裝置時，請注意最大允許暴露量 (MPE) 安全距離，輻射器與您身體之間至少保持 20 cm 的距離。

或者，也可以將裝置安裝在裝置背面的三個安裝槽之一上。

![](/img/c5e03fa807689f16.webp)

![](/img/be7006c56abe1792.webp)

- 例如，您可以使用金屬環。
- 使用十字螺絲刀鬆開金屬環。
- 將其一端穿過三個安裝槽中最方便的一個。
- 將裝置放在將要安裝的立杆上。
- 將安裝環鬆脫的一端滑回其閉合卡扣，並使用螺絲刀擰緊。

建議使用紮帶將乙太網線纜固定到立杆上，與裝置的距離約為 30 cm。

作為附加選項，您可以使用 "quickMOUNT-X"——可單獨購買的便於調節的安裝支架。產品網頁：[https://mikrotik.com/product/qm_x](https://mikrotik.com/product/qm_x)

![](/img/8f9318498c6d2b23.webp)

專門設計，可在立杆上進行垂直和水平調節。

## 接地 {#grounding}

本裝置包含一個接地連線（標記為 ⏚），您應將其連線到裝置使用地所在塔架或建築物的接地裝置。這可大幅降低靜電放電和雷擊損壞的風險。

## 供電 {#powering}

Cube Lite60 接受來自無源 PoE 供電器的 DC ⎓ 電源（隨附一個電源和一個 PoE 供電器），接受 12-28 V DC ⎓，最大負載功耗為 4 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線纜連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自您本地網路 (LAN) 的乙太網線纜連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 10/100 乙太網埠。
- 整合的 w60g 介面，帶有內建天線。

## 復位按鈕 {#reset-button}

routerBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置復位為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置並恢復預設值。
- 當 LED 不再亮起（約 20 秒）後鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。無論使用上述哪種選項，如果在裝置接通電源之前按下按鈕，系統將載入備份的 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的附件：

- EU/US 開關電源 24V DC ⎓，0.38 A，9 W，Level VI，線纜：1.5 m。
- 帶遮蔽乙太網線纜/聯結器的 POE 供電器 (RBPOE)。
- SXT_SQ_Mountv1。
- K-70 緊固套件。

## 規格 {#specifications}

有關 SQ 系列產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/cube_lite60](https://mikrotik.com/product/cube_lite60)

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及更高版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

本裝置符合 ETSI 法規規定的最大 TX 功率限制。在歐盟，頻率和最大發射功率如下所示：57-66GHz：34.92 dBm。60 GHz 頻段的工作模式：58.32 GHz、60.48 GHz、62.64 GHz、64.80 GHz。本裝置已透過認證，可用於室外的點對多點應用。在以下國家/地區，本裝置不能用於固定點對點應用：

![](/img/01438e2d9209ce7d.webp)

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCCID</th></tr></thead><tbody><tr><td>RBCube-60ad</td><td>TV7CUBE60</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝環境中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區執行本裝置很可能會造成有害干擾，在這種情況下，使用者將需要自費糾正干擾。

**FCC 警告：** 未經合規責任方明確批准的任何更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不會造成有害干擾，並且 (2) 本裝置必須接受接收到的任何干擾，包括可能導致非預期操作的干擾。本裝置及其天線不得與其他任何天線或發射器處於同一位置或聯合執行。

除 FCC CFR §15.255 (b) 中列出的條件外，本裝置不得在飛機上使用。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置的安裝和操作應使輻射器與您身體的任何部位之間保持至少 20 cm 的最小距離。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBCube-60ad</td><td>7442A-CUBE60</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和操作應使輻射器與您身體的任何部位之間保持至少 20 cm 的最小距離。Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

除 ISED RSS-210 附錄 J.1 中列出的條件外，本裝置不得在飛機上使用。Cet appareil ne doit pas être utilisé sur un avion, sauf dans les conditions énumérées ISED RSS-210 Annex J.1.

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

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

## 烏克蘭國家通訊和資訊國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBCube-60ad 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WiGig {#wigig}

<table><thead><tr><th>工作通道 / 最大輸出功率 Betriebskanäle / maximale Ausgangsleistung Canaux opérationnels / puissance de sortie maximale Canali operativi / massima potenza di uscita Canales operacionales / potencia de salida máxima Операционные каналы / максимальная выходная мощность</th><th>58.32 GHz / &lt;40 dBm</th></tr></thead><tbody><tr><td>60.48 GHz / &lt;40 dBm</td><td></td></tr><tr><td>62.64 GHz / &lt;40 dBm</td><td></td></tr><tr><td>64.80 GHz / &lt;40 dBm</td><td></td></tr></tbody></table>
