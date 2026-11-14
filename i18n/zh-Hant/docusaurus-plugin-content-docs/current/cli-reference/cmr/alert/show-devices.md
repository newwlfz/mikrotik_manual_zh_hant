---
sidebar_key: "cli-reference/cmr/alert/show-devices"
sidebar_position: 1
title: "show-devices"
sidebar_label: 'show-devices'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/alert/show-devices
captured_at: '2026-11-09T11:35:47.715Z'
pagination_prev: "cli-reference/cmr/alert"
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/alert/show-devices {#cmralertshow-devices}
**軟體包：** cmr
**型別：** 命令

列出狀態警報規則的狀態警報處於活動狀態的裝置，併為每個裝置提供狀態標誌（參見以下標誌）。事件警報從不保持活動狀態，因此它們不會列出任何裝置。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="p" typ="remote-pending">控制器請求配對。</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">裝置處於非活動狀態。</ArgTableRow>
<ArgTableRow arg="S" typ="stale">無連線（陳舊）。</ArgTableRow>
<ArgTableRow arg="L" typ="controller">CMR 伺服器本身（自身用戶端）。</ArgTableRow>
<ArgTableRow arg="C" typ="connected">裝置已連線。</ArgTableRow>
<ArgTableRow arg="U" typ="upgrade-available">有可用的較新更新。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="on-only" typ="bool">僅顯示告警規則處於活動狀態的裝置。</ArgTableRow>
</ArgTable>
