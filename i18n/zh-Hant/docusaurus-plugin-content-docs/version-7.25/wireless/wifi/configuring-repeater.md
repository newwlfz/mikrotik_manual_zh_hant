---
sidebar_key: "wireless/wifi/configuring-repeater"
sidebar_position: 3
title: "配置無線中繼器"
sidebar_label: "配置無線中繼器"
description: "本指南介紹如何使用 MikroTik RouterOS 的 wifi-qcom 軟體包配置無線中繼器，詳細說明雙頻介面（2.4 GHz 和 5 GHz）的設定步驟、SSID 管理、安全設定，以及漫遊行為和距離限制等故障排查注意事項。"
tags:
  - 'wifi'
  - 'repeater'
  - 'station-mode'
source: https://manual.mikrotik.com/docs/7.25/wireless/wifi/configuring-repeater
captured_at: '2026-11-04T11:24:25+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**軟體包：** `wifi-qcom`

:::info
本指南適用於執行 `wifi-qcom` 軟體包/驅動程式的 802.11 AX 裝置。
:::

Wi-Fi 範圍有限。AP（廣播 Wi-Fi 網路的裝置）執行在 2.4 和/或 5 GHz 頻率上。5 GHz 網路可提供更好的吞吐量，但覆蓋範圍較小。2.4 GHz 網路可確保更好的覆蓋，但吞吐量較低。

室內 AP 通常配備全向天線（可在 AP 周圍以“甜甜圈”形狀 360° 廣播訊號）。對於室內和短距離室外安裝，它是理想的天線選擇。使用帶有全向天線的簡單家用 AP，在“理想”的無干擾視距環境中，您可實現最遠 ±100 米的距離；在建築物內部，該距離會進一步大幅縮短。混凝土、管道、金屬、水……以及各種其他不同材料都會影響室內 Wi-Fi。有些物體會吸收訊號，有些會反射，有些會衍射，有些會散射訊號。

考慮到這一點，使用單個 AP/路由器並不總能覆蓋所需範圍，因此需要安裝額外的 AP。

為獲得最佳吞吐量，每個 AP 都應透過乙太網線纜連線到主網路。但是！由於各種原因……很可能是為了美觀，並不總是能夠將線纜從 AP 布放到主路由器。

這時“**中繼器**”或“**擴充套件器**”就能派上用場。

擴充套件器/中繼器的工作是作為“用戶端”或“station”與主路由器建立 Wi-Fi 連線，將此連線用作上行鏈路連線，同時廣播擴充套件器自身的 Wi-Fi 網路。

:::info
**吞吐量！**

當裝置用作擴充套件器時，您從中獲得的吞吐量至少會減半。

一半資源被分配用於保持與路由器的持續連線，而另一半則留給重傳。這會使總空口時間加倍。

另外！由於您將擴充套件器安裝在距離主路由器較遠的位置……隨著距離增加，Wi-Fi 吞吐量會進一步降低。
:::

:::info
**漫遊！**

如果您從路由器設定中複製 SSID 名稱，並將擴充套件器配置為廣播相同的 SSID 名稱 → 漫遊將完全取決於用戶端。

漫遊是指您的用戶端裝置在使用相同 Wi-Fi 名稱的不同 AP 之間切換。有些標準可以幫助“加速”和“平滑”切換（如 802.11 r/k/v），但遺憾的是，在此設定中無法使用它們，因此，“漫遊”或“不漫遊”的決定完全由用戶端決定。不同廠商實現了不同的演算法，來決定您的用戶端裝置應如何以及何時切換。

請記住這一點！一些具有良好演算法（決策）的裝置會正確漫遊，而其他裝置可能會粘在訊號較差的、最遠的 AP 上。
:::

## 中繼器設定 {#repeater-setup}

:::info
**使用哪個頻率？**

雙頻路由器和接入點從一開始就應該有兩個 Wi-Fi 介面 → wifi1 和 wifi2，分別代表特定頻率，即 5 GHz 和 2.4 GHz。對於中繼器設定，需要將其中一個介面轉換為 **station** 介面（它將作為另一個網路的用戶端），而另一個介面應設定為 **ap** 模式（這將允許裝置廣播自己的網路）。

如果我們將 2.4 GHz 用作 **station** 介面，這會增加我們可以安裝中繼器的距離，但也會降低從中獲得的吞吐量。如果我們將 5 GHz 用作 **station** 介面，我們會縮小覆蓋範圍，但提高吞吐量。
:::

:::warning
由於我們將更改 Wi-Fi 和埠相關配置，建議使用 MAC 地址透過乙太網埠/線纜連線到裝置設定。您可以使用 [Winbox](../../management-tools/winbox.md) 的“Neighbors”標籤頁，並雙擊列表中的裝置 MAC 地址。這樣，您以後在更改介面相關設定時就不會失去訪問許可權。
:::

在我們的示例中，我們希望將 wifi2（2.4 GHz）用作“station”介面，同時讓 wifi1（5 GHz）廣播中繼器自己的 SSID（並且還可能透過 2.4 GHz 重新廣播路由器的 SSID）：

![](/img/bc62e140b589d78a.webp)

整體配置：

```ros
/interface/wifi
set [ find default-name=wifi2 ] configuration.mode=station-bridge configuration.country=Latvia .ssid=router.ssid.2 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
set [ find default-name=wifi1 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.5 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
add configuration.mode=ap .ssid=router.ssid.2 disabled=no master-interface=wifi2 name=wifi3 security.authentication-types=wpa2-psk .passphrase=router.password
/interface/list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface/bridge
add auto-mac=no comment=defconf name=bridge
/interface/bridge/port
add interface=all bridge=bridge 
/interface/list/member
add comment=defconf interface=bridge list=LAN
/ip/dhcp-client
add interface=bridge
```

### 2.4 GHz 介面配置 {#24-ghz-interface-configuration}

```ros
/interface/wifi
set [ find default-name=wifi2 ] configuration.mode=station-bridge .ssid=router.ssid.2 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=station-bridge` → 選擇 [station 模式](../user-guides/wireless-station-modes.md)。

:::info
**使用哪種 station 模式？**

對於 **MikroTik Wi-Fi 6 AX**（使用 `wifi-qcom` 軟體包/驅動程式的路由器）到 **MikroTik Wi-Fi 6 AX**（使用 `wifi-qcom` 軟體包/驅動程式的中繼器/station）連線，請使用 **`station-bridge`** 模式。

對於 **第三方廠商** 或 **MikroTik 傳統 WiFi 5 AC 及以下**（路由器）到 **Wi-Fi 6 AX**（中繼器）連線，請使用 **`station-pseudobridge`** 模式。

`station-pseudobridge` 做類似“網路地址轉換”的事情，但針對的是 MAC 地址。使用此模式時，如果您有多臺裝置連線到中繼器並且它們都訪問網際網路，路由器會看到所有這些嘗試都來自單個 MAC 地址。基本上，所有用戶端裝置都會隱藏在一個 MAC 地址後面，這可能會導致網路問題。不建議使用此模式，但在這種情況下，沒有其他選擇。

此外，在傳統 MikroTik 裝置上使用 `station-pseudobridge` 時，請確保傳統裝置已使用命令 `/interface/bridge/set protocol-mode=none` 在其橋接埠上停用 [RSTP](../../bridging-and-switching/user-guides/spanning-tree-protocol.md)。否則，RSTP 可能會導致 DHCP-client 功能出現問題，以及透過橋接埠傳遞 IP 地址時出現問題。
:::

- `configuration.country=Latvia` → 選擇您實際所在的國家/地區，以免違反任何法規（您所在國家的“法律”）。不同的國家/地區配置檔案針對不同頻率範圍允許不同的輸出功率。
- `ssid=router.ssid.2` → 這是路由器廣播的 2.4 GHz SSID 網路名稱（中繼器應連線到此網路）。
- `security.authentication-types=wpa2-psk` → 選擇主路由器使用的認證型別。
- `passphrase=router.password` → 配置主路由器網路的密碼。這是您路由器設定中配置的密碼。

### 5 GHz 介面配置 {#5-ghz-interface-configuration}

```ros
/interface/wifi
set [ find default-name=wifi1 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.5 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=ap` → 將介面配置為在“接入點”模式下工作。
- `configuration.country=Latvia` → 選擇您實際所在的國家/地區，以免違反任何法規（您所在國家的“法律”）。不同的國家/地區配置檔案針對不同頻率範圍允許不同的輸出功率。
- `ssid=router.ssid.5` → 配置中繼器需要重新廣播的無線網路名稱（SSID）。它可以與主路由器使用的網路名稱相同，也可以是不同的名稱。為進行測試，最好使用“唯一”的名稱，以便區分網路。要發生“用戶端漫遊”，請使用路由器設定中完全相同的 Wi-Fi 名稱。
- `security.authentication-types=wpa2-psk` → 選擇要使用的認證型別。要發生“用戶端漫遊”，請使用路由器設定中完全相同的認證型別。
- `passphrase=router.password` → 設定中繼器 Wi-Fi 網路的密碼。要發生“用戶端漫遊”，請使用路由器設定中完全相同的密碼。

### 可選步驟 - 新增虛擬介面 {#optional-step---adding-virtual-interface}

如果您希望擴充套件器使用兩個頻率重新廣播無線網路（例如，`wifi2` 保留給 `mode=station-bridge`，而您只剩下 `wifi1` 用於 `mode=ap`），請在 `station` 介面之上建立一個虛擬介面：

```ros
/interface/wifi
add configuration.mode=ap .ssid=router.ssid.2 disabled=no master-interface=wifi2 name=wifi3 security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=ap` → 確保它將充當“接入點”介面。
- `ssid=router.ssid.2` → 配置中繼器需要重新廣播的無線網路名稱（SSID）。要發生“用戶端漫遊”，請使用路由器設定中完全相同的 Wi-Fi 名稱。
- `master-interface=wifi2` → 指定“虛擬”介面所“基於”的介面（指定在哪個介面之上建立它）。選擇用作 `station` 介面的介面。
- `name=wifi3` → 命名虛擬介面。
- `security.authentication-types=wpa2-psk` → 選擇要使用的認證型別。要發生“用戶端漫遊”，請使用路由器設定中完全相同的認證型別。
- `passphrase=router.password` → 設定中繼器 Wi-Fi 網路的密碼。要發生“用戶端漫遊”，請使用路由器設定中完全相同的密碼。

:::info
虛擬介面將使用與 `station` 介面連線路由器所使用的完全相同的頻率通道。此介面的 Wi-Fi 頻率通道無法更改。
:::

### 橋接和列表 {#bridging-and-listing}

[橋接所有埠](../../bridging-and-switching/index.md#example-1)（乙太網、Wi-Fi 和虛擬 Wi-Fi 介面）：

```ros
/interface/bridge
add auto-mac=no comment=defconf name=bridge
/interface/bridge/port
add interface=all bridge=bridge 
```

並確保橋接介面被列為“LAN”介面（`/interface list member add comment=defconf interface=bridge list=LAN`），以便防火牆規則不會阻止對擴充套件器管理的訪問：

```ros
/interface/list/member
add comment=defconf interface=bridge list=LAN
```

當然，前提是您在主路由器上添加了適當的防火牆和訪問限制。否則，請對其進行限制。

### DHCP {#dhcp}

```ros
/ip/dhcp-client
add interface=bridge
```

在橋接介面之上應用 [DHCP 用戶端](../../network-management/dhcp/client.md#configuration-examples)，以便中繼器本身及其所有連線的用戶端從主路由器獲取 IP 地址。

停用 [DHCP 伺服器](../../network-management/dhcp/server.md) 功能。

### 地址 {#address}

移除/停用預設配置橋接介面分配的 [IP 地址](../../getting-started/networking-fundamentals/index.md#address-configuration)，以防您的路由器網路使用相同子網，從而避免與閘道器 IP“衝突”。
