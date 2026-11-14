---
sidebar_key: "cli-reference/cmr/push-button"
sidebar_position: 5
title: "push-button"
sidebar_label: 'push-button'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/push-button
captured_at: '2026-11-09T11:35:47.715Z'
pagination_next: "cli-reference/cmr/upgrade"
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/push-button {#cmrpush-button}
**型別：** Command

使用此命令，可以透過伺服器裝置上的物理 routerboard/reset 按鈕來完成裝置配對。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="multi { array-id, interface: iface_enum
 }" unset="1">選擇要在其上搜尋 CMR 用戶端的介面或介面列表。預設值：all.</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="state" typ="string">裝置配對的狀態。</ArgTableRow>
<ArgTableRow arg="error" typ="string" unset="1">錯誤資訊，用於配對不成功的情況。</ArgTableRow>
<ArgTableRow arg="peer" typ="multi { array-id, mac: macAddr
 }" unset="1">對端地址。</ArgTableRow>
<ArgTableRow arg="peer-id" typ="string" unset="1">對端 ID。</ArgTableRow>
</ArgTable>
