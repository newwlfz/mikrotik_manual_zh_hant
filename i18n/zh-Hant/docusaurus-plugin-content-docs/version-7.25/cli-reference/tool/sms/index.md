---
sidebar_key: "cli-reference/tool/sms/index"
sidebar_position: 2
title: "sms"
sidebar_label: 'sms'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/sms
captured_at: '2026-11-01T21:25:57+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/sms {#toolsms}
**條件：** !smips
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="receive-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="port" typ="alt { serial: enum
, interface: iface_enum { none }
 }"></ArgTableRow>
<ArgTableRow arg="channel" typ="num"></ArgTableRow>
<ArgTableRow arg="secret" typ="string"></ArgTableRow>
<ArgTableRow arg="allowed-number" typ="multi { array-id, number: string
 }"></ArgTableRow>
<ArgTableRow arg="sim-pin" typ="string"></ArgTableRow>
<ArgTableRow arg="sms-storage" typ="enum (modem | sim)">用於讀取、寫入、傳送和接收操作的儲存器（ETSI TS 127 005 中的 `<mem1>`、`<mem2>` 和 `<mem3>`），將用於後續 +CPMS 命令（僅在使用 AT 命令時設定生效）</ArgTableRow>
<ArgTableRow arg="polling" typ="bool">每 5s 輪詢新 SMS。建議僅在接收新 SMS 出現問題時才啟用輪詢，否則不建議啟用。</ArgTableRow>
<ArgTableRow arg="remove-sent-sms-after-send" typ="bool">在調變解調器自動儲存已傳送的 SMS 時有用</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="enum (off | running)"></ArgTableRow>
<ArgTableRow arg="last-ussd" typ="string"></ArgTableRow>
</ArgTable>
