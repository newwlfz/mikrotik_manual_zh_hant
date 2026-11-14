---
sidebar_key: "cli-reference/cmr/wifi/radio"
sidebar_position: 1
title: "radio"
sidebar_label: 'radio'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/wifi/radio
captured_at: '2026-11-09T11:35:47.715Z'
pagination_prev: "cli-reference/cmr/wifi"
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/wifi/radio {#cmrwifiradio}
**包：** cmr
**型別：** 目錄

複製到所選裝置的無線電配置。這些引數擴充套件了標準 RouterOS `/interface/wifi` 無線電配置引數。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">無線電配置已停用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="labels" typ="object" unset="1">選擇使用標籤將無線電配置複製到的裝置。支援用 + 和 - 符號分別表示 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。</ArgTableRow>
<ArgTableRow arg="configuration.country" typ="enum" unset="1">國家程式碼。</ArgTableRow>
<ArgTableRow arg="configuration.chains" typ="ubit (0, 1, 2, 3, 4, 5, 6, 7)" unset="1">要使用的無線電鏈路。</ArgTableRow>
<ArgTableRow arg="configuration.tx-chains" typ="ubit ()" unset="1">傳送鏈路。</ArgTableRow>
<ArgTableRow arg="configuration.tx-power" typ="num" unset="1">發射功率。</ArgTableRow>
<ArgTableRow arg="configuration.antenna-gain" typ="num" unset="1">天線增益。</ArgTableRow>
<ArgTableRow arg="configuration.distance" typ="num" unset="1">到最遠已連線用戶端的距離。</ArgTableRow>
<ArgTableRow arg="configuration.installation" typ="enum (outdoor | indoor)" unset="1">安裝型別：`outdoor` 或 `indoor`。</ArgTableRow>
<ArgTableRow arg="security.authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, wpa3-psk-gd, owe, wpa3-eap, wpa3-eap-192)" unset="1">支援的認證型別。</ArgTableRow>
<ArgTableRow arg="channel.frequency" typ="object" unset="1">通道頻率。</ArgTableRow>
<ArgTableRow arg="channel.secondary-frequency" typ="multi { array-id, secondary-frequency: alt { secondary-frequency-disable: enum (disabled)
, secondary-frequency-num: num
 }
 }" unset="1">次要通道頻率。</ArgTableRow>
<ArgTableRow arg="channel.band" typ="enum (60ghz-ad | 5ghz-a | 5ghz-n | 5ghz-ac | 5ghz-ax | 5ghz-be | 2ghz-g | 2ghz-n | 2ghz-ax | 2ghz-be | s1ghz-ah | 6ghz-ax | 6ghz-be)" unset="1">工作頻段。</ArgTableRow>
<ArgTableRow arg="channel.width" typ="enum (20mhz | 20/40mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz | 20/40/80+80mhz | 20/40/80/160mhz | 20/40/80/160/320mhz | 1mhz | 1/2mhz | 1/2/4mhz | 1/2/4/8mhz | 1080mhz | 2160mhz)" unset="1">通道寬度。</ArgTableRow>
<ArgTableRow arg="channel.skip-dfs-channels" typ="enum (disabled | all | 10min-cac)" unset="1">DFS 通道處理方式：`disabled`、`all`、`10min-cac`。</ArgTableRow>
<ArgTableRow arg="channel.deprioritize-unii-3-4" typ="bool" unset="1">降低 UNII-3/UNII-4 通道的優先順序。</ArgTableRow>
<ArgTableRow arg="channel.reselect-interval" typ="super { reselect-interval-min: time [1 .. 60*60*24*300]
, [reselect-interval-max] ..time [1 .. 60*60*24*300]
 }" unset="1">通道重選間隔範圍。</ArgTableRow>
<ArgTableRow arg="channel.reselect-time" typ="super { reselect-time-min: date
, [reselect-time-max] ..date
 }" unset="1">通道重選時間範圍。</ArgTableRow>
<ArgTableRow arg="channel.preamble-puncturing" typ="alt { preamble-puncturing: enum (yes | no) { yes:-1, no:0 }
 }" unset="1">前導碼打孔：`yes` 或 `no`。</ArgTableRow>
<ArgTableRow arg="channel.afc" typ="bool" unset="1">啟用 AFC（自動頻率協調）。</ArgTableRow>
</ArgTable>
