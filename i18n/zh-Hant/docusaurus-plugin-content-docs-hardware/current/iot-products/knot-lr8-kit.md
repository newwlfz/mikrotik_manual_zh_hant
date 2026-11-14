---
title: "KNOT LR8 套件"
slug: /knot-lr8-kit
source: https://manual.mikrotik.com/hardware/knot-lr8-kit
captured_at: '2026-11-04T09:52:08+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可以下載為 <a href="/assets/files/knot-lr8-kit-14575ab2838632fcb5f7fa7175683a56.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/7955d232dcd19d10.webp)

### [KNOT LR8 kit](https://mikrotik.com/product/knot_lr8) (RB924iR-2nD-BT5&BG77&R11e-LR8) {#knot-lr8-kit-rb924ir-2nd-bt5bg77r11e-lr8}

適用於最靈活多樣且經濟高效的部署的 IoT 閘道器。有關完整規格和宣傳冊，請參閱 [KNOT LR8 kit 產品頁面](https://mikrotik.com/product/knot_lr8)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計為安裝在 35 mm DIN 導軌上或壁掛安裝。開始安裝前請仔細閱讀安裝說明。使用不正確的硬體或不遵循正確的操作流程，可能會對人員造成危險並損壞系統。
- 本產品僅適合室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 只能使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作應與您的身體、職業使用者或普通公眾保持不少於 20 釐米的距離。

## 快速開始 {#quickstart}

- 確保您的網際網路服務提供商允許更換硬體，並會自動分配 IP 地址；
- 將 ISP 線纜連線到第一個乙太網埠；
- 將裝置連線到電源；
- 開啟計算機上的網路連線部分，找到名為 "MikroTik-…" 的無線網路。連線到它（請檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用 WinBox 配置工具：[https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方法以確保可訪問性；**
- 使用預設 IP 地址 192.168.88.1，用所選工具開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 Neighbors 標籤頁來查詢裝置；
- 使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者密碼和無線密碼）；
- 單擊 Check for updates 按鈕，將 RouterOS 更新到最新版本。
- 如需手動更新，請訪問 mikrotik.com，選擇您的型號，並從 Downloads 部分下載所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 Files 選單，然後重啟裝置；
- 透過將 RouterOS 升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 Quick Set → WISP AP 選單中，選擇您所在的國家/地區以應用相應的法規設定；
- 設定您的無線網路密碼；
- 設定您的路由器密碼。

*包裝中不包含 U.FL 轉 SMA 饋線和外接藍牙天線。*

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>描述</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>RB924iR-2nD-BT5&BG77&R11e-LR8</td></tr><tr><td>**架構**</td><td>MIPSBE</td></tr><tr><td>**CPU**</td><td>QCA9531，1 核，650 MHz</td></tr><tr><td>**RAM**</td><td>64 MB</td></tr><tr><td>**儲存**</td><td>128 MB NAND</td></tr><tr><td>**RouterOS 許可證**</td><td>4</td></tr><tr><td>**作業系統**</td><td>RouterOS v7</td></tr><tr><td>**乙太網**</td><td>2 × 10/100 (Auto MDI/X)</td></tr><tr><td>**PoE 輸入**</td><td>802.3af/at, 12–57 V DC</td></tr><tr><td>**PoE 輸出**</td><td>Ether2，無源 PoE 最高 57 V</td></tr><tr><td>**最大功耗**</td><td>20 W</td></tr><tr><td>**無線 2.4 GHz**</td><td>802.11b/g/n, 2×2, 1.5 dBi</td></tr><tr><td>**藍牙**</td><td>5.2</td></tr><tr><td>**USB**</td><td>1 × microUSB (type AB)</td></tr><tr><td>**SIM**</td><td>1 × nano-SIM</td></tr><tr><td>**序列**</td><td>RS485</td></tr><tr><td>**LoRa 卡**</td><td>R11e-LR8, 863–870 MHz (EU), 14 dBm, Class A/C</td></tr><tr><td>**尺寸**</td><td>122 × 87 × 26 mm</td></tr><tr><td>**工作溫度**</td><td>−40 °C … +70 °C</td></tr><tr><td>**IP 防護等級**</td><td>IP20</td></tr><tr><td>**MTBF**</td><td>≈ 100 000 h @ 25 °C</td></tr><tr><td>**認證**</td><td>CE, FCC, IC, EAC, RoHS</td></tr></tbody></table>

## 安裝 {#mounting}

![](/img/60a25f0b55a2a55d.webp)

- 可使用隨附的 DIN 導軌安裝套件安裝本裝置。設計適配標準 35 mm x 7.5 mm DIN 導軌。使用隨附的兩顆螺絲將其固定到裝置上，然後將裝置安裝到 DIN 導軌上。包裝中不包含 DIN 導軌。
- 或者，可使用裝置背面的螺孔將裝置安裝到牆上。裝置的安裝方式應使線纜開口朝下，如圖所示。**警告：** 本裝置的安裝和操作應與身體保持至少 20 釐米的距離。在住宅環境中操作本裝置可能會造成無線電干擾。本裝置的安裝和配置應由合格人員完成。

## 供電 {#powering}

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2.1 mm，母頭，中心正極插頭）可接受 12-57 V DC。
- microUSB 埠接受 5 V 供電。
- 乙太網埠接受 802.3af/at 乙太網供電 12-57 V DC。
- 在帶附件的情況下，最大負載下的功耗可達 20 W。
- 連線到 PoE 介面卡：

- 將裝置上的乙太網線纜連線到 PoE 介面卡的 PoE+DATA 埠。
- 將乙太網線纜從您的本地網路（LAN）連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/46b18e887e695663.webp)

- 2.4 GHz，802.11b/g/n，天線增益 1.5 dBi。
- 內建 GPS 模組（GPS、GLONASS、BeiDou、Galileo），適用於 KNOT、KNOT LR8 和 KNOT LR9。KNOT LR8G/9G 的 LR 卡內部帶有 GPS 模組（不支援 GLONASS、BeiDou、Galileo）。
- 兩個 10/100 乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X）。連線其他網路裝置時可以使用直通或交叉線纜。乙太網埠可透過 802.3af/at PoE 注入器接受 12-57 V DC 電源。
- 一個 microUSB 2.0 埠用於供電（對於 KNOT LR8/LR8G 和 KNOT LR9/LR9G 套件，該埠也可用於外設）。
- 一個 nano SIM 插槽。
- 藍牙版本 5.2，天線增益 2 dBi。

**KNOT LR8 kit：**

- LR8 卡。

## Modbus {#modbus}

KNOT 的 Modbus 配置指南。

## Bluetooth 天線 {#bluetooth-antenna}

預設情況下，KNOT 具有可使用的內建天線，但也可以改為連線外接天線以增加藍牙工作範圍。這適用於 KNOT RB924i-2nD-BT5&BG77 裝置。

對於 KNOT LR8 kit、KNOT LR8G kit、KNOT LR9 kit 和 KNOT LR9G kit，藍牙外接天線饋線預留位**不可用**（此處已有一個由 LoRa 使用的 SMA 插槽）。

要使用外接天線，您需要一個 U.FL (female) 轉 SMA 聯結器（pigtail）以及一個 Bluetooth 天線（可連線到 SMA）。

![](/img/fdb0c8a7e4b9a21f.webp)

- 擰下 CAT-M/NB 和 GNSS 兩個 SMA 插槽之間的螺絲，並取下外殼。
- 將 U.FL（母頭）饋線連線到板上的 BT 插槽（如上圖所示）。
- 按圖示在外殼的特定位置（外殼內側的圓形輪廓）鑽孔，並將 SMA 固定到外殼上（鑽孔處）。
- 將藍牙天線連線到 SMA 插槽。您需要在 RouterOS 設定中更改要使用的天線（新連線的"外接"或內建的"內建"）（位於 IoT→ Bluetooth→Devices→雙擊藍牙介面→ 在 Antenna 欄位中）：

![](/img/0b9b0fd9fbf0ff90.webp)

包裝中不包含 U.FL 轉 SMA 饋線和外接藍牙天線。

## GPS 與 NB/CAT-M {#gps-and-nbcat-m}

將您的天線連線到 SMA 聯結器：

![](/img/fa4fa700c587500b.webp)

BG77 支援 NB 和 GNSS。對於 KNOT、KNOT LR8 和 KNOT LR9 kit，兩者（NB+GNSS）不能同時使用。

下面在**蜂窩與 GNSS 優先順序切換自動化**一節中給出了自動切換蜂窩和 GNSS 優先順序配置的示例。另請檢視 [WWAN 和 GNSS 優先順序自動化](/docs/mobile-networking/bg77-modem-at-commands/wwan-and-gnss-priority-automatization) 指南。

必須連線外部天線才能使用窄帶調變解調器和 GPS。包裝中不提供。

名為 "modem" 的埠用於蜂窩連線（序列/PPP 連線）和 GNSS NMEA 資料：

```
/port print
Flags: I - INACTIVE
Columns: DEVICE, NAME, CHANNELS, USED-BY, BAUD-RATE
#   DEVICE  NAME    CHANNELS  USED-BY  BAUD-RATE
0           modbus         1                9600
1   1-1.4   modem          5              115200

```

預設調變解調器埠通道分配：

1 - GNSS NMEA 輸出埠；

2 - AT/modem 埠；

4 - AUX AT/modem 埠 - 最大頻寬 115200bps，僅適用於 KNOT LoRa 套件和帶內部 USB 集線器的 KNOT。

### 蜂窩調變解調器配置 {#cellular-modem-configuration}

與 LTE 裝置不同，KNOT BG77 預設不提供直接的 IP 調變解調器介面（LTE 介面），而是提供用於序列/PPP 連線的 AT/modem 序列埠。

BG77 調變解調器 AT 命令可在 [BG77 AT 命令手冊](https://mikrotik.com/product/knot#tab0) 中找到。

KNOT 預設具有 serial/PPP 連線預設：

```
/interface ppp-client print
Flags: X - disabled; R - running
 0 R  name="ppp-out1" max-mtu=1500 max-mru=1500 mrru=disabled port=modem data-channel=2 info-channel=4 apn="internet"
      pin="" user="" password="" profile=default phone="" dial-command="ATDT" modem-init="AT+QGPSCFG="priority",1"
      null-modem=no dial-on-demand=yes add-default-route=yes default-route-distance=1 use-peer-dns=yes keepalive-timeout=30
      allow=pap,chap,mschap1,mschap2

```

有關調變解調器埠配置的更多詳細資訊，請參閱上面的 KNOT 埠配置/對映。

有關 serial/PPP 連線的更多詳細資訊，請檢視 [PPP Client](/docs/mobile-networking/ppp) 文件。

### GNSS 配置 {#gnss-configuration}

您可以檢視 GNSS 配置指南以獲取更多資訊。

BG77 調變解調器為 IoT 蜂窩連線和 GNSS 訊號接收共用同一個接收器。可以透過 **modem-init** 字串（在 /interface ppp-client 下配置）和 GNSS 服務的 **init-string**（在 /system gps 下配置）來設定優先使用的服務。

AT 命令為：

AT+QGPSCFG="priority",0 → 優先使用 GNSS；AT+QGPSCFG="priority",1 → 優先使用蜂窩 IoT 連線；

AT+QGPSEND → 停止 GNSS 接收；AT+QGPS=1 → 啟動 GNSS 接收。

此外，還可以藉助 AT 命令配置支援的 GNSS 星座：

AT+QGPSCFG="gnssconfig"[,&lt;GNSS_config&gt;]

，該命令僅在模組重啟後生效，其中 &lt;GNSS_config&gt; 代表星座本身（可為 "1" 到 "5"）：

- 1 → GPS + GLONASS
- 2 → GPS + BeiDou
- 3 → GPS + Galileo
- 4 → GPS + QZSS
- 5 → 可變 - 根據所駐留網路的 MCC 從選項（1–4）中選擇一個

### 蜂窩調變解調器韌體升級 {#cellular-modem-firmware-upgrade}

請注意：

- 可以使用任何網際網路連線（包括 Wi-Fi 和乙太網上行鏈路）進行 DFOTA 韌體檢查/升級。因此，即使 BG77 沒有蜂窩連線（例如僅用作 GPS 接收器），也可以升級其調變解調器韌體。
- 當 BG77 調變解調器的序列/PPP 介面使用主 AT/modem 通道（data-channel=2）時，支援韌體升級。要檢視當前安裝的 BG77 韌體版本，請使用以下命令指定 "upgrade=no" 引數：

```
/interface/ppp-client/firmware-upgrade ppp-out1 upgrade=no
  installed: BG77LAR02A04_01.001.01.001
     latest: BG77LAR02A04_01.009.01.009

```

要更新 BG77 調變解調器韌體，請設定引數 "upgrade=yes"：

```
/interface/ppp-client/firmware-upgrade ppp-out1 upgrade=yes

```

### 蜂窩與 GNSS 優先順序切換自動化 {#cellular-and-gnss-priority-switch-automation}

可以使用 ppp 配置檔案的 **on-down** 指令碼、**idle-timeout** 功能以及 PPP 介面的 **dial on demand** 設定來實現自動化。

實施後，當存在網際網路流量時，BG77 調變解調器將使用蜂窩資料（在此期間不會收到 GNSS 座標），而當未檢測到網際網路流量時，將自動啟用 GPS 接收。

**Idle-timeout** 引數指定在沒有活動的情況下，鏈路將在多長時間後終止。

**On-down** 指令碼欄位允許你配置一個指令碼，該指令碼將在每次 PPP 介面關閉時執行（包括在 **idle-timeout** 不活動之後）。該指令碼會將調變解調器的優先順序設定為 GNSS 接收。

**Dial-on-demand** 將確保 PPP 介面僅在存在出站流量時嘗試建立連線（此外，調變解調器將自動設定 WWAN/蜂窩連線優先順序）。這將確保在發生 **idle-timeout** 後，除非檢測到出站封包，否則連線不會自動重新建立。

透過組合這三個功能，你可以實現以下場景：

- 如果有出站流量，PPP 介面將處於執行狀態（由於 **dial on demand**），並且優先順序將設定為蜂窩連線。此時會發送 PPP 介面用於 WWAN 優先順序的調變解調器初始化 AT 命令（該命令配置在 PPP 介面的 modem-init="AT+QGPSCFG=\"priority\",1" 設定中）。在此期間，不會接收 GPS 座標。
- 如果在 **idle-timeout** 無活動視窗之後檢測不到流量，PPP 介面將斷開，並且由於 **dial on demand** 設定，在檢測到出站封包之前不會建立連線。此時會執行 **on-down** 指令碼，將 WWAN 優先順序切換為 GNSS 優先順序。要實現這一點，只需新增一個新的 PPP 配置檔案：

```
/ppp profile add idle-timeout=30s name=BG77 on-down="/interface ppp-client at-chat [find where modem-init=\"AT+QGPSCFG=\\\"priority\\\",1\"] input=\"AT+QGPSCFG=\\\"priority\\\",0\""

```

上面的示例建立了一個名為 "BG77" 的新配置檔案，將 **idle-timeout** 設定為 30 秒，並啟用 **on-down** 指令碼，該指令碼將傳送 GNSS 優先順序 AT 命令。

之後，請確保將此新建立的配置檔案應用到 PPP 介面：

```
/interface ppp-client set [find] profile=BG77

```

並確認它已應用（profile=BG77）：

```
/interface ppp-client print
Flags: X - disabled; R - running
0 R name="ppp-out1" max-mtu=1500 max-mru=1500 mrru=disabled port=modem data-channel=2 info-channel=2
apn="internet" pin="" user="" password="" profile=BG77 phone="" dial-command="ATDT"
modem-init="AT+QGPSCFG="priority",1" null-modem=no dial-on-demand=yes add-default-route=yes
default-route-distance=1 use-peer-dns=yes keepalive-timeout=30 allow=pap,chap,mschap1,mschap2

```

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請將裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議在其中一個不起作用時驗證兩個選項。

- **Regular Booter:** 要進入 etherboot 模式，請在給裝置通電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter:** 關閉裝置。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，可透過 Netinstall 重新安裝 RouterOS。視型號而定，這可能由 **USR, USER, System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## GPIO 引腳排列 {#gpio-pinout}

GPIO 引腳位於外殼下方的電路板上，如圖所示：

![](/img/aa56f6a091950f7a.webp)

ADC 輸入/模擬輸入（pin2 或 pin3）：

![](/img/0201b8beb9b054ef.webp)

**注意：** *模擬輸入電壓為 0-60 V。理論解析度為 4 mV（14 位 ADC）。模擬輸入阻抗約為 72K 歐姆。*

已連線的繼電器（pin4 或 pin6）：

![](/img/4b8f177a2150596d.webp)

*注意：最大功耗（對於數字輸出開漏電晶體）為 0.48 W。建議在持續執行期間不要超過 24V 或 0.5A。絕對最大漏源電壓為 30V，最大電流為 2.8A。*

![](/img/4c01507e5fd17337.webp)

*GPIO 輸出為開漏配置。**邏輯狀態 "0"**（電晶體開路狀態）使輸出電晶體處於低阻狀態，輸出約為 0V。**邏輯狀態 "1"**（電晶體閉合狀態）使輸出電晶體處於高阻狀態，輸出電壓取決於外部電路。*

防拆開關（pin5）：

![](/img/597abb74d2c7dc9c.webp)

**注意：** *數字輸入電壓最大為 0-2.5 V。*

*無 PCB 上拉電阻：*

-

*要在引腳上獲得邏輯 "0"，電壓應在 0-1.47 V 之間；*

-

*要在引腳上收到邏輯 "1"，電壓應在 1.48-2.5 V 之間。* *使用 PCB 上拉電阻時：*

-

*要在引腳上收到邏輯 "0"，電壓應在 0-1.34 V 之間；*

-

*要在引腳上收到邏輯 "1"，電壓應在 1.35-2.5 V 之間。* *較新的 routerboard 將在 PCB（板上）上帶有 10k ohm 上拉電阻。較舊的板（首批發布批次）可能需要外部上拉電阻。*

## 配件 {#accessories}

包裝中包含以下隨裝置附帶的配件：

- ADAPT1_ 歐盟/美國開關電源 24V，1.2A，28.8W，86.8%，VI。
- CAB1_ USB A 母頭轉 Micro B 線纜。
- SET1_ K-47 壁掛安裝套件、兩顆螺絲和膨脹螺栓。
- SET2_ K-74 DIN 導軌安裝套件。
- Modbus 聯結器，A+、B-。

HGO-LTE-W 天線可單獨購買。

![](/img/90314e3eea2eb9bb.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

## 配置 {#configuration}

除了本文件中所述的內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始，以熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help)。如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下會阻止來自網際網路埠的所有訪問）。出於恢復目的，可以從網路引導裝置，請參閱 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 文件。

**注意：** 請確保事先安裝了 **iot** 軟體包。

如果您擁有 LR8 或 LR9 KNOT 變體，並且有興趣使用 LoRa 協定，請點選我們的 LoRa 指南。

要檢視其他 IoT 功能，請訪問 IoT 頁面。

## 概述 {#overview}

MQTT 和 HTTP 等協定被廣泛用於在 M2M 網路內推送資料。M2M 拓撲可以使用不同的技術（例如 Wi-Fi 或藍牙）在網路內傳送資料。

KNOT 是我們 IoT 解決方案系列中的新成員。KNOT 充當 IoT 閘道器（使用窄帶和 CAT-M 技術），並使用藍牙掃描廣播資訊。藉助藍牙介面，您可以將 KNOT 用於基於藍牙廣播封包的資產跟蹤和遙測。KNOT 支援任何傳送廣播資料的 BLE 標籤。iBeacon、Eddystone 或任何其他格式。它具有強大的過濾器，僅轉發相關封包而忽略其他封包。閘道器處理收到的資料後，可以使用 ISP 連線將資料進一步釋出到任何已相應配置的訂閱者或伺服器。

您需要做的只是配置一個指令碼。該指令碼可以過濾廣播資訊並將其推送到網際網路。

本文介紹如何配置 KNOT 以使用 MQTT 或 http 協定釋出資料。

必須連線外部天線才能使用窄帶調變解調器和 GPS。包裝中不提供。

## 報告 {#reports}

導航到 IoT &gt; Bluetooth。

您可以在 Advertising reports 標籤頁中找到所有廣播裝置。

![](/img/4ee647301a86eb0c.webp)

在此選單中，您可以按下 Filter 圖示來設定過濾器。例如，如果知道裝置的 MAC 地址，您可以設定過濾器以僅顯示特定的報告。

![](/img/bf2032dfd2080349.webp)

您可以使用 + 圖示新增更多過濾器選項。

您可以使用 - 圖示移除篩選選項。

## MQTT Broker 配置 {#mqtt-broker-configuration}

導航到 IoT &gt; MQTT。

您可以透過 + 按鈕新增新的 broker。

![](/img/1a3a89d9fc694e82.webp)

<table><thead><tr><th>屬性</th><th>描述</th></tr></thead><tbody><tr><td>Name</td><td>標識。broker 的名稱。</td></tr><tr><td>Address</td><td>MQTT broker 的 IP 地址或 FQDN 名稱，不帶 ssl:// 或 tcp:// 字首。</td></tr><tr><td>Port</td><td>broker 的網路埠。通常為 1883 或 8883（用於 SSL）。</td></tr><tr><td>SSL</td><td>啟用/停用 Secure Socket Layer。如果伺服器使用自簽名證書或由不受信任的 CA 簽名的證書，您必須將伺服器的證書 &lt;crt&gt; 檔案上傳到 RouterOS。將 .cer 檔案上傳到 Files 選單，並將該檔案匯入到 System&gt;Certificates 標籤頁中的證書中。</td></tr><tr><td>Username</td><td>MQTT broker 的使用者名稱。</td></tr><tr><td>Password</td><td>MQTT broker 的密碼。</td></tr><tr><td>Client Id</td><td>用於連線的唯一 ID。broker 使用此 ID 來識別用戶端。</td></tr><tr><td>Certificate</td><td>如果雙向認證需要，請選擇證書。</td></tr></tbody></table>

**注意：** 您不必在 MQTT broker 設定中指定伺服器證書（.cer 檔案）。Certificate 欄位用於用戶端證書。

**注意：** Name、Address 和 Port 欄位配置是必需的。其他引數可以是可選的或必需的 - 取決於伺服器/broker 的設定方式。

## 釋出 {#publish}

建立 broker 後，單擊 Publish 按鈕。此框允許您選擇 broker 並指定訊息資訊。

![](/img/d3b62757ecbe08c5.webp)

在 Broker 欄位（下拉選單）中選擇已配置的 broker。

然後您可以指定 Topic（broker 用於過濾訊息的字串）、Message（訊息本身）、QoS（指示訊息的服務質量級別）和 Retain（是保留還是丟棄訊息）引數。

**注意：** Broker 和 Topic 欄位配置是必需的。Message、QoS 和 Retain 可以是可選的或必需的 - 取決於伺服器/broker 的設定方式。

## MQTT 與指令碼場景 {#mqtt-with-script-scenario}

可以使用指令碼配置 MQTT broker。

建立一個新指令碼，以模板作為參考，相應地更改引數並執行指令碼。

每一行以符號 "**#**" 開頭的都是說明性內容，它描述將在該行下方配置的引數。請更改引號 "" 內適用於您具體情況的引數。

指令碼示例：

```
## Required packages: iot

################################ Configuration ################################
## Name of an existing MQTT broker that should be used for publishing
:local broker "Demo Device"

## MQTT topic where the message should be published
:local topic "v1/devices/me/telemetry"

## Interface whose MAC should be used as 'Locator ID'
:local locatorIface "ether1"

## POSIX regex for filtering advertisement Bluetooth addresses. E.g. "^BC:33:AC"
## would only include addresses which start with those 3 octets.
## To disable this filter, set it to ""
:local addressRegex ""

## POSIX regex for filtering Bluetooth advertisements based on their data. Same
## usage as with 'addressRegex'.
:local advertisingDataRegex ""

## Signal strength filter. E.g. -40 would only include Bluetooth advertisements
## whose signal strength is stronger than -40dBm.
## To disable this filter, set it to ""
:local rssiThreshold ""

#################################### System ###################################
:put ("[*] Gathering system info...")
:local ifaceMac [/interface get [/interface find name=$locatorIface] mac-address]
:local cpuLoad [/system resource get cpu-load]
:local freeMemory [/system resource get free-memory]
:local usedMemory ([/system resource get total-memory] - $freeMemory)
:local rosVersion [/system package get value-name=version \
    [/system package find where name ~ "^routeros"]]
:local model [/system routerboard get value-name=model]
:local serialNumber [/system routerboard get value-name=serial-number]
## Health is a bit iffy since '/system health' does not have 'find' in ROS6
:local health [/system health print as-value]
:local supplyVoltage 0
:local boardTemp 0
:foreach entry in=$health do={
    :if ($entry->"name" = "voltage") do={:set $supplyVoltage ($entry->"value")}
    :if ($entry->"name" = "board-temperature1") do={:set $boardTemp ($entry->"value")}
}

################################## Bluetooth ##################################
:put ("[*] Gathering Bluetooth info...")
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # First time this script has been run since booting, need to initialize
    # persistent variables
    :set $btOldestAdvertisementTimestamp 0
}
:local btProcessingStart [/system clock get time]
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex and \
        data ~ $advertisingDataRegex and \
        rssi > $rssiThreshold]
:local advJson ""
:local advCount 0
:local advSeparator ""
:local lastAdvTimestamp 0
## Remove semicolons from MAC/Bluetooth addresses
:local minimizeMac do={
    :local minimized
    :local lastIdx ([:len $address] - 1)
    :for idx from=0 to=$lastIdx step=1 do={
        :local char [:pick $address $idx]
        :if ($char != ":") do={
            :set $minimized "$minimized$char"
        }
    }
    :return $minimized
}

:foreach adv in=$advertisements do={
    :local address ($adv->"address")
    :local ts ($adv->"epoch")
    :local rssi ($adv->"rssi")
    :local ad ($adv->"data")
    :local obj "\
        {\
            \"id\":\"$[$minimizeMac address=$address]\",\
            \"ts\":$ts,\
            \"rssi\":$rssi,\
            \"ed\":{\
                \"ad\":\"$ad\"\
            }\
        }"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $ts
    # Ensure that the last object is not terminated by a comma
    :set $advJson "$advJson$advSeparator$obj"
    :if ($advSeparator = "") do={
        :set $advSeparator ","
    }
}

:if ($advCount > 0) do={

    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp

}

:put ("[*] Found $advCount new advertisements \
    (processing time: $[([/system clock get time] - $btProcessingStart)])")

#################################### MQTT #####################################
:local message \
    "{\
        \"clientId\":\"$[/iot mqtt brokers get value-name=client-id \
            [/iot mqtt brokers find name=$broker]]\",\
        \"t\":0,\
        \"v\":1,\
        \"OldestAdvertisementTimestamp\":$btOldestAdvertisementTimestamp,\
        \"locs\":[{\
            \"id\":\"$[$minimizeMac address=$ifaceMac]\",\
            \"tags\":[$advJson],\
            \"ed\":{\
                \"model\":\"$model\",\
                \"sn\":\"$serialNumber\",\
                \"ros\":\"$rosVersion\",\
                \"cpu\":$cpuLoad,\
                \"umem\":$usedMemory,\
                \"fmem\":$freeMemory,\
                \"psu\":$supplyVoltage,\
                \"temp\":$boardTemp\
            }\
        }]\
    }"
:log info "$message";
:put ("[*] Total message size: $[:len $message] bytes")
:put ("[*] Sending message to MQTT broker...")
/iot mqtt publish broker=$broker topic=$topic message=$message
:put ("[*] Done")

```

要執行此指令碼，Broker 應預先配置：

![](/img/ce0edf2496617c43.webp)

例如，thingsboard 只需要上面截圖中顯示的設定。成功配置 broker 後，指令碼中唯一需要更改的是：

```
:local broker "Demo Device"

```

行，你應在引號 "" 內指定 broker 的名稱。

另一個需要考慮的行是：

```
:local topic "v1/devices/me/telemetry"

```

，您應在其中指定 topic。

指令碼配置的其餘部分取決於整體需求。指令碼中說明了配置了哪些確切引數用於釋出。

導航到 System &gt; Scripts，並在那裡新增新指令碼（為其命名，例如 script1）。

要執行指令碼，您可以使用命令列：

/system script run script1

## HTTP fetch 與指令碼場景 {#http-fetch-with-script-scenario}

釋出資料的另一種方式是使用 HTTP（而不是 MQTT）。這可以使用 fetch 工具實現。

同樣的原則適用：

建立一個新指令碼，以模板作為參考，相應地更改引數並執行指令碼。

每一行以符號 "**#**" 開頭的都是說明性內容，它描述將在該行下方配置的引數。請更改引號 "" 內適用於您具體情況的引數。

指令碼示例：

```
## Required packages: iot

################################ Configuration ################################
## Interface whose MAC should be used as 'Locator ID'
:local locatorIface "ether1"

## POSIX regex for filtering advertisement Bluetooth addresses. E.g. "^BC:33:AC"
## would only include addresses which start with those 3 octets.
## To disable this filter, set it to ""
:local addressRegex ""

## POSIX regex for filtering Bluetooth advertisements based on their data. Same
## usage as with 'addressRegex'.
:local advertisingDataRegex ""

## Signal strength filter. E.g. -40 would only include Bluetooth advertisements
## whose signal strength is stronger than -40dBm.
## To disable this filter, set it to ""
:local rssiThreshold ""

#################################### System ###################################
:put ("[*] Gathering system info...")
:local ifaceMac [/interface get [/interface find name=$locatorIface] mac-address]
:local cpuLoad [/system resource get cpu-load]
:local freeMemory [/system resource get free-memory]
:local usedMemory ([/system resource get total-memory] - $freeMemory)
:local rosVersion [/system package get value-name=version \
    [/system package find where name ~ "^routeros"]]
:local model [/system routerboard get value-name=model]
:local serialNumber [/system routerboard get value-name=serial-number]
## Health is a bit iffy since '/system health' does not have 'find' in ROS6
:local health [/system health print as-value]
:local supplyVoltage 0
:local boardTemp 0
:foreach entry in=$health do={
    :if ($entry->"name" = "voltage") do={:set $supplyVoltage ($entry->"value")}
    :if ($entry->"name" = "board-temperature1") do={:set $boardTemp ($entry->"value")}
}

################################## Bluetooth ##################################
:put ("[*] Gathering Bluetooth info...")
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # First time this script has been run since booting, need to initialize
    # persistent variables
    :set $btOldestAdvertisementTimestamp 0
}
:local btProcessingStart [/system clock get time]
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex and \
        data ~ $advertisingDataRegex and \
        rssi > $rssiThreshold]
:local advJson ""
:local advCount 0
:local advSeparator ""
:local lastAdvTimestamp 0
## Remove semicolons from MAC/Bluetooth addresses
:local minimizeMac do={
    :local minimized
    :local lastIdx ([:len $address] - 1)
    :for idx from=0 to=$lastIdx step=1 do={
        :local char [:pick $address $idx]
        :if ($char != ":") do={
            :set $minimized "$minimized$char"
        }
    }
    :return $minimized
}

:foreach adv in=$advertisements do={
    :local address ($adv->"address")
    :local ts ($adv->"epoch")
    :local rssi ($adv->"rssi")
    :local ad ($adv->"data")
    :local obj "\
        {\
            \"id\":\"$[$minimizeMac address=$address]\",\
            \"ts\":$ts,\
            \"rssi\":$rssi,\
            \"ed\":{\
                \"ad\":\"$ad\"\
            }\
        }"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $ts
    # Ensure that the last object is not terminated by a comma
    :set $advJson "$advJson$advSeparator$obj"
    :if ($advSeparator = "") do={
        :set $advSeparator ","
    }
}

:if ($advCount > 0) do={

    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp

}

:put ("[*] Found $advCount new advertisements \
    (processing time: $[([/system clock get time] - $btProcessingStart)])")

#################################### MQTT #####################################
:local message \
    "{\
        \"t\":0,\
        \"v\":1,\
        \"OldestAdvertisementTimestamp\":$btOldestAdvertisementTimestamp,\
        \"locs\":[{\
            \"id\":\"$[$minimizeMac address=$ifaceMac]\",\
            \"tags\":[$advJson],\
            \"ed\":{\
                \"model\":\"$model\",\
                \"sn\":\"$serialNumber\",\
                \"ros\":\"$rosVersion\",\
                \"cpu\":$cpuLoad,\
                \"umem\":$usedMemory,\
                \"fmem\":$freeMemory,\
                \"psu\":$supplyVoltage,\
                \"temp\":$boardTemp\
            }\
        }]\
    }"
:log info "$message";
:put ("[*] Total message size: $[:len $message] bytes")
/tool fetch http-method=post http-header-field="Content-Type:application/json" http-data=$message url="https://demo.thingsboard.io/api/v1/Q99YlBqv59NdzOel6tyP/telemetry"
:put ("[*] Done")

```

相應地更改 URL（取決於伺服器配置）。

```
/tool fetch http-method=post http-header-field="Content-Type:application/json" http-data=$message url="https://demo.thingsboard.io/api/v1/Q99YlBqv59NdzOel6tyP/telemetry"

```

導航到 System &gt; Scripts，並在那裡新增新指令碼（為其命名，例如 script1）。

要執行指令碼，您可以使用命令列：

/system script run script1

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟該應用程式。
- 預設情況下，IP 地址和使用者名稱將已預先填入。
- 單擊 Connect 以透過無線網路建立與裝置的連線。
- 選擇 Quick setup，該應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置場處置。請了解將裝置正確運輸到您所在地區指定處置場的相關程式。

**Bluetooth 合格產品**

![](/img/cf3c8d2919f980e2.webp)

本產品已成功完成藍牙認證流程。有關 Bluetooth 認證產品的更多資訊，請使用以下連結：[https://launchstudio.bluetooth.com/Listings/Search](https://launchstudio.bluetooth.com/Listings/Search)
