---
sidebar_key: "cli-reference/ipv6/dhcp-server/binding/send-reconfigure"
sidebar_position: 2
title: "send-reconfigure"
sidebar_label: 'send-reconfigure'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ipv6/dhcp-server/binding/send-reconfigure
captured_at: '2026-11-01T21:24:36+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-server/binding/send-reconfigure {#ipv6dhcp-serverbindingsend-reconfigure}
**型別：** 命令

向該繫結的用戶端傳送一條 Reconfigure 訊息，使用戶端立即進行續約。要求伺服器上設定 `use-reconfigure=yes`，並且用戶端接受 Reconfigure 訊息，例如啟用了 `allow-reconfigure=yes` 的 RouterOS DHCPv6 用戶端。
