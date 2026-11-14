---
sidebar_key: "getting-started/manual-network-setup"
sidebar_position: 2
title: "手動網路設定（無預設配置）"
sidebar_label: "手動網路設定"
description: "如何手動設定沒有預設配置的 MikroTik 路由器：重設為乾淨狀態、建立 bridge、分配 LAN IP 地址，並使用 CLI 或 WinBox/WebFig 配置 DHCP 伺服器。"
tags:
  - 'dhcp'
source: https://manual.mikrotik.com/docs/7.25/getting-started/manual-network-setup
captured_at: '2026-11-04T11:17:03+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

大多數 MikroTik 路由器都自帶[預設配置](./configuration-management/default-configurations.md)，其中已經提供了網橋、LAN IP 地址、DHCP 伺服器和基礎防火牆。如果你保留預設配置，可以跳過本頁。

僅當你的裝置**沒有預設配置**，或者你已將其重設為乾淨狀態時，才需要按照以下步驟操作。

## 從乾淨配置開始 {#start-from-a-clean-configuration}

1. 將網線連線到路由器的 **ether1** 埠。
2. 將你的計算機連線到任意其他 **乙太網** 埠。
3. 開啟 WinBox，使用鄰居發現（Neighbor Discovery）定位路由器。詳細說明請參閱 [WinBox 文章](../management-tools/winbox.md)。
4. 選擇路由器的 MAC 地址並點選 **Connect**。

要從完全乾淨的配置開始，請執行以下命令：

```ros
/system/reset-configuration no-defaults=yes skip-backup=yes
```

路由器將重啟，且不包含任何預設設定、防火牆規則或已配置的服務。

或者在 WinBox 中操作：

![](/img/36c689cf791cbd73.png)

## 建立網橋並分配 IP 地址 {#create-a-bridge-and-assign-an-ip-address}

由於 MAC 連線有時可能不可靠，第一步是啟用 IP 連通性。這涉及三個主要任務：

- 建立網橋介面並分配網橋埠
- 為網橋介面分配 IP 地址
- 配置 DHCP 伺服器

<Tabs>
<TabItem value="cli" label="CLI" default>

建立網橋介面，將所需的乙太網埠新增為網橋埠，併為網橋分配 IP 地址：

```ros
/interface/bridge/add name=bridge1
/interface/bridge/port/add interface=ether2 bridge=bridge1
/ip/address/add address=192.168.88.1/24 interface=bridge1
```

</TabItem>
<TabItem value="winbox" label="WinBox / WebFig">

1. 開啟 **Bridge** 視窗，確保選中 **Bridge** 標籤頁。
   - 點選 <kbd>**New**</kbd> 或 <kbd>**+**</kbd> 按鈕以開啟新對話方塊。你可以輸入自定義網橋名稱，或保留預設的 **bridge1**，然後點選 <kbd>**OK**</kbd> 繼續。

     ![](/img/5e212f2237271f88.png)
2. 切換到 **Ports** 標籤頁，點選 <kbd>**New**</kbd> 或 <kbd>**+**</kbd> 按鈕以開啟另一個對話方塊。
   - 選擇 **ether2** 作為介面、**bridge1** 作為網橋，然後點選 <kbd>**OK**</kbd>。對於要新增到網橋的每個額外埠，重複此步驟。

     ![](/img/a838eb33fc38a49c.png)
   - 你可以關閉網橋對話方塊。
3. 進入 **IP** 選單並導航到 **Address** 對話方塊。
   - 點選 <kbd>**New**</kbd> 或 <kbd>**+**</kbd> 按鈕以開啟新對話方塊。
   - 輸入 IP 地址 **`192.168.88.1/24`**，並從下拉列表中選擇介面 **bridge1**。

     ![](/img/895805f4eba17159.png)
   - 點選 <kbd>**OK**</kbd> 確認設定。

</TabItem>
</Tabs>

## 設定 DHCP 伺服器 {#set-up-a-dhcp-server}

<Tabs>
<TabItem value="cli" label="CLI" default>

為了簡化和加快此過程，請執行設定命令。大多數配置選項會自動確定，因此你只需按 <kbd>Enter</kbd> 接受每個值：

```ros
[admin@MikroTik] > ip dhcp-server/ setup [enter]
Select interface to run DHCP server on 

dhcp server interface: bridge1 [enter]
Select network for DHCP addresses 

dhcp address space: 192.168.88.0/24 [enter]
Select gateway for given network 

gateway for dhcp network: 192.168.88.1 [enter]
Select pool of ip addresses given out by DHCP server 

addresses to give out: 192.168.88.2-192.168.88.254 [enter]
Select DNS servers 

dns servers: 192.168.88.1 [enter]               
Select lease time 

lease time: 1800 [enter]
```

</TabItem>
<TabItem value="winbox" label="WinBox / WebFig">

DHCP Server Setup 嚮導也可在 [WinBox](../management-tools/winbox.md) 和 [WebFig](../management-tools/webfig.md) 中使用：

- 導航到 **IP → DHCP Server** 視窗，確保選中 **DHCP** 標籤頁。
- 點選 <kbd>**DHCP Setup**</kbd> 按鈕以開啟新對話方塊。

  ![](/img/bc007e09d5e538fa.png)

- 選擇 **bridge1** 作為 **DHCP Server Interface**，然後點選 <kbd>**Next**</kbd>。
- 按照嚮導完成設定。

</TabItem>
</Tabs>

按照這些步驟操作後，已連線的 PC 應能自動獲取動態 IP 地址。然後你可以關閉 WinBox，並使用 IP 地址 **`192.168.88.1`** 重新連線到路由器。

當 IP 連通性正常後，請繼續閱讀[配置網際網路連線](./first-time-configuration.md#configuring-the-internet-connection-wan)以及首次配置指南的其餘部分。
