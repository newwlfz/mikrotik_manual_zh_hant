---
sidebar_key: "user-guides/routing-and-networking-protocols/policy-routing"
sidebar_position: 4
title: "策略路由"
sidebar_label: "策略路由"
description: "RouterOS 中的策略路由允許根據條件將流量引導到特定閘道器，並使用自定義路由表和規則。它支援透過防火牆 mangle 標記或基本路由規則配置進行動態路由決策，以實現流量控制。"
tags:
  - 'routing'
  - 'policy-routing'
source: https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/policy-routing
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

策略路由將匹配條件的流量引導到特定閘道器。使用它可強制選定的客戶或協定（例如 HTTP 流量）始終使用特定閘道器。它還可以讓本地和海外流量透過不同閘道器路由。

RouterOS 為策略路由提供以下元件：

- 路由表。
- 路由規則。
- 防火牆 mangle 標記。

## 路由表 {#routing-tables}

一個路由器可以有多個路由表，每個路由表都有各自用於同一目標但不同閘道器的路由。

透過 `/routing/table` 選單檢視和配置表。

預設情況下，RouterOS 只有 **main** 路由表：

```text
[admin@rack1_b33_CCR1036] /routing/table> print
Flags: D - dynamic; X - disabled, I - invalid; U - used
0 D name="main" fib

```

在配置中的其他位置使用自定義路由表之前，請先在此選單中定義它。

考慮一個基本示例：有兩個閘道器 172.16.1.1 和 172.16.2.1，並且在名為 **myTable** 的路由表中有一條到 8.8.8.8 的路由，該路由使用閘道器 172.16.2.1：

```ros
/routing/table/add name=myTable fib
/ip/route/add dst-address=8.8.8.8 gateway=172.16.1.1
/ip/route/add dst-address=8.8.8.8 gateway=172.16.2.1@main routing-table=myTable
```

:::tip
為了讓使用者建立的表能夠解析目標，main 路由表也必須能夠解析該目標。
:::

在此示例中，**main** 路由表還應包含到 8.8.8.8 的路由，或至少一條預設路由。由於 DHCP 會出於安全考慮動態新增預設路由，請將 8.8.8.8 顯式新增到 main 表中。

```text
[admin@rack1_b33_CCR1036] /ip/route> print detail Flags: D - dynamic; X - disabled, I - inactive, A - active;
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, y - cop
y;
H - hw-offloaded; + - ecmp
   DAd   dst-address=0.0.0.0/0 routing-table=main pref-src="" gateway=172.16.1.1
         immediate-gw=172.16.1.1%ether8 distance=1 scope=30 target-scope=10
         vrf-interface=ether8 suppress-hw-offload=no

 0  As   dst-address=8.8.8.8/32 routing-table=main pref-src="" gateway=172.16.1.1
         immediate-gw=172.16.1.1%ether8 distance=1 scope=30 target-scope=10 suppress-hw-offload=no

    DAc   dst-address=172.16.1.0/24 routing-table=main gateway=ether8 immediate-gw=ether8
         distance=0 scope=10 suppress-hw-offload=no local-address=172.16.1.2%ether8

    DAc   dst-address=172.16.2.0/24 routing-table=main gateway=ether7 immediate-gw=ether7
         distance=0 scope=10 suppress-hw-offload=no local-address=172.16.2.2%ether7

 1  As   dst-address=8.8.8.8/32 routing-table=myTable pref-src="" gateway=172.16.2.1
         immediate-gw=172.16.2.1%ether7 distance=1 scope=30 target-scope=10 suppress-hw-offload=no

```

上面的配置還不夠。你需要一種方法來強制流量使用新表。RouterOS 提供兩個選項：

- firewall mangle - 對用於引導流量的條件提供更多控制，例如按連線或按封包均衡。示例請參見[防火牆標記](../../firewall-and-quality-of-service/firewall/mangle.md)。
- 路由規則 - 一組用於快速引導流量的基本引數。此示例使用路由規則。

除非必要，不要同時使用這兩種方法。如果 mangle 和路由規則一起使用，預設情況下 mangle 具有更高的優先順序。如果 mangle 標記的流量可以在表中解析，路由規則將永遠看不到該流量。執行順序可以[更改](./routing-decision.md#routing-table-lookup)。

:::warning
路由表數量限制為 4096 個唯一表。
:::

## 路由規則 {#routing-rules}

路由規則根據源地址、目標地址、in-interface 等基本引數引導流量。

在此示例中，選擇發往 8.8.8.8 的流量，並防止回退到 **main** 表：

```ros
/routing/rule/add dst-address=8.8.8.8 action=lookup-only-in-table table=myTable
```

如果某個客戶連線到 ether4，並且只有該客戶應將 8.8.8.8 路由到特定閘道器，請使用此規則：

```ros
/routing/rule/add dst-address=8.8.8.8 action=lookup-only-in-table table=myTable interface=ether4
```

如果表中使用的閘道器宕機，查詢會失敗，目標將變得不可達。在 active-backup 設定中，透過將動作從 `lookup-only-in-table` 改為 `lookup`，允許流量回退到 **main** 表。

路由規則還可以充當基本防火牆。例如，要阻止 ether4 上的客戶訪問 192.168.1.0/24：

```ros
/routing/rule/add dst-address=192.168.1.0/24 interface=ether4 action=drop
```

## 示例：讓一臺裝置透過第二個 WAN {#example-send-one-device-through-a-second-wan}

路由器有兩條網際網路連線：ether1 上的 WAN1，其預設路由來自其 DHCP 用戶端；以及 ether2 上的 WAN2，閘道器為 10.20.0.1。LAN 192.168.88.0/24 上的所有裝置都使用 WAN1，但 192.168.88.50 除外，它必須使用 WAN2。為該裝置分配固定地址，以便規則能持續匹配它（參見[為裝置分配固定地址](../../network-management/dhcp/server.md#give-a-device-a-fixed-address)）。

1. 建立一條經由 WAN2 的預設路由的路由表。使用 `check-gateway=ping` 時，當閘道器停止響應，該路由會變為非活動狀態：

   ```ros
   /routing/table/add name=to-wan2 fib
   /ip/route/add dst-address=0.0.0.0/0 gateway=10.20.0.1 routing-table=to-wan2 check-gateway=ping
   ```

2. 將裝置的流量傳送到該表：

   ```ros
   /routing/rule/add src-address=192.168.88.50/32 action=lookup table=to-wan2
   ```

   使用 `action=lookup` 時，當經由 WAN2 的路由處於非活動狀態，該裝置會回退到 WAN1。若要使其不經過 WAN1，請使用 `lookup-only-in-table`。

3. 對經由 WAN2 離開的流量進行偽裝，與 WAN1 相同：

   ```ros
   /ip/firewall/nat/add chain=srcnat out-interface=ether2 action=masquerade
   ```

該規則會將裝置的所有流量傳送到該表，包括髮往路由器上其他網路的流量，例如訪客 LAN 或 WAN1 調變解調器所在的網路。要直接訪問此類網路，請在第一條規則之前為其新增一條規則：

```ros
/routing/rule/add dst-address=192.168.1.0/24 action=lookup-only-in-table table=main place-before=0
```

在你新增規則之前裝置已建立的連線可能會繼續使用 WAN1，直到這些連線結束。要檢查路徑，請在裝置上執行 traceroute：路由器之後的下一跳就是 WAN2 閘道器。
