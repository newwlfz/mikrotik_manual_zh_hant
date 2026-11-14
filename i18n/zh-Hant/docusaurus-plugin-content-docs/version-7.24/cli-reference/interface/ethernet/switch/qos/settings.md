---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/settings"
sidebar_position: 6
title: "settings"
sidebar_label: "settings"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/qos/settings
captured_at: '2026-11-01T21:27:17+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/settings {#interfaceethernetswitchqossettings}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="multicast-buffers" typ="num">組播流量的封包緩衝區最大數量（佔總緩衝區記憶體的百分比）</ArgTableRow>
<ArgTableRow arg="mirror-buffers" typ="num" syscap="!prestera-cpss">映象流量的封包緩衝區最大數量（佔總緩衝區記憶體的百分比）</ArgTableRow>
<ArgTableRow arg="mirror-profile" typ="enum">應用於映象封包的 QoS 配置檔案</ArgTableRow>
<ArgTableRow arg="shared-buffers" typ="num">埠之間共享的封包緩衝區數量（佔總緩衝區記憶體的百分比）</ArgTableRow>
<ArgTableRow arg="lossless-buffers" typ="num" syscap="!prestera-ac3">無損共享池的大小（佔共享緩衝區的百分比）</ArgTableRow>
<ArgTableRow arg="lossless-traffic-class" typ="multi { array-id, tc: num [ .. 7]
 }" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="wred-threshold" typ="enum (low | medium | high) { low:1, medium:2, high:3 }" syscap="!prestera-ac3">開始隨機尾丟棄或 ECN 標記的相對佇列填充級別</ArgTableRow>
</ArgTable>
