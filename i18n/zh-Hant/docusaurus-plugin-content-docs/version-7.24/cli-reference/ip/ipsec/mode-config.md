---
sidebar_key: "cli-reference/ip/ipsec/mode-config"
sidebar_position: 5
title: "mode-config"
sidebar_label: "mode-config"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/ipsec/mode-config
captured_at: '2026-11-01T21:28:47+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/mode-config {#ipipsecmode-config}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="R" typ="responder">responder</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="responder" typ="bool">對端應請求或傳送配置</ArgTableRow>
<ArgTableRow arg="system-dns" typ="bool">向對端傳送系統 DNS 伺服器</ArgTableRow>
<ArgTableRow arg="static-dns" typ="object { address: alt { address4: ipAddr
 }
 }">傳送給對端的 DNS 伺服器，與 system-dns 互斥</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (none) { none:-1 }">從此地址池中為對端分配一個地址</ArgTableRow>
<ArgTableRow arg="address-prefix-length" typ="num">所分配地址的子網掩碼</ArgTableRow>
<ArgTableRow arg="split-include" typ="object { subnet: alt { subnet4: ipPrefix
 }
 }">額外的受保護子網</ArgTableRow>
<ArgTableRow arg="split-dns" typ="multi { array-id, dns: string
 }">要使用內部伺服器解析的 DNS 名稱</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="enum ()">要新增到發起方 srcnat 鏈的地址列表名稱</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="enum ()">要新增到發起方 srcnat 鏈的 conection-mark</ArgTableRow>
<ArgTableRow arg="use-responder-dns" typ="enum (no | yes | exclusively)">傳送的 DNS 伺服器是否應由發起方使用</ArgTableRow>
</ArgTable>
