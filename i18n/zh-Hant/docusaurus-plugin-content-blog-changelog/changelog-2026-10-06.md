---
title: "文件更新 - 2026年10月6日"
date: 2026-10-06
slug: /changelog-2026-10-06
source: https://manual.mikrotik.com/changelog/changelog-2026-10-06
captured_at: '2026-11-04T06:09:01+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026年10月6日文件變更摘要。

## 管理工具 {#management-tools}

- **[CMR](/docs/management-tools/cmr)**：告警規則部分現在將狀態告警與事件告警分開，並用一個表格進行比較：

- 狀態告警（CPU、記憶體、磁碟和健康閾值，connected、disconnected-more-than、upgrade-available）在所有條件匹配期間保持活動。它在變為活動時執行一次動作，並在 devices-on 和儀表板中計數，直到清除。
- 事件告警（interface-change、upgrade-done、upgrade-job-done、rebooted、unpaired-device-connected，或由 log-topics 和 log-regex 匹配的日誌訊息）每次發生都執行其動作，且從不保持活動。一條規則可以組合多個狀態條件，但最多有一個事件條件。
- 新增“裝置和系統範圍”部分：大多數告警按裝置應用，而 upgrade-job-done 是系統告警，報告整個升級作業而不帶裝置上下文。
- show-devices 列出規則的狀態告警處於活動狀態的裝置。對於事件告警，它不列出任何裝置，其 fired 值改為統計發生次數。

- **[CMR](/docs/management-tools/cmr)**、**[CMR-Client](/docs/management-tools/cmr/client)**：關於連線和配對用戶端的更正：

- 用戶端透過 TCP 埠 54321 連線到伺服器。在伺服器的 input 鏈以及用戶端與伺服器之間的任何防火牆中允許該埠。用戶端針對 status: searching 的故障排除現在指向該埠和防火牆。
- 用戶端的 pairing-requirement 支援 none 和 password。confirm 僅存在於伺服器上，由 /cmr/device/pair 批准配對。用戶端側的 confirm 情況已從故障排除列表中移除。

- **[CMR](/docs/management-tools/cmr)**、**[CMR-Client](/docs/management-tools/cmr/client)**：升級、重啟和告警的詳細資訊：

- 不帶 channel 的 /cmr/device/upgrade 會在每臺裝置各自的升級通道上升級該裝置，而使用 schedule-time 時，作業會等待該時間的下一次出現。它為按編號選擇的裝置啟動作業時沒有標籤，而 run-next 會自行啟動以這種方式計劃的作業。
- 刪除已計劃作業會將其標記為 cancelled 並保留在列表中。刪除已取消的作業會將其刪除。
- 列出了伺服器關於裝置升級結果、新可用版本和重啟的日誌訊息。reboot 會立即返回。
- 告警變數：[state] 對於已配對且沒有進行中任務的裝置為空，使用率值在裝置報告之前為 unknown，[upgrade-error] 在成功升級後為空，[upgrade-state] 是裝置在作業中的最終狀態，作業時間的形式為 2026.10.06-14:20:36。
- 當 CMR 在伺服器上重啟時，仍然匹配的狀態告警會再次變為活動並執行其動作。
- REST API 會將 WiFi 密碼短語返回給具有 sensitive 策略的使用者。
- 用戶端會記錄其狀態的每次變更，並在與伺服器的連線斷開時使用現有配對重新連線。

- **[CMR](/docs/management-tools/cmr)**、**[CMR-Client](/docs/management-tools/cmr/client)**：預設值和伺服器設定：

- fail-policy 預設為 stop，並且 strategy=parallel 的 stop 不再需要 order。只有 continue-order 才需要它。
- upgrade-check-interval 預設為 10h。apptraffic-devices 預設為閘道器標籤，all 表示選擇每臺裝置。
- 用戶端的 pairing-requirement 預設為 password。
- 用戶端透過鄰居發現或 DNS 查詢伺服器：用戶端解析 _cmr._tcp.lan 以及 _cmr._tcp. 後跟來自 DHCP 選項 15 的域名。僅靠 DHCP 不會通告伺服器。
- /cmr set !&lt;setting&gt; 會將設定恢復為預設值。更改 packages-directory、upgrade-check-interval 或 pairing-requirement 會重啟伺服器上的 CMR，因此每個用戶端都會重新連線，狀態告警也會再次觸發。
- 更改已啟用的告警規則，即使只更改其註釋，也會使該規則的狀態告警在匹配的裝置上再次觸發。
- 在佈局連結的 links 值中，埠名前的 * 表示直接物理鏈路。它不表示 PoE 供電方。

- **[CMR](/docs/management-tools/cmr)**：節點座標相對於佈局中心：x 向右增加，y 向下增加，因此較小的 y 會將節點放置在圖上更高的位置。
- **[SSH](/docs/management-tools/ssh)**：頁面已圍繞 SSH 伺服器、互動式用戶端和指令碼化使用重新組織。新增的“驗證遠端主機金鑰”部分說明了 known-hosts-validation 設定（新安裝時啟用，升級時保持原樣）、/system/ssh 的互動式信任和金鑰更新提示，以及在使用驗證時讓 ssh-exec 和 SFTP fetch 正常工作的方式：在 /ip/ssh/known-hosts 中固定金鑰、known-hosts-ignore 或 known-hosts-trusted-subnets。“伺服器主機金鑰”部分記錄了指紋、重新生成以及匯出檔名。匯入用戶端私鑰現在列出了可接受的 PEM 格式，並說明 OpenSSH 私鑰會被拒絕。ssh-exec 示例不再包含明文密碼，並說明了其先決條件。

## CLI 參考 {#cli-reference}

- **[/cmr/alert](/docs/cli-reference/ip/dhcp-server/alert)**、**[show-devices](/docs/cli-reference/cmr/alert/show-devices)**：描述遵循狀態和事件拆分。connected 是狀態條件，rebooted 和日誌條件是事件條件，devices-on 僅統計活動的狀態告警，reset-on-disconnect 適用於狀態告警。show-devices 列出規則的狀態告警處於活動狀態的裝置。
- **[/cmr](/docs/cli-reference/cmr)**：pairing-requirement=password 使用裝置上 RouterOS 使用者的使用者名稱和密碼，如 [CMR](/docs/management-tools/cmr#pairing) 指南中所述。CMR 沒有單獨的配對密碼。
- **[/cmr/device/upgrade](/docs/cli-reference/cmr/device/upgrade)**、**[reboot](/docs/cli-reference/system/reboot)**、**[/cmr/upgrade/job](/docs/cli-reference/system/script/job)**、**[run-next](/docs/cli-reference/cmr/upgrade/job/run-next)**：裝置升級的 channel 和 schedule-time 的描述、其作業的空標籤和 channel、以這種方式計劃的作業的 run-next，以及重啟後的日誌訊息。
- **[/cmr](/docs/cli-reference/cmr)**、**[/cmr/client](/docs/cli-reference/cmr/client)**、**[/cmr/upgrade](/docs/cli-reference/cmr/upgrade)**、**[/cmr/device/upgrade](/docs/cli-reference/cmr/device/upgrade)**、**[/cmr/layout/link](/docs/cli-reference/cmr/layout/link)**：upgrade-check-interval、apptraffic-devices、fail-policy 和用戶端 pairing-requirement 的預設值，controller-addresses 中的 DNS 發現，僅 continue-order 需要 order，以及 links 中的 *。
- **[/cmr/client](/docs/cli-reference/cmr/client)**、**[/tool/apptraffic](/docs/cli-reference/tool/apptraffic)**、**[/system/routerboard/usb](/docs/cli-reference/system/routerboard/usb)**：沒有 RouterOS 7 版本的 MIPS-LE 架構（mipsel）不再列在這些頁面的條件中，也不再列在 [CMR](/docs/management-tools/cmr#application-traffic) 指南的應用流量說明中。/system/routerboard/settings/keep-frequency 頁面已移除：該命令僅存在於 MIPS-LE 裝置上。
- **[/ip/ssh](/docs/cli-reference/ip/ssh)**、**[known-hosts](/docs/cli-reference/ip/ssh/known-hosts)**、**[/system/ssh](/docs/cli-reference/system/ssh)**、**[/system/ssh-exec](/docs/cli-reference/system/ssh-exec)**：所有引數說明均已填寫，包括主機金鑰驗證設定以及以前未記錄的 host、key、port 和 vrf 引數。ssh-exec 現在記錄了遠端命令失敗時其 exit-code 和 output 攜帶的內容。
- **[/interface/wifi/radio](/docs/cli-reference/interface/wifi/radio)**：刪除了對未釋出的“meshpoint”模式的引用。
- **[/ip/dns/adlist](/docs/cli-reference/ip/dns/adlist)**、**[DNS](/docs/network-management/dns)**：停用 adlist 不會釋放其快取記憶體。

## 行動網路 {#mobile-networking}

- **[LTE/5G](/docs/mobile-networking/lte-5g)**：新增“Multi APN”部分：使用 show-capabilities 檢查 max-apn-count，為每個額外 APN 連線建立帶 master= 的從屬 LTE 介面，並且介面的 apn-profiles 引數已重新命名為 apn-profile（對於單 APN 配置，舊名稱仍被接受）。

## 防火牆與 QoS {#firewall--qos}

- **[封包流](/docs/firewall-and-quality-of-service/packet-flow-in-routeros)**：封包流圖已更新。

## 硬體 {#hardware}

- **[CRS310-8G+2S+IN](/hardware/crs310-8g-plus-2s-plus-in)**：復位按鈕部分列出了它的三個功能。配置重設現在等待 PWR LED 閃爍，而不是 USR LED，並且 Netinstall 描述了 Regular Booter（開機後按 Reset 1–2 秒）和 Backup Booter（開機時按住 Reset，直到 LED 閃爍、變為常亮，然後熄滅）。
