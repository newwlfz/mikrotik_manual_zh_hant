---
sidebar_key: "hardware/poe-out"
sidebar_position: 7
title: "PoE"
sidebar_label: "PoE"
description: "本頁介紹 MikroTik 裝置上的 PoE（乙太網供電）：支援的標準和功率等級，在 RouterOS 和 SwOS 中配置和監控 PoE out（PSE）與 PoE in（PD）埠，以及日誌記錄、警告、示例和故障排除。"
tags:
  - 'poe'
  - 'power-over-ethernet'
source: https://manual.mikrotik.com/docs/7.25/hardware/poe-out
captured_at: '2026-11-04T11:17:28+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

本頁介紹 MikroTik 裝置上的 PoE(乙太網供電):使用 **PoE out** 埠為其他裝置供電(此時裝置作為 PSE,即供電裝置),以及在某些型號上透過 **PoE in** 埠被供電(此時裝置作為 PD,即受電裝置)。MikroTik 裝置使用 RJ45 Mode B 引腳定義進行供電,PoE 透過引腳 4 和 5(+)以及引腳 7 和 8(-)提供。

## MikroTik 支援的 PoE 標準 {#mikrotik-supported-poe-standards}

MikroTik 裝置可以支援以下部分或全部 PoE 標準——既用於為其他裝置供電(PoE out,裝置作為 PSE),在某些型號上也用於自身被供電(PoE in,裝置作為 PD):

- **最高 30 V 的無源 PoE** - 無源 PoE,PSE(供電裝置)與 PD(受電裝置)之間沒有協商。PoE out 埠輸出的電壓與提供給 PSE 本身的電壓相同。適用於支援最高 30 V 輸入電壓的裝置。(例如 [hEX PoE lite](https://mikrotik.com/product/RB750UPr2)、[RB3011UiAS-RM](https://mikrotik.com/product/RB3011UiAS-RM)、[RB2011iL-IN](https://mikrotik.com/product/RB2011iL-IN)。)

- **最高 57 V 的無源 PoE** - 工作原理與低壓(最高 30 V)無源 PoE 相同,但可以透過 PoE 埠提供或接受更高的電壓。對於 PoE out,輸出電壓取決於連線到 PSE 的電源。它也可以為相容 af/at、透過 4,5(+) 和 7,8(-) 線對接受供電且不需要 PoE 協商的 PD 供電。(例如 [cAP ac](https://mikrotik.com/product/cap_ac)、[hAP ac](https://mikrotik.com/product/RB962UiGS-5HacT2HnT)、[wsAP ac lite](https://mikrotik.com/product/wsap_ac_lite)。)

- **IEEE 802.3af/at 標準** - 也稱為 PoE(802.3af,Type 1)和 PoE+(802.3at,Type 2),這些 IEEE 標準確保不同廠商之間的相容性。支援這些標準的 PSE 可以為 Type 1 和 Type 2 PD 供電,支援這些標準的 PD 可以由任何符合標準的 PSE 供電。(例如 [CRS112-8P-4S-IN](https://mikrotik.com/product/crs112_8p_4s_in)、[CRS328-24P-4S+RM](https://mikrotik.com/product/crs328_24p_4s_rm)、[CRS354-48P-4S+2Q+RM](https://mikrotik.com/product/crs354_48p_4s_2q_rm)。)

- **IEEE 802.3bt 標準** - 802.3bt 標準也稱為 PoE++,它擴充套件了早期的 PoE 標準,並引入了 "Type 3"(Class 5-6)和 "Type 4"(Class 7-8)。該標準使用千兆乙太網電纜中的全部四對線來傳輸電力,因此得名 4PPoE/802.3bt("4-pair Power over Ethernet")。視型號而定,802.3bt 用於 PoE out、PoE in 或兩者兼有。(例如 [CRS320-8P-8B-4S+RM](https://mikrotik.com/product/crs320_8p_8b_4s_rm))

每個 PoE out 實現都支援過載和短路檢測。

### 功率等級 {#power-classes}

802.3 PoE 標準定義了功率等級,用於描述 PSE 向 PD 提供的最大功率:

| 等級 | 標準 | PSE 輸出功率 | PD 可用功率 |
| :-- | :-- | :-- | :-- |
| 0-3 | 802.3af(Type 1) | 15.4 W | 12.95 W |
| 4 | 802.3at(Type 2) | 30 W | 25.5 W |
| 5 | 802.3bt(Type 3) | 45 W | 40 W |
| 6 | 802.3bt(Type 3) | 60 W | 51 W |
| 7 | 802.3bt(Type 4) | 75 W | 62 W |
| 8 | 802.3bt(Type 4) | 90 W | 71.3 W |

PSE 和 PD 使用功率等級來商定可以傳輸多少功率:PD 發出其等級訊號,PSE 隨後分配相應的功率預算。

您可以從裝置的規格頁面判斷它支援哪種無源 PoE 標準:"PoE-OUT" 部分下的 **`Low voltage PoE-Out current limit`** 條目表示該裝置支援**最高 30 V 的無源 PoE**,如果還有 **`High voltage PoE-Out current limit`** 條目,則表示它同時支援**最高 57 V 的無源 PoE**。支援的 IEEE 標準會直接列在規格頁面上,如 `PoE out`(例如 802.3af/at 或 802.3bt)。

如上面的列表所述,**最高 57 V 的無源 PoE** 也可以為相容 802.3af/at、不需要 PoE 協商的裝置(PD)供電——對於 MikroTik PD,這可以可靠工作。但是,第三方 PD 在沒有協商時可能會將自己歸入較低的 PoE 等級,並請求比其本來可以使用的更少的功率——這可能表現為射頻輸出功率降低、外設被停用等類似症狀。不同 PD 的行為有所不同。

## 配置 {#configuration}

所有帶 PoE 介面的 MikroTik 裝置都支援 PoE 配置。可以在 RouterOS 和 SwOS 介面中進行編輯。

### RouterOS {#routeros}

**子選單：** `/interface/ethernet/poe`

#### 用法 {#usage}

RouterOS 提供了透過 Winbox、Webfig 和 CLI 配置和監控 PoE 的選項。使用 CLI 的基本命令如下

| 屬性 | 描述 |
| :-- | :-- |
| **print** () | 列印與 PoE 相關的設定。 |
| **export** () | PoE 配置匯出在 `/interface/ethernet` 選單下。 |
| **monitor** (*string\| interface*) | 監控指定埠的 PoE 狀態——PoE out 埠上的 `poe-out-status`、電壓、電流和功率,PoE in 埠上協商得到的功率相關資訊。可以用 `/interface/ethernet/poe/monitor [find]` 監控所有埠。 |
| **power-cycle** (*duration: 0..1m*; 預設值：**5s**) | 在指定時間段內關閉 PoE out 埠的 PoE 輸出供電。 |

### SwOS {#swos}

SwOS 介面提供基本的 PoE out 配置和監控選項,更多詳情請參見 [SwOS 手冊](../bridging-and-switching/swos/index.md)。

## 監控 {#monitoring}

**子選單：** `/interface/ethernet/poe/monitor`

| 屬性 | 描述 |
| :-- | :-- |
| **name** () | 介面名稱。 |
| **port-type** () | 顯示該介面是否支援 PoE out、PoE in 或兩者(**poe-out**、**poe-in**、**poe-in/poe-out**)。 |
| **poe-out** () | 顯示 PoE out 狀態。 |
| **poe-voltage** () | 顯示 PoE out 電壓選擇(**auto**、**low**、**high**)。 |
| **poe-out-status** () | 顯示埠上當前的 PoE out 狀態(參見下方的[狀態列表](#poe-out-statuses))。 |
| **poe-out-voltage** () | 顯示施加到 PD 的電壓。 |
| **poe-out-current** () | 顯示 PD 拉取的埠電流(mA)。 |
| **poe-out-power** () | 顯示 PD 功耗。 |
| **poe-out-power-pair()** | 顯示 PSE 在哪些電源線對上向 PD 供電:**a** - 1,2 (+) 3,6 (-);**b** - 4,5 (+) 7,8 (-);**bt** - 全部 4 對線。 |
| **power-cycle-host-alive** (*yes \| no*) | 顯示被監控的主機是否可達(在啟用 [power-cycle-ping](#power-cycle-settings) 功能時顯示)。只讀。 |
| **power-cycle-after** (*time*) | 顯示埠將在多久之後進行電源迴圈(在啟用 [power-cycle-ping](#power-cycle-settings) 功能時顯示)。只讀。 |

#### PoE out 狀態 {#poe-out-statuses}

- **powered-on** - 埠已施加電源，PoE out 正常工作。
- **waiting-for-load** - PSE 嘗試檢測是否可以向埠施加電源。為了供電，電阻應在 3kΩ 到 26.5kΩ 範圍內。
- **short-circuit** - 在 PoE out 埠上檢測到短路；電源被關閉，僅進行低電壓檢測。這也可能意味著連線的裝置不支援 PoE。
- **overload** - 超過 PoE out 電流限制，埠電源被關閉。有關埠限制，請參閱各型號的規格。
- **voltage-too-low** - PD 無法使用 PSE 提供的電壓供電（例如，Vmin =>30V，但僅提供 24V）。
- **voltage-too-high** - 連線的裝置被檢測為 PoE in 裝置，但 PSE 的輸出電壓高於 PD 支援的範圍。
- **current-too-low** - PD 抽取的電流（低於 10 mA）低於正常 PoE out 裝置應有的電流。
- **no-valid-PSU** - 未檢測到有效的電源單元：PSE 沒有足夠或具備相應功率能力的電源來為該埠提供 PoE out，因此不施加電源。支援的電源組合見[供電要求](#powering-requirements)。
- **lldp-power-off** - 板卡透過 PoE in 受電，且從上游 PSE 收到的 LLDP 批准功率預算不足以給板卡自身的 PoE out 埠供電。
- **low-voltage-pd-detected** - 連線的 PD 僅支援低電壓，無法使用當前選擇的電壓從此 PSE 受電。為避免損壞 PD，不施加電源。請使用低壓 PSE 為該 PD 供電，或在具有可切換電壓模式的 PSE 上將埠切換為低電壓（`poe-voltage=low`）。
- **voltage-on-poe-in** - 意外在 PoE out 埠上檢測到電壓，這可能發生在兩種情況下：
  - **外部電源** - 另一臺裝置正在向該埠供電（PoE in 電壓）。
  - **內部故障** - 該埠上的 PoE out 電路可能已損壞。
- **low-voltage-too-low** - PSE 上的低輸入電壓過低，無法為 PD 供電；不施加電源。
- **disabled** - 該埠的所有檢測和電源均已關閉（`poe-out=off`）。
- **power_reset** - PSE 控制器正在復位電源，例如在 PoE 控制器升級期間、執行電源迴圈命令時或 ping 失敗時（power-cycle-ping）。
- **controller-init** - PSE 控制器初始化。
- **controller-upgrade** - PSE 控制器正在升級。
- **controller-error** - PSE 控制器無響應。

### PoE in 埠 {#poe-in-ports}

:::note
PoE in 監控僅在支援帶 LLDP 的 PoE in 的裝置上可用。較舊的裝置不會在監控中顯示 PoE in 埠。
:::

監控 **PoE in** 埠(`port-type: poe-in`)時,監控會顯示裝置透過 PoE 接收的電力的資訊,例如在支援 802.3bt PoE in 的板卡上:

```ros
/interface/ethernet/poe/monitor ether1
```

```
              name: ether1
         port-type: poe-in
```

監控還可能顯示 `power-limiting port` 訊息。這表示 PD(本裝置)在受限功率下供電,因為 LLDP 協商批准的功率低於 PD 請求的功率。

### SNMP {#snmp}

可以使用 SNMP 協定監控 PoE out 數值。必須在 PSE 上啟用 [SNMP](../diagnostics-monitoring-and-troubleshooting/snmp.md)。

可用的 SNMP OID:

| OID | 值 |
| :-- | :-- |
| 1.3.6.1.4.1.14988.1.1.15.1.1.1 | 介面 ID |
| 1.3.6.1.4.1.14988.1.1.15.1.1.2 | 介面名稱 |
| 1.3.6.1.4.1.14988.1.1.15.1.1.3 | PoE out 狀態(與 [monitor](#monitoring) `poe-out-status` 顯示的值相同) |
| 1.3.6.1.4.1.14988.1.1.15.1.1.4 | 電壓,單位 dV(分伏) |
| 1.3.6.1.4.1.14988.1.1.15.1.1.5 | 電流,單位 mA |
| 1.3.6.1.4.1.14988.1.1.15.1.1.6 | 功耗,單位 dW(分瓦) |

也可以從 RouterOS 請求 SNMP 數值,例如 `snmp-walk` 會列印所有可用 PoE out 埠的當前電流 mA:

```ros
/tool/snmp-walk address=10.155.149.252 oid=1.3.6.1.4.1.14988.1.1.15.1.1.5
```

要獲取非常具體的 OID 值,請使用 `snmp-get` 工具(顯示 ether3 介面上的當前 mA):

```ros
/tool/snmp-get address=10.155.149.252 oid=1.3.6.1.4.1.14988.1.1.15.1.1.5.3
```

## 日誌與通知 {#logging-and-notifications}

### 日誌 {#logging}

PoE 事件預設會被[記錄](../diagnostics-monitoring-and-troubleshooting/log/index.md)。PoE out 狀態變化使用 `poe-out` 主題,PoE in 事件(例如透過 PoE 供電的板卡上的 LLDP 功率協商)使用 `poe-in` 主題。重要事件(例如過載或短路)以 "warning" 主題記錄,資訊性狀態變化以 "info" 主題記錄,例如:

```
2026-10-08 11:42:45 poe-out,info ether16 detected poe-out status: on
```

為避免在 PD 因 current-too-low 而未供電時產生不必要的日誌,RouterOS 會過濾此類事件,每 512 次 current-too-low 事件才記錄一條日誌。

`poe-out` 和 `poe-in` 主題遵循標準[日誌](../diagnostics-monitoring-and-troubleshooting/log/index.md)機制——它們可以像其他任何主題一樣被排除、按嚴重程度過濾,或傳送到單獨的日誌目標。

詳細的 LLDP 功率協商訊息使用 "debug" 主題,例如:

```
06:56:50 poe-out,debug ether4 LLDP TLV 25.0W request denied : hw-limit
```

可能的 LLDP 功率請求被拒絕的原因:

| 原因 | 描述 |
| :-- | :-- |
| **budget** | 請求的功率超過 PSE 的總預算。 |
| **hw-limit** | 請求的功率超過硬體支援的上限(受 PSU 影響)。 |
| **low-voltage** | 向低壓埠發起 LLDP 請求。 |
| **off** | 埠已關閉。 |
| **class-limit** | LLDP 請求的功率超過該等級所能提供的功率。 |
| **cmd-failed** | RouterOS 無法向控制器發出請求。 |

### GUI/CLI 警告 {#guicli-warnings}

重要的 PoE 相關問題會以警告形式顯示:在 Winbox / WebFig 的介面列表(Interfaces 下)、CLI 介面列印輸出中的標誌註釋、[monitor](#monitoring) 中的埠狀態,以及[日誌](#logging-and-notifications)中。

觸發警告的 PoE out 狀態:

| 狀態 | 描述 |
| :-- | :-- |
| **overload** | 超過 PoE out 電流限制。 |
| **short-circuit** | 在埠上檢測到短路。 |
| **current-too-low** | 所連線的 PD 拉取的電流低於應有值。 |
| **voltage-on-poe-in** | 在埠上檢測到意外電壓(例如另一臺裝置正在向它供電)。 |

## PoE 輸出 {#poe-out}

### 如何選擇 PoE PSE {#how-to-choose-your-poe-pse}

此表可幫助您選擇最適合需求的 PSE 裝置。

<WideTable>

| 裝置名稱 | 軟體 | PoE out 埠數 | PoE 型別 | 電源輸入 | 低壓 PoE out 電流限制,A | 高壓 PoE out 電流限制,A | 最大總輸出功率,W |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **OmniTIK 5 PoE** | RouterOS | 4 | 無源 | 僅 PoE in(11-30 V) | 1 |  | 60 |
| **RB260GSP** | SwOS | 4 | 無源 | DC 插孔 / PoE in(11-30 V) | 1 |  | 60 |
| **hEX PoE lite / PowerBox** | RouterOS | 4 | 無源 | DC 插孔 / PoE in(8-30 V) | 1 | - | 60 |
| **OmniTIK 5 PoE ac** | RouterOS | 4 | 無源、af/at | 僅 PoE in(12-57 V) | 1 | 0.45 | 102 |
| **hEX PoE / PowerBox Pro** | RouterOS | 4 | 無源、af/at | DC 插孔 / PoE in(12-57 V) | 1 | 0.45 | 102 |
| **RB5009UPr+S+** | RouterOS | 8 | 無源、af/at | DC 插孔 / 2 針 / PoE in(24-57 V) | 0.9 | 0.44 | 130 |
| **netPower Lite 8P** | SwOS | 8 | 無源、af/at | 3× 2 針端子(24-57 V) | 1 | 0.64 | 120 |
| **CRS112-8P-4S-IN** | RouterOS | 8 | 無源、af/at | 2× DC 插孔(18-28 V / 48-57 V) | 1 | 0.45 | 150 |
| **CRS418-8P-8G-2S+RM** | RouterOS | 8 | 無源、af/at | AC(2 個 PSU 插槽) | 1.1 | 0.56 | 150 |
| **CSS610-8P-2S+IN** | SwOS | 8 | 無源、af/at | AC &amp; DC 48-57 V | 1 | 0.625 | 140 |
| **CRS320-8P-8B-4S+RM** | RouterOS / SwOS | 16 | 無源、af/at、bt | AC(2 個 PSU 插槽) | - | 0.56 (af/at) / 1.67 (bt) | 963 |
| **netPower 16P** | RouterOS / SwOS | 16 | 無源、af/at | 2× DC 插孔(18-30 V / 48-57 V) | 1.1 | 0.6 | 160 |
| **CRS328-24P-4S+RM** | RouterOS / SwOS | 24 | 無源、af/at | AC | 1 | 0.45 | 450 |
| **CRS354-48P-4S+2Q+RM** | RouterOS / SwOS | 48 | 無源、af/at | AC | 1 | 0.57 | 700 |

</WideTable>

:::tip
使用 PoE out 為其他裝置供電時,請使用至少 18V 的輸入電壓。
:::

### 設定 {#settings}

#### 全域性設定 {#global-settings}

**子選單：** `/interface/ethernet/poe/settings`

某些 MikroTik PoE out 裝置支援全域性 PoE 設定

| 屬性 | 說明 |
| :-- | :-- |
| **ether1-poe-in-long-cable** (*yes \| no*) | 當裝置自身透過長線纜以 PoE in 供電時，將其設定為 "yes"。它會停用嚴格的輸入電流監測（短路檢測），以免長線纜被錯誤地檢測為短路。**這是一項潛在危險的設定，應謹慎使用。** 它還可能影響由 DC 接頭供電的 PSE 的 PoE out 行為 |
| <strong>psuX-max-power</strong><br/><strong>jack-max-power</strong><br/><strong>2pin-max-power</strong> | 指定可從給定電源（PSU、DC 插孔或 2 針端子）獲取的最大功率（瓦特）。預設值：**96W** |
| **poe-in-max-power** | 指定當裝置（PSE）自身透過 PoE in 供電時，PoE 注入器（例如 802.3bt）可提供的最大功率（瓦特） |
| **routerboard-max-self-power** | 指定裝置為自身供電預留的功率。只讀。 |
| **routerboard-max-total-power** | 板卡自身的最大功耗，不含 PoE out。它用於在 PoE 預算由 PSU 功率決定的裝置上計算 PoE out 預算（PoE 預算 = PSU 功率 − 板卡功率）。只讀。 |
| **poe-out-limit-power** | PoE out 總預算上限。只讀。 |
| <strong>psuX-poe-out-max-power</strong><br/><strong>jack-poe-out-max-power</strong><br/><strong>2pin-poe-out-max-power</strong><br/><strong>poe-in-poe-out-max-power</strong> | 每個電源（PSU、DC 插孔、2 針端子或 PoE in 注入器）的 PoE out 限制（瓦特）。只讀。 |
| **version** | PoE 控制器（ATtiny）韌體版本。只讀。 |

#### 埠設定 {#port-settings}

**子選單：** `/interface/ethernet/poe`

可以在此選單中按埠配置 PoE out。每個埠都可以獨立控制。

| 屬性 | 描述 |
| :-- | :-- |
| **name** () | 介面名稱。 |
| **port-type** () | 顯示該埠是否支援 PoE out、PoE in 或兩者(poe-out、poe-in、poe-in/poe-out)。只讀。 |
| **poe-out** (*auto-on \| forced-on \| forced-on-a \| forced-on-bt \| off*; 預設值：**auto-on**) | 指定 PoE out 狀態。auto-on - 首先檢查埠上的電阻,僅當電阻在 3kΩ 到 26.5kΩ 範圍內時才施加電源。forced-on - 停用電阻檢測,並始終在 B 對(alt)上提供電源。off - 該埠的所有檢測和供電均被關閉。在支援 802.3bt PoE out 的 PSE 上的附加狀態:forced-on-a - 與 forced-on 相同,但在 A 對(main)上提供電源。forced-on-bt - 與 forced-on 相同,但在全部 4 對線上提供電源(僅可從 CLI 使用,無法在 Winbox/WebFig 中選擇此狀態)。**注意:** 無論選擇哪種 PoE out 狀態,短路和過載保護始終開啟。 |
| **poe-priority** (*integer: 0..99*; 預設值：**10**) | poe-priority 指定 PoE out 埠的重要性,當達到 PoE out 總限制時,埠優先順序最低的介面將首先被斷電。最高優先順序為 0,最低優先順序為 99。如果有 2 個或更多埠具有相同優先順序,則埠號最小的埠優先順序更高。每 6 秒會檢查一次因埠優先順序而被關閉的埠是否可以提供 PoE out。 |
| **poe-voltage** (*auto \| low \| high*; 預設值：**auto**) | 此功能允許在 PoE out 埠上手動切換兩種電壓輸出。它僅對具有可切換電壓模式的 PSE 生效([CRS112-8P-4S-IN](https://mikrotik.com/product/crs112_8p_4s_in)、[CRS328-24P-4S+RM](https://mikrotik.com/product/crs328_24p_4s_rm)、[netPower 16P](https://mikrotik.com/product/netpower_16p)、[CRS354-48P-4S+2Q+RM](https://mikrotik.com/product/crs354_48p_4s_2q_rm))。 |

從 RouterOS 7.15 開始,舊的 **poe-lldp-enabled** 埠屬性已被移除。PSE 與 PD 之間的 LLDP 功率協商透過[鄰居發現](../cli-reference/ip/neighbor/discovery-settings.md)的 `lldp-poe-power` 屬性進行配置。

#### 電源迴圈設定 {#power-cycle-settings}

RouterOS 提供了使用 ping 監控 PD,並在主機無響應時對 PoE out 埠進行電源迴圈的功能。power-cycle-ping 功能可以在 `/interface/ethernet/poe` 選單下啟用。

| 屬性 | 描述 |
| :-- | :-- |
| **power-cycle-ping-enabled** (*yes \| no*; 預設值：**no**) | 啟用 ping 看門狗,如果主機不響應 ICMP 或 MAC-Telnet 封包,則對埠進行電源迴圈。 |
| **power-cycle-ping-address** (*IPv4 \| IPv6 \| MAC*) | 將被監控的地址。從 RouterOS 6.46beta16 開始,如果配置了 IP 地址,則需要有一條通往 PD 的活動路由,因此請確保 PSE 可以訪問 PD。如果指定的是 MAC 地址,PSE 將僅從指定的乙太網介面傳送 MAC-Telnet ping 請求。在配置 [bridge vlan-filtering](../bridging-and-switching/index.md#bridge-vlan-filtering) 或某種 [VLAN 交換](../bridging-and-switching/user-guides/basic-vlan-switching.md)時,建議使用 IP 地址來監控您的 PD。 |
| **power-cycle-ping-timeout** (*time: 0..1h*; 預設值：**5s**) | 如果主機在超過該超時時間後仍無響應,則 PoE out 埠會關閉 5s。 |
| **power-cycle-interval** (*time \| none*; 預設值：**none**) | 每隔指定間隔定期對 PoE out 埠進行電源迴圈(關閉電源 5s 後再開啟)。與 power-cycle-ping 功能無關。 |

如果啟用了 power-cycle-ping 功能,[監控](#monitoring)還會顯示被監控主機的狀態以及距離下次電源迴圈的時間。

### LEDs {#leds}

大多數裝置為每個埠用一個 LED 指示 PoE out 狀態——同一個 LED 可以以不同顏色亮起:

| LED | PoE out 狀態 |
| :-- | :-- |
| 紅色 | **Powered-on** - 在不支援電壓選擇的型號上無論電壓如何都顯示紅色;在支援電壓選擇的型號和 802.3bt 型號上,表示 PD 由高壓(802.3af/at)供電 |
| 綠色 | **Powered-on**,PD 使用低壓(具有可選電壓輸出的型號) |
| 紫色 | **Powered-on**,PD 透過全部 4 對線供電(802.3bt) |
| 閃爍(任意顏色) | **Short-circuit** 或 **overload** |

#### 特定型號的 LED 行為 {#model-specific-led-behavior}

- [CRS112-8P-4S-IN](https://mikrotik.com/product/crs112_8p_4s_in)、[netPower 16P](https://mikrotik.com/product/netpower_16p) - 所有 PoE LED 閃爍:其中一個埠插入了電壓不正確的 PSU。

### 工作原理 {#how-it-works}

#### PoE out 模式 {#poe-out-modes}

- **auto-on** - 板卡檢查所連線埠上的電阻,僅當電阻在 3kΩ 到 26.5kΩ 範圍內時才施加電源:
  - 施加電源後,PSE 會持續檢查過載和短路;
  - 如果電纜被拔出,埠會返回檢測狀態並保持關閉,直到再次檢測到合適的 PD。
- **forced-on** - 停用電阻檢測,即使沒有連線電纜也會施加電源:
  - 根據配置的 `poe-out` 狀態(`forced-on`、`forced-on-a` 或 `forced-on-bt`)線上對上施加電源;
  - PSE 仍會持續檢查過載和短路;
  - 電纜拔出後,埠仍保持供電。
- **off** - 埠上的 PoE out 被關閉,不進行檢測,該介面的行為類似於普通乙太網埠。

#### PoE out 限制 {#poe-out-limits}

以下 PoE out 特性因 PSE 型號而異——請檢視裝置的規格頁面:

- **埠限制** - PoE out 埠受特定電壓下支援的最大電流限制。低壓裝置(最高 30 V)和高壓裝置的最大電流通常不同。
- **總限制** - PSE 還有 PoE out 總電流限制,即使單個埠限制允許,也不能超過該總限制。總限制的範圍因型號而異:在限制按埠組(例如每 8 埠段)計算的板卡上,功率優先順序也在該埠組內生效。
- **極性** - 大多數 MikroTik PSE 使用相同的 PoE out 引腳極性,[Mode B](https://en.wikipedia.org/wiki/Power_over_Ethernet#Pinouts) - 4,5 (+) 和 7,8 (-)。具有 802.3bt 埠的 PSE 使用兩種極性:1,2 (+) 和 3,6 (-) 作為 Mode A,4,5 (+) 和 7,8 (-) 作為 Mode B。

#### 安全性 {#safety}

PSE 具有以下安全特性:

- **相容性檢測** - 在 auto-on 模式下,首先檢查埠上的電阻,僅當電阻在 3kΩ 到 26.5kΩ 的允許範圍內時才施加電源。超出此範圍的非標準 PD 不會獲得供電。
- **過載保護** - 當 PoE out 埠通電時,會持續檢查是否過載。如果檢測到過載,會關閉該埠的 PoE out 以避免損壞 PD 或 PSE,並在幾秒後再次開啟以檢查情況是否發生變化。
- **短路檢測** - 當 PoE out 埠施加電源時,PSE 會持續檢查是否短路。如果檢測到短路,會關閉該埠的電源以避免對 PD 和 PSE 造成進一步損壞,並持續檢查該埠,直到環境恢復正常。

#### 特定型號的功能 {#model-specific-features}

某些 PSE 具有獨立的 8 埠段。在此類裝置上,PoE out 獨立於 RouterOS 執行:您可以重啟或升級 RouterOS,而受電裝置不會斷電。例外情況是 PoE 控制器韌體升級,在此期間電源會中斷——此類升級總會在 RouterOS 變更日誌中提及。

PoE 預算的定義方式也因型號而異:在某些裝置上,預算限制針對整個板卡設定,在另一些裝置上則按 8 埠段設定。同樣,PoE out 優先順序在預算範圍內生效:在按段設定預算的板卡上,優先順序按段應用;在按整板設定預算的板卡上,優先順序全域性應用。

## PoE 輸入 {#poe-in}

MikroTik 裝置也可以自身透過乙太網供電,充當 PD(受電裝置)。PoE in 埠在同一個 `/interface/ethernet/poe` 選單中管理,可以在監控輸出中透過 `port-type: poe-in` 識別。

### 配置 {#configuration-1}

PoE in 相關選項是[全域性設定](#global-settings)的一部分,例如:

- **poe-in-max-power** - 告知裝置為其供電的 PoE 注入器(例如 802.3bt)的最大功率,以便正確計算 PoE out 預算;
- **ether1-poe-in-long-cable** - 當裝置透過長電纜供電時,停用嚴格的輸入/輸出電流監控。

### 供電要求 {#powering-requirements}

透過 PoE in 為裝置供電時,電源必須與裝置的輸入相匹配。請檢視裝置規格頁面以瞭解支援的 PoE in 電壓範圍和標準:

- PSU 或 PoE 注入器的輸出電壓必須在裝置的輸入電壓範圍內(例如無源 PoE 型號上的 8-30 V 或 12-57 V)。電壓過低可能導致裝置無法啟動或在負載下重啟,電壓過高則可能損壞裝置。
- 電源必須提供足夠的功率供裝置自身使用,如果裝置還為其他裝置供電,還要滿足 PoE out 預算——請參見 [PoE out 限制](#poe-out-limits)和[設定](#global-settings)瞭解預算的計算方式。
- MikroTik 裝置上的無源 PoE in 使用 Mode B 極性(引腳 4,5 (+) 和 7,8 (-)),但具有 802.3bt PoE in 的裝置除外,它們接受全部四對線的供電。
- 使用 802.3af/at PSE 或無源 2 對線注入器為支援 PoE out 和 802.3bt(PoE++)PoE in 的裝置供電不被視為有效電源:PoE out 將無法工作,監控會在 PoE out 埠上顯示 `no-valid-PSU` 狀態。請改用 802.3bt PSE 或 4 對線無源注入器。

當裝置本身透過 PoE 供電並使用 LLDP 功率協商時(參見[鄰居發現](../cli-reference/ip/neighbor/discovery-settings.md)的 `lldp-poe-power`),裝置會將其請求的功率告知上游 PSE,由上游 PSE 相應地批准功率。如果批准的功率低於請求的功率,監控會顯示 `power-limiting port` 訊息(參見 [PoE in 埠](#poe-in-ports)),並且某些 PoE out 埠可能不會供電。

## 示例 {#examples}

### PoE 輸出 {#poe-out-1}

#### 為非標準 PD 供電(forced-on) {#powering-non-standard-pds-forced-on}

在 `auto-on` 模式下,不呈現所需電阻(3kΩ 到 26.5kΩ)的 PD 不會獲得供電。請改用 `forced-on` 為其供電:

```ros
/interface/ethernet/poe set ether5 poe-out=forced-on
```

在支援 802.3bt 的 PSE 上,`forced-on-a` 和 `forced-on-bt` 透過 A 對或全部四對線為 PD 供電(僅限 CLI,參見[埠設定](#port-settings))。為節省電力並提高安全性,請使用 `poe-out=off` 關閉未使用埠上的 PoE out。

#### 埠優先順序 {#port-priorities}

PoE out 優先順序定義了達到 PoE out 總限制時哪些埠會首先斷電。優先順序 *0* 最高,*99* 最低:

```ros
/interface/ethernet/poe set ether2 poe-priority=10
/interface/ethernet/poe set ether3 poe-priority=13
/interface/ethernet/poe set ether4 poe-priority=11
/interface/ethernet/poe set ether5 poe-priority=14
```

如果超出總限制,優先順序最低的埠會首先被停用(ether5,然後是 ether3)。被停用的埠每隔幾秒會重新檢查,一旦預算允許,會按相反順序重新供電。

當多個埠具有相同優先順序時,埠號最小的埠優先:在所有埠優先順序相同的情況下,ether5 首先被停用,然後是 ether4,然後是 ether3。

#### 定時電源迴圈 {#scheduled-power-cycle}

使用 [power-cycle-interval](#power-cycle-settings) 定期對 PoE out 埠進行電源迴圈,例如每天重啟一次所連線的裝置:

```ros
/interface/ethernet/poe set ether5 power-cycle-interval=1d
```

#### 電源迴圈看門狗(power-cycle-ping) {#power-cycle-watchdog-power-cycle-ping}

監控所連線的 PD,並在主機無響應時對該埠進行電源迴圈:

```ros
/interface/ethernet/poe set ether1 power-cycle-ping-enabled=yes power-cycle-ping-address=192.168.88.10 power-cycle-ping-timeout=30s
```

ether1 上的 PD 透過 ICMP ping 進行監控。如果 192.168.88.10 上的主機在超過 30s 內無響應,該埠的 PoE out 會關閉 5s。

#### 監控 PoE out {#monitoring-poe-out}

```ros
/interface/ethernet/poe/monitor ether9
```

```
                name: ether9
             poe-out: auto-on
      poe-out-status: powered-on
     poe-out-voltage: 54.2V
     poe-out-current: 449mA
       poe-out-power: 24.3W
  poe-out-power-pair: b
```

#### 檢查功率限制 {#checking-the-power-limits}

使用全域性設定檢視 PoE out 預算和裝置的只讀功率限制:

```ros
/interface/ethernet/poe settings print
```

```
               jack-max-power: 96W
               2pin-max-power: 150W
   routerboard-max-self-power: 20W
  routerboard-max-total-power: 30W
          poe-out-limit-power: 240W
       jack-poe-out-max-power: 66W
       2pin-poe-out-max-power: 120W
```

在本示例中,板卡自身預留 20 W,PoE out 的總預算為 240 W,其中透過 DC 插孔供電時可使用 66 W,或透過 2 針端子供電時可使用 120 W。

### PoE 輸入 {#poe-in-1}

當裝置本身由 PoE 注入器(例如 802.3bt)供電時,請使用 [poe-in-max-power](#global-settings) 全域性設定宣告注入器的功率,以便正確計算 PoE out 預算:

```ros
/interface/ethernet/poe settings set poe-in-max-power=144
```

## 故障排除 {#troubleshooting}

如果 PD 在使用 PoE out 供電時無法啟動或意外重啟,請按以下檢查清單逐項排查:

1. **首先檢查埠狀態。** 在該埠上執行 `/interface/ethernet/poe/monitor`——`poe-out-status` 的值通常直接指出問題所在,例如 `overload`、`short-circuit`、`voltage-too-low` 或 `no-valid-PSU`。參見完整的[狀態列表](#poe-out-statuses)。
2. **檢查日誌。** PoE 狀態變化以 `poe-out` 主題記錄,參見[日誌](#logging)。
3. **嘗試更換電纜。** 直接在 PSE 上使用短的高質量跳線,以排除佈線問題。
4. **檢查 PSE 的電源。** 使用 `/interface/ethernet/poe settings print` 檢視限制:
   - PSU 必須覆蓋 PSE 自身的功耗、所有受電 PD 的功耗,並留出約 10% 的餘量。
   - 輸入電壓過低可能導致 PD 出現 `voltage-too-low` 狀態(例如 DC 電纜過長或 PSU 負載過大)。
   - 在具有 802.3bt PoE in 的板卡上,請確保裝置由有效電源供電,否則會出現 `no-valid-PSU` 狀態且 PoE out 保持關閉——參見[供電要求](#powering-requirements)。
5. **對照 PD 的資料手冊檢查相容性:**
   - 同時檢查 PSE 和 PD 的規格:無源 PoE in 裝置(例如輸入最高 30 V)不能由更高電壓的電源供電。在無源 PSE 上,PoE out 電壓與 PSE 輸入電壓相同,因此使用 48 V PSU 供電的 PSE 也會在其 PoE out 埠上輸出 48 V——對於低壓 PD,請使用低壓 PSU 或具有可選電壓輸出的 PSE。
   - PD 支援的輸入電壓必須與 PSE 輸出電壓相匹配。
   - PSE 與 PD 之間的引腳極性差異(Mode A 或反接)。
6. **對非標準 PD 嘗試 `forced-on`**,在此之前請確認 PD 支援 PSE 的電壓和極性(參見[示例](#powering-non-standard-pds-forced-on))。
7. **更新 RouterOS。** PoE 功能會定期獲得修復和更新,請確保執行最新的 [RouterOS 版本](https://mikrotik.com/download)。
8. **隔離 PD。** 用匹配的無源 PoE 注入器為其供電。如果透過注入器可以工作,但透過 PSE 埠不能,則問題出在該埠或其配置上。

如果以上步驟均無法解決問題,請收集監控輸出和日誌,生成 [supout.rif 檔案](../cli-reference/system/sup-output.md),並聯系 MikroTik 支援。
