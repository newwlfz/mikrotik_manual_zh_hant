---
sidebar_key: "hardware/ports"
sidebar_position: 8
title: "埠"
sidebar_label: "埠"
description: "本頁介紹 MikroTik RouterOS 埠配置選項，涵蓋用於初始設定的序列埠和 USB 埠、3G 調變解調器連線、透過 RFC 2217 進行遠端訪問，以及波特率、流控和停止位等詳細的埠屬性。"
tags:
  - 'serial-port'
  - 'baud-rate'
  - 'remote-access'
source: https://manual.mikrotik.com/docs/7.24/hardware/ports
captured_at: '2026-11-04T11:29:26+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

路由器為其埠提供了多種使用選項。最常見的用途是序列埠，安裝後用於初始 RouterOS 配置。預設情況下，serial0 由序列終端使用。

序列埠和 USB 埠還可用於：

- 連線 3G 調變解調器。
- 透過序列埠線連線到另一臺裝置。
- 遠端訪問透過序列埠線連線的裝置。

## 常規 {#general}

**子選單：** `/port`

此選單顯示路由器上所有可用的序列埠和 USB 埠，並允許配置埠引數，例如 baud-rate、flow-control 及其他設定。

以下示例顯示 LtAP 裝置上的預設埠配置：

```ros
[admin@LtAP] > /port/print                 
Columns: DEVICE, NAME, CHANNELS, USED-BY, BAUD-RATE
# DEVICE  NAME     CHANNELS  USED-BY                                     BAUD-RATE
0         serial0         1  Serial Console(#0)                          auto     
1         gps             1  GPS(#0)                                     115200   
```

:::warning
埠列表由 RouterOS 自動維護。

:::

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **baud-rate** (*integer \| auto*; 預設值：**auto**) | 埠使用的波特率（速度）。如果設定為 **auto**，RouterOS 會嘗試自動檢測波特率。 |
| **data-bits** (*7 \| 8*; 預設值：) | 每個字元中的資料位數。7 - 真 ASCII；8 - 任意資料（與一個位元組的大小相匹配） |
| **dtr** (*on \| off*; 預設值：) | 是否啟用流控使用的 RS-232 DTR 訊號電路。 |
| **flow-control** (*hardware \| none \| xon-xoff*; 預設值：) | 用於暫停和恢復資料傳輸的流控方法。 |
| **name** (*string*; 預設值：) | 埠名稱。 |
| **parity** (*even \| none \| odd*; 預設值：) | 錯誤檢測方法。如果啟用，會發送一個額外位來檢測通訊錯誤。大多數情況下，parity 設定為 **none**，錯誤由通訊協定處理。 |
| **rts** (*on \| off*; 預設值：) | 是否啟用流控使用的 RS-232 RTS 訊號電路。 |
| **stop-bits** (*1 \| 2*; 預設值：) | 每個字元後傳送的停止位。電子裝置通常使用 1 個停止位。 |

### 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **channels** (*integer*) | 埠支援的通道數。 |
| **inactive** (*yes \| no*) | 顯示當前埠狀態，**inactive=yes** - 埠之前連線到的裝置，但當前不存在 |
| **line-state** () |  |
| **used-by** (*string*) | 顯示當前誰在使用埠和通道（#）。例如，預設情況下 **Serial0** 由 serial-console 使用。 |

## 遠端訪問 {#remote-access}

**子選單：** `/port/remote-access`

遠端訪問功能允許您連線到透過 COM 埠通訊且位於路由器後方的序列裝置。使用 RFC 2217，RouterOS 可以透過 TCP 連線與序列裝置之間傳輸資料。

在 RouterOS 上啟用遠端訪問很簡單：

```ros
/port/remote-access/add port=serial0 protocol=rfc2217 tcp-port=9999
```

:::warning
預設情況下，serial0 由序列終端使用。必須先釋放該埠，才能將其用於 remote-access 或其他服務。

:::

## 屬性 {#properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **allowed-addresses** (*IP address range*; 預設值：**0.0.0.0/0**) | 允許遠端訪問埠的 IP 地址範圍。 |
| **channel** (*integer [0..4294967295]*; 預設值：**0**) | 將使用的埠通道。如果埠只有一個通道，則通道號應始終為 **0**。 |
| **disabled** (*yes \| no*; 預設值：**no**) |  |
| **local-address** (*IP address*; 預設值：) | 用作源地址的 IP 地址。 |
| **log-file** (*string*; 預設值：**""**) | 用於記錄通訊日誌的檔名。預設情況下停用日誌記錄。 |
| **port** (*string*; 預設值：) | 埠列表中的埠名稱。 |
| **protocol** (*raw \| rfc2217*; 預設值：**rfc2217**) | RFC 2217 定義了透過 TCP 與序列裝置之間傳輸資料的協定。如果設定為 **raw**，則資料按原樣傳送到序列埠。 |
| **tcp-port** (*integer [0..65535]*; 預設值：**0**) | 用於監聽傳入連線的 TCP 埠。 |

## 只讀屬性 {#read-only-properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **active** (*yes \| no*) | 遠端訪問是否處於活動狀態並準備好接受連線。 |
| **busy** (*yes \| no*) | 埠當前是否忙碌。 |
| **inactive** (*yes \| no*) |  |
| **logging-active** (*yes \| no*) | 當前是否正在記錄到檔案 |
| **remote-address** (*IP address*) | 當前連線的遠端位置的 IP 地址。 |
