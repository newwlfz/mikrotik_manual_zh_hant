---
sidebar_key: "cli-reference/ip/dns/static"
sidebar_position: 4
title: "static"
sidebar_label: 'static'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dns/static
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dns/static {#ipdnsstatic}
**型別：** 目錄

靜態 DNS 條目。路由器會自行應答針對這些名稱的查詢，而不會詢問上游伺服器，並且還會將其應用到來自上游的 CNAME 應答的目標上。對於具有靜態條目的名稱，針對其他記錄型別的查詢會發往上游伺服器，路由器會轉發該應答；當上遊伺服器沒有此類記錄時，路由器會以無記錄的 NOERROR 應答。對於給定的名稱和記錄型別，只建立一個匹配條目：當多個條目匹配時，列表順序並不決定由哪一個條目進行應答。有關示例，請參閱 [DNS](../../../network-management/dns.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">該條目由其他服務新增，而非由使用者新增。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">該條目已停用，路由器會忽略它。新建條目預設啟用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">條目的域名。路由器在匹配前會將查詢名稱轉換為小寫，因此匹配不區分大小寫。</ArgTableRow>
<ArgTableRow arg="regexp" typ="string">用於匹配查詢名稱的正則表示式，而不是 `name`。路由器會將其與小寫形式的名稱進行匹配，因此請使用小寫編寫該表示式：包含大寫字母的表示式永遠不會匹配。路由器不會為正則表示式條目建立 PTR 記錄。不要讓正則表示式與同一名稱的其他條目重疊：列表順序並不決定多個匹配條目中由哪一個進行應答。在命令列中，將反斜槓寫作 `\\`，將 `$` 寫作 `\$`；例如，`regexp="^host[0-9]+\\.example\\.com\$"` 會儲存為 `^host[0-9]+\.example\.com$`。使用 `print` 檢查儲存的值。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (NXDOMAIN | A | NS | CNAME | MX | TXT | AAAA | SRV | FWD) { NXDOMAIN:65281, A:1, NS:2, CNAME:5, MX:15, TXT:16, AAAA:28, SRV:33, FWD:65280 }">
條目的型別。
- `A`（預設）- `address` 中的 IPv4 地址。
- `AAAA` - `address` 中的 IPv6 地址。
- `CNAME` - `cname` 中名稱的別名。路由器會使用 CNAME 記錄以及目標的記錄進行應答，這些記錄來自靜態條目或上游。
- `FWD` - 將該名稱的查詢轉發到 `forward-to` 中的伺服器，而不是上游伺服器。
- `MX` - `mx-exchange` 中的郵件伺服器，使用 `mx-preference`。
- `NS` - `ns` 中的名稱伺服器。
- `NXDOMAIN` - 對每種記錄型別都應答 NXDOMAIN（名稱不存在）。
- `SRV` - `srv-target`、`srv-port`、`srv-priority` 和 `srv-weight` 中的服務位置。
- `TXT` - `text` 中的文字。
</ArgTableRow>
<ArgTableRow arg="forward-to" typ="alt { forwarder: enum
, ip: ipAddr
, ipv6: ip6Addr
, host: string
 }">路由器將 `FWD` 條目的查詢轉發到哪裡：伺服器的 IPv4 或 IPv6 地址或 DNS 名稱，或 [`/ip/dns/forwarders`](./forwarders.md) 中的轉發器名稱。沒有 `forward-to` 時，查詢會發往常規伺服器（`servers`、`dynamic-servers` 或 DoH 伺服器），並且該名稱不受 adlists 約束。當伺服器未在 `query-total-timeout` 內應答時，用戶端會收到 SERVFAIL 應答。</ArgTableRow>
<ArgTableRow arg="address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }">`A` 條目的 IPv4 地址，或 `AAAA` 條目的 IPv6 地址。對於具有 `name` 的條目，路由器還會應答該地址的反向（PTR）查詢。</ArgTableRow>
<ArgTableRow arg="mx-preference" typ="num">`MX` 條目郵件伺服器的優先順序；值越低越優先。</ArgTableRow>
<ArgTableRow arg="mx-exchange" typ="string">`MX` 條目郵件伺服器的主機名。</ArgTableRow>
<ArgTableRow arg="cname" typ="string">`CNAME` 條目的目標名稱。</ArgTableRow>
<ArgTableRow arg="text" typ="string">`TXT` 條目的文字。</ArgTableRow>
<ArgTableRow arg="ns" typ="string">`NS` 條目名稱伺服器的主機名。</ArgTableRow>
<ArgTableRow arg="srv-priority" typ="num">`SRV` 條目的優先順序；值越低越優先。</ArgTableRow>
<ArgTableRow arg="srv-weight" typ="num">`SRV` 條目在具有相同優先順序的條目中的權重。</ArgTableRow>
<ArgTableRow arg="srv-port" typ="num">`SRV` 條目服務的 TCP 或 UDP 埠。</ArgTableRow>
<ArgTableRow arg="srv-target" typ="string">提供 `SRV` 條目服務的主機名。</ArgTableRow>
<ArgTableRow arg="ttl" typ="time">此條目應答中的生存時間。 [`/ip/dns`](./index.md) 中的 `cache-max-ttl` 不會縮短它。預設值：1d。</ArgTableRow>
<ArgTableRow arg="match-subdomain" typ="bool">該條目是否也匹配 `name` 下的任意深度的所有名稱。使用 `yes` 時，`example.com` 的條目也會應答 `www.example.com` 和 `a.b.example.com`。預設值：no。</ArgTableRow>
<ArgTableRow arg="address-list" typ="string">路由器將應答中的地址新增到的防火牆地址列表，作為動態條目，註釋為 `created for <name>.`。對於 `FWD` 條目，這些是上游應答中的地址。當應答的 TTL 和 [`/ip/dns`](./index.md) 中的 `address-list-extra-time` 已過時，路由器會移除該條目。</ArgTableRow>
</ArgTable>
