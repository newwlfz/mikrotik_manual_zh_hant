---
title: "NetMetal ax"
slug: /netmetal-ax
source: https://manual.mikrotik.com/hardware/netmetal-ax
captured_at: '2026-11-04T09:57:16+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/968aa8d79379672b.jpg)

## [NetMetal ax](https://mikrotik.com/product/netmetal_ax)（L23UGSR-5HaxD2HaxD-NM） {#netmetal-ax-l23ugsr-5haxd2haxd-nm}

網路世界中的火星探測車。我們最堅固的遠距離室外接入點 —— 現在支援 Wi-Fi 6！完整規格和宣傳冊請參見 [NetMetal ax 產品頁面](https://mikrotik.com/product/netmetal_ax)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行。
- 在任何牆面上安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於安裝在室外的立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和附件，它們可在本產品的原廠包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置出現故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

**暴露於射頻輻射：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行距離您的身體、職業使用者或公眾不得小於 20 釐米。

## 快速開始 {#quickstart}

配置與 AP 模式下的 PTP Bridge 相同，對於 PTMP 設定，無線模式也設為 AP。可以直接使用該地址訪問路由器。如果裝置連線到啟用了 DHCP 伺服器的網路，則 bridge 介面上配置的 DHCP 用戶端將獲取 IP 地址，可用於訪問路由器。

請按照以下快速步驟設定您的裝置：

- 開啟上蓋（參見拆卸上蓋和下蓋）；
- 將外接天線連線到 SMA 接頭（參見天線的使用）；
- 開啟下蓋（參見拆卸上蓋和下蓋）；
- 將您的 ISP 線纜連線到裝置，確保 ISP 允許硬體變更並會自動分配 IP 地址；
- 將裝置連線到電源（參見供電）；
- 在計算機上進入網路連線部分，找到名為 "*MikroTik-...*" 的無線網路。然後連線到它（無線密碼請檢視貼紙）；
- 配置應透過無線網路使用移動應用程式進行，也可以使用 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)；
- 下載並開啟 **WinBox**，選擇 **Neighbors** 標籤頁以查詢裝置；
- 點選 MAC 地址。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 找到您的產品。所需的軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 **WinBox** 的 "**Files**" 選單並重啟裝置。將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 wifi-interface 選單中設定以下內容：選擇您的國家/地區，以應用該國家/地區的法規設定；SSID；模式；參見手冊頁面：[WiFi](/docs/wireless/wifi)
- 設定您的無線網路安全配置檔案；
- 如果需要使用 SIM 卡，請開啟機殼並將所需的調變解調器裝入 miniPCIe 插槽；
- 將 Nano SIM 卡插入插槽。

## 供電 {#powering}

裝置可透過以下方式供電：

- 乙太網埠支援無源 PoE，輸入電壓 18-28 V DC；
- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）支援 12-28 V DC。

無附加裝置時的最大功耗為 12 W，在最大負載下可達 25 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線纜連線到 PoE 介面卡的 PoE+DATA 埠；
- 將來自您本地網路（LAN）的乙太網線纜連線到 PoE 介面卡；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟應用程式。
- 預設情況下，IP 地址和使用者名稱已預先填入。
- 點選 Connect 透過無線網路與您的裝置建立連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 還提供高階選單，可完整配置所有必要的設定。

## 拆卸上蓋和下蓋 {#removing-upper-and-bottom-covers}

- 要拆下上蓋，請擰鬆兩顆防脫螺釘並將其從主體上滑下。不要完全取下螺釘，組裝時擰緊扭矩為 0.2 Nm。
- 要拆下下蓋，請鬆開兩個固定件的卡扣，蓋子即可開啟。

![](/img/26178b9c61788031.webp)

## 安裝 {#mounting}

NetMetal ax 設計用於戶外使用，可安裝在立杆或 DIN 導軌上。

安裝時，請確保線纜出口朝下。本裝置的 IP 防護等級為 IP66。我們建議使用 Cat6 遮蔽線纜。警告！本裝置的安裝和執行應使裝置與您的身體之間保持至少 20 cm 的距離。在居住環境中操作本裝置可能造成無線電干擾。本裝置的安裝和配置應由合格人員完成。包裝中附帶安裝用軟管卡箍。

![](/img/888d0d7f203dd8db.webp)

- 將軟管卡箍穿過裝置背面的開口。
- 將其固定到立杆或桅杆上。
- 使用 PH2 螺絲刀對齊並擰緊軟管卡箍螺釘。
- 裝置應始終以上蓋朝上的方式放置。

![](/img/f15a01cb176e5195.webp)

- 安裝在 DIN 導軌上時，請在包裝中找到專用支架，並用四顆螺釘將其固定到裝置背面。

![](/img/40aa019a9c63ef9b.webp)

- 裝上安裝支架後，您就可以將裝置滑入 DIN 導軌。

## 接地 {#grounding}

安裝基礎設施（塔和桅杆）以及路由器本身都必須正確接地。裝置配有接地線固定螺釘。將接地線連線到接地螺釘，然後將接地線的另一端連線到已接地的桅杆。

![](/img/b3a6ace755736ed2.webp)

請將所有鬆散的乙太網線和天線線纜固定在距裝置約 30cm 處的立杆或桅杆上，以免線纜重量拉扯埠和接頭。

## 前面板狀態 LED 行為 {#front-status-led-behavior}

RouterOS 允許按使用者的意願配置每個 LED 的活動。可以配置 LED 顯示無線訊號強度、在介面流量活動時閃爍以及許多其他選項。更多資訊請參見 [LEDs](/docs/hardware/leds) 頁面。本裝置的出廠預設配置：

![](/img/526195de166b417d.webp)

- 常亮藍色 —— 裝置已通電。
- 常亮綠色 —— SFP 埠活動。
- 常亮綠色 —— 乙太網埠活動。
- 常亮綠色 —— 五個綠色 LED 的組合，顯示訊號強度。

## 配置 {#configuration}

裝置被配置為無線接入點，乙太網埠被配置為 DHCP 用戶端，用於連線到您的 ISP 路由器或交換器。無線介面上配置了 DHCP 伺服器。我們建議點選 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳的效能和穩定性。對於無線型號，請確保您已選擇裝置將使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問都被阻止）。出於恢復目的，可以引導裝置進行重新安裝，請參見 Reset 按鈕一節。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。直通線或交叉線均可用於連線其他網路裝置。
- SFP 埠（支援 2.5G）。
- 外接 SMA 天線接頭。
- MiniPCIe 插槽。
- 整合無線模組，工作於 2.4 GHz，802.11b/g/n/ax 協定。
- 整合無線模組，工作於 5 GHz，802.11a/n/ac/ax 協定。
- USB type-A。
- Nano SIM 插槽。

## Reset 按鈕 {#reset-button}

Reset 按鈕有三種功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置此時將查詢 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。

無論使用上述哪種方式，如果在裝置上電前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下附件：

- EU 開關電源 24 V ⎓ 1,2 A。
- 千兆 PoE 注入器。
- K-27 DIN 導軌支架安裝套件。
- 軟管卡箍 40/60 w2 A2 9 mm。受支援的 SFP 模組請參見 [MikroTik wired interface compatibility](/docs/wired-connections/mikrotik-wired-interface-compatibility) 表。

## MiniPCIe 插槽的使用 {#minipcie-slot-usage}

此 NetMetal ax 版本未安裝調變解調器。要安裝模組，您需要拆下上蓋並開啟下蓋（參見拆卸上蓋和下蓋）。安裝 miniPCIe 模組應由合格人員完成，處理電氣裝置時請遵循安全預防措施：

- 在拆包和處理電氣元件時，請使用腕帶接地，以避免靜電放電（ESD）損壞。
- 使用螺絲刀拆下四顆螺釘。

![](/img/3d63a4287bb06b8b.webp)

- 向上抬起以拆下頂蓋。
- 在 PCB 上找到 miniPCIe 插槽，並拆下出廠時安裝的兩顆螺釘。

![](/img/d6c2929801f06cb6.webp)

- 將隨附的厚導熱墊貼到卡上，並將卡裝入 miniPCIe 插槽，使導熱墊位於 PCB 與卡之間。
- 使用先前拆下的兩顆螺釘將卡固定到位。
- 將灰色 uFL 接頭連線到調變解調器的 MAIN 天線接頭，將黑色線纜連線到輔助（或 AUX）接頭。
- 在卡的頂部貼上較薄的導熱墊。

![](/img/5c2c2beff2ec1921.webp)

- 為 SMA 接頭鑽孔。
- 引導卡上的線纜穿過。
- 重新組裝。

組裝時，請確保橡膠密封件牢固地環繞在機殼周圍並均勻分佈，以防止進水汙染。機殼螺釘扭矩為 2,5 Nm。為已安裝的卡安裝天線時，請確保將它們與無線天線分開並保持足夠的距離。

## 天線的使用 {#antenna-usage}

天線安裝。警告：安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用經產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，明確禁止使用未經產品認證的任何其他天線。安裝人員應根據國家/地區法規和天線型別配置天線的輸出功率水平。帶接頭的裝置需要專業安裝，以確保符合健康與安全要求。已批准的 2GHz 天線列表：

-

5 dBi Dipole ACOMNIRPSMA 已批准的 5GHz 天線列表：

-

30 dBi 拋物面天線 MTAD-5G-30D3

-

19 dBi 扇區天線 MTAS-5G-19D120 在符合認證要求的情況下，可以使用與上述天線型別相同且增益更低的天線。有關 WiFi 介面的更多資訊：[WiFi](/docs/wireless/wifi)

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>說明</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>L23UGSR-5HaxD2HaxD-NM</td></tr><tr><td>**架構**</td><td>ARM 32-bit</td></tr><tr><td>**CPU**</td><td>IPQ-5010, 2 core, 800 MHz</td></tr><tr><td>**RAM**</td><td>256 MB</td></tr><tr><td>**儲存**</td><td>128 MB, NAND</td></tr><tr><td>**作業系統**</td><td>RouterOS v7（許可證級別 4）</td></tr><tr><td>**無線 2.4 GHz**</td><td>802.11b/g/n/ax, 2 chains, 574 Mbit/s</td></tr><tr><td>**無線 5 GHz**</td><td>802.11a/n/ac/ax, 2 chains, 2400 Mbit/s</td></tr><tr><td>**天線**</td><td>2 × RP-SMA 母頭，不含天線</td></tr><tr><td>**10/100/1000 乙太網埠**</td><td>1</td></tr><tr><td>**SFP 埠**</td><td>1（支援 2.5G）</td></tr><tr><td>**USB 埠**</td><td>1 × USB type-A</td></tr><tr><td>**SIM 插槽**</td><td>1 × Nano SIM</td></tr><tr><td>**miniPCIe 插槽**</td><td>1</td></tr><tr><td>**DC 輸入數量**</td><td>2（DC 插孔、PoE-in）</td></tr><tr><td>**PoE-in**</td><td>無源 PoE，18-28 V</td></tr><tr><td>**DC 插孔輸入電壓**</td><td>12-28 V</td></tr><tr><td>**最大功耗**</td><td>25 W</td></tr><tr><td>**無附加裝置時的最大功耗**</td><td>12 W</td></tr><tr><td>**散熱方式**</td><td>被動散熱</td></tr><tr><td>**尺寸**</td><td>143 × 247 × 48 mm</td></tr><tr><td>**工作溫度**</td><td>-40 °C 至 +70 °C</td></tr><tr><td>**MTBF**</td><td>25 °C 下約 200,000 小時</td></tr><tr><td>**認證**</td><td>CE, FCC, IC, EAC, ROHS</td></tr><tr><td>**IP 等級**</td><td>IP66</td></tr></tbody></table>

有關本產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/netmetal_ax](https://mikrotik.com/product/netmetal_ax)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource。其他作業系統尚未經過測試。
