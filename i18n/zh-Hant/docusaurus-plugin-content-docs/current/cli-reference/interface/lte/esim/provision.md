---
sidebar_key: "cli-reference/interface/lte/esim/provision"
sidebar_position: 5
title: "provision"
sidebar_label: 'provision'
source: https://manual.mikrotik.com/docs/cli-reference/interface/lte/esim/provision
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/lte/esim/provision {#interfacelteesimprovision}
**條件：** !smips
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="activation-code" typ="string">配置檔案啟用碼。示例：LPA:1$server.example.io$ABCD10EFGHI5KL6M</ArgTableRow>
<ArgTableRow arg="activate" typ="bool">在配置檔案開通後啟用新建立的配置檔案（預設：是）</ArgTableRow>
<ArgTableRow arg="sm-dp-plus" typ="string">SM-DP+ 伺服器主機名。示例：sm-dp-plus=server.example.io</ArgTableRow>
<ArgTableRow arg="matching-id" typ="string">啟用碼令牌。示例：matching-id=ABCD10EFGHI5KL6M</ArgTableRow>
<ArgTableRow arg="confirmation-code" typ="string">運營商提供的可選程式碼</ArgTableRow>
<ArgTableRow arg="sm-dp-plus-oid" typ="string">運營商提供的可選 SM-DP+</ArgTableRow>
<ArgTableRow arg="force-confirmation" typ="bool">不等待使用者確認並自動接受配置檔案開通（預設：否）</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="iccid" typ="string"></ArgTableRow>
<ArgTableRow arg="spn" typ="string"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
