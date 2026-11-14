---
title: "L14G-2ax-BT5-HL9&EG800Q（KNOT Gateway HL9）"
slug: /l14g-2ax-bt5-hl9-and-eg800q
source: https://manual.mikrotik.com/hardware/l14g-2ax-bt5-hl9-and-eg800q
captured_at: '2026-11-04T09:53:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可以下載為 <a href="/assets/files/l14g-2ax-bt5-hl9-and-eg800q-87762c8938cbe57a3dcfaa63cee67b53.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/f9479f22ec666562.webp)

![](/img/cb9a99a1b9413676.webp)

## [KNOT Gateway HL9](https://mikrotik.com/product/knot_gateway_hl)（L14G-2ax-BT5-HL9&EG800Q） {#knot-gateway-hl9-l14g-2ax-bt5-hl9eg800q}

一款堅固耐用的 IP66 IoT 閘道器，集成了 BLE 5.1、915 MHz Wi-Fi HaLow、Wi-Fi、千兆乙太網、LTE Cat 1 bis 和 GNSS。完整規格和宣傳冊請參見 [KNOT Gateway HL9 產品頁面](https://mikrotik.com/product/knot_gateway_hl)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於戶外安裝，可安裝在牆壁或立杆上。開始安裝之前，請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能會對人員造成危險情況並損壞系統。
- 僅使用製造商認可的電源和配件，這些電源和配件可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和執行時，與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>描述</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>L14G-2ax-BT5-HL9&EG800Q</td></tr><tr><td>**架構**</td><td>ARM 64 位</td></tr><tr><td>**CPU**</td><td>IPQ-5010，2 核，800 MHz</td></tr><tr><td>**RAM / 儲存**</td><td>256 MB RAM / 128 MB NAND</td></tr><tr><td>**作業系統**</td><td>RouterOS v7，許可證級別 4</td></tr><tr><td>**行動網路：LTE**</td><td>Category 1 bis（10 Mbps ↓ / 5 Mbps ↑）</td></tr><tr><td>**MIMO**</td><td>DL 1×1，UL 1×1</td></tr><tr><td>**LTE FDD 頻段**</td><td>2（1900 MHz）、4（1700 MHz）、5（850 MHz）、12（700 MHz）、13（700 MHz）、66（1700 MHz）</td></tr><tr><td>**TAC**</td><td>01688100</td></tr><tr><td>**無線**</td><td>2.4 GHz 802.11b/g/n/ax，Wi-Fi 6，1 條鏈路，287 Mbit/s，3.9 dBi</td></tr><tr><td>**Wi-Fi HaLow**</td><td>915 MHz</td></tr><tr><td>**藍牙**</td><td>5.1</td></tr><tr><td>**乙太網**</td><td>1 × 1 GbE RJ45（PoE-in 802.3af/at，18-57 V）</td></tr><tr><td>**SIM**</td><td>1 × Nano-SIM 和 eSIM</td></tr><tr><td>**電源**</td><td>PoE-in（18-57 V）或 2 針端子（12-57 V），最大 7 W</td></tr><tr><td>**散熱**</td><td>被動散熱</td></tr><tr><td>**尺寸**</td><td>254 × 88 × 57 mm</td></tr><tr><td>**工作溫度**</td><td>–40 °C … +50 °C</td></tr><tr><td>**MTBF**</td><td>25 °C 下約 200,000 小時</td></tr><tr><td>**認證**</td><td>FCC、IC、EAC</td></tr><tr><td>**IP**</td><td>IP66</td></tr></tbody></table>

## 快速開始 {#quickstart}

- 確保您的網際網路服務提供商（ISP）允許硬體更換並自動分配 IP 地址；
- 將 ISP 網線連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 之外的任意埠，或無線網路 "MikroTik-..." 連線到裝置（在標籤上檢視無線密碼）；
- 使用移動應用程式建立連線。或者，使用網頁瀏覽器中的 **WebFig**，或使用 **WinBox** 配置工具，地址為 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在所選的工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請在標籤上檢視使用者名稱和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 Quick Set 的 WISP AP 選單中，選擇您所在的國家/地區以應用國家法規設定；
- 設定您的無線網路密碼；
- 設定您的路由器密碼。

## 安裝 {#mounting}

該裝置專為戶外使用而設計，可安裝在牆壁或立杆上。

### 將裝置安裝到牆壁上 {#to-mount-the-device-on-the-wall}

- 在裝置背面與安裝點對應的位置鑽 6 mm 的孔，包括用於安全/鎖定點的額外孔；
- 將螺絲插入膨脹螺栓中，使螺帽露出約 10 mm；

![](/img/f6d85d25026306b6.png)

- 放置裝置並將其與安裝點對齊；

![](/img/b60aa64414031dce.png)

- 擰緊螺絲，將裝置固定到牆上。

![](/img/553b3983a5a2daf1.png)

![](/img/88b12c8ab64bceb3.png)

### 將裝置安裝到立杆上 {#to-mount-the-device-on-a-pole}

- 將軟管卡箍穿過安裝支架上的孔；
- 將裝置靠在立杆上，並把卡箍繞在立杆上；
- 擰緊卡箍，將裝置牢固地固定到位。

![](/img/1090de71679314c2.png)

:::warning warning

本裝置安裝和執行時，裝置與人體之間應保持至少 20 cm 的最小距離。在住宅環境中操作本裝置可能會造成無線電干擾。

本裝置的安裝和配置應由合格人員進行。

:::

## 供電 {#powering}

- 2 針端子支援 12-57 V DC⎓；
- 乙太網埠支援 802.3af/at Power over Ethernet 18-57 V DC。

最大功耗可達 7 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將一根乙太網線從裝置連線到 PoE 介面卡的 **PoE + DATA** 埠；
- 將一根乙太網線從您的本地網路（LAN）連線到 PoE 介面卡的 **DATA** 埠；
- 將電源線連線到介面卡，然後將其插入電源插座。

## 蜂窩調變解調器配置 {#cellular-modem-configuration}

子選單：/interface lte

有關頻段選擇、漫遊或高階選項，請參閱 [LTE/5G 手冊](/docs/mobile-networking/lte-5g)。

## 重設按鈕 {#reset-button}

重設按鈕有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住重設按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS 時，需使裝置進入 BOOTP 模式。有兩個 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議對這兩個選項都進行驗證，以防其中一個無法使用。

- **Regular Booter:** 要進入 etherboot 模式，請在給裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter:** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備好透過 **Netinstall** 重新安裝 RouterOS。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的配件：

- KNOT Gateway HL9。
- 24 V、0.5 A 電源介面卡。
- 千兆 PoE 注入器。
- K-66 緊固套件。
- 軟管卡箍（2 個）。

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。
