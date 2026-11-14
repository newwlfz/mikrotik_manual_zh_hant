---
title: "LHG Lite60"
slug: /lhg-lite60
source: https://manual.mikrotik.com/hardware/lhg-lite60
captured_at: '2026-11-04T09:53:41+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可下載為 <a href="/assets/files/lhg-lite60-78d98dce5497554c58a20e9c0f69791e.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/c0b45e24aa858424.webp)

## [LHG Lite60](https://mikrotik.com/product/lhg_lite60) (RBLHG-60ad) {#lhg-lite60-rblhg-60ad}

LHG Lite 60 是一款室外無線路由器，內建定向天線，工作於 60GHz 頻段。它可用作 CPE，連線到工作在 60GHz 接入點模式下的 MikroTik 裝置。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 在任何牆面上安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計為室外抱杆安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置，或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 請僅使用製造商認可的電源和配件，這些均可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在法律允許的頻段內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。
- 本裝置為 A 類裝置。在居住環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

## 組裝 {#assembly}

將兩條支腳安裝到 LHG 外殼上，然後將組裝好的 LHG 單元對準相應位置卡入網格中。用兩顆自攻螺釘（隨附，請使用 PH2 十字螺絲刀）將支腳固定到位。包裝中還包含一個接地線聯結器和一個精密對準支架。對準說明可在產品頁面上查閱：[https://mikrotik.com/products/](https://mikrotik.com/products/)。

## 連線 {#connecting}

- 開啟乙太網艙門，將乙太網線連線到乙太網埠，並將網線的另一端連線到隨附的 PoE 供電器（LHG Lite60），或連線到 802.3af/at 電源（僅 LHG 60G 型號支援）。
- 將 PoE 供電器插入您的網路交換器或 ISP 網際網路介面。
- 將隨附的電源插入 PoE 供電器，為裝置啟動供電。
- 為便於配置，請將您計算機的 IP 配置設為靜態，地址範圍 192.168.88.0-254（/24 或 255.255.255.0）。
- 裝置的預設 IP 地址為 192.168.88.1/24，請在網頁瀏覽器中開啟該地址以開始配置。使用者名稱為 admin，沒有密碼（某些型號請檢視貼紙上的使用者名稱和無線密碼）。裝置已預配置為 w60g station，您只需選擇要連線的 AP 並設定裝置密碼即可。可在預設載入的 quickSET 標籤頁中完成此操作。如果無法透過 IP 連線，可以使用 WinBox 透過裝置的 MAC 地址進行連線。我們建議點選 "Check for updates" 按鈕並將 RouterOS 軟體更新到最新版本，以確保最佳的效能和穩定性。有關使用 RouterOS 和連線此裝置的更多資訊，請參閱我們的文件：[https://mt.lv/help](https://mt.lv/help)

## 供電 {#powering}

LHG Lite60 僅接受來自無源 PoE 供電器的 12-30 V 供電（隨附一個電源和一個 PoE 供電器）。LHG 60G 接受 12-57 V 的 802.3af/at 供電，同時也支援無源 PoE。兩種型號在最大負載下的功耗均可達到 5 W。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個乙太網口（10/100 Mbit 或千兆，取決於型號），支援自動交叉/直通線纜糾正（Auto MDI/X），因此您可以使用直通線或交叉線連線到其他網路裝置。
- 一個整合的 w60g 介面，帶內建天線。

## 按鈕和跳線 {#buttons-and-jumpers}

routerBOOT 復位按鈕具有以下功能。按住按鈕並通電，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置並恢復預設值。
- 當 LED 熄滅（約 20 秒）後鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時所需）。無論使用上述哪種方式，如果在給裝置通電之前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。裝置包含一個接地連線（標記為 ⏚），您應將其連線到裝置使用地點所在塔架或建築物的接地裝置。這可大幅降低靜電放電和雷擊損壞的風險。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統未經測試。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBLHG-60ad</td><td>TV7LHG60AD</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制要求。這些限制旨在為商業安裝環境中的有害干擾提供合理防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在居住區域操作本裝置很可能造成有害干擾，此時使用者需要自費糾正該干擾。

**FCC 警告：** 未經負責合規的一方明確批准的任何更改或修改，可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的規定。其操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與其他任何天線或發射器放置在一起或聯合執行。

除 FCC CFR §15.255 (b) 所列條件外，本裝置不得在飛機上使用。

**重要提示：射頻輻射暴露。** 天線與使用者之間必須保持至少 20 cm 的距離。在此配置下，可滿足 FCC 針對人群/非受控環境所規定的射頻暴露限值。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBLHG-60ad</td><td>7442A-LHG60AD</td></tr></tbody></table>

本裝置符合加拿大工業部免許可證 RSS 標準。其操作須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置操作異常的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

**重要說明！IC 輻射暴露宣告：** 本裝置符合 IC RSS-102 針對非受控環境所規定的輻射暴露限值。本裝置安裝和執行時，輻射源與您身體之間的最小距離應為 20cm。Cet équipement est conforme aux limites d'exposition aux rayonnements IC établies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé avec un minimum de 20 cm de distance entre la source de rayonnement et votre corps.

除 ISED RSS-210 Annex J.1 所列條件外，本裝置不得在飛機上使用。Cet appareil ne doit pas être utilisé sur un avion, sauf dans les conditions énumérées ISED RSS-210 Annex J.1.
