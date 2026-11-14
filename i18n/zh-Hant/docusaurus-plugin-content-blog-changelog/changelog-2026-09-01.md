---
title: "文件更新 - 2026年9月1日"
date: 2026-09-01
slug: /changelog-2026-09-01
source: https://manual.mikrotik.com/changelog/changelog-2026-09-01
captured_at: '2026-11-04T06:08:40+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 9 月 1 日文件變更摘要。

## 系統 {#system}

- **[Clock](/docs/system-information-and-utilities/clock)**、**[Device Mode](/docs/system-information-and-utilities/device-mode)**、**[E-mail](/docs/system-information-and-utilities/e-mail)**、**[Fetch](/docs/system-information-and-utilities/fetch)**、**[Files](/docs/system-information-and-utilities/files)**、**[Identity](/docs/system-information-and-utilities/identity)**、**[IP Packing](/docs/system-information-and-utilities/ip-packing)** 和 **[Neighbor Discovery](/docs/system-information-and-utilities/neighbor-discovery)**：修復了語法問題，並將 CLI 引數說明移至 CLI Reference。
- **Interface Lists**：刪除了舊的 System 頁面，並將其內容移至 [CLI Reference](/docs/cli-reference/interface/list)，同時更新了手冊中的所有交叉連結。

## 管理工具 {#management-tools}

- **[TR-069](/docs/management-tools/tr-069)**：修復了語法和樣式問題，並將 CLI 引數移至 CLI Reference。

## 入門 {#getting-started}

- **[Upgrade](/docs/getting-started/installation-and-upgrade/upgrade)**：記錄了安全軟體包下載方式以及更新所使用的 IP 版本。
- **[x86 Licensing](/docs/getting-started/routeros-licensing/x86)**：說明 demo 許可證僅限單個介面。

## 容器 {#containers}

- **[Container Apps](/docs/containers/apps)**：擴充套件了 app YAML 參考，新增了欄位（auto-update、icon、url-path、user、entrypoint、healthcheck、secrets、configs、shm_size、stop_grace_period），並澄清了 ports 語法。
