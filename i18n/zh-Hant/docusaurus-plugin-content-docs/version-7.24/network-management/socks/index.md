---
sidebar_key: "network-management/socks/index"
sidebar_position: 1
title: "SOCKS"
sidebar_label: "SOCKS"
description: "本頁介紹 MikroTik RouterOS 中的 SOCKS 代理配置，涵蓋連線超時、埠分配、用於保障安全的訪問列表以及活動連線監控等設定。它說明了如何啟用帶身份驗證的 SOCKS5/4 代理，並透過訪問規則控制用戶端與伺服器之間的流量。"
tags:
  - 'socks'
  - 'access-control'
  - 'proxy'
source: https://manual.mikrotik.com/docs/7.24/network-management/socks
captured_at: '2026-11-04T11:32:53+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 SOCKS 功能。你可以用它來配置 RouterOS 上的 SOCKS 代理行為和 socksify 規則。

<DocCardList />

SOCKS（Socket Secure）是一種代理伺服器，它允許基於 TCP 的應用資料跨越防火牆進行中繼，即使防火牆會阻止這些封包。SOCKS 協定與具體的應用協定無關，因此可用於許多服務，例如 WWW、FTP、TELNET 等。

首先，應用用戶端連線到 SOCKS 代理伺服器，然後代理伺服器查詢其訪問列表，以確定該用戶端是否被允許訪問遠端應用資源；如果允許，代理伺服器會將封包中繼到應用伺服器，並在應用伺服器與用戶端之間建立連線。

請記得配置你的應用用戶端使用 SOCKS！

你應使用訪問列表和/或防火牆保護 SOCKS 代理，禁止來自外部的訪問。未能保護代理伺服器可能會給你的網路帶來安全問題，並可能為垃圾郵件傳送者提供透過路由器傳送垃圾郵件的途徑。

### 屬性說明 {#property-description}

| 屬性 | 說明 |
| :-- | :-- |
| **connection-idle-timeout**（time；預設值：2m） | 空閒連線被終止前的等待時間 |
| **enabled**（yes \| no；預設值：no） | 是否啟用 SOCKS 代理 |
| **max-connections**（integer: 1..500；預設值：200） | 同時連線的最大數量 |
| **port**（integer: 1..65535；預設值：1080） | SOCKS 伺服器監聽連線的 TCP 埠 |
| **vrf**（VRF name；預設值：main） | 設定服務建立連線所使用的 VRF。 |
| **version**（4 \| 5；預設值：4） | SOCKS 版本。|
| **auth-method**（none \| password；預設值：none） | SOCKS 認證方法。|

## 訪問列表 {#access-list}

**子選單：** `/ip/socks/access`

在 SOCKS 訪問列表中，你可以新增用於控制對 SOCKS 伺服器訪問的規則。此列表與防火牆列表類似。

| 屬性 | 描述 |
| :-- | :-- |
| **action**（allow \| deny；預設值：allow） | allow - 允許匹配此規則的封包被轉發以進行進一步處理  deny - 拒絕匹配此規則的封包訪問 |
| **dst-address**（IP address/netmask） | 目標（伺服器）地址 |
| **dst-port**（port） | 目標 TCP 埠 |
| **src-address**（IP address/netmask） | 封包的源（用戶端）地址 |
| **src-port**（port） | 源 TCP 埠 |

## 活動連線 {#active-connections}

活動連線列表顯示透過 SOCKS 代理伺服器維護的所有已建立的 TCP 連線。

**子選單：** `/ip/socks/connections`

| 屬性 | 描述 |
| :-- | :-- |
| **dst-address**（只讀：IP address） | 目標（應用伺服器）IP 地址 |
| **rx**（只讀：integer） | 接收的位元組數 |
| **src-address**（只讀：IP address） | 源（應用用戶端）IP 地址 |
| **tx**（只讀：integer） | 傳送的位元組數 |
| **type**（只讀：in \| out \| unknown）- 連線型別 | in - 入站連線  out - 出站連線  unknown - 連線剛剛被髮起 |
| **user**（只讀：string） | 用於該連線的 `/ip/socks/users` 選單中的使用者|

## 使用者 {#users}

用於 SOCKS 伺服器訪問的特定使用者。

**子選單：** `/ip/socks/users`

| 屬性 | 說明 |
| :-- | :-- |
| **disabled**（*yes* \| *no*；預設值：yes） | 該使用者記錄是否處於活動狀態。 |
| **name**（*string*；預設值：） | SOCKS 使用者的名稱。 |
| **password**（*string*；預設值：）*[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於 SOCKS 伺服器訪問的密碼。 |
| **only-one**（*yes* \| *no*；預設值：no） |  每個使用者僅允許一個連線。 |
| **rate-limit**（*integer*；預設值：） | 特定使用者的速率限制（單位為位元每秒） |

### 示例 {#example}

檢視當前 TCP 連線：

```ros
[admin@MikroTik] /ip/socks/connections> print
 # SRC-ADDRESS                DST-ADDRESS                TX         RX
 0 192.168.0.2:3242           159.148.147.196:80         4847       2880
 1 192.168.0.2:3243           159.148.147.196:80         3408       2127
 2 192.168.0.2:3246           159.148.95.16:80           10172      25207
 3 192.168.0.2:3248           194.8.18.26:80             474        1629
 4 192.168.0.2:3249           159.148.95.16:80           6477       18695
 5 192.168.0.2:3250           159.148.95.16:80           4137       27568
 6 192.168.0.2:3251           159.148.95.16:80           1712       14296
 7 192.168.0.2:3258           80.91.34.241:80            314        208
 8 192.168.0.2:3259           80.91.34.241:80            934        524
 9 192.168.0.2:3260           80.91.34.241:80            930        524
10 192.168.0.2:3261           80.91.34.241:80            312        158
11 192.168.0.2:3262           80.91.34.241:80            312        158
[admin@MikroTik] /ip/socks/connections>
```

## 應用示例 {#application-examples}

### 透過 SOCKS 伺服器使用 FTP 服務 {#ftp-service-through-socks-server}

假設我們有一個 192.168.0.0/24 的網路進行了偽裝，使用的是一臺具有公網 IP 203.0.113.104/24 和私有 IP 192.168.0.1/24 的路由器。網路中某處有一臺 IP 地址為 198.51.100.8 的 FTP 伺服器。我們希望允許本地網路中 IP 地址為 192.168.0.2/24 的用戶端訪問此 FTP 伺服器。

我們已經對本地網路進行了偽裝：

```ros
[admin@MikroTik] /ip/firewall/nat> print
Flags: X - disabled, I - invalid, D - dynamic
 0   chain=srcnat action=masquerade src-address=192.168.0.0/24
[admin@MikroTik] /ip/firewall/nat>
```

並且防火牆中拒絕了對公共 FTP 伺服器的訪問：

```ros
[admin@MikroTik] /ip/firewall/filter> print
Flags: X - disabled, I - invalid, D - dynamic
 0   chain=forward action=drop src-address=192.168.0.0/24 dst-port=21 protocol=tcp
[admin@MikroTik] /ip/firewall/filter>
```

我們必須啟用 SOCKS 伺服器：

```ros
[admin@MikroTik] /ip/socks> set enabled=yes
[admin@MikroTik] /ip/socks> print
                    enabled: yes
                       port: 1080
    connection-idle-timeout: 2m
            max-connections: 200
               version: 4
           auth-method: none
[admin@MikroTik] /ip/socks>
```

在 SOCKS 訪問列表中新增對 IP 地址為 192.168.0.2/32 的用戶端的訪問，允許從 FTP 伺服器到該用戶端的資料傳輸（允許任意 IP 地址的目標埠 1024 到 65535），並丟棄其他所有內容：

```ros
[admin@MikroTik] /ip/socks/access> add src-address=192.168.0.2 dst-port=21 \
\... action=allow
[admin@MikroTik] /ip/socks/access> add dst-port=1024-65535 action=allow
[admin@MikroTik] /ip/socks/access> add action=deny
[admin@MikroTik] /ip/socks/access> print
Flags: X - disabled
 0   src-address=192.168.0.2 dst-port=21 action=allow
 1   dst-port=1024-65535 action=allow
 2   action=deny
[admin@MikroTik] /ip/socks/access>
```

就這樣——SOCKS 伺服器已配置完成。檢視活動連線以及傳送和接收的資料：

```ros
[admin@MikroTik] /ip/socks/connections> print
 # SRC-ADDRESS                DST-ADDRESS                TX         RX
 0 192.168.0.2:1238           198.51.100.8:21                1163       4625
 1 192.168.0.2:1258           198.51.100.8:3423              0          3231744
[admin@MikroTik] /ip/socks/connections>
```

:::warning
要使用 SOCKS 代理伺服器，你必須在 FTP 用戶端中指定其 IP 地址和埠。在本例中，IP 地址為 192.168.0.1（路由器/SOCKS 伺服器的本地 IP 地址），TCP 埠為 1080。
:::
