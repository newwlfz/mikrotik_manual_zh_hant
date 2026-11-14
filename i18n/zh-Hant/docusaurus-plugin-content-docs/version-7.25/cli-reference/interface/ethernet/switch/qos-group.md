---
sidebar_key: "cli-reference/interface/ethernet/switch/qos-group"
sidebar_position: 19
title: "qos-group"
sidebar_label: 'qos-group'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/qos-group
captured_at: '2026-11-01T21:22:38+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos-group {#interfaceethernetswitchqos-group}
**系統能力：** musicswitch
**型別：** 目錄

全域性 QoS 組表用於基於 VLAN、基於協定和基於 MAC 的 QoS 組分配配置。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">QoS 組的名稱。</ArgTableRow>
<ArgTableRow arg="pcp" typ="num">QoS 組的 PCP 新值。</ArgTableRow>
<ArgTableRow arg="dei" typ="num">QoS 組的 DEI 新值。</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">QoS 組的 DSCP 新值。</ArgTableRow>
<ArgTableRow arg="priority" typ="num">內部優先順序具有本地意義，用於將流量分類到埠上的不同出口佇列（1 最高，15 最低）。</ArgTableRow>
<ArgTableRow arg="drop-precedence" typ="enum (green | yellow | red | drop)">丟棄優先順序是用於封包入隊或丟棄的內部 QoS 屬性。</ArgTableRow>
</ArgTable>
