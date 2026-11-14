---
sidebar_key: "cli-reference/system/ntp/server"
sidebar_position: 4
title: "server"
sidebar_label: 'server'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/ntp/server
captured_at: '2026-11-01T21:25:34+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ntp/server {#systemntpserver}
**型別：** 設定目錄

NTP 伺服器設定。伺服器會應答網路上 NTP 用戶端的時間查詢；它提供路由器自身所同步的時間。請參閱 [NTP](../../../system-information-and-utilities/ntp.md) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">啟用 NTP 伺服器。預設：no。</ArgTableRow>
<ArgTableRow arg="broadcast" typ="bool">定期將時間傳送到 `broadcast-addresses` 中的地址。預設：no。</ArgTableRow>
<ArgTableRow arg="multicast" typ="bool">以組播方式將時間分發到本地網路。預設：no。</ArgTableRow>
<ArgTableRow arg="manycast" typ="bool">參與 manycast 發現，在該發現過程中用戶端透過組播查詢找到伺服器。預設：no。</ArgTableRow>
<ArgTableRow arg="broadcast-addresses" typ="multi { broadcast-address: ipAddr
 }">當啟用 `broadcast` 時，用於傳送時間的廣播地址。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">伺服器執行所在的 VRF。預設：main。</ArgTableRow>
<ArgTableRow arg="use-local-clock" typ="bool">當沒有更好的時間源可用時，使用路由器的本地時鐘作為時間參考；此時守護程式會以 `local-clock-stratum` 提供並跟隨自己的時鐘。在此狀態下，用戶端的 `status` 會顯示 `using-local-clock`。路由器時鐘在沒有外部同步時會發生漂移，因此不要將其用於精確計時。預設：no。</ArgTableRow>
<ArgTableRow arg="local-clock-stratum" typ="num">啟用 `use-local-clock` 時，為本地時鐘通告的 Stratum。預設：5。</ArgTableRow>
<ArgTableRow arg="auth-key" typ="enum (none) { none:0 }">用於時間交換的對稱金鑰認證的金鑰，來自 [`/system/ntp/key`](./key.md)。預設：none（不進行認證）。</ArgTableRow>
</ArgTable>
