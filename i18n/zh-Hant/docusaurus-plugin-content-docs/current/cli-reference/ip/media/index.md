---
sidebar_key: "cli-reference/ip/media"
title: "media"
sidebar_label: 'media'
source: https://manual.mikrotik.com/docs/cli-reference/ip/media
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/media {#ipmedia}
**條件：** !smips
**型別：**目錄

DLNA 媒體伺服器。每個條目會將磁碟資料夾中的媒體檔案共享給一個介面上的播放器：它會在該介面上透過 SSDP 宣告自身，並透過 HTTP 在 TCP 埠 2828 上提供這些檔案。標記為 `D` 的條目由磁碟媒體共享建立（`/disk` 中的 `media-sharing`，`/disk/settings` 中的 `auto-media-sharing`）。請參閱 [DLNA 媒體伺服器](../../../storage/dlna.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用：伺服器不執行。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態：由磁碟媒體共享為磁碟或 tmpfs 資料夾建立（`media-sharing` 位於 `/disk`，或 `auto-media-sharing` 位於 `/disk/settings`），名稱取自 identity 和磁碟槽位。動態條目無法編輯或移除（`failure: can't edit dynamic object`）；請改為關閉該磁碟的 `media-sharing`。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="path" typ="file">伺服器共享其媒體檔案的磁碟資料夾，例如 `usb1/media`，或磁碟的根資料夾（`usb1`）。沒有 `path` 時，伺服器共享路由器的整個檔案列表。其子資料夾顯示為資料夾。副檔名為小寫的影片、音樂和圖片檔案會被列出；其他檔案以及副檔名為大寫的檔案（例如 `.MP4`）不會。資料夾不存在時，`status` 會顯示 `Error, can't find directory`。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">伺服器執行的介面。伺服器僅在此介面上宣告自身並提供請求。監聽器會在所有介面上接受連線，但若針對此伺服器的請求從另一介面到達，則會收到 HTTP 404 錯誤；防火牆會阻止 WAN 訪問。</ArgTableRow>
<ArgTableRow arg="friendly-name" typ="string">播放器為伺服器顯示的名稱。預設值：MikroTik Home Media Server。</ArgTableRow>
<ArgTableRow arg="allowed-ip" typ="ipAddr">伺服器僅提供服務的唯一 IP 地址。其他裝置不會獲得內容。只能有一個地址；子網會被拒絕。`0.0.0.0` 允許該介面上的所有裝置。不能與 `allowed-hostname` 同時設定。預設值：0.0.0.0。</ArgTableRow>
<ArgTableRow arg="allowed-hostname" typ="string">僅允許此主機名對應的 IP 地址訪問內容，該主機名由此路由器的 DHCP 伺服器所知（租約的 `host-name`）。匹配為精確匹配且區分大小寫。留空允許所有裝置。不能與 `allowed-ip` 同時設定（`failure: can't set both allowed IP and allowed hostname`）。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">
- `Running` - 伺服器執行並提供檔案。
- `Error, can't find directory` - `path` 中的資料夾不存在。
</ArgTableRow>
</ArgTable>
