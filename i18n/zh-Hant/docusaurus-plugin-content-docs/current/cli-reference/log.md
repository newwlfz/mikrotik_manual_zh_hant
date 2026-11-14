---
sidebar_key: "cli-reference/log"
sidebar_position: 20
title: "log"
sidebar_label: 'log'
source: https://manual.mikrotik.com/docs/cli-reference/log
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## log {#log}
**型別：** 目錄

路由器儲存在記憶體中的日誌條目：預設的 `memory` 緩衝區、其他 memory 動作的緩衝區以及 disk 動作的最新條目。`/log/print` 會列出每個緩衝區的條目；`where buffer=<action name>` 將輸出限制為其中一個，`follow` 持續列印新條目，`follow-only` 僅列印新條目，`with-extra-info` 追加額外欄位，而 `file=<name>` 將輸出儲存到 `<name>.txt`。`/log/info`、`/log/warning`、`/log/error` 和 `/log/debug` 命令會新增一條帶有 `script` 主題和相應級別的訊息，與指令碼中的 `:log` 相同。保留哪些訊息由 [`/system/logging`](./system/logging/index.md) 中的規則設定。參見 [日誌](../diagnostics-monitoring-and-troubleshooting/log/index.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="buffer" typ="enum">條目所屬的緩衝區：預設緩衝區為 `memory`，也可以是另一個 memory 動作或某個 disk 動作的名稱。disk 動作的最新條目會顯示在這裡，重啟後則顯示其活動檔案的條目。不帶過濾器的 `/log/print` 會列出每個緩衝區，因此傳遞給多個動作的訊息會按動作各顯示一次。</ArgTableRow>
<ArgTableRow arg="time" typ="date">新增條目的日期和時間。</ArgTableRow>
<ArgTableRow arg="topics" typ="multi { array-id, topic: enum
 }">條目的主題，例如 `system,info,account`。 [`/system/logging`](./system/logging/index.md) 中的規則會根據這些主題選擇訊息。</ArgTableRow>
<ArgTableRow arg="message" typ="string">條目文字；當規則有 `prefix` 時，將其放在前面。</ArgTableRow>
<ArgTableRow arg="extra-info" typ="string">某些訊息攜帶的額外 `key=value` 欄位，例如一次登入：`app=ssh duser=admin outcome=success src=192.0.2.1`。 `print with-extra-info` 會將它們追加到訊息中，而 `cef` 遠端日誌格式會在 `msg=` 之後傳送它們。</ArgTableRow>
</ArgTable>
