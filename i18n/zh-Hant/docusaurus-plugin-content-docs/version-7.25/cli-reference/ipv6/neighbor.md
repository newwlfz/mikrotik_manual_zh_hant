---
sidebar_key: "cli-reference/ipv6/neighbor"
sidebar_position: 7
title: "neighbor"
sidebar_label: 'neighbor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ipv6/neighbor
captured_at: '2026-11-01T21:24:41+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/neighbor {#ipv6neighbor}
**型別：** 目錄

由 IPv6 [Neighbor Discovery](https://tools.ietf.org/html/rfc4861) 協定發現的所有節點，或透過配置手動新增的節點的列表。

預設的最大鄰居條目數取決於已安裝的 RAM。可透過 `/ipv6/settings/set max-neighbor-entries=x` 調整。詳情請參閱 [IPv6 設定](./settings.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="R" typ="router">router</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="ip6Addr">鄰居的 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">此鄰居所連線的介面名稱。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">要新增的裝置的 MAC 地址。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">
快取條目的狀態：
- **noarp** - 鄰居條目有效。RouterOS 不會驗證此條目，但其生存期到期時可將其刪除。
- **incomplete** - 地址解析正在進行，鄰居的鏈路層地址尚未確定。
- **reachable** - 鄰居最近（數十秒內）可達。
- **stale** - 鄰居不再被視為可達。在嘗試可達性驗證之前，將繼續向該鄰居傳送流量。
- **delay** - 鄰居不再被視為可達，且最近已向該鄰居傳送過流量。RouterOS 會短暫延遲探測，以便上層協定確認可達性。
- **probe** - 鄰居不再被視為可達，且正在傳送單播 Neighbor Solicitation 探測以驗證可達性。
- **failed** - RouterOS 無法使用 Neighbor Discovery 協定解析鄰居的 MAC 地址。
</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">指示與此鄰居條目關聯的 VRF。</ArgTableRow>
</ArgTable>
