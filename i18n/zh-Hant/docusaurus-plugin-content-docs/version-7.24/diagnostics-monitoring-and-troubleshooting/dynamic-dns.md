---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/dynamic-dns"
sidebar_position: 18
title: "動態 DNS"
sidebar_label: "動態 DNS"
description: "動態 DNS 更新工具支援使用符合 RFC 的演算法為動態 IP 地址安全更新域名記錄，但僅支援 hmac-md5。它需要 BIND DNS 伺服器，並與 IP、DNS server、key 和 TTL 等指定屬性配合工作。"
tags:
  - 'dns-updates'
  - 'dynamic-ip'
  - 'hmac-md5'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/dynamic-dns
captured_at: '2026-11-04T11:27:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/tool/dns-update`

**標準：** `RFC 2136, RFC 3007`

動態 DNS 更新工具提供了一種讓域名始終指向動態 IP 地址的方法。它透過向擁有待更新區域的名稱伺服器傳送域名系統更新請求來工作。也支援安全 DNS 更新。

DNS 更新工具僅支援一種演算法 - **hmac-md5**。它是用於對 DNS 訊息進行簽名的唯一提議演算法。

:::warning
DNS 更新工具僅適用於 BIND 伺服器；它無法與 DynDNS、EveryDNS 或任何其他類似服務配合使用。
:::

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP*; 預設： ) | 定義與域名關聯的 IP 地址。 |
| **dns-server** (*IP*; 預設： ) | 要將更新發送到的 DNS 伺服器。 |
| **key** (*string*; 預設： ) | 用於訪問伺服器的授權金鑰。 |
| **key-name** (*string*; 預設： ) | 用於訪問伺服器的授權金鑰名稱（類似於使用者名稱）。 |
| **name** (*string*; 預設： ) | 要附加到 IP 地址的名稱。 |
| **ttl** (*integer*; 預設： ) | 該項的生存時間（以秒為單位）。 |
| **zone** (*string*; 預設： ) | 要更新域名的 DNS 區域。 |

:::warning
路由器上的系統時鐘時間與 DNS 伺服器的時間相差不能超過 5 分鐘。否則，DNS 伺服器將忽略此請求。
:::

## 示例 {#example}

要告訴 23.34.45.56 DNS 伺服器將 myzone.com 區域中的 mydomain 名稱（重新）關聯到 68.42.14.4 IP 地址，並指定金鑰名稱為 dns-update-key、實際金鑰為 update：

```ros
[admin@MikroTik] tool> dns-update dns-server=23.34.45.56 name=mydomain \
\... zone=myzone.com address=68.42.14.4 key-name=dns-update-key key=update
```
