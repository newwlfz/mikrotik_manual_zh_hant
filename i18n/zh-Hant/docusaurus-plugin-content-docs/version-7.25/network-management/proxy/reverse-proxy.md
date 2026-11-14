---
sidebar_key: "network-management/proxy/reverse-proxy"
sidebar_position: 2
title: "反向代理"
sidebar_label: "反向代理"
description: "RouterOS 反向代理接受 HTTPS 連線，根據 TLS 伺服器名稱選擇規則，並將請求以 HTTP 轉發到路由器後方的伺服器或容器應用。"
tags:
  - 'reverse-proxy'
  - 'certificates'
source: https://manual.mikrotik.com/docs/7.25/network-management/proxy/reverse-proxy
captured_at: '2026-11-04T11:21:13+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/ip/reverse-proxy`

反向代理使路由器後面的 Web 伺服器可以透過主機名經 HTTPS 訪問，而無需為每臺伺服器配置目標 NAT 規則。路由器在埠 443 上接受 HTTPS 連線，並根據用戶端請求的主機名選擇規則。它使用該規則的證書終止 TLS，並將請求作為 HTTP 轉發到該規則的伺服器。多臺伺服器可以共享同一個公網地址和埠，每臺伺服器都有自己的主機名和證書。

RouterOS 還會自動為容器應用新增規則。

所有規則屬性都在 [`/ip/reverse-proxy`](../../cli-reference/ip/reverse-proxy.md) CLI 參考中說明。

:::info
反向代理不支援 SMIPS 裝置（hAP lite、hAP lite TC 和 hAP mini）。
:::

## 配置示例 {#configuration-example}

此示例使位於 `192.168.88.10`、埠 8080 的 Web 伺服器可透過 `https://nas.example.com` 訪問。

前置條件：

- DNS 名稱 `nas.example.com` 解析到路由器的公網地址。
- 你擁有 `nas.example.com` 的證書和私鑰，例如來自公共證書頒發機構，分別位於檔案 `nas.crt` 和 `nas.key` 中。
- Web 伺服器在埠 8080 上接受明文 HTTP。

將這兩個檔案上傳到路由器，並將它們匯入為名為 `nas` 的證書：

```ros
/certificate/import file-name=nas.crt name=nas passphrase=""
/certificate/import file-name=nas.key passphrase=""
```

新增規則：

```ros
/ip/reverse-proxy/add sni=nas.example.com ip-address=192.168.88.10 port=8080 certificate=nas
```

預設防火牆配置會丟棄不是來自 LAN 的、發往路由器的連線。在 input 鏈中、預設丟棄規則之前接受 HTTPS：

```ros
/ip/firewall/filter/add chain=input protocol=tcp dst-port=443 in-interface-list=WAN action=accept comment="reverse proxy" place-before=[find comment="defconf: drop all not coming from LAN"]
```

有關輸入規則的更多資訊，請參閱 [過濾器](../../firewall-and-quality-of-service/firewall/filter.md)。

## 規則選擇 {#rule-selection}

路由器會將用戶端在 TLS 握手中傳送的伺服器名稱（Server Name Indication，SNI）與每個已啟用規則的 `sni` 進行比較。名稱必須完全匹配：諸如 `*.example.com` 的萬用字元不會匹配任何內容。當沒有規則匹配時，路由器會關閉連線。

## 證書 {#certificates}

路由器會向用戶端出示匹配規則的證書。當規則具有 `certificate=none` 時，路由器改為出示 [`/ip/service`](../../system-information-and-utilities/services.md) 中 `reverse-proxy` 服務的證書。當一個證書（例如萬用字元證書）涵蓋多個規則的主機名時，請設定服務證書。當規則和服務都沒有證書時，TLS 握手會失敗。

## 發往伺服器的請求 {#requests-to-the-server}

路由器從其自身地址連線到伺服器，並將每個請求作為 HTTP/1.1 轉發。即使伺服器埠為 443，它也使用明文 HTTP，因此伺服器必須在該埠上接受 HTTP。

路由器保留請求的 `Host` 頭，並新增用於告知伺服器原始用戶端資訊的頭：

- `X-Forwarded-For` 和 `X-Real-Ip` - 用戶端的地址。
- `X-Forwarded-Proto` - `https`。
- `X-Forwarded-Host` - 用戶端請求的主機名。
- `Forwarded` - 路由器地址、用戶端地址、協定和主機名，採用 RFC 7239 的格式。

## 服務埠 {#service-port}

反向代理監聽 [`/ip/service`](../../system-information-and-utilities/services.md) 中 `reverse-proxy` 服務的埠，預設為 443。僅當至少存在一個已啟用規則時，該埠才會開放。

:::warning
HTTPS Web 服務 `www-ssl` 預設也使用 443 埠。當兩個服務都啟用在同一埠上時，先啟動的那個會佔用該埠，另一個則會顯示 `cannot bind to port 443: Address in use`。重啟後，`www-ssl` 會佔用該埠，因此即使反向代理在重啟前正常工作，重啟後也會停止工作。

保持停用 `www-ssl`（這是預設值），或將其移到另一個埠：

```ros
/ip/service/set www-ssl port=8443
```
:::

## 容器應用 {#container-apps}

具有 `use-https=yes`（預設值）和 Web 介面的[容器應用](../../containers/apps/index.md)會獲得一條動態反向代理規則，並透過 `D` 標誌顯示。該規則的 `sni` 是應用 URL（`ui-url`）的主機名，規則會轉發到應用的 Web 埠。該規則使用 `/app/settings` 中設定的證書。

## 故障排除 {#troubleshooting}

反向代理會使用 `rproxy` 主題將其訊息寫入日誌：

```ros
/log/print where topics~"rproxy"
```

- `no matching rule for <name>, client: <address>:<port>` - 用戶端請求的主機名沒有任何已啟用規則將其作為 `sni`。
- `certificate missing for rule <sni>` - 規則和 `reverse-proxy` 服務都沒有證書。

當反向代理完全不接受連線時，請檢查是否至少啟用了一條規則。然後檢查 `/ip/service/print` 中 `reverse-proxy` 服務是否有 `cannot bind to port` 註釋，這意味著另一個服務（通常是 `www-ssl`）使用了相同埠。
