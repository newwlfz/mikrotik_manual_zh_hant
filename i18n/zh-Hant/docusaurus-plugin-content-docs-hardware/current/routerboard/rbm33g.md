---
title: "RBM33G"
slug: /rbm33g
source: https://manual.mikrotik.com/hardware/rbm33g
captured_at: '2026-11-04T10:03:14+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/c3cd190322c3d0c9.jpg)

功能強大的 OEM 板，配備三個千兆 LAN 口和兩個 miniPCIe 插槽。完整規格和宣傳冊請參見 [RBM33G 產品頁面](https://mikrotik.com/product/rbm33g)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的通用做法。本產品的最終處置應遵守所有國家法律和法規。在任何牆面上安裝接入點的所有安裝方法均需獲得當地管轄部門的認可。裝置的安裝必須符合當地和國家的電氣規範。本產品設計用於安裝在戶外立柱上，但也可在室內安裝。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體和配置或未遵循正確的操作流程，可能給人員帶來危險情況並對系統造成損壞。請僅使用製造商認可的電源和附件，這些可在本產品的原始包裝中找到。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！如果裝置出現故障，請斷開其電源。最快捷的方法是拔下電源插座上的電源插頭。客戶有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

## 首次使用 {#first-use}

- （可選）將裝置安裝到外殼中。
- 將線纜連線到無線網路卡和乙太網埠。
- 插入電源線（直接插入或透過 PoE 注入器）以開啟裝置，請參見（連結）段落。
- 初始連線必須透過乙太網線，使用 MikroTik WinBox 工具完成。應使用 WinBox 連線到預設 IP 地址 192.168.88.1，使用者名稱為 admin，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。
- 我們建議點選 "Check for updates" 按鈕並將 RouterOS 軟體更新至最新版本，以確保最佳效能和穩定性，
- 選擇您所在的國家，以應用國家法規設定（如適用），並在隨後載入的介面中設定您的密碼。

## 組裝 {#assembly}

M33G 供專業用途使用。每臺裝置均採用 ESD 防護包裝。處理電氣裝置時，請遵守以下安全預防措施：

- 拆包和處理電子元件時，請使用腕部接地帶，以避免靜電放電（ESD）損壞。
- 拆包後，請將路由器放置在防靜電墊上。
- 安裝裝置時，請確保沒有可能損壞或接觸 PCB 板的物體。
- 請注意，ETH、USB 及其他埠超出 PCB 板的邊緣。可使用 PCB 板上裝置兩側預留的四個孔，將裝置安裝到您期望的位置。

## 安裝 {#mounting}

本裝置的安裝和配置應由具備資質的人員執行。

安裝基礎設施（塔架和桅杆）以及路由器本身必須正確接地。

## 供電 {#powering}

裝置可透過以下方式接受供電：

- 無源 11-28 V DC ⎓ PoE 輸入到 J1 乙太網埠。為補償長線纜上的功率損耗，建議至少使用 18 V 的較高電壓。
- 直接輸入到電源插孔 DC ⎓ 11-28 V。所有介面滿載時的最大總功耗為 24 W。每個擴充套件卡的最大供電為 3 A。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線連線到 PoE 介面卡的 POE 埠。
- 將來自您 LAN 的乙太網線連線到 PoE 介面卡的 LAN 埠，請注意資料和電力流向的箭頭。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 啟動過程 {#booting-process}

RouterOS 是所有 RouterBOARD 路由器的作業系統。請參見文件：[https://mt.lv/help](https://mt.lv/help) 本裝置除乙太網埠上的 IP 地址外未進行預配置。其他配置必須按照上述連結的文件手冊進行。如果您希望從網路啟動裝置，例如使用 MikroTik Netinstall，請在啟動時按住裝置的復位按鈕，直到 LED 燈熄滅，裝置便會開始尋找 Netinstall 伺服器。如果 IP 連線不可用，也可以使用 WinBox 工具連線到裝置的 MAC 地址。更多資訊請參見文件。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 三個千兆乙太網埠（支援 Auto MDI/X，因此可使用直通線或交叉線連線到其他網路裝置）。J1（最左側）乙太網埠接受來自無源 PoE 注入器的 11-30 V DC 供電。
- 兩個 miniPCIe 插槽，可安裝 802.11 無線網路卡或 3G/LTE 調變解調器。提供用於 miniPCIe 3G/LTE 調變解調器的 Mini-SIM 2FF 插槽，未安裝調變解調器時不具備任何功能。
- 一個 M.2（M key）插槽，用於 PCI-e SSD 磁碟。安裝孔適用於 2242 尺寸的卡，其他尺寸建議使用延長件。任何速度的 M.2 卡都將以 1x PCIe 速度執行。
- 一個 microSD 插槽，用於儲存卡。
- 一個 DB9 RS232 序列埠，用於序列控制檯訪問。配置為 115200 bit/s，8 個數據位，1 個停止位，無校驗。

## USB 跳線 {#usb-jumper}

位於 USB 3.0 埠右側。安裝跳線後，USB 3.0 埠啟用。移除跳線可將 USB 2.0 線路切換到 J10（中央）miniPCIe 插槽（USB 3.0 線路仍保持對 USB 埠啟用）。如果您需要在裝置中使用兩個蜂窩調變解調器，則此項為必需。通常，您可以在 J8（左側）插槽中使用 LTE 調變解調器，並在 J10 插槽中使用 802.11 無線網路卡。這種情況下可以保留跳線，因為大多數無線網路卡工作在 PCI express 上。移除跳線可在中央 J10 插槽中使用第二個蜂窩調變解調器，但會停用 USB 埠的 USB 2.0 功能，而 USB 埠仍可使用 USB 3.0。請參見下圖：

![](/img/7de67a6d3dcc15ef.webp)

## 啟動配置跳線 {#boot-configuration-jumpers}

MikroTik RouterOS 啟動的預設跳線配置：

![](/img/1bd58303e71cd179.webp)

## MiniPCIe、SIM 插槽使用 {#minipcie-sim-slot-usage}

安裝 miniPCIe 模組應由具備資質的人員執行，處理電氣裝置時請遵守安全預防措施：

- 拆包和處理電子元件時，請使用腕部接地帶，以避免靜電放電（ESD）損壞。
- 將 PCB 板放置在防靜電墊上。
- 找到 PCB 上的 miniPCIe 插槽，並卸下兩顆出廠固定的螺絲。
- 將卡安裝到 miniPCIe 插槽中。
- 使用先前卸下的兩顆螺絲將卡固定到位。
- 將灰色 uFL 接頭連線到調變解調器的 MAIN 天線接頭，將黑色線纜連線到輔助（或 AUX）接頭。將移動運營商的 SIM 卡滑入 SIM 插槽。該插槽接受 miniSIM（2FF）。每個 MiniPCIe 插槽對應位於其下方的 SIM 插槽。SIM 插槽無法在 RouterOS 中切換。

## GPIO 引腳排列 {#gpio-pinout}

M33 引腳定義如下所示：

![](/img/5ec065a7d1c7b3ec.webp)

所有輸出引腳均為開漏。

數字輸入電壓最高為 0 至 3.63 V。

要在引腳上獲得邏輯 "0"，電壓應在 0 至 1.4 V 之間。

要在引腳上獲得邏輯 "1"，電壓應在 1.41 至 3.63 V 之間。

預設情況下，引腳 12、13、15、16 配置為第二個 "serial1" 埠使用：

```
/system/routerboard/settings/set gpio-function=serial1

```

可以在 /iot/gpio/digital 選單中透過以下命令將它們重新分配為 GPIO 使用：

```
/system/routerboard/settings/set gpio-function=""
/system/reboot

```

## 按鈕和跳線 {#buttons-and-jumpers}

**RouterBOOT 復位按鈕。** 該按鈕具有以下功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（總計 5 秒）。
- 繼續按住 5 秒，LED 常亮，此時鬆開可開啟 CAPs 模式（總計 10 秒）。* 繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（總計 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入器。這對 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包括隨裝置提供的以下配件：

- K-25 套裝。

## 規格 {#specifications}

有關本產品、規格和圖片的更多資訊，請訪問我們的網頁：[https://mikrotik.com/product/rbm33g](https://mikrotik.com/product/rbm33g)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統未經測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱將已填入。
- 點選 Connect，透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 可使用高階選單完整配置所有必要設定。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的流程。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的有害干擾防護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉再開啟裝置來確定），建議使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。FCC 警告：任何未經合規負責方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受所收到的任何干擾，包括可能導致非預期操作的干擾。注意：本機在外設上使用遮蔽線纜進行了測試。為確保合規，必須在本機上使用遮蔽線纜。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置製造日期的資訊，標註在其標籤上序列號的末尾，以斜線分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

歐盟符合性宣告全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
