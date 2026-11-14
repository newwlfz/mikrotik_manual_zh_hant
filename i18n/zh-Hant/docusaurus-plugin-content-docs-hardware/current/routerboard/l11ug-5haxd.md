---
title: "L11UG-5HaxD"
slug: /l11ug-5haxd
source: https://manual.mikrotik.com/hardware/l11ug-5haxd
captured_at: '2026-11-04T09:52:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/ec8ebacd87b1d206.jpg)

![](/img/00e8935b6a55ef3c.webp)

使用 Wi-Fi 6、雙核 ARM CPU、PoE-in、千兆乙太網和 RouterOS v7 構建您自己的定製室外 5 GHz CPE 或 AP！MMCX 聯結器可讓您打造多功能的全向接入點和強大的點對點鏈路。完整規格和宣傳冊請參見 [L11UG-5HaxD 產品頁面](https://mikrotik.com/product/l11ug_5haxd)。

## 安全警告 {#safety-warnings}

在操作任何 MikroTik 裝置之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。本產品的最終處置應遵守所有國家法律和法規。本產品出廠時不帶外殼，需由經過培訓的合格人員安裝到外殼中。安裝人員負責確保裝置的安裝符合當地和國家的電氣規範。請勿嘗試拆卸、修理或改裝裝置。開始安裝前，請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的步驟，可能會對人員造成危險情況並損壞系統。請讓本裝置遠離水、火、潮溼或高溫環境。在開箱和處理電子元件時，請使用腕部接地帶，以避免靜電放電（ESD）損壞。開箱後，請將路由器放置在防靜電墊上。安裝裝置時，請確保沒有可能損壞或觸碰 PCB 板的物體。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定區域。請熟悉將裝置正確運送至您所在地區指定收集點的程式。本產品為 A 類產品。在居住環境中，本產品可能會引起無線電干擾，此時使用者可能需要採取適當的措施。

**暴露於射頻輻射**：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置應與您的身體、職業使用者或普通公眾保持不少於 20 釐米的距離。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 本產品出廠時不帶外殼，設計用於安裝到使用者的最終產品或外殼中。相容 CA411-711 和 CA433U MikroTik 外殼。
- 裝置採用 ESD 防護包裝。處理電氣裝置時，請遵守以下安全預防措施：在開箱和處理電子元件時，請使用腕部接地帶，以避免靜電放電（ESD）損壞；
- 開箱後，請將路由器放置在防靜電墊上；
- 安裝裝置時，請確保沒有可能損壞或觸碰 PCB 板的物體；
- 可使用 PCB 板上出廠預留的孔位將裝置安裝到所需位置，這些孔位位於裝置兩側；
- 使用乙太網線將裝置連線到隨附的 PoE 注入器的資料+電源端；
- 將 PoE 注入器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 應使用 WinBox 配置工具進行配置 [https://mt.lv/winbox](https://mt.lv/winbox) 下載並開啟 **WinBox**，選擇 "**Neighbors**" 標籤頁以查詢裝置；
- 點選 MAC 地址。使用者名稱為 "**admin**"，沒有密碼（或者，某些型號請檢視貼紙上的使用者名稱和無線密碼）；
- 如需手動更新裝置，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 查詢您的產品。所需軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 **WinBox** 的 **Files** 選單並重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 "*QuickSet"* 選單中設定 *"PTP Bridge AP"* 模式並選擇您的國家，以應用國家法規設定；
- 根據所用天線設定天線增益；
- 在底部欄位中設定路由器密碼。

## 供電 {#powering}

裝置可透過以下方式接受供電：

- 直接輸入電源插孔（外徑 5.5mm、內徑 2mm，母頭，中心正極插頭）接受 12-28 V DC。
- 乙太網埠接受 Passive PoE 18-28 V DC ⎓。最大負載下的功耗可達 15 W。

## 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 使用乙太網線將裝置連線到隨附的 PoE 注入器的資料+電源端；
- 將 PoE 注入器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 注入器。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個千兆乙太網埠；透過 passive PoE 注入器支援 18-28 V DC 輸入。
- 一個 USB 埠。
- 2 個外部 MMCX 天線聯結器。
- 整合無線模組，工作在 5 GHz，支援 802.11a/n/ac/ax 協定。

## 安裝 {#mounting}

您可以將 L11UG-5HaxD 整合到各種場景中，例如自動售貨機、ATM、售票站等；但如果是獨立安裝，您可能需要訂購我們的鋁製室內外殼。這些外殼與 RB411、911、912 和 922 所使用的相同，因此可重複使用。

## 配置 {#configuration}

我們建議點選 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。請確保您已選擇裝置將要使用的國家，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。請向您當地的培訓師尋求更多幫助，或自己成為培訓師 [https://mikrotik.com/training/about](https://mikrotik.com/training/about)

## 復位按鈕 {#reset-button}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（總共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置隨後將查詢 CAPsMAN 伺服器（總共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總共 15 秒）。無論使用上述哪種方式，如果在對裝置通電之前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這有助於 RouterBOOT 偵錯和恢復。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的附件：

- 歐盟開關電源 24 V DC ⎓，1.2 A，28.8 W。
- 帶遮蔽聯結器的千兆 POE 注入器線纜（RBGPOE）。

## 天線使用 {#antenna-usage}

請在裝置關閉時連線和斷開天線！

配置資訊請參見 [Wireless Interface](/docs/wireless/abgn/wireless-interface)。

## 相容外殼 {#compatible-enclosures}

相容 CA411-711 和 CA433U MikroTik 外殼。

## 規格 {#specifications}

有關本產品的更多資訊、規格、圖片和下載內容，請訪問我們的網頁：[https://mikrotik.com/product/l11ug_5haxd](https://mikrotik.com/product/l11ug_5haxd)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及更高版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。
