---
title: "文件更新 - 2026年9月23日"
date: 2026-09-23
slug: /changelog-2026-09-23
source: https://manual.mikrotik.com/changelog/changelog-2026-09-23
captured_at: '2026-11-04T06:08:50+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 9 月 23 日所做的文件變更摘要。

## 網路管理 {#network-management}

- **[DHCP](/docs/network-management/dhcp)**：將原本單一的 DHCP 頁面拆分為一個章節，其中為 [DHCP 用戶端](/docs/network-management/dhcp/client)、[DHCP 伺服器](/docs/network-management/dhcp/server)、[DHCP 中繼](/docs/network-management/dhcp/relay)、[DHCPv6 用戶端](/docs/network-management/dhcp/dhcpv6-client) 和 [DHCPv6 伺服器](/docs/network-management/dhcp/dhcpv6-server) 分別設立獨立頁面。該章節頁面現在解釋了 DHCP 的工作原理：DISCOVER/OFFER/REQUEST/ACK 互動與廣播標誌、租約續期（在租約時間的 50% 處續期、在 87.5% 處重新繫結）、地址衝突檢查、用戶端標識、常用選項以及為什麼選項 121 會使用戶端忽略選項 3、中繼與 giaddr，還有 DHCPv6 的差異所在。所有 DHCP 頁面上的行為均已在 RouterOS 7.25 上核對，現在每個頁面都以配置示例開頭，而屬性表則移至 CLI 參考。
- **[DHCP 用戶端](/docs/network-management/dhcp/client)**：新增引言，說明用戶端會從租約中應用哪些內容；新增“來自租約的路由”一節，涵蓋 add-default-route 的各種模式、路由距離以及與另一條預設路由之間的 ECMP，還有 VRF 表中的路由。更正了 disabled（no）和 default-route-distance（1）的預設值，記錄了 dhcp-options，並移除了 RouterOS v6 的 client-id 和 host-name 屬性。修復了兩個無法工作的指令碼示例：子網外閘道器指令碼現在被設定為用戶端自身的指令碼（作為單獨的系統指令碼時它無法看到租約變數），而 WAN1 租約指令碼現在會建立其路由表。
- **[DHCP 伺服器](/docs/network-management/dhcp/server)**：重寫了租約分配的描述（地址透過 ARP 和 ICMP 進行檢查，正在使用的地址會保留為衝突租約，靜態地址不進行檢查），並精確解釋了 authoritative：no 僅忽略針對未知地址的廣播請求，而單播續期則始終會被應答。刪除了關於 DNS 條目需要已存在 DNS 區域的錯誤說明，將設定演練更新為當前提示（包括新增的 send dns 問題），把手動配置改為編號步驟，並修正了 force 示例，該示例原先未指明任何選項。
- **[DHCP 中繼](/docs/network-management/dhcp/relay)**：基於兩臺路由器的測試重寫。新增關於中繼代理資訊（選項 82）以及 DHCP 伺服器如何將其用於租約和靜態租約匹配的一節，指出新建的 IPv4 中繼預設處於停用狀態，解釋了 VRF 示例為何需要其 dst-nat 規則和跨 VRF 路由，並更正了 DHCPv6 中繼的描述：它傳送的是 Relay-Forward 訊息（而非逐跳選項），預設防火牆必須在用戶端側介面上允許 UDP 埠 547，另有一節新增內容介紹 store-relayed-bindings。
- **[DHCPv6 用戶端](/docs/network-management/dhcp/dhcpv6-client)**、**[DHCPv6 伺服器](/docs/network-management/dhcp/dhcpv6-server)**：新增引言，涵蓋請求型別、動態地址池、DUID 和 IAID，以及伺服器發起的續期（當伺服器設定發生變化時，它會自行傳送 Reconfigure 訊息）。記錄了 DNS 條目僅針對地址繫結建立為 AAAA 記錄，修正了示例中無效的 IPv6 字首，並將所有示例輸出更新為 RouterOS 7 格式。
- **[反向代理](/docs/network-management/proxy/reverse-proxy)**：用配置示例（匯入證書、新增規則並在防火牆中允許 HTTPS）重寫了該頁面，並新增若干章節：規則如何按 TLS 伺服器名稱（SNI，僅精確匹配）選擇、路由器呈現哪張證書、Web 伺服器收到什麼（帶 X-Forwarded-For、X-Forwarded-Proto、Forwarded 及相關頭部的純 HTTP/1.1）、服務埠、容器應用的動態規則，以及使用 rproxy 日誌進行故障排查。新增一則警告，說明當兩個服務都使用 443 埠時，重啟後 www-ssl 會佔用該埠。更正了選單路徑（/ip/reverse-proxy）和預設值：新規則預設啟用，且 sni、ip-address 和 port 為必填項。屬性表移至 CLI 參考。

## CLI 參考 {#cli-reference}

- **[/ip/dhcp-client](/docs/cli-reference/ip/dhcp-client)**、**[/ip/dhcp-server](/docs/cli-reference/ip/dhcp-server)**、**[/ip/dhcp-relay](/docs/cli-reference/ip/dhcp-relay)**、**[/ipv6/dhcp-client](/docs/cli-reference/ipv6/dhcp-client)**、**[/ipv6/dhcp-server](/docs/cli-reference/ipv6/dhcp-server)**、**[/ipv6/dhcp-relay](/docs/cli-reference/ipv6/dhcp-relay)**：為 DHCP 和 DHCPv6 的用戶端、伺服器、租約、繫結、網路、選項、匹配器、警報和中繼的大約 180 個此前為空的引數、標誌和命令撰寫了描述（包括預設值），全部在 RouterOS 7.25 上核對。這涵蓋了此前任何地方都未記錄的引數，例如 ipv6-only-preferred（選項 108）、accept-prefix-without-address、rapid-commit、中繼監控計數器以及 DHCPv6 中繼路由選單，並更正了諸如靜態 DHCPv6 繫結的預設生命期（1w）和 server-address 的含義等錯誤細節。
- **[/ip/reverse-proxy](/docs/cli-reference/ip/reverse-proxy)**：描述了規則標誌以及 sni、ip-address、port 和 certificate 引數，已在 RouterOS 7.25 上核對，包括回退到 /ip/service 證書，以及名稱未匹配和證書缺失時的日誌訊息。

## 系統 {#system}

- **[服務](/docs/system-information-and-utilities/services)**：reverse-proxy 服務會連結到“反向代理”頁面，並且證書屬性中說明，沒有自帶證書的反向代理規則會使用服務證書。

## 儲存 {#storage}

- **[加密儲存](/docs/storage/encrypted-storage)**：從 RAID1 示例中移除了 crypt-mode=encryption-and-integrity 設定。
