---
sidebar_key: "wireless/w60g/fail-over-ptp-gui-example"
sidebar_position: 4
title: "故障轉移 PtP GUI 示例"
sidebar_label: "故障轉移 PtP GUI 示例"
description: "本指南演示如何使用 MikroTik RouterOS GUI 在 60GHz 無線網橋與繫結 5GHz 介面之間配置自動故障切換，包括網橋設定、無線模式選擇以及用於實現無縫冗餘的安全配置檔案建立。"
tags:
  - 'bonding'
  - 'wireless'
  - 'winbox'
source: https://manual.mikrotik.com/docs/7.25/wireless/w60g/fail-over-ptp-gui-example
captured_at: '2026-11-04T11:24:31+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 概述 {#summary}

本示例展示如何在 GUI 中配置與 60Ghz 裝置結合使用的自動故障轉移（bonding）5Ghz 鏈路。  
當 60Ghz 無線連線丟失時，它將自動使用 bonding 介面。  
本示例在空配置狀態下使用 [[WinBox](https://mikrotik.com/download)] 實用工具完成。

### 連線到裝置 {#connect-to-the-device}

配置重設後，只能使用 mac-telnet。在 WinBox 主介面中點選 Neighbours，選擇裝置的 MAC 地址，然後點選 Connect：

1. 選擇正確的裝置 **MAC 地址**。
2. 預設登入名為 “**admin**”，未設定密碼。
3. 點選 **Connect**。

![](/img/fa8bab19f7283e15.webp)

### 配置 bridge {#configure-bridge}

新增新 bridge：

1. 開啟 Bridge 子選單；
2. 點選 “+” 新增新的 bridge；
3. 應用更改。

![](/img/c99185067ee63bea.webp)

*後續說明中需要為其分配 bridge 成員。這將允許流量從 Ethernet 傳遞到 W60G 介面而無需路由。*

### 設定 60GHz 無線連線 {#set-up-60ghz-wireless-connection}

之前說明的所有步驟對於 **bridge** 和 **station** 裝置都是相同的。配置無線介面時需要使用不同的模式。

按如下方式配置 **bridge** 裝置：

1. 開啟 Interface 選單；
2. 雙擊 wlan60-1 介面；
3. 點選 Wireless 子選單並將模式設定為 **bridge**（對於 PtmP，使用 **ap-bridge**）；
4. 設定 SSID、密碼和區域；
5. 在 “Put Stations In Bridge” 下選擇之前建立的 bridge；
6. 應用更改；
7. 點選 Enable 開始傳輸。

![](/img/d697b1afd1973489.webp)

按如下方式配置 **station** 裝置：

1. 開啟 Interface 選單；
2. 雙擊 wlan60-1 介面；
3. 點選 Wireless 子選單並將模式設定為 **station bridge**；
4. 設定 SSID 和密碼；
5. 應用更改；
6. 點選 enable 開始傳輸。

![](/img/b95c7f99cf4ba6e1.webp)

### 設定 5GHz 無線連線 {#set-up-5ghz-wireless-connection}

#### 為裝置選擇 Security Profile {#choose-security-profile-for-your-devices}

1. 選擇 **Wireless** 選單；
2. 選擇 **Security Profiles** 子選單；
3. 使用 “**+**” 符號新增新配置檔案；
4. 選擇 **名稱**、**模式**、**身份驗證型別** 和安全密碼；
5. **Apply** 配置。

**![](/img/152343ce0e0acf7d.webp)**

#### 對於網橋裝置 {#for-bridge-device}

1. 開啟 **Interfaces** 選單；
2. 雙擊 **wlan1** 介面；
3. 點選 **Wireless** 子選單並將模式設定為 **bridge**（對於 PtmP，使用 **ap-bridge**）；
4. 設定 **SSID**、**密碼** 和 **國家/地區**；
5. 點選 **Advanced Mode**；

![](/img/b548cbf46135d6c8.webp)

1. 選擇您的 **Security Profile**；
2. **Apply** 更改；
3. 點選 **enable** 開始傳輸。

![](/img/111658df04501ba6.webp)

#### 對於站點裝置 {#for-station-device}

1. 開啟 **Interfaces** 選單；
2. 雙擊 **wlan1** 介面；
3. 開啟 **Wireless** 子選單並將模式設定為 **station-bridge**；
4. 設定 **SSID**、**密碼** 和 **國家/地區**；
5. 開啟 **advanced** 模式（與 bridge 裝置類似\*）；
6. 選擇 **Security Profile**；
7. **Apply** 更改；
8. 點選 **enable** 開始傳輸。

![](/img/ccd706458bd9b7df.webp)

*如果一切操作正確，應出現 running (R) 標誌，如截圖所示：*  
![](/img/6c356acee6743a8a.webp)

### 配置 bonding {#configure-bonding}

*配置 bonding 並分配從介面；在本設定中，選擇內建 wlan1 介面，但在其他型別的設定中，它也可以是 ether 介面。*

#### 對於網橋裝置 {#for-bridge-device-1}

1. 點選 **Bonding** 子選單；
2. 使用 “**+**” 新增新成員；
3. 將介面成員（**wlan1** 和 **wlan60-station-1**）作為 **Slaves** 新增到 **bonding** 介面；
4. 將介面成員 **wlan60-station-1** 新增為 **Primary** 介面；
5. 將 Mode 選擇為 **active backup**；
6. **Apply** 配置。

![](/img/5dcc3469009f324b.webp)

#### 對於站點裝置 {#for-station-device-1}

1. 點選 **Bonding** 子選單；
2. 使用 “**+**” 新增新成員；
3. 將介面成員（**wlan1** 和 **wlan60-1**）作為 **Slaves** 新增到 **bonding** 介面；
4. 將介面成員 **wlan60-1** 新增為 **Primary** 介面；
5. 將 Mode 選擇為 **active backup**；
6. **Apply** 配置。

![](/img/d305d625521b39c0.webp)

### 配置 bridge {#configure-bridge-1}

*配置 bridge 設定（包括 bonding 介面）對於 active-backup 在所用裝置上生效是必需的（在本例中，bridge 和 station 裝置的設定相同）：*

1. 點選 **Bridge** 子選單；
2. 使用 “**+**” 新增新成員；
3. 將介面成員新增為 **ether1**，將 Bridge 成員新增為 **bridge1**；
4. **Apply** 配置；

*![](/img/e4b242fa377fc206.webp)*

1. 點選 **Bridge** 子選單；
2. 使用 “**+**” 新增新成員；
3. 將介面成員新增為 **bonding1**，將 Bridge 成員新增為 **bridge1**；
4. **Apply** 配置。

*![](/img/3efb230842ca5e1b.webp)*

### 其他配置 {#additional-configuration}

介面從灰色狀態啟用後，將變為活動狀態。

完成之前說明的所有步驟後，應建立鏈路。建議在兩臺裝置上設定管理員密碼。
