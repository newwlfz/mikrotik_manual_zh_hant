---
sidebar_key: "cli-reference/system/ntp/client/servers"
sidebar_position: 2
title: "servers"
sidebar_label: 'servers'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/ntp/client/servers
captured_at: '2026-11-01T21:25:33+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ntp/client/servers {#systemntpclientservers}
**型別：** 目錄

用戶端的 NTP 伺服器。靜態條目在此處新增，或透過 [`/system/ntp/client`](./index.md) 中的 `servers` 新增；從 DHCP 學習到的條目（當 DHCP 用戶端設定了 `use-peer-ntp=yes` 時）為動態條目。請參閱 [NTP](../../../../system-information-and-utilities/ntp.md) 指南。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該條目已停用。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態條目，從 DHCP 學習得到。動態條目無法編輯。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="address (flags=46D)" mandatory="1">NTP 伺服器的 IP 地址或域名。IPv4 和 IPv6 地址可以帶有 `@vrf` 字尾，鏈路本地 IPv6 地址可以帶有 `%interface` 字尾。域名透過 `/ip/dns` 解析；結果顯示在 `resolved-address` 中。</ArgTableRow>
<ArgTableRow arg="min-poll" typ="num">向該伺服器查詢的最短間隔，以 2 的冪表示秒數（6 表示每 64 秒一次）。必須小於 `max-poll`。範圍：3..17。預設值：6。</ArgTableRow>
<ArgTableRow arg="max-poll" typ="num">向該伺服器查詢的最長間隔，以 2 的冪表示秒數（10 表示每 1024 秒一次）。範圍：3..17。預設值：10。</ArgTableRow>
<ArgTableRow arg="iburst" typ="bool">啟用後，用戶端會在新增伺服器後立即傳送一組間隔約一秒的查詢突發，以便快速獲得初始估算。預設值：yes。</ArgTableRow>
<ArgTableRow arg="auth-key" typ="enum (none) { none:0 }">來自 [`/system/ntp/key`](../key.md) 的金鑰，用於驗證該伺服器的回覆。未透過驗證的回覆會被拒絕（crypto NAK），用戶端不會進行同步。預設值：none。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="resolved-address" typ="address (flags=46)">`address` 中的域名所解析到的 IP 地址。</ArgTableRow>
</ArgTable>
