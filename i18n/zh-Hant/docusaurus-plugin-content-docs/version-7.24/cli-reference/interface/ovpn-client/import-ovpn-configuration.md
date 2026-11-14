---
sidebar_key: "cli-reference/interface/ovpn-client/import-ovpn-configuration"
sidebar_position: 1
title: "import-ovpn-configuration"
sidebar_label: "import-ovpn-configuration"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ovpn-client/import-ovpn-configuration
captured_at: '2026-11-01T21:27:30+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ovpn-client/import-ovpn-configuration {#interfaceovpn-clientimport-ovpn-configuration}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="file-name" typ="file">.ovpn 用戶端配置檔案</ArgTableRow>
<ArgTableRow arg="skip-cert-import" typ="bool">如果 ovpn 檔案中的證書資訊由使用者手動新增，則忽略這些證書資訊</ArgTableRow>
<ArgTableRow arg="key-passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="ovpn-user" typ="string"></ArgTableRow>
<ArgTableRow arg="ovpn-password" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>
