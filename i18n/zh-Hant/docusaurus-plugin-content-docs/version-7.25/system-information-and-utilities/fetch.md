---
sidebar_key: "system-information-and-utilities/fetch"
sidebar_position: 4
title: "獲取"
sidebar_label: "獲取"
description: "Fetch 透過 HTTP、HTTPS、FTP、TFTP 和 SFTP 傳輸檔案，並可從控制檯或指令碼發起 HTTP 請求：下載、上傳、POST 資料與 webhooks、證書檢查、重定向、結果變數以及 VRF 支援。"
tags:
  - 'fetch'
source: https://manual.mikrotik.com/docs/7.25/system-information-and-utilities/fetch
captured_at: '2026-11-04T11:21:58+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

fetch 透過 HTTP、HTTPS、FTP、TFTP 和 SFTP 下載和上傳檔案，並向遠端伺服器傳送 HTTP 請求（GET、POST、PUT 等）。它可在控制檯和指令碼中執行，即時列印狀態，並把結果儲存到檔案或返回到指令碼變數中。

在 WinBox 中，從左側選單選擇 **New Terminal** 即可執行本頁的命令。終端會顯示傳輸狀態；當命令把結果儲存到路由器時，開啟 **Files** 即可找到下載的檔案。

## 下載和上傳檔案 {#download-and-upload-files}

透過 FTP 從另一臺 RouterOS 裝置複製檔案。該裝置需要啟用 FTP 服務（`/ip/service`），並擁有一個帶密碼的賬戶：

```ros
/tool/fetch mode=ftp address=192.168.88.2 user=admin \
    password=mypassword src-path=conf.rsc dst-path=backup.rsc
```

若要改為上傳檔案，請設定 `upload=yes` 並交換路徑：`src-path` 是本地路由器上的檔案，`dst-path` 是遠端裝置上的檔名：

```ros
/tool/fetch mode=ftp address=192.168.88.2 user=admin \
    password=mypassword src-path=backup.rsc dst-path=conf.rsc upload=yes
```

同樣的傳輸也可以使用埠 22 上的 `mode=sftp`。SFTP 使用遠端裝置的 SSH 服務，RouterOS 預設啟用該服務。上傳（`upload=yes`）僅在 `ftp` 和 `sftp` 模式下可用；若要把資料傳送到 Web 伺服器，請使用帶 `http-data` 的 HTTP 請求。未指定 `user` 時，FTP 以 `anonymous` 身份登入。

你可以把地址、憑據和路徑合併到一個 URL 中；此時模式會根據協定字首自動識別：

```ros
/tool/fetch url="ftp://admin:mypassword@192.168.88.2/conf.rsc" \
    dst-path=backup.rsc
```

`mode=tftp` 從 TFTP 伺服器下載，例如另一臺路由器上的 [`/ip/tftp`](../cli-reference/ip/tftp/index.md)：

```ros
/tool/fetch address=192.168.88.2 mode=tftp src-path=conf.rsc \
    dst-path=backup.rsc
```

:::note
SFTP 主機金鑰驗證在新安裝中預設啟用，在升級後的路由器上則保持停用（[`/ip/ssh`](../cli-reference/ip/ssh/index.md) 中的 `known-hosts-validation` 設定）。啟用驗證後，若所訪問伺服器的金鑰不在 [`/ip/ssh/known-hosts`](../cli-reference/ip/ssh/known-hosts.md) 中，fetch 會失敗並報 `host key not trusted`；`sftp-known-hosts-ignore=yes` 可為單次傳輸繞過該檢查，`known-hosts-trusted-subnets` 則對整個子網跳過檢查。
:::

## 發起 HTTP 請求 {#make-http-requests}

使用 `url` 引數時，fetch 會從協定字首識別協定，並以 URL 中的名稱儲存檔案，除非 `dst-path` 覆蓋該名稱：

```ros
[admin@MikroTik] > /tool/fetch check-certificate=yes \
    url="https://download.mikrotik.com/routeros/7.19/CHANGELOG"
  status: connecting

      status: finished
        code: 200
  downloaded: 18KiB
       total: 18KiB
    duration: 1s
```

fetch 預設不校驗 TLS 證書：未設定 `check-certificate` 時，即使伺服器證書已過期或為自簽名證書，它也會建立連線。對於你依賴的 HTTPS 下載，請設定 `check-certificate=yes`，並且在你匯入或執行下載的內容之前一定要先設定。RouterOS 內建了包含公共根證書的信任儲存（`/certificate/settings` 中的 `builtin-trust-store`），因此訪問公共站點無需額外匯入證書。對於使用你自己 CA 簽發證書的伺服器，請用 `/certificate/import` 匯入該 CA 的證書；參見 [證書](../authentication-authorization-accounting/certificates.md)。該檢查還會驗證 URL 中的主機名，並把證書的日期與路由器的時鐘進行比較，因此在依賴它之前請先設定時鐘（例如使用 [NTP client](./ntp.md)）。證書無效會導致 fetch 失敗：

```text
failure: SSL: ssl: cert not valid (after: Sun Apr 12 23:59:59 2015 < now: Tue Sep 29 06:51:00 2026) - "OU=PositiveSSL Wildcard, CN=*.badssl.com" (6)
```

對於需要 HTTP 認證的伺服器，請設定 `user` 和 `password`。Basic 認證是預設方式，會在第一次請求時傳送憑據；若要使用 digest 認證，請設定 `http-auth-scheme=digest`。

HTTP 重定向會被自動跟隨。`http-max-redirect-count` 限制 fetch 跟隨的重定向次數：在預設值 2 下，會跟隨兩次重定向組成的鏈，第三次重定向則以該重定向狀態使請求失敗，例如 `failure: Status 302, Found (Location: "https://mikrotik.com/download")`。

### 向伺服器傳送資料 {#send-data-to-a-server}

對 API 端點使用 `http-method`、`http-header-field` 和 `http-data`：

```ros
/tool/fetch url="https://192.0.2.10/collector" http-method=post \
    http-header-field="Content-Type: application/json" \
    http-data="{\"lat\":\"56.12\",\"lon\":\"25.12\"}"
```

若 `http-header-field` 中沒有 `Content-Type`，請求體會以 `application/x-www-form-urlencoded` 傳送。多個頭欄位用逗號分隔（`"X-One: a,X-Two: b"`）。使用 `http-content-encoding=gzip`（或 `deflate`）時，POST 或 PUT 的請求體會以壓縮形式傳送，並帶有匹配的 `Content-Encoding` 頭。

若要傳送生成的內容，請先把它儲存到檔案，再把檔案讀入變數，並將該變數作為 `http-data` 傳入。請把命令放在同一個塊中，因為 `:local` 變數只在其所在塊記憶體在，並用 `find` 找到該檔案：

```ros
{
    /export file=export.rsc
    :local data [/file/get [find name=export.rsc] contents]
    /tool/fetch url="https://192.0.2.10/collector" http-method=put \
        http-data=$data
}
```

這適用於不超過 60000 位元組的檔案，即在 `http-data` 的 64 KB 限制之內。更大的檔案請改用 FTP 或 SFTP 上傳。若要呼叫另一臺 RouterOS 裝置的 REST API，參見 [REST API](../developer-guides/rest-api.md)。

## 自動化常見任務 {#automate-common-tasks}

### 將備份上傳到伺服器 {#upload-a-backup-to-a-server}

儲存加密備份並將其上傳到 SFTP 伺服器。`/system/backup/save` 會在下一條命令執行之前完成。請從 [scheduler](./scheduler.md) 指令碼中執行這些命令，以便每晚在路由器之外保留一份副本：

```ros
/system/backup/save name=nightly password="backup-file-password"
/tool/fetch url="sftp://192.168.88.2/nightly.backup" upload=yes \
    src-path=nightly.backup user=backup password="server-password"
```

關於備份包含哪些內容以及如何恢復，參見 [備份](../getting-started/configuration-management/backup.md)。

### 下載並執行指令碼 {#download-and-run-a-script}

從你的伺服器獲取配置指令碼並匯入。`check-certificate=yes` 可確保檔案來自你的伺服器；`/import` 會執行檔案中的每條命令，因此請只從你掌控的伺服器獲取指令碼。在同一個塊中，下載失敗會中止該塊，因此舊版本的檔案不會被匯入：

```ros
{
    /tool/fetch url="https://config.example.com/branch.rsc" \
        check-certificate=yes dst-path=branch.rsc
    /import file-name=branch.rsc
}
```

### 向 webhook 傳送通知 {#send-a-notification-to-a-webhook}

聊天服務、監控和自動化工具在 webhook URL 上接受 JSON 訊息；欄位名稱取決於具體服務，因此請查閱其 webhook 文件。`$[...]` 會把命令的輸出插入訊息中，此處是路由器的名稱。插入的文字不會被轉義：其中的引號或反斜槓會破壞 JSON。

```ros
/tool/fetch url="https://hooks.example.com/notify" http-method=post \
    http-header-field="Content-Type: application/json" \
    check-certificate=yes output=none \
    http-data="{\"text\":\"$[/system/identity/get name]: backup done\"}"
```

當身份為 `branch-office-1` 時，伺服器會收到 `{"text":"branch-office-1: backup done"}`。`output=none` 會丟棄回覆。

## 在指令碼中使用 fetch {#use-fetch-in-scripts}

使用 `as-value` 時，fetch 返回一個數組，而不是列印到控制檯。關於 `:local` 變數、`{ }` 塊和 `:onerror`，參見 [指令碼](../developer-guides/scripting/index.md)。`output` 決定響應體的去向：

- `file`（預設）- 一個檔案，即 `dst-path` 或來自 URL 的名稱。
- `none` - 不儲存到任何地方。
- `user` - 放入 `data` 鍵，最多 64512 位元組（63 KiB）。
- `user-with-headers` - 放入 `data` 鍵，最多 20480 位元組（20 KiB），並把響應頭放入 `http-headers`。

更長的響應體會被截斷且不會報錯：當 `[:len ($result->"data")]` 等於該限制時，響應體很可能更長。

下面的指令碼在網頁內容以 `0` 開頭時停用 `ether5`，否則啟用它。`:pick` 取第一個字元，因為文字檔案通常以換行符結尾。fetch 失敗會丟擲錯誤，由 `:onerror` 捕獲並記錄日誌，埠保持原狀：

```ros
{
    :local url "http://192.0.2.10/state.txt"
    :onerror e in={
        :local result [/tool/fetch url=$url as-value output=user]
        :if ([:pick ($result->"data") 0 1] = "0") do={
            /interface/ethernet/set [find name=ether5] disabled=yes
        } else={
            /interface/ethernet/set [find name=ether5] disabled=no
        }
    } do={:log warning "state check failed: $e"}
}
```

`:onerror` 會把錯誤訊息放入第一個變數；對於 HTTP 錯誤，第二個變數儲存狀態 `code` 和返回的 `http-headers`：

```ros
:onerror err,attr in={
    /tool/fetch url=http://192.168.88.2/nonexistent as-value
} do={
    :put $err; :put ($attr->"code"); :put ($attr->"http-headers")
}
```

```text
failure: Status 404, Not Found (/tool/fetch; line 2)
404
Cache-Control: no-store;Connection: Keep-Alive;Content-Length: 99;Content-Type: text/html;Date: Tue, 29 Sep 2026 07:05:39 GMT;Expires: 0;Pragma: no-cache;X-Frame-Options: sameorigin
```

## 在 VRF 中執行 fetch {#run-fetch-in-a-vrf}

要讓 fetch 使用 [VRF](../user-guides/routing-and-networking-protocols/vrf.md)，請在 `address` 引數中於 `@` 之後追加 VRF 名稱。兩種寫法都可以：

```ros
/tool/fetch url="ftp://admin:mypassword@192.168.88.2/conf.rsc" \
    address=@vrf1 dst-path=backup.rsc
/tool/fetch mode=ftp address=192.168.88.2@vrf1 user=admin \
    password=mypassword src-path=conf.rsc dst-path=backup.rsc
```

VRF 不能直接寫進 URL 本身：在 `url="http://192.168.88.2@vrf1/…"` 中，`@` 之後的所有內容都被當作主機名，請求會因解析錯誤而失敗。

## 技術細節 {#technical-details}

- fetch 會列印諸如 `status: connecting` 或 `status: requesting` 之類的中間狀態行，並在完成時列印包含 `status`、`code`、傳輸大小和 `duration` 的摘要。大小以 KiB 顯示，向下取整，且有資料到達時至少為 1；`as-value` 的 `downloaded`、`uploaded` 和 `total` 欄位包含相同的值。
- 每個 HTTP 請求都帶有 `User-Agent: RouterOS <version>` 和 `Accept-Encoding: deflate, gzip`。
- 在 ARM64 和 x86/CHR 裝置上，HTTPS 可使用 `http-version=http2`；HTTP/2 響應會用諸如 `:status` 的 HTTP/2 偽頭來表示其頭部。
- 當指令碼把 `as-value` 與 `address=` 和 `src-path=` 一起使用時，fetch 會失敗並報 `Conflicting remote paths provided in URI and parameter`。請改用 `url` 形式，或去掉 `as-value`。

有關所有屬性的說明，請參閱 CLI 參考中的 [`/tool/fetch`](../cli-reference/tool/fetch.md)。
