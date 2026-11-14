---
sidebar_key: "cli-reference/routing/bgp/session/clear"
sidebar_position: 1
title: "clear"
sidebar_label: 'clear'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/bgp/session/clear
captured_at: '2026-11-01T21:25:05+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bgp/session/clear {#routingbgpsessionclear}
**條件：** !smips
**型別：** 命令

清除會話標誌。例如，要在達到字首限制後能夠重新建立會話，必須清除 "limit-exceeded" 標誌。可以透過指定 `flag` 引數來完成，該引數可以取以下值：

* input-last-notification  
* limit-exceeded  
* output-last-notification  
* refused-cap-opt  
* stopped

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="flag" typ="enum (refused-cap-opt | stopped | limit-exceeded | input-last-notification | output-last-notification)">要從 BGP 會話中清除的標誌。</ArgTableRow>
</ArgTable>
