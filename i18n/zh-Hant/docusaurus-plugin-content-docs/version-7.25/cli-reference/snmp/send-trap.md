---
sidebar_key: "cli-reference/snmp/send-trap"
sidebar_position: 2
title: "send-trap"
sidebar_label: 'send-trap'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/snmp/send-trap
captured_at: '2026-11-01T21:25:23+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## snmp/send-trap {#snmpsend-trap}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="oid" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (integer | string | nullobj | obj-id | ip-address | counter32 | timeticks | unsigned) { integer:0x02, string:0x04, nullobj:0x05, obj-id:0x06, ip-address:0x40, counter32:0x41, timeticks:0x43, unsigned:0x47 }"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
</ArgTable>
