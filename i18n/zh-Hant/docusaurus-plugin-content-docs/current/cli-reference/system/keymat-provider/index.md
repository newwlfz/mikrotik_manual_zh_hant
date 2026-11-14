---
sidebar_key: "cli-reference/system/keymat-provider"
title: "keymat-provider"
sidebar_label: 'keymat-provider'
source: https://manual.mikrotik.com/docs/cli-reference/system/keymat-provider
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/keymat-provider {#systemkeymat-provider}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (qkd | hkdf)"></ArgTableRow>
<ArgTableRow arg="key-size" typ="num">以位為單位</ArgTableRow>
<ArgTableRow arg="qkd-address" typ="string">KME 裝置地址</ArgTableRow>
<ArgTableRow arg="qkd-kme-id" typ="string">應與收到的 TLS 證書中的 KME ID 匹配</ArgTableRow>
<ArgTableRow arg="qkd-certificate" typ="enum (none)">這也會指定你的 SAE ID</ArgTableRow>
<ArgTableRow arg="qkd-peer-sae-id" typ="string">對端（主裝置或從裝置）SAE ID</ArgTableRow>
<ArgTableRow arg="qkd-cache-size" typ="num">要保留在快取中的未使用金鑰數量</ArgTableRow>
<ArgTableRow arg="hkdf-secret" typ="string"></ArgTableRow>
<ArgTableRow arg="hkdf-hash" typ="enum (sha256 | sha512)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="qkd-cache-state" typ="num">當前快取中未使用金鑰的數量</ArgTableRow>
<ArgTableRow arg="qkd-total-keys-received" typ="num">已接收金鑰的總數</ArgTableRow>
</ArgTable>
