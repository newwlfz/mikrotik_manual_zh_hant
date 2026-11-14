---
sidebar_key: "firewall-and-quality-of-service/firewall/address-lists"
sidebar_position: 1
title: "地址列表"
sidebar_label: "地址列表"
description: "地址列表將一個名稱下的 IP 地址、字首、範圍和 DNS 名稱分組，用於防火牆規則。條目可以是靜態的、由帶超時的規則新增，或從名稱解析得到。"
tags:
  - 'address-lists'
source: https://manual.mikrotik.com/docs/firewall-and-quality-of-service/firewall/address-lists
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

地址列表是一組命名的 IP 地址、字首，以及（僅限 IPv4）地址範圍。filter、NAT、mangle 和 raw 規則透過 `src-address-list` 和 `dst-address-list` 與其匹配，在名稱前加 `!` 則匹配不在該列表中的每個地址。這樣一條規則就能覆蓋多個地址，而你要改變規則適用的物件時，只需修改列表，不必修改規則。

條目來自三個來源：你手動新增、防火牆規則透過 `add-src-to-address-list` 和 `add-dst-to-address-list` 動作新增，以及路由器解析你放入列表的 DNS 名稱。IPv4 列表位於 `/ip/firewall/address-list`，IPv6 列表位於 `/ipv6/firewall/address-list`。二者相互獨立，即使兩個列表中使用了相同的名稱也是如此。

## 遮蔽來自地址列表的流量 {#block-traffic-from-a-list-of-addresses}

丟棄來自 WAN 且源地址屬於 `blocked` 列表的所有流量。`WAN` 是預設配置中承載網際網路埠的介面列表：

```ros
/ip/firewall/address-list/add list=blocked address=203.0.113.0/24 \
    comment="Abuse reports"
/ip/firewall/address-list/add list=blocked address=198.51.100.7
/ip/firewall/raw/add chain=prerouting action=drop \
    in-interface-list=WAN src-address-list=blocked \
    comment="Drop traffic from blocked addresses"
```

```ros
[admin@MikroTik] > /ip/firewall/address-list/print where list=blocked
Columns: LIST, ADDRESS, CREATION-TIME
# LIST     ADDRESS         CREATION-TIME
;;; Abuse reports
0 blocked  203.0.113.0/24  2026-10-01 08:50:12
1 blocked  198.51.100.7    2026-10-01 08:50:12
```

`/ip/firewall/raw` 中的規則在[連線跟蹤](../connection-tracking.md)之前執行，因此這條規則會丟棄從這些地址到達 WAN 的每一個數據包：包括髮往路由器自身和轉發服務的新連線，也包括你 LAN 內主機向它們發起連線後收到的應答。以後若要遮蔽更多地址，將它們加入列表即可。

要一次新增多條條目，可將多行 `add` 貼上到終端，或將它們寫入 `.rsc` 檔案再用 `/import` 匯入。`203.0.113.77/24` 與 `203.0.113.0/24` 是同一條目，因此第二次 `add` 會失敗並提示 `failure: already have such entry`，匯入也會就此停止。

IPv6 地址要加入 IPv6 列表，並在 `/ipv6/firewall/raw` 中使用相同的丟棄規則：

```ros
/ipv6/firewall/address-list/add list=blocked address=2001:db8:bad::/48
/ipv6/firewall/raw/add chain=prerouting action=drop \
    in-interface-list=WAN src-address-list=blocked \
    comment="Drop traffic from blocked addresses"
```

IPv6 主機可以在其 /64 內更換地址。對於 IPv6，應列出整個字首（/64 或更長），而不要列單個地址。

## 按名稱允許來自動態地址的訪問 {#allow-access-from-a-dynamic-address-by-name}

遠端辦公室或家庭連線常常使用會變化的地址。把它的 DNS 名稱放入列表，例如辦公室路由器的 DDNS 名稱，並允許來自它的 SSH 和 WinBox 訪問（SSH 為 TCP 埠 22，WinBox 為 TCP 埠 8291）：

```ros
/ip/firewall/address-list/add list=trusted address=office.example.com \
    comment="Office router"
/ip/firewall/filter/add chain=input action=accept protocol=tcp \
    dst-port=22,8291 src-address-list=trusted \
    comment="Allow SSH and WinBox from trusted addresses" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

該規則會排在預設的 `drop all not coming from LAN` 規則之前。若只是簡單地執行 `add`，規則會被放在丟棄規則之後，在那裡它永遠不會匹配。

路由器會解析該名稱，並將地址新增為動態條目，條目註釋就是該名稱：

```ros
[admin@MikroTik] > /ip/firewall/address-list/print where list=trusted
Flags: D - DYNAMIC
Columns: LIST, ADDRESS, CREATION-TIME
#   LIST     ADDRESS             CREATION-TIME
;;; Office router
4   trusted  office.example.com  2026-10-01 08:52:00
;;; office.example.com
5 D trusted  198.51.100.20       2026-10-01 08:52:00
```

當 DNS 記錄過期時，路由器會重新解析該名稱並替換已變化的地址，因此規則會跟隨辦公室的地址。

:::warning
該規則會向所有擁有該名稱所解析地址的主機開放 SSH 和 WinBox。請使用只有你能控制的名稱。訪問許可權取決於路由器 DNS 伺服器的應答，因此請使用你信任的 DNS 伺服器，並保留另一種進入方式，例如 VPN。如果 `/ip/service` 透過 `available-from` 限制了 WinBox 或 SSH，該地址也必須在那裡被允許（參見[限制誰可以使用某項服務](../../system-information-and-utilities/services.md#limit-who-can-use-a-service)）。
:::

## 遮蔽探測關閉埠的主機 {#block-hosts-that-probe-a-closed-port}

試圖訪問你 WAN 地址上 Telnet 的主機通常是在掃描弱裝置。將這類主機列入列表一天並丟棄其全部流量，包括髮往你轉發到 LAN 的服務的流量：

```ros
/ip/firewall/raw/add chain=prerouting action=add-src-to-address-list \
    in-interface-list=WAN protocol=tcp dst-port=23 \
    src-address-list=!trusted \
    address-list=port-scanners address-list-timeout=1d \
    comment="List hosts that probe the Telnet port"
/ip/firewall/raw/add chain=prerouting action=drop \
    in-interface-list=WAN src-address-list=port-scanners \
    comment="Drop listed hosts"
```

第一條規則將源地址加入 `port-scanners`，並把封包交給下一條規則。此後，第二條規則會丟棄來自該主機的每一個數據包，直到超時結束。每次新的探測都會把超時重設為整整一天。

一個數據包就足以把它的源地址列入列表，而封包的源地址是可以偽造的。請把依賴的地址（例如你的 DNS 伺服器、VPN 對端和辦公室）放入上一節中的 `trusted` 列表：`src-address-list=!trusted` 會使第一條規則跳過它們。

```ros
[admin@MikroTik] > /ip/firewall/address-list/print where list=port-scanners
Flags: D - DYNAMIC
Columns: LIST, ADDRESS, CREATION-TIME, TIMEOUT
#   LIST           ADDRESS        CREATION-TIME        TIMEOUT
2 D port-scanners  198.51.100.23  2026-10-01 08:50:30  23h59m55s
```

帶超時的條目是動態的（`D`）：它們不會被儲存到配置中，重啟後即被清除。掃描者還會再來，因此列表會再次被填滿。`address-list-timeout=none-static` 可以讓條目在重啟後保留，但這樣一來列表會隨著每個掃描者不斷增長，直到你手動刪除條目，而且每個新條目都會改動已儲存的配置。

若需要僅在多次嘗試後才將主機列入列表的規則，請參見 [SSH 暴力破解防護](../user-guides/bruteforce-prevention.md)和[埠敲門](../user-guides/port-knocking.md)，後者只在經過一段秘密的連線嘗試序列後才會開放埠。

## 檢視、刪除和匯出條目 {#view-remove-and-export-entries}

顯示列表，或僅統計其條目數量：

```ros
/ip/firewall/address-list/print where list=port-scanners
/ip/firewall/address-list/print count-only where list=port-scanners
```

刪除單條條目：

```ros
/ip/firewall/address-list
remove [find list=port-scanners address=198.51.100.23]
```

要把列表複製到另一臺路由器，請將其匯出到檔案。`file=` 要寫在 `where` 之前，因為 `where` 會把命令餘下的部分當作其條件。若把 `file=` 放在其後，匯出內容會列印到終端，而不會寫入檔案。

```ros
/ip/firewall/address-list/export file=blocked where list=blocked
```

檔案 `blocked.rsc` 包含該列表的靜態條目。動態條目不會被匯出。

```ros
/ip firewall address-list
add address=203.0.113.0/24 comment="Abuse reports" disabled=no dynamic=no \
    list=blocked
add address=198.51.100.7 disabled=no dynamic=no list=blocked
```

用 WinBox 中的 **Files**（參見[在 WinBox 中管理檔案](../../system-information-and-utilities/files.md#manage-files-in-winbox)）或使用 `scp` 把檔案複製到另一臺路由器，然後匯入：

```ros
/import blocked.rsc
```

該檔案只包含條目：另一臺路由器上的丟棄規則也需要另外新增。匯入會在遇到第一個已存在於列表中的地址時停止，並提示 `failure: already have such entry`。若以後要更新另一臺路由器上的列表，請先刪除其條目（該列表不含 DNS 名稱），再匯入新檔案：

```ros
/ip/firewall/address-list/remove [find list=blocked]
/import blocked.rsc
```

要清空含有 DNS 名稱的列表，請分兩步刪除：

```ros
/ip/firewall/address-list/remove [find list=trusted !dynamic]
/ip/firewall/address-list/remove [find list=trusted]
```

第一條命令刪除靜態條目；刪除名稱條目也會同時刪除它解析出的地址。第二條命令刪除由規則新增的動態條目。只執行一次 `remove [find list=trusted]` 也會選中該名稱對應的地址，並且在名稱被刪除後會以 `no such item` 停止。

## 條目的行為 {#how-entries-behave}

### 靜態條目與動態條目 {#static-and-dynamic-entries}

| 條目的建立方式 | 標誌 | 是否儲存到配置和匯出 | 重啟後 |
| :-- | :-- | :-- | :-- |
| 不帶 `timeout` 的 `add` |  | yes | 保留 |
| 使用 `address-list-timeout=none-static` 的規則 |  | yes | 保留 |
| 帶 `timeout` 或 `dynamic=yes` 的 `add` | `D` | no | 丟失 |
| 帶時間或 `address-list-timeout=none-dynamic` 的規則 | `D` | no | 丟失 |
| 由 DNS 名稱解析出的地址 | `D` | 否，但名稱條目會儲存 | 名稱條目保留 |

靜態條目在重啟後保留其 `creation-time`。由 DNS 和 DHCP 伺服器新增的條目也是動態的。

### 超時 {#timeouts}

最長超時為 `35w3d13h13m56s`。更長的超時會導致失敗並提示 `value of timeout is out of range (00:00:00 .. 35w3d13:13:56)`。

當規則匹配到列表中已存在的地址時，會重設該條目的超時。若該地址在該列表中已是靜態條目，則該條目保持靜態，不會被設定超時。

### 地址、字首和範圍 {#addresses-prefixes-and-ranges}

- 帶字首長度的地址會按其網路儲存：`203.0.113.77/24` 變為 `203.0.113.0/24`。
- 恰好等於一個字首的 IPv4 範圍會儲存為該字首：`198.51.100.0-198.51.100.255` 變為 `198.51.100.0/24`。其他範圍仍保持為範圍，例如 `198.51.100.10-198.51.100.20`。
- 已存在於列表中的條目會被拒絕並提示 `failure: already have such entry`。重疊的條目會被接受，例如一個 /24 和其中的某個地址。
- IPv6 列表接受地址和字首，但不接受範圍：會提示 `failure: 2001:db8::1-2001:db8::5 is not a valid dns name`。不帶字首長度的 IPv6 地址會按 /128 儲存。

:::note
任何不是有效地址的內容都會被當作 DNS 名稱儲存，且不會報錯。用簡寫形式寫的範圍（例如 `203.0.113.1-254`）會變成一個永遠無法解析的名稱，該條目不會匹配任何內容。請完整寫出範圍：`203.0.113.1-203.0.113.254`。
:::

### 域名 {#domain-names}

- 路由器使用自己的 DNS 設定（`/ip/dns`）解析名稱，併為應答中的每個地址新增一條動態條目，條目註釋為該名稱。IPv4 列表獲取 A 記錄，IPv6 列表獲取 AAAA 記錄。
- 動態條目不顯示超時。當 DNS 記錄過期時，路由器會重新解析該名稱：已變化的地址被替換，其餘保持不變。
- 列表儲存的是路由器 DNS 伺服器所應答的內容。若過濾型 DNS 伺服器對某個名稱應答 `0.0.0.0`，列表中就會放入 `0.0.0.0`。若某裝置使用其他 DNS 伺服器，則可能為同一名稱得到其他地址。
- 由 CDN 或輪詢 DNS 提供服務的名稱在每次查詢時可能返回不同地址，因此由該名稱構建的列表可能遺漏裝置實際使用的地址。當這些裝置使用路由器作為其 DNS 伺服器時，帶 `address-list` 的靜態 DNS `FWD` 條目會準確新增路由器向它們應答的地址（參見[在防火牆規則中使用域名](../../network-management/dns.md#use-domain-names-in-firewall-rules)）。
- 儲存名稱的條目會在 `ADDRESS` 中顯示該名稱。當名稱解析成功後，以其為註釋的動態條目會隨之出現。若沒有這些動態條目，則該名稱條目未解析成功，簡寫形式範圍變成名稱的情況就是這樣顯現的。
- 刪除名稱條目會同時刪除它解析出的地址。

## 其他可新增條目的功能 {#other-features-that-add-entries}

- DNS：帶 `address-list` 的靜態 DNS 條目會新增路由器為該名稱應答的地址，參見[在防火牆規則中使用域名](../../network-management/dns.md#use-domain-names-in-firewall-rules)。
- DHCP 伺服器：伺服器上或租約上的 `address-lists` 會新增已繫結租約的地址，參見 [`/ip/dhcp-server`](../../cli-reference/ip/dhcp-server/index.md) 和 [`/ip/dhcp-server/lease`](../../cli-reference/ip/dhcp-server/lease/index.md)。
- PPP：PPP 配置檔案中的 `address-list` 會新增伺服器分配的地址或用戶端收到的地址，參見[使用者配置檔案](../../authentication-authorization-accounting/ppp-aaa.md#user-profiles)。

有關所有引數，請參見 [`/ip/firewall/address-list`](../../cli-reference/ip/firewall/address-list.md) 和 [`/ipv6/firewall/address-list`](../../cli-reference/ipv6/firewall/address-list.md) 的 CLI 參考。
