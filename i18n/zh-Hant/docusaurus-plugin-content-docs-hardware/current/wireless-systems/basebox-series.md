---
title: "BaseBox 系列"
slug: /basebox-series
source: https://manual.mikrotik.com/hardware/basebox-series
captured_at: '2026-11-04T09:43:23+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/715fc30cd77673f2.jpg)

## [BaseBox 5](https://mikrotik.com/product/RB912UAG-5HPnD-OUT) (RB912UAG-5HPnD-OUT) {#basebox-5-rb912uag-5hpnd-out}

:::info 本文涵蓋

- **[BaseBox 2](https://mikrotik.com/product/RB912UAG-2HPnD-OUT)** (RB912UAG-2HPnD-OUT)
- **[BaseBox 5](https://mikrotik.com/product/RB912UAG-5HPnD-OUT)** (RB912UAG-5HPnD-OUT)
- **[BaseBox 6](https://mikrotik.com/product/basebox_6)** (RB912UAG-6HPnD-OUT)
:::

Basebox 是一款堅固且防風雨的戶外裝置，基於 RB912 無線路由器型號。它具備高功率無線和 一個支援 MDI-X 自動檢測的千兆乙太網介面。該裝置有兩個 RPSMA 介面，用於連線外接天線。裝置包裝內附帶電源介面卡、PoE 注入器和兩個安裝環。在這種情況下，裝置上還提供了更多 RP-SMA 介面的備用位置。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準操作規範。
- 本產品的最終處置應遵守所有國家法律法規。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本產品擬安裝在戶外立杆上。開始安裝前，請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能對人員造成危險情況並損壞系統。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。

## 首次使用 {#first-use}

- 請選擇您的供電解決方案，請參閱復位按鈕。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

BaseBox 2 型號 - 2.4 GHz，802.11b/g/n。

- BaseBox 5 型號 - 5 GHz，802.11a/n。
- BaseBox 6 型號 - 6 GHz，802.11a/n。
- 一個 10/100/1000 千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通線或交叉線連線其他網路裝置。
- USB type-A 插槽。
- 一個 miniPCIe 插槽。*本裝置可能與 R11e-LTE 國際版調變解調器不相容。*

## miniPCI-e 插槽的使用 {#the-minipci-e-slot-usage}

- 取下頂蓋；
- 擰下裝置背面的兩顆螺絲；

![](/img/e274298dd19ae257.webp)

- 開啟乙太網埠蓋，並將其從裝置底座中拔出；

![](/img/010c63866323c8b6.webp)

- 擰下天線介面；

![](/img/d01c9eb3d3c98f7f.webp)

- 將 PCB 板從底蓋中取出；

![](/img/fa3c45a2c403db34.webp)

- 安裝您的調變解調器並重新組裝。

## 復位按鈕 {#reset-button}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置現在會查詢 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。這對 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未測試。

## 隨附部件 {#included-parts}

![](/img/dec8180f44424e05.webp)

*DIN 安裝件包含四顆螺絲，用於將其固定到裝置背面。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置正確運輸至指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝環境中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區域操作本裝置可能會造成有害干擾，此時使用者需自行承擔費用來糾正干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與其他任何天線或發射器位於同一位置或協同工作。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置安裝和操作時，輻射體與您身體的任何部位之間應保持最小距離，請參閱下表。

<table><thead><tr><th>**型號**</th><th>**FCC ID**</th><th>**射頻暴露最小安全距離**</th></tr></thead><tbody><tr><td>BaseBox 2</td><td>TV7RB912G-2HPND</td><td>142 cm</td></tr><tr><td>BaseBox 5</td><td>TV7RB912G-5HPNDM</td><td>375 cm</td></tr><tr><td>BaseBox 6</td><td>TV7RB912G-6HPND</td><td>375 cm</td></tr></tbody></table>

**天線安裝警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地方）使用經授權的天線時，只能使用經本產品認證的天線。安裝人員應根據國家法規和天線型別配置天線的輸出功率水平。帶有介面的裝置需要由專業人員安裝，以確保符合健康與安全要求。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可證 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-3 (A)/NMB-3(A)

在 5150–5250 MHz 頻段內操作的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和操作時，輻射體與您身體的任何部位之間應保持最小距離，請參閱下表。Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé avec une distance minimale entre le radiateur et toute partie de votre corps, voir le tableau ci-dessous.

<table><thead><tr><th>**型號**</th><th>**IC**</th><th>**射頻暴露最小安全距離**</th></tr></thead><tbody><tr><td>BaseBox 2</td><td>7442A-912G2HPND</td><td>142 cm</td></tr><tr><td>BaseBox 5</td><td>7442A-912G5HPNDM</td><td>378 cm</td></tr><tr><td>BaseBox 6</td><td>7442A-912G6HPNDM</td><td>378 cm</td></tr></tbody></table>

**天線安裝警告：** 安裝人員有責任確保在加拿大（或適用 IC 規則的地方）使用經授權的天線時，只能使用經本產品認證的天線。安裝人員應根據國家法規和天線型別配置天線的輸出功率水平。帶有介面的裝置需要由專業人員安裝，以確保符合健康與安全要求。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный диапазон</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц, 6425-7100 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，且。
- 本裝置必須接受任何干擾，包括可能導致其非預期執行的干擾。製造商：MikroTikls SIA, Unijas 2, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA, Вулиця Уніяс 2, Рига, Латвія, LV1039。

Робоча частота (Максимальна вихідна потужність): 2400-2483.5 МГц (20 дБм)5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

![](/img/7182f05dc1a2f3bc.webp)

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均不受任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參閱上文的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.請在認證實驗室中使用我們的裝置測試您的天線，以符合歐盟規則。
