---
sidebar_key: "developer-guides/rest-api"
sidebar_position: 2
title: "REST API"
sidebar_label: "REST API"
description: "RouterOS REST API：使用最小許可權使用者啟用 HTTPS 訪問，透過 GET、PUT、PATCH 和 DELETE 讀取和更改配置，使用 POST 執行任意控制檯命令，在 60 秒限制和每使用者會話範圍內工作，並在此基礎上構建指令碼、整合和儀表板。"
tags:
  - 'api'
  - 'management'
  - 'rest-api'
source: https://manual.mikrotik.com/docs/developer-guides/rest-api
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

REST API 提供對 RouterOS 命令列的 HTTP 訪問。每個選單都是 `/rest` 下的一個 URL：`/ip/address` 選單是 `https://192.168.88.1/rest/ip/address`。JSON 請求可以讀取、建立、更改和刪除配置，並執行任何控制檯命令。指令碼、監控系統、自動化工具和 Web 儀表板使用它來管理路由器，無需 WinBox 或 SSH。

REST API 是 [API](./api/index.md) 的 JSON 封裝：Web 伺服器以經過身份驗證的使用者身份登入 API，並將每個請求作為 API 命令執行。因此，REST API 提供與控制檯相同的選單、引數和許可權，[CLI 參考](../cli-reference/index.md) 對它們進行了描述。Web 伺服器透過 `www-ssl` 服務（`https://<router>/rest`）以 HTTPS 提供 REST API，並透過 `www` 服務（`http://<router>/rest`）以 HTTP 提供 REST API。

使用 cURL 的第一個請求。它使用 [設定 HTTPS](#set-up-https) 中的 `rest-ca.crt` 檔案，並詢問 [建立 REST 使用者](#create-a-rest-user) 中 `monitoring` 使用者的密碼：

```bash
curl --cacert rest-ca.crt -u monitoring -G \
    https://192.168.88.1/rest/system/resource \
    -d .proplist=board-name,cpu-load,free-memory,uptime
```

```json
{"board-name":"hAP ax^2","cpu-load":"7","free-memory":"687116288","uptime":"1d7h44m20s"}
```

任何 HTTP 用戶端都可以使用：cURL、wget、程式語言的 HTTP 庫，以及另一臺 RouterOS 裝置上的 [`/tool/fetch`](../system-information-and-utilities/fetch.md)。

## 啟用 REST 訪問 {#enable-rest-access}

REST 用戶端需要路由器上具備三樣東西：執行中的 Web 服務（HTTPS 使用 `www-ssl`，HTTP 使用 `www`）、用於 HTTPS 的證書，以及其所在組允許使用 REST API 的使用者。

### 設定 HTTPS {#set-up-https}

REST API 使用 [HTTP 基本身份驗證](https://en.wikipedia.org/wiki/Basic_access_authentication) 進行身份驗證：每個請求都攜帶使用者名稱和密碼。透過 HTTP 時，任何能看到流量的人都可以讀取它們。僅在攻擊者無法訪問的網路上或加密隧道內使用 HTTP，其他所有地方都使用 HTTPS。

要使用自己的證書頒發機構提供 HTTPS，請建立並簽署該機構以及路由器地址的伺服器證書，匯出該機構的證書，並將伺服器證書分配給 `www-ssl`。在路由器上的終端（WinBox Terminal 或 SSH）中執行這些命令：

```ros
/certificate/add name=rest-ca common-name=rest-ca \
    key-usage=key-cert-sign,crl-sign days-valid=3650
/certificate/sign rest-ca
:delay 3s
/certificate/add name=rest-https common-name=192.168.88.1 \
    subject-alt-name=IP:192.168.88.1 days-valid=365
/certificate/sign rest-https ca=rest-ca
:delay 3s
/certificate/export-certificate rest-ca file-name=rest-ca
/ip/service/set www-ssl certificate=rest-https disabled=no
```

在 `sign` 報告 `done` 後，已簽署的證書需要片刻才能供其他命令使用；`:delay` 行會等待這一點。沒有它們時，下一條命令可能會失敗並顯示 `input does not match any value of ca`（或 `of certificate`）；請再次執行它。

將 `rest-ca.crt` 從路由器檔案複製到用戶端（例如使用 `scp admin@192.168.88.1:rest-ca.crt .`），並讓用戶端信任它：cURL 中使用 `--cacert rest-ca.crt`，Python 中使用 `verify="rest-ca.crt"`。在 URL 中按證書命名的方式訪問路由器，這裡是 `192.168.88.1`；用戶端會拒絕為其他名稱或地址頒發的證書。伺服器證書有效期為一年（`days-valid=365`）；請在過期前建立新證書。

對於具有公共 DNS 名稱的路由器，可以改用 Let's Encrypt 證書；請參閱 [證書](../authentication-authorization-accounting/certificates.md)。如需快速測試，cURL 中的 `-k` 和 wget 中的 `--no-check-certificate` 會跳過檢查，同時也會跳過證書提供的保護。

`www-ssl` 接受 TLS 1.0、1.1 和 1.2。設定 `tls-version=only-1.2` 以拒絕較舊版本。沒有證書（`certificate=none`）時，`www-ssl` 僅提供匿名密碼套件，瀏覽器和 cURL 不接受這些套件，因此 HTTPS 請求會失敗。有關所有服務設定，請參閱 [`/ip/service`](../cli-reference/ip/service/index.md)。

### 建立 REST 使用者 {#create-a-rest-user}

REST API 代表使用者登入 API，因此使用者所在組需要同時具有 `rest-api` 和 `api` 策略。它還需要使用者所執行操作對應的策略：讀取需要 `read`，更改配置需要 `write`，`ping` 需要 `test`，寫入檔案（`export` 到檔案）需要 `ftp`，使用 `/file/read` 讀取檔案需要 `ftp` 和 `test`，檢視密碼和金鑰需要 `sensitive`，更改自己的密碼需要 `password`。預設的 `read`、`write` 和 `full` 組包含 `api` 和 `rest-api`，但也包含 `reboot`、`sensitive` 以及用於 WinBox、SSH 和 WebFig 登入的策略，因此請為 REST 用戶端建立自己的組。

為每個用戶端提供自己的使用者，並僅授予其所需的策略。監控系統或儀表板只讀取：

```ros
/user/group/add name=rest-read policy=read,api,rest-api
/user/add name=monitoring group=rest-read \
    password="use-a-long-random-password"
```

本頁中更改配置的示例使用 `admin`。對於指令碼，請建立具有其任務所需策略的使用者，例如用於阻止地址的 `read,write,api,rest-api`，或用於配置備份的 `read,write,ftp,test,api,rest-api`。

`/user/group/add` 會撤銷它未列出的每個策略。`/user/group/set` 僅更改它列出的策略，因此使用 `!` 撤銷策略，例如 `policy=!write`。有關所有策略，請參閱 [`/user/group`](../cli-reference/user/group.md) 和 [使用者](../authentication-authorization-accounting/user.md)。

### 限制訪問 {#restrict-access}

預設防火牆會丟棄不是來自 `LAN` 介面列表的連線，這也使 REST API 與網際網路隔離。請保持這樣做：透過諸如 [WireGuard](../virtual-private-networks/wireguard.md) 之類的 VPN 訪問遠端路由器，而不是將 Web 服務開放到網際網路。請參閱 [保護路由器安全](../getting-started/securing-your-router.md)。REST API 不使用 `api` 服務：停用 `api` 或限制其 `available-from` 不會影響 REST。

限制哪些用戶端可以使用該服務（如果 VPN 用戶端使用 REST，請包括它們的地址），並關閉透過 HTTP 的 REST API：

```ros
/ip/service/set www-ssl available-from=192.168.88.0/24
/ip/service/webserver/set rest-plain=no
```

- 使用 `available-from` 時，路由器會關閉來自其他地址的連線而不為其提供服務。埠仍然可見，因此請使用防火牆抵禦不受信任的網路。`available-from` 適用於該服務的每個使用者；要將一個使用者繫結到一個用戶端，請改為設定該使用者的 `address`，例如 `/user/set monitoring address=192.168.88.10/32`。來自其他地址的請求隨後會得到 `401 Unauthorized`。
- `rest-plain=no` 會關閉透過 HTTP 的 REST API（回覆為 `403 Forbidden`），而透過 HTTP 的 WebFig 仍可工作。要完全關閉 HTTP，請停用 `www` 服務。
- 要僅透過 HTTPS 提供 REST API，還需設定 `index-secure=no webfig-secure=no graphs-secure=no`。然後透過 HTTPS 訪問主頁、WebFig、圖表和靜態檔案時會返回 `403 Forbidden`。

有關 Web 伺服器設定，請參閱 [`/ip/service/webserver`](../cli-reference/ip/service/webserver.md)。

## 讀取資料 {#read-data}

`GET` 請求讀取一個選單，類似於控制檯中的 `print`。回覆是記錄列表：

```bash
curl --cacert rest-ca.crt -u monitoring -G \
    https://192.168.88.1/rest/ip/address \
    -d .proplist=.id,address,interface
```

```json
[{".id":"*1","address":"192.168.88.1/24","interface":"bridge"}]
```

要讀取一條記錄，請將其 ID 追加到 URL。在記錄具有名稱的選單中，名稱也可以使用：

```bash
curl --cacert rest-ca.crt -u monitoring -G \
    "https://192.168.88.1/rest/ip/address/*1" \
    -d .proplist=address,network,interface
curl --cacert rest-ca.crt -u monitoring -G \
    https://192.168.88.1/rest/interface/ether1 \
    -d .proplist=name,type,running,mtu
```

```json
{"address":"192.168.88.1/24","interface":"bridge","network":"192.168.88.0"}
{"mtu":"1500","name":"ether1","running":"false","type":"ether"}
```

- ID 以 `*` 開頭。對包含 ID 的 URL 加引號，以免 shell 展開它。按原樣傳送星號：路由器不會解碼 `%2A`。
- 對名稱中的其他保留字元進行編碼，例如將空格編碼為 `%20`，或將資料夾中檔名的斜槓編碼為 `%2F`（`/rest/file/flash%2Fbackup.rsc`）。
- 沒有記錄的選單（例如 `/system/identity` 或 `/ip/dns`）返回一個物件。

查詢引數用於篩選記錄。一條記錄必須匹配每個引數，且值必須完全匹配。例如，具有鏈路的乙太網介面（`running=true` 或 `yes`）：

```bash
curl --cacert rest-ca.crt -u monitoring -G \
    https://192.168.88.1/rest/interface \
    -d type=ether -d running=true -d .proplist=name
```

```json
[{".id":"*5","name":"ether2"}]
```

- `.proplist` 選擇回覆的屬性。對列表的 `GET` 始終包含 `.id`。
- 當沒有記錄匹配時，回覆是空列表 `[]`。
- 對於其他條件（或、非、小於），請在 `print` 命令的正文中使用 `.query`，如 [選擇記錄和屬性](#select-records-and-properties) 中所示。在 URL 中，`.query` 不是查詢。

## 更改配置 {#change-the-configuration}

HTTP 方法選擇控制檯命令：

| 方法 | 控制檯命令 | 成功時的回覆 |
| :-- | :-- | :-- |
| `GET` | `print` | `200 OK`，帶有記錄或記錄列表 |
| `PUT` | `add` | `201 Created`，帶有新記錄；`Location` 頭包含其 URL |
| `PATCH` | `set` | `200 OK`，帶有更改後的記錄 |
| `DELETE` | `remove` | `204 No Content`，空正文 |
| `POST` | 任意命令 | `200 OK`，帶有命令的回覆 |

將引數作為 JSON 物件傳送，並帶有 `Content-Type: application/json` 頭。沒有該頭時，路由器會返回 `415 Unsupported Media Type`。

### 建立記錄 {#create-a-record}

對選單執行 `PUT` 會為每個請求建立一條記錄，這裡是在 `guest` 上的一個地址，`guest` 是訪客網路的網橋：

```bash
curl --cacert rest-ca.crt -u admin -X PUT \
    https://192.168.88.1/rest/ip/address \
    -H "Content-Type: application/json" \
    --data '{"address":"192.168.99.1/24","interface":"guest"}'
```

```json
{".id":"*18","actual-interface":"guest","address":"192.168.99.1/24","disabled":"false","dynamic":"false","interface":"guest","invalid":"false","network":"192.168.99.0","slave":"false","vrf":"main"}
```

### 更改記錄 {#change-a-record}

對記錄 URL 執行 `PATCH` 會更改正文中的引數並返回整條記錄：

```bash
curl --cacert rest-ca.crt -u admin -X PATCH \
    "https://192.168.88.1/rest/ip/address/*18" \
    -H "Content-Type: application/json" \
    --data '{"comment":"guest network"}'
```

```json
{".id":"*18","actual-interface":"guest","address":"192.168.99.1/24","comment":"guest network","disabled":"false","dynamic":"false","interface":"guest","invalid":"false","network":"192.168.99.0","slave":"false","vrf":"main"}
```

沒有 `write` 策略的使用者執行 `PATCH` 會失敗，返回 `400` 和 `missing or invalid resource identifier`。要在一次請求中更改多條記錄，請向選單的 `set` 命令傳送 `POST`，並用逗號分隔 ID：`{".id":"*12,*13","comment":"imported"}`。

`PATCH` 僅適用於記錄。要更改沒有記錄的選單，例如 `/system/identity`、`/ip/dns` 或 `/ip/service/webserver`，請使用 `POST` 執行其 `set` 命令。`set` 返回空列表：

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/system/identity/set \
    -H "Content-Type: application/json" \
    --data '{"name":"branch-office-1"}'
curl --cacert rest-ca.crt -u monitoring \
    https://192.168.88.1/rest/system/identity
```

```json
[]
{"name":"branch-office-1"}
```

### 刪除記錄 {#delete-a-record}

對記錄 URL 執行 `DELETE` 會刪除它並返回空正文。對同一 ID 第二次執行 `DELETE` 會返回 `404`，這是這兩條命令的唯一輸出：

```bash
curl --cacert rest-ca.crt -u admin -X DELETE \
    "https://192.168.88.1/rest/ip/address/*18"
curl --cacert rest-ca.crt -u admin -X DELETE \
    "https://192.168.88.1/rest/ip/address/*18"
```

```json
{"error":404,"message":"Not Found"}
```

### 值 {#values}

- 回覆將每個值編碼為字串，數字和布林值也是如此（`"true"`、`"false"`）。
- 請求可以將值作為字串傳送，也可以作為 JSON 數字和布林值傳送：`"disabled":"yes"` 和 `"disabled":true` 效果相同。
- 不帶值的命令標誌（例如 `once`、`compact` 或 `as-string`）使用空字串：`"once":""`。
- 控制檯的未命名引數（例如 `/interface/ethernet/monitor ether2` 中的介面）是 `numbers`：`{"numbers":"ether2","once":""}`。

## 執行命令 {#run-commands}

`POST` 執行任何控制檯命令。URL 是選單路徑和命令名，JSON 正文包含命令的引數。例如，要更改經過身份驗證的使用者自己的密碼（該使用者需要 `password` 策略）：

```text
POST https://192.168.88.1/rest/password
{"old-password":"old","new-password":"N3w","confirm-new-password":"N3w"}
```

回覆的結構與 [API](./api/index.md) 回覆相同：

- 返回記錄的命令（`print`、`ping`、`monitor-traffic`）返回物件列表，每條記錄一個物件（`!re` 語句）。
- 在 `!done` 語句中返回資料的命令會返回包含該資料的物件，通常是 `ret` 中的值：`add` 的新記錄 ID、`print count-only` 的記錄數、帶有 `as-string` 的 `execute` 的輸出。
- 不返回任何內容的命令返回空列表 `[]`，對於某些命令則返回 `[{}]`。
- 報告進度的命令（`bandwidth-test`、`fetch`、`check-for-updates`）會在 `.section` 中對其回覆編號。

回覆在命令結束時到達：REST API 不會流式傳輸輸出。

### 選擇記錄和屬性 {#select-records-and-properties}

兩個特殊鍵選擇命令返回的內容：`.proplist` 選擇屬性，適用於任何返回記錄的命令；`.query` 選擇記錄，適用於 `print`。`.proplist` 是逗號分隔的字串或字串列表：

```bash
curl --cacert rest-ca.crt -u monitoring -X POST \
    https://192.168.88.1/rest/ip/address/print \
    -H "Content-Type: application/json" \
    --data '{".proplist":"address,interface"}'
```

```json
[{"address":"192.168.88.1/24","interface":"bridge"}]
```

`.query` 是 API 查詢詞的列表，不帶前導 `?`，按棧求值：`type=ether` 匹配值，`<l2mtu=1600` 和 `>` 進行比較，`#|!` 用 OR 組合前兩個結果並對結果取反。例如，`{".query":["type=ether","type=vlan","#|!"]}` 是以下 API 語句：

```text
/interface/print
?type=ether
?type=vlan
?#|!
```

[API 查詢](./api/index.md#queries) 部分解釋了查詢詞和運算子。以下請求返回既不是乙太網介面也不是 VLAN 介面的介面：

```bash
curl --cacert rest-ca.crt -u monitoring -X POST \
    https://192.168.88.1/rest/interface/print \
    -H "Content-Type: application/json" \
    --data '{".proplist":"name,type",
        ".query":["type=ether","type=vlan","#|!"]}'
```

```json
[{"name":"bridge","type":"bridge"},{"name":"guest","type":"bridge"},
{"name":"lo","type":"loopback"},{"name":"wifi1","type":"wifi"},
{"name":"wifi2","type":"wifi"}]
```

`count-only` 則返回記錄數：

```bash
curl --cacert rest-ca.crt -u monitoring -X POST \
    https://192.168.88.1/rest/ip/address/print \
    -H "Content-Type: application/json" --data '{"count-only":""}'
```

```json
{"ret":"1"}
```

### 將命令保持在 60 秒以內 {#keep-commands-within-60-seconds}

路由器會結束執行 60 秒的請求，並返回 `400 Bad Request`，詳細資訊為 `Session closed`。持續時間引數不會延長該限制：要求執行一小時的頻寬測試仍會在 60 秒後結束。

一直執行直到你停止的命令，例如不帶 `count` 的 `ping`、`monitor` 命令以及不帶 `duration` 的 `bandwidth-test`，總是會觸及該限制：

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/ping \
    -H "Content-Type: application/json" \
    --data '{"address":"192.168.88.10"}'
```

```json
{"detail":"Session closed","error":400,"message":"Bad Request"}
```

使用引數限制此類命令。使用 `count` 時，`ping` 會為每個回顯回覆返回一條記錄：

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/ping \
    -H "Content-Type: application/json" \
    --data '{"address":"192.168.88.10","count":"3"}'
```

```json
[{"avg-rtt":"551us","host":"192.168.88.10","max-rtt":"551us","min-rtt":"551us","packet-loss":"0","received":"1","sent":"1","seq":"0","size":"56","time":"551us","ttl":"64"},
{"avg-rtt":"536us","host":"192.168.88.10","max-rtt":"551us","min-rtt":"521us","packet-loss":"0","received":"2","sent":"2","seq":"1","size":"56","time":"521us","ttl":"64"},
{"avg-rtt":"538us","host":"192.168.88.10","max-rtt":"551us","min-rtt":"521us","packet-loss":"0","received":"3","sent":"3","seq":"2","size":"56","time":"542us","ttl":"64"}]
```

`duration` 短於限制的頻寬測試每秒返回一條記錄，其中包含測試的 `status`：

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/tool/bandwidth-test \
    -H "Content-Type: application/json" \
    --data '{"address":"192.168.88.2","user":"admin",
        "password":"<password>","duration":"3s",
        ".proplist":"status,duration"}'
```

```json
[{".section":"0","status":"connecting"},
{".section":"1","duration":"0s","status":"running"},
{".section":"2","duration":"1s","status":"running"},
{".section":"3","duration":"2s","status":"running"},
{".section":"4","duration":"3s","status":"done testing"}]
```

`monitor` 命令使用 `once` 並返回單個樣本。例如，兩個介面上的當前流量，以位元每秒為單位：

```bash
curl --cacert rest-ca.crt -u monitoring -X POST \
    https://192.168.88.1/rest/interface/monitor-traffic \
    -H "Content-Type: application/json" \
    --data '{"interface":"ether1,ether2","once":"",
        ".proplist":"name,rx-bits-per-second,tx-bits-per-second"}'
```

```json
[{"name":"ether1","rx-bits-per-second":"0","tx-bits-per-second":"0"},
{"name":"ether2","rx-bits-per-second":"25128","tx-bits-per-second":"8816"}]
```

要執行耗時超過 60 秒的任務，請使用不帶 `as-string` 的 `/execute` 將其作為後臺作業啟動（請參閱 [執行指令碼並寫入日誌](#run-a-script-and-write-to-the-log)）：請求會立即返回作業 ID，作業繼續執行。讓作業將其結果寫入日誌或檔案。

### 從不同使用者傳送並行請求 {#send-parallel-requests-from-separate-users}

路由器按到達順序一次執行一個使用者的請求。不同使用者的請求並行執行。因此，長命令會阻塞同一使用者的所有其他請求，直到它結束。

當用戶端放棄請求時，該請求仍會在路由器上繼續執行，直到命令結束或達到 60 秒限制。排在其後的同一使用者請求在達到限制時會失敗並顯示 `Session closed`。為獨立工作的用戶端（例如儀表板和自動化指令碼）分配不同的使用者。

## 自動化常見任務 {#automate-common-tasks}

### 阻止一個地址一天 {#block-an-address-for-a-day}

入侵檢測系統或日誌分析器可以將攻擊者的地址新增到防火牆會丟棄的地址列表中。使用 `timeout` 時，路由器會自行刪除該條目：

```bash
curl --cacert rest-ca.crt -u admin -X PUT \
    https://192.168.88.1/rest/ip/firewall/address-list \
    -H "Content-Type: application/json" \
    --data '{"list":"blocked","address":"203.0.113.45",
        "timeout":"1d","comment":"reported by IDS"}'
```

```json
{".id":"*3C","address":"203.0.113.45","comment":"reported by IDS","creation-time":"2026-09-28 16:48:57","disabled":"false","dynamic":"true","list":"blocked","timeout":"1d"}
```

超時結束時，路由器會刪除該條目；要提前解除對該地址的阻止，請 `DELETE` 該條目的 URL（`/rest/ip/firewall/address-list/*3C`）。新增已在列表中的地址會失敗，返回 `400` 和 `failure: already have such entry`。

該列表本身不會阻止任何內容：防火牆規則會丟棄其地址。在路由器上的終端中一次性新增該規則。`raw` 表中的規則在連線跟蹤之前處理封包，因此它會盡早丟棄被阻止的地址，適用於發往路由器和經過路由器的流量。`in-interface-list=WAN` 將其限制為來自網際網路的封包，因此錯誤的報告不會切斷你的 LAN：

```ros
/ip/firewall/raw/add chain=prerouting action=drop \
    in-interface-list=WAN src-address-list=blocked \
    comment="drop blocked addresses"
```

在整個超時期間，被阻止的地址無法從網際網路訪問路由器或其後面的網路，因此在自動化之前，請檢查報告系統傳送的內容。請參閱 [地址列表](../firewall-and-quality-of-service/firewall/address-lists.md)。

另一臺 RouterOS 裝置可以使用 `/tool/fetch` 傳送此類請求；這個請求新增一個沒有超時的條目。呼叫方路由器需要匯入 `rest-ca.crt`（`/certificate/import`）以檢查證書；沒有它，fetch 會失敗並顯示 `no trusted CA certificate found`：

```ros
/tool/fetch url="https://192.168.88.1/rest/ip/firewall/address-list" \
    http-method=put check-certificate=yes \
    http-header-field="Content-Type: application/json" \
    http-data="{\"list\":\"blocked\",\"address\":\"203.0.113.46\"}" \
    user=admin password="<password>" output=user
```

### 將配置儲存到伺服器 {#save-the-configuration-to-a-server}

帶 `file` 的 `export` 會將配置寫入路由器上的檔案。`/file/read` 從 `offset` 開始，每次請求最多返回 32768 位元組，因此備份伺服器可以收集該檔案並將其從路由器刪除。使用者需要 `read,write,ftp,test,api,rest-api`。在以下命令中，`jq` 從 JSON 回覆中提取檔案內容：

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/export \
    -H "Content-Type: application/json" --data '{"file":"backup"}'
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/file/read \
    -H "Content-Type: application/json" \
    --data '{"file":"backup.rsc","chunk-size":"32768","offset":"0"}' \
    | jq -j '.[0].data' > backup.rsc
curl --cacert rest-ca.crt -u admin -X DELETE \
    https://192.168.88.1/rest/file/backup.rsc
```

對於大於 32768 位元組的檔案，請重複讀取，並將 `offset` 增加已接收的位元組數，直到回覆中不再包含資料（檔案末尾為 `[{"data":""}]`；超過末尾的 offset 會失敗並顯示 `failure: chunk out of file bounds`）。請參閱 [`/file/read`](../cli-reference/file/read.md)。

匯出會省略密碼和私鑰。要包含它們，請新增 `"show-sensitive":""`，並同時為使用者授予 `sensitive` 策略；沒有該策略時，檔案仍會省略它們。請像保護路由器密碼一樣保護此類檔案。有關整個配置的二進位制備份，請參閱 [備份](../getting-started/configuration-management/backup.md)。

### 執行指令碼並寫入日誌 {#run-a-script-and-write-to-the-log}

要執行 `/system/script` 中的指令碼，請在 `.id` 中指定其名稱（或提供其 ID）：

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/system/script/run \
    -H "Content-Type: application/json" --data '{".id":"daily-report"}'
```

`/execute` 執行作為指令碼給出的控制檯命令。沒有 `as-string` 時，它會將指令碼作為作業啟動並返回作業 ID；使用 `as-string` 時，它會等待並返回指令碼的輸出：

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/execute \
    -H "Content-Type: application/json" \
    --data '{"script":"/log/info \"backup job started\""}'
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/execute \
    -H "Content-Type: application/json" \
    --data '{"script":":put [/system/clock/get date]","as-string":""}'
```

```json
{"ret":"*126"}
{"ret":"2026-09-28"}
```

### 檢查 RouterOS 更新 {#check-for-routeros-updates}

`check-for-updates` 向更新伺服器詢問路由器通道的最新版本。沒有 `once` 時，回覆會列出檢查結束前的進度，最後一條記錄包含 `status` 和 `latest-version`：

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/system/package/update/check-for-updates \
    -H "Content-Type: application/json" --data '{}'
```

### 移動防火牆規則 {#move-a-firewall-rule}

`move` 將一條規則放在另一條規則之前，就像在控制檯中一樣：

```bash
curl --cacert rest-ca.crt -u admin -X POST \
    https://192.168.88.1/rest/ip/firewall/nat/move \
    -H "Content-Type: application/json" \
    --data '{".id":"*9","destination":"*C"}'
```

要在某個位置建立規則，請在 `PUT` 正文中新增 `place-before`，其值為必須跟隨其後的規則的 ID。

### 讀取 SNMP OID {#read-snmp-oids}

帶 `oid` 的 `print` 會返回每個具有 SNMP OID 的屬性的 OID，而不是其值：

```bash
curl --cacert rest-ca.crt -u monitoring -X POST \
    https://192.168.88.1/rest/system/resource/print \
    -H "Content-Type: application/json" --data '{"oid":""}'
```

```json
[{"build-time":".1.3.6.1.4.1.14988.1.1.7.6.0","cpu-frequency":".1.3.6.1.4.1.14988.1.1.3.14.0","total-memory":".1.3.6.1.2.1.25.2.3.1.5.65536","uptime":".1.3.6.1.2.1.1.3.0"}]
```

### 在 Python 中讀取介面流量 {#read-interface-traffic-in-python}

以下 Python 程式使用 `requests` 庫列印每個具有鏈路的乙太網介面的當前流量。`json=` 會以 JSON 形式傳送正文並帶有 `Content-Type` 頭，會話會為兩個請求複用一個連線：

```python

ROUTER = "https://192.168.88.1/rest"

session = requests.Session()
session.auth = ("monitoring", "use-a-long-random-password")
session.verify = "rest-ca.crt"

# Names of the Ethernet interfaces that have a link
ports = session.get(
    f"{ROUTER}/interface",
    params={"type": "ether", "running": "true", ".proplist": "name"},
)
ports.raise_for_status()
names = ",".join(port["name"] for port in ports.json())

# One sample of the traffic on these interfaces
traffic = session.post(
    f"{ROUTER}/interface/monitor-traffic",
    json={"interface": names, "once": ""},
)
traffic.raise_for_status()

for port in traffic.json():
    rx = int(port["rx-bits-per-second"]) / 1_000_000
    tx = int(port["tx-bits-per-second"]) / 1_000_000
    print(f"{port['name']}: rx {rx:.1f} Mbit/s, tx {tx:.1f} Mbit/s")
```

```text
ether2: rx 0.1 Mbit/s, tx 0.0 Mbit/s
```

有關二進位制 [API](./api/index.md)，請參閱 [Python 3 示例](./api/python3-example.md)。

## 構建儀表板或整合 {#build-a-dashboard-or-integration}

Web 儀表板、狀態頁面或與另一系統的整合可以透過 REST API 讀取路由器，AI 助手可以根據本頁和 CLI 參考編寫此類工具：向它提供本頁的地址以及該工具所用選單的 CLI 參考頁面的地址。給助手提供以下資訊，或者在你自行編寫時牢記：

- **用於 REST 呼叫的後端。** 路由器不傳送 CORS 頭，並以 `503` 回應 `OPTIONS` 預檢請求，因此從另一個地址提供的網頁無法從瀏覽器呼叫 REST API。讓一個小型伺服器端程式（儀表板的後端或代理）傳送請求。它還能讓路由器的密碼不進入瀏覽器。
- **只讀使用者。** 建立一個具有 `read,api,rest-api` 的組，如 [建立 REST 使用者](#create-a-rest-user) 中所述，併為儀表板建立一個單獨的使用者，將該使用者的 `address` 設定為後端的地址。僅讀取的儀表板即使程式碼有誤也無法更改配置。
- **不要讓助手獲得管理員密碼。** 不要向 AI 助手或它編寫的程式碼提供 `admin` 憑據。為生成的程式碼提供只讀使用者，並僅為該工具真正需要的操作新增寫訪問許可權。
- **自己的使用者，以及短請求。** 一個使用者的請求一次執行一個，因此一次輪詢許多值的儀表板會逐個等待。使用帶 `once` 的 `monitor` 命令、帶 `count` 的 `ping` 以及 `.proplist` 來保持回覆較小。
- **回覆中的字串。** 每個值都以字串形式到達：在計算前轉換數字。流量速率以位元每秒為單位，記憶體和磁碟大小以位元組為單位，`cpu-load` 以百分比為單位，`uptime` 等持續時間採用 RouterOS 格式，例如 `1d7h44m20s`。
- **一個連線。** 為輪詢複用 HTTP 連線（keep-alive）以節省 TCP 和 TLS 設定。路由器在任何連線上都會將使用者的登入狀態保持 10 分鐘，因此頻繁輪詢不會每次都登入。
- **選單和引數。** [CLI 參考](../cli-reference/index.md) 描述了每個選單和引數。路由器還透過 `/console/inspect` 描述自身，它會列出選單的命令和引數：

```bash
curl --cacert rest-ca.crt -u monitoring -X POST \
    https://192.168.88.1/rest/console/inspect \
    -H "Content-Type: application/json" \
    --data '{"request":"child","path":"ip,address,add",
        ".proplist":"name,node-type"}'
```

```json
[{"name":"add","node-type":"cmd"},{"name":"address","node-type":"arg"},{"name":"broadcast","node-type":"arg"},{"name":"comment","node-type":"arg"},{"name":"copy-from","node-type":"arg"},{"name":"disabled","node-type":"arg"},{"name":"interface","node-type":"arg"},{"name":"netmask","node-type":"arg"},{"name":"network","node-type":"arg"}]
```

在針對生產路由器執行助手編寫的程式碼之前，請使用只讀使用者或在測試路由器上進行測試。

## 排查 REST 請求問題 {#troubleshoot-rest-requests}

HTTP 狀態碼顯示請求是否成功。失敗時（400 或更高），正文是一個 JSON 物件，程式碼在 `error` 中，描述在 `message` 中，對於大多數錯誤，路由器的原因在 `detail` 中。例如，使用 `{".id":"ether1"}` 的 `POST /rest/interface/remove` 會失敗，因為 `/interface` 沒有 `remove` 命令：

```json
{"detail":"no such command or directory (remove)","error":400,"message":"Bad Request"}
```

| 回覆 | 原因 |
| :-- | :-- |
| `401 Unauthorized` | 使用者名稱或密碼錯誤，組沒有 `rest-api` 策略，或使用者的 `address` 不允許該用戶端。 |
| `500`、`std failure: not allowed (9)` | 組具有 `rest-api` 但沒有 `api` 策略。 |
| `500`、`not enough permissions (9)` | 組缺少該命令的策略，例如更改需要 `write`，`ping` 需要 `test`。 |
| `400`、`missing or invalid resource identifier` | 路由器無法對記錄應用 `PATCH` 或 `DELETE`：URL 中沒有記錄 ID（例如對沒有記錄的選單執行 `PATCH`；請使用帶 `set` 的 `POST`）、無法刪除的記錄（乙太網介面）、路由器拒絕的值，或沒有 `write` 策略的使用者。 |
| `400`、`no such command or directory (x)` | 選單、命令或記錄名稱 `x` 不存在。 |
| `400`、`no such command` | 選單中不存在該命令，或對命令傳送了 `GET`。 |
| `400`、`no such command prefix` | URL 的 ID 中包含百分號編碼的 `*`（`%2A`）。 |
| `400`、`unknown parameter x`、`invalid value for argument x`、`missing =x=`、`failure: ...` | 控制檯拒絕了這些引數；詳細資訊是控制檯的錯誤訊息。 |
| `400`、`Failed to parse json` | 正文不是有效的 JSON，或數字包含指數。 |
| `400`、`Session closed` | 命令運行了 60 秒，或請求排在同一使用者的此類請求之後等待。請參閱 [將命令保持在 60 秒以內](#keep-commands-within-60-seconds)。 |
| `403 Forbidden`（HTML 頁面） | 此協定的 REST API 已關閉（`/ip/service/webserver` 中的 `rest-plain` 或 `rest-secure`）。 |
| `404 Not Found` | 沒有記錄具有此 ID。 |
| `415 Unsupported Media Type` | 請求有正文但沒有 `Content-Type: application/json` 頭。 |
| 連線重設 | 用戶端地址不在服務的 `available-from` 中。 |
| TLS 或證書錯誤 | 用戶端不信任證書，URL 中路由器的名稱與證書不同，或 `www-ssl` 沒有證書。 |

日誌在 `account` 主題中記錄 REST 登入：`user monitoring logged in from 192.168.88.10 via rest-api`，隨後是 `via api` 的登入。沒有 `api` 策略的組會在 REST 登入後記錄 `login failure for user monitoring via api`：

```ros
/log/print where topics~"account"
```

`/user/active` 會將每個 REST 登入列出兩次：一次是透過 `via rest-api` 並帶有用戶端地址，一次是透過 `via api` 且沒有地址。

## 技術細節 {#technical-details}

### 會話 {#sessions}

- REST 伺服器使用使用者的憑據登入 API，並將該登入保持 10 分鐘。在此期間，無論請求透過一個還是多個 HTTP 連線到達，都會使用該登入；10 分鐘後的下一個請求會再次登入。
- 使用 `/user/set`（密碼、`disabled`、`address`）或 `/user/remove` 對使用者所做的更改會在下一個請求時生效。對組策略的更改會在登入續期時生效，最多 10 分鐘後。
- 一個使用者的請求一次執行一個；不同使用者的請求並行執行。

### JSON 格式 {#json-format}

路由器大體遵循 ECMA-404 JSON 標準：

- 回覆將每個值編碼為字串，即使屬性包含數字或布林值。
- 請求中的 JSON 數字可以是八進位制（前導 `0`，`010` 為 8）或十六進位制（`0x` 字首）。帶指數的數字（`2e0`）會被拒絕並顯示 `Failed to parse json`。
- 作為字串傳送的數字會按控制檯讀取它的方式讀取：`"5"` 為 5，`"0x4"` 為 4。

### HTTP {#http}

- 路由器使用 HTTP/1.1 並保持連線開啟（keep-alive），這節省了下一個請求的 TCP 和 TLS 設定。
- 沒有憑據的請求會得到 `401` 和 `WWW-Authenticate: Basic`。
- `PUT` 會返回 `201 Created`，並在 `Location` 頭中包含新記錄的 URL，例如 `Location: https://192.168.88.1/rest/ip/address/*18`。`DELETE` 返回 `204 No Content`。
- REST API 的錯誤回覆是 JSON 物件；在 `/ip/service/webserver` 中關閉的 Web 伺服器部分會返回 HTML `403` 頁面。
