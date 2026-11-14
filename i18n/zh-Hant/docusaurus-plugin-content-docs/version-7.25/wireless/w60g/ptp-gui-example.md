---
sidebar_key: "wireless/w60g/ptp-gui-example"
sidebar_position: 6
title: "點對點圖形介面示例"
sidebar_label: "點對點圖形介面示例"
description: "本指南演示如何使用 WinBox 在兩臺 MikroTik W60G 裝置之間配置透明無線橋接，內容涵蓋介面設定、建立網橋、為 bridge 和 station 兩種角色配置無線模式，以及額外的安全建議。"
tags:
  - 'bridging'
  - 'wireless'
  - 'winbox'
source: https://manual.mikrotik.com/docs/7.25/wireless/w60g/ptp-gui-example
captured_at: '2026-11-04T11:24:24+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 概述 {#summary}

本示例展示如何在 GUI 中配置從一臺 W60G 裝置到另一臺 W60G 裝置的透明無線橋接。

示例是在空配置狀態下使用 [[WinBox](https://mikrotik.com/download)] 實用程式完成的

### 連線到裝置 {#connect-to-the-device}

配置重設後，只能使用 mac-telnet。在 WinBox 主介面中點選 Neighbours，選擇裝置的 MAC 地址，然後點選 Connect：

![](/img/35b82e384ea98fed.webp)

### 配置 bridge {#configure-bridge}

新增一個新網橋併為其分配網橋成員。這樣無需路由即可將流量從乙太網傳遞到 W60G 介面：

1. 開啟 Bridge 子選單；
2. 點選 “+” 新增新的 bridge；
3. 應用更改。

![](/img/c99185067ee63bea.webp)

將介面成員（ether1 和 wlan60-1）新增到新建的網橋：

1. 點選 Ports 子選單；
2. 使用“+”新增新成員；
3. 選擇正確的介面；
4. 應用設定。

![](/img/d0275e2820cf50b4.webp)

![](/img/2d6695312a5e1d14.webp)

### 設定無線連線 {#set-up-wireless-connection}

之前說明的所有步驟對於 **bridge** 和 **station** 裝置都是相同的。配置無線介面時需要使用不同的模式。

按如下方式配置 **bridge** 裝置：

1. 開啟 Interface 選單；
2. 雙擊 wlan60-1 介面；
3. 點選 Wireless 子選單並將模式設定為 **bridge**；
4. 設定 SSID、密碼和區域；
5. 在“Put Stations In Bridge”下選擇之前建立的網橋；
6. 應用更改；
7. 點選 enable 開始傳輸。

![](/img/7d465133495ed1ce.webp)

按如下方式配置 **station** 裝置：

1. 開啟 Interface 選單；
2. 雙擊 wlan60-1 介面；
3. 點選 Wireless 子選單並將模式設定為 **station bridge**；
4. 設定 SSID 和密碼；
5. 應用更改；
6. 點選 enable 開始傳輸。

![](/img/a09cd3c87e452fe7.webp)

### 其他配置 {#additional-configuration}

介面從灰色狀態啟用後，將變為活動狀態。

完成前面說明的所有步驟後，鏈路應已建立。建議在兩臺裝置上設定管理員密碼。

要建立點對多點設定：在 bridge 裝置上必須設定 ap-bridge，在 station 裝置上必須設定 station-bridge。
