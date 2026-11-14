---
sidebar_key: "wireless/wifi/capsman"
sidebar_position: 1
title: "WiFi CAPsMAN"
sidebar_label: "WiFi CAPsMAN"
description: "適用於 wifi-qcom / wifi-qcom-ac 軟體包的 WiFi CAPsMAN（受控接入點系統管理器）可集中管理多個 WiFi 接入點。內容涵蓋 CAP 發現、無線射頻配置、資料路徑/轉發模式、VLAN 和 OWE 示例，以及 CAPsMAN/CAP/配置屬性參考。"
tags:
  - 'wifi'
  - 'caps-man'
  - 'capsman'
source: https://manual.mikrotik.com/docs/wireless/wifi/capsman
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
本節介紹 wifi-qcom 和 wifi-qcom-ac 軟體包中 CAPsMAN 功能的操作。對於使用舊版 "wireless" 軟體包的裝置，請參見[此處相應手冊](../abgn/capsman/index.md)。本文及下文提到 "WiFi" 時，指的是新的 WiFi 選單，而不是該技術本身。
:::

受控接入點系統管理器 (CAPsMAN) 允許從集中配置介面向多個 MikroTik WiFi AP 裝置應用無線設定，即允許集中管理無線網路。使用 CAPsMAN 時，網路將由多個提供無線連線的“受控接入點”(CAP) 和一個管理 AP 配置並負責用戶端認證的“系統管理器”(CAPsMAN) 組成。

要求：

- 任何支援 WiFi 軟體包的 RouterOS 裝置，只要至少具有 Level 4 RouterOS 許可證，就可以作為受控無線接入點 (CAP)。
- WiFi CAPsMAN 伺服器可以安裝在任何支援 WiFi 軟體包的 RouterOS 裝置上，即使該裝置本身沒有無線介面。
- CAPsMAN 支援無限數量的 CAP（接入點）。

:::info
WiFi CAPsMAN 只能控制 WiFi 介面，WiFi CAP 也只能加入 WiFi CAPsMAN。同樣，常規 CAPsMAN 僅支援非 WiFi CAP。

CAP 不會向 CAPsMAN 傳送流量使用資訊。
:::

### CAP 發現 CAPsMAN {#capsman-discovery-by-cap}

CAP 透過以下方式發現 CAPsMAN 地址/主機名：

- 二層發現。
- DHCP 選項 138（CAPsMAN 地址）。
- DHCP 選項 15（自定義域）：`resolves _capsman._tcp.<domain>.`
- 預設 MikroTik 'lan' 域：`resolves _capsman._tcp.lan.`

### 射頻預配 {#radio-provisioning}

建立配置模板後，你可以選擇哪些裝置應使用每個模板進行預配置。當然，在簡單設定中，只有一條預配置規則就足夠了；但如果你希望向 2.4GHz 介面傳送一種配置，向 5GHz 介面傳送另一種配置，則可以建立兩條預配置規則，並使用 `supported-bands` 引數定義哪個模板傳送到哪裡。

CAPsMAN 根據內建 MAC 地址 (radio-mac) 區分實際無線介面（射頻）。這意味著不可能在同一 CAPsMAN 上管理兩個具有相同 MAC 地址的射頻。當前由 CAPsMAN 管理的射頻（由已連線的 CAP 提供）列在 `/interface/wifi/radio` 選單中。此列表還會包含 CAPsMAN 自身存在的內建 WiFi 介面（如果有）：

```ros
[admin@c52i] > /interface/wifi/radio/print 
Flags: L - LOCAL
Columns: CAP, RADIO-MAC, INTERFACE
#   CAP                  RADIO-MAC          INTERFACE 
0 L                      18:FD:74:AF:F4:28  wifi1     
1 L                      18:FD:74:AF:F4:29  wifi2     
2   hapAX3@192.168.88.30  48:A9:8A:0B:F7:4B  cap1
```

當 CAP 連線時，CAPsMAN 首先會嘗試根據 radio-mac 將每個 CAP 射頻繫結到 CAPsMAN 主介面。如果找到合適的介面，則使用主介面配置以及引用該特定主介面的從介面配置來設定該射頻。此時，介面（包括主介面和從介面）被視為已繫結到射頻，並且該射頻被視為已預配置。僅當 `/interface/wifi` 下已存在匹配的靜態條目時才會發生這種情況；通常該條目是先前手動建立的，或透過包含 "create-enabled" 或 "create-disabled" 動作的預配置規則建立的。

如果未找到與該射頻匹配的主介面，CAPsMAN 會執行在 `/interface/wifi/provisioning/` 下定義的“預配置規則”。預配置規則是一個有序規則列表，其中包含指定要匹配哪個射頻的設定，以及確定射頻匹配後要執行什麼動作的設定。

當 CAP 加入 CAPsMAN，且 `/interface/wifi` 下沒有與之匹配的介面時，系統會自動檢查預配置規則；一旦找到匹配項，CAP 的無線介面就會出現在 `/interface/wifi` 下。這樣的介面就是“已預配置”；在此上下文中，預配置意味著該射頻存在一個 WiFi 介面，並且已為其分配配置配置檔案。

還可以選擇手動預配置介面，這會讓 CAPsMAN 開始針對特定介面評估預配置規則，並在匹配時建立新介面。如果 `/interface/wifi/` 下已存在該射頻的條目，該條目將被刪除並重新建立。手動預配置會重新建立介面，**通常不需要**，因為預配置規則會自動評估；並且如果你更改與預配置規則關聯的配置配置檔案，這些更改將應用到所有使用該配置的 WiFi 介面。如果手動預配置介面，介面 ID 或名稱可能會改變，從而導致對其他物件（例如橋接埠）的引用失效。

可以在 `/interface/wifi/capsman/remote-cap/provision` 下執行手動預配置，以預配置與特定 CAP 關聯的所有射頻；也可以在 `/interface/wifi/radio/provision` 下預配置特定射頻。

CAPsMAN 無法使用 `configuration.manager=capsman` 管理自身的 WiFi 介面；只需像使用預配置規則那樣，在本地介面上手動設定相同的配置配置檔案即可，最終結果與將它們作為 CAP 時相同。話雖如此，也可以透過 `/interface/wifi/radio` 選單預配置本地介面；需要注意的是，預配置後若要重新獲得對本地介面的控制，你需要停用匹配的預配置規則並再次按 "provision"，這會使本地介面恢復到未配置狀態。

:::info
預配置只需在初始階段執行；如果存在已啟用的匹配預配置規則，則 CAP 加入時會自動執行。  
如果你調整了與已預配置介面關聯的任何配置配置檔案，只要應用對該配置檔案的更改，所有更改都會被“推送”，無需重新建立已存在的介面。  
預配置本身並不是用於傳送配置，而本質上是用於建立新介面。在大多數情況下，一旦 CAP 介面已在執行，就沒有理由執行手動預配置。
:::

### CAPSMAN 資料路徑 {#capsman-datapath}

資料路徑設定控制與資料轉發相關的方面。在 CAPsMAN 上，資料路徑設定可在資料路徑配置檔案選單 **/interface/wifi/datapath/** 中配置，也可在配置配置檔案或介面選單中作為帶有 **datapath.** 字首的設定直接配置。

有兩種主要的轉發/流量處理模式：

- 本地轉發模式（`traffic-processing=on-cap`），其中 CAP 在本地向無線介面轉發資料以及從無線介面轉發資料；
- CAPsMAN 轉發模式（`traffic-processing=on-capsman`），其中 CAP 將所有透過無線接收的資料傳送給 CAPsMAN，並且只發送從 CAPsMAN 接收的無線資料。

:::info
僅從 **7.21beta2** 版本開始才可能使用 CAPsMAN 轉發。**在較舊版本中，僅支援 CAP 轉發。**

**wifi-qcom-ac** 裝置不支援 CAPsMAN 轉發（wifi-qcom-ac 驅動僅**支援** **本地轉發**）。
:::

:::note
MLO 目前不支援 CAPsMAN 轉發（`traffic-processing=on-capsman`）。
:::

### CAPsMAN - CAP 簡單配置示例 {#capsman---cap-simple-configuration-example}

WiFi 中的 CAPsMAN 使用與普通 WiFi 介面相同的選單，這意味著當你向 CAP 傳遞配置時，必須使用與普通 WiFi 介面相同的配置、安全、通道配置等。

:::info
你可以直接在 `/interface/wifi/configuration` 下配置子配置選單，或在主配置檔案中引用之前建立的配置檔案
:::

#### CAPsMAN {#capsman}

```ros
#创建安全配置文件
/interface/wifi/security
add authentication-types=wpa3-psk name=sec1 passphrase=HaveAg00dDay

#创建用于下发的配置模板
/interface/wifi/configuration
add country=Latvia name=5ghz security=sec1 ssid=CAPsMAN_5
add name=2ghz security=sec1 ssid=CAPsMAN2
add country=Latvia name=5ghz_v security=sec1 ssid=CAPsMAN5_v

#配置下发规则，按需配置频段匹配
/interface/wifi/provisioning
add action=create-dynamic-enabled master-configuration=5ghz slave-configurations=5ghz_v supported-bands=\
    5ghz-n
add action=create-dynamic-enabled master-configuration=2ghz supported-bands=2ghz-n

#启用 CAPsMAN 服务
/interface/wifi/capsman
set ca-certificate=auto enabled=yes
```

如果要使用 MLO（由 WiFi 7 BE CAP 支援），構成 MLD 的所有介面必須使用相同的 SSID：

```ros
#为主 SSID 和 IoT SSID 创建配置模板
/interface/wifi/configuration
add country=Latvia disabled=no mode=ap name=cfg-main security.authentication-types=wpa3-psk security.passphrase=HaveAg00dDay ssid=main
add country=Latvia disabled=no mode=ap name=cfg-iot security.authentication-types=wpa3-psk security.passphrase=HaveAg00dDay ssid=IoT

#为所有 radio 下发配置，并将主接口和虚拟接口都设为 MLO
/interface/wifi/provisioning
add action=create-dynamic-enabled disabled=no master-configuration=cfg-main multi-link-mode=auto slave-configurations=cfg-iot

#启用 CAPsMAN 并生成 CA 证书
/interface/wifi/capsman
set ca-certificate=auto enabled=yes
```

:::note
如果你希望虛擬介面是基礎介面（非 MLO），請改用 `multi-link-mode=master`。
:::

#### CAP {#cap}

```ros
#启用 CAP 服务，此处 CAPsMAN 位于同一 LAN，但也可以在此指定 "caps-man-addresses=x.x.x.x"
/interface/wifi/cap/set enabled=yes

#在应作为 CAP 的 WiFi 接口上设置 configuration.manager=
/interface/wifi/set wifi1,wifi2 configuration.manager=capsman-or-local
```

:::note
非 MLO 與 MLO CAP 場景的唯一區別在於：MLO CAP 會自動新增 MLD 介面，並且應在 `/interface/wifi/cap` 下配置 `mld-datapath=capdp`。
:::

:::warning
如果 CAP 是 hAP ax<sup>2</sup> 或 hAP ax<sup>3</sup>，強烈建議在 CAP 上的橋接配置中啟用 RSTP，

configuration.manager 只應在 CAP 裝置本身上設定，不要將其傳遞給 CAP 或你預配置的配置配置檔案。
:::

:::info
應作為 CAP 的介面需要在 `/interface/wifi/set wifi1 configuration.manager=` 下進行額外配置
:::

### CAPsMAN - CAP VLAN 配置示例 {#capsman---cap-vlan-configuration-example}

在此示例中，我們將把 VLAN10 分配給主 SSID，併為訪客網路新增 VLAN20；CAPsMAN 的 ether5 連線到 CAP。

:::info
使用 "wifi-qcom" 軟體包的 CAP 可以透過 CAPsMAN 的 Datapath 獲取 "vlan-id"；使用 "wifi-qcom-ac" 軟體包的 CAP 則需要使用本示例末尾提供的配置。
:::

#### CAPsMAN {#capsman-1}

```ros
/interface/bridge
add name=br vlan-filtering=yes
/interface/vlan
add interface=br name=MAIN vlan-id=10
add interface=br name=GUEST vlan-id=20
/interface/wifi/datapath
add bridge=br name=MAIN vlan-id=10
add bridge=br name=GUEST vlan-id=20
/interface/wifi/security
add authentication-types=wpa2-psk,wpa3-psk ft=yes ft-over-ds=yes name=Security_MAIN passphrase=HaveAg00dDay
add authentication-types=wpa2-psk,wpa3-psk ft=yes ft-over-ds=yes name=Security_GUEST passphrase=HaveAg00dDay
/interface/wifi/configuration
add datapath=MAIN name=MAIN security=Security_MAIN ssid=MAIN_Network
add datapath=GUEST name=GUEST security=Security_GUEST ssid=GUEST_Network
/ip/pool
add name=dhcp_pool0 ranges=192.168.1.2-192.168.1.254
add name=dhcp_pool1 ranges=192.168.10.2-192.168.10.254
add name=dhcp_pool2 ranges=192.168.20.2-192.168.20.254
/ip/dhcp-server
add address-pool=dhcp_pool0 disabled=yes interface=br name=dhcp1
add address-pool=dhcp_pool1 interface=MAIN name=dhcp2
add address-pool=dhcp_pool2 interface=GUEST name=dhcp3
/interface/bridge/port
add bridge=br interface=ether5 
add bridge=br interface=ether4 
add bridge=br interface=ether3 
add bridge=br interface=ether2 
/interface/bridge/vlan
add bridge=br tagged=br,ether5,ether4,ether3,ether2 vlan-ids=20
add bridge=br tagged=br,ether5,ether4,ether3,ether2 vlan-ids=10
/interface/wifi/capsman
set enabled=yes interfaces=br
/interface/wifi/provisioning
add action=create-dynamic-enabled master-configuration=MAIN slave-configurations=GUEST supported-bands=5ghz-ax
add action=create-dynamic-enabled master-configuration=MAIN slave-configurations=GUEST supported-bands=2ghz-ax
/ip/address
add address=192.168.1.1/24 interface=br network=192.168.1.0
add address=192.168.10.1/24 interface=MAIN network=192.168.10.0
add address=192.168.20.1/24 interface=GUEST network=192.168.20.0
/ip/dhcp-server/network
add address=192.168.1.0/24 gateway=192.168.1.1
add address=192.168.10.0/24 gateway=192.168.10.1
add address=192.168.20.0/24 gateway=192.168.20.1
/system/identity
set name=cAP_Controller
```

:::note
當將 MLO 與 VLAN 配合使用時：

- 在安全配置檔案中僅啟用 `wpa3-psk`（MLO 不支援 `wpa2-psk`）。
- 在預配置規則中匹配 Wi-Fi 7 射頻支援的頻段，例如 `supported-bands=5ghz-be,2ghz-be`，或者省略 `supported-bands`，併為相同的 master 和 slave 配置保留單條預配置規則，使其適用於所有頻段。
- 在預配置規則中設定 `multi-link-mode=master`（或 `all`/`auto`）。請參閱[預配置](#provisioning)。
:::

#### 使用 "wifi-qcom" 和 "wifi-mediatek" 軟體包的 CAP {#cap-using-wifi-qcom-and-wifi-mediatek-packages}

```ros
/interface/bridge
add name=bridgeLocal
/interface/wifi/datapath
add bridge=bridgeLocal comment=defconf disabled=no name=capdp
/interface/wifi
set [ find default-name=wifi1 ] configuration.manager=capsman datapath=capdp disabled=no
set [ find default-name=wifi2 ] configuration.manager=capsman datapath=capdp disabled=no
/interface/bridge/port
add bridge=bridgeLocal comment=defconf interface=ether1
add bridge=bridgeLocal comment=defconf interface=ether2
add bridge=bridgeLocal comment=defconf interface=ether3
add bridge=bridgeLocal comment=defconf interface=ether4
add bridge=bridgeLocal comment=defconf interface=ether5
/interface/wifi/cap
set discovery-interfaces=bridgeLocal enabled=yes slaves-datapath=capdp
/ip/dhcp-client
add interface=bridgeLocal disabled=no
```

:::note
使用支援 MLO 的 CAP 時，請確保 `/interface/wifi/cap` 下的 `mld-datapath` 指向一個能將 MLD 介面新增到正確網橋的資料路徑配置檔案，例如 `mld-datapath=capdp`。
:::

#### 使用 "wifi-qcom-ac" 軟體包的 CAP {#cap-using-wifi-qcom-ac-package}

```ros
/interface/bridge
add name=bridgeLocal vlan-filtering=yes
/interface/wifi
set [ find default-name=wifi1 ] configuration.manager=capsman disabled=no
set [ find default-name=wifi2 ] configuration.manager=capsman disabled=no
/interface/bridge/port
add bridge=bridgeLocal comment=defconf interface=ether1
add bridge=bridgeLocal comment=defconf interface=ether2
add bridge=bridgeLocal comment=defconf interface=ether3
add bridge=bridgeLocal comment=defconf interface=ether4
add bridge=bridgeLocal comment=defconf interface=ether5
add bridge=bridgeLocal interface=wifi1 pvid=10
add bridge=bridgeLocal interface=wifi21 pvid=20
add bridge=bridgeLocal interface=wifi2 pvid=10
add bridge=bridgeLocal interface=wifi22 pvid=20
/interface/bridge/vlan
add bridge=bridgeLocal tagged=ether1 untagged=wifi1,wifi2 vlan-ids=10
add bridge=bridgeLocal tagged=ether1 untagged=wifi21,wifi22 vlan-ids=20
/interface/wifi/cap
set discovery-interfaces=bridgeLocal enabled=yes slaves-static=yes
```

:::info
檢查動態建立的介面，並將 PVID 分配給相應的介面。確保不要使用 `/interface/bridge/port/add bridge=bridgeLocal interface=all`，因為這會阻止你向 WiFi 介面應用 PVID。
:::

此外，以下配置必須新增到 **CAPsMAN 配置**中：

```ros
/interface/wifi/datapath
add bridge=br name=DP_AC
/interface/wifi/configuration
add datapath=DP_AC name=MAIN_AC security=Security_MAIN ssid=MAIN_Network
add datapath=DP_AC name=GUEST_AC security=Security_GUEST ssid=GUEST_Network
/interface/wifi/provisioning
add action=create-dynamic-enabled master-configuration=MAIN_AC slave-configurations=GUEST_AC supported-bands=5ghz-ac
add action=create-dynamic-enabled master-configuration=MAIN_AC slave-configurations=GUEST_AC supported-bands=2ghz-n
```

:::info
將示例開頭的 datapaths "MAIN/GUEST" 傳遞給 "wifi-qcom-ac" CAP 會是錯誤配置；請確保向此類裝置使用未指定 "vlan-id" 的 datapath。

對於 wifi-qcom-ac 驅動，不需要在 CAPSMAN 上設定 datapath。該示例只是說明必須省略 "vlan-id"。
:::

### CAPsMAN - OWE 配置示例 {#capsman---owe-configuration-example}

#### CAPsMAN {#capsman-2}

```ros
/interface/wifi/configuration
add country=Latvia disabled=no hide-ssid=yes name=OWE security.authentication-types=owe .owe-transition-interface=auto ssid=MikroTik_OWE
add country=Latvia disabled=no name=open security.owe-transition-interface=auto ssid=Mikrotik_open

/interface/wifi/provisioning
add action=create-dynamic-enabled disabled=no master-configuration=open slave-configurations=OWE

/interface/wifi/capsman
set ca-certificate=auto enabled=yes
```

#### CAP {#cap-1}

```ros
/interface/wifi/cap/set enabled=yes
/interface/wifi/set wifi1,wifi2 configuration.manager=capsman-or-local
```

## 屬性參考 {#property-reference}

### CAPsMAN 全域性配置 {#capsman-global-configuration}

選單：`/interface/wifi/capsman`

| 屬性 | 描述 |
| :-- | :-- |
| **ca-certificate** (*auto* \| *證書名稱*; 預設：**auto**) | 裝置 CA 證書，CAPsMAN 伺服器需要證書，CAP 上的證書是可選的。 |
| **certificate** (*auto* \| *證書名稱* \| *none*; 預設：**none**) | 裝置證書 |
| **enabled** (*no* \| *yes*) | 停用或啟用 CAPsMAN 功能 |
| **package-path** (*string*) | RouterOS 軟體包的資料夾位置。例如，使用 "/upgrade" 指定 files 部分中的升級資料夾。如果設定為空字串，CAPsMAN 可以使用內建的 RouterOS 軟體包。注意，在這種情況下，只有與 CAPsMAN 架構相同的 CAP 會被升級。 |
| **require-peer-certificate** (*yes* \| *no*; 預設：**no**) | 要求所有連線的 CAP 都具有有效證書 |
| **upgrade-policy** (*none* \| *require-same-version* \| *suggest-same-upgrade*; 預設：**none**) | 升級策略選項 <br/><ul><li>none - 不執行升級</li><li>require-same-version - CAPsMAN 建議升級 CAP 的 RouterOS 版本；如果升級失敗，則不會對 CAP 執行 provisioning。（仍然可以手動 provisioning）</li><li>suggest-same-version - CAPsMAN 建議升級 CAP 的 RouterOS 版本，如果升級失敗，仍會執行 provisioning</li></ul> |
| **interfaces** (*all* \| *介面名稱* \| *none*; 預設：**all**) | CAPsMAN 將在其上監聽第 2 層 CAP 連線的介面 |

### Provisioning {#provisioning}

用於匹配射頻的預配置規則在 `/interface/wifi/provisioning/` 選單中配置：

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*create-disabled* \| *create-enabled* \| *create-dynamic-enabled* \| none; 預設：**none**) | 如果規則匹配項由以下設定指定，則採取的操作：<ul><li><strong>create-disabled</strong> - 為 radio 建立已停用的靜態介面。即，介面將繫結到 radio，但在手動啟用介面之前，radio 不會執行；</li><li><strong>create-enabled</strong> - 建立已啟用的靜態介面。即，介面將繫結到 radio，並且 radio 將執行；</li><li><strong>create-dynamic-enabled</strong> - 建立已啟用的動態介面。即，介面將繫結到 radio，並且 radio 將執行；</li><li><strong>none</strong> - 不執行任何操作，使 radio 保持在未配置狀態；</li></ul> enabled 與 dynamic-enabled 的基本區別在於，動態介面不能手動編輯以覆蓋設定，也不能在防火牆或其他選單中引用，因為它們會被重新建立。在兩種情況下，任何 <code>/interface/wifi/configuration</code> 更改都會自動推送到 CAP。 |
| **comment** (*string*) | Provisioning 規則的簡短描述 |
| **common-name-regexp** (*string*) | 用於按 common name 匹配 radio 的正則表示式。每個 CAP 的 common name 識別符號可在 `/interface/wifi/radio` 下作為值 "REMOTE-CAP-NAME" 找到 |
| **supported-bands** (*2ghz-ax* \| *2ghz-be* \| *2ghz-g* \| *2ghz-n* \| *5ghz-a* \| *5ghz-ac* \| *5ghz-ax* \| *5ghz-be* \| *5ghz-n* \| *60ghz-ad* \| *6ghz-ax* \| *6ghz-be*) | 按支援的無線模式匹配 radio。此引數接受一個或多個頻段，以逗號分隔列表形式表示（例如，*supported-bands=5ghz-ac,5ghz-ax*）。指定多個頻段時，裝置必須支援所有列出的頻段，匹配才能成功，定義的配置才會被應用。 |
| **supported-hw-caps** (*beacon-protection* \| *channel-switch* \| *hw-protection-mode* \| *mlo* \| *qos-qualifier* \| *sniffer* \| *spectral*) | 按 radio 支援的附加功能匹配 radio，這些功能在 `/interface/wifi/radio` 下的 *hw-caps* 欄位中報告。接受一個或多個逗號分隔的值。radio 必須支援所有列出的能力，才能匹配此 provisioning 規則。 |
| **identity-regexp** (*string*) | 用於按路由器 identity 匹配 radio 的正則表示式 |
| **address-ranges** (*IpAddressRange[,IpAddressRanges] max 100x*;) | 匹配 IP 在已配置地址範圍內的 CAP。僅適用於透過 IP（而非 MAC 地址）加入 CAPsMAN 的 CAP。 |
| **master-configuration** (*string*) | 如果 **action** 指定建立介面，則將建立一個新的 master 介面，其配置設定為此 configuration profile |
| **multi-link-mode** (*all* \| *auto* \| *disabled* \| *master*; 預設：**disabled**) | 控制 provisioning 期間的 MLO（Multi-Link Operation）行為。<ul><li><strong>all</strong> 或 <strong>auto</strong> - CAPsMAN 會自動將已配置的 WiFi 介面分配為 MLD 介面的關聯鏈路。如果尚不存在匹配的 MLD 介面，將使用相應配置建立一個。這適用於 master 和 slave 介面；</li><li><strong>disabled</strong> - 在 provisioning 期間不會建立或分配任何 MLD 介面；</li><li><strong>master</strong> - 行為與 <strong>all</strong> 或 <strong>auto</strong> 相同，但僅將 master 介面新增為關聯的 MLD 鏈路；</li></ul> |
| **name-format** (*string*) | 用於構造已配置介面名稱的基礎字串。每個新介面將透過取基礎字串並在其末尾追加數字來建立。僅當字串不唯一時才會追加數字。 <br/> 如果字串中包含字元序列 <strong>%I</strong>，它將被替換為 cAP 的系統 identity，<strong>%C</strong> 將被替換為 cAP 的 TLS 證書的 Common Name，<strong>%R</strong>，或小寫的 <strong>%r</strong>，將被替換為 CAP 的 radio MAC <br/> 預設："cap-wifi" |
| **slave-name-format** (*string*) | 用於構造虛擬介面名稱的基礎字串。每個新介面將透過取基礎字串並在其末尾追加數字來建立。僅當字串不唯一時才會追加數字。 <br/> 如果字串中包含字元序列 <strong>%v</strong>，它將被替換為 "virtual"；如果包含字元序列 <strong>%m</strong>，它將被替換為 master 介面的名稱；如果字串中包含字元序列 <strong>%I</strong>，它將被替換為 cAP 的系統 identity，<strong>%C</strong> 將被替換為 cAP 的 TLS 證書的 Common Name，<strong>%R</strong>，或小寫的 <strong>%r</strong>，將被替換為 CAP 的 radio MAC <br/> 預設："<em>master-interface-name</em>-virtual" |
| **radio-mac** (*MAC 地址*) | 要匹配的 radio 的 MAC 地址。沒有預設值。 |
| **slave-configurations** (*string*) | 如果 **action** 指定建立介面，則會為列表中的每個 configuration profile 建立一個新的 slave 介面。 |
| **disabled** (*yes* \| *no*) | 指定 provisioning 規則是否被停用。 |

### CAP 配置 {#cap-configuration}

選單：`/interface/wifi/cap`

| 屬性 | 描述 |
| :-- | :-- |
| **caps-man-addresses** (*IP 地址或主機名列表* ; 預設：**_capsman._tcp.lan**) | 逗號分隔的 Manager IP 地址或主機名列表，CAP 將在發現期間嘗試聯絡這些地址或主機名 |
| **caps-man-names** () | CAP 將連線到的 CAPs Manager 名稱的有序列表；如果為空，CAP 不檢查 manager 名稱 |
| **discovery-interfaces** (*介面列表*) | CAP 應嘗試透過其發現 Manager 的介面列表 |
| **lock-to-caps-man** (*yes* \| no; 預設：**no**) | 設定 CAP 是否應鎖定到它連線的第一個 CAPsMAN。 |
| **slaves-static** (*yes* \| *no*; 預設：**no**) | 建立靜態虛擬介面，並允許為這些介面分配 IP 配置。從 CAPsMAN 應用配置時，使用 MAC 地址來記住每個 static-interface。 |
| **mld-static** (*yes* \| *no*; 預設：**no**) | 設定為 yes 時，CAPsMAN 在 cAP 上建立的 MLD 介面為靜態介面；否則為動態介面。靜態介面具有持久內部 ID，可以手動操作、新增到網橋、在防火牆規則中引用等。動態介面在重啟之間不會持久保留。應為它們分配適當的 datapath profile。 |
| **caps-man-certificate-common-names** () | CAP 將連線到的 Manager 證書 CommonName 列表；如果為空，CAP 不檢查 Manager 證書 CommonName |
| **certificate** () | 用於認證的證書 |
| **enabled** (*yes* \| *no*; 預設：**no**) | 停用或啟用 CAP 功能 |
| **current-caps-man-address** () | 顯示當前使用的 CAPsMAN 地址 |
| **current-caps-man-identity** () | 顯示當前使用的 CAPsMAN identity |
| **slaves-datapath** (*datapath profile*) | 要應用到 slave 介面的 datapath profile。主要用於指定 slave 介面在 CAP 上自動新增到的網橋。使用本地轉發（*traffic-processing=on-cap*）時必需，因為在該模式下，所有路由和轉發決策都由 CAP 本身做出 — CAPsMAN 不會將這些介面包含在其自己的網橋中，因此必須在此處或在 CAP 上手動設定 datapath。 |
| **mld-datapath** (*datapath profile*) | 要應用到 CAPsMAN 建立的 MLD 介面的 datapath profile。決定流量在 MLD 介面上的轉發方式，包括將其新增到哪個網橋，以及轉發是在 CAP 上本地處理還是由 CAPsMAN 集中處理。僅在 MLD 使用時生效。 |

### 遠端 CAP {#remote-cap}

執行 `/interface/wifi/capsman/remote-cap/print detail` 命令可以檢視有關遠端 CAP 的資訊。

| 屬性 | 說明 |
| :-- | :-- |
| **address**(*IP address/MAC address%interface*) | CAP 的 IP 地址，或用於連線到 CAPsMAN 的 MAC 地址 |
| **identity** (*list of integers*) | CAP 的已配置系統身份 |
| **board-name** (*string*) | 描述型號名稱 |
| **serial** (*string*) | CAP 的序列號 |
| **version** (*string*) | CAP 的 RouterOS 版本 |
| **base-mac** (*MAC address*) | CAP 以 '[XX:XX:XX:XX:XX:XX]' 形式提供的基礎 MAC |
| **common-name** (*string*) | CAP 的通用名稱 |
| **connected-time** (*time*) | 自 CAP 連線到 CAPsMAN 以來經過的時間間隔 |
| **uptime** (*time*) | 自啟動以來經過的時間間隔 |
