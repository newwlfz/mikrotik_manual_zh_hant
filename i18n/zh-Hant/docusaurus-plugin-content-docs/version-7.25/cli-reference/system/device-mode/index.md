---
sidebar_key: "cli-reference/system/device-mode/index"
sidebar_position: 1
title: "device-mode"
sidebar_label: 'device-mode'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/device-mode
captured_at: '2026-11-01T21:25:29+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/device-mode {#systemdevice-mode}
**型別：** 設定目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mode" typ="enum">當前裝置模式：basic、home、advanced 或 ros。</ArgTableRow>
<ArgTableRow arg="allowed-versions" typ="string">被視為安全的 RouterOS 版本列表。用於防止降級到易受攻擊的版本。</ArgTableRow>
<ArgTableRow arg="flagged" typ="bool">裝置是否處於 flagged 狀態。檢測到可疑配置時設定為 yes。</ArgTableRow>
<ArgTableRow arg="flagging-enabled" typ="bool">是否啟用針對可疑程式碼的配置分析。預設值：yes。</ArgTableRow>
<ArgTableRow arg="scheduler" typ="bool">是否允許使用 `/system/scheduler`。</ArgTableRow>
<ArgTableRow arg="socks" typ="bool">是否允許使用 `/ip/socks`。</ArgTableRow>
<ArgTableRow arg="fetch" typ="bool">是否允許使用 `/tool/fetch`。</ArgTableRow>
<ArgTableRow arg="pptp" typ="bool">是否允許使用 PPTP 用戶端和伺服器介面。</ArgTableRow>
<ArgTableRow arg="l2tp" typ="bool">是否允許使用 L2TP 用戶端和伺服器介面。</ArgTableRow>
<ArgTableRow arg="bandwidth-test" typ="bool">是否允許使用 `/tool/bandwidth-test` 和 `/tool/bandwidth-server`。</ArgTableRow>
<ArgTableRow arg="traffic-gen" typ="bool">是否允許使用 `/tool/traffic-generator`、`/tool/flood-ping` 和 `/tool/ping-speed`。</ArgTableRow>
<ArgTableRow arg="sniffer" typ="bool">是否允許使用 `/tool/sniffer`。</ArgTableRow>
<ArgTableRow arg="ipsec" typ="bool">是否允許使用 `/ip/ipsec`。</ArgTableRow>
<ArgTableRow arg="romon" typ="bool">是否允許使用 `/tool/romon`。</ArgTableRow>
<ArgTableRow arg="proxy" typ="bool">是否允許使用 `/ip/proxy`。</ArgTableRow>
<ArgTableRow arg="hotspot" typ="bool">是否允許使用 `/ip/hotspot`。</ArgTableRow>
<ArgTableRow arg="smb" typ="bool">是否允許使用 `/ip/smb`。</ArgTableRow>
<ArgTableRow arg="email" typ="bool">是否允許使用 `/tool/e-mail`。</ArgTableRow>
<ArgTableRow arg="zerotier" typ="bool">是否允許使用 `/zerotier`。</ArgTableRow>
<ArgTableRow arg="container" typ="bool">是否允許使用容器功能。</ArgTableRow>
<ArgTableRow arg="install-any-version" typ="bool">是否允許降級到 allowed-versions 列表之外的 RouterOS 版本。</ArgTableRow>
<ArgTableRow arg="partitions" typ="bool">是否允許更改分割區數量。</ArgTableRow>
<ArgTableRow arg="routerboard" typ="bool">是否允許使用 `/system/routerboard/settings`（auto-upgrade 除外），以及雙啟動裝置上的 SwOS/RouterOS 切換。</ArgTableRow>
<ArgTableRow arg="attempt-count" typ="num">失敗的 device-mode 更改嘗試次數。</ArgTableRow>
</ArgTable>
