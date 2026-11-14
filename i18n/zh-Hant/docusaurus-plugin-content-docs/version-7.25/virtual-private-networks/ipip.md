---
sidebar_key: "virtual-private-networks/ipip"
sidebar_position: 4
title: "IPIP"
sidebar_label: "IPIP"
description: "IPIP（IP-in-IP）是 RouterOS 中的一種隧道協定，用於在 IP 網路上建立安全的點對點連線，支援 IPv4 封裝以及與其他平臺的互操作性。它提供 MTU、keepalive 和 DSCP 設定等基本配置選項，並附帶有關缺乏加密的警告。"
tags:
  - 'ip'
  - 'tunnel'
source: https://manual.mikrotik.com/docs/7.25/virtual-private-networks/ipip
captured_at: '2026-11-04T11:23:05+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

IPIP（IP-in-IP）是 RFC 2003 中定義的一種簡單隧道協定，它將 IP 封包封裝在另一個 IP 頭中，以便在兩個端點之間傳輸流量。在 RouterOS 中，IPIP 可用於在中間 IP 網路上的路由器之間建立點對點隧道。

IPIP 隧道介面在介面列表中表示為虛擬介面，並且可以像其他邏輯介面一樣進行配置。該協定受到多種網路平臺的支援，包括 RouterOS、Linux 和 Cisco 裝置，從而實現不同廠商之間的互操作。

IPIP 通常用於透過公共或私有 IP 基礎設施連線遠端網路，而無需直接的二層連線。該協定支援封裝 IPv4 流量，並且通常用作不需要加密的輕量級隧道機制。

IPIP 的典型用例包括透過網際網路隧道傳輸私有網路、在遠端站點之間建立路由鏈路，以及在網路設計中提供源路由的替代方案。由於 IPIP 不提供加密、身份驗證或流量完整性保護，因此在需要安全傳輸時，通常與 IPsec 結合使用。

IPIP 在 [`/interface/ipip`](../cli-reference/interface/ipip.md) 和 [`/interface/ipipv6`](../cli-reference/interface/ipipv6.md) 選單中配置。

## 示例 {#example}

本示例在路由器 R1 和 R2 之間新增一條 IPIP 隧道：

![](/img/8a32f4a39173d818.webp)

首先，配置 IPIP 介面併為其新增 IP 地址。
  
**R1** 路由器的配置如下：

```ros
[admin@MikroTik] /interface/ipip> add
local-address: 10.0.0.1
remote-address: 22.63.11.6
[admin@MikroTik] /interface/ipip> print
Flags: X - disabled, R - running
# NAME MTU LOCAL-ADDRESS REMOTE-ADDRESS
0 X ipip1 1480 10.0.0.1 22.63.11.6

[admin@MikroTik] /interface/ipip> en 0
[admin@MikroTik] /interface/ipip> /ip/address/add address=1.1.1.1/24 interface=ipip1
```

路由器 **R2** 的配置如下：

```ros
[admin@MikroTik] /interface/ipip> add local-address=22.63.11.6 remote-address=10.
0.0.1
[admin@MikroTik] /interface/ipip> print
Flags: X - disabled, R - running
# NAME MTU LOCAL-ADDRESS REMOTE-ADDRESS
0 X ipip1 1480 22.63.11.6 10.0.0.1

[admin@MikroTik] /interface/ipip> enable 0
[admin@MikroTik] /interface/ipip> /ip/address/add address=1.1.1.2/24 interface=ipip1
```

現在兩臺路由器可以互相 ping 通：

```ros
[admin@MikroTik] /interface/ipip> /ping 1.1.1.2
1.1.1.2 64 byte ping: ttl=64 time=24 ms
1.1.1.2 64 byte ping: ttl=64 time=19 ms
1.1.1.2 64 byte ping: ttl=64 time=20 ms
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 19/21.0/24 ms
[admin@MikroTik] /interface/ipip>
```
