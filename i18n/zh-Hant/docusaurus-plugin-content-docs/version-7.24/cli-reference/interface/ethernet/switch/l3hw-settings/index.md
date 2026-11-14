---
sidebar_key: "cli-reference/interface/ethernet/switch/l3hw-settings/index"
sidebar_position: 2
title: "l3hw-settings"
sidebar_label: "l3hw-settings"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/l3hw-settings
captured_at: '2026-11-01T21:27:10+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/l3hw-settings {#interfaceethernetswitchl3hw-settings}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="autorestart" typ="bool" syscap="!prestera-cpss">驅動程式發生故障時自動重啟 L3HW</ArgTableRow>
<ArgTableRow arg="fasttrack-hw" typ="bool" syscap="!prestera-ac3">FastTrack 連線的硬體解除安裝</ArgTableRow>
<ArgTableRow arg="ipv6-hw" typ="bool">IPv6 硬體解除安裝</ArgTableRow>
<ArgTableRow arg="icmp-reply-on-error" typ="bool">發生封包錯誤（TTL、MTU 等）時，要麼將封包重定向到 CPU 以進行 ICMP 回覆（yes），要麼靜默丟棄（no）</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hw-supports-fasttrack" typ="bool">硬體是否支援 FastTrack 解除安裝？</ArgTableRow>
</ArgTable>
