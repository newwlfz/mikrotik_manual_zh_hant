---
sidebar_key: "cli-reference/routing/pimsm/instance"
sidebar_position: 3
title: "instance"
sidebar_label: 'instance'
source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/instance
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/pimsm/instance {#routingpimsminstance}
**條件：** !smips
**型別：** 目錄

instance 選單定義主要的 PIM-SM 設定。隨後，該例項用於所有其他與 PIM 相關的配置，例如 interface-template、靜態 RP 和 Bootstrap Router。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="vrf" typ="enum">用於控制連線的 VRF 名稱。</ArgTableRow>
<ArgTableRow arg="name" typ="string">例項的名稱。</ArgTableRow>
<ArgTableRow arg="afi" typ="enum (ip | ipv6)">指定 PIM 的地址族。</ArgTableRow>
<ArgTableRow arg="switch-to-spt" typ="bool">達到組播資料頻寬閾值時是否切換到最短路徑樹（SPT）。如果停用此選項，路由器將不會從協定階段一（註冊封裝）進入原生組播流量轉發。建議啟用此選項。</ArgTableRow>
<ArgTableRow arg="switch-to-spt-interval" typ="time">用於統計組播資料頻寬的時間間隔，與 `switch-to-spt-bytes` 配合使用，以確定是否達到切換閾值。</ArgTableRow>
<ArgTableRow arg="switch-to-spt-bytes" typ="num">組播資料頻寬閾值。如果在指定的時間間隔內達到此閾值，就會切換到最短路徑樹（SPT）。如果配置值為 0，則會立即切換。</ArgTableRow>
<ArgTableRow arg="crp-advertise-contained" typ="bool">當前未實現。</ArgTableRow>
<ArgTableRow arg="bsm-forward-back" typ="bool">當前未實現。</ArgTableRow>
<ArgTableRow arg="rp-hash-mask-length" typ="num">雜湊掩碼允許更改將多少個組對映到其中一個匹配的 RP。</ArgTableRow>
<ArgTableRow arg="rp-static-override" typ="bool">更改靜態 RP 的選擇優先順序。停用時，bootstrap RP 集具有更高的優先順序。啟用時，靜態 RP 具有更高的優先順序。</ArgTableRow>
<ArgTableRow arg="ssm-range" typ="address (flags=46/)">當前未實現。</ArgTableRow>
</ArgTable>
