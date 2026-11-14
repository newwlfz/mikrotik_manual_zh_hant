---
sidebar_key: "cli-reference/interface/xfrm"
sidebar_position: 44
title: "xfrm"
sidebar_label: 'xfrm'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/xfrm
captured_at: '2026-11-01T21:23:31+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/xfrm {#interfacexfrm}
**型別：** 目錄

XFRM 介面提供基於路由的 IPsec 端點。將 IPsec 策略組繫結到該介面，然後將發往遠端網路的流量透過該介面路由。繫結組中的策略會加密進入該介面的流量，解密後的流量透過同一介面傳遞。

配置示例請參見 [基於路由的 IPsec 與 XFRM 介面](../../virtual-private-networks/ipsec/index.md#route-based-ipsec-with-xfrm-interfaces)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">介面是否已停用。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。當使用該介面的 IPsec SA 建立時，該標誌會出現。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面名稱。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">第 3 層最大傳輸單元。預設值：`1400`。</ArgTableRow>
</ArgTable>
