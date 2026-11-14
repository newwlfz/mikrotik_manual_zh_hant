---
title: "PWR-LINE"
slug: /pwr-line
source: https://manual.mikrotik.com/hardware/pwr-line
captured_at: '2026-11-04T06:02:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/edf3c57522595fc4.webp" alt="" width={768} height={768} /></p>

PWR-LINE 系列裝置允許受支援的裝置之間透過普通電力線實現類似乙太網的連線。當插入同一電路時，PWR 裝置將使用 HomePlug AV 標準建立乙太網連線。PWR-LINE 是一款內建 USB 線纜的智慧電源介面卡。該裝置專為帶有 microUSB 埠並支援 PWR-LINE 的 MikroTik 產品而設計。將此介面卡連線到電源插座，然後連線 USB 線纜為受支援的 MikroTik 裝置供電。在場所內較遠處對另一臺相容 PWR-LINE 的裝置執行相同的操作，這些裝置便會建立連線，無需安裝任何 LAN 線纜。該裝置將在路由器的配置介面中顯示為額外的乙太網介面。您可以安裝更多 PWR-LINE 裝置來進一步擴充套件網路。

## 連線 {#connecting}

- 將一臺 PWR-LINE 裝置插入電源插座。
- 將內建 USB 線纜連線到受支援的 MikroTik 路由器的 microUSB 埠。
- 在同一電路中的某處插入另一臺 PWR-LINE 裝置（或任何其他相容裝置）。使用 sync 按鈕連線裝置，您的本地網路將自動擴充套件。有關如何配對更多 PWR-LINE 裝置，請參閱“按鈕和跳線”章節。

## 供電 {#powering}

該裝置可直接由所插入的 100-230 V ~50/60Hz 牆壁插座供電。最大負載下的功耗可達 5 W。

## 按鈕和跳線 {#buttons-and-jumpers}

### PWR 連線按鈕（sync） {#pwr-connection-button-sync}

- 按住 0.5 – 3 秒。裝置將在 120 秒內嘗試與另一臺 PWR-LINE 裝置通訊。橙色 LED 閃爍表示裝置處於搜尋模式。您還必須在另一臺 PWR 裝置上執行相同的操作，以便它們能夠同步。再次按下按鈕可取消搜尋。
- 按住 5 – 8 秒。將生成新的安全金鑰。從現有 PWR 網路中移除 PWR-LINE 裝置時需要使用此操作。
- 按住 10 – 15 秒。重設所有與 PWR 相關的設定。

為避免汙染環境，請勿將裝置與生活垃圾一起丟棄，請以安全的方式處理，例如送至指定的廢棄物處理場所。請了解您所在地區將裝置正確運送至指定處理場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝提供合理的有害干擾防護。

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉並重新開啟裝置來確定），則建議使用者嘗試透過以下措施之一來消除干擾：

- 調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以獲取幫助。FCC 警告：未經負責合規的一方明確批准的任何更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其執行須滿足以下兩個條件：(1) 本裝置不得產生有害干擾，且 (2) 本裝置必須接受所接收的任何干擾，包括可能導致非預期執行的干擾。本裝置及其天線不得與任何其他天線或發射器共址或聯合執行。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可證 RSS 標準。其執行須滿足以下兩個條件：(1) 本裝置不得產生干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置非預期執行的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## Norma Oficial Mexicana {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
