---
sidebar_key: "cli-reference/app/settings/index"
sidebar_position: 5
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/7.24/cli-reference/app/settings
captured_at: '2026-11-01T21:26:18+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## app/settings {#appsettings}
**系統能力：** app
**軟體包：** container
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="disk" typ="enum (none)">全域性設定，指定用於儲存操作的磁碟</ArgTableRow>
<ArgTableRow arg="router-ip" typ="ipAddr">手動指定當前 RouterOS 裝置可被訪問到的 IP 地址</ArgTableRow>
<ArgTableRow arg="lan-bridge" typ="iface_enum { none }">手動指定代表區域網路（LAN）的橋接介面</ArgTableRow>
<ArgTableRow arg="media-path" typ="file">手動指定存放所有媒體檔案的目錄路徑</ArgTableRow>
<ArgTableRow arg="download-path" typ="file">手動指定存放所有已下載內容的目錄路徑</ArgTableRow>
<ArgTableRow arg="show-in-webfig" typ="bool">控制是否在 WebFig 登入頁面上顯示已啟用應用的連結</ArgTableRow>
<ArgTableRow arg="auto-update" typ="bool">全域性設定，為所有已安裝的應用包啟用自動更新</ArgTableRow>
<ArgTableRow arg="registry-mirrors" typ="multi { array-id, array-id, src-and-dst: composite { src: string
, dst: string
 }
 }">指定一個或多個用於拉取容器映象的 registry 映象 URL</ArgTableRow>
<ArgTableRow arg="app-store-urls" typ="multi { array-id, app-store-url: string
 }">自定義應用商店的 URL。必須指向一個 YAML 陣列，其中每個應用為一個元素</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="assumed-router-ip" typ="ipAddr">自動檢測到的 RouterOS 裝置網路 IP 地址</ArgTableRow>
<ArgTableRow arg="assumed-lan-bridge" typ="iface_enum { none }">自動檢測到的用於 LAN 連線的橋接介面</ArgTableRow>
<ArgTableRow arg="assumed-media-path" typ="file">預設媒體儲存路徑，通常位於系統磁碟上</ArgTableRow>
<ArgTableRow arg="assumed-download-path" typ="file">預設下載目錄路徑，通常位於媒體儲存區域內</ArgTableRow>
<ArgTableRow arg="certificate-status" typ="string"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>
