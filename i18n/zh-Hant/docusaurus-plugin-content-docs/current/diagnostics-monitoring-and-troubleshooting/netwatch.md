---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/netwatch"
sidebar_position: 10
title: "網路監控"
sidebar_label: "網路監控"
description: "Netwatch 按可配置的間隔和閾值，使用 simple、ICMP、TCP、HTTP、HTTPS 或 DNS 探測來監控網路主機，並在主機上線或下線時執行指令碼。"
tags:
  - 'netwatch'
  - 'icmp'
  - 'scripting'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/netwatch
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Netwatch 監視網路上主機的狀態，並在主機狀態發生變化時執行指令碼。每個探測監視一臺主機，並具有一個狀態（在首次測試完成前為 `unknown`，之後為 `up` 或 `down`）、測試統計資訊以及自己的 `interval` 和超時。

有六種探測型別可用：

- **simple** - 每次測試一個 ICMP 回顯請求。這是舊版 RouterOS 中 Netwatch 的工作方式；其預設 `interval` 為 60s，而所有其他探測型別預設值為 10s。
- **icmp** - 每次測試一系列 ICMP 回顯請求（預設 10 個），並提供往返時間、抖動和丟包統計資訊以及可配置的失敗閾值。
- **tcp-conn** - 測試是否可以建立到某個埠的 TCP 連線。
- **http-get** - 請求一個頁面並檢查 HTTP 響應程式碼和響應時間。
- **https-get** - 類似於 `http-get`，但透過 HTTPS。
- **dns** - 傳送 DNS 查詢並檢查是否返回所請求的記錄。

每個探測都需要一個 `host`：IP 地址、DNS 名稱、帶 VRF 字尾的地址（`192.0.2.1@vrf1`），或帶介面的鏈路本地 IPv6 地址（`fe80::1%ether1`）。

## Simple 探測 {#simple-probe}

簡單探測會定期傳送一個 ICMP 回顯請求以檢查主機是否可達。僅適用通用探測引數。

Ping Google 的公共 DNS 解析器並記錄狀態變化：

```ros
/tool/netwatch/add host=8.8.8.8 \
    up-script=":log info \"Ping to 8.8.8.8 successful\"" \
    down-script=":log info \"Ping to 8.8.8.8 failed\""
```

首次測試在探測被新增或啟用後約 3 秒執行（預設 `start-delay`），狀態變化會被記錄（主題 `netwatch,info`），並執行匹配的指令碼：

```ros
[admin@MikroTik] > /log/print where message~"8.8.8.8"
 2026-10-09 09:57:10 netwatch,info event up [ type: simple, host: 8.8.8.8 ]
 2026-10-09 09:57:10 script,info Ping to 8.8.8.8 successful
```

在 WinBox 中的相同探測（**Tools > Netwatch**）：

![Simple Netwatch probe for 8.8.8.8 with up and down scripts in WinBox](/img/35c3e779718b3382.webp)

## ICMP 探測 {#icmp-probe}

`icmp` 探測型別每次測試會發送多個 ICMP 回顯請求，並根據 `thr-*` 閾值評估結果。它是 `simple` 探測的更高階版本：你可以觀察往返時間、抖動或丟包，而不是僅判斷可達性。

觀察發往 8.8.8.8 的平均往返時間，並在其超過 10 ms 時使探測失敗：

```ros
/tool/netwatch/add host=8.8.8.8 type=icmp thr-avg=10ms \
    up-script=":log info \"rtt average is \$\"rtt-avg\" us\"" \
    down-script=":log info \"8.8.8.8 down: \$\"loss-percent\"% loss\""
```

指令碼可以讀取探測的統計資料，例如 `rtt-avg` 和 `loss-percent`。往返值以微秒為單位傳遞給指令碼：

```ros
[admin@MikroTik] > /log/print where message~"8.8.8.8"
 2026-10-09 09:57:11 netwatch,info event up [ type: icmp, host: 8.8.8.8 ]
 2026-10-09 09:57:11 script,info rtt average is 9739 us
```

同一探測收集到的統計資料：

```ros
[admin@MikroTik] > /tool/netwatch/print stats
1  type=icmp host=8.8.8.8 status=up since=2026-10-09 09:57:11 done-tests=1
   failed-tests=0 sent-count=10 response-count=10 loss-count=0 loss-percent=0%
   rtt-min=9ms686us rtt-max=9ms935us rtt-avg=9ms739us rtt-jitter=249us
   rtt-stdev=121us
```

藉助 `thr-loss-count`，Netwatch 還可以在封包序列結束前報告判定結果：`early-failure-detection=yes` 會在丟包計數使失敗成為確定時立即報告 `down`，而 `early-success-detection=yes` 會在剩餘封包不再可能越過閾值時立即報告 `up`。沒有 `thr-loss-count` 時，只有序列中所有封包都統計完畢後才能知道結果，因此提前檢測選項主要與該閾值一起使用。

即使未設定任何閾值，閾值也有預設值（例如 `thr-avg=100ms`），因此一條緩慢但仍可工作的鏈路在使用普通 `type=icmp` 探測時也可能報告 `down`；請提高閾值，或檢查 `print stats` 以檢視是哪個閾值被觸發。

WinBox 中的同一探測：

![ICMP Netwatch probe with thr-avg threshold in WinBox](/img/fc9860af2c64f65d.webp)

## TCP-conn 探測 {#tcp-conn-probe}

`tcp-conn` 探測型別檢查路由器能否與特定埠上的主機建立 TCP 連線。用它來監控特定服務，而不是透過 ICMP 監控裝置的總體可用性。連線時間儲存在 `tcp-connect-time` 中，當握手耗時過長時，`thr-tcp-conn-time` 會使探測失敗。

檢查 8.8.8.8 的 DNS 服務是否在埠 53 上接受 TCP 連線：

```ros
/tool/netwatch/add host=8.8.8.8 type=tcp-conn port=53 \
    up-script=":log info \"TCP handshake to 8.8.8.8:53 successful\"" \
    down-script=":log info \"TCP handshake to 8.8.8.8:53 failed\""
```

```ros
[admin@MikroTik] > /log/print where message~"8.8.8.8"
 2026-10-09 09:57:10 netwatch,info event up [ type: tcp_conn, host: 8.8.8.8 ]
 2026-10-09 09:57:10 script,info TCP handshake to 8.8.8.8:53 successful
```

WinBox 中的同一探測：

![TCP Netwatch probe for port 53 in WinBox](/img/79980d58ff16c187.webp)

## HTTP-GET 探測 {#http-get-probe}

`http-get` 探測型別會向主機執行 HTTP GET 請求，並根據配置的 `http-codes` 範圍（預設 `100-299`）檢查返回的 HTTP 狀態碼。與 ICMP 或 TCP 探測不同，它會驗證應用層可用性：Web 服務必須作出應答，而不僅僅是接受連線。通常用於監控網站或 API 的可用性。響應程式碼儲存在 `http-status-code` 中，響應時間儲存在 `http-resp-time` 中；`thr-http-time` 會在響應緩慢時使探測失敗。

請求 mikrotik.com (159.148.172.205) 的首頁並記錄響應程式碼：

```ros
/tool/netwatch/add host=159.148.172.205 type=http-get \
    up-script=":log info \"Probe up, code \$\"http-status-code\"\"" \
    down-script=":log info \"Probe down, code \$\"http-status-code\"\""
```

探測會變為 down，因為 mikrotik.com 返回重定向 (302)，這超出了預設接受範圍 `100-299`。要同時接受重定向，請擴大範圍，例如 `http-codes=100-399`（像 `100-299,302` 這樣的範圍列表也可以）。日誌輸出：

```ros
[admin@MikroTik] > /log/print where message~"159.148.172.205"
 2026-10-09 09:59:01 netwatch,info event down [ type: http_get, host: 159.148.172.205 ]
 2026-10-09 09:59:01 script,info Probe down, code 302
```

WinBox 中的同一探測：

![HTTP-GET Netwatch probe in WinBox](/img/34194a20300b4f6c.webp)

## HTTPS-GET 探測 {#https-get-probe}

`https-get` 探測型別與 `http-get` 相同，但使用 HTTPS 而不是 HTTP，並增加了 `check-certificate` 和 `certificate` 引數，用於 [TLS 證書](../authentication-authorization-accounting/certificates.md) 驗證。

監控路由器自身的 `www-ssl` 服務，該服務透過 [WebFig](../management-tools/webfig.md) 提供 HTTPS 訪問：

```ros
/tool/netwatch/add host=127.0.0.1 type=https-get \
    up-script=":log info \"HTTPS WebFig is enabled\"" \
    down-script=":log info \"HTTPS WebFig is disabled\""
```

為使探測能夠變為 up，必須啟用 `www-ssl` 併為其配置證書；若使用普通的自簽名證書，請保留 `check-certificate=no`：

```ros
[admin@MikroTik] > /log/print where message~"WebFig"
 2026-10-09 09:57:10 netwatch,info event up [ type: https_get, host: 127.0.0.1 ]
 2026-10-09 09:57:10 script,info HTTPS WebFig is enabled
```

WinBox 中的同一探測：

![HTTPS-GET Netwatch probe for 127.0.0.1 in WinBox](/img/1e6b20cef194e69a.webp)

## DNS 探測 {#dns-probe}

`dns` 探測型別會解析 `host` 名稱，並檢查是否返回了所請求的 `record-type`（A、AAAA、MX 或 NS）。透過 `dns-server` 可以選擇要查詢的伺服器；否則將使用 [`/ip/dns`](../network-management/dns.md) 中配置的伺服器。結果儲存在只讀的 `ip`、`ip6`、`mail-servers` 和 `name-servers` 值中。

使用 Google 的公共 DNS 伺服器解析 mikrotik.com，並記錄該地址：

```ros
/tool/netwatch/add host=mikrotik.com type=dns \
    dns-server=8.8.8.8 record-type=A \
    up-script=":log info \"A type record found: \$ip\"" \
    down-script=":log info \"No A type record found\""
```

```ros
[admin@MikroTik] > /log/print where message~"record"
 2026-10-09 09:57:10 netwatch,info event up [ type: dns, host: mikrotik.com ]
 2026-10-09 09:57:10 script,info A type record found: 159.148.172.205
```

WinBox 中的同一探測：

![DNS Netwatch probe for mikrotik.com in WinBox](/img/65b91b0c127c4543.webp)

## 指令碼 {#scripts}

Netwatch 會在探測狀態變化時執行指令碼，因此 RouterOS 可以自動做出反應：切換到備用路由、重啟隧道、傳送[電子郵件](../system-information-and-utilities/e-mail.md)或寫入日誌條目（請參閱[指令碼編寫文件](../developer-guides/scripting/index.md)）：

- `up-script` 在狀態從 `down` 變為 `up`，或從 `unknown` 變為 `up` 時執行（除非 `ignore-initial-up=yes` 抑制首次轉換，例如在重啟之後）；
- `down-script` 在狀態從 `up` 變為 `down`，或從 `unknown` 變為 `down` 時執行（除非 `ignore-initial-down=yes`）；
- `test-script` 在每次探測測試後執行。

在指令碼內部，探測的值可作為變數使用，例如 `host`、`type`、`status`（已經是新狀態）和 `done-tests`。包含 `-` 的名稱必須用 `$"..."` 加引號，例如 `$"rtt-avg"`；往返時間值以微秒報告。

指令碼以內部 `*sys` 使用者在其自身環境中執行，與其他使用者、[scheduler](../system-information-and-utilities/scheduler.md) 及其他探測相互隔離：在 Netwatch 指令碼中設定的全域性變數在其他任何地方都不可見。

:::warning
Netwatch 指令碼僅限於 `read`、`write`、`test` 和 `reboot` 策略。更多資訊請參閱[指令碼許可權](../developer-guides/scripting/index.md#script-permissions)。
:::

如果仍要執行這樣的命令，請將其放入 `/system/script` 下具有自己的 `policy` 和 `dont-require-permissions=yes` 的指令碼中，並從 Netwatch 指令碼中用 `/system/script/run <name>` 呼叫它：這樣它就會使用該指令碼的策略而不是 Netwatch 的策略來執行。這會關閉該指令碼的許可權檢查，因此請保持指令碼簡短，並且只授予它所需的策略（參見 [dont-require-permissions](../developer-guides/scripting/scripting-tips-and-tricks.md#be-careful-when-using-dont-require-permissions)）。

狀態變化會以 `netwatch,info` 主題記錄日誌。帶有 `name` 的探測會記錄該名稱（`event up [ my-probe ]`），未命名的探測會記錄其型別和主機（`event up [ type: icmp, host: 198.51.100.1 ]`）。要獲取每個測試的詳細資訊，請新增一條使用 `netwatch,debug` 主題的日誌規則（參見 [日誌](./log/index.md)）。

## 檢查與故障排除 {#check-and-troubleshoot}

顯示探測狀態以及上次測試的統計資訊：

```ros
/tool/netwatch/print stats
```

`status` 顯示判定結果，`since` 顯示上次狀態變化的時間，`done-tests`/`failed-tests` 顯示歷史計數器。按型別的值僅涵蓋上次測試，例如 ICMP 的 `rtt-*` 或 HTTP-GET 的 `http-status-code`。

出現意外 `down` 狀態的常見原因：

- 在你檢視之前發生了短暫中斷：`since` 顯示上次狀態變化，`failed-tests` 統計失敗次數，`netwatch,info` 日誌儲存歷史記錄。
- ICMP 閾值：主機有響應，但 `rtt-avg` 或其他值越過某個 `thr-*` 閾值 - 將 `print stats` 與閾值進行比較。
- HTTP 探測：響應程式碼不在 `http-codes` 中（預設情況下重定向即為 down），或者響應比 `thr-http-time` 更慢。
- DNS 探測：NXDOMAIN 或無法訪問的 `dns-server` 即為 down；探測自身的 `timeout` 生效，不受 `/ip/dns` 超時影響。

## 技術細節 {#technical-details}

- 要讓探測不立即進行測試，請使用 `start-delay`（在新增和啟用時生效；預設 3s）和 `startup-delay`（重啟後生效；預設 5m）。
- 日誌行會用下劃線拼寫探測型別：`tcp-conn` 探測記錄 `type: tcp_conn`，`http-get` 探測記錄 `http_get`。
- 使用 `src-address` 時，探測會從特定的路由器地址發出；當該地址不再位於路由器上（例如 PPP 鏈路斷開）時，探測會報告 `down`，指令碼可利用這一點對可用上行鏈路作出反應，而不僅僅是對可訪問的主機作出反應。
- 當 ICMP 封包序列不適合探測的時間安排（`interval < (packet-count - 1) * packet-interval + timeout`）時，RouterOS 會記錄一條 "packet train not fitting in interval" 警告，並在內部延長所使用的間隔。
- Simple、ICMP、TCP-conn 和 HTTP/HTTPS-GET 探測在傳送時會設定 "don't fragment" 標誌。因此，增加 `packet-size` 的 `icmp` 探測只有在整條路徑都能承載該大小的封包時才會應答，這有助於解決[路徑 MTU 問題](../hardware/mtu-in-routeros.md)。

有關所有屬性、只讀值及其預設值，請參閱 CLI 參考中的 [`/tool/netwatch`](../cli-reference/tool/netwatch.md)。
