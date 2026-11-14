---
sidebar_key: "cli-reference/cmr/vlan"
sidebar_position: 7
title: "vlan"
sidebar_label: 'vlan'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/vlan
captured_at: '2026-11-09T11:35:47.715Z'
pagination_next: "cli-reference/cmr/wifi"
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/vlan {#cmrvlan}
**軟體包：** cmr
**型別：** Directory

`/cmr/vlan` 選單在選定的 CMR 用戶端上建立網橋和 VLAN 配置。每條規則透過 `labels` 選擇裝置，透過 `port-labels` 選擇埠（與裝置的介面名稱以及 `/cmr/device` 中分配的埠標籤進行匹配），列出 `vlan-ids`，併為每個埠分配一個 `role`。在選定的裝置上，該規則會建立一個名為 `cmr-bridge` 的專用網橋，啟用 VLAN 過濾，並將選定的埠移入其中。刪除規則會恢復之前的配置。請參閱 CMR 指南的 [VLAN 配置](../../management-tools/cmr.md#vlan-provisioning) 部分。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">VLAN 配置規則已停用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="labels" typ="object" unset="1">選擇此規則所配置的 CMR 用戶端。支援 + 和 - 符號分別作為 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。如果省略，則該規則適用於所有已連線的裝置。</ArgTableRow>
<ArgTableRow arg="port-labels" typ="object" unset="1" mandatory="1">按介面名稱（例如 `ether1`）或按在 `/cmr/device` 中分配給埠的埠標籤（例如 `uplink`）選擇要在所選裝置上配置的埠。該引數為必填項，因此規則始終會指明其配置的埠。</ArgTableRow>
<ArgTableRow arg="vlan-ids" typ="multi { vlan-range: range [1 .. 4094]
 }" mandatory="1">分配給所選埠的 VLAN ID，採用逗號分隔列表或範圍形式，例如 `100,200` 或 `100-200`。在 trunk 埠上，每個 VLAN ID 都會打上標籤；在 access 埠上，僅使用第一個 VLAN ID 作為該埠的 PVID。</ArgTableRow>
<ArgTableRow arg="role" typ="enum (access | trunk)" unset="1">
分配給所選埠的埠角色：
- `access`（預設）- 該埠屬於單個 VLAN，該 VLAN 被設定為該埠的 PVID，並承載未打標籤的幀
- `trunk` - 該埠承載多個 VLAN；幀會帶有 802.1Q 標頭標籤，以便對端能夠區分它們
</ArgTableRow>
</ArgTable>
