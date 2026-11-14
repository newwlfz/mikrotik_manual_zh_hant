---
sidebar_key: "cli-reference/file"
title: "file"
sidebar_label: 'file'
source: https://manual.mikrotik.com/docs/cli-reference/file
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## file {#file}
**型別：** 目錄

`/file` 選單列出路由器儲存上的使用者檔案並對其進行管理：建立、編輯、複製和刪除檔案及目錄。對於上傳的 RouterOS `.npk` 檔案，該選單還會顯示軟體包詳細資訊，例如架構和構建時間。透過 [檔案共享](../../network-management/cloud/file-share.md)（Back To Home（遠端回家））共享的檔案和目錄會帶有 shared 標誌，並具有包含分享連結的 `url` 屬性。請參閱 [檔案](../../system-information-and-utilities/files.md) 指南。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="S" typ="shared">該檔案或目錄透過 [檔案共享](../../network-management/cloud/file-share.md)（Back To Home）共享。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="file" mandatory="1">檔案或目錄的名稱，包括路徑。開頭的 `/` 是可選的。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (file | directory)">條目的型別。預設值：file。</ArgTableRow>
<ArgTableRow arg="contents" typ="string">檔案的實際內容。限制為略低於 60 KiB（61439 bytes）：建立內容更長的檔案會失敗，而大於該限制的檔案在此處不會返回任何內容。使用 [`/file/read`](./read.md) 讀取更大的檔案。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="size" typ="num">檔案大小，單位為 bytes。</ArgTableRow>
<ArgTableRow arg="last-modified" typ="date">檔案建立或最後修改的時間。</ArgTableRow>
<ArgTableRow arg="package-name" typ="string">可安裝軟體包的名稱。僅適用於 RouterOS .npk 檔案。</ArgTableRow>
<ArgTableRow arg="package-version" typ="string">可安裝軟體包的版本。僅適用於 RouterOS .npk 檔案。</ArgTableRow>
<ArgTableRow arg="package-build-time" typ="date">軟體包的構建時間。僅適用於 RouterOS .npk 檔案。</ArgTableRow>
<ArgTableRow arg="package-architecture" typ="string">軟體包所針對的架構。僅適用於 RouterOS .npk 檔案。</ArgTableRow>
<ArgTableRow arg="url" typ="string" syscap="cloud-vpn">用於 cloud VPN 檔案共享的 URL。對於透過 [檔案共享](../../network-management/cloud/file-share.md)（Back To Home）共享的檔案和目錄會顯示。</ArgTableRow>
</ArgTable>
