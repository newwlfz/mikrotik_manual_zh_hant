---
sidebar_key: "cli-reference/ip/arp"
sidebar_position: 2
title: "arp"
sidebar_label: 'arp'
source: https://manual.mikrotik.com/docs/cli-reference/ip/arp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/arp {#iparp}
**型別：** 目錄

儘管 IP 封包使用 IP 地址進行定址，但主機之間的資料傳輸必須使用硬體地址。地址解析協定（ARP）用於將 OSI 第 3 層 IP 地址對映到 OSI 第 2 層 MAC 地址。路由器維護著一個當前使用的 ARP 條目表。通常該表是動態構建的，但為了增強網路安全性，可以透過新增靜態條目來部分或完全靜態構建該表。如需瞭解 ARP 的工作原理，請閱讀[網路基礎](../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together)。

:::info
預設的 ARP 條目最大數量取決於已安裝的記憶體容量。可使用命令 "`/ip/settings/set max-neighbor-entries=`x" 進行調整，更多詳細資訊請參閱 [IPv4 設定](./settings.md)。
:::

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該 ARP 條目是否已停用。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">該條目是否無效。</ArgTableRow>
<ArgTableRow arg="H" typ="dhcp">該 ARP 條目是否由 DHCP 伺服器新增。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">該條目是否動態建立。</ArgTableRow>
<ArgTableRow arg="P" typ="published">published</ArgTableRow>
<ArgTableRow arg="C" typ="complete">當 ARP `status` 為 permanent、reachable、stale、probe 或 delay 時，ARP 條目中會包含 Complete 標誌。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="ipAddr">要對映的 IP 地址。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">要對映到的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">分配該 IP 地址的介面名稱。</ArgTableRow>
<ArgTableRow arg="published" typ="bool">用於單個 IP 地址的靜態 proxy-arp 條目。當收到針對特定 IP 地址的 ARP 查詢時，裝置將用自己的 MAC 地址進行響應。無需在介面本身上設定 proxy-arp 即可代理所有 MAC 地址。僅當裝置存在通往目標的活動路由時，介面才會響應 ARP 請求。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">
顯示 ARP 條目狀態。
- `delay` - 鄰居條目驗證當前被延遲。
- `failed` - ARP 解析失敗。
- `incomplete` - 系統沒有該 IP 地址的 MAC 地址資訊。
- `permanent` - ARP 條目被視為永久條目，且不會被移除。
- `probe` - 正在探測鄰居。
- `reachable` - ARP 解析成功，MAC 地址已知。
- `stale` - 條目仍然有效，但已老化。
</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">指示此 ARP 條目與哪個 VRF 相關聯。</ArgTableRow>
</ArgTable>
