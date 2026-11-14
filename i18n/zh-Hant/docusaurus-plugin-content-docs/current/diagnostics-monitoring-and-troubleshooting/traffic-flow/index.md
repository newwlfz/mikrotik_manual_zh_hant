---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/traffic-flow"
title: "流量監控"
sidebar_label: "流量監控"
description: "Traffic-Flow 將經過路由器的封包流統計資訊以 Cisco NetFlow（v1/v5/v9）或 IPFIX 格式匯出到收集器：啟用該服務，選擇介面和超時時間，新增目標，並使用 monitor 命令進行驗證。"
tags:
  - 'traffic-flow'
  - 'netflow'
  - 'ipfix'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/traffic-flow
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MikroTik Traffic-Flow 提供有關經過路由器的封包的統計資訊。除了網路監控和計費外，系統管理員還可以識別網路中出現的各種問題，並分析和最佳化整體網路效能。Traffic-Flow 與 Cisco NetFlow 相容，因此為 NetFlow 設計的工具也能與它配合工作。

Traffic Flow 僅處理經過路由器 CPU 的流量。HW-offloaded 流量（例如，交換器晶片埠之間 HW-offloaded 的橋接流量）絕不會出現在 Traffic Flow 中。

支援的匯出格式：

- **version 1** - 原始 NetFlow 格式。提供有關流經路由器的 IP 封包的基本資訊，但不支援不同型別的協定和服務型別 (ToS)。
- **version 5** - 對 version 1 的增強，支援服務型別 (ToS)、TCP 標誌和自治系統資訊。RouterOS 不會填充 BGP AS 號。
- **version 9** - 基於模板的匯出格式，支援新的記錄型別；匯出 IPv4 和 IPv6 流資訊。
- **IPFIX** - 基於 NetFlow version 9 的 IETF 標準化協定，具有更可自定義的流記錄；支援多播等較新欄位。

## 啟用 Traffic Flow 並選擇介面 {#enable-traffic-flow-and-choose-interfaces}

在 [`/ip/traffic-flow`](../../cli-reference/ip/traffic-flow/index.md) 中啟用該服務：

```ros
[admin@MikroTik] > /ip/traffic-flow/set enabled=yes
[admin@MikroTik] > /ip/traffic-flow/print
                enabled: yes
             interfaces: all
          cache-entries: 256k
    active-flow-timeout: 30m
  inactive-flow-timeout: 15s
        packet-sampling: no
      sampling-interval: 0
         sampling-space: 0
```

`cache-entries` 的預設值取決於裝置的記憶體（較大主機板上為 256k，最小主機板上為 4k）。`active-flow-timeout` 和 `inactive-flow-timeout` 決定流何時過期並匯出（請參閱[引數說明](../../cli-reference/ip/traffic-flow/index.md)）。

### 封包取樣 {#packet-sampling}

封包取樣只對一部分封包進行抽樣：

```ros
/ip/traffic-flow/set packet-sampling=yes sampling-interval=2222 \
    sampling-space=1111
```

連續取樣 2222 個數據包，然後省略 1111 個，如此迴圈重複。

## 新增匯出目標 {#add-export-targets}

在 [`/ip/traffic-flow/target`](../../cli-reference/ip/traffic-flow/target.md) 中新增接收流資料的主機：

```ros
[admin@MikroTik] > /ip/traffic-flow/target/add dst-address=192.168.0.2 \
    port=2055 version=9
[admin@MikroTik] > /ip/traffic-flow/target/print
Columns: SRC-ADDRESS, DST-ADDRESS, PORT, VERSION
# SRC-ADDRESS  DST-ADDRESS  PORT  VERSION
0 0.0.0.0      192.168.0.2  2055  9
```

`src-address=0.0.0.0` 表示路由器自動選擇出介面的源地址。匯出資料以所選格式透過 UDP（預設埠 2055）發出，此處以 NetFlow 版本 9 為例。

## 檢視流計數器 {#watch-the-flow-counters}

`/ip/traffic-flow/monitor` 命令顯示流快取的狀態（即時更新；在 `duration` 之後停止）：

```ros
[admin@MikroTik] > /ip/traffic-flow/monitor duration=3
    finished-flows: 0
      active-flows: 8
  unmanaged-packets: 0
    unmanaged-bytes: 0
```

如果收集器收不到任何資料，請檢查流是否出現在此處：隨著路由器轉發流量，`active-flows` 會上升；而當流超時並被匯出後，`finished-flows` 開始上升（預設 `inactive-flow-timeout` 為流的最後一個數據包之後 15s）。請檢查目標條目，並確認你所監視的流量確實由 CPU 路由（而非硬體解除安裝）。

## 為 IPFIX 選擇匯出的欄位 {#choose-exported-fields-for-ipfix}

[`/ip/traffic-flow/ipfix`](../../cli-reference/ip/traffic-flow/ipfix.md) 選單選擇 IPFIX 流記錄中顯示哪些欄位：地址、埠、協定、標誌、介面、時間資訊（例如 `sys-init-time`、`first-forwarded`、`last-forwarded`）、NAT 地址和埠等——所有這些行都列在 [CLI 參考](../../cli-reference/ip/traffic-flow/ipfix.md) 中。

所有欄位預設啟用；使用 `set` 刪除不需要的欄位：

```ros
[admin@MikroTik] > /ip/traffic-flow/ipfix/set gateway=no tcp-flags=no
```

## 說明 {#notes}

Traffic flow 在 [封包流](../../firewall-and-quality-of-service/packet-flow-in-routeros.md) 圖的 input、forward 和 output 鏈棧末尾記錄流量，因此只有到達這些鏈之一的流量才會被計入。

因此，連線到路由器的交換器上的映象埠不能用於統計映象封包：映象幀在到達 input 鏈之前會被丟棄。

如果流量經過其他介面和監控介面，其他介面也會出現在報告中。

## 最小端到端示例 {#minimal-end-to-end-example}

在單臺路由器上從零開始設定，將 NetFlow v9 匯出到 192.168.0.2 上的收集器：

```ros
/ip/traffic-flow/set enabled=yes
/ip/traffic-flow/target/add dst-address=192.168.0.2 port=2055 version=9
```

路由器開始傳送帶有流資訊的匯出封包；可使用 `/ip/traffic-flow/monitor` 進行觀察。

:::info
要在 MikroTik 上使用 ntop-ng，你需要使用 Nprobe，這是一款付費軟體。
:::

### 另請參閱 {#see-more}

- [NetFlow 基礎](https://etutorials.org/Networking/network+management/Part+II+Implementations+on+the+Cisco+Devices/Chapter+7.+NetFlow/Fundamentals+of+NetFlow/)
- [在 MikroTik 上使用 Ntop 進行流量流分析](https://github.com/ntop/ntopng/issues/1575)

## 相關主題 {#related-topics}

<DocCardList />
