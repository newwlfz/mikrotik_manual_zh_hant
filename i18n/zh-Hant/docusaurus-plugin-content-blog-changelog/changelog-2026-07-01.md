---
title: "文件更新 - 2026年7月1日"
date: 2026-07-01
slug: /changelog-2026-07-01
source: https://manual.mikrotik.com/changelog/changelog-2026-07-01
captured_at: '2026-11-04T06:08:05+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 7 月 1 日所做的文件變更摘要。

## 診斷與監控 {#diagnostics--monitoring}

- **[Netwatch](/docs/diagnostics-monitoring-and-troubleshooting/netwatch)**：probe-type 列表（Simple、ICMP、TCP-conn、HTTP-GET、HTTPS-GET、DNS）現在已加粗以提高可讀性，並修正了若干拼寫和措辭問題。CLI 參考中的每個 ICMP、TCP-conn 和 HTTP/S-GET 引數現在都直接連結到本頁上對應的 probe-type 部分。

## 網路管理 {#network-management}

- **[Socksify](/docs/network-management/socks/socksify)**：添加了指向 CLI 參考的交叉連結，並記錄了所有 Socksify 引數的說明和預設值——connection-timeout（60s）、port（952）、socks5-server（0.0.0.0，僅 IPv4）、socks5-port（1080）、socks5-user 和 socks5-password。現在註明 X 標誌預設已設定。

## CLI 參考 {#cli-reference}

- **[/app](/docs/cli-reference/app)**：為容器應用標誌（X、R、c、s）以及所有引數添加了說明，包括 container-command-lines、auto-update、use-https、network、network-pvid、network-outgoing-access、firewall-redirects、yaml 和 required-mounts。
- **[/beep](/docs/cli-reference/beep) 和 [/blink](/docs/cli-reference/blink)**：添加了命令說明和引數詳細資訊——beep 的頻率（Hz）和長度，blink 的持續時間。註明 beep 僅在帶有蜂鳴器的裝置上受支援。
