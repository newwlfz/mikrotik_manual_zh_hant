---
sidebar_key: "firewall-and-quality-of-service/kid-control"
sidebar_position: 5
title: "兒童上網管控"
sidebar_label: "兒童上網管控"
description: "Kid Control 是 RouterOS 的一項功能，它透過配置檔案和防火牆規則為 LAN 裝置設定每日網際網路訪問時間表、頻寬限制以及針對特定裝置的限制，從而實現對 LAN 裝置的家長控制。"
tags:
  - 'kid-control'
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/kid-control
captured_at: '2026-11-04T11:28:13+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/ip/kid-control`

"Kid control" 是一項家長控制功能，用於限制 LAN 裝置的網際網路連線。

## 屬性說明 {#property-description}

在此選單中，可以為每個孩子建立配置檔案，並限制其網際網路訪問。

| 屬性 | 說明 |
| :-- | :-- |
| **name** (*string*) | 孩子的配置檔名稱 |
| **mon,tue,wed,thu,fri,sat,sun** (*time*) | 一週中的每一天。允許網際網路訪問的時間段 |
| **disabled** (*yes \| no*) | 配置檔案是否被停用 |
| **rate-limit** (*string*) | 流的最大可用資料速率 |
| **tur-mon,tur-tue,tur-wed,tur-thu,tur-fri,tur-sat,tur-sun** (*time*) | 不限速時間。網際網路訪問不受限制的時間段 |

不限速引數比 rate-limit 引數具有更高的優先順序。

## 裝置 {#devices}

**子選單：** `/ip/kid-control/device`

此子選單包含有關已連線到網際網路的多個裝置（手機、平板電腦、遊戲主機、電視等）的資訊。裝置透過從 ARP 表中獲取的 MAC 地址來識別。相應的 IP 地址也從那裡獲取。

| 屬性 | 說明 |
| :-- | :-- |
| **name** (*string*) | 裝置的名稱 |
| **mac-address** (*string*) | 裝置的 MAC 地址 |
| **user** (*string*) | 要將裝置加入的配置檔案 |
| **reset-counters** (*[id, name]*) | 重設 bytes-up 和 bytes-down 計數器。 |

## 應用示例 {#application-example}

在以下示例中，我們將限制 Peter 的手機的訪問：

- 在週一、週三和週五停用網際網路訪問
- 在以下時間允許不限量的網際網路訪問：
  - 週二
  - 週四 11:00-22:00
  - 週日 15:00-21:00
- 在週六 18:30-22:00 將 Peter 的手機的頻寬限制為 3Mbps

```ros
[admin@MikroTik] > /ip/kid-control/add name=Peter mon="" tur-tue="00:00-24h" wed="" tur-thu="11:00-22:00" fri="" sat="18:30-22:00" tur-sun="15h-21h" rate-limit=3M
[admin@MikroTik] > /ip/kid-control/device/add name=Mobile-phone user=Peter mac-address=FF:FF:FF:ED:83:63
```

網際網路訪問限制是透過新增動態防火牆過濾規則或簡單佇列規則實現的。以下是防火牆過濾規則的示例：

```ros
[admin@MikroTik] > /ip/firewall/filter/print

1  D ;;; Mobile-phone, kid-control
      chain=forward action=reject src-address=192.168.88.254 

2  D ;;; Mobile-phone, kid-control
      chain=forward action=reject dst-address=192.168.88.254
```

動態建立的簡單佇列：

```ros
[admin@MikroTik] > /queue/simple/print
Flags: X - disabled, I - invalid, D - dynamic 

 1  D ;;; Mobile-phone, kid-control
      name="queue1" target=192.168.88.254/32 parent=none packet-marks="" priority=8/8 queue=default-small/default-small limit-at=3M/3M max-limit=3M/3M burst-limit=0/0 
      burst-threshold=0/0 burst-time=0s/0s bucket-size=0.1/0.1  
```

可以監控特定裝置使用了多少資料：

```ros
[admin@MikroTik] > /ip/kid-control/device/print stats

Flags: X - disabled, D - dynamic, B - blocked, L - limited, I - inactive 
 #    NAME                                                                                                                 IDLE-TIME    RATE-DOWN   RATE-UP   BYTES-DOWN     BYTES-UP
 1 BI Mobile-phone                                                                                                               30s         0bps      0bps    3438.1KiB       8.9KiB
```

也可以為已建立的孩子**暫停**網際網路訪問；這將限制所有訪問，直到使用 **恢復**，之後將繼續按配置的設定執行：

```ros
[admin@MikroTik] > /ip/kid-control/pause Peter 
[admin@MikroTik] > /ip/kid-control/print
Flags: X - disabled, P - paused, B - blocked, L - rate-limited 
 #   NAME                                                                                                                    SUN      MON      TUE      WED      THU      FRI      SAT     
 0 PB Peter                                                                                                                 15h-21h                             11h-22h          18:30h-22h  
```
