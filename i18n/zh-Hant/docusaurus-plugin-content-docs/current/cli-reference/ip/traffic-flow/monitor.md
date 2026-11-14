---
sidebar_key: "cli-reference/ip/traffic-flow/monitor"
sidebar_position: 2
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/cli-reference/ip/traffic-flow/monitor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/traffic-flow/monitor {#iptraffic-flowmonitor}
**型別：** 命令
顯示當前的 flow-cache 計數器（輸出即時更新；在 `duration` 之後停止）。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="finished-flows" typ="num">已過期並匯出的流數量</ArgTableRow>
<ArgTableRow arg="active-flows" typ="num">當前快取中的流數量</ArgTableRow>
<ArgTableRow arg="unmanaged-packets" typ="num">未能歸入任何被跟蹤流的報文</ArgTableRow>
<ArgTableRow arg="unmanaged-bytes" typ="num">未管理報文的位元組數</ArgTableRow>
</ArgTable>
