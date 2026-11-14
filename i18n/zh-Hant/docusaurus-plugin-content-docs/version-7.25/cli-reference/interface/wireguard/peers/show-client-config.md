---
sidebar_key: "cli-reference/interface/wireguard/peers/show-client-config"
sidebar_position: 1
title: "show-client-config"
sidebar_label: 'show-client-config'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/wireguard/peers/show-client-config
captured_at: '2026-11-01T21:23:18+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireguard/peers/show-client-config {#interfacewireguardpeersshow-client-config}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="file" typ="file">用於儲存用戶端配置的檔名。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="conf" typ="string">用戶端配置文字。</ArgTableRow>
<ArgTableRow arg="qr" typ="pic">根據用戶端配置生成的 QR 碼，便於在移動裝置上設定對端。</ArgTableRow>
</ArgTable>
