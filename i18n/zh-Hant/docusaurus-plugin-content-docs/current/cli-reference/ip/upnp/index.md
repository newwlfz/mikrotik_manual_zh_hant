---
sidebar_key: "cli-reference/ip/upnp"
title: "upnp"
sidebar_label: 'upnp'
source: https://manual.mikrotik.com/docs/cli-reference/ip/upnp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/upnp {#ipupnp}
**型別：** 設定目錄

通用即插即用（UPnP）服務設定。該服務在每個[內部介面](./interfaces.md)的 UDP 埠 1900 上應答 SSDP 發現請求，並在 TCP 埠 2828 上處理控制連線。此選單中的任何更改都會重啟服務：所有動態埠對映都會被移除，用戶端必須重新請求它們。配置示例見 [UPnP 指南頁面](../../../firewall-and-quality-of-service/upnp.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">啟用 UPnP 服務。預設：no。</ArgTableRow>
<ArgTableRow arg="allow-disable-external-interface" typ="bool">允許內部介面上的 UPnP 用戶端透過 `ForceTermination` 動作停用路由器的外部介面，且無需任何身份驗證。UPnP 標準要求此動作可用；設定為 `no` 可防止本地用戶端斷開 Internet 連線。以這種方式停用外部介面還會移除其動態埠對映。預設：no。</ArgTableRow>
<ArgTableRow arg="show-dummy-rule" typ="bool">當用戶端列舉埠對映時，將一條非活動的佔位埠對映（埠 0、用戶端 0.0.0.0、描述 "Dummy inactive rule for windows to work"）作為第一條記錄報告。這是針對在不存在任何埠對映時行為異常的用戶端應用程式的變通方法。該佔位條目永遠不會出現在 `/ip/firewall/nat` 中。預設：yes。</ArgTableRow>
</ArgTable>
