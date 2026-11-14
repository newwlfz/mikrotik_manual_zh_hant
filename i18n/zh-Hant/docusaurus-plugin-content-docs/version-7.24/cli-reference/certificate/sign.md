---
sidebar_key: "cli-reference/certificate/sign"
sidebar_position: 17
title: "sign"
sidebar_label: "sign"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/certificate/sign
captured_at: '2026-11-01T21:26:30+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## certificate/sign {#certificatesign}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-crl-host" typ="multi { array-id, host: string
 }">將 CRL URL 新增到建立的證書</ArgTableRow>
<ArgTableRow arg="ca-on-smart-card" typ="bool">將 CA 的私鑰儲存在智慧卡上</ArgTableRow>
<ArgTableRow arg="ca" typ="enum">簽發 CA</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>
