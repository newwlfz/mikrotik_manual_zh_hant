---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/graphing"
sidebar_position: 11
title: "圖表"
sidebar_label: "圖表"
description: "RouterOS 圖形化監控：隨時間記錄 CPU、記憶體和磁碟使用情況，以及介面和簡單佇列的流量，在路由器的 `/graphs/` 網頁或 WinBox 中檢視每日、每週、每月和每年的圖表，選擇誰可以檢視這些圖表，並讓圖表在重啟後仍然保留。"
tags:
  - 'graphing'
  - 'monitoring'
  - 'resource-usage'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/graphing
captured_at: '2026-11-04T11:15:33+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

圖形記錄會跟蹤路由器隨時間的資源使用情況，併為其繪製圖形：

- CPU、記憶體和磁碟使用率。
- 透過某個介面的流量。
- 透過簡單佇列的流量。

你可以在路由器的 `/graphs/` 頁面上透過網頁瀏覽器檢視這些圖形，也可以在 WinBox 中檢視。在你為其新增規則之前，不會繪製任何圖形：路由器預設沒有圖形規則。如需完整演示，請觀看 [MikroTik YouTube 頻道上的圖形影片](https://youtu.be/FTQEnDZVHNc)。

## 為介面和路由器資源繪製圖形 {#graph-an-interface-and-the-routers-resources}

要為 `ether1`（預設配置中的 WAN 埠）上的網際網路流量以及 CPU、記憶體和磁碟使用率繪製圖形，並只向你自己的計算機 192.168.88.10 顯示，請新增一條介面規則和一條資源規則：

```ros
/tool/graphing/interface/add interface=ether1 \
    allow-address=192.168.88.10/32
/tool/graphing/resource/add allow-address=192.168.88.10/32
```

要在 WinBox 中建立相同的規則：

1. 開啟 **Tools > Graphing** 並選擇 **Interface Rules**。
2. 選擇 **New**，將 **Interface** 設為 `ether1`，並在 **Allow Address** 中輸入 `192.168.88.10/32`。保持 **Enabled** 和 **Store on Disk** 處於選中狀態，然後選擇 **OK**。
3. 選擇 **Resource Rules** 和 **New**。輸入相同的 **Allow Address**，保持 **Enabled** 和 **Store on Disk** 處於選中狀態，然後選擇 **OK**。此規則會同時收集 CPU、記憶體和磁碟使用率。

![WinBox Interface Graphing Rule dialog with ether1 selected, Allow Address set to 192.168.88.10/32, and Enabled and Store on Disk selected](/img/ada1611061bd9e96.webp)

在該計算機的網頁瀏覽器中開啟 `http://192.168.88.1/graphs/`。頁面會列出你的地址可以檢視的圖形：CPU usage、Memory usage、Disk usage 和 `ether1`。每個圖形頁面有四張圖：

- Daily graph - 5 分鐘平均值。
- Weekly graph - 30 分鐘平均值。
- Monthly graph - 2 小時平均值。
- Yearly graph - 1 天平均值。

第一批數值會在幾分鐘內出現，即第一個 5 分鐘平均值完成後。每張圖下方，頁面會顯示最大值、平均值和當前值。流量圖以位元每秒為單位，分別顯示傳入（`In`，介面上接收的）和傳出（`Out`，傳送的）流量。每個數值都是圖形區間內的平均值，因此短時突發會顯示得低於其峰值。

![Memory usage graphs in a web browser: daily, weekly, monthly and yearly graphs of the used memory, each with its maximum, average and current value](/img/42a3d6819ca0c861.webp)

要為每個介面繪製圖形，請新增一條帶有 `interface=all` 的規則。

## 為簡單佇列繪製圖形 {#graph-simple-queues}

如果你用[簡單佇列](../firewall-and-quality-of-service/queues/index.md#simple-queue)限制每個客戶，你可以為每個佇列繪製圖形，並讓每個客戶檢視自己佇列的圖形。例如，使用以下客戶佇列：

```ros
/queue/simple/add name=customer-12 target=192.168.88.12/32 \
    max-limit=20M/20M
/queue/simple/add name=customer-13 target=192.168.88.13/32 \
    max-limit=50M/50M
```

為所有簡單佇列繪製圖形，並讓運維人員的計算機 192.168.88.10 檢視所有圖形：

```ros
/tool/graphing/queue/add simple-queue=all allow-address=192.168.88.10/32
```

在 WinBox 中，開啟 **Tools > Graphing > Queue Rules** 並選擇 **New**。將 **Simple Queue** 設為 `all`，將 **Allow Address** 設為 `192.168.88.10/32`。保持 **Enabled**、**Store on Disk** 和 **Allow Target** 處於選中狀態，然後選擇 **OK**。若只為某個佇列繪製圖形，請在 **Simple Queue** 中選擇其名稱。

![WinBox Queue Graphing Rule dialog with all simple queues selected, Allow Address set to 192.168.88.10/32, and Allow Target selected](/img/30402c9aa121604f.webp)

`simple-queue=all` 還會為你之後新增的佇列以及 PPP 使用者的動態佇列繪製圖形。使用 `allow-target=yes`（預設值）時，佇列 `target` 中的每個地址也能看到該佇列的圖形。地址為 192.168.88.12 的客戶開啟 `http://192.168.88.1/graphs/`，會找到 `customer-12` 圖形，但看不到其他客戶的圖形。在佇列圖形中，`In` 是發往目標（客戶的下載）的流量，`Out` 是來自目標的流量（上傳），兩者各自也顯示為佇列 `max-limit` 的佔比。

:::warning
使用 `allow-target=yes` 時，target 範圍較寬的佇列會向其範圍內的所有人顯示圖形：target 為 192.168.88.0/24 的父佇列會向整個子網顯示，而 target 為 0.0.0.0/0 或某個介面的佇列，會向所有能訪問路由器 Web 伺服器的用戶端顯示。PPPoE 及其他 PPP 使用者的動態佇列以各自的介面作為 target。為同一佇列再新增一條帶 `allow-target=no` 的規則並不能隱藏該圖形，因為只要有任何一條規則允許，用戶端就能看到該圖形。存在此類佇列時，請將 `simple-queue=all` 規則設為 `allow-target=no`，併為每個應向其客戶可見的客戶佇列新增一條帶 `allow-target=yes` 的規則。
:::

## 為 PPPoE 使用者繪製圖形 {#graph-pppoe-users}

`interface=all` 會為每個 PPPoE 使用者的動態介面繪製圖形，例如使用者 `customer-12` 的 `<pppoe-customer-12>`，僅在使用者連線期間存在，使用者重新連線後索引會再次列出它。針對某個動態介面的規則無法在重新連線後繼續有效：介面會獲得新的 ID，而該規則會顯示一個未知介面，例如 `*F00000`。要為某個使用者永久繪製圖形，請為該使用者建立一個靜態 PPPoE 伺服器繫結，將 `service` 設為你 PPPoE 伺服器的 `service-name`，併為該繫結繪製圖形：

```ros
/interface/pppoe-server/add name=pppoe-customer-12 user=customer-12 \
    service=isp
/tool/graphing/interface/add interface=pppoe-customer-12 \
    allow-address=192.168.88.10/32
```

## 控制誰可以檢視圖形 {#control-who-can-see-the-graphs}

圖形頁面無需登入。當用戶端地址位於該圖形所對應規則的 `allow-address` 中時，該用戶端就能看到該圖形。預設的 `allow-address=0.0.0.0/0` 允許所有 IPv4 地址，因此請始終將其設定為需要檢視圖形的地址。`allow-address` 的更改會立即生效：

```ros
/tool/graphing/interface/set [find] allow-address=192.168.88.10/32
```

- 訪問許可權按圖形型別區分：介面規則開放其介面的圖形，資源規則開放 CPU、記憶體和磁碟圖形，佇列規則開放其佇列的圖形。
- 如需允許多個地址範圍，請為每個範圍新增一條規則。你可以為同一介面、佇列或資源新增多條規則，每條規則都有自己的 `allow-address`。
- `/graphs/` 頁面只列出你的地址可以檢視的圖形。你無權檢視的圖形頁面會顯示 `ERROR: NO ACCESS!`；不存在的圖形會顯示 `ERROR: INVALID ID!`。
- 已停用的規則不會顯示其圖形。
- 規則中的 `interface` 或 `simple-queue` 無法更改：請刪除該規則並新增一條新規則。

圖形由路由器的 Web 伺服器提供，HTTP 由 `www` 服務提供，HTTPS 由 `www-ssl` 提供，後者需要證書。預設配置的防火牆會丟棄來自網際網路發往路由器的連線，因此只能在 LAN 內訪問圖形。要限制哪些地址可以訪問 Web 伺服器（包括 WebFig 和 REST API），請在 [服務](../system-information-and-utilities/services.md) 中設定這些服務的 `available-from`。

要在不顯示 WebFig 登入頁的情況下向客戶顯示圖形，請關閉 [`/ip/service/webserver`](../cli-reference/ip/service/webserver.md) 中的 WebFig，並使用 WinBox 或 SSH 管理路由器：

```ros
/ip/service/webserver/set webfig-plain=no webfig-secure=no
```

要關閉圖形頁面並保留 Web 伺服器的其餘部分：

```ros
/ip/service/webserver/set graphs-plain=no graphs-secure=no
```

## 重啟後保留圖形 {#keep-the-graphs-across-reboots}

使用 `store-on-disk=yes`（預設值）時，路由器會將收集的資料寫入其內建儲存（即其檔案所在位置），圖形可在重啟後保留。使用 `store-on-disk=no` 時，資料保留在 RAM 中，重啟後圖形會從空白開始。路由器無法將圖形資料寫入 USB 或 SD 磁碟。

`store-every` 設定路由器寫入已收集資料的頻率：每 5 分鐘（預設值）、每小時或每天一次。從 RouterOS 進行的重啟會保留自上次寫入以來收集的資料。該設定適用於所有規則：

```ros
/tool/graphing/set store-every=hour
```

在 WinBox 中，開啟 **Tools > Graphing**，選擇 **Interface Rules**，然後在右側面板中選擇 **Graphing Settings**。在 **Store Every** 中選擇寫入間隔並選擇 **OK**。**Page Refresh** 控制瀏覽器重新載入 Web 圖形頁面的頻率；它不會改變資料收集間隔。截圖顯示的是預設值。

![WinBox Graphing Settings dialog showing Store Every set to 5 min and Page Refresh set to 00:05:00](/img/8ea93049cbe84f94.webp)

要更改某條規則是否在重啟後保留其資料，請在 **Interface Rules**、**Queue Rules** 或 **Resource Rules** 中開啟該規則，更改 **Store on Disk**，然後選擇 **OK**。

:::tip
在快閃記憶體儲存較小的裝置上，每條帶 `store-on-disk=yes` 的規則都會增加資料並向快閃記憶體寫入。對於重啟後不需要其圖形的規則，請將 `store-on-disk=no` 設為，例如帶有 `interface=all` 的規則。
:::

## WinBox 中的圖形 {#graphs-in-winbox}

WinBox 顯示相同的圖形。開啟 **Tools > Graphing**，選擇 **Interface Graphs**、**Queue Graphs** 或 **Resource Graphs** 標籤頁，然後開啟一個條目。在圖形視窗中選擇 **Daily**、**Weekly**、**Monthly** 或 **Yearly** 以更改時間範圍。拖動視窗邊緣可放大圖形。

![WinBox Graphing window with Resource Graphs selected and an enlarged Memory graph window showing the Daily, Weekly, Monthly and Yearly tabs; no samples have been collected](/img/d5a0be9655fca5e2.webp)

## 圖形故障排查 {#troubleshoot-the-graphs}

- `/graphs/` 不列出任何圖形 - 不存在規則，或者沒有規則允許你的地址。請使用 `/tool/graphing/interface/print`、`/tool/graphing/queue/print` 和 `/tool/graphing/resource/print` 檢查 `allow-address`。
- 新介面圖形缺失，或其頁面顯示 `ERROR: INVALID ID!` - 新增規則後，圖形可能需要幾分鐘才會出現。要立即顯示，請停用並啟用該規則。
- 圖形頁面顯示 `ERROR: NO ACCESS!` - 該圖形的規則不允許你的地址。對於佇列圖形，當規則帶有 `allow-target=yes` 時，你的地址也可能位於佇列的 `target` 中。
- `Can't change interface, please create new config` 或 `Can't change queue, please create new config` - 規則中的介面或佇列無法更改。請刪除該規則並新增一條新規則。
- 重啟後圖形為空 - 該規則帶有 `store-on-disk=no`。
- 規則顯示類似 `*F00000` 的介面 - 該規則指定的動態介面（例如 PPPoE 使用者）已重新連線。請透過靜態 PPPoE 伺服器繫結為該使用者繪製圖形。
- `/graphs/` 返回 `403 Forbidden` - 圖形頁面已透過 `/ip/service/webserver` 中的 `graphs-plain`（HTTP）或 `graphs-secure`（HTTPS）關閉。

## 技術細節 {#technical-details}

### 網頁 {#web-pages}

- `/graphs/` - 用戶端可以檢視的圖形列表。
- `/graphs/cpu/`、`/graphs/ram/`、`/graphs/hdd/` - CPU、記憶體和磁碟使用率。
- `/graphs/iface/<interface>/` - 某個介面的流量。
- `/graphs/queue/<queue>/` - 某個簡單佇列的流量。

索引會以 URL 編碼形式連結名稱，例如 `/graphs/queue/customer%2D12/`；使用純名稱也可以。佇列頁面還會顯示佇列的 target、`max-limit` 和 `limit-at`。每個圖形頁面都從其自己的資料夾以 GIF 影像形式載入圖形：`daily.gif`、`weekly.gif`、`monthly.gif` 和 `yearly.gif`。這些頁面會將 `page-refresh` 值（預設 300 秒）作為 HTTP `refresh` 頭髮送，因此瀏覽器會重新載入它們；當 `page-refresh=never` 時，會省略該頭。用戶端無權檢視的頁面會以 HTTP 狀態碼 200 和文字 `ERROR: NO ACCESS!` 或 `ERROR: INVALID ID!` 響應，而不是 HTTP 錯誤。

### 規則 {#rules}

- 沒有 `interface` 或 `simple-queue` 的規則適用於 `all`。
- 具有相同介面或佇列以及相同 `allow-address` 的第二條規則會被拒絕，並提示 `Graphing rule already exists`。
- `interface=all` 會為每個介面繪製圖形，也包括已停用的介面和環回介面 `lo`。
- 圖形規則沒有註釋：傳遞給 `add` 的 `comment` 不會被保留。

有關所有設定，請參閱 CLI 參考中的 [`/tool/graphing`](../cli-reference/tool/graphing/index.md)。
