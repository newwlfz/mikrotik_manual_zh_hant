---
sidebar_key: "cli-reference/system/ptp"
title: "ptp"
sidebar_label: 'ptp'
source: https://manual.mikrotik.com/docs/cli-reference/system/ptp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ptp {#systemptp}
**條件：** !smips
**系統能力：** ptp
**型別：** Directory
PTP（IEEE 1588-2008，PTPv2）例項配置。每個條目對應一個 PTP 配置檔案例項；埠在 [`/system/ptp/port`](./port.md) 中加入它。僅在特定交換器/路由器硬體上支援（請參閱[精確時間協定](../../../system-information-and-utilities/precision-time-protocol.md)指南）。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">PTP 配置檔案例項的名稱</ArgTableRow>
<ArgTableRow arg="priority1" typ="enum (auto) { auto:0 }">主時鐘選舉的第一個值；值越小越優先。使用 `auto` 時，採用所選配置的值（802.1AS：246，其他配置：128）</ArgTableRow>
<ArgTableRow arg="priority2" typ="enum (auto)">主時鐘選舉的第二個值，用於平局時判定。使用 `auto` 時，採用所選配置的值（802.1AS：248，其他配置：128）</ArgTableRow>
<ArgTableRow arg="delay-mode" typ="enum (auto | e2e | p2p)">延遲測量機制：`e2e`（請求-響應）或 `p2p`（對等延遲）。使用 `auto` 時，採用配置的預設值（802.1AS：p2p，其他配置：e2e）</ArgTableRow>
<ArgTableRow arg="transport" typ="enum (auto | ipv4 | l2-non-forwardable | l2-forwardable)">用於 PTP 報文的傳輸方式：`ipv4`（PTP 主報文使用組播 224.0.1.129，對等延遲報文使用 224.0.0.107）、`l2-forwardable`（組播 MAC 01-1B-19-00-00-00，由不感知 PTP 的網橋轉發）或 `l2-non-forwardable`（01-80-C2-00-00-0E，符合標準的網橋不會轉發）。使用 `auto` 時，採用配置的預設值（802.1AS 和 G.8275.1 使用 `l2-non-forwardable`；AES67、SMPTE 和預設配置使用 `ipv4`）</ArgTableRow>
<ArgTableRow arg="profile" typ="enum (default | 802.1as | g8275.1 | aes67 | smpte-2059)">執行配置：`default`（普通 PTPv2）、`802.1as`（AVB/TSN，IEEE 802.1AS-2020）、`aes67`（IP 音訊）、`g8275.1`（電信頻率和相位）、`smpte-2059`（專業廣播）。該配置還會預設 domain、priority1/2、transport 和 delay-mode 的 auto 值</ArgTableRow>
<ArgTableRow arg="domain" typ="enum (auto)">PTP 域號，用於在同一網路上分隔相互獨立的 PTP 例項。允許的範圍因配置而異（大多數為 0-127，G.8275.1 為 24-43）。使用 `auto` 時，採用配置的預設值（預設配置/AES67：0，G.8275.1：24，SMPTE：127）</ArgTableRow>
<ArgTableRow arg="ptp-mode" typ="enum (ordinary-clock | transparent-clock)">例項的時鐘模式：普通時鐘（終端裝置；主時鐘或從時鐘）或透明時鐘（測量並轉發駐留時間，但不充當終端裝置）</ArgTableRow>
</ArgTable>
