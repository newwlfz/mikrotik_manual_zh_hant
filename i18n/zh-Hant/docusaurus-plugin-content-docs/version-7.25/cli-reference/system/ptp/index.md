---
sidebar_key: "cli-reference/system/ptp/index"
sidebar_position: 1
title: "ptp"
sidebar_label: 'ptp'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/ptp
captured_at: '2026-11-01T21:25:37+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ptp {#systemptp}
**條件：** !smips
**系統能力：** ptp
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="priority1" typ="enum (auto) { auto:0 }"></ArgTableRow>
<ArgTableRow arg="priority2" typ="enum (auto)"></ArgTableRow>
<ArgTableRow arg="delay-mode" typ="enum (auto | e2e | p2p)"></ArgTableRow>
<ArgTableRow arg="transport" typ="enum (auto | ipv4 | l2-non-forwardable | l2-forwardable)"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum (default | 802.1as | g8275.1 | aes67 | smpte-2059)"></ArgTableRow>
<ArgTableRow arg="domain" typ="enum (auto)"></ArgTableRow>
<ArgTableRow arg="ptp-mode" typ="enum (ordinary-clock | transparent-clock)"></ArgTableRow>
</ArgTable>
