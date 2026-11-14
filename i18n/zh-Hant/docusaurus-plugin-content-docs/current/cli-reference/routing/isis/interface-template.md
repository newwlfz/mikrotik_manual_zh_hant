---
sidebar_key: "cli-reference/routing/isis/interface-template"
sidebar_position: 2
title: "interface-template"
sidebar_label: 'interface-template'
source: https://manual.mikrotik.com/docs/cli-reference/routing/isis/interface-template
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/isis/interface-template {#routingisisinterface-template}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { interface: iface_enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="levels" typ="ubit (l1, l2)"></ArgTableRow>
<ArgTableRow arg="ptp" typ="switch" unset="1"></ArgTableRow>
<ArgTableRow arg="passive" typ="switch" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.hello-3way" typ="switch" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l1.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l1.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l1.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l2.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l2.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l2.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.hello-interval-dr" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.hello-interval-dr" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.metric" typ="num" unset="1"></ArgTableRow>
</ArgTable>
