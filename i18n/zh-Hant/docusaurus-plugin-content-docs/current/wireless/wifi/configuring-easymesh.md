---
sidebar_key: "wireless/wifi/configuring-easymesh"
sidebar_position: 2
title: "配置 EasyMesh"
sidebar_label: "配置 EasyMesh"
description: "在 RouterOS 中配置 Wi-Fi EasyMesh 網路：設定控制器和代理，建立前傳和回傳配置，透過 WPS 新增代理，並監控 mesh。"
tags:
  - 'wifi'
  - 'easymesh'
  - 'mesh'
  - 'controller'
  - 'agent'
source: https://manual.mikrotik.com/docs/wireless/wifi/configuring-easymesh
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**Package:** `wifi-qcom`, `wifi-qcom-ac`

:::warning

- EasyMesh 可在 CLI 中使用（尚不支援 GUI）。
- 目前，它僅在 `wifi-qcom` 和 `wifi-qcom-ac` 上工作。
- 透過 Wi-Fi 接入代理節點時，請使用 `wpa2-psk` 或 `wpa2-psk,wpa3-psk` 配置前傳。WPS 入網使用前傳配置，而代理節點的回傳憑據透過回傳鏈路傳遞。WPS 不支援僅 WPA3（SAE）。
- 尚未實現 DPP（Wi-Fi Easy Connect）入網。要接入代理節點，請使用 WPS 按鈕或透過乙太網連線代理節點。
:::

EasyMesh 是 Wi-Fi Alliance 的一項標準，用於將來自不同供應商的 Wi-Fi AP 和無線擴充套件器作為同一個協調網路進行管理。控制器將 fronthaul（用戶端 SSID）和 backhaul（agent SSID）設定分發給受管 AP（agent），這些 AP 透過二層將其 fronthaul 介面橋接到無線或乙太網 backhaul 介面，在轉發用戶端流量時保留用戶端 MAC 地址。最終結果是在單個控制器下形成一個二層網路。有關所有設定，請參閱 [EasyMesh CLI 參考](../../cli-reference/interface/wifi/easymesh.md)。

[CAPsMAN](./capsman.md) 為 MikroTik 裝置提供類似的集中管理，但它主要面向透過乙太網連線到網路的接入點。它不提供標準化的無線 backhaul 和 WPS 引導。EasyMesh 認證允許控制器管理來自不同供應商的認證 agent。互操作性仍取決於裝置，因此請在部署前測試控制器與 agent 的組合。

## 拓撲 {#topology}

一個 EasyMesh 網路有一個控制器和一個或多個 agent。控制器和 agent 必須位於同一個二層網路中。Agent 透過有線乙太網連線或無線 backhaul 鏈路連線到控制器。Backhaul（有線和無線）承載 EasyMesh 管理流量以及每個 agent 的用戶端流量。

裝置承擔三種 EasyMesh 角色之一：

- `controller` - 管理 EasyMesh 網路。它提供 fronthaul 和 backhaul 配置並協調各個 agent。在僅承擔控制器職責的裝置上使用它。
- `agent` - 加入 EasyMesh 網路並從控制器接收其配置。它廣播已配置的 fronthaul 網路，並透過無線 backhaul 鏈路或有線乙太網連線連線到控制器。在額外的接入點上使用它。
- `controller-and-agent` - 在同一臺裝置上同時承擔兩種角色。單臺 Wi-Fi 裝置既可以管理 EasyMesh 網路，也可以作為 agent 為用戶端提供服務。在帶 Wi-Fi 射頻的主路由器或接入點上使用它。

只有控制器管理網路。Agent 接收並應用配置（它不管理其他 agent，但可以透過 backhaul 中繼控制器流量）。

在大多數設定中，主路由器使用 `controller-and-agent`，而附加接入點使用 `agent`。

這些裝置上的射頻可以承擔以下角色：

- Fronthaul AP - 廣播用戶端網路。用戶端裝置連線到這些 BSS。
- Backhaul AP - 廣播回傳網路。Agent 使用它連線到控制器。用戶端裝置不使用此網路。
- Backhaul station - 將 agent 連線到控制器的 backhaul AP。它僅用於無線回傳。

同一射頻可同時提供 fronthaul 和 backhaul BSS。Fronthaul 介面專用於用戶端，並橋接到 backhaul。

控制器和 agent 使用 IEEE 1905.1 標準（EtherType `0x893A`）交換 EasyMesh 控制訊息。它透過 Layer 2 回傳承載 Wi-Fi Alliance Multi-AP Control Message Data Units (CMDUs) 和 TLV。WPS 入網使用 802.11/EAP-WSC。

## 控制器配置 {#controller-configuration}

### 設定射頻管理器 {#set-the-radio-manager}

在 EasyMesh 應控制的每個射頻上設定 EasyMesh 管理器：

```ros
/interface/wifi
set [find default-name=wifi1] configuration.manager=easymesh
set [find default-name=wifi2] configuration.manager=easymesh
```

調整介面名稱以匹配你的裝置。

### 建立 Wi-Fi 配置 {#create-the-wi-fi-configurations}

為用戶端建立前傳配置，併為無線代理建立回傳配置：

```ros
/interface/wifi/configuration
add name=em_fh ssid=em_fh security.authentication-types=wpa2-psk security.passphrase=fronthaul-password
add name=em_bh ssid=em_bh security.authentication-types=wpa2-psk security.passphrase=backhaul-password
```

- `em_fh` 是用戶端網路，由代理為用戶端裝置廣播。
- `em_bh` 是回傳網路，由代理廣播，供其他代理連線。請使用與用戶端網路不同的 SSID 和密碼。

### 啟用控制器 {#enable-the-controller}

```ros
/interface/wifi/easymesh
set enabled=yes role=controller-and-agent bridge=bridge bhaul-configuration=em_bh fhaul-configurations=em_fh dpp-onboarding=no
```

- `role=controller-and-agent` 使裝置管理網路並提供 Wi-Fi。如果裝置僅管理網路，請使用 `role=controller`。
- `bridge=bridge` 是連線控制器與代理的網橋。請使用現有的 LAN 網橋。
- `bhaul-configuration=em_bh` 選擇回傳配置。
- `fhaul-configurations=em_fh` 選擇用戶端網路。新增更多配置名稱可廣播更多網路。

回傳 SSID 和安全設定來自 `em_bh` 配置。無線代理在加入過程中接收這些憑據。

## 代理配置 {#agent-configuration}

### 準備接入點 {#prepare-the-access-point}

將代理配置為橋接接入點。在每個射頻上設定 EasyMesh 管理器：

```ros
/interface/wifi
set [find default-name=wifi1] configuration.manager=easymesh
set [find default-name=wifi2] configuration.manager=easymesh
```

按[配置獨立接入點](./configuring-standalone-access-point.md)所述配置網橋和管理 IP 地址。網橋必須包含用於有線回程的乙太網埠。

### 啟用代理 {#enable-the-agent}

```ros
/interface/wifi/easymesh
set enabled=yes role=agent bridge=bridge dpp-onboarding=no
```

EasyMesh 會將其 Wi-Fi 介面新增到 `bridge` 設定中指定的網橋。不要在代理上設定 `bhaul-configuration` 或 `fhaul-configurations`。控制器會在入網過程中提供它們。

## 入網引導 {#onboarding}

### 有線回程 {#wired-backhaul}

將代理的乙太網埠連線到控制器的 LAN。不需要 WPS。當代理位於同一二層網路時，控制器會發現它並自動應用配置。

### 無線回程 {#wireless-backhaul}

當代理沒有到控制器的乙太網連線時，會使用無線回傳。控制器透過其 `bhaul-configuration` 提供回傳網路。回傳 AP 會廣播該網路，代理的回傳工作站使用在入網期間收到的憑據連線到它。

使用 WPS 按鈕讓代理入網：

```ros
/interface/wifi/easymesh/wps-push-button
```

先在控制器上執行該命令，然後在代理上執行。代理會連線到控制器的回傳網路，並接收回傳和前傳配置。

入網後，`agent-state` 將變為 `wifi-backhaul-connected`：

```ros
[admin@hAP] > /interface/wifi/easymesh/print
                     enabled: yes
                        role: agent
                      bridge: bridge
                  bhaul-ssid: em_bh
            bhaul-passphrase: backhaul-password
  bhaul-authentication-types: wpa2-psk
            bhaul-encryption: ccmp
                              gcmp
              dpp-onboarding: no
                 agent-state: wifi-backhaul-connected
```

:::tip
在入網過程中，使 Agent 靠近 Controller。在回傳鏈路建立後，將其移至最終位置。
:::

## 驗證設定 {#verify-the-setup}

執行以下命令以檢視 EasyMesh 狀態：

```ros
/interface/wifi/easymesh/print
/interface/wifi/easymesh/topology/print
/interface/wifi/easymesh/bss/print
/interface/wifi/easymesh/sta/print
```

- `print` 顯示全域性 EasyMesh 設定、代理狀態，以及包含控制器、代理、射頻和 BSSes 的拓撲樹。
- `topology/print` 按已連線代理的 AL MAC 地址列出它們。
- `bss/print` 列出所有 BSSes 及其前傳/回傳角色、通道、利用率和用戶端數量。
- `sta/print` 列出已連線的用戶端和回傳工作站。

:::info
AL MAC 是 IEEE 1905.1 抽象層 MAC 地址。EasyMesh 將其用作控制訊息和拓撲中的裝置標識，獨立於承載流量的介面。
:::

`print` 輸出顯示全域性設定、代理狀態和拓撲樹：

```ros
[admin@cAP] > /interface/wifi/easymesh/print
               enabled: yes
                  role: controller-and-agent
                bridge: bridge
   bhaul-configuration: em_bh
  fhaul-configurations: em_fh
        dpp-onboarding: no
           agent-state: wired-backhaul-connected
               network: CONTROLLER: AL-MAC: 48:XX:XX:XX:XX:74
                            ETHERNET: mac: 48:XX:XX:XX:XX:74
                                AGENT: AL-MAC: D0:XX:XX:XX:XX:D3 via mac: D0:XX:XX:XX:XX:D3
                                    ETHERNET: mac: D0:XX:XX:XX:XX:D3
                                    ETHERNET: mac: D0:XX:XX:XX:XX:D4
                                    ETHERNET: mac: D0:XX:XX:XX:XX:D5
                                    ETHERNET: mac: D0:XX:XX:XX:XX:D6
                                    ETHERNET: mac: D0:XX:XX:XX:XX:D7
                                    RADIO: mac: D0:XX:XX:XX:XX:D9
                                        bVAP[0]: bssid: D0:XX:XX:XX:XX:D9, ssid: em_bh, bw: 160 MHz, ccfi1: 50
                                        fVAP[1]: bssid: D2:XX:XX:XX:XX:DA, ssid: em_fh, bw: 160 MHz, ccfi1: 50
                                    RADIO: mac: D0:XX:XX:XX:XX:D8
                                        bVAP[0]: bssid: D2:XX:XX:XX:XX:D8, ssid: em_bh, bw: 40 MHz, ccfi1: 11
                                        fVAP[1]: bssid: D2:XX:XX:XX:XX:D9, ssid: em_fh, bw: 40 MHz, ccfi1: 11
                            ETHERNET: mac: 48:XX:XX:XX:XX:75
                            RADIO: mac: 48:XX:XX:XX:XX:77
                                bVAP[0]: bssid: 48:XX:XX:XX:XX:77, ssid: em_bh, bw: 40 MHz, ccfi1: 5
                                fVAP[1]: bssid: 4A:XX:XX:XX:XX:77, ssid: em_fh, bw: 40 MHz, ccfi1: 5
                            RADIO: mac: 48:XX:XX:XX:XX:76
                                bVAP[0]: bssid: 48:XX:XX:XX:XX:76, ssid: em_bh, bw: 80 MHz, ccfi1: 58
                                fVAP[1]: bssid: 4A:XX:XX:XX:XX:76, ssid: em_fh, bw: 80 MHz, ccfi1: 58
```

拓撲表列出已連線的代理：

```ros
[admin@cAP] > /interface/wifi/easymesh/topology/print
Columns: ALMAC
#  ALMAC
0  D0:XX:XX:XX:XX:D3
```

BSS 表列出控制器和代理上的前傳和回傳 BSS：

```ros
[admin@cAP] > /interface/wifi/easymesh/bss/print
Flags: A - ACTIVE
Columns: ALMAC, RADIO-MAC, BSSID, SSID, FRONTHAUL, BACKHAUL, UTILIZATION, BRANCH-UTILIZATION, STA-COUNT, OPCLASS, PRIMARY-CHAN, IEEE-CHAN
#   ALMAC              RADIO-MAC          BSSID              SSID   FRONTHAUL  BACKHAUL  UTI  BRA  S  OPCLASS  PRI  IEEE-CHAN
0 A 48:XX:XX:XX:XX:74  48:XX:XX:XX:XX:76  48:XX:XX:XX:XX:76  em_bh  no         yes       0%   0%   0  128      136  138
1 A 48:XX:XX:XX:XX:74  48:XX:XX:XX:XX:77  48:XX:XX:XX:XX:77  em_bh  no         yes       33%  33%  1  84       5    5
2 A 48:XX:XX:XX:XX:74  48:XX:XX:XX:XX:76  4A:XX:XX:XX:XX:76  em_fh  yes        no        0%   0%   1  128      136  138
3 A 48:XX:XX:XX:XX:74  48:XX:XX:XX:XX:77  4A:XX:XX:XX:XX:77  em_fh  yes        no        33%  33%  0  84       5    5
4 A D0:XX:XX:XX:XX:D3  D0:XX:XX:XX:XX:D9  D0:XX:XX:XX:XX:D9  em_bh  no         yes       0%   33%  0  129      64   50
5 A D0:XX:XX:XX:XX:D3  D0:XX:XX:XX:XX:D8  D2:XX:XX:XX:XX:D8  em_bh  no         yes       0%   33%  0  84       5    5
6 A D0:XX:XX:XX:XX:D3  D0:XX:XX:XX:XX:D8  D2:XX:XX:XX:XX:D9  em_fh  yes        no        0%   33%  0  84       5    5
7 A D0:XX:XX:XX:XX:D3  D0:XX:XX:XX:XX:D9  D2:XX:XX:XX:XX:DA  em_fh  yes        no        0%   33%  0  129      64   50
```

STA 表列出已連線用戶端和回傳站點：

```ros
[admin@cAP] > /interface/wifi/easymesh/sta/print
Columns: BSSID, SSID, ALMAC, MAC-ADDRESS, UPTIME, LAST-ACTIVITY, SIGNAL, BACKHAUL
#  BSSID              SSID   ALMAC              MAC-ADDRESS        UPTIME  LAST-ACTIVITY  SIGNAL  BACKHAUL
0  4A:XX:XX:XX:XX:76  em_fh  48:XX:XX:XX:XX:74  3C:XX:XX:XX:XX:AD  6s      1s510ms        -32     no
1  48:XX:XX:XX:XX:77  em_bh  48:XX:XX:XX:XX:74  D0:XX:XX:XX:XX:D8  16s     1s820ms        -22     yes
```

## 故障排除 {#troubleshooting}

- 如果代理未出現在 `topology` 中，請檢查兩臺裝置是否位於同一二層網路、代理的網橋是否包含正確的埠，以及是否已設定 `enabled=yes`、`role=agent` 和 `configuration.manager=easymesh`。
- 如果無線回傳未能建立，請在兩臺裝置上再次執行 WPS 按鈕命令。從控制器開始。
- 如果用戶端看不到網路，請檢查控制器是否具有正確的 `fhaul-configurations` 值，以及代理是否已完成入網。
- 一個射頻只能使用一個管理器。不要在同一介面上同時使用 EasyMesh 和 CAPsMAN。

## 說明 {#notes}

:::note

- 每個 EasyMesh 網路使用一個控制器。
- 所有控制器和代理節點必須位於同一二層網路中。
- 跨廠商互操作性需要經過認證的 EasyMesh 裝置。部署前請測試特定的控制器和代理節點組合。
:::
