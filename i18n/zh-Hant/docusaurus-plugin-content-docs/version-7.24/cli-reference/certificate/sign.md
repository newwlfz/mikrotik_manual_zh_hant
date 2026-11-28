---
title: "sign"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/certificate/sign
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## certificate/sign 
**類型：** 指令

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-crl-host" typ="multi { array-id, host: string
 }">adds CRL URL to created certificate</ArgTableRow>
<ArgTableRow arg="ca-on-smart-card" typ="bool">stores CA's private key on smart card</ArgTableRow>
<ArgTableRow arg="ca" typ="enum">issuer CA</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>
