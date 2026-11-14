---
sidebar_key: "cli-reference/system/license/generate-new-id"
sidebar_position: 1
title: "generate-new-id"
sidebar_label: 'generate-new-id'
source: https://manual.mikrotik.com/docs/cli-reference/system/license/generate-new-id
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/license/generate-new-id {#systemlicensegenerate-new-id}
**系統能力：** chr
**型別：** 命令

為 CHR 例項生成一個新的唯一系統 ID。當從同一磁碟映象部署多個 CHR 例項時，請在首次啟動之後、申請試用許可證之前使用該命令，以避免出現相同的系統 ID。

:::warning
該命令只能在執行 Free 許可證級別的 CHR 上使用。在已應用試用許可證或付費許可證之後，請勿使用該命令。
:::
