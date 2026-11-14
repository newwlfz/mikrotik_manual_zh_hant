---
sidebar_key: "system-information-and-utilities/precision-time-protocol"
sidebar_position: 12
title: "精確時間協定"
sidebar_label: "精確時間協定"
description: "MikroTik RouterOS 文件介紹了精確時間協定（PTP），用於在網路中實現亞微秒級時鐘同步，支援帶硬體時間戳的 IEEE 1588-2008，並提供多種配置檔案選項，包括面向特定行業的 802.1AS、AES67、G.8275.1 和 SMPTE。"
tags:
  - 'ptp'
  - 'precision-time-protocol'
  - 'ieee-1588'
source: https://manual.mikrotik.com/docs/7.25/system-information-and-utilities/precision-time-protocol
captured_at: '2026-11-04T11:22:13+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

精確時間協定 (PTP) 由電氣電子工程師學會 (IEEE) 制定，是一種用於在區域網路內同步時鐘的協定。在電信、金融和工業自動化等對精確計時至關重要的行業和應用中，它不可或缺。PTP 通常可確保亞微秒級的時間精度，但在滿足硬體要求時，也可以實現納秒級精度。MikroTik 的 PTP 實現支援 IEEE 1588-2008 (PTPv2)，幷包含硬體時間戳功能，可確保在納秒範圍內實現同步。有關 MikroTik PTP 功能的更多詳細資訊，請參閱下面的列表。

- 兩步式普通時鐘和邊界時鐘。
- 硬體時間戳，確保在納秒 (ns) 範圍內實現時鐘同步。
- IPv4 和二層 (L2) 組播傳輸模式。
- 端到端 (E2E) 和對等 (P2P) 延遲機制。
- IEEE 1588-2008 (PTPv2)。
- 配置檔支援：
  - 802.1AS：用於音訊影片橋接 (AVB) 和時間敏感網路 (TSN) 的計時與同步，基於 IEEE 802.1AS-2020。
  - AES67：高效能的 IP 音訊互操作性。
  - G.8275.1：在支援 PTP 的網路中進行頻率和相位同步。
  - SMPTE：專業廣播環境中的音訊/影片同步。

:::info
MikroTik PTP 支援取決於硬體；請參閱[支援的裝置。](./precision-time-protocol.md#supported-devices)
:::

## 常規屬性 {#general-properties}

**子選單：** `/system/ptp`

| 屬性 | 描述 |
| :-- | :-- |
| **port** | 用於新增、刪除或檢視已分配埠的子選單。 |
| **status** | 顯示 PTP 埠、其狀態以及從埠延遲的子選單。 |
| **comment** (*string*; 預設值： ) | PTP 配置檔的簡短描述。 |
| **name** (*string*; 預設值： ) | PTP 配置檔的名稱。 |
| **domain** (預設值：**auto**) | 用於區分不同 PTP 例項的識別符號。每個 PTP 配置檔定義自己允許的 domain 範圍和預設值：• 802.1AS 範圍：0–127，預設值：0 (auto) • AES67 範圍：0–127，預設值：0 (auto) • G.8275.1 範圍：24–43，預設值：24 (auto) • SMPTE 範圍：0–127，預設值：127 (auto) • Default 範圍：0–127，預設值：0 (auto) 注意：- “auto” 會選擇該配置檔的預設 domain 值。 |
| **delay-mode** (*auto \| e2e \| p2p*; 預設值：**auto**) | auto - 根據所使用的配置檔自動選擇延遲模式。e2e - 使用延遲請求-響應機制。p2p - 使用對等延遲機制。 |
| **priority1** (*integer [0..255]*; auto; 預設值：**auto**) | 參與 grandmaster 時鐘選舉的引數。 |
| **priority2** (*integer [0..255]*; auto; 預設值：**auto**) | 參與備用 grandmaster 時鐘選舉的引數。 |
| **profile**(*802.1as; aes67; g8275.1; smpte; default;* 預設值：**default**) | 每個配置檔都附帶自己預定義的 PTP 執行引數和選項 auto 值：802.1as 是 PTP 的適配版本，用於音訊影片橋接 (AVB) 和時間敏感網路 (TSN)。預設 (auto) 值：priority1=246, priority2=248, transport=l2-non-forwardable, delay-mode=p2p。aes67 配置檔用於高效能的 IP 音訊互操作性。預設 (auto) 值：priority1=128, priority2=128, domain=0, transport=ipv4, delay-mode=e2e。g8275.1 配置檔用於全 PTP 感知網路中的頻率和相位同步。預設 (auto) 值：priority1=128, priority2=128, domain=24, transport=l2-non-forwardable, delay-mode=e2e。smpte 配置檔用於專業廣播環境中音訊/影片裝置的同步。預設 (auto) 值：priority1=128, priority2=128, domain=127, transport=ipv4, delay-mode=e2e。default 配置檔為 PTPv2 預設配置，允許比其他配置檔更多的配置選項。預設 (auto) 值：priority1=128, priority2=128, domain=0, transport=ipv4, delay-mode=e2e。 |
| **transport** (*auto; ipv4; l2-forwardable; l2-non-forwardable;* 預設值：**auto**) | 要使用的傳輸協定：auto - 根據所使用的 PTP 配置檔自動選擇傳輸模式。ipv4 - 使用 IPv4 組播地址 224.0.1.129 用於 PTP 主訊息，224.0.0.107 用於 PTP 對等延遲訊息。l2-forwardable - 使用組播 MAC 地址 <code>01-1B-19-00-00-00</code>，該地址會透過不支援 PTP 的網路裝置轉發。l2-non-forwardable - 使用組播 MAC 地址 <code>01-80-C2-00-00-0E</code>，確保 PTP 訊息不會透過不支援 PTP 的網路裝置轉發。 |

## 配置 {#configuration}

在 MikroTik 裝置上配置精確時間協定 (PTP) 是一個簡單的過程。主要步驟包括建立 PTP 配置檔，並將相關埠分配給此配置檔以進行 PTP 操作。

#### 建立 PTP 配置檔 {#create-a-ptp-profile}

要建立 PTP 配置檔，請使用以下命令。在此示例中，我們使用 802.1as 配置檔，但你可以根據需要選擇其他可用配置檔：

```ros
/system/ptp/add name=ptp1 profile=802.1as
```

要驗證配置檔是否已成功建立，請執行：

```routeros
/system/ptp/print
```

輸出將顯示已建立的配置檔及其當前設定：

```routeros
 Flags: I - inactive, X - disabled 
 0   name="ptp1" priority1=auto priority2=auto delay-mode=auto transport=auto profile=802.1as domain=auto  
```

:::note
預設情況下，每個配置檔的引數都設定為“auto”，它會根據所選配置檔自動選擇合適的值。在進行手動調整之前，請驗證設定符合相關標準（例如 ITU-T G.8275.1、IEEE 802.1as、SMPTE、AES67）。
:::

#### 為 PTP 配置檔分配埠 {#assign-ports-to-the-ptp-profile}

作為最後一步，分配將參與 PTP 的埠。例如，讓我們包含幾個 sfp28 介面。SFP28-12 連線到 grandmaster 時鐘，而 SFP28-1 和 SFP28-2 連線到普通時鐘/從時鐘：

```ros
/system/ptp/port/add interface=sfp28-1 ptp=ptp1
/system/ptp/port/add interface=sfp28-2 ptp=ptp1
/system/ptp/port/add interface=sfp28-12 ptp=ptp1
```

#### VLAN 埠上的 PTP {#ptp-on-vlan-ports}

當 PTP 埠同時也是邊界時鐘裝置上 VLAN 的一部分時，對於包含 PTP 埠的每個條目，你必須在[橋 VLAN 表](../bridging-and-switching/user-guides/bridge-vlan-table.md)中將橋介面新增為未標記埠。

這是必要的，因為橋介面充當通往 CPU 的橋埠。因此，它必須與 PTP 埠一起包含在 VLAN 表中，以確保封包可以從物理埠正確接收，並透過橋轉發到 CPU。讓我們繼續使用之前的配置來更清楚地說明這一點：

```routeros
# 创建新的桥接接口
/interface/bridge/add name=bridge1

# 分配将属于此桥接的端口
/interface/bridge/port/add bridge=bridge1 interface=sfp28-1 pvid=10
/interface/bridge/port/add bridge=bridge1 interface=sfp28-2 pvid=20

# 为 Bridge VLAN Table 创建新条目
/interface/bridge/vlan/add bridge=bridge1 vlan-ids=10 untagged=bridge1,sfp28-1
/interface/bridge/vlan/add bridge=bridge1 vlan-ids=20 untagged=bridge1,sfp28-2
```

:::note
這適用於 IPv4 和 l2-forwardable (01-1B-19-00-00-00) 傳輸模式。唯一的例外是 l2-non-forwardable (01-80-C2-00-00-0E)，在這種情況下，無需將橋介面作為未標記埠新增到橋 VLAN 表中。

要檢查每個配置檔的預設 (auto) 傳輸模式值，請參閱“[常規屬性](./precision-time-protocol.md#general-properties)”部分。
:::

#### 使用 IGMP Snooping 的 PTP {#ptp-with-igmp-snooping}

如果橋上啟用了 IGMP snooping，並且 VLAN 按上一個示例配置，則必須為每個包含使用 **IPv4** (224.0.1.129) 作為傳輸模式的 PTP 埠的 VLAN 手動新增靜態組播資料庫 (MDB) 條目。這可確保 PTP 組播流量正確轉發。

```routeros
/interface/bridge/mdb/add group=224.0.1.129 bridge=bridge1 ports=bridge1 vid=10
/interface/bridge/mdb/add group=224.0.1.129 bridge=bridge1 ports=bridge1 vid=20
```

:::note
在 PTP 設定中，僅當 IGMP snooping 與 VLAN 一起啟用時，才需要靜態 MDB 條目。
:::

## 監控 {#monitoring}

要監控 PTP 配置檔的狀態和效能，請使用以下命令：

```ros
/system/ptp/monitor 0
```

輸出將提供有關配置檔執行狀態的詳細資訊：

```routeros
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

此資訊包括時鐘 ID、優先順序值和時間偏移等關鍵細節，這些對於監控 PTP 設定的準確性和同步至關重要。

#### 監控屬性 {#monitor-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **clock-id:** | 本地時鐘識別符號，用於在 PTP 網路中唯一標識該時鐘。 |
| **priority1:** | 用於 grandmaster 時鐘選舉的優先順序引數。值越低表示優先順序越高。 |
| **priority2:** | 用於備用 grandmaster 時鐘選舉的優先順序引數。值越低表示優先順序越高。 |
| **i-am-gm:** yes | no | 指示裝置是否為 grandmaster 時鐘（`yes`）或不是（`no`）。 |
| **gm-clock-id:** | grandmaster 時鐘的識別符號。這是提供主時間源的時鐘。 |
| **gm-priority1:** | 從從裝置看到的 grandmaster 時鐘的 `priority1` 值。 |
| **gm-priority2:** | 從從裝置看到的 grandmaster 時鐘的 `priority2` 值。 |
| **master-clock-id:** | PTP 通訊路徑中 master 時鐘的識別符號。根據網路拓撲，它可能是 grandmaster 時鐘或邊界時鐘。 |
| **slave-port:** | 裝置上連線到 master 或 grandmaster 時鐘的埠。 |
| **freq-drift:** | master 時鐘與從時鐘之間的頻率漂移，以十億分之一 (ppb) 為單位。這表示從時鐘的頻率偏離 master 時鐘頻率的程度。 |
| **offset:** | master 時鐘與從時鐘之間的時間差，以納秒 (ns) 為單位。這反映同步精度。 |
| **hw-offset:** | 與硬體時鐘的偏移差。 |
| **slave-port-delay:** | 封包在兩個裝置之間傳輸的時間延遲，以納秒 (ns) 為單位。此延遲可能受網路中使用的電纜和收發器質量的影響。 |
| **name**  | PTP 配置檔的名稱。 |

## 支援的裝置 {#supported-devices}

- **CRS326-24G-2S+：** 僅在千兆乙太網埠上支援。
- **CRS328-24P-4S+：** 僅在千兆乙太網埠上支援。
- **CRS317-1G-16S+：** 所有埠均支援。
- **CRS326-24S+2Q+：** SFP+ 和 QSFP+ 介面支援。
- **CRS312-4C+8XG：** 所有埠均支援。
- **CRS318-16P-2S+：** 僅在千兆乙太網埠上支援。
- **CRS318-1Fi-15Fr-2S：** 僅支援 100M 乙太網埠。

### RouterOS 7.16 及更高版本中新增的 PTP 支援 {#ptp-support-added-in-routeros-version-716-and-later}

- **CCR2116-12G-4S+：** 在所有埠上支援。
- **CCR2216-1G-12XS-2XQ：** 在所有埠上支援。
- **CRS518-16XS-2XQ：** 在所有埠上支援。
- **CRS504-4XQ：** 在所有埠上支援。
- **CRS510-8XS-2XQ：** 在所有埠上支援。
- **CRS520-4XS-16XQ：** 在所有埠上支援。

### RouterOS 7.17 及更高版本中新增的 PTP 支援 {#ptp-support-added-in-routeros-version-717-and-later}

- **CRS320-8P-8B-4S+RM：** 僅在千兆乙太網埠上支援。
- **CRS326-4C+20G+2Q+：** 在所有埠上支援。

### RouterOS 7.20 及更高版本中新增的 PTP 支援 {#ptp-support-added-in-routeros-version-720-and-later}

- **RDS2216-2XG-4S+4XS-2XQ：** 在所有埠上支援。

:::info
本節未列出的裝置不支援 Precision Time Protocol。
:::
:::info
任何裝置上的 MGMT（管理）埠都不支援 PTP。“所有埠”指所有資料介面，不包括 MGMT 埠。
:::
