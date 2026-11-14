---
title: "wAP ax"
slug: /wap-ax
source: https://manual.mikrotik.com/hardware/wap-ax
captured_at: '2026-11-04T06:05:23+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## [wAP ax](https://mikrotik.com/product/wap_ax) (wAPG-5HaxD2HaxD) {#wap-ax-wapg-5haxd2haxd}

wAP ax 能為您的鄉間度假屋或其他任何嚴苛環境——比如鄉村加油站或公交車站——帶來快速可靠的 Wi-Fi 6。完整規格和產品手冊請參見 [wAP ax 產品頁面](https://mikrotik.com/product/wap_ax)。

<p><Img src="/img/54d372412bde265a.jpg" alt="" width={438} height={800} /></p>

## 安全警告 {#safety-warnings}

- 在接觸任何 MikroTik 裝置之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。
- 僅使用製造商批准的電源和附件，這些均可在本產品的原包裝中找到。
- 本裝置應由受過培訓的合格人員按照本安裝說明進行安裝。安裝人員有責任確保裝置的安裝符合當地和國家的電氣規範。請勿嘗試拆卸、修理或改裝裝置。
- 本產品設計用於安裝在室外的立柱上，但也可在室內安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的步驟，可能導致人員處於危險境地並造成系統損壞。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 插座應安裝在裝置附近並便於插拔。
- 若裝置發生故障，請斷開其電源。最快的方法是將電源介面卡從電源插座中拔出。
- 為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定區域。請熟悉將裝置妥善運送至您所在地區指定收集點的相關程式。
- 本產品為 A 類產品。在居住環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

- 確保您的 ISP 允許更換硬體，並會分配自動 IP 地址；
- 開啟底部蓋板；
- 用乙太網線將裝置連線到隨附的 PoE 供電器的 *"data+power"* 端；
- 將 PoE 供電器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 供電器；
- 在計算機上進入網路連線部分，找到名為 "*MikroTik-...*" 的無線網路。然後連線它（無線密碼請檢視標籤）；
- 配置應透過無線網路使用移動應用程式完成，也可以使用 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。下載並開啟 **WinBox**，選擇 **Neighbors** 標籤頁以查詢裝置；
- 點選 MAC 地址。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視標籤上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 查詢您的產品。所需的軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 **WinBox** 的 **Files** 選單並重啟裝置。將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 **QuickSet** 選單中進行以下設定：選擇您的國家，以應用該國的法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 安裝 {#mounting}

本裝置有多種安裝方式：牆壁、天花板、立柱，也可以放置在隨包裝提供的 MikroTik 專用支架中。包裝內附有帶說明的鑽孔模板，幫助您完成乙太網線的安裝以及在天花板或牆壁上的固定。包裝內還附有一個鋼製支架，用於放置在天花板吊頂板的另一側，以及兩顆螺釘和牆塞。裝置可用紮帶或鋼卡箍固定在立柱上。為防止底部蓋板被開啟，可使用不同的螺釘。包裝內附有一顆 Torx T20 安全螺釘供選用。請配合附帶的 L 形扳手將其固定到底部蓋板中。更換螺釘的詳細說明見包裝內。

使用和安裝本裝置時，請注意最大允許暴露（MPE）安全距離，輻射體與您身體之間至少保持 31 釐米。

**安裝在桅杆或立柱上：**

<p><Img src="/img/b21639053eb61552.webp" alt="" width={455} height={595} /></p>

**建議使用電工膠帶以增加材料之間的摩擦力。**

- 將塑膠紮帶穿過孔洞安裝到鋼製支架上。
- 將支架安裝到裝置上。
- 用螺釘將其固定。
- 將裝置安裝並調整對齊到立柱或桅杆上。
- 將乙太網線穿過開口並連線到乙太網埠。
- 閉合底部卡扣並用螺釘固定。
- 建議使用紮帶將乙太網線固定在立柱上，與裝置的距離約為 30 釐米。

<p><Img src="/img/42ebcb18fdb0e686.webp" alt="" width={462} height={650} /></p>

**將裝置安裝在牆上：**

- 使用附帶的模板標記鑽孔位置，如有需要也標記乙太網線孔位。請相應地調整對齊，這取決於裝置最終將如何安裝。
- 如有需要，插入膨脹螺栓，具體取決於牆體結構和材質。
- 將附帶的鋼製支架放置在牆上。
- 用螺釘將其固定到位。
- 將您的乙太網線穿過開口並連線到乙太網埠。
- 將裝置安裝到鋼製支架上
- 用螺釘將其固定到位。
- 閉合底部卡扣。

## 安裝在天花板上 {#mounting-on-the-ceiling}

<p><Img src="/img/35cd19164cabfd89.webp" alt="" width={459} height={532} /></p>

包裝內附有一個專用支架，用於安裝在天花板吊頂板上。它由兩部分組成，分別固定在天花板吊頂板的兩側。

-

使用模板標記鑽孔位置。

-

將兩個安裝支架放置在標記位置。

-

用螺釘將它們固定在一起。

-

如果安裝在牆上，請以同樣的方式繼續組裝。

-

將您的乙太網線穿過開口並連線到乙太網埠。

-

將裝置安裝到鋼製支架上。

-

用螺釘將其固定到位。

-

閉合底部卡扣。

## 底部蓋板 {#bottom-lid}

- 底部蓋板由固定螺釘固定到位。
- 使用 Philips PH2 螺絲刀將其擰鬆，但不要完全取下螺釘。

<p><Img src="/img/b67c9df3c35b1165.webp" alt="" width={194} height={118} /></p>

- 沿與裝置相反的方向拉動蓋板以將其取下。

<p><Img src="/img/23a475b4789e443e.webp" alt="" width={314} height={145} /></p>

- 重新裝回。

## 供電 {#powering}

裝置可透過電源插孔或乙太網埠供電，兩者均隨包裝提供：

- 直流直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心針正極插頭）支援 12-57 V ⎓ DC；
- 乙太網埠支援 802.3af/at PoE 18-57 V ⎓ DC。

最大負載下的功耗可達 9 W。請將接地線連線到 底部蓋板下方的螺釘上。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠；
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡；
- 將電源線連線到介面卡，然後將電源線插入電源插座。接地螺釘位於底部蓋板下方：

<p><Img src="/img/e459e23d5228cdb3.webp" alt="" width={174} height={213} /></p>

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<p><Img src="/img/315d6f9c6929731a.webp" alt="" width={613} height={462} /></p>

- 產品程式碼：wAPG-5HaxD2HaxD
- CPU：IPQ-5010 800 MHz
- CPU 架構：ARM
- CPU 核心數：2
- 記憶體容量：256 MB
- 記憶體型別：DDR3L
- 儲存：128 MB，NAND
- 1G 乙太網埠數量：2
- PoE 輸入：Ether1
- 作業系統：RouterOS（許可證級別 4）
- 無線介面型號：IPQ-5010（2.4 GHz）、QCN-6102（5 GHz）
- 無線：2.4 GHz 802.11b/g/n/ax 雙鏈；5 GHz 802.11a/n/ac/ax 雙鏈
- 天線增益 2.4 GHz：7 dBi
- 天線增益 5 GHz：7 dBi
- 5 GHz 無線代數：Wi-Fi 6
- WiFi 速率：AX3000
- 尺寸 220 x 125 x 22 mm
- 工作溫度 -40°C 至 +70°C
- IP 54

## 配置 {#configuration}

我們建議點選 "Check for updates" 按鈕並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。

- 網際網路連線配置 [https://mt.lv/configuration](https://mt.lv/configuration)；
- RouterOS 軟體升級選項 [https://mt.lv/upgrade](https://mt.lv/upgrade)；除本文件所述內容之外，RouterOS 還包含許多配置選項。建議您訪問 RouterOS 文件頁面以熟悉這些可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的所有訪問均被阻止）。可以從網路引導裝置，使用 Netinstall 實用程式重灌 RouterOS 以進行恢復。此操作可透過第一個乙太網埠完成。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 開始閃爍，然後鬆開按鈕以重設 RouterOS 配置。
- 繼續按住復位按鈕直到 LED 常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議在其中一個不起作用時對兩個選項都進行驗證。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。具體型號可能透過 **USR、USER、System** 或 **ACT** LED，或透過 SFP 埠 LED 來指示。

無論使用上述哪個選項，只要在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

<p><Img src="/img/9bcba09a7b6a0d53.webp" alt="" width={249} height={246} /></p>

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟該應用程式。
- 點選 Connect 透過無線網路與您的裝置建立連線（無線密碼請檢視標籤）。
- 使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視標籤上的使用者和無線密碼）。
- 選擇 Quick Setup，應用程式將通過幾個簡單的步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

## 配件 {#accessories}

<p><Img src="/img/a4537cde5d551f97.webp" alt="" width={971} height={157} /></p>
