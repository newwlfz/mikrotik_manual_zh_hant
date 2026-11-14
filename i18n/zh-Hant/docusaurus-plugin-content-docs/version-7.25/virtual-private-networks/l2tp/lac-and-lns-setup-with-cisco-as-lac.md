---
sidebar_key: "virtual-private-networks/l2tp/lac-and-lns-setup-with-cisco-as-lac"
sidebar_position: 1
title: "使用 Cisco 作為 LAC 的 LAC 和 LNS 設定"
sidebar_label: "使用 Cisco 作為 LAC 的 LAC 和 LNS 設定"
description: "本頁介紹如何將 MikroTik RouterOS 裝置配置為 L2TP 網路伺服器（LNS），以便與充當 LAC 的 Cisco 路由器建立 VPDN 連線。其中包含在 LAC 上配置 PPPoE 用戶端、在 LNS 上啟用 L2TP 伺服器的基礎配置示例，以及適用於這兩種角色的 RouterOS 命令示例。"
tags:
  - 'vpdn'
  - 'l2tp'
  - 'ppp'
source: https://manual.mikrotik.com/docs/7.25/virtual-private-networks/l2tp/lac-and-lns-setup-with-cisco-as-lac
captured_at: '2026-11-04T11:23:15+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

LAC/LNS 設定，也稱為虛擬專用撥號網路（VPDN），允許遠端撥號使用者與專用網路之間建立長距離點對點連線。

撥號用戶端使用 PPPOE 連線到 L2TP 接入集中器（LAC），LAC 確定該會話應透過 IP 網路轉發到 L2TP 網路伺服器（LNS），建立 L2TP 隧道，並將 PPP 幀轉發到伺服器；在伺服器上，用戶端透過身份驗證並建立會話（見下圖）。

![](/img/fd5eb4904ada5626.svg)

在撰寫本文時，RouterOS 無法用於 LAC 角色。因此，本文將演示如何搭建一個非常基礎的網路，其中 RouterOS 作為 LNS，Cisco 路由器作為 LAC。

## 配置 {#configuration}

我們將使用一個簡單配置來演示 VPDN 設定的基礎知識。假設 LAC 將把 FQDN 名稱包含 [mt.lv](https://mt.lv) 域的用戶端轉發到 LNS。

### 用戶端 {#client}

為簡單起見，假設用戶端是一臺 RouterOS 路由器：

```ros
/interface/pppoe-client/add interface=ether1 user=good_worker@mt.lv password=strongpass
```

### LAC {#lac}

假設用戶端連線到 GigabitEthernet1 埠，並且 LNS 伺服器的 IP 地址為 10.155.101.231

```text
aaa new-model
!
aaa authentication ppp default local
!
vpdn enable
vpdn aaa attribute nas-ip-address vpdn-nas
vpdn search-order domain dnis 
!
vpdn-group LAC
 request-dialin
  protocol l2tp
  domain mt.lv
 initiate-to ip 10.155.101.231
 source-ip 10.155.101.216
 local name LAC
 l2tp tunnel password 0 tunnelpass
!
bba-group pppoe MAIN-BBA
 virtual-template 1
!
interface GigabitEthernet1
 pppoe enable group MAIN-BBA
!
interface Virtual-Template1
 description pppoe MAIN-BBA
 no ip address
 no peer default ip address
 ppp mtu adaptive
 ppp authentication chap
!

```

請注意，為簡單起見，此設定既不會在本地也不會透過 RADIUS 對用戶端進行身份驗證，實際上不會檢查域名，也不會控制 L2 訪問。如果要使用這些功能，請參閱 Cisco 配置手冊。

### LNS {#lns}

在 LNS 上，我們需要啟用 L2TP 伺服器，並設定一種方法來對來自 LAC 的 L2TP 連線進行身份驗證。

```ros
/interface/l2tp-server/server
set enabled=yes
/ppp/l2tp-secret
add address=10.155.101.216/32 secret=tunnelpass
```

現在進行實際的使用者身份驗證。在本例中，為簡單起見，我們將使用本地身份驗證方法。

```ros
/ip/pool
add name=pool0 ranges=192.168.99.2-192.168.99.99
/ppp/profile
set default local-address=192.168.99.1 remote-address=pool0
/ppp/secret
add name=good_worker@mt.lv password=strongpass
```

## 狀態檢查 {#status-check}

在 LNS 上，你可以透過檢查 l2tp 伺服器介面或檢查活動的 ppp 連線來檢視所有成功連線的用戶端：

```text
[admin@CHR_v6_bgp] /interface/l2tp-server> print
Flags: X - disabled, D - dynamic, R - running
# NAME USER MTU CLIENT-ADDRESS UPTIME ENCODING
0 DR <l2tp-... good_worker@mt.lv 1450 10.155.101.216 6h13m49s

[admin@CHR_v6_bgp] /ppp/active> print
Flags: R - radius
# NAME SERVICE CALLER-ID ADDRESS UPTIME ENCODING
0 good_worker@mt.lv l2tp 10.155.101.216 192.168.99.2 6h15m57s 

```

在 LAC 上，我們還可以看到活動的用戶端會話以及 LAC 與 LNS 之間的活動 L2TP 隧道：

```text
csrLAC#show vpdn

L2TP Tunnel and Session Information Total tunnels 1 sessions 1

LocTunID RemTunID Remote Name State Remote Address Sessn L2TP Class/
Count VPDN Group
26090 11 CHR_v6_bgp est 10.155.101.231 1 LAC

LocID RemID TunID Username, Intf/ State Last Chg Uniq ID
Vcid, Circuit
18521 16 26090 good_worker@mt.lv, Gi1 est 06:17:07 571

```

## 會話建立 {#session-establishment}

讓我們仔細看看用戶端會話如何透過 LAC 進行身份驗證並建立。

![](/img/2926b26e48134203.svg)

- 用戶端發起 PPPoE 呼叫。
- LAC 和用戶端開始 LCP 協商。
- CHAP 協商完成後，LAC 傳送 CHAP 質詢。
- 用戶端傳送 CHAP 響應。
- LAC 根據收到的域名檢查是否應將用戶端會話轉發到 LNS。該檢查可以在本地進行，也可以使用 RADIUS 伺服器進行。在轉發會話之前，也可以在此處對用戶端進行身份驗證。
- LAC 建立 L2TP 隧道。
- LNS 檢查是否允許 LAC 開啟隧道並執行身份驗證過程。隧道已啟動並準備好轉發 VPDN 會話。
- LAC 將與用戶端協商的 LCP 選項、使用者名稱和密碼轉發到 LNS。
- LNS 在本地或使用 RADIUS 對用戶端進行身份驗證，併發送 CHAP Success 或 CHAP Failure 訊息。
- 執行 IP 控制協定（IPCP）階段，安裝 IP 地址和路由。此時，會話被視為已建立。
