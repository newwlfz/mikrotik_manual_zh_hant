---
title: "LHG kit 系列"
slug: /lhg-kit-series
source: https://manual.mikrotik.com/hardware/lhg-kit-series
captured_at: '2026-11-04T09:53:54+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/7c2295886e9fa394.webp)

:::info 本文涵蓋

- **LHG LTE6 kit** (RBLHGR&R11e-LTE6)
- **LHG LTE kit** (RBLHGR&R11e-LTE)
- **LHG LTE kit-US** (RBLHGR&R11e-LTE-US)
:::

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規執行。
- 在任何牆面上安裝接入點的所有安裝方法均須獲得當地主管部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於在戶外立杆上安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置，或未遵循正確的操作步驟，可能會對人員造成危險情況並對系統造成損壞。
- 僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。
- 這是 A 類裝置。在居住環境中，本產品可能會引起無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或普通公眾的距離不得小於 130 釐米。

## 快速開始 {#quickstart}

預設配置 CPE RouterMode：

- *WAN 埠受防火牆保護並啟用了 DHCP 用戶端。
- LAN 配置：
- 在 ether1（LAN 埠）上設定了 IP 地址 192.168.188.1/24；
- 已啟用 DHCP 伺服器；
- 已啟用 DNS；
- WAN（閘道器）配置：
- 閘道器：lte1；
- ip4 防火牆：已啟用；
- NAT：已啟用。
- 握住裝置的中央立柱，同時用力按壓保持鎖釦閉合的卡舌，直到鎖釦彈開。
- 將 SIM 卡插入卡槽，晶片朝上。
- 透過將支腳安裝到裝置底座來組裝外殼，參見（連結）段落。
- 將裝置安裝到所需位置，參見（連結）段落。
- 將 LAN 計算機的 IP 配置設定為*自動*（DHCP）。
- 在網頁瀏覽器中開啟 [https://192.168.188.1](https://192.168.188.1) 以開始配置。
- 使用者名稱：a*dmin*，預設沒有密碼，您將自動登入到 Quick Set 介面（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。
- 透過點選右側的 "Check for updates" 按鈕並更新您的 RouterOS 軟體至最新版本來更新裝置，以確保最佳效能和穩定性。必須插入有效的 SIM 卡。
- 要手動更新裝置，請訪問 [https://mikrotik.com/download](https://mikrotik.com/download)
- 為該裝置選擇 MIPSBE 軟體包並將其下載到您的 PC。
- 將下載的軟體包上傳到 WebFig 的 "Files" 選單並重啟裝置。
- 將 RouterOS 軟體更新至最新版本可確保最佳效能、穩定性和安全更新。
- 在右側底部的 "Password" 欄位中設定路由器密碼，並在 "Confirm Password" 欄位中重複輸入，該密碼將在下次登入時使用。
- 選擇 "Apply Configuration" 以儲存更改。所有 7.1.4 之前的 ROS 版本預設 IP 均設定為 192.168.88.1，升級到 7.1.4 之後預設 IP 設定為 192.168.188.1。

## 外殼組裝 {#case-assembly}

- 透過將兩個支腳滑到各自的一側，將它們安裝到 LHG 外殼上，這兩個支腳是不同的，不能互換（觀察產品時，請將其擺放為乙太網埠蓋朝向您，標記為 R 的支腳用於右側，標記為 L 的支腳用於左側）。
- 將組裝好的 LHG 裝置卡入網格的相應中央位置。
- 使用隨附的兩顆自攻螺釘（十字螺絲刀 PH2）將兩個支腳固定到位。包裝中還包含一個接地線聯結器和一個 5 度角介面卡，便於進行向上或向下的傾斜調節。參見段落。

## 開啟外殼蓋 {#opening-the-case-cover}

可選——如需接觸 miniPCIe 插槽，需要開啟裝置頂蓋。作為開啟工具，您可以使用大號一字螺絲刀或一枚小硬幣。開啟時請格外小心，因為不正確的開啟方式可能會將卡扣折斷！*本裝置的安裝和配置應由合格人員完成。* 請按照以下步驟操作：

![](/img/82b7fa2a4a679f2f.webp)

掀起蓋子時還需額外注意，請勿使用尖銳物體強行撬動。

## miniPCIe 插槽使用 {#minipcie-slot-usage}

本裝置配備一個 miniPCIe 插槽，並已根據您所擁有的型號預裝了調變解調器。提供一個 SIM 卡槽，與 miniPCIe 調變解調器配合使用。SIM 卡槽不可單獨使用。更換 miniPCIe 模組應由合格人員完成，處理電氣裝置時請遵循安全預防措施：

- 拆包和處理電子元件時，請使用腕部接地帶以避免靜電放電（ESD）損壞；
- 按照前面的說明開啟上蓋；
- 天線位於 PCB 下方；
- 在 PCB 上找到 miniPCIe 插槽，並卸下兩顆出廠安裝的螺釘；

![](/img/3ce4a8956b2c2a41.webp)

- 將隨機提供的厚導熱墊貼到卡上，並將卡安裝到 miniPCIe 插槽中，使導熱墊位於 PCB 與卡之間；
- 插入您需要的卡；
- 使用先前卸下的兩顆螺釘將卡固定到位；
- 將灰色 uFL 聯結器連線到調變解調器的 MAIN 天線聯結器，將黑色線纜連線到輔助（或 AUX）聯結器；
- 在卡的頂部貼上一片較薄的導熱墊；
- 重新組裝。重新組裝後，將您的移動運營商的 SIM 卡滑入 SIM 卡槽，晶片朝上，如埠標籤所示。該卡槽支援 MicroSIM（3FF）。

## 供電 {#powering}

本裝置可由 12-57 V 802.3af/at 電源以及無源 PoE 注入器供電（隨附一個電源和一個 PoE 注入器）。最大功耗為 6 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線纜連線到 PoE 介面卡的 PoE+DATA 埠；
- 將來自您本地網路（LAN）的乙太網線纜連線到 PoE 介面卡；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 安裝 {#mounting}

![](/img/819eccc51163cf32.webp)

- 將隨附的金屬安裝環滑入天線盤背面的兩個槽中。
- 將裝置安裝到立杆上，乙太網埠朝下。
- 使用 PH2 螺絲刀擰緊安裝環。
- 使用紮帶將乙太網線纜固定到立杆上，距離裝置不超過一米，以避免線纜從埠中被拉出。
- 檢查安裝角度和位置。
- 可選：如有需要，在安裝裝置之前，您可以將隨附的 5 度調節介面卡插入安裝環所插入的頂部或底部槽中。這樣當裝置擰緊到垂直立杆上時，會產生額外的向上或向下角度。
- 將 5 度角介面卡插入其中一個槽中，然後重新安裝裝置。在戶外安裝時，請確保所有線纜開口朝下。使用 POE 注入器並進行正確接地，本裝置在埠蓋下方設有專門設計的接地聯結器。建議使用遮蔽 Cat5/6 線纜。本裝置的 IP 防護等級為 IP54。*警告！本裝置的安裝和執行位置與您身體之間的距離應至少為 120 釐米。在居住環境中執行本裝置可能會引起無線電干擾。*

## 配置 {#configuration}

登入後，您應在 QuickSet 選單中選擇 "Check for updates" 按鈕，因為將 RouterOS 軟體更新至最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始以熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以引導裝置進行重新安裝，請參見相關章節。

## 配件 {#accessories}

包裝中包含以下隨附配件：

![](/img/a62040f544ef34ab.webp)

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個 10/100 乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。直通線或交叉線均可用於連線到其他網路裝置。該乙太網埠可接受來自無源 PoE 注入器的 9-30 V DC 電源。
- MiniPCIe 插槽和 SIM 卡槽（不可單獨使用），用於配合 3G/4G/LTE 調變解調器使用。

## 復位按鈕 {#reset-button}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）；
- 繼續按住 5 秒，LED 常亮，此時鬆開可開啟 CAP 模式。裝置將開始查詢 CAPsMAN 伺服器（共 10 秒）；
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）；無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 模式按鈕 {#mode-button}

模式按鈕的動作可透過 RouterOS 軟體進行配置，以執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。模式按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置。

## 規格 {#specifications}

有關本產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/lhg_lte6_kit](https://mikrotik.com/product/lhg_lte6_kit)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統未經測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置場處置。請熟悉您所在地區將裝置正確運輸到指定處置場的程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>包含的 FCCID</th></tr></thead><tbody><tr><td>RBLHGR&R11e-LTE6</td><td>TV7R11ELTE6</td></tr><tr><td>RBLHGR&R11e-LTE-US</td><td>TV7R11ELTE</td></tr></tbody></table>

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝提供合理的保護，防止有害干擾。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區執行本裝置可能會造成有害干擾，此時使用者將被要求自費糾正干擾

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，(2) 本裝置必須接受任何收到的干擾，包括可能導致非預期操作的干擾。本裝置及其天線不得與任何其他天線或發射器位於同一位置或一起執行。**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置的安裝和執行位置與輻射體與您身體任何部位之間的距離應至少為 130 釐米。使用 CBRS 頻段時，最終主機裝置的 CBSD 類別取決於所使用的功率設定和天線增益。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>包含的 FCCID</th></tr></thead><tbody><tr><td>RBLHGR&R11e-LTE6</td><td>7442A-R11ELTE6</td></tr><tr><td>RBLHGR&R11e-LTE-US</td><td>7442A-R11ELTE</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：

-

本裝置不得造成干擾；

-

本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。本裝置中包含的免許可發射器/接收器符合加拿大創新、科學和經濟發展部適用於免許可無線電裝置的 CNR。操作須滿足以下兩個條件：

-

本裝置不得產生干擾；

-

本裝置必須接受任何無線電干擾，即使該干擾可能導致非預期操作。本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和執行位置與輻射體與您身體任何部位之間的距離應至少為 130 釐米。本裝置符合針對非受控環境規定的 IC 輻射暴露限值。本裝置應安裝並使用，且輻射體與您身體任何部位之間的距離至少為 130 釐米。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置生產日期的資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），接下來的兩位數字表示週數。

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

## 烏克蘭國家通訊和資訊領域監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭執行須按照 NKRZI 2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）所規定的程式取得執行許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型別的無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/product/lhg_lte_kit](https://mikrotik.com/product/lhg_lte_kit)

### WCDMA / LTE / 5G {#wcdma--lte--5g}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>E-GSM-900</th><th>900 MHz / 33 dBm</th></tr></thead><tbody><tr><td>DCS-1800</td><td>1800 MHz / 30 dBm</td><td></td></tr><tr><td>WCDMA Band I</td><td>1922.4 MHz / 24 dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>882.4 MHz / 24 dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1</td><td>2100 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8</td><td>900 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dBm ± 2.7 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 和 LTE 發射功率限值。有關更詳細的資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所設定的最大 WLAN 和 LTE 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置遵守 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的 WLAN 和 LTE 最大發射功率限值。更多資訊請參見上文的符合性宣告。
