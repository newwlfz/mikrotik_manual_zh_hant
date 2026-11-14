---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/detect-internet"
sidebar_position: 17
title: "檢測網際網路"
sidebar_label: "檢測網際網路"
description: "Detect Internet 是一款 RouterOS 工具，可將受監控的介面歸類為 Internet、WAN、LAN 和 unknown 等狀態，並會針對 DHCP 用戶端安裝以及基於鏈路狀態和雲可達性的狀態轉換髮出警告。"
tags:
  - 'detnet'
  - 'detect-internet'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/detect-internet
captured_at: '2026-11-04T11:27:56+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Detect Internet 是一個工具，會將受監控的介面歸類為以下狀態 - **Internet**、**WAN**、**LAN**、**unknown**、**slave** 和 **no-link**。

:::warning
注意，Detect Internet 可以安裝 DHCP 用戶端、預設路由、DNS 伺服器並影響其他功能。
請謹慎使用，並且在啟用該服務後，檢查它如何幹擾你的其他配置。
:::

### 狀態 {#state}

此子選單顯示由 *detect-interface-list* 引數定義的所有受監控介面的狀態：

```ros
/interface/detect-internet/state/print
```

### LAN {#lan}

所有二層介面最初都具有此狀態。

### 廣域網路 {#wan}

任何 L3 隧道和 LTE 介面最初都將具有此狀態。二層介面在滿足以下條件時可以獲取此狀態：

- 介面在主路由表中具有到 8.8.8.8 的活動路由。
- 介面可以獲取（建立動態 DHCP 用戶端）或已從 DHCP 獲取地址（如果 DHCP 伺服器也在 DHCP 伺服器介面上執行 Detect Internet，則不適用）。

:::warning
WAN 介面僅在鏈路狀態變化時才能回退到 LAN 狀態。LAN 介面在 1h 後會鎖定為 LAN，之後僅在鏈路狀態變化時才會改變。
:::

### 網際網路 {#internet}

能夠使用 UDP 協定埠 30000 訪問 cloud.mikrotik.com 的 *WAN* 介面可以獲取此狀態。每 2 分鐘檢查一次可達性。預設情況下，如果 4 分鐘內無法訪問雲，狀態會回退到 **WAN**。

## 配置 {#configuration}

**子選單：** `/interface/detect-internet`

| 屬性 | 描述 |
| :-- | :-- |
| **detect-interface-list** (*interface list*; 預設：**none**) | 列表中的所有介面都將由 Detect Internet 監控 |
| **internet-interface-list** (*interface list*; 預設：**none**) | 狀態為 Internet 的介面將動態新增到此列表 |
| **lan-interface-list** (*interface list*; 預設：**none**) | 狀態為 Lan 的介面將動態新增到此列表 |
| **wan-interface-list** (*interface list*; 預設：**none**) | 狀態為 Wan 的介面將動態新增到此列表 |
| **request-interval**(time; 預設：**2m**) | 介面狀態檢查之間的時間間隔 |

```ros
[admin@MikroTik] > /interface/detect-internet/print 
detect-interface-list: none
lan-interface-list: none
wan-interface-list: none
internet-interface-list: none
[admin@MikroTik] > /interface/detect-internet/set internet-interface-list=all wan-interface-list=all lan-interface-list=all detect-interface-list=all 
[admin@MikroTik] > /interface/detect-internet/state/print 
Columns: NAME, STATE, STATE-CHANGE-TIME, CLOUD-RTT
# NAME STATE STATE-CHANGE-TIME CLO
0 ether1 internet 2020-12-22 13:46:18 5ms
```
