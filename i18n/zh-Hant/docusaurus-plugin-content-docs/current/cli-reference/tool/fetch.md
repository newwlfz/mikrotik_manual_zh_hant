---
sidebar_key: "cli-reference/tool/fetch"
sidebar_position: 7
title: "fetch"
sidebar_label: 'fetch'
source: https://manual.mikrotik.com/docs/cli-reference/tool/fetch
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/fetch {#toolfetch}
**型別：** 命令

從控制檯或指令碼中下載和上傳檔案，併發出 HTTP 請求。參見 [獲取](../../system-information-and-utilities/fetch.md) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="url" typ="string">資源的完整 URL，例如 https://download.mikrotik.com/routeros/7.19/CHANGELOG 或 ftp://user:password@192.168.88.2/conf.rsc。協定方案會選擇模式，ftp/sftp URL 可以攜帶憑據。可以替代單獨的 address 和 src-path 引數。不能在 URL 內指定 VRF：在 http://192.168.88.2@vrf1/ 中，@ 後面的部分會被當作主機名。請使用 address 引數指定 VRF。</ArgTableRow>
<ArgTableRow arg="output" typ="enum (none | file | user | user-with-headers)">
決定獲取的資料儲存在何處。
- `none` - 不儲存下載的資料。
- `file`（預設）- 將下載的資料儲存到檔案中（`dst-path`；使用 `url` 且未指定 `dst-path` 時，檔案以 URL 路徑的最後一部分命名）。
- `user` - 將下載的資料儲存到 `as-value` 的 `data` 值中，最多 64512 位元組（63 KiB）；更長的正文會被截斷且不報錯。
- `user-with-headers` - 將下載的資料儲存到 `data`（最多 20480 位元組，20 KiB），並將響應頭儲存到 `http-headers`（最多 44 KB）。
</ArgTableRow>
<ArgTableRow arg="http-method" typ="enum (get | post | put | delete | head | patch)">
HTTP 請求方法。不帶 `http-data` 的 PUT 和 PATCH 會發送空正文。
- `get`（預設）- 請求資源。
- `post` - 將 `http-data` 傳送到資源。
- `put` - 將 `http-data` 作為資源的新內容傳送。
- `delete` - 刪除資源。
- `head` - 僅請求響應頭。
- `patch` - 將 `http-data` 作為資源的區域性更改傳送。
</ArgTableRow>
<ArgTableRow arg="http-auth-scheme" typ="enum (basic | digest)">用於 `user` 和 `password` 的 HTTP 身份驗證方案。使用 `basic` 時，憑據會隨第一個請求傳送，而不等待質詢。預設值：basic。</ArgTableRow>
<ArgTableRow arg="http-data" typ="string">POST、PUT 和 PATCH 的請求正文。資料上限為 64 KB。如果 `http-header-field` 中沒有 `Content-Type`，則正文以 `application/x-www-form-urlencoded` 傳送。</ArgTableRow>
<ArgTableRow arg="http-header-field" typ="multi { array-id, header-field: string
 }">HTTP 頭欄位和值，形式為 "h1:fff,h2:yyy"：逗號開始下一個頭。要在單個頭值中保留逗號，請用兩個反斜槓對其進行轉義，例如 "h:fff\\,yyy" 會發送 `h: fff,yyy`。Fetch 始終傳送 `User-Agent: RouterOS <version>` 和 `Accept-Encoding: deflate, gzip`。</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum (no | yes | yes-without-crl)">
HTTPS 的 TLS 證書驗證。
- `no`（預設）- 不驗證：即使伺服器使用過期或自簽名證書，fetch 也會連線。
- `yes` - 根據本地證書儲存驗證信任鏈，該儲存包含帶有公共根證書的內建信任儲存。無效證書會使 fetch 失敗，例如出現 `failure: SSL: ssl: cert not valid (after: ... < now: ...)`。
- `yes-without-crl` - 在不進行 CRL 檢查的情況下驗證證書。
</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum">證書儲存中用於 HTTPS 模式下伺服器驗證的證書。僅在啟用 `check-certificate` 時適用。</ArgTableRow>
<ArgTableRow arg="address" typ="alt { address: address (flags=46vi)
, address: ipAddr
 }">目標裝置的 IP 地址或主機名。追加 @vrf_name 以在特定 VRF 內執行 fetch 操作，或者僅設定 address=@vrf_name，並讓 url 引數提供地址。</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ip6: ip6Addr
 }">用於建立連線的源 IP 地址。僅適用於 HTTP、HTTPS 和 SFTP 模式。</ArgTableRow>
<ArgTableRow arg="port" typ="num">用於連線的埠。預設值：該模式的埠（`http` 為 80，`https` 為 443，`ftp` 為 21，`sftp` 為 22，`tftp` 為 69），或 `url` 中給出的埠。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (http | https | ftp | tftp | sftp)">
用於連線的協定。使用 `url` 時，協定來自 URL 方案。
- `http`（預設）- HTTP。
- `https` - 基於 TLS 的 HTTP。
- `ftp` - FTP；下載和上傳。
- `tftp` - TFTP；從 TFTP 伺服器下載，例如另一臺路由器上的 `/ip/tftp`。
- `sftp` - 基於 SSH 的 SFTP；下載和上傳。
</ArgTableRow>
<ArgTableRow arg="http-content-encoding" typ="enum (deflate | gzip)">使用 gzip 或 deflate 壓縮 `http-data`，並新增匹配的 `Content-Encoding` 頭。僅適用於 POST 和 PUT 方法。</ArgTableRow>
<ArgTableRow arg="ip-type" typ="enum (any | ipv4 | ipv6)">
解析域名時的 IP 地址族偏好。
- `any`（預設）- 使用 IPv4 或 IPv6。
- `ipv4` - 僅使用 IPv4。
- `ipv6` - 僅使用 IPv6。
</ArgTableRow>
<ArgTableRow arg="src-path" typ="file">遠端檔案的路徑；使用 `upload=yes` 時，為要上傳的本地檔案。</ArgTableRow>
<ArgTableRow arg="dst-path" typ="file">儲存獲取檔案的目標路徑；使用 `upload=yes` 時，為遠端裝置上的檔名。未指定 `dst-path` 時，下載檔案以 URL 路徑的最後一部分命名。</ArgTableRow>
<ArgTableRow arg="user" typ="string">用於在遠端裝置上進行身份驗證的使用者名稱。未指定 `user` 時，FTP 以 `anonymous` 登入，HTTP 不傳送憑據。</ArgTableRow>
<ArgTableRow arg="password" typ="string">`user` 的密碼。指定 `user` 但未指定 `password` 時，HTTP 會發送空密碼。</ArgTableRow>
<ArgTableRow arg="host" typ="string">遠端 Web 伺服器的主機名或虛擬主機名。當同一 IP 服務多個虛擬主機時很有用。例如，`address=manual.mikrotik.com host=forum.mikrotik.com`。</ArgTableRow>
<ArgTableRow arg="ascii" typ="bool">為 FTP/TFTP 傳輸啟用 ASCII 模式。預設值：no。</ArgTableRow>
<ArgTableRow arg="upload" typ="bool">為 FTP 和 SFTP 傳輸啟用上傳模式：`src-path` 是本地檔案，`dst-path`（或 `url` 中的路徑）是遠端裝置上的名稱。不支援 HTTP 上傳；請將 `http-method=put` 與 `http-data` 一起使用。預設值：no。</ArgTableRow>
<ArgTableRow arg="sftp-known-hosts-ignore" typ="bool">為此 SFTP 傳輸跳過 SSH 主機金鑰驗證。當 /ip/ssh 中的 known-hosts-validation 已啟用時有效；未啟用驗證時，接受任何主機金鑰。預設值：no。</ArgTableRow>
<ArgTableRow arg="keep-result" typ="bool">已棄用，請改用 output 引數。</ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="alt { idle-timeout: time [1 .. 604800]
, idle-timeout: enum (none) { none:0 }
 }">自上次讀/寫操作以來的空閒超時。預設值：10s。</ArgTableRow>
<ArgTableRow arg="http-max-redirect-count" typ="num">fetch 遵循的 HTTP 重定向最大次數。預設值為 2 時，會遵循由兩次重定向組成的鏈，而第三次重定向會使 fetch 失敗，並返回收到的 3xx 狀態。預設值：2。</ArgTableRow>
<ArgTableRow arg="http-percent-encoding" typ="bool">對請求路徑中的每個字元進行百分號編碼，但字母數字以及 `-._~/?^=:` 除外。預設值：no。</ArgTableRow>
<ArgTableRow arg="http-version" typ="enum (http1_1 | http2 | http2-forced)">HTTP 協定版本。HTTP2 僅在 ARM64 和 x86/CHR 裝置上受支援。預設值：http1_1。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="enum (none | connecting | requesting | downloading | uploading | finished | failed)">fetch 操作的當前狀態。</ArgTableRow>
<ArgTableRow arg="code" typ="num">伺服器返回的 HTTP 狀態碼。</ArgTableRow>
<ArgTableRow arg="downloaded" typ="num">已下載的資料量，單位為 KiB，向下取整；當有資料到達時至少為 1（7 位元組和 2047 位元組都顯示為 1）。使用 `output=user` 時，為儲存在 `data` 中的資料量；將 `[:len ($r->"data")]` 與限制比較，以檢測正文是否被截斷。</ArgTableRow>
<ArgTableRow arg="uploaded" typ="num">已上傳的資料量，單位為 KiB，向下取整。</ArgTableRow>
<ArgTableRow arg="total" typ="num">傳輸的總大小，單位為 KiB，向下取整。</ArgTableRow>
<ArgTableRow arg="duration" typ="time">fetch 操作的總持續時間。</ArgTableRow>
<ArgTableRow arg="data" typ="string">當 `output` 為 `user`（至多 64512 位元組）或 `user-with-headers`（至多 20480 位元組）時獲取的資料。更長的正文會被截斷而不報錯。</ArgTableRow>
<ArgTableRow arg="http-headers" typ="object { http-header: super { key: string
, [value] : string
 }
 }">伺服器返回的 HTTP 頭。</ArgTableRow>
</ArgTable>
