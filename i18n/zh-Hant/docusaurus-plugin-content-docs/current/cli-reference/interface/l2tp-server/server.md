---
sidebar_key: "cli-reference/interface/l2tp-server/server"
sidebar_position: 2
title: "server"
sidebar_label: 'server'
source: https://manual.mikrotik.com/docs/cli-reference/interface/l2tp-server/server
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/l2tp-server/server {#interfacel2tp-serverserver}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">啟用或停用 L2TP 伺服器。</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大傳輸單元。L2TP 介面無需分片即可傳送的最大封包大小。</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">最大接收單元。L2TP 介面無需分片即可接收的最大封包大小。</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">鏈路上可接收的最大封包大小。如果封包大於隧道 MTU，它會被拆分為多個數據包，從而允許透過隧道傳送完整大小的 IP 或乙太網封包。</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">允許的認證方法。</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">保活超時時間（秒）。</ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num">最大併發 L2TP 會話數。</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">指定建立隧道時使用哪個 PPP 配置檔案。</ArgTableRow>
<ArgTableRow arg="use-ipsec" typ="enum (no | yes | required) { no:0, yes:1, required:2 }">是否使用 IPsec 加密。`required` 會強制所有用戶端使用 IPsec。</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string">IPsec 預共享金鑰。</ArgTableRow>
<ArgTableRow arg="caller-id-type" typ="enum (ip-address | number) { ip-address:0, number:1 }">向用戶端報告的呼叫方 ID 型別。</ArgTableRow>
<ArgTableRow arg="one-session-per-host" typ="bool">是否允許每個主機僅建立一個會話。</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">是否允許 FastPath 處理。</ArgTableRow>
<ArgTableRow arg="l2tpv3-circuit-id" typ="string">L2TPv3 電路識別符號。</ArgTableRow>
<ArgTableRow arg="l2tpv3-cookie-length" typ="enum (0 | 4-bytes | 8-bytes) { 0:0, 4-bytes:4, 8-bytes:8 }">L2TPv3 cookie 長度。</ArgTableRow>
<ArgTableRow arg="l2tpv3-digest-hash" typ="enum (none | md5 | sha1) { none:99, md5:0, sha1:1 }">L2TPv3 摘要雜湊演算法。</ArgTableRow>
<ArgTableRow arg="l2tpv3-ether-interface-list" typ="enum">L2TPv3 乙太網偽線端點的介面列表。</ArgTableRow>
<ArgTableRow arg="accept-pseudowire-type" typ="enum (all | ether | ppp) { all:0, ether:5, ppp:7 }">接受的偽線型別。</ArgTableRow>
<ArgTableRow arg="accept-proto-version" typ="enum (all | l2tpv2 | l2tpv3) { all:0, l2tpv2:2, l2tpv3:3 }">接受的 L2TP 協定版本。</ArgTableRow>
</ArgTable>
