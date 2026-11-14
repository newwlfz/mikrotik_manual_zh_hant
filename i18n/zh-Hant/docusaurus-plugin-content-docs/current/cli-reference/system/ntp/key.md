---
sidebar_key: "cli-reference/system/ntp/key"
sidebar_position: 2
title: "key"
sidebar_label: 'key'
source: https://manual.mikrotik.com/docs/cli-reference/system/ntp/key
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ntp/key {#systemntpkey}
**型別：** 目錄

用於 NTP 身份驗證的對稱金鑰，透過其在 [`/system/ntp/client/servers`](./client/servers.md) 和 [`/system/ntp/server`](./server.md) 中的金鑰 ID 進行選擇。金鑰值屬於敏感資訊：它不會顯示在 `print` 中，也不會儲存到 `export` 輸出中。請參閱 [NTP](../../../system-information-and-utilities/ntp.md) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="key-id" typ="num" mandatory="1">金鑰識別符號，由用戶端和伺服器配置中的 `auth-key` 引用。</ArgTableRow>
<ArgTableRow arg="key-val" typ="string" mandatory="1">共享金鑰。不包含在 `export` 輸出中。</ArgTableRow>
</ArgTable>
