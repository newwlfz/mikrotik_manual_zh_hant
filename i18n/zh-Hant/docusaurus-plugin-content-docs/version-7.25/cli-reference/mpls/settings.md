---
sidebar_key: "cli-reference/mpls/settings"
sidebar_position: 5
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/mpls/settings
captured_at: '2026-11-01T21:24:50+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/settings {#mplssettings}
**條件：** !smips
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="dynamic-label-range" typ="range">用於動態分配的標籤編號範圍。前 16 個標籤保留用於特殊用途（如 RFC 中所定義）。如果打算靜態配置標籤，請調整動態預設範圍，使其不包含將在靜態配置中使用的編號。</ArgTableRow>
<ArgTableRow arg="propagate-ttl" typ="enum (yes | no)">是否將 TTL 值從 IP 首部複製到 MPLS 首部。如果此選項設定為 **no**，則 MPLS 雲內部的跳數將對 traceroute 不可見。</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="enum (yes | no)">啟用/停用 MPLS fast-path 支援。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mpls-fast-path-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="mpls-fast-path-bytes" typ="num"></ArgTableRow>
</ArgTable>
