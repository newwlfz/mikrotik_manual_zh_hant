---
sidebar_key: "cli-reference/routing/rpki/session"
sidebar_position: 3
title: "session"
sidebar_label: 'session'
source: https://manual.mikrotik.com/docs/cli-reference/routing/rpki/session
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/rpki/session {#routingrpkisession}
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (idle | connecting | prepare | loading | sync | error)"></ArgTableRow>
<ArgTableRow arg="version" typ="num">協商後的 RTR 協定版本。RouterOS 從版本 2 開始，當驗證器不支援版本 2 時回退到版本 1。ASPA 資料只能透過版本 2 獲取。該欄位在會話同步後顯示。</ArgTableRow>
<ArgTableRow arg="session" typ="num"></ArgTableRow>
<ArgTableRow arg="serial" typ="num"></ArgTableRow>
<ArgTableRow arg="expires" typ="time"></ArgTableRow>
</ArgTable>
