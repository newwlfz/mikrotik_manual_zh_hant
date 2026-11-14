---
sidebar_key: "cli-reference/cmr/device/reboot"
sidebar_position: 4
title: "reboot"
sidebar_label: 'reboot'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/device/reboot
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/device/reboot {#cmrdevicereboot}
**包：** cmr
**型別：** 命令

重啟所選裝置。該命令會立即返回。當裝置重啟完成後，示例告警規則 `rebooted` 會記錄 `<device> rebooted`，其中 `<device>` 為 `identity@address`。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="labels" typ="object" unset="1">選擇要使用標籤重啟的裝置。分別支援用 + 和 - 符號作為 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。</ArgTableRow>
</ArgTable>
