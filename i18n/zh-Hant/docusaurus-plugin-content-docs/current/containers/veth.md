---
sidebar_key: "containers/veth"
sidebar_position: 2
title: "VETH"
sidebar_label: "VETH"
description: "veth 將容器連線到 RouterOS：一端是路由器介面，另一端是容器的網路介面。將容器置於 NAT 之後，或透過 DHCP、IPv4 和 IPv6 放在 LAN 上。"
tags:
  - 'veth'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/containers/veth
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

veth（虛擬乙太網）是一對相連的乙太網端點。一端是 `/interface/veth` 中的 RouterOS 介面；另一端是容器的網路介面。在容器內部，該介面具有 veth 的名稱和 `container-mac-address`。veth 的地址、閘道器和 DHCP 設定會在容器內部應用，而不是在路由器上應用。

在使用它的容器啟動之前，veth 不會執行。在此之前，其 MAC 地址顯示為 `00:00:00:00:00:00`，並且路由器上為其配置的 IP 地址會被標記為無效。

要建立並執行容器，請參閱 [容器](./index.md)。[應用](./apps/index.md) 會自動建立其 veth。

## 將容器置於 NAT 之後 {#put-a-container-behind-nat}

容器會獲得自己的子網，路由器作為其閘道器，並將其流量轉換到網際網路。使用容器的地址和閘道器建立 veth，在 veth 上為路由器分配閘道器地址，並對該子網進行偽裝：

```ros
/interface/veth/add name=veth1 address=172.17.0.2/24 \
    gateway=172.17.0.1
/ip/address/add address=172.17.0.1/24 interface=veth1
/ip/firewall/nat/add chain=srcnat action=masquerade \
    src-address=172.17.0.0/24
```

然後為容器使用該 veth：

```ros
/container/add remote-image=alpine:latest interface=veth1 \
    root-dir=usb1/alpine
```

容器會獲得 172.17.0.2/24，以及一條經由 172.17.0.1（路由器在 veth 上的地址）的預設路由。偽裝規則使其能夠訪問網際網路。要從外部訪問容器中的服務，請新增一條 `dst-nat` 規則，將埠轉發到 172.17.0.2（請參閱 [NAT](../firewall-and-quality-of-service/firewall/nat.md)）。

## 將容器接入 LAN {#put-a-container-on-the-lan}

容器會像 LAN 上的任何其他裝置一樣，從 LAN 的 DHCP 伺服器獲取地址。使用 `dhcp=yes` 建立 veth，並將其新增到 LAN 網橋：

```ros
/interface/veth/add name=veth2 dhcp=yes
/interface/bridge/port/add bridge=bridge interface=veth2
```

RouterOS 會為容器執行 DHCP 用戶端，並在容器內部應用租約：容器會獲得租用的地址以及來自 DHCP 的預設路由。`/interface/veth/print` 的 `dhcp-address` 列會顯示租用的地址。

DHCP 伺服器看到的是 veth 的路由器側 MAC 地址（`mac-address`）和主機名 `<identity>-<veth name>`，例如 `MikroTik-veth2`。為容器設定靜態租約時必須使用 `mac-address`，而不是 `container-mac-address`。

容器的 DNS 伺服器來自容器設定，而不是來自 DHCP；請參閱 [容器](./index.md)。

在網橋上啟用路由器通告後，容器還會根據通告的字首（SLAAC）配置 IPv6 地址和 IPv6 預設路由。

## 靜態 IPv4 和 IPv6 地址 {#static-ipv4-and-ipv6-addresses}

`address` 接受多個地址，以逗號分隔，包括 IPv4 和 IPv6。`gateway` 和 `gateway6` 會在容器內部設定 IPv4 和 IPv6 預設路由。在 veth 上為路由器分配匹配的閘道器地址：

```ros
/interface/veth/add name=veth1 \
    address=172.17.0.2/24,2001:db8:17::2/64 \
    gateway=172.17.0.1 gateway6=2001:db8:17::1
/ip/address/add address=172.17.0.1/24 interface=veth1
/ipv6/address/add address=2001:db8:17::1/64 interface=veth1 \
    advertise=no
```

更改 veth 的設定之前，請先停止容器，然後在更改完成後重新啟動它。

## 檢查 veth {#check-the-veth}

在 `/interface/veth/print` 中，標誌 `R` 表示有正在執行的容器正在使用該 veth。`MAC-ADDRESS` 是路由器端，`CONTAINER-MAC-ADDRESS` 是容器端；兩者都會在容器啟動時設定。對於 `dhcp=yes` 的 veth，`DHCP-ADDRESS` 會顯示租用的地址。

要檢視容器內部的地址和路由，請使用 `/container/shell` 開啟其 shell，並執行 `ip addr` 和 `ip route`（如果容器映象包含 `ip` 命令）。

有關所有引數，請參閱 [`/interface/veth`](../cli-reference/interface/veth.md) CLI 參考。
