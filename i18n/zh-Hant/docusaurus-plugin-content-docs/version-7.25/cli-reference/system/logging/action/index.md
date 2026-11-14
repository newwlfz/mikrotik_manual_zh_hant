---
sidebar_key: "cli-reference/system/logging/action/index"
sidebar_position: 2
title: "action"
sidebar_label: 'action'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/logging/action
captured_at: '2026-11-01T21:25:33+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/logging/action {#systemloggingaction}
**型別：** 目錄

這些操作會儲存或傳送由 [`/system/logging`](../index.md) 中的規則選中的訊息。預設操作包括 `memory`（`/log` 顯示的緩衝區）、`disk`（名為 `log` 的檔案）、`echo`（開啟的終端會話）和 `remote`（syslog 伺服器，未設定地址）。每個 memory 操作都保留自己的緩衝區，[`clear`](./clear.md) 會將其清空。參見 [日誌](../../../../diagnostics-monitoring-and-troubleshooting/log/index.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">預設操作之一：`memory`、`disk`、`echo` 和 `remote`。</ArgTableRow>
<ArgTableRow arg="Y" typ="managed"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">動作的名稱，僅限字母和數字。規則透過此名稱引用該動作；對於 `target=memory`，它也是 [`/log`](../../../log.md) 的 `buffer` 欄位中顯示的緩衝區名稱。</ArgTableRow>
<ArgTableRow arg="target" typ="enum (memory | disk | echo | remote | email | script) { memory:0, disk:1, echo:2, remote:3, email:4, script:5 }" mandatory="1">
訊息的去向：
- `memory` - 將它們儲存在以該操作命名的記憶體緩衝區中，由 `/log/print` 顯示。重啟後該緩衝區為空。
- `disk` - 將它們寫入文字檔案（`disk-file-name`）。
- `echo` - 將它們列印到開啟的終端會話（`remember`）。
- `remote` - 將它們傳送到 syslog 伺服器（`remote`）。
- `email` - 將每條訊息作為電子郵件傳送（`email-to`）。
- `script` - 為每條訊息執行指令碼（`script`）。
</ArgTableRow>
<ArgTableRow arg="memory-lines" typ="num">緩衝區保留的條目數，`1..65535`。緩衝區滿時，每條新條目都會丟棄最舊的條目，除非設定了 `memory-stop-on-full`。預設值：1000。</ArgTableRow>
<ArgTableRow arg="memory-stop-on-full" typ="bool">當為 `yes` 時，緩衝區會保留最初的 `memory-lines` 個條目，並丟棄新條目，直到使用 [`clear`](./clear.md) 將其清空。預設值：no。</ArgTableRow>
<ArgTableRow arg="disk-file-name" typ="string">日誌檔案的名稱，不含副檔名。該操作會寫入 `<name>.0.txt`；當該檔案滿時，它會變為 `<name>.1.txt`，並開始新的 `<name>.0.txt`。要寫入其他磁碟或資料夾，請將其名稱放在前面，例如 `usb1/log`。資料夾必須存在，否則該操作會被拒絕，並提示 `bad disk file name`。兩個 disk 操作不能使用相同的檔名。預設值：log。</ArgTableRow>
<ArgTableRow arg="disk-lines-per-file" typ="num">在操作開始新檔案之前，每個檔案中的行數，`1..65535`。預設值：1000。</ArgTableRow>
<ArgTableRow arg="disk-file-count" typ="num">該操作保留的檔案數，`1..65535`。當開始新檔案且達到該數量時，最舊的檔案及其條目會被丟棄。預設值：2。</ArgTableRow>
<ArgTableRow arg="disk-stop-on-full" typ="bool">當日志文件滿時停止寫入此操作，而不是丟棄最舊的條目。預設值：no。</ArgTableRow>
<ArgTableRow arg="remote" typ="alt { ipv6: ip6Addr
, ip: ipAddr
, hostname: string
 }">syslog 伺服器的地址：IPv4 或 IPv6 地址，或主機名。預設的 `remote` 操作使用 `0.0.0.0`（未設定伺服器）。預設值：0.0.0.0。</ArgTableRow>
<ArgTableRow arg="remote-port" typ="num">syslog 伺服器的埠。預設值：514。</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">傳送到 syslog 伺服器的封包的源地址。`0.0.0.0` 表示由路由器選擇。預設值：0.0.0.0。</ArgTableRow>
<ArgTableRow arg="remote-log-format" typ="enum (default | syslog | cef)">
傳送到 syslog 伺服器的訊息格式：
- `default`（預設） - 主題和訊息，`<topics> <message>`，不含時間或主機名。
- `syslog` - BSD syslog（RFC 3164）：`<PRI>`（設施和嚴重級別）、時間、路由器標識和訊息。`syslog-facility`、`syslog-severity`、`syslog-time-format` 和 `add-topics-string` 適用於它。
- `cef` - Common Event Format：時間和路由器標識，然後是 `CEF:0|MikroTik|<model>|<version>|`，包含主題、嚴重級別（`Low`、`Medium`、`High`）以及欄位 `dvchost`、`dvc` 和 `msg`，後面是訊息的額外欄位。每條訊息以 `cef-event-delimiter` 結尾。
</ArgTableRow>
<ArgTableRow arg="remote-protocol" typ="enum (udp | tcp | tls)">
到 syslog 伺服器的傳輸方式。每種格式都適用於每種傳輸方式，且傳送到相同地址和埠的操作共享一個連線。
- `udp`（預設） - 每條訊息一個數據報。伺服器不可達時傳送的訊息會丟失。
- `tcp` - 一個 TCP 連線。伺服器不可達時記錄的最多 1000 條訊息（所有 remote 操作合計）會儲存在記憶體中，並在連線恢復時傳送；緩衝區滿時，較新的訊息會被丟棄。`default` 和 `syslog` 訊息在流中沒有分隔符；請在 TCP 上使用 `cef`。
- `tls` - 與 `tcp` 相同，但使用 TLS 加密（`check-certificate`）。
</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="bool">對於 `remote-protocol=tls`：是否根據 [`/certificate`](../../../certificate/index.md) 中的受信任證書驗證伺服器證書。驗證失敗時，路由器不會發送，記錄日誌 `ssld,error client session, logging, remote IP: <address>, ssl: no trusted CA certificate found`，並稍後重試。證書中的名稱不會與伺服器地址進行比較，因此只應信任日誌伺服器的 CA。預設值：no。</ArgTableRow>
<ArgTableRow arg="cef-event-delimiter" typ="string">新增到每條 `cef` 訊息末尾的字元，在 UDP 上也是如此。預設值：`\r\n`。</ArgTableRow>
<ArgTableRow arg="syslog-time-format" typ="enum (bsd-syslog | iso8601)">
`syslog` 訊息的時間格式：
- `bsd-syslog`（預設） - `Oct  2 16:51:21`，路由器本地時間，不含年份。
- `iso8601` - `2026-10-02T16:51:21.726+03:00`，包含毫秒和時區偏移。
</ArgTableRow>
<ArgTableRow arg="syslog-facility" typ="enum (kern | user | mail | daemon | auth | syslog | lpr | news | uucp | cron | authpriv | ftp | ntp | local0 | local1 | local2 | local3 | local4 | local5 | local6 | local7) { kern:0, user:1, mail:2, daemon:3, auth:4, syslog:5, lpr:6, news:7, uucp:8, cron:9, authpriv:10, ftp:11, ntp:12, local0:16, local1:17, local2:18, local3:19, local4:20, local5:21, local6:22, local7:23 }">
`syslog` 訊息 `<PRI>` 中的 facility 及其程式碼：
- `kern` (0)
- `user` (1)
- `mail` (2)
- `daemon` (3)（預設）
- `auth` (4)
- `syslog` (5)
- `lpr` (6)
- `news` (7)
- `uucp` (8)
- `cron` (9)
- `authpriv` (10)
- `ftp` (11)
- `ntp` (12)
- 從 `local0` 到 `local7`（16 到 23）
</ArgTableRow>
<ArgTableRow arg="syslog-severity" typ="enum (auto | emergency | alert | critical | error | warning | notice | info | debug) { auto:0xffffffff, emergency:0, alert:1, critical:2, error:3, warning:4, notice:5, info:6, debug:7 }">
`syslog` 訊息 `<PRI>` 中的嚴重級別。除 `auto` 以外的值會以該嚴重級別傳送每條訊息。
- `auto`（預設） - 從訊息主題獲取嚴重級別：`debug` 7、`info` 6、`warning` 4、`error` 3。同時帶有 `error` 和 `critical` 的訊息取 3。
- `emergency`（0） - 系統不可用。
- `alert`（1） - 必須立即採取措施。
- `critical`（2） - 嚴重狀況。
- `error`（3） - 錯誤狀況。
- `warning`（4） - 警告狀況。
- `notice`（5） - 重要狀況。
- `info`（6） - 資訊性訊息。
- `debug`（7） - 偵錯訊息。
</ArgTableRow>
<ArgTableRow arg="email-to" typ="string">email 操作傳送到的地址。每條匹配的訊息都會作為單獨的電子郵件傳送，以 `<topics> <message>` 作為主題和正文，透過 [`/tool/e-mail`](../../../tool/e-mail/index.md) 中設定的 SMTP 伺服器、埠、TLS 模式和發件人傳送。參見 [電子郵件](../../../../system-information-and-utilities/e-mail.md)。</ArgTableRow>
<ArgTableRow arg="email-cc" typ="multi { array-id, cc: string
 }">email 操作的額外收件人，位於 CC 頭中。允許有多個地址。</ArgTableRow>
<ArgTableRow arg="email-start-tls" typ="bool">電子郵件動作不使用此項：STARTTLS 遵循 [`/tool/e-mail`](../../../tool/e-mail/index.md) 中的 `tls` 設定。預設值：no。</ArgTableRow>
<ArgTableRow arg="remember" typ="bool">對於 `target=echo`：保留沒有開啟終端會話時記錄的訊息，並在下次登入時列印一次。預設值：yes。</ArgTableRow>
<ArgTableRow arg="add-topics-string" typ="bool">對於 `remote-log-format=syslog`：將主題放在訊息前面，`<PRI><time> <identity> <topics> <message>`。`default` 格式始終包含主題。預設值：no。</ArgTableRow>
<ArgTableRow arg="script" typ="enum ()">對於 `target=script`：為每條匹配的訊息執行來自 [`/system/script`](../../script/index.md) 的指令碼。指令碼會獲得變數 `$topics`（以文字表示的主題，例如 `system,error,critical`）和 `$message`。指令碼仍在執行時匹配到的訊息會被跳過，指令碼自身記錄的訊息不會再次執行該指令碼。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum ()">remote 操作連線所使用的 VRF。預設值：main。</ArgTableRow>
</ArgTable>
