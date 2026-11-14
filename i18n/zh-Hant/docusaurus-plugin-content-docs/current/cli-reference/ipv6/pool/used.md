---
sidebar_key: "cli-reference/ipv6/pool/used"
sidebar_position: 1
title: "used"
sidebar_label: 'used'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/pool/used
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/pool/used {#ipv6poolused}
**型別：**目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="pool" typ="enum">為該字首預留地址的地址池名稱。</ArgTableRow>
<ArgTableRow arg="prefix" typ="ip6Prefix">從地址池中分配給用戶端的 IPv6 字首。</ArgTableRow>
<ArgTableRow arg="owner" typ="string">由什麼預留了該字首（"DHCP" 等）</ArgTableRow>
<ArgTableRow arg="info" typ="string">顯示從用戶端收到的 DUID 相關資訊（十六進位制值）。也可能包含十六進位制的原始時間戳。</ArgTableRow>
</ArgTable>
