---
sidebar_key: "cli-reference/disk/nvme-discover"
sidebar_position: 8
title: "nvme-discover"
sidebar_label: 'nvme-discover'
source: https://manual.mikrotik.com/docs/cli-reference/disk/nvme-discover
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/nvme-discover {#disknvme-discover}
**條件：** !smips
**系統能力：** storage
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="ipAddr">NVMe over TCP 控制器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="port" typ="num">控制器發現服務的 TCP 埠。預設值：4420。</ArgTableRow>
<ArgTableRow arg="host-name" typ="string">此路由器向控制器呈現的主機 NQN，用於標識和基於主機的訪問控制。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="nqn" typ="string">控制器公開的某個子系統的 NVMe 限定名稱。</ArgTableRow>
</ArgTable>
