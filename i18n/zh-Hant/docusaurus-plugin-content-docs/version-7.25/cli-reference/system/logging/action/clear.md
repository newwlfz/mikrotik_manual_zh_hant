---
sidebar_key: "cli-reference/system/logging/action/clear"
sidebar_position: 1
title: "clear"
sidebar_label: 'clear'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/logging/action/clear
captured_at: '2026-11-01T21:25:32+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/logging/action/clear {#systemloggingactionclear}
**型別：** 命令

清空 memory 動作的緩衝區，例如對預設緩衝區執行 `/system/logging/action/clear action=memory`。具有 `memory-stop-on-full=yes` 的緩衝區在清空後會再次接受新條目。disk 動作會拒絕，並提示 `cleanup not supported on this target`。請參閱 [`/system/logging/action`](./index.md) 和 [日誌](../../../../diagnostics-monitoring-and-troubleshooting/log/index.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="action" typ="enum">要清空其緩衝區的 memory 動作的名稱。</ArgTableRow>
</ArgTable>
