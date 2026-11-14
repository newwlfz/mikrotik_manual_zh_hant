---
title: "CCR2004-1G-2XS-PCIe"
slug: /ccr2004-1g-2xs-pcie
source: https://manual.mikrotik.com/hardware/ccr2004-1g-2xs-pcie
captured_at: '2026-11-04T05:55:49+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/d6a158969481e5d2.jpg" alt="" width={799} height={571} /></p>

## [CCR2004-1G-2XS-PCIe](https://mikrotik.com/product/ccr2004_1g_2xs_pcie) {#ccr2004-1g-2xs-pcie}

一款智慧 PCIe 網路介面卡，可為您的伺服器新增功能完備的路由器能力。如果您想節省伺服器機房的空間，這是建立 25 Gigabit 網路的智慧且簡便的方法！完整規格和產品手冊請參閱 [CCR2004-1G-2XS-PCIe 產品頁面](https://mikrotik.com/product/ccr2004_1g_2xs_pcie)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置擬安裝於機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或未遵循正確的操作步驟，可能會對人員造成危險情況並損壞系統。
- 本產品適合室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規。所有 MikroTik 裝置必須由專業人員安裝。
- 本產品為 Class A 產品。在家庭環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施。

## 快速開始 {#quickstart}

- 將裝置插入計算機的 PCIe 插槽；
- 開啟計算機；
- 應使用 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置，開啟 **Neighbors** 標籤頁並使用 MAC 地址連線到裝置；
- 使用者名稱：**admin**，預設沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 查詢您的產品。所需軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 WinBox 的 "Files" 選單並重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

本裝置透過 PCIe 供電，最大功耗為 29W。

## 配置 {#configuration}

預設情況下，PCIe 介面將顯示為四個虛擬乙太網介面。其中兩個介面以直通模式連線到 25G SFP28 籠。其餘兩個虛擬乙太網-PCIe 介面與千兆乙太網埠橋接，用於管理訪問。

## 規格 {#specifications}

- 產品程式碼 CCR2004-1G-2XS-PCIe
- CPU AL32400 2 GHz
- CPU 架構 ARM 64bit
- CPU 核心數 4
- 記憶體大小 4 GB
- 記憶體型別 DDR4
- 儲存 128 MB，NAND
- 1G 乙太網埠數量 1
- 25G SFP28 埠數量 2
- 作業系統 RouterOS（License level 6）
- 尺寸 170 x 69 x 18 mm
- 工作溫度 -20°C 至 +60°C
- 最大功耗 25 W

## 重設 {#reset}

<p><Img src="/img/41f7dd6ead35bd0c.webp" alt="" width={600} height={800} /></p>

要將此裝置重設為出廠設定，您必須關閉您的 PC。

- 將金屬物體放入復位孔，使其與兩側金屬化部分接觸。
- 開啟 PC 並按住螺絲刀，直到兩個 25G SFP28 LED 開始閃爍紅色後鬆開，它將重設 RouterOS 配置。
- 如果您繼續按住超過 5 秒直至 20 秒，直到紅色 LED 熄滅，則會使 RouterBOARD 查詢 Netinstall 伺服器。

## 隨附部件 {#included-parts}

<p><Img src="/img/a0c855ba0573e499.webp" alt="" width={238} height={227} /></p>

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及更高版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

**本裝置在 Linux（最低核心 5.15.25）和 RouterOS（最低版本 7.x）中受支援，但在 Windows 中無法被識別。**

[https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git/commit/?id=bf8e59fd315f](https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git/commit/?id=bf8e59fd315f)

<p><Img src="/img/9451b2eb2e7bf01c.webp" alt="" width={576} height={521} /></p>

安全提示：存在觸電危險。本裝置只能由受過培訓的人員進行維修。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置場所。請熟悉將裝置妥善運送到您所在地區指定處置場所的程式。

### 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 Class A 數字裝置的限制。這些限制旨在為商業安裝提供合理的有害干擾防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能會造成有害干擾，此時使用者將需要自行承擔費用來糾正干擾。

FCC 警告：任何未經合規負責方明確批准的更改或修改，都可能會使使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。其操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致非預期操作的干擾。

注意：本裝置在測試時使用了外圍裝置的遮蔽電纜。為確保合規，必須使用遮蔽電纜與本裝置配合使用。

### 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。其操作須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

### UKCA 標誌 {#ukca-marking}

<p><Img src="/img/387853c20d5a4c82.gif" alt="" width={2115} height={2113} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Unijas iela 2, Riga, LV-1039, Latvia.

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
