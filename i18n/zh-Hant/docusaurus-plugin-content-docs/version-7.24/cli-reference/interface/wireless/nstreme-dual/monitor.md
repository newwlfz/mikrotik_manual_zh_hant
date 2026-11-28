---
title: "monitor"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/wireless/nstreme-dual/monitor
captured_at: '2026-11-28T10:19:39.818Z'
pagination_prev: "cli-reference/interface/wireless/nstreme-dual"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/wireless/nstreme-dual/monitor 
**套件:** wireless-rep
**類型:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="rx-signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="connected" typ="bool"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="frames" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="frame-bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="hw-frames" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="hw-frame-bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-retries-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-retries-lost" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-seqs" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-duplicates" typ="num"></ArgTableRow>
</ArgTable>
