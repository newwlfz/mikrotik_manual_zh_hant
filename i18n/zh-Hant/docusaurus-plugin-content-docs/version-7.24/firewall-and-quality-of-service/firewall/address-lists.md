---
sidebar_key: "firewall-and-quality-of-service/firewall/address-lists"
sidebar_position: 1
title: "地址列表"
sidebar_label: "地址列表"
description: "本頁面介紹如何在 MikroTik RouterOS 中為防火牆規則建立和管理地址列表，包括新增靜態條目以及基於連線嘗試生成的動態條目，並透過超時來控制流量阻斷的持續時間。"
tags:
  - 'address-lists'
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/firewall/address-lists
captured_at: '2026-11-04T11:28:07+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

以下示例建立一個動態地址列表，其中包含正在連線路由器 23 埠（telnet）的主機，並在 5 分鐘內丟棄來自它們的全部後續流量。此外，該地址列表還將包含一條 192.0.34.166/32（[www.example.com](http://www.example.com)）的靜態地址列表條目：

```ros
/ip/firewall/address-list/add list=drop_traffic address=192.0.34.166/32
```

```ros
/ip/firewall/address-list/print
Flags: X - disabled, D - dynamic
 #   LIST         ADDRESS
 0   drop_traffic 192.0.34.166
```

```ros
/ip/firewall/mangle/add action=add-src-to-address-list address-list=drop_traffic address-list-timeout=5m chain=prerouting dst-port=23 protocol=tcp
/ip/firewall/filter/add action=drop chain=input src-address-list=drop_traffic
```

```ros
/ip/firewall/address-list/print
Flags: X - disabled, D - dynamic
 #   LIST         ADDRESS
 0   drop_traffic 192.0.34.166
 1 D drop_traffic 1.1.1.1
 2 D drop_traffic 10.5.11.8
```

從最後一條 print 命令的輸出可以看出，地址列表中出現了兩個新的動態條目（狀態標記為 'D'）。具有這些 IP 地址的主機嘗試與路由器建立 telnet 會話，隨後被過濾規則丟棄。
