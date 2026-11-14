---
sidebar_key: "cli-reference/ip/dhcp-relay/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/dhcp-relay/monitor
captured_at: '2026-11-01T21:23:50+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-relay/monitor {#ipdhcp-relaymonitor}
**型別：** 命令

顯示 DHCP 中繼的計數器。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="requests" typ="num">中繼轉發給伺服器的用戶端請求數量。</ArgTableRow>
<ArgTableRow arg="responses" typ="num">中繼遞送給用戶端的伺服器回覆數量。</ArgTableRow>
</ArgTable>
