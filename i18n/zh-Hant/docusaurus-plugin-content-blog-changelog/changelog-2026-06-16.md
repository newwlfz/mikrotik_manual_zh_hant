---
title: "文件更新 - 2026年6月16日"
date: 2026-06-16
slug: /changelog-2026-06-16
source: https://manual.mikrotik.com/changelog/changelog-2026-06-16
captured_at: '2026-11-04T06:07:59+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 6 月 16 日文件變更摘要。

## 無線 {#wireless}

- **[Wi-Fi 6 / 7 (802.11ax/be)](/docs/wireless/wifi)**：將 WiFi 頁面標題從 "Wi-Fi 6 / 6E" 改為 "Wi-Fi 6 / 7 (802.11ax/be)"，並把 "這是正確的章節嗎？" 提示重構為驅動包表格，記錄新增的 wifi-qcom-be（Wi-Fi 7，例如 hAP be3 media）和 wifi-mediatek（例如 hAP ax S、hAP be lite）包，與 wifi-qcom 並列。同時更新側邊欄標籤和指向該頁面的交叉引用以保持一致。
- **[無線概述](/docs/wireless)**：將即將推出的 Wi-Fi 7 驅動型別 —— wifi-qcom-be 和 wifi-mediatek —— 加入包選擇表，並新增 WiFi 7 產品系列條目，同時在型號命名示例中加入 hAP be lite。
- **[Wi-Fi 5 (802.11ac)](/docs/wireless/wifi-ac)**：說明 wifi-qcom-ac 會*替換* wireless 包，而非與之並存安裝，並弱化了驅動相容性警告的措辭。
- **[無線 station 模式](/docs/wireless/user-guides/wireless-station-modes)**：在 station 模式適用性矩陣中新增 wifi-qcom 列，並說明可用的 station 模式取決於所安裝的驅動和無線協定。
- **[802.11 a/b/g/n](/docs/wireless/abgn)**：對舊版 /interface/wireless、CAPsMAN、W60G 和 WiFi 配置指南進行審校修正 —— 包括 CAPsMAN 的 upgrade-policy 和 rates.basic 說明以及證書有效期示例。

## 物聯網 {#internet-of-things}

- **[ChirpStack](/docs/internet-of-things/lora/user-guides/chirpstack)**：新增指南，介紹如何將 MikroTik LoRaWAN 網關注冊到開源 ChirpStack 伺服器。

## 防火牆與 QoS {#firewall--qos}

- **[連線跟蹤](/docs/firewall-and-quality-of-service/connection-tracking)**：對該章節進行審校修正 —— 擴充了 untracked 連線狀態與 RAW 規則的說明，記錄了 loose-tcp-tracking 和 udp-timeout，並對 NAT、過濾規則、佇列（CAKE、HTB、FIFO）以及 DDoS 防護和埠敲擊案例研究作出澄清。

## 使用者指南 {#user-guides}

- **[路由決策](/docs/user-guides/routing-and-networking-protocols/routing-decision)**：路由文件審校修正 —— 澄清了 nexthop 查詢以及透過路由過濾器進行的路由重分發，並修正了 BGP、OSPF、MPLS/VPLS、組播、VRF 以及 ROSv6→v7 遷移頁面中的問題。

## 入門 {#getting-started}

- **[備份](/docs/getting-started/configuration-management/backup)**：記錄了備份加密屬性（aes-sha256 / rc4）和密碼加密行為，並對安裝/升級、網路基礎（IPv6）以及保護路由器頁面做了進一步的審校澄清。
- **[首次配置](/docs/getting-started/first-time-configuration)**：重構了該指南，更新了內容並新增 WinBox4 截圖 —— 更清晰的分步流程（物理連線、下載 WinBox、透過 Neighbor Discovery 查詢路由器、加固安全以及使用者密碼管理），並將無線設定拆分為三代：舊版 /interface wireless、現代 /interface wifi，以及高階的 MLD / 多射頻 / WiFi 6E 風格配置。

## 硬體 {#hardware}

- **[磁碟](/docs/hardware/disks)**：對硬體頁面進行審校修正 —— 新增磁碟共享屬性（auto-media-sharing、SMB/NFS 共享）和支援的格式化檔案系統，並修正了接地、LED、LCD 觸控式螢幕、PoE-out、埠、產品命名和 RouterBOOT 相關的措辭。

## 診斷與監控 {#diagnostics--monitoring}

- **[Detect Internet](/docs/diagnostics-monitoring-and-troubleshooting/detect-internet)**：審校修正 —— 澄清了 WAN 可達性檢查（透過 UDP 埠 30000 訪問 cloud.mikrotik.com，每 2 分鐘檢查一次），並修正了日誌、Netwatch、SNMP、traffic-flow、torch 及其他診斷工具中的問題。

## 高可用性解決方案 {#high-availability-solutions}

- **[Bonding](/docs/high-availability-solutions/bonding)**：對 bonding 和負載均衡指南進行審校修正，包括修正 EoIP 隧道示例。

## 開發者指南 {#developer-guides}

- **[API](/docs/developer-guides/api)**：審校修正 —— 澄清了 API 協定長度編碼（四位元組長度，最大 0xFFFFFFFF），更新了 Python 3 TLS 示例，並修正了 REST API 和指令碼頁面。

## CLI 參考 {#cli-reference}

- **[CLI 參考](/docs/cli-reference)**：記錄了 m 地址標誌（組播地址）。

## 其他章節 {#other-sections}

- **第二輪文件審校**：對剩餘章節進行拼寫、語法、措辭和事實性修正 —— [系統](/docs/system-information-and-utilities/fetch)（Fetch、電子郵件、時鐘、device-mode、IP packing）、[儲存](/docs/storage/nvme-over-tcp)（更清晰的 NVMe-over-TCP 配置、BTRFS、RAID、SMB、加密儲存）、[網路管理](/docs/network-management/dhcp)（DHCP、DNS、Cloud Back To Home（遠端回家） / 檔案共享、Web/反向代理、SOCKS）、[行動網路](/docs/mobile-networking/lte-5g)（LTE/5G、GPS、雙 SIM、簡訊）、[管理工具](/docs/management-tools/tr-069)（TR-069、CLI、Quick Set、SSH、WinBox）、[物聯網](/docs/internet-of-things/mqtt)（MQTT、藍牙、LoRa、GPIO、Wiliot）、[有線連線](/docs/wired-connections/ethernet)（Ethernet、介面相容性、PWR-Line）以及 [VPN](/docs/virtual-private-networks/ipsec)（IPsec、L2TP、SSTP、OpenVPN、WireGuard、PPPoE 以及各隧道指南）。
- **[無線](/docs/wireless/wifi)**：格式修正 —— 表格內的警告訊息現在可以正確渲染，hAP ac² 等硬體型號名稱使用正確的上標。
