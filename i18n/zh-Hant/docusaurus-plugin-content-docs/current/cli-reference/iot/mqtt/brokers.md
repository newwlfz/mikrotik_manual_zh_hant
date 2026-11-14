---
sidebar_key: "cli-reference/iot/mqtt/brokers"
sidebar_position: 1
title: "brokers"
sidebar_label: 'brokers'
source: https://manual.mikrotik.com/docs/cli-reference/iot/mqtt/brokers
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/mqtt/brokers {#iotmqttbrokers}
**軟體包：** iot
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="W" typ="Will message enabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="ssl" typ="bool"></ArgTableRow>
<ArgTableRow arg="client-id" typ="string"></ArgTableRow>
<ArgTableRow arg="username" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="will-topic" typ="string"></ArgTableRow>
<ArgTableRow arg="will-message" typ="string"></ArgTableRow>
<ArgTableRow arg="will-qos" typ="num"></ArgTableRow>
<ArgTableRow arg="will-retain" typ="bool"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="auto-connect" typ="bool"></ArgTableRow>
<ArgTableRow arg="keep-alive" typ="num"></ArgTableRow>
<ArgTableRow arg="parallel-scripts-limit" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="connected" typ="bool"></ArgTableRow>
</ArgTable>
