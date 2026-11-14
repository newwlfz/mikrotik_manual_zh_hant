---
sidebar_key: "cli-reference/openflow/flow"
sidebar_position: 1
title: "flow"
sidebar_label: 'flow'
source: https://manual.mikrotik.com/docs/cli-reference/openflow/flow
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## openflow/flow {#openflowflow}
**軟體包：** openflow
**型別：** 目錄

此選單列出負責在 OpenFlow 埠之間轉發封包的已安裝流。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="switch" typ="enum">安裝該規則的控制器名稱。</ArgTableRow>
<ArgTableRow arg="version" typ="num">安裝該流的交換器的 OpenFlow 協定版本。</ArgTableRow>
<ArgTableRow arg="match" typ="string">流條目用於匹配的匹配欄位。</ArgTableRow>
<ArgTableRow arg="actions" typ="string">應用於與流條目匹配的封包的動作。</ArgTableRow>
<ArgTableRow arg="info" typ="string">其他流條目資訊，例如優先順序、超時和 cookie。</ArgTableRow>
<ArgTableRow arg="table-id" typ="num">規則所在表的 ID。</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">該規則匹配的位元組數。</ArgTableRow>
<ArgTableRow arg="packets" typ="num">該規則匹配的封包數。</ArgTableRow>
<ArgTableRow arg="duration" typ="time">自流條目安裝以來經過的時間。</ArgTableRow>
</ArgTable>
