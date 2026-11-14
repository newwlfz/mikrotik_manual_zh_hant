---
sidebar_key: "cli-reference/system/resource/irq/rps"
sidebar_position: 1
title: "rps"
sidebar_label: 'rps'
source: https://manual.mikrotik.com/docs/cli-reference/system/resource/irq/rps
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/resource/irq/rps {#systemresourceirqrps}
**系統能力：** rps
**型別：** Directory
接收封包引導（RPS）條目：每個條目為其介面啟用 RPS（該介面接收路徑的封包處理工作透過軟體分散到各個 CPU 核心上）。有關 RPS 何時能帶來收益，請參閱[資源指南](../../../../diagnostics-monitoring-and-troubleshooting/resource.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用的條目（此介面的 RPS steering 已關閉）</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">接收路徑被引導的介面</ArgTableRow>
</ArgTable>
