---
sidebar_key: "cli-reference/system/device-mode"
title: "device-mode"
sidebar_label: 'device-mode'
source: https://manual.mikrotik.com/docs/cli-reference/system/device-mode
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/device-mode {#systemdevice-mode}
**型別：** 設定目錄

當前 device-mode 設定。模式和各項功能開關在啟動時生效，並且只能透過 [`update`](./update.md) 更改，更改需要物理確認。請參閱[裝置模式](../../../system-information-and-utilities/device-mode.md)指南。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mode" typ="enum">
當前裝置模式。
- `advanced` - 適用於 CCR 和 1100 系列裝置；以前稱為 `enterprise`。
- `basic` - 適用於大多數其他裝置。
- `home` - 適用於家用路由器。
- `rose` - 適用於 RDS 及類似具有大量磁碟使用的裝置。
</ArgTableRow>
<ArgTableRow arg="allowed-versions" typ="string">以逗號分隔的被視為安全的 RouterOS 版本列表，用於阻止降級到存在漏洞的版本（例如 `7.13+,6.49.8+`）。升級到附帶更新列表的版本會更新該列表；降級則不會。當啟用 `install-any-version` 時，此項被忽略。</ArgTableRow>
<ArgTableRow arg="flagged" typ="bool">裝置是否處於標記狀態：啟動配置分析發現了未經授權訪問的跡象，並停用了可疑配置。透過 `update flagged=no` 進行審查並清除。</ArgTableRow>
<ArgTableRow arg="flagging-enabled" typ="bool">是否在啟動時運行針對未經授權訪問跡象的配置分析。預設值：yes。</ArgTableRow>
<ArgTableRow arg="scheduler" typ="bool">是否允許 `/system/scheduler` 執行操作。</ArgTableRow>
<ArgTableRow arg="socks" typ="bool">是否允許 `/ip/socks` 中的 SOCKS 代理。</ArgTableRow>
<ArgTableRow arg="fetch" typ="bool">是否允許使用 `/tool/fetch`。</ArgTableRow>
<ArgTableRow arg="pptp" typ="bool">是否允許 `/interface/pptp-client` 和 `/interface/pptp-server`。</ArgTableRow>
<ArgTableRow arg="l2tp" typ="bool">是否允許 `/interface/l2tp-client` 和 `/interface/l2tp-server`。</ArgTableRow>
<ArgTableRow arg="bandwidth-test" typ="bool">是否允許使用 `/tool/bandwidth-test`、`/tool/bandwidth-server` 和 `/tool/speed-test`。</ArgTableRow>
<ArgTableRow arg="traffic-gen" typ="bool">是否允許使用 `/tool/traffic-generator`、`/tool/flood-ping` 和 `/tool/ping-speed`。</ArgTableRow>
<ArgTableRow arg="sniffer" typ="bool">是否允許使用 `/tool/sniffer`。</ArgTableRow>
<ArgTableRow arg="ipsec" typ="bool">是否允許使用 `/ip/ipsec`。</ArgTableRow>
<ArgTableRow arg="romon" typ="bool">是否允許使用 `/tool/romon`。</ArgTableRow>
<ArgTableRow arg="proxy" typ="bool">是否允許使用 `/ip/proxy` 中的 Web 代理。</ArgTableRow>
<ArgTableRow arg="hotspot" typ="bool">是否允許使用 `/ip/hotspot`。</ArgTableRow>
<ArgTableRow arg="smb" typ="bool">是否允許使用 `/ip/smb`。</ArgTableRow>
<ArgTableRow arg="email" typ="bool">是否允許使用 `/tool/e-mail`。</ArgTableRow>
<ArgTableRow arg="zerotier" typ="bool">是否允許使用 `/zerotier`。</ArgTableRow>
<ArgTableRow arg="container" typ="bool">是否允許使用容器功能（`/container`）。</ArgTableRow>
<ArgTableRow arg="install-any-version" typ="bool">是否允許安裝 `allowed-versions` 列表之外的 RouterOS 版本。</ArgTableRow>
<ArgTableRow arg="partitions" typ="bool">是否允許更改分割區數量（`/partitions`）。</ArgTableRow>
<ArgTableRow arg="routerboard" typ="bool">是否允許更改 `/system/routerboard/settings` 選項（自動升級除外）以及在雙啟動裝置上進行 SwOS/RouterOS 切換。</ArgTableRow>
<ArgTableRow arg="attempt-count" typ="num">自上次重設以來裝置模式更新失敗的嘗試次數；取消待處理更新的請求不計入其中。達到三次後，`update` 將被拒絕，並會開啟一個重設視窗，其時長由最後一次 `activation-timeout` 設定；在該視窗內按下按鈕或斷電重啟會重設計數器。已確認的更新也會重設計數器。預設值：0。</ArgTableRow>
</ArgTable>
