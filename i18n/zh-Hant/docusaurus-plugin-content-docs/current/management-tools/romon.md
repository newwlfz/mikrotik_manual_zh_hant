---
sidebar_key: "management-tools/romon"
sidebar_position: 10
title: "RoMON"
sidebar_label: "RoMON"
description: "RoMON（Router Management Overlay Network，路由器管理覆蓋網路）在路由器之間建立一個獨立的 MAC 層覆蓋網路用於管理：對等節點發現、MAC ping、RoMON SSH、使用金鑰進行訊息認證，以及按埠參與並計算開銷。"
tags:
  - 'romon'
  - 'mac-layer'
  - 'management'
source: https://manual.mikrotik.com/docs/management-tools/romon
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RoMON（Router Management Overlay Network）在路由器之間構建獨立的 MAC 層對等發現和資料轉發網路。RoMON 封包使用 EtherType 0x88bf 和目的組播 MAC 01:80:c2:00:88:bf，並獨立於 L2 或 L3 配置進行處理：即使路由器的 IP 配置、路由或防火牆出現故障，仍然可以透過 RoMON 保持可達。這使得 RoMON 成為進入配置錯誤的路由器的恢復路徑，每次透過一個 overlay 跳。

RoMON 網路上的每臺路由器都有一個 RoMON ID，可以自動從埠 MAC 地址中選擇，也可以透過 `id` 配置。

RoMON 協定不加密訊息。加密來自執行在其之上的應用，例如 SSH 或安全的 WinBox 連線。

:::info
RoMON 封包可以透過網路交換器或網橋轉發，除非對組播流量有特定限制。使用帶硬體解除安裝的 MikroTik 網橋時，這些封包會被視為普通組播封包，並在網路中泛洪。

如果啟用了 RoMON 服務且交換晶片支援 ACL 規則，系統會自動建立動態規則，將這些封包重定向到 CPU，RoMON 服務在 CPU 上執行。但是，如果交換器不支援 ACL 規則且配置不一致，例如 CPU 和 RoMON 未打標籤封包不在同一 VLAN 中，RoMON 服務可能無法按預期工作。

**RB5009**（switch-chip 88E6393X）不支援此路徑。該晶片的 frame-types=admit-only-vlan-tagged 過濾器會在應用任何 ACL 規則之前丟棄 RoMON 幀，因此這些封包永遠無法到達 CPU。
:::

## 啟用 RoMON {#enable-romon}

在 [`/tool/romon`](../cli-reference/tool/romon/index.md) 選單中啟用該服務：

```ros
/tool/romon/set enabled=yes
```

當未配置 ID 時，它會自動選擇：

```ros
[admin@MikroTik] > /tool/romon/print
     enabled: yes
          id: 00:00:00:00:00:00
  current-id: DC:2C:6E:E7:10:6B
```

## 選擇埠 {#choose-ports}

參與 RoMON 網路的埠在 [`/tool/romon/port`](../cli-reference/tool/romon/port.md) 選單中配置。每個條目匹配一個物理介面名稱（或內建萬用字元 `all`），並可以禁止該介面上的 RoMON，或使用埠開銷允許它。網橋或其他主介面不能作為 RoMON 埠 — 請命名與網路通訊的物理埠。更具體的條目會覆蓋萬用字元條目。

預配置了一個介面列表為 `all` 的預設條目，因此在你更改它之前，每個介面都會以開銷 100 參與：

```ros
[admin@MikroTik] > /tool/romon/port/print
Flags: * - DEFAULT
Columns: INTERFACE, FORBID, COST
#   INTERFACE  FORBID  COST
0 * all        no       100
```

RoMON 不應監聽路由器的不可信側（它透過 MAC 地址接受管理連線）。禁止 WAN 埠並保留 LAN：

```ros
/tool/romon/port/add interface=ether1 forbid=yes
```

或者反過來：用萬用字元條目禁止所有內容，然後逐個允許受信任的介面：

```ros
/tool/romon/port/set [find default=yes] forbid=yes
/tool/romon/port/add interface=ether2 forbid=no
/tool/romon/port/add interface=ether3 forbid=no
```

## 使用金鑰保護覆蓋網路 {#protect-the-overlay-with-secrets}

RoMON 金鑰透過對訊息內容進行 MD5 雜湊來驗證訊息、檢查其完整性並防止重放。同一 RoMON 網路中的每臺路由器都應使用相同的金鑰。在全新設定中，在所有路由器上設定金鑰：

```ros
/tool/romon/set secrets="mysecret"
```

全域性列表位於 `/tool/romon`；特定於介面的列表可以在 `/tool/romon/port` 中按埠設定（如果埠列表為空，則使用全域性列表）。

傳送時，訊息會使用列表中的第一個 secret 進行雜湊，除非列表為空或以空 secret 開頭（在這種情況下，訊息會以未雜湊形式傳送）。接收時，未雜湊訊息只會被空列表或包含空 secret 的列表接受；而雜湊訊息只要攜帶列表中的任意 secret 就會被接受。

這種行為使得無需拆分網路即可進行滾動更換——而且即使你透過 RoMON 本身連線時執行輪換，輪換也能正常工作：

```ros
# 1. 每台路由器仍然发送未哈希的值，但也接受 "mysecret"
/tool/romon/set secrets=("","mysecret")
# 2. 每台路由器发送用 "mysecret" 哈希后的值，但仍接受未哈希的值
/tool/romon/set secrets=("mysecret","")
# 3. 每台路由器发送且只接受 "mysecret"
/tool/romon/set secrets="mysecret"
```

之後要更換 secret 時，請在一段時間內將舊 secret 和新 secret 都保留在列表中，並執行相同的輪換。

:::note
在 CLI 中，包含空 secret 的列表條目需要使用括號：`secrets=("","mysecret")`。在 WinBox 中，按 **Secrets** 欄位中的小 **+**，並將第一行留空。
:::

secret 不匹配的用戶端不會得到應答：

```ros
[admin@MikroTik] > /tool/romon/ping id=DC:2C:6E:E7:10:6B count=3
  SEQ HOST                                    TIME  SIZE STATUS
    0 DC:2C:6E:E7:10:6B                           32 timeout
    1 DC:2C:6E:E7:10:6B                           32 timeout
    2 DC:2C:6E:E7:10:6B                           32 timeout
    sent=3 received=0 packet-loss=100%
```

## 在覆蓋網路中查詢路由器 {#find-routers-in-the-overlay}

執行 [`/tool/romon/discover`](../cli-reference/tool/romon/discover.md) 可列出可到達的路由器：

```ros
[admin@MikroTik] > /tool/romon/discover
Flags: A - ACTIVE
Columns: ADDRESS, COST, HOPS, PATH, L2MTU, IDENTITY, VERSION
  ADDRESS            COST  HOPS  PATH               L2MTU  IDENTITY  VERSION
A F4:1E:57:46:89:89   200     1  F4:1E:57:46:89:89   1500  Router-B  7.26beta1
```

發現表會持續重新整理；使用 `duration` 時，它會在給定時間後停止。`address` 列儲存所找到路由器的 RoMON ID，其他 RoMON 工具使用的正是這個 ID。

## 使用 RoMON ping 測試連通性 {#test-connectivity-with-romon-ping}

```ros
[admin@MikroTik] > /tool/romon/ping id=F4:1E:57:46:89:89 count=5
  SEQ HOST                                    TIME   SIZE STATUS
    0 F4:1E:57:46:89:89                       1ms      32
    1 F4:1E:57:46:89:89                       0ms      32
    ...
    sent=5 received=5 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=1ms
```

## 透過 RoMON 開啟 SSH 會話 {#open-an-ssh-session-over-romon}

[`/tool/romon/ssh`](../cli-reference/tool/romon/ssh.md) 透過 overlay 開啟 SSH 會話，即使遠端路由器沒有 IP 地址也可以：

```ros
[admin@MikroTik] > /tool/romon/ssh F4:1E:57:46:89:89 user=admin
```

## 使用 WinBox 連線 {#connect-with-winbox}

在 WinBox 中，在登入介面選擇 **Connect To > RoMON Agent**，並選擇一個已儲存且啟用了 RoMON 的路由器作為代理，然後透過目標路由器的 RoMON ID 連線（參見 [WinBox](./winbox.md)）。觀看[影片教程](https://www.youtube.com/watch?v=Peg6UcSJ_eA)。

你也可以從命令列執行 WinBox，並指定 RoMON 代理和目標路由器的 ID。代理路由器必須已儲存在 WinBox 的受管路由器列表中，連線才能成功：

```bash
winbox.exe --romon 192.168.88.24 F4:1E:57:46:89:89 admin ""
```

## 技術細節 {#technical-details}

- 發現、ping 和 RoMON SSH 都透過原始乙太網幀執行，因此即使沒有任何 IP 配置也能繼續工作。
- [封包嗅探器](../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md)和 [Torch](../diagnostics-monitoring-and-troubleshooting/torch.md) 只顯示路由器傳送的 RoMON 幀；接收到的 RoMON 幀不會顯示。
- 發現表中的 `hops`、`path` 和 `cost` 描述 RoMON 路徑：執行 RoMON 的路由器會轉發 overlay 流量，因此相隔多個網段的目標會在 `path` 中顯示中間 ID。
- 始終存在一個 `[find default=yes]` 通配埠條目：它不能被移除、停用或啟用——只能修改其 `cost`、`forbid` 和 `secrets`（"failure: only cost, forbid and secrets can be changed for preset"）。將其設定為 `forbid=yes` 會把預設條目變成“全部拒絕”。

嗅探器和 Torch 僅在 `tx` 方向看到 RoMON 幀（EtherType 0x88BF）。接收到的 RoMON 幀不會出現在抓包或 Torch 中，即使使用 `mac-protocol=romon` 或 `direction=rx` 也是如此，因此在一臺響應另一臺路由器發現請求的路由器上抓包，只會包含它傳送的幀：

```ros
[admin@MikroTik] > /tool/sniffer/start interface=ether2 mac-protocol=romon
[admin@MikroTik] > /tool/sniffer/stop
[admin@MikroTik] > /tool/sniffer/packet/print proplist=time,direction,src-mac,dst-mac,protocol,size
Columns: TIME, DIRECTION, SRC-MAC, DST-MAC, PROTOCOL, SIZE
#  TIME      DIRECTION  SRC-MAC            DST-MAC            PROTOCOL  SIZE
0  0.449619  tx         DC:2C:6E:E7:10:6B  F4:1E:57:46:89:89  romon      171
1  0.44973   tx         DC:2C:6E:E7:10:6B  F4:1E:57:46:89:89  romon      145
2  0.950712  tx         DC:2C:6E:E7:10:6B  F4:1E:57:46:89:89  romon      171
3  0.951016  tx         DC:2C:6E:E7:10:6B  F4:1E:57:46:89:89  romon      145
```

要檢視 RoMON 交換的兩個方向，請在兩臺路由器之間的裝置上抓包，例如透過交換器的映象埠。

有關所有引數，請參閱 [`/tool/romon`](../cli-reference/tool/romon/index.md)、[`/tool/romon/port`](../cli-reference/tool/romon/port.md)、[`/tool/romon/discover`](../cli-reference/tool/romon/discover.md)、[`/tool/romon/ping`](../cli-reference/tool/romon/ping.md) 和 [`/tool/romon/ssh`](../cli-reference/tool/romon/ssh.md) CLI 參考頁面。
