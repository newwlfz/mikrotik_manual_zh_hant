---
sidebar_key: "cli-reference/system/license/index"
sidebar_position: 2
title: "license"
sidebar_label: 'license'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/license
captured_at: '2026-11-01T21:25:31+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/license {#systemlicense}
**型別：** 設定目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="software-id" typ="string" syscap="nochr">MikroTik 硬體和 x86 系統的唯一識別符號，用於授權。繫結到裝置儲存。</ArgTableRow>
<ArgTableRow arg="old-software-id" typ="string" syscap="nochr">之前的 Software ID，在 ID 發生變化時顯示。</ArgTableRow>
<ArgTableRow arg="nlevel" typ="num" syscap="nochr">許可證級別編號（0-6）。</ArgTableRow>
<ArgTableRow arg="features" typ="ubit (AP, synchronous, radiolan, wireless, extra-channels, , , )" syscap="nochr">已授權功能的位掩碼。</ArgTableRow>
<ArgTableRow arg="expires-in" typ="time" syscap="nochr">試用許可證到期前剩餘的時間。</ArgTableRow>
<ArgTableRow arg="system-id" typ="string" syscap="chr">CHR 例項的唯一識別符號，用於授權。許可證直接繫結到 CHR 系統 ID。</ArgTableRow>
<ArgTableRow arg="level" typ="enum (free | p1 | p10 | p-unlimited) { free:0, p1:1, p10:2, p-unlimited:3 }" syscap="chr">當前 CHR 許可證級別。</ArgTableRow>
<ArgTableRow arg="limited-upgrades" typ="bool" syscap="chr">指示 RouterOS 升級是否受限。當值為 `yes` 時，無法升級 RouterOS，並且停用軟體包更改。</ArgTableRow>
<ArgTableRow arg="next-renewal-at" typ="date" syscap="chr">路由器下次嘗試聯絡 MikroTik 許可證伺服器的時間。</ArgTableRow>
<ArgTableRow arg="deadline-at" typ="date" syscap="chr">必須與許可證伺服器成功通訊的最晚時間。</ArgTableRow>
</ArgTable>
