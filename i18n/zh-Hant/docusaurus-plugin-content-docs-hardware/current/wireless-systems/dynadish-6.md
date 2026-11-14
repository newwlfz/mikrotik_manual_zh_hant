---
title: "DynaDish 6"
slug: /dynadish-6
source: https://manual.mikrotik.com/hardware/dynadish-6
captured_at: '2026-11-04T09:48:03+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/b28805dc6f440e18.webp)

## [DynaDish 6](https://mikrotik.com/product/dynadish_6)（RBDynaDishG-6HnD） {#dynadish-6-rbdynadishg-6hnd}

DynaDish 6 採用了與我們成功的 5 GHz 型號相同的有效天線設計和外殼，但這款新裝置工作在需要許可的 6GHz 頻段。這意味著相比經常擁堵的 5 GHz 頻段，干擾更少，從而獲得更高的速度和更遠的覆蓋範圍。透過工作在主流 WiFi 頻段之上，您現在可以從繁忙的基站搭建無線鏈路，而不必忍受噪聲問題。

它是一款簡單且完全整合的產品，包含快速安裝可靠的點對點鏈路所需的一切。

本產品不適用於無需許可的 ISM 頻段。裝置的使用受各國法規約束。可用性可能因經銷商庫存和國家法規而受到限制。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行處理。
- 裝置的安裝必須符合地方和國家電氣規範。
- 本產品設計為安裝在室外的抱杆上。使用錯誤的硬體和配置或未遵循正確的操作流程，可能會對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 使用乙太網線將裝置連線到隨附 PoE 注入器的資料+電源端；
- 將 PoE 注入器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 透過 **WebFig** 或 **WinBox** 工具在 [https://mt.lv/WinBox](https://mt.lv/WinBox) 使用網頁瀏覽器配置您的裝置；提供多種配置方法以確保可訪問性；
- 開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 供電 {#powering}

裝置接受來自無源 PoE 注入器的 12-30 V DC。功耗最高為 10 W。

## 啟動過程 {#booting-process}

裝置已預配置為無線用戶端（CPE），您只需選擇要連線的 AP 並設定裝置密碼。您可以在預設載入的 quickSET 標籤頁中完成此操作。如果 IP 連線不可用，可以使用 WinBox 透過裝置的 MAC 地址進行連線。如果您希望從網路啟動裝置，例如使用 MikroTik Netinstall，請在啟動時按住裝置的 RESET 按鈕，直到 LED 燈熄滅，然後裝置將開始尋找 Netinstall 伺服器。有關使用 RouterOS 以及連線此裝置的更多資訊，請參閱我們的文件：+[https://mt.lv/help##](https://mt.lv/help##) 擴充套件插槽和埠

- 一個 10/100/1000 Gigabit 乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X），因此您可以使用直通線或交叉線連線到其他網路裝置。
- 一個整合的無線 802.11a/n，2x2 MIMO，內建拋物面天線，最大增益 25dBi

## 按鈕和跳線 {#buttons-and-jumpers}

RouterBOOT 復位按鈕（RESET，前面板）具有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（總計 5 秒）
- 或者繼續按住按鈕，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（總計 15 秒）

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列在 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置場所。請了解您所在地區將裝置妥善運送到指定處置場所的相關流程。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID：TV7DYNADISHGAC

本裝置經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝中的有害干擾提供合理保護。

本裝置產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置可能會造成有害干擾，在這種情況下，使用者需自行承擔費用糾正干擾。

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。

注：本裝置在外圍裝置上使用遮蔽電纜進行了測試。必須使用遮蔽電纜連線本裝置以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC：7442A-DYNADISHGAC

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 標準的免許可發射器/接收器。操作須符合以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期的資訊在標籤上序列號末尾以斜槓分隔的形式標出。第一位數字表示年份編號（年份的最後一位數字），後面兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準（Norma Oficial Mexicana） {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBDynaDishG-6HnD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
