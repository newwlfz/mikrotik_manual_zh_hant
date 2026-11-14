---
title: "文件更新 - 2026 年 6 月 8 日"
date: 2026-06-08
slug: /changelog-2026-06-08
source: https://manual.mikrotik.com/changelog/changelog-2026-06-08
captured_at: '2026-11-04T06:07:54+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## CLI 參考 {#cli-reference}

- **[IPv6 Address](/docs/cli-reference/ipv6/address)**：改進了 from-pool-policy 選項說明，格式更清晰，示例更好。重寫了 auto-link-local 說明，更清楚地解釋手動新增鏈路本地地址會覆蓋自動生成的地址。
- **[IPv6 Mangle](/docs/cli-reference/ipv6/firewall/mangle)**：將 action 引數冗長的行內說明重新整理為針對每個 action 值的正確專案符號列表。改進了 dnpt 和 snpt 說明，分別明確為“目標 IPv6 網路字首轉換”和“源 IPv6 網路字首轉換”。
- **[IPv6 Neighbor Discovery](/docs/cli-reference/ipv6/nd)**：修正了 ra-lifetime 的 RFC 章節引用（6.2.3 → 6.2.1）。擴充了 advertise-dns 引數選項，為全部三個值（no、yes、self）提供了適當說明。改進了 ra-preference 說明，使其使用正確的引數名。
- **[IPv6 ND Prefix](/docs/cli-reference/ipv6/nd/prefix)**：在 dhcp6-pd-preferred 引數說明中添加了正確的 RFC 9762 連結。
- **[IPv6 ND Settings](/docs/cli-reference/ipv6/nd/settings)**：改進了選單說明，並重寫了 router-advertisement-ignored-options 說明以提高畫質晰度。
- **[IPv6 Neighbor](/docs/cli-reference/ipv6/neighbor)**：澄清了 stale 鄰居狀態說明（“將繼續傳送流量”而不是“傳送流量”）。
- **[IPv6 Pool](/docs/cli-reference/ipv6/pool)**：更新了說明，以澄清該選單處理的是 IPv6 字首（而不是 IP 地址）。
- **[IPv6 Settings](/docs/cli-reference/ipv6/settings)**：修復了損壞的 Fast Path 連結，使其指向 Packet Flow 文件。簡化了重啟說明，刪除了冗餘措辭。
- **[IPv4 Firewall Filter](/docs/cli-reference/ip/firewall/filter)**：修復了 ICMP reject-with 引數——它之前引用 ICMPv6 錯誤型別（ICMP 型別 1），現在正確顯示 IPv4 ICMP 型別 3 值及相應錯誤說明。添加了 tcp-reset 說明（傳送設定了 RST 標誌的 TCP 段）。擴充了 connection-nat-state，以記錄用於端點無關 NAT 的 ein-snat 和 ein-dnat 值。
- **[IPv4 Firewall Mangle](/docs/cli-reference/ip/firewall/mangle)**：修復了 fasttrack-connection 說明（“顯示 fasttrack 計數器” → “將連線標記為 FastTrack”）。修正了 new-priority 中“ets” → “Sets”的拼寫錯誤。修復了 mark-routing 說明末尾的雙句號。在所有防火牆表中，將 rst TCP 標誌說明從“斷開連線”一致更新為“重設連線”。
- **[IPv6 Firewall Filter](/docs/cli-reference/ipv6/firewall/filter)**：擴充了 reject-with 引數，詳細說明每種 ICMPv6 錯誤型別及其對應的 ICMP 型別/程式碼值，並添加了指向 IANA ICMPv6 引數登錄檔的連結。
- **[Disk](/docs/cli-reference/disk)**：修復了自加密標誌說明——從顯示的標誌名中刪除了冗餘的“tcg-opal-”字首。
- **[IP Settings](/docs/cli-reference/ip/settings)**：為 accept-source-route 添加了安全警告，指出接受源路由封包存在欺騙風險。將 rp-filter 選項重新整理為正確的專案符號列表，並澄清嚴格模式會導致非對稱/VPN 路由問題。修復了損壞的 Fast Path 連結。

## 入門 {#getting-started}

- **[MikroTik Hardware Licensing](/docs/getting-started/routeros-licensing/mikrotik-hardware)**：新增了“自定義無線通道”一節，介紹適用於 Atheros 92xx 裝置的 Advanced Channels 功能，涵蓋擴充套件掃描列表、支援以 kHz 為粒度的精確頻率自定義，以及非標準通道寬度。

## 橋接與交換 {#bridging--switching}

- **[SwOS](/docs/bridging-and-switching)**：為 CSS106、CSS610 和 GPEN21 交換器型號新增了 81 張 SwOS 截圖，涵蓋 VLAN 配置、統計資訊、系統設定、ACL、鏈路狀態、IGMP 等。
