---
sidebar_key: "cli-reference/tool/mac-telnet"
sidebar_position: 12
title: "mac-telnet"
sidebar_label: 'mac-telnet'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/mac-telnet
captured_at: '2026-11-01T21:25:55+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/mac-telnet {#toolmac-telnet}
**型別：** 命令

透過 MAC 地址，向同一二層網段上的裝置開啟一個 MAC Telnet 會話。用戶端會提示輸入使用者名稱和密碼。當裝置無響應或拒絕連線時，該命令會直接返回到提示符，不顯示任何錯誤資訊。示例請參見 [MAC 伺服器](../../management-tools/mac-server.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="host" typ="enum ()">要連線的裝置的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" unset="1">用於發出連線嘗試的介面。若不指定，用戶端會從每個介面發出連線嘗試。</ArgTableRow>
</ArgTable>
