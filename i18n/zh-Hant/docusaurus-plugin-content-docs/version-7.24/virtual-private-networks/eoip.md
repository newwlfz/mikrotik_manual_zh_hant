---
sidebar_key: "virtual-private-networks/eoip"
sidebar_position: 2
title: "EoIP"
sidebar_label: "EoIP"
description: "MikroTik RouterOS 中的乙太網 over IP（EoIP）隧道使用 GRE 封裝在 IP 網路上建立安全的二層橋接，支援 LAN 擴充套件和透過 IPsec 加密連線等靈活拓撲。"
tags:
  - 'eoip'
  - 'bridging'
source: https://manual.mikrotik.com/docs/7.24/virtual-private-networks/eoip
captured_at: '2026-11-04T11:34:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Ethernet over IP (EoIP) 隧道是一種 MikroTik RouterOS 協定，旨在透過 IP 網路在兩臺路由器之間建立乙太網隧道。它基於 GRE 封裝（RFC 1701），允許乙太網幀透過路由式 IP 基礎設施傳輸，從而有效地在遠端站點之間擴充套件二層網路。

EoIP 隧道介面在 RouterOS 中顯示為虛擬乙太網介面，並可與橋接功能配合使用。當新增到網橋後，所有乙太網流量（包括廣播和非 IP 協定）都會透過隧道轉發，就像兩個端點由物理乙太網鏈路直接連線一樣。

EoIP 隧道可執行在 IPIP、PPTP 或任何其他支援 GRE 封裝的基於 IP 的傳輸之上。這為構建各種網路拓撲提供了靈活性。

EoIP 的典型用例包括透過網際網路橋接 LAN 網段、跨加密隧道擴充套件 LAN（與 IPsec 或其他安全傳輸結合使用時），以及透過無線點對點或自組網鏈路連線網路。

EoIP 將乙太網幀封裝在 GRE（IP 協定 47）封包內，並將其轉發到遠端隧道端點。接收路由器會解封裝這些封包，並將原始乙太網幀注入本地橋接域。
**子選單：** `/interface/eoip`

## 屬性說明 {#property-description}

| 屬性 | 描述 |
| :-- | :-- |
| **allow-fast-path** (*yes \| no*; 預設值：**yes**) | 是否允許 FastPath 處理。如果使用 IPsec 隧道，則必須停用。 |
| **arp (***disabled \| enabled \| proxy-arp \| reply-only*; 預設：**enabled)** | Address Resolution Protocol 模式。disabled - 介面將不使用 ARP；enabled - 介面將使用 ARP；proxy-arp - 介面將使用 ARP 代理功能；reply-only - 介面將僅回覆來自與 `/ip/arp` 表中靜態條目匹配的 IP 地址/MAC 地址組合的請求。不會自動在 `/ip/arp` 表中儲存動態條目。因此，為使通訊成功，必須已存在有效的靜態條目。 |
| **arp-timeout** (*integer[/time]*; 預設：**auto**) | ARP 條目應超時的時間間隔。 |
| **clamp-tcp-mss** (*yes \| no*; 預設：**yes**) | 控制是否更改收到的 TCP SYN 封包的 MSS 大小。啟用後，如果當前 MSS 大小超過隧道介面 MTU（考慮 TCP/IP 開銷），路由器將更改收到的 TCP SYN 封包的 MSS 大小。收到的封裝封包仍將包含原始 MSS，並且只有在解封裝後才會更改 MSS。 |
| **comment** (*string*; 預設值: ) | 介面的簡短描述。 |
| **disabled** (*yes \| no*; 預設：**no**) | 專案是否已停用。 |
| **dont-fragment** (*inherit \| no*; 預設：**no**) | 是否在相關封包中包含 DF 位：  *no* - 如有需要則分片，*inherit* - 使用原始封包的 Don't Fragment 標誌。  （未設定 Don't Fragment 時：inherit - 封包可能被分片）。 |
| **dscp** (*integer: 0-63*; 預設：**inherit**) | 封包的 DSCP 值。inherit 選項表示 dscp 值將從將要被封裝的封包中繼承。 |
| **ipsec-secret** (*string*; 預設：) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 當指定 secret 後，路由器會使用預共享金鑰和策略向 remote-address 新增動態 IPsec 對等體（預設情況下 phase2 使用 sha1/aes128cbc）。 |
| **keepalive** (*integer[/time],integer 0..4294967295*; 預設：**10s,10**) | 隧道 keepalive 引數設定即使隧道遠端宕機時隧道 running 標誌仍將保持的時間間隔。如果配置的時間、重試次數失敗，則移除介面 running 標誌。引數按以下格式書寫：`KeepaliveInterval,KeepaliveRetries`，其中 `KeepaliveInterval` 是時間間隔，`KeepaliveRetries` 是重試嘗試次數。預設情況下，keepalive 設定為 10 秒和 10 次重試。 |
| **l2mtu** (*integer; 只讀*) | 二層最大傳輸單元。對於 EoIP 不可配置。 [RouterOS 中的 MTU](../hardware/mtu-in-routeros.md) |
| **local-address** (*IP*; 預設：) | 隧道封包的源地址，位於本地路由器上。 |
| **loop-protect** |  |
| **loop-protect-disable-time** |  |
| **loop-protect-send-interval** |  |
| **mac-address** (*MAC*; 預設：) | 介面的 Media Access Control 編號。地址編號機構 IANA 允許自由使用 **00:00:5E:80:00:00 - 00:00:5E:FF:FF:FF** 範圍內的 MAC 地址 |
| **mtu** (*integer*; 預設：**auto**) | 三層最大傳輸單元 |
| **name** (*string*；預設：) | 介面名稱 |
| **remote-address** (*IP*; 預設：) | EoIP 隧道遠端的 IP 地址 |
| **tunnel-id** (*integer: 0..65535*; 預設：) | 唯一的隧道識別符號，必須與隧道另一側匹配 |

## 配置示例 {#configuration-examples}

引數 tunnel-id 是標識隧道的一種方法。對於每個 EoIP 隧道，它必須唯一。

:::tip
EoIP 隧道至少增加 42 位元組開銷（8 位元組 GRE + 14 位元組 Ethernet + 20 位元組 IP）。應將 MTU 設定為 1500，以消除隧道內的封包分片（這樣可以透明橋接類似乙太網的網路，從而能夠透過隧道傳輸完整大小的乙太網幀）。
:::

在橋接 EoIP 隧道時，強烈建議為每個隧道設定唯一的 MAC 地址，以便橋接演算法正常工作。對於 EoIP 介面，可以使用 **00:00:5E:80:00:00 - 00:00:5E:FF:FF:FF** 範圍內的 MAC 地址，IANA 已為此類情況保留該範圍。或者，可以設定第一個位元組的第二位，將自動分配的地址修改為由網路管理員分配的“本地管理地址”，從而使用任意 MAC 地址。只需確保它們在同一網橋所連線的主機之間唯一即可。

### 示例 {#example}

假設我們要橋接兩個網路：'Station' 和 'AP'。透過使用 EoIP，可以進行相應設定，使 Station 和 AP 的 LAN 處於同一個二層廣播域中。

考慮以下設定：

![](/img/f10b94c88193db8a.webp)

如你所知，無線站點無法被橋接；為克服此限制（不涉及 WDS），我們將透過無線鏈路建立 EoIP 隧道，並將其與連線到本地網路的介面一起橋接。

本示例不會涵蓋無線配置，我們假設無線鏈路已經建立。

首先，我們在 AP 上建立一個 EoIP 隧道：

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

接下來，我們將在 AP 上將本地介面與 EoIP 隧道進行橋接。如果你已經有本地網橋介面，只需將 EoIP 介面新增到其中：

```ros
/interface/bridge/port/add bridge=bridge1 interface=eoip-remote
```

網橋埠列表應列出所有本地 LAN 介面和 EoIP 介面：

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
