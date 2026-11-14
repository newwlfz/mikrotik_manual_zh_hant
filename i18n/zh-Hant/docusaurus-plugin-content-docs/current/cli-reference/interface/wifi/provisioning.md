---
sidebar_key: "cli-reference/interface/wifi/provisioning"
sidebar_position: 17
title: "provisioning"
sidebar_label: 'provisioning'
source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/provisioning
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wifi/provisioning {#interfacewifiprovisioning}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="radio-mac" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="identity-regexp" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="common-name-regexp" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="address-ranges" typ="object { address-range: super { address-range-start: address (flags=46)
, [address-range-end] -address (flags=46)
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="supported-bands" typ="multi { array-id, supported-band: enum ()
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="supported-hw-caps" typ="multi { array-id, supported-hw-cap: enum ()
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (none | create-enabled | create-disabled | create-dynamic-enabled | use-network-config)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="master-configuration" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="slave-configurations" typ="multi { array-id, slave-configuration: enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="multi-link-mode" typ="enum (auto | disabled | master | all)" unset="1"></ArgTableRow>
<ArgTableRow arg="name-format" typ="string"></ArgTableRow>
<ArgTableRow arg="slave-name-format" typ="string"></ArgTableRow>
</ArgTable>
