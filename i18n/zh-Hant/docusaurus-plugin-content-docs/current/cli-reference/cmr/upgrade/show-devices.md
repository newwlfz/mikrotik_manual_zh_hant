---
sidebar_key: "cli-reference/cmr/upgrade/show-devices"
sidebar_position: 2
title: "show-devices"
sidebar_label: 'show-devices'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/upgrade/show-devices
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/upgrade/show-devices {#cmrupgradeshow-devices}
**軟體包：** cmr
**型別：** Command

列出所選升級規則覆蓋的裝置。裝置由列表中第一條覆蓋它的規則認領，因此當較早的規則覆蓋了所有裝置時，某條規則可能不列出任何裝置。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="p" typ="remote-pending">控制器請求配對。</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">裝置處於非活動狀態。</ArgTableRow>
<ArgTableRow arg="S" typ="stale">無連線（陳舊）。</ArgTableRow>
<ArgTableRow arg="L" typ="controller">CMR 伺服器本身（自身用戶端）。</ArgTableRow>
<ArgTableRow arg="C" typ="connected">裝置已連線。</ArgTableRow>
<ArgTableRow arg="U" typ="upgrade-available">有可用的較新更新。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="only-upgradable" typ="bool">僅顯示實際可升級的裝置。</ArgTableRow>
</ArgTable>
