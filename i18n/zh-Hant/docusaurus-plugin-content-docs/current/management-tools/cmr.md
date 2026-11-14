---
sidebar_key: "management-tools/cmr"
title: "CMR"
description: "CMR 是用於 RouterOS 裝置機群的集中監控平臺。它支援對整個機群進行更新、監控和告警管理。"
tags:
  - 'cmr'
  - 'management'
source: https://manual.mikrotik.com/docs/management-tools/cmr
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

CMR 是一個面向 RouterOS 裝置機群的集中式監控平臺，可在整個機群範圍內進行更新、監控和告警管理。

:::info
`cmr` [軟體包](../getting-started/installation-and-upgrade/packages.md#extra-packages) 僅在具有 **arm**、**arm64** 和 **x86** 架構的裝置上受支援。CMR 用戶端是 RouterOS 的一部分，因此除具有 **smips** 和 **powerpc** 架構的裝置外，每臺裝置都可以作為 CMR 用戶端。
:::

## 概述 {#overview}

CMR 透過機群中的一臺裝置來管理整個 RouterOS 裝置機群。其中一臺裝置執行 CMR 伺服器，其他裝置作為 CMR 用戶端連線到它。在伺服器上，你可以檢視整個機群的狀態、對其進行升級、接收告警、在多臺裝置上同時執行命令、繪製網路拓撲圖，以及配置 WiFi 網路和 VLAN 埠。

### CMR 的功能 {#what-cmr-does}

- **裝置清單** - 列出每個用戶端的標識、板卡型號、RouterOS 版本、已安裝的軟體包、連線狀態和標籤。
- **機群升級** - 按規則升級裝置組：通道或固定版本、計劃時間、裝置組的順序以及故障策略。軟體包來自 MikroTik 更新伺服器或伺服器上的某個目錄。
- **告警** - 監視資源使用情況、健康感測器、可用性、升級、介面和日誌行，在滿足條件時寫入日誌訊息、執行指令碼或呼叫 webhook。
- **在多臺裝置上執行命令** - 在選定的裝置上執行指令碼並顯示各裝置的輸出，還可重啟、升級或配對裝置。
- **儀表板** - 顯示所選裝置的即時摘要：連線狀態、資源使用情況、介面、流量和 WiFi 用戶端。
- **網路拓撲** - 繪製網路拓撲圖，裝置之間的鏈路根據鄰居和埠資料生成。該圖在 GUI 中顯示。
- **應用流量** - 收集經過所選路由器（通常是閘道器）的各類應用的統計資料。
- **WiFi 配置下發** - 一次性定義 WiFi 網路和射頻設定，並將其應用到選定的接入點，還可按頻段分別應用。
- **VLAN 配置下發** - 將用戶端的選定埠作為 access 埠或 trunk 埠加入 VLAN。

### CMR 不具備的功能 {#what-cmr-does-not-do}

- CMR 不配置 IP 地址、DHCP、路由、防火牆、使用者或其他裝置設定。請在裝置上使用 WinBox、WebFig 或 CLI 進行配置。若需在多臺裝置上做一次性更改，請使用 `run-script`。
- CMR 不會編輯或接管裝置現有的配置。它會在其旁邊建立自己的配置物件，並在重疊之處接管，例如某個 WiFi 射頻或某個網橋埠。
- CMR WiFi 會把配置寫入每個接入點。它不負責協調接入點之間的漫遊，也不充當集中認證伺服器。

### 工作原理 {#how-it-works}

- 伺服器執行在安裝了 `cmr` 軟體包的裝置上。用戶端是 RouterOS 的一部分，因此除 **smips** 和 **powerpc** 架構的裝置外，每臺裝置都可以作為用戶端。
- 用戶端透過鄰居發現（MNDP）或 DNS 找到伺服器，也可以連線到 `controller-addresses` 中設定的地址。使用 DNS 時，用戶端會解析 `_cmr._tcp.lan` 和 `_cmr._tcp.<domain>`，其中 `<domain>` 是它從 DHCP 收到的域名（選項 15，`domain-name`）。伺服器不必是閘道器，用戶端可以跨路由網路連線，包括透過 NAT 或 VPN。
- 用戶端被管理之前，雙方必須達成一致。這稱為配對。配對後，伺服器從用戶端收集狀態資料，並向其下發配置，例如 WiFi 網路。
- CMR 下發的配置在用戶端上以受管物件的形式儲存，並標記為 **Y** 標誌。它們無法在用戶端上修改，並且在伺服器不可達時仍然生效。停用用戶端會移除這些物件。
- 請使用 WinBox 4 或 WebFig 來訪問 CMR 選單。WinBox 3 不支援這些選單。

CMR 最適合執行預設配置或接近預設配置的裝置，例如開箱即用的裝置。CMR 不會讓其物件去適配自定義的網橋、VLAN 或 WiFi 設定，因此對於大量使用非標準配置的裝置，可能需要先進行手動調整，CMR 配置下發才能按預期工作。

### 入門 {#getting-started}

1. 在將作為伺服器的裝置上安裝 `cmr` 包，並使用 `/cmr set enabled=yes` 啟用伺服器。
2. 在每臺要管理的裝置上，使用 `/cmr/client set enabled=yes` 啟用用戶端。如果用戶端無法自行發現伺服器，請新增 `controller-addresses`。
3. 批准配對。在預設配置中，伺服器會等待批准：新裝置會以 **P** 標誌列在 `/cmr/device` 中，直到你為它們執行 `pair`。配對部分介紹了這些選項。
4. 為裝置分配標籤，例如按站點和按角色，以便規則可以選擇裝置組。
5. 為這些標籤建立升級規則和告警規則。

[`CMR CLI Reference`](../cli-reference/cmr.md) 提供了伺服器上 [`/cmr`](../cli-reference/cmr.md) 選單中每個引數和命令的詳細說明。[CMR-用戶端](./cmr/client.md) 指南介紹了用戶端側，而 [`CMR-Client CLI Reference`](../cli-reference/cmr/client.md) 提供了受管裝置上 [`/cmr/client`](../cli-reference/cmr/client.md) 選單中每個引數和命令的詳細說明。

CMR 伺服器透過 [`/cmr`](../cli-reference/cmr.md) 選單進行配置。

## 啟用 CMR 伺服器 {#enable-the-cmr-server}

CMR 用戶端透過 TCP 埠 `54321` 連線到伺服器。在伺服器的防火牆（`input` 鏈）中允許來自用戶端的入站連線訪問此埠，並允許此流量透過用戶端與伺服器之間的任何防火牆。

啟用伺服器：

```ros
[admin@MikroTik] > /cmr set enabled=yes
```

啟用伺服器後，該路由器將成為已連線 CMR 用戶端的管理控制器。裝置列表（包括伺服器本身）顯示在 [`/cmr/device`](../cli-reference/cmr/device.md) 選單中。

### 伺服器設定 {#server-settings}

[`/cmr`](../cli-reference/cmr.md) 選單還控制用戶端如何找到伺服器，以及伺服器從用戶端收集哪些內容：

- `controller-addresses` - 當裝置無法透過鄰居發現（MNDP）或 DNS 自動發現伺服器時，傳送給這些裝置的伺服器 IP 地址。
- `track-topology` - 從用戶端獲取路由、WiFi 登錄檔、ARP 表、鄰居、DHCP 狀態和介面狀態。網路拓撲佈局的自動鏈路依賴於此資料。預設值：`yes`。
- `fetch-comments` - 從用戶端獲取介面、埠和 WiFi 登錄檔條目的註釋。預設值：`yes`。
- `auto-labels` - 選擇伺服器從用戶端獲取哪些自動標籤：`version`、`architecture`、`model`、`board-name`、`identity`、`address` 和 `ssid` 中的任意項，或者 `all` 或 `none`。預設值：`all`。
- `apptraffic-devices` - 按標籤選擇要從中收集應用流量統計資訊的裝置。預設值：`gateway`，即帶有 `gateway` 標籤的裝置。設定為 `all` 可選擇所有裝置。
- `upgrade-check-interval` - 伺服器檢查更新伺服器以獲取新版本的頻率。最小為 1 分鐘。預設值：`10h`。
- `packages-directory`、`packages-cache-type` 和 `packages-cache-limit` - 伺服器從哪裡獲取並存儲升級包。“升級源”部分描述了它們。

目前，對於未設定的項，`/cmr/get` 返回空值，而不是其預設值。要將某個設定恢復為預設值，請在其名稱前加上 `!`，例如 `/cmr set !upgrade-check-interval`。

目前，更改 `packages-directory`、`upgrade-check-interval` 或 `pairing-requirement` 會重啟伺服器上的 CMR：每個用戶端都會重新連線，仍然匹配的狀態警報會再次執行其操作。

## 配對 {#pairing}

只有雙方裝置都同意，配對才會建立。每臺裝置都有自己的 `pairing-requirement` 設定，它定義了在本地裝置接受配對之前，遠端裝置必須做什麼。由於每一方都有自己的要求，只有在雙方裝置的要求都得到滿足後，配對才會成功。

在本地執行 `pair` 命令始終會從此裝置批准配對，無論其配置的要求是什麼。CMR 伺服器和用戶端都支援 `pairing-requirement=none`、`password` 和 `confirm`：

- **none** - 不需要額外批准。此裝置會自動接受配對。
- **password** - 遠端裝置可以透過提供此裝置上 RouterOS 使用者的使用者名稱和密碼來批准配對，使用 `pair` 命令的 `username` 和 `password` 引數。CMR 沒有單獨的配對密碼。也可以透過 `pair` 命令在本地批准配對。
- **confirm** - 必須使用此裝置的 `pair` 命令在本地批准配對，伺服器上為 `/cmr/device/pair`，用戶端上為 `/cmr/client/pair`；無法從遠端側批准。

把 `pairing-requirement` 理解為在此裝置同意配對之前必須發生的事情。只有在雙方裝置都同意後，配對才會完成。

### 典型配對場景 {#typical-pairing-scenarios}

- **none** 適用於可信環境，在此類環境中，裝置一旦發現彼此就應自動配對。例如，同一受管 LAN 上的 CMR 伺服器和用戶端都可以使用 **none**，從而無需使用者互動即可完成配對。
- **confirm** 強制在伺服器上進行明確的本地批准：僅發現新用戶端本身還不夠；管理員必須在伺服器上執行 `pair` 命令，伺服器才會接受該用戶端。
- **password** 適用於需要遠端批准，但物理或管理訪問兩臺裝置都不方便的情況。例如，用戶端可以使用 **password**，允許 CMR 伺服器使用用戶端上某個使用者的憑據遠端滿足用戶端的要求。

兩臺裝置上的要求相互獨立。用戶端會自動接受配對（`none`），在伺服器提供用戶端上某個使用者的憑據時接受配對（`password`），或者僅在用戶端上執行 `/cmr/client/pair` 後才接受配對（`confirm`）。例如：

- CMR 伺服器：**none**，用戶端：**none** - 兩臺裝置都會自動接受。
- CMR 伺服器：**none**，用戶端：**password** - 當伺服器提供用戶端上某個使用者的憑據時，用戶端會接受。
- CMR 伺服器：**password**，用戶端：**none** - 當用戶端提供伺服器上某個使用者的憑據時，伺服器會接受。
- CMR 伺服器：**password**，用戶端：**password** - 每臺裝置都必須滿足另一臺裝置的 password 要求，除非使用 `pair` 命令在本地批准配對。
- CMR 伺服器：**confirm**，用戶端：**none** - 用戶端會自動接受，但必須在伺服器上執行 `pair` 命令。
- CMR 伺服器：**confirm**，用戶端：**password** - 當伺服器提供用戶端上某個使用者的憑據時，用戶端會接受，但還必須在伺服器上執行 `pair` 命令。

每條 `pair` 命令都使用 **另一臺** 裝置的使用者名稱和密碼：在伺服器上，[`/cmr/device/pair`](../cli-reference/cmr/device/pair.md) 使用正在配對的裝置的某個使用者，而在用戶端上，[`/cmr/client/pair`](../cli-reference/cmr/client/pair.md) 使用伺服器上的某個使用者。不帶憑據執行 `pair` 會批准本裝置這一側；當遠端側的要求為 `none` 時，這就能滿足雙方。配對通常可以從一個控制檯完成：在伺服器上，`/cmr/device/pair` 已經批准了伺服器這一側，因此伺服器自己的 `password` 只會在用戶端的控制檯輸入，絕不會在伺服器上輸入。伺服器的 `password` 要求僅在從用戶端發起配對時才重要。`confirm` 是唯一會強制在裝置自己的控制檯上執行操作的要求：在伺服器上設定時，配對無法僅從用戶端完成；在用戶端上設定時，配對也無法僅從伺服器完成。

透過 password 進行配對還會為你找到裝置：伺服器會向每臺選定的裝置提供 `username` 和 `password`，因此你不需要知道哪臺裝置對應哪個密碼。當一個站點中的每臺裝置各自帶有不同的出廠密碼，並且你面前有它們的包裝盒時，請對每個包裝盒執行一次 [`/cmr/device/pair`](../cli-reference/cmr/device/pair.md) `username=admin password=<password from one box>`：每次執行都會配對具有該密碼的裝置，其他裝置則保持待處理狀態。使用 `labels` 而不是 `all` 可將一次配對執行限制在裝置群的一部分。

要開始配對，請在其中一個裝置上執行 `pair` 命令：在 CMR 伺服器上執行 [`/cmr/device/pair`](../cli-reference/cmr/device/pair.md)，或在用戶端上執行 [`/cmr/client/pair`](../cli-reference/cmr/client/pair.md)。也可以使用物理復位按鈕執行配對：在伺服器上使用 [`/cmr/push-button`](../cli-reference/cmr/push-button.md)，或在用戶端上使用 [`/cmr/client/push-button`](../cli-reference/cmr/client/push-button.md)。

## 管理裝置 {#managing-devices}

[`/cmr/device`](../cli-reference/cmr/device.md) 選單列出由伺服器管理的裝置。裝置一連線到伺服器就會出現在列表中；在配對獲得批准之前，它會帶有 **P**（pending）標誌。伺服器自身顯示為帶有 **L** 標誌的裝置。每個條目顯示裝置標識、板卡、RouterOS 版本、標籤和執行時間。對於已連線的裝置，列表還會顯示連線地址。窄控制檯會省略放不下的列，因此那裡可能缺少地址，而 `print detail` 會顯示每個值：

```ros
[admin@MikroTik] > /cmr/device/print where labels~"Group2"
Flags: C - CONNECTED; U - UPGRADE-AVAILABLE
Columns: IDENTITY, BOARD, VERSION, LABELS, UPTIME, ADDRESS
 #    IDENTITY  BOARD       VERSION  LABELS  UPTIME   ADDRESS
 2 CU MikroTik  RB4011iGS+  7.x      Group2  1h5m53s  192.168.1.98
 3 CU MikroTik  RB4011iGS+  7.x      Group2  1h3m8s   192.168.1.99
 9 CU MikroTik  RB4011iGS+  7.x      Group2  1h9m37s  192.168.1.100
```

裝置的 `address` 是其連線到伺服器時的源地址。對於位於 NAT 後面的用戶端，它是轉換後的地址，因此多個用戶端可能顯示相同的地址。

這些標誌表示裝置狀態：`L` 表示伺服器自身，`P` 表示配對待處理，`C` 表示已連線，`S` 表示陳舊（無連線），`U` 表示裝置的升級通道上有不同版本可用。`U` 版本也可能早於已安裝版本，例如當裝置執行測試版本且其升級規則使用 `stable` 通道時。[`/cmr/device`](../cli-reference/cmr/device.md) CLI 參考列出了每個標誌和每個只讀值，例如板卡、序列號、已安裝軟體包、告警計數以及覆蓋該裝置的升級規則。

### 設定裝置屬性 {#set-device-properties}

你可以從伺服器更改受管裝置的以下屬性：

- `identity` - 重新命名裝置。新標識會應用到裝置本身。
- `labels` - 分配標籤以對裝置分組。標籤是整個 CMR 中通用的選擇機制：升級規則、告警規則、`run-script` 以及其他裝置命令都按標籤選擇裝置。
- `port-labels` - 按埠分配標籤。將每個埠寫為 `port:label`，同一埠的多個標籤用 `/` 分隔，埠之間用 `,` 分隔，例如 `port-labels=ether1:uplink/trunk,ether5:office`。列印輸出會用 `;` 分隔埠。`/cmr/vlan` 規則的 `port-labels` 會按這些標籤或按介面名稱選擇埠。
- `pairing-requirement` - 為單個裝置覆蓋伺服器的配對要求。

可使用 `where` 按這些屬性中的任意一個篩選列表，例如 `/cmr/device/print where connected` 或 `/cmr/device/print where labels~\"office\"`。對標籤使用 `~`，因為一個裝置可以有多個標籤：`labels=office` 只匹配整個標籤列表為 `office` 的裝置。要從裝置中刪除所有標籤，請將 `labels` 設定為空值。

`/cmr/device/export` 將裝置列表列印為 `add` 命令，每個裝置一條，包含其 `identity`、`ids`、`labels` 和 `pairing-requirement`，而 `/cmr/device/add` 會根據這些值建立裝置條目。

### 標籤與裝置選擇 {#labels-and-device-selection}

標籤對裝置進行分組。升級規則、警報規則、WiFi 和 VLAN 預配、佈局、`apptraffic-devices` 設定以及裝置命令均按標籤選擇裝置。

除了你分配的標籤之外，每臺裝置還有自動標籤，顯示在只讀的 `auto-labels` 值中：例如其地址、架構、型號、板卡名稱和標識。自動標籤與你自己標籤的選擇方式相同，因此 `labels=arm` 會選擇所有使用 `arm` 架構的裝置，而 `labels=Office-AP1` 會選擇具有該標識的裝置。

`labels` 值是以逗號分隔的列表。普通標籤使用 OR 組合。以 `+` 開頭的標籤還必須匹配（AND），以 `-` 開頭的標籤會排除裝置（AND NOT）。`all` 選擇所有裝置，包括 CMR 伺服器。

| 選擇器 | 選中的裝置 |
| --- | --- |
| `labels=office,lab` | 具有 `office` 標籤或 `lab` 標籤的裝置。 |
| `labels=office,+ap` | 同時具有 `office` 和 `ap` 標籤的裝置。 |
| `labels=office,-ap` | 具有 `office` 標籤的裝置，但具有 `ap` 標籤的裝置除外。 |
| `labels=office,lab,-ap` | 具有 `office` 或 `lab` 標籤的裝置，但具有 `ap` 標籤的裝置除外。 |
| `labels=all,-core` 或 `labels=-core` | 除具有 `core` 標籤的裝置之外的所有裝置。 |

:::note
`+` 和 `-` 符號必須位於列表元素的開頭。沒有逗號時，`labels=office+ap` 是單個標籤名稱。沒有任何裝置具有的標籤會被接受且不會發出警告，因此在依賴某一選擇之前請先檢查它，例如使用升級規則的 `show-devices` 或告警規則的 `devices` 計數。
:::

WiFi 專案還可以使用頻段標籤選擇某個頻段的無線電，VLAN 規則可以使用埠標籤選擇埠。WiFi 配置和 VLAN 預配章節對這些進行了說明。

### 在裝置上執行命令 {#run-commands-on-devices}

裝置選單提供了對選定裝置執行操作的命令，以及這些命令報告的只讀值：

- [`run-script`](../cli-reference/cmr/device/run-script.md) - 在每臺所選裝置上執行單行 RouterOS 指令碼並顯示其輸出。指令碼以有限許可權執行：需要 `policy` 許可權的命令（例如新增使用者）會失敗並提示 "not enough permissions (9)"。
- [`upgrade`](../cli-reference/cmr/device/upgrade.md) - 為所選裝置啟動升級任務，無論其升級規則的計劃如何。
- [`reboot`](../cli-reference/cmr/device/reboot.md) - 重啟所選裝置。該命令會立即返回。裝置重啟後，`rebooted` 示例告警規則會記錄 `<device> rebooted`，其中 `<device>` 為 `identity@address`。
- [`pair`](../cli-reference/cmr/device/pair.md) - 開始與所選裝置配對。
- [`wifi-logs`](../cli-reference/cmr/device/wifi-logs.md) - 監控所選裝置的 WiFi 日誌。按 `event`（`connected`、`disconnected` 或 `failed`）、按用戶端 MAC 地址（`address`）、按 `bssid` 或按時間範圍（`time-start` 和 `time-end`）篩選條目。由 CAPsMAN 管理的接入點的事件由 CAPsMAN 裝置記錄，並顯示在其下。如果未選擇裝置，則顯示所有記錄 WiFi 事件的裝置的條目。使用 `labels` 選擇裝置以僅顯示其條目。按 `c` 切換到用戶端檢視，該檢視列出每個用戶端及其最後接入點、連線、斷開和失敗次數、IP 地址、SSID 和訊號；按 `l` 返回日誌條目。
- [`apptraffic`](../cli-reference/cmr/device/apptraffic.md) - 所選裝置的應用流量監控器。
- [`dashboard`](../cli-reference/cmr/device/dashboard.md) - 所選裝置的即時檢視。

每個命令透過 `labels`（或 `numbers`）選擇裝置，並按裝置報告結果。例如，在所有帶有 `Group2` 標籤的裝置上執行命令：

```ros
[admin@MikroTik] > /cmr/device/run-script labels=Group2 script="/system/identity/print"
Columns: DEVICE, STATUS
DEVICE                  STATUS
MikroTik@192.168.1.98   running
MikroTik@192.168.1.99   running
MikroTik@192.168.1.100  running

Columns: DEVICE, STATUS, OUTPUT
DEVICE                  STATUS   OUTPUT
MikroTik@192.168.1.98   success   name: MikroTik
MikroTik@192.168.1.99   success   name: MikroTik
MikroTik@192.168.1.100  success   name: MikroTik
```

該命令首先將所選裝置列為 `running`，然後在指令碼完成時顯示每個裝置的 `STATUS` 和 `OUTPUT`。`run-script` 拒絕空選擇：沒有 `numbers` 或 `labels` 時，它會失敗並提示 "numbers and/or labels required"；如果標籤不匹配任何裝置，它會失敗並提示 "no devices selected"。此處，`labels` 遵循 CMR 中各處相同的標籤語法：一個逗號分隔的列表，其中普通標籤以 OR 組合，以 `+` 開頭的標籤也必須匹配（AND），以 `-` 開頭的標籤排除裝置（AND NOT）。例如，`labels=office,+ap` 選擇同時具有兩個標籤的裝置，而 `labels=all,-core` 選擇除帶有 `core` 標籤的裝置之外的所有裝置。沒有逗號時，`office+ap` 會被讀取為單個標籤名。目前，在指令碼中，`as-value` 與 `labels` 組合會失敗並提示 `no such item`。在那裡使用 `numbers` 選擇裝置，例如 `numbers=[find where identity="Office-AP1"]`。

#### run-script 許可權 {#run-script-permissions}

使用 [`/cmr/device/run-script`](../cli-reference/cmr/device/run-script.md) 傳送的指令碼會在每個用戶端上以 `read`、`write`、`test` 和 `reboot` 策略執行，且沒有使用者會話。需要其他策略的命令會失敗並提示 "not enough permissions (9)"，例如 `/user add` 需要 `policy` 策略，而 `/tool sniffer` 需要 `sniff` 策略。`/system backup save`、`/system reset-configuration` 和 `/file copy` 會以相同錯誤失敗。`/export` 可用：它會在輸出中返回用戶端的配置，因此 `run-script` 可以從整個裝置群收集配置匯出。敏感值不可讀取：`/export` 會省略它們，`/export show-sensitive` 也不會顯示它們的值，而 `get` 會將它們顯示為 `*`。它們仍然可以被設定，例如 PPP secret 密碼。

由 `run-script` 建立的指令碼和排程器條目會以相同的四個策略儲存，顯示為 `policy=reboot,read,write,test`。`owner` 是系統使用者（`*sys`），而不是控制器使用者。策略集無法在用戶端上更改：嘗試授予更寬策略的指令碼，其 `policy` 會被縮減為這四個策略。下表顯示了在 `run-script` 下每個策略可以執行的操作：

| 策略 | 示例命令 | 結果 |
| --- | --- | --- |
| `read` | `:put [/system identity get name]` | 正常，返回值。 |
| `read` | `/export` | 正常，返回不含敏感值的配置。 |
| `write` | `/file add contents=x`, `/ip service set telnet port=2323`, `/tool romon set enabled=no` | 正常，配置已更改。 |
| `write` | `/system script add`, `/system scheduler add` | 正常，條目以 `policy=reboot,read,write,test` 儲存。 |
| `write` | `/ppp secret add name=test password=abc` | 正常，即使缺少 `sensitive` 策略，密碼也會被設定。 |
| `test` | `/ping`, `/tool traceroute` | 正常 |
| `reboot` | `/system reboot` | 正常，用戶端會重啟並重新連線到伺服器。 |
| `policy` | `/user add`, `/user group add` | 失敗並提示 "not enough permissions (9)"。 |
| `sniff` | `/tool sniffer quick` | 失敗並提示 "not enough permissions (9)"。 |
| `sensitive` | `:put [/ppp secret get ... password]` | 該值顯示為 `*`。 |

#### CMR 所做更改的日誌記錄 {#logging-of-changes-made-by-cmr}

CMR 在用戶端上所做的更改會記錄在用戶端日誌中。訊息的 `by` 欄位表明該更改來自 CMR，幷包含使用者和伺服器地址：`cmr:<user>@<address>`，其中 `<user>` 是在 CMR 伺服器上執行該命令的使用者，`<address>` 是用戶端所見的伺服器地址。當 CMR 未提供使用者時，該欄位為 `cmr@<address>`。如果伺服器地址不可用，則僅顯示已知部分，例如 `cmr:<user>`，或者當也沒有使用者時僅顯示 `cmr`。例如：

```ros
system,info device added by cmr:admin@192.168.1.2 (*E = /interface bridge add comment=cmr-perm name=cmrperm-br)
```

## 儀表板 {#dashboard}

[`/cmr/device/dashboard`](../cli-reference/cmr/device/dashboard.md) 命令會開啟所選裝置的即時檢視：有多少臺已連線、CPU、記憶體和磁碟使用率、介面狀態、流量吞吐量，以及接入點及其站點。該檢視每隔幾秒重複一次，直到你停止它。按 `m`、`l`、`a`、`p`、`w` 或 `s` 可在主檢視、警報、裝置、埠、WiFi 和資源檢視之間切換，按 `D` 可將當前檢視寫入 `console-dump.txt` 檔案，按 <kbd>Control</kbd>+<kbd>Z</kbd> 暫停它，按 `Q` 退出。在裝置檢視中，`m` 返回主檢視：

```ros
[admin@MikroTik] > /cmr/device/dashboard labels=Group2
DEVICES          TOTAL  PAIRED  ONLINE  RESOURCES                MIN  AVG  MAX
                 3      3       3       CPU        ------------  0    0    1
                                        Memory     =====-------  21   46   85
                                        HDD        ==----------  15   23   29

NETWORK INTERFACES -------------------  BANDWIDTH ----------------------------
16     Ethernet                                             TX        RX
16     Enabled   =====================  Total               336.9KiB  194.1KiB
8      Running   =============--------  Uplink              37.9KiB   78.0KiB
7      Wifi                             Ethernet            169.3KiB  173.0KiB
7      Enabled   =====================  Wifi                167.5KiB  21.1KiB

ACCESS POINTS ------------------------  STATIONS -----------------------------
7      Total                            18     Total
3      Slave                            16     2.4GHz  =====================--
7      Running  ======================  2      5GHz    ==---------------------
3      2.4GHz   ============----------  17     N       ======================-
3      5GHz     ============----------  1      OFDM    -----------------------
1      6GHz     ====------------------  18     WPA2    =======================
2      BE       ========--------------
2      AX       ========--------------
3      N        ============----------
```

`labels` 引數接受與 CMR 其餘部分相同的標籤語法，因此 `labels=Group2` 顯示帶有 `Group2` 標籤的裝置，而 `labels=house,-ap` 顯示帶有 `house` 標籤但排除帶有 `ap` 標籤的裝置。[`/cmr/device/dashboard`](../cli-reference/cmr/device/dashboard.md) CLI 參考列出了其所有引數。

WebFig GUI 中會顯示相同的即時檢視：

<center>![](/img/30d86cdd185e9d5c.webp)</center>

<center>**The image shows the CMR dashboard in the WebFig GUI.**</center>

### 儀表板分割區 {#dashboard-sections}

儀表板分為八個部分：

- **裝置** - 已配對裝置和線上裝置的數量。只有當前已連線的已配對裝置才計為線上，因此離線的已配對裝置，或尚未配對的裝置，不會顯示為線上。
- **資源** - 每臺裝置當前的 CPU、記憶體和磁碟使用率。
- **頻寬** - 裝置流量吞吐量的即時圖表。綠色區域是上傳頻寬，紅色/棕色區域是下載頻寬，繪製最近幾分鐘的資料。摘要顯示當前、平均和最大下載與上傳速率。
- **活動警報** - 當前已觸發的警報規則，以及每個警報在多少臺裝置上處於活動狀態。
- **可用更新** - 在其升級通道上有不同 RouterOS 版本可用的裝置，這些版本由其升級規則提供。
- **流量** - 來自應用流量分類器的裝置應用流量表，涵蓋最近一小時。每一行是一個應用，包含其名稱、下載量及佔總量的份額（以進度條顯示），以及上傳量及其份額。
- **接入點** - 裝置上執行的接入點數量。WiFi 頻段選擇器（2.4、5 或 6 GHz）會篩選檢視，柱狀圖顯示每個通道上執行多少個接入點。
- **站點** - 連線到這些接入點的用戶端站點數量。WiFi 頻段選擇器會像對接入點那樣篩選檢視，柱狀圖顯示每個通道上連線了多少個站點。

## 裝置群升級 {#fleet-upgrades}

CMR 透過 [`/cmr/upgrade`](../cli-reference/cmr/upgrade.md) 選單中的升級規則管理整個裝置群的軟體升級。升級規則透過 `labels` 選擇其覆蓋的裝置、設定升級執行的時間，並定義要安裝的通道或版本。

### 升級規則 {#upgrade-rules}

規則透過 `labels` 選擇其覆蓋的裝置，這與 CMR 各處使用的標籤相同。如果省略 `labels`，則規則覆蓋所有已連線的裝置（`labels=all`）。普通列表將標籤以 OR 組合，而以 `+` 或 `-` 開頭的列表元素則以 AND 和 AND NOT 組合它們，例如 `labels=all,-core`。

例如，此規則建立一個每晚將所有已連線裝置升級到最新 `stable` 版本的升級任務：

```ros
[admin@MikroTik] > /cmr/upgrade/add name=nightly labels=all channel=stable schedule-time="00:00:00" strategy=sequential fail-policy=continue
```

每個引數設定規則的一個屬性：

- `name=nightly` 為規則命名。該名稱會顯示在規則列表中，並用於選擇該規則以立即執行。
- `labels=all` 選擇所有已連線的裝置。顯式給出 `all` 與省略 `labels` 相同。
- `channel=stable` 選擇升級通道：`long-term`、`stable`、`testing` 或 `development`。要固定到特定版本，可直接將版本設為通道值，例如 `channel=7.24.4`。
- `strategy=sequential` 依次升級裝置，並等待每臺裝置完成。另一種選擇是 `parallel`，它會同時升級所有覆蓋的裝置。
- `fail-policy=continue` 跳過失敗的裝置並繼續處理其餘裝置。未設定 `fail-policy` 時，規則使用 `stop`。第三種失敗策略是 `continue-order`。
- `schedule-time="00:00:00"` 每天午夜觸發此規則。`schedule-time` 是一個時間，可附帶可選的工作日，例如 `14:00:00`（每天 14:00）或 `00:00:00@sat`（每週六午夜）。多個時間用逗號分隔，例如 `00:00:00@sat,00:00:00@sun`。工作日用 `@` 分隔：如果使用空格，例如 `"14:00 sat"`，工作日會被丟棄，規則每天執行。

<center>![](/img/0d8b9ffebfe5c1f9.webp)</center>

<center>**The image shows the nightly rule as configured in the WinBox GUI.**</center>

每週規則以相同方式建立。例如，此規則每週六 14:00 升級兩個標籤組，並在首次失敗時停止：

```ros
[admin@MikroTik] > /cmr/upgrade/add name=weekly labels=Group1,Group2 channel=stable schedule-time="14:00:00@sat" strategy=parallel fail-policy=stop order=Group1,Group2
```

- `schedule-time="14:00:00@sat"` 每週六 14:00 啟動升級。工作日位於 `@` 之後，可以是 `sun`、`mon`、`tue`、`wed`、`thu`、`fri` 或 `sat`。
- `order=Group1,Group2` 設定標籤組及其處理順序。
- `fail-policy=stop` 在裝置失敗時停止整個升級。在此示例中，`Group1` 中的裝置失敗會停止升級，`Group2` 不會被升級。

<center>![](/img/8bea2f1401468823.webp)</center>

<center>**The image shows the weekly rule as configured in the WinBox GUI.**</center>

:::info
規則的順序決定優先順序。當多條規則選擇重疊的裝置時（例如一條 `labels=all` 規則和帶有特定標籤的規則），列表中第一條匹配某臺裝置的規則會認領該裝置。因此，放在首位的 `labels=all` 規則會覆蓋每臺裝置，而後續規則在 [`/cmr/upgrade/show-devices`](../cli-reference/cmr/upgrade/show-devices.md) 中不會顯示任何裝置。當每個標籤組都需要自己的規則時，請將特定標籤規則列在 `labels=all` 規則之前，並使用 `show-devices` 驗證每臺裝置的分配情況。
:::

啟用伺服器後，規則列表包含一個名為 `default` 的動態規則（標誌 `D`、`labels=all`、`channel=stable`）。它列在你自己的規則之後，並覆蓋沒有其他規則匹配的裝置。該規則沒有排程：它設定用於檢查這些裝置的 `U` 標誌和 `available-version` 的通道。如果你的裝置執行測試版或開發版構建，請建立覆蓋它們的規則，以免向它們提供 `stable` 作為升級。

要更改規則的位置，請使用 [`move`](../cli-reference/cmr/upgrade.md)，例如 `/cmr/upgrade/move [find name=weekly] 0`。目前，`add` 的 `place-before` 引數會將新規則新增到列表末尾。

### 執行升級 {#running-an-upgrade}

建立規則後，會根據其 `schedule-time` 排程一個作業。你無需等待排程時間即可開始升級：

- [`/cmr/upgrade/trigger`](../cli-reference/cmr/upgrade/trigger.md) - 立即啟動所選規則的作業，並提前升級其覆蓋的裝置，而無需等待 `schedule-time`。
- [`/cmr/upgrade/job/run-next`](../cli-reference/cmr/upgrade/job/run-next.md) - 立即執行已排程作業。對於升級規則的作業，原已排程作業仍保留在計劃中，而此次執行會作為新作業新增。使用 `/cmr/device/upgrade` 排程的作業沒有需要保留的排程，因此 `run-next` 會自行啟動該作業。
- [`/cmr/device/upgrade`](../cli-reference/cmr/device/upgrade.md) - 無論其規則的排程如何，升級選定裝置：立即升級，或在 `schedule-time` 的下一次出現時升級。未指定 `channel` 時，每臺裝置都在其自己的升級通道上升級，即 `/cmr/device` 中顯示的 `channel` 值。

在控制檯上，`/cmr/device/upgrade` 會顯示其啟動的作業中的裝置及其狀態，直到你按下 <kbd>Control</kbd>+<kbd>C</kbd> 或 `duration` 中給定的時間結束。停止輸出不會停止作業，作業會在伺服器上繼續執行。之後可使用 [`/cmr/upgrade/job/show-devices`](../cli-reference/cmr/upgrade/job/show-devices.md) 跟蹤它。

一次只能執行一個升級作業。當另一個作業正在進行時觸發第二個作業，會將新作業置於 `queued` 狀態，直到正在執行的作業完成。使用 [`/cmr/upgrade/version-check`](../cli-reference/cmr/upgrade/version-check.md) 檢視你的升級規則中配置的通道可用的最新版本。

### 升級源 {#upgrade-sources}

伺服器會檢查 MikroTik 更新伺服器，以獲取升級規則所使用的每個通道的最新版本。[`/cmr/upgrade/version-check`](../cli-reference/cmr/upgrade/version-check.md) 會顯示結果，而已連線的裝置會在 [`/cmr/device`](../cli-reference/cmr/device.md) 選單的只讀引數 `available-version` 中顯示最新可用版本。[`/cmr`](../cli-reference/cmr.md) 選單中的 `upgrade-check-interval` 設定控制該檢查執行的頻率。

當執行升級且所需版本在本地尚不可用時，伺服器會下載軟體包檔案，將其儲存起來併發送給裝置；而定期的版本檢查只查詢有哪些版本可用。[`/cmr`](../cli-reference/cmr.md) 選單中包含快取設定：`packages-cache-type` 選擇下載的軟體包是儲存在伺服器的儲存上（`directory`，即 `packages-directory` 下的 `cmrcache` 子目錄）還是儲存在 RAM 中（`memory`），`packages-cache-limit` 以兆位元組為單位設定快取的最大大小。當快取已滿時，伺服器會清除較舊的條目，為新下載的軟體包騰出空間。

要讓伺服器提供你自己的軟體包，請將 `.npk` 檔案放在伺服器檔案系統上的某個目錄中，並將 `packages-directory` 設定為該目錄。軟體包是逐個解析的：所需版本的軟體包如果已在該目錄中，就直接從那裡提供，無需重新下載，只有缺失的軟體包才會被下載到快取中。

使用軟體包目錄可以安裝更新伺服器不提供的版本。將每個架構的軟體包以及所覆蓋裝置已安裝的每個軟體包放入該目錄，將其選為 `packages-directory`，並將版本設定為通道。例如，對於具有 `arm` 架構和 `wifi-qcom` 軟體包的裝置：

```ros
[admin@MikroTik] > /file add name=cmr-packages type=directory
```

將 `routeros-<version>-arm.npk` 和 `wifi-qcom-<version>-arm.npk` 上傳到 `cmr-packages`，例如使用 SFTP，然後選擇該目錄並升級裝置：

```ros
[admin@MikroTik] > /cmr set packages-directory=cmr-packages/
[admin@MikroTik] > /cmr/device/upgrade labels=testgroup channel=7.24.4
```

`packages-directory` 的值從現有目錄中選擇，並以 `/` 結尾。目前，更改 `packages-directory` 會重啟伺服器上的 CMR，所有用戶端都會重新連線，因此請在用戶端在 `/cmr/device` 中重新顯示為已連線後再啟動升級任務。

如果在選中之後該目錄被刪除，`/cmr print` 仍會顯示它且不會給出警告，並且伺服器會將下載的軟體包保留在 RAM 中。使用相同的名稱重新建立該目錄，例如 `/file add name=cmr-packages type=directory`，並將軟體包放入其中。該設定不會改變，因此 CMR 不會重啟。

在將一組裝置升級到固定版本之前，請先升級該組中的一臺裝置。如果目錄中缺少某個軟體包，該任務會讓裝置保持在 `pending` 狀態並顯示錯誤 **no upgrade available**，同時不會重啟它。

:::warning
即使設定為通道的版本早於已安裝版本，也會安裝該版本，因此固定通道可能會降級裝置。
:::

### 作業狀態與結果 {#job-states-and-results}

作業列在 [`/cmr/upgrade/job`](../cli-reference/cmr/upgrade/job.md) 選單中，表示一次升級執行。作業會經歷 `scheduled`、`queued`、`waiting devices`、`version check`、`processing` 這些狀態，最後變為 `done` 或 `cancelled`。`success` 計數器為 `upgraded/total`，例如 `6/7`。由升級規則啟動的作業會帶有 `R` 標誌。

由 `/cmr/device/upgrade` 為按編號選擇的裝置啟動的作業沒有 `labels`，並且僅當指定了版本時才顯示 `channel`。其裝置由 [`/cmr/upgrade/job/show-devices`](../cli-reference/cmr/upgrade/job/show-devices.md) 列出。

:::note
`success` 計數器只統計任務實際升級的裝置。任務無法升級的受覆蓋裝置會保持 `pending` 狀態並帶有錯誤：當其已處於目標版本或已停用，或者固定版本的軟體包既不在 `packages-directory` 中也不在更新伺服器上時，為 **no upgrade available**，而當其未連線到伺服器時，為 **disconnected**。

此類裝置會被計為失敗。使用 `fail-policy=stop` 時，它會在任何裝置升級之前停止任務，其他裝置會保持 `pending` 狀態，並帶有 **skipped by fail-policy**。請使用 `fail-policy=continue`，或者只選擇已連線且有可用升級的裝置，例如透過 `/cmr/device/upgrade`。
:::

當伺服器自行升級時，其作業以 `done` 結束，結果為 `0/1`，並且 `show-devices` 會讓伺服器保持 `rebooting` 狀態，即使升級成功也是如此：伺服器會在記錄結果之前重啟。請在 `/system/resource` 中或 `/cmr/device` 中伺服器自身條目的 `version` 中檢查已安裝版本。目前，此類作業的 `start-time` 以 UTC 顯示。

可以透過移除作業來取消它。使用 [`/cmr/upgrade/job/remove`](../cli-reference/cmr/upgrade/job.md) 移除作業。移除已排程或已排隊的作業會將其標記為 `cancelled`，且該作業仍保留在列表中。移除處理中的作業會停止此次執行，並將剩餘裝置標記為 `cancelled`。中斷的安裝仍有可能在裝置重啟後完成。移除 `cancelled` 作業會將其從列表中刪除。

### 策略與故障處理 {#strategy-and-failure-handling}

`strategy` 控制覆蓋的裝置如何升級。可選的 `order` 會將覆蓋的裝置拆分為標籤組，並定義處理這些組的順序。

- **Parallel** - 同時升級所有覆蓋範圍內的裝置。與 `order` 結合使用時，同一標籤組內的裝置一起升級，各組按照 `order` 給出的順序依次處理。
- **Sequential** - 逐個升級裝置，並等待每個裝置完成。與 `order` 結合使用時，`order` 中的各組依次處理，組內裝置則一次升級一個。

`fail-policy` 控制當裝置失敗時會發生什麼：

- `continue` - 跳過失敗的裝置，繼續處理其餘裝置。
- `stop` - 在第一次失敗時停止整個升級。任務不會繼續處理剩餘裝置，也不會繼續處理 `order` 中的下一個標籤組。這是預設值。
- `continue-order` - 跳過失敗的裝置，並繼續處理 `order` 中的下一個標籤組。需要 `order`，它列出要逐組處理的標籤。沒有它時，`continue-order` 不被接受。失敗裝置所在組的處理方式取決於 `strategy`：
  - **sequential** - 跳過該組的其餘部分（尚未啟動的裝置保持 `pending`），任務繼續處理 `order` 中的下一組。
  - **parallel** - 只放棄失敗的裝置。同一組中已在進行的裝置會完成，任務繼續處理 `order` 中的下一組。

#### 按網路順序升級 {#upgrade-in-network-order}

裝置在升級期間會重啟。重啟時，透過該裝置連線到伺服器的裝置也會失去與伺服器的連線。如果先升級交換器或閘道器，而後升級其背後的裝置，這些裝置會在任務中途斷開。伺服器不會根據網路拓撲推導順序：順序由 `order` 定義。

根據裝置在網路中的位置為其設定標籤，並在 `order` 中按從網路邊緣到伺服器的方向列出這些標籤。例如，接入點標籤為 `ap`，它們連線的交換器標籤為 `switch`，閘道器標籤為 `gw`：

```ros
[admin@MikroTik] > /cmr/upgrade/add name=fleet labels=ap,switch,gw order=ap,switch,gw channel=stable strategy=sequential fail-policy=stop
```

- `order=ap,switch,gw` 先升級接入點，然後升級交換器，最後升級閘道器。
- `strategy=sequential` 一次升級一個裝置，因此網路一次只有一部分會重啟。
- `fail-policy=stop` 在裝置失敗時停止任務，且發生在透過該裝置連線的裝置被升級之前。覆蓋範圍內已是最新狀態或未連線的裝置也會計為失敗，正如“任務狀態和結果”部分中的註釋所述。

在裝置群的任務完成後，再升級 CMR 伺服器本身，可使用其自身的規則或使用 `/cmr/device/upgrade`。

### 備註 {#notes}

- 刪除升級規則不會取消其已啟動或已排隊的作業。使用 `/cmr/upgrade/job/remove` 顯式取消作業。
- [`/cmr/upgrade/show-devices`](../cli-reference/cmr/upgrade/show-devices.md) 和 [`/cmr/upgrade/job/show-devices`](../cli-reference/cmr/upgrade/job/show-devices.md) 都會列出規則或作業的每裝置覆蓋範圍和狀態。它們會顯示每裝置備註，例如前幾節中描述的“upgrade available”和“no upgrade available”狀態。
- 示例告警規則會使用 `cmr` 主題將每次裝置升級的結果寫入日誌，例如 `<device> has successfully upgraded to version <version>` 或 `<device> failed to upgrade from <version> to <version>, error: <reason>`，並在裝置的升級通道為其提供新版本時記錄 `<device> has new version available`。告警規則的“示例規則”部分描述了它們。

## 告警規則 {#alert-rules}

告警規則定義條件（何時觸發）和操作（要做什麼）：寫入日誌訊息、執行 RouterOS 指令碼、傳送 HTTP 請求，或組合這些操作。規則透過 `labels` 選擇裝置，並在 CMR 伺服器上執行其操作。在 [`/cmr/alert`](../cli-reference/cmr/alert.md) 選單中管理規則。

配置的條件決定規則是**狀態告警**還是**事件告警**。狀態告警在其條件滿足期間保持活動狀態。事件告警會為每個匹配的發生執行其操作，並且從不保持活動狀態。

| 行為 | 狀態告警 | 事件告警 |
| --- | --- | --- |
| 表示 | 一個持續中的狀況，例如高 CPU 使用率。 | 已經發生的事情，例如匹配的日誌訊息。 |
| 評估 | 當新的裝置資料到達或定時器執行時。 | 當事件發生時。 |
| 操作執行 | 在告警變為活動狀態時執行一次；僅在其清除並再次變為活動狀態後再次執行。 | 對每個匹配的發生立即執行。 |
| 活動告警和儀表板計數器 | 活動期間保持可見並計入計數。 | 不會作為活動告警出現，也不會加入活動告警計數器。 |
| 每條規則的條件 | 多個狀態條件，使用邏輯 AND 組合。 | 最多一個事件條件。 |

### 示例規則 {#example-rules}

伺服器附帶示例規則，並用註釋 `example` 標記。它們包括 CPU 使用率高於 95%、記憶體使用率高於 90%、升級失敗和成功、可用升級、未配對裝置連線以及重啟的規則。每條規則都會寫入一條日誌訊息，例如 `[device] has successfully upgraded to version [version]` 或 `[device] rebooted`，因此無需進一步配置，日誌就會記錄這些事件。可以像自己的規則一樣更改、停用或刪除它們。

`upgrade available` 示例規則使用 `[upgrade-version]` 寫入其訊息，而只有升級完成事件會填充該佔位符，因此記錄的日誌訊息以 `unknown` 結尾。在你自己的規則中，使用 `[available-version]` 表示提供的版本。

### 建立告警規則 {#create-an-alert-rule}

規則至少需要一個條件和一個動作。例如，建立一個狀態告警，當任意裝置的 CPU 負載升至 95% 以上時記錄一條警告：

```ros
[admin@MikroTik] > /cmr/alert/add name=cpu-load labels=all cpu-above=95 action.log="[device] CPU usage is above 95% ([cpu-usage]%)" action.log-topics=cmr,warning severity=high category=performance
[admin@MikroTik] > /cmr/alert/print where name=cpu-load
11  name="cpu-load" labels=all cpu-above=95
    action.log="[device] CPU usage is above 95% ([cpu-usage]%)"
    .log-topics=cmr,warning severity=high category=performance devices=9
    devices-on=0 fired=0 action-failures=0
```

`devices` 值統計由規則的 `labels` 選中的裝置數量。`devices-on` 值統計具有活動狀態告警的裝置數量，`fired` 統計規則已觸發的次數。此示例在裝置開始滿足 CPU 條件時記錄一次日誌。當條件持續成立時，該裝置仍會計入 `devices-on`，但不會重複記錄日誌訊息。

### 條件 {#conditions}

規則透過 `labels` 選擇其適用的裝置，這些 labels 與 CMR 中使用的相同。[`/cmr/alert`](../cli-reference/cmr/alert.md) CLI 參考列出了每個條件和引數。

#### 狀態告警 {#state-alerts}

狀態條件描述持續為真或為假的情況。當新的裝置資料到達時（例如儀表板統計資訊或健康讀數），或在定時器觸發時，CMR 會重新評估這些條件。多個狀態條件可以組合在一個規則中：僅當所有條件都匹配時，告警才處於活動狀態（邏輯與）。例如，`hdd-above=80 hdd-below=95` 匹配從 80% 到 95%（不包括 95%）的磁碟使用率。對於二選一的情況，請建立兩個規則。

動作在告警變為活動狀態時執行一次。隨後，告警會保持可見並在儀表板中計數，直到其條件不再匹配。僅當告警清除並再次變為活動狀態後，動作才會再次執行。例如，CPU 規則的活動告警計數為五，表示有五臺裝置滿足 CPU 條件，而不是已發生五次 CPU 事件。

狀態條件包括：

- **使用閾值** - `cpu-above` 和 `cpu-below`、`mem-above` 和 `mem-below`，以及 `hdd-above` 和 `hdd-below` 將 CPU、RAM 或磁碟使用率與某個百分比進行比較。
- **健康感測器** - `health-above` 和 `health-below` 將健康感測器與某個值進行比較。`health-value` 指定感測器名稱，並與 `/system/health/print` 中的名稱匹配（例如 `cpu-temperature`）。規則只會在報告該感測器的裝置上比較該感測器；沒有該感測器的裝置會被忽略。等於 `above` 條件閾值的值也會觸發規則；`below` 條件僅對嚴格低於閾值的值觸發。
- **可用性** - `connected` 匹配裝置是已連線還是已斷開。`disconnected-more-than` 匹配斷開時間超過給定時間的裝置。
- **可用升級** - `upgrade-available` 在裝置有更新的 RouterOS 版本可用時匹配。

#### 事件告警 {#event-alerts}

事件條件描述單次發生的事件。規則會對每個匹配的事件立即執行其操作。事件告警從不保持啟用狀態，因此它們不會在儀表板中顯示為活動告警，也不會計入 `devices-on`。一條規則最多隻能包含一個事件條件。

例如，一條匹配的日誌訊息可以使 CMR 寫入一條日誌條目、執行指令碼或傳送 HTTP 請求。該訊息不會建立需要稍後清除的持久告警狀態。另一條匹配的訊息會再次執行這些操作。

事件條件包括：

- **介面** - `interface-change` 在介面變為 `running` 或 `not-running`，或者被 `added` 或 `removed` 時觸發。可選地透過 `interface-type`（`ethernet`、`wifi` 或 `bridge`）進行過濾。目前，在接入點上停用或啟用 CAPsMAN 管理的 WiFi 介面不會觸發 `interface-type=wifi` 規則，因為該介面會保持執行狀態。其 `running` 和 `not-running` 變化（例如接入點重啟期間）會觸發該規則。
- **裝置升級** - `upgrade-done` 在裝置升級完成時觸發。可選擇成功的升級、失敗的升級，或兩者都選。
- **升級任務** - `upgrade-job-done` 在多裝置升級任務整體完成時觸發。可選擇成功的任務、失敗的任務，或兩者都選。
- **重啟** - `rebooted` 在裝置重啟時觸發，包括重啟是升級的一部分或來自 `reboot` 命令的情況。
- **未配對的連線** - `unpaired-device-connected` 在未配對裝置連線時觸發。
- **日誌行** - `log-topics` 和 `log-regex` 定義一個日誌訊息事件條件，匹配所配置的主題和訊息正則表示式。CMR 會自動指示裝置轉發匹配的日誌訊息。轉發的訊息也會出現在伺服器的日誌中，其自身的主題中會新增 `cmrclnt` 主題，例如 `cmrclnt,script,info`。匹配的值可透過 `[message]` 和 `[message-topics]` 獲取。

### 裝置與系統範圍 {#device-and-system-scope}

告警範圍與狀態/事件之分是相互獨立的：

- **裝置警報** 適用於每個受管裝置。大多數警報具有裝置範圍。每個裝置獨立跟蹤狀態警報，統計資訊會區分規則選擇了多少裝置，以及有多少裝置激活了該警報。裝置事件（例如 `upgrade-done`）會為觸發它們的單個裝置執行操作。
- **系統警報** 與 CMR 伺服器相關，而不是與單個受管裝置相關。例如，`upgrade-job-done` 是系統事件警報：它報告整個多裝置升級作業的結果，並且沒有單個裝置上下文。

### 操作 {#actions}

當規則觸發時，它會執行已設定的每個操作：

- `action.log` 搭配可選的 `action.log-prefix` 和 `action.log-topics`，會向 CMR 日誌寫入一條訊息。預設主題為 `cmr,info`；對於日誌行條件，則為 `cmr,warning`。對於日誌行條件，訊息以傳送該日誌行的裝置開頭，格式為 `identity|board|address:`，因此僅 `[message]` 就足以作為訊息文字，例如 `action.log="[message]"`。
- `action.script` 會執行一個指定的系統指令碼，`action.script-vars` 會向它提供觸發該警報的裝置所對應的值。指令碼必須允許自身以縮減後的許可權執行（`dont-require-permissions=yes`），否則該操作會記錄“not enough permissions”。
- `action.http-url`、`action.http-method`、`action.http-body` 和 `action.http-headers` 會呼叫 HTTP 或 HTTPS webhook。請求體中的佔位符會按裝置替換。該呼叫本身不會設定 `Content-Type` 標頭，因此當接收方需要時，請透過 `action.http-headers` 新增一個（例如為 JSON 正文使用 `Content-Type: application/json`）。失敗的呼叫會以 `warning` 寫入 `cmr` 主題，並計入 `action-failures`，例如 `alert "name" HTTP action failed: request failed: Connection refused`。當伺服器的裝置模式不允許 `fetch` 時，該 webhook 也能正常工作。

### 操作文字中的變數 {#variables-in-action-text}

操作文字支援 `[variable]` 展開，例如 `[identity]`、`[severity]` 和 `[alert-name]`。佔位符會替換為來自警報及其裝置或事件上下文的值。當名稱列在 `action.script-vars` 中時，由 `action.script` 觸發的指令碼也可使用相同的值（例如 `action.script-vars="device,version"` 會在指令碼中設定 `$device` 和 `$version`）。可用變數取決於觸發警報的內容。

**裝置變數** 對於每個裝置警報都可用，來自觸發該警報的裝置：

| 佔位符 | 值 |
| --- | --- |
| `[device]` | 裝置標識和地址（`identity@address`）。當地址未知時，僅使用標識，例如對於控制器本身。 |
| `[identity]`, `[address]`, `[board]`, `[version]` | 裝置標識、地址、板卡和 RouterOS 版本。 |
| `[arch]`, `[serial]` | 裝置架構和序列號。 |
| `[packages]` | 已安裝軟體包的逗號分隔列表。 |
| `[labels]` | 使用者標籤和自動標籤的逗號分隔列表。 |
| `[state]` | 裝置狀態，例如配對狀態或升級狀態。對於已配對且沒有進行中操作的裝置，為空。 |
| `[available-version]` | 裝置可用的較新 RouterOS 版本，或 `unknown`。 |
| `[upgrade-state]` | 當前升級進度或結果，或 `unknown`。 |
| `[cpu-usage]`, `[mem-usage]`, `[hdd-usage]` | CPU、RAM 和磁碟使用率（百分比），或在裝置連線後上報它們之前為 `unknown`。 |
| `[<sensor>]` | 規則指定的健康感測器的當前讀數，例如 `[cpu-temperature]`。 |

**事件變數** 在規則的事件條件匹配時可用：

| 佔位符 | 值 |
| --- | --- |
| `[iface-name]`、`[iface-type]`、`[iface-change]` | interface-change 條件的介面名稱、型別和變更（`running`、`not-running`、`added` 或 `removed`）。 |
| `[upgrade-version]`、`[upgrade-error]`、`[upgrade-state]` | 由 upgrade-finished 條件報告的版本、錯誤和升級最終狀態。`[upgrade-error]` 是裝置未升級的原因，例如 `no upgrade available`，升級成功後將為空。`[upgrade-state]` 是裝置在作業中的最終狀態，例如 `done`，或者對於作業未升級的裝置為 `pending`。 |
| `[message]`、`[message-topics]` | log-line 條件的匹配日誌行的訊息和主題。 |
| `[job-device-count]`、`[job-success-count]` | upgrade-job-finished 事件的總裝置數和成功升級的裝置數。 |
| `[job-start-time]`、`[job-end-time]`、`[job-run-time]` | 已完成作業的開始時間和結束時間，例如 `2026.10.06-14:20:36`，以及其持續時間（秒）。 |

:::note
upgrade-job-finished 事件是一個沒有裝置上下文的系統事件，因此上表中的裝置變數對它不可用。其他事件條件會針對裝置觸發，裝置變數可與事件變數一起使用。
:::

**告警變數**對每個告警都可用，無論是什麼觸發了它：

| 佔位符 | 值 |
| --- | --- |
| `[alert-name]` | 配置的規則名稱，或根據條件生成的名稱。 |
| `[severity]`、`[category]` | 規則嚴重性和逗號分隔的類別。 |
| `[alert-users]` | 告警適用的裝置數量。 |
| `[alert-fired-count]` | 告警已觸發的次數。 |
| `[action-fail-count]` | 失敗的操作執行次數。 |

不適用於某條規則的佔位符會呈現為 `unknown`。值不可用的佔位符會呈現為 `(empty)`，例如控制器自身的 `[address]`。

### 規則如何觸發 {#how-a-rule-fires}

新建的狀態告警會立即對每個已配對且已滿足其條件的裝置觸發。當裝置斷開連線時，狀態告警預設會保留該裝置的狀態；設定 `reset-on-disconnect=yes` 可在斷開連線時清除狀態，以便裝置在重新連線後仍滿足條件時再次觸發該規則。狀態告警僅針對已配對裝置進行評估。事件告警沒有需要重設的持久狀態，並且會在每次匹配發生時觸發，包括 `unpaired-device-connected` 的未配對連線。

當伺服器上的 CMR 重啟時，例如在重啟或更改 `packages-directory` 之後，它會再次評估狀態告警：仍然匹配的告警會重新變為活動狀態並執行其操作。更改已啟用的規則（即使只更改其註釋）會對該規則產生相同效果：其狀態告警會在匹配的裝置上重新變為活動狀態並執行其操作。其 `fired` 計數器會從零重新開始。

每條規則都有一個 `severity`（`critical`、`high`、`medium` 或 `low`，預設 `medium`）和一個 `category`，後者由控制器根據規則的條件分配（例如 `performance`、`availability` 或 `version`）；類別可以更改。只讀值描述規則的狀態：

- `devices` - 由規則標籤選中的裝置數量。
- `devices-on` - 具有活動狀態告警的裝置數量。事件發生不會增加此計數。
- `fired` - 規則觸發的總次數，包括事件發生次數。
- `action-failures` - 動作失敗的次數。

### 測試並檢查規則 {#test-and-inspect-a-rule}

- [`test`](../cli-reference/cmr/alert/test.md) 立即執行規則的動作，並將佔位符替換為 `[placeholder]` 值，以驗證動作是否正常工作。目前，每次測試執行也會計入規則的 `fired` 值。
- [`show-devices`](../cli-reference/cmr/alert/show-devices.md) 列出其上規則狀態告警處於活動狀態的裝置。事件告警從不保持活動狀態，因此 `show-devices` 不會為其列出任何裝置，而其 `fired` 值改為統計發生次數。
- 由 `action.log` 寫入的訊息會出現在路由器日誌中規則所設定的主題下，因此使用 `/log/print where topics~"cmr"` 讀取它們。

[`/cmr/alert`](../cli-reference/cmr/alert.md) CLI 參考詳細描述了每個引數和只讀值。

## 網路拓撲 {#network-topology}

[`/cmr/layout`](../cli-reference/cmr/layout.md) 選單儲存網路拓撲。拓撲由節點和鏈路組成：[`node`](../cli-reference/cmr/layout/node.md) 將裝置或另一個佈局對映到某個位置，[`link`](../cli-reference/cmr/layout/link.md) 連線兩個節點。可以使用 [`rebuild-links`](../cli-reference/cmr/layout/rebuild-links.md) 從埠資料自動生成鏈路，並可以使用 [`add-devices`](../cli-reference/cmr/layout/add-devices.md) 批次新增裝置。拓撲本身僅在 GUI 中顯示。

自動鏈路根據 `track-topology` 從用戶端獲取的資料構建，因此使用 `rebuild-links` 時請保持 `track-topology=yes`。`rebuild-links` 僅在直接連線的裝置之間建立鏈路。將其他連線（例如透過 VPN 或不是 CMR 用戶端的交換器建立的連線）作為你自己的鏈路新增。自動鏈路會顯示兩端裝置上已連線的埠及其流量計數器和 PoE 狀態。一個節點可以表示另一個佈局（`target-layout`），因此概覽佈局可以顯示並連結各自包含自己裝置的站點或樓宇佈局。節點名稱在所有佈局中必須唯一。

例如，為一個站點建立佈局，新增帶有 `office` 標籤的裝置，並生成它們之間的鏈路：

```ros
[admin@MikroTik] > /cmr/layout/add name=Office
[admin@MikroTik] > /cmr/layout/add-devices [find name=Office] labels=office
[admin@MikroTik] > /cmr/layout/rebuild-links [find name=Office]
```

下方截圖中的拓撲儲存為一個佈局，每個裝置對應一個節點，相連的裝置之間有一條連結：

<center>![](/img/3b99d765d47a187e.webp)</center>
<center>**The image shows an example network topology in the WebFig GUI.**</center>

```ros
[admin@MikroTik] > /cmr/layout/print detail
 0  name="Example" scale=110 file="Floor_0.png"
 1  name="1_floor" file=""

[admin@MikroTik] > /cmr/layout/node/print detail
 0  name="RB5009UPr" layout=Example device=RB5009UPr x=300 y=25
 1  name="CRS354" layout=Example device=CRS354@192.168.255.2 x=308 y=99
 2  name="hAP" layout=Example device=hAP@192.168.1.96 x=285 y=-113
 3  name="hAP-1" layout=Example device=hAP@192.168.2.92 x=636 y=-104
 4  name="cAP ac 1" layout=Example device=cAP ac 1@192.168.2.91 x=628 y=227
 5  name="To_Floor_1" layout=Example target-layout=1_floor x=295 y=159

[admin@MikroTik] > /cmr/layout/link/print
 #   LAYOUT   NODE1      NODE2
 0   Example  CRS354     RB5009UPr
 1   Example  RB5009UPr  hAP
 2   Example  CRS354     hAP-1
 3   Example  CRS354     cAP ac 1
 4   Example  CRS354     To_Floor_1
```

佈局在 `file` 中儲存其名稱、背景圖片的 `scale` 以及圖片本身。節點在佈局中要麼使用 `device` 放置裝置（例如 `RB5009UPr` 或 `cAP ac 1@192.168.2.91`），要麼使用 `target-layout` 放置另一個佈局；`device` 和 `target-layout` 互斥。上方的 `To_Floor_1` 節點會開啟示例中的 `1_floor` 佈局，因此概覽佈局可以顯示並連結整個站點或建築的佈局。

:::info
在 GUI 中，右鍵單擊拓撲圖中的空白位置以建立節點：

- 裝置節點，透過選擇一個裝置來建立，以及
- 佈局節點，透過選擇另一個佈局來建立。

右鍵單擊現有節點以建立到另一個節點的鏈路。也可以在 CLI 中使用 `add`、`node` 和 `link` 命令完成相同操作。
:::

連結連線佈局的兩個節點。由 [`rebuild-links`](../cli-reference/cmr/layout/rebuild-links.md) 建立的連結還會顯示兩臺裝置上的連線埠及其流量計數器和 PoE 狀態：

```ros
[admin@MikroTik] > /cmr/layout/link/print detail where layout=Example
 0  layout=Example node1=CRS354 node2=RB5009UPr
     links=*ether47(poe=waiting-for-load,tx=520,rx=0)--
        *ether2(poe=waiting-for-load,tx=132.0KiB,rx=160.9KiB),
        ether49(,tx=913.0KiB,rx=30.8KiB)--
        ether1(poe=waiting-for-load,tx=350.7KiB,rx=67.5KiB)
 1  layout=Example node1=RB5009UPr node2=hAP
     links=*ether6(poe=powered-on,tx=0,rx=0)--*ether1(,tx=0,rx=0)
```

這裡，`CRS354` 上的 `ether2` 連線到 `RB5009UPr` 上的 `ether1`，並且 `ether6` 向 `hAP` 上的 `ether1` 提供 PoE 供電。埠名前的 `*` 表示兩個埠之間的直接物理連結；`poe=powered-on` 和 `poe=waiting-for-load` 顯示每一側的 PoE 狀態，`tx`/`rx` 顯示流量計數器。僅連線兩個佈局的連結（例如 `CRS354` 與 `To_Floor_1` 之間的連結）不攜帶埠。

節點座標相對於佈局中心，因此 `x=0, y=0` 標記中心，並且允許負值。`x` 向右增大，`y` 向下增大，因此較小的 `y` 會將節點放置在圖上更高的位置：在上方截圖中，`y=-113` 的節點靠近頂部，而 `y=227` 的節點位於底部。`print` 輸出將座標顯示為帶符號數字，例如 `y=-113`。

## 應用流量 {#application-traffic}

CMR 可以從選定的裝置收集應用流量統計資訊。在 [`/cmr`](../cli-reference/cmr.md) 選單中使用 `apptraffic-devices` 設定按標籤選擇裝置，該設定預設選擇帶有 `gateway` 標籤的裝置；隨後伺服器會在選定的裝置上啟用應用流量分類器（`/tool/apptraffic`）：

```ros
[admin@MikroTik] > /cmr set apptraffic-devices=gateway
```

分類器只能看到裝置路由的流量。一個接入點如果在橋接快速路徑中橋接其用戶端的流量，則只能看到自己的流量，例如其 DNS 查詢和管理會話。請選擇路由網路流量的路由器，例如閘道器，以檢視用戶端的應用。

統計資訊在 GUI 的 **CMR > Traffic** 下按應用或按類別顯示，包含最後一分鐘、小時、天和周的流入和流出流量。CLI 檢視（[`/cmr/device/apptraffic`](../cli-reference/cmr/device/apptraffic.md)）列出每個檢測到的應用及其最後一分鐘、小時、天和周的流量。較窄的控制檯會省略不適合顯示的列。

分類器在 **mmips**、**smips** 和 **powerpc** 架構的裝置上不可用。

## WiFi 配置 {#wifi-configuration}

[`/cmr/wifi`](../cli-reference/cmr/wifi.md) 選單定義裝置群的 WiFi 網路，[`/cmr/wifi/radio`](../cli-reference/cmr/wifi/radio.md) 選單定義射頻配置。項會應用到與其 `labels` 匹配的裝置，這與升級和告警規則使用的標籤選擇相同。引數延續 [`/interface/wifi`](../wireless/wifi/index.md) 配置：網路項包含連線性和 `security` 設定，射頻項包含 `configuration` 和 `channel` 設定。項沒有名稱；`labels` 選擇目標裝置，`numbers` 選擇要編輯的項。

### 定義 WiFi 網路 {#define-a-wifi-network}

為帶有 `Group2` 標籤的裝置建立一個網路，該網路廣播 SSID `Office`，使用 WPA2 和 `ccmp` 密碼套件進行認證，並用 VLAN 10 標記用戶端流量：

```ros
[admin@MikroTik] > /cmr/wifi/add labels=Group2 ssid=Office vlan-id=10 security.authentication-types=wpa2-psk security.encryption=ccmp security.passphrase="office-passphrase" comment=office-wifi
```

網路會出現在列表中。組的設定帶有帶點的名稱。在 `print` 輸出中，組名只寫一次，該組的其餘值則以帶前導點的形式寫出：

```ros
[admin@MikroTik] > /cmr/wifi/print
0  ;;; office-wifi
   labels=Group2 ssid="Office" security.encryption=ccmp
   .authentication-types=wpa2-psk vlan-id=10
```

{/* Screenshot placeholder — add `../img/cmr_wifi_network.webp` when the WinBox screenshot is available:
<center>![](../../../../../docs/management-tools/img/cmr_wifi_network.webp)</center>
<center>**該圖顯示在 WinBox GUI 中配置的 WiFi 網路。**</center>

*/}

網路的引數與 [`/interface/wifi`](../wireless/wifi/index.md) 的網路引數相對應：

- `labels` - 應用該網路的裝置。
- `ssid` - 向用戶端廣播的網路名稱。
- `mode` - 執行模式：`ap`、`station`、`station-bridge` 或 `station-pseudobridge`。
- `vlan-id` - 用戶端流量所標記的 VLAN。
- `security.authentication-types` - 認證方式，例如 `wpa2-psk`、`wpa3-psk` 或 `owe`。
- `security.encryption` - 允許的加密演算法，例如 `ccmp` 或 `gcmp`。
- `security.passphrase` - 個人認證型別所用的網路密碼。passphrase 是敏感值，不會出現在 print 輸出中。REST API 會將其返回給擁有 `sensitive` 策略的使用者。

停用網路可在不刪除它的情況下停止應用它。已停用的網路會標記為 `X` 標誌：

```ros
[admin@MikroTik] > /cmr/wifi/set 0 disabled=yes
[admin@MikroTik] > /cmr/wifi/print
Flags: X - DISABLED
 0  X ;;; office-wifi
      labels=Group2 ssid="Office" security.encryption=ccmp
      .authentication-types=wpa2-psk vlan-id=10
```

### 配置 radio {#configure-the-radio}

[`/cmr/wifi/radio`](../cli-reference/cmr/wifi/radio.md) 選單用於設定所選裝置的 radio 引數。一個 radio 項會應用到它所選裝置的每一個 radio 上，因此請用頻段標籤（例如 `+5ghz`）將通道設定限制在單個頻段。若不加頻段標籤，5 GHz 頻率也會被應用到 2.4 GHz radio，後者隨後會因“no available channels”而保持不活動。為帶有 `Group2` 標籤的裝置的 5 GHz radio 設定監管域、radio 鏈和通道：

```ros
[admin@MikroTik] > /cmr/wifi/radio/add labels=Group2,+5ghz configuration.country=Latvia configuration.chains=0,1 channel.band=5ghz-ax channel.frequency=5180 channel.width=20mhz comment=office-radio
```

```ros
[admin@MikroTik] > /cmr/wifi/radio/print
0  ;;; office-radio
   labels=Group2,+5ghz configuration.country=Latvia .chains=0,1
   channel.frequency=5180 .band=5ghz-ax .width=20mhz
```

`configuration` 和 `channel` 組與 [`/interface/wifi`](../wireless/wifi/index.md) 的 radio 引數相對應：`configuration.country` 設定監管域，`configuration.chains` 設定 radio 鏈，而 `channel.band`、`channel.frequency` 和 `channel.width` 設定通道選擇。

[`/cmr/wifi`](../cli-reference/cmr/wifi.md) 和 [`/cmr/wifi/radio`](../cli-reference/cmr/wifi/radio.md) CLI 參考列出了這兩個選單的每個引數。

### 配置如何應用 {#how-the-configuration-is-applied}

在每臺選定的裝置上，WiFi 網路會作為受管條目（標誌 **Y**）寫入裝置的 `/interface/wifi/network` 選單，radio 項則會作為受管條目寫入 `/interface/wifi/network/radio`。受管條目會應用到該項所選擇的 radio：

- 沒有頻段標籤時，網路或 radio 項會應用到所選裝置的每個 radio。新增頻段標籤可選擇某個頻段的 radio：`+2ghz`、`+5ghz` 或 `+6ghz`。例如，`labels=Group2,+5ghz` 僅選擇帶有 `Group2` 標籤的裝置的 5 GHz radio。
- CMR 網路會接管其選擇的 radio，並替換其現有配置，包括由 CAPsMAN 管理的 radio 和具有本地配置的 radio。沒有 CMR 網路選擇的 radio 會保留其配置，因此接入點的 2.4 GHz radio 可以繼續處於 CAPsMAN 管理下，而其 5 GHz radio 由 CMR 配置。
- radio 項僅應用於 CMR 網路也選擇的 radio。
- 在具有 WiFi 7 radio 的裝置上，裝置會為 CMR 網路建立 MLD 介面。
- 受管條目無法在裝置上更改。請在 CMR 伺服器上更改它們。

:::warning
目前，移除或停用 CMR WiFi 網路，或在裝置上停用 CMR 用戶端，都不會恢復射頻的先前配置。射頻會回退到與其匹配的本地 `/interface/wifi/network` 條目，當沒有匹配條目時則保持停用。必須在裝置上重新設定其先前的 CAPsMAN 或每介面配置，因此在將 CMR 網路應用到接入點之前，請匯出該接入點的 WiFi 配置。
:::

### 網橋和 VLAN {#bridge-and-vlan}

目前，CMR WiFi 網路無法選擇網橋，因為 `/cmr/wifi` 沒有 `datapath` 設定。網橋取決於網路的 `vlan-id`：

- 使用 `vlan-id` 時，WiFi 介面會新增到受管 `cmr-bridge`（與 VLAN 配置建立的是同一個網橋），並啟用 VLAN 過濾，且將 `vlan-id` 作為其 PVID。
- 不使用 `vlan-id` 時，WiFi 介面不會新增到任何網橋，用戶端將沒有網路訪問。目前，請為每個 CMR WiFi 網路設定 `vlan-id`。

`cmr-bridge` 在裝置的某個埠加入它之前不會連線到網路的其餘部分。使用 VLAN 配置規則將接入點的上行鏈路埠新增到 `cmr-bridge`，以便上行鏈路承載網路的 VLAN。例如，對於帶有 `office-ap` 標籤的接入點上 VLAN 10 的辦公網路，以 `ether1` 作為上行鏈路：

```ros
[admin@MikroTik] > /cmr/wifi/add labels=office-ap ssid=Office vlan-id=10 security.authentication-types=wpa2-psk,wpa3-psk security.passphrase="office-passphrase"
[admin@MikroTik] > /cmr/vlan/add labels=office-ap port-labels=ether1 vlan-ids=10 role=trunk comment=ap-uplink
```

交換器埠和上聯鏈路另一端的路由器必須攜帶帶標籤的 VLAN 10。路由器為該網路提供 IP 地址分配、DHCP 和防火牆規則；CMR 不配置這些內容。

:::warning
當接入點的上行鏈路加入 `cmr-bridge` 時，它會離開該接入點先前的網橋，並且透過該網橋的管理訪問會停止。`trunk` 埠還只接受帶 VLAN 標記的幀，因此上行鏈路上的未標記流量會被丟棄。在將接入點的上行鏈路新增到 `cmr-bridge` 之前，請規劃該接入點的管理訪問。
:::

## VLAN 配置 {#vlan-provisioning}

[`/cmr/vlan`](../cli-reference/cmr/vlan.md) 選單會在選定的 CMR 用戶端上建立網橋和 VLAN 配置。規則透過 `labels` 選擇裝置，透過 `port-labels` 選擇埠（裝置介面名，例如 `ether1`，或在 `/cmr/device` 中分配給埠的埠標籤，例如 `uplink`），定義 `vlan-ids`（逗號分隔列表或範圍，例如 `10,20` 或 `10-20`），併為每個埠分配一個 `role`：`access`（預設）或 `trunk`。`port-labels` 引數為必填項，因此規則始終會指明其配置的埠，不會意外應用到裝置的所有埠。

在選定的裝置上，規則會建立一個啟用了 VLAN 過濾的專用 `cmr-bridge` 網橋，並將選定的埠移入其中：

- `access` 埠屬於單個 VLAN，即 `vlan-ids` 中的第一個 VLAN，該 VLAN 被設定為埠的 PVID。它傳輸不帶標籤的幀。在用戶端上，當埠有鏈路時，該 VLAN 會作為動態無標籤條目出現在網橋的 VLAN 表中。
- `trunk` 埠傳輸 `vlan-ids` 中的每個 VLAN，使用 802.1Q 頭打標籤，並且只接受帶 VLAN 標籤的幀。

一條規則可以選擇多個埠；每個選定的埠都以相同方式配置。`trunk` 埠只接受帶 VLAN 標籤的幀，即使 `vlan-ids` 中包含 VLAN 1 也是如此，因此一個埠不能同時傳輸無標籤和帶標籤的 VLAN。目前，當多條規則選擇同一埠時，第一條規則生效，其他規則會被忽略且不會給出警告。

例如，為帶有 `office` 標籤的裝置提供一個 VLAN 10 上的 access 埠和一個承載 VLAN 10 和 20 的上聯埠：

```ros
[admin@MikroTik] > /cmr/vlan/add labels=office port-labels=ether5 vlan-ids=10 role=access comment=office-access
[admin@MikroTik] > /cmr/vlan/add labels=office port-labels=ether6 vlan-ids=10,20 role=trunk comment=office-uplink
```

```ros
[admin@MikroTik] > /cmr/vlan/print
0  ;;; office-access
   labels=office port-labels=ether5 vlan-ids=10 role=access

1  ;;; office-uplink
   labels=office port-labels=ether6 vlan-ids=10,20 role=trunk
```

刪除或停用規則會撤銷其配置：選定的埠會恢復到之前的網橋和埠配置，當最後一條使用 `cmr-bridge` 的規則被刪除時，`cmr-bridge` 也會被刪除。

:::warning
配置下發會將選定的埠移入受管理的 `cmr-bridge`，這會斷開該埠當前的流量，並且如果選中的是管理埠或上行鏈路埠，還可能切斷裝置的管理訪問。`port-labels` 引數是必需的，因此規則始終會指明其更改的埠，但沒有 `labels` 的規則仍會將這些埠應用到所有連線的裝置，包括 CMR 控制器本身；應用此類規則可能會斷開整個裝置群以及控制器自身的管理訪問。也要保持裝置選擇明確。停用或移除規則會恢復先前的配置，前提是裝置仍可從控制器訪問；同時配置裝置自身上行鏈路的規則可能會切斷該鏈路，隨後會保留 `cmr-bridge`，直到與裝置的 CMR 連線重新建立，例如透過重新啟用 CMR 用戶端。
:::
