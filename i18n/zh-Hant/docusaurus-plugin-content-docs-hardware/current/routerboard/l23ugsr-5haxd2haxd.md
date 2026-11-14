---
title: "L23UGSR-5HaxD2HaxD"
slug: /l23ugsr-5haxd2haxd
source: https://manual.mikrotik.com/hardware/l23ugsr-5haxd2haxd
captured_at: '2026-11-04T09:52:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/f76c8433138ca7f1.jpg)

打造屬於你自己的定製戶外 Wi-Fi 6 接入點或 CPE！這款模組化無線路由器配備便捷的 MMCX 聯結器，讓你能夠構建多功能的​​全向接入點和強大的點對點鏈路。完整規格和宣傳冊請參見 [L23UGSR-5HaxD2HaxD 產品頁面](https://mikrotik.com/product/l23ugsr_5haxd2haxd)。

## 安全警告 {#safety-warnings}

在操作任何 MikroTik 裝置之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。本產品的最終處置應按照所有國家法律和法規進行。本產品出廠時不帶外殼，須由經過培訓的合格人員安裝到外殼中。安裝人員負責確保裝置安裝符合當地和國家的電氣規範。請勿嘗試拆卸、修理或改裝裝置。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體和配置或未遵循正確的操作步驟，可能對人員造成危險情況並對系統造成損壞。請使本裝置遠離水、火、潮溼或高溫環境。拆包和處理電氣元件時，請使用腕帶接地，以避免靜電放電（ESD）損壞。拆包後，請將路由器放置在防靜電墊上。安裝本機時，請確保沒有可能損壞或接觸 PCB 板的物體。我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，風險自負！為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定區域。請熟悉將裝置正確運送到您所在地區指定收集點的程式。本產品為 A 類產品。在住宅環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露**：** 本 MikroTik 裝置符合針對非受控環境制定的歐盟輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或普通公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 本產品出廠時不帶外殼，設計為安裝到使用者的最終產品或外殼中。相容 CA411-711 和 CA433U MikroTik 外殼。
- 裝置採用防靜電保護包裝。處理電氣裝置時，請遵守以下安全預防措施：拆包和處理電氣元件時，請使用腕帶接地，以避免靜電放電（ESD）損壞；
- 拆包後，請將路由器放置在防靜電墊上；
- 安裝本機時，請確保沒有可能損壞或接觸 PCB 板的物體；
- 可使用 PCB 板上出廠預留的孔位（位於裝置兩側）將裝置安裝到您想要的位置；
- 連線外部天線（必需）；
- 將裝置連線到電源；
- 在計算機上進入網路連線部分，找到名為“*MikroTik-...*”的無線網路。然後連線到它（請檢視貼紙上的無線密碼）；
- 應透過移動應用程式使用無線網路進行配置，也可以使用 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。下載並開啟 **WinBox**，然後選擇 **Neighbors** 標籤頁找到裝置；
- 點選 MAC 地址。使用者名稱為“**admin**”，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 如需手動更新裝置，請訪問 [https://mikrotik.com/products](https://mikrotik.com/products) 的產品頁面找到您的產品。所需軟體包可在“Support&Downloads”選單下獲取；
- 將下載的軟體包上傳到 **WinBox** 的 **Files** 選單並重啟裝置。將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 **QuickSet** 選單中設定以下內容：選擇您所在的國家/地區，以應用國家/地區法規設定；
- 在左側欄位設定無線網路密碼；
- 在底部欄位設定路由器密碼；
- 如果需要使用 SIM 卡，請將所需的調變解調器安裝到 miniPCIe 插槽中；
- 將 Nano SIM 卡插入插槽。

## 供電 {#powering}

本裝置可透過以下方式供電：

- 直接輸入電源插孔（外徑 5.5mm、內徑 2mm，母頭，正極針式插頭）接受 12-28 V DC。
- 乙太網埠接受 Passive PoE 18-28 V DC ⎓。最大負載下的功耗可達 25 W。

## 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 使用乙太網線將裝置連線到隨附的 PoE 供電器的資料+電源端；
- 將 PoE 供電器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 供電器。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個千兆乙太網埠；支援透過 Passive PoE 供電器輸入 18-28 V DC。
- 一個 SFP 埠（支援 2.5G）。
- 一個 USB type A 埠。
- 一個 MiniPCI-e 插槽。
- 一個 SIM 插槽（Nano SIM）。
- 2 個外部 MMCX 天線聯結器。
- 工作於 5 GHz 的整合無線模組，802.11a/n/ac/ax 協定。

## 安裝 {#mounting}

您可以將 L23UGSR-5HaxD2HaxD 整合到各種場景中，例如自動售貨機、ATM、售票站等，但如果是獨立搭建，您可能需要訂購我們的某款鋁製室內機箱。與 RB411、911、912 和 922 所使用的機箱相同，因此可以重複使用。

## 配置 {#configuration}

我們建議點選 QuickSet 選單中的“Check for updates”按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。請確保您已選擇裝置將要使用的國家/地區，以符合當地法規。RouterOS 除本文件所述之外還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問都會被阻止）。請向當地的培訓師尋求更多幫助，或自己成為培訓師 [https://mikrotik.com/training/about](https://mikrotik.com/training/about)

## Reset 按鈕 {#reset-button}

Reset 按鈕有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置此時將尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝內含以下隨裝置提供的配件：

- 歐盟開關電源 24 V DC ⎓，1.2 A，28.8 W。
- 帶遮蔽聯結器的千兆 POE 供電器線纜（RBGPOE）。

## 天線使用 {#antenna-usage}

請在裝置關閉時連線和斷開天線！

有關配置資訊，請參見[無線介面](/docs/wireless/abgn/wireless-interface)。

## 相容外殼 {#compatible-enclosures}

相容 CA411-711 和 CA433U MikroTik 外殼。

## 規格 {#specifications}

如需瞭解有關本產品的更多資訊、規格、圖片和下載內容，請訪問我們的網頁：[https://mikrotik.com/product/l23ugsr_5haxd2haxd#fndtn-specifications](https://mikrotik.com/product/l23ugsr_5haxd2haxd#fndtn-specifications)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。
