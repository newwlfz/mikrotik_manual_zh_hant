---
sidebar_key: "system-information-and-utilities/ip-packing"
sidebar_position: 7
title: "IP 打包"
sidebar_label: "IP 打包"
description: "IP Packing 會將鏈路上的出站封包收整合更大的封包，並可對其進行壓縮；另一臺路由器會將它們解包。兩臺路由器都需要在該鏈路上進行鄰居發現。"
tags:
  - 'ip-packing'
  - 'packet-aggregation'
source: https://manual.mikrotik.com/docs/system-information-and-utilities/ip-packing
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

IP Packing 會把介面的出站封包收整合更大的封包（聚合），並且還能對它們進行壓縮。鏈路另一端的路由器會再次將它們解包。兩臺路由器都執行 RouterOS；打包是 system 軟體包的一部分。在那些大量小封包的代價高於少量大封包的鏈路上使用它。

:::warning
路由器自身透過打包鏈路發起的 TCP 連線會失敗，例如 fetch 或頻寬測試。解包後承載資料的 TCP 段會以錯誤的校驗和到達並被丟棄，因此這些連線永遠無法完成。Ping 可以透過。在把打包功能啟用到生產鏈路之前，請先在測試鏈路上測試你需要的流量。
:::

## 先決條件 {#prerequisites}

- [鄰居發現](./neighbor-discovery.md) 在兩端路由器的該介面上執行：[`/ip/neighbor/discovery-settings`](../cli-reference/ip/neighbor/discovery-settings.md) 中的 `discover-interface-list` 包含該介面。預設配置只在 `LAN` 介面列表上進行發現，因此隧道或 WAN 介面需要一個包含它的列表。`LAN` 列表還決定預設防火牆信任什麼，因此請為發現使用單獨的列表，而不是把這樣的介面新增到 `LAN` 中。例如，一個同時包含 `LAN` 列表和 `ether1` 的列表：

  ```ros
  /interface/list/add name=discover include=LAN
  /interface/list/member/add list=discover interface=ether1
  /ip/neighbor/discovery-settings/set discover-interface-list=discover
  ```

- 兩臺路由器共享一條二層鏈路：一根網線、一條橋接的無線鏈路或一個 EoIP 隧道。打包後的封包在乙太網幀中傳輸，而鄰居發現工作在二層。
- 兩臺路由器對稱配置：一臺路由器打包的內容由另一臺解包。只有當鄰居通告它會解包時，路由器才會向該鄰居打包。

## 配置打包 {#configure-packing}

Router-A 和 Router-B 用一根網線相連，分別接在 Router-A 的 `ether1` 和 Router-B 的 `ether3` 上。本示例聚合 Router-A 傳送的封包，而 Router-B 發出的封包保持原樣。

在 Router-A 上：

```ros
/ip/packing/add interface=ether1 packing=simple unpacking=none
```

在 Router-B 上：

```ros
/ip/packing/add interface=ether3 packing=none unpacking=simple
```

要在兩個方向上都打包，請在兩端路由器上都設定 `packing=simple unpacking=simple`。

預設的 `aggregated-size` 為 1500 位元組，這是打包在傳送封包之前試圖達到的大小。

在 WinBox 中，開啟 **IP > Packing** 並選擇 **New**：

1. 在 **Interface** 中選擇鏈路介面，例如 Router-A 上的 `ether1`。截圖顯示的是尚未選擇介面時的新規則。
2. 設定 **Packing**、**Unpacking** 和 **Aggregated Size**，使其與流量方向以及另一臺路由器上的設定相匹配。對於示例中的 Router-A，使用 `simple`、`none` 和 `1500`，然後選擇 **OK**。

![WinBox new IP Packing rule](/img/6a0182a999b77dc7.webp)

## 檢查打包是否正常工作 {#check-that-packing-works}

每臺路由器都會透過鄰居發現通告自己的解包設定。在 Router-A 上執行 `/ip/neighbor/print detail where interface=ether1`：Router-B 對應的條目會顯示 `unpack=simple`，因為 Router-B 會解包。在 Router-B 上，Router-A 對應的條目顯示 `unpack=none`。值 `none`、`simple`、`uncompress-headers` 和 `uncompress-all` 分別對應於 `unpacking` 設定 `none`、`simple`、`compress-headers` 和 `compress-all`。

當遠端路由器在該介面上沒有鄰居條目，或其條目顯示 `unpack=none` 時，路由器不會向它打包，而是按原樣傳送封包。

在抓包中，打包後的幀的 EtherType 為 0x9000。

## 延遲 {#latency}

打包會短暫地暫留封包以便將它們合併，因此會增加延遲。在高速鏈路上，ping 往返時間可能從不到一毫秒上升到數十毫秒。對於語音和其他即時流量，需要考慮這一點。

有關所有引數，請參閱 [`/ip/packing`](../cli-reference/ip/packing.md) 和 [`/ip/neighbor/discovery-settings`](../cli-reference/ip/neighbor/discovery-settings.md) 的 CLI 參考。
