---
sidebar_key: "cli-reference/ip/cloud/back-to-home-user"
title: "back-to-home-user"
sidebar_label: 'back-to-home-user'
source: https://manual.mikrotik.com/docs/cli-reference/ip/cloud/back-to-home-user
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/cloud/back-to-home-user {#ipcloudback-to-home-user}
**系統能力：** cloud-vpn
**型別：** 目錄

Back To Home（遠端回家） 使用者。每個使用者都是 `back-to-home-vpn` 介面的一個 WireGuard 用戶端，擁有自己的金鑰和地址，路由器會為其新增一個動態對等體。Back To Home 應用會為它建立的每個隧道建立一個使用者：`name` 是手機的型號識別符號，例如 `iPhone18,1`，而 comment 是應用中顯示的隧道名稱。多個使用者可以具有相同的名稱。[`show-client-config`](./show-client-config.md) 會列印某個使用者的用戶端配置。只有在 Back To Home 執行時（`vpn-status: running`）才能新增使用者；否則，`add` 會失敗並顯示 `back-to-home vpn not enabled`。撤銷 Back To Home（`back-to-home-vpn=revoked-and-disabled` 在 [`/ip/cloud`](../index.md) 中）會刪除所有使用者。有關概述，請參閱 [Back To Home](../../../../network-management/cloud/back-to-home.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該使用者已停用。</ArgTableRow>
<ArgTableRow arg="A" typ="active">該使用者處於活動狀態。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">使用者的名稱。名稱不必唯一；Back To Home 應用使用手機的型號識別符號。用戶端配置會在 `# Name` 註釋行中包含使用者的註釋；如果沒有註釋，則包含名稱；Back To Home 應用會將這個註釋行用作隧道名稱。</ArgTableRow>
<ArgTableRow arg="expires" typ="alt { expires: enum (never) { never:0xFFFFFFFF }
, interval: time
, date-time: date
 }">使用者停止工作的時間：`never`（預設）、日期和時間（例如 `"2026-10-01 00:00:00"`）或時間間隔（例如 `1d`）。路由器會將時間間隔轉換為日期。使用者建立後無法更改該值：`set` 會接受它，但保留舊日期。要更改它，請重新建立使用者。</ArgTableRow>
<ArgTableRow arg="client-dns" typ="address (flags=46/)">寫入使用者用戶端配置（`DNS =`）的 DNS 伺服器。沒有它時，配置中沒有 DNS 行，用戶端會保留自己的 DNS 伺服器。</ArgTableRow>
<ArgTableRow arg="client-allowed-address" typ="multi { client-allowed-address: address (flags=46/)
 }">用戶端透過隧道傳送的地址，會作為路由器對等體的 `AllowedIPs` 寫入用戶端配置，例如 `192.168.88.0/24` 表示僅訪問本地網路。預設：空（`0.0.0.0/0, ::/0`，所有流量）。</ArgTableRow>
<ArgTableRow arg="allow-lan" typ="bool">使用者是否可以訪問本地網路。為 `no` 時，路由器會將使用者地址放入動態地址列表 `back-to-home-lan-restricted-peers`，並且一條動態轉發規則會丟棄其發往 `LAN` 介面列表的流量，因此該使用者只能透過路由器使用網際網路。預設：no。</ArgTableRow>
<ArgTableRow arg="private-key" typ="string">使用者用戶端配置的私鑰。未設定時，路由器會生成它。</ArgTableRow>
<ArgTableRow arg="public-key" typ="string">使用者的公鑰。未設定時，路由器會從生成的金鑰推匯出它。</ArgTableRow>
<ArgTableRow arg="file-access" typ="enum (disabled | read-only | full)">
使用者透過 File Share 服務訪問 `file-access-path` 中檔案的許可權。新增具有檔案訪問許可權的使用者會使路由器請求 File Share 證書。
- `disabled`（預設） - 無檔案訪問許可權。
- `read-only` - 讀取檔案。
- `full` - 讀取和更改檔案。
</ArgTableRow>
<ArgTableRow arg="file-access-path" typ="string">使用者可透過 `file-access` 訪問的目錄，以 `/file/print` 顯示的形式表示。當 `file-access` 不是 `disabled` 時為必填；否則，新增使用者會失敗並提示 `invalid files path`。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="client-address" typ="multi { address: address (flags=46/)
 }">使用者在隧道中的 IPv4 和 IPv6 地址，即從 192.168.216.0/24 和 fc00:0:0:216::/64 中分配的下一個空閒地址。由路由器分配；無法設定。</ArgTableRow>
<ArgTableRow arg="file-access-token" typ="string">路由器為使用者檔案訪問生成的令牌。當 `file-access` 不為 `disabled` 時，用戶端配置會將其包含在 `# FilesToken` 行中。</ArgTableRow>
</ArgTable>
