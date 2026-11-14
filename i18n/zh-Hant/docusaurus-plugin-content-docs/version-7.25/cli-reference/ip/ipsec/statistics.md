---
sidebar_key: "cli-reference/ip/ipsec/statistics"
sidebar_position: 11
title: "statistics"
sidebar_label: 'statistics'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/ipsec/statistics
captured_at: '2026-11-01T21:24:14+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/statistics {#ipipsecstatistics}
**型別：** 設定目錄

此選單顯示各種 IPsec 統計資訊和錯誤。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="in-errors" typ="num">輸入錯誤事件的數量。</ArgTableRow>
<ArgTableRow arg="in-buffer-errors" typ="num">輸入緩衝區錯誤的數量。</ArgTableRow>
<ArgTableRow arg="in-header-errors" typ="num">輸入頭部錯誤的數量。</ArgTableRow>
<ArgTableRow arg="in-no-states" typ="num">因無匹配狀態而丟棄的輸入封包數量。</ArgTableRow>
<ArgTableRow arg="in-state-protocol-errors" typ="num">輸入狀態協定錯誤的數量。</ArgTableRow>
<ArgTableRow arg="in-state-mode-errors" typ="num">輸入狀態模式錯誤的數量。</ArgTableRow>
<ArgTableRow arg="in-state-sequence-errors" typ="num">輸入狀態序列錯誤的數量。</ArgTableRow>
<ArgTableRow arg="in-state-expired" typ="num">狀態已過期的輸入封包數量。</ArgTableRow>
<ArgTableRow arg="in-state-mismatches" typ="num">輸入狀態不匹配的數量。</ArgTableRow>
<ArgTableRow arg="in-state-invalid" typ="num">狀態無效的輸入封包數量。</ArgTableRow>
<ArgTableRow arg="in-template-mismatches" typ="num">輸入模板不匹配的數量。</ArgTableRow>
<ArgTableRow arg="in-no-policies" typ="num">無匹配策略的輸入封包數量。</ArgTableRow>
<ArgTableRow arg="in-policy-blocked" typ="num">被策略阻止的輸入封包數量。</ArgTableRow>
<ArgTableRow arg="in-policy-errors" typ="num">輸入策略錯誤的數量。</ArgTableRow>
<ArgTableRow arg="out-errors" typ="num">輸出錯誤事件的數量。</ArgTableRow>
<ArgTableRow arg="out-bundle-errors" typ="num">輸出捆綁錯誤的數量。</ArgTableRow>
<ArgTableRow arg="out-bundle-check-errors" typ="num">輸出捆綁檢查錯誤的數量。</ArgTableRow>
<ArgTableRow arg="out-no-states" typ="num">因無匹配狀態而丟棄的輸出封包數量。</ArgTableRow>
<ArgTableRow arg="out-state-protocol-errors" typ="num">輸出狀態協定錯誤的數量。</ArgTableRow>
<ArgTableRow arg="out-state-mode-errors" typ="num">輸出狀態模式錯誤的數量。</ArgTableRow>
<ArgTableRow arg="out-state-sequence-errors" typ="num">輸出狀態序列錯誤的數量。</ArgTableRow>
<ArgTableRow arg="out-state-expired" typ="num">狀態已過期的輸出封包數量。</ArgTableRow>
<ArgTableRow arg="out-policy-blocked" typ="num">被策略阻止的輸出封包數量。</ArgTableRow>
<ArgTableRow arg="out-policy-dead" typ="num">策略已失效的輸出封包數量。</ArgTableRow>
<ArgTableRow arg="out-policy-errors" typ="num">輸出策略錯誤的數量。</ArgTableRow>
</ArgTable>
