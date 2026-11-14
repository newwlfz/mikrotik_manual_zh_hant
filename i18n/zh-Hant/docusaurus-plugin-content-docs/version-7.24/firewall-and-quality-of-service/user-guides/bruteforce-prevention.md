---
sidebar_key: "firewall-and-quality-of-service/user-guides/bruteforce-prevention"
sidebar_position: 1
title: "暴力破解防護"
sidebar_label: "暴力破解防護"
description: "本頁說明如何在 MikroTik RouterOS 上配置暴力破解防護：透過防火牆過濾器在多次失敗嘗試後阻止 SSH 登入嘗試，併為每個嘗試級別設定不同的超時時間，最後為合法使用者放行。"
tags:
  - 'ssh'
  - 'bruteforce-prevention'
  - 'security'
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/user-guides/bruteforce-prevention
captured_at: '2026-11-04T11:28:22+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

這個示例演示如何防護針對 SSH 埠的暴力破解攻擊。請注意，SSH 每個連線允許 3 次登入嘗試，並且地址列表在成功登入後不會被清除。這意味著如果你觸發了防護規則，可能會誤將自己加入黑名單。

```
/ip/firewall/filter/add action=add-src-to-address-list address-list=bruteforce_blacklist address-list-timeout=1d chain=input comment="Blacklist" connection-state=new dst-port=22 protocol=tcp src-address-list=connection3

/ip/firewall/filter/add action=add-src-to-address-list address-list=connection3 address-list-timeout=1h chain=input comment="Third attempt" connection-state=new dst-port=22 protocol=tcp src-address-list=connection2

/ip/firewall/filter/add action=add-src-to-address-list address-list=connection2 address-list-timeout=15m chain=input comment="Second attempt" connection-state=new dst-port=22 protocol=tcp src-address-list=connection1

/ip/firewall/filter/add action=add-src-to-address-list address-list=connection1 address-list-timeout=5m chain=input comment="First attempt" connection-state=new dst-port=22 protocol=tcp

/ip/firewall/filter/add action=accept chain=input dst-port=22 protocol=tcp src-address-list=!bruteforce_blacklist
```

如果三個連線列表都使用 1 分鐘的超時時間，攻擊者每分鐘可以進行 9 次猜測。而採用上述結構，每 5 分鐘最多隻能進行 3 次猜測。

:::warning
地址列表的命名遵循 Port knocking 文章中使用的約定。類似的命名方案也用於將受信任的地址列表命名為 "secured"。
:::
