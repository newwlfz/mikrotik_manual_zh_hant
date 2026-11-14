---
sidebar_key: "wired-connections/ethernet"
sidebar_position: 1
title: "乙太網"
sidebar_label: "乙太網"
description: "MikroTik RouterOS 支援從 10Mbps 到 100Gbps 的多種乙太網介面，包括銅纜和光纖選項以及 combo 介面。它可以控制鏈路速率、雙工模式、自動協商，並可透過手動 advertise 設定配置 SFP/QSFP 介面，以精確指定鏈路模式。"
tags:
  - 'ethernet'
  - 'auto-negotiation'
  - 'link-modes'
source: https://manual.mikrotik.com/docs/7.24/wired-connections/ethernet
captured_at: '2026-11-04T11:35:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MikroTik RouterOS 支援多種型別的乙太網介面——從 10Mbps 到 10Gbps 的雙絞銅線乙太網，到 1Gbps、10Gbps、25Gbps 的 SFP/SFP+/SFP28 介面，以及 40Gbps、100Gbps、200Gbps、400Gbps 的 QSFP+/QSFP28/QSFP56/QSFP56-DD 介面。某些 RouterBoard 裝置配備 combo 介面，該介面同時包含兩種介面型別（例如雙絞線乙太網和 SFP/SFP+ 介面），允許選擇最合適的選項或建立物理鏈路故障轉移。透過 RouterOS，可以控制各種與乙太網相關的屬性，如鏈路速度、自動協商、雙工模式等，監控收發器診斷資訊，並檢視各種與乙太網相關的統計資訊。

:::info
有關 MikroTik SFP 和 QSFP 型別介面及其相容性的更多資訊，請參閱[有線介面相容性](./mikrotik-wired-interface-compatibility.md)頁面。
:::

## 自動協商和強制鏈路模式 {#auto-negotiation-and-forced-link-mode}

自動協商是一種通訊方法，也是一組由透過雙絞線電纜連線的乙太網裝置所採用的步驟。它使這些裝置能夠就關鍵傳輸設定達成一致，包括速度、雙工模式和流控制。在此過程中，連線的裝置首先交換有關這些設定的能力資訊。之後，它們共同選擇雙方都能有效支援的最佳傳輸模式。

然而，在 RouterOS 中，SFP/QSFP 埠上的自動協商行為與標準 RJ45 乙太網埠不同。對於 SFP/QSFP 介面，協商過程不涉及交換通告的能力（不共享通告位）。相反，RouterOS 會嘗試使用每一側支援的最高模式來建立鏈路。要成功連線，兩臺裝置必須通告相同的最高公共模式。

## 示例 {#for-example}

- 裝置 A 通告 `10G-baseCR` 和 `25G-baseCR`。
- 裝置 B 僅通告 `10G-baseCR`。

在這種情況下，鏈路將無法建立，因為裝置 A 優先使用 25G，而裝置 B 僅通告 10G。

## 確保鏈路成功 {#to-ensure-a-successful-link}

- 裝置 A 和裝置 B 必須具有相同的最高通告模式。  
  因此，如果裝置 B 通告 `25G-baseCR`，並且裝置 A 也包含 `25G-baseCR` 作為其最高通告，則鏈路將建立。

總之，在配置 SFP/QSFP 介面時，請確保兩端的最高支援模式匹配，以確保正確建立鏈路。

### 通告 {#advertise}

在 RouterOS 7.12 版本之前，當啟用自動協商時，介面會嘗試猜測另一端介面的最大可用速度（這使得 advertise 設定不適用於 SFP/QSFP 介面）。

在 RouterOS 7.12 版本之後，現在可以手動設定 advertise 位，以指定要使用的所需鏈路模式。速度引數也已修訂，以提供更清晰的表示，因為之前的值過於模糊。此外，full-duplex 設定已被移除，因為新的鏈路模式已經包含雙工選項（見下表）。

| 鏈路模式（用於 advertise 和 speed 屬性） | 描述 |
| :-- | :-- |
| 10M-baseT-half | 10M 雙絞線半雙工 |
| 10M-baseT-full | 10M 雙絞線全雙工 |
| 100M-baseT-half | 100M 雙絞線半雙工 |
| 100M-baseT-full | 100M 雙絞線全雙工 |
| 100M-baseFX-full | 100M 光纖 |
| 1G-baseT-half | 1G 雙絞線半雙工 |
| 1G-baseT-full | 1G 雙絞線全雙工 |
| 1G-baseX | 1G 光纖 |
| 2.5G-baseT | 2.5G 雙絞線全雙工 |
| 2.5G-baseX | 2.5G 光纖 |
| 5G-baseT | 5G 雙絞線全雙工 |
| 10G-baseT | 10G 雙絞線全雙工 |
| 10G-baseSR-LR | 10G 光纖 |
| 10G-baseCR | 10G 雙軸銅纜 |
| 40G-baseSR4-LR4 | 4x10G 光纖 |
| 40G-baseCR4 | 4x10G 雙軸銅纜 |
| 25G-baseSR-LR | 25G 光纖 |
| 25G-baseCR | 25G 雙軸銅纜 |
| 50G-baseSR2-LR2 | 2x25G 光纖 |
| 50G-baseCR2 | 2x25G 雙軸銅纜 |
| 100G-baseSR4-LR4 | 4x25G 光纖 |
| 100G-baseCR4 | 4x25G 雙軸銅纜 |
| 50G-baseSR-LR | 50G 光纖 |
| 50G-baseCR | 50G 雙軸銅纜 |
| 100G-baseSR2-LR2 | 2x50G 光纖 |
| 100G-baseCR2 | 2x50G 雙軸銅纜 |
| 200G-baseSR4-LR4 | 4x50G 光纖 |
| 200G-baseCR4 | 4x50G 雙軸銅纜 |
| 400G-baseSR8-LR8 | 8x50G 光纖 |
| 400G-baseCR8 | 8x50G 雙軸銅纜 |

:::info
**鏈路模式命名方案**

**傳輸速率**：第一個數字後跟 'M' 或 'G'（例如 10M、100M、1G）表示以兆位元或吉位元每秒為單位的資料傳輸速率。

**介面型別**："base" 後面的符號表示介面型別：

- **T**：代表雙絞線電纜，後面跟雙工模式（半雙工或全雙工）。
- **SR-LR**：代表“短距離”和“長距離”光模組，包括 LRM、ER、ZR 等其他變體。這些鏈路模式應與光模組一起使用。
- **CR**：代表雙軸銅纜，與直連銅纜（DAC）一起使用。對於 1Gbps DAC，合適的鏈路模式是 1G-baseX。
- **FX:** 代表光纖電纜上的快速乙太網。這還包括 LX——長波長標準。

**線路數量**：

- **SR2-LR2/CR2**：表示兩條線路。
- **SR4-LR4/CR4**：表示四條線路。
- **SR8-LR8/CR8:** 表示八條線路。

:::

在手動配置介面的 advertise 位之前，請先透過執行命令 `/interface/ethernet/monitor` 並檢查 "supported" 列表來確定支援哪些位。您還可以在 "sfp-supported" 欄位下檢視收發器支援的 advertise 位。此外，"advertising" 將顯示 RouterOS 已自動設定的位。該列表是透過比較介面和收發器上的最大可用鏈路模式值並選擇匹配的值生成的。

```ros
[admin@MikroTik] > /interface/ethernet/monitor qsfp28-1-1
                      name: qsfp28-1-1
                 supported: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full,
                            1G-baseX,2.5G-baseT,2.5G-baseX,5G-baseT,10G-baseT,10G-baseSR-LR,10G-baseCR,40G-baseSR4-LR4,
                            40G-baseCR4,25G-baseSR-LR,25G-baseCR,50G-baseSR2-LR2,50G-baseCR2,100G-baseSR4-LR4,100G-baseCR4
             sfp-supported: 10G-baseSR-LR,25G-baseSR-LR,100G-baseSR4-LR4
               advertising: 10G-baseSR-LR,25G-baseSR-LR,100G-baseSR4-LR4
... 
```

手動設定 advertise 設定的一個應用場景是 QSFP 下的所有子介面。整體配置過程從最上方已啟用的埠開始。如果所選模式有效且受支援，則將應用該模式。如果該特定鏈路模式需要多個通道，則下一個介面的 advertise 和 speed 配置將被忽略，但該介面應保持 **enabled**。下一個可用的空閒通道或埠遵循類似過程。

```ros
/interface/ethernet
set [ find default-name=qsfp28-1-1 ] advertise=50G-baseCR2
set [ find default-name=qsfp28-1-3 ] advertise=25G-baseCR
set [ find default-name=qsfp28-1-4 ] advertise=25G-baseCR
```

:::warning
**注意**：多通道介面鏈路模式（50G-baseCR2、50G-baseSR2-LR2）不能配置到單通道介面（SFP28/SFP56）上。

IEEE 802.3az 節能乙太網（EEE）功能在我們所有產品上均被停用。沒有選項可以手動啟用或停用 EEE 設定。
:::

### 乙太網 LED 行為 {#ethernet-led-behavior}

#### 綠色 LED（鏈路/速度） {#green-led-linkspeed}

- 亮（常亮）——最高速率

#### 黃色/琥珀色 LED（活動/速度） {#yellowamber-led-activityspeed}

- 亮（常亮）——鏈路已建立。  
- 滅——無鏈路。  
- 閃爍——正在傳輸資料。

### 強制模式 {#forced-mode}

在連線 DAC 電纜或光模組後，日誌記錄中出現警告訊息的情況下，例如：

```ros
10:20:47 interface,warning sfp-sfpplus1 module auto-initialization failed, try forced-mode
```

這可能表示所連線的電纜或模組具有損壞或錯誤的 EEPROM 校驗和，從而導致自動連線配置失敗。此功能在 RouterOS 7.12 版本中引入，可能會影響某些過去因錯誤假設模組/電纜屬性而誤工作的鏈路，這可能導致與鏈路連線和裝置功能相關的各種問題。

在這種情況下，您可以嘗試手動設定鏈路模式，這可能有助於建立可工作的鏈路。以下提供了強制埠設定示例：

- 對於 DAC 電纜以及 1G/10G/25G 的連線速度。

```ros
/interface/ethernet
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=1G-baseX
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=10G-baseCR
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=25G-baseCR
```

:::info
注意：在選擇介面速度設定時，請注意您的 DAC 電纜支援哪些速率（檢查電纜規格資料）
:::

- 對於光模組以及 1G/10G/25G 的連線速度。

```ros
/interface/ethernet
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=1G-baseX
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=10G-baseSR-LR
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=25G-baseSR-LR
```

:::warning
注意：在選擇介面速度設定時，請注意您的光模組支援哪些速率（檢查模組規格資料）

具有錯誤 EEPROM 校驗和的模組不會向乙太網監視器輸出任何 EEPROM 資訊，這也意味著 SFP DDM 監視器對此類模組不起作用。
:::

### FEC {#fec}

FEC（前向糾錯）是一種數字訊號處理方法，它透過在傳送端向資料新增資訊（奇偶校驗位）來改善 SFP28、QSFP+ 和 QSFP28 鏈路的誤位元速率。然後接收端使用此資訊來檢測並糾正傳輸期間可能引入的錯誤。

為確保鏈路成功，鏈路兩端應使用相同的 *fec-mode*。RouterOS 預設將 *fec-mode* 設定為停用，但可以更改為 *fec74*（也稱為 FC-FEC）或 *fec91*（也稱為 RS-FEC）。有關 FEC 模式選項的更多資訊，請參閱[屬性](./ethernet.md#properties)說明。下表顯示了鏈路模式和支援的 FEC 模式：

| 鏈路模式（用於 advertise 和 speed 屬性） | 支援的 FEC 模式 |
| :-- | :-- |
| 40G-baseSR4-LR4 | fec74 |
| 40G-baseCR4 | fec74 |
| 25G-baseSR-LR | fec74, fec91\* |
| 25G-baseCR | fec74, fec91\* |
| 50G-baseSR2-LR2 | fec74, fec91 |
| 50G-baseCR2 | fec74, fec91 |
| 100G-baseSR4-LR4 | fec91 |
| 100G-baseCR4 | fec91 |
| 50G-baseSR-LR | fec91（必需） |
| 50G-baseCR | fec91（必需） |
| 100G-baseSR2-LR2 | fec91（必需） |
| 100G-baseCR2 | fec91（必需） |
| 200G-baseSR4-LR4 | fec91（必需） |
| 200G-baseCR4 | fec91（必需） |
| 400G-baseSR8-LR8 | fec91（必需） |
| 400G-baseCR8 | fec91（必需） |

:::warning
**注意**：CCR2004-1G-2XS-PCIe 裝置不支援 SFP28 介面上的 fec91。
:::

## 屬性 {#properties}

**子選單：** `/interface/ethernet`

本節介紹乙太網介面配置選項。

| 屬性 | 描述 |
| :-- | :-- |
| <strong>advertise</strong>（自 RouterOS v7.12 起：<em>10M-baseT-half &#124; 10M-baseT-full&#124; 100M-baseT-half &#124; 100M-baseT-full &#124; 1G-baseT-half &#124; 1G-baseT-full &#124; 1G-baseX &#124; 2.5G-baseT &#124; 2.5G-baseX &#124; 5G-baseT &#124; 10G-baseT &#124; 10G-baseSR-LR &#124; 10G-baseCR &#124; 40G-baseSR4-LR4 &#124; 40G-baseCR4 &#124; 25G-baseSR-LR &#124; 25G-baseCR &#124; 50G-baseSR2-LR2 &#124; 50G-baseCR2 &#124; 100G-baseSR4-LR4 &#124; 100G-baseCR4;</em> 預設值：）<br/>（較舊版本的 RouterOS：<em>10M-full &#124; 10M-half &#124; 100M-full &#124; 100M-half &#124; 1000M-full &#124; 1000M-half &#124; 2500M-full &#124; 5000M-full &#124; 10000M-full</em>；預設值：） | 通告的鏈路模式，僅在啟用自動協商時生效。通告高於介面實際支援速度的值可能導致未定義的行為。允許使用多個選項。 |
| **arp**（*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*；預設值：**enabled**） | 地址解析協定模式：<ul><li>disabled - 介面將不使用 ARP</li><li>enabled - 介面將使用 ARP</li><li>local-proxy-arp - 路由器在介面上執行代理 ARP，並將回覆傳送到同一介面</li><li>proxy-arp - 路由器在介面上執行代理 ARP，並將回覆傳送到其他介面</li><li>reply-only - 介面僅回覆源自與 [ARP](../network-management/arp.md) 表中靜態條目相匹配的 IP 地址/MAC 地址組合的請求。動態條目不會被自動儲存到 ARP 表中。因此，為使通訊成功，必須已存在有效的靜態條目。</li></ul> |
| **arp-timeout**（*auto \| integer*；預設值：**auto**） | 在未從該 IP 收到封包後，ARP 記錄在 ARP 表中保有的時長。值 `auto` 等同於 IP/Settings 中的 `arp-timeout` 值，預設為 30s。 |
| **auto-negotiation**（*yes \| no*；預設值：**yes**） | 啟用後，介面會“通告”其最大能力，以實現儘可能最佳的連線。<ul><li><strong>注意1：</strong> 不應僅在一端停用自動協商，否則乙太網介面可能無法正常工作。</li><li><strong>注意2：</strong> 千兆乙太網和 NBASE-T 乙太網鏈路在停用自動協商的情況下無法工作。</li></ul> |
| **bandwidth**（*integer/integer*；預設值：**unlimited/unlimited**） | 設定介面將處理的最大 rx/tx 頻寬（以 kbps 為單位）。所有 Atheros [switch-chip](../bridging-and-switching/switch-chip-features.md) 埠均支援 TX 限制。僅 Atheros8327/QCA8337 switch-chip 埠支援 RX 限制。 |
| **cable-setting**（*default \| short \| standard*；預設值：**default**） | 更改線纜長度設定（僅適用於 NS DP83815/6 卡） |
| **combo-mode**（*auto \| copper \| sfp*；預設值：**auto**） | 選擇 auto 模式時，先連線的埠將建立鏈路。若該鏈路失效，另一埠將嘗試建立新鏈路。若發生重啟，兩個埠中的任意一個都可能執行，取決於哪個埠先成功建立鏈路。選擇 sfp 模式時，介面僅透過 SFP/SFP+ 插槽工作。選擇 copper 模式時，介面僅透過 RJ45 乙太網埠工作。 |
| **comment** (*string*; Default: ) | 條目的描述性名稱 |
| **disable-running-check**（*yes \| no*；預設值：**yes**） | 停用執行檢查。若將此值設為 'no'，路由器將自動檢測網路卡是否與網路中的裝置相連。預設值為 'yes'，因為較舊的網路卡不支援該功能。（僅與 CHR 和 x86 相關） |
| **fec-mode**（*auto \| fec74 \| fec91 \| off；* 預設值：**auto**） | 更改 SFP28、QSFP+ 和 QSFP28 介面的前向糾錯（FEC）模式。鏈路兩端應使用相同模式，否則 FEC 不匹配可能導致鏈路無法工作，甚至出現虛假的鏈路連通。<br/><strong>建議啟用 FEC，尤其是在 CRS3xx、CRS5xx 系列交換器之間建立鏈路時。某些光模組可能依賴 MAC 中的 FEC 功能。</strong><br/><ul><li>auto - 與 off 相同</li><li>fec74 - 啟用 IEEE 802.3 第 74 條 FEC（又稱 FC-FEC），可用於 25Gbps、40Gbps 和 50Gbps 鏈路模式</li><li>fec91 - 啟用 IEEE 802.3 第 91 條 FEC（又稱 RS-FEC），可用於 25Gbps、50Gbps、100Gbps、200Gbps 和 400Gbps 鏈路模式</li><li>off - 停用 FEC。</li></ul> |
| **tx-flow-control**（*on \| off \| auto*；預設值：**off**） | 設為 on 時，埠將向上遊裝置生成暫停幀，以暫時停止封包傳輸。僅當路由器的某個輸出介面擁塞且封包無法再傳輸時才會生成暫停幀。**auto** 與 **on** 相同，但當 auto-negotiation=yes 時，流控狀態會參考對端通告的內容來確定。 |
| **rx-flow-control**（*on \| off \| auto*；預設值：**off**） | 設為 on 時，埠將處理收到的暫停幀，並在需要時暫停傳輸。**auto** 與 **on** 相同，但當 auto-negotiation=yes 時，流控狀態會參考對端通告的內容來確定。 |
| **full-duplex**（*yes \| no*；預設值：**yes**） | 定義資料是否同時雙向傳輸，僅在停用自動協商時生效。自 RouterOS v7.12 起，該設定已由新的速率鏈路模式取代。 |
| **l2mtu**（*integer [0..65536]*；預設值：） | 二層最大傳輸單元。[瞭解更多](../hardware/mtu-in-routeros.md)。 |
| **mac-address** (*MAC*; Default: ) | 介面的媒體訪問控制編號。 |
| **mdix-enable**（*yes \| no*；預設值：**yes**） | 是否為該埠啟用 MDI/X 自動交叉線纜糾正功能（與硬體相關，例如 RB500 上的 ether1 可設為 yes/no。在其他硬體上固定為 'yes'。） |
| **mtu** (*integer [0..65536]*; Default: **1500**) | 三層最大傳輸單元 |
| **name** (*string*; Default: ) | 介面的名稱 |
| **orig-mac-address**（*read-only：MAC*；預設值：） | 介面的原始媒體訪問控制編號。 |
| **passthrough-interface**（*interface*；預設值：） | 在 CCR2004-1G-2XS-PCIe 裝置上設定處於直通模式的介面。預設情況下，PCIe 介面將顯示為四個虛擬乙太網介面。其中兩個介面處於直通模式，通向 25G SFP28 插槽。其餘兩個虛擬乙太網-PCIe 介面與千兆乙太網埠橋接，用於管理訪問。 |
| **poe-out**（*auto-on \| forced-on \| off*；預設值：**off**） | PoE 輸出設定。[`了解更多`](../hardware/poe-out.md)。 |
| **poe-priority**（*integer [0..99]*；預設值：） | PoE 輸出設定。[`了解更多`](../hardware/poe-out.md)。 |
| **sfp-shutdown-temperature**（*integer*；預設值：**95** \| **80**） | 當檢測到的 SFP 模組溫度過高時，介面將被暫時關閉的溫度（攝氏度）（v6.48 引入）。SFP/SFP+/SFP28 介面的預設值為 95，QSFP+/QSFP28 介面的預設值為 80（v7.6 引入）。 |
| **sfp-rate-select**（*high \| low*；預設值：**high**） | 允許控制 SFP 埠的速率選擇引腳。 |
| <strong>speed</strong>（自 RouterOS v7.12 起：<em>10M-baseT-half &#124; 10M-baseT-full&#124; 100M-baseT-half &#124; 100M-baseT-full &#124; 1G-baseT-half &#124; 1G-baseT-full &#124; 1G-baseX &#124; 2.5G-baseT &#124; 2.5G-baseX &#124; 5G-baseT &#124; 10G-baseT &#124; 10G-baseSR-LR &#124; 10G-baseCR &#124; 40G-baseSR4-LR4 &#124; 40G-baseCR4 &#124; 25G-baseSR-LR &#124; 25G-baseCR &#124; 50G-baseSR2-LR2 &#124; 50G-baseCR2 &#124; 100G-baseSR4-LR4 &#124; 100G-baseCR4;</em> 預設值：）<br/>（較舊版本的 RouterOS：<em>10Mbps &#124; 10Gbps &#124; 100Mbps &#124; 1Gbps &#124; 2.5Gbps &#124; 5Gbps &#124; 25Gbps &#124; 40Gbps &#124; 100Gbps</em>；預設值：） | 設定介面資料傳輸速率，僅在停用自動協商時生效。設定高於介面實際支援速度的值可能導致未定義的行為。僅允許使用單個選項。 |

**只讀屬性**

| 屬性 | 描述 |
| :-- | :-- |
| **running**（*yes \| no*） | 介面是否正在執行。請注意，某些介面沒有執行檢查，它們始終報告為 "running"。 |
| **slave**（*yes \| no*） | 介面是否配置為另一個介面的從屬介面（例如 [繫結](../high-availability-solutions/bonding.md) 或 [Bridge](../bridging-and-switching/index.md)） |
| **switch**（*integer*） | 交換器晶片介面所屬的 ID。 |

## 選單專用命令 {#menu-specific-commands}

| 屬性 | 描述 |
| :-- | :-- |
| **blink**（*[id, name]*） | 使乙太網 LED 閃爍 |
| **monitor**（*[id, name]*） | 監控乙太網狀態。[瞭解更多](./ethernet.md#monitor)。 |
| **reset-counters**（*[id, name]*） | 重設統計計數器。[瞭解更多](./ethernet.md#stats)。 |
| **reset-mac-address**（*[id, name]*） | 將 MAC 地址重設為製造商的預設值。 |
| **cable-test**（*string*） | 顯示檢測到的電纜對問題。[`Read More`](./ethernet.md#detect-cable-problems)。 |

## 監控 {#monitor}

要列印當前鏈路速率和其他乙太網相關屬性，或檢視收發器的詳細診斷資訊，請使用 `/interface/ethernet/monitor` 命令。所提供的資訊可能因介面型別（例如雙絞線乙太網或 SFP 介面）或收發器（例如 SFP 和 QSFP）而異。

### 屬性 {#properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **advertising**（自 RouterOS v7.12 起：*10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4*）（較舊 RouterOS：*10M-full \| 10M-half \| 100M-full \| 100M-half \| 1000M-full \| 1000M-half \| 2500M-full \| 5000M-full \| 10000M-full*） | 通告的鏈路模式僅在啟用自動協商時適用 |
| **auto-negotiation**（*disabled \| done \| failed \| incomplete*） | 當前自動協商狀態：disabled - 協商已停用；done - 協商已完成；failed - 協商失敗；incomplete - 協商尚未完成 |
| **default-cable-settings**（*short \| standard*） | 預設電纜長度設定（僅適用於 NS DP83815/6 卡）；short - 支援短電纜；standard - 支援標準電纜 |
| **fec**（*fec74 \| fec91 \| off*） | 當前 FEC 模式。 |
| **full-duplex**（*yes \| no*） | 資料是否同時雙向傳輸 |
| **link-partner-advertising**（自 RouterOS v7.12 起：*10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4*）（較舊 RouterOS：*10M-full \| 10M-half \| 100M-full \| 100M-half \| 1000M-full \| 1000M-half \| 2500M-full \| 5000M-full \| 10000M-full*） | 鏈路夥伴通告的鏈路模式僅在啟用自動協商時適用 |
| **rate**（*10Mbps \| 100Mbps \| 1Gbps \| 2.5Gbps \| 5Gbps \| 10Gbps \| 25Gbps \| 40Gbps \| 50Gbps \| 100Gbps \| 200Gbps \| 400Gbps*） | 連線的實際資料速率。 |
| **status**（*link-ok \| no-link \| unknown*） | 介面的當前鏈路狀態：link-ok - 網路卡已連線到網路；no-link - 網路卡未連線到網路；unknown - 無法識別連線（如果網路卡不報告連線狀態） |
| **tx-flow-control**（*yes \| no*） | 是否使用 TX 流控制 |
| **rx-flow-control**（*yes \| no*） | 是否使用 RX 流控制 |
| **combo-state**（*copper \| sfp*） | combo 介面使用的 combo-mode |
| **sfp-module-present**（*yes \| no*） | 插槽中是否有收發器 |
| **sfp-rx-loss**（*yes \| no*） | 是否丟失接收器訊號 |
| **sfp-tx-fault**（*yes \| no*） | 收發器傳送器是否處於故障狀態 |
| **sfp-type**（*SFP/SFP+/SFP28/SFP56 \| DWDM-SFP/SFP+ \| QSFP \| QSFP+ \| QSFP28/QSFP56 \| QSFPDD*） | 使用的收發器型別 |
| **sfp-cmis-revision**（*string*） | 收發器 CMIS 修訂號 |
| **sfp-connector-type**（*SC \| LC \| optical-pigtail \| copper-pigtail \| multifiber-parallel-optic-1x12 \| multifiber-parallel-optic-1x16 \| no-separable-connector \| RJ45*） | 使用的收發器聯結器型別 |
| **sfp-link-length-9um**（*m*） | 收發器支援的單模 9/125um 光纖鏈路長度 |
| **sfp-link-length-sm**（*km*） | 收發器支援的單模光纖鏈路長度 |
| **sfp-link-length-om3**（*m*） | 收發器支援的多模（OM3）鏈路長度 |
| **sfp-link-length-om4**（*m*） | 收發器支援的多模（OM4）鏈路長度 |
| **sfp-link-length-om5**（*m*） | 收發器支援的多模（OM5）鏈路長度 |
| **sfp-link-length-om2**（*m*） | 收發器支援的多模 50/125um 光纖（OM2）鏈路長度 |
| **sfp-link-length-om1**（*m*） | 收發器支援的多模 62.5/125um 光纖（OM1）鏈路長度 |
| **sfp-link-length-copper**（*m*） | 銅纜收發器支援的鏈路長度 |
| **sfp-vendor-name**（*string*） | 收發器製造商 |
| **sfp-vendor-part-number**（*string*） | 收發器部件號 |
| **sfp-vendor-revision**（*string*） | 收發器修訂號 |
| **sfp-vendor-serial**（*string*） | 收發器序列號 |
| **sfp-manufacturing-date**（*date*） | 收發器製造日期 |
| **sfp-power-class**（*string*） | 收發器功率等級 |
| **sfp-max-power**（*W*） | 收發器最大功耗 |
| **sfp-wavelength**（*nm*） | 收發器傳送器光訊號波長 |
| **sfp-temperature**（*C*） | 收發器溫度 |
| **sfp-supply-voltage**（*V*） | 收發器供電電壓 |
| **sfp-tx-bias-current**（*mA*） | 收發器 Tx 偏置電流 |
| **sfp-tx-power**（*dBm*） | 收發器傳送光功率 |
| **sfp-rx-power**（*dBm*） | 收發器接收光功率 |
| **sfp-supported**（*10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4 \| 50G-baseSR-LR \| 50G-baseCR \| 100G-baseSR2-LR2 \| 100G-baseCR2 \| 200G-baseSR4-LR4 \| 200G-baseCR4 \| 400G-baseSR8-LR8 \| 400G-baseCR8*） | 模組支援的鏈路模式。此屬性僅適用於某些裝置。 |
| **supported**（*10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4 \| 50G-baseSR-LR \| 50G-baseCR \| 100G-baseSR2-LR2 \| 100G-baseCR2 \| 200G-baseSR4-LR4 \| 200G-baseCR4 \| 400G-baseSR8-LR8 \| 400G-baseCR8*） | 顯示支援的介面硬體鏈路模式能力。 |
| **eeprom-checksum**（*good \| bad*） | EEPROM 校驗和是否正確 |
| **eeprom**（*hex dump*） | 收發器的原始 EEPROM |

乙太網狀態輸出示例：

```ros
[admin@MikroTik] > /interface/ethernet/monitor ether2 
                      name: ether2
                    status: link-ok
          auto-negotiation: done
                      rate: 1Gbps
               full-duplex: yes
           tx-flow-control: no
           rx-flow-control: no
                 supported: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
               advertising: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
  link-partner-advertising: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
```

SFP 狀態輸出示例：

```ros
[admin@MikroTik] > /interface/ethernet/monitor sfp3
                      name: sfp3
                    status: link-ok
          auto-negotiation: done
                       rate: 1Gbps
                full-duplex: yes
            tx-flow-control: no
           rx-flow-control: no
                 supported: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full,1G-baseX
             sfp-supported: 1G-baseX
               advertising: 1G-baseX
  link-partner-advertising: 
        sfp-module-present: yes
               sfp-rx-loss: no
              sfp-tx-fault: no
                  sfp-type: SFP/SFP+/SFP28/SFP56
        sfp-connector-type: LC
       sfp-link-length-om1: 500m
       sfp-link-length-om2: 550m
           sfp-vendor-name: Mikrotik
    sfp-vendor-part-number: S-85DLC05D
         sfp-vendor-serial: SG85M31401687
    sfp-manufacturing-date: 13-04-24
            sfp-wavelength: 850nm
           sfp-temperature: 33C
        sfp-supply-voltage: 3.237V
       sfp-tx-bias-current: 2mA
              sfp-tx-power: -5.792dBm
              sfp-rx-power: -5.22dBm
           eeprom-checksum: good
                    eeprom: 0000: 03 04 07 00 00 00 01 00  00 00 00 03 0d 00 00 00  ........ ........
                            0010: 37 32 00 00 4d 69 6b 72  6f 74 69 6b 20 20 20 20  72..Mikr otik    
                            0020: 20 20 20 20 00 00 00 00  53 2d 38 35 44 4c 43 30      .... S-85DLC0
                            0030: 35 44 20 20 20 20 20 20  00 00 00 00 03 52 00 50  5D       .....R.P
                            0040: 00 1a 00 00 53 47 38 35  4d 33 31 34 30 31 36 38  ....SG85 M3140168
                            0050: 37 20 20 20 31 33 30 34  32 34 20 20 68 b0 01 f3  7   1304 24  h...
                            0060: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ........ ........
                            *
                            0080: 64 00 d2 ff 5a 00 d7 ff  8c a0 75 30 88 b8 79 18  d...Z... ..u0..y.
                            0090: 75 30 00 fa 61 a8 01 f4  1f 07 03 1a 18 a5 03 e7  u0..a... ........
                            00a0: 31 2e 00 13 27 12 00 27  00 00 00 00 00 00 00 00  1...'..' ........
                            00b0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ........ ........
                            00c0: 00 00 00 00 3f 80 00 00  00 00 00 00 01 00 00 00  ....?... ........
                            00d0: 01 00 00 00 01 00 00 00  01 00 00 00 00 00 00 23  ........ .......#
                            00e0: 21 7c 7e 72 05 27 0a 4b  0b be 00 00 00 00 00 94  !|~r.'.K ........
                            00f0: 00 00 00 00 00 00 00 00  20 21 2a ff ff ff ff 00  ........  !*.....

```

## 檢測電纜問題 {#detect-cable-problems}

如果電纜另一端未插上，因此處於 "no-link" 狀態，電纜測試可以檢測問題或測量近似電纜長度。RouterOS 將顯示：

- 哪一對電纜損壞
- 到問題的距離
- 電纜究竟如何斷開——短路還是開路

如果另一端只是未插上，這也有效——在這種情況下，將顯示總電纜長度。

以下是輸出示例：

```ros
[admin@CCR] > interface ethernet cable-test ether2 
name: ether2 
status: no-link 
cable-pairs: open:4,open:4,open:4,open:4
```

在上面的示例中，電纜沒有短路，而是在 4 米距離處“開路”；所有電纜對在距交換器晶片相同距離處同樣故障。

目前 `cable-test` 在以下裝置上實現：

| 裝置 |  |  |
| :-- | :-- | :-- |
| CCR1xxx 系列 | RB952Ui-5ac2nD | RBLHGG-5acD |
| CRS1xx 系列 | RB962UiGS-5HacT2HnT | RB5009 系列（eth1） |
| CRS2xx 系列 | RB1100AHx2 | C52iG-5HaxD2HaxD |
| OmniTIK 系列 | RB1100x4 | C53UiG+5HPaxD2HPaxD |
| RB450G 系列 | RBD52G-5HacD2HnD | S53UG+5HaxD2HaxD 系列 |
| RB951 系列 | RBD53G-5HacD2HnD 系列 | H53UiG-5HaxQ2HaxQ |
| RB2011 系列 | RBcAPGi-5acD2nD |  |
| RB4011 系列 | RBmAPL-2nD |  |
| RB750Gr2 | RBmAP2nD |  |
| RB750UPr2 | RBwsAP-5Hac2nD |  |
| RB751U-2HnD | RB3011UiAS-RM |  |
| RB850Gx2 | RBMetal 2SHPn |  |
| RB931-2nD | RBDynaDishG-5HacD |  |
| RB941-2nD | RBLDFG-5acD |  |

:::warning
目前 Combo 埠不支援 `cable-test`。
:::

## 統計 {#stats}

使用 `/interface/ethernet/print stats` 命令，可以檢視各種與乙太網相關的統計資訊。由於乙太網驅動程式不同，RouterBoard 裝置之間的統計資訊列表可能有所不同。下面的列表包含所有 RouterBoard 裝置上所有可用的計數器。大多數乙太網統計資訊可以使用 [SNMP](../diagnostics-monitoring-and-troubleshooting/snmp.md) 和 MIKROTIK-MIB 進行遠端監控。

| 屬性 | 描述 |
| :-- | :-- |
| **driver-rx-byte**（*integer*） | 裝置 CPU 上接收位元組的總數 |
| **driver-rx-packet**（*integer*） | 裝置 CPU 上接收封包的總數 |
| **driver-tx-byte**（*integer*） | 裝置 CPU 傳送位元組的總數 |
| **driver-tx-packet**（*integer*） | 裝置 CPU 傳送封包的總數 |
| **fc-fec-block-corrected**（*integer*） | FC-FEC 糾正塊的總數。僅在使用 fec74 模式時適用。 |
| **fc-fec-block-uncorrected**（*integer*） | FC-FEC 未糾正塊的總數。僅在使用 fec74 模式時適用。 |
| **fc-fec-rx-block**（*integer*） | FC-FEC 接收塊的總數。僅在使用 fec74 模式時適用。 |
| **rs-fec-corrected**（*integer*） | RS-FEC 糾正碼字的總數。僅在使用 fec91 模式時適用。 |
| **rs-fec-symbol-error**（*integer*） | RS-FEC 符號錯誤的總數。僅在使用 fec91 模式時適用。 |
| **rs-fec-uncorrected**（*integer*） | RS-FEC 未糾正碼字的總數。僅在使用 fec91 模式時適用。 |
| **rx-64**（*integer*） | 接收的 64 位元組幀總數 |
| **rx-65-127**（*integer*） | 接收的 65 至 127 位元組幀總數 |
| **rx-128-255**（*integer*） | 接收的 128 至 255 位元組幀總數 |
| **rx-256-511**（*integer*） | 接收的 256 至 511 位元組幀總數 |
| **rx-512-1023**（*integer*） | 接收的 512 至 1023 位元組幀總數 |
| **rx-1024-1518**（*integer*） | 接收的 1024 至 1518 位元組幀總數 |
| **rx-1519-max**（*integer*） | 接收的大於 1519 位元組的幀總數 |
| **rx-align-error**（*integer*） | 接收的對齊錯誤事件總數——位未沿八位組邊界對齊的封包 |
| **rx-broadcast**（*integer*） | 接收的廣播幀總數 |
| **rx-bytes**（*integer*） | 接收位元組總數 |
| **rx-carrier-error**（*integer*） | 接收的帶載波偵聽錯誤的幀總數 |
| **rx-code-error**（*integer*） | 接收的帶編碼錯誤的幀總數 |
| **rx-control**（*integer*） | 接收的控制幀或暫停幀總數 |
| **rx-error-events**（*integer*） | 接收的帶活動錯誤事件的幀總數 |
| **rx-fcs-error**（*integer*） | 接收的帶錯誤校驗和的幀總數 |
| **rx-fragment**（*integer*） | 接收的分片幀總數（與 IP 分片無關） |
| **rx-ip-header-checksum-error**（*integer*） | 接收的帶 IP 頭部校驗和錯誤的幀總數 |
| **rx-jabber**（*integer*） | 接收的 jabber 封包總數——傳輸長度超過最大封包長度的封包 |
| **rx-length-error**（*integer*） | 接收的帶幀長度錯誤的幀總數 |
| **rx-multicast**（*integer*） | 接收的多播幀總數 |
| **rx-overflow**（*integer*） | 接收的溢位幀總數，可能因裝置資源不足以接收某個幀而導致 |
| **rx-pause**（*integer*） | 接收的暫停幀總數 |
| **rx-runt**（*integer*） | 接收的短於最小 64 位元組的幀總數，通常由衝突導致 |
| **rx-tcp-checksum-error**（*integer*） | 接收的帶 TCP 頭部校驗和錯誤的幀總數 |
| **rx-too-long**（*integer*） | 接收的大於網路裝置支援的最大幀大小的幀總數，請參閱 max-l2mtu 屬性 |
| **rx-too-short**（*integer*） | 接收的短於最小 64 位元組的幀總數 |
| **rx-udp-checksum-error**（*integer*） | 接收的帶 UDP 頭部校驗和錯誤的幀總數 |
| **rx-unicast**（*integer*） | 接收的單播幀總數 |
| **rx-unknown-op**（*integer*） | 接收的帶未知乙太網協定的幀總數 |
| **tx-64**（*integer*） | 傳送的 64 位元組幀總數 |
| **tx-65-127**（*integer*） | 傳送的 65 至 127 位元組幀總數 |
| **tx-128-255**（*integer*） | 傳送的 128 至 255 位元組幀總數 |
| **tx-256-511**（*integer*） | 傳送的 256 至 511 位元組幀總數 |
| **tx-512-1023**（*integer*） | 傳送的 512 至 1023 位元組幀總數 |
| **tx-1024-1518**（*integer*） | 傳送的 1024 至 1518 位元組幀總數 |
| **tx-1519-max**（*integer*） | 傳送的大於 1519 位元組的幀總數 |
| **tx-align-error**（*integer*） | 傳送的對齊錯誤事件總數——位未沿八位組邊界對齊的封包 |
| **tx-broadcast**（*integer*） | 傳送的廣播幀總數 |
| **tx-bytes**（*integer*） | 傳送位元組總數 |
| **tx-collision**（*integer*） | 傳送的發生衝突的幀總數 |
| **tx-control**（*integer*） | 傳送的控制幀或暫停幀總數 |
| **tx-deferred**（*integer*） | 傳送的因介質已忙而在首次傳送嘗試時被延遲的幀總數 |
| **tx-drop**（*integer*） | 傳送的因輸出佇列已滿而被丟棄的幀總數 |
| **tx-excessive-collision**（*integer*） | 傳送的已發生多次衝突且從未成功傳輸的幀總數 |
| **tx-excessive-deferred**（*integer*） | 傳送的因介質已忙而被延遲過長時間的幀總數 |
| **tx-fcs-error**（*integer*） | 傳送的帶錯誤校驗和的幀總數 |
| **tx-fragment**（*integer*） | 傳送的分片幀總數（與 IP 分片無關） |
| **tx-carrier-sense-error**（*integer*） | 傳送的帶載波偵聽錯誤的幀總數 |
| **tx-late-collision**（*integer*） | 傳送的在已傳輸一半後發生衝突的幀總數 |
| **tx-multicast**（*integer*） | 傳送的多播幀總數 |
| **tx-multiple-collision**（*integer*） | 傳送的發生不止一次衝突隨後成功傳輸的幀總數 |
| **tx-overflow**（*integer*） | 傳送的溢位幀總數 |
| **tx-pause**（*integer*） | 傳送的暫停幀總數 |
| **tx-all-queue-drop-byte**（*integer*） | 所有輸出佇列丟棄的傳送位元組總數 |
| **tx-all-queue-drop-packet**（*integer*） | 所有輸出佇列丟棄的傳送封包總數 |
| **tx-queueX-byte**（*integer*） | 某個佇列上傳送位元組的總數，**X** 應替換為佇列編號 |
| **tx-queueX-packet**（*integer*） | 某個佇列上傳送幀的總數，**X** 應替換為佇列編號 |
| **tx-runt**（*integer*） | 傳送的短於最小 64 位元組的幀總數，通常由衝突導致 |
| **tx-too-short**（*integer*） | 傳送的短於最小 64 位元組的幀總數 |
| **tx-rx-64**（*integer*） | 傳送和接收的 64 位元組幀總數 |
| **tx-rx-64-127**（*integer*） | 傳送和接收的 64 至 127 位元組幀總數 |
| **tx-rx-128-255**（*integer*） | 傳送和接收的 128 至 255 位元組幀總數 |
| **tx-rx-256-511**（*integer*） | 傳送和接收的 256 至 511 位元組幀總數 |
| **tx-rx-512-1023**（*integer*） | 傳送和接收的 512 至 1023 位元組幀總數 |
| **tx-rx-1024-max**（*integer*） | 傳送和接收的大於 1024 位元組的幀總數 |
| **tx-single-collision**（*integer*） | 傳送的僅發生一次衝突隨後成功傳輸的幀總數 |
| **tx-too-long**（*integer*） | 傳送的大於最大封包大小的封包總數 |
| **tx-underrun**（*integer*） | 欠載執行幀總數，可能因裝置資源不足以傳送某個幀而導致 |
| **tx-unicast**（*integer*） | 傳送的單播幀總數 |

例如，hAP ac2 裝置上的乙太網統計輸出：

```ros
[admin@MikroTik] > /interface/ethernet/print stats
                      name:           ether1 ether2         ether3        ether4 ether5
            driver-rx-byte:  182 334 805 898      0  5 836 927 820    24 895 692      0
          driver-rx-packet:    4 449 562 546      0  4 320 155 362       259 449      0
            driver-tx-byte:   15 881 099 971      0 70 502 669 211    60 498 056     53
          driver-tx-packet:       52 724 428      0     54 231 229       106 498      1
                  rx-bytes:  178 663 398 808      0  5 983 590 739 1 358 140 795      0
              rx-too-short:                0      0              0             0      0
                     rx-64:       12 749 144      0        362 459       125 917      0
                 rx-65-127:        9 612 406      0     20 366 513       292 189      0
                rx-128-255:        6 259 883      0      1 672 588       261 013      0
                rx-256-511:        2 950 578      0        211 380       278 147      0
               rx-512-1023:        3 992 258      0        185 666       163 241      0
              rx-1024-1518:      119 034 611      0      2 796 559       696 254      0
               rx-1519-max:                0      0              0             0      0
               rx-too-long:                0      0              0             0      0
              rx-broadcast:       12 025 189      0      1 006 377        64 178      0
                  rx-pause:                0      0              0             0      0
              rx-multicast:        4 687 869      0         36 188       220 136      0
              rx-fcs-error:                0      0              0             0      0
            rx-align-error:                0      0              0             0      0
               rx-fragment:                0      0              0             0      0
               rx-overflow:                0      0              0             0      0
                  tx-bytes:   16 098 535 973      0 72 066 425 886   225 001 772      0
                     tx-64:        1 063 375      0        924 855        37 877      0
                 tx-65-127:       26 924 514      0      2 442 200       959 209      0
                tx-128-255:       14 588 113      0        924 746       295 961      0
                tx-256-511:        1 323 733      0      1 036 515        33 252      0
               tx-512-1023:        1 287 464      0      2 281 554         3 625      0
              tx-1024-1518:        7 537 154      0     48 212 304        64 659      0
               tx-1519-max:                0      0              0             0      0
               tx-too-long:                0      0              0             0      0
              tx-broadcast:              590      0        145 800       823 038      0
                  tx-pause:                0      0              0             0      0
              tx-multicast:                0      0      1 039 243        41 716      0
               tx-underrun:                0      0              0             0      0
              tx-collision:                0      0              0             0      0
    tx-excessive-collision:                0      0              0             0      0
     tx-multiple-collision:                0      0              0             0      0
       tx-single-collision:                0      0              0             0      0
     tx-excessive-deferred:                0      0              0             0      0
               tx-deferred:                0      0              0             0      0
         tx-late-collision:                0      0              0             0      0
```
