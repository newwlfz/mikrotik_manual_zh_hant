---
sidebar_key: "wireless/wifi/index"
sidebar_position: 6
title: "Wi-Fi 6 / 7（802.11ax/be）"
sidebar_label: "Wi-Fi 6 / 7"
description: "本頁介紹 RouterOS 中的 WiFi 配置選單，涵蓋受密碼保護和 OWE 過渡模式接入點的基本設定。其中說明了配置配置檔案、安全設定，幷包含重設配置的示例。"
tags:
  - 'wifi'
  - 'configuration-profiles'
  - 'access-lists'
source: https://manual.mikrotik.com/docs/7.24/wireless/wifi
captured_at: '2026-11-04T11:36:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 MikroTik **Wi-Fi 6 / 6E / 7 (802.11ax/be)** 裝置，這些裝置均透過共享的 **`/interface/wifi`** 選單進行配置。裝置需要哪個驅動程式包取決於其無線晶片組和標準。同一選單也涵蓋執行 **`wifi-qcom-ac`** 包的 **Wi-Fi 5 (802.11ac)** 裝置。

:::tip[這一節是否適用於我的裝置？]
凡執行下列任一驅動包的裝置，都使用本選單（以及本手冊）：

| 包 | 裝置 | 示例 |
| :-- | :-- | :-- |
| `wifi-qcom` | Wi-Fi 6 / 6E (Qualcomm) | wAP ax, cAP ax, hAP ax³ |
| `wifi-qcom-be` | Wi-Fi 7 (Qualcomm) | hAP be3 media |
| `wifi-mediatek` | Wi-Fi 6 / 7 (MediaTek) | hAP ax S, hAP be lite |
| `wifi-qcom-ac` | Wi-Fi 5 / 802.11ac (Qualcomm) | 參見 [Wi-Fi 5 (802.11ac)](../wifi-ac/index.md) |

標準通常已體現在型號名稱中——Wi-Fi 6 為 **ax**，Wi-Fi 7 為 **be**。對於 `wifi-qcom-ac` 裝置，請參見 [Wi-Fi 5 (802.11ac)](../wifi-ac/index.md)，以確認你的裝置應使用本選單還是舊版 `/interface/wireless` 選單。

如果你的裝置改用舊版 `/interface/wireless` 選單，請參見 [802.11 a/b/g/n](../abgn/index.md)。
:::

:::note
在 7.13 之前的 RouterOS 版本中，此選單是一個名為 `wifiwave2` 的獨立包的一部分。
:::

## 快速開始 {#getting-started}

剛接觸這類裝置？請先從面向任務的指南開始，然後使用本頁後面的屬性參考瞭解各項設定：

- [配置獨立接入點](./configuring-standalone-access-point.md)
- [配置中繼器](./configuring-repeater.md)
- [配置室外 CPE 到 AP 鏈路](./configuring-outdoor-cpe-to-ap-links.md)
- [WiFi6 的 Interworking（802.11u / Hotspot 2.0）](./interworking-for-wifi6.md)
- [使用 WiFi CAPsMAN 進行集中管理](./capsman.md)

## WiFi 術語 {#wifi-terminology}

在繼續之前，先來熟悉一些對理解該選單運作方式很重要的術語。這些術語將在整篇文章中使用。

- **配置檔案（Profile）**——指在以下某個 WiFi 子選單下建立的配置預設：**aaa**、**channel**、**security**、**datapath** 或 **interworking**。
- **配置配置檔案（Configuration profile）**——在 `/interface/wifi/configuration` 下定義的配置預設，它可以引用各種配置檔案。
- **站點（Station）**——無線用戶端。

## 基本配置 {#basic-configuration}

### 基本的受密碼保護的 AP {#basic-password-protected-ap}

```ros
/interface/wifi
set wifi1 disabled=no configuration.country=Latvia configuration.ssid=MikroTik security.authentication-types=wpa2-psk,wpa3-psk security.passphrase=8-63_characters
```

### 帶 OWE 過渡模式的開放 AP {#open-ap-with-owe-transition-mode}

機會性無線加密（OWE）允許建立無需知道密碼即可連線、但仍具備流量加密和管理幀保護優點的無線網路。它是對常規開放接入點的改進。

然而，由於一個網路不能同時既加密又不加密，因此需要 2 個獨立的介面配置，才能既為不支援 OWE 的舊裝置提供連線，又為支援 OWE 的裝置提供 OWE 的優勢。

這種配置稱為 OWE 過渡模式。

```ros
/interface/wifi
add master-interface=wifi1 name=wifi1_owe configuration.ssid=MikroTik_OWE security.authentication-types=owe security.owe-transition-interface=wifi1 configuration.hide-ssid=yes
set wifi1 configuration.country=Latvia configuration.ssid=MikroTik security.authentication-types="" security.owe-transition-interface=wifi1_owe
enable wifi1,wifi1_owe
```

使用這樣的設定，AP 將廣播兩個 SSID → 可見的 `MikroTik` SSID，它應提供"未加密"接入（面向不支援 OWE 的舊裝置），以及隱藏的 SSID `MikroTik_OWE`，它應使用"OWE"安全（無密碼保護，但已加密）。用戶端裝置不會（在用戶端的 WiFi 列表中）看到隱藏的 `MikroTik_OWE` SSID，但可見 `MikroTik` SSID 的信標包會在信標包中使用"OWE Transition mode"引數，改為通告指向隱藏 `MikroTik_OWE` 網路的連結。因此，用戶端裝置應會優先透過 `owe-transition-interface` 設定連線到"OWE"網路。

支援 OWE 的用戶端裝置會優先選擇 OWE 介面。如果你在登錄檔中看不到任何關聯到常規開放 AP 的裝置，那麼可以考慮從過渡模式設定改為單一的 OWE 加密介面：

```ros
/interface/wifi
set wifi1 configuration.country=Latvia configuration.ssid=MikroTik_OWE security.authentication-types=owe
```

:::info
802.11r（快速漫遊）無法在 OWE 網路上工作。
:::

### 重設配置 {#resetting-configuration}

WiFi 介面配置可以透過 'reset' 命令重設。

```ros
/interface/wifi/reset wifi1
```

物理介面的 MAC 地址可以透過 'reset-mac-address' 命令重設為預設值。

```ros
/interface/wifi/reset-mac-address wifi1
```

## 配置配置檔案 {#configuration-profiles}

WiFi 的新增功能之一是配置配置檔案。你可以建立各種預設，並按需分配給介面。WiFi 的配置設定按照本頁末尾的引數分節分組到**配置檔案**中——**aaa**、**channel**、**configuration**、**datapath**、**interworking** 和 **security**，然後可以分配給介面。**配置配置檔案**可以包含其他配置檔案，也可以包含來自其他類別的單獨引數。

這種可選的靈活性旨在讓每位使用者都能按最適合自己的方式組織配置，但這也意味著同一個引數在配置的不同部分可能被賦予不同的值。

以下優先順序決定了最終使用哪個值：

1. 介面設定中的值。
2. 分配給介面的配置檔案中的值。
3. 分配給介面的配置配置檔案中的值。
4. 分配給配置配置檔案的配置檔案（該配置配置檔案又分配給介面）中的值。

如果在任何時候不確定介面會使用哪個引數值，可以執行 "/interface/wifi/print detail"。print 命令會顯示介面將具有的所有值，包括繼承來的值。

若只想檢視直接在介面上配置的值，而不顯示繼承來的值，請使用 "/interface/wifi/print config"。

關於配置配置檔案用法的示例，請參見以下內容（雙頻家用 AP 示例）：

```ros
# 创建安全配置文件，两个接口将共用该配置
/interface/wifi/security
add name=common-auth authentication-types=wpa2-psk,wpa3-psk passphrase="diceware makes good passwords" wps=disable
# 创建通用配置模板，并将安全配置文件关联到它
/interface/wifi/configuration
add name=common-conf ssid=MikroTik country=Latvia security=common-auth
# 为每个频段分别创建信道配置
/interface/wifi/channel
add name=ch-2ghz frequency=2412,2432,2472 width=20mhz
add name=ch-5ghz frequency=5180,5260,5500 width=20/40/80mhz
# 为每个接口分配通用模板以及特定频段的信道模板；如果接口上出现 "no supported channels" 消息，请确保为每个接口应用了正确的（信道）配置。
set wifi1 channel=ch-5ghz configuration=common-conf disabled=no
set wifi2 channel=ch-2ghz configuration=common-conf disabled=no

#"print detail" 将显示接口将使用的所有值，包括继承的值
[admin@c52i] > /interface/wifi/print detail 
Flags: M - master; D - dynamic; B - bound; X - disabled, I - inactive, R - running 
 0 M B  default-name="wifi1" name="wifi1" l2mtu=1560 mac-address=18:FD:74:AF:F4:28 arp-timeout=auto radio-mac=18:FD:74:AF:F4:28 configuration=common-conf 
        configuration.mode=ap .ssid="MikroTik" .country=Latvia 
        security.authentication-types=wpa2-psk,wpa3-psk .passphrase="diceware makes good passwords" .wps=disable 
        channel=ch-5ghz 
        channel.frequency=5180,5260,5500 .width=20/40/80mhz 

 1 M B  default-name="wifi2" name="wifi2" l2mtu=1560 mac-address=18:FD:74:AF:F4:29 arp-timeout=auto radio-mac=18:FD:74:AF:F4:29 configuration=common-conf 
        configuration.mode=ap .ssid="MikroTik" .country=Latvia 
        security.authentication-types=wpa2-psk,wpa3-psk .passphrase="diceware makes good passwords" .wps=disable 
        channel=ch-2ghz 
        channel.frequency=2412,2432,2472 .width=20mhz 
#使用 "print detail config" 只显示直接在接口上配置的值
[admin@c52i] > /interface/wifi/print detail config  
Flags: M - master; D - dynamic; B - bound; X - disabled, I - inactive, R - running 
 0 M B  default-name="wifi1" name="wifi1" l2mtu=1560 mac-address=18:FD:74:AF:F4:28 arp-timeout=auto radio-mac=18:FD:74:AF:F4:28 configuration=common-conf 
        configuration.mode=ap 
        channel=ch-5ghz 

 1 M B  default-name="wifi2" name="wifi2" l2mtu=1560 mac-address=18:FD:74:AF:F4:29 arp-timeout=auto radio-mac=18:FD:74:AF:F4:29 configuration=common-conf 
        configuration.mode=ap 
        channel=ch-2ghz 
```

:::info
`print detail` 和 `print detail config` 也可以用於 `/interface/wifi/configuration`，其工作方式與在 `/interface/wifi/` 選單中相同。
:::

## 網路 {#network}

`/interface/wifi/network` 選單把 SSID、安全、datapath 和 radio 設定打包成單一的配置實體。network 會應用於與其 `labels` 匹配的 WiFi 介面。如果未指定 `labels`，則該 network 的配置會應用到所有介面。

關於 network 配置用法的示例，請參見以下內容：

```ros
# 创建包含 SSID、安全和 datapath 设置的网络预设，该预设会应用到所有可用接口
/interface/wifi/network
add ssid=MikroTik mode=ap security.authentication-types=wpa2-psk,wpa3-psk security.passphrase="strong_password" datapath.bridge=bridge1 disabled=no

# 创建网络 radio 预设，该预设会应用到整个 radio。
/interface/wifi/network/radio
add configuration.country=Latvia
```

啟用多鏈路操作（MLO）的示例：

```ros
/interface/wifi/network
add datapath.bridge=bridge1 disabled=no mlo=yes mode=ap security.authentication-types=wpa3-psk ssid="MikroTik" security.passphrase="strong_password"
```

| 屬性 | 說明 |
| :-- | :-- |
| **mlo** (*no* \| *yes; default: **yes***) | 為 Wi-Fi 7 啟用多鏈路操作。 |
| **labels** (*comma-separated strings*) | 在與所提供任一標籤匹配的 radio 上啟用該 network 配置。 |
| **ssid** (*string*) | 無線網路名稱（ESSID）。 |
| **mode** (*ap* \| *station* \| *station-bridge* \| *station-pseudobridge*; default: **ap***) | 介面執行模式。 |
| **disabled** (*no* \| *yes; default: **no***) | 該 network 是否被停用。 |

所有安全、認證和加密引數（passphrase、WPA3/SAE、EAP 等）共用[安全屬性](#security-properties)中描述的相同屬性。Datapath 引數（bridge、VLAN、用戶端隔離、流量處理）遵循 [Datapath 屬性](#datapath-properties)。

### Network radio 屬性 {#network-radio-properties}

`/interface/wifi/network/radio` 下按 radio 劃分的設定：

| 屬性 | 說明 |
| :-- | :-- |
| **labels** (*object*) | 將 radio 配置與具有給定標籤的物理 radio 匹配。 |
| **extra-labels** (*multi string*) | 用於匹配的額外標籤，用於擴充套件主 `labels` 欄位。 |
| **disabled** (*no* \| *yes; default: **no***) | 該 radio 條目是否被停用。 |

Radio 引數（country、band、frequency、width、chains、power 等）使用[通道屬性](#channel-properties)和[配置屬性](#configuration-properties)中描述的相同屬性。

## 訪問列表 {#access-list}

訪問列表提供了多種過濾和管理無線連線的方式。

RouterOS 會檢查每個新連線，看其引數是否匹配任一訪問列表規則中指定的引數。

規則按其在列表中出現的順序進行檢查。每個連線只應用第一條匹配規則中指定的管理動作。

被訪問列表規則接受的連線會被定期檢查，以確認它們是否仍處於允許的 **time、days** 和 **signal-range** 範圍內。如果不滿足，連線將被終止。

:::warning
編寫拒絕用戶端的訪問列表規則時要小心。用戶端裝置在被 AP 反覆拒絕後，可能會開始避開它。對於 wifi-qcom-ac 介面的用戶端，如果不先為介面配置 pvid 值，訪問列表就無法為其設定 VLAN ID。
:::

訪問列表有兩類引數——[過濾](#access-list)引數和[動作](#access-list)引數。過濾屬性僅用於匹配應應用該訪問列表規則的用戶端。動作引數可以更改該特定用戶端的連線引數，並可能用訪問列表規則中指定的值覆蓋其預設連線引數。

### MAC 地址認證 {#mac-address-authentication}

MAC 地址認證透過 **query-radius** 動作實現，是一種使用 RADIUS 伺服器實現用戶端 MAC 地址集中白名單的方式。

當用戶端設備嘗試關聯到配置為執行 MAC 地址認證的 AP 時，AP 會向 RADIUS 伺服器傳送一條 access-request 訊息，以裝置的 MAC 地址作為使用者名稱並提供空密碼。如果 RADIUS 伺服器對此類請求回覆 access-accept，AP 就會繼續執行介面所配置的常規認證流程（passphrase 或 EAP 認證）。

### 訪問規則示例 {#access-rule-examples}

僅在工作時間接受附近裝置連線到訪客網路：

```ros
/interface/wifi/access-list/print detail
Flags: X - disabled 
 0   signal-range=-60..0 allow-signal-out-of-range=5m ssid-regexp="MikroTik Guest" time=7h-19h days=mon,tue,wed,thu,fri action=accept

 1   ssid-regexp="MikroTik Guest" action=reject 
```

拒絕來自本地管理（"匿名"/"隨機化"）MAC 地址的連線：

```ros
/interface/wifi/access-list/print detail
Flags: X - disabled
 0   mac-address=02:00:00:00:00:00 mac-address-mask=02:00:00:00:00:00 action=reject
```

為特定用戶端分配不同的 passphrase 可能很有用，例如你需要為某個用戶端提供無線接入，但不想共享無線密碼，或不想建立單獨的 SSID。當匹配的用戶端連線到此網路時，訪問列表會讓該用戶端使用不同的密碼，而不是介面配置中定義的密碼。只需確保該特定用戶端不會被更通用的訪問列表規則先行匹配即可。

或者拒絕所有未知 MAC 地址——可以作為最終規則新增到訪問列表末尾。——如果你只想允許特定用戶端接入網路，請務必也在 access-list 末尾新增一條 reject 規則，因為預設情況下並不存在隱式拒絕規則。

```ros
/interface/wifi/access-list
add action=accept disabled=no mac-address=22:F9:70:E5:D2:8E interface=wifi1 passphrase=StrongPassword
```

## 頻率掃描 {#frequency-scan}

`/interface/wifi/frequency-scan wifi1` 命令提供可用通道上射頻狀況的資訊，這些資訊可透過執行 frequency-scan 命令獲得。它用於估算頻譜使用情況，有助於找到不那麼擁擠的頻率。

![](/img/b57fb1af479c697c.png)

:::info
執行頻率掃描會斷開所有已連線的用戶端；如果介面處於 station 模式，則會斷開與 AP 的連線。
:::

## scan 命令 {#scan-command}

`/interface/wifi/scan` 命令會掃描接入點，並列印其檢測到的所有 AP 的資訊。它不會顯示每個通道的頻率使用情況，但會顯示所有正在傳送訊號的接入點。你可以使用 "connect" 按鈕發起與特定 AP 的連線。

scan 命令接受與 frequency-scan 命令相同的所有引數。
![](/img/296804ab8faca3df.png)

## 嗅探器 {#sniffer}

sniffer 命令會在無線介面上啟用監視模式。這會把介面變成所有 WiFi 傳輸的被動接收器。  
該命令會持續列印收到的封包資訊，並可將它們本地儲存為 pcap 檔案，或使用 TZSP 協定進行流式傳輸。

sniffer 會在所選介面配置的任一通道上工作。

![](/img/0ecc1c29a0286bab.png)

## 頻譜掃描 {#spectral-scan}

頻譜掃描可以掃描你的 wifi 介面所支援的頻率，並直接在控制檯中繪製出來。

:::info
頻譜掃描僅受 wifi-qcom 驅動支援；wifi-qcom-ac 驅動不支援。
:::

```ros
/interface/wifi/spectral-scan <wifiinterface name> range=
```

![](/img/cb53652d1a12ce6b.png)

該命令會持續監影片譜資料。此命令使用與 `spectral-history` 相同的資料來源，並共用許多引數。

要使用頻譜掃描，必須使用 `range=` 屬性。

每一行顯示一個頻譜圖分桶——頻率、幅度（dBm）、峰值，以及一個字元圖形條。圖形條用 ':' 字元表示功率值，用 '.' 字元表示平均峰值保持。

`data` - min/max/avg，預設使用平均值作為資料。大多數場景下應使用平均值，但在某些情況下 "min" 可用於檢查是否存在持續輸出恆定訊號的頻率。Max 表示在掃描間隔內檢測到的最強訊號，與峰值類似。  
`duration` - 在指定時間後終止命令。預設值為無限期；  
`freeze-frame-interval` - 更新命令輸出的時間間隔  
`interval` - 更新主要資料值（而非峰值）的間隔  
`peak-mode` - avg/max/disabled - 峰值反映 peak-hold-duration 期間的最強訊號。預設使用 "avg"。它是 "peak-hold-duration" 期間最大值的平均值。如果使用 "max"，則會顯示最高值，直到下一次 "peak-hold-duration" 更新。  
`peak-hold-duration` - 更改 peak-mode 使用的峰值保持時長，預設 5 秒。  
`range` - 掃描指定範圍，必填；  
`resolution` - 頻譜掃描的頻率步進  
`show-interference` - yes/no

可分類的干擾型別：

- 微波爐（`MWO`）。
- 連續波（`CW`）。
- WLAN（寬頻）（`WIFI`）。
- 無繩電話 2.4（`CORDLESS24`）。
- 無繩電話 5（`CORDLESS5`）。
- 藍牙（`BLUETOOTH`）。
- 跳頻擴頻（`FHSS`）。

## 頻譜歷史 {#spectral-history}

```ros
/interface/wifi/spectral-history <wifi interface name> range=
```

![](/img/407c01ab7a981996.png)

繪製頻譜圖。落在不同區間的功率值會以不同顏色、但前景色與背景色相同的字元列印，因此可以複製並貼上該命令的終端輸出。

`data` - min/max/avg，預設使用平均值作為資料。大多數場景下應使用平均值，但在某些情況下 "min" 可用於檢查是否存在持續輸出恆定訊號的頻率。Max 將顯示檢測到的最強訊號，而非平均訊號。  
`interv` - 更新資料值的間隔；  
`interval` - 列印頻譜圖行的間隔；  
`duration` - 在指定時間後終止命令。預設值為無限期；  
`range` - 掃描指定範圍，必填；  
`resolution` - 頻率步進；  
`show-interference` - yes/no

可分類的干擾型別：

- 微波爐（`O`）。
- 連續波（`C`）。
- WLAN（寬頻）（`W`）。
- 無繩電話 2.4（`T`）。
- 無繩電話 5（`T`）。
- 藍牙（`BB`）。
- 跳頻擴頻（`F`）。

## WPS {#wps}

### WPS 用戶端 {#wps-client}

wps-client 命令可用於從啟用了 WPS 的 AP 獲取認證資訊。

```ros
/interface/wifi/wps-client/wifi1
```

### WPS 伺服器 {#wps-server}

執行以下命令，可使 AP 在 2 分鐘內接受用戶端裝置的 WPS 認證。

```ros
/interface/wifi/wps-push-button wifi1
```

## 射頻 {#radios}

執行 `/interface/wifi/radio/print detail` 命令可以獲取每個 radio 的能力資訊。它有助於檢視介面支援哪些頻段以及可以選用哪些通道。應用於介面的國家配置檔案會影響結果。

```ros
/interface/wifi/radio/print detail 
Flags: L - local 
 0 L radio-mac=48:A9:8A:0B:F7:4A phy-id=0 tx-chains=0,1 rx-chains=0,1 
     bands=5ghz-a:20mhz,5ghz-n:20mhz,20/40mhz,5ghz-ac:20mhz,20/40mhz,20/40/80mhz,5ghz-ax:20mhz,
      20/40mhz,20/40/80mhz 
     ciphers=tkip,ccmp,gcmp,ccmp-256,gcmp-256,cmac,gmac,cmac-256,gmac-256 countries=all 
     5g-channels=5180,5200,5220,5240,5260,5280,5300,5320,5500,5520,5540,5560,5580,5600,5620,5640,5660,
            5680,5700,5720,5745,5765,5785,5805,5825 
     max-vlans=128 max-interfaces=16 max-station-interfaces=3 max-peers=120 hw-type="QCA6018" 
     hw-caps=sniffer interface=wifi1 current-country=Latvia 
     current-channels=5180/a,5180/n,5180/n/Ce,5180/ac,5180/ac/Ce,5180/ac/Ceee,5180/ax,5180/ax/Ce,
                 5180/ax/Ceee,5200/a,5200/n,5200/n/eC,5200/ac,5200/ac/eC,5200/ac/eCee,5200/ax...
                 ...5680/n/eC,5680/ac,5680/ac/eC,5680/ax,5680/ax/eC,5700/a,5700/n,5700/ac,5700/ax 
     current-gopclasses=115,116,128,117,118,119,120,121,122,123 current-max-reg-power=30 
```

Radio 資訊能告訴我們所支援的通道寬度，但也可以從產品頁面推斷出這一資訊。為此，你需要檢視以下引數：**鏈數量**、**最大資料速率**。瞭解這些引數後，你需要檢視調製與編碼方案（MCS）表，例如這裡：[https://mcsindex.com/](https://mcsindex.com/)。

以 hAP ax <sup>2</sup> 為例，可以看到鏈數量為 2，最大資料速率在 MCS 表中為 1200 - 1201。在 MCS 表中我們需要找到 2 條空間流（鏈）的條目及相應的資料速率，本例中這表明 80MHz 是支援的最大通道寬度。

## 登錄檔 {#registration-table}

`/interface/wifi/registration-table/` 顯示已連線的無線用戶端列表及其詳細資訊。

![](/img/0a33a5fa049e4b23.png)

### 去認證 {#de-authentication}

可以透過將無線對端從登錄檔中移除，手動對其去認證（強制重新關聯）。

```ros
/interface/wifi/registration-table/remove [find where mac-address=02:01:02:03:04:05]
```

## WiFi CAPsMAN {#wifi-capsman}

新 WiFi 選單的 CAPsMAN（受控接入點系統管理器，Controlled Access Point system Manager）讓你可以從中央控制器把無線設定應用到眾多 MikroTik WiFi AP。參見專門頁面：[WiFi CAPsMAN](./capsman.md)。

## 高階示例 {#advanced-examples}

[使用 User Manager v5 的企業級無線安全](../user-guides/enterprise-wireless-security-user.md)

## 替換 'wireless' 包 {#replacing-wireless-package}

一些 MikroTik Wi-Fi 5 AP 出廠時其介面由 'wireless' 選單管理，它們可以用 'wifi-qcom-ac' 包替換 'wireless' 包，從而讓介面改由 'wifi' 選單管理。

為此，需要先解除安裝 'wireless' 包，然後安裝 'wifi-qcom-**ac**'。

:::info
請注意，"wifi-qcom-ac" 驅動對資源的要求高得多。使用新包時可用 RAM 會更少，這一點需要留意。
:::

### 相容性 {#compatibility}

wifi-qcom-**ac** 包為 IPQ4018/4019 和 QCA9984 radio 提供了替代驅動，使其與 WiFi 配置選單相容。關於可能的 wifi-qcom-ac/wifi-qcom/wireless 包組合，請參見[此處](../index.md)的包型別部分。

一般來說，該包與採用 ARM CPU 的 802.11ac 產品相容。它**不**相容我們任何採用 MIPS CPU 的 802.11ac 產品。

| 相容性 | 裝置 |
| :-- | :-- |
| 相容 | Audience, Audience LTE kit, Chateau（D53 的所有變體）, hAP ac<sup>2</sup>, hAP ac<sup>3</sup>, cAP ac, cAP XL ac, LDF 5 ac, LHG XL 5 ac, LHG XL 52 ac, NetMetal ac<sup>2</sup>, mANTBox 52 15s, wAP ac (RBwAPG-5HacD2HnD), SXTsq 5 ac |
| 不相容 | RB4011iGS+5HacQ2HnD-IN（不支援 2.4GHz 介面）, Cube 60Pro ac（不支援 60GHz 介面）, wAP ac (RBwAPG-5HacT2HnD) 以及**所有其他採用 MIPSBE CPU 的裝置** |

### 優勢 {#benefits}

- WPA3 認證和 OWE（機會性無線加密）。
- 802.11w 標準管理幀保護。
- 802.11r/k/v。
- MU-MIMO 和波束成形。
- IPQ4019 介面在 2.4GHz 頻段的最大資料速率為 400Mb/s。

:::info
這些優勢同時適用於 wifi-qcom 和 wifi-qcom-ac 包。
:::

### 失去的功能 {#lost-features}

在 802.11ac 產品上執行相容 'wifi' 管理介面的驅動時，會失去以下顯著功能：

- Nstreme 和 Nv2 無線協定。
- 無線設定中的 VLAN 配置（按介面的 VLAN 可在 bridge 設定中配置）。
- 與 'wireless' 包中所實現的 station-bridging 的相容性。Station-bridge 只能在同一型別的驅動之間工作。WiFi 到 WiFi，以及 [無線](../index.md) 到 Wireless。

## 屬性參考 {#property-reference}

### AAA 屬性 {#aaa-properties}

此類別中的屬性用於配置接入點與 AAA（RADIUS）伺服器的互動。

下表中的某些引數以 *format-string* 作為其值。在 *format-string* 中，某些字元按以下方式解釋：

| 字元 | 解釋 |
| :-- | :-- |
| a | 構成用戶端裝置 MAC 地址的十六進位制字元，小寫 |
| A | 構成用戶端裝置 MAC 地址的十六進位制字元，大寫 |
| i | 構成 AP 介面 MAC 地址的十六進位制字元，小寫 |
| I（大寫 'i'） | 構成 AP 介面 MAC 地址的十六進位制字元，大寫 |
| N | AP 介面的完整名稱（例如 'wifi1'） |
| S | 完整的 SSID |

所有其他字元均按原樣使用，不做任何解釋。示例請參見預設值。

| 屬性 | 描述 |
| :-- | :-- |
| **called-format** (*format-string*; *Default: **II-II-II-II-II-II:S**)* | AP 發往 RADIUS 伺服器的報文中，Called-Station-Id RADIUS 屬性值的格式。 |
| **calling-format** (*format-string*; *Default: **AA:AA:AA:AA:AA:AA**)* | AP 發往 RADIUS 伺服器的報文中，Calling-Station-Id RADIUS 屬性值的格式。 |
| **interim-update** (*time interval; Default: ****5m****)* | 向 RADIUS 伺服器傳送流量計費臨時更新的間隔。 |
| **mac-caching** (*time interval;* *Default: **disabled**)* | 啟用 MAC 地址認證時，快取 RADIUS 伺服器回覆的時長。這可以解決因 RADIUS 伺服器回覆延遲相對較高而導致用戶端裝置認證超時的問題。 |
| **name** (*string*; *Default: **no**)* | AAA 配置檔案的唯一名稱。 |
| **nas-identifier** (*string*) | AP 發往 RADIUS 伺服器的訊息中 NAS-Identifier 屬性的值。預設為裝置的主機名（/system/identity）。 |
| **password-format** (*format-string*) | 執行 MAC 地址認證時，用於計算 AP 發往 RADIUS 伺服器的訊息中 User-Password 屬性值的格式。 <br/> 預設值：""（空字串）。 |
| **username-format** (*format-string*; *Default: **AA:AA:AA:AA:AA:AA**)* | 執行 MAC 地址認證時，AP 發往 RADIUS 伺服器報文中 User-Name 屬性值的格式。 |

### 通道屬性 {#channel-properties}

此類別中的屬性指定所需的無線通道。

| 屬性 | 描述 |
| :-- | :-- |
| **band** (*2ghz-g* \| *2ghz-n* \| *2ghz-ax*\| *2ghz-be* \| *5ghz-a* \| *5ghz-ac* \| *5ghz-an* \| *5ghz-ax* \| *5ghz-be*\| *6ghz-ax* \| *6ghz-be*) | AP 將使用的頻段和無線標準。預設為支援的最新標準。<strong>請注意，頻段支援受無線射頻能力限制。</strong><br/> |
| **deprioritize-unii-3-4** (*no* \| *yes*) | 是否將控制頻率為 5720 或 5825-5885 MHz 的通道分配較低優先順序。某些用戶端裝置不支援這些通道，因此不希望自動選擇它們。在 ETSI 監管域中預設為“yes”，其他地區預設為“no”。 <br/> |
| **frequency** (*list of numbers or number ranges*) | 對於處於 AP 模式的介面，指定在選擇控制通道中心頻率時要考慮的頻率（單位 MHz）。 <br/> 對於處於 station 模式的介面，指定用於掃描 AP 的頻率。 <br/> 保持未設定（預設）以考慮無線射頻支援且適用監管配置檔案允許的所有頻率。 <br/> 該引數可包含 1 個或多個以逗號分隔的十進位制數值，或可選地包含使用語法 RangeBeginning-RangeEnd:RangeStep 表示的數字範圍 <br/> 有效的 channel.frequency 值示例： <br/><ul><li>2412</li><li>2412,2432,2472</li><li>5180-5240:20,5500-5580:20</li></ul> |
| **preamble-puncturing** (*no \| yes; Default: **no***) |  在此介面上為 DFS/雷達啟用打孔（puncturing）支援（僅 802.11be）。設定後，當檢測到雷達訊號時，接入點可以只停用（"打孔"）寬 80/160 MHz 通道中受影響的 20 MHz 部分，而不是切換整個通道。對於 80 MHz 通道，可以打孔單個 20 MHz 子通道。對於 160 MHz 通道，可以打孔一個 20 MHz 子通道或一個 40 MHz 塊。  當前打孔狀態可在該介面的 `/interface/wifi/monitor` 輸出中檢視，其中被打孔的子通道用字母 `o` 標記。  |
| **reselect-interval** (*time interval; Default: **disabled***) | 指定介面應執行"重新掃描通道可用性"並選擇最合適通道的間隔。指定該間隔將允許系統動態且隨機地選擇此間隔。這有助於避免多個 AP 同時掃描網路、選擇同一通道並同時偏好使用它的情況。reselect-interval 使用後臺掃描。重新選擇過程會綜合考慮通道中的網路數量、通道使用情況以及與相鄰通道中網路的重疊，從而選擇最合適的通道。它可用於已定義了頻率列表的情況，也可在未設定 `frequency` 時使用所有受支援的頻率。示例：01:00..01:30 → 會將通道重新掃描設定為每 1 小時 + 最多 30 分鐘隨機時間執行一次。第一次可能在"1 小時 15 分鐘"後執行，之後可能是"1 小時 1 秒"，再之後可能是"1 小時 29 分 59 秒"……隨機地，重新掃描會在每 1 小時到 1 小時 30 分鐘之間發生。 |
| **reselect-time** (*time interval; Default: **disabled***) | 指定介面應執行"重新掃描通道可用性"並選擇最合適通道的時鐘時間。指定該時鐘時間將允許系統動態且隨機地選擇此時間。這有助於避免多個 AP 同時掃描網路、選擇同一通道並同時偏好使用它的情況。reselect-time 使用後臺掃描。重新選擇過程會綜合考慮通道中的網路數量、通道使用情況以及與相鄰通道中網路的重疊，從而選擇最合適的通道。它可用於已定義了頻率列表的情況，也可在未設定 `frequency` 時使用所有受支援的頻率。示例：01:00..01:30 → 會將通道重新掃描設定為每晚一次，在系統時鐘時間 01:00 AM 到 01:30 AM 之間隨機執行。14:00..14:30 → 會將通道重新掃描設定為每天（午後）一次，在系統時鐘時間 14:00:00 到 14:30:00（即下午 2 點到 2 點半）之間隨機執行。 |
| **secondary-frequency** (*list of integers* \| *Default: **disabled***) | 對於 80+80MHz 分離通道，指定輔助 80MHz 段允許的中心頻率。對於 320MHz 通道，指定允許的 320MHz 通道中心。未設定（預設）時不限制通道選擇。例如 'width=20/40/80+80mhz frequency=5180' 允許將通道 42 與任何其他受支援的 80MHz 通道組合。'width=20/40/80+80mhz frequency=5180 secondary-frequency=5530' 僅允許組合通道 42 和 106。'width=20/40/80/160/320mhz frequency=6115' 允許使用通道 31 或 63。'width=20/40/80/160/320mhz frequency=6115 secondary-frequency=6265' 僅允許使用通道 63。有效的 [5GHz](https://en.wikipedia.org/wiki/List_of_WLAN_channels#5_GHz_(802.11a/h/n/ac/ax/be)) 和 [6GHz](https://en.wikipedia.org/wiki/List_of_WLAN_channels#6_GHz_(802.11ax_and_802.11be)) 通道列表見此處。 |
| **skip-dfs-channels**  (*10min-cac* \| *all* \| *disabled; Default: **disabled***) | 是否避免使用需要執行通道可用性檢查（偵聽雷達訊號是否存在）的通道。10min-cac - 介面將避免使用需要 10 分鐘 CAC 的通道；all - 介面將避免使用所有需要 CAC 的通道；disabled - 介面可以選擇任何受支援的通道，無論 CAC 要求如何 |
| **width** ( *20mhz* \| *20/40mhz* \| *20/40mhz-Ce* \| *20/40mhz-eC* \| *20/40/80mhz* \| *20/40/80+80mhz* \| *20/40/80/160mhz*\| *20/40/80/160/320mhz*) | 無線通道寬度。預設為無線射頻硬體支援的最寬通道。 |

### 配置屬性 {#configuration-properties}

本節包含與介面及相關 radio 執行有關的屬性。

| 屬性 | 描述 |
| :-- | :-- |
| **antenna-gain** (*integer 0..30*) | 覆蓋預設天線增益。每個無線射頻的 <em>master</em> 介面為使用同一無線射頻的每個介面設定天線增益。 <br/> 此設定不能將天線增益覆蓋為低於無線射頻的最小天線增益。無預設值。 <br/> |
| **beacon-interval** (*time interval 100ms..1s; default: **100ms***) | AP 信標幀之間的間隔。🛈 **重要：** 802.11 標準以*時間單位*（1 TU = 1.024 ms）定義信標間隔。每配置 1 ms，實際信標間隔即為 1 TU。⚠️ **警告：** 在同一 radio 上執行的所有 AP（即 master AP 及其所有"虛擬"/"從屬"AP）必須使用相同的信標間隔。  |
| **chains** (*list of integer 0..7* ) | 用於接收訊號的[射頻鏈](https://en.wikipedia.org/wiki/RF_chain)。預設為對應無線射頻硬體可用的所有鏈。 |
| **country** (*name of a country; default: **Latvia***) | 決定介面應用哪些監管域限制。⚠️ **警告：** 正確設定此值以符合當地法規並確保與其他裝置的互操作性非常重要。  在受控環境中，或如果你所在地區有特殊許可，可以選擇 `country=Superchannel`（使用此國家配置檔案時，路由器的發射輸出功率不受軟體限制，路由器會輸出其硬體晶片允許的最大功率，除非透過手動 `tx-power` 將其調低）。對 **wifi-qcom-ac** 驅動無效。 |
| **distance** () | 最大鏈路距離（公里），需要為遠距離室外鏈路設定。該值應反映距離裝置最遠的 AP 或 station 的距離。未配置該值時允許使用 2 km 鏈路。⚠️ **警告：** wifi-qcom-ac 包不使用 `distance`。將 `distance` 設定為高於實際需要的值可能對吞吐量和延遲產生不利影響。  |
| **dtim-period** (*integer 1..255; default: **1***) | DTIM 是信標幀的一部分，用於通知節能（休眠）station 有即將到來的組播和廣播流量。該設定配置當 AP 上連線有處於節能模式的用戶端裝置時，傳送組播或廣播流量的週期。以信標間隔的倍數表示（例如使用預設值 `dtim-period=1` 和 `beacon-interval=100ms` 時，每 1 x 100 ms = 100 ms 傳送一次）。較高的值讓用戶端裝置節省更多能量，但會增加網路延遲。較低的值讓用戶端更頻繁地喚醒，消耗更多能量。 |
| **hide-ssid** (*no \| yes; default: **no***) | yes - AP 不在信標幀中包含其 SSID，也不回覆具有廣播 SSID 的探測請求。no - AP 在信標幀中包含其 SSID，並回復具有廣播 SSID 的探測請求。 |
| **hw-protection-mode** (*cts-to-self* \| none \| *rts-cts)* | 為減少幀衝突，可以使用： <br/><ul><li><em>cts-to-self</em> - 介面在傳送 MPDU 之前向自己的地址傳送 CTS 幀（以通知附近裝置推遲相互通訊）；</li><li><em>none </em> - 介面不使用任何硬體保護機制；</li><li><em>rts-cts -</em> 介面在每個 MPDU 之前傳送 RTS 幀（RTS 之後是來自接收方的 CTS，通訊在此之後進行——RTS 和 CTS 幀都可推遲其他裝置）；</li></ul> 預設（未設定）：介面在重傳的 MPDU 之前傳送 RTS 幀。 |
| **installation** (*indoor*\|*outdoor*; *default*: **indoor**) | 安裝在室外的裝置將避免使用僅限室內的無線通道。 |
| **manager** (*capsman* \|*capsman-or-local* \| *local*; default: **local**) | capsman - 介面僅作為 CAP 工作；此選項**不應**透過 provisioning 規則傳遞給 CAP  capsman-or-local - 介面將透過 CAPsMAN 獲取配置，如果未啟用 `/interface/wifi/cap`，則使用自身配置。  local - 介面不會聯絡 CAPsMAN 獲取配置。 |
| **max-clients** (*integer 1..1000; default: **1000**)* | 關聯用戶端的最大數量。 |
| **mode** (*ap* \| *station*) | 介面操作模式 <br/><ul><li><em>ap</em>（預設）- 介面作為接入點執行</li><li><em>station</em> - 介面充當用戶端裝置，掃描通告已配置 SSID 的接入點</li><li>station-bridge - 介面充當用戶端裝置並啟用對 4 地址幀格式的支援，以便該介面可用作橋接埠</li><li>station-pseudobridge - 介面跟蹤出站 IP 連線，並執行 MAC 地址轉換，其方式類似於 IP 偽裝的工作方式</li></ul><br/>🛈 <strong>重要：</strong> 'wifi' station-bridge 模式與執行較舊 'wireless' 軟體包的 AP 不相容，反之亦然。 <br/><br/> |
| **multicast-enhance** (*enabled*\| *disabled; default: **disabled***) | 啟用 multicast-enhance 功能後，AP 會把每個組播地址的 IP 或 IPv6 封包轉換為面向每個已連線 station 的多個單播地址幀。這可以提升鏈路吞吐量和可靠性，因為與組播幀不同，單播幀會被 station 確認並以更高的資料速率傳送。 |
| **qos-classifier** (*dscp-high-3-bits*\| *priority; default: **priority***) | 指定遵循哪套 WMM 規則集。AP 和用戶端根據分配給封包的優先順序（按 WMM 規範）進行分類 → 1,2 - 背景；0,3 - 盡力而為；4,5 - 影片；6,7 - 語音。"更好"的接入類別獲得通道訪問權的機率更高（例如語音幀在通道變為"空閒"後的"退避"時間更短，從而更可能比"較差"類別的幀更早傳送）。dscp-high-3-bits - 介面將使用等於 IP DSCP 欄位最高 3 位值的 WMM 優先順序傳送封包；priority - 介面將使用由 IP firewall 或 bridge filter 設定的 WMM 優先順序傳送封包。🛈  **重要：** 802.11ac 無線晶片組不支援 dscp-high-3-bits 分類器模式。對於 802.11ac 介面，請參見 [DSCP from priority](https://en.wikipedia.org/wiki/RF_chain)。     |
| **ssid** *(string; default: **no**)* | 無線網路的名稱，即 (E)SSID。 |
| **station-roaming** *(no \| yes; Default: **no**)* | 執行在 station 或 station-bridge 模式的 Wifi 介面會定期掃描可漫遊的候選 AP。到 AP 的訊號越弱，掃描越頻繁。如果發現訊號更好的 AP，station 會漫遊到它。支援 FT，並且如果啟用了 `steering.wnm`，station 會響應 BSS Transition Request。 |
| **tx-chains** (*list of integer 0..7*) | 用於傳送訊號的[射頻鏈](https://en.wikipedia.org/wiki/RF_chain)。預設為對應無線射頻硬體可用的所有鏈。 |
| **tx-power** (*integer 0..40*) | 介面發射功率（單位 dBm）的限制。不能用於將功率設定為高於監管配置檔案規定的限制。預設未設定。 |

### Datapath 屬性 {#datapath-properties}

與向無線用戶端裝置轉發封包及從其接收封包有關的引數。

| 屬性 | 描述 |
| :-- | :-- |
| **bridge** (*bridge interface*) | 要將介面作為橋接埠新增到的橋接介面。虛擬（“從屬”）介面預設會新增到與對應主介面相同的橋接（如果有）。主介面預設不會新增到任何橋接。 |
| **bridge-cost** (*integer; default: **10***) | 作為 bridge 埠新增時使用的 bridge 埠開銷。 |
| **bridge-horizon** (*none* \| *integer; default: **none**)* | 作為 bridge 埠新增時使用的 bridge horizon。 |
| **client-isolation** (*no* \| *yes; default: **no***) | 決定連線到此介面的用戶端裝置是否（預設）與其他用戶端隔離。該策略可以透過訪問列表規則按用戶端覆蓋，因此一個 AP 可以同時有隔離和非隔離的用戶端。來自隔離用戶端的流量不會被轉發給其他用戶端，來自非隔離用戶端的單播流量也不會被轉發給隔離用戶端。 |
| **interface-list** (*interface list; default: **no***) | 要將介面作為成員新增到的列表。 |
| **traffic-processing** (*on-cap \| on-capsman \| on-capsman-secure*) | 🛈  **重要：** 此設定僅從 **7.21beta2** 版本開始可用。  <code>on-cap</code>，會讓 CAP 自身負責處理所有 WiFi 流量（與任何獨立 AP 相同）；<code>on-capsman</code>，會讓 CAP 的 WiFi 流量被轉發到通往 CAPsMAN 的偽隧道，由 CAPsMAN 負責 CAP 的流量處理；<code>on-capsman-secure</code>，會讓 CAP 的 WiFi 流量被轉發到通往 CAPsMAN 的加密偽隧道，由 CAPsMAN 負責 CAP 的流量處理。 🛈  **重要：** 使用 `traffic-processing=on-capsman` 設定時請注意，由於 CAP 的所有 WiFi 流量現在都由 CAPsMAN 處理（被推入 CAPsMAN），會增加 CAPsMAN 的資源消耗（CPU 和 RAM 使用）。     |
| **vlan-id** (none \| integer 1..4095; default: **none**) | 分配給連線到此介面的用戶端裝置的預設 VLAN ID（僅與 AP 模式下的介面相關）。當為用戶端分配了 VLAN ID 時，來自該用戶端的流量會自動打上該 ID 標記，並且只有帶此 ID 標記的封包才會被轉發給該用戶端。  ⚠️ **警告：** 802.11ac 晶片組不支援這種型別的 VLAN 標記，但可以在 bridge 設定中將它們[配置](../../bridging-and-switching/index.md#vlan-example-trunk-and-access-ports)為 VLAN 接入埠。  |

### 安全屬性 {#security-properties}

與認證有關的引數。

| 屬性 | 描述 |
| :-- | :-- |
| **authentication-types** （*wpa-psk、wpa2-psk、wpa2-psk-sha2、wpa-eap、wpa2-eap、wpa3-psk、owe、wpa3-eap、wpa3-eap-192 的列表*） | 要在介面上啟用的認證型別。 <br/> 預設值為空列表（不進行認證，開放網路）。 <br/> 配置 passphrase 會將 <em>wpa2-psk</em> 認證方法新增到預設列表（如果介面是 AP），或將 <em>wpa-psk</em> 和 <em>wpa2-psk</em> 兩者都新增（如果介面是 station）。 <br/> 配置 <em>eap-username</em> 和 <em>eap-password</em> 會將 <em>wpa-eap 和 wpa2-eap</em> 認證方法新增到預設列表。 |
| **beacon-protection** (*disabled*\| *enabled*) | 是否啟用信標完整性保護。支援情況取決於“beacon-protection”無線射頻能力。 <br/> 對 802.11be 介面預設啟用。 |
| **connect-group** ( *string*) | 同一 connect group 內的 AP 不允許超過 1 個具有相同 MAC 地址的用戶端裝置。這是為了防止惡意的授權使用者攔截髮往其他使用者的流量（“MacStealer”攻擊），或透過偽造受害者的 MAC 地址執行拒絕服務攻擊。 <br/> 對具有重複 MAC 地址的新連線的處理取決於所涉及 AP 介面的 connect-priority。 <br/> 預設情況下，所有 AP 都分配相同的 connect-group。 |
| **connect-priority** (accept-priority/hold-priority (*integers*)) | 這些引數決定當用戶端裝置的 MAC 地址與到另一個 AP 的另一活動連線相同如何處理連線。 <br/>如果（AP2 的 accept-priority） &lt; （AP1 的 hold-priority），到 AP2 的連線將導致用戶端從 AP1 斷開。<br/> 如果（AP2 的 accept-priority） = （AP1 的 hold-priority），僅當無法再透過 AP1 訪問該 MAC 地址時，才允許到 AP2 的連線。<br/> 如果（AP2 的 accept-priority） &gt; （AP1 的 hold-priority），到 AP2 的連線將不被接受。 <br/><br/> 如果省略，hold-priority 與 accept-priority 相同。預設情況下，執行使用者認證的 AP 比開放 AP 具有更高優先順序（更低的整數值）。 |
| **dh-groups** (*list of 19, 20, 21*) | 在 SAE（WPA3）認證中使用的[橢圓曲線密碼學群組](http://www.iana.org/assignments/ipsec-registry/ipsec-registry.xhtml#ipsec-registry-10)識別符號。 |
| **disable-pmkid** （*no* \| *yes；預設：**no***） | 對於處於 AP 模式的介面，禁止在 EAPOL 幀中包含 PMKID。停用 PMKID 可能導致使用它的用戶端裝置出現相容性問題。<ul><li><em>yes</em> - 不要在 EAPOL 幀中包含 PMKID。</li><li><em>no</em> - 在 EAPOL 幀中包含 PMKID。</li></ul> |
| **eap-accounting** （*no* \| *yes；預設：**no***） | 向 RADIUS 伺服器傳送透過 EAP 認證的對等端的計費資訊。 <br/><br/>⚠️ <strong>警告：</strong> 與 EAP 相關的屬性僅與處於 station 模式的介面相關。AP 會將 EAP 認證委託（透傳）給 RADIUS 伺服器。 <br/> |
| **eap-anonymous-identity** （*字串；預設：**none***） | 用於 EAP 外部認證的可選匿名身份。 |
| **eap-certificate-mode** （*dont-verify-certificate* \| *no-certificates* \| *verify-certificate* \| *verify-certificate-with-crl*；預設：**dont-verify-certificate***） | 處理 RADIUS 伺服器 TLS 證書的策略。 <br/><ul><li>verify-certificate - 要求伺服器具有有效證書。檢查該證書是否由受信任的證書頒發機構簽名。</li><li>dont-verify-certificate - 不對證書執行任何檢查。</li><li>no-certificates - 嘗試透過執行匿名 Diffie-Hellman 金鑰交換來建立 TLS 隧道。在 RADIUS 伺服器完全沒有證書時使用。</li><li>verify-certificate-with-crl - 與 <em>verify-certificate</em> 相同，但還會透過檢查證書吊銷列表來驗證證書是否有效。</li></ul> |
| **eap-methods** (*list of* *peap, tls, ttls*) | 認證時要考慮的 EAP 方法。預設為所有支援的方法。 |
| **eap-password** （*字串；預設：**none***） *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 當所選 EAP 方法需要密碼時使用的密碼。 |
| **eap-tls-certificate** （*證書；預設：**none***） | 當所選 EAP 認證方法需要證書時，要使用的裝置證書儲存中的證書名稱或 id。 |
| **eap-username** （*字串；預設：**none***） | 當所選 EAP 方法需要使用者名稱時使用的使用者名稱。 <br/><br/>⚠️ <strong>注意：</strong> 配置加密密碼時請務必小心。 <br/> 所有用戶端裝置都必須支援 AP 用於連線的組加密密碼，並且某些用戶端裝置（尤其是 Intel® 8260）如果單播密碼列表中包含它們不支援的任何密碼，也會無法連線。 <br/> |
| **encryption** （*ccmp、ccmp-256、gcmp、gcmp-256、tkip 的列表；預設：**ccmp***） | 用於加密單播流量所支援的密碼列表。 <br/> 預設為 <em>ccmp</em>。 <br/><br/>⚠️ <strong>警告：</strong> 為了讓用戶端裝置在兩個 AP 之間成功漫遊，這些 AP 需要由同一個 RouterOS 例項管理。有關如何集中管理多個 AP 的資訊，請參閱 [CAPsMAN](./capsman.md)<br/> |
| **ft** （*no \| yes：預設：**no***） | 是否啟用 802.11r 快速 BSS 轉換（漫遊）。 |
| **ft-mobility-domain** （*0..65535 的整數；預設：**44484 (0xADC4)***） | 快速 BSS 轉換移動域 ID。 |
| **ft-nas-identifier** (string of *2..96 hex characters*) | 快速 BSS 轉換 PMK-R0 金鑰持有者識別符號。預設：介面的 MAC 地址。 |
| **ft-over-ds** （*no* \| *yes*；預設：**no***） | 是否啟用透過 DS（分散式系統）的快速 BSS 轉換。 |
| **ft-preserve-vlanid** (*no* \| *yes* ) | no - 當用戶端透過 802.11r 快速 BSS 轉換連線到此 AP 時，會根據接入和/或介面設定為其分配 VLAN ID；yes（預設）- 當用戶端透過 802.11r 快速 BSS 轉換連線到此 AP 時，會保留其在初始認證期間分配的 VLAN ID。當依賴 RADIUS 伺服器為使用者分配 VLAN ID 時，預設行為至關重要，因為 RADIUS 伺服器只用於初始認證。 |
| **ft-r0-key-lifetime** （*時間間隔 1s..6w3d12h15m；預設：**600000s (~7 days)***） | 快速 BSS 轉換 PMK-R0 加密金鑰的生命週期。 |
| **ft-reassociation-deadline** （*時間間隔 0..70s；預設：**20s***） | 快速 BSS 轉換重新關聯截止時間。 |
| **group-encryption** （*ccmp* \| *ccmp-256* \| *gcmp* \| *gcmp-256* \| *tkip*；預設：**ccmp***） | 用於加密組播流量的密碼。 |
| **group-key-update** （*時間間隔；預設：**24 hours***） | 組臨時金鑰（用於加密廣播流量的金鑰）的更新間隔。 |
| **management-encryption** （*cmac* \| *cmac-256* \| *gmac* \| *gmac-256*；預設：**cmac***） | 用於加密受保護管理幀的密碼。 |
| **management-protection** （*allowed* \| *disabled* \| *required*） | 是否使用 802.11w 管理幀保護。<strong>與 standard wireless package 中的管理幀保護不相容</strong>。 <br/> 預設值取決於所選認證型別的值。WPA2 允許使用管理保護，WPA3 則要求使用。 |
| **multi-passphrase-group** (*string*) | 要使用的 `/interface/wifi/security/multi-passphrase/` 組名稱。在安全配置檔案下只能定義一個組。 |
| **owe-transition-interface** (*interface* \| *auto*) | 執行在 OWE 轉換模式時，要通告其 MAC 地址和 SSID 作為匹配 AP 的介面名稱。 <br/> 將值設定為 'auto' 將使 RouterOS 嘗試自動匹配同一無線射頻上的開放 AP 和 OWE AP。 <br/> 設定提供 OWE 但也適用於不支援該標準的較舊裝置的開放 AP 所必需。請參閱<a href="#open-ap-with-owe-transition-mode">上面的配置示例</a>。 |
| **passphrase** (*string of up to 63 characters*) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於 PSK 認證型別的密碼短語。預設為空字串 - ""。 <br/> WPA-PSK 和 WPA2-PSK 認證要求至少 8 個字元，而 WPA3-PSK 沒有最小密碼短語長度要求。 |
| **sae-anti-clogging-threshold** （*disabled* \| *整數；預設：**5***） | 由於 SAE（WPA3）關聯會消耗大量 CPU 資源，用虛假認證請求淹沒 AP 會構成一種可行的拒絕服務攻擊。 <br/> 此引數提供了一種緩解此類攻擊的方法：指定正在進行中的 SAE 認證閾值，達到該閾值後，AP 將開始要求用戶端裝置在其認證請求中包含繫結到其 MAC 地址的 cookie。之後，它將僅處理包含有效 cookie 的認證請求。 |
| **sae-max-failure-rate** （*disabled* \| *整數；預設：**40***） | 每分鐘失敗的 SAE（WPA3）關聯速率，達到該速率後，AP 將停止處理新的關聯請求。 |
| **sae-pwe** （*both* \| *hash-to-element* \| *hunting-and-pecking；預設：**both***） | 用於派生 SAE 密碼元素所支援的方法。 |
| **wps** （*disabled* \| *push-button；預設：**push-button***） | <ul><li><em>push-button</em> - 在呼叫 'wps-push-button' 命令後，AP 將在 2 分鐘內接受 WPS 認證。物理 WPS 按鈕功能尚未實現。</li><li><em>disabled </em> - AP 將不接受 WPS 認證</li></ul> |

### 安全 multi-passphrase 屬性 {#security-multi-passphrase-properties}

`/interface/wifi/security/multi-passphrase`

`multi-passphrase` 允許使用 PPSK——私有預共享金鑰。
可以透過建立訪問列表條目並設定 `multi-passphrase-group` 名稱來使用，也可以將組分配給介面所使用的安全配置檔案。

支援的 passphrase 總上限為 10000。該上限在所有介面之間共享。當介面關聯了 multi-passphrase 組時，啟用後它會開始快取指定組中的所有 passphrase。快取進行期間，認證會變慢。快取完成後，使用 multi-passphrase 組就不會再帶來可感知的額外延遲。

如果使用訪問列表來應用 `multi-passphrase-group`，快取將在首次匹配到該組時開始，並持續到找到匹配的 passphrase 為止。

如果單個組下可能有成千上萬個 passphrase 條目，則快取可能需要幾分鐘才能完成，具體取決於裝置配置和型號。

:::info
multi-passphrase 不支援 WPA3-PSK 認證型別。
:::

| 屬性 | 描述 |
| :-- | :-- |
| **group** (*string*) | 將組分配給安全配置檔案或訪問列表後，即可使用該組下定義的所有密碼短語 |
| **passphrase** (*string of up to 63 characters*) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於 PSK 認證型別的密碼短語。多個使用者可以使用同一個密碼短語。 <br/> 與 WPA3-PSK 不相容。 |
| **vlan-id** (*integer 0..4095; Default: **none***) | 將分配給使用此 passphrase 的用戶端的 vlan-id   ⚠️ **注意：** 僅在 wifi-qcom 介面上受支援。如果 wifi-qcom-ac AP 有用戶端使用帶有關聯 vlan-id 的 passphrase，該用戶端將無法加入。 |
| **expires** (*date and time*; "YYYY-MM-DD HH:SS") | 此條目中指定的密碼短語的過期日期和時間，不影響整個組。一旦到達該日期，使用此密碼短語的現有用戶端將被斷開連線，新用戶端將無法使用該密碼短語連線。如果未設定，則該密碼短語可以無限期使用。 |
| **isolation** (*yes* \| *no*; Default: **no**) | 決定使用此 passphrase 的用戶端裝置是否與 AP 上的其他用戶端隔離。來自隔離用戶端的流量不會被轉發給其他用戶端，來自非隔離用戶端的單播流量也不會被轉發給隔離用戶端。 |
| **disabled**（*yes* \| *no*；預設：**no**） |  |

### Steering 屬性 {#steering-properties}

:::info
非請求式 802.11v BSS 轉換管理請求功能從 7.21 起受支援。
:::

此類別中的屬性管理向用戶端裝置通告潛在漫遊候選的機制。

| 屬性 | 描述 |
| :-- | :-- |
| **2g-probe-delay**(*no* \| *yes*; Default: *no*) | 如果在 2.4GHz AP 上將此屬性設定為 yes，且該 AP 與至少一個 5GHz AP 位於同一個 steering neighbor 組中，則該 2.4GHz AP 將在 60 秒間隔內，不響應來自每個用戶端的、信噪比大於 35 dB 的前 3 個探測請求。  |
| **neighbor-group** (*string*) | 在傳送鄰居報告和 BSS 轉換管理請求時，AP 會將其鄰居組內的所有其他 AP 列為潛在的漫遊候選。 <br/> 預設情況下，會為每組具有相同 SSID 和認證設定的 AP 建立動態鄰居組。工作在 5GHz 頻段的 AP 會被指示為優先於工作在 2.4GHz 頻段的 AP。 <br/> 如果使用 EAP，則不會建立動態鄰居組；需要手動定義。 <br/><br/> |
| **rrm** (*no* \| *yes; Default: **yes***) | 啟用 802.11k 鄰居報告的傳送。  當裝置想要"探索/描繪"其周圍環境時，用戶端可以向 AP 請求"鄰居報告"（用戶端裝置可以儲存該報告，並立即或在稍後使用它進行漫遊）。 |
| **transition-threshold** (*integer; Default: **-80***) | 設定傳送非請求式 802.11v BSS 轉換管理請求的 RSSI 閾值。如果用戶端裝置在 `transition-threshold-time` 期間一直處於配置閾值"以下"，它就會被標記為"轉換候選"。 |
| **transition-threshold-time** (*time interval; Default: **10***) | 定義用戶端裝置可以處於配置的 `transition-threshold` 值"以下"多長時間（秒），才會被標記為"轉換候選"。 |
| **transition-request-period** (*time interval; Default: **30***) | 定義以秒為單位的間隔，如果用戶端裝置是"轉換候選"，AP 將按此間隔向其傳送非請求式 802.11v BSS 轉換管理請求。  例如使用預設值（30s），將每 30 秒向用戶端傳送一次請求，總共傳送 `transition-request-count` 次。 |
| **transition-request-count** (*count, unlimited; Default: **3***) | 定義應向被標記為"轉換候選"的用戶端傳送多少次非請求式 802.11v BSS 轉換管理請求。用戶端獲得"轉換候選"狀態後（"-1"次計數）會立即傳送一次請求，其餘"count"次將每隔 `transition-request-period` 傳送一次。  例如使用預設值（3），當用戶端獲得"轉換候選"狀態時傳送第 1 次請求；第 2 次請求在 `transition-request-period` 秒後傳送，第 3 次（最後一次）在又一個 `transition-request-period` 後傳送。  如果你想不限次數地傳送請求，請設定為 `unlimited`。 |
| **transition-time** (*time interval, immediate \| unlimited; Default: **unlimited***) | 定義用戶端裝置在被迫去認證之前可以作為"轉換候選"多長時間。它可以是秒為單位的 `time interval`（在裝置成為"轉換候選"後開始計時，時間到後對用戶端去認證），可以是 `immediate`（用戶端成為"轉換候選"後立即去認證），也可以是 `unlimited`（從不強制用戶端斷開，並繼續每隔 `transition-request-period` 秒傳送 `transition-request-count` 次轉換請求）。🛈  **重要：** 注意，使用 `transition-time=immediate` 時，`transition-request-period` 和 `transition-request-count` 將變得無用，因為用戶端會在 `transition-threshold-time` 之後立即被去認證。     |
| **wnm** (*no* \| *yes; Default: **yes***) | 啟用請求式 802.11v BSS 轉換管理請求的傳送。  用戶端可以請求包含"鄰居列表"的"漫遊建議"封包，以幫助裝置切換 AP。用戶端裝置可以接受建議並立即漫遊，也可以忽略建議並保持當前連線。 |

:::info
請理解**用戶端可以忽略 BSS 轉換管理請求**。BSS 轉換請求只是"建議"用戶端去尋找其他訊號更好的 AP。收到轉換請求後，是否切換 AP 或保持與當前 AP 的連線，完全由用戶端決定。
:::

:::info
**請求式 802.11v BSS 轉換管理請求的行為：**

請求式 802.11v BSS 轉換管理封包是根據用戶端自身的請求傳送給它的。用戶端裝置"請求" AP 提供"漫遊建議"（帶有"鄰居列表"），AP 則以轉換請求（包含"鄰居列表"）作為響應。
:::

:::info
**非請求式 802.11v BSS 轉換管理請求的行為：**

非請求式 802.11v 請求無需等待用戶端請求即可傳送給用戶端。即使用戶端沒有請求，也會發送該請求。

如果用戶端訊號低於 `transition-threshold`（預設值：-80 dBm）的時間超過 `transition-threshold-time`（預設值：10 s），則用戶端被標記為"轉換候選"。如果用戶端訊號高於 `transition-threshold`，則用戶端的"轉換候選"狀態被移除。

如果用戶端是"轉換候選"，它將開始收到**非請求式 802.11v BSS 轉換管理請求**封包（"建議"其移動到附近其他 AP 的封包）。第一個此類封包會在用戶端狀態變為"轉換候選"後立即傳送，後續封包每隔 `transition-request-period`（預設值：30 s）傳送。總共會發送 `transition-request-count`（預設值：3）個轉換請求，之後 AP 將停止建議轉換（除非配置了 `transition-request-count=unlimited`，這會讓 AP 不停地傳送請求，每個 `transition-request-period` 一個）。`transition-request-count` 次數用完後，用戶端將在自己請求之後，或在其被取消標記並再次被標記為"轉換候選"之後，收到下一個轉換請求。

`transition-time` 中的值定義了用戶端裝置在被強制斷開之前可以保持"轉換候選"狀態多長時間。可能的 `transition-time` 值：**unlimited**（繼續按 `transition-request-period` 間隔傳送 `transition-request-count` 數量的轉換請求，且從不強制對用戶端去認證）、**可配置時間**（秒，繼續按 `transition-request-period` 間隔傳送 `transition-request-count` 數量的轉換請求，然後在配置的 `transition-time` 用完後斷開用戶端），以及 **immediate**（當用戶端成為"轉換候選"時向其傳送轉換請求，並立即斷開它）。
:::

### 其他屬性 {#miscellaneous-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **arp** (*disabled* \| *enabled* \| *local-proxy-arp*  \| *proxy-arp* \| *reply-only; default: **enabled**)* | 地址解析協定模式：disabled - 介面不使用 ARP；enabled - 介面使用 ARP；local-proxy-arp - 路由器在介面上執行代理 ARP，並向同一介面傳送回覆；proxy-arp - 路由器在介面上執行代理 ARP，並向其他介面傳送回覆；reply-only - 介面只回復源自 ARP 表中靜態條目所匹配的 IP 地址/MAC 地址組合的請求。ARP 表中不會自動儲存動態條目。因此，為使通訊成功，必須已存在有效的靜態條目。 |
| **arp-timeout** (*time interval* \| *'auto'; default: **30s***) | 決定動態新增的 ARP 表條目在從相應 IP 地址收到最後一個數據包後被視為有效的時長。值 *auto* 等於*`/ip/settings`* 中 *arp-timeout* 的值，預設為 30s。 |
| **disable-running-check** *(no* \| *yes; default: **no***) | yes - 只要介面未被停用，其 running 屬性就為 true；no - 只有當介面已與另一裝置建立鏈路時，其 running 屬性才為 true |
| **disabled**（*no* \| *yes*；預設：**yes**） |  |
| **mac-address** (*MAC*) | 用於介面的 MAC 地址（BSSID）。 <br/> 硬體介面預設使用關聯無線介面的 MAC 地址。 <br/> 虛擬介面的預設 MAC 地址透過以下方式生成 <br/><ol><li>取關聯主介面的 MAC 地址</li><li>將第一個位元組的次最低有效位設定為 1，從而得到<a href="https://en.wikipedia.org/wiki/MAC_address#Ranges_of_group_and_locally_administered_addresses" rel="nofollow">本地管理 MAC 地址</a></li><li>如有需要，遞增地址的最後一個位元組，以確保它不與裝置上另一個介面的地址重疊</li></ol> |
| **mtu** *(integer [32..2290]; Default: **1500**)* | 第 3 層最大傳輸單元。 |
| **mld-interface** (*interface; default: **none***) | 指定關聯的 MLD（多鏈路裝置）介面。當兩個或更多 wifi 介面被分配相同的 MLD 介面（例如 *mld-interface=mld1*）時，它們會作為單個邏輯 AP MLD 協同工作，從而啟用多鏈路操作（MLO）。MLD 介面是邏輯資料轉發點——流量在 MLD 介面層面處理，而不是在各個關聯的 WiFi 介面上處理。所有關聯的 WiFi 介面必須共享相同的 SSID，並且所有參與的 radio 必須屬於同一裝置。MLO 需要相容的 Wi-Fi 7（802.11be）硬體。 |
| **mld-name** (*string*) | 一個唯一識別符號，用於將此介面指定為 MLD 介面。手動建立 MLD 介面時，必須唯一且明確設定。 |
| **l2mtu** *(integer [32..2290]; Default: **2290**)* | 第 2 層最大傳輸單元。 |
| **master-interface** (*interface; default: **none***) | 每個無線 radio 上可以同時執行多種介面配置。  其中只有一個決定 radio 的狀態（是否啟用、使用哪個頻率等）。這個"master"介面*繫結*到具有相應 *radio-mac* 的 radio。  要在某個 radio 上建立額外的（"虛擬"）介面配置，需要將它們*繫結*到相應的 master 介面。 |
| **name** (*string*) | 介面的名稱。預設為 *wifiN*，其中 *N* 是尚未用於介面命名的最小整數。 |

### 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **bound** (*boolean*) (B) | 對於當前可供 WiFi 管理器使用的 *master* 介面為 true。  對於虛擬介面（連線到 master 介面的配置），當介面本身及其 master 介面均未被停用，且 *master* 介面具有 bound 標誌時為 true。 |
| **cap** (string) | 如果此路由器是 CAPsMAN，且介面不屬於裝置本身而是屬於 CAPsMAN 控制的 CAP 裝置，則顯示有關該 CAP 裝置的資訊。 |
| **default-name** (*string*) | 介面的預設名稱。 |
| **inactive** (*boolean*) (I) | 對於 AP 模式下的介面，當其已選定工作通道（即配置已成功應用）時為 false。  對於 station 模式下的介面，當其已連線到 AP（即配置已成功應用，並找到了匹配設定的 AP）時為 false。  其他情況為 true。 |
| **master** (*boolean*) (M) | 對於路由器本身的物理介面，或在作為 CAPsMAN 執行時檢測到的 CAP 為 true。  對於虛擬介面為 false。 |
| **radio-mac** (*MAC*) | 關聯 radio 的 MAC 地址。 |
| **running** (*boolean*) (R) | 當介面已與另一裝置建立鏈路時為 true。  如果 *disable-running-check* 設為 'yes'，則只要介面未被停用就為 true。 |

### 訪問列表 {#access-list-1}

過濾引數：

| 引數 | 說明 |
| :-- | :-- |
| **interface** (*interface* \| *interface-list* \| *any; default: **any***) | 如果連線發生在指定介面或屬於指定列表的介面上則匹配。 |
| **mac-address** (*MAC address; default: **none***) | 如果用戶端裝置具有指定的 MAC 地址則匹配。 |
| **mac-address-mask** (*MAC address*) | 修改 **mac-address** 引數，使其在等於對用戶端 MAC 地址與給定地址掩碼執行按位 AND 運算的結果時匹配。  預設：FF:FF:FF:FF:FF:FF（即用戶端的 MAC 地址必須與 **mac-address** 的值完全一致） |
| **signal-range** (*min..max*) | 如果從用戶端裝置接收到的訊號強度在給定範圍內，則匹配。允許的值：'-120..120' |
| **ssid-regexp** (*regex*) | 如果給定的正則表示式與 SSID 匹配，則匹配。 |
| **time** (*start-end,days*) | 在指定的每日時間和（可選的）星期幾期間匹配。允許的值：0s-1d |
| **multi-passphrase-group** (*string*) | 將要使用的 `/interface/wifi/security/multi-passphrase/` 組的名稱。一個訪問列表條目下只能設定一個組。 |

動作引數：

| 引數 | 說明 |
| :-- | :-- |
| **allow-signal-out-of-range** *(time period \| always; default: **0s**)* | 已連線對端的訊號強度被允許超出 **signal-range** 引數所要求範圍的時間長度，之後它將被斷開。  如果值設為 'always'，則只在關聯時檢查對端訊號強度。 |
| **action** (*accept* \| *reject* \| *query-radius; default: **accept***) | 是否授權連線：accept - 允許連線；reject - 不允許連線；query-radius -  如果對用戶端 MAC 地址的 MAC 地址認證成功，則允許連線 |
| **client-isolation** (*no* \| *yes; default: **none***) | 是否將用戶端與連線到同一 AP 的其他用戶端[隔離](./index.md#datapath-properties)。 |
| **passphrase** (*string; *default: **none***) [sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用給定值覆蓋預設 passphrase。 |
| **radius-accounting** (*no* \| *yes; *default: **none***)* | 用給定值覆蓋預設 RADIUS 計費策略。 |
| **vlan-id** (*none* \| *integer 1..4095; *default: **none***)* | 為匹配的用戶端分配給定的 [VLAN ID](./index.md#datapath-properties)。 |

### 頻率掃描 {#frequency-scan-1}

執行 frequency-scan 命令可以獲得可用通道上射頻狀況的資訊。
命令引數：

| 引數 | 說明 |
| :-- | :-- |
| **duration** (*time interval; *default: **none***)* | 執行掃描多長時間後退出。對非互動式使用很有用。 |
| **freeze-frame-interval** (*time interval; default: **1s**)* | 更新命令輸出的時間間隔。 |
| **frequency** (*list of frequencies/ranges)* | 要執行掃描的頻率。詳情參見上文的 [channel.frequency 引數語法](#channel-properties)。預設為所有受支援的頻率。 |
| **number** (*string*; *default*: **none**) | 用於執行掃描的介面名稱或內部 id。必填。 |
| **rounds** (*integer*; *default*: **none**) | 退出前遍歷可掃描頻率列表的次數。對非互動式使用很有用。 |
| **save-file** (*string*; *default*: **none**) | 用於儲存輸出的檔名。 |

輸出引數：

| 引數 | 說明 |
| :-- | :-- |
| **channel** (*integer*) | 所掃描通道的頻率（MHz）。 |
| **networks** (*integer*) | 該通道上檢測到的接入點數量。 |
| **load** (*integer*) | 掃描期間該通道處於忙狀態的百分比。 |
| **nf** (integer) | 該通道的噪聲底（dBm）。 |
| **max-signal** (*integer*) | 該通道中檢測到的 AP 的最大訊號強度（dBm）。 |
| **min-signal** (*integer*) | 該通道中檢測到的 AP 的最小訊號強度（dBm）。 |
| **primary** (*boolean*) (P) | 該通道正被某個 AP 用作主（控制）通道。 |
| **secondary** (*boolean*) (S) | 該通道正被某個 AP 用作輔助（擴充套件）通道。 |

### Flat-snoop {#flat-snoop}

`/interface/wifi/flat-snoop` 是一個用於勘測 AP 和 station 的工具。它監影片率使用情況，並顯示哪些裝置佔用各個頻率。它比 scan 提供更詳細的附近 AP 資訊，並可按 station/AP 數量輕鬆概覽頻率使用情況。
輸出引數：

| 引數 | 描述 |
| :-- | :-- |
| **duration** (*time interval*; *預設*: **none**) | 在執行掃描多長時間後退出。適用於非互動式使用。 |
| **filter-type** (*bss \| frequency \| stas*) | bss - 活動 AP 及其引數的列表。 <br/> frequency - 每個掃描頻率的 station 和 AP 數量列表 <br/> stas - 每個掃描頻率上 station 的詳細列表 <br/> 如果未指定 filter-type，將返回所有型別。 |
| **freeze-frame-interval** (*time interval; default: **1s**)* | 更新命令輸出的時間間隔。 |

### scan 命令 {#scan-command-1}

`/interface/wifi/scan` 命令會掃描接入點，並列印其檢測到的所有 AP 的資訊。
scan 命令接受與 frequency-scan 命令相同的所有引數。
輸出引數：

| 引數 | 說明 |
| :-- | :-- |
| **active** (*boolean*) (A) | 這表示在過去 30 秒內收到了來自該 AP 的信標。 |
| **address** (*MAC*) | AP 的 MAC 地址（BSSID）。 |
| **channel** (*string*) | AP 使用的控制通道頻率、其支援的無線標準以及控制/擴充套件通道佈局。 |
| **security** (*string*) | AP 支援的認證方法。 |
| **signal** (*integer*) | AP 信標的訊號強度（dBm）。 |
| **ssid** (*string*) | AP 的擴充套件服務集識別符號。 |
| **sta-count** (*integer*) | 與該 AP 關聯的用戶端裝置數量。僅當 AP 在其信標中包含此資訊時才可用。 |

### 嗅探器 {#sniffer-1}

命令引數：

| 引數 | 描述 |
| :-- | :-- |
| **duration** (*time interval*; **default: **none***)* | 在指定時間過後自動中斷 sniffer。 |
| **filter** (*string*) | 一個字串，指定要應用於捕獲幀的過濾器。只有與過濾表示式匹配的幀才會被顯示、儲存或流式傳輸。 <br/> 例如，其工作方式類似於 libpcap 中的過濾字串。 <br/> 過濾器可以匹配 <br/><ul><li>地址欄位（addr1、addr2、addr3）</li><li>無線幀型別和子型別，包括 'beacon'（type == 0 &amp;&amp; subtype == 8）等簡寫</li><li>標誌位（to-ds、from-ds、retry、power、protected）</li></ul> 字串可以包含以下運算子： <br/><ul><li>==（精確匹配）</li><li>!=（不等於）</li><li>&amp;&amp;（邏輯與）</li><li> &#124;&#124;（邏輯或）</li><li>()（用於對過濾表示式進行分組）</li></ul> |
| <strong>number</strong> (<em>interface</em>) <br/> | 用於嗅探的介面。 |
| **pcap-file** (*string*) | 將捕獲的幀儲存到具有給定名稱的檔案中。沒有預設值（預設情況下捕獲的幀不會儲存到檔案）。 |
| **pcap-size-limit** (*integer*; *預設*: **none**) | 在本地儲存捕獲幀時的檔案大小限制（以位元組為單位）。達到此限制後，不會再向捕獲檔案新增新幀。 |
| **stream-address** (*IP address*; *default*: **none**) | 透過 TZSP 協定將捕獲的封包流式傳輸到給定地址。沒有預設值（預設情況下捕獲的封包不會流式傳輸到任何地方）。 |
| **stream-rate** (*integer*) | 限制透過 TZSP 流式傳輸捕獲幀的速率（以每秒封包數為單位）。 |

### WPS {#wps-1}

`/interface/wifi/wps-client/wifi`
命令引數：

| 引數 | 說明 |
| :-- | :-- |
| **duration** (*time interval*) | 如果未找到 AP，命令超時前的時間長度。預設無限制。 |
| **interval** (*time interval; default: **1s***) | 更新命令輸出的時間間隔。預設：1s。 |
| **mac-address** (*MAC*; *default*: **none**) | 僅嘗試連線到具有指定 MAC（BSSID）的 AP。 |
| **number** (*string; default: **none***) | 用於嘗試連線的介面名稱或內部 id。 |
| **ssid** (*string; default: **none***) | 僅嘗試連線到具有指定 SSID 的 AP。 |

### 射頻 {#radios-1}

執行 `/interface/wifi/radio/print detail` 命令可以獲取每個 radio 的能力資訊。

| 屬性 | 說明 |
| :-- | :-- |
| **2g-channels** (*list of integers*) | 2.4GHz 頻段支援的頻率。 |
| **5g-channels** (*list of integers*) | 5GHz 頻段支援的頻率。 |
| **6g-channels** (*list of integers*) | 6GHz 頻段支援的頻率。 |
| **bands** (*list of strings*) | 支援的頻段、無線標準和通道寬度。 |
| **ciphers** (*list of strings*) | 支援的加密演算法。 |
| **countries** (*list of strings*) | 介面支援的監管域。 |
| **hw-caps** (*list of strings*) | 額外支援的功能（例如 sniffer、qos-classifier-dscp）。 |
| **hw-type** (*string*) | Radio 硬體型號編號。 |
| **max-interfaces** (*integer*) | 最大邏輯介面數。 |
| **max-peers** (*integer*) | 最大關聯對端數（已連線 station）。 |
| **max-station-interfaces** (*integer*) | station 模式下的最大邏輯介面數。 |
| **max-vlans** (*integer*) | 最大不同按使用者 VLAN 數。 |
| **min-antenna-gain** (*integer*) | 介面允許的最小天線增益。 |
| **ml-group** (*MAC address*) | 具有共同 ML（多鏈路）組的 radio 可配置為利用多鏈路操作。 |
| **phy-id** (*string*) | 一個唯一識別符號。 |
| **radio-mac** (*MAC*) | radio 介面的 MAC 地址。可用於將 radio 與介面配置匹配。 |
| **rx-chains** (*list of integers*) | 可用於接收無線電訊號的射頻鏈 ID。 |
| **tx-chains** (*list of integers*) | 可用於傳送無線電訊號的射頻鏈 ID。 |

### 登錄檔 {#registration-table-1}

登錄檔包含有關已關聯無線裝置的只讀資訊。

| 引數 | 說明 |
| :-- | :-- |
| **authorized** (*boolean*) (A) | 當對端已成功透過認證時為 true。 |
| **auth-type** (*string*) | 該特定用戶端使用的認證型別。 |
| **band** (*string*) | 該特定路由器與 AP 通訊所用的頻段。 |
| **bytes** (*list of integers*) | 傳送給對端和從對端接收的封包位元組數。 |
| **interface** (*string*) | 用於與對端關聯的介面名稱。 |
| **last-activity**(time) | 介面最近一次資料收發活動 |
| **mac-address** (*MAC*) | 對端的 MAC 地址。 |
| **packets** (*list of integers*) | 傳送給對端和從對端接收的封包數量。 |
| **tx-bits-per-second** (*integer*) | 每秒向對端傳送資料的速率。 |
| **rx-bits-per-second** (*integer*) | 每秒從對端接收資料的速率。 |
| **rx-rate** *(string*) | 從對端接收傳輸的位元率。 |
| **signal** (*integer*) | 從對端接收的訊號強度（dBm）。 |
| **ssid** *(string*) | 用戶端所連線到的 SSID。 |
| **tx-rate** (*string*) | 用於向對端傳送的位元率。 |
| **uptime** (*time interval*) | 自關聯以來的時間。 |
| **vlan-id** (*integer*) | 由 AP 或 RADIUS 為該特定對端流量分配的 VLAN。 |
