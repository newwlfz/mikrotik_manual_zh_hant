---
sidebar_key: "cli-reference/tool/sniffer/host"
sidebar_position: 2
title: "host"
sidebar_label: 'host'
source: https://manual.mikrotik.com/docs/cli-reference/tool/sniffer/host
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/sniffer/host {#toolsnifferhost}
**型別：** 目錄

上次捕獲流量中涉及的地址，及其速率和位元組數。請參閱 [封包嗅探器](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="ipAddr">在捕獲的封包中看到的地址。</ArgTableRow>
<ArgTableRow arg="rate" typ="composite { in: num
, out: num
 }">捕獲到的該地址流量的速率，以位元每秒為單位，包含兩個值：in（到該地址）和 out（從該地址）。這些速率在捕獲停止時計算；在 sniffer 執行期間，它們顯示為 0。</ArgTableRow>
<ArgTableRow arg="peak-rate" typ="composite { in: num
, out: num
 }">捕獲期間捕獲到的該地址流量的最高速率，以位元每秒為單位（in/out），在捕獲停止時計算。</ArgTableRow>
<ArgTableRow arg="total" typ="composite { in: num
, out: num
 }">捕獲到的該地址流量位元組數：in（到該地址）和 out（從該地址）。</ArgTableRow>
</ArgTable>
