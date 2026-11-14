---
sidebar_key: "cli-reference/system/note"
sidebar_position: 16
title: "note"
sidebar_label: 'note'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/note
captured_at: '2026-11-01T21:25:32+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/note {#systemnote}
**型別：** 設定目錄

路由器在登入時向管理員顯示的文字，例如路由器的用途、聯絡方式或警告資訊。示例請參閱 [備註](../../system-information-and-utilities/note.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="show-at-login" typ="bool">登入後顯示該備註：在 SSH 或 Telnet 等互動式命令列會話中，緊接在登入橫幅之後顯示，並在 WinBox 中顯示。透過 SSH 執行但沒有互動式會話的命令不會顯示它。預設值：yes。</ArgTableRow>
<ArgTableRow arg="show-at-cli-login" typ="bool">還會在 Telnet 登入提示符之前向任何連線的人顯示該備註，無需身份驗證；獨立於 `show-at-login`。SSH 不會在登入前顯示該備註，而 MAC Telnet 會在連線前要求提供憑據。預設值：no。</ArgTableRow>
<ArgTableRow arg="note" typ="string">備註的文字。`\n` 會開始新的一行；`/system/note/edit note` 會在內建編輯器中開啟該文字。位於檔案儲存根目錄中名為 `sys-note.txt` 的檔案會在下次啟動時替換該備註，然後路由器會刪除該檔案。預設值：empty。</ArgTableRow>
</ArgTable>
