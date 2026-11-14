---
sidebar_key: "cli-reference/ip/pool/used"
sidebar_position: 1
title: "used"
sidebar_label: "used"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/pool/used
captured_at: '2026-11-01T21:28:52+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/pool/used {#ippoolused}
**型別：** 目錄

選單列出 IP 池中所有已使用的 IP 地址。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="pool" typ="enum">IP 池的名稱。</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">從池中分配給用戶端的 IP 地址。</ArgTableRow>
<ArgTableRow arg="owner" typ="string">獲取此 IP 地址的服務名稱。</ArgTableRow>
<ArgTableRow arg="info" typ="string">附加資訊，例如，對於 DHCP——來自租約選單的 MAC 地址；對於 PPP——PPP 型別用戶端的連線使用者名稱。</ArgTableRow>
</ArgTable>
