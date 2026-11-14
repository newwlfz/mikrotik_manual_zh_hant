---
sidebar_key: "cli-reference/ip/tftp/settings"
sidebar_position: 1
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/cli-reference/ip/tftp/settings
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/tftp/settings {#iptftpsettings}
**型別：** 設定目錄

TFTP 伺服器的設定。參見 [TFTP](../../../system-information-and-utilities/tftp.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="max-block-size" typ="enum (512 | 1454 | 4096 | 8192) { 512:512, 1454:1454, 4096:4096, 8192:8192 }">當用戶端請求塊大小時，路由器接受的最大塊大小（`blksize` 選項）；請求更大值的用戶端將得到此大小。未請求的用戶端使用 512 位元組。值：`512`、`1454`、`4096`、`8192`。預設：4096。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">TFTP 伺服器監聽的 VRF。預設：main。</ArgTableRow>
</ArgTable>
