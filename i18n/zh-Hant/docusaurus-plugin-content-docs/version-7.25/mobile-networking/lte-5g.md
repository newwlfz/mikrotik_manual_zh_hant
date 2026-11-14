---
sidebar_key: "mobile-networking/lte-5g"
sidebar_position: 1
title: "LTE/5G"
sidebar_label: "LTE/5G"
description: "本頁面介紹 MikroTik RouterOS 中的 LTE 和 5G 配置，涵蓋介面設定、APN 配置檔案、LTE 設定以及執行模式，包括 RouterOS v7 中的 MBIM 支援。文中包含用於啟用 PPP 模擬、管理漫遊以及配置 MTU 和 PIN 碼等調變解調器引數的 CLI 命令。"
tags:
  - 'lte'
  - '5g'
  - 'apn'
source: https://manual.mikrotik.com/docs/7.25/mobile-networking/lte-5g
captured_at: '2026-11-04T11:20:53+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

```ros
Package: system
Optional lte-mipsbe.npk package is only required for SXT 3-7 built-in modem.
```

僅支援 Direct-IP 模式型別的卡。MBIM 支援在 RouterOS v7 版本中可用，並且 MBIM 驅動會自動載入。如果調變解調器在 RouterOS v6 中無法識別。請在 v7 版本中測試後再尋求 RouterOS v6 支援。

要透過 PPP 介面而不是 LTE 介面進行訪問，請使用 `/interface/lte/settings/set mode=serial` CLI 命令將執行模式更改為 "serial" 並重啟。請注意，使用 PPP 模擬模式時，可能無法獲得與使用 LTE 介面模擬型別相同的吞吐速度。

:::warning
對於 RouterOS v7，`ignore-direct-modem` 引數已重新命名為 `mode`，並移至 `/interface/lte/settings` 選單。
:::

### LTE 用戶端 {#lte-client}

**子選單：** `/interface/lte`

#### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **allow-roaming** (*yes \| no*; 預設值：**no**) | 啟用資料漫遊，以便連線到其他國家/地區的資料提供商。並非所有 LTE 調變解調器都支援此功能。部分未完全支援此功能的調變解調器會連線到網路，但當 allow-roaming 設定為 no 時不會建立 IP 資料連線。 |
| **apn-profiles** (*string*；預設：**default**) | 用於此介面的 APN 配置檔案 |
| **band** (*integer list*; 預設值：**""**) | 通訊中使用的 LTE 頻段 `LTE Bands and bandwidths` |
| **nr-band** (*integer list*; 預設值： "") | 通訊中使用的 5G NR 頻段 `5G NR Bands and bandwidths` |
| **comment** (*string*; 預設值：**""**) | 條目的描述性名稱 |
| **disabled** (*yes \| no*; 預設值：**no**) | 介面是否被停用。預設情況下已啟用。 |
| **modem-init** (*string*; 預設值：**""**) | 調變解調器初始化字串（將在調變解調器啟動時執行的 AT 命令） |
| **mtu** (*integer \| auto*; 預設值：**1500**) | 最大傳輸單元。LTE 介面在不進行封包分片時能夠傳送的最大封包大小。 <ul><li>auto - 對於支援該功能的調變解調器（MBIM 調變解調器），使用網路通告的 MTU。其他調變解調器將回退到預設值（1500）。</li></ul> |
| **name** (*string*; 預設值：**""**) | 介面的描述性名稱。 |
| **network-mode** (*3g \| gsm \| lte \| 5g*) | 選擇/強制 LTE 介面執行的 RAT 模式。要使 5G NSA 正常工作，必須同時選擇 lte 和 5g 網路模式！僅選擇 5g 將只允許連線到 5G SA。 |
| **operator** (*integer*; 預設值：**""**) | 用於將裝置鎖定到特定運營商。鎖定使用由 MCC+MNC 組成的完整 PLMN 號碼。[PLMN 程式碼](https://en.wikipedia.org/wiki/Public_land_mobile_network) |
| **pin** (*integer*; 預設值：**""**) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | SIM 卡的 PIN 碼。 |
| **sms-protocol** (*at \| auto \| mbim*) | SMS 功能。  **mbim**：使用 MBIM 驅動程式。  **at**：使用 AT-Commands。  **auto**：根據調變解調器選擇適當的選項。 |

#### APN 配置檔案 {#apn-profiles}

所有與網路相關的設定都在配置檔案中

**子選單：** `/interface/lte/apn`

| 屬性 | 描述 |
| :-- | :-- |
| **add-default-route** (*yes \| no*) | 是否新增預設路由，以透過 LTE 介面轉發所有流量。 |
| **apn** (*string*) | 服務提供商的接入點名稱 |
| **authentication** (*pap \| chap \| none*；預設：**none**) | 允許用於認證的協定 |
| **default-route-distance** (*integer*；預設：**2**) | 設定當同時選擇 add-default-route 時應用於自動建立預設路由的距離值。預設情況下，LTE 路由的距離為 2，以便優先使用有線路由而不是 LTE |
| **ip-type** (*auto \| ipv4 \| ipv4-ipv6 \| ipv6*；預設：auto ) | 請求的 PDN 型別 |
| **ipv6-interface** (; 預設： ) | 用於通告 IPv6 字首的介面 |
| **name** (*string*；預設： ) | APN 配置檔名稱 |
| **number** (*integer*；預設： ) | APN 配置檔案編號 |
| **passthrough-interface** (; 預設： ) | 用於傳遞 IP 配置的介面（啟用直通） |
| **passthrough-mac** (*MAC*；預設：**auto**) | 如果設定為 auto，則它會從第一個封包中學習 MAC |
| **passthrough-subnet-selection** (*auto / p2p*；預設：**auto**) | "auto" 選擇可用於直通介面的最小子網。"p2p" 將直通介面子網設定為 /32，並從 10.177.0.0/16 範圍中選擇閘道器地址。除非 APN 配置發生更改，否則閘道器地址保持不變。 |
| **password** (*string*；預設： ) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 如果任何認證協定處於活動狀態，則使用該密碼 |
| **use-network-apn** (*yes \| no*；預設：**yes**) | 該引數從 RouterOS v7 開始可用，並且僅用於 MBIM 調變解調器。如果設定為 yes，則使用網路提供的 APN。 |
| **use-peer-dns** (*yes \| no*；預設：**yes**) | 如果設定為 yes，則使用從 LTE 介面接收到的 DNS |
| **user** (*string*) | 如果任何認證協定處於活動狀態，則使用的使用者名稱 |

#### LTE 設定 {#lte-settings}

LTE 和路由器特定的 LTE 設定。該選單從 RouterOS v7 開始可用。

**子選單：** `/interface/lte/settings`

| 屬性 | 描述 |
| :-- | :-- |
| **mode** (*auto \| mbim \| serial* / *user*；*預設：**auto***) | 執行模式設定。auto - 自動選擇執行模式。serial - 僅提供序列埠。mbim - 如果可能，將調變解調器切換到 MBIM 模式。user - 作業系統不會嘗試自動切換調變解調器模式。（從 RouterOS 7.16 開始可用） |
| **firmware-path** (*string*) | 主機作業系統中的韌體路徑。[調變解調器 Gobi 韌體](./lte-5g.md#modem-fotadfota-downloads) |
| **external-antenna** (*auto \| both \| div \| main \| none*；預設：**auto**) | 此設定僅適用於 "Chateau" 路由器，但 Chateau 5G 版本除外。auto - 測量內部和外部天線上的訊號電平，並選擇訊號最佳（RSRP）的天線。both - 兩根天線都設定為外部天線。div - 分集天線設定為外部天線。main - 主天線設定為外部天線。none - 未選擇外部天線（使用內部天線）  |
| **external-antenna-selected** () | 此設定僅適用於 "Chateau" 路由器，但 Chateau 5G 版本除外。如果 "**external-antenna**" 設定為 "auto"，則顯示當前選擇的天線 |
| **sim-slot** () | 此設定適用於具有可切換 SIM 插槽的路由器（LtAP、SXT）。不同產品的選擇選項有所不同。 |
| **esim-channel** (*auto \| at;* 預設：*auto*)  | 用於 eSIM 管理的控制通道 |
| **link-recovery-timer** (*integer* 預設：*120* 範圍：*120..4294967295*)  | 如果 LTE 介面未進入 (R)running 狀態，則在經過該秒數後重新配置介面 |

#### LTE eSIM {#lte-esim}

```ros
RouterOS version: 7.18+
```

[MikroTips：如何首次啟用你的 eSIM！](https://www.youtube.com/watch?v=v0WtU1xBB-Q)

此選單包含與使用 RouterOS 內建 LPA（eSIM [Local Profile Assistant](http://en.wikipedia.org/wiki/ESIM)）進行 eSIM（[embedded Subscriber Identification Module](http://en.wikipedia.org/wiki/Remote_SIM_provisioning)）開通和管理相關的命令。

單個 eSIM 晶片可以儲存多個 eSIM 配置檔案，最大配置檔案數量取決於所使用的 eSIM 晶片。

RouterOS LPA 支援：

- 韌體支援 SIM 低階訪問命令（AT+CCHO；AT+CCHC；AT+CGLA）的 AT 調變解調器。
- 其韌體支援 SIM 低層訪問服務的 MBIM 調變解調器（UUID\_SERVICE\_MS\_UICC）。

其他要求：

- 插入 RouterBoard SIM 插槽的 SIM 卡外形尺寸 eSIM（物理 eSIM）。
- 調變解調器上存在 eSIM/eUICC（焊接晶片），並且調變解調器已設定為使用此插槽。
- 在 eSIM 晶片上開通和刪除 SIM 配置檔案期間，需要連線到 eSIM SIM 配置檔案提供商 SM-DP+ 開通伺服器（為獲得連線性，你可以使用另一個 eSIM 配置檔案或另一個 WAN 介面）。
- 僅當活動插槽為 eSIM 時，才能開通 eSIM。
- 某些裝置具有多個 SIM 插槽，要使用 eSIM，你需要使用命令 "/interface/lte/settings/set sim-slot=esim" 切換插槽。

命令 `/interface/lte/esim/esim-id [find /interface/lte]` 可用於檢查調變解調器是否支援 SIM 低階訪問命令以及是否存在 eSIM。

如果使用帶有嵌入式 eSIM 晶片的第三方調變解調器，請查閱調變解調器手冊，瞭解選擇 eSIM 插槽所需的 AT 命令（AT!UIMS；AT+QUIMSLOT 等）。

**命令**

| 屬性 | 描述 |
| :-- | :-- |
| **deactivate** | 停用（停用）eSIM 配置檔案。`/interface/lte/esim/deactivate number=0` |
| **activate** | 啟用（啟用）eSIM 配置檔案。`/interface/lte/esim/activate number=0` |
| **delete** | 從 eSIM 卡中永久刪除 eSIM 配置檔案。`/interface/lte/esim/delete number=0` |
| **print** | 列出 eSIM 上安裝的 eSIM 配置檔案 `/interface/lte/esim/print` |
| **provision** | 開通新的 eSIM 配置檔案。該命令接受四個引數：interface - 將為哪個介面啟用 eSIM 配置檔案。matching-id - 啟用碼令牌。示例： matching-id=ABCD10EFGHI5KL6M sm-dp-plus - SM-DP+ 伺服器主機名 confirmation-code - 確認碼（某些情況下需要的一次性密碼） activate - 在開通後啟用新建立的配置檔案（yes\|no；預設：yes）[從 7.20beta6 版本開始可用。在 7.20beta6 之前，配置檔案在開通後預設不會啟用。] force-confirmation - 如果設定為 yes，命令不會等待使用者確認，並自動接受配置檔案開通（yes\|no；預設：no）示例：從二維條碼解碼的 eSIM LPA 字串：**LPA:1$server.example.io$ABCD10EFGHI5KL6M** `/interface/lte/esim/provision interface=lte1 sm-dp-plus=server.example.io matching-id=ABCD10EFGHI5KL6M` |
| **esim-id** | 查詢 eSIM ID。該命令接受一個引數：interface - 選擇要查詢 eSIM ID 的介面。`/interface/lte/esim/esim-id interface=lte1   eid: 8903302342630000000004181FFFFFFF` |
| **set-nickname** | 為 eSIM 配置檔案設定暱稱。`/interface/lte/esim/set-nickname number=0 nickname=nickname1` |
| **refresh-profile-list** | 重新查詢 eSIM 配置檔案列表。該命令接受一個引數：interface - 選擇將重新查詢其 eSIM 配置檔案的介面。 |

##### 內建 eSIM 晶片的裝置（MikroTik Connectivity） {#devices-with-built-in-esim-chip-mikrotik-connectivity}

:::info
這些裝置預裝了 MikroTik Connectivity eSIM 配置檔案。
https://mikrotik.com/connectivity
:::

| 裝置型號 | 調變解調器 |
| :-- | :-- |
| S53UG+5HaxD2HaxD-TC&RG650E-EU | RG650E-EU |
| ATLGM&RG520F-EU | RG520F-EU |
| EC25-EU&KNe | EC25-EU |

##### 調變解調器 eSIM 管理支援表 {#modem-esim-management-support-table}

:::note
\* 這些調變解調器沒有內建 eSIM。它們需要外部 eSIM 晶片。例如，物理 eSIM 卡（標準 SIM 外形尺寸的 eSIM）。
:::

| 調變解調器 | 支援 | 註釋 |
| :-- | :-- | :-- |
| EC200A-EU | yes\* |  |
| EG06-A | yes\* |  |
| EG18-EA | yes\* |  |
| EG12-EA | yes\* |  |
| EG120K-EA | yes\* |  |
| RG520F-EU | yes\* |  |
| EP06-A | yes\* |  |
| RG502Q-EA | yes\* |  |
| FG621-EA | yes\* | 無法管理空 eSIM（無配置檔案） |
| R11e-LTE6 | yes\* | 從韌體版本 R11e-LTE6\_V039 開始 |
| R11e-LTE-US | no |  |
| R11e-4G | no |  |
| R11e-LTE | no |  |

#### 掃描器 {#scanner}

可以使用 `/interface/lte/scan` 命令掃描 LTE 介面。示例：

```ros
[admin@MikroTik] > /interface/lte/scan duration=60 number=0
Columns: OPERATOR, MCC-MNC, RSSI, RSRP, RSRQ
OPERATOR  MCC-MNC  RSSI    RSRP    RSRQ
LMT         24701  -36dBm  -63dBm  -7dB
```

可用屬性：

| 屬性 | 描述 |
| :-- | :-- |
| **duration** (*integer*) | 掃描持續時間（秒） |
| **freeze-frame-interval** (*integer*) | 資料列印之間的時間 |
| **number** (*integer*) | 介面編號或名稱 |

#### 監控 LTE 詳細資訊 {#monitoring-lte-details}

你可以使用 CLI 命令 `/interface/lte/monitor` 監控 LTE 介面引數。它會返回小區級資料（例如運營商、小區 ID、訊號資訊）和調變解調器元資料（韌體、型號、SIM 識別符號）。

```
[admin@MikroTik] > /interface/lte/monitor lte1
            status: connected
             model: EG18-EA
          revision: EG18EAPAR01A12M4G
  current-operator: LMT
    current-cellid: 3103242
            enb-id: 12122
         sector-id: 10
        phy-cellid: 480
        data-class: LTE
    session-uptime: 15m54s
              imei: 86981604098XXXX
              imsi: 24701060267XXXX
              iccid: 8937101122102057XXXX
      primary-band: B3@20Mhz earfcn: 1300 phy-cellid: 480
     dl-modulation: qpsk
               cqi: 7
                ri: 2
               mcs: 1
              rssi: -68dBm
              rsrp: -97dBm
              rsrq: -9dB
              sinr: 6dB
```

#### LTE 介面能力 {#lte-interface-capabilities}

你可以使用 `/interface/lte/show-capabilities` CLI 命令檢查 LTE 介面能力。

##### 示例輸出 {#example-output}

```
[admin@MikroTik] > interface/lte/show-capabilities lte1
  modem-bus-location: 2-1
           cell-scan: yes
        network-scan: yes
     roaming-barring: yes
  apn-address-family: IPv4,IPv6
       max-apn-count: 8
           rat-modes: 3g,lte,5g
      band-selection: yes
           lte-bands: 1,3,5,7,8,20,28,32,38,40,41,42,43
            nr-bands: 1,3,5,7,8,20,28,38,40,41,75,76,77,78
         passthrough: yes
     firmware-update: yes
   lte-attach-config: yes
             at-chat: yes
    framed-route-apn: any
```

| 能力 | 描述 |
|------------|-------------|
| **modem-bus-location** | LTE 調變解調器連線到的物理 USB 匯流排 |
| **cell-scan** | 支援 `interface/lte/cell-monitor` 命令 |
| **network-scan** | 支援 `interface/lte/scan` 命令 |
| **roaming-barring** | 支援漫遊限制 |
| **apn-address-family** | 支援的 IP 地址族（IPv4、IPv6） |
| **max-apn-count** | 可同時處於活動狀態的 APN 配置檔案最大數量 |
| **rat-modes** | 支援的無線接入技術（GSM、3G、LTE、5G） |
| **band-selection** | 支援 LTE/5G 頻段設定命令 |
| **lte-bands** | 調變解調器支援的 LTE 頻段列表 |
| **nr-bands** | 調變解調器支援的 5G 頻段列表 |
| **passthrough** | 支援 LTE 直通 |
| **firmware-update** | 支援 `interface/lte/firmware-upgrade` |
| **lte-attach-config** | 支援 LTE attach APN 配置（設定與配置相同的 APN） |
| **at-chat** | 支援 `interface/lte/at-chat` |
| **framed-route-apn** | 在多 APN 設定中，哪個 APN 支援 framed routing（後置路由） |

#### 調變解調器 firmware-upgrade 命令 {#modem-firmware-upgrade-command}

該命令允許在受支援的 MikroTik 調變解調器有可用更新時檢查並升級調變解調器韌體。

要檢查韌體更新可用性並進行安裝，需要活動的網際網路連線；根據調變解調器的不同，可以使用任意 RouterOS 介面或調變解調器介面（FOTA）提供網際網路連線，關於每種調變解調器支援的連線方法，請參見下表。

| 引數 / 屬性 | 描述 |
| :-- | :-- |
| **upgrade** (*yes \| no；預設：**no***) | 設定命令執行模式：no - 顯示當前調變解調器韌體版本並顯示最新可用韌體版本。yes - 執行韌體安裝。 |
| **update-channel** (*stable \| testing*；預設：**stable**)  | 設定使用哪個韌體更新通道：stable - 用於一般使用的韌體版本。testing - 早期訪問/測試通道，調變解調器韌體在釋出到 stable 通道之前會在此釋出。該功能從 v7.17beta2 開始可用。 |
| **firmware-file** (*string*；預設："" ) | 允許使用者覆蓋韌體更新源，在無法透過網際網路連線 MikroTik 升級伺服器進行升級的環境中（例如私有網路等），從自定義位置（檔案、URL）執行升級。 |

:::warning
在嘗試升級 LTE 調變解調器韌體之前 - 將 RouterOS 版本升級到最新版本 [如何升級 RouterOS](../getting-started/installation-and-upgrade/upgrade.md)
:::

##### 支援韌體更新且需要連線性的調變解調器 {#modems-with-firmware-update-support-and-connectivity-required}

使用命令 ***`/interface/lte/monitor [find]` 一次*** 獲取返回的屬性 "model"，以識別已安裝的調變解調器型號。

| 調變解調器 | 連線到 MikroTik 升級伺服器所需的連線性 |
| :-- | :-- |
| **EC200A-EU**  R11eL-EC200A-EU | 使用調變解調器 LTE 介面；使用任意 RouterOS 介面（7.18beta1+） |
| **EG06-A** | 使用任意 RouterOS 介面 |
| **EP06-A** | 使用任意 RouterOS 介面 |
| **EG12-EA** | 使用任意 RouterOS 介面 |
| **EG18-EA** | 使用任意 RouterOS 介面 |
| **FG621-EA**  R11eL-FG621-EA | 使用任意 RouterOS 介面 |
| **R11-LTE** | 使用調變解調器 LTE 介面 |
| **R11e-4G** | 使用任意 RouterOS 介面 |
| **R11e-LTE6** | 使用任意 RouterOS 介面 |
| **RG502Q-EA** | 使用任意 RouterOS 介面 |
| **RG520F-EU** | 使用任意 RouterOS 介面 |

##### 調變解調器 firmware-upgrade 命令示例 {#modem-firmware-upgrade-command-examples}

檢查是否有新的韌體更新可用

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1
  installed: EG12EAPAR01A13M4G_02.001.02.001
     latest: EG12EAPAR01A15M4G_01.201.01.201
```

檢查早期訪問/測試通道中是否有新的韌體更新可用

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1 update-channel=testing
  installed: EG12EAPAR01A15M4G_01.201.01.201
     latest: EG12EAPAR01A15M4G_01.203.01.203
```

安裝最新韌體

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1 upgrade=yes
```

從早期訪問/測試通道安裝最新韌體

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1 upgrade=yes update-channel=testing
```

從自定義位置（檔案或 HTTP URL）執行韌體升級。
在執行 `firmware-upgrade` 命令之前，介面必須處於 R（running）或 X（disabled）狀態。

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1 firmware-file=R11e-LTE6_V039_image upgrade=yes

[admin@D53G] > /interface/lte/firmware-upgrade lte1 firmware-file=http://firmwareserver.com/R11e-LTE6_V039_image upgrade=yes
```

##### 調變解調器 FOTA/DFOTA 下載 {#modem-fotadfota-downloads}

以下是我們調變解調器的所有最新韌體版本：
https://box.mikrotik.com/d/bfa49081454e4da1972d/

你可以使用這些 FOTA 檔案進行離線更新，或在無法訪問 MikroTik 升級伺服器以進行標準調變解調器韌體升級的環境中使用。

:::warning
在嘗試升級 LTE 調變解調器韌體之前，請將 RouterOS 升級到最新版本。[如何升級 RouterOS](../getting-started/installation-and-upgrade/upgrade.md)

LTE 調變解調器設計為儘可能拒絕不相容的 FOTA/DFOTA 韌體包。但是，手動韌體升級始終存在風險。安裝錯誤的韌體映象可能導致調變解調器故障、功能喪失或永久損壞，從而可能需要更換調變解調器。

不要中斷升級過程。在寫入韌體期間發生斷電、裝置重啟、調變解調器重設或任何其他中斷，都可能使調變解調器處於無法恢復的狀態。

使用者有責任確認韌體檔案適用於正在升級的確切調變解調器型號和硬體版本，並確保在整個升級過程中提供穩定的電源。對於因刷寫錯誤韌體檔案或中斷韌體升級過程而導致的任何損壞、功能喪失或其他問題，MikroTik 不承擔責任。
:::

###### FOTA 調變解調器 {#fota-modems}

FOTA（Firmware Over‑The‑Air，韌體空中更新）。這些調變解調器沒有源版本子資料夾。你可以從任何當前韌體版本安裝最新的調變解調器韌體。

| 調變解調器型號 | 註釋 |
|---|---|
| R11e-LTE | 調變解調器透過其 LTE 連線自行下載韌體（FOTA）。無法進行離線升級；如果你的設定中無法訪問 MikroTik 升級伺服器，你可以將韌體託管在調變解調器可訪問的某個 HTTP 伺服器上，並以此方式升級韌體 |
| R11e-LTE6 | - |
| R11l-LTE7 | - |
| R11e-4G | - |
| EC25-EU | 調變解調器韌體作為 NPK 包安裝 |
| EG25-G | 調變解調器韌體作為 NPK 包安裝 |
| SXT-LTE | 僅單一產品 - RBSXTLTE3-7。調變解調器韌體作為 NPK 包安裝 |

###### DFOTA 調變解調器 {#dfota-modems}

DFOTA（Delta Firmware Over‑The‑Air，增量韌體空中更新）。這些調變解調器具有按版本劃分的子資料夾 `modem/<model>/<currentVersion>/<targetVersion>_image`，其中 targetVersion 是從當前韌體版本可用的最新升級版本。如果你的當前韌體版本較舊，可能需要多步升級。

| 調變解調器型號 | 註釋 |
|---|---|
| EC200A-EU | 最新的 RouterOS v7 版本支援離線 DFOTA 升級。在較舊版本中，調變解調器透過其 LTE 連線自行下載韌體 |
| EP06-A | - |
| EG06-A | - |
| EG12-EA | - |
| EG18-EA | - |
| EG120K-EA | - |
| RG502Q-EA | - |
| RG520F-EU | - |
| RG520F-EUX | 適用於 ATL 5G R16（ATLGM&RG520F-EU）的特殊調變解調器韌體版本 |
| RG650E-EU | 此調變解調器使用 A/B 系統更新機制，而不是 DFOTA。由於完整韌體映象會寫入非活動系統分割區，因此韌體包明顯大於典型的 DFOTA 包 |
| FG621-EA | - |
| BG77 | PPP 序列調變解調器。`/interface/ppp-client/firmware-upgrade ppp-out1 upgrade=yes firmware-file=` |
| BG770A | PPP 序列調變解調器。`/interface/ppp-client/firmware-upgrade ppp-out1 upgrade=yes firmware-file=` |

#### 使用者 at-chat 命令 {#user-at-chat-command}

可以使用 `/interface/lte/at-chat` 命令向 LTE 介面傳送使用者定義的 "at-chat" 命令。

```ros
[admin@MikroTik] > /interface/lte/at-chat lte1 input="AT"
  output: OK
```

還可以在該命令中使用 "wait" 引數 *wait=yes*，使 "at-chat" 等待 5 秒並返回所有輸出，而不是僅返回首次接收到的資料。這對於某些返回多行輸出或大塊資料的命令很有用。

```ros
[admin@MikroTik] > /interface/lte/at-chat lte1 input="at+qcfg=?"
  output:

[admin@MikroTik] > /interface/lte/at-chat lte1 input="at+qcfg=?" wait=yes
  output: +QCFG: "rrc",(0-5)
          +QCFG: "hsdpacat",(6,8,10-24)
          +QCFG: "hsupacat",(5,6)
          +QCFG: "pdp/duplicatechk",(0,1)
          +QCFG: "risignaltype",("respective","physical")
          +QCFG: "lte/bandprior",(1-43),(1-43),(1-43)
          +QCFG: "volte_disable",(0,1)
          +QCFG: "diversity/config",(4,6),(1-4),(0)
          +QCFG: "div_test_mode",(0,1)
          +QCFG: "usbspeed",("20","30")
          +QCFG: "data_interface",(0,1),(0,1)
          +QCFG: "pcie/mode",(0,1)
          +QCFG: "pcie_mbim",(0,1)
          +QCFG: "sms_control",(0,1),(0,1)
          +QCFG: "call_control",(0,1),(0,1)
          +QCFG: "usb/maxpower",(0-900)
          +QCFG: "efratctl",(0,1)
          +QCFG: "netmaskset",(0,1)[,<netmask>]
          +QCFG: "mmwave",ant_chip,ant_type
          +QCFG: "gatewayset",(0,1)[,<gateway>]
          +QCFG: "clat",(0,1),(0,1),<prefix>,(0,32,40,48,56,64,96),<fqdn>,(0,1),(0,1,2,4,8),(0,1),(0,1),(0,1,2),(0,1,2)
          +QCFG: "usage/apmem"
          +QCFG: "enable_gea1"[,(0,1)]
          +QCFG: "dhcppktfltr",(0,1)
          OK
```

你也可以在指令碼中使用 "at-chat" 函式，並將命令輸出賦值給變數。

```ros
[admin@MikroTik] > :global "lte_command" [/interface/lte/at-chat lte1 input="AT+CEREG?" as-value ]
[admin@MikroTik] > :put $"lte_command"
output=+CEREG: 0,1
OK
```

### 快速設定示例 {#quick-setup-example}

從網路設定開始 - 在 LTE APN 配置檔案下新增新的連線引數（由網路提供商提供）：

```ros
/interface/lte/apn/add name=profile1 apn=phoneprovider.net authentication=chap password=web user=web
```

為 LTE 連線選擇新建立的配置檔案：

```ros
/interface/lte/set [find] apn-profiles=profile1
```

LTE 介面應以 running（R）標誌出現：

```ros
[admin@MikroTik] > /interface/lte/print
Flags: X - disabled, R - running
0 R name="lte1" mtu=1500 mac-address=AA:AA:AA:AA:AA:AA
```

如有需要，為 LTE 介面新增 NAT Masquerade，以便將網際網路接入本地網路：

```ros
/ip/firewall/nat/add action=masquerade chain=srcnat out-interface=lte1
```

新增介面後，你可以使用 "info" 命令檢視用戶端獲取了哪些引數（返回的引數取決於 LTE 硬體裝置）：

```
[admin@MikroTik] > /interface/lte/monitor lte1
            status: connected
             model: EG18-EA
          revision: EG18EAPAR01A12M4G
  current-operator: LMT
    current-cellid: 3103242
            enb-id: 12122
         sector-id: 10
        phy-cellid: 480
        data-class: LTE
    session-uptime: 15m54s
              imei: 86981604098XXXX
              imsi: 24701060267XXXX
              iccid: 8937101122102057XXXX
      primary-band: B3@20Mhz earfcn: 1300 phy-cellid: 480
     dl-modulation: qpsk
               cqi: 7
                ri: 2
               mcs: 1
              rssi: -68dBm
              rsrp: -97dBm
              rsrq: -9dB
              sinr: 6dB
```

### 直通示例 {#passthrough-example}

某些 LTE 介面支援 LTE 直通功能，其中 IP 配置會直接應用到用戶端裝置。在這種情況下，調變解調器韌體負責 IP 配置，路由器僅用於配置調變解調器設定 - APN、網路技術和 IP 型別。在此配置中，路由器不會從調變解調器獲取 IP 配置。如果調變解調器支援，LTE 直通調變解調器可以同時傳遞 IPv4 和 IPv6 地址。某些調變解調器支援多個 APN，你可以將每個 APN 的流量傳遞到特定的路由器介面。

直通僅適用於一臺主機。路由器會自動檢測第一個接收到的封包的 MAC 地址，並將其用於直通。如果網路中有多臺主機，可以將直通鎖定到特定 MAC。在直通提供 IP 的網路主機上，該介面也應啟用 DHCP 用戶端。請注意，將無法透過公共 LTE IP 地址或從直通所使用的主機連線到 LTE 路由器。建議為配置目的建立一條從 LTE 路由器到該主機的額外連線。例如，在 LTE 路由器和主機之間建立 VLAN 介面。

要啟用直通，需要在 `/interface/lte/apn` 選單中新增條目或更改預設條目

:::warning
並非所有晶片組都支援 Passthrough。
要檢查您的調變解調器是否支援 Passthrough：

```ros
/interface/lte/show-capabilities [find]
```
:::

#### 示例 {#examples}

要在 ether1 上配置直通：

```ros
[admin@MikroTik] > /interface/lte/apn/add apn=apn1 passthrough-interface=ether1
[admin@MikroTik] > /interface/lte/set lte1 apn-profiles=apn1
```

要在 ether1 主機 00:0C:42:03:06:AB 上配置直通：

```ros
[admin@MikroTik] > /interface/lte/apn/add apn=apn1 passthrough-interface=ether1 passthrough-mac=00:0C:42:03:06:AB
[admin@MikroTik] > /interface/lte/set lte1 apn-profiles=apn1
```

要在 ether1 和 ether2 上配置多個 APN：

```ros
[admin@MikroTik] > /interface/lte/apn/add apn=apn1 passthrough-interface=ether1
[admin@MikroTik] > /interface/lte/apn/add apn=apn2 passthrough-interface=ether2
[admin@MikroTik] > /interface/lte/set lte1 apn-profiles=apn1,apn2
```

要為不同介面配置具有相同 APN 的多個 APN：

```ros
[admin@MikroTik] > /interface/lte/apn/add name=interface1 apn=apn1
[admin@MikroTik] > /interface/lte/apn/add name=interface2 apn=apn1 passthrough-interface=ether1
[admin@MikroTik] > /interface/lte/set lte1 apn-profiles=interface1
[admin@MikroTik] > /interface/lte/set lte2 apn-profiles=interface2
```

此外，你可以透過在同一 passthrough-interface 上手動建立 DHCP 伺服器，來覆蓋預設的動態 DHCP 伺服器引數/選項。例如，預設租期為 1 分鐘：

```routeros
[admin@MikroTik] > /ip/dhcp-server/print detail
Flags: D - dynamic; X - disabled, I - invalid
 0 D  name="apn2" interface=ether2 lease-time=1m address-pool=static-only use-radius=no lease-script="" address-lists=""
```

現在，如果你想將租期更改為例如 30 分鐘，則可以在 passthrough-interface（在此例中為 ether2）上建立新的 DHCP 伺服器：

```routeros
[admin@MikroTik] > /ip/dhcp-server/add interface=ether2 name=dhcp1 lease-time=30m
[admin@MikroTik] > /ip/dhcp-server/print detail
Flags: D - dynamic; X - disabled, I - invalid
 0    name="dhcp1" interface=ether2 lease-time=30m address-pool=static-only use-radius=no lease-script="" address-lists=""
```

### 雙 SIM {#dual-sim}

#### 具有可切換 SIM 插槽的板卡 {#boards-with-switchable-sim-slots}

| RouterBoard | 調變解調器插槽 | SIM 插槽 1 | SIM 插槽 2 | 可切換 |
| :-- | :-- | :-- | :-- | :-- |
| LtAP | lower | 2 | 3 | Y |
|  | upper | 1 |  | N |
| LtAP mini |  | 上 | 下 | Y |
| SXT R |  | a | b | Y |
| ATL 5G |  | sim | esim | Y |

SIM 插槽切換命令

- RouterOS v7

```ros
/interface/lte/settings/set sim-slot=down
```

- RouterOS v6 6.45.1 之後

```ros
/system/routerboard/modem/set sim-slot=down
```

- RouterOS v6 6.45.1 之前：

```ros
/system/routerboard/sim/set sim-slot=down
```

更多參考資訊，請參閱板卡框圖、快速指南和使用者手冊。

#### 使用示例 {#usage-example}

請訪問此連結 - [雙 SIM 應用](./dual-sim-application.md)，檢視如何藉助 RouterOS 指令碼和排程器，根據漫遊狀態以及介面狀態為 down 時更改 SIM 插槽的示例。

### 技巧與提示 {#tips-and-tricks}

本段包含有關附加功能和使用場景的資訊。

#### 使用小區資訊查詢裝置位置 {#find-device-location-using-cell-information}

在使用 R11e-LTE 國際版卡（wAP LTE kit）的裝置上，info 命令下會提供一些額外資訊。

```
   current-operator: 24701
                lac: 40
     current-cellid: 2514442
```

| 屬性 | 描述 |
| :-- | :-- |
| **current-operator** (*integer*；預設： ) | 包含 MCC 和 MNC。例如：current-operator: 24701 分解為：MCC=247 MNC=01 |
| **lac** (*integer*；預設： ) | 位置區程式碼（LAC） |
| **current-cellid** (*integer*；預設： ) | 站標識號 |

可以使用這些值在資料庫中查詢位置：[Cell Mapper](http://www.cellmapper.net)

#### 使用小區鎖定 {#using-cell-lock}

可以將 R11e-LTE、R11e-LTE6 和 R11e-4G 調變解調器及配備這些調變解調器的裝置鎖定到確切的 LTE 基站。LTE info 命令提供當前使用的蜂窩基站資訊：

```
         phy-cellid: 384
             earfcn: 1300 (band 3, bandwidth 20Mhz)
```

| 屬性 | 描述 |
| :-- | :-- |
| **phy-cellid** (*integer*；預設： ) | 當前使用的蜂窩基站的物理小區標識（PCI）。 |
| **earfcn** (*integer*；預設： ) | 絕對無線頻率通道號 |

確切的基站位置以及可用頻段和其他資訊可以從移動運營商處獲取，也可以透過線上服務獲取：

[CellMapper](https://www.cellmapper.net/map)

使用這些獲取的變數，可以按以下格式向調變解調器傳送 AT 命令以鎖定到基站：

**適用於 R11e-LTE 和 R11e-LTE6**

```
AT*Cell=<mode>,<NetworkMode>,<band>,<EARFCN>,<PCI>

where

<mode> :
0 – Cell/Frequency disabled
1 – Frequency lock enabled
2 – Cell lock enabled

<NetworkMode>
0 – GSM
1 – UMTS_TD
2 – UMTS_WB
3 – LTE

<band>
Not in use, leave this blank

<EARFCN>
earfcn from lte info

<PCI>
phy-cellid from lte info
```

要鎖定調變解調器到之前使用的基站，可以使用 at-chat：

```ros
/interface/lte/at-chat lte1 input="AT*Cell=2,3,,1300,384"
```

對於 R11e-LTE，所有已設定的鎖定都會在重啟或調變解調器重設後丟失。小區資料也可以透過 "cell-monitor" 收集。

對於 R11e-LTE6，小區鎖定僅適用於主頻段。如果你在同一頻段上有多個通道，並希望將其鎖定到特定 earfcn，這會很有用。請注意，小區鎖定不特定於頻段，對於 ca-band，它也可以使用其他頻段，除非你使用頻段鎖定。

使用小區鎖定將主頻段設定為 1300 earfcn，並將第二個通道用於 ca-band：

```ros
/interface/lte/at-chat lte1 input="AT*Cell=2,3,,1300,138"
```

現在主通道使用 earfcn: 1300：

```
         primary-band: B3@20Mhz earfcn: 1300 phy-cellid: 138
              ca-band: B3@5Mhz earfcn: 1417 phy-cellid: 138
```

你也可以反過來設定：

```ros
/interface/lte/at-chat lte1 input="AT*Cell=2,3,,1417,138"
```

現在主通道使用 earfcn: 1417：

```
         primary-band: B3@5Mhz earfcn: 1417 phy-cellid: 138
              ca-band: B3@20Mhz earfcn: 1300 phy-cellid: 138
```

對於 R11e-LTE6 調變解調器，小區鎖定資訊在重啟或調變解調器重設後不會丟失。要移除小區鎖定，請使用 at-chat 命令：

```ros
/interface/lte/at-chat lte1 input="AT*Cell=0"
```

**適用於 R11e-4G**

```
AT%CLCMD=<mode>,<mode2>,<EARFCN>,<PCI>,<PLMN>
AT%CLCMD=1,1,3250,244,\"24705\"

where

<mode> :
0 – Cell/Frequency disabled
1 – Cell lock enabled

<mode2> :
0 - Save lock for first scan
1 - Always use lock
(after each reset modem will clear out previous settings no matter what is used here)

<EARFCN>
earfcn from lte info

<PCI>
phy-cellid from lte info

<PLMN>
Mobile operator code
```

所有 PLMN 程式碼見[此處](https://en.wikipedia.org/wiki/Mobile_country_code)。此變數也可以留空

要將調變解調器鎖定到小區 - 調變解調器需要處於非執行狀態，對於 **R11e-4G** 調變解調器，最簡單的方法是在 "modem-init" 字串中新增 CellLock 行：

```ros
/interface/lte/set lte1 modem-init="AT%CLCMD=1,1,3250,244,\"24705\""
```

也可以透過提供列表而不是一個基站資訊來新增多個小區，格式如下：

```
AT%CLCMD=<mode>,<mode2>,<EARFCN_1>,<PCI_1>,<PLMN_1>,<EARFCN_2>,<PCI_2>,<PLMN_2>
```

例如，要鎖定到同一頻段和運營商內的兩個不同 PCI：

```ros
/interface/lte/set lte1 modem-init="AT%CLCMD=1,1,6300,384,\"24701\",6300,385,\"24701\""
```

**適用於 Chateau LTE12、Chateau LTE18、Chateau 5G、Chateau 5G R16、LHG LTE18、ATL LTE18、ATL 5G R16、Chateau 5G R17 ax**

```
AT+QNWLOCK="common/4g",<num of cells>,[[<freq>,<pci>],...]
AT+QNWLOCK=\"common/4g\",1,6300,384

where

<num of cells>
number of cells to cell lock

<freq>
earfcn from lte info

<pci>
phy-cellid from lte info

```

單小區鎖定示例：

```ros
/interface/lte/at-chat lte1 input="AT+QNWLOCK=\"common/4g\",1,3050,448"
```

查詢當前配置：

```ros
/interface/lte/at-chat lte1 input="AT+QNWLOCK=\"common/4g\""
```

也可以將多個小區新增到小區鎖定中。例如，要鎖定到兩個不同的小區：

```ros
/interface/lte/at-chat lte1 input="AT+QNWLOCK=\"common/4g\",2,3050,448,1574,474"
```

要移除小區鎖定，請使用此 at-chat 命令：

```ros
/interface/lte/at-chat lte1 input="at+qnwlock=\"common/4g\",0"
```

:::warning

1. 重啟或調變解調器復位後，小區鎖定資訊將不會被儲存。2. AT+QNWLOCK 命令可以鎖定小區和頻率。因此，可以優先讓模組註冊到鎖定小區；但是，根據 3gpp 協定，模組會被重定向或切換到訊號指示更好的小區，即使該小區不在該命令的鎖定範圍內。此現象是正常的。
:::

**對於支援 5G 的裝置，也可以鎖定 5G SA 小區**

```
AT+QNWLOCK="common/5g",<pci>,<freq>,<scs>,<band>
AT+QNWLOCK=\"common/5g\",901,504990,30,41

where
<pci> String type. Cell physical ID. 0 indicates disabling locking module to the specified cell.
<freq> Integer type. Cell frequency (earfcn).
<scs> Integer type. NR sub carrier space. Unit: kHz. For FR1(Sub-6 GHz) FDD band, please set <scs> to 15; for FR1 TDD band, please set <scs> to 30. Otherwise, an error code may be returned.
15
30
<band> Integer type. NR5G frequency band.
```

鎖定到 TDD n78 頻段且 earfcn=628032、phy-cellid=138 的小區鎖定示例：

```ros
/interface/lte/at-chat lte1 input="AT+QNWLOCK=\"common/5g\",138,628032,30,78"
```

查詢當前配置：

```ros
[admin@MikroTik] > /interface/lte/at-chat lte1 input="AT+QNWLOCK=\"common/5g\""
  output: +QNWLOCK: "common/5g",138,628032,30,78
          OK
```

要移除小區鎖定，請使用此 at-chat 命令：

```ros
/interface/lte/at-chat lte1 input="AT+QNWLOCK=\"common/5g\",0"
```

:::warning

1. 重啟或調變解調器復位後，小區鎖定資訊將不會被儲存。

2. AT+QNWLOCK 命令可以鎖定小區和頻率。因此，可以優先讓模組註冊到鎖定小區；但是，根據 3gpp 協定，模組會被重定向或切換到訊號指示更好的小區，即使該小區不在該命令的鎖定範圍內。此現象是正常的。

3. 鎖定小區時，請確保模組支援鎖定小區對應的頻段，否則將返回錯誤程式碼。

4. AT+QNWLOCK="common/5g" 不支援鎖定 NSA 的 5G 小區。（你仍可使用 AT+QNWLOCK="common/4g" 命令鎖定到 lte 錨定小區。）

5. 此寫命令只能在模組處於全功能模式（lte 介面未停用）時執行。

6. 不建議將此命令用於商業用途。
:::

**適用於 FG621-EA**

```
AT+GTCELLLOCK=<mode>[,<rat>,<type>,<earfcn>[,<PCI>]]

where

< mode >: integer type; 0 Disable this function 1 Enable this function 2 Add new cell to be locked

<rat>: integer type; 0 LTE 1 WCDMA

<type>: integer type; 0 Lock PCI 1 Lock frequency

<earfcn>: integer type; the range is 0-65535.

<PCI>: integer type; If second parameter value is 0, the range is 0-503 for LTE If second parameter value is 1, the range is 0-512 for WCDMA
```

示例：

```ros
/interface/lte/at-chat lte1 input="AT+GTCELLLOCK=1,0,0,6175,176"
```

#### 小區監控 {#cell-monitor}

小區監控允許掃描附近可用的行動網路小區：

```ros
[admin@MikroTik] > /interface/lte/cell-monitor lte1
PHY-CELLID BAND         PSC EARFCN                 RSRP          RSRQ          RSSI         SINR
        49 B20              6300                -110dBm       -19.5dB
       272 B20              6300                -116dBm       -19.5dB
       374 B20              6300                -108dBm         -16dB
       384 B1               150                 -105dBm       -13.5dB
       384 B3               1300                -106dBm         -12dB
       384 B7               2850                -107dBm       -11.5dB
       432 B7               2850                -119dBm       -19.5dB
```

收集到的資料可用於更精確的位置檢測或小區鎖定。

:::warning
並非所有調變解調器都支援此功能
:::

### 故障排除 {#troubleshooting}

#### 啟用 LTE 日誌記錄 {#enable-lte-logging}

```ros
[admin@MikroTik] > /system/logging/add topics=lte
```

#### 檢查日誌中的錯誤 {#check-for-errors-in-log}

```ros
[admin@MikroTik] > /log/print

11:08:59 lte,async lte1: sent AT+CPIN?
11:08:59 lte,async lte1: rcvd +CME ERROR: 10
```

線上搜尋 CME 錯誤描述，

在本例中：CME error 10 - SIM not inserted

#### 在 Huawei 和其他調變解調器上鎖定頻段 {#locking-band-on-huawei-and-other-modems}

要為 Huawei 調變解調器鎖定頻段，不能使用 `/interface/lte/set lte1 band=""` 選項。

可以使用 AT 命令手動鎖定到所需頻段。

要檢查所有支援的頻段，請執行 at-chat 命令：

```ros
[admin@MikroTik] /interface/lte/at-chat lte1 input="AT^SYSCFGEX=\?"

output: ^SYSCFGEX: ("00","03","02","01","99"),((2000004e80380,"GSM850/GSM900/GSM1800/GSM1900/WCDMA BCI/WCDMA BCII/WCDMA BCV/WCDMA BCVIII"),
(3fffffff,"All Bands")),(0-2),(0-4),((800d7,"LTE BC1/LTE BC2/LTE
BC3/LTE BC5/LTE BC7/LTE BC8/LTE BC20"),(7fffffffffffffff,"All Bands"))
OK

```

鎖定到 LTE 頻段 7 的示例：

```ros
[admin@MikroTik] /interface/lte/set lte1 modem-init="AT^SYSCFGEX=\"03\",3FFFFFFF,2,4,40,,"
```

將最後部分 **40** 更改為所需頻段指定的十六進位制值，其中：

```
4 LTE BC3
40 LTE BC7
80000 LTE BC20
7FFFFFFFFFFFFFFF  All bands
etc
```

所有頻段 HEX 值和 AT 命令可在 [Huawei AT Command Interface Specification guide](https://download-c.huawei.com/download/downloadCenter?downloadId=29741&version=72288&siteCode=) 中找到

檢查頻段是否已鎖定：

```ros
[admin@MikroTik] /interface/lte/at-chat lte1 input="AT^SYSCFGEX\?"

output: ^SYSCFGEX: "03",3FFFFFFF,0,2,40
OK
```

更多資訊請查閱調變解調器製造商的 AT 命令參考手冊。

#### 搭配 RB9xx 系列裝置的 mPCIe 調變解調器 {#mpcie-modems-with-rb9xx-series-devices}

如果調變解調器在軟重啟後未被識別，則可能需要在 USB 埠初始化之前新增延遲。可以使用以下命令完成：

```ros
/system/routerboard/settings/set init-delay=5s
```

#### 具有 USB-A 埠和 mPCIe 的板卡 {#boards-with-usb-a-port-and-mpcie}

某些裝置（例如特定的 RB9xx 和 RBLtAP-2HnD）在單個 mPCIe 插槽和 USB-A 埠之間共享相同的 USB 線路。如果未進行自動切換且調變解調器未被檢測到，你可能需要手動切換為使用 USB-A 或 mini-PCIe：

```ros
/system/routerboard/usb/set type=mini-PCIe
```

#### 避免網路共享速度限制 {#avoiding-tethering-speed-throttling}

某些運營商僅對使用 SIM 卡的裝置允許無限資料，來自移動熱點或網路共享的所有其他資料都會在流量或吞吐速度上受到高度限制。一些來源發現，此限制是透過監控封包的 TTL（Time To Live）值來確定是否需要應用限制（每經過一個“跳”TTL 減 1）。RouterOS 允許更改從路由器發出的封包的 TTL 引數，以隱藏子網。請記住，這可能與公平使用政策衝突。

```ros
IPv4 mangle rule:
/ip/firewall/mangle
add action=change-ttl chain=postrouting new-ttl=set:65 out-interface=lte1 passthrough=yes
IPv6 mangle rule:
/ipv6/firewall/mangle
add action=change-hop-limit chain=postrouting new-hop-limit=set:65 passthrough=yes
```

#### 多次輸入錯誤 PIN 碼後解鎖 SIM 卡 {#unlocking-sim-card-after-multiple-wrong-pin-code-attempts}

鎖定 SIM 卡後，可以透過 "at-chat" 解鎖

檢查當前 PIN 碼狀態：

```ros
/interface/lte/at-chat lte1 input="at+cpin\?"
```

如果卡已鎖定 - 透過提供以下內容解鎖：

```ros
/interface/lte/at-chat lte1 input="AT+CPIN=\"PUK_code\",\"NEW_PIN\""
```

將 PUK\_code 和 NEW\_PIN 替換為匹配的值。

:::warning
SIM 插槽選擇命令在 v6.45.1 中發生變化，並在 v7 中再次變化。某些裝置型號（如 SXT）的 SIM 插槽命名為 "a" 和 "b"，而不是 "up" 和 "down"
:::
