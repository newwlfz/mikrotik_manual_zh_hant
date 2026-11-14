---
sidebar_key: "cli-reference/tool/mac-scan"
sidebar_position: 11
title: "mac-scan"
sidebar_label: 'mac-scan'
source: https://manual.mikrotik.com/docs/cli-reference/tool/mac-scan
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/mac-scan {#toolmac-scan}
**條件：** !smips
**型別：** 命令

列出在介面上傳送 MikroTik Neighbor Discovery (MNDP) 通告的裝置及其 MAC 地址和 IPv4 地址，以便查詢用於 MAC Telnet 或 MAC WinBox 的 MAC 地址。無論裝置的 MAC 伺服器設定如何，裝置都會顯示；如果裝置在該介面上關閉了鄰居發現，則不會顯示。未指定 `duration` 時，掃描會一直執行，直到你停止它。有關示例，請參閱 [MAC 伺服器](../../management-tools/mac-server.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum">要掃描的介面，或使用 `all` 表示所有介面。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr">裝置的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">裝置在鄰居發現中通告的 IPv4 地址。</ArgTableRow>
<ArgTableRow arg="age" typ="num">自裝置上次鄰居發現通告以來的秒數。</ArgTableRow>
</ArgTable>
