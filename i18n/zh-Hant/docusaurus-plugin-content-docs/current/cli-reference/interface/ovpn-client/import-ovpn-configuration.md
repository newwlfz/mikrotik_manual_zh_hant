---
sidebar_key: "cli-reference/interface/ovpn-client/import-ovpn-configuration"
sidebar_position: 1
title: "import-ovpn-configuration"
sidebar_label: 'import-ovpn-configuration'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ovpn-client/import-ovpn-configuration
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ovpn-client/import-ovpn-configuration {#interfaceovpn-clientimport-ovpn-configuration}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="file-name" typ="file">要匯入的 .ovpn 用戶端配置檔案路徑。</ArgTableRow>
<ArgTableRow arg="skip-cert-import" typ="bool">如果證書是手動新增的，則忽略 .ovpn 檔案中的證書資訊。</ArgTableRow>
<ArgTableRow arg="key-passphrase" typ="string">證書私鑰的密碼短語。</ArgTableRow>
<ArgTableRow arg="ovpn-user" typ="string">用於與 OVPN 伺服器進行身份驗證的使用者名稱。</ArgTableRow>
<ArgTableRow arg="ovpn-password" typ="string">用於與 OVPN 伺服器進行身份驗證的密碼。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="progress" typ="string">匯入進度狀態。</ArgTableRow>
</ArgTable>
