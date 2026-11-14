---
title: "SXTsq 嵌入式 LTE4"
slug: /sxtsq-embedded-lte4
source: https://manual.mikrotik.com/hardware/sxtsq-embedded-lte4
captured_at: '2026-11-04T10:05:20+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/8cf0beb24d86b5a7.jpg)

## [SXTsq 嵌入式 LTE4](https://mikrotik.com/product/sxtsq_emb_lte4)（EC25-EU&SXTsq） {#sxtsq-embedded-lte4-ec25-eusxtsq}

一款經濟高效的室外 LTE 裝置，整合 2×2 MIMO 定向天線、Cat4 LTE 調變解調器和 RouterOS v7，專為可靠的遠端連線而設計。提供支援 eSIM 的歐盟版（EC25-EU）和全球版（EG25-G），具備 PoE-in 以及堅固的 IP 防護等級 SXTsq 室外外殼，最大功耗僅 5 W 即可提供穩定的 LTE 連線。這是常規版或歐盟版。完整規格和宣傳冊請參見 [SXTsq Embedded LTE4 產品頁面](https://mikrotik.com/product/sxtsq_emb_lte4)。

## 安全警告 {#safety-warnings}

- 在對任何 MikroTik 裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。
- 僅使用製造商認可的電源和配件，這些電源和配件可在本產品的原包裝中找到。
- 本裝置應由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責確保裝置的安裝符合當地和國家的電氣規範。
- 請勿嘗試拆卸、修理或改裝裝置。如需服務，請聯絡 MikroTik 支援。
- 本產品適合安裝在室外的立杆上。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體和配置或未遵循正確的步驟，可能會對人員造成危險情況並損壞系統。
- 我們無法保證因不當使用本裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 插座應安裝在裝置附近，且應易於觸及。
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源介面卡從電源插座上拔下。
- 為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處理，例如在指定區域處理。請熟悉將裝置正確運送至您所在地區指定收集點的流程。

## 快速開始 {#quickstart}

- 按照指示將 Nano SIM 卡插入卡槽；
- 將裝置連線到隨附的電源介面卡；
- 使用乙太網線將裝置連線到計算機；
- 透過 **WebFig** 使用 Web 瀏覽器，或使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）來配置裝置。**提供了多種配置方法以確保可訪問性；**
- 開啟 [https://192.168.188.1](https://192.168.188.1) 即可訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後選擇 MAC 地址。使用者名稱為 "**admin**"，無密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如果您的行動網路運營商要求，請輸入 PIN 碼；
- 選擇 "Check for updates" 按鈕並將 RouterOS 更新到最新版本。必須插入有效的 SIM 卡或已設定 [eSIM](/docs/mobile-networking/lte-5g#lte-esim)，並且需要有效的網際網路連線；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱將已填寫。
- 選擇 Connect 以透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

## 配置 {#configuration}

可以透過 Web 瀏覽器使用 WebFig 進行配置，WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）等方法可確保可訪問性。

- 如需訪問 WebFig，請在瀏覽器中開啟 [https://192.168.188.1](https://192.168.188.1)。
- 對於 WinBox，請下載該工具，進入 Neighbors 標籤頁，然後選擇 MAC 地址。預設使用者名稱為 "admin"，**請在裝置貼紙上查詢密碼**。您應經常檢查更新，以確保 RouterOS 軟體保持最新，從而獲得最佳效能和穩定性。在 WinBox 或 WebFig 中選擇 "Check for updates" 按鈕即可更新到最新版本。

必須插入有效的 SIM 卡或設定 eSIM，並具備有效的網際網路連線，更新才能正常工作。

RouterOS 提供了本文件所述之外的廣泛配置選項。建議訪問 [https://mt.lv/help](https://mt.lv/help) 瞭解這些功能。

出於恢復目的，可以讓裝置引導以進行重新安裝，請參見相應章節。

## 安裝 {#mounting}

本裝置的 IP 防護等級為 IP67。在室外安裝時，請確保任何電纜開口朝下。您應使用 POE 供電器並進行正確接地。使用和安裝本裝置時，請注意最大允許暴露量（MPE）安全距離，輻射體與您身體之間至少保持 20 cm。

![](/img/03f503e6f8717d99.webp)

本裝置隨附一個金屬安裝環，可用於裝置背面的安裝槽。

- 使用十字螺絲刀鬆開金屬環。
- 將其一端穿過三個安裝槽中最方便的一個。
- 將裝置放置在將要安裝的立杆上。
- 將安裝環的松端滑回其閉合卡扣，並用螺絲刀將其擰緊。
- 隨附的環形支架可安裝在直徑 3-7 cm 的立杆上。建議使用紮帶將乙太網線固定在立杆上，與裝置的距離約為 30 cm。

![](/img/7f35ee2b81792bc8.webp)

![](/img/cfba0947d7d0fe38.webp)

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>說明</th></tr></thead><tbody><tr><td>產品型號</td><td>EC25-EU&SXTsq</td></tr><tr><td>**架構**</td><td>ARM 32bit</td></tr><tr><td>**CPU**</td><td>Cortex A7</td></tr><tr><td>**CPU 核心數**</td><td>1</td></tr><tr><td>**CPU 標稱頻率**</td><td>800 MHz</td></tr><tr><td>**RouterOS 許可證**</td><td>Level 3</td></tr><tr><td>**作業系統**</td><td>RouterOS v7</td></tr><tr><td>**記憶體**</td><td>256 MB</td></tr><tr><td>**儲存**</td><td>512 MB NAND</td></tr><tr><td>**MTBF**</td><td>25°C 下約 100'000 小時</td></tr><tr><td>**工作溫度**</td><td>-40°C 至 +70°C</td></tr><tr><td>**最大功耗**</td><td>5 W</td></tr><tr><td>**供電**</td><td>PoE-IN（被動），12–28 V</td></tr><tr><td>**散熱**</td><td>被動散熱</td></tr><tr><td>**乙太網**</td><td>1 × 10/100/1000 Mbps</td></tr><tr><td>**SIM**</td><td>2 個調變解調器：Nano SIM + eSIM</td></tr><tr><td>**行動網路：2G**</td><td>Class 33</td></tr><tr><td>**2G 頻段**</td><td>3 (1800 MHz), 8 (900 MHz)</td></tr><tr><td>**行動網路：3G**</td><td>Category R8（下行 42.2 Mbps / 上行 5.76 Mbps）</td></tr><tr><td>**3G 頻段**</td><td>1 (2100 MHz), 8 (900 MHz)</td></tr><tr><td>**行動網路：LTE**</td><td>Category 4（下行 150 Mbps / 上行 50 Mbps）</td></tr><tr><td>**MIMO**</td><td>下行 2×2</td></tr><tr><td>**LTE FDD 頻段**</td><td>1 (2100 MHz), 3 (1800 MHz), 7 (2600 MHz), 8 (900 MHz), 20 (800 MHz), 28A (700 MHz)</td></tr><tr><td>**LTE TDD 頻段**</td><td>38 (2600 MHz), 40 (2300 MHz), 41 (2500 MHz)</td></tr><tr><td>**TAC**</td><td>86554604</td></tr><tr><td>**監控**</td><td>CPU 溫度監控</td></tr><tr><td>**eSIM**</td><td>是</td></tr><tr><td>**認證**</td><td>CE, EAC, ROHS</td></tr><tr><td>**IP 防護等級**</td><td>IP67</td></tr></tbody></table>

## 供電 {#powering}

本裝置透過 PoE 802.3af/at 接受 **12–28 V DC ⎓**。隨附電源和 PoE 供電器。

**連線電源：**

- 將裝置的乙太網線連線到 PoE 供電器的 **PoE+DATA** 埠。
- 將您的 LAN 線纜連線到供電器。
- 連線電源並將其插入插座。

## eSIM 設定 {#esim-settings}

預設情況下，裝置配置為使用 SIM 卡槽。如需使用板載 eSIM，請使用以下命令切換卡槽：**/interface/lte/settings/set sim-slot=esim**

單個 eSIM 晶片可以儲存多個 eSIM 配置檔案，最大配置檔案數量取決於所使用的 eSIM 晶片。

詳情請參見 [LTE eSIM](/docs/mobile-networking/lte-5g#lte-esim) 頁面。

## 復位按鈕 {#reset-button}

復位按鈕有三個功能：

- 在啟動過程中按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（共 10 秒）。
- 使用 Netinstall 重新安裝 RouterOS。如需使用 Netinstall 實用工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種可用的載入程式：常規載入程式和備用載入程式。常規載入程式 - 開啟裝置電源，等待 1-2 秒，然後按下並按住復位按鈕。等待直到 "USR" LED 閃爍，然後變為常亮 "On"。當 "USR" LED 變為 "Off" 時，鬆開復位按鈕 - 裝置將進入 BOOTP 模式。
- 備用載入程式 – 關閉裝置電源，按下並按住復位按鈕，然後開啟電源。等待直到 "USR" LED 閃爍，然後變為常亮 "On"。當 "USR" LED 變為 "Off" 時，鬆開復位按鈕 - 裝置將使用備用載入程式進入 BOOTP 模式。無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統都將載入備用 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

Netinstall執行 Netinstall 時，請確保 ROS 檔案和 Netinstall 軟體均使用最新的 v7 版本。

## 接地 {#grounding}

本裝置包含一個接地連線（標記為 ⏚），您應將其連線到使用該裝置的鐵塔或建築物的接地裝置。這可以大幅降低靜電放電和雷擊損壞的風險。

## 配件 {#accessories}

包裝中包含以下隨裝置附帶的配件：

- EU/US 開關電源 24V DC ⎓，0.38 A，9 W
- 帶遮蔽接頭的 POE 供電器/千兆 POE 供電器。
- 軟管卡箍 SUS304（十字型；夾緊直徑範圍 30-70 mm）。

![](/img/3bbd38be7147e5cf.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。
