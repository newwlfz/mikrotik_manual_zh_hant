---
sidebar_key: "cli-reference/tool/sniffer/save"
sidebar_position: 6
title: "save"
sidebar_label: 'save'
source: https://manual.mikrotik.com/docs/cli-reference/tool/sniffer/save
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/sniffer/save {#toolsniffersave}
**型別：** 命令

將記憶體中的封包寫入檔案。從 RouterOS 7.20 起，檔案始終為 pcapng 格式，即使副檔名為 `.pcap`；它會包含每個封包的介面名稱、方向以及納秒級時間戳。請參閱[封包嗅探器](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="file-name" typ="file">要寫入的檔名，例如 `capture.pcap`。</ArgTableRow>
</ArgTable>
