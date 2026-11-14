---
sidebar_key: "cli-reference/routing/id"
sidebar_position: 7
title: "id"
sidebar_label: "id"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/id
captured_at: '2026-11-01T21:29:33+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/id {#routingid}
**型別：** 目錄

全域性 Router ID 選舉配置。可以顯式配置 Router ID，或從路由器的某個 IP 地址中選舉產生。

對於每個 VRF 表，RouterOS 會新增一個動態 ID 例項，該例項從該 VRF 中的某個 IP 地址選舉 Router ID：

```text
[admin@rack1_b33_CCR1036] /routing/id> print
Flags: D - DYNAMIC, I - INACTIVE
Columns: NAME, DYNAMIC-ID, SELECT-DYNAMIC-ID, SELECT-FROM-VRF
#   NAME   DYNAMIC-ID      SELECT-D   SELE
0 D main   111.111.111.2   only-vrf   main

```

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">如果獲取有效 ID 時出現問題，則該項可能變為非活動狀態。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="id" typ="ipAddr" unset="1">要顯式設定的 Router ID。如果未設定 Router ID，RouterOS 可以從已配置的某個 IP 地址中選舉它。參見 `select-dynamic-id` 和 `select-from-vrf`。</ArgTableRow>
<ArgTableRow arg="select-dynamic-id" typ="ubit (any, only-static, only-loopback, only-vrf, only-active, lowest)" unset="1">
選擇 RouterOS 用於 Router ID 選舉的 IP 地址：
- `any` - 路由器上找到的任何地址都可以被選舉為 Router ID。
- `lowest` - 選擇最小的 IP 地址。
- `only-static` - 僅選擇靜態配置的地址。
- `only-active` - 僅從活動 IP 地址中選擇 ID。
- `only-loopback` - 僅從環回地址中選擇 ID（環回地址是任何非點對點 /32 地址）。
- `only-vrf` - 僅從選定的 VRF 中選擇 ID。與 `select-from-vrf` 配合使用。
</ArgTableRow>
<ArgTableRow arg="select-from-vrf" typ="enum" unset="1">用於為 ID 選舉選擇 IP 地址的 VRF。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="dynamic-id" typ="ipAddr">當前選定的 ID。</ArgTableRow>
</ArgTable>
