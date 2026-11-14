---
title: "L14G-2ax-BT5-LR8&EG800K（KNOT 閘道器 LR8）"
slug: /l14g-2ax-bt5-lr8-and-eg800k
source: https://manual.mikrotik.com/hardware/l14g-2ax-bt5-lr8-and-eg800k
captured_at: '2026-11-04T09:53:06+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可以下載為 <a href="/assets/files/l14g-2ax-bt5-lr8-and-eg800k-ec6d57bb0b77794ca044e26fe7be0500.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/f9479f22ec666562.webp)

![](/img/cb9a99a1b9413676.webp)

## [KNOT 閘道器 LR8](https://mikrotik.com/product/knot_gateway_lr8)（L14G-2ax-BT5-LR8&EG800K） {#knot-gateway-lr8-l14g-2ax-bt5-lr8eg800k}

KNOT Gateway LR8——隨處可用的連線能力。最初為咖啡機和自動售貨機而設計——非常適合各類工業自動化場景。完整規格和宣傳冊請參見 [KNOT Gateway LR8 產品頁面](https://mikrotik.com/product/knot_gateway_lr8)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適合安裝在戶外的牆壁或立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或不遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 只能使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或普通公眾的距離不得小於 20 釐米。

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>描述</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>L14G-2ax-BT5-LR8&EG800K</td></tr><tr><td>**架構**</td><td>ARM 64 位</td></tr><tr><td>**CPU**</td><td>IPQ-5010，2 核，800 MHz</td></tr><tr><td>**RAM / 儲存**</td><td>256 MB RAM / 128 MB NAND</td></tr><tr><td>**作業系統**</td><td>RouterOS v7，許可證級別 4</td></tr><tr><td>**行動網路：LTE**</td><td>Category 1 bis（10 Mbps ↓ / 5 Mbps ↑）</td></tr><tr><td>**MIMO**</td><td>DL 1×1，UL 1×1</td></tr><tr><td>**LTE FDD 頻段**</td><td>1（2100 MHz）、3（1800 MHz）、5（850 MHz）、7（2600 MHz）、8（900 MHz）、20（800 MHz）、28（700 MHz）</td></tr><tr><td>**TAC**</td><td>86684606</td></tr><tr><td>**無線**</td><td>2.4 GHz 802.11b/g/n/ax，Wi-Fi 6，1 條鏈路，287 Mbit/s，3.9 dBi</td></tr><tr><td>**藍牙**</td><td>5.1</td></tr><tr><td>**乙太網**</td><td>1 × 1 GbE RJ45（PoE-in 802.3af/at，18-57 V）</td></tr><tr><td>**SIM**</td><td>1 × Nano-SIM & eSIM</td></tr><tr><td>**電源**</td><td>PoE-in（18-57 V）或 2 針端子（12-57 V），最大 9 W</td></tr><tr><td>**散熱**</td><td>被動散熱</td></tr><tr><td>**尺寸**</td><td>254 × 88 × 57 mm</td></tr><tr><td>**工作溫度**</td><td>–40 °C … +50 °C</td></tr><tr><td>**MTBF**</td><td>25 °C 下約 200,000 小時</td></tr><tr><td>**IP**</td><td>IP66</td></tr></tbody></table>

## 快速開始 {#quickstart}

- 確保您的網際網路服務提供商（ISP）允許更換硬體並自動分配 IP 地址；
- 將 ISP 網線連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 之外的任一埠，或無線網路"MikroTik-..."（無線密碼請檢視標籤）連線到裝置；
- 使用移動應用程式建立連線。也可以使用網頁瀏覽器中的 **WebFig**，或 [https://mt.lv/winbox](https://mt.lv/winbox) 上的 **WinBox** 配置工具。**提供了多種配置方式以確保可訪問性；**
- 使用預設 IP 地址 192.168.88.1 在所選工具中開始配置。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視標籤上的使用者名稱和無線密碼）；
- 點選 "Check for updates" 按鈕，並將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 Quick Set 的 WISP AP 選單中，選擇您所在的國家/地區以應用國家/地區法規設定；
- 設定您的無線網路密碼；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置為戶外使用而設計，可安裝在牆壁或立杆上。

### 將裝置安裝到牆上 {#to-mount-the-device-on-the-wall}

- 按照裝置背面的安裝孔位鑽 6 mm 的孔，包括用於安全/鎖定點的額外孔位；
- 將螺絲插入膨脹錨栓，使螺絲頭露出約 10 mm；

![](/img/f6d85d25026306b6.png)

- 放置裝置並將其與安裝孔位對齊；

![](/img/b60aa64414031dce.png)

- 擰緊螺絲，將裝置固定到牆上。

![](/img/553b3983a5a2daf1.png)

![](/img/88b12c8ab64bceb3.png)

### 將裝置安裝到立杆上 {#to-mount-the-device-on-a-pole}

- 將軟管卡箍穿過安裝支架上的孔；
- 將裝置靠在立杆上，並將卡箍繞過立杆；
- 擰緊卡箍，將裝置牢固固定到位。

![](/img/1090de71679314c2.png)

:::warning warning

本裝置的安裝和執行應使裝置與您的身體之間保持至少 20 釐米的距離。在居住環境中操作本裝置可能會造成無線電干擾。

本裝置的安裝和配置應由具備資質的人員完成。

:::

## 供電 {#powering}

- 2 針端子支援 12-57 V DC⎓；
- 乙太網埠支援 802.3af/at Power over Ethernet 18-57 V DC。

最大功耗可達 9 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置上的乙太網線連線到 PoE 介面卡的 **PoE + DATA** 埠；
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡的 **DATA** 埠；
- 將電源線連線到介面卡，然後插入電源插座。

## 蜂窩調變解調器配置 {#cellular-modem-configuration}

子選單：/interface lte

有關頻段選擇、漫遊或高階選項，請參閱 [LTE/5G 手冊](/docs/mobile-networking/lte-5g)。

## 復位按鈕 {#reset-button}

復位按鈕有三個功能：

- 在啟動過程中按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可復位 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 常亮，然後鬆開即可啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 工具重新安裝 RouterOS，請使裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議在其中一個無法工作時對兩個選項都進行驗證。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電後等待 1–2 秒再按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

- KNOT Gateway LR8。
- 24 V、0.5 A 電源介面卡。
- 千兆 PoE 注入器。
- K-66 固定套件。
- 軟管卡箍（2 個）。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統未經測試。
