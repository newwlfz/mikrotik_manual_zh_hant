---
sidebar_key: "cli-reference/ip/cloud/back-to-home-user/show-client-config"
sidebar_position: 1
title: "show-client-config"
sidebar_label: 'show-client-config'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/cloud/back-to-home-user/show-client-config
captured_at: '2026-11-01T21:23:51+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/cloud/back-to-home-user/show-client-config {#ipcloudback-to-home-usershow-client-config}
**系統能力：** cloud-vpn
**型別：** 命令

列印某個使用者的 WireGuard 配置，並以二維條碼形式輸出同一份配置。在 WireGuard 應用中匯入它。透過編號指定使用者，或使用 `[find name=<name>]` 指定；僅給出名稱屬於語法錯誤。該配置包含第二個對等體，其使用佔位金鑰且 `AllowedIPs = 0.0.0.0/32`，不會承載任何流量；用戶端透過第一個對等體建立連線，當路由器使用中繼時也是如此。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="conf" typ="string">該使用者的 WireGuard 配置。</ArgTableRow>
<ArgTableRow arg="qr" typ="pic">以二維條碼形式表示的配置。</ArgTableRow>
</ArgTable>
