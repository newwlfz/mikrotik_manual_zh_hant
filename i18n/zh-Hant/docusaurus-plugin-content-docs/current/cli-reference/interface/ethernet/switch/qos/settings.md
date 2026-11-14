---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/settings"
sidebar_position: 6
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos/settings
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/settings {#interfaceethernetswitchqossettings}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="multicast-buffers" typ="num">用於組播流量的最大封包緩衝區數量（佔總緩衝區記憶體的百分比）。</ArgTableRow>
<ArgTableRow arg="mirror-buffers" typ="num" syscap="!prestera-cpss">用於[映象](../../../../../bridging-and-switching/marvell-prestera-switch-chip-features.md#mirroring)流量的最大封包緩衝區數量（佔總緩衝區記憶體的百分比）。</ArgTableRow>
<ArgTableRow arg="mirror-profile" typ="enum">要分配給[映象](./profile.md)封包的 [QoS 配置檔案](../../../../../bridging-and-switching/marvell-prestera-switch-chip-features.md#mirroring)名稱。</ArgTableRow>
<ArgTableRow arg="shared-buffers" typ="num">
埠之間共享的最大封包緩衝區數量（佔總緩衝區記憶體的百分比）。將其設定為 0 會停用緩衝區共享。剩餘的緩衝區記憶體會在埠之間分配。
使用 **Dynamic Buffers** 的新一代交換晶片會將所有緩衝區視為共享。交換晶片會根據當前擁塞程度自動調整埠和佇列緩衝區限制。使用 auto 值可以讓裝置利用 100% 的可用緩衝區記憶體，這是大多數場景的推薦設定。在延遲比避免丟包更重要的特定用例中，可以手動降低緩衝區限制。
</ArgTableRow>
<ArgTableRow arg="lossless-buffers" typ="num" syscap="!prestera-ac3">如果裝置支援多個共享緩衝池，此設定允許調整無損池的大小（佔共享緩衝區記憶體的百分比，其中 100% 表示由 `shared-buffers` 設定分配的所有共享緩衝區）。例如，如果 shared-buffers=50 且 lossless-buffers=80，無損池會獲得總緩衝區記憶體的 40%（50% 的 80%，即 "0.8 * 0.5 = 0.4"），而有損池會獲得剩餘的 10% 共享緩衝區。</ArgTableRow>
<ArgTableRow arg="lossless-traffic-class" typ="multi { array-id, tc: num [ .. 7]
 }" syscap="!prestera-ac3">無損流量類的列表。</ArgTableRow>
<ArgTableRow arg="wred-threshold" typ="enum (low | medium | high) { low:1, medium:2, high:3 }" syscap="!prestera-ac3">超過共享佇列上限（`queueX-shared-packet-cap` 或 `queueX-shared-byte-cap`）時發生隨機丟棄的封包相對數量。此閾值僅應用於啟用了[加權隨機早期檢測](../../../../../bridging-and-switching/quality-of-service.md#weighted-random-early-detection-wred)（`wred=yes`）且使用共享緩衝區（`use-shared-buffers=yes`）的佇列。佇列緩衝區填充水平越高，封包丟棄機率就越高。`low` 閾值表示隨機尾部丟棄開始得更晚；`high` 則開始得更早。</ArgTableRow>
</ArgTable>
