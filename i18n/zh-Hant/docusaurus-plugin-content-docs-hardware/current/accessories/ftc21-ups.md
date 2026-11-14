---
title: "FTC21-ups"
slug: /ftc21-ups
source: https://manual.mikrotik.com/hardware/ftc21-ups
captured_at: '2026-11-04T09:48:28+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/b1af4c483480665f.webp)

![](/img/cba1723b8ed02117.webp)

## [FTC21-ups](https://mikrotik.com/product/ftc21_ups) {#ftc21-ups}

一款防風雨的光纖轉銅纜轉換器，配備 2.5G SFP 埠和兩個千兆乙太網埠，其中 Ether2 支援 PoE-out。其內建電池可在短暫斷電期間保持鏈路穩定，避免不必要的重新協商和裝置重啟。完整規格和手冊請參見 [FTC21-ups 產品頁面](https://mikrotik.com/product/ftc21_ups)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適用於戶外使用，可安裝在立柱或牆壁上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- AC/DC 電源介面卡僅供室內使用。插座應安裝在裝置附近且易於觸及。
- 本裝置內建鋰離子電池。請勿開啟、損壞或嘗試更換電池；維修和更換隻能由授權人員執行。
- 請勿將需要 802.3af/at 協商的裝置連線到被動 PoE-out 埠。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源介面卡從電源插座中拔出。

## 快速開始 {#quickstart}

- 找到乙太網和 SFP 埠；
- 將 PC 的 IP 設定為 192.168.88.2/24；
- 連線裝置併為其通電：

- 使用 PoE-in（802.3af/at 48-57 V）：

- 用乙太網線將裝置連線到隨附 PoE 注入器的 data+power 端；
- 將 PoE 注入器的 data 端連線到電腦；
- 將電源介面卡連線到 PoE 注入器；

- 使用 DC 插孔（24-57 V）：

- 使用隨附的電源介面卡透過 DC 插孔為裝置供電；

- 在網頁瀏覽器中開啟 https://192.168.88.1。使用 "**admin**" 作為使用者名稱（預設無密碼）；
- 從 mikrotik.com/download 下載最新的 SwOS Lite。在 "**Upgrade**" 標籤頁中上傳，然後讓裝置重啟；
- 設定密碼以保護裝置；
- 如有需要，可將裝置安裝在立柱或牆壁上；
- 包裝內包含帶膨脹螺栓的螺釘。

## 安裝 {#mounting}

可使用隨附的 K-95 緊固套件和喉箍將裝置安裝在立柱或牆壁上。

要將裝置安裝在牆壁上：

- 將支架放在安裝位置並標記鑽孔點；
- 鑽孔，如有需要插入隨附的膨脹螺栓；
- 將支架擰緊固定在牆上；
- 將裝置安裝到支架上並調整對齊；
- 擰開底部蓋板，將線纜穿過開口，並連線到相應的埠；
- 合上底部蓋板並用螺釘固定。

要將裝置安裝在立柱上：

- 使用隨附的喉箍將支架固定到立柱上；
- 將裝置安裝到支架上並調整對齊；
- 擰開底部蓋板，將線纜穿過開口，並連線到相應的埠；
- 合上底部蓋板並用螺釘固定。

戶外安裝時，請確保所有線纜開口朝下。本裝置的防護等級為 IP67。請使用 Cat5/6 線纜，並正確連線機殼接地。

## 供電 {#powering}

本裝置有兩個直流輸入：

- DC 插孔接受 24-57 V DC；
- Ether1 接受 802.3af/at PoE-in，48-57 V DC。

最大功耗為 28 W。未連線附件時為 3 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將來自裝置的乙太網線連線到 PoE 介面卡的 **PoE + DATA** 埠；
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡的 **DATA** 埠；
- 將電源線連線到介面卡，然後插入電源插座。

### PoE 輸出 {#poe-output}

Ether2 提供被動 PoE-out。輸出電壓透過硬體開關選擇：24 V 或 48 V。該輸出不進行 802.3af/at 協商。

- 低壓 PoE-out 電流限制：0.625 A。
- 高壓 PoE-out 電流限制：0.315 A。
- 總輸出功率：15 W。

請勿將需要 802.3af/at 協商的裝置連線到 Ether2。

### 電池 {#battery}

本裝置內建鋰離子電池，可在短暫斷電和電壓跌落期間保持鏈路及所連裝置正常執行。它並非為長時間供電而設計。

電池在運輸途中處於非活動狀態，首次通電時會被啟用。可透過 SwOS Lite 遠端將其置於運輸模式。電池不可由使用者更換。

續航時間取決於所連負載、電池狀態和環境溫度。

## LED 指示燈 {#led-indicators}

- PWR LED 指示電源。
- PoE-in LED 指示 PoE 輸入。
- ETH1 和 ETH2 LED 指示乙太網鏈路和活動。
- SFP LED 指示 SFP 鏈路和活動。

## 復位按鈕與備份韌體 {#reset-button-and-backup-firmware}

復位按鈕位於底部蓋板下方。在裝置通電並啟動時按住它幾秒鐘，將重設配置並載入備份 SwOS Lite 韌體。

載入備份韌體後，在網頁瀏覽器中連線到 192.168.88.1（或 DHCP 伺服器分配的地址），並安裝最新的 SwOS Lite 韌體。

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>描述</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>FTC21-ups</td></tr><tr><td>**交換晶片型號**</td><td>88E6341</td></tr><tr><td>**作業系統**</td><td>SwOS Lite</td></tr><tr><td>**10/100/1000 乙太網埠**</td><td>2</td></tr><tr><td>**帶 PoE-out 的 1G 乙太網埠**</td><td>1</td></tr><tr><td>**SFP 埠**</td><td>1（支援 2.5G）</td></tr><tr><td>**DC 輸入數量**</td><td>2（DC 插孔、PoE-in）</td></tr><tr><td>**DC 插孔輸入電壓**</td><td>24-57 V</td></tr><tr><td>**PoE-in**</td><td>802.3af/at</td></tr><tr><td>**PoE-in 輸入電壓**</td><td>48-57 V</td></tr><tr><td>**PoE-out 埠**</td><td>Ether2</td></tr><tr><td>**PoE-out**</td><td>被動 PoE，透過硬體開關選擇 24 V 或 48 V</td></tr><tr><td>**低壓 PoE-out 電流限制**</td><td>0.625 A</td></tr><tr><td>**高壓 PoE-out 電流限制**</td><td>0.315 A</td></tr><tr><td>**總輸出功率**</td><td>15 W</td></tr><tr><td>**最大功耗**</td><td>28 W</td></tr><tr><td>**未連線附件時的最大功耗**</td><td>3 W</td></tr><tr><td>**電池**</td><td>鋰離子，8.4 V，3500 mAh</td></tr><tr><td>**電池放電溫度**</td><td>-20 °C 至 +65 °C</td></tr><tr><td>**尺寸**</td><td>268 × 113 × 44 mm</td></tr><tr><td>**工作溫度**</td><td>-40 °C 至 +70 °C</td></tr><tr><td>**MTBF**</td><td>25 °C 下約 100,000 小時</td></tr><tr><td>**散熱方式**</td><td>被動</td></tr><tr><td>**PCB 溫度監控**</td><td>是</td></tr><tr><td>**認證**</td><td>CE, EAC, ROHS</td></tr><tr><td>**防護等級**</td><td>IP67</td></tr></tbody></table>

## 配件 {#accessories}

包裝內包含以下隨裝置提供的附件：

![](/img/6fb7adf18655cfe9.webp)

- 48 V、0.95 A 電源介面卡。
- 千兆 PoE 注入器。
- 喉箍（1 個）。
- K-95 緊固套件。

不含 SFP 模組。

## 作業系統支援 {#operating-system-support}

本裝置執行 SwOS Lite。出廠安裝的版本列於 SwOS Lite 網頁介面中。不支援其他作業系統。
