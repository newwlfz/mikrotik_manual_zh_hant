---
sidebar_key: "cli-reference/interface/macsec/index"
sidebar_position: 1
title: "macsec"
sidebar_label: 'macsec'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/macsec
captured_at: '2026-11-01T21:22:51+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/macsec {#interfacemacsec}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬體解除安裝</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="cak" typ="string"></ArgTableRow>
<ArgTableRow arg="ckn" typ="string"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-untagged" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-untagged" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-too-long" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-no-tag" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-tag" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-unknown-sci" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-no-sci" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-overrun" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-sc-protected-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sc-protected-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sc-encrypted-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sc-encrypted-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-validated-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-decrypted-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-unchecked" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-delayed" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-ok" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-invalid" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-late" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-not-valid" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-not-using-sa" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-unused-sa" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-ok" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-invalid" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-not-valid" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-not-using-sa" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-unused-sa" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sa-protected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sa-encrypted" typ="multi { counter: num
 }"></ArgTableRow>
</ArgTable>
