---
sidebar_key: "cli-reference/routing/ospf/area/index"
sidebar_position: 1
title: "area"
sidebar_label: "area"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/ospf/area
captured_at: '2026-11-01T21:29:34+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/ospf/area {#routingospfarea}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="T" typ="transit-capable">transit-capable</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">區域的名稱</ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">此區域所屬的 OSPF 例項的名稱。</ArgTableRow>
<ArgTableRow arg="area-id" typ="ipAddr">OSPF 區域識別符號。如果路由器在多個區域中都有網路，則必須始終存在一個 `area-id=0.0.0.0` 的區域（骨幹區域）。骨幹區域始終包含所有區域邊界路由器。骨幹區域負責在非骨幹區域之間分發路由資訊。骨幹區域必須是連續的，即不能存在斷開的段。但是，區域邊界路由器不需要物理連線到骨幹區域——與骨幹區域的連線可以使用虛擬鏈路來模擬。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (default | stub | nssa)">區域型別。有關區域型別的更多資訊，請參閱 [OSPF 使用者指南](../../../../user-guides/routing-and-networking-protocols/unicast/ospf/index.md)。</ArgTableRow>
<ArgTableRow arg="no-summaries" typ="switch">標誌引數；如果設定，則該區域將不會在 stub 區域中泛洪 summary LSA。</ArgTableRow>
<ArgTableRow arg="default-cost" typ="num" unset="1">注入到該區域的 LSA 的預設開銷。如果未設定該值，則不會生成 stub 區域的 type-3 預設 LSA。</ArgTableRow>
<ArgTableRow arg="nssa-translator" typ="enum (candidate | no | yes)" unset="1">
該引數指示哪個 ABR 將用作從 `type-7` 到 `type-5` LSA 的轉換器。僅當區域型別為 NSSA 時適用。
- yes - 路由器將始終用作轉換器。
- no - 路由器絕不會用作轉換器。
- candidate - OSPF 會從候選路由器中選擇一個作為轉換器。
</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="transit-capable" typ="bool"></ArgTableRow>
</ArgTable>
