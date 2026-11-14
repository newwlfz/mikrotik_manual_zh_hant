---
sidebar_key: "getting-started/first-time-configuration"
sidebar_position: 1
title: "首次配置"
sidebar_label: "首次配置"
description: "本頁提供首次配置 MikroTik RouterOS 的分步指南，涵蓋前提條件、連線設定以及 DHCP、NAT 和防火牆等關鍵概念。它包含面向新使用者和高階使用者的 WinBox 圖形介面與 CLI 方法。"
tags:
  - 'dhcp'
  - 'firewall'
source: https://manual.mikrotik.com/docs/7.25/getting-started/first-time-configuration
captured_at: '2026-11-04T11:16:39+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 開始之前 {#before-you-begin}

### 前提條件 {#prerequisites}

在開始配置過程之前，請確保您具備以下條件：

- 一臺 MikroTik 路由器
- 一臺帶乙太網埠的計算機（推薦）。如果路由器提供無線接入點，也支援透過 WiFi 進行配置
- 一根乙太網線
- 來自您的 ISP 的有效網際網路連線
- 30–60 分鐘不受打擾的時間

### 關鍵概念 {#key-concepts}

- **預設配置：** 出廠預裝設定，可能需要根據您的網路需求進行調整
- **網橋：** 一種虛擬介面，可將多個物理埠組合成單個網段
- **DHCP：** 一種自動為網路中的裝置分配 IP 地址的協定
- **NAT：** 網路地址轉換，允許多臺裝置共享單個公共 IP 地址
- **防火牆：** 一組用於控制並過濾網路流量以保障安全的規則

### 選擇您的配置方法 {#choose-your-configuration-method}

本指南介紹如何使用以下任一方式配置 RouterOS：

- 使用 [WinBox](../management-tools/winbox.md) 或 [WebFig](../management-tools/webfig.md) 的圖形介面
- 命令列介面（CLI）

如何選擇：

- **新使用者：** 建議按照 WinBox 說明進行操作
- **高階使用者：** 可以使用程式碼塊中顯示的 CLI 命令

:::tip
After completing each major configuration section, it is recommended to create a backup of your settings. → 完成每個主要配置部分後，建議對您的設定建立備份。

**CLI 方法：**

```
/export file=backup-step3
```

**WinBox 方法：**

1. 開啟 **Files** 選單
2. 點選 **Backup**
3. 輸入一個描述性名稱（例如：`after-internet-setup`）

如果出現問題，你可以在 **Files** 選單中選中備份並點選 **Restore** 來恢復配置。
:::

## 訪問路由器 {#accessing-the-router}

大多數 MikroTik 路由器出廠時自帶預設配置，可立即訪問。但是，一些專業裝置（例如 CCR 系列）可能出廠時配置極少或沒有預設配置。在這種情況下，請先手動設定網路——請參閱 [手動網路設定](./manual-network-setup.md)。

### 步驟 1：物理連線 {#step-1-physical-connection}

1. 將乙太網線從您的計算機連線到路由器的任意乙太網埠，**但 ether1 除外**。
2. 將 ISP 線纜連線到 **ether1**（通常用作 WAN 介面）。
3. 開啟路由器電源，等待大約一分鐘使其完全啟動。

```
Internet ─── [ISP] ─── [ether1] MikroTik Router [ether2-ether5] ─── [Switch / Devices]

                                                 │

                                          [WiFi Clients]
```

### 步驟 2：下載 WinBox {#step-2-download-winbox}

如果您還沒有 WinBox：

為您的作業系統 **[下載 WinBox](https://mt.lv/winbox)**：

可用軟體包：

- **Windows：** ZIP 壓縮包（包含 `WinBox.exe`）
- **Linux：** ZIP 壓縮包（包含一個二進位制可執行檔案）
- **macOS：** DMG 包

1. 解壓或開啟下載的軟體包。
2. 啟動 WinBox：
   - Windows：執行 `WinBox.exe`
   - Linux：使該二進位制檔案可執行並執行它
   - macOS：開啟 `.dmg` 並啟動 WinBox

無需安裝。更多詳細資訊，請參閱 [WinBox 手冊](../management-tools/winbox.md)。

### 步驟 3：使用鄰居發現查詢您的路由器 {#step-3-find-your-router-using-neighbor-discovery}

1. 開啟 WinBox。
2. 在 **Select from** 下拉選單中，選擇 **Neighbors**。
3. 您的路由器應會出現在 **Neighbors** 列表中。
4. 雙擊路由器條目以進行連線：
   - 如果 IP 地址不可達或顯示為 `0.0.0.0`，請優先使用 **MAC 地址**。
5. 出現提示時，輸入登入憑據：
   - **使用者名稱：** `admin`
   - **密碼：** 留空，或使用裝置標籤上列印的密碼（如適用）

### 步驟 4：保護路由器 {#step-4-protecting-the-router}

路由器可訪問後，請保護它免遭未經授權的訪問和基本攻擊。請先完成以下操作：

1. **設定管理員密碼。** 空密碼會允許對路由器進行不受限制的訪問。
2. **確認防火牆已啟用。** 大多數 MikroTik 裝置出廠時帶有預設防火牆配置，可阻止最常見的外部攻擊。不要停用現有規則；僅在需要時新增新規則。
3. **停用來自網際網路的直接管理訪問。** 這在沒有預設防火牆的裝置上尤為重要。如果需要遠端訪問，請使用 **WireGuard** 或 **IPsec** 等安全方法，而不要直接暴露管理埠。

### 使用者密碼管理 {#user-password-management}

使用強密碼保護您的 MikroTik 路由器至關重要。請使用符合以下條件的密碼：

- 至少 12 個字元長
- 包含大寫和小寫字母、數字和符號
- 避免詞典單詞或簡單模式

使用 CLI 設定管理員密碼：

```ros
/user set 0 password="Your_Super_Strong_Password_123!@#$%^&*"
```

或以互動方式更改：

```ros
[admin@MikroTik] > /password 
old-password: ********
new-password: ****************************
confirm-new-password: ****************************
```

:::danger
請記住您的密碼。如果丟失，將沒有恢復選項。您將需要重設路由器或重新安裝 RouterOS。
:::

您還可以在 `/user` 選單中管理使用者：

```ros
/user/add name=myname password=mypassword group=full
/user/remove admin
```

:::tip
最佳實踐是建立一個使用強密碼的新管理員使用者，驗證其可以正常工作，然後停用或刪除預設的 **admin** 賬戶。
:::

## 瞭解預設配置 {#understanding-default-configuration}

首次連線到 MikroTik 路由器時，您可能會看到有關[預設配置](./configuration-management/default-configurations.md)的提示。以下是您需要了解的內容：

- **對於初學者：** 建議保留預設配置，因為它提供了基本安全性和必要功能。
- **預設設定包括：** 基本防火牆、DHCP 伺服器以及預設無線安全設定（如適用）。
- **您可以安全地自定義它**，並將預設結構作為基礎保留。

![Default configuration prompt](/img/37a911aa919894e3.png)

:::danger
移除預設配置會移除所有內建安全規則和服務。僅建議計劃手動配置路由器的高階使用者這樣做。
:::

如果您的裝置**沒有預設配置**，或者您將其重設為乾淨狀態，則必須手動設定網橋、LAN IP 地址和 DHCP 伺服器——繼續之前請參閱 **[手動網路設定](./manual-network-setup.md)**。

## 配置網際網路連線（WAN） {#configuring-the-internet-connection-wan}

要讓路由器接入網際網路，您需要知道您的 ISP 使用哪種連線型別。請向您的 ISP 確認，或參考以下說明：

- **DHCP / 動態 IP** — 大多數電纜調變解調器和部分光纖連線。插上後即可自動獲得網際網路連線。
- **靜態 IP** — 企業連線或部分住宅光纖。您的 ISP 為您提供了特定的 IP 地址、閘道器和 DNS 伺服器。
- **PPPoE** — DSL 連線或部分光纖提供商。您的 ISP 為您提供了用於連線的使用者名稱和密碼。

:::tip
**不確定？** 從 DHCP 開始——它適用於約 80% 的家庭連線。
:::

### DHCP / 動態 IP（最常見） {#dhcp--dynamic-ip-most-common}

這是家庭使用者最簡單、最常見的設定。在公共介面上配置 DHCP 用戶端，以自動從您的 ISP 獲取 IP 地址、DNS 伺服器、NTP 伺服器和預設路由。

```ros
/ip/dhcp-client/add disabled=no interface=ether1
```

新增用戶端後，驗證分配的地址，並確認狀態顯示為 "bound"：

```ros
[admin@MikroTik] > ip dhcp-client print
Columns: INTERFACE, USE-PEER-DNS, ADD-DEFAULT-ROUTE, STATUS, ADDRESS
# INTERFACE  USE-PEER-DNS  ADD-DEFAULT-ROUTE  STATUS  ADDRESS        
0 ether1     yes           yes                bound   1.2.3.100/24
```

### 靜態 IP {#static-ip}

如果您的 ISP 提供了永不變的特定網路設定，請使用此方式。您的 ISP 會提供三個引數：

- IP 地址：**`1.2.3.100/24`**
- 閘道器：**`1.2.3.1`**
- DNS 伺服器：**`8.8.8.8`**

將 IP 地址新增到 WAN 介面，使用閘道器建立預設路由，並設定 DNS 伺服器：

```ros
/ip/address/add address=1.2.3.100/24 interface=ether1
/ip/route/add gateway=1.2.3.1
/ip/dns/set servers=8.8.8.8
```

### PPPoE {#pppoe}

如果您的 ISP 提供了登入憑據（DSL 提供商常見），請使用此方式。PPPoE 提供動態 IP 地址，並可自動配置 DNS 伺服器和預設路由。

<Tabs>
<TabItem value="cli" label="CLI" default>

```ros
/interface/pppoe-client
add disabled=no interface=ether1 user=me password=123 \
  add-default-route=yes use-peer-dns=yes
```

</TabItem>
<TabItem value="winbox" label="WinBox / WebFig">

1. 開啟 **PPP** 視窗，然後轉到 **Interface** 標籤頁。
2. 點選 <kbd>**New**</kbd> 或 <kbd>**+**</kbd> 按鈕以新增新介面。
3. 從下拉列表中選擇 **PPPoE Client**。
4. 輸入連線名稱，並選擇 **ether1** 作為介面。

   ![](/img/edf9954b4e4acb7b.png)
5. 轉到 **Dial Out** 標籤頁，輸入您的 ISP 提供的使用者名稱和密碼。
6. 根據您的 ISP 要求配置任何附加引數。
7. 點選 <kbd>**OK**</kbd> 儲存設定。

   ![](/img/b58b7f7c04d8c45d.png)

</TabItem>
</Tabs>

:::warning
配置後，WAN 介面將變為 **pppoe-out1**，而不是 **ether1**。請將所有後續與 WAN 相關的配置都使用此介面。
:::

## 驗證網際網路連線 {#verify-internet-connectivity}

配置 WAN 連線後，請確認路由器本身可以訪問網際網路。首先透過 ping 一個已知的公共 IP 地址來測試 IP 連通性——Google 的公共 DNS 伺服器 `8.8.8.8`：

```ros
[admin@MikroTik] > /ping 8.8.8.8
  SEQ HOST                                     SIZE TTL TIME       STATUS             
    0 8.8.8.8                                    56  55 14ms399us 
    1 8.8.8.8                                    56  55 18ms534us 
    2 8.8.8.8                                    56  55 14ms384us 
```

然後透過 ping 一個域名來驗證 DNS 解析是否正常工作：

```ros
[admin@MikroTik] > /ping google.com
  SEQ HOST                                     SIZE TTL TIME       STATUS             
    0 142.250.74.14                              56  55 14ms475us 
    1 142.250.74.14                              56  55 14ms308us 
    2 142.250.74.14                              56  55 14ms238us
```

如果 IP ping 成功但域名 ping 失敗，則連線正常，但 DNS 配置不正確。如果兩者都成功，則路由器自身的網際網路連線完全正常。如果任一失敗，請參閱[故障排除](#troubleshooting)部分。

路由器後面的本地裝置仍需要有效的 NAT 規則才能訪問網際網路——請參閱下一節。

## NAT 配置 {#nat-configuration}

:::note
如果您保留了**預設配置**，則 WAN 介面上已經設定了源 NAT（masquerade）規則，因此本地裝置已經可以訪問網際網路——您可以跳過本節。以下步驟僅適用於您的路由器**沒有預設配置**或您正在構建自定義設定的情況。
:::

要讓本地裝置訪問網際網路，路由器必須將其出站封包的私有源地址轉換為其自己的公共 IP 地址。私有地址無法在網際網路上路由，因此如果沒有此轉換，遠端主機將無法回覆您的本地裝置。這透過 WAN 介面上的源 NAT（masquerade）規則完成：

```ros
/ip/firewall/nat
add chain=srcnat out-interface=ether1 action=masquerade
```

:::danger
如果公共介面是 PPPoE、LTE 或任何其他型別，則應將 'out-interface' 設定為該介面。
:::

或者，可以使用介面列表進行更靈活的配置。

首先，建立一個名為 WAN 的介面列表，並將所有外部介面新增到其中：

```ros
/interface list add name=WAN
/interface list member add list=WAN interface=ether1
```

然後在 NAT 規則中使用該介面列表：

```ros
/ip/firewall/nat
add chain=srcnat out-interface-list=WAN ipsec-policy=out,none action=masquerade
```

此設定的另一個好處是，路由器後面的用戶端預設無法從網際網路直接訪問，這有助於保護它們免受未經請求的入站流量影響。

### 埠轉發 {#port-forwarding}

某些用戶端裝置可能需要從網際網路透過特定埠直接訪問。例如，IP 地址為 192.168.88.254 的用戶端裝置必須可透過遠端桌面協定（RDP）訪問。

快速搜尋後可以發現，RDP 執行在 TCP 埠 3389 上。現在您可以新增目標 NAT 規則，將 RDP 流量重定向到用戶端 PC。

```ros
/ip/firewall/nat/add chain=dstnat action=dst-nat protocol=tcp dst-port=3389 to-addresses=192.168.88.254 to-ports=3389
```

:::tip
如果您設定了嚴格的防火牆規則，則必須在防火牆過濾器的 forward 鏈中允許 RDP 協定。
:::

## 設定無線 / WiFi {#setting-up-wireless--wifi}

無線配置方式取決於您的 RouterOS 代次和驅動程式：

- **現代 WiFi**（`/interface wifi`）— 帶有新 WiFi 協定棧的 RouterOS v7 裝置。
- **傳統無線**（`/interface wireless`）— RouterOS v6 和較舊的 v7 軟體包。

本指南展示一個基本的安全接入點（SSID + WPA2/WPA3 密碼）。有關高階主題——Wi-Fi 6/7、MLD / 多鏈路、多射頻、CAPsMAN、中繼器以及針對不同裝置系列的指導——請參閱[無線](../wireless/index.md)部分。

:::note
以下示例假設：country = `Latvia`，SSID = `MikroTik-12345`，在支援的地方啟用 WPA2/WPA3，停用 WPS。
:::

<Tabs>
<TabItem value="wifi" label="Modern WiFi (/interface wifi)" default>

建立安全配置檔案：

```ros
/interface wifi security
add name=myProfile authentication-types=wpa2-psk,wpa3-psk \
  passphrase="YOUR_STRONG_PASSWORD"
```

配置射頻：

```ros
/interface wifi
set [ find default-name=wifi1 ] configuration.country=Latvia \
  .mode=ap .ssid="MikroTik-12345" .hide-ssid=no \
  channel.width=20mhz disabled=no \
  security=myProfile security.wps=disable

set [ find default-name=wifi2 ] configuration.country=Latvia \
  .mode=ap .ssid="MikroTik-12345" .hide-ssid=no \
  channel.width=20mhz disabled=no \
  security=myProfile security.wps=disable
```

![](/img/1cb7c0cf6e4760c3.png)

</TabItem>
<TabItem value="legacy" label="Legacy Wireless (/interface wireless)">

建立安全配置檔案：

```ros
/interface/wireless/security-profiles
add name="myProfile" authentication-types=wpa2-psk mode=dynamic-keys \
wpa2-pre-shared-key="YOUR_STRONG_PASSWORD"
```

配置射頻：

```ros
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=20/40mhz-Ce distance=indoors \
  mode=ap-bridge ssid=MikroTik-12345 wireless-protocol=802.11 \
  security-profile=myProfile frequency-mode=regulatory-domain \
  country=latvia antenna-gain=3

set [ find default-name=wlan2 ] band=5ghz-a/n/ac channel-width=20/40mhz-Ce distance=indoors \
  mode=ap-bridge ssid=MikroTik-12345 wireless-protocol=802.11 \
  security-profile=myProfile frequency-mode=regulatory-domain \
  country=latvia antenna-gain=3
```

<video controls width="600">
  <source src="/videos/wireless-setup_video.mp4" type="video/mp4" />
</video>

</TabItem>
</Tabs>

### 將無線介面新增到網橋 {#add-the-wireless-interface-to-the-bridge}

每個應提供 LAN 訪問的無線介面都必須新增到網橋。如果沒有新增，即使 WiFi 連線成功，無線用戶端也無法接收 DHCP 地址、訪問 LAN 裝置或訪問網際網路。

:::note
如果您保留了**預設配置**，無線介面通常已經在網橋中，因此可以跳過此步驟。此步驟主要適用於手動設定，其中網橋建立為 `bridge1`。
:::

```ros
/interface bridge port
add interface=wifi1 bridge=bridge1
add interface=wifi2 bridge=bridge1
```

對於傳統無線，請改用 `wlanN` 介面名稱（例如 `wlan1`、`wlan2`）。

## 配置完成 {#configuration-complete}

此時，路由器應：

- 為本地裝置提供網際網路訪問
- 使用 DHCP 自動分配 IP 地址
- 保護裝置免受來自網際網路的未經請求的訪問
- 提供無線連線（如適用）

現在您可以繼續學習更高階的主題，例如 VPN、VLAN、路由、監控和網路管理。

## 下一步：保護您的路由器 {#next-secure-your-router}

您的路由器現已上線。在將其投入生產環境之前，請加強防護以防止未經授權的訪問：設定強密碼和唯一使用者名稱，保留預設防火牆規則，限制管理服務，並停用任何您不使用的功能。

有關完整的安全加固檢查清單，請參閱 **[保護您的路由器](./securing-your-router.md)**，其中包括公共介面的防火牆規則、MAC 訪問和鄰居發現限制、服務埠加固以及 SSH 強加密。

## 故障排除 {#troubleshooting}

RouterOS 具有各種內建故障排除工具，例如 ping、traceroute、torch、封包嗅探器、頻寬測試等。

我們在本文中已經使用了 ping 工具來[驗證網際網路連線](#verify-internet-connectivity)。

### ping 失敗時的故障排除 {#troubleshoot-if-ping-fails}

ping 工具的問題在於，它只顯示目標**不可達**，但沒有更詳細的資訊可用。讓我們回顧一下基本錯誤。

您無法從連線到 MikroTik 裝置的計算機訪問 [www.google.com](https://www.google.com)：

![](/img/b7cb6bca84393134.jpg)

:::tip
如果您不確定如何準確配置閘道器裝置，請聯絡 MikroTik 官方[顧問](https://mikrotik.com/consultants)獲取配置支援。
:::
