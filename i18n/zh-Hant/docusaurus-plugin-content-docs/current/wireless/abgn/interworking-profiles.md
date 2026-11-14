---
sidebar_key: "wireless/abgn/interworking-profiles"
sidebar_position: 3
title: "互通配置檔案"
sidebar_label: "互通配置檔案"
description: "本頁介紹用於無線網路的 MikroTik RouterOS 互通配置檔案，使裝置能夠透過 IEEE 802.11u 和 Hotspot 2.0 標準交換資訊。文中詳細說明了網路型別、ANQP 元素和場所資訊等配置屬性，以增強用戶端裝置的選擇與安全性。"
tags:
  - 'interworking'
  - 'hotspot-20'
  - 'anqp'
source: https://manual.mikrotik.com/docs/wireless/abgn/interworking-profiles
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 互通 {#interworking}

互通是指兩個或多個事物協同工作。為了獲得更好的無線網路體驗，接入點與無線用戶端裝置之間必須交換網路資訊。基本無線信標和探測請求中可包含的資訊有限。因此，制定了 IEEE 802.11u™-2011（與外部網路互通）標準，該標準規定了裝置之間應如何交換資訊。透過網路互通服務，可以增強網路發現和接入點選擇過程。無線用戶端裝置可以有更多標準來選擇要關聯的網路。

## Hotspot 2.0 {#hotspot-20}

Hotspot 2.0 是由 Wi-Fi Alliance 制定並擁有的規範。它旨在讓連線 Wi-Fi 網路時獲得更接近蜂窩網路的體驗。為了提高無線網路安全性，Hotspot 2.0 接入點使用強制 WPA2 認證。Hotspot 2.0 依賴互通，並增加了自身的一些屬性和流程。

互通配置檔案按照 IEEE 802.11u 和 Hotspot 2.0 Release 1 規範實現。

:::info
本手冊頁面介紹舊版 `wireless` 軟體包（`/interface/wireless`）的互通配置。對於 `wifi` 軟體包（`/interface/wifi`），請參閱 [WiFi6 的互通](../wifi/interworking-for-wifi6.md)。
:::

## 配置屬性 {#configuration-properties}

**子選單：** `/interface/wireless/interworking-profiles`

### 信標和探測響應中的資訊元素 {#information-elements-in-beacon-and-probe-response}

可以透過 Interworking 元素向信標和探測響應封包新增一些資訊。Interworking 元素的以下引數可以配置：

| 屬性 | 描述 |
| :-- | :-- |
| **asra** (*yes \| no*；預設值：**no**) | 訪問所需的額外步驟。如果使用者需要採取額外步驟才能訪問網際網路（例如圍牆花園），則設定為 `yes`。 |
| **esr** (*yes \| no*; 預設值：**no**) | 緊急服務可達 (ESR)。設定為 `yes` 以表示可透過該接入點訪問緊急服務。 |
| **hessid** (*MAC 地址*；預設值：) | 同構擴充套件服務集識別符號（HESSID）。提供對同一外部網路訪問的裝置處於同一個同構擴充套件服務集中。該服務集可透過 HESSID 標識，此服務集中所有接入點上的 HESSID 相同。HESSID 的 6 位元組值表示為 MAC 地址。它應全域性唯一，因此建議使用該服務集中某個接入點的 MAC 地址。 |
| **internet** (*yes \| no*; 預設值：**yes**) | 透過此連線是否可訪問網際網路。此資訊包含在 Interworking 元素中。 |
| **network-type** (*emergency-only \| personal-device \| private \| private-with-guest \| public-chargeable \| public-free \| test \| wildcard*；預設值：**wildcard**) | 關於網路接入型別的資訊。<code>emergency-only</code> - 專用於且僅限於訪問緊急服務的網路；<code>personal-device</code> - 個人裝置網路。此類網路的一個示例是連線到印表機的相機，從而形成用於列印照片的網路；<code>private</code> - 供擁有使用者賬戶的使用者使用的網路。通常用於企業中的員工，而不是訪客；<code>private-with-guest</code> - 與 private 相同，但提供訪客賬戶；<code>public-chargeable</code> - 任何人付費即可使用的網路。例如，Hotspot 2.0 服務訂閱或酒店客房內網際網路接入；<code>public-free</code> - 任何人無需付費即可使用的網路。例如，城市中的市政網路或機場 Hotspot；<code>test</code> - 用於測試和實驗用途的網路。不用於生產環境；<code>wildcard</code> - 用於無線用戶端。傳送將網路型別值設為 wildcard 的探測請求會使所有互通接入點響應，而不管其實際 network-type 設定如何。用戶端傳送 network-type 設定為其感興趣值的探測請求幀。它將僅收到具有相同值的接入點的回覆（wildcard 的情況除外）。 |
| **uesa** (*yes \| no*; 預設值：**no**) | 未認證緊急服務可訪問 (UESA)。<code>no</code> - 表示無法透過此接入點訪問未認證緊急服務；<code>yes</code> - 表示可透過此接入點訪問更高層的未認證緊急服務。 |
| **venue** (*venue*；預設值：**unspecified**) | 指定接入點所在的場所。從可用值中選擇。一些示例：`venue=business-bank``venue=mercantile-shopping-mall``venue=educational-university-or-college` |

### ANQP 元素 {#anqp-elements}

接入網路查詢協定（ANQP）。並非所有必要資訊都包含在探測響應和信標幀中。為了讓用戶端裝置在選擇要關聯的接入點之前獲取更多資訊，會使用 ANQP。接入點可以在多個 ANQP 元素中儲存資訊。用戶端裝置將使用 ANQP 僅查詢其感興趣的資訊。這可減少關聯前所需的時間。

| 屬性 | 描述 |
| :-- | :-- |
| **3gpp-raw** (*octet string in hex*；預設值：) | 蜂窩網路通告資訊 - 國家和網路程式碼。這有助於 Hotspot 2.0 用戶端選擇接入點以訪問 3GPP 網路。有關此欄位的格式，請參閱 3GPP TS 24.302（附錄 H）。如果被查詢，此值會在 ANQP 響應中傳送。 |
| **3gpp-info**(*number/number*；預設值：) | 蜂窩網路通告資訊 - 國家和網路程式碼。這有助於 Hotspot 2.0 用戶端選擇接入點以訪問 3GPP 網路。寫作 "mcc/mnc"。用法與 "3gpp-raw" 相同，但不使用十六進位制。可以透過逗號分隔來定義多個 mcc/mnc 對。 |
| **authentication-types** (*dns-redirection:`url` \| https-redirection:`url` \| online-enrollment:`url` \| terms-and-conditions:`url`*；預設值：) | 此屬性僅在 asra 設定為 `yes` 時有效。`url` 的值是可選的；如果選擇了 `dns-redirection` 或 `online-enrollment`，則不需要該值。要將 `url` 的值設定為空字串，請使用雙引號。例如：`authentication-types=online-enrollment:""` |
| **connection-capabilities** (*number:number:closed\|open\|unknown*；預設值：) | 此選項允許提供有關允許的 IP 協定和埠的資訊。此資訊可在 ANQP 響應中提供。第一個數字表示 IP 協定號，第二個數字表示埠號。<code>closed</code> - 如果協定和埠組合不被允許，則設定；<code>open</code> - 如果協定和埠組合被允許，則設定；<code>unknown</code> - 如果協定和埠組合為開放或關閉，則設定。示例：`connection-capabilities=6:80:open,17:5060:closed` 在接入點上設定此類值會告知正在連線到該接入點的無線用戶端：允許 HTTP（6 - TCP，80 - HTTP），不允許 VoIP（17 - UDP；5060 - VoIP）。此屬性不會限制或允許這些協定和埠的使用，它僅向正在連線到接入點的站裝置提供資訊。 |
| **domain-names** (*字串列表*; 預設值： ) | 零個或多個完全限定域名 (FQDN)，用於指示運營該 Hotspot 的實體。正在連線接入點的站可以請求此 ANQP 屬性，並檢查其擁有憑據的任何域名是否存在後綴匹配。 |
| **ipv4-availability** (*double-nated \| not-available \| port-restricted \| port-restricted-double-nated \| port-restricted-single-nated \| public \| single-nated \| unknown*；預設值：**not-available**) | 關於可用的 IPv4 地址和訪問方式的資訊。<code>not-available</code> - 地址型別不可用；<code>public</code> - 可用的公共 IPv4 地址；<code>port-restricted</code> - 可用的埠受限 IPv4 地址；<code>single-nated</code> - 可用的單 NAT 私有 IPv4 地址；<code>double-nated</code> - 可用的雙 NAT 私有 IPv4 地址；<code>port-restricted-single-nated</code> - 可用的埠受限 IPv4 地址和單 NAT IPv4 地址；<code>port-restricted-double-nated</code> - 可用的埠受限 IPv4 地址和雙 NAT IPv4 地址；<code>unknown</code> - 地址型別的可用性未知。 |
| **ipv6-availability** (*available \| not-available \| unknown*；預設值：**not-available**) | 關於可用的 IPv6 地址和訪問方式的資訊。<code>not-available</code> - 地址型別不可用；<code>available</code> - 地址型別可用；<code>unknown</code> - 地址型別的可用性未知。 |
| **realms** (*string:eap-sim\|eap-aka\|eap-tls\|not-specified*；預設值：) | 關於支援的 realm 及相應 EAP 方法的資訊。`realms=example.com:eap-tls,foo.ba:not-specified` |
| **realms-raw** (*十六進位制八位位元組字串*; 預設值： ) | 手動設定 NAI Realm ANQP 元素。 |
| **roaming-ois** (*octet string in hex*；預設值：) | 組織識別符號（OI）通常是 24 位唯一識別符號，例如組織唯一識別符號（OUI）或公司識別符號（CID）。在某些情況下，OI 會更長，例如 OUI-36。訂閱服務提供商（SSP）可透過其 OI 指定。roaming-ois 屬性可以包含零個或多個 SSP 的 OI，這些 SSP 的網路可透過此 AP 訪問。OI 的長度應指定在 OI 本身之前。例如，要設定 E4-8D-8C 和 6C-3B-6B：`roaming-ois=03E48D8C036C3B6B` |
| **venue-names** (*string:lang*；預設值：) | 場所名稱可用於提供有關場所的附加資訊。它可以幫助用戶端選擇合適的接入點。Venue-names 引數由零個或多個二元組組成，這些二元組包含場所名稱和語言程式碼：`venue-names=CoffeeShop:eng,TiendaDeCafe:es` 語言程式碼欄位值是從 ISO-639 中選擇的兩字元或三字元語言程式碼。 |

#### Realms 原始值 {#realms-raw}

**realms-raw** - 一個包含十六進位制值的字串列表。每個字串指定 "NAI Realm Tuple" 的內容，不包括 "NAI Realm Data Field Length" 欄位。

每個十六進位制編碼字串必須由以下欄位組成：

```
- NAI Realm Encoding (1 byte)
- NAI Realm Length (1 byte)
- NAI Realm (variable)
- EAP Method Count (1 byte)
- EAP Method Tuples (variable)
```

例如，值 "00045465737401020d00" 解碼為：

```
- NAI Realm Encoding: 0 (rfc4282)
- NAI Realm Length: 4
- NAI Realm: Test
- EAP Method Count: 1
- EAP Method Length: 2
- EAP Method Tuple: TLS, no EAP method parameters
```

請注意，設定 "realms-raw=00045465737401020d00" 會產生與設定 "realms=Test:eap-tls" 相同的通告內容。

有關完整的 NAI Realm 編碼，請參閱 802.11-2016 第 9.4.5.10 節。

### Hotspot 2.0 ANQP 元素 {#hotspot-20-anqp-elements}

Hotspot 2.0 規範引入了一些額外的 ANQP 元素。這些元素使用 ANQP 廠商特定元素 ID。以下是可用於更改這些元素的屬性。

| 屬性 | 描述 |
| :-- | :-- |
| **hotspot20** (*yes \| no*; 預設值：**yes**) | 指示接入點的 Hotspot 2.0 能力。 |
| **hotspot20-dgaf** (*yes \| no*; 預設值：**yes**) | 下游組定址轉發 (DGAF)。設定 DGAF 位值，以指示發往用戶端的組播和廣播幀是停用還是啟用。<code>yes</code> - 發往用戶端的組播和廣播幀已啟用；<code>no</code> - 發往用戶端的組播和廣播幀已停用。要停用組播和廣播幀，請設定 `multicast-helper=full`。 |
| **operational-classes** (*數字列表*; 預設值： ) | 有關同一 ESS 其他可用頻段的資訊。 |
| **operator-names** (*string:lang*；預設值：) | 設定運營商名稱。必須為每個運營商名稱條目指定語言。Operator-names 引數由零個或多個二元組組成，這些二元組包含運營商名稱和語言程式碼：`operator-names=BestOperator:eng,MejorOperador:es` 語言程式碼欄位值是從 ISO-639 中選擇的兩字元或三字元語言程式碼。 |
| **wan-at-capacity** (*yes \| no*; 預設值：**no**) | 接入點或網路是否已達到最大容量。如果設定為 `yes`，則不允許其他移動裝置關聯到 AP。 |
| **wan-downlink** (*number*; 預設值：**0**) | WAN 連線的下行速度，以 kbps 為單位設定。如果下行速度未知，請設定為 0。 |
| **wan-downlink-load** (*number*; 預設值：**0**) | 在 `wan-measurement-duration` 期間測量的 WAN 連線下行負載。值為 0 到 255。<code>0</code> - 未知；<code>255</code> - 100%。 |
| **wan-measurement-duration** (*number*; 預設值：**0**) | 測量 wan-downlink-load 和 `wan-uplink-load` 的持續時間。值為 0 到 65535 的數字，表示十分之一秒。<code>0</code> - 未測量；<code>10</code> - 1 秒；<code>65535</code> - 1 小時 49 分鐘或更長時間。 |
| **wan-status** (*down \| reserved \| test \| up*；預設值：**reserved**) | 關於接入點 WAN 連線狀態的資訊。值 `reserved` 表示不通告狀態。 |
| **wan-symmetric** (*yes \| no*; 預設值：**no**) | WAN 鏈路是否對稱（上傳和下載速度相同）。 |
| **wan-uplink** (*number*；預設值：**0**) | WAN 連線的上行速度，單位為 kbps。如果上行速度未知，請設定為 0。 |
| **wan-uplink-load** (*number*; 預設值：**0**) | 在 wan-measurement-duration 期間測量的 WAN 連線上行負載。值為 0 到 255。<code>0</code> - 未知；<code>255</code> - 100%。 |

### 其他屬性 {#other-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*；預設值：) | 配置檔案的簡短描述 |
| **name** (*string*；預設值：) | 互通配置檔案的名稱。 |

## 使用原生 RadSec 和 Orion Wifi 的配置指南 {#configuration-guide-using-native-radsec-and-orion-wifi}

本指南介紹如何設定 MikroTik 裝置，以便將其與 RadSec 代理和 Orion Wifi 配合使用；主要配置步驟保持不變，也適用於不同的提供商：
請確保使用最新的長期支援版或穩定版 RouterOS 發行版。

在無線 LAN 控制器與 Orion Wifi 之間建立安全的 RADIUS 連線非常重要。  
Orion Wifi 使用 RADIUS over TLS（RadSec）來確保 AAA 流量的端到端加密。

1) 匯入您從 Orion 下載的 RadSec 證書：

在 WinBox 中拖放證書，然後使用其匯入功能；該功能位於 WinBox 的 `/system/certificates` 下。等效的命令列如下：

```
/certificate/import file-name=bw.radsec.cacert.pem passphrase=""
/certificate/import file-name=cert.pem passphrase=""
/certificate/import file-name=key.pem passphrase=""
```

![](/img/ec7b39addec96eaa.webp)

![](/img/e93c0b62bdad9bb8.webp)

![](/img/2b9f3644dbfb3754.webp)

證書匯入後，應如下所示：

![](/img/008d1c527283a5f9.webp)

1) 配置 Radius 用戶端：

![](/img/c4e4a528043cd9a8.webp)

等效命令列如下：

```
/radius/add address=216.239.32.91 certificate=cert.pem_0 protocol=radsec service=wireless timeout=1s500ms
```

1) 建立執行 802.1x 認證的無線安全配置檔案：

![](/img/6a844b5ed2cbd001.webp)

![](/img/d13a1203c4fd8709.webp)

![](/img/ba985a4fbb9fdfd3.webp)

等效命令列如下：

```
/interface/wireless/security-profiles/add authentication-types=wpa2-eap management-protection=allowed mode=dynamic-keys name=dot1x_profile supplicant-identity="" radius-eap-accounting=yes eap-methods=passthrough
```

1) 下一步是配置無線介面並分配已建立的安全配置檔案。按“高階模式”以檢視所有選項：

![](/img/6b80df698a47676c.webp)

等效命令列如下：

```
/interface/wireless/set [ find default-name=wlan1 ] mode=ap-bridge security-profile=dot1x_profile wps-mode=disabled
```

請確保已配置正確的國家/地區配置檔案。在本例中，我們使用“wlan1”，但同一命令也適用於其他介面，或可寫為 `/interface/wireless/set wlan1`。

1) 配置互通設定（hotspot 2.0）：

![](/img/d8b8c002900a5610.webp)

![](/img/a43e7faa87cacd15.webp)

![](/img/42cd3e6d600d6811.webp)

等效命令列如下：

```
/interface/wireless/interworking-profile/add domain-names=orion.area120.com ipv4-availability=public name=Orion_MikroTik network-type=public-chargeable operator-names=Orion:eng realms=orion.area120.com:eap-tls roaming-ois=f4f5e8f5f4,baa2D00100,baa2d00000 venue=business-unspecified venue-names=Orion:eng wan-downlink=50 wan-uplink=50 wan-status=up
```

:::warning
請特別注意 "wan-downlink" 和 "wan-uplink"；在此場景中，"50" 僅用作佔位值，請務必根據您的設定調整這些值。某些用戶端裝置會用它來判斷是否應加入網路。請根據實際情況設定 “venue”（場所型別）、“venue-names” 和其他屬性。“domain-names” 應為 hotspot 2.0 運營商的域名。
:::

1) 將互通配置檔案分配給介面：

![](/img/9fd765802020f3be.webp)

等效命令列如下：

```
/interface/wireless/set wlan1 interworking-profile=Orion_MikroTik
```

如果看不到 interworking-profile 欄位，請按“高階模式”。

注意：Orion 用於區分網路的 NAS-id 等於系統標識；要調整 nas-id，可以執行 `/system/identity/set name=exampleName`。

## 使用 RadSec 代理和 Orion Wifi 的配置指南 {#configuration-guide-using-radsec-proxy-and-orion-wifi}

本指南介紹如何設定 MikroTik 裝置，以便將其與 RadSec 代理和 Orion Wifi 配合使用；主要配置步驟保持不變，也適用於不同的提供商：
本指南假設您已使用 Orion Wifi 憑據配置了 radsecproxy。請確保使用最新的長期支援版或穩定版 RouterOS 發行版。  
  
在無線 LAN 控制器與 Orion Wifi 之間建立安全的 RADIUS 連線非常重要。  
Orion Wifi 使用 RADIUS over TLS（RadSec）來確保 AAA 流量的端到端加密。本指南適用於 RouterOS 接入點在流量透過網際網路傳送之前，將 AAA 流量重定向到 RadSec 代理（radsecproxy）的場景。

1) 配置指向 radsecproxy 的 Radius 用戶端：

![](/img/3db4b81f657ab534.webp)

等效命令列如下：

```
/radius/add address=192.168.88.233 secret=yourSecret service=wireless timeout=1s500ms
```

該 secret 應與 radsecproxy 上配置的 secret 匹配。在本例中，“192.168.88.233” 是執行該代理的虛擬機器。

1) 建立將執行 802.1x 認證的無線安全配置檔案：

![](/img/6a844b5ed2cbd001.webp)

![](/img/d13a1203c4fd8709.webp)

![](/img/ba985a4fbb9fdfd3.webp)

等效命令列如下：

```
/interface/wireless/security-profiles/add authentication-types=wpa2-eap management-protection=allowed mode=dynamic-keys name=dot1x_profile supplicant-identity="" radius-eap-accounting=yes eap-methods=passthrough
```

1) 下一步是配置無線介面並分配已建立的安全配置檔案。按“高階模式”以檢視所有選項：

![](/img/6b80df698a47676c.webp)

等效命令列如下：

```
/interface/wireless/set [ find default-name=wlan1 ] mode=ap-bridge security-profile=dot1x_profile wps-mode=disabled
```

請確保已配置正確的國家/地區配置檔案。在本例中，我們使用“wlan1”，但同一命令也適用於其他介面，或可寫為 `/interface/wireless/set wlan1`。

1) 配置互通設定（hotspot 2.0）：

![](/img/d8b8c002900a5610.webp)

![](/img/9bc913aff00b5c99.png)

![](/img/42cd3e6d600d6811.webp)

等效命令列如下：

```
/interface/wireless/interworking-profile/add domain-names=orion.area120.com ipv4-availability=public name=Orion_MikroTik network-type=public-chargeable operator-names=Orion:eng realms=orion.area120.com:eap-tls roaming-ois=f4f5e8f5f4,baa2D00100,baa2d00000 venue=business-unspecified venue-names=Orion:eng wan-downlink=50 wan-uplink=50 wan-status=up
```

:::warning
請務必為 "wan-downlink" 和 "wan-uplink" 指定某個值；在此場景中，"50" 僅用作佔位值，某些用戶端裝置會用它來判斷是否應加入網路。請根據實際情況設定 “venue”（場所型別）、“venue-names” 和其他屬性。“domain-names” 應為 hotspot 2.0 運營商的域名。
:::

1) 將互通配置檔案分配給介面：

![](/img/9fd765802020f3be.webp)

此步驟也可以透過以下命令完成：

```
/interface/wireless/set wlan1 interworking-profile=Orion_MikroTik
```

如果 radsecproxy 正常工作，則安裝了相應 Hotspot 配置檔案的用戶端應能夠連線。

注意：Orion 用於區分網路的 NAS-id 等於系統標識。要調整 nas-id，可以執行 `/system/identity/set name=exampleName`。

## 故障排除 {#troubleshooting}

要檢查 RADIUS 訊息的狀態，可以使用 radius 選單。  
![](/img/69cd6d8993c7246c.webp)  
或者，透過命令列執行 `/radius/monitor X`，其中 X 是數字 ID。可以使用 `/radius/print` 檢視這些 ID。  
有關更多資訊，可以在 `/system/logging/add topics=radius,debug,packet` 下配置額外日誌。可以在 [`/log`](../../diagnostics-monitoring-and-troubleshooting/log/index.md) 下檢視結果。

要檢視活動無線連線，請檢查無線登錄檔 `/interface/wireless/registration-table/print`：

![](/img/ac8d84eba6b9b178.webp)
