---
title: "CRS320-8P-8B-4S+RM"
slug: /crs320-8p-8b-4s-plus-rm
source: https://manual.mikrotik.com/hardware/crs320-8p-8b-4s-plus-rm
captured_at: '2026-11-04T09:46:33+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/a9bb18c725c83d36.jpg)

## [CRS320-8P-8B-4S+RM](https://mikrotik.com/product/crs320_8p_8b_4s_rm) {#crs320-8p-8b-4srm}

首款 MikroTik 大功率 PoE++ 交換器 —— 可輕鬆且經濟高效地為符合行業標準的 802.3af/at/bt 裝置供電。告別數不清的電源線 —— 用 PoE++ 打造更整潔的空間！完整規格和宣傳手冊請參見 [CRS320-8P-8B-4S+RM 產品頁面](https://mikrotik.com/product/crs320_8p_8b_4s_rm)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用不正確的硬體或不遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 本產品適用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 插座應安裝在裝置附近且便於插拔。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置出現故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規。所有 MikroTik 裝置必須由專業人員進行安裝。
- 本產品為 A 類產品。在居住環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施

## 快速開始 {#quickstart}

- 用您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，然後在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內使用，可使用隨附的機架安裝耳將其安裝在機架機箱中，也可以放置在桌面上。如果希望放置在平坦表面上，請在路由器底部貼上橡膠腳墊；如果指定用於機架機箱，請使用十字螺絲刀在裝置兩側安裝機架安裝耳：

- 將機架安裝耳安裝到裝置兩側，並擰緊四顆螺絲將其固定到位，如圖所示。

![](/img/837a6d2bb5f312fe.webp)

- 將裝置放入機架機箱並對齊孔位，使裝置能夠方便地裝入。
- 擰緊螺絲將其固定到位。裝置沒有防水保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 網線。本裝置的安裝和配置應由合格的人員完成。

## 供電 {#powering}

本裝置配備一個熱插拔 IEC 型交流電源，636 W，支援 100-240 V AC（~50/60 Hz，最大 11 A）。

第二個 PSU 插槽用於安裝相同的熱插拔 IEC 型交流電源，636 W，支援 100-240 V AC（~50/60 Hz，最大 11 A）。

無附件時的最大功耗為 36 W。在最大負載下使用兩個電源時，功耗可達 1150 W。

## 配置 {#configuration}

完整的 RouterOS 和 SwOS 文件可在 [https://mt.lv/help](https://mt.lv/help) 獲取。除主乙太網埠上的 IP 地址外，本裝置未進行其他預配置。您可以從任意埠連線，因為預設情況下所有埠都交換在一起。其他配置必須按照上面連結的文件手冊進行。

初始連線必須透過乙太網線完成，可使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 工具。使用 **WinBox** 從任意埠連線到預設 IP 地址 192.168.88.1，使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。

如果無法使用 IP 連線，也可以使用 **WinBox** 工具連線到裝置的 MAC 地址。這僅適用於裝置已啟動 RouterOS 的情況。

出於恢復目的，可以從網路啟動裝置，請參閱 Reset 按鈕。

本裝置配備一個 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無校驗。可以使用標準的 RJ45 轉 COM 線纜；引腳定義可在 [RouterOS 文件](https://mt.lv/help) 中找到。Marvell Prestera 交換晶片功能在 [Marvell Prestera 交換晶片功能](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) 手冊中有描述。

## 電源輸出 {#power-output}

本裝置可透過其乙太網埠為外部裝置提供 PoE 供電。所有埠均提供約 54V 電壓。

**乙太網埠 1 至 8** 可為 802.3 af/at 裝置供電。預設情況下，PoE 模式設定為 auto，確保不會損壞裝置。它會自動檢測支援 PoE 的裝置並提供供電。一旦檢測到 PoE 裝置，就會為其供電，PoE LED 會點亮。**乙太網埠 9 至 16** 可為 802.3 af/at/bt 裝置供電，支援 "Type 3"（Class 5-6）和 "Type 4"（Class 7-8）。每個 802.3 af/at 埠可在高電壓下提供高達 30W 的功率。每個 802.3 bt 埠可提供高達 90W 的功率。

僅支援完全符合 802.3 at/af/bt 標準的 PD 裝置：mAP-lite、RB1100AHx4、CRS510-8XS-2XQ、CRS504-4XQ-OUT、CRS504-4XQ-IN

像 NetMetal ax 這樣的非隔離裝置，如果 PSU 或接地線形成了接地路徑，可能會引起接地環路問題。如果需要此類裝置，應使用 RBGPOE-CON-HP 提供電氣隔離

## 使用場景方案 {#use-case-schemes}

### 推薦連線方案中所用術語的說明 {#description-of-terminology-used-in-the-recommended-connection-schemes}

與之前的 802.3 af/at 供電裝置不同，這是我們首款完整實現 802.3 af/at/bt 標準的 PoE 交換器。它僅支援完全符合 802.3 af/at/bt 標準的受電裝置，例如 CRS510-8XS-2XQ-IN、CRS504-4XQ-IN、CRS504-4XQ-OUT、FTC11XG、mAP lite、RB1100AHx4 以及未來的型號。

**PSE** —— 供電裝置。**PD** —— 受電裝置。**PSU** —— 電源單元。**AF/AT** —— IEEE 802.3af 和 802.3at 是乙太網供電（PoE）標準，允許乙太網線纜在傳輸資料的同時傳輸電力，為 IP 攝像頭、無線接入點和 VoIP 電話等裝置供電。**8P** —— 八個 IEEE 802.3 af/at 埠。**8B** —— 八個 IEEE 802.3 bt 埠。

#### 使用場景 1 {#use-case-1}

**802.3 af/at/bt** 裝置（例如 CRS504-4XQ-OUT、CRS510-8XS-2XQ-IN 或 CRS504-4XQ-IN）可連線到某個 **8B** 埠，但不應再額外連線接地的 **PSU**。

![](/img/7ba88acb3f5466e1.webp)

#### 使用場景 2 {#use-case-2}

要為 Passive PoE 裝置供電，應使用 RBGPOE-CON-HP。可使用接地或浮地的 **PSU** 實現冗餘。

![](/img/4fe5847c663f97ad.webp)

#### 使用場景 3 —— 802.3 af/at 受電裝置使用非隔離 PoE 的特殊情況 {#use-case-3---special-cases-for-8023-afat-powered-device-with-non-isolated-poe}

- 應避免任何接地連線。
- 如果需要接地連線，對於使用非隔離 PoE 的受電裝置，應使用 RBGPOE-CON-HP。
- 不能同時為受電裝置使用接地的 PSU。
- SFP 籠、USB 和 RS232 埠不應與地相連。

![](/img/26252a58bcdf000a.webp)

## Reset 按鈕 {#reset-button}

Reset 按鈕具有以下功能：

- 在啟動過程中按住此按鈕，直到 USR LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 按住 Reset 按鈕並給裝置上電（等待 "USR" 燈閃爍後變為穩定 "On"，當 "USR" 燈 "Off" 時——鬆開 Reset 按鈕）——裝置將以 bootp 模式啟動，使用 Netinstall 重新安裝 RouterOS。**Netinstall 過程使用 MGMT/BOOT 乙太網埠。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。

無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。在 LED 開始閃爍之前鬆開按鈕，則僅載入備份 RouterBOOT 而不進行重設。這對於 RouterBOOT 偵錯和恢復很有用。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 16 個千兆乙太網埠（支援 Auto MDI/X，因此您可以使用直通線或交叉線連線其他網路裝置）。
- 4 個 10G SFP 埠。
- 標記為 MGMT/BOOT 的埠。
- RJ45 序列埠。

## LED 指示燈 {#led-indicators}

- 路由器通電時 PWR LED 點亮。
- USER LED 指示裝置在進入不同模式（例如重設配置或為使用 Netinstall 工具而啟動裝置）時的狀態。
- PoE FAULT LED 指示超出了整體最大 PoE 輸出限制。
- FAN FAULT LED 指示任一散熱風扇出現問題。
- 三角形 LED（上排）指示 PoE-Out 狀態：**紅色 LED：** 表示相應埠使用 PoE 802.3af/at。
- **單個紅色 LED 閃爍：** 表示啟動低壓或高壓（802.3af/at）裝置時出現問題。
- **紫色 LED：** 表示相應埠使用 PoE 802.3bt。
- **單個紫色 LED 閃爍：** 表示啟動高壓（802.3bt）裝置時出現問題。
- 方形橙色和綠色乙太網埠 LED 指示各個乙太網埠的活動。
- 三角形 SFP+ 埠綠色 LED 指示各個 SFP+ 埠的活動。

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>描述</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>CRS320-8P-8B-4S+RM</td></tr><tr><td>**架構**</td><td>ARM 32 位</td></tr><tr><td>**CPU**</td><td>98DX226S，2 核，800 MHz</td></tr><tr><td>**交換晶片型號**</td><td>98DX226S</td></tr><tr><td>**RAM**</td><td>256 MB</td></tr><tr><td>**儲存**</td><td>32 MB，Flash</td></tr><tr><td>**10/100/1000 乙太網埠**</td><td>17（16 個帶 PoE-out）</td></tr><tr><td>**SFP+ 埠**</td><td>4</td></tr><tr><td>**PoE-out**</td><td>802.3af/at/bt</td></tr><tr><td>**PoE-out 埠**</td><td>Ether1-Ether8（802.3af/at），Ether9-Ether16（802.3bt）</td></tr><tr><td>**每埠最大輸出**</td><td>高達 90 W（802.3bt）</td></tr><tr><td>**交流輸入**</td><td>100-240 V，50/60 Hz</td></tr><tr><td>**PSU 插槽數量**</td><td>2</td></tr><tr><td>**最大功耗**</td><td>600 W（使用第二個 PSU 時為 1150 W）</td></tr><tr><td>**無附件時的最大功耗**</td><td>36 W</td></tr><tr><td>**散熱**</td><td>3 個風扇</td></tr><tr><td>**工作溫度**</td><td>-10 °C 至 +50 °C</td></tr><tr><td>**作業系統**</td><td>RouterOS v7 / SwOS（雙啟動）</td></tr><tr><td>**MTBF**</td><td>25 °C 下約 200,000 小時</td></tr><tr><td>**認證**</td><td>CE、EAC、ROHS</td></tr><tr><td>**IP 防護等級**</td><td>IP20</td></tr></tbody></table>

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/crs320_8p_8b_4s_rm](https://mikrotik.com/product/crs320_8p_8b_4s_rm)

## 配件 {#accessories}

包裝內包含隨裝置提供的以下配件：

![](/img/185d3677850674bc.webp)

支援的 SFP 模組請參見 [MikroTik 有線介面相容性](/docs/wired-connections/mikrotik-wired-interface-compatibility) 表。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本和 SwOS。出廠預裝的具體 RouterOS 版本列在 /system resource 中。其他作業系統尚未經過測試。
