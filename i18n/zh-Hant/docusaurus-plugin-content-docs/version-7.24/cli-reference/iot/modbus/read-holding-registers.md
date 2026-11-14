---
sidebar_key: "cli-reference/iot/modbus/read-holding-registers"
sidebar_position: 1
title: "read-holding-registers"
sidebar_label: "read-holding-registers"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/iot/modbus/read-holding-registers
captured_at: '2026-11-01T21:28:17+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/modbus/read-holding-registers {#iotmodbusread-holding-registers}
**包：** iot
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="slave-id" typ="num"></ArgTableRow>
<ArgTableRow arg="reg-addr" typ="num"></ArgTableRow>
<ArgTableRow arg="num-regs" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="values" typ="multi { array-id, value: num
 }"></ArgTableRow>
</ArgTable>
