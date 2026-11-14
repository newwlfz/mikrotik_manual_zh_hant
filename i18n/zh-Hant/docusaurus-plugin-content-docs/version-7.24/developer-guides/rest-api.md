---
sidebar_key: "developer-guides/rest-api"
sidebar_position: 2
title: "REST API"
sidebar_label: "REST API"
description: "面向開發者的 REST API 及示例。"
tags:
  - 'api'
  - 'management'
source: https://manual.mikrotik.com/docs/7.24/developer-guides/rest-api
captured_at: '2026-11-04T11:27:50+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**REST API** 一詞通常指透過 HTTP 協定在一組預定義的面向資源的 URL 上訪問的 **API**。
**REST API** 實現為 [**API**](./api/index.md) 的 JSON 封裝介面。它允許你建立、讀取、更新和刪除資源，並呼叫任意控制檯命令。

要開始使用 REST API，請在 [`IP Service`](../system-information-and-utilities/services.md) 選單中啟用 `www-ssl` 或 `www` 服務。

當 `www-ssl` 服務執行（HTTPS 訪問）時，你可以連線到：

- `https://<router_IP>/rest`。

當 `www` 服務執行（HTTP 訪問）時，你可以連線到：

- `http://<router_IP>/rest`。

使用 HTTP 訪問（`www` 服務）的主要風險是身份驗證憑據可能被被動竊聽讀取。僅在攻擊者無法訪問的網路上進行測試時使用它，或當你確定資料無法被解密時使用，例如當 HTTP 透過加密隧道傳輸時。

最簡單的開始方式是使用 cURL、wget、fetch 工具或任何其他簡單的 HTTP 用戶端。

```sh
$ curl -k -u admin: https://10.155.101.214/rest/system/resource

[{"architecture-name":"tile","board-name":"CCR1016-12S-1S+",
"build-time":"2020-12-04 14:19:51","cpu":"tilegx","cpu-count":"16",
"cpu-frequency":"1200","cpu-load":"1","free-hdd-space":"83439616",
"free-memory":"1503133696","platform":"MikroTik",
"total-hdd-space":"134217728","total-memory":"2046820352",
"uptime":"2d20h12m20s","version":"7.1beta4 (development)"}]
```

## 身份驗證 {#authentication}

對 REST API 的身份驗證使用 [HTTP Basic Auth](http://en.wikipedia.org/wiki/Basic_access_authentication)。你的使用者名稱和密碼與控制檯使用者相同（預設情況下，**admin** 無密碼）。

要使用安全連線（HTTPS），請在 [證書選單](../authentication-authorization-accounting/certificates.md) 中設定證書，並配置 `www-ssl` 使用新建立或匯入的證書。如果你使用自簽名證書，請將其 CA 匯入用戶端的受信任根儲存。進行測試時，你可以不安全地連線（cURL 使用 `-k`，或 wget 使用 `--no-check-certificate`）。

### JSON 格式 {#json-format}

伺服器大體遵循 ECMA‑404 標準，並有以下說明：

- 在 JSON 回覆中，所有物件值都編碼為字串，即使底層資料是數字或布林值。
- 伺服器還接受八進位制格式（以 0 開頭）和十六進位制格式（以 0x 開頭）的數字。如果數字以字串格式傳送，則假定為十進位制格式。
- 不支援帶指數的數字。

## HTTP 方法 {#http-methods}

下表彙總了支援的 HTTP 方法

| HTTP 動詞   | CRUD          | ROS    | 描述                                                     |
|:--|:--|:--|:--|
| GET         | 讀取          | print  | 獲取記錄。                                               |
| PATCH       | 更新/修改     | set    | 更新單條記錄。                                           |
| PUT         | 建立          | add    | 建立新記錄。                                             |
| DELETE      | 刪除          | remove | 刪除單條記錄。                                           |
| POST        |               |        | 訪問所有控制檯命令的通用方法。                           |

### GET {#get}

此方法允許從 URL 中編碼的指定選單獲取所有記錄的列表或單條記錄。
例如，獲取所有 IP 地址（等同於 `ip/address/print` CLI 命令）：

```sh
$ curl -k -u admin: https://10.155.101.214/rest/ip/address

[{".id":"*1","actual-interface":"ether2","address":"10.0.0.111/24","disabled":"false",
"dynamic":"false","interface":"ether2","invalid":"false","network":"10.0.0.0"},
{".id":"*2","actual-interface":"ether3","address":"10.0.0.109/24","disabled":"true",
"dynamic":"false","interface":"ether3","invalid":"false","network":"10.0.0.0"}]
```

在 URL 末尾附加 ID 以返回單條記錄：

```sh
$ curl -k -u admin: https://10.155.101.214/rest/ip/address/*1

{".id":"*1","actual-interface":"ether2","address":"10.0.0.111/24","disabled":"false",
"dynamic":"false","interface":"ether2","invalid":"false","network":"10.0.0.0"}
```

如果表中包含命名引數，你可以使用名稱代替 ID；例如，獲取 **ether1**：

```sh
curl -k -u admin: https://10.155.101.214/rest/interface/ether1
```

你還可以篩選輸出；例如，僅返回屬於 10.155.101.0 網路的動態地址：

```sh
$ curl -k -u admin: "https://10.155.101.214/rest/ip/address?network=10.155.101.0&dynamic=true"

[{".id":"*8","actual-interface":"sfp12","address":"10.155.101.214/24","disabled":"false",
"dynamic":"true","interface":"sfp12","invalid":"false","network":"10.155.101.0"}]
```

另一個示例僅返回 "dummy" 介面上且註釋為 "test" 的地址：

```sh
$ curl -k -u admin: 'https://10.155.101.214/rest/ip/address?comment=test&interface=dummy'

[{".id":"*3","actual-interface":"dummy","address":"192.168.99.2/24","comment":"test",
"disabled":"false","dynamic":"false","interface":"dummy","invalid":"false","network":"192.168.99.0"}]
```

如果你只想返回特定屬性，可以使用 `.proplist`，後跟 `=` 字元和逗號分隔的屬性列表。例如，僅顯示 address 屬性以及其是否被停用：

```sh
$ curl -k -u admin: https://10.155.101.214/rest/ip/address?.proplist=address,disabled

[{"address":"10.0.0.111/24","disabled":"false"},{"address":"10.0.0.109/24","disabled":"true"}]
```

### PATCH {#patch}

使用此方法更新單條記錄。將 PATCH 請求的正文設定為包含欄位及其新值的 JSON 物件。例如，添加註釋：

```sh
$ curl -k -u admin: -X PATCH https://10.155.101.214/rest/ip/address/*3 \
  --data '{"comment": "test"}' -H "content-type: application/json"

{".id":"*3","actual-interface":"dummy","address":"192.168.99.2/24","comment":"test",
"disabled":"false","dynamic":"false","interface":"dummy","invalid":"false","network":"192.168.99.0"}
```

更新成功時，伺服器返回包含其全部引數的更新後物件。

### PUT {#put}

此方法建立新記錄。將請求正文設定為包含該記錄引數的 JSON 物件。每次請求只能建立一條記錄。

成功時，伺服器返回包含其全部引數的已建立物件。
例如，向 dummy 介面新增 IP 地址：

```sh
$ curl -k -u admin: -X PUT https://10.155.101.214/rest/ip/address \
  --data '{"address": "192.168.111.111", "interface": "dummy"}' -H "content-type: application/json"

{".id":"*A","actual-interface":"dummy","address":"192.168.111.111/32","disabled":"false",
"dynamic":"false","interface":"dummy","invalid":"false","network":"192.168.111.111"}
```

### DELETE {#delete}

使用此方法刪除具有指定 ID 的記錄。如果刪除成功，伺服器返回空正文。例如，連續兩次呼叫同一刪除操作會導致路由器在第二次嘗試時返回 `404` 錯誤：

```sh
$ curl -k -u admin: -X DELETE https://10.155.101.214/rest/ip/address/*9
$ curl -k -u admin: -X DELETE https://10.155.101.214/rest/ip/address/*9
{"error":404,"message":"Not Found"}
```

### POST {#post}

所有 [**API**](./api/index.md) 功能均可透過 `POST` 使用。將命令字編碼到 URL 中，並將可選引數作為 JSON 物件中的欄位傳遞。例如，要更改活動使用者的密碼，請傳送：

```
POST https://router/rest/password
{"old-password":"old","new-password":"N3w", "confirm-new-password":"N3w"}
```

REST 響應與 API 響應具有相同的結構：

- 如果響應包含 `!re` 語句（記錄），則 JSON 回覆將包含物件列表。
- 如果 `!done` 語句包含資料，則 JSON 回覆將包含帶有該資料的物件。
- 如果 `!done` 語句中沒有記錄或資料，則響應將包含空列表。

有兩個特殊鍵：`.proplist` 和 `.query`，它們與 `print` 命令字一起使用。有關 API 響應、屬性列表和查詢的更多資訊，請參閱 [API](./api/index.md) 文件。

#### 屬性列表 {#proplist}

使用 `.proplist` 鍵指定要返回哪些屬性。該值可以是單個逗號分隔字串：

```
POST https://router/rest/interface/print
{".proplist":"name,type"}
```

或字串列表：

```
POST https://router/rest/interface/print
{".proplist":["name","type"]}
```

例如，從 `ip/address` 選單返回 address 和 interface 屬性：

```sh
$ curl -k -u admin: -X POST https://10.155.101.214/rest/ip/address/print\
  --data '{".proplist": ["address","interface"]}' -H "content-type: application/json"

[{"address":"192.168.99.2/24","interface":"dummy"},
{"address":"172.16.5.1/24","interface":"sfpplus1"},
{"address":"172.16.6.1/24","interface":"sfp2"},
{"address":"172.16.7.1/24","interface":"sfp3"},
{"address":"10.155.101.214/24","interface":"sfp12"},
{"address":"192.168.111.111/32","interface":"dummy"}]
```

#### 查詢 {#query}

`.query` 鍵用於建立查詢棧。該值是查詢詞列表。例如：

```
POST https://router/rest/interface/print
{".query":["type=ether","type=vlan","#|!"]}
```

等同於 **API** 語句：

```
/interface/print
?type=ether
?type=vlan
?#|!
```

組合 `query` 和 `proplist` 的示例，為所有動態記錄以及網路為 192.168.111.111 的記錄返回 `.id`、`address` 和 `interface` 屬性

```sh
$ curl -k -u admin: -X POST https://10.155.101.214/rest/ip/address/print \
  --data '{".proplist": [".id","address","interface"], ".query": ["network=192.168.111.111","dynamic=true","#|"]}'\
  -H "content-type: application/json"

[{".id":"*8","address":"10.155.101.214/24","interface":"sfp12"},
{".id":"*A","address":"192.168.111.111/32","interface":"dummy"}]
```

#### 超時 {#timeout}

如果命令無限期執行，它最終會超時，連線將因錯誤而關閉。當前超時間隔為 60 秒。為避免超時錯誤，請新增能充分限制命令執行時間的引數。

例如，除非新增 count 引數來限制執行，否則 ping 命令將超過超時時間：

```sh
$ curl -k -u admin: -X POST https://10.155.101.214/rest/ping \
  --data '{"address":"10.155.101.1"}' \
  -H "content-type: application/json"

{"detail":"Session closed","error":400,"message":"Bad Request"}

$ curl -k -u admin: -X POST https://10.155.101.214/rest/ping \
  --data '{"address":"10.155.101.1","count":"4"}' \
  -H "content-type: application/json"

[{"avg-rtt":"453us","host":"10.155.101.1","max-rtt":"453us","min-rtt":"453us","packet-loss":"0","received":"1","sent":"1","seq":"0","size":"56","time":"453us","ttl":"64"},
{"avg-rtt":"417us","host":"10.155.101.1","max-rtt":"453us","min-rtt":"382us","packet-loss":"0","received":"2","sent":"2","seq":"1","size":"56","time":"382us","ttl":"64"},
{"avg-rtt":"495us","host":"10.155.101.1","max-rtt":"650us","min-rtt":"382us","packet-loss":"0","received":"3","sent":"3","seq":"2","size":"56","time":"650us","ttl":"64"},
{"avg-rtt":"461us","host":"10.155.101.1","max-rtt":"650us","min-rtt":"359us","packet-loss":"0","received":"4","sent":"4","seq":"3","size":"56","time":"359us","ttl":"64"}]
```

對於接受 duration 引數的命令，REST 超時仍然適用。即使要求命令執行一小時，它也會提前終止並返回錯誤。

例如，可以透過提供小於超時值的執行持續時間來限制頻寬測試工具：

```sh
$ curl -k -u admin: -X POST 'https://10.155.101.214/rest/tool/bandwidth-test' \
  --data '{"address":"10.155.101.1","duration":"3s"}' \
  -H "content-type: application/json"

[{".section":"0","connection-count":"20","direction":"receive","lost-packets":"0",
"random-data":"false","rx-10-second-average":"0","rx-current":"0","rx-size":"1500",
"rx-total-average":"0",
"status":"connecting"},
{".section":"1","connection-count":"20","direction":"receive","duration":"1s",
"lost-packets":"0","random-data":"false","rx-10-second-average":"0","rx-current":"0",
"rx-size":"1500","rx-total-average":"0",
"status":"running"},
{".section":"2","connection-count":"20","direction":"receive","duration":"2s",
"lost-packets":"581175","random-data":"false","rx-10-second-average":"854372352",
"rx-current":"854372352","rx-size":"1500","rx-total-average":"854372352",
"status":"running"},
{".section":"3","connection-count":"20","direction":"receive","duration":"3s",
"lost-packets":"9014","random-data":"false","rx-10-second-average":"891979008",
"rx-current":"929585664","rx-size":"1500","rx-total-average":"891979008",
"status":"done testing"}]
```

## 錯誤 {#errors}

API 呼叫的成功或失敗由 HTTP 狀態碼指示。失敗時（400 或更高），響應正文包含帶有錯誤碼、描述和可選詳細資訊的 JSON 物件。例如，嘗試刪除介面會返回

```text
{"error":406,"message":"Not Acceptable","detail":"no such command or directory (remove)"}
```

## 監控 {#monitor}

REST API 不支援 `monitor` 之類的連續命令。使用 `monitor once` 引數列印單個結果。

## 示例 {#examples}

下面我們添加了一組簡短的 REST API 呼叫示例，你可以對裝置執行這些呼叫：

建立日誌條目：

```bash
curl -k -u <username>:<password> -X POST https://<ip-address>/rest/execute --data '{"script":"/log/info test"}' -H "content-type: application/json"
```

執行指令碼：

```bash
curl -k -u <username>:<password> https://<ip-address>/rest/system/script/run --data '{".id":"*1"}' -H "content-type: application/json"
```

LTE 監控一次：

```bash
curl -k -u <username>:<password> https://<ip-address>/rest/interface/lte/monitor -d '{"numbers":"0", "once":""}' -H "content-type: application/json"
```

匯出裝置配置：

```bash
curl -k -u <username>:<password> https://<ip-address>/rest/export --data '{"compact":"","file":"test.rsc"}' -H "content-type: application/json"
```

移動防火牆條目（切換位置）：

```bash
curl -k -u <username>:<password> -X POST https://<ip-address>/rest/ip/firewall/nat/move --data '{".id":"*9","destination":"*C"}' -H "content-type: application/json"
```

LTE 韌體更新：

```bash
curl -k -u <username>:<password> -X POST 'https://<ip-address>/rest/interface/lte/firmware-upgrade'   --data '{"numbers":"lte2"}' -H "content-type: application/json"
```

從 `/system/resource` 選單獲取 OID：

```bash
curl -k -u <username>:<password> -X POST https://<ip-address>/rest/system/resource/print --data '{"oid":""}' -H "content-type: application/json"
```

使用 `/tool/fetch` 從一個 RouterOS 裝置向另一個 RouterOS 裝置執行 REST API POST：

```ros
/tool fetch http-method=post url="https://<ip-address>/rest/execute" \
http-data="{\"script\":\"/log info fetchtest\"}" \
http-header-field="Content-Type:application/json" \
output=user user=<username> password=<password>
```
