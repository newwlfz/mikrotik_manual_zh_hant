---
sidebar_key: "cli-reference/ip/ipsec/settings"
sidebar_position: 10
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/ipsec/settings
captured_at: '2026-11-01T21:24:14+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/settings {#ipipsecsettings}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="xauth-use-radius" typ="bool">是否對 XAuth 使用者使用 Radius 用戶端。該屬性僅適用於使用 IKEv1 交換模式的對等體。</ArgTableRow>
<ArgTableRow arg="accounting" typ="bool">是否向 RADIUS 伺服器傳送 RADIUS 計費請求。適用於使用 EAP Radius（auth-method=eap-radius）或使用帶 XAuth 認證方法的預共享金鑰（auth-method=pre-shared-key-xauth）的情況。</ArgTableRow>
<ArgTableRow arg="interim-update" typ="time">每次連續 RADIUS 計費 Interim 更新之間的間隔。必須啟用計費。</ArgTableRow>
<ArgTableRow arg="ddos-cookie-threshold" typ="num">DDOS cookie 啟用閾值。</ArgTableRow>
</ArgTable>
