---
sidebar_key: "virtual-private-networks/pppoe/mlppp-over-single-and-multiple-links"
sidebar_position: 2
title: "基於單鏈路和多鏈路的 MLPPP"
sidebar_label: "基於單鏈路和多鏈路的 MLPPP"
description: "MLPPP 透過將資料拆分並重新組合到多條邏輯或物理鏈路上來增強 PPP 鏈路，從而在不升級硬體的情況下提升頻寬。它同時支援單鏈路（使用 MRRU）和多鏈路配置，並提供了 PPPoE 伺服器/用戶端設定的示例。"
tags:
  - 'mlppp'
  - 'ppp'
  - 'lcp'
source: https://manual.mikrotik.com/docs/virtual-private-networks/pppoe/mlppp-over-single-and-multiple-links
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**標準：** `RFC 1990`

Multi-Link Point to Point Protocol（MP、Multi-Link PPP、MultiPPP 或 MLPPP）是一種在多個邏輯資料鏈路上拆分、重組和排序資料的方法。

在一對裝置之間存在多條 DSL 鏈路的情況下，可以透過使用 Multi-Link PPP 來“拓寬管道”，從而提升兩臺裝置之間的效能，而無需採用更新、更昂貴的技術。

大包實際上會被拆分成片段，並均勻地透過所有邏輯資料鏈路傳送。這一過程瞬時完成，且不會損失頻寬。需要理解的是，鏈路另一端必須使用相同的協定來重組你的資料。

Multilink 基於 [LCP](../../mobile-networking/ppp.md#introduction) 選項協商，該協商允許向對端表明自己能夠合併多條物理鏈路。

## 單鏈路 MLPPP {#mlppp-over-single-link}

通常，由於開銷，透過 PPP 鏈路傳送的封包大小會減小。MP 可用於在單條 ppp 鏈路上傳送和接收完整幀。為實現這一點，Multilink Protocol 使用額外的 LCP 配置選項 **Multilink Maximum Received Reconstructed Unit (MRRU)**

要在單條鏈路上啟用 Multi-link PPP，必須指定 MRRU（Maximum Receive Reconstructed Unit）選項。如果雙方都支援此功能，則無需進行 MSS 調整（在防火牆 mangle 中）。研究表明，與每個用戶端使用 2 條 mangle 規則相比，MRRU 的 CPU 開銷更小。MRRU 允許你將封包劃分到多個通道，因此可提高可能的 MTU 和 MRU（最高 65535 位元組）。

在 Windows 下，可以在網路標籤頁的“設定”按鈕中啟用“Negotiate multi-link for single link connections”。其 MRRU 被硬編碼為 1614。

:::warning
啟用 MPPE 加密時，MTU 會減少 4 位元組以確保正常工作
:::

### 配置示例 {#configuration-example}

讓我們配置一個相容 Windows 用戶端並啟用 MRRU 的 PPPoE 伺服器。

```ros
[admin@RB800] /interface/pppoe-server/server> add service-name=myPPP interface=ether1 mrru=1614
[admin@RB800] /interface/pppoe-server/server> print 
Flags: X - disabled 
 0   service-name="myPPP" interface=ether1 max-mtu=1480 max-mru=1480 mrru=1614 
     authentication=pap,chap,mschap1,mschap2 keepalive-timeout=10 one-session-per-host=no 
     max-sessions=0 default-profile=default 
 
```

簡而言之——標準 PPP 鏈路——只需在兩端指定 MRRU。

## 多鏈路 MLPPP {#mlppp-over-multiple-links}

多鏈路 MLPPP 允許在多個物理連線上建立一條 PPP 鏈路。所有 PPP 鏈路必須來自同一臺伺服器（伺服器必須支援多鏈路 MLPPP），並且所有 PPP 鏈路必須具有相同的使用者名稱和密碼。

而要啟用 MLPPP，你只需建立一個 PPP 用戶端並指定多個介面，而不是單個介面。RouterOS 僅支援 MLPPP 用戶端。目前沒有可用的 MLPPP 伺服器支援。

### 配置示例 {#configuration-example-1}

![](/img/7c7ea14f6d0a9d21.webp)

ISP 為其客戶提供兩條物理鏈路（DSL 線路），每條 1Mbps。要獲得聚合的 2Mbps 管道，我們必須設定 MLPPP。假設 ISP 路由器已預配置為支援 MLPPP。

路由器（R1）上的配置為：

```ros
/interface/pppoe-client 
   add service-name=ISP interface=ether1,ether2 user=xxx password=yyy disabled=no \
   add-default-route=yes use-peer-dns=yes
```

```ros
[admin@RB800] /interface/pppoe-client> print 
Flags: X - disabled, R - running 
 0    name="pppoe-out1" max-mtu=1480 max-mru=1480 mrru=disabled interface=ether1,ether2 
      user="xxx" password="yyy" profile=default service-name="ISP" ac-name="" add-default-route=yes
      dial-on-demand=no use-peer-dns=yes allow=pap,chap,mschap1,mschap2  
```

現在，當 PPPoE 用戶端連線後，我們可以設定其餘配置、本地網路地址、啟用 DNS 請求、設定 masquerade 和防火牆

```ros
/ip/address/add address=192.168.88.1/24 interface=local

/ip/dns/set allow-remote-request=yes

/ip/firewall/nat
add chain=srcnat action=masquerade out-interface=pppoe-out1

/ip/firewall/filter
add chain=input connection-state=invalid action=drop \
	comment="Drop Invalid connections"  
add chain=input connection-state=established action=accept \
	comment="Allow Established connections"  
add chain=input protocol=icmp action=accept \
	comment="Allow ICMP" 
add chain=input src-address=192.168.88.0/24 action=accept \
	in-interface=!pppoe-out1
add chain=input action=drop comment="Drop everything else"   
```

如需更高階的路由器和客戶保護，請檢視[防火牆示例](../../firewall-and-quality-of-service/firewall/filter.md)。
