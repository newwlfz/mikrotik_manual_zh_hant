---
sidebar_key: "cli-reference/certificate/settings"
sidebar_position: 15
title: "settings"
sidebar_label: "settings"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/certificate/settings
captured_at: '2026-11-01T21:26:28+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## certificate/settings {#certificatesettings}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="builtin-trust-store" typ="alt { all-none: enum (default | all | untrusted)
, component: ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging)
 }">RouterOS 提供的 CA 證書</ArgTableRow>
<ArgTableRow arg="current-defaults" typ="ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging)"></ArgTableRow>
<ArgTableRow arg="crl-download" typ="bool">自動下載並更新 CRL</ArgTableRow>
<ArgTableRow arg="crl-use" typ="bool">驗證信任鏈時執行 CRL 檢查</ArgTableRow>
<ArgTableRow arg="crl-store" typ="enum (system | ram)">CRL 儲存位置</ArgTableRow>
</ArgTable>
