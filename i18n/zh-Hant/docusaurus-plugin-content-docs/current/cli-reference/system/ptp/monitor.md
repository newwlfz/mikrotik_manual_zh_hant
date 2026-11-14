---
sidebar_key: "cli-reference/system/ptp/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/cli-reference/system/ptp/monitor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ptp/monitor {#systemptpmonitor}
**條件：** !smips
**系統能力：** ptp
**型別：** 命令
顯示 PTP 配置檔案例項的詳細狀態和同步精度，`monitor <number or name>`。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">PTP 配置檔案例項的名稱</ArgTableRow>
<ArgTableRow arg="clock-id" typ="string">本地時鐘的識別符號</ArgTableRow>
<ArgTableRow arg="priority1" typ="num">主時鐘選舉中本地的 priority1 值</ArgTableRow>
<ArgTableRow arg="priority2" typ="num">主時鐘選舉中本地的 priority2 值</ArgTableRow>
<ArgTableRow arg="i-am-gm" typ="bool">此裝置是否為主時鐘（grandmaster clock）</ArgTableRow>
<ArgTableRow arg="gm-clock-id" typ="string">主時鐘（grandmaster clock）的識別符號</ArgTableRow>
<ArgTableRow arg="gm-priority1" typ="num">主時鐘（grandmaster clock）的 priority1</ArgTableRow>
<ArgTableRow arg="gm-priority2" typ="num">主時鐘（grandmaster clock）的 priority2</ArgTableRow>
<ArgTableRow arg="master-clock-id" typ="string">PTP 路徑中主時鐘的識別符號（grandmaster clock 或 boundary clock）</ArgTableRow>
<ArgTableRow arg="slave-port" typ="iface_enum">連線到主時鐘的本地埠</ArgTableRow>
<ArgTableRow arg="freq-drift" typ="num">主時鐘與從時鐘之間的頻率漂移，單位為十億分之一</ArgTableRow>
<ArgTableRow arg="offset" typ="num">主時鐘與從時鐘之間的時間差，單位為納秒</ArgTableRow>
<ArgTableRow arg="slave-port-delay" typ="num">兩個時鐘之間封包測得的延遲，單位為納秒（線纜和收發器長度會影響結果）</ArgTableRow>
</ArgTable>
