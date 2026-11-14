---
sidebar_key: "cli-reference/system/package/local-update/mirror/index"
sidebar_position: 2
title: "mirror"
sidebar_label: 'mirror'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/package/local-update/mirror
captured_at: '2026-11-01T21:25:36+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/package/local-update/mirror {#systempackagelocal-updatemirror}
**型別：** 設定目錄

你可以使用此選單從主本地軟體包伺服器映象軟體包（適用於所有架構）。下載的軟體包會儲存到根目錄下的 `packs` 資料夾中。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">是否啟用定期檢查並從本地軟體包伺服器下載軟體包。</ArgTableRow>
<ArgTableRow arg="primary-server" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">主本地軟體包伺服器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="secondary-server" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">備用本地軟體包伺服器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="check-interval" typ="time">裝置檢查本地軟體包伺服器是否有新軟體包可用的時間間隔。如果發現新軟體包，就會開始下載該軟體包。僅下載裝置上尚不存在的軟體包。</ArgTableRow>
<ArgTableRow arg="user" typ="string">用於訪問本地軟體包伺服器的使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string">用於訪問本地軟體包伺服器的密碼。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="software-id" typ="string">裝置的軟體 ID。</ArgTableRow>
</ArgTable>
