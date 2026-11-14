---
sidebar_key: "virtual-private-networks/pptp"
sidebar_position: 9
title: "PPTP"
sidebar_label: "PPTP"
description: "本頁介紹 MikroTik RouterOS 中 PPTP（點對點隧道協定）的實現，涵蓋用戶端和伺服器配置選項，包括認證方式、MTU/MRRU 設定以及 TCP 埠要求。文中還指出了安全方面的侷限性，並提供了用於 PPTP 用戶端連線的示例設定命令。"
tags:
  - 'pptp'
  - 'vpn'
source: https://manual.mikrotik.com/docs/7.25/virtual-private-networks/pptp
captured_at: '2026-11-04T11:23:22+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Point-to-Point Tunneling Protocol (PPTP) 是一種傳統 VPN 協定，旨在為遠端訪問連線封裝 PPP 流量。PPTP 受到許多作業系統和網路裝置的廣泛支援，因此在以相容性為首要需求的環境中，部署和配置都很簡單。

由於存在多個已知的加密和協定級漏洞，PPTP 不適合用於保護敏感或不可信的網路流量。其使用通常僅限於相容性場景、測試環境或加密強度不是主要需求的網路。

PPTP 不支援 IPv6 傳輸或 IPv6 流量轉發。

PPTP 使用 TCP 埠 1723 進行隧道管理，並使用 Generic Routing Encapsulation（GRE，IP 協定 47）進行資料傳輸，這些由 Internet Assigned Numbers Authority（IANA）分配。為使 PPTP 透過防火牆或路由器正確執行，必須允許並正確轉發 TCP 埠 1723 和 GRE 流量。

PPTP 為每個用戶端會話支援 PPP 身份驗證、加密和計費機制。身份驗證和計費可以在本地執行，也可以透過外部 RADIUS 伺服器執行。

## 靜態和動態介面 {#static-and-dynamic-interfaces}

為連線到伺服器的每條隧道都會建立一個介面。PPTP 伺服器的配置中有兩種型別的介面：

- 靜態介面是在需要引用為特定使用者建立的某個介面名稱（在防火牆規則或其他位置）時，由管理員手動新增的。
- 當用戶連線且其使用者名稱不匹配任何現有靜態條目時（或者該條目已經處於活動狀態，因為不能有兩個不同的隧道介面由同一名稱引用），動態介面會自動新增到此列表中。

動態介面在使用者連線時出現，在使用者斷開連線時消失，因此無法在路由器配置中（例如在防火牆中）引用為該使用者建立的隧道。如果需要為該使用者保留持久規則，請為該使用者建立靜態條目。否則，使用動態配置是安全的。

:::warning
無論哪種情況，都必須正確配置 PPP 使用者——靜態條目不能替代 PPP 配置。
:::

## 示例 {#example}

![](/img/35df5d1aa3979ebf.webp)

### PPTP 用戶端 {#pptp-client}

以下示例演示如何設定使用者名稱為 "MT-User"、密碼為 "StrongPass"、伺服器為 192.168.62.2 的 PPTP 用戶端：

```ros
[admin@MikroTik] > /interface/pptp-client/add connect-to=192.168.62.2 disabled=no name=pptp-out1 password=StrongPass user=MT-User
[admin@MikroTik] > /interface/pptp-client/print 
Flags: X - disabled; R - running 
 0  R name="pptp-out1" max-mtu=1450 max-mru=1450 mrru=disabled connect-to=192.168.62.2 user="MT-User" 
      password="StrongPass" profile=default-encryption keepalive-timeout=60 add-default-route=no 
      dial-on-demand=no allow=pap,chap,mschap1,mschap2 
```

### PPTP 伺服器 {#pptp-server}

在另一側，啟用 PPTP 伺服器併為特定使用者建立 PPP secret：

```ros
[admin@MikroTik] >  /interface/pptp-server/server/set enabled=yes
[admin@MikroTik] >  /ppp/secret/add local-address=10.0.0.1 name=MT-User password=StrongPass profile=default-encryption remote-address=10.0.0.5 service=pptp
[admin@MikroTik] >  interface pptp-server print
Flags: D - dynamic; R - running
Columns: NAME, USER, MTU, CLIENT-ADDRESS, UPTIME, ENCODING
#      NAME            USER     MTU  CLIENT-ADDRESS  UPTIM  ENCODING         
0  DR  <pptp-MT-User>  MT-User  1450  192.168.51.3   44m8s  MPPE128 stateless
```
