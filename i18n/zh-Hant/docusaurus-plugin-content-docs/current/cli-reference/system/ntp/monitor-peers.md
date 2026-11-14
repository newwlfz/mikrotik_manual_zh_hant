---
sidebar_key: "cli-reference/system/ntp/monitor-peers"
sidebar_position: 3
title: "monitor-peers"
sidebar_label: 'monitor-peers'
source: https://manual.mikrotik.com/docs/cli-reference/system/ntp/monitor-peers
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ntp/monitor-peers {#systemntpmonitor-peers}
**型別：** 命令

持續顯示用戶端對其時間源的檢視，並在原位置重新整理。當啟用 `use-local-clock` 時，會包含本地參考時鐘（127.127.1.0）。請參閱 [NTP](../../../system-information-and-utilities/ntp.md) 指南。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="type" typ="string">關聯型別，例如單播伺服器為 `ucast-client`。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">來自伺服器列表的對等體地址，或本地參考時鐘的 127.127.1.0。</ArgTableRow>
<ArgTableRow arg="refid" typ="string">參考 ID：對等體的時間源（通常是該對等體自身上游源的地址）。當對等體未同步時為空。</ArgTableRow>
<ArgTableRow arg="stratum" typ="num">對等體通告的層級。16 表示未同步。</ArgTableRow>
<ArgTableRow arg="hpoll" typ="num">當前與該對等體的輪詢間隔，以 2 的冪表示秒數（6 = 64 秒）。</ArgTableRow>
<ArgTableRow arg="ppoll" typ="num">對等體請求的輪詢間隔，以 2 的冪表示秒數。</ArgTableRow>
<ArgTableRow arg="root-delay" typ="num">從該對等體到根（第 1 層）時間源的總往返延遲。</ArgTableRow>
<ArgTableRow arg="root-disp" typ="num">該對等體相對於根時間源的最大誤差。</ArgTableRow>
<ArgTableRow arg="offset" typ="num">該對等體相對於本地時鐘的估計時鐘偏移。</ArgTableRow>
<ArgTableRow arg="delay" typ="num">到該對等體的往返延遲。</ArgTableRow>
<ArgTableRow arg="disp" typ="num">該對等體的離散度：其時間的累計測量誤差。</ArgTableRow>
<ArgTableRow arg="jitter" typ="num">連續取樣之間偏移的變化量。</ArgTableRow>
</ArgTable>
