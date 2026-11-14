---
sidebar_key: "system-information-and-utilities/wake-on-lan"
sidebar_position: 18
title: "網路喚醒"
sidebar_label: "網路喚醒"
description: "區域網路喚醒 (WoL) 可透過向遠端裝置的 MAC 地址傳送 UDP Magic Packet 來為遠端裝置開機，這需要正確的介面和硬體配置。"
tags:
  - 'wol'
  - 'ip-broadcast'
  - 'mac'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/wake-on-lan
captured_at: '2026-11-04T11:33:40+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

[*Wake on LAN CLI 參考*](../cli-reference/tool/wol.md)

**子選單：** `/tool/wol`

Wake on LAN（WoL）是一種網路功能，它會向廣播地址傳送 UDP Magic Packet。此封包包含目標裝置的 MAC 地址。如果目標裝置支援 Wake on LAN（即具備所需的硬體和軟體配置），它就會從睡眠或關機狀態啟動。不支援安全 WoL。

## Wake-on-LAN 命令 {#wake-on-lan-command}

`/tool/wol` 命令需要一個 MAC 地址引數和一個介面才能正常工作。

:::warning
如果未指定介面，Magic Packet 會從預設閘道器介面作為 IP 廣播發送。
:::

```ros
/tool/wol mac=FE:4B:71:05:EA:8B interface=ether1
```

以下示例展示了 [WinBox](../management-tools/winbox.md) 中的 Wake on LAN 工具。

![Wake on LAN tool in WinBox](/img/c63eb8e43babeb3a.webp)
