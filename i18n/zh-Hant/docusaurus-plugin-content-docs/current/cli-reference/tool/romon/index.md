---
sidebar_key: "cli-reference/tool/romon"
title: "romon"
sidebar_label: 'romon'
source: https://manual.mikrotik.com/docs/cli-reference/tool/romon
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/romon {#toolromon}
**型別：** 設定目錄

RoMON（Router Management Overlay Network，路由器管理覆蓋網路）服務的設定。請參閱 [RoMON](../../../management-tools/romon.md) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">停用或啟用 RoMON 功能。</ArgTableRow>
<ArgTableRow arg="id" typ="macAddr">用作此路由器 ID 的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="secrets" typ="multi { array-id, name: string
 }">用於 RoMON 訊息雜湊的全域性金鑰列表。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="current-id" typ="macAddr">當前正在使用的 RoMON ID，在未設定 `id` 時自動從埠 MAC 地址中選擇。</ArgTableRow>
</ArgTable>
