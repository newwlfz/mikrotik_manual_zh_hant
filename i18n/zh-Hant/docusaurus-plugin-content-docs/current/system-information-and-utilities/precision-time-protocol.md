---
sidebar_key: "system-information-and-utilities/precision-time-protocol"
sidebar_position: 12
title: "精確時間協定"
sidebar_label: "精確時間協定"
description: "RouterOS 上的精確時間協定（PTP，IEEE 1588-2008）時鐘同步：支援的硬體、配置檔案（802.1AS、AES67、G.8275.1、SMPTE 2059）、埠、硬體時間戳與同步監控。"
tags:
  - 'ptp'
  - 'precision-time-protocol'
  - 'ieee-1588'
source: https://manual.mikrotik.com/docs/system-information-and-utilities/precision-time-protocol
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Precision Time Protocol（PTP，IEEE 1588-2008，也稱為 PTPv2）可在區域網路內同步時鐘，這在電信、廣播、音訊製作和工業自動化中非常重要。MikroTik 的實現具有以下特性：

- 兩步 Ordinary Clock 和 Boundary Clock。
- 硬體時間戳，可將時鐘同步精度提升到納秒級。
- IPv4 和二層組播傳輸模式。
- 端到端（E2E）和對等（P2P）延遲機制。
- 配置檔案：802.1AS（AVB/TSN，依據 IEEE 802.1AS-2020）、AES67（IP 音訊）、G.8275.1（電信頻率與相位同步）和 SMPTE 2059（專業廣播）。

:::info
PTP 支援取決於硬體；請參閱[支援的裝置](#supported-devices)。未列在那裡的裝置根本沒有 `/system/ptp` 選單。MGMT（管理）埠在任何裝置上都不支援 PTP；“所有埠”指所有資料介面，不包括 MGMT 埠。
:::

## 配置 PTP {#configure-ptp}

配置分為兩步：在 [`/system/ptp`](../cli-reference/system/ptp/index.md) 中建立 PTP 配置檔案，然後在 [`/system/ptp/port`](../cli-reference/system/ptp/port.md) 中分配參與該配置檔案的埠。

建立一個配置檔案例項（本示例使用 802.1AS 配置檔案）：

```ros
/system/ptp/add name=ptp1 profile=802.1as
```

只有當鏈路上的所有時鐘運行同一個配置檔案時，PTP 才會同步，因此請使該配置檔案（以及隨之確定的域、傳輸和延遲模式）與您的 grandmaster 及 PTP 網路中的其餘部分相匹配。

保留為 `auto` 的配置檔案引數會採用其配置檔案所定義的值（例如 802.1AS 會設定 `priority1=246`、`priority2=248`、二層傳輸和 P2P 延遲測量——各配置檔案的預設值列在 CLI 參考行中）。只有在所選標準允許時才手動更改它們；G.8275.1、802.1AS、SMPTE 2059 和 AES67 各自定義了自己所需的值。

```ros
[admin@MikroTik] > /system/ptp/print
 Flags: I - inactive, X - disabled
 0   name="ptp1" priority1=auto priority2=auto delay-mode=auto transport=auto profile=802.1as domain=auto
```

然後分配該配置檔案的埠。此處 sfp28-12 連線到 grandmaster 時鐘，而 sfp28-1 和 sfp28-2 連線到普通時鐘（從時鐘）：

```ros
/system/ptp/port/add interface=sfp28-1 ptp=ptp1
/system/ptp/port/add interface=sfp28-2 ptp=ptp1
/system/ptp/port/add interface=sfp28-12 ptp=ptp1
```

埠也可以固定其角色，而不是讓最佳主時鐘演算法決定：使用 `role=bmca` 時，該演算法選擇 master 或 slave；在已知拓撲中，可以直接用 `role=master` 或 `role=slave` 固定埠。[`/system/ptp`](../cli-reference/system/ptp/index.md) 中的 `ptp-mode` 用於在 ordinary-clock 和 transparent-clock 行為之間進行選擇。

### VLAN 埠上的 PTP {#ptp-on-vlan-ports}

當 PTP 埠同時也是你的邊界時鐘裝置上 VLAN 的一部分時，對於每個包含 PTP 埠的條目，你必須在[橋 VLAN 表](../bridging-and-switching/user-guides/bridge-vlan-table.md)中將橋介面新增為未標記埠。繼續使用 sfp28-1 位於 VLAN 10、sfp28-2 位於 VLAN 20 的示例：

```ros
/interface/bridge/add name=bridge1
/interface/bridge/port/add bridge=bridge1 interface=sfp28-1 pvid=10
/interface/bridge/port/add bridge=bridge1 interface=sfp28-2 pvid=20
/interface/bridge/vlan/add bridge=bridge1 vlan-ids=10 \
    untagged=bridge1,sfp28-1
/interface/bridge/vlan/add bridge=bridge1 vlan-ids=20 \
    untagged=bridge1,sfp28-2
```

這是必要的，因為橋介面充當通往 CPU 的橋埠。因此，必須將其與 PTP 埠一起包含在 VLAN 表中，以便封包能夠從物理埠正確接收，並透過橋轉發到 CPU。

如果 PTP 改為透過 trunk 埠以帶標記方式到達，請直接在 PTP 埠上使用 [`/system/ptp/port`](../cli-reference/system/ptp/port.md) 中的 `vlan-id` 設定標記。

:::note
這適用於 IPv4 和 L2-forwardable (01-1B-19-00-00-00) 傳輸模式。唯一的例外是 L2-non-forwardable (01-80-C2-00-00-0E)，在這種情況下，網橋不必包含在 bridge VLAN 表中。

要檢視每個配置檔案的預設（auto）傳輸模式值，請參閱 CLI 參考中 [`transport`](../cli-reference/system/ptp/index.md) 的說明。
:::

### PTP 與 IGMP snooping {#ptp-with-igmp-snooping}

如果已在橋上啟用 IGMP snooping，並且 VLAN 按如上所示配置，請為每個包含使用 **IPv4** (224.0.1.129) 作為傳輸模式的 PTP 埠的 VLAN 手動新增靜態組播資料庫 (MDB) 條目。這可確保 PTP 組播流量正確轉發：

```ros
/interface/bridge/mdb/add group=224.0.1.129 bridge=bridge1 \
    ports=bridge1 vid=10
/interface/bridge/mdb/add group=224.0.1.129 bridge=bridge1 \
    ports=bridge1 vid=20
```

在 PTP 設定中，僅當 IGMP snooping 與 VLAN 一起啟用時，才需要靜態 MDB 條目。

## 監控同步 {#monitor-synchronization}

首先檢查埠是否已啟動並正常執行：

```ros
/system/ptp/status/print
```

`state`、`delay` 和 `as-capable` 列顯示在同步穩定之前埠卡在哪裡。

然後使用 [`/system/ptp/monitor`](../cli-reference/system/ptp/monitor.md) 監控 profile 例項（按編號或名稱）：

```ros
/system/ptp/monitor ptp1
```

同步時鐘的示例：

```text
name: ptp1
clock-id: 64:D1:54:FF:FE:EB:AD:C7
priority1: 246
priority2: 248
i-am-gm: no
gm-clock-id: 64:D1:54:FF:FE:EB:AE:C3
gm-priority1: 100
gm-priority2: 248
master-clock-id: 64:D1:54:FF:FE:EB:AE:C3
slave-port: ether1
freq-drift: 2690 ppb
offset: 3 ns
hw-offset: -889419842 ns
slave-port-delay: 306 ns
```

要關注的數值：`i-am-gm`/`gm-clock-id` 表示誰是 grandmaster，`offset` 是相對於主時鐘的時間誤差，`freq-drift` 是長期時鐘頻率校正，`slave-port-delay` 是測得的從埠單向路徑延遲。

## 支援的裝置 {#supported-devices}

- **CRS326-24G-2S+:** 僅支援千兆乙太網埠。
- **CRS328-24P-4S+:** 僅支援千兆乙太網埠。
- **CRS317-1G-16S+:** 所有埠均支援。
- **CRS326-24S+2Q+:** 支援 SFP+ 和 QSFP+ 介面。
- **CRS312-4C+8XG:** 所有埠均支援。
- **CRS318-16P-2S+:** 僅支援千兆乙太網埠。
- **CRS318-1Fi-15Fr-2S:** 僅支援 100M 乙太網埠。
- **CCR2116-12G-4S+:** 所有埠均支援。
- **CCR2216-1G-12XS-2XQ:** 所有埠均支援。
- **CRS518-16XS-2XQ:** 所有埠均支援。
- **CRS504-4XQ:** 所有埠均支援。
- **CRS510-8XS-2XQ:** 所有埠均支援。
- **CRS520-4XS-16XQ:** 所有埠均支援。
- **CRS320-8P-8B-4S+RM:** 僅支援千兆乙太網埠。
- **CRS326-4C+20G+2Q+:** 所有埠均支援。
- **RDS2216-2XG-4S+4XS-2XQ:** 所有埠均支援。

:::info
本節未列出的裝置不支援 Precision Time Protocol。
:::

## 技術細節 {#technical-details}

配置檔案會預設那些你保留為 `auto` 的引數值：

| 配置檔案 | priority1 | priority2 | 域 | transport | delay-mode |
| :-- | :-- | :-- | :-- | :-- |  :-- |
| default | 128 | 128 | 0 | ipv4 | e2e |
| 802.1AS | 246 | 248 | 0 | l2-non-forwardable | p2p |
| AES67 | 128 | 128 | 0 | ipv4 | e2e |
| G.8275.1 | 128 | 128 | 24 | l2-non-forwardable | e2e |
| SMPTE 2059 | 128 | 128 | 127 | ipv4 | e2e |

- IPv4 transport 將 PTP 主訊息組播到 224.0.1.129，並將對等延遲訊息組播到 224.0.0.107。
- L2-forwardable 使用組播 MAC 01-1B-19-00-00-00，PTP-unaware 網橋會轉發它；L2-non-forwardable 使用 01-80-C2-00-00-0E，符合標準的網橋無法轉發它，因此 PTP 通訊保持在本地鏈路上。
- 域將同一網路上的獨立 PTP 例項分隔開；允許的範圍因配置檔案而異（大多數配置檔案為 0-127，G.8275.1 為 24-43）。

有關所有引數，請參閱 [`/system/ptp`](../cli-reference/system/ptp/index.md)、[`/system/ptp/port`](../cli-reference/system/ptp/port.md)、[`/system/ptp/status`](../cli-reference/system/ptp/status.md) 和 [`/system/ptp/monitor`](../cli-reference/system/ptp/monitor.md) CLI 參考頁面。
