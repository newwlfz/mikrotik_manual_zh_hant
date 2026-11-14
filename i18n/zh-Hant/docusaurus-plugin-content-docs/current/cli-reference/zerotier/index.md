---
sidebar_key: "cli-reference/zerotier"
title: "zerotier"
sidebar_label: 'zerotier'
source: https://manual.mikrotik.com/docs/cli-reference/zerotier
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## zerotier {#zerotier}
**軟體包：** zerotier
**型別：** 目錄

[ZeroTier](../../virtual-private-networks/zerotier.md) 網路虛擬機器監控程式是一個自包含的網路虛擬化引擎，它實現乙太網虛擬化層

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">條目是否已停用。</ArgTableRow>
<ArgTableRow arg="R" typ="online">例項是否線上。</ArgTableRow>
<ArgTableRow arg="F" typ="tcp-fallback">TCP 回退是否處於活動狀態。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">例項名稱。</ArgTableRow>
<ArgTableRow arg="disabled" typ="bool">條目是否已停用。</ArgTableRow>
<ArgTableRow arg="port" typ="num">例項監聽的埠號。</ArgTableRow>
<ArgTableRow arg="identity" typ="string">例項的 40 位唯一地址。</ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, interface: iface_enum
 }">用於透過 ARP 和 IP 型別連線發現 ZeroTier 對等體的介面列表。</ArgTableRow>
<ArgTableRow arg="route-distance" typ="num">從 planet/moon 伺服器獲取的路由所對應的路由距離。</ArgTableRow>
<ArgTableRow arg="backup-priorities" typ="multi { array-id, array-id, backup-priority: composite { interface: iface_enum
, priority: num
 }
 }">用於故障轉移的備用介面優先順序。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="identity.public" typ="string">例項的公開身份。</ArgTableRow>
<ArgTableRow arg="state" typ="string">例項的當前狀態。</ArgTableRow>
<ArgTableRow arg="moons" typ="multi { array-id, moon: string
 }">例項連線到的 moon 列表。</ArgTableRow>
</ArgTable>
