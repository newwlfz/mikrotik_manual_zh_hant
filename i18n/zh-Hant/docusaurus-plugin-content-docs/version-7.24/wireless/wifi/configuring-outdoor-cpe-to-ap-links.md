---
sidebar_key: "wireless/wifi/configuring-outdoor-cpe-to-ap-links"
sidebar_position: 2
title: "配置室外 CPE 到 AP 鏈路"
sidebar_label: "配置室外 CPE 到 AP 鏈路"
description: "使用 MikroTik RouterOS 的 `wifi-qcom` 軟體包配置室外 CPE 到 AP Wi-Fi 鏈路的指南，涵蓋頻率選擇、國家法規、AP 模式設定、安全性以及長距離連線的距離考量。"
tags:
  - 'wifi'
  - 'ap-configuration'
source: https://manual.mikrotik.com/docs/7.24/wireless/wifi/configuring-outdoor-cpe-to-ap-links
captured_at: '2026-11-04T11:36:02+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**軟體包：** `wifi-qcom`

眾所周知，室內接入點的 Wi-Fi 覆蓋範圍是有限的。它主要受當地法規影響，這些法規會限制裝置的輸出功率（具體取決於使用哪個頻率通道）。典型的室內 Wi-Fi 連線建立在 AP（接入點）與用戶端（station）裝置（智慧手機、筆記型電腦等）之間。

室內 AP 通常配備全向天線（可將訊號以“甜甜圈”形狀廣播到 AP 周圍），其天線增益相對較低。對於室內和短距離室外安裝，這是非常合適的天線。使用帶有全向天線的簡單家用 AP，在“理想”的無干擾視距環境中，你可以達到最遠約 ±100 米的距離；而在建築物內部，這一距離會大幅縮短。

但是！如果你提高 AP 的天線增益，並將訊號以更小的角度“定向”到特定目的地（而不是以 360° 廣播訊號），就可以實現距離長得多的連線（前提是 station 裝置位於定向角度內）。這正是室外遠距離 AP 和 CPE 的用武之地。它們允許建立跨越數公里距離的 Wi-Fi 連線。

遠距離連線需要一臺執行在“AP”模式的裝置，以及一臺執行在“station”模式的用戶端裝置。多個 station 可以連線到單個 AP。

:::info
本指南適用於執行 `wifi-qcom` 軟體包/驅動程式的 802.11 AX 裝置。
:::

## AP 設定 {#ap-setup}

### 頻率選擇 {#frequency-selection}

如引言所述，當地主管部門會監管 Wi-Fi 裝置的輸出功率。不同國家/地區的不同頻率範圍可能具有不同的允許功率。你可以使用以下命令檢查適用於你所在國家配置檔案的限制：

```ros
/interface/wifi/radio/reg-info country=Latvia 0           
  ranges: 2402-2482/20dBm/40MHz            
          5170-5250/23dBm/160MHz/indoor    
          5250-5330/23dBm/160MHz/indoor/dfs
          5490-5730/30dBm/160MHz/dfs       
          5735-5875/14dBm/80MHz 
```

根據該表，我們可以看到（使用“Latvia”國家配置檔案時）在通道 `5490-5730` 上可獲得的最大功率為 `30 dBm`。

此表中顯示的“dBm”表示“允許的 EIRP”（EIRP=發射功率 + 天線增益）。為了不違反任何法規和“法律”，裝置的天線增益越高，設定的發射功率就越低（如果裝置具有內建天線，這將**自動**發生），以匹配允許的“EIRP”值。

另請注意，最高“EIRP”的通道可能是“DFS”通道（意味著如果在該通道上檢測到雷達，廣播就會停止）。這一點需要牢記！

根據這些資訊和該表，我們可以看到明智的做法是避免使用 `5735-5875` 範圍，因為它只允許 `14 dBm`。

通道上允許的“EIRP”越高 = 可用輸出功率越大 = 訊號越強 = 可獲得的距離越遠。

:::note
請注意，有一個名為“Superchannel”的國家配置檔案。在此配置檔案中，沒有對輸出功率應用軟體限制。此模式只應在受控環境中使用，或者如果你所在地區有特殊許可可以使用它。你可以將其與直接在設定中“降低”發射功率值相結合，以獲得“自定義”功率輸出。
:::

此外，從頻率方面來說，請記住通道寬度越小，干擾越少，可獲得的距離越遠。也就是說，對於更長距離，請使用 20 MHz。

### WiFi 介面配置 {#wifi-interface-configuration}

要配置 AP 模式，請執行以下命令：

```ros
/interface/wifi
set [ find default-name=wifi1 ] channel.frequency=5500 configuration.country=Latvia .mode=ap .ssid=input_your_SSID_here security.authentication-types=wpa2-psk .passphrase=input_your_password_here channel.width=20mhz
```

- `channel.frequency` → 選擇執行 AP 的頻率通道。如果你想使用“自動”通道選擇，可以跳過此項。
- `configuration.country` → 應用國家配置檔案，使裝置遵守輸出功率法規。
- `.mode=ap` → 將 WiFi 介面設定為在“接入點”模式下執行。
- `.ssid=input_your_SSID_here` → 配置 AP 將要廣播的 SSID 名稱。
- `security.authentication-types=wpa2-psk` → 指定要支援的身份驗證型別。
- `.passphrase=input_your_password_here` → 設定該 SSID 的密碼。

:::warning
如果你的鏈路長度超過 2km，還必須額外配置“distance”引數。此設定對 `wifi-qcom-ac` 驅動程式無效。
:::

- `configuration.distance=distance_in_km` → 設定最大鏈路距離，單位為千米。該值應反映距離裝置最遠的 AP 或 station 的距離。未配置該值時允許使用 2 km 鏈路。
- `channel.width=20mhz` → 設定通道寬度。通道寬度越小，距離越遠（干擾越少）。

### 其他需要考慮的設定 {#other-settings-to-consider}

#### 場景 #1 {#scenario-1}

如果你拓撲中已有負責向網路提供 IP 地址的 DHCP 伺服器，並且你想將 AP 安裝在其後方：

![](/img/fbef14d774a94c76.webp)

1. 確保 AP 已新增[橋接介面](../../bridging-and-switching/index.md#example)，並且所有乙太網和 WiFi 埠[都屬於該介面](../../bridging-and-switching/index.md#example-1)。
2. 在該橋接介面上設定 [DHCP 用戶端](../../network-management/dhcp.md#dhcp-client)，或者改為靜態新增 [IP 地址](../../getting-started/networking-fundamentals/index.md#address-configuration)和[預設路由](../../user-guides/routing-and-networking-protocols/routing-decision.md#default-route)。
3. 如有需要，更改介面列表成員角色。

#### 場景 #2 {#scenario-2}

如果你希望讓 AP 本身充當 station 的 DHCP 伺服器：

![](/img/9114f213f2546935.webp)

1. 將乙太網埠配置為上聯/WAN 埠，即為乙太網介面設定 [DHCP 用戶端](../../network-management/dhcp.md#dhcp-client)或[靜態 IP](../../getting-started/networking-fundamentals/index.md#address-configuration)，設定預設[路由](../../user-guides/routing-and-networking-protocols/routing-decision.md)，並在介面列表設定中將該埠歸類為“WAN”埠。
2. 在 WiFi 介面之上（或在該 WiFi 埠所屬的橋接介面之上）設定 [DHCP 伺服器](../../system-information-and-utilities/interface-lists.md)，併為該介面新增相應的  [IP 地址](../../network-management/dhcp.md#dhcp-server)。

## Station 設定 {#station-setup}

### WiFi 介面配置 {#wifi-interface-configuration-1}

要配置 station 模式，請執行以下命令：

```ros
/interface/wifi
set [ find default-name=wifi1 ] channel.frequency=5500 configuration.country=Latvia .mode=station .ssid=input_your_SSID_here security.authentication-types=wpa2-psk .passphrase=input_your_password_here
```

- `channel.frequency` → 選擇 AP 使用的頻率通道。如果你想使用“自動”通道選擇，可以跳過此項。
- `configuration.country` → 應用國家配置檔案，使裝置遵守輸出功率法規。
- `.mode=station` → 將 WiFi 介面設定為在“station”模式下執行。
- `.ssid=input_your_SSID_here` → 輸入 AP 正在廣播的 SSID 名稱。
- `security.authentication-types=wpa2-psk` → 指定要支援的身份驗證型別。
- `.passphrase=input_your_password_here` → 設定 AP 所期望的密碼。

:::warning
如果你的鏈路長度超過 2km，還必須額外配置“distance”引數。此引數對 `wifi-qcom-ac` 驅動程式無效。
:::

- `configuration.distance=distance_in_km` → 設定最大鏈路距離，單位為千米。該值應反映距離裝置最遠的 AP 或 station 的距離。未配置該值時允許使用 2 km 鏈路。

### 其他需要考慮的設定 {#other-settings-to-consider-1}

#### 場景 #1 {#scenario-1-1}

此場景中，station 的 WiFi 介面被歸類為“WAN”介面，這使 station 的用戶端可以隱藏在 [NAT](../../firewall-and-quality-of-service/firewall/nat.md) 之後。這是應用於大多數 CPE 裝置的出廠配置。

此類拓撲的示例：

![](/img/f962c200f2e841f3.webp)

此類設定要求 CPE 具備以下條件：

1. WiFi 介面在介面列表成員選單中被歸類為“WAN”埠。
2. 在“其他/乙太網”介面上執行 [DHCP 伺服器](../../system-information-and-utilities/interface-lists.md)（建議確保 AP 的 DHCP 伺服器和 Station 的 DHCP 伺服器網路不使用相同子網，因為這可能導致三層/路由問題）。
3. 為 WiFi 介面應用 [DHCP 用戶端](../../network-management/dhcp.md#dhcp-server)或[靜態 IP](../../network-management/dhcp.md#dhcp-client)，並配置[預設路由](../../getting-started/networking-fundamentals/index.md#address-configuration)。
4. 在 WiFi 設定中配置 [`mode=station`](../../user-guides/routing-and-networking-protocols/routing-decision.md)。

#### 場景 #2 {#scenario-2-1}

此場景中，你可以橋接 station 的埠，使 CPE 本身以及所有 CPE 用戶端都從 AP 獲取 DHCP 地址。

此類拓撲的示例：

![](/img/3ede6b8ead1ad35b.webp)

此類設定要求 CPE 具備以下條件：

1. 所有埠（WiFi 和乙太網）都加入同一個[橋接介面](../../bridging-and-switching/index.md#example)。
2. 該橋接介面在介面列表成員選單中被歸類為“LAN”介面。
3. 停用 [DHCP 伺服器](../../system-information-and-utilities/interface-lists.md)。
4. 為橋接介面應用 [DHCP 用戶端](../../network-management/dhcp.md#dhcp-server)或[靜態 IP](../../network-management/dhcp.md#dhcp-client)。
5. 在 WiFi 設定中配置 [`mode=station-bridge`](../../getting-started/networking-fundamentals/index.md#address-configuration)：

```ros
/interface/wifi
set [ find default-name=wifi1 ] configuration.mode=station-bridge
```

## 驗證 {#verification}

連線成功後，AP 和 Station 都應在“Registration”表中顯示一個新條目：

```ros
/interface/wifi/registration-table/print
Flags: A - AUTHORIZED
Columns: INTERFACE, SSID, MAC-ADDRESS, UPTIME, LAST-ACTIVITY, SIGNAL, AUTH-TYPE, BAND
#   INTERFACE  SSID        MAC-ADDRESS        UPTIME    LAST-ACTIVITY  SIGNAL  AUTH-TYPE  BAND   
0 A wifi1      input_SSID  XX:YY:ZZ:AA:30:6E  6h24m21s  0ms            -72     wpa2-psk   5ghz-ax
```

你還可以透過 CPE 使用“scan”命令檢查它是否正確發現/識別 AP：

```ros
/interface/wifi/scan [find where name=wifi1]
Flags: A - ACTIVE
Columns: ADDRESS, SSID, CHANNEL, SECURITY, SIGNAL, STA-COUNT
  ADDRESS            SSID               CHANNEL           SECURITY                              SIGNAL  STA-COUNT
A XX:YY:ZZ:AA:F4:28  SSID_Y             5620/ax           WPA2-PSK/WPA3-PSK                     -60             0
A XX:YY:ZZ:BB:0B:DA  SSID_X             5745/ax/Ce        WPA3-PSK                              -68             0
A XX:YY:ZZ:CC:0B:DA  input_SSID         5745/ax/Ce        WPA2-PSK                              -68             0
A XX:YY:ZZ:DD:0B:DA                     5745/ax/Ce        WPA2-PSK                              -68             0
```
