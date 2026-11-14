---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/ip-scan"
sidebar_position: 16
title: "IP 掃描"
sidebar_label: "IP 掃描"
description: "IP scan 可發現網路上的裝置：掃描地址範圍可列出主機及其 MAC 地址、響應時間、DNS 和 SNMP 名稱，或在介面上監聽以檢視裝置使用的地址，包括使用未知靜態地址的裝置。"
tags:
  - 'ip'
  - 'arp'
  - 'scanning'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/ip-scan
captured_at: '2026-11-04T11:15:22+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

IP 掃描用於查詢網路中的裝置。它有兩種工作方式：

- 掃描地址範圍：路由器探測該範圍內的每個地址，並列出有響應的主機，以及這些主機的 MAC 地址、響應時間、DNS 名稱和 SNMP 名稱。
- 在介面上監聽：路由器不向主機發送探測包，而是列出它在該介面流量中看到的地址。

可以用它查詢印表機或攝像頭的地址，在分配地址前檢查該地址是否空閒，或者檢視某個網段上有哪些裝置。IP 掃描僅適用於 IPv4。它不適用於採用 SMIPS 架構的裝置；`/system/resource/print` 中的 `architecture-name` 會顯示路由器的架構。

## 查詢區域網路中的裝置 {#find-the-devices-on-your-lan}

掃描區域網路子網：

```ros
/tool/ip-scan address-range=192.168.88.0/24
```

```text
Columns: ADDRESS, MAC-ADDRESS, TIME, DNS, SNMP
ADDRESS        MAC-ADDRESS        TIME  DNS                  SNMP
192.168.88.1                      1ms
192.168.88.20  FE:2F:28:FC:FE:16  1ms   printer.office.lan.  Test2
192.168.88.21  FE:A2:FB:A4:C8:34  1ms
```

掃描會一直執行，直到你按 <kbd>Control</kbd>+<kbd>C</kbd> 停止，或者執行到 `duration` 指定的時間，例如 `duration=30s`。各列含義如下：

- `ADDRESS` - 主機的地址。範圍內的路由器自身地址也會列出，但不帶 MAC 地址。
- `MAC-ADDRESS` - 來自主機 ARP 應答的 MAC 地址。
- `TIME` - 對 ICMP 回顯請求的響應時間。
- `DNS` - 透過路由器的 [DNS 解析器](../network-management/dns.md) 進行反向 DNS 查詢得到的名稱，例如來自靜態 DNS 條目。許多區域網路沒有反向名稱，此時該列會保持為空。
- `SNMP` - 當主機使用團體名 `public` 應答 SNMP 查詢時，顯示該主機的系統名稱。印表機、交換器和路由器通常會在這裡顯示其名稱或型號。
- `NETBIOS` - 當主機應答 NetBIOS 名稱查詢時，顯示其 NetBIOS 名稱，例如 Windows 計算機。

只有當主機在該列有值時，該列才會出現。要將主機與裝置對應起來，請將其 MAC 地址與裝置標籤或 [DHCP 伺服器租約](../network-management/dhcp/server.md#leases) 中的主機名進行比較。

主機會在應答 ARP 時被列出，因此，即使某臺計算機的防火牆丟棄 ping，它仍然會顯示出來，只是 `TIME` 為空。

## 檢查地址是否空閒 {#check-that-an-address-is-free}

要檢查單個地址，請僅掃描該地址：

```ros
/tool/ip-scan address-range=192.168.88.50 duration=5s
```

列表為空表示當時沒有裝置應答。已關閉的裝置也不會應答，因此在將地址作為靜態地址分配給伺服器之前，還要檢查該地址不在 DHCP 伺服器的地址池中，並且那裡沒有它的租約。

## 查詢地址未知的裝置 {#find-a-device-with-an-unknown-address}

使用另一子網靜態地址的裝置（例如攝像頭，或使用出廠地址的交換器）不會應答對 LAN 範圍的掃描。此時應改為在介面上監聽：當裝置傳送流量時，例如傳送針對其閘道器的 ARP 請求，路由器就會列出它的地址。裝置在啟動時會發送此類流量，因此在掃描執行期間重啟裝置：

```ros
/tool/ip-scan interface=bridge duration=30s
```

```text
Columns: ADDRESS, MAC-ADDRESS, TIME
ADDRESS       MAC-ADDRESS        TIME
172.16.99.5   FE:6B:12:9C:3A:05
192.168.88.1                     0ms
```

172.16.99.5 處的裝置位於網橋上，儘管其地址不在 LAN 子網中。路由器自身的地址也會列出。要從路由器訪問該裝置，請臨時將一個屬於其子網的地址新增到網橋上，並在用完後將其刪除：

```ros
/ip/address/add address=172.16.99.1/24 interface=bridge
/ping 172.16.99.5 count=3
/ip/address/remove [find address="172.16.99.1/24"]
```

路由器會在該裝置所在子網中直接訪問它。LAN 中的計算機只有在裝置的閘道器是你新增的地址時，才能透過路由器訪問該裝置；否則，請為該計算機配置一個屬於裝置子網的第二個地址。

在此模式下，路由器會列出它在到達介面上其 CPU 的流量中看到的地址。在啟用了硬體解除安裝的網橋上，這類流量是廣播流量（例如 ARP 請求）以及發往路由器的流量；其他兩個裝置之間的流量不會被看到。不傳送任何流量的裝置不會出現。

## 掃描遠端網路 {#scan-a-remote-network}

範圍可以是路由器後面的網路，例如透過 VPN 到達的分支機構。此類網路上的主機透過 ping 查詢，因此列表中沒有 MAC 地址，並且丟棄 ping 的主機不會出現：

```ros
/tool/ip-scan address-range=198.51.100.0/29 duration=8s
```

```text
Columns: ADDRESS, TIME, SNMP
ADDRESS       TIME  SNMP
198.51.100.1  0ms   Test2
198.51.100.2  0ms   Test2
198.51.100.3  0ms   Test2
```

在那裡找到的主機也會收到 SNMP 和 NetBIOS 查詢。

當你同時指定 `address-range` 和 `interface` 時，路由器會掃描該範圍，結果與不指定 `interface` 時相同。

## 技術細節 {#technical-details}

對於直連子網中的地址範圍，路由器會向每個地址傳送 ARP 請求。對於每個應答的主機，它會發送：

- 一個 ICMP 回顯請求，用於獲取 `TIME`。
- 一個 SNMPv1 請求，使用團體名 `public` 查詢系統名稱（`sysName`），用於獲取 `SNMP`。
- 一個發往 UDP 埠 137 的 NetBIOS 名稱查詢，用於獲取 `NETBIOS`。

它還會透過其 DNS 解析器查詢每個地址的名稱，用於獲取 `DNS`。

在兩種模式下，路由器還會在介面上傳送一個 BOOTP 請求。能夠應答 BOOTP 請求的 DHCP 伺服器可以將一個地址租給路由器的 MAC 地址。RouterOS DHCP 伺服器預設只對靜態租約應答 BOOTP 請求（`bootp-support=static`），而在 `bootp-support=dynamic` 時會對所有用戶端應答。

有關引數，請參閱 [`/tool/ip-scan` CLI 參考](../cli-reference/tool/ip-scan.md)。
