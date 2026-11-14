---
sidebar_key: "cli-reference/interface"
title: "interface"
sidebar_label: 'interface'
source: https://manual.mikrotik.com/docs/cli-reference/interface
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface {#interface}
**型別：** 目錄
帶計數器和狀態的介面列表。每條介面行都統計其自身的報文和位元組數；以 `fp` 開頭的值表示該流量中 Fast Path 所佔的份額（精簡的 CPU 轉發；HW 解除安裝的流量在兩者中均不顯示），而 `tx-queue-drop` 統計因介面佇列而丟棄的報文數。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">dynamic（自動建立）</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="S" typ="slave">slave（網橋或 bond 的成員）</ArgTableRow>
<ArgTableRow arg="P" typ="passthrough">passthrough</ArgTableRow>
<ArgTableRow arg="w" typ="power-limited">power-limited（在 PoE-out 板上電源預算生效）</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面名稱</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">已配置的 MTU</ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num">已配置的二層 MTU</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="default-name" typ="string">介面的出廠名稱</ArgTableRow>
<ArgTableRow arg="type" typ="string">介面型別</ArgTableRow>
<ArgTableRow arg="actual-mtu" typ="num">生效的 MTU（硬體/驅動協商）</ArgTableRow>
<ArgTableRow arg="max-l2mtu" typ="num">硬體/驅動支援的最大二層 MTU</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">介面所繫結的 VRF（留空表示主路由表）</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">介面的 MAC 地址</ArgTableRow>
<ArgTableRow arg="last-link-down-time" typ="date">鏈路最後一次斷開的時間</ArgTableRow>
<ArgTableRow arg="last-link-up-time" typ="date">鏈路最後一次連通的時間</ArgTableRow>
<ArgTableRow arg="link-downs" typ="num">鏈路斷開的次數</ArgTableRow>
<ArgTableRow arg="rx-byte" typ="num">接收的位元組數</ArgTableRow>
<ArgTableRow arg="tx-byte" typ="num">傳送的位元組數</ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num">接收的封包數</ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num">傳送的封包數</ArgTableRow>
<ArgTableRow arg="rx-drop" typ="num">接收但被丟棄的封包數</ArgTableRow>
<ArgTableRow arg="tx-drop" typ="num">傳輸過程中被丟棄的封包數</ArgTableRow>
<ArgTableRow arg="tx-queue-drop" typ="num">被介面佇列丟棄的封包數(擁塞訊號)</ArgTableRow>
<ArgTableRow arg="rx-error" typ="num">損壞的接收幀數</ArgTableRow>
<ArgTableRow arg="tx-error" typ="num">傳輸錯誤數</ArgTableRow>
<ArgTableRow arg="fp-rx-byte" typ="num">透過 Fast Path 接收的位元組數</ArgTableRow>
<ArgTableRow arg="fp-tx-byte" typ="num">透過 Fast Path 傳送的位元組數</ArgTableRow>
<ArgTableRow arg="fp-rx-packet" typ="num">透過 Fast Path 接收的封包數</ArgTableRow>
<ArgTableRow arg="fp-tx-packet" typ="num">透過 Fast Path 傳送的封包數</ArgTableRow>
<ArgTableRow arg="fp-rps-drop" typ="num">在 receive-packet-steering 路徑中丟棄的封包數</ArgTableRow>
</ArgTable>
