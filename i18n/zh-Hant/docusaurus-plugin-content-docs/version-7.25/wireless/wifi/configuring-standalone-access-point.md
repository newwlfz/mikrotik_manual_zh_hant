---
sidebar_key: "wireless/wifi/configuring-standalone-access-point"
sidebar_position: 4
title: "配置獨立接入點"
sidebar_label: "配置獨立接入點"
description: "本指南提供有關使用 MikroTik RouterOS 的 wifi-qcom 軟體包配置獨立接入點（AP）的說明，詳細介紹了 2.4/5 GHz 網路的設定步驟、天線選擇以及橋接配置，同時提醒在沒有 CAPsMAN 管理的情況下漫遊存在限制。"
tags:
  - 'wifi'
  - 'access-point'
  - 'ssid'
source: https://manual.mikrotik.com/docs/7.25/wireless/wifi/configuring-standalone-access-point
captured_at: '2026-11-04T11:24:19+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**軟體包：** `wifi-qcom`

:::info
本指南適用於執行 `wifi-qcom` 軟體包/驅動程式的 802.11 AX 裝置。
:::

Wi-Fi 裝置可以扮演不同的角色。幾乎所有家庭都有的最常見裝置稱為 Wi-Fi 路由器。典型的 Wi-Fi 路由器通常具有 WAN 埠（用於 ISP 連線）、LAN 埠（用於本地 PC、有線印表機等）和一個 WLAN 網路（Wi-Fi 網路）。路由器也被稱為“閘道器”和“防火牆”，因為它們充當本地網路用戶端進入 Internet 的“門戶”（這些裝置會將連線到 LAN 的用戶端“隱藏”在其後面並保護它們）。

:::info
路由器是防火牆/閘道器裝置，其連線了 ISP 線纜，受[防火牆保護](../../firewall-and-quality-of-service/firewall/index.md)並啟用了 [DHCP 伺服器](../../network-management/dhcp/server.md) 功能（該功能會向透過無線和有線方式連線的 LAN 用戶端提供 IP 地址）。
:::

Wi-Fi 裝置的另一種角色稱為“接入點”，簡稱“AP”。這些裝置通常透過乙太網連線（連線到路由器的 LAN 埠）連線到主“路由器/閘道器/防火牆”；它們不受防火牆保護，也未啟用 DHCP-server 功能（它們不提供 IP 地址）。AP 會將其所有 Wi-Fi 和 LAN 介面/埠橋接，因此，AP 會從路由器連線中“獲取”IP 地址，並將其“傳遞”給連線到 AP 的用戶端（充當“二層”橋接/交換器）。

:::info
接入點是“橋接”裝置，使用乙太網線連線到路由器；它們不受[防火牆保護](../../firewall-and-quality-of-service/firewall/index.md)，並且已停用 [DHCP 伺服器](../../network-management/dhcp/server.md) 功能（它們會把來自路由器的 DHCP 請求“橋接”到 AP 的用戶端）。
:::

換言之，**Wi-Fi 路由器** **就是** **具備附加功能的 AP**。

AP（廣播 Wi-Fi 網路的裝置）執行在 2.4 和/或 5 GHz 頻率上。5 GHz 網路可提供更好的吞吐量，但覆蓋範圍較小。2.4 GHz 網路可確保更好的覆蓋範圍，但吞吐量較低。

室內 AP 通常配備全向天線（可在 AP 周圍以“甜甜圈”形狀 360° 廣播訊號）。對於室內和短距離室外安裝，它是理想的天線選擇。使用帶有全向天線的簡單家用 AP，在“理想”的無干擾視距環境中，您可實現最遠 ±100 米的距離；在建築物內部，該距離會進一步大幅縮短。混凝土、管道、金屬、水……以及各種其他不同材料都會影響室內 Wi-Fi。有些物體會吸收訊號，有些會反射，有些會衍射，有些會散射訊號。

考慮到這一點，使用單個 AP/路由器並不總是能夠覆蓋所需範圍，可能需要安裝額外的 AP；這意味著，如果你家中有 Wi-Fi 訊號較差或不存在的問題區域，請考慮在更靠近該問題區域的位置安裝新的 AP。

:::warning
**本指南適用於**“基礎”或所謂的 **“獨立” AP 設定**。如果你使用的是第三方廠商 Wi-Fi 路由器（非 MikroTik）、舊版 Wi-Fi 5 (AC) MikroTik 路由器，或者你之前的設定中完全沒有 Wi-Fi AP，則可以使用本指南。

**對於由 `wifi-qcom` 軟體包/驅動 AP 組成的設定，請使用 [CAPSMAN 管理](./capsman.md)**，因為它支援 802.11 r/k/v 漫遊標準，可讓用戶端切換更平滑。
:::

:::note
**非 802.11 r/k/v 漫遊！**

在“獨立”AP 設定中，如果你只是從路由器設定中複製 SSID 名稱，並將 AP 配置為廣播相同的 SSID 名稱 → 漫遊將完全取決於用戶端。

漫遊是指用戶端裝置在使用相同 WiFi 名稱的不同 AP 之間切換。有些標準可以幫助“加速”和“平滑”切換（例如 802.11 r/k/v），但遺憾的是，在此設定中無法使用它們（因為不存在“管理”裝置），因此，“是否漫遊”完全由用戶端決定。不同廠商實現了不同的演算法來決定用戶端裝置應如何以及何時切換。

請牢記這一點！一些具有良好演算法（決策能力）的裝置會正確漫遊，而其他裝置可能會一直連線到訊號較差（距離最遠）的 AP。
:::

我們的大多數（如果不是全部）MikroTik Wi-Fi 裝置都預配置為[“路由器”角色](../../getting-started/first-time-configuration.md)。本指南將展示如何將它們轉換為獨立 AP 角色裝置（二層橋接 AP）。

## 接入點設定 {#access-point-setup}

:::warning
由於我們將更改 Wi-Fi 和埠相關配置，建議使用 MAC 地址透過乙太網埠/網線連線到裝置設定。你可以使用 [Winbox](../../management-tools/winbox.md) 的“Neighbors”標籤頁，並雙擊列表中的裝置 MAC 地址。這樣，在之後更改介面相關設定時，你就不會失去訪問許可權。
:::

整體配置：

```ros
/interface/wifi
set [ find default-name=wifi2 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.2 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
set [ find default-name=wifi1 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.5 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
add configuration.mode=ap .ssid=guest.ssid.2 disabled=no master-interface=wifi2 name=wifi3 security.authentication-types=wpa2-psk .passphrase=guest.password
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
set [ find default-name=wifi2 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.2 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=ap` → 將介面配置為在“接入點”模式下工作。
- `configuration.country=Latvia` → 選擇你實際所在的國家/地區，以免違反任何法規（你所在國家的“法律”）。不同的國家/地區配置檔案針對不同頻率範圍允許不同的輸出功率。
- `ssid=router.ssid.2` → 配置 AP 需要廣播的無線網路名稱（SSID）。它可以與主路由器使用的網路名稱相同，也可以是不同的名稱。測試時，最好使用“唯一”名稱，以便區分網路。要實現“用戶端漫遊”，請使用路由器設定中完全相同的 WiFi 名稱。
- `security.authentication-types=wpa2-psk` → 選擇要使用的認證型別。要實現“用戶端漫遊”，請使用路由器設定中完全相同的認證型別。
- `passphrase=router.password` → 設定 AP 的 WiFi 網路密碼。要實現“用戶端漫遊”，請使用路由器設定中完全相同的密碼。

### 5 GHz 介面配置 {#5-ghz-interface-configuration}

```ros
/interface/wifi
set [ find default-name=wifi1 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.5 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=ap` → 將介面配置為在“接入點”模式下工作。
- `configuration.country=Latvia` → 選擇你實際所在的國家/地區，以免違反任何法規（你所在國家的“法律”）。不同的國家/地區配置檔案針對不同頻率範圍允許不同的輸出功率。
- `ssid=router.ssid.5` → 配置 AP 需要廣播的無線網路名稱（SSID）。它可以與主路由器使用的網路名稱相同，也可以是不同的名稱。測試時，最好使用“唯一”名稱，以便區分網路。要實現“用戶端漫遊”，請使用路由器設定中完全相同的 WiFi 名稱。
- `security.authentication-types=wpa2-psk` → 選擇要使用的認證型別。要實現“用戶端漫遊”，請使用路由器設定中完全相同的認證型別。
- `passphrase=router.password` → 設定 AP 的 WiFi 網路密碼。要實現“用戶端漫遊”，請使用路由器設定中完全相同的密碼。

#### **增大 5 GHz 覆蓋範圍** {#increasing-5-ghz-range}

地方主管部門會管制 Wi-Fi 裝置的輸出功率。不同國家/地區的不同頻率範圍可能允許不同的功率。你可以使用以下命令檢查你的國家/地區配置檔案適用哪些限制：

```ros
/interface/wifi/radio/reg-info country=Latvia 0      
  ranges: 2402-2482/20dBm/40MHz   
          5170-5250/23dBm/160MHz/indoor    
          5250-5330/23dBm/160MHz/indoor/dfs
          5490-5730/30dBm/160MHz/dfs     
          5735-5875/14dBm/80MHz 
```

根據該表，我們可以看到（使用“Latvia”國家配置檔案時）在通道 `5490-5730` 上可獲得的最大功率為 `30 dBm`。

此表中顯示的“dBm”表示“允許的 EIRP”（EIRP=Tx power + 天線增益）。為了不違反任何法規和“法律”，裝置的天線增益越高，設定的 Tx power 就越低（如果裝置具有內建天線，這將**自動**發生），以匹配允許的“EIRP”值。

另請注意，最高“EIRP”的通道可能是“DFS”通道（意味著如果在該通道上檢測到雷達，廣播就會停止）。這一點需要牢記！

根據這些資訊和該表，我們可以看到明智的做法是避免使用 `5735-5875` 範圍，因為它只允許 `14 dBm`。

通道允許的“EIRP”越大 = 可用輸出功率越大 = 訊號越強 = 可達到的距離越遠。

:::info
請注意，有一個名為 `Superchannel` 的國家/地區配置檔案。在此配置檔案中，輸出功率不受任何軟體限制。此模式只應在受控環境中使用，或者在你擁有所在地區使用許可時使用。你可以將其與直接在設定中“降低”Tx power 值結合使用，以獲得“自定義”輸出功率。
:::

要設定通道或範圍，請執行以下命令：

```ros
/interface/wifi
set [ find default-name=wifi1 ] channel.frequency=5490-5730
```

### 可選步驟 - 新增虛擬介面 {#optional-step---adding-virtual-interface}

如果你想建立額外網路（額外 SSID 名稱），可以在另一個介面之上建立 `virtual` 介面：

```ros
/interface/wifi
add configuration.mode=ap .ssid=guest.ssid.2 disabled=no master-interface=wifi2 name=wifi3 security.authentication-types=wpa2-psk .passphrase=guest.password
```

- `configuration.mode=ap` → 確保它將作為“接入點”介面工作。
- `ssid=guest.ssid.2` → 配置 AP 需要廣播的無線網路名稱（SSID）。要實現“用戶端漫遊”，請使用路由器設定中完全相同的 WiFi 名稱。
- `master-interface=wifi2` → 指定將“虛擬”介面“基於”哪個介面（指定在哪個介面之上建立它）。
- `name=wifi3` → 為虛擬介面命名。
- `security.authentication-types=wpa2-psk` → 選擇要使用的認證型別。要實現“用戶端漫遊”，請使用路由器設定中完全相同的認證型別。
- `passphrase=guest.password` → 設定 AP 的 WiFi 網路密碼。要實現“用戶端漫遊”，請使用路由器設定中完全相同的密碼。

:::info
虛擬介面將使用與 `master` 介面完全相同的頻率通道。此介面的 Wi-Fi 頻率通道無法更改。
:::

### 橋接和列表 {#bridging-and-listing}

[橋接所有埠](../../bridging-and-switching/index.md#example-1)：

```ros
/interface/bridge
add auto-mac=no comment=defconf name=bridge
/interface/bridge/port
add interface=all bridge=bridge 
```

並確保橋接介面被列為“LAN”介面（`/interface list member add comment=defconf interface=bridge list=LAN`），以便防火牆規則不會阻止對 AP 管理介面的訪問：

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

在橋接介面之上應用 [DHCP 用戶端](../../network-management/dhcp/client.md#configuration-examples)，以便 AP 本身及其所有連線的用戶端都從主路由器獲取 IP 地址。

停用 [DHCP 伺服器](../../network-management/dhcp/server.md) 功能。

### 地址 {#address}

如果路由器網路使用相同子網，請移除/停用預設配置中由橋接分配的 [IP 地址](../../getting-started/networking-fundamentals/index.md#address-configuration)，以免與閘道器 IP 發生“衝突”。
