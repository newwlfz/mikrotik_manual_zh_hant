---
sidebar_key: "virtual-private-networks/gre"
sidebar_position: 3
title: "GRE"
sidebar_label: "GRE"
description: "通用路由封裝（GRE）是一種隧道協定，它在 RouterOS 中將 IP over IP 封裝為虛擬點對點鏈路，並支援 keepalive 監控、MTU 和 MSS 處理、DSCP 設定以及用於加密隧道的可選 IPsec-secret。"
tags:
  - 'gre'
source: https://manual.mikrotik.com/docs/virtual-private-networks/gre
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Generic Routing Encapsulation (GRE) 是一種隧道協定，最初由 Cisco 開發，用於在 IP 網路上封裝各種網路層協定。它在隧道端點之間建立虛擬點對點鏈路，允許不同的協定流量透過路由基礎設施傳輸。

在 RouterOS 中，GRE 在 [`/interface/gre`](../cli-reference/interface/gre.md)（基於 IPv4）和 [`/interface/gre6`](../cli-reference/interface/gre6.md)（基於 IPv6）選單中實現為虛擬介面。這些介面是路由（第 3 層）隧道：GRE 隧道僅在兩個端點之間承載 IP 和 IPv6 封包。若要透過 IP 網路實現第 2 層連線（橋接乙太網幀），請改用 [EoIP](./eoip.md)。

## 隧道工作原理 {#how-the-tunnel-works}

GRE 是無狀態隧道，行為類似於 [IPIP](./ipip.md) 和 EoIP。端點之間不維護會話狀態：即使遠端變得不可達，路由器仍會繼續向遠端轉發封包，而隧道流量會被丟棄，直到連線恢復或隧道被重新配置。

路由器在遠端至少響應一次後，才會認為隧道處於 **running**（`R` 標誌）。從那時起，Keepalive 會監控遠端：路由器每隔一個 keepalive 間隔向 remote-address 傳送 GRE echo 探測，並在隧道處於 up 狀態時應答遠端的探測。Keepalive 預設啟用（`10s,10`——間隔 10 秒，重試 10 次），間隔最短可設為 1 秒以便更快檢測（設定為 0 秒會被拒絕）。在當前 RouterOS 上，只要隧道已啟用，running 標誌就會保持——遠端不可達的隧道仍保持 running，隧道流量會被丟棄，直到遠端再次響應。如果自動故障轉移必須對失效隧道做出反應，請新增可達性檢查（例如用指令碼 ping 遠端並調整路由），而不是依賴 running 標誌。

:::tip
GRE 隧道會增加每包開銷：在 IPv4 上為 24 位元組（4 位元組 GRE 頭部 + 20 位元組 IP 頭部），在 IPv6 上為 44 位元組（4 位元組 GRE 頭部 + 40 位元組 IPv6 頭部）。使用預設 `mtu=auto` 時，路由器會相應地設定隧道 MTU——對於 GRE over IPv4，在 1500 位元組介面上 `actual-mtu` 為 1476，對於 GRE over IPv6 為 1456。隧道僅承載 IP 和 IPv6 封包（EtherType 0x0800 和 0x86DD）。當 GRE 隧道用作路由閘道器時，不要使用“Check gateway”選項 `arp`。
:::

所有 GRE 屬性在 [`/interface/gre`](../cli-reference/interface/gre.md) 和 [`/interface/gre6`](../cli-reference/interface/gre6.md) CLI 參考中均有描述。

## 示例：連線兩個站點 {#example-connect-two-sites}

該示例透過 GRE 隧道經網際網路連線兩個站點，併為每個站點提供到另一站點本地網路的第 3 層訪問。

![GRE tunnel between two sites](/img/6412953c9c3ec94f.webp)

**Site1** 的本地網路為 **10.1.101.0/24**，**Site2** 的本地網路為 **10.1.202.0/24**。隧道端點是路由器的公網地址，此處為 **192.168.80.1**（Site1）和 **192.168.90.1**（Site2）——請替換為你自己路由器的網際網路地址。

在 Site1 路由器上建立隧道：

```ros
/interface/gre/add name=myGre \
    remote-address=192.168.90.1 local-address=192.168.80.1
```

在 Site2 路由器上建立隧道：

```ros
/interface/gre/add name=myGre \
    remote-address=192.168.80.1 local-address=192.168.90.1
```

:::note
該示例將 keepalive 保留為預設值（`10s,10`）。在遠端應答後，隧道會顯示 running 標誌。GRE 是無狀態的：如果一端變得不可達，running 標誌會保持，進入隧道的流量會被丟棄，直到遠端再次可達。
:::

現在兩端都有了隧道，但還需要地址才能在隧道上路由。為隧道兩端分配私有地址範圍的地址，並新增通往遠端站點本地網路的路由。在 Site1 路由器上：

```ros
/ip/address/add address=172.16.1.1/30 interface=myGre
/ip/route/add dst-address=10.1.202.0/24 gateway=172.16.1.2
```

在 Site2 路由器上：

```ros
/ip/address/add address=172.16.1.2/30 interface=myGre
/ip/route/add dst-address=10.1.101.0/24 gateway=172.16.1.1
```

此時兩個站點已透過 GRE 隧道建立了三層連通性。請進行端到端驗證——對遠端隧道地址的 ping 必須得到應答，並且兩個站點上的隧道都必須顯示 `R` 標誌：

```ros
/ping 172.16.1.2
/interface/gre/print where name=myGre
```

## 故障排除 {#troubleshooting}

- **隧道沒有 running 標誌。** 遠端尚未應答。使用 `/ping <remote-address>` 檢查隧道端點是否可達，確認遠端路由器有匹配的隧道且其 `remote-address` 指向回本端，並確認隧道的 `local-address` 設定正確。只有在遠端應答後，running 標誌才會出現。
- **透過隧道的流量丟失。** GRE 是無狀態的：當遠端不可達時，路由器會繼續將隧道流量傳送進隧道，而這些流量會被丟棄。檢查 `remote-address` 的可達性，並將隧道的 `actual-mtu` 與站點之間的路徑 MTU 進行比較（MTU 不匹配會丟棄過大的封包）。
- **隧道已建立，但站點之間沒有流量透過。** 站點之間的 WAN 防火牆必須允許兩個隧道端點之間的 GRE（IP 協定 47）——如果隧道配置了 `ipsec-secret`，還需要允許 IPsec 埠——並且隧道流量不得被 NAT。
- **遠端的地址發生了變化。** `remote-address` 接受的是 IP 地址，而不是主機名；如果某個站點的公網地址發生變化，請更新另一端的隧道，或使用具有穩定地址的端點。
- **非 IP 流量無法透過。** GRE 是路由隧道，只承載 IP 和 IPv6 封包。若要在 IP 網路上橋接乙太網幀，請使用 [EoIP](./eoip.md)。
