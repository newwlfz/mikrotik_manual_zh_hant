---
sidebar_key: "cli-reference/tool/netwatch"
sidebar_position: 13
title: "netwatch"
sidebar_label: "netwatch"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/netwatch
captured_at: '2026-11-01T21:30:18+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/netwatch {#toolnetwatch}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">Netwatch 探測的名稱。</ArgTableRow>
<ArgTableRow arg="host" typ="address (flags=46viD)" mandatory="1">要探測的伺服器的 IP 地址或域名。請參閱 [地址標誌](../index.md#address-flags)</ArgTableRow>
<ArgTableRow arg="type" typ="enum (simple | icmp | tcp-conn | http-get | https-get | dns)">
探測型別（預設值：**"simple"**）：
- simple - 簡化的 ICMP 探測，選項比 "ICMP" 型別少，用於向後相容舊版 Netwatch
- icmp - （ping 風格）帶統計資訊的一系列 ICMP 請求-響應
- tcp-conn - 測試到由 IP 和埠指定的伺服器的 TCP 連線（三次握手）
- http-get - 執行 HTTP Get 請求並測試響應是否在正確回覆範圍內
- https-get - 執行 HTTPS Get 請求並測試響應是否在正確回覆範圍內
- dns - 對域名執行指定的 DNS 查詢
</ArgTableRow>
<ArgTableRow arg="src-address" typ="address (flags=46)" unset="1">Netwatch 將嘗試用於訪問主機的源 IP 地址。如果該地址未在路由器上配置或已丟失，則主機會被視為 "down"。請參閱 [地址標誌](../index.md#address-flags)</ArgTableRow>
<ArgTableRow arg="interval" typ="time" unset="1">探測測試之間的時間間隔。（預設值：**10s**）</ArgTableRow>
<ArgTableRow arg="timeout" typ="time" unset="1">等待響應的最長時間限制。（預設值：**3s**）</ArgTableRow>
<ArgTableRow arg="start-delay" typ="time" unset="1">啟動探測前等待的時間。（預設值：**3s**）（在新增、啟用或系統啟動時，當 "startup-delay" 值小於 "start-delay" 值時）</ArgTableRow>
<ArgTableRow arg="startup-delay" typ="time" unset="1">系統啟動後等待多久開始 Netwatch 探測。（預設值：**5m**）</ArgTableRow>
<ArgTableRow arg="ignore-initial-up" typ="bool" unset="1">指定當探測狀態從 Unknown 變為 "Up" 時是否應執行 "Up" 指令碼，用於幫助避免啟用探測後或重啟後出現的誤報。"no" 表示從 "Unknown" 到 "Up" 的變化不會被忽略。（預設值：**no**）</ArgTableRow>
<ArgTableRow arg="ignore-initial-down" typ="bool" unset="1">指定當探測狀態從 Unknown 變為 "Down" 時是否應執行 "Down" 指令碼。"no" 表示從 "Unknown" 到 "Down" 的變化不會被忽略。（預設值：**no**）  **警告**：應謹慎使用，因為第一次 "Down" 狀態不會被執行，且只有當探測從 "Up" 變為 "Down" 狀態時才會執行 Down 指令碼。</ArgTableRow>
<ArgTableRow arg="up-script" typ="alt { script: string
 }" unset="1">當探測狀態從 "Down" 變為 "Up" 時執行的指令碼。</ArgTableRow>
<ArgTableRow arg="down-script" typ="alt { script: string
 }" unset="1">當探測狀態從 "Up" 變為 "Down" 時執行的指令碼。</ArgTableRow>
<ArgTableRow arg="test-script" typ="alt { script: string
 }" unset="1">在每次探測測試結束時執行的指令碼。</ArgTableRow>
<ArgTableRow arg="packet-interval" typ="time" unset="1">傳送 ICMP 請求封包之間的時間。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**50ms**）</ArgTableRow>
<ArgTableRow arg="packet-count" typ="num" unset="1">單次測試中要傳送的 ICMP 封包總數。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**10**）</ArgTableRow>
<ArgTableRow arg="packet-size" typ="num" unset="1">IP ICMP 封包的總大小。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**50**）</ArgTableRow>
<ArgTableRow arg="ttl" typ="num" unset="1">手動設定 ICMP 封包的生存時間值。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**255**）</ArgTableRow>
<ArgTableRow arg="accept-icmp-time-exceeded" typ="bool" unset="1">是否應將 ICMP "time exceeded" 訊息視為有效響應。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**no**）</ArgTableRow>
<ArgTableRow arg="early-success-detection" typ="bool" unset="1">如果已經知道主機將被視為 "Down"，Netwatch 不會等待所有封包處理完畢才更改探測狀態。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**no**）</ArgTableRow>
<ArgTableRow arg="early-failure-detection" typ="bool" unset="1">如果已經知道主機將被視為 "Down"，Netwatch 不會等待所有封包處理完畢才更改探測狀態。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**no**）</ArgTableRow>
<ArgTableRow arg="thr-max" typ="time" unset="1">rtt-max 的失敗閾值。（高於 thr-max 的值視為探測失敗）此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**1s**）</ArgTableRow>
<ArgTableRow arg="thr-avg" typ="time" unset="1">rtt-avg 的失敗閾值。（平均往返時間）此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**100ms**）</ArgTableRow>
<ArgTableRow arg="thr-stdev" typ="time" unset="1">rtt-stdev 的失敗閾值。（往返時間的標準差）此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**250ms**）</ArgTableRow>
<ArgTableRow arg="thr-jitter" typ="time" unset="1">rtt-jitter 的失敗閾值。（往返時間的抖動（= max - min））此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**1s**）</ArgTableRow>
<ArgTableRow arg="thr-loss-percent" typ="num" unset="1">loss-percent 的失敗閾值。（丟失封包的百分比）此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**85%**）</ArgTableRow>
<ArgTableRow arg="thr-loss-count" typ="num" unset="1">loss-count 的失敗閾值。（丟失的封包數量）此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。（預設值：**4294967295(max)**）</ArgTableRow>
<ArgTableRow arg="port" typ="num" unset="1">TCP 埠。此引數特定於 [**TCP-conn**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#tcp-conn-probe) 和 [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#http-get-probe) 探測型別。（預設值：**80**（TCP-conn、HTTP-GET）和  **443**（HTTPS-GET））</ArgTableRow>
<ArgTableRow arg="thr-tcp-conn-time" typ="time" unset="1">tcp-connect-time 的失敗閾值，配置使用微秒；如果未指定時間單位（s/m/h），日誌和狀態頁面會以毫秒顯示相同的值。此引數特定於 [**TCP-conn**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#tcp-conn-probe) 探測型別。（預設值：**1s**）</ArgTableRow>
<ArgTableRow arg="thr-http-time" typ="time" unset="1">http-resp-time 的失敗閾值。此引數特定於 [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#http-get-probe) 探測型別。（預設值：**10s**）</ArgTableRow>
<ArgTableRow arg="http-codes" typ="multi { http-response-range: range [100 .. 599]
 }" unset="1">可作為探測 "Up" 狀態接受的 HTTP 響應狀態碼範圍。請參閱 [mozilla-http-status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) 或 [RFC7231](https://datatracker.ietf.org/doc/html/rfc7231#section-6)。此引數特定於 [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#http-get-probe) 探測型別。（預設值：**100-299**）</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }" unset="1">用於主機驗證的來自本地儲存的證書。此引數特定於 [**HTTPS-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#https-get-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="bool" unset="1">啟用來自本地證書儲存的信任鏈驗證。此引數特定於 [**HTTPS-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#https-get-probe) 探測型別。（預設值：**no**）</ArgTableRow>
<ArgTableRow arg="record-type" typ="enum (A | AAAA | MX | NS)" unset="1">將用於 DNS 探測的記錄型別。此引數特定於 [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#dns-probe) 探測型別。（預設值：**A**）</ArgTableRow>
<ArgTableRow arg="dns-server" typ="address (flags=46)" unset="1">探測應向其傳送請求的 DNS 伺服器；如果未指定，將使用 `/ip/dns` 中的值。此引數特定於 [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#dns-probe) 探測型別。請參閱 [地址標誌](../index.md#address-flags)</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="enum (unknown | down | up)" unset="1">探測的當前狀態。</ArgTableRow>
<ArgTableRow arg="since" typ="date">上次狀態變化發生的時間。</ArgTableRow>
<ArgTableRow arg="done-tests" typ="num">已完成探測測試的總數。</ArgTableRow>
<ArgTableRow arg="failed-tests" typ="num">失敗探測測試的總數。</ArgTableRow>
<ArgTableRow arg="sent-count" typ="num">上次探測測試期間傳送的 ICMP 封包數量。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="response-count" typ="num">上次探測測試期間收到的 ICMP 響應封包數量。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="loss-count" typ="num">上次探測測試期間丟失的 ICMP 響應封包數量。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="loss-percent" typ="num">上次探測測試期間丟失的 ICMP 響應封包百分比。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="rtt-avg" typ="time">往返時間的平均值。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="rtt-min" typ="time">最小往返時間。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="rtt-max" typ="time">最大往返時間。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="rtt-jitter" typ="time">往返時間的抖動（= max - min）。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="rtt-stdev" typ="time">往返時間的標準差。此引數特定於 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#icmp-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="tcp-connect-time" typ="time">建立 TCP 連線所花費的時間。此引數特定於 [**TCP-conn**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#tcp-conn-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="http-status-code" typ="num">HTTP 響應狀態碼（200 OK、404 Not Found 等）。請參閱 [mozilla-http-status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) 或 [RFC7231](https://datatracker.ietf.org/doc/html/rfc7231#section-6)。此引數特定於 [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#http-get-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="http-resp-time" typ="time">HTTP/S 伺服器在收到請求後傳送響應所花費的時間，通常以毫秒為單位。此引數特定於 [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#http-get-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="ip" typ="ipAddr">IPv4 IP 地址 - A 記錄型別探測的結果。此引數特定於 [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#dns-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="ip6" typ="ip6Addr">IPv6 IP 地址 - AAAA 記錄型別探測的結果。此引數特定於 [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#dns-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="name-servers" typ="multi { array-id, name-servers: string
 }">名稱伺服器 - NS 記錄型別探測的結果。此引數特定於 [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#dns-probe) 探測型別。</ArgTableRow>
<ArgTableRow arg="mail-servers" typ="multi { array-id, mail-servers: string
 }">郵件伺服器及其優先順序 - MX 記錄型別探測的結果。此引數特定於 [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch.md#dns-probe) 探測型別。</ArgTableRow>
</ArgTable>
