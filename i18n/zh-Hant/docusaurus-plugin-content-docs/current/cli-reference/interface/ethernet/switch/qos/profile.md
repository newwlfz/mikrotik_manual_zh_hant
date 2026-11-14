---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/profile"
sidebar_position: 5
title: "profile"
sidebar_label: 'profile'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos/profile
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/profile {#interfaceethernetswitchqosprofile}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 目錄

QoS 配置檔案決定轉發/路由封包的優先順序欄位值（PCP、DSCP）。擁塞避免/解決基於 QoS 配置檔案。每個封包會根據入站交換器埠 QoS 設定獲得一個 QoS 配置檔案分配（參見 `/in/eth/sw/port`）。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">使用者定義的 QoS 配置檔名稱。</ArgTableRow>
<ArgTableRow arg="pcp" typ="num">VLAN 優先順序值（IEEE 802.1q PCP - 優先順序程式碼點）。僅當分配給該 QoS 配置檔案的出站封包帶有 VLAN 標籤（具有 802.1q 報頭）時使用。該值可透過 QoS Egress Map 進一步修改。</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">分配給該 QoS 配置檔案的出站封包的 IPv4/IPv6 DSCP 欄位值。</ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num">流量類別決定封包優先順序和出站佇列。佇列編號通常與流量類別相同（tc0 的封包進入 queue0，tc1 - queue1，... tc7 - queue7）。TC0 始終選擇最低優先順序。</ArgTableRow>
<ArgTableRow arg="automap" typ="bool">自動將 PCP 或 DSCP 值匹配的封包對映到該 QoS 配置檔案。僅適用於 **trusted** 埠。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>
