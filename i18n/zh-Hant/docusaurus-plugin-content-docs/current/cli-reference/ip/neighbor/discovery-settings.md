---
sidebar_key: "cli-reference/ip/neighbor/discovery-settings"
sidebar_position: 1
title: "discovery-settings"
sidebar_label: 'discovery-settings'
source: https://manual.mikrotik.com/docs/cli-reference/ip/neighbor/discovery-settings
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/neighbor/discovery-settings {#ipneighbordiscovery-settings}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="discover-interface-list" typ="super { !
, discover-interface-list: enum
 }">將在其成員上執行發現協定的介面列表。預設值：static。</ArgTableRow>
<ArgTableRow arg="discover-interval" typ="time">傳送鄰居發現數據包的頻率。還會使用公式 (discover-interval * 4) + 1 調整 CDP 和 LLDP 封包的 TTL TLV 值。範圍：5s..9h6m8s。預設值：30s。</ArgTableRow>
<ArgTableRow arg="lldp-med" typ="bool">是否通告 LLDP-MED Media Capabilities TLV。使用 lldp-med-net-policy-vlan 時必須啟用。預設值：yes。</ArgTableRow>
<ArgTableRow arg="lldp-med-net-policy-vlan" typ="alt { constant: enum (disabled)
, vlan-id: num [ .. 4094]
 }">用於 LLDP-MED Network Policy TLV 的通告 VLAN ID。允許為支援 LLDP-MED 的裝置（例如 VoIP 電話）分配 VLAN ID。該 TLV 僅新增到發現支援 LLDP-MED 的裝置且已啟用 lldp-med 的介面。其他 TLV 值（Application Type、VLAN Type、L2 Priority、DSCP Priority）是預定義的。應使用 protocol 設定排除 CDP，以避免 LLDP-MED 配置錯誤。預設值：disabled。</ArgTableRow>
<ArgTableRow arg="lldp-mac-phy-config" typ="bool">是否在 LLDP 中傳送 MAC/PHY Configuration/Status TLV，以指示介面能力、雙工狀態、位元率和自動協商。僅適用於 Ethernet 介面。傳送 LLDP-MED 時自動包含。預設值：no。</ArgTableRow>
<ArgTableRow arg="lldp-max-frame-size" typ="bool">是否在 LLDP 中傳送 Maximum Frame Size TLV，以位元組為單位指示介面的最大幀大小能力（l2mtu + 18）。僅適用於 Ethernet 介面。預設值：no。</ArgTableRow>
<ArgTableRow arg="lldp-vlan-info" typ="bool">是否在 LLDP 中傳送與 VLAN 相關的 IEEE 802.1 Organizationally Specific TLV。啟用後，會通告三個 TLV：Port VLAN ID（網橋埠 pvid）、Port And Protocol VLAN ID（不支援）和 VLAN Name（來自網橋 VLAN 表的最多 10 個活動 VLAN）。與 vlan-filtering 網橋上的介面相關。預設值：no。</ArgTableRow>
<ArgTableRow arg="lldp-poe-power" typ="bool" syscap="poe">是否在 LLDP 訊息中傳輸 IEEE 802.3 Organizationally Specific Power Via MDI TLV。替代 PoE-out 埠的 poe-lldp-enabled 設定。僅與支援 PoE-Out 的 Ethernet 介面相關。預設值：yes。</ArgTableRow>
<ArgTableRow arg="lldp-poe-in-power" typ="bool" syscap="poe-in">是否在 LLDP 訊息中傳輸 PoE 輸入功率 TLV。</ArgTableRow>
<ArgTableRow arg="lldp-dcbx" typ="bool" syscap="crs_prestera">是否傳送 Data Center Bridging Capabilities Exchange Protocol (DCBX) TLV，使用 LLDP 與相鄰裝置交流交換器的 QoS 設定和能力。僅適用於帶有 Marvell Prestera 交換器的裝置（例如 CRS3xx）。包括 ETS Configuration、Priority Assignment、Bandwidth Allocation 和 TSA 表。預設值：no。</ArgTableRow>
<ArgTableRow arg="protocol" typ="ubit (cdp, lldp, mndp)">要使用的發現協定列表。預設值：cdp,lldp,mndp。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (tx-and-rx | tx-only | rx-only)">鄰居發現數據包的傳送和接收模式。預設值：tx-and-rx。</ArgTableRow>
<ArgTableRow arg="dying-gasp" typ="bool">是否在正常重啟、關機或升級前傳送 TTL=0 的鄰居發現數據包。斷電或核心恐慌時不會發送。在接收端，TTL=0 的封包會立即刪除相應的鄰居條目。預設值：no。</ArgTableRow>
<ArgTableRow arg="add-dns-entries" typ="bool">是否為發現的鄰居建立動態 DNS 條目，並使用其身份作為域名。</ArgTableRow>
<ArgTableRow arg="add-dns-entries-suffix" typ="string">為每個鄰居建立的動態 DNS 條目新增的字尾。</ArgTableRow>
</ArgTable>
