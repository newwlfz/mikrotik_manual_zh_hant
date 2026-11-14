---
sidebar_key: "cli-reference/interface/pptp-server/server"
sidebar_position: 2
title: "server"
sidebar_label: 'server'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/pptp-server/server
captured_at: '2026-11-01T21:22:59+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/pptp-server/server {#interfacepptp-serverserver}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">定義是否啟用 PPTP 伺服器。</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大傳輸單元。PPTP 介面在不發生封包分片的情況下能夠傳送的最大封包大小。</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">最大接收單元。PPTP 介面在不發生封包分片的情況下能夠接收的最大封包大小。</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">鏈路上能夠接收的最大封包大小。如果封包大於隧道 MTU，則會被拆分為多個數據包，從而允許透過隧道傳送完整的 IP 或乙太網封包。</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">伺服器接受的認證方式。</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">如果伺服器在保活週期內沒有收到任何封包，它將每秒傳送一次保活封包，共傳送五次。如果伺服器沒有收到用戶端的響應，連線將在 5 秒後斷開。</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">指定建立隧道時使用的 PPP 配置檔案。</ArgTableRow>
</ArgTable>
