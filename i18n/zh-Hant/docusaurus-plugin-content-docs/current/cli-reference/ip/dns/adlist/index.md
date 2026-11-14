---
sidebar_key: "cli-reference/ip/dns/adlist"
title: "adlist"
sidebar_label: 'adlist'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dns/adlist
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dns/adlist {#ipdnsadlist}
**型別：** 目錄

Ad-blocking 列表。路由器對這些列表中的名稱的 A 和 AAAA 查詢回覆 `0.0.0.0` 和 `::`（TTL 2 秒），而不是向上遊詢問；其他查詢型別（如 MX 或 HTTPS）則轉發到上游。僅精確名稱被阻止，其子域不受影響。這些名稱儲存在 DNS 快取記憶體中，並計入 [`/ip/dns`](../index.md) 的 `cache-size`：每個名稱佔用約 75 位元組，因此 76 500 個名稱約佔用 5.6 MiB。當快取太小時，匯入會停止，並記錄日誌訊息 `adlist read: max cache size reached` 和 `could not add name, stopping import`，`name-count` 顯示已匯入的名稱數量；之後提高 `cache-size` 不會補全列表，因此請刪除該 adlist 並重新新增。停用 adlist 不會釋放其名稱佔用的快取記憶體：在列表被刪除之前，它們仍計入 `cache-size`。路由器每 4 小時重新檢查一次列表。最多可新增 64 個 adlist。靜態 `FWD` 條目可使某個名稱豁免所有 adlist；僅靜態 A 條目則不行。有關示例，請參閱 [DNS](../../../../network-management/dns.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該 adlist 已停用，不會攔截任何內容。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="file" typ="file">
路由器上包含要攔截名稱的檔案，格式與 `/file/print` 顯示的一致。每行一個名稱，使用小寫，格式為以下之一：
- `0.0.0.0 name`、`127.0.0.1 name` 或 `::1 name` - Hosts 檔案格式。
- `name` - 僅名稱。

以 `#` 開頭的行以及名稱後的註釋會被忽略。不支援 `*.example.com` 等萬用字元以及一行包含多個名稱。
</ArgTableRow>
<ArgTableRow arg="url" typ="string">列表的 URL，格式與 `file` 相同，例如公共 hosts 檔案。路由器會下載該列表並在其儲存中保留一份副本（不會顯示在 `/file` 中）。</ArgTableRow>
<ArgTableRow arg="ssl-verify" typ="bool">路由器是否根據內建信任儲存和 `/certificate` 中的證書來驗證 `url` 伺服器的證書。檢查失敗時，路由器不會匯入該列表，並在 `dns` 主題中記錄 `http client error: SSL: ...`。對於使用自簽名證書的伺服器，匯入其 CA 證書或設定 `ssl-verify=no`。預設值：yes.</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="match-count" typ="num">從此列表應答的查詢數量。</ArgTableRow>
<ArgTableRow arg="name-count" typ="num">從此列表匯入的名稱數量。</ArgTableRow>
</ArgTable>
