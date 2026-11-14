---
sidebar_key: "cli-reference/ip/ipsec/profile"
sidebar_position: 8
title: "profile"
sidebar_label: 'profile'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/ipsec/profile
captured_at: '2026-11-01T21:24:12+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/profile {#ipipsecprofile}
**型別：** 目錄

配置檔案定義了一組用於 Phase 1 期間 IKE 協商的引數。這些引數可與其他對等體配置共享。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">該項是否為預設項。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">配置檔名稱。</ArgTableRow>
<ArgTableRow arg="hash-algorithm" typ="enum (md5 | sha1 | sha256 | sha384 | sha512)">雜湊演算法。</ArgTableRow>
<ArgTableRow arg="prf-algorithm" typ="enum (auto | sha1 | sha256 | sha384 | sha512)">PRF 演算法（僅 IKEv2）。</ArgTableRow>
<ArgTableRow arg="enc-algorithm" typ="ubit (aes-256, aes-192, aes-128, 3des, des)">加密演算法。</ArgTableRow>
<ArgTableRow arg="dh-group" typ="ubit (x25519, ecp256, ecp384, ecp521, modp6144, modp4096, modp3072, modp2048, modp1536, modp1024, modp768)">Diffie-Hellman 組。</ArgTableRow>
<ArgTableRow arg="lifetime" typ="time">Phase 1 lifetime（僅 IKEv1）。</ArgTableRow>
<ArgTableRow arg="lifebytes" typ="num">Phase 1 lifetime（以位元組為單位，僅 IKEv1）。它僅作為管理值新增到提議中。用於遠端對等體需要特定 lifebytes 值才能建立 Phase 1 的情況。</ArgTableRow>
<ArgTableRow arg="proposal-check" typ="enum (obey | strict | claim | exact) { obey:1, strict:2, claim:3, exact:4 }">
Phase 2 lifetime 檢查邏輯：
- `claim` - 取提議的 lifetime 和配置的 lifetime 中較短者，並就此通知發起方。
- `exact` - 要求 lifetime 相同。
- `obey` - 接受發起方傳送的任何內容。
- `strict` - 如果提議的 lifetime 長於預設值，則拒絕該提議，否則接受提議的 lifetime。
</ArgTableRow>
<ArgTableRow arg="nat-traversal" typ="bool">使用 Linux NAT-T 機制解決 IPsec 對等體之間因 NAT 路由器而出現的 IPsec 不相容問題。此功能只能與 ESP 協定配合使用（按設計不支援 AH，因為 AH 會對完整封包（包括 IP 頭部）進行簽名，而 NAT 會更改 IP 頭部，從而使 AH 簽名無效）。該方法將 IPsec ESP 流量封裝到 UDP 流中，以克服一些導致 ESP 與 NAT 不相容的小問題。</ArgTableRow>
<ArgTableRow arg="ppk" typ="enum (no | psk | qkd | psk-ike-initial)">後量子預共享金鑰（僅 IKEv2）。</ArgTableRow>
<ArgTableRow arg="dpd-interval" typ="alt { special: enum (disable-dpd) { disable-dpd:0 }
, num: time [ .. 3600]
 }">對等體失效檢測間隔。</ArgTableRow>
<ArgTableRow arg="dpd-maximum-failures" typ="num">在對等體被視為失效之前允許的最大 DPD 失敗次數（僅 IKEv1）。</ArgTableRow>
</ArgTable>
