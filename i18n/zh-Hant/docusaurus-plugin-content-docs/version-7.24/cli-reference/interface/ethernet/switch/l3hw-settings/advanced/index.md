---
sidebar_key: "cli-reference/interface/ethernet/switch/l3hw-settings/advanced/index"
sidebar_position: 1
title: "advanced"
sidebar_label: "advanced"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/l3hw-settings/advanced
captured_at: '2026-11-01T21:27:12+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/l3hw-settings/advanced {#interfaceethernetswitchl3hw-settingsadvanced}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="route-queue-limit-high" typ="num" syscap="!prestera-cpss">如果佇列中的路由數量超過此值，則停用索引</ArgTableRow>
<ArgTableRow arg="route-queue-limit-low" typ="num" syscap="!prestera-cpss">如果佇列中的路由數量降至該值，則重新啟用索引</ArgTableRow>
<ArgTableRow arg="shwp-reset-counter" typ="num">在路由表發生此數量的變更後，重設 Shortest HW Prefix 並嘗試完整路由表解除安裝</ArgTableRow>
<ArgTableRow arg="partial-offload-chunk" typ="num" syscap="prestera-bc2">部分解除安裝時進行增量新增所需的最小路由數量</ArgTableRow>
<ArgTableRow arg="route-index-delay-min" typ="time" syscap="!prestera-cpss">路由處理與表索引之間的最短時間</ArgTableRow>
<ArgTableRow arg="route-index-delay-max" typ="time">路由處理與表索引之間的最長時間</ArgTableRow>
<ArgTableRow arg="neigh-keepalive-interval" typ="time" syscap="!prestera-cpss">保持硬體解除安裝鄰居（主機）存活的時間間隔</ArgTableRow>
<ArgTableRow arg="neigh-discovery-interval" typ="time" syscap="!prestera-cpss">傳送 ARP/ND 請求以檢查硬體解除安裝鄰居可用性的時間間隔</ArgTableRow>
<ArgTableRow arg="neigh-discovery-burst-limit" typ="num" syscap="!prestera-cpss">限制一次可傳送的 ARP/ND 請求數量</ArgTableRow>
<ArgTableRow arg="neigh-discovery-burst-delay" typ="time" syscap="!prestera-cpss">ARP/ND 請求突發之間的時間間隔</ArgTableRow>
<ArgTableRow arg="neigh-dump-retries" typ="num" syscap="!prestera-cpss">在失敗情況下解除安裝鄰居表的最大重試次數</ArgTableRow>
</ArgTable>
