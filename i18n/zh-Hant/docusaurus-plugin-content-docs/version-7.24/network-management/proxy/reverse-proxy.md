---
sidebar_key: "network-management/proxy/reverse-proxy"
sidebar_position: 1
title: "反向代理"
sidebar_label: "反向代理"
description: "MikroTik RouterOS 上的反向代理服務允許使用簡單的 URL（而非 NAT 規則）將 HTTPS 流量路由到伺服器或應用程式，並可配置 IP/埠和 SNI 設定，但需要停用埠 443 上預設的 www-ssl 服務。"
tags:
  - 'reverse-proxy'
  - 'certificates'
source: https://manual.mikrotik.com/docs/7.24/network-management/proxy/reverse-proxy
captured_at: '2026-11-04T11:32:43+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

反向代理是一項服務，當應用設定中啟用 "use-https" 引數時，它允許路由器透過一個簡單的 URL（而不是 IP 地址並建立單獨的目標 NAT 規則）將 HTTPS 流量傳送到路由器後面的伺服器或 RouterOS 容器/應用。

:::danger
請注意，預設情況下，反向代理服務使用 HTTPS 埠 443，與預設的 www-ssl 服務埠相同。要使反向代理正常工作，您需要確保 www-ssl 服務已停用或使用不同的 TCP 埠。（[/ip/service 文件](../../system-information-and-utilities/services.md)
:::

:::info
SMIPS 裝置不支援反向代理（hAP lite、hAP lite TC 和 hAP mini）。
:::

### 屬性說明 {#property-description}

**子選單：** `/ip/reverse-proxy`

| 屬性 | 說明 |
| :-- | :-- |
| **disabled**（*yes* \| *no*；預設：**yes**） | 反向代理記錄是否處於活動狀態。 |
| **ip-address**(IPv4/IPv6; 預設：**0.0.0.0** ) | 需要代理連線到的伺服器的 IP 地址。 |
| **port**(integer: 0..65535; 預設：**0**) | 伺服器的監聽埠。 |
| **sni** (string; 預設： ) | 伺服器的伺服器名稱指示（SNI）。 |
| **certificate**(certificate; 預設：**none**) | 特定反向代理例項所使用的[證書](../../authentication-authorization-accounting/certificates.md)名稱。設定為 **none** 時，反向代理例項將使用在 `/ip/service` 選單中設定的反向代理服務證書。 |
| **vrf** (name; 預設：main ) | 要使用的虛擬路由轉發（VRF）例項。 |
| **comment**(string; 預設： ) | 專案的描述性名稱。 |
