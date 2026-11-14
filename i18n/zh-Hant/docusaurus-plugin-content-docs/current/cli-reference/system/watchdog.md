---
sidebar_key: "cli-reference/system/watchdog"
sidebar_position: 37
title: "watchdog"
sidebar_label: 'watchdog'
source: https://manual.mikrotik.com/docs/cli-reference/system/watchdog
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/watchdog {#systemwatchdog}
**型別:** 設定目錄

當系統停止響應（軟體 watchdog 定時器）或某個 IP 地址停止響應 ping（ping watchdog）時重啟路由器，並在軟體故障後寫入支援輸出檔案。參見 [看門狗](../../diagnostics-monitoring-and-troubleshooting/watchdog.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="watch-address" typ="alt { ip: ipAddr
, ipv6: composite { address: ip6Addr
, interface: [ iface_enum]
 }
 }">ping 看門狗所 ping 的地址。路由器在 `ping-timeout` 時間內傳送六次 ping，當六次全部失敗時重啟。`none` 會關閉 ping 看門狗。請使用一個可靠線上、並能透過要監視的鏈路訪問到的地址，例如閘道器；對於 VPN，則使用遠端的隧道地址。如果該地址一直不可達，路由器會在每次啟動後再次重啟，大約每隔 `ping-start-after-boot` 加上 `ping-timeout` 的時間。預設值：none。</ArgTableRow>
<ArgTableRow arg="watchdog-timer" typ="bool">系統無響應達一分鐘時，路由器是否重啟。預設值：yes。</ArgTableRow>
<ArgTableRow arg="ping-start-after-boot" typ="time">啟動後到 ping 看門狗向 `watch-address` 傳送第一次 ping 之前的時間。在已執行超過該時間的路由器上，設定 `watch-address` 會立即開始傳送 ping。請將其設定得比被監視鏈路在啟動後建立連線所需的時間更長。較舊的匯出中稱其為 `no-ping-delay`。預設值：5m。</ArgTableRow>
<ArgTableRow arg="ping-timeout" typ="time">ping 看門狗向 `watch-address` 傳送六次 ping 所使用的時間，即每隔 `ping-timeout` 的六分之一發送一次。當六次全部失敗時，路由器會重啟。預設值：1m。</ArgTableRow>
<ArgTableRow arg="automatic-supout" typ="bool">軟體發生故障時，路由器是否寫入 `autosupout.rif`。先前的檔案會被重新命名為 `autosupout.old.rif`。ping 看門狗觸發的重啟不會寫入該檔案。預設值：yes。</ArgTableRow>
<ArgTableRow arg="auto-send-supout" typ="bool">路由器是否將自動支援輸出檔案透過電子郵件傳送到 `send-email-to`。預設值：no。</ArgTableRow>
<ArgTableRow arg="send-email-to" typ="string">當 `auto-send-supout=yes` 時，自動支援輸出檔案傳送到的電子郵件地址。</ArgTableRow>
<ArgTableRow arg="send-email-from" typ="string">包含自動支援輸出檔案的電子郵件的發件人地址。未設定時，使用 `/tool/e-mail` 中的值。</ArgTableRow>
<ArgTableRow arg="send-smtp-server" typ="alt { ipv4: ipAddr
, fqdn: string
 }">用於傳送包含自動支援輸出檔案的電子郵件的 SMTP 伺服器，可為 IPv4 地址或名稱。未設定時，使用 `/tool/e-mail` 中的值。</ArgTableRow>
</ArgTable>
