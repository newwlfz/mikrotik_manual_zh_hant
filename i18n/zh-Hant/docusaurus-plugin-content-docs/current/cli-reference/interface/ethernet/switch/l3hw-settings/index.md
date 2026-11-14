---
sidebar_key: "cli-reference/interface/ethernet/switch/l3hw-settings"
title: "l3hw-settings"
sidebar_label: 'l3hw-settings'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/l3hw-settings
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/l3hw-settings {#interfaceethernetswitchl3hw-settings}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 設定目錄

L3HW 設定選單允許為三層硬體解除安裝驅動程式配置全域性引數。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="autorestart" typ="bool" syscap="!prestera-cpss">在驅動故障時自動重啟 L3HW。如果未啟用 autorestart，則 `l3-hw-offloading` 會被停用，錯誤程式碼會顯示在 [monitor](./monitor.md) 中。Autorestart 不適用於系統故障，例如 OOM（記憶體不足）。</ArgTableRow>
<ArgTableRow arg="fasttrack-hw" typ="bool" syscap="!prestera-ac3">啟用或停用 FastTrack 硬體解除安裝。除非需要預留 HW TCAM 記憶體（例如用於建立動態交換器 ACL 規則），否則請保持啟用。並非所有交換器晶片都支援 FastTrack 硬體解除安裝（參見 [`hw-supports-fasttrack`](#hw-supports-fasttrack)）。</ArgTableRow>
<ArgTableRow arg="ipv6-hw" typ="bool">IPv6 硬體解除安裝。IPv6 路由會佔用大量 HW 記憶體，僅當 IPv6 流量足夠大、能從硬體路由中獲益時，才啟用此選項。</ArgTableRow>
<ArgTableRow arg="icmp-reply-on-error" typ="bool">由於硬體無法傳送 ICMP 訊息，發生錯誤時（例如，“Time Exceeded”、“Fragmentation required”等），必須將封包重定向到 CPU 以傳送 ICMP 回覆。啟用它有助於網路診斷，但可能為 DDoS 攻擊帶來潛在漏洞。停用後，在發生錯誤時會在硬體層面靜默丟棄封包。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hw-supports-fasttrack" typ="bool">指示硬體（交換器晶片）是否支援 FastTrack 硬體解除安裝。</ArgTableRow>
</ArgTable>
