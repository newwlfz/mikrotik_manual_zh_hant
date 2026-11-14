---
sidebar_key: "cli-reference/system/package/index"
sidebar_position: 5
title: "package"
sidebar_label: "package"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/package
captured_at: '2026-11-01T21:29:57+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/package {#systempackage}
**型別：** 目錄

在此選單中執行的命令只會在路由器重啟時生效。在此之前，您可以自由安排或還原已設定的操作。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="A" typ="available"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">軟體包的名稱。</ArgTableRow>
<ArgTableRow arg="version" typ="string">軟體包的版本。</ArgTableRow>
<ArgTableRow arg="build-time" typ="date">軟體包的構建日期和時間。</ArgTableRow>
<ArgTableRow arg="scheduled" typ="enum ( | scheduled for uninstall | scheduled for disable | scheduled for enable | Use `apply-changes` to proceed with install) { :0, scheduled for uninstall:1, scheduled for disable:2, scheduled for enable:3, Use `apply-changes` to proceed with install:4 }">軟體包在下次重啟後的計劃操作。</ArgTableRow>
<ArgTableRow arg="bundle" typ="enum">此軟體包所屬的 bundle 軟體包。</ArgTableRow>
<ArgTableRow arg="size" typ="num">軟體包大小，以位元組為單位。</ArgTableRow>
</ArgTable>
