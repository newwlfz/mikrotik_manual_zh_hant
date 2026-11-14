---
title: "LHG-5axD"
slug: /lhg-5axd
source: https://manual.mikrotik.com/hardware/lhg-5axd
captured_at: '2026-11-04T09:55:08+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/2703f96e0e805ba3.jpg)

## [LHG 5 ax](https://mikrotik.com/product/lhg_5_ax) (LHG-5axD) {#lhg-5-ax-lhg-5axd}

具有現代 Wi-Fi 6 效能、堅固設計和無與倫比價格的長距離室外 CPE。請參閱 [LHG-5axD 產品頁面](https://mikrotik.com/product/lhg_5_ax) 瞭解完整規格和宣傳冊。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本產品 intended to be mounted outdoors on a pole. 請閱讀安裝說明 carefully before beginning installation. 未使用正確的硬體和配置或未遵循正確的程式可能會導致人員危險和系統損壞。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和附件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、布纜要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 此 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。此 MikroTik 裝置的安裝和執行位置應距離您的身體、職業使用者或公眾不少於 20 釐米。

- 為避免環境汙染，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請熟悉將裝置正確運輸到您所在地區指定處置場所的程式。

## 組裝與安裝 {#assembly-and-mounting}

- 將兩條支腿安裝到 LHG 外殼上。

![](/img/d58c3d73abedbf96.webp)

- 將組裝好的 LHG 裝置卡入網格的適當位置。
- 用兩顆自攻螺釘固定支腿（使用 PH2 十字螺絲刀）。

![](/img/4333f6bb76f982d7.webp)

該裝置設計為使用紮帶或鋼製卡箍安裝在立杆上，如圖所示。隨附鋼製卡箍的夾持直徑為 35 – 70 mm。

![](/img/e29801f908debc24.webp)

- 將隨附的鋼製卡箍穿過裝置。
- 將裝置固定到立杆上。
- 對齊並擰緊卡箍以固定裝置。可選：如有需要，在安裝裝置前，您可以將隨附的 5 度調節轉接頭插入頂部或底部插槽（安裝環插入的位置）。當裝置緊固到垂直立杆上時，這將產生額外的向上或向下角度。

![](/img/0aaffeda7585ef66.webp)

裝置包含一個接地連線（標記為 ⏚），您應將其連線到裝置使用所在塔架或建築的接地裝置。這是為了大幅降低 ESD 和雷擊損壞的風險。警告！此裝置的安裝和執行應與身體保持至少 40 釐米的距離。在住宅環境中操作此裝置可能會導致無線電干擾。

將乙太網電纜連線到門下方的乙太網埠，並如圖所示穿過支腿：

![](/img/6a72f386ce5fdaa5.webp)

其他安裝支架可單獨購買：

LHG 安裝支架

![](/img/89ac01f14397f7f4.webp)

solidMOUNT

![](/img/5b3e2f6bc7ad89e2.webp)

## 快速開始 {#quickstart}

- 用乙太網電纜將裝置連線到隨附 PoE 注入器的 data+power 端；
- 將 PoE 注入器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 透過 Web 瀏覽器使用 **WebFig** 或 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）配置裝置。**有多種配置方法可用，以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 即可訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後單擊 MAC 地址。使用者名稱為 “**admin**”，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 “Downloads” 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 “**Files**” 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 “Quick Set” 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。該裝置已預配置為無線用戶端，您只需選擇要連線的 AP 並設定裝置密碼。您可以在預設開啟的 Quick Set 標籤頁中執行此操作。我們建議單擊 “Check for updates” 按鈕，並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。如果 IP 連線不可用，可以使用 WinBox 連線到裝置的 MAC 地址。如果您希望從網路啟動裝置，例如使用 MikroTik Netinstall，請在啟動裝置時按住裝置的 RESET 按鈕，直到 LED 燈熄滅，然後裝置將開始查詢 Netinstall 伺服器。有關使用 RouterOS 和連線此裝置的更多資訊，請參閱我們的文件：[https://mt.lv/help##](https://mt.lv/help##) 供電：該裝置僅接受來自 Passive PoE 注入器的供電。PoE 輸入電壓：12-28 V。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個乙太網埠，支援自動交叉/直通電纜校正（Auto MDI/X），因此您可以使用直通或交叉電纜連線其他網路裝置。
- 一個整合無線裝置，帶有內建網格天線。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三項功能：

- 重設 RouterOS 配置 - 在啟動期間按住按鈕，直到 USR LED 燈開始閃爍，然後鬆開以重設配置（約 5 秒）。
- 啟用 CAP 模式。繼續按住 5 秒（總共 10 秒），直到 USR LED 變為常亮，然後鬆開以開啟 CAP 模式。裝置現在將搜尋 CAPsMAN 伺服器。
- 使用 Netinstall 重新安裝 RouterOS（BOOTP 模式）。有兩種載入程式可用：常規載入程式 - 開啟裝置電源，等待 1-2 秒，然後按住 Reset 按鈕。等待 USR LED 閃爍，然後變為常亮。當 USR LED 熄滅時，鬆開 Reset 按鈕 - 裝置將進入 BOOTP 模式。
- 備份載入程式 - 關閉裝置電源，按住 Reset 按鈕，然後開啟電源。等待 USR LED 閃爍，然後變為常亮。當 USR LED 熄滅時，鬆開 Reset 按鈕 - 裝置將使用備份載入程式進入 BOOTP 模式。無論使用上述哪個選項，如果在裝置通電前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。用於 RouterBOOT 偵錯和恢復。

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未測試。
