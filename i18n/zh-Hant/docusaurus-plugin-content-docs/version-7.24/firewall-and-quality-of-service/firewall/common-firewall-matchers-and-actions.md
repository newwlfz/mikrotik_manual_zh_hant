---
sidebar_key: "firewall-and-quality-of-service/firewall/common-firewall-matchers-and-actions"
sidebar_position: 2
title: "常用防火牆匹配器和動作"
sidebar_label: "常用防火牆匹配器和動作"
description: "本頁介紹 MikroTik RouterOS 防火牆統計資訊與命令，詳細說明如何檢視 IPv4/IPv6 規則的匹配統計、重設計數器，並列出防火牆過濾中常用的匹配項，如 MAC 地址、介面、IP 範圍和埠。"
tags:
  - 'firewall'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/firewall/common-firewall-matchers-and-actions
captured_at: '2026-11-04T11:28:08+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 統計 {#stats}

要按防火牆規則檢視匹配統計資訊，請執行 `/ip/firewall/filter/print stats` 命令；對於 IPv6 防火牆，請執行 `/ipv6/firewall/filter/print stats`。

| 屬性 | 描述 |
| :-- | :-- |
| **bytes** (*integer*) | 該規則匹配的 bytes 總量 |
| **packets** (*integer*) | 該規則匹配的 packets 總量 |

```text
[admin@MikroTik] > ip firewall filter print stats
Flags: X - disabled, I - invalid, D - dynamic
 #    CHAIN                                                                                                                 ACTION                            BYTES         PACKETS
 0  D ;;; special dummy rule to show fasttrack counters
      forward                                                                                                               passthrough              50 507 925 242      50 048 246
 1    ;;; defconf: drop invalid
      forward                                                                                                               drop                            432 270           9 719
 2    ;;; defconf: drop invalid
      input                                                                                                                 drop                            125 943           2 434
 3    input                                                                                                                 accept                   20 090 211 549      20 009 864
 4    ;;; defconf: accept ICMP
      input                                                                                                                 accept                          634 926           7 648
 5    ;;; defconf: drop all not coming from LAN
      input                                                                                                                 drop                          4 288 079          83 428
  6    ;;; defconf: accept in ipsec policy
       forward                                                                                                               accept                                0               0
  7    ;;; defconf: accept out ipsec policy
       forward                                                                                                               accept                                0               0
  8    ;;; defconf: fasttrack
       forward                                                                                                               fasttrack-connection     28 505 528 775      31 504 682
  9    ;;; defconf: accept established,related, untracked
       forward                                                                                                               accept                   28 505 528 775      31 504 682
 10    ;;; defconf: drop all from WAN not DSTNATed
      forward                                                                                                               drop                                  0               0
```

統計引數可透過以下命令重設：

| 命令 | 描述 |
| :-- | :-- |
| **reset-counters** (*id*) | 重設特定防火牆規則或規則列表的統計計數器。 |
| **reset-counters-all** | 重設表中所有防火牆規則的統計計數器。 |

## 其他有用命令 {#other-useful-commands}

預設情況下，print 等同於 `print static`，並且僅顯示靜態規則。

要同時列印動態規則，請使用 `print all`。

或者僅列印動態規則，請使用 `print dynamic`。

## 匹配器 {#matchers}

匹配器按特定順序執行。

### 對於 IPv4 {#for-ipv4}

- 源 MAC 地址
- 入/出介面
- 入/出介面列表
- IP 範圍
- 地址型別
- 地址列表
- TTL
- DSCP
- 長度
- TLS
- IPv4 選項
- 目的埠
- 源埠
- 任意埠
- TCP 選項
- TCP MSS
- ICMP 程式碼
- 入站優先順序
- 優先順序
- 封包標記
- Realm（路由表）
- Hotspot
- 連線標記
- 連線狀態
- 連線 NAT 狀態
- 連線位元組數
- 連線限制
- 連線速率
- Ipsec 策略
- Helper
- 字串（內容）
- PSD
- Layer7
- 隨機
- Nth
- PCC
- 限制
- 目的限制
- 日誌

### 對於 IPv6 {#for-ipv6}

- 地址型別
- 地址列表
- 源 MAC 地址
- 入/出介面
- 入/出介面列表
- 跳數限制
- DSCP
- 長度
- TLS
- IPv6 報頭
- 目的埠
- 源埠
- 任意埠
- TCP 選項
- TCP MSS
- ICMPv6 程式碼
- 入站優先順序
- 優先順序
- 封包標記
- 連線標記
- 連線狀態
- 連線 NAT 狀態
- 連線位元組數
- 連線限制
- 連線速率
- Ipsec 策略
- Helper
- 匹配字串（內容）
- 隨機
- Nth
- PCC
- 限制
- 目的限制
- 日誌
