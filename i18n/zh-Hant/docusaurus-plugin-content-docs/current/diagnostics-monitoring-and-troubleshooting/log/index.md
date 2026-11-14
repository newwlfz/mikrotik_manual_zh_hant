---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/log"
title: "日誌"
sidebar_label: "日誌"
description: "RouterOS 在主題中記錄系統事件；/system/logging 中的規則會將這些事件傳送到記憶體、磁碟、控制檯、syslog 伺服器（UDP、TCP 或 TLS；syslog 或 CEF 格式）、電子郵件或指令碼。使用 /log/print 讀取日誌。"
tags:
  - 'logging'
  - 'syslog'
  - 'system-management'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/log
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 會把事件寫入系統日誌：登入和登入失敗、配置更改以及更改者、介面 up 和 down、DHCP 租約、協定狀態變化和錯誤。每條條目都有時間、一個或多個主題（說明它來自哪裡以及有多重要，例如 `dhcp,info` 或 `system,error,critical`）和一條訊息。

兩個選單決定保留什麼以及傳送到哪裡：

- `/system/logging` 中的規則按主題選擇條目，並將它們傳遞給動作。
- `/system/logging/action` 中的動作將條目儲存在記憶體或磁碟上的檔案中，列印到控制檯，傳送到 syslog 伺服器或透過電子郵件傳送，或執行指令碼。

預設配置有四條規則：

| 主題 | 動作 | 結果 |
| :-- | :-- | :-- |
| `info` | `memory` | 儲存在 RAM 中。 |
| `error` | `memory` | 儲存在 RAM 中。 |
| `warning` | `memory` | 儲存在 RAM 中。 |
| `critical` | `echo` | 列印到已開啟的終端；當沒有終端開啟時，在下次登入時列印。 |

`memory` 動作保留最新的 1000 條條目，路由器重啟時這些條目會丟失。預設不記錄偵錯訊息。要在重啟後保留日誌，請記錄到磁碟或 syslog 伺服器。

如需影片介紹，請參見 [日誌記錄基礎](https://www.youtube.com/watch?v=E-QAhaWtsnU)。

## 讀取日誌 {#read-the-log}

`/log/print` 顯示記憶體中保留的條目，最舊的在前。用 `where` 過濾它們：`topics~` 針對主題匹配模式，`message~` 針對訊息文字匹配。

```ros
[admin@MikroTik] > /log/print where topics~"interface|dhcp"
 2026-10-02 17:34:34 interface,info lo link up
 2026-10-02 17:34:42 interface,info ether2 link up (speed 1G, full duplex)
 2026-10-02 17:34:47 dhcp,info bridge on bridge got IP address 192.168.88.36
```

要即時檢視新到達的條目，請新增 `follow`（先列印現有條目）或 `follow-only`（僅新條目）。按 <kbd>Space</kbd> 列印分隔線，按 <kbd>Control</kbd>+<kbd>C</kbd> 停止。例如，要監視失敗的登入：

```ros
[admin@MikroTik] > /log/print follow-only where topics~"critical"
 = = =   = = =   = = =      = = =   = = =   = = =      = = =   = = =   = = =
2026-10-02 17:35:45 system,error,critical login failure for user admin from 192.168.88.17 via ssh
2026-10-02 17:35:45 system,error,critical login failure for user root from 192.168.88.17 via ssh
-- Ctrl-C to quit. Space prints separator. New entries will appear at bottom.
```

登入和防火牆條目帶有額外欄位，例如使用者、服務和源地址。`with-extra-info` 會將它們新增到該行：

```ros
[admin@MikroTik] > /log/print with-extra-info where message~"login failure"
 2026-10-02 17:35:45 system,error,critical login failure for user admin from 192.168.88.17 via ssh app=ssh duser=admin outcome=failure src=192.168.88.17
 2026-10-02 17:35:45 system,error,critical login failure for user root from 192.168.88.17 via ssh app=ssh duser=root outcome=failure src=192.168.88.17
```

`/log/print` 還會列出其他 memory 動作的緩衝區以及 disk 動作的最新條目，因此一個由多個動作儲存的條目會按動作分別顯示一次。新增 `where buffer=memory` 可只檢視預設緩衝區。

要將列印的條目儲存到檔案，請新增 `file=`：`/log/print file=log-before-upgrade` 會寫入 `log-before-upgrade.txt`。

### 查詢某個時間發生了什麼 {#find-what-happened-at-a-certain-time}

將 `time` 與日期和時間比較，可檢視某個時間段（例如一夜）的條目：

```ros
/log/print where time>"2026-10-02 01:00:00" and time<"2026-10-02 06:00:00"
```

上行鏈路丟失通常表現為 WAN 介面的 `interface,info ether1 link down` 和 `link up` 條目，以及 DHCP 用戶端或 PPP 條目。當上行鏈路保持 up 但提供商停止轉發流量時，不會記錄任何內容；請使用 [網路監控](../netwatch.md) 記錄此類中斷。預設緩衝區的 1000 條條目能回溯多久取決於路由器記錄了多少日誌。要保留更多，請記錄到磁碟或 syslog 伺服器。

### 查明誰更改了配置 {#find-out-who-changed-the-configuration}

每次配置更改都會記錄主題 `system,info`、更改者（使用者以及該使用者如何連線，或排程器條目）和命令：

```ros
[admin@MikroTik] > /log/print where topics~"system" and message~" by "
 2026-10-02 17:33:27 system,info static dns entry added by scheduler:add-nas-dns (*2 = /ip dns static add address=192.168.88.20 name=nas.lan)
```

### 寫入自己的條目 {#write-your-own-entries}

指令碼使用 `:log info`、`:log warning`、`:log error` 和 `:log debug` 寫入日誌。在命令列上，`/log/info`、`/log/warning`、`/log/error` 和 `/log/debug` 作用相同。這些條目會獲得主題 `script,info`、`script,warning` 等。參見 [指令碼](../../developer-guides/scripting/index.md)。

## 為某個功能記錄偵錯訊息 {#log-debug-messages-for-one-feature}

許多功能會寫入偵錯訊息，只有在規則選擇它們時才會記錄。要對某個功能進行故障排除，請將其 `debug` 訊息記錄到單獨的記憶體緩衝區，以免它們將其他條目擠出預設緩衝區。例如，當用戶端無法從 DHCP 伺服器獲取地址時：

```ros
/system/logging/action/add name=dhcpdebug target=memory \
    memory-lines=2000
/system/logging/add topics=dhcp,debug action=dhcpdebug
```

讀取緩衝區，並在測試之間清空它：

```ros
/log/print where buffer=dhcpdebug
/system/logging/action/clear action=dhcpdebug
```

規則只匹配擁有其全部主題的條目，因此 `topics=dhcp,debug` 只選擇 DHCP 偵錯訊息，不選擇其他內容。要排除某些功能新增的封包轉儲，請用 `!` 排除主題，例如 `topics=ntp,debug,!packet`。

完成後，將緩衝區儲存到檔案，然後刪除規則和動作。刪除規則會清空緩衝區：

```ros
/log/print where buffer=dhcpdebug file=dhcp-debug
/system/logging/remove [find action=dhcpdebug]
/system/logging/action/remove dhcpdebug
```

:::warning
偵錯訊息可能包含機密。例如，`ssh,debug` 會記錄會話加密金鑰，`ssh,debug,packet` 會記錄會話內容。請將偵錯訊息儲存在本地緩衝區中，不要將它們傳送到 syslog 伺服器或透過電子郵件傳送。
:::

## 重啟後保留日誌 {#keep-the-log-across-reboots}

預設的 `disk` 動作寫入路由器儲存上的檔案。為每個要保留的主題新增規則：

```ros
/system/logging/add topics=info action=disk
/system/logging/add topics=warning action=disk
/system/logging/add topics=error action=disk
/system/logging/add topics=critical action=disk
```

該動作會寫入 `log.0.txt`，直到它包含 `disk-lines-per-file` 行（預設 1000）。然後該檔案被重新命名為 `log.1.txt`，並開始新的 `log.0.txt`。該動作保留 `disk-file-count` 個檔案（預設 2），並刪除最舊的檔案。這些檔案位於 `/file`：

```ros
[admin@MikroTik] > /file/print where name~"^log"
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME       TYPE       SIZE  LAST-MODIFIED
0 log.0.txt  .txt file  1956  2026-10-02 17:32:13
```

最新條目也會顯示在 `/log/print` 中該動作的名稱下，因此每個條目會在那裡顯示兩次；新增 `where buffer=memory` 或 `where buffer=disk`。重啟後，當前檔案中的條目會再次顯示在 `buffer=disk` 下。要讀取較舊的檔案，請列印其內容，或從 `/file` 下載它：

```ros
:put [/file/get log.1.txt contents]
```

要保留更多歷史記錄，請提高這兩個值。要寫入 USB 驅動器或其他磁碟，請將磁碟的資料夾放在檔名前面；該資料夾必須存在：

```ros
/system/logging/action/set disk disk-file-name=usb1/log \
    disk-lines-per-file=5000 disk-file-count=5
```

要限制對內部快閃記憶體的寫入，請僅將所需的主題記錄到磁碟，或使用外部磁碟。

## 將日誌傳送到 syslog 伺服器 {#send-the-log-to-a-syslog-server}

預設的 `remote` 動作透過 UDP 埠 514 將條目傳送到 syslog 伺服器。它沒有伺服器地址（`remote=0.0.0.0`），也沒有預設規則使用它。設定伺服器和格式，併為每個主題新增規則：

```ros
/system/logging/action/set remote remote=192.0.2.10 \
    remote-log-format=syslog
/system/logging/add topics=info action=remote
/system/logging/add topics=warning action=remote
/system/logging/add topics=error action=remote
/system/logging/add topics=critical action=remote
```

使用單獨的規則：一條 `topics=info,warning,error` 的規則只匹配同時具有這三個主題的條目，而這樣的條目不存在。要僅傳送登入和登出，請使用 `topics=account`；失敗的登入具有主題 `system,error,critical`，因此它們會隨 `error` 或 `critical` 傳送。

要檢查伺服器是否收到條目，請自行寫入一條：

```ros
/log/warning "syslog test"
```

`remote-log-format` 選擇伺服器接收的內容（示例見“技術細節”）：

- `default` - 主題和訊息，不包含時間和主機名。
- `syslog` - BSD syslog（RFC 3164），正如大多數 syslog 伺服器透過 UDP 所期望的：優先順序、時間和路由器的身份（`/system/identity`）位於訊息之前。facility 為 `daemon`，severity 來自主題；設定 `syslog-facility` 和 `syslog-severity` 可更改它們。不傳送主題；設定 `add-topics-string=yes` 可將它們新增到訊息之前，以便伺服器能夠區分，例如 DHCP 和防火牆條目。不支援 RFC 5424。
- `cef` - Common Event Format，用於安全資訊和事件管理（SIEM）系統：登入和防火牆條目的額外欄位（使用者、服務、地址、介面）會變成 CEF 欄位。

BSD 時間沒有年份和時區，因此伺服器採用自己的時區。當路由器和伺服器位於不同時區時，設定 `syslog-time-format=iso8601`（`cef` 也會使用它），並使用 [NTP](../../system-information-and-utilities/ntp.md) 保持路由器時鐘正確。

透過 UDP 時，伺服器不可達期間條目會丟失。使用 `remote-protocol=tcp` 或 `tls` 時，路由器會在連線斷開期間在記憶體中為所有 remote 動作一起保留最多 1000 條條目，並在連線恢復後傳送它們；當緩衝區已滿時，較新的條目會被丟棄，且緩衝區會在重啟時丟失。透過 TCP 和 TLS 時，請使用 `remote-log-format=cef`：CEF 條目以分隔符（`cef-event-delimiter`）結尾，而 `default` 和 `syslog` 條目在流中彼此相連且沒有分隔符，因此大多數伺服器無法判斷一個條目在哪裡結束。

使用 `src-address` 選擇源地址，當伺服器可透過 [VRF](../../user-guides/routing-and-networking-protocols/vrf.md) 訪問時使用 `vrf`。

以下指南設定 Elasticsearch 以接收和分析 RouterOS 日誌：

<DocCardList />

### 透過 TLS 傳送日誌 {#send-the-log-over-tls}

要加密日誌，請使用 `remote-protocol=tls`。要檢查伺服器證書，請匯入簽署該證書的 CA 的證書，並設定 `check-certificate=yes`。如果沒有 `check-certificate=yes`，路由器會加密連線但接受任何證書：

```ros
/certificate/import file-name=syslog-ca.pem name=syslog-ca \
    passphrase="" trusted=yes
/system/logging/action/add name=siem target=remote remote=192.0.2.10 \
    remote-port=6514 remote-protocol=tls remote-log-format=cef \
    check-certificate=yes
/system/logging/add topics=info action=siem
/system/logging/add topics=warning action=siem
/system/logging/add topics=error action=siem
/system/logging/add topics=critical action=siem
```

當無法驗證證書時，路由器不傳送任何內容，會重試，並記錄一條以 `ssl: no trusted CA certificate found` 結尾的 `ssld,error` 條目。

`check-certificate=yes` 會檢查伺服器證書是否由受信任的證書籤署。它不會比較證書中的名稱與伺服器地址，因此來自任何受信任 CA 的證書都會透過：只信任你的日誌伺服器的 CA，或匯入伺服器自己的證書。路由器不會提供用戶端證書。

傳送到相同伺服器地址和埠的動作共享一個連線。請為它們設定相同的 `remote-protocol` 和 `check-certificate`。

## 透過電子郵件傳送日誌訊息 {#email-log-messages}

`email` 目標會為每個條目傳送一封電子郵件，主題和正文分別是主題和訊息。它使用 `/tool/e-mail` 的伺服器、埠、TLS 模式和發件人，因此請先配置該項（參見 [電子郵件](../../system-information-and-utilities/e-mail.md)）。例如，要為每個 critical 條目（例如登入失敗、看門狗重啟或時鐘校正）收到電子郵件：

```ros
/system/logging/action/add name=mail target=email \
    email-to=admin@example.com
/system/logging/add topics=critical action=mail
```

要僅接收失敗登入的電子郵件，請新增訊息必須匹配的 `regex`；`^` 表示訊息以該文字開頭：

```ros
/system/logging/add topics=critical regex="^login failure" action=mail
```

`email-cc` 可新增更多收件人。每封傳送的電子郵件都會記錄為 `e-mail,info sent <topics message> to: <address>`。請謹慎選擇主題：每個條目都會發送一封電子郵件，因此密碼猜測攻擊會發送數百封。請改用防火牆阻止此類攻擊（參見 [SSH 暴力破解防護](../../firewall-and-quality-of-service/user-guides/bruteforce-prevention.md)）。

## 在日誌訊息上執行指令碼 {#run-a-script-on-a-log-message}

`script` 目標會針對其規則匹配的條目執行 `/system/script` 中的指令碼。指令碼透過兩個變數獲取條目：`$topics`（例如 `system,error,critical`）和 `$message`。在指令碼仍在執行時匹配的條目會被跳過，指令碼自身記錄的條目不會再次啟動它。

例如，要針對任何服務（SSH、WinBox、WebFig、API）將失敗登入的源地址收集到地址列表中。地址在其最後一次失敗登入後會在列表中保留一天：

```ros
/system/script/add name=login-failure source={
    :local at [:find $message " from "]
    :while ([:typeof [:find $message " from " $at]] = "num") do={
        :set at [:find $message " from " $at]
    }
    :local ip [:pick $message ($at + 6) [:find $message " via " $at]]
    /ip/firewall/address-list/remove [find list=login-fail address=$ip]
    /ip/firewall/address-list/add list=login-fail address=$ip timeout=1d
}
/system/logging/action/add name=loginfailure target=script \
    script=login-failure
/system/logging/add topics=critical regex="^login failure" \
    action=loginfailure
```

規則的 `regex` 將指令碼限制為諸如 `login failure for user admin from 192.168.88.17 via ssh` 的條目。訊息中的使用者名稱來自用戶端，可能包含空格和單詞 `from`，因此指令碼取最後一個 ` from ` 之後的地址，該地址由路由器自己寫入。該列表本身不執行任何操作：請在防火牆規則中使用它（參見 [地址列表](../../firewall-and-quality-of-service/firewall/address-lists.md)），並豁免你自己的管理地址，以免輸錯密碼將你鎖定在外。

## 規則如何匹配條目 {#how-rules-match-entries}

當以下所有條件都成立時，規則會將條目傳遞給其動作：

- 條目擁有 `topics` 中列出的每個主題，並且不包含用 `!` 列出的任何主題。`topics=script,warning` 匹配 `script,warning` 條目，而不是每個 `script` 條目和每個 `warning` 條目。
- 當規則包含 `regex` 時，訊息與它匹配。正則表示式還會看到訊息之後的條目的額外欄位，因此 `$` 不會匹配登入條目訊息的結尾。
- 規則已啟用。

沒有 `topics` 的規則會匹配每個條目，包括偵錯訊息。

每條匹配的規則都會傳遞自己的副本，因此一個條目可以同時進入記憶體、磁碟和 syslog 伺服器。當兩條規則將同一條目傳遞給同一個動作時，該動作只儲存一次。

`prefix` 會為該規則的動作在訊息前新增文字：`prefix=core1` 會儲存和傳送 `core1: <message>`。可用它在共享 syslog 伺服器上區分路由器。

當你更改或停用使用 memory 動作的唯一規則時，該動作的緩衝區會被清空。更改動作本身，或使用該動作的多條規則中的一條，會保留條目。

## 主題 {#topics}

每個條目都有一個或多個主題。通常一個主題命名寫入該條目的功能，一個主題給出其重要性，某些功能還會新增更多主題。失敗登入具有主題 `system,error,critical`；SSH 偵錯訊息具有 `ssh,debug`，其封包轉儲具有 `ssh,debug,packet`。

### 重要性主題 {#importance-topics}

| 主題 | 條目 |
| :-- | :-- |
| `critical` | 需要關注的事件，例如登入失敗、看門狗重啟和時鐘校正。預設規則會將它們列印到控制檯。 |
| `error` | 錯誤。 |
| `warning` | 警告。 |
| `info` | 資訊性條目，例如登入、配置更改和鏈路狀態變化。 |
| `debug` | 用於故障排除的詳細訊息，僅在規則要求時記錄。 |
| `packet` | 已傳送或接收的封包內容（已解碼）。 |
| `raw` | 原始內容，例如十六進位制形式的封包，或與 LTE 調變解調器交換的 AT 命令。 |

### 功能主題 {#feature-topics}

| 主題 | 條目 |
| :-- | :-- |
| `account` | 使用者的登入和登出。 |
| `acme-client` | 獲取證書的 ACME 用戶端。 |
| `async` | LTE 調變解調器的命令通道。 |
| `backup` | 備份建立。 |
| `bfd` | BFD. |
| `bgp` | BGP. |
| `bridge` | 網橋。 |
| `calc` | 路由計算。 |
| `caps` | CAPsMAN 和 CAP。 |
| `certificate` | 證書。 |
| `clock` | 時鐘變更，例如由 NTP 或 IP Cloud 觸發。 |
| `container` | 容器。 |
| `ddns` | 動態 DNS。 |
| `dhcp` | DHCP 用戶端、伺服器和中繼。 |
| `discover` | 鄰居發現。 |
| `disk` | 磁碟。 |
| `dns` | DNS. |
| `dot1x` | 802.1X 認證。 |
| `dude` | The Dude. |
| `e-mail` | 電子郵件工具（`/tool/e-mail`）。 |
| `event` | 事件，例如已安裝到路由表中的路由或來自 LTE 調變解調器的訊息。 |
| `evpn` | EVPN. |
| `fetch` | fetch 工具。 |
| `firewall` | 防火牆規則，使用 `action=log` 或 `log=yes`，並帶有其 `log-prefix`。 |
| `gps` | GPS. |
| `gsm` | GSM 調變解調器和 SMS 工具。 |
| `health` | 健康監控（電壓、溫度、風扇）。 |
| `hotspot` | HotSpot. |
| `igmp-proxy` | IGMP 代理。 |
| `interface` | 介面，例如鏈路啟用和鏈路斷開。 |
| `ipsec` | IPsec. |
| `iscsi` | iSCSI. |
| `isis` | IS-IS. |
| `kvm` | 虛擬機器（KVM）。 |
| `l2tp` | L2TP 用戶端和伺服器。 |
| `ldp` | LDP. |
| `lora` | LoRa. |
| `lte` | LTE 和 5G 調變解調器。 |
| `manager` | User Manager. |
| `mpls` | MPLS. |
| `mqtt` | MQTT. |
| `mvrp` | MVRP. |
| `natpmp` | NAT-PMP. |
| `netwatch` | Netwatch. |
| `ntp` | NTP 用戶端和伺服器。 |
| `ospf` | OSPF. |
| `ovpn` | OpenVPN. |
| `pim` | PIM-SM. |
| `poe-in` | PoE-In 事件，例如當裝置自身透過 PoE 供電時的 LLDP 功率協商。 |
| `poe-out` | PoE 輸出。 |
| `pon` | PON SFP 模組。 |
| `ppp` | PPP. |
| `pppoe` | PPPoE 用戶端和伺服器。 |
| `pptp` | PPTP 用戶端和伺服器。 |
| `ptp` | 精確時間協定。 |
| `queue` | 佇列。 |
| `radius` | RADIUS 用戶端。 |
| `radvd` | IPv6 路由器通告。 |
| `rip` | RIP. |
| `route` | 路由。 |
| `rpki` | RPKI. |
| `rproxy` | 反向代理。 |
| `rsvp` | RSVP. |
| `script` | 指令碼（`:log`）以及 `/log/info` 及相關命令。 |
| `sertcp` | 序列埠遠端訪問（`/port/remote-access`）。 |
| `smb` | SMB 伺服器。 |
| `snmp` | SNMP. |
| `socksify` | Socksify. |
| `ssh` | SSH 伺服器和用戶端。 |
| `ssld` | RouterOS 功能的 TLS 連線，例如無法驗證的伺服器證書。 |
| `sstp` | SSTP 用戶端和伺服器。 |
| `stp` | 生成樹。 |
| `system` | 系統訊息，例如重啟和配置變更。 |
| `tftp` | TFTP 伺服器。 |
| `timer` | 定時器，例如 BGP keepalive 定時器。 |
| `tr069` | TR-069 用戶端。 |
| `update` | 軟體包更新。 |
| `upnp` | UPnP. |
| `ups` | UPS 監控。 |
| `vpls` | VPLS. |
| `vrrp` | VRRP. |
| `watchdog` | 看門狗。 |
| `web-proxy` | Web 代理。 |
| `wiliot` | Wiliot. |
| `wireguard` | WireGuard. |
| `wireless` | 無線介面。 |
| `zerotier` | ZeroTier. |

路由器還會列出主題 `amt`、`isdn`、`mme`、`read`、`simulator`、`state`、`store`、`telephony` 和 `write`，以及在 `option` 軟體包中的 `netinstall`。

## 故障排除 {#troubleshoot}

| 問題 | 原因和解決方法 |
| :-- | :-- |
| syslog 伺服器未收到任何內容。 | 預設的 `remote` 動作具有 `remote=0.0.0.0`；請設定伺服器地址。檢查是否有規則將條目傳遞給該動作：具有多個主題的規則需要所有這些主題。檢查路由器從 `src-address` 並在 `vrf` 中能夠到達伺服器，並且伺服器接受該協定和埠。 |
| TLS 日誌未傳送任何內容。 | 查詢 `ssld,error` 條目。`no trusted CA certificate found` 表示伺服器的 CA 證書未匯入或不受信任。 |
| 伺服器將多個條目顯示為一個。 | 透過 TCP 和 TLS 時，`default` 和 `syslog` 條目沒有分隔符；請使用 `remote-log-format=cef`。 |
| 條目在 `/log/print` 中顯示多次。 | 多個動作儲存了它們；用 `where buffer=memory` 過濾。 |
| 重啟後日志為空。 | memory 動作在重啟後不會保留；請記錄到磁碟或 syslog 伺服器。 |
| 某個 memory 緩衝區自行清空了。 | 使用它的唯一規則被更改或停用了。 |
| `bad disk file name` | `disk-file-name` 中的資料夾不存在。 |
| `action name can contain only letters and numbers` | 動作名稱不能包含 `-`、`_` 或其他字元。 |

## 技術細節 {#technical-details}

### 訊息格式 {#message-formats}

同一條登入失敗，在每種 `remote-log-format` 下伺服器接收到的內容（使用 `syslog-time-format=bsd-syslog` 和身份 `MikroTik`）：

```text
system,error,critical login failure for user guest from 192.168.88.17 via ssh
<27>Oct  2 17:36:35 MikroTik login failure for user guest from 192.168.88.17 via ssh
Oct  2 17:36:35 MikroTik CEF:0|MikroTik|hAP ax^2|7.25beta5|10|system,error,critical|High|dvchost=MikroTik dvc=192.168.88.36 msg=login failure for user guest from 192.168.88.17 via ssh app=ssh duser=guest outcome=failure src=192.168.88.17
```

- `syslog` 格式不攜帶 tag 欄位；訊息跟在身份之後。
- 使用 `syslog-severity=auto` 時，severity 來自主題：`debug` 7、`info` 6、`warning` 4、`error` 3。同時具有 `error` 和 `critical` 的條目（如示例中所示）會得到 3，因此針對 severity `crit` 的伺服器過濾器會漏掉登入失敗。優先順序是 facility 乘以 8 加上 severity：`daemon`（3）和 `error`（3）得到 `<27>`。
- CEF 頭包含板名、RouterOS 版本、事件類編號、主題和 severity（`info` 和 `debug` 為 `Low`，`warning` 為 `Medium`，`error` 為 `High`）。`dvchost` 是身份，`dvc` 是路由器的一個地址，`msg` 是訊息，隨後是條目的額外欄位。防火牆條目攜帶鏈、日誌字首、介面、地址和協定。值中的 `=` 和 `\` 會轉義為 `\=` 和 `\\`。每條 CEF 訊息以 `cef-event-delimiter` 結尾（預設 `\r\n`）。

### TCP 和 TLS {#tcp-and-tls}

- UDP 為每個條目傳送一個數據報。TCP 和 TLS 為每個伺服器地址和埠保持一個連線，由所有傳送到那裡的動作共享。
- 當 TCP 或 TLS 伺服器不可達時，路由器會在一個緩衝區中為所有 remote 動作保留條目，並重試連線。該緩衝區會在重啟時丟失。
- 當伺服器不可達時，最多 1000 條條目會在記憶體中等待；當緩衝區已滿時，較新的條目會被丟棄。
- CEF 訊息以分隔符結尾；`default` 和 `syslog` 訊息在流中彼此相連且沒有分隔符。
- `check-certificate=yes` 會根據 `/certificate` 中的受信任證書檢查伺服器證書，而不是檢查其中的名稱。路由器提供 TLS 1.2。

### 磁碟檔案 {#disk-files}

檔案中的每一行都以自己格式的日期開頭，`Oct/02/2026 16:49:36`，隨後是主題和訊息。`/system/logging/action/clear` 僅清空 memory 動作；對 disk 動作，它會失敗並顯示 `cleanup not supported on this target`。

有關所有引數，請參見 [`/system/logging`](../../cli-reference/system/logging/index.md) 和 [`/system/logging/action`](../../cli-reference/system/logging/action/index.md) CLI 參考，以及 [`/log`](../../cli-reference/log.md) 中的條目。
