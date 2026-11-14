---
title: "文件更新 - 2026年9月30日"
date: 2026-09-30
slug: /changelog-2026-09-30
source: https://manual.mikrotik.com/changelog/changelog-2026-09-30
captured_at: '2026-11-04T06:08:53+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 9 月 30 日文件變更摘要。

## 診斷與監控 {#diagnostics--monitoring}

- **[Ping](/docs/diagnostics-monitoring-and-troubleshooting/ping)**：圍繞讀者實際要完成的任務重寫，所有輸出均在 RouterOS 7.26 上透過三跳測試網路捕獲：

- 按地址和按名稱檢查網際網路連通性；無法解析的名稱會以 resolve failed 失敗。
- 一張狀態值表格（timeout、net unreachable、host unreachable、admin prohibited、TTL exceeded、no route to host、兩個 Don't Fragment 狀態以及 echo reply）及各自的含義。
- 用 do-not-fragment 查詢路徑 MTU：哪臺路由器會應答、為什麼更大的 ping 隨即失敗，以及透過 MSS clamping 進行的修復。
- 從 LAN 地址發起 ping 以測試 IPsec 隧道、從 VRF 發起 ping，以及透過帶 src-address 和路由規則的政策路由表發起 ping。
- 用 ARP ping 和 ND ping 訪問丟棄 ICMP 的主機，用 ff02::1 發現 IPv6 主機，對 MAC 地址執行 ping，並在指令碼中使用 ping。
- 已更正：size 是整個 IP 包（含包頭），因此 size=1500 相當於 Windows 上的 ping -l 1472；晚於 interval 的應答會被計為 timeout；WinBox 4 和 WebFig 使用路由器的 DNS 解析名稱（只有 WinBox 3 使用電腦的 DNS）。

- **[Traceroute](/docs/diagnostics-monitoring-and-troubleshooting/traceroute)**：從一個兩跳示例重寫為閱讀跟蹤結果的指南。它解釋了各列的含義以及 RouterOS 如何執行跟蹤（ICMP 探測、最多 30 跳、多輪重複並給出每跳統計）。新增了故障排查案例，每個案例都附有捕獲的輸出：某些跳不再應答、某臺路由器拒絕流量（status 列顯示 network unreachable、host unreachable 和 packet filtered）、路由環路、某一跳的丟包但並非路徑丟包，以及往返時間持續上升。此外新增：使用 use-dns 獲取主機名、用 do-not-fragment 找出 MTU 較小的那一跳，以及從 VRF 或指定源地址進行跟蹤。
- **[Torch](/docs/diagnostics-monitoring-and-troubleshooting/torch)**：重寫了輸出含義的說明，並在 RouterOS 7.26 上用已知大小和速率的流量做了測試。每一行是一個流。SRC-ADDRESS 始終是被監視介面的對端，因此在 LAN 網橋上，TX 是主機下載的流量，RX 是主機上傳的流量。新增了帶捕獲輸出的任務：找出佔用頻寬的主機、監視某個協定或埠、檢查 VLAN 標籤和 DSCP 標記（只在一個方向上標記的流會顯示為兩行）、檢視被防火牆丟棄的流量，以及檢視哪個 CPU 處理某個流。已更正：port 只接受一個埠（舊的 port=80,443 示例會失敗）；Torch 執行期間 IP fast path 和 FastTrack 處於關閉狀態。
- **[IP Scan](/docs/diagnostics-monitoring-and-troubleshooting/ip-scan)**：圍繞任務進行了重寫，輸出在 RouterOS 7.26 上捕獲：查詢 LAN 上的裝置、確認某個地址是否空閒、透過在某個介面上監聽來找出使用未知靜態地址的裝置（然後用臨時地址訪問它），以及掃描遠端網路。新增：掃描會發送什麼（ARP、ping、用於獲取系統名稱的 SNMP 查詢、NetBIOS 查詢、反向 DNS 查詢，以及一個 BOOTP 請求）。已更正：同時設定 interface 和 address-range 時會掃描該範圍，因此刪除了原先關於結果不確定的警告。
- **[Flood Ping](/docs/diagnostics-monitoring-and-troubleshooting/flood-ping)**：圍繞丟包測試進行了重寫。新增：flood ping 需要 traffic-gen device-mode 功能（否則命令會以 not allowed by device-mode 失敗）以及如何啟用它，還有從路由器上讀到的引數限制（每次執行最多 1000 個請求，size 為 10 到 1500）。移除了關於傳送速率的無法驗證的說法和一段舊輸出。
- **[Graphing](/docs/diagnostics-monitoring-and-troubleshooting/graphing)**：新增了針對介面、資源和佇列規則以及 graphing 設定的 WinBox 步驟（附截圖），並將舊的 WinBox 圖形截圖替換為原生截圖。

## 系統 {#system}

- **[Services](/docs/system-information-and-utilities/services)**：圍繞路由器監聽什麼進行了重寫：/ip/service 中的動態條目及其對防火牆的意義、同時為多個服務設定 available-from（只含 IPv4 字首的列表會拒絕 IPv6 用戶端），以及 VRF 中的管理服務。協定和埠列表現在分為三張表（TCP、UDP、IP 協定），並已針對各功能開啟的監聽埠做了核對：

- 移除了 RouterOS 7 不使用的埠：MME 和基於 UDP 的 RSVP。
- 已更正：OpenFlow 連線到其控制器而不監聽，TCP 埠 20 也不是監聽埠。
- 已新增：TFTP、OpenVPN、RADIUS incoming、IPsec NAT traversal、用於 WiFi 的 CAPsMAN、WireGuard 和 ICMPv6。
- 一條說明指出，IP 防火牆無法阻止 MAC Telnet、MAC WinBox 和 MAC ping，而 /tool/mac-server 中的 allowed-interface-list 可以。

- **[Wake on LAN](/docs/system-information-and-utilities/wake-on-lan)**：用任務形式重寫，每項任務都經過測試：喚醒 LAN 上的一臺電腦、從網路外部透過 VPN 喚醒、在指定時間喚醒，以及用指令碼在工作日喚醒一組辦公電腦。說明：指定 interface 時，RouterOS 會把 magic packet 作為乙太網幀從該介面發出；不指定時，則作為 UDP 廣播經預設路由（通常是網際網路連線）發出，因此請始終給出 LAN 介面。
- **[Note](/docs/system-information-and-utilities/note)**：重寫了 note 顯示位置的章節，每種情況都經過測試：在互動式 SSH、Telnet 和 MAC Telnet 登入時顯示在 banner 之後；配合 show-at-cli-login 時還會顯示在 Telnet 登入提示之前，任何能連線的人都能讀到（新增警告）。已更正：sys-note.txt 檔案只在下次啟動時才設定 note。
- **[Identity](/docs/system-information-and-utilities/identity)**：名稱出現的位置（提示符、鄰居發現、SNMP 系統名稱、DHCP 主機名）、64 字元的限制，以及一個已更正的 SNMP 示例：設定名稱需要具有寫許可權的 community，因為 public 只能讀取。新增了關於寫 community 允許哪些操作的警告。
- **[Clock](/docs/system-information-and-utilities/clock)、[Device mode](/docs/system-information-and-utilities/device-mode)、[E-mail](/docs/system-information-and-utilities/e-mail)、[Fetch](/docs/system-information-and-utilities/fetch)、[Files](/docs/system-information-and-utilities/files)、[Identity](/docs/system-information-and-utilities/identity)、[IP packing](/docs/system-information-and-utilities/ip-packing)、[Neighbor discovery](/docs/system-information-and-utilities/neighbor-discovery)、[Note](/docs/system-information-and-utilities/note)、[NTP](/docs/system-information-and-utilities/ntp)、[Partitions](/docs/system-information-and-utilities/partitions)、[Scheduler](/docs/system-information-and-utilities/scheduler)、[Services](/docs/system-information-and-utilities/services)、[TFTP](/docs/system-information-and-utilities/tftp)、[Wake on LAN](/docs/system-information-and-utilities/wake-on-lan)**：每個頁面現在都有一個簡短的 WinBox 小節，附有同一任務對應的原生 WinBox 視窗的帶標註截圖。

## 管理工具 {#management-tools}

- **[MAC server](/docs/management-tools/mac-server)**：圍繞使用 MAC Telnet（或按 MAC 地址使用 WinBox）連線、用 MAC scan 查詢路由器，以及只在可信介面上允許 MAC 訪問進行了重寫，並在兩臺路由器之間做了測試。新增並已驗證：

- MAC Telnet 不加密：命令和輸出以明文經過鏈路，但密碼不會。
- IP 防火牆無法阻止 MAC 訪問；allowed-interface-list 或某個埠上的網橋過濾規則可以。
- 應把網橋（而不是它的埠）加入列表；none 會關閉訪問；已開啟的會話會保持開啟。
- 使用者的 address 設定不適用於 MAC 登入。
- 已更正：MAC scan 會列出傳送鄰居發現的裝置，無論其 MAC server 設定如何；關閉 MAC ping 不影響 ARP ping。

- **[Quick Set](/docs/management-tools/quick-set)**：用帶標註的 WinBox 截圖進行說明：Home AP Dual 模式的主要區域、網路名稱和 Wi-Fi 密碼、網際網路連線型別以及本地網路設定。

## CLI 參考 {#cli-reference}

- **[/tool/ping](/docs/cli-reference/tool/ping)**：每一行現在都有取值範圍和預設值，並用抓包進行了核對：size 為整個 IP 包（IPv4 為 28..65535，IPv6 為 48..65535）、ttl（IPv4 為 255，IPv6 的 hop limit 為 64）、interval、dscp、源地址選擇、interface，以及各個 status 值。
- **[/tool/traceroute](/docs/cli-reference/tool/traceroute)**：描述了所有行：探測型別和大小、max-hops（30）、timeout（1 秒）、port（UDP 探測為 33434）、use-dns、vrf，以及某一跳可能報告的 status 值。
- **[/tool/mac-server](/docs/cli-reference/tool/mac-server)、[/tool/mac-telnet](/docs/cli-reference/tool/mac-telnet)、[/tool/mac-scan](/docs/cli-reference/tool/mac-scan)**：描述了所有行和選單簡介：允許的介面列表（預設 all，預設配置會設為 LAN）、MAC ping、會話列表、用戶端的 interface，以及 MAC scan 顯示的內容。
- **[/tool/torch](/docs/cli-reference/tool/torch)**：描述了全部 24 行：各個過濾器及其匹配方式、port 每次一個埠、cpu=any，以及 tx 和 rx 的方向與單位。
- **[/tool/wol](/docs/cli-reference/tool/wol)、[/tool/ip-scan](/docs/cli-reference/tool/ip-scan)**：描述了 Wake on LAN 的兩種封包形式，以及 IP scan 的每一行及其各列的來源。
- **[/system/note](/docs/cli-reference/system/note)、[/system/identity](/docs/cli-reference/system/identity)、[/tool/flood-ping](/docs/cli-reference/tool/flood-ping)**：描述了所有行，包括 flood ping 的限制及其 device-mode 要求。

## 硬體 {#hardware}

- **[KNOT](/hardware/knot) 及其他 IoT 產品頁面**：每個頁面現在都有一個 A4 PDF 版本，連結位於頁面標題下方。
