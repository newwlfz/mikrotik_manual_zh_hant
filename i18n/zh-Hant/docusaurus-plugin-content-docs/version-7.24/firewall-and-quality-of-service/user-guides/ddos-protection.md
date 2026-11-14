---
sidebar_key: "firewall-and-quality-of-service/user-guides/ddos-protection"
sidebar_position: 4
title: "DDoS 防護"
sidebar_label: "DDoS 防護"
description: "本頁介紹 MikroTik RouterOS 的 DDoS 防護配置，涵蓋用於檢測和阻止 HTTP floods、SYN floods 和 DNS amplification 等各類攻擊的防火牆規則。內容包括 address lists、firewall chains 以及特定 TCP SYN cookie 設定的詳細配置示例，以緩解 DoS/DDoS 攻擊。"
tags:
  - 'firewall'
  - 'ddos'
  - 'syn-flood'
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/user-guides/ddos-protection
captured_at: '2026-11-04T11:28:28+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

拒絕服務（DoS）或分散式拒絕服務（DDoS）攻擊是一種惡意嘗試，透過用大量網際網路流量淹沒目標或其周邊基礎設施，來干擾目標伺服器、服務或網路的正常流量。DDoS 攻擊有多種型別，例如 HTTP 泛洪、SYN 泛洪、DNS 放大等。

![](/img/d7c46fdda6459931.jpg)

## DDoS 防護 {#protection-against-ddos}

### 配置命令 {#configuration-lines}

:::warning
這些規則只是對防火牆的改進，請不要忘記正確保護你的裝置。
:::

```ros
/ip/firewall/address-list
add list=ddos-attackers
add list=ddos-targets
/ip/firewall/filter
add chain=forward connection-state=new action=jump jump-target=detect-ddos
add action=return chain=detect-ddos dst-limit=32,32,src-and-dst-addresses/10s
add action=add-dst-to-address-list address-list=ddos-targets address-list-timeout=10m chain=detect-ddos
add action=add-src-to-address-list address-list=ddos-attackers address-list-timeout=10m chain=detect-ddos
/ip/firewall/raw
add action=drop chain=prerouting dst-address-list=ddos-targets src-address-list=ddos-attackers
```

### 配置說明 {#configuration-explained}

首先，我們會把每個新連線傳送到特定的防火牆鏈中，並在那裡檢測 DDoS：

```ros
/ip/firewall/filter/add chain=forward connection-state=new action=jump jump-target=detect-ddos
```

在新建的鏈中，我們會新增以下帶有 "dst-limit" 引數的規則。該引數的格式如下：**dst-limit=****count[/time],burst,mode[/expire]**。我們會根據目標地址和源地址流，匹配 32 個數據包，突發為 32 個數據包，每 10 秒更新一次。該規則會一直生效，直到超過給定速率。

```ros
/ip/firewall/filter/add chain=detect-ddos dst-limit=32,32,src-and-dst-addresses/10s action=return
```

到目前為止，所有合法流量都應透過 "action=return"，但在 DoS/DDoS 的情況下，"dst-limit" 緩衝區會被填滿，規則將不再“捕獲”任何新流量。接下來是處理攻擊的後續規則。我們先為要丟棄的攻擊者和受害者建立列表：

```ros
/ip/firewall/address-list/add list=ddos-attackers
/ip/firewall/address-list/add list=ddos-targets
/ip/firewall/raw/add chain=prerouting action=drop src-address-list=ddos-attackers dst-address-list=ddos-targets
```

透過防火牆過濾規則部分，我們會把攻擊者新增到 "DDoS-attackers"，把受害者新增到 "ddos-targets" 列表：

```ros
/ip/firewall/filter
add action=add-dst-to-address-list address-list=ddos-targets address-list-timeout=10m chain=detect-ddos
add action=add-src-to-address-list address-list=ddos-attackers address-list-timeout=10m chain=detect-ddos
```

## SYN 攻擊 {#syn-attack}

### SYN 泛洪 {#syn-flood}

SYN 泛洪是一種 DoS 攻擊形式，攻擊者向目標系統傳送一連串 SYN 請求，試圖消耗足夠的伺服器資源，使系統無法響應合法流量。幸運的是，RouterOS 針對此類攻擊提供了特定功能：

```ros
/ip/settings/set tcp-syncookies=yes
```

該功能的工作方式是發回包含少量加密雜湊的 SYN-ACK 封包，響應用戶端會在其 ACK 封包中回顯該雜湊。如果核心在回覆封包中看不到這個“cookie”，就會認為連線是偽造的並將其丟棄。

### SYN-ACK 泛洪 {#syn-ack-flood}

SYN-ACK 泛洪是一種攻擊方法，它以高速率向目標伺服器傳送偽造的 SYN-ACK 封包。伺服器需要大量資源來亂序處理此類封包（不符合正常的 SYN、SYN-ACK、ACK TCP 三次握手機制）。伺服器可能忙於處理攻擊流量，以至於無法處理合法流量，因此攻擊者便實現了 DoS/DDoS 狀態。在 RouterOS 中，我們可以配置前面示例中的類似規則，但更針對 SYN-ACK 泛洪：

```ros
/ip/firewall/filter/add action=return chain=detect-ddos dst-limit=32,32,src-and-dst-addresses/10s protocol=tcp tcp-flags=syn,ack
```
