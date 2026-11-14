---
sidebar_key: "cli-reference/ip/dhcp-server/lease/send-reconfigure"
sidebar_position: 3
title: "send-reconfigure"
sidebar_label: 'send-reconfigure'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-server/lease/send-reconfigure
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/lease/send-reconfigure {#ipdhcp-serverleasesend-reconfigure}
**型別:** Command

向該租約的用戶端傳送 Reconfigure（FORCERENEW）訊息，使用戶端立即續租。它僅對獲得了 reconfigure 金鑰的用戶端有效，這要求伺服器上設定 `use-reconfigure=yes`，並且用戶端請求該金鑰，例如使用 `allow-reconfigure=yes` 的 RouterOS DHCP 用戶端。
