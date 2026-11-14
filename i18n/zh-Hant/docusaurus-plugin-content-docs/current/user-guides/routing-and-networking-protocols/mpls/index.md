---
sidebar_key: "user-guides/routing-and-networking-protocols/mpls"
title: "MPLS"
sidebar_label: "MPLS"
description: "MPLS 是一種使用標籤而非 IP 報頭分析來實現更快封包轉發的路由技術，RouterOS 支援 MPLS 交換、LDP/RSVP-TE 協定、VPLS 和 MP-BGP VPN，但不包括某些 LDP/TE 功能。"
tags:
  - 'mpls'
source: https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/mpls
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MPLS 代表多協定標籤交換（MultiProtocol Label Switching）。MPLS 不採用 IP 路由，而是根據附加到封包上的標籤，而非 IP 報頭中的欄位（例如目標地址）和路由表，來決定封包轉發（出介面和下一跳路由器）。這種方法加快了轉發過程，因為下一跳查詢比路由查詢（查詢最長匹配字首）更簡單。

轉發過程的效率是 MPLS 的主要優勢。但是請記住，MPLS 轉發會停用對網路層（例如 IP）報頭的處理。因此，無法對 MPLS 轉發的封包應用諸如 NAT 和過濾等基於網路層的操作。請在 MPLS 雲的入口或出口處應用任何基於網路層的操作，其中入口是首選方法。這樣，你打算丟棄的流量就不會經過 MPLS 骨幹網。

MPLS 透過使用 LDP 協定為活動路由分發標籤來運作，帶標籤的封包會沿與不帶標籤的封包相同的路徑傳輸。當路由器沿某條路由轉發不帶標籤的封包，並且已從該路由的下一跳收到標籤時，它會為該封包壓入標籤並將其傳送到下一跳，在那裡由 MPLS 沿路徑進一步交換。當路由器收到一個帶有其已分配給特定路由的標籤的封包時，它會將該封包標籤替換為從該路由的下一跳收到的標籤，並將封包傳送到下一跳。標籤交換路徑可確保將資料送達 MPLS 雲出口點。MPLS 應用基於標籤交換路徑這一概念。

建立標籤交換路徑的另一種方式是使用 RSVP-TE 協定的流量工程隧道（TE 隧道）。流量工程隧道允許顯式路由的 LSP 和基於約束的路徑選擇（其中約束是介面屬性和可用頻寬）。

由於 MPLS 引入了複雜性和新協定，併為路由網路和橋接網路增加了不同的概念，因此在生產網路中實施 MPLS 之前，你應深入理解 MPLS 概念。一些建議閱讀材料：

- 多協定標籤交換 [http://en.wikipedia.org/wiki/Multiprotocol_Label_Switching](http://en.wikipedia.org/wiki/Multiprotocol_Label_Switching)
- RFC3031 多協定標籤交換架構 [http://www.ietf.org/rfc/rfc3031.txt](http://www.ietf.org/rfc/rfc3031.txt)
- 《MPLS 基礎》，Luc De Ghein 著 [http://www.amazon.com/MPLS-Fundamentals-Luc-Ghein/dp/1587051974](http://www.amazon.com/MPLS-Fundamentals-Luc-Ghein/dp/1587051974)

:::info
此功能在 SMIPS 裝置上不受支援（hAP lite、hAP lite TC 和 hAP mini）。
:::

## 支援的功能 {#supported-features}

RouterOS 支援以下與 MPLS 相關的功能：

- 支援倒數第二跳彈出的 MPLS 交換。
- IPv4 和 IPv6 的靜態本地標籤繫結。
- IPv4 和 IPv6 的靜態遠端標籤繫結。
- 適用於 IPv4 和 IPv6 的 Label Distribution Protocol（[RFC 3036](https://tools.ietf.org/html/rfc3036)、[RFC 5036](https://tools.ietf.org/html/rfc5036) 和 [RFC 7552](https://tools.ietf.org/html/rfc7552)）：
  - 下游非請求標籤通告。
  - 獨立標籤分發控制。
  - 寬鬆標籤保留。
  - 定向會話建立。
  - 可選環路檢測。
  - 支援 ECMP。
- Virtual Private LAN Service (VPLS)：
  - VPLS LDP 信令（[RFC 4762](https://tools.ietf.org/html/rfc4762)）。
  - Cisco 風格的靜態 VPLS 偽線（[RFC 4447](https://tools.ietf.org/html/rfc4447) FEC 型別 0x80）。
  - VPLS 偽線分片和重組（[RFC 4623](https://tools.ietf.org/html/rfc4623)）。
  - 基於 VPLS MP-BGP 的自動發現和信令（[RFC 4761](https://tools.ietf.org/html/rfc4761)）。
  - Cisco VPLS 基於 BGP 的自動發現（[draft-ietf-l2vpn-signaling-08](https://tools.ietf.org/html/draft-ietf-l2vpn-signaling-08)）。
  - 支援基於 BGP 的 VPLS 的多個匯入/匯出 route-target 擴展團體（同時支援 [RFC 4761](https://tools.ietf.org/html/rfc4761) 和 [draft-ietf-l2vpn-signaling-08](https://tools.ietf.org/html/draft-ietf-l2vpn-signaling-08)）。
- RSVP-TE 隧道：
  - 隧道頭端。
  - 顯式路徑。
  - 用於 TE 隧道的 OSPF 擴充套件。
  - CSPF 路徑選擇。
  - 在 TE 隧道上轉發 VPLS 和 MPLS IP VPN 流量。
  - 入口 TE 隧道速率限制和自動預留頻寬調整。有關更多資訊，請參閱 [流量工程](./traffic-eng.md)。
  - 所有隧道頻寬設定均以位元/秒為單位指定和顯示。
- 基於 MP-BGP 的 MPLS IP VPN。
- 基於 MP-BGP 的 MPLS VPN 的按字首和按 VRF 標籤分發策略。
- 用於 MPLS TE 的 OSPF 擴充套件。
- 支援將 OSPF 作為 CE-PE 協定。
- 針對指定 VRF 的 ping 和 traceroute。
- 控制 MPLS 中網路層 TTL 的傳播。
- 將 RIP 作為 CE-PE 協定。
- 按 VRF 的 BGP 例項重分發設定。

## RouterOS 尚不具備的 MPLS 功能 {#mpls-features-that-routeros-does-not-have-yet}

- LDP 功能：
  - 下游按需標籤通告。
  - 有序標籤分發控制。
  - 保守標籤保留。
- TE 功能：
  - 快速重路由。
  - 鏈路/節點保護。
- 支援將 BGP 作為標籤分發協定。

<DocCardList />
