---
sidebar_key: "network-management/socks/socksify"
sidebar_position: 1
title: "Socksify"
sidebar_label: "Socksify"
description: "Socksify 將透過防火牆 NAT 規則選定的流量透過上游 SOCKS5 伺服器轉發，因此不支援 SOCKS 的應用程式也可以使用 SOCKS 代理。包含一個 Tor 代理示例。"
tags:
  - 'socksify'
  - 'firewall'
  - 'nat'
source: https://manual.mikrotik.com/docs/network-management/socks/socksify
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Socksify 會透過上游 SOCKS5 伺服器轉發由防火牆規則選中的流量，適用於自身不支援 SOCKS 的應用程式。帶有 `action=socksify` 的目標 NAT 規則會把匹配的連線重定向到該服務，服務再請求 SOCKS 伺服器連線到該連線的原始目標地址。

可以同時配置多個 socksify 服務，每個服務轉發到各自的上游伺服器，因此不同的流量類別可以使用不同的代理。

前置條件：

- 上游伺服器必須支援 SOCKS5。RouterOS 的 SOCKS 伺服器在設定為 `version=5` 時可以正常工作；在預設的 `version=4` 下，SOCKS5 用戶端會被拒絕。
- `socks5-server` 僅接受 IPv4 地址。
- 新記錄建立時處於停用狀態。對記錄設定的更改需要先停用再重新啟用該記錄後才會生效，在執行期間不會生效。
- 上游憑據在 `print detail` 輸出中以明文可見。

該服務拒絕對 LAN 目標（RFC 1918 私有地址）的代理連線；日誌會在 `socksify` 主題下顯示 `cannot socksify LAN destination`。

:::warning
請使用 NAT 規則匹配條件謹慎選擇需要重定向的流量。務必使用 `dst-address-type=!local` 排除路由器自身的地址：否則，匹配範圍過大的規則會把路由器自身的服務（例如 SSH 或 WebFig）重定向到代理，從而切斷管理訪問。
:::

## 與 Tor 代理組合使用 {#use-in-combination-with-a-tor-proxy}

Socksify 可以透過 Tor 轉發流量以保護隱私。該配置會透過 Tor SOCKS5 代理伺服器轉發 HTTP 和 HTTPS 流量。

首先建立 socksify 服務：

```ros
/ip/socksify
add connection-timeout=10 disabled=no name=Tor_socksify socks5-port=9050 socks5-server=<TOR_SOCKS_PROXY_IP>
```

然後配置防火牆，對選中的流量執行 socksify，並允許其訪問該服務：

```ros
/ip/firewall/filter
add action=accept chain=input dst-port=952 protocol=tcp src-address=<SOCKS_CLIENT_IP>
/ip/firewall/nat
add action=socksify chain=dstnat dst-address-type=!local dst-port=80,443 protocol=tcp socksify-service=Tor_socksify src-address=<SOCKS_CLIENT_IP>
```

需要這條 input 接受規則，是因為被重定向的連線會到達路由器本身（socksify 服務的 952 埠）；當 input 過濾器丟棄來自用戶端的流量時，服務就永遠看不到這些流量。`dst-address-type=!local` 匹配條件會把發往路由器自身地址的流量排除在代理之外。

## Tor 容器與安全 DNS 教程 {#tor-container-and-secure-dns-tutorial}

RouterOS 還可以在容器中執行 Tor 代理。當你使用 Tor 瀏覽網頁時，請考慮同時保護你的 DNS 請求。

有關詳細的分步說明，請觀看 [Tor 容器與安全 DNS 教程影片](https://www.youtube.com/watch?v=ECRjxpb5IgE&lc=Ugy6V6EEAwyu2UC8ZJB4AaABAg)。
