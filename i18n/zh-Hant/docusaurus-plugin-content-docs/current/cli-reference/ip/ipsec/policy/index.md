---
sidebar_key: "cli-reference/ip/ipsec/policy"
title: "policy"
sidebar_label: 'policy'
source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/policy
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/policy {#ipipsecpolicy}
**型別：**目錄

:::info
策略順序很重要。它的工作方式類似於防火牆過濾器，策略從上到下執行（priority 引數已移除）。

在隧道模式下，所有封包都會被 IPIP 封裝，並且其新 IP 報頭的 src-address 和 dst-address 會設定為此策略的 sa-src-address 和 sa-dst-address 值。如果不使用隧道模式（即使用傳輸模式），則只有源地址和目標地址與 sa-src-address 和 sa-dst-address 相同的封包才能由此策略處理。傳輸模式只能處理源自主機且目的地為 IPsec 對等體（已建立安全關聯的主機）的封包。要加密網路之間（或網路與主機之間）的流量，必須使用隧道模式。
:::

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="T" typ="template">該項是否為用於分配給動態對等體的模板。</ArgTableRow>
<ArgTableRow arg="B" typ="backup">該項是否包含在備份中。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">該項是否已停用。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">該項是否為動態建立。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">此策略是否無效——可能原因是存在具有相同 src-address 和 dst-address 的重複策略。</ArgTableRow>
<ArgTableRow arg="A" typ="active">該項當前是否處於活動狀態。</ArgTableRow>
<ArgTableRow arg="*" typ="default">該項是否為預設項。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="peer" typ="multi { array-id, peer: enum
 }">策略應用到的對等體名稱。c</ArgTableRow>
<ArgTableRow arg="tunnel" typ="bool">是否使用隧道模式。</ArgTableRow>
<ArgTableRow arg="group" typ="enum">策略組名稱。</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { prefix6: ip6Prefix
, prefix4: ipPrefix
 }">封包中要匹配的源地址或網路。適用於使用隧道模式（`tunnel=yes`）或模板（`template=yes`）時。</ArgTableRow>
<ArgTableRow arg="src-port" typ="num">源埠。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { prefix6: ip6Prefix
, prefix4: ipPrefix
 }">封包中要匹配的目標地址或網路。適用於使用隧道模式（`tunnel=yes`）或模板（`template=yes`）時。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="num">目標埠。</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (all) { all:255 }">IP 協定號或名稱。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (encrypt | discard | none) { encrypt:2, discard:0, none:1 }">
對匹配流量採取的操作。
- `none` - 原樣傳遞封包。
- `discard` - 丟棄封包。
- `encrypt` - 應用此策略及其 SA 中指定的轉換。
</ArgTableRow>
<ArgTableRow arg="level" typ="enum (require | use | unique) { require:2, use:1, unique:3 }">
指定當無法找到此策略的部分 SA 時應執行的操作：
- `use` - 跳過此轉換，不丟棄封包，也不從 IKE 守護程式獲取 SA；
- `require` - 丟棄封包並獲取 SA；
- `unique` - 丟棄封包並獲取僅與此特定策略一起使用的唯一 SA。它用於多個用戶端可位於同一公共 IP 地址之後的設定中（NAT 後面的用戶端）。
</ArgTableRow>
<ArgTableRow arg="ipsec-protocols" typ="enum (ah | esp) { ah:1, esp:2 }">指定要對匹配流量應用的 Authentication Header 與 Encapsulating Security Payload 協定組合。</ArgTableRow>
<ArgTableRow arg="sa-src-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">端點地址</ArgTableRow>
<ArgTableRow arg="sa-dst-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">端點地址</ArgTableRow>
<ArgTableRow arg="proposal" typ="enum">提議模板名稱。</ArgTableRow>
<ArgTableRow arg="template" typ="bool">此策略是否為模板。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="active-interface" typ="iface_enum">建立 SA 所經過的介面。</ArgTableRow>
<ArgTableRow arg="ph2-count" typ="num">階段 2 交換的數量。</ArgTableRow>
<ArgTableRow arg="ph2-state" typ="enum (spawning | starting | ready-to-send | getspi-sent | getspi-done | msg1-sent | ready-to-establish | commiting | adding-sa | established | expired | no-phase2) { spawning:0, starting:1, ready-to-send:2, getspi-sent:3, getspi-done:4, msg1-sent:5, ready-to-establish:6, commiting:7, adding-sa:8, established:9, expired:10, no-phase2:11 }">當前階段 2 狀態。</ArgTableRow>
</ArgTable>
