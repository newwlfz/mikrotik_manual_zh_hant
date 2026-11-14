---
sidebar_key: "cli-reference/app/settings"
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/cli-reference/app/settings
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## app/settings {#appsettings}
**系統能力：** app
**軟體包：** container
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="disk" typ="enum (none)">用於應用映象、資料和下載的磁碟。由設定嚮導設定。預設值：none。</ArgTableRow>
<ArgTableRow arg="router-ip" typ="ipAddr">用戶端訪問路由器所使用的 IP 地址。應用會在生成的 URL 和埠轉發規則中使用它。預設值：none。在未配置該項的情況下啟用的應用會以 `status=waiting for router ip to be configured` 狀態等待。</ArgTableRow>
<ArgTableRow arg="lan-bridge" typ="iface_enum { none }">用作 LAN 的網橋。預設網路為 `lan` 的應用會將其 VETH 介面接入該網橋。預設值：none。</ArgTableRow>
<ArgTableRow arg="media-path" typ="file">用於存放應用媒體檔案的目錄。預設值：none；RouterOS 使用 `assumed-media-path`。</ArgTableRow>
<ArgTableRow arg="download-path" typ="file">用於存放已下載應用內容的目錄。預設值：none；RouterOS 使用 `assumed-download-path`。</ArgTableRow>
<ArgTableRow arg="show-in-webfig" typ="bool">WebFig 是否在登入頁面上顯示指向已啟用應用的連結。預設值：yes。</ArgTableRow>
<ArgTableRow arg="auto-update" typ="bool">已安裝應用的預設自動更新設定。每個應用都可以透過自身的 `auto-update` 屬性覆蓋它。預設值：no。</ArgTableRow>
<ArgTableRow arg="registry-mirrors" typ="multi { array-id, array-id, src-and-dst: composite { src: string
, dst: string
 }
 }">以 `source:destination` 形式表示的登錄檔映象對映，例如 `*:mirror.example.com` 表示為所有登錄檔使用同一個映象。預設值：none。</ArgTableRow>
<ArgTableRow arg="app-store-urls" typ="multi { array-id, app-store-url: string
 }">自定義 app 商店的 URL。每個 URL 必須返回一個 YAML 應用定義陣列。預設值：none.</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="assumed-router-ip" typ="ipAddr">自動檢測到的路由器 IP 地址（如果可用）。</ArgTableRow>
<ArgTableRow arg="assumed-lan-bridge" typ="iface_enum { none }">自動檢測到的 LAN 網橋（如果可用）。</ArgTableRow>
<ArgTableRow arg="assumed-media-path" typ="file">所選 app 磁碟上的預設媒體目錄。</ArgTableRow>
<ArgTableRow arg="assumed-download-path" typ="file">媒體目錄內的預設下載目錄。</ArgTableRow>
<ArgTableRow arg="certificate-status" typ="string">用於 app HTTPS URL 的證書狀態。`ok` 表示該證書可用。</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)">用於 app HTTPS URL 的證書名稱。</ArgTableRow>
</ArgTable>
