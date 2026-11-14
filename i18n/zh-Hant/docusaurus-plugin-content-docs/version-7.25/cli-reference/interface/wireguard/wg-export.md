---
sidebar_key: "cli-reference/interface/wireguard/wg-export"
sidebar_position: 2
title: "wg-export"
sidebar_label: 'wg-export'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/wireguard/wg-export
captured_at: '2026-11-01T21:23:20+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireguard/wg-export {#interfacewireguardwg-export}
**型別：** 命令

以標準 WireGuard 配置格式匯出所選 WireGuard 介面及其對等體。使用 `[find name=...]` 選擇介面。匯出內容不包括介面 IP 地址、路由或防火牆規則。如需可執行的 RouterOS 指令碼，請使用常規的 `/interface/wireguard/export` 命令。請參閱 [WireGuard](../../../virtual-private-networks/wireguard.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="file" typ="file">用於將所選 WireGuard 介面及其對等體匯出到的檔名。該檔案包含 `[Interface]` 和 `[Peer]` 部分以及私鑰；請妥善儲存。</ArgTableRow>
</ArgTable>
