---
sidebar_key: "cli-reference/ip/tftp"
title: "tftp"
sidebar_label: 'tftp'
source: https://manual.mikrotik.com/docs/cli-reference/ip/tftp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/tftp {#iptftp}
**型別：** 目錄

TFTP 伺服器的訪問規則。只要至少存在一條規則，伺服器就會執行（`/ip/service` 中 UDP 埠 69 上的動態 `tftpd` 條目）。每個請求都會按順序與規則進行匹配，第一條同時匹配用戶端地址和請求檔名的規則起決定作用；沒有任何規則匹配的請求會被拒絕，並返回 `permission denied!`。參見 [TFTP](../../../system-information-and-utilities/tftp.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該規則已停用，不會被使用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ip-addresses" typ="object { ip-addresses: alt { ip6: ip6Prefix
, ip: ipRange
 }
 }">該規則適用的用戶端地址：IPv4 地址、範圍或字首，或 IPv6 字首。空值（預設）表示任意用戶端。</ArgTableRow>
<ArgTableRow arg="req-filename" typ="string">作為正則表示式的請求檔名；空值（預設）匹配任意名稱。區分大小寫。不以 `^` 開頭的值必須匹配整個名稱（`phone\.cfg` 只匹配 `phone.cfg`，`.*\.cfg` 匹配每個 `.cfg` 名稱）；錨點會新增在整個值的前後，因此請將備選項寫在分組中，例如 `(aaa|bbb)\.bin`。以 `^` 開頭的值按原樣使用。這裡的名稱是用戶端請求的名稱，而不是路由器上的路徑。在提供資料夾或所請求名稱的規則中，諸如 `.*` 這樣的模式或空值也會匹配指向資料夾外部的名稱：請使用諸如 `[^/.][^/]*` 這樣的模式，該模式不允許斜槓，也不允許開頭的點。</ArgTableRow>
<ArgTableRow arg="real-filename" typ="string">該規則所提供的內容。為空（預設）時提供所請求的名稱本身；檔案表示為每個匹配的請求提供該檔案；資料夾會置於所請求名稱之前（`real-filename=tftp` 對 `phone.cfg` 或 `/phone.cfg` 的請求以 `tftp/phone.cfg` 應答）。上傳內容會寫入同一位置。該值按字面使用：不支援諸如 `\1` 這樣引用 `req-filename` 各部分的寫法。</ArgTableRow>
<ArgTableRow arg="allow" typ="bool">`yes` 允許匹配的請求，`no` 會以 `permission denied!` 拒絕這些請求。預設值：yes。</ArgTableRow>
<ArgTableRow arg="read-only" typ="bool">當為 `yes` 時，上傳會失敗並返回 `illegal operation`。設定為 `no` 可接受上傳。預設值：yes。</ArgTableRow>
<ArgTableRow arg="allow-rollover" typ="bool">允許傳輸超過 65535 個塊：在第 65535 塊之後，路由器會從第 0 塊繼續，用戶端必須支援這一點。如果未啟用，此類傳輸會在達到限制時失敗並返回 `illegal operation`。預設值：no。</ArgTableRow>
<ArgTableRow arg="allow-overwrite" typ="bool">當 `read-only=no` 時，允許上傳替換現有檔案。如果未啟用，上傳會失敗並返回 `file exists`。預設值：no。</ArgTableRow>
<ArgTableRow arg="reading-window-size" typ="alt { window-size: enum (none | pipelining) { none:0 }
 }">
- `none`（預設）- 在前一個塊被確認後傳送下載的每個塊。
- `pipelining` - 在等待確認之前傳送下載的多個塊，從而加快下載速度。
</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hits" typ="num">該規則應答的請求數。</ArgTableRow>
</ArgTable>
