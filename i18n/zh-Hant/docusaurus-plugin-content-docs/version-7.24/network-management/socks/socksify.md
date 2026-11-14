---
sidebar_key: "network-management/socks/socksify"
sidebar_position: 1
title: "Socksify"
sidebar_label: "Socksify"
description: "Socksify 能夠透過 SOCKS 代理伺服器路由特定流量，使沒有原生代理支援的應用程式也能使用代理。它支援多種服務，並可透過防火牆過濾器進行配置以實現精確的流量管理，包括使用 TOR 的示例。"
tags:
  - 'socksify'
  - 'firewall'
  - 'nat'
source: https://manual.mikrotik.com/docs/7.24/network-management/socks/socksify
captured_at: '2026-11-04T11:32:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

[*Socksify CLI 參考*](../../cli-reference/ip/socksify.md)

Socksify 是一項服務，允許路由器透過 SOCKS 代理伺服器傳送特定流量，即使應用程式本身不原生支援代理連線。  
它會攔截網路呼叫，並透過已配置的 SOCKS 代理重定向這些呼叫。

Socksify 服務與 [NAT](../../firewall-and-quality-of-service/firewall/nat.md) 動作 `socksify` 結合使用。所有可用的防火牆過濾器均可用於精確選擇僅將按應用程式/來源的流量透過 SOCKS 代理重定向。

可以同時配置多個 Socksify 服務，從而允許連線到多個 SOCKS 伺服器，以實現更好的流量管理。

### 屬性說明 {#property-description}

**子選單：** `/ip/socksify`

| 屬性 | 說明 |
| :-- | :-- |
| **disabled** (*yes* \| *no*; 預設值：yes) | Socksify 記錄是否處於活動狀態。 |
| **socks5-password** (*string*; 預設值： ) | 用於訪問 SOCKS5 代理伺服器的密碼。 |
| **socks5-user**(*string*; 預設值： ) | 用於訪問 SOCKS5 代理伺服器的使用者名稱。 |
| **connection-timeout** (*integer:* 0..3000; 預設值：60) | 以秒為單位的時間，指定在連線建立期間等待 SOCKS 代理或目標響應多長時間後因錯誤而中止。將此值設定為 0 將停用連線超時。 |
| **name**(*string*; 預設值： ) | Socksify 服務的名稱。 |
| **socks5-port**(*integer*: 1..65535; 預設值：1080) | SOCKS5 代理伺服器的監聽埠。 |
| **socks5-server** (*IPv4;* 預設值：0.0.0.0 ) | SOCKS5 代理伺服器的 IP 地址。（僅支援 IPv4 地址） |
| **port** (*integer*: 1..65535; 預設值：952) | Socksify 服務將使用的 TCP 埠。 |

## 配置示例 {#configuration-examples}

### 與 TOR SOCKS5 代理伺服器結合使用 {#use-in-combination-with-tor-socks5-proxy-server}

Socksify 可與 TOR 結合使用，為沒有整合 SOCKS 支援的應用程式實現更好的隱私和匿名性。  
下面的配置將允許你透過 TOR SOCKS5 代理伺服器轉發 HTTP/s 流量。  
首先需要配置 Socksify 服務。

```ros
/ip/socksify 
add connection-timeout=10 disabled=no name=TOR_socksify socks5-port=9050 socks5-server=<TOR_SOCKS_proxy_IP>
```

之後，你需要配置防火牆，以確保正確的流量經過 Socksify 處理，並允許 SOCKS 流量。

```ros
/ip/firewall/filter
add action=accept chain=input dst-port=952 protocol=tcp src-address=<SOCKS_client_IP> 
/ip/firewall/nat
add action=socksify chain=dstnat dst-port=80,443 protocol=tcp socksify-service=TOR_socksify src-address=<SOCKS_client_IP> 
```

### TOR 容器與安全 DNS 教程 {#tor-container-and-secure-dns-tutorial}

由於 RouterOS 支援執行容器，你還可以在容器中設定 Tor 代理。此外，如果你打算使用 Tor 瀏覽網頁，應考慮保護你的 DNS 請求。

有關詳細的分步說明，請觀看[此處](https://www.youtube.com/watch?v=ECRjxpb5IgE&lc=Ugy6V6EEAwyu2UC8ZJB4AaABAg)的影片。
