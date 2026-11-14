---
sidebar_key: "virtual-private-networks/eoip"
sidebar_position: 2
title: "EoIP"
sidebar_label: "EoIP"
description: "MikroTik RouterOS 中的乙太網 over IP（EoIP）隧道使用 GRE 封裝在 IP 網路上建立安全的二層橋接，支援 LAN 擴充套件和透過 IPsec 加密連線等靈活拓撲。"
tags:
  - 'eoip'
  - 'bridging'
source: https://manual.mikrotik.com/docs/7.25/virtual-private-networks/eoip
captured_at: '2026-11-04T11:23:02+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Ethernet over IP (EoIP) 隧道是一種 MikroTik RouterOS 協定，旨在透過 IP 網路在兩臺路由器之間建立乙太網隧道。它基於 GRE 封裝（RFC 1701），允許乙太網幀透過路由式 IP 基礎設施傳輸，從而有效地在遠端站點之間擴充套件二層網路。

EoIP 隧道介面在 RouterOS 中顯示為虛擬乙太網介面，並可與橋接功能配合使用。當新增到網橋後，所有乙太網流量（包括廣播和非 IP 協定）都會透過隧道轉發，就像兩個端點由物理乙太網鏈路直接連線一樣。

EoIP 隧道可執行在 IPIP、PPTP 或任何其他支援 GRE 封裝的基於 IP 的傳輸之上。這為構建各種網路拓撲提供了靈活性。

EoIP 的典型用例包括透過網際網路橋接 LAN 網段、跨加密隧道擴充套件 LAN（與 IPsec 或其他安全傳輸結合使用時），以及透過無線點對點或自組網鏈路連線網路。

EoIP 將 Ethernet 幀封裝在 GRE（IP 協定 47）封包內，並將其轉發到遠端隧道端點。接收路由器會解封裝這些封包，並將原始 Ethernet 幀注入本地網橋域。

EoIP 在 [`/interface/eoip`](../cli-reference/interface/eoip.md) 和 [`/interface/eoipv6`](../cli-reference/interface/eoipv6.md)選單中配置。

## 配置示例 {#configuration-examples}

引數 tunnel-id 是標識隧道的一種方法。對於每個 EoIP 隧道，它必須唯一。

:::tip
EoIP 隧道至少增加 42 位元組開銷（8 位元組 GRE + 14 位元組 Ethernet + 20 位元組 IP）。將 MTU 設定為 1500 可消除隧道內的封包分片，從而允許對類 Ethernet 網路進行透明橋接，以便透過隧道傳輸完整大小的 Ethernet 幀。
:::

在橋接 EoIP 隧道時，應為每個隧道設定唯一的 MAC 地址，以便網橋演算法正常工作。對於 EoIP 介面，可以使用 **00:00:5E:80:00:00 - 00:00:5E:FF:FF:FF** 範圍內的 MAC 地址，IANA 已為此類情況保留該範圍。或者，可以設定第一個位元組的第二位，將自動分配的地址修改為“本地管理地址”（由網路管理員分配），從而可以使用任意 MAC 地址。只需確保它們在連線到同一個網橋的主機之間是唯一的。

### 示例 {#example}

本示例展示如何橋接兩個網路：'Station' 和 'AP'。使用 EoIP，可以設定網路，使 Station 和 AP 的 LAN 共享同一個二層廣播域。

考慮以下設定：

![](/img/f10b94c88193db8a.webp)

無線站點無法橋接。為了在不使用 WDS 的情況下克服此限制，請在無線鏈路上建立 EoIP 隧道，並將其與連線到本地網路的介面進行橋接。

本示例不涉及無線配置。假設無線鏈路已經建立。

首先，在 AP 上建立 EoIP 隧道：

```ros
/interface/eoip/add name="eoip-remote" tunnel-id=0 remote-address=10.0.0.2 disabled=no
```

驗證介面已建立：

```ros
[admin@AP] > /interface/eoip/print
Flags: X - disabled; R - running 
 0  R name="eoip-remote" mtu=auto actual-mtu=1458 l2mtu=65535 mac-address=FE:A5:6C:3F:26:C5 arp=enabled 
      arp-timeout=auto loop-protect=default loop-protect-status=off loop-protect-send-interval=5s 
      loop-protect-disable-time=5m local-address=0.0.0.0 remote-address=10.0.0.2 tunnel-id=0 
      keepalive=10s,10 dscp=inherit clamp-tcp-mss=yes dont-fragment=no allow-fast-path=yes 
```

Station 路由器：

```ros
/interface/eoip/add name="eoip-main" tunnel-id=0 remote-address=10.0.0.1 disabled=no
```

驗證介面已建立：

```ros
[admin@Station] >  /interface/eoip/print
Flags: X - disabled; R - running 
 0  R name="eoip-main" mtu=auto actual-mtu=1458 l2mtu=65535 mac-address=FE:4B:71:05:EA:8B arp=enabled 
      arp-timeout=auto loop-protect=default loop-protect-status=off loop-protect-send-interval=5s 
      loop-protect-disable-time=5m local-address=0.0.0.0 remote-address=10.0.0.1 tunnel-id=0 
      keepalive=10s,10 dscp=inherit clamp-tcp-mss=yes dont-fragment=no allow-fast-path=yes  
```

接下來，在 AP 上將本地介面與 EoIP 隧道橋接。如果已有本地網橋介面，請將 EoIP 介面新增到其中：

```ros
/interface/bridge/port/add bridge=bridge1 interface=eoip-remote
```

網橋埠列表會顯示所有本地 LAN 介面和 EoIP 介面：

```ros
[admin@AP] > /interface/bridge/port/print 
Flags: I - INACTIVE; H - HW-OFFLOAD
Columns: INTERFACE, BRIDGE, HW, PVID, PRIORITY, PATH-COST, INTERNAL-PATH-COST, HORIZON
#    INTERFACE       BRIDGE   HW   PVID  PRIORITY  PATH-COST  INTERNAL-PATH-COST  HORIZON
0  H ether2          bridge1  yes     1  0x80             10                  10  none   
1  H ether3          bridge1  yes     1  0x80             10                  10  none    
2    eoip-remote     bridge1  yes     1  0x80             10                  10  none    
```

在 Station 路由器上，如果沒有本地網橋介面，請建立一個新網橋，並將 EoIP 和本地 LAN 介面都新增到其中：

```ros
/interface/bridge/add name=bridge1
/interface/bridge/port/add bridge=bridge1 interface=ether2
/interface/bridge/port/add bridge=bridge1 interface=eoip-main
```

驗證網橋埠部分：

```ros
[admin@Station] > /interface/bridge/port/print 
Flags: I - INACTIVE; H - HW-OFFLOAD
Columns: INTERFACE, BRIDGE, HW, PVID, PRIORITY, PATH-COST, INTERNAL-PATH-COST, HORIZON
#    INTERFACE     BRIDGE   HW   PVID  PRIORITY  PATH-COST  INTERNAL-PATH-COST  HORIZON
0  H ether2        bridge1  yes     1  0x80             10                  10  none    
2    eoip-main     bridge1  yes     1  0x80             10                  10  none    
```

現在兩個站點處於同一個二層廣播域中。你可以在兩個站點上設定來自同一網路的 IP 地址。
