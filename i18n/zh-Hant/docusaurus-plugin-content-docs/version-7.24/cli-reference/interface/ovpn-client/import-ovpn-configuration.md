---
title: "import-ovpn-configuration"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ovpn-client/import-ovpn-configuration
captured_at: '2026-11-28T10:19:39.818Z'
pagination_prev: "cli-reference/interface/ovpn-client"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/ovpn-client/import-ovpn-configuration 
**類型：** 指令

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file-name" typ="file">.ovpn client configuration file</ArgTableRow>
<ArgTableRow arg="skip-cert-import" typ="bool">Ignore certificate information in ovpn file in case these are added by user manualy</ArgTableRow>
<ArgTableRow arg="key-passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="ovpn-user" typ="string"></ArgTableRow>
<ArgTableRow arg="ovpn-password" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>
