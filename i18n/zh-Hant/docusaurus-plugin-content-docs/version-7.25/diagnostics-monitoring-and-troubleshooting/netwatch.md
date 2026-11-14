---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/netwatch"
sidebar_position: 10
title: "網路監控"
sidebar_label: "網路監控"
description: "Netwatch 使用多種探測型別（包括 ICMP、TCP、HTTP、DNS 和簡單 ping）監控網路主機。它允許為狀態變化自定義指令碼，並支援 VRFs 和鏈路本地 IPv6 地址，且具有可配置的閾值和間隔設定。"
tags:
  - 'netwatch'
  - 'icmp'
  - 'scripting'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/netwatch
captured_at: '2026-11-04T11:15:33+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

[*Netwatch CLI 參考*](../cli-reference/tool/netwatch.md)

Netwatch 監控網路中主機的狀態。監控可以透過以下探測型別完成：
1) [**Simple**](#simple-probe) - 使用 ping，不使用高階指標
2) [**ICMP**](#icmp-probe) - 向指定 IP 地址的主機發送 ping，並可調整閾值
3) [**TCP-conn**](#tcp-conn-probe) - 測試 TCP 連線
4) [**HTTP-GET**](#http-get-probe) - 向正在監控的伺服器傳送請求
5) [**HTTPS-GET**](#https-get-probe) - 向正在監控的伺服器傳送請求
6) [**DNS**](#dns-probe) - 向 DNS 伺服器傳送 DNS 查詢並檢查響應。  

## 通用配置資訊 {#general-configuration-information}

本節介紹與所有 Netwatch 探測型別相關的資訊。

* 始終使用 Netwatch 的預設值——**即使使用者未定義它們**。可配置變數列表（含預設值）以及只讀/統計變數可在 [Netwatch CLI 參考頁面](../cli-reference/tool/netwatch.md) 檢視。請務必檢查預設變數是否適合您的使用場景。

* 對於所有探測型別，`host` 變數都是必填的，因為它定義了應被監控的裝置的地址。

* Netwatch 探測可以根據探測狀態變化執行指令碼，使 RouterOS 能夠動態調整路由器配置或傳送通知（*更多資訊，請參閱[指令碼編寫文件](../developer-guides/scripting/index.md)*）。Netwatch 支援三種指令碼型別，每種在不同條件下執行：

  * `up-script` 在狀態從 **Unknown**（*取決於 `ignore-initial-up` 變數；更多資訊請參閱 [CLI 參考](../cli-reference/tool/netwatch.md)*）或 **Down** 變為 **Up** 時執行；
  * `down-script` 在狀態從 **Unknown**（*取決於 `ignore-initial-down` 變數；更多資訊請參閱 [CLI 參考](../cli-reference/tool/netwatch.md)*）或 **Up** 變為 **Down** 時執行；
  * `test-script` 在每次探測測試期間執行。

* 如果沒有為探測指定指令碼，仍然可以在日誌中觀察探測狀態變化。當啟用 `info` 主題[日誌](./log/index.md)時，探測標識資訊和狀態變化會列印到日誌中。詳細的探測統計資訊和配置會列印到 `debug` 主題級別。

* 您可以檢視統計資訊並在指令碼編寫中使用這些變數。請記住，包含 "-" 的變數必須這樣書寫，例如，"done-tests" 應寫作 $"done-tests"

* Netwatch 以 *sys 使用者身份執行指令碼，因此 Netwatch 指令碼中定義的任何全域性變數都無法被例如[排程器](../system-information-and-utilities/scheduler.md)或其他使用者讀取。

* Netwatch 僅限於 *read,write,test,reboot* [指令碼策略](../developer-guides/scripting/index.md)。如果指令碼的所有者沒有足夠的許可權執行指令碼中的某個命令，則指令碼將不會被執行。如果指令碼具有超過 *read,write,test,reboot* 的策略，那麼指令碼也不會被執行。請確保您的指令碼不超過上述策略。

* 可以在 *`/system/scripts`* 選單下停用 RouterOS 指令碼的許可權檢查（[指令碼編寫文件](../developer-guides/scripting/index.md)）。當 Netwatch 沒有足夠許可權執行指令碼時這很有用，但這會降低整體安全性。建議改為為指令碼分配適當的許可權。

* Simple、ICMP、HTTP 和 TCP-connect 探測傳送時設定了 "don't fragment" 標誌。使用 ICMP 探測時，您可以設定 `packet-size`，它與 DF 標誌結合使用可幫助進行[路徑 MTU 發現](../hardware/mtu-in-routeros.md)。

:::warning
Netwatch 指令碼僅限於 `read`、`write`、`test` 和 `reboot` 策略。更多資訊請參閱[指令碼許可權](../developer-guides/scripting/index.md#script-permissions)。
:::

## Simple 探測 {#simple-probe}

定期傳送簡單的 ICMP ping 請求以檢查主機可用性。此探測型別僅適用通用探測引數。

### 配置示例 {#configuration-example}

Simple 探測配置，檢查 Google DNS 服務，並使用指令碼記錄探測狀態的變化。

```ros
/tool/netwatch/add host=8.8.8.8 up-script=":log info \"Ping to 8.8.8.8 successful\"" down-script=":log info \"Ping to 8.8.8.8 failed\""
```

在此示例中，配置了一個 simple 探測來檢查 8.8.8.8 是否可透過 ping 訪問。當探測狀態變化時，會根據狀態變化的型別建立日誌條目。

下面，您可以看到相同的配置示例在 [WinBox](../management-tools/winbox.md) 檢視中的顯示，而非 CLI。

![netwatch_01_simple_probe_example_winbox](/img/35c3e779718b3382.webp)

在日誌部分，您可以看到 Netwatch 執行了指令碼。下面的示例顯示了 `up-script` 的執行和 Netwatch 狀態變化。在這種情況下，必須啟用 `info` 主題的日誌記錄，這些日誌條目才會出現。

```ros
[admin@MikroTik] > /log/print where message~"8.8.8.8"
 2026-06-10 14:48:17 netwatch,info event up [ type: simple, host: 8.8.8.8 ]
 2026-06-10 14:48:17 script,info Ping to 8.8.8.8 successful
```

## ICMP 探測 {#icmp-probe}

`simple` 探測型別的更高階版本，同樣使用 ICMP 封包檢查主機狀態。與 `simple` 探測型別相比，`ICMP` 允許更復雜的閾值配置，並且可以傳送多個 ICMP ping 封包而不是僅一個。

### 配置示例 {#configuration-example-1}

此示例展示瞭如何使用 `ICMP` 探測閾值，此示例使用 `thr-avg` 閾值來監控到伺服器的平均往返時間。

```ros
/tool/netwatch/add host=8.8.8.8 type=icmp thr-avg=10ms up-script=":log info \"rtt average is \$\"rtt-avg\", threshold passed, ping to 8\
    .8.8.8 successful\"" down-script=":if (\$\"loss-percent\" < 85) do={ :log info \"rtt average i\
    s \$\"rtt-avg\", which is higher then threshold, please check connection\" } else={ :\
    log info \"Ping to 8.8.8.8 failed\"}"
```

該探測檢查 8.8.8.8 是否可透過 ping 訪問，並額外驗證 `rtt-avg` 值是否小於 10 ms。`up-script` 和 `down-script` 在執行時都會記錄 `rtt-avg` 值，除非 `down-script` 是由 85% 或更高的封包丟失觸發的。這樣可以區分由封包丟失引起的探測失敗和由配置閾值未滿足引起的失敗。

下面，您可以看到相同的配置示例在 [WinBox](../management-tools/winbox.md) 檢視中的顯示，而非 CLI。

![netwatch_02_ICMP_probe_example_winbox](/img/fc9860af2c64f65d.webp)

下面的示例顯示了 `up-script` 的執行和 Netwatch 狀態變化。如所示，平均 RTT 值以微秒為單位的原始值傳遞，因此在編寫 Netwatch 指令碼時請務必考慮到這一點。

```ros
 2026-06-17 10:31:01 netwatch,info event up [ type: icmp, host: 8.8.8.8 ]
 2026-06-17 10:31:01 script,info rtt average is 7686, threshold passed, ping to 8.8.8.8 successful
```

## TCP-conn 探測 {#tcp-conn-probe}

`tcp-conn` 探測型別檢查路由器能否與特定 TCP 埠上的主機建立 TCP 連線。這允許監控裝置上的特定服務，而不是透過 ICMP 監控裝置的總體可用性。

### 配置示例 {#configuration-example-2}

此示例使用 `tcp-conn` 探測型別檢查 8.8.8.8 的 DNS 埠是否正常執行。

```ros
/tool/netwatch/add host=8.8.8.8 type=tcp-conn port=53 up-script=":log info \"TCP handshake to 8.8.8.8:53 successful\"" down-script=":log info \"TCP handshake to 8.8.8.8:53 failed\""
```

`tcp-conn` 探測專門檢查 TCP 埠 53（DNS 埠）是否能夠與路由器完成 TCP 握手。

下面，您可以看到相同的配置示例在 [WinBox](../management-tools/winbox.md) 檢視中的顯示，而非 CLI。

![netwatch_03_TCP_probe_example_winbox](/img/79980d58ff16c187.webp)

## HTTP-GET 探測 {#http-get-probe}

`http-get` 探測向指定主機執行 HTTP-GET 請求，並驗證返回的 HTTP 狀態碼和響應時間。與 ICMP 或 TCP 探測不同，它驗證應用層可用性，確保 Web 服務確實在響應。當響應碼落在配置的 `http-codes` 範圍內且響應時間在配置的閾值內時，探測被視為成功。通常用於監控網站或 API 的可用性。

### 配置示例 {#configuration-example-3}

在此示例中，探測嘗試從 159.148.172.205 上的 mikrotik.com 獲取 HTTP 響應，並記錄響應碼。

 ```ros
 /tool/netwatch/add host=159.148.172.205 type=http-get down-script=":log info \"Probe down, response code: \$\"http-status-code\"\"" up-script=":log info \"Probe up, response code: \$\"http-status-code\"\""
 ```

下面，您可以看到相同的配置示例在 [WinBox](../management-tools/winbox.md) 檢視中的顯示，而非 CLI。

![netwatch_04_httpget_probe_example_winbox](/img/34194a20300b4f6c.webp)

在此日誌示例中，您可以看到探測變為 down，因為它未滿足 100-299 的狀態碼閾值，並收到了程式碼 302，因為 mikrotik.com 嘗試將探測重定向到 HTTPS。

```ros
 2026-06-19 14:09:26 netwatch,info event down [ type: http_get, host: 159.148.172.205 ]
 2026-06-19 14:09:26 script,info Probe down, response code: 302
```

## HTTPS-GET 探測 {#https-get-probe}

`https-get` 探測型別與 `http-get` 探測型別完全相同，唯一的區別是它使用 HTTPS 而不是 HTTP。例如，這允許探測執行額外的 [TLS/SSL 證書](../authentication-authorization-accounting/certificates.md)驗證檢查。

### 配置示例 {#configuration-example-4}

在此示例中，探測監控路由器自身的 `www-ssl` 服務。`www-ssl` 服務用於透過 [WebFig](../management-tools/webfig.md) 提供對路由器的 HTTPS 訪問。（[更多資訊](../system-information-and-utilities/services.md)）

```ros
 /tool/netwatch/add host=127.0.0.1 type=https-get down-script=":log info \"HTTPS WebFig is disabled\"" up-script=":log info \"HTTPS WebFig is enabled\""
```

該探測嘗試從路由器的本地地址（`127.0.0.1`）獲取 HTTPS 響應。為使此探測正常工作，請確保 `www-ssl` 服務配置了有效的 [TLS/SSL 證書](../authentication-authorization-accounting/certificates.md)。

下面，您可以看到相同的配置示例在 [WinBox](../management-tools/winbox.md) 檢視中的顯示，而非 CLI。

![netwatch_05_httpsget_probe_example_winbox](/img/1e6b20cef194e69a.webp)

## DNS 探測 {#dns-probe}

`dns` 探測型別檢查指定的域名能否由 DNS 伺服器解析。如果 DNS 伺服器為請求的域名返回有效記錄，則探測被視為 `Up`。

### 配置示例 {#configuration-example-5}

在此配置示例中，探測使用 Google 的公共 DNS 伺服器檢查 mikrotik.com 的 A 記錄。

```ros
 /tool/netwatch/add host=mikrotik.com type=dns dns-server=8.8.8.8 record-type=A down-script=":log info \"No A type record found\"" up-script=":log info \"A type record found: \$ip\""
```

如所示，`host` 設定為 `mikrotik.com`，`dns-server` 配置為 `8.8.8.8` 以覆蓋 [`/ip/dns`](../network-management/dns.md) 中配置的 DNS 伺服器，`record-type` 設定為 `A` 以查詢 IPv4 地址記錄。

下面，您可以看到相同的配置示例在 [WinBox](../management-tools/winbox.md) 檢視中的顯示，而非 CLI。

![netwatch_06_dns_probe_example_winbox](/img/65b91b0c127c4543.webp)

下面的示例顯示了 up-script 的執行和 Netwatch 狀態變化。

```ros
 2026-06-29 10:10:55 netwatch,info event up [ type: dns, host: mikrotik.com ]
 2026-06-29 10:10:55 script,info A type record found: 159.148.172.205
```
