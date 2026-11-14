---
sidebar_key: "cli-reference/system/device-mode/update"
sidebar_position: 1
title: "update"
sidebar_label: 'update'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/device-mode/update
captured_at: '2026-11-01T21:25:28+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/device-mode/update {#systemdevice-modeupdate}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="mode" typ="enum">要應用的裝置模式：basic、home、advanced 或 ros。</ArgTableRow>
<ArgTableRow arg="flagged" typ="bool">設為 no 以退出 flagged 狀態。需要物理確認。</ArgTableRow>
<ArgTableRow arg="flagging-enabled" typ="bool">啟用或停用對可疑程式碼的配置分析。預設值：yes。</ArgTableRow>
<ArgTableRow arg="scheduler" typ="bool">允許或阻止 `/system/scheduler`。</ArgTableRow>
<ArgTableRow arg="socks" typ="bool">允許或阻止 `/ip/socks`。</ArgTableRow>
<ArgTableRow arg="fetch" typ="bool">允許或阻止 `/tool/fetch`。</ArgTableRow>
<ArgTableRow arg="pptp" typ="bool">允許或阻止 PPTP 用戶端和伺服器介面。</ArgTableRow>
<ArgTableRow arg="l2tp" typ="bool">允許或阻止 L2TP 用戶端和伺服器介面。</ArgTableRow>
<ArgTableRow arg="bandwidth-test" typ="bool">允許或阻止 `/tool/bandwidth-test` 和 `/tool/bandwidth-server`。</ArgTableRow>
<ArgTableRow arg="traffic-gen" typ="bool">允許或阻止 `/tool/traffic-generator`、`/tool/flood-ping` 和 `/tool/ping-speed`。</ArgTableRow>
<ArgTableRow arg="sniffer" typ="bool">允許或阻止 `/tool/sniffer`。</ArgTableRow>
<ArgTableRow arg="ipsec" typ="bool">允許或阻止 `/ip/ipsec`。</ArgTableRow>
<ArgTableRow arg="romon" typ="bool">允許或阻止 `/tool/romon`。</ArgTableRow>
<ArgTableRow arg="proxy" typ="bool">允許或阻止 `/ip/proxy`。</ArgTableRow>
<ArgTableRow arg="hotspot" typ="bool">允許或阻止 `/ip/hotspot`。</ArgTableRow>
<ArgTableRow arg="smb" typ="bool">允許或阻止 `/ip/smb`。</ArgTableRow>
<ArgTableRow arg="email" typ="bool">允許或阻止 `/tool/e-mail`。</ArgTableRow>
<ArgTableRow arg="zerotier" typ="bool">允許或阻止 `/zerotier`。</ArgTableRow>
<ArgTableRow arg="container" typ="bool">允許或阻止容器功能。</ArgTableRow>
<ArgTableRow arg="install-any-version" typ="bool">允許或阻止降級到 allowed-versions 列表之外的 RouterOS 版本。</ArgTableRow>
<ArgTableRow arg="partitions" typ="bool">允許或阻止更改分割區數量。</ArgTableRow>
<ArgTableRow arg="routerboard" typ="bool">允許或阻止 `/system/routerboard/settings`（auto-upgrade 除外）以及雙啟動裝置上的 SwOS/RouterOS 切換。</ArgTableRow>
<ArgTableRow arg="activation-timeout" typ="time">取消更新前等待物理確認（按下重設按鈕或斷電重啟）的時間。範圍：00:00:10 至 1d00:00:00。預設值：5m。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="update" typ="string">待處理 device-mode 更新的狀態訊息。提示使用者透過關機或按下按鈕進行確認。</ArgTableRow>
</ArgTable>
