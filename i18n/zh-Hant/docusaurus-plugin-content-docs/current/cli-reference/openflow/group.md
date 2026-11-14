---
sidebar_key: "cli-reference/openflow/group"
sidebar_position: 2
title: "group"
sidebar_label: 'group'
source: https://manual.mikrotik.com/docs/cli-reference/openflow/group
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## openflow/group {#openflowgroup}
**包：** openflow
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="switch" typ="enum">安裝該組的控制器名稱。</ArgTableRow>
<ArgTableRow arg="id" typ="num">組的識別符號。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (all | select | indirect | ff)">組型別，決定動作桶的處理方式：all、select、indirect 或 fast failover。</ArgTableRow>
<ArgTableRow arg="bucket-count" typ="num">組中動作桶的數量。</ArgTableRow>
<ArgTableRow arg="flow-count" typ="num">引用該組的流表項數量。</ArgTableRow>
<ArgTableRow arg="buckets" typ="string">組中動作桶的列表。</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">該組處理的位元組數。</ArgTableRow>
<ArgTableRow arg="packets" typ="num">該組處理的封包數。</ArgTableRow>
<ArgTableRow arg="duration" typ="time">自該組安裝以來經過的時間。</ArgTableRow>
<ArgTableRow arg="bucket-stats" typ="string">每個桶的封包和位元組統計資訊。</ArgTableRow>
</ArgTable>
