---
sidebar_key: "cli-reference/ip/socks/access"
sidebar_position: 1
title: "access"
sidebar_label: 'access'
source: https://manual.mikrotik.com/docs/cli-reference/ip/socks/access
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/socks/access {#ipsocksaccess}
**型別：** 目錄

伺服器在撥號連線所請求的目標之前評估的訪問控制列表。規則按順序檢查，第一條匹配的規則決定結果。不匹配任何規則的請求會被允許，因此空列表允許所有請求，而限制性列表需要在末尾新增一條 `deny` 規則。更多資訊，請參閱 [SOCKS](../../../network-management/socks/index.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">disabled。該規則未被使用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="super { !
, alt-address: alt { range: ipRange
, src-ipv6: ip6Prefix
 }
 }">SOCKS 用戶端（請求方）的地址或子網。未設定時匹配任意。</ArgTableRow>
<ArgTableRow arg="src-port" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }">用戶端連線的源 TCP 埠。未設定時匹配任意。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, alt-address: alt { range: ipRange
, dst-ipv6: ip6Prefix
, dst-domain: string
 }
 }">用戶端請求的目標：IP 地址、範圍或域名。域名僅匹配按名稱請求目標的用戶端（SOCKS5 域名地址型別）。[`socksify`](../socksify.md) 用戶端始終按 IP 地址請求，因此域名規則不會匹配經 socksify 處理的流量。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }">請求的目標埠或範圍，例如 `21` 或 `1024-65535`。未設定時匹配任意。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (deny | allow) { deny:0, allow:1 }">
伺服器對匹配請求執行的操作。
- `allow` (預設) - 將連線轉發到目標。
- `deny` - 拒絕連線。
</ArgTableRow>
</ArgTable>
