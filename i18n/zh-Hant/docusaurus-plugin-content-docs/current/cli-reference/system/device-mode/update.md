---
sidebar_key: "cli-reference/system/device-mode/update"
sidebar_position: 1
title: "update"
sidebar_label: 'update'
source: https://manual.mikrotik.com/docs/cli-reference/system/device-mode/update
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/device-mode/update {#systemdevice-modeupdate}
**型別：** 命令

啟動裝置模式配置更改。該更改在按下按鈕或電源迴圈後生效並重啟裝置；如果在 `activation-timeout` 內未確認，則會取消。常規重啟也會取消該更改。不帶引數執行 `update` 會取消待處理的更新；當另一個更新待處理時，帶引數執行 `update` 會取消該待處理更新，且自身不會應用。請參閱[裝置模式](../../../system-information-and-utilities/device-mode.md)指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="mode" typ="enum">
要應用的裝置模式。指定 `mode` 會替換整個 device-mode 配置，但同一條命令中給出的其他引數除外；未指定的功能將採用新模式的預設值。
- `advanced` - 以前稱為 `enterprise`。
- `basic` - 適用於大多數其他裝置。
- `home` - 適用於家用路由器。
- `rose` - 適用於 RDS 及類似具有大量磁碟使用的裝置。
</ArgTableRow>
<ArgTableRow arg="flagged" typ="bool">設定為 `no` 可清除標記狀態，在此之前請檢查配置是否存在未經授權的更改。需要物理確認。</ArgTableRow>
<ArgTableRow arg="flagging-enabled" typ="bool">啟用或停用對配置中未經授權訪問跡象的分析。預設值：yes.</ArgTableRow>
<ArgTableRow arg="scheduler" typ="bool">允許或阻止 `/system/scheduler`。</ArgTableRow>
<ArgTableRow arg="socks" typ="bool">允許或阻止 `/ip/socks`。</ArgTableRow>
<ArgTableRow arg="fetch" typ="bool">允許或阻止 `/tool/fetch`。</ArgTableRow>
<ArgTableRow arg="pptp" typ="bool">允許或阻止 PPTP 用戶端和伺服器介面。</ArgTableRow>
<ArgTableRow arg="l2tp" typ="bool">允許或阻止 L2TP 用戶端和伺服器介面。</ArgTableRow>
<ArgTableRow arg="bandwidth-test" typ="bool">允許或阻止 `/tool/bandwidth-test`、`/tool/bandwidth-server` 和 `/tool/speed-test`。</ArgTableRow>
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
<ArgTableRow arg="activation-timeout" typ="time">在更新被取消之前，等待物理確認（按下按鈕或斷電重啟）的時長。當更新在三次不成功嘗試後被拒絕時，還會設定 `attempt-count` 重設視窗的長度。範圍：00:00:10 到 1d00:00:00。預設值：5m.</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="update" typ="string">待處理更新的狀態以及剩餘確認時間；無待處理更新時為空。</ArgTableRow>
</ArgTable>
