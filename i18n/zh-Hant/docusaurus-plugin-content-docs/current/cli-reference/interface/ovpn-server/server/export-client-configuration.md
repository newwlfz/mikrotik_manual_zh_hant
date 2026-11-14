---
sidebar_key: "cli-reference/interface/ovpn-server/server/export-client-configuration"
sidebar_position: 1
title: "export-client-configuration"
sidebar_label: 'export-client-configuration'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ovpn-server/server/export-client-configuration
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ovpn-server/server/export-client-configuration {#interfaceovpn-serverserverexport-client-configuration}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="server" typ="enum">要從中匯出配置的 OVPN 伺服器名稱。</ArgTableRow>
<ArgTableRow arg="server-address" typ="string">用戶端用於連線此 VPN 伺服器的公共 IP 地址或 DNS 名稱。</ArgTableRow>
<ArgTableRow arg="ca-certificate" typ="file">用戶端 OVPN 配置使用的 CA 證書。</ArgTableRow>
<ArgTableRow arg="client-certificate" typ="file">用戶端 OVPN 配置使用的用戶端證書。</ArgTableRow>
<ArgTableRow arg="client-cert-key" typ="file">用戶端 OVPN 配置使用的用戶端私鑰。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="progress" typ="string">匯出進度狀態。</ArgTableRow>
</ArgTable>
