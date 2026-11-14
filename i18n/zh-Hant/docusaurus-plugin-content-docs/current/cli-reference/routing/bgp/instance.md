---
sidebar_key: "cli-reference/routing/bgp/instance"
sidebar_position: 4
title: "instance"
sidebar_label: 'instance'
source: https://manual.mikrotik.com/docs/cli-reference/routing/bgp/instance
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bgp/instance {#routingbgpinstance}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1">用於安裝路由的路由表名稱。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">BGP 連線所使用的 VRF 名稱。預設始終使用 "main" 路由表。</ArgTableRow>
<ArgTableRow arg="router-id" typ="alt { ip: ipAddr
, name: enum
 }" unset="1">要使用的 BGP 路由器 ID。透過指定引用名稱來使用 `/routing/router-id` 配置中的 ID，或直接指定 IP 來設定 ID。相同的 router-id 也用於將 peer 分組到同一個例項中。</ArgTableRow>
<ArgTableRow arg="as" typ="super { as: as
, [sub-as] [ /as]
 }" unset="1">32 位 BGP 自治系統號。以 AS-Plain 或 AS-Dot 格式輸入該值。使用以下格式配置 BGP 聯盟：_`confederation_as/as`_。例如，如果你的 AS 是 34，聯盟 AS 是 43，請設定 `as=43/34`。</ArgTableRow>
<ArgTableRow arg="cluster-id" typ="ipAddr" unset="1">對於路由反射器例項，指定路由反射器叢集的叢集 ID。此屬性用於識別來自叢集中其他路由反射器的路由更新，以避免路由資訊環路。通常每個叢集只有一個路由反射器；在這種情況下，不要配置 'cluster-id'，而會改用 BGP 路由器 ID。</ArgTableRow>
<ArgTableRow arg="ignore-as-path-len" typ="bool" unset="1">在 BGP 路由選擇演算法中忽略 **AS_PATH** 屬性。適用於輸入。</ArgTableRow>
<ArgTableRow arg="multipath" typ="num" unset="1">安裝指定數量的 ECMP 路由，這些路由由 add-path 接收或由[最佳路徑選擇](../../../user-guides/routing-and-networking-protocols/unicast/bgp/understanding-bgp.md#best-path-selection)選出。</ArgTableRow>
<ArgTableRow arg="always-compare-med" typ="bool" unset="1"></ArgTableRow>
</ArgTable>
