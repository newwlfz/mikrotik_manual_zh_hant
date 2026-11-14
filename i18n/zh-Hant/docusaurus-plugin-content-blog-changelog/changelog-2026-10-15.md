---
title: "文件更新 - 2026 年 10 月 15 日"
date: 2026-10-15
slug: /changelog-2026-10-15
source: https://manual.mikrotik.com/changelog/changelog-2026-10-15
captured_at: '2026-11-04T06:09:03+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026年10月15日文件變更摘要。

## 系統 {#system}

- **[SNMP](/docs/diagnostics-monitoring-and-troubleshooting/snmp)**：全面重寫，已在 hAP ax² 板卡上的 RouterOS 7.26beta1 中測試。改造為面向任務的指南：為採集器啟用 SNMP、限制 community、SNMPv3 安全（MD5/SHA1/SHA256/SHA384/SHA512、DES/AES、密碼最少 8 個字元）、如何用 `print oid` 查詢任意 OID、接收 trap（trap 版本、`trap-interfaces` 的語義、`send-trap`）以及 SNMP 寫入（identity、執行指令碼、重啟），另外還包括檢查與故障排查章節以及技術細節（engine ID 與 `engine-id-suffix` 的區別、回覆源地址、MIB 集合）。所有示例和輸出均為最新抓取結果；按 community 配置的 `denied-oids` 黑名單現已寫入文件。圖片帶有替代文字，舊的錯誤說法已被刪除（“指令碼值不能為 0”規則、關於地址與 `trap-interfaces` 的錯誤表述）。

## CLI 參考 {#cli-reference}

- **[/snmp](/docs/cli-reference/snmp)**、**[/snmp/community](/docs/cli-reference/snmp/community)**、**[/snmp/send-trap](/docs/cli-reference/snmp/send-trap)**：選單介紹和所有引數說明均已補全（27 行），包括 `engine-id-suffix`、`denied-oids`、SHA-2 認證協定以及 trap 生成器選項。
- **[/tool/snmp-get](/docs/cli-reference/tool/snmp-get)**、**[/tool/snmp-walk](/docs/cli-reference/tool/snmp-walk)**：所有引數說明均已補全（此前為空），包括 `port`、`next`（GETNEXT）以及 SNMPv3 引數。
