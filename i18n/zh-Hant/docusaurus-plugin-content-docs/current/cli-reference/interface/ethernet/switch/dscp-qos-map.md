---
sidebar_key: "cli-reference/interface/ethernet/switch/dscp-qos-map"
sidebar_position: 2
title: "dscp-qos-map"
sidebar_label: 'dscp-qos-map'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/dscp-qos-map
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/dscp-qos-map {#interfaceethernetswitchdscp-qos-map}
**系統能力：** musicswitch
**型別：** 目錄

全域性 DSCP 到 QoS 對映表用於將封包的 DSCP 對映到表中配置的新 QoS 屬性。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="drop-precedence" typ="enum (green | yellow | red | drop)">該 DSCP 到 QoS 對映條目的新 Drop precedence 值。</ArgTableRow>
<ArgTableRow arg="dei" typ="num">該 DSCP 到 QoS 對映條目的新 DEI 值。</ArgTableRow>
<ArgTableRow arg="pcp" typ="num">該 DSCP 到 QoS 對映條目的新 PCP 值。</ArgTableRow>
<ArgTableRow arg="priority" typ="num">該 DSCP 到 QoS 對映條目的新內部優先順序值。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="hex" typ="num"></ArgTableRow>
</ArgTable>
