---
sidebar_key: "wireless/abgn/capsman/index"
sidebar_position: 4
title: "CAPsMAN"
sidebar_label: "CAPsMAN"
description: "本頁面介紹 RouterOS 中的 CAPsMAN（集中式接入點管理），涵蓋無線控制器設定的配置，包括 AAA 認證、RADIUS 伺服器整合、用於用戶端管理的訪問列表以及安全配置檔案。其中詳細說明了 MAC 地址格式、快取間隔和 RADIUS 計費更新等引數，並提供了跨多個 SSID 進行 radius 認證的示例配置。"
tags:
  - 'caps-man'
  - 'radius'
  - 'access-list'
source: https://manual.mikrotik.com/docs/7.24/wireless/abgn/capsman
captured_at: '2026-11-04T11:35:26+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
這是舊版 CAPsMAN（`/caps-man`），供執行 `wireless` 軟體包（`/interface/wireless`）的裝置使用。對於執行 `wifi-qcom` 或 `wifi-qcom-ac` 軟體包（`/interface/wifi` 選單）的裝置，請改閱 [WiFi CAPsMAN](../../wifi/capsman.md)。兩者相互獨立：WiFi CAP 只能加入 WiFi CAPsMAN，舊版 CAP 只能加入舊版 CAPsMAN。
:::

本節介紹 CAPsMAN 無線控制器文件。可用它為受支援的 RouterOS 無線裝置配置集中式接入點管理。

<DocCardList />

## CAPsMAN AAA {#capsman-aaa}

用於配置 CAPsMAN AAA 功能的設定位於 `/caps-man/aaa` 選單中：

| 屬性 | 說明 |
| :-- | :-- |
| **mac-format** (*string*；預設值：**XX:XX:XX:XX:XX:XX**) | 控制接入點在 MAC 認證和 MAC 計費 RADIUS 請求的 User-Name 屬性中如何編碼用戶端的 MAC 地址。 |
| **mac-mode** (*as-username \| as-username-and-password*；預設值：**as-username**) | 預設情況下，接入點在 MAC 認證期間傳送 Access-Request 時使用空密碼。當此屬性設定為 as-username-and-password 時，接入點會將 User-Password 屬性設定為與 User-Name 屬性相同的值。 |
| **mac-caching** (*disabled \| time-interval*；預設值：**disabled**) | 如果將此值設定為時間間隔，接入點會快取 RADIUS MAC 認證響應一段指定時間，並且在已存在匹配快取條目時不再聯絡 RADIUS 伺服器。值 disabled 會停用快取。接入點將始終聯絡 RADIUS 伺服器。 |
| **interim-update** (*disabled \| time-interval*；預設值：**disabled**) | 使用 RADIUS 計費時，接入點會定期向 RADIUS 伺服器傳送計費資訊更新。此屬性指定預設更新間隔，RADIUS 伺服器可使用 [Acct-Interim-Interval](#capsman-aaa) 屬性覆蓋該間隔。 |
| **called-format** (*mac \| mac:ssid \| ssid*；預設值：**mac:ssid**) | 指定 "called-id" 識別符號傳遞給 RADIUS 的格式。配置 radius 伺服器用戶端時，可以指定 "called-id" 以分隔多個條目。 |

### 示例 {#example}

假設其餘設定均已配置，只剩下“Security”部分。

#### 使用單個伺服器進行 RADIUS 認證 {#radius-authentication-with-one-server}

1. 建立 CAPsMAN 安全配置。

2. 配置 Radius 伺服器用戶端。

3. 將配置分配到主配置檔案（或直接分配到 CAP 本身）。

```ros
/caps-man/security/add authentication-types=wpa2-eap eap-methods=passthrough encryption=aes-ccm group-encryption=aes-ccm name=radius
/radius/add address=x.x.x.x secret=SecretUserPass service=wireless
/caps-man/configuration/set security=radius
```

#### 為每個 SSID 使用不同 RADIUS 伺服器進行 RADIUS 認證 {#radius-authentication-with-different-radius-servers-for-each-ssid}

1. 建立 CAPsMAN 安全配置。

2. 配置 AAA 設定。

3. 配置 Radius 伺服器用戶端。

4. 將配置分配到主配置檔案（或直接分配到 CAP 本身）。

```ros
/caps-man/security/add authentication-types=wpa2-eap eap-methods=passthrough encryption=aes-ccm group-encryption=aes-ccm name=radius 
/caps-man/aaa/set called-format=ssid 
/radius/add address=x.x.x.x secret=SecretUserPass service=wireless called-id=SSID1 
/radius/add address=y.y.y.y secret=SecretUserPass service=wireless called-id=SSID2 
/caps-man/configuration/set security=radius
```

現在，所有連線到 ssid=**SSID1** 的 CAP 的使用者，其 radius 認證請求都會發送到 **x.x.x.x**；所有連線到 ssid=**SSID2** 的 CAP 的使用者，其 radius 認證請求都會發送到 **y.y.y.y**。

## CAPsMAN 訪問列表 {#capsman-access-list}

CAPsMAN 上的訪問列表是一個有序規則列表，用於允許/拒絕用戶端連線到 CAPsMAN 控制下的任何 CAP。當用戶端嘗試連線到由 CAPsMAN 控制的 CAP 時，CAP 會將該請求轉發給 CAPsMAN。作為註冊過程的一部分，CAPsMAN 會查詢訪問列表，以確定是否應允許用戶端連線。訪問列表的預設行為是允許連線。

訪問列表規則會逐條處理，直到找到匹配規則。然後執行匹配規則中的動作。如果動作指定應接受用戶端，則接受該用戶端，並可能用訪問列表規則中指定的連線引數覆蓋其預設連線引數。

訪問列表在 `/caps-man/access-list` 選單中配置。訪問列表規則有以下引數：

- 用戶端匹配引數：
  - address - 用戶端的 MAC 地址。
  - mask - 比較用戶端地址時要應用的 MAC 地址掩碼。
  - interface - 可選介面，用於與用戶端實際連線的介面進行比較。
  - time - 規則匹配的時段和星期幾。
  - signal-range - 規則匹配時用戶端訊號必須落入的範圍。
  - allow-signal-out-of-range - 允許用戶端訊號始終或在一段時間間隔內超出範圍的選項。
- 動作引數 - 指定用戶端匹配時要執行的動作：
  - accept - 接受用戶端。
  - reject - 拒絕用戶端。
  - query-radius - 查詢 RADIUS 伺服器，以確定是否允許特定用戶端連線。
- 連線引數：
  - ap-tx-limit - 朝向用戶端方向的傳送速率限制。
  - client-tx-limit - 朝向 AP 方向的傳送速率限制（僅適用於 RouterOS 用戶端）。
  - client-to-client-forwarding - 指定是否允許將從該用戶端收到的資料轉發到連線到同一介面的其他用戶端。
  - private-passphrase - 如果使用某種 PSK 認證演算法，則為該用戶端使用的 *[敏感](../../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* PSK 口令。
  - radius-accounting - 指定如果為該用戶端完成 RADIUS 認證，是否應使用 RADIUS 流量計費。
  - vlan-mode - VLAN 標記模式，指定來自用戶端的流量是否應被標記（並在發往用戶端時取消標記）。
  - vlan-id - 進行 VLAN 標記時要使用的 VLAN ID。

## CAPsMAN 通道 {#capsman-channel}

通道組設定允許配置與無線電通道相關的設定列表，例如無線電頻段、頻率、Tx Power、擴充套件通道和寬度。

通道組設定在 Channels 配置檔案選單 `/caps-man/channels` 中配置。

| 屬性 | 說明 |
| :-- | :-- |
| **band** (*2ghz-b \| 2ghz-b/g \| 2ghz-b/g/n \| 2ghz-onlyg \| 2ghz-onlyn \| 5ghz-a \| 5ghz-a/n \| 5ghz-onlyn*；預設值： ) | 根據無線網路卡的硬體能力定義工作無線電頻段和模式 |
| **comment** (*string*；預設值： ) | 通道組配置檔案的簡短描述 |
| **extension-channel** (*Ce \| Ceee \| eC \| eCee \| eeCe \| eeeC \| disabled*；預設值： ) | 擴充套件通道配置。（例如 Ce = 擴充套件通道位於控制通道之上，eC = 擴充套件通道位於控制通道之下） |
| **frequency** (*integer [0..4294967295]*；預設值： ) | AP 將工作的通道頻率值，單位為 MHz。 |
| **name** (*string*；預設值： ) | 通道組配置檔案的描述性名稱 |
| **tx-power** (*integer [-30..40]*；預設值： ) | CAP 介面的 TX Power（針對整個介面，而不是單個鏈），單位為 dBm。不能設定得高於國家法規或介面允許的值。預設情況下，使用國家或介面允許的最大值。 |
| **width** (；預設值： ) | 設定通道寬度，單位為 MHz。（例如 20、40） |
| **save-selected** (；預設值：**yes**) | 為 CAP 無線電儲存所選通道——CAP 重新連線到 CAPsMAN 後將選擇此通道，並一直使用，直到對該 CAP 完成通道重新最佳化。 |

## CAPsMAN 配置 {#capsman-configuration}

配置配置檔案允許將預定義的“頂層”主設定應用於正在預配的 CAP 無線電。

配置模板在 `/caps-man/configuration` 選單中配置：

| 屬性 | 描述 |
| :-- | :-- |
| **channel** (*list*；預設值： ) | 從 Channel 名稱（`/caps-man/channels`）中獲取的使用者定義列表 |
| **channel.band** (*2ghz-b \| 2ghz-b/g \| 2ghz-b/g/n \| 2ghz-onlyg \| 2ghz-onlyn \| 5ghz-a \| 5ghz-a/n \| 5ghz-onlyn \| 5ghz-a/n/ac \| 5ghz-only-ac*；預設值： ) | 定義所用通道集合。 |
| **channel.control-channel-width** (*40mhz-turbo \| 20mhz \| 10mhz \| 5mhz*；預設值： ) | 定義所用通道寬度集合。 |
| **channel.extension-channel** (*Ce \| Ceee \| eC \| eCee \| eeCe \| eeeC \| xx \| xxxx \| disabled*；預設值： ) | 擴充套件通道配置。（例如 Ce = 擴充套件通道位於控制通道之上，eC = 擴充套件通道位於控制通道之下） |
| **channel.frequency** (*integer [0..4294967295]*；預設值： ) | AP 將工作的通道頻率值，單位為 MHz。如果留空，CAPsMAN 會自動確定佔用最少的最佳頻率。 |
| **channel.reselect-interval** (*time [00:00:00]; [00:00:00..00:00:00]*；預設值： ) | 選擇佔用最少頻率的間隔，可定義為隨機間隔，例如 "30m..60m"。僅當 **channel.frequency** 留空時有效。 |
| **channel.save-selected** (*yes \| no*；預設值：**no**) | 如果自動選擇通道頻率並且使用了 **channel.reselect-interval**，則儲存最後選取的頻率。 |
| **channel.secondary-frequency** (*integer [0..4294967295]*；預設值：**auto**) | 指定用於 80+80MHz 配置的第二個頻率。將其設定為 **Disabled** 可停用 80+80MHz 能力。 |
| **channel.skip-dfs-channels** (*yes \| no*；預設值：**no**) | 如果 **channel.frequency** 留空，選擇時將跳過 DFS 通道 |
| **channel.tx-power** (*integer [-30..40]*；預設值： ) | CAP 介面的 TX Power（針對整個介面，而不是單個鏈），單位為 dBm。不能設定得高於國家法規或介面允許的值。預設情況下，使用國家或介面允許的最大值。 |
| **channel.width** (；預設值： ) | 設定通道寬度，單位為 MHz。 |
| **comment** (*string*；預設值： ) | 配置配置檔案的簡短描述 |
| **country** (*name of the country \| no\_country\_set*；預設值：**no\_country\_set**) | 限制可用頻段、頻率以及每個頻率的最大發射功率。還指定 **scan-list** 的預設值。值 *no\_country\_set* 是一組符合 FCC 的通道。 |
| **datapath** (*list*；預設值： ) | 從 Datapath 名稱（`/caps-man/datapath`）中獲取的使用者定義列表 |
| **datapath.bridge** (*list*；預設值： ) | 應將特定介面自動新增為埠的網橋。僅當未使用 local-forwarding 時必需。 |
| **datapath.bridge-cost** (*integer [1..*200000000*]*；預設值： ) | 作為網橋埠新增時要使用的網橋埠開銷 |
| **datapath.bridge-horizon** (*integer [0..4294967295]*；預設值： ) | 作為網橋埠新增時要使用的網橋 horizon |
| **datapath.client-to-client-forwarding** (*yes \| no*；預設值：**no**) | 控制是否允許連線到介面的無線用戶端之間進行用戶端到用戶端轉發；在本地轉發模式下此功能由 CAP 執行，否則由 CAPsMAN 執行 |
| **datapath.interface-list** (；預設值： ) |  |
| **datapath.l2mtu** (；預設值： ) | 設定二層 MTU 大小 |
| **datapath.local-forwarding** (*yes \| no*；預設值：**no**) | 控制轉發模式。如果停用，所有 L2 和 L3 資料都將轉發到 CAPsMAN，之後才會做出進一步轉發決策。**注意**，如果停用，請確保同一廣播域中參與的每個 CAP 介面 MAC 地址都是唯一的（包括本地 MAC，例如 Bridge-MAC）。 |
| **datapath.mtu** (；預設值： ) | 設定 MTU 大小 |
| **datapath.openflow-switch** (；預設值： ) | 要將介面新增到的 OpenFlow 交換器埠（啟用時） |
| **datapath.vlan-id** (*integer [1..4095]*；預設值： ) | 如果 vlan-mode 啟用 VLAN 標記，則分配給介面的 VLAN ID |
| **datapath.vlan-mode** (*use-service-tag \| use-tag*；預設值： ) | 啟用並指定要分配給介面的 VLAN 標記型別（使所有接收到的資料都打上 VLAN 標記，並允許介面只發送帶有指定標記的資料） |
| **disconnect-timeout** (；預設值： ) |  |
| **distance** (；預設值： ) |  |
| **frame-lifetime** (；預設值： ) |  |
| **guard-interval** (*any \| long*；預設值：**any**) | 是否允許使用短保護間隔（請參閱 802.11n MCS 規範，瞭解這可能如何影響吞吐量）。"any" 將根據資料速率使用短或長保護間隔，"long" 將僅使用長保護間隔。 |
| **hide-ssid** (*yes \| no*；預設值： ) | yes - AP 不會在信標幀中包含 SSID，也不會回覆具有廣播 SSID 的探測請求。no - AP 會在信標幀中包含 SSID，並回復具有廣播 SSID 的探測請求。此屬性僅在 AP 模式下生效。將其設定為 *yes* 可能會使某些用戶端軟體顯示的無線網路列表中移除該網路。更改此設定不會提高無線網路的安全性，因為 AP 傳送的其他幀中仍包含 SSID。 |
| **hw-protection-mode** (；預設值： ) |  |
| **hw-retries** (；預設值： ) |  |
| **installation** (*any \| indoor \| outdoor*；預設值：**any**) |  |
| **keepalive-frames** (*enabled \| disabled*；預設值：**enabled**) |  |
| **load-balancing-group** (*string*；預設值： ) | 將介面標記到負載均衡組。要使用戶端連線到該組中的介面，該介面已連線的用戶端數量應與組中所有其他介面相同或更少。在多個 CAP 的覆蓋範圍大多重疊的部署中很有用。 |
| **max-sta-count** (*integer [1..2007]*；預設值： ) | 最大關聯用戶端數。 |
| **mode** (；預設值：**ap**) | 設定工作模式。目前僅支援 ap。 |
| **multicast-helper** (*default \| disabled \| full*；預設值：**default**) | 設定為 full 時，組播封包將使用單播目標 MAC 地址傳送，從而解決無線鏈路上的組播問題。此選項只應在接入點上啟用，用戶端應配置為 **station-bridge** 模式。disabled - 停用助手，並使用組播目標 MAC 地址傳送組播封包。full - 在傳送前將所有組播封包的 MAC 地址更改為單播 MAC 地址。default - 預設選擇，目前設定為 disabled。該值可能會在將來的版本中更改。 |
| **name** (*string*；預設值： ) | Configuration Profile 的描述性名稱 |
| **rates** (；預設值： ) | 從 Rates 名稱（`/caps-man/rates`）中獲取的使用者定義列表 |
| **rates.basic** (*1Mbps \| 2Mbps \| 5.5Mbps \| 6Mbps \| 9Mbps \| 11Mbps \| 12Mbps \| 18Mbps \| 24Mbps \| 36Mbps \| 48Mbps \| 54Mbps*；預設值： ) |  |
| **rates.supported** (*1Mbps \| 2Mbps \| 5.5Mbps \| 6Mbps \| 9Mbps \| 11Mbps \| 12Mbps \| 18Mbps \| 24Mbps \| 36Mbps \| 48Mbps \| 54Mbps*；預設值： ) |  |
| **rates.ht-basic-mcs** (*list of (mcs-0 \| mcs-1 \| mcs-2 \| mcs-3 \| mcs-4 \| mcs-5 \| mcs-6 \| mcs-7 \| mcs-8 \| mcs-9 \| mcs-10 \| mcs-11 \| mcs-12 \| mcs-13 \| mcs-14 \| mcs-15 \| mcs-16 \| mcs-17 \| mcs-18 \| mcs-19 \| mcs-20 \| mcs-21 \| mcs-22 \| mcs-23)*；預設值：**mcs-0; mcs-1; mcs-2; mcs-3; mcs-4; mcs-5; mcs-6; mcs-7**) | 每個連線的用戶端都必須支援的 [調製與編碼方案](http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates)。有關 MCS 規範，請參閱 802.11n。 |
| **rates.ht-supported-mcs** (*list of (mcs-0 \| mcs-1 \| mcs-2 \| mcs-3 \| mcs-4 \| mcs-5 \| mcs-6 \| mcs-7 \| mcs-8 \| mcs-9 \| mcs-10 \| mcs-11 \| mcs-12 \| mcs-13 \| mcs-14 \| mcs-15 \| mcs-16 \| mcs-17 \| mcs-18 \| mcs-19 \| mcs-20 \| mcs-21 \| mcs-22 \| mcs-23)*；預設值：**mcs-0; mcs-1; mcs-2; mcs-3; mcs-4; mcs-5; mcs-6; mcs-7; mcs-8; mcs-9; mcs-10; mcs-11; mcs-12; mcs-13; mcs-14; mcs-15; mcs-16; mcs-17; mcs-18; mcs-19; mcs-20; mcs-21; mcs-22; mcs-23**) | 此裝置宣告支援的 [調製與編碼方案](http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates)。有關 MCS 規範，請參閱 802.11n。 |
| **rates.vht-basic-mcs** (*none \| MCS 0-7 \| MCS 0-8 \| MCS 0-9*；預設值：**none**) | 每個連線的用戶端都必須支援的 [調製與編碼方案](../../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)。有關 MCS 規範，請參閱 802.11ac。可以為每個空間流設定 MCS 區間：none - 將不使用所選空間流；MCS 0-7 - 用戶端必須支援 MCS-0 到 MCS-7；MCS 0-8 - 用戶端必須支援 MCS-0 到 MCS-8；MCS 0-9 - 用戶端必須支援 MCS-0 到 MCS-9 |
| **rates.vht-supported-mcs** (*none \| MCS 0-7 \| MCS 0-8 \| MCS 0-9*；預設值：**none**) | 此裝置宣告支援的 [調製與編碼方案](http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed)。有關 MCS 規範，請參閱 802.11ac。可以為每個空間流設定 MCS 區間：none - 將不使用所選空間流；MCS 0-7 - 裝置將宣告支援 MCS-0 到 MCS-7；MCS 0-8 - 裝置將宣告支援 MCS-0 到 MCS-8；MCS 0-9 - 裝置將宣告支援 MCS-0 到 MCS-9 |
| **rx-chains** (*list of integer [0..3]*；預設值：**0**) | 用於接收的天線。 |
| **security** (*string*；預設值：**none**) | 來自 `/caps-man/security` 的安全配置名稱 |
| **security.authentication-types** (*list of string*；預設值：**none**) | 指定認證型別，可選值為 **wpa-psk**、**wpa2-psk**、**wpa-eap** 或 **wpa2-eap** |
| **security.disable-pmkid** (；預設值： ) |  |
| **security.eap-methods** (*eap-tls \| passthrough*；預設值：**none**) | eap-tls - 使用內建 EAP TLS 認證。passthrough - 接入點會將認證過程中繼到 RADIUS 伺服器。 |
| **security.eap-radius-accounting** (；預設值： ) | 指定如果為該用戶端完成 RADIUS 認證，是否應使用 RADIUS 流量計費 |
| **security.encryption** (*aes-ccm \| tkip*；預設值： ) | 設定所使用的單播加密演算法型別 |
| **security.group-encryption** (*aes-ccm \| tkip*；預設值：**aes-ccm**) | 接入點會通告這些密碼之一，可以選擇多個值。接入點使用它來加密所有廣播和組播幀。用戶端只會嘗試連線到使用指定組密碼之一的接入點。tkip - Temporal Key Integrity Protocol - 加密協定，與舊版 WEP 裝置相容，但經過增強以修正一些 WEP 缺陷。aes-ccm - 更安全的 WPA 加密協定，基於可靠的 AES（Advanced Encryption Standard）。沒有 WEP 遺留問題的網路應只使用此密碼。 |
| **security.group-key-update** (*time: 30s..1h*；預設值：**5m**) | 控制接入點更新組金鑰的頻率。此金鑰用於加密所有廣播和組播幀。該屬性僅對 Access Point 生效。 |
| **security.passphrase** (*string*；預設值： ) *[敏感](../../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | WPA 或 WPA2 預共享金鑰 |
| **security.tls-certificate** (*none \| name*；預設值： ) | 當 **security.tls-mode** 設定為 **no-certificates** 以外的值時，接入點始終需要證書。 |
| **security.tls-mode** (*verify-certificate \| dont-verify-certificate \| no-certificates \| verify-certificate-with-crl*；預設值： ) | 此屬性僅在 **security.eap-methods** 包含 *eap-tls* 時生效。verify-certificate - 要求遠端裝置具有有效證書。檢查該證書是否由已知證書頒發機構簽名。不會進行額外的身份驗證。證書可能包含其有效時間段的資訊。如果路由器的時間和日期不正確，可能會因為路由器的時鐘不在該時間段內而拒絕有效證書。另請參閱 Certificates 配置。dont-verify-certificate - 不檢查遠端裝置的證書。接入點不會要求用戶端提供證書。no-certificates - 不使用證書。TLS 會話使用 2048 位匿名 Diffie-Hellman 金鑰交換建立。verify-certificate-with-crl - 與 verify-certificate 相同，但還會透過檢查證書吊銷列表來驗證證書是否有效。 |
| **ssid** (*string (0..32 chars)*；預設值： ) | SSID（服務集識別符號）是在信標中廣播的名稱，用於標識無線網路。 |
| **tx-chains** (*list of integer [0..3]*；預設值：**0**) | 用於傳送的天線。 |

## CAPsMAN 資料路徑 {#capsman-datapath}

資料路徑設定控制與資料轉發相關的方面。在 CAPsMAN 中，資料路徑設定可在資料路徑配置檔案選單 `/caps-man/datapath` 中配置，也可在配置配置檔案或介面選單中直接以帶 **datapath.** 字首的設定進行配置。

有 2 種主要轉發模式：

- 本地轉發模式，其中 CAP 在本地向無線介面轉發資料以及從無線介面轉發資料。
- 管理器轉發模式，其中 CAP 將無線接收到的所有資料傳送給 CAPsMAN，並且只發送從 CAPsMAN 收到的無線資料。在此模式下，甚至用戶端到用戶端轉發也由 CAPsMAN 控制和執行。

轉發模式按介面配置——因此，如果一個 CAP 提供 2 個射頻介面，一個可以配置為在本地轉發模式下執行，另一個可以配置為在 Manager 轉發模式下執行。這同樣適用於 Virtual-AP 介面——每個介面可以具有與主介面或其他 Virtual-AP 介面不同的轉發模式。

大多數 datapath 設定僅在 Manager 轉發模式下使用，因為在本地轉發模式下，CAPsMAN 無法控制資料轉發。

有以下 datapath 設定：

- bridge -- 啟用時，要將介面作為網橋埠新增到的網橋介面。
- bridge-cost -- 作為網橋埠新增時要使用的網橋埠開銷。
- bridge-horizon -- 作為網橋埠新增時要使用的網橋 horizon。
- client-to-client-forwarding -- 控制是否允許連線到介面的無線用戶端之間進行用戶端到用戶端轉發；在本地轉發模式下此功能由 CAP 執行，否則由 CAPsMAN 執行。
- local-forwarding -- 控制轉發模式。
- openflow-switch -- 啟用時，要將介面作為埠新增到的 OpenFlow 交換器。
- vlan-id -- 如果 vlan-mode 啟用 VLAN 標記，則分配給介面的 VLAN ID。
- vlan-mode -- VLAN 標記模式，指定是否應為介面分配 VLAN 標記（使所有接收到的資料都打上 VLAN 標記，並允許介面只發送帶有指定標記的資料）。

## CAPsMAN 介面 {#capsman-interface}

CAPsMAN 介面在 `/caps-man/interface` 選單中管理：

```ros
[admin@CM] > /caps-man/interface/print 
Flags: M - master, D - dynamic, B - bound, X - disabled, I - inactive, R - running 
# NAME RADIO-MAC MASTER-INTERFACE 
0 M BR cap2 00:0C:42:1B:4E:F5 none 
1 B cap3 00:00:00:00:00:00 cap2
```

## CAPsMAN 管理器 {#capsman-manager}

| 屬性 | 描述 |
| :-- | :-- |
| **enabled** (*yes \| no*；預設值：**no**) | 停用或啟用 CAPsMAN 功能 |
| **certificate** (*auto \| certificate name \| none*; Default: **none**) | 裝置證書 |
| **ca-certificate** (*auto \| certificate name \| none*；預設值：**none**) | 裝置 CA 證書 |
| **require-peer-certificate** (*yes \| no*；預設值：**no**) | 要求所有連線的 CAP 都具有有效證書 |
| **package-path** (*string \|*；預設值： ) | RouterOS 軟體包的資料夾位置。例如，使用 "/upgrade" 指定檔案部分中的 upgrade 資料夾。如果設定為空字串，CAPsMAN 可以使用內建 RouterOS 軟體包；請注意，在這種情況下，只有與 CAPsMAN 架構相同的 CAP 才會被升級。 |
| **upgrade-policy** (*none \| require-same-version \| suggest-same-version*；預設值：**none**) | CAPsMAN 可以向 CAP 裝置傳送 NPK 軟體包以進行升級。這會繞過 CAP 裝置可能具有的任何升級通道偏好，並透過簡單的版本號比較來工作。如果 CAPsMAN 上安裝了更新版本，它將傳送軟體包並升級裝置，無論通道如何。none - 不執行升級。require-same-version - CAPsMAN 建議升級 CAP 的 RouterOS 版本；如果升級失敗，則不會預配該 CAP。（仍可手動預配。）suggest-same-version - CAPsMAN 建議升級 CAP 的 RouterOS 版本；如果升級失敗，仍會進行預配。 |

## CAPsMAN 預配置 {#capsman-provisioning}

CAPsMAN 根據 common-name 識別符號來區分 CAP。該識別符號根據以下規則生成：

- 如果 CAP 提供證書，則識別符號設定為證書中的 Common Name 欄位。
- 否則，識別符號基於 CAP 提供的 Base-MAC，格式為：'[XX:XX:XX:XX:XX:XX]'。

當與 CAP 的 DTLS 連線成功建立時（這意味著 CAP 識別符號已知且有效），CAPsMAN 會確保不存在使用相同識別符號的陳舊 CAP 連線。當前連線的 CAP 列在 `/caps-man/remote-cap` 選單中：

```ros
[admin@CM] /caps-man> remote-cap print 
# ADDRESS IDENT STATE RADIOS
0 00:0C:42:00:C0:32/27044 MT-000C4200C032 Run 1
```

CAPsMAN 根據實際無線介面（無線電）的內建 MAC 地址（radio-mac）來區分它們。這意味著無法在一個 CAPsMAN 上管理兩個具有相同 MAC 地址的無線電。當前由 CAPsMAN 管理（由已連線 CAP 提供）的無線電列在 `/caps-man/radio` 選單中：

```ros
[admin@CM] /caps-man> radio print 
Flags: L - local, P - provisioned 
# RADIO-MAC INTERFACE REMOTE-AP-IDENT 
0 P 00:03:7F:48:CC:07 cap1 MT-000C4200C032
```

當 CAP 連線時，CAPsMAN 首先嚐試根據 radio-mac 將每個 CAP 無線電繫結到 CAPsMAN 主介面。如果找到合適的介面，則會使用主介面配置以及引用該特定主介面的從介面配置來設定該無線電。此時，這些介面（主介面和從介面）被視為已繫結到該無線電，並且該無線電被視為已預配。

如果未找到與該射頻匹配的主介面，CAPsMAN 將執行“預配規則”。預配規則是一個有序規則列表，其中包含指定要匹配哪些射頻的設定，以及指定射頻匹配後採取何種操作的設定。

用於匹配無線電的預配規則在 `/caps-man/provisioning` 選單中配置：

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*create-disabled \| create-enabled \| create-dynamic-enabled \| none*；預設值：**none**) | 規則匹配時要執行的動作，由以下設定指定：create-disabled - 為無線電建立停用的靜態介面。也就是說，介面將繫結到該無線電，但在手動啟用介面之前，該無線電不會工作；create-enabled - 建立啟用的靜態介面。也就是說，介面將繫結到該無線電，並且該無線電將工作；create-dynamic-enabled - 建立啟用的動態介面。也就是說，介面將繫結到該無線電，並且該無線電將工作；none - 不執行任何操作，使無線電保持未預配狀態； |
| **comment** (*string*；預設值： ) | 預配規則的簡短描述 |
| **common-name-regexp** (*string*；預設值： ) | 用於按 common name 匹配無線電的正則表示式。每個 CAP 的 common name 識別符號可在 `/caps-man/radio` 下作為值 "REMOTE-CAP-NAME" 找到 |
| **hw-supported-modes** (*a\|a-turbo\|ac\|an\|b\|g\|g-turbo\|gn*；預設值： ) | 按支援的無線模式匹配無線電 |
| **identity-regexp** (*string*；預設值： ) | 用於按路由器身份匹配無線電的正則表示式 |
| **ip-address-ranges** (*IpAddressRange[,IpAddressRanges] max 100x*；預設值：**""**) | 匹配 IP 位於所配置地址範圍內的 CAP。 |
| **master-configuration** (*string*；預設值： ) | 如果 **action** 設定為建立介面，則將建立一個新的主介面，其配置設定為此配置配置檔案 |
| **name-format** (*cap \| identity \| prefix \| prefix-identity*；預設值：**cap**) | 指定 CAP 介面名稱建立的語法：cap - 預設名稱；identity - CAP 板的系統身份名稱；prefix - 來自 name-prefix 值的名稱；prefix-identity - 來自 name-prefix 值和 CAP 板系統身份名稱的名稱 |
| **name-prefix** (*string*；預設值： ) | 可在 name-format 中用於建立 CAP 介面名稱的名稱字首 |
| **radio-mac** (*MAC address*；預設值：**00:00:00:00:00:00**) | 要匹配的無線電的 MAC 地址；空 MAC（00:00:00:00:00:00）表示匹配所有 MAC 地址 |
| **slave-configurations** (*string*；預設值： ) | 如果 **action** 設定為建立介面，則為該列表中的每個配置配置檔案建立一個新的從介面。 |

:::warning
如果沒有規則匹配該無線電，則執行隱式預設規則，其動作為 **create-enabled**，且未設定任何配置。
:::

獲取活動的預配匹配器：

```ros
[admin@CM] /caps-man/provisioning> print 
Flags: X - disabled 
0 radio-mac=00:00:00:00:00:00 action=create-enabled master-configuration=main-cfg 
slave-configurations=virtual-ap-cfg name-prefix=""
```

為方便使用者，有一些命令可以針對某個無線電或某個 AP 提供的所有無線電重新執行預配過程：

```ros
[admin@CM] > /caps-man/radio/provision 0
```

以及

```ros
[admin@CM] > /caps-man/remote-cap/provision 0
```

### CAPsMAN 無線電 {#capsman-radio}

[參見 `/caps-man/provisioning`](#capsman-provisioning)

### CAPsMAN 速率 {#capsman-rates}

[參見 `/caps-man/configuration`](#capsman-configuration)

### CAPsMAN 登錄檔 {#capsman-registration-table}

登錄檔包含連線到由 CAPsMAN 控制的射頻的用戶端列表，可在 `/caps-man/registration-table` 選單中檢視：

```ros
[admin@CM] /caps-man> registration-table print
# INTERFACE MAC-ADDRESS UPTIME RX-SIGNAL
0 cap1 00:03:7F:48:CC:0B 1h38m9s210ms -36
```

### CAPsMAN 遠端 CAP {#capsman-remote-cap}

[參見 `/caps-man/provisioning`](#capsman-provisioning)

### CAPsMAN 安全 {#capsman-security}

假設其餘設定均已配置，只剩下“Security”部分。

**使用單個伺服器進行 RADIUS 認證**

1. 建立 CAPsMAN 安全配置。

2. 配置 Radius 伺服器用戶端。

3. 將配置分配到主配置檔案（或直接分配到 CAP 本身）。

```ros
/caps-man/security/add authentication-types=wpa2-eap eap-methods=passthrough encryption=aes-ccm group-encryption=aes-ccm name=radius 
/radius/add address=x.x.x.x secret=SecretUserPass service=wireless 
/caps-man/configuration/set security=radius
```

**為每個 SSID 使用不同 RADIUS 伺服器進行 RADIUS 認證**

1. 建立 CAPsMAN 安全配置。

2. 配置 AAA 設定。

3. 配置 Radius 伺服器用戶端。

4. 將配置分配到主配置檔案（或直接分配到 CAP 本身）。

```ros
/caps-man/security/add authentication-types=wpa2-eap eap-methods=passthrough encryption=aes-ccm group-encryption=aes-ccm name=radius 
/caps-man/aaa/set called-format=ssid 
/radius/add address=x.x.x.x secret=SecretUserPass service=wireless called-id=SSID1 
/radius/add address=y.y.y.y secret=SecretUserPass service=wireless called-id=SSID2 
/caps-man/configuration/set security=radius
```

現在，所有連線到 ssid=**SSID1** 的 CAP 的使用者，其 radius 認證請求都會發送到 **x.x.x.x**；所有連線到 ssid=**SSID2** 的 CAP 的使用者，其 radius 認證請求都會發送到 **y.y.y.y**。
