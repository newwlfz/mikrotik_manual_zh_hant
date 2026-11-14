---
sidebar_key: "cli-reference/tool/traffic-generator/inject"
sidebar_position: 2
title: "inject"
sidebar_label: 'inject'
source: https://manual.mikrotik.com/docs/cli-reference/tool/traffic-generator/inject
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/inject {#tooltraffic-generatorinject}
**型別：** 命令
將原始資料注入到介面。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum">將原始資料注入到的介面。</ArgTableRow>
<ArgTableRow arg="data" typ="string">要注入的原始資料，以十六進位制字串表示。</ArgTableRow>
<ArgTableRow arg="priority" typ="num" unset="1">注入封包的優先順序。</ArgTableRow>
</ArgTable>
