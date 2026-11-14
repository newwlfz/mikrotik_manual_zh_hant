---
sidebar_key: "cli-reference/interface/sstp-server/server"
sidebar_position: 2
title: "server"
sidebar_label: 'server'
source: https://manual.mikrotik.com/docs/cli-reference/interface/sstp-server/server
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/sstp-server/server {#interfacesstp-serverserver}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">啟用或停用 SSTP 伺服器。</ArgTableRow>
<ArgTableRow arg="port" typ="num">SSTP 伺服器的監聽埠。</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">最大接收單元。</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">可在鏈路上接收的最大封包大小。如果封包大於隧道 MTU，則會拆分為多個數據包，從而允許透過隧道傳送完整大小的 IP 或 Ethernet 封包。</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">Keepalive 超時時間（秒）。</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">指定建立隧道時使用哪個 PPP 配置檔案配置。</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">允許的認證方法。預設情況下允許所有方法。</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }">證書儲存中的伺服器證書。</ArgTableRow>
<ArgTableRow arg="verify-client-certificate" typ="bool">根據路由器的證書儲存驗證用戶端證書。</ArgTableRow>
<ArgTableRow arg="pfs" typ="enum (no | yes | required) { no:0, yes:1, required:2 }">指定要使用哪種 TLS 認證。`yes` - TLS 使用 ECDHE-RSA 和 DHE-RSA。`required` - 僅使用 ECDHE。</ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }">指定允許使用哪個 TLS 版本。</ArgTableRow>
<ArgTableRow arg="ciphers" typ="ubit (aes256-sha, aes256-gcm-sha384)">允許的加密套件。</ArgTableRow>
</ArgTable>
