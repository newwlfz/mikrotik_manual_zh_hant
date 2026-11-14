---
title: "CME22-2n-BG77"
slug: /cme22-2n-bg77
source: https://manual.mikrotik.com/hardware/cme22-2n-bg77
captured_at: '2026-11-04T09:45:45+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可以下載為 <a href="/assets/files/cme22-2n-bg77-d526c6030e99db740f8481f8d47777e7.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/67393146bd5122a7.jpg)

一款堅固耐用、低成本、低頻寬的調變解調器，可將乙太網裝置連線到 CAT-M 行動網路……以史上最緊張的預算！完整規格和宣傳冊請參見 [CME Gateway 產品頁面](https://mikrotik.com/product/cme_gateway)。

### [CME Gateway](https://mikrotik.com/product/cme_gateway) (CME22-2n-BG77) {#cme-gateway-cme22-2n-bg77}

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置適合安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作流程，可能會給人員帶來危險並損壞系統。
- 本產品適合室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 請僅使用製造商認可並在本產品原包裝中提供的電源和附件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置出現故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和執行時，與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 連線 {#connecting}

- 確保您的網際網路服務提供商允許硬體更換，並將自動分配 IP 地址。
- 將 ISP 線纜連線到第一個乙太網埠；如果需要蜂窩 CAT-M 連線，請開啟底部區域，將 SIM 卡安裝到相應的 SIM 插槽中；
- 將裝置連線到電源；
- 在計算機上開啟網路連線，搜尋 MikroTik 無線網路並連線，或者將您的 PC 連線到第二個乙太網埠；
- 可以透過無線網路使用網頁瀏覽器或移動應用完成配置，也可以透過乙太網連線使用網頁瀏覽器完成配置。或者，您可以使用 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。在網頁瀏覽器中開啟 192.168.88.1 開始配置，使用者名稱為 admin，預設沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 單擊 Check for updates 按鈕，將 RouterOS 軟體更新到最新版本，這需要有可用的網際網路連線；
- 在 Quick Set 中選擇您所在的國家，並應用國家法規和無線設定；
- 設定您的無線網路密碼；
- 設定您的路由器密碼。

## 安裝與底蓋 {#mounting-and-bottom-lid}

- 裝置背面有 2 個孔，可將金屬環穿入其中。
- 擰鬆金屬環，將金屬環的一端穿入孔中，把金屬環繞在杆或桅杆上，然後擰緊金屬環——參見 1。

![](/img/718b6077ac5c5a05.webp)

- 擰下底蓋下方的兩顆螺絲。螺絲鬆開後，輕輕向下拉底蓋，即可開啟乙太網埠、SIM 插槽和復位按鈕的檢修口——參見 2。

## 供電 {#powering}

- 乙太網埠支援 802.3af/at 乙太網供電 18-57 V DC。
- 2 針端子輸入電壓 12-57 V DC。帶附件的最大負載下功耗可達 31 W。不帶附件時的最大功耗為 6W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置上的乙太網線纜連線到 PoE 介面卡的 PoE+DATA 埠。
- 將乙太網線纜從您的本地網路 (LAN) 連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 接地 {#grounding}

接地線應連線到 RouterBOARD 的接地線連線點。然後該線應連線到安裝位置的基座，確保連線符合接地標準。

## 配置 {#configuration}

登入後，我們建議單擊 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置使用所在的國家，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可以使用 WinBox 工具 ([https://mt.lv/winbox](https://mt.lv/winbox)) 從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問都被阻止）。為了恢復目的，可以引導裝置進行重新安裝，請參見 Buttons and jumpers 章節。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 2.4 GHz，802.11b/g/n，天線增益 2 dBi。
- 內建 GPS 模組（GPS、GLONASS、BeiDou、Galileo）。
- 兩個 10/100 乙太網埠，支援自動交叉/直通線纜糾正 (Auto MDI/X)。直通或交叉線纜均可用於連線其他網路裝置。乙太網埠可從 802.3af/at PoE 注入器接受 18-57 V DC 電源。
- 一個 nano SIM 插槽。

## GPS 與 CAT-M {#gps-and-cat-m}

CME22-2n-BG77 支援 CAT-M 和 GNSS。兩者不能同時使用。

自動切換蜂窩和 GNSS 優先順序的配置示例顯示在下面的 **蜂窩與 GNSS 優先順序切換自動化** 章節中。另請檢視以下指南 - WWAN and GNSS priority automatization。

名為 "modem" 的埠用於蜂窩連線（序列/PPP 連線）和 GNSS NMEA 資料：

```
/port print
Flags: I - INACTIVE
Columns: NAME, CHANNELS, BAUD-RATE
# NAME CHANNELS BAUD-RATE
0 modem 4 115200

```

預設 modem 埠通道分配：

1 - GNSS NMEA 輸出埠；

2 - AT/modem 埠；

### 蜂窩調變解調器配置 {#cellular-modem-configuration}

與 LTE 裝置不同，BG77 調變解調器預設不提供直接的 IP 調變解調器介面（LTE 介面），而是提供用於序列/PPP 連線的 AT/modem 序列埠。

BG77 調變解調器 AT 命令可透過該連結找到。

裝置預設了序列/PPP 連線：

```
/interface ppp-client print
Flags: X - disabled; R - running
 0 R name="ppp-out1" max-mtu=1500 max-mru=1500 mrru=disabled port=modem data-channel=2 info-channel=2 apn="internet"
 pin="" user="" password="" profile=default phone="" dial-command="ATDT" modem-init="AT+QGPSCFG="priority",1"
 null-modem=no dial-on-demand=yes add-default-route=yes default-route-distance=2 use-peer-dns=yes keepalive-timeout=30
 allow=pap,chap,mschap1,mschap2

```

有關序列/PPP 連線的更多詳細資訊，請檢視該連結。

### GNSS 配置 {#gnss-configuration}

您可以檢視此處的指南獲取更多資訊。

BG77 調變解調器為 IoT 蜂窩連線和 GNSS 訊號接收共用同一接收器。可透過 **modem-init** 字串（在 /interface ppp-client 下配置）和 GNSS 服務的 **init-string**（在 /system gps 下配置）來設定優先使用的服務。

AT 命令為：

AT+QGPSCFG="priority",0 → 優先使用 GNSS；AT+QGPSCFG="priority",1 → 優先使用蜂窩 IoT 連線；

AT+QGPSEND → 停止 GNSS 接收；AT+QGPS=1 → 啟動 GNSS 接收。

此外，您還可以藉助 AT 命令配置支援的 GNSS 星座：

AT+QGPSCFG="gnssconfig"[,&lt;GNSS_config&gt;]

，該命令僅在模組重啟後生效，其中 &lt;GNSS_config&gt; 表示星座本身（可為 "1" 到 "5"）：

- 1 → GPS + GLONASS
- 2 → GPS + BeiDou
- 3 → GPS + Galileo
- 4 → GPS + QZSS
- 5 → 可變 - 根據駐留網路的 MCC 選擇選項（1–4）之一

### 蜂窩調變解調器韌體升級 {#cellular-modem-firmware-upgrade}

請注意：

- DFOTA 韌體檢查/升級可以使用任何網際網路連線進行（包括 wi-fi 和 ethernet 上行鏈路）。因此，對於 BG77 不具備蜂窩連線的裝置（例如僅用作 GPS 接收器時），也可以升級調變解調器韌體。
- 當 BG77 調變解調器序列/PPP 介面使用主 AT/modem 通道（data-channel=2）時支援韌體升級。要檢查當前安裝的 BG77 韌體版本，請使用以下命令指定 "upgrade=no" 引數：

```
/interface/ppp-client/firmware-upgrade ppp-out1 upgrade=no
 installed: BG77LAR02A04_01.001.01.001
 latest: BG77LAR02A04_01.009.01.009

```

要更新 BG77 調變解調器韌體，請將引數設定為 "upgrade=yes"：

```
/interface/ppp-client/firmware-upgrade ppp-out1 upgrade=yes

```

### 蜂窩與 GNSS 優先順序切換自動化 {#cellular-and-gnss-priority-switch-automation}

可以透過 ppp 配置檔案的 "**on-down**"指令碼、"**idle-timeout**" 功能以及 PPP 介面的 "**dial on demand**" 設定來實現自動化。

實施後，當存在網際網路流量時，BG77 調變解調器將使用蜂窩資料（在此期間不會收到 GNSS 座標），而當未檢測到網際網路流量時，將自動啟用 GPS 接收。

**Idle-timeout** 引數指定在沒有活動的情況下，鏈路將在多長時間後終止。

**On-down**指令碼欄位允許您配置一個指令碼，該指令碼將在每次 PPP 介面斷開時執行（包括在 **idle-timeout**不活動之後）。該指令碼會將調變解調器的優先順序設定為 GNSS 接收。

**Dial-on-demand**將確保 PPP 介面僅在存在出站流量時才嘗試建立連線（此外，調變解調器會自動設定 WWAN/蜂窩連線優先順序）。這將確保在 **idle-timeout** 發生後，除非檢測到出站封包，否則連線不會自動重新建立。

透過組合這三個功能，你可以實現以下場景：

- 如果有出站流量，PPP 介面將會處於執行狀態（因為 "**dial on demand**"），並且優先順序將設定為蜂窩連線。此時會發送 PPP 介面的調變解調器初始化 AT 命令（配置在 PPP 介面的 modem-init="AT+QGPSCFG="priority",1" 設定中）以設定 WWAN 優先順序。在此期間，不會接收 GPS 座標。
- 如果在 "**idle-timeout**" 不活動視窗後未檢測到流量，PPP 介面將斷開，並且由於 "**dial on demand**" 設定，在檢測到出站封包之前不會建立連線。此時會執行 "**on-down**" 指令碼，將 WWAN 優先順序切換為 GNSS 優先順序。要實現這一點，只需新增一個新的 PPP 配置檔案：

```
/ppp profile add idle-timeout=30s name=BG77 on-down="/interface ppp-client at-chat [find where modem-init=\"AT+QGPSCFG=\\\"priority\\\",1\"] input=\"AT+QGPSCFG=\\\"priority\\\",0\""

```

上面的示例建立了一個名為 "BG77" 的新配置檔案，將 **idle-timeout** 設定為 30 秒，並啟用 **on-down** 指令碼，該指令碼將傳送 GNSS 優先順序 AT 命令。

之後，請確保將此新建立的配置檔案應用到 PPP 介面：

```
/interface ppp-client set [find] profile=BG77

```

並確認它已被應用（profile=BG77）：

```
/interface ppp-client print
Flags: X - disabled; R - running
0 R name="ppp-out1" max-mtu=1500 max-mru=1500 mrru=disabled port=modem data-channel=2 info-channel=2
apn="internet" pin="" user="" password="" profile=BG77 phone="" dial-command="ATDT"
modem-init="AT+QGPSCFG="priority",1" null-modem=no dial-on-demand=yes add-default-route=yes
default-route-distance=1 use-peer-dns=yes keepalive-timeout=30 allow=pap,chap,mschap1,mschap2

```

## 按鈕和跳線 {#buttons-and-jumpers}

### Reset 按鈕 {#reset-button}

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置現在將尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都將載入備用 RouterBOOT 載入程式。這對 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的附件：

![](/img/59434738aabaa7c4.webp)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置場。請熟悉您所在地區將裝置正確運輸到指定處置場的程式。
