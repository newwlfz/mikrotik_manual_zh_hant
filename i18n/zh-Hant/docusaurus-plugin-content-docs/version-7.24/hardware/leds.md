---
sidebar_key: "hardware/leds"
sidebar_position: 4
title: "LED 指示燈"
sidebar_label: "LED 指示燈"
description: "RouterOS 允許在受支援的裝置上自定義 LED 行為，用於無線訊號強度、介面流量活動和其他狀態指示。使用者可以為特定功能配置單個 LED，例如無線訊號強度、乙太網活動或調變解調器訊號，並會收到有關硬體限制的警告。"
tags:
  - 'leds'
  - 'system-configuration'
source: https://manual.mikrotik.com/docs/7.24/hardware/leds
captured_at: '2026-11-04T11:29:24+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

**子選單：** `/system/leds`

RouterOS 允許按照使用者希望的方式配置每個 LED 的活動狀態。可以將 LED 配置為顯示無線訊號強度、在介面流量活動時使 LED 閃爍，以及許多其他選項。

例如，Groove 上的預設 LED 配置

```ros
[admin@MikroTik] /system/leds> print 
Flags: X - disabled 
# TYPE INTERFACE LEDS 
0 wireless-signal-strength led1 
led2 
led3 
led4 
led5 
1 interface-activity ether1 user-led 

```

:::warning
並非所有板卡都具備支援此功能所需的硬體能力。

:::

:::warning
RB Groove 使用五個 LED 顯示無線訊號強度，並使用一個 LED 監控乙太網活動。

:::

## 屬性說明 {#property-description}

| 屬性 | 描述 |
| :-- | :-- |
| **disabled** (*yes \| no*; 預設：**no**) | 專案是否被停用 |
| **interface** (*string*；預設值：) | 用於 LED 狀態的介面名稱。僅在 **type** 為介面相關型別時適用。 |
| **modem-signal-treshold** (*integer [-113..-51]*；預設值：) | 當型別為 **modem-signal** 時適用 |
| **leds** (*list of leds*；預設值：) | 用於狀態報告的 LED 名稱列表。例如，無線訊號強度需要不止一個 LED。 |
| **type** (*align-down \| align-left \| align-right \| align-up \| ap-cap \| fan-fault \| flash-access \| interface-activity \| interface-receive \| interface-speed \| interface-speed-1G \| interface-speed-25G \| interface-speed-100G \| interface-status \| interface-transmit \| modem-signal \| modem-technology \| off \| on \| poe-fault \| poe-out \| wireless-signal-strength \| wireless-status*；預設值：) | 狀態型別：align-down - 如果 w60g 裝置需要向下對準以獲得最佳訊號質量，則點亮 LED；align-left - 如果 w60g 裝置需要向左對準，則點亮 LED；align-right - 如果 w60g 裝置需要向右對準，則點亮 LED；align-up - 如果 w60g 裝置需要向上對準，則點亮 LED；ap-cap - 在 CAP 透過 CAPsMAN 初始化時閃爍，連線後常亮；fan-fault - 當裝置控制的任一風扇停止工作時點亮 LED；flash-access - 在快閃記憶體訪問時使 LED 閃爍；interface-activity - 在介面（流量）活動時使 LED 閃爍；interface-receive - 在介面接收流量時使 LED 閃爍；interface-speed - 當介面以 10Gbit 速率工作時點亮 LED；interface-speed-1G - 當介面以 1Gbit 速率工作時點亮 LED；interface-speed-25G - 當介面以 25Gbit 速率工作時點亮 LED；interface-speed-100G - 當介面以 100Gbit 速率工作時點亮 LED；interface-status - 在介面狀態變化時點亮 LED；interface-transmit - 在介面傳送流量時使 LED 閃爍；modem-signal - 根據 3G 調變解調器訊號（USB 或 miniPCIe）使 LED 閃爍；modem-technology - 按照調變解調器技術代際順序點亮 LED：GSM；3G；LTE；僅當 LTE 處於活動狀態時，單個 LED 才會點亮；off - 關閉 LED；on - 點亮 LED；poe-fault - 當 PoE 輸出預算接近支援的最大限制時點亮 LED；poe-out - 當介面 PoE 輸出開啟時點亮 LED；wireless-signal-strength - 點亮用於顯示無線訊號的 LED（需要不止一個 LED）；wireless-status - 在無線狀態變化時點亮 LED。 |

## LED 設定 {#led-settings}

全域性設定儲存在 LED 設定選單中。

**子選單：** `/system/leds/setting`

| 屬性 | 說明 |
| :-- | :-- |
| **all-leds-off** (*after-1h \| after-1min \| immediate \| never*；預設值：**never**) | 路由器的所有 LED 是否可以以及何時可以關閉 |

列出的裝置支援關閉其 LED（LED 暗色模式）；但是，由於裝置設計因素，某些 LED 仍無法關閉。

### **室內裝置** {#indoor-devices}

| RouterBoard | LED 說明 |
| :-- | :-- |
| **CRS305-1G-4S+; CRS309-1G-8S+** | 關閉所有 LED，但乙太網 LED 和電源 LED 除外 |
| **RB5009UG+S+IN; RB5009UPr+S+** | 關閉所有 LED |
| **L009UiGS-RM; L009UiGS-2HaxD-IN** | 關閉 PWR、USR 和 Ether1 LED |
| **L41G-2axD; L41G-2axD&FG621-EA (hAP ax lite 系列)** | 關閉所有 LED，但乙太網 LED 除外 |
| **RB760iGS (hEX S)** | 關閉電源 LED 和 SFP LED |
| **E50UG** | 關閉所有 LED，但 Ethernet1 LED 除外 |
| **RB924i-2nD-BT5&BG77; RB924iR-2nD-BT5&BG77 (KNOT 系列)** | 關閉所有 LED |
| **RB951Ui-2HnD** | 關閉所有 LED，但電源 LED 除外 |
| **RB951Ui-2nD (hAP); RB952Ui-5ac2nD (hAP ac lite); RB952Ui-5ac2nD-TC (hAP ac lite TC)** | 關閉所有 LED，但電源 LED 除外 |
| **RB962UiGS-5HacT2HnT (hAP ac)** | 關閉所有 LED，但 Port5 PoE LED 除外 |
| **RBcAP2n; RBcAP2nD (cAP)** | 關閉所有 LED |
| **RBcAPGi-5acD2nD (cAP ac); RBcAPGi-5acD2nD-XL (cAP XL ac)** | 關閉所有 LED |
| **cAPGi-5HaxD2HaxD (cAP ax)** | 關閉所有 LED，但乙太網 LED 除外 |
| **RBD25G/RB25GR-5HPacQD2HPnD (Audience)** | 關閉所有 LED，但乙太網 LED 除外 |
| **RBD52G-5HacD2HnD-TC (hAP ac^2)** | 關閉所有 LED |
| **RBD53iG-5HacD2HnD (hAP ac^3)** | 關閉所有 LED |
| **RBD53G-5HacD2HnD-TC (Chateau 系列)** | 關閉所有 LED |
| **RBwsAP5Hac2nD (wsAP ac lite)** | 關閉所有 LED |
| **C52iG-5HaxD2HaxD-TC (hAP ax^2)** | 關閉所有 LED，但乙太網 LED 除外 |
| **C53UiG+5HPaxD2HPaxD (hAP ax^3)** | 關閉所有 LED，但乙太網 LED 除外 |
| **S53UG+5HaxD2HaxD-TC (Chateau ax 系列)** | 關閉所有 LED，但乙太網 LED 除外 |

### **無線系統** {#wireless-systems}

| RouterBoard | LED 說明 |
| :-- | :-- |
| **CME22-2n-BG77 (CME Gateway)** | 關閉所有 LED |
| **CubeG-5ac60ay (Cube 60Pro ac); CubeG-5ac60ay-SA (CubeSA 60Pro ac)** | 關閉所有 LED |
| **CubeG-5ac60ad (Cube 60G ac)** | 關閉所有 LED |
| **RB912R-2nD-LTm (ltAP mini / ltAP mini LTE kit)** | 關閉所有 LED |
| **RB912UAG-6HPnD (BaseBox 6)** | 關閉所有 LED |
| **RBD23UGS-5HPacD2HnD (NetMetal ac^2)** | 關閉所有 LED |
| **L11UG-5HaxD; L11UG-5HaxD-NB (NetBox 5 ax)** | 關閉所有 LED |
| **L22UGS-5HaxD2HaxD-15S (mANTBox ax 15s)** | 關閉所有 LED |
| **L23UGSR-5HaxD2HaxD; L23UGSR-5HaxD2HaxD-NM (NetMetal ax)** | 關閉所有 LED |
| **RBLDF-2nD (LDF 2); RBLDF-5nD (LDF 5); RBLHGR** | 關閉所有 LED |
| **RBLDFG-5acD (LDF 5 ac)** | 關閉所有 LED，但乙太網 LED 除外 |
| **RBLHG2nD (LHG 2); RBLHG2nD-XL (LHG XL 2)** | 關閉所有 LED |
| **RBLHG5nD (LHG 5); RBLHG5HPnD (LHG HP5); RBLHG5HPnD-XL (LHG XL HP5)** | 關閉所有 LED |
| **RBLHGG-5acD (LHG 5 ac); RBLHGG-5acD-XL (LHG XL 5 ac); RBLHGG-5HPacD2HPnD (LHG XL 52 ac); RBSXTsqG-5acD (SXTsq 5 ac)** | 關閉所有 LED，但乙太網 LED 除外 |
| **RBLHGG-60ad (Wireless Wire Dish)** | 關閉所有 LED |
| **LHGGM&EG18-EA (LHG LTE18 kit); ATLGM&EG18-EA (ATL LTE18 kit)** | 關閉所有 LED |
| **RBLtAP-2HnD (LtAP)** | 關閉所有 LED，但乙太網 LED 除外 |
| **RBSXTsq-60ad (SXTsq Lite60); RBCube-60ad (Cube Lite60)** | 關閉所有 LED |
| **RBwAPG-60ad (Wireless Wire)** | 關閉所有 LED |
| **RBwAPGR-5HacD2HnD (wAP ac)** | 關閉所有 LED，但乙太網 LED 除外 |

## 示例 {#examples}

### 基本示例 {#basic-example}

用於指令碼編寫的 LED 控制 CLI 命令：

```ros
#将具有特定类型 "on" 或 "off" 的 led 条目添加到 leds 菜单
/system/leds/add leds=led1 type=off
#用于控制 led
/system/leds/set [find where leds="led1"] type=on
or
/system/leds/set [find where leds="led1"] type=off

```

在 RB951 上啟用 User ACT LED 以顯示當前 CAP 狀態

```ros
/system/leds
add leds=user-led type=ap-cap
```

### Modem 訊號強度示例 {#modem-signal-strength-example}

modem-signal 訊號強度的整個範圍為 [-113..-51]，而 modem-signal-threshold 將最弱訊號限制提高到 -91，因此用於 LED 指示的訊號範圍為 [-91..-51]。該範圍會根據為 modem-signal LED 觸發器配置的 LED 數量等分。當訊號高於 -91 時第一個 LED 點亮，當訊號達到 -51 時最後一個 LED 點亮。

```ros
/system/leds
add interface=lte1 leds=led1,led2,led3,led4,led5 modem-signal-treshold=-91 type=modem-signal

```

### Modem 接入技術示例 {#modem-access-technology-example}

這些 LED 觸發器示例按照調變解調器技術代際順序點亮 LED：GSM；3G；LTE。

- 1 個 LED：當 LTE 處於活動狀態時，led1 點亮。

```ros
/system/leds/add interface=lte1 leds=led1 type=modem-technology
```

- 2 個 LED：led1 - 3G；led2 - LTE；

```ros
/system/leds
add interface=lte1 leds=led1,led2 type=modem-technology

```

- 3 個 LED：led1 - GSM；led2 - 3G；led3 - LTE

```ros
/system/leds/add interface=lte1 leds=led1,led2,led3 type=modem-technology
```
