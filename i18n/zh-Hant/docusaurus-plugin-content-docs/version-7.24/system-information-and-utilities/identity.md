---
sidebar_key: "system-information-and-utilities/identity"
sidebar_position: 6
title: "身份"
sidebar_label: "身份"
description: "本頁介紹在 MikroTik RouterOS 中配置 System Identity，該功能為網路通訊以及 DHCP 等服務設定唯一識別符號。它說明了如何透過 CLI 或 SNMP 設定標識，並警告存在 64 個字元的限制。"
tags:
  - 'system-identity'
  - 'snmp'
  - 'configuration'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/identity
captured_at: '2026-11-04T11:33:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

設定系統身份會提供一個唯一的標識名稱，用於系統在網路中向其他路由器標識自身，以及在訪問 DHCP、Neighbour Discovery 和預設無線 SSID 等服務時使用。預設系統身份設定為 'MikroTik'。

:::warning
系統身份的最大字元長度為 64
:::

## 配置 {#configuration}

要在 RouterOS 中設定系統身份：

```ros
[admin@MikroTik] > /system/identity/set name=New_Identity 
[admin@New_Identity] >
```

當前系統身份始終顯示在已登入賬戶名之後，並可透過 print 命令顯示：

```ros
[admin@New_Identity] /system/identity>print
name: New_Identity
[admin@New_Identity] /system/identity>

```

### SNMP {#snmp}

也可以透過 SNMP set 命令更改路由器系統身份：

```ros
snmpset -c public -v 1 192.168.0.0 1.3.6.1.2.1.1.5.0 s New_Identity
```

*snmpset* - 基於 Linux 的 SNMP 應用程式，用於透過 SNMP SET 請求設定網路實體上的資訊；

- *public* - 路由器的團體名；
- *192.168.0.0* - 路由器的 IP 地址；
- *1.3.6.1.2.1.1.5.0* - 路由器身份的 SNMP 值；
