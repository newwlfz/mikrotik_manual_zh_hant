---
sidebar_key: "cli-reference/interface/detect-internet"
title: "detect-internet"
sidebar_label: 'detect-internet'
source: https://manual.mikrotik.com/docs/cli-reference/interface/detect-internet
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/detect-internet {#interfacedetect-internet}
**型別：** 設定目錄

Detect Internet 的設定。它會根據鏈路狀態、經過該介面的路由，以及 `cloud.mikrotik.com` 是否能透過該介面在 UDP 埠 30000 上應答，為 `detect-interface-list` 中的每個介面賦予一個狀態（見 [`state`](./state.md)），並把介面新增到此處設定的 LAN、WAN 和 internet 介面列表中。參見 [檢測網際網路](../../../diagnostics-monitoring-and-troubleshooting/detect-internet.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="detect-interface-list" typ="enum">Detect Internet 所監視的介面列表。`none` 會關閉 Detect Internet。預設值：none。</ArgTableRow>
<ArgTableRow arg="lan-interface-list" typ="enum">該介面列表會以動態成員的形式接收處於 `lan` 狀態的介面，並帶有註釋 `LAN detected`。預設值：none。</ArgTableRow>
<ArgTableRow arg="wan-interface-list" typ="enum">該介面列表會以動態成員的形式接收處於 `wan` 狀態的介面，並帶有註釋 `WAN detected`。預設值：none。</ArgTableRow>
<ArgTableRow arg="internet-interface-list" typ="enum">該介面列表會以動態成員的形式接收處於 `internet` 狀態的介面，並帶有註釋 `INTERNET detected`。預設值：none。</ArgTableRow>
<ArgTableRow arg="request-interval" typ="time">設定路由器檢查雲端的頻率：它會以此間隔的一半向 `cloud.mikrotik.com` 傳送 UDP 訊息，使用 `2m` 時約每分鐘一次。使用預設值時，處於 `internet` 狀態的介面在約 4 分鐘無應答後會回退為 `wan`。範圍：1m..1d。預設值：2m。</ArgTableRow>
</ArgTable>
