---
sidebar_key: "cli-reference/tool/wol"
sidebar_position: 28
title: "wol"
sidebar_label: 'wol'
source: https://manual.mikrotik.com/docs/cli-reference/tool/wol
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/wol {#toolwol}
**型別：** 命令

關於完整文件，請參閱 [網路喚醒](../../system-information-and-utilities/wake-on-lan.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum">傳送魔術包所用的介面，例如 LAN 網橋。指定介面時，路由器會向其上的廣播 MAC 地址傳送乙太網幀（EtherType `0x0842`）。未指定介面時，它會透過預設路由向 `255.255.255.255` 的 9 埠傳送 UDP 封包，而在大多數路由器上，預設路由就是網際網路連線。</ArgTableRow>
<ArgTableRow arg="mac" typ="macAddr">要喚醒的計算機的 MAC 地址。魔術包中會包含該地址 16 次。</ArgTableRow>
</ArgTable>
