---
title: "文件更新 - 2026年7月30日"
date: 2026-07-30
slug: /changelog-2026-07-30
source: https://manual.mikrotik.com/changelog/changelog-2026-07-30
captured_at: '2026-11-04T06:08:22+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 7 月 30 日的文件變更摘要。

## 防火牆與 QoS {#firewall--qos}

- **[Queues](/docs/firewall-and-quality-of-service/queues)** 和 **[CAKE](/docs/firewall-and-quality-of-service/queues/queue-types/cake)**：大幅重寫了 CAKE 文件——新增了適合初學者的操作流程，闡明瞭 cake-bandwidth 與 HTB 的 limit-at/max-limit 之間的區別，解釋了 Interface Queue 在傳送與接收方向上的行為差異，補全了若干此前為空的引數說明，並精簡了 Queues 頁面上重複的 CAKE 概述，改為連結到完整指南。

## 入門 {#getting-started}

- **[Netinstall Package](/docs/getting-started/installation-and-upgrade/netinstall/netinstall-package)**：為 preboot-etherboot-server 添加了一條 IP 範圍配置說明。
