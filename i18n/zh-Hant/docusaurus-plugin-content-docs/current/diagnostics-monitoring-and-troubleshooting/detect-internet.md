---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/detect-internet"
sidebar_position: 17
title: "檢測網際網路"
sidebar_label: "檢測網際網路"
description: "Detect Internet 會根據每個受監視介面的鏈路、路由以及 MikroTik 雲可達性，為其分配一個狀態（lan、wan、internet 及其他），並根據結果保持介面列表最新。"
tags:
  - 'detnet'
  - 'detect-internet'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/detect-internet
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Detect Internet 會監視 `detect-interface-list` 中的介面，併為每個介面賦予一個狀態：它是否已連線（link）、路由器通往網際網路的路由是否經過它，以及 MikroTik 的雲伺服器是否能透過它應答。它會把每個介面加入你指定的 LAN、WAN 或 internet 介面列表，因此使用這些列表的設定和指令碼會跟隨介面的當前狀態。

Detect Internet 預設處於關閉狀態（`detect-interface-list=none`），並且 hAP ax² 的預設配置不會開啟它。在它執行期間，路由器會透過 UDP 埠 30000 聯絡 `cloud.mikrotik.com` 以檢查網際網路狀態，參見[與 MikroTik 雲服務的通訊](../network-management/cloud/communication-mikrotik-cloud-servers.md)。

:::note
Detect Internet 會自行更改介面列表的成員。使用這些列表的規則和設定會在介面狀態變化時改變其效果。
:::

## 檢視哪個介面有網際網路 {#see-which-interface-has-internet}

為有網際網路的介面建立一個列表，並監視所有介面：

```ros
/interface/list/add name=internet
/interface/detect-internet/set detect-interface-list=all \
    internet-interface-list=internet
```

每個介面的狀態顯示在 `state` 選單中：

```ros
[admin@MikroTik] > /interface/detect-internet/state/print
Columns: NAME, STATE, STATE-CHANGE-TIME, CLOUD-RTT
#  NAME    STATE     STATE-CHANGE-TIME    CLOUD-RTT
0  lo      lan       2026-10-01 13:48:56
1  ether1  no-link   2026-10-01 13:48:56
2  ether2  slave     2026-10-01 13:48:56
3  ether3  slave     2026-10-01 13:48:56
4  ether4  slave     2026-10-01 13:48:56
5  ether5  slave     2026-10-01 13:48:56
6  wifi1   slave     2026-10-01 13:48:56
7  wifi2   slave     2026-10-01 13:48:56
8  bridge  internet  2026-10-01 13:49:02  12ms
```

這臺路由器透過其區域網路中的另一臺路由器獲得網際網路，因此它的 `bridge` 具有 internet 狀態。在典型的家用路由器上，internet 狀態會落在具有預設路由的介面上，例如 `ether1`。網橋的埠顯示為 `slave`，而這裡的 `ether1` 沒有網線（`no-link`）。`lo` 是路由器的環回介面，顯示為 `lan`。

具有 internet 狀態的介面是 `internet` 列表的動態成員：

```ros
[admin@MikroTik] > /interface/list/member/print where list=internet
Flags: D - DYNAMIC
Columns: LIST, INTERFACE
#   LIST      INTERFACE
;;; INTERNET detected
0 D internet  bridge
```

## 謹慎使用這些列表 {#use-the-lists-with-care}

這些列表會自行變化：介面狀態改變時，它會離開 `internet` 或 `wan` 列表；鏈路發生變化後，每個介面又會重新變為 `lan`。不要將這些列表用於信任決策，例如在接受流量的防火牆規則中，也不要將它們設定為預設配置的 `LAN` 和 `WAN` 列表。它們適合資訊性用途，例如在報告哪條線路有網際網路的指令碼中。

以相同方式設定 `lan-interface-list` 和 `wan-interface-list`，以填充其他狀態對應的列表。

## 狀態如何工作 {#how-the-states-work}

| 狀態 | 含義 |
| :-- | :-- |
| `no-link` | 介面沒有鏈路。 |
| `slave` | 該介面是網橋或其他介面的埠，例如網橋埠或網橋中的 Wi-Fi 介面。 |
| `lan` | 二層介面的起始狀態，也是鏈路變化後重新回到的狀態。 |
| `unknown` | 路由器正在檢查該介面。大約持續 6 秒。 |
| `wan` | 路由器到 8.8.8.8 的活動路由經過該介面。三層隧道（例如 IPIP）在其鏈路建立後會變為 `wan`。 |
| `internet` | 一個 `wan` 介面，路由器透過它在 UDP 埠 30000 上到達 `cloud.mikrotik.com`。路由器到雲伺服器的路由必須經過該介面。 |

路由器會在鏈路變化、路由變化或 Detect Internet 設定變化後再次檢查介面。以下規則決定哪些狀態可以變化：

- 保持 `lan` 狀態達一小時的介面會被鎖定。它只會在鏈路變化後改變，即使之後有一條到 8.8.8.8 的路由經過它也是如此。
- `wan` 介面只會在鏈路變化後回到 `lan`。
- 當雲伺服器停止應答時（在預設 `request-interval` 下大約 4 分鐘後），或當到雲伺服器的路由不再經過該介面時，`internet` 介面會回退為 `wan`。當伺服器再次應答時，該介面會重新獲得 `internet` 狀態。
- 如果有兩條等開銷路由經不同介面到達 8.8.8.8，則這兩個介面都不會變為 `wan`。

鏈路變化是指介面的鏈路斷開並再次建立，例如網線被拔出再插入，或介面被停用再啟用。

:::note
Detect Internet 顯示的是路由器活動路由所使用哪個介面，而不是每條線路的健康狀況。路由未啟用的備用線路會保持 `lan`，並且一小時後會被鎖定，因此 Detect Internet 並不是用於故障轉移的健康檢查。某些故障轉移設定會使用經一條線路到 8.8.8.8 的 /32 路由，這會在這條線路上保持 `wan` 狀態。要檢查備用線路，請使用帶 `check-gateway` 的路由（參見[故障轉移（WAN 備份）](../high-availability-solutions/load-balancing/failover-wan-backup.md)）或 [網路監控](./netwatch.md)。
:::

每次狀態變化都會以 `interface` 主題記錄日誌，例如 `ether1 detect WAN`。

## 故障排除 {#troubleshoot}

當所有介面都保持 `lan` 時：

- 檢查路由器到網際網路的活動路由是否經過該介面：

  ```ros
  /ip/route/print where active and dst-address=0.0.0.0/0
  ```

- 保持 `lan` 狀態達一小時的介面會被鎖定。請停用再啟用它，或拔出再插入其網線，以便路由器再次檢查它。
- 如果有兩條等開銷路由經不同介面到達 8.8.8.8，則這兩個介面都不會變為 `wan`。

當某介面為 `wan` 但從未變為 `internet` 時，請檢查路由器到 `cloud.mikrotik.com` 的路由是否經過該介面，以及通往雲伺服器的 UDP 埠 30000 是否在途中被阻止。

## 技術細節 {#technical-details}

### 雲檢查 {#cloud-check}

對於 `wan` 介面，路由器會向 `cloud.mikrotik.com` 的埠 30000 傳送一條 32 位元組的 UDP 訊息，伺服器會將其發回。路由器以 `request-interval` 的一半頻率傳送該訊息，因此在預設 2 分鐘的情況下大約每分鐘一次。`request-interval` 的取值範圍為 1 分鐘到 1 天。`state` 選單中的 `CLOUD-RTT` 顯示最後一次應答的往返時間。

### 動態列表成員 {#dynamic-list-members}

每個列表的每個動態成員都會獲得一條註釋，說明新增它的狀態：`LAN detected`、`WAN detected` 或 `INTERNET detected`。

### 設定變更 {#settings-changes}

Detect Internet 設定的變更會重新檢查所有被監視的介面。每個介面會顯示 `unknown` 幾秒鐘，然後顯示其狀態。

## 關閉它 {#turn-it-off}

停止監視介面：

```ros
/interface/detect-internet/set detect-interface-list=none
```

這也會從列表中移除動態成員。沒有要監視的介面後，Detect Internet 便不再聯絡雲伺服器。

有關所有引數，請參閱 [`/interface/detect-internet`](../cli-reference/interface/detect-internet/index.md) 和 [`/interface/detect-internet/state`](../cli-reference/interface/detect-internet/state.md) 的 CLI 參考。
