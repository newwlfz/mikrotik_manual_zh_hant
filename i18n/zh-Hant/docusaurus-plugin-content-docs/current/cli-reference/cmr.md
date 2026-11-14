---
sidebar_key: "cli-reference/cmr"
title: "cmr"
source: https://manual.mikrotik.com/docs/cli-reference/cmr
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr {#cmr}
**軟體包：** cmr
**型別：** 設定目錄

CMR 伺服器的設定，該伺服器控制一組 CMR 用戶端。使用 `enabled=yes` 啟用伺服器；隨後它會分發軟體包、發現並跟蹤裝置，並評估用於監控這些裝置的告警規則。有關該軟體包的概述，請參見 [CMR](../management-tools/cmr.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="enum (yes | no)">CMR 伺服器是否啟用。預設值：no.</ArgTableRow>
<ArgTableRow arg="local-id" typ="string" unset="1">唯一的 CMR 專用裝置識別符號。</ArgTableRow>
<ArgTableRow arg="pairing-requirement" typ="enum (none | password | confirm)" unset="1">
定義遠端裝置必須執行哪些操作，本裝置才會接受配對：
- **none** - 本裝置自動接受配對，無需額外檢查
- **password** - 遠端裝置可以透過提供本裝置上 RouterOS 使用者的使用者名稱和密碼來批准配對；CMR 沒有單獨的配對密碼
- **confirm** - 必須在本裝置上執行 `pair` 命令來本地批准配對；無法從遠端側批准
</ArgTableRow>
<ArgTableRow arg="packages-directory" typ="file" unset="1">伺服器檔案系統上包含 RouterOS 軟體包的目錄；當這些軟體包與升級所需版本匹配時，伺服器會將其分發給受管裝置並從這裡提供。該值從路由器的檔案列表中選擇：目錄條目帶尾部斜槓輸入（例如 `cmrpkgs/`），普通檔案則不帶。軟體包按需分別解析：此處已存在所需版本的軟體包會直接傳送，而不會再次下載；只會下載並快取缺失的軟體包。如果值未指向現有目錄，則會保留但無法使用；此時 `/cmr` 選單會顯示 `directory does not exist, using memory`，改為從記憶體提供軟體包。</ArgTableRow>
<ArgTableRow arg="packages-cache-type" typ="enum (directory | memory)" unset="1">伺服器在哪裡儲存其下載的軟體包檔案：`directory` 將它們儲存在伺服器的儲存中，`memory` 將它們儲存在 RAM 中。使用 `directory` 時，伺服器會將它們儲存在 `packages-directory` 的 `cmrcache` 子目錄中，該子目錄由伺服器在路由器的檔案列表中建立；已經存在於 `packages-directory` 中的軟體包會直接從那裡提供，無需下載。當該目錄缺失或不可用時，伺服器會在 `/cmr` 選單中報告 `directory does not exist, using memory`，改為將軟體包儲存在 RAM 中，並在該目錄再次可用時切換回該目錄。</ArgTableRow>
<ArgTableRow arg="packages-cache-limit" typ="num" unset="1">快取中儲存的軟體包資料的最大量，以兆位元組為單位。大於可用 RAM 或儲存空間的值會被接受，伺服器會顯示一條資訊性說明；隨後快取會使用所有可用空間，並在必須儲存大於剩餘空間的檔案時逐出較舊的條目。</ArgTableRow>
<ArgTableRow arg="upgrade-check-interval" typ="time" unset="1">CMR 伺服器檢查 MikroTik 更新伺服器以獲取可用版本的頻率。最小值為 1 分鐘。預設值：`10h`.</ArgTableRow>
<ArgTableRow arg="track-topology" typ="bool" unset="1">啟用網路拓撲發現。從 CMR 用戶端獲取以下資訊：路由、WiFi 登錄檔、ARP 表、鄰居、DHCP 狀態和介面狀態。此資訊是實現完整 CMR 功能所必需的，例如在 `/cmr/layout` 選單中自動發現鏈路。預設值：yes.</ArgTableRow>
<ArgTableRow arg="fetch-comments" typ="bool" unset="1">啟用獲取介面/埠和 WiFi 登錄檔的註釋。預設值：yes。</ArgTableRow>
<ArgTableRow arg="controller-addresses" typ="multi { array-id, address: address (flags=46D)
 }" unset="1">當控制器地址無法自動發現時（MNDP，或 DNS：用戶端解析 `_cmr._tcp.lan` 和 `_cmr._tcp.` 加上來自 DHCP 的域名），傳送到裝置的 CMR 伺服器 IP 地址。</ArgTableRow>
<ArgTableRow arg="apptraffic-devices" typ="object" unset="1">使用標籤選擇要為其收集應用流量資料的裝置。支援 + 和 - 符號分別作為 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。預設值：`gateway`；`all` 選擇所有裝置。</ArgTableRow>
<ArgTableRow arg="auto-labels" typ="alt { auto-labels: enum (none | all) { none:0, all:0xffff }
, auto-labels: ubit (version, architecture, model, board-name, identity, address, ssid)
 }" unset="1">是否從連線的 cmr-client 裝置獲取標籤資訊。可配置為僅獲取特定標籤。預設值：all。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="self-client-id" typ="string" unset="1">CMR 伺服器用於連線自身的 ID，以便在裝置列表中顯示。</ArgTableRow>
</ArgTable>
