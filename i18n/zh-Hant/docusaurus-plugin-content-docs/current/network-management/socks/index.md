---
sidebar_key: "network-management/socks"
title: "SOCKS"
sidebar_label: "SOCKS"
description: "RouterOS 中的 SOCKS 代理伺服器：啟用伺服器，使用訪問列表限制誰可以使用它，使用使用者對用戶端進行身份驗證，並監控活動的代理連線。"
tags:
  - 'socks'
  - 'access-control'
  - 'proxy'
source: https://manual.mikrotik.com/docs/network-management/socks
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

SOCKS 是一種用於 TCP 連線的代理協定。支援 SOCKS 的應用程式連線到代理，指明它想要的目標地址，然後由代理建立連線並轉發資料。由於連線由代理發起，凡是能夠訪問代理的應用程式都可以使用那些原本會被防火牆規則阻止的目標地址，而且你可以在一個地方集中控制允許哪些用戶端和哪些目標地址。SOCKS 適用於任何基於 TCP 的協定，例如 HTTP、FTP 或 SSH。

RouterOS 中既包含 SOCKS 伺服器（位於 `/ip/socks`，即本頁內容），也包含用於反方向的 [Socksify](./socksify.md) 服務：把由防火牆規則選出的流量透過上游 SOCKS 伺服器轉發。

<DocCardList />

## 啟用伺服器 {#enable-the-server}

伺服器預設處於停用狀態。設定協定 `version` 並將其啟用：

```ros
/ip/socks/set version=5 enabled=yes
```

預設的 `version=4` 只接受 SOCKS4 用戶端，SOCKS5 用戶端會被拒絕。若要讓 SOCKS5 用戶端接入，請選擇 `5`；密碼認證同樣需要 version 5。

使用這些設定後，伺服器會在路由器所有地址的 TCP 埠 1080 上監聽。在你新增訪問列表規則之前，任何能夠訪問該埠的人都可以使用這個代理。

## 訪問列表 {#access-list}

**子選單：** `/ip/socks/access`

訪問列表控制伺服器接受哪些請求。規則按順序進行檢查，由第一條匹配的規則做出決定。不匹配任何規則的請求會被**允許**；空列表允許一切。若要使用限制性的列表，請在末尾新增一條 `deny` 規則：

```ros
/ip/socks/access/add src-address=192.168.0.0/24 action=allow
/ip/socks/access/add action=deny
```

除了地址和埠之外，`dst-address` 還接受域名，此時只匹配按名稱請求該目標地址的用戶端。

:::warning
請使用訪問列表或防火牆規則保護該代理。開放的 SOCKS 代理會讓任何人都能透過路由器轉發連線，例如濫用它來發送垃圾郵件。
:::

## 使用者與認證 {#users-and-authentication}

**子選單：** `/ip/socks/users`

使用 `/ip/socks/set auth-method=password` 時，用戶端必須使用列表中某個使用者的使用者名稱和密碼進行認證；如果不存在任何使用者，連線會被拒絕。認證使用 SOCKS5 使用者名稱/密碼方法：

```ros
/ip/socks/set version=5 auth-method=password
/ip/socks/users/add name=alice password=s3cret
```

新建使用者預設處於啟用狀態。密碼不會在 `print` 輸出中顯示：

```ros
[admin@MikroTik] /ip/socks/users> print
Columns: NAME, ONLY-ONE
# NAME      ONLY-ONE
0 alice     no
```

## 監控連線 {#monitor-connections}

**子選單：** `/ip/socks/connections`

這個只讀列表顯示伺服器當前轉發的連線，包括用戶端地址、請求的目標地址以及位元組計數器。`user` 列顯示已認證的使用者（如果有）：

```ros
[admin@MikroTik] /ip/socks/connections> print detail
0  src-address=192.168.0.2:59264 dst-address=198.51.100.8:21 type=out
   tx=103 rx=737 user=alice
```

## 應用示例：透過 SOCKS 伺服器使用 FTP {#application-example-ftp-through-the-socks-server}

你的網路 192.168.0.0/24 透過一臺擁有地址 203.0.113.104 和 192.168.0.1 的路由器進行偽裝（masquerade），並且防火牆阻止了直接訪問 FTP：

```ros
[admin@MikroTik] /ip/firewall/nat> print
0   chain=srcnat action=masquerade src-address=192.168.0.0/24
[admin@MikroTik] /ip/firewall/filter> print
0   chain=forward action=drop protocol=tcp src-address=192.168.0.0/24
    dst-port=21
```

若要允許用戶端 192.168.0.2 透過代理訪問位於 198.51.100.8 的 FTP 伺服器，請啟用伺服器並新增訪問規則：允許該用戶端連線到 FTP 伺服器的埠 21，並允許它向該伺服器開啟被動資料連線（高位埠），然後拒絕其他一切：

```ros
[admin@MikroTik] /ip/socks> set enabled=yes version=5
[admin@MikroTik] /ip/socks> print
                  enabled: yes
                     port: 1080
  connection-idle-timeout: 2m
          max-connections: 200
                      vrf: main
                  version: 5
              auth-method: none
[admin@MikroTik] /ip/socks> access/add src-address=192.168.0.2 dst-address=198.51.100.8 dst-port=21 action=allow
[admin@MikroTik] /ip/socks> access/add src-address=192.168.0.2 dst-address=198.51.100.8 dst-port=1024-65535 action=allow
[admin@MikroTik] /ip/socks> access/add action=deny
[admin@MikroTik] /ip/socks> access/print
0   src-address=192.168.0.2 dst-address=198.51.100.8 dst-port=21 action=allow

1   src-address=192.168.0.2 dst-address=198.51.100.8 dst-port=1024-65535 action=allow

2   action=deny
```

在傳輸進行期間，控制連線和被動資料連線會顯示在上一節所述的連線列表中。

請將 FTP 用戶端配置為使用 SOCKS，代理地址填寫路由器的地址 192.168.0.1，TCP 埠為 1080。
