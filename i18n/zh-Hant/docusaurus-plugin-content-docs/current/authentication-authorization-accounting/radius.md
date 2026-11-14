---
sidebar_key: "authentication-authorization-accounting/radius"
sidebar_position: 5
title: "RADIUS"
sidebar_label: "RADIUS"
description: "RADIUS 透過 UDP 或 RadSec 協定連線到 RADIUS 伺服器，為 MikroTik RouterOS 中的 PPP、HotSpot 及其他服務提供集中式認證和計費，並支援可配置的埠、共享金鑰以及針對具體服務的設定。"
tags:
  - 'radius'
  - 'authentication'
  - 'vpn'
source: https://manual.mikrotik.com/docs/authentication-authorization-accounting/radius
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RADIUS（Remote Authentication Dial-In User Service 的縮寫）是一種遠端伺服器，可為各種網路裝置提供認證和計費功能。RADIUS 認證和計費使 ISP 或網路管理員能夠透過一臺伺服器在整個大型網路中管理 PPP 使用者訪問和計費。MikroTik RouterOS 具有 RADIUS 用戶端，可對[路由器的本地](./user.md) [使用者](./user.md)、[HotSpot](./hotspot-captive-portal/index.md)、[PPP](../mobile-networking/ppp.md) 和 ISDN 連線進行認證。從 RADIUS 伺服器收到的屬性會覆蓋預設配置檔案中設定的屬性，但如果未收到某些引數，則會從相應的預設配置檔案中獲取。

僅當在路由器本地資料庫中未找到匹配的使用者訪問記錄時，才會查詢 RADIUS 伺服器資料庫。

如果啟用了 RADIUS 計費，計費資訊還會發送到該服務的預設 RADIUS 伺服器。

## RADIUS 用戶端 {#radius-client}

**子選單：** `/radius`

此子選單允許新增和刪除 RADIUS 用戶端。

:::warning
此列表中已新增項的順序很重要。

:::

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **accounting-backup** (*yes \| no*; Default: **no**) | 配置是否用於備份 RADIUS 伺服器 |
| **accounting-port** (*integer [1..65535]*; Default: **1813**) | 用於計費的 RADIUS 伺服器埠 |
| **address** (*IPv4/IPv6 address*; Default: **0.0.0.0**) | RADIUS 伺服器的 IPv4 或 IPv6 地址。<br/> 接受以下格式：<br/> - <em>ipv4</em> - <em>ipv4</em><code>@</code><em>vrf</em> - <em>ipv6</em> - <em>ipv6</em><code>@</code><em>vrf</em> |
| **authentication-port** (*integer [1..65535]*; Default: **1812**) | 用於認證的 RADIUS 伺服器埠。 |
| **called-id** (*string*; Default: ) | 值取決於 Point-to-Point 協定：PPPoE - 服務名稱，PPTP - 伺服器 IP 地址，L2TP - 伺服器 IP 地址。 |
| **certificate** (*string*; Default: ) | [來自證書儲存的證書](./certificates.md)，用於在啟用 RadSec 時與 RADIUS 伺服器通訊。 |
| **comment** (*string*; 預設值： ) |  |
| **disabled** (*yes \| no*; 預設值：**no**) |  |
| **domain** (*string*; Default: ) | 傳遞給需要域驗證的 RADIUS 伺服器的用戶端 Microsoft Windows 域。 |
| **protocol** (*radsec \| udp*; Default: **udp**) | 指定與 RADIUS 伺服器通訊時要使用的協定。 |
| **radsec-timeout**(*time,* Default: **3300ms**) | 超時時間，超過後應透過 RadSec 協定重新發送請求。 |
| **require-message-auth** (*no \| yes-for-request-resp* Default: **yes-for-request-resp**) | 指定是否需要 Message-Authenticator 屬性。 |
| **realm** (*string*; Default: ) | 顯式宣告的 realm（使用者域），因此使用者無需在使用者名稱中提供正確的 ISP 域名。 |
| **secret** (*string*; Default: ) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於訪問 RADIUS 伺服器的共享金鑰。 |
| **service** (*ppp\|login\|hotspot\|wireless\|dhcp\|ipsec\|dot1x*; Default: ) | 將使用此 RADIUS 伺服器的路由器服務：<ul><li>hotspot - HotSpot 認證服務</li><li>login - 路由器本地使用者認證</li><li>ppp - Point-to-Point 用戶端認證</li><li>wireless - 無線用戶端認證</li><li>dhcp - DHCP 協定用戶端認證（用戶端的 MAC 地址作為 User-Name 傳送）</li><li>ipsec - ipsec 用戶端認證</li><li>dot1x - dot1x 認證</li></ul> |
| **src-address** (*ipv4/ipv6 address*; Default: **0.0.0.0**) | 傳送到 RADIUS 伺服器的封包的源 IP/IPv6 地址 |
| **timeout** (*time*; Default: **1100ms**) | 超時時間，超過後應重新發送請求。 |

:::warning
當 RADIUS 伺服器使用 CHAP、MS-CHAPv1、MS-CHAPv2 對使用者進行認證時，它不使用共享金鑰；該金鑰僅用於認證回覆中，並由路由器（RADIUS 用戶端）進行驗證。因此，如果共享金鑰錯誤，RADIUS 伺服器會接受請求，但路由器不會接受回覆。可透過 “*`/radius/monitor`*” 命令觀察到這一點，每當有人嘗試連線時，“bad-replies” 數值都應增加。

:::

:::danger
如果啟用了 RadSec，請確保您的 RADIUS 伺服器使用 “**radsec**” 作為共享金鑰，否則 RADIUS 伺服器將無法正確解密資料（會出現不可列印字元）。使用 RadSec 時，RouterOS 會強制將共享金鑰設為 “radsec”，無論手動設定的是什麼。有關詳細資訊，請參閱 RFC6614。

:::

:::info
如果使用 RadSec，RouterOS 將覆蓋為使用 TCP 埠 2083
:::

### 示例 {#example}

要設定一個用於 HotSpot 和 PPP 服務並對 RADIUS 伺服器（10.0.0.3）進行認證的 RADIUS 用戶端，需要執行以下操作：

```ros
[admin@MikroTik] > /radius/add service=hotspot,ppp address=10.0.0.3 secret=ex
[admin@MikroTik] > /radius/print
Flags: X - disabled
# SERVICE CALLED-ID DOMAIN ADDRESS SECRET
0 ppp,hotspot 
```

要設定使用 RadSec 的 RADIUS 用戶端，需要執行以下操作：

```ros
[admin@MikroTik] > /radius/add service=hotspot,ppp address=10.0.0.3 secret=radsec protocol=radsec certificate=client.crt
[admin@MikroTik] > /radius/print
Flags: X - disabled
# SERVICE CALLED-ID DOMAIN ADDRESS SECRET
0 ppp,hotspot 10.0.0.3 radsec
```

:::warning
請確保指定的證書受信任，並且兩端的 common-name 驗證都能正常工作。

:::

以下是一個可用於 RADIUS RadSec 配置的證書簡單示例：

```ros
On server:

#CN 应为 RADIUS 服务器 IP
/certificate/add name=radsec_server common-name=10.155.114.91
/certificate/sign radsec_server

#CN 应为 RADIUS 客户端 IP
/certificate/add name=radsec_client1 common-name=10.155.114.92
/certificate/sign radsec_client1
/user-manager/set radsec-certificate=radsec_server

#在服务器上导出证书，以便在客户端上应用它们
/certificate/export-certificate type=pkcs12 export-passphrase=verystrongpassword radsec_client1
/certificate/export-certificate type=pkcs12 radsec_server

On client:

#下载这两个文件并将它们上传到客户端
/certificate/import file-name=cert_export_radsec_client1.p12 passphrase=verystrongpassword
/certificate/import file-name=cert_export_radsec_server.p12
/radius/set <radius_client_id_in_list> certificate=cert_export_radsec_client1.p12_0

#之后，当 RADIUS 客户端尝试连接到服务器时，你应该在 status 字段中看到：status="TLS connected"。
```

要檢視 RADIUS 用戶端統計資訊，需要執行以下操作：

```ros
[admin@MikroTik] > /radius/monitor 0
pending: 0
requests: 10
accepts: 4
rejects: 1
resends: 15
timeouts: 5
bad-replies: 0
last-request-rtt: 0s
```

請確保為所需服務啟用 RADIUS 認證：

```ros
/ppp/aaa/set use-radius=yes
/ip/hotspot/profile/set default use-radius=yes
```

## 從 RADIUS 終止連線 {#connection-terminating-from-radius}

**子選單：** `/radius/incoming`

此功能支援從 RADIUS 伺服器傳送的非請求訊息。非請求訊息擴充套件了 RADIUS 協定命令，允許終止已從 RADIUS 伺服器連線的會話。為此，使用 DM（Disconnect-Messages）。斷開訊息會立即終止使用者會話。

:::warning
RouterOS 不支援 POD（Packet of Disconnect），這是另一種執行與 Disconnect Messages 類似功能的 RADIUS 訪問請求封包

:::

### 屬性 {#properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **accept** (*yes \| no*; 預設：**no**) | 是否接受非請求訊息 |
| **port** (*integer*; 預設：**1700**) | 用於監聽請求的埠號 |
| **vrf** (*VRF name*; 預設值：**main**) | 設定服務監聽傳入連線所在的 VRF |

## 支援的 RADIUS 屬性 {#supported-radius-attributes}

您可以在此處下載 [RADIUS reference dictionary.txt](pathname:///assets/319783010_RADIUS_reference_dictionary.txt)，其中包含 MikroTik 裝置支援的所有 RADIUS 屬性。此檔案專為 FreeRADIUS 設計，但也可供其他 RADIUS 伺服器使用。請注意，它可能與您的 RADIUS 伺服器的預設配置檔案衝突。請修正配置，而不是字典，因為 MikroTik RouterOS 不支援其他屬性。還有 [MikroTik Vendor attributes.txt](pathname:///assets/319783011_MikroTik_Vendor_attributes.txt)，可將其包含在現有字典中，以支援 MikroTik 廠商特定屬性。

下面將介紹屬性以及在 MikroTik 裝置與 RADIUS 通訊期間如何使用這些屬性。

### 定義 {#definitions}

- **PPPs** - PPP、PPTP、PPPoE
- **預設配置** - 預設配置檔案中的設定（適用於 PPPs）或 HotSpot 伺服器設定（適用於 HotSpot）

### Access-Request 封包 {#access-request-packet}

- **Service-Type** - 始終為 “Framed”（僅適用於 PPPs）。
- **Framed-Protocol** - 始終為 “PPP”（僅適用於 PPPs）。
- **NAS-Identifier** - 路由器的 identity 名稱。
- **NAS-IP-Address** - 路由器自身的 IP 地址。
- **NAS-Port** - 此屬性表示正在對使用者進行認證的 NAS 的物理埠號。
- **Acct-Session-Id** - 唯一會話 ID。會話 ID 的前兩個符號表示服務（PPP、Hotspot 等）。下一個符號在每次重啟時遞增。最後一組符號在每次新會話時遞增。這意味著，在同一次啟動中，對於同一 RADIUS 型別服務的 100 萬次重連，您無法獲得相同的 ID。如果您丟失了會話停止訊息，而 RADIUS 伺服器仍保持該會話開啟，但隨後收到另一條會話啟動訊息，那麼它必須意識到停止訊息已丟失，關閉舊會話並啟動新會話。
- **NAS-Port-Type** - Async PPP - “Async”；PPTP 和 L2TP - “Virtual”；PPPoE - “Ethernet”；ISDN - “ISDN Sync”；HotSpot - “Ethernet | Cable | Wireless-802.11”（取決於 `/ip/hotspot/profile` 中 nas-port-type 引數的值）。
- **Calling-Station-Id** - PPPoE 和 HotSpot - 大寫字母表示的用戶端 MAC 地址；PPTP 和 L2TP - 用戶端公網 IP 地址。
- **Called-Station-Id** - PPPoE - 服務名；PPTP 和 L2TP - 伺服器 IP 地址；HotSpot - HotSpot 伺服器名稱。
- **NAS-Port-Id** - Async PPP - 序列埠名稱；PPPoE - 伺服器執行所在的乙太網介面名稱；HotSpot - 物理 HotSpot 介面的名稱（如果已橋接，此處顯示橋接埠名稱）；ISDN、PPTP 和 L2TP 不存在此屬性。
- **Framed-IP-Address** - Universal Client 轉換後 HotSpot 用戶端的 IP 地址。
- **Mikrotik-Host-IP** - Universal Client 轉換前 HotSpot 用戶端的 IP 地址（用戶端的原始 IP 地址）。
- **User-Name** - 用戶端登入名。
- **MS-CHAP-Domain** - 使用者域（如果存在）。
- **Mikrotik-Realm** - 如果在 /radius 選單中設定了它，則它會作為 Mikrotik-Realm 屬性包含在每個 RADIUS 請求中。如果未設定，則傳送與 MS-CHAP-Domain 屬性相同的值（如果缺少 MS-CHAP-Domain，則也不包含 Realm）。
- **WISPr-Location-ID** - 在 HotSpot 伺服器的 radius-location-id 屬性中指定的文字字串。
- **WISPr-Location-Name** - 在 HotSpot 伺服器的 radius-location-name 屬性中指定的文字字串。
- **WISPr-Logoff-URL** - 登出頁面的完整連結（例如，**[](http://10.48.0.1/lv/logout)**）。

取決於認證方法（注意：HotSpot 預設使用 CHAP，如果啟用了未加密密碼，也可能使用 PAP；它不能使用 MSCHAP）：

- **User-Password** - 加密密碼（與 PAP 認證一起使用）。
- **CHAP-Password**、**CHAP-Challenge** - 加密密碼和挑戰（與 CHAP 認證一起使用）。
- **MS-CHAP-Response**, MS-CHAP-Challenge - 加密密碼和挑戰（與 MS-CHAPv1 認證一起使用）。
- **MS-CHAP2-Response**、**MS-CHAP-Challenge** - 加密密碼和挑戰（與 MS-CHAPv2 認證一起使用）。

### Access-Accepts 封包 {#access-accepts-packet}

- **Framed-IP-Address** - 分配給用戶端的 IP 地址。如果該地址屬於 127.0.0.0/8 或 224.0.0.0/3 網路，則使用預設配置檔案中的 IP 池來分配用戶端 IP 地址。如果指定了 Framed-IP-Address，則忽略 Framed-Pool。
- **Framed-IP-Netmask** - 用戶端子網掩碼。PPPs - 如果指定，將透過 Framed-IP-Address 閘道器建立到 Framed-IP-Address 所屬網路的路由；HotSpot - 被 HotSpot 忽略。
- **Framed-Pool** - 用於為用戶端獲取 IP 地址的（路由器上的）IP 池名稱。如果指定了 Framed-IP-Address，則忽略此屬性。
- **Framed-IPv6-Prefix** - 分配給用戶端的 IPv6 字首。
- **Mikrotik-Delegated-IPv6-Pool** - 用於字首委派的 IPv6 池。
- **Delegated-IPv6-Prefix** - IPv6 字首。
- **Delegated-IPv6-Prefix-Pool** - 用於字首委派的 IPv6 字首池。

注意：如果指定了 Framed-IP-Address 或 Framed-Pool，則它會覆蓋預設配置中的 remote-address。

- **Idle-Timeout** - 覆蓋預設配置中的 idle-timeout。
- **Session-Timeout** - 覆蓋預設配置中的 session-timeout。
- **Port-Limit** - 使用同一使用者名稱的最大併發連線數（覆蓋 HotSpot 使用者配置檔案的 shared-users 屬性）。
- **Class** - Cookie。將原樣包含在 Accounting-Request 中。
- **Framed-Route** - 要在伺服器上新增的路由。格式在 RFC 2865（第 5.22 章）中指定。可根據需要指定多次。
- **Filter-Id** - 防火牆過濾鏈名稱。它用於建立動態防火牆規則。防火牆鏈名稱可以帶有 .in 或 .out 字尾，這樣規則只會對傳入或傳出流量安裝。可以提供多個 Filter-id，但只會使用傳入和傳出的最後一個。對於 PPPs - ppp 鏈中的過濾規則，如果封包來自/發往用戶端，則會跳轉到指定鏈（這意味著您應首先建立 ppp 鏈，並建立將實際流量放入此鏈的跳轉規則）。HotSpot 同理，但規則將在 hotspot 鏈中建立。
- **Mikrotik-Mark-Id** - 防火牆 mangle 鏈名稱（僅 HotSpot）。MikroTik RADIUS 用戶端在收到此屬性後，會建立一條動態防火牆 mangle 規則，其中 action=jump chain=hotspot，jump-target 等於該屬性值。Mangle 鏈名稱可以帶有 .in 或 .out 字尾，這樣規則只會對傳入或傳出流量安裝。可以提供多個 Mark-id 屬性，但只會使用傳入和傳出的最後一個。
- **Acct-Interim-Interval** - RADIUS 用戶端的臨時更新。PPP - 如果為 0，則使用 RADIUS 用戶端中指定的值。HotSpot - 僅當 HotSpot 伺服器配置檔案中的 radius-interim-update=received 時才會生效。
- **MS-MPPE-Encryption-Policy** - Require-encryption 屬性（僅 PPPs）。
- **MS-MPPE-Encryption-Types** - Use-encryption 屬性。非零值表示使用加密（僅 PPPs）。
- **Ascend-Data-Rate** - Tx/rx 資料速率限制；如果提供多個屬性，第一個限制 tx 資料速率，第二個限制 rx 資料速率。如果與 Ascend-Xmit-Rate 一起使用，則指定 rx 速率。0 表示不限速。如果存在 Rate-Limit 屬性，則忽略此項。
- **Ascend-Xmit-Rate** - Tx 資料速率限制。它可用於僅指定 tx 限制，而不傳送兩個連續的 Ascend-Data-Rate 屬性（在這種情況下，Ascend-Data-Rate 將指定接收速率）。0 表示不限速。如果存在 Rate-Limit 屬性，則忽略此項。
- **MS-CHAP2-Success** - 如果使用了 MS-CHAPv2，則為認證響應（僅適用於 PPPs）。
- **MS-MPPE-Send-Key, MS-MPPE-Recv-Key** - 僅當使用 MS-CHAPv2 作為認證時，由 RADIUS 伺服器提供的加密 PPP 的加密金鑰（僅適用於 PPPs）。
- **Ascend-Client-Gateway** - 用於 DHCP-pool HotSpot 登入方法的用戶端閘道器（僅 HotSpot）。
- **Mikrotik-Recv-Limit** - 用戶端的總接收限制，以位元組為單位。
- **Mikrotik-Recv-Limit-Gigawords** - 總接收限制的 4G（2^32）位元組部分（位 32..63，其中位 0..31 在 Mikrotik-Recv-Limit 中傳遞）。
- **Mikrotik-Xmit-Limit** - 用戶端的總髮送限制，以位元組為單位。
- **Mikrotik-Xmit-Limit-Gigawords** - 總髮送限制的 4G（2^32）位元組部分（位 32..63，其中位 0..31 在 Mikrotik-Xmit-Limit 中傳遞）。
- **Mikrotik-Wireless-Forward** - 如果此屬性設定為 “0”，則不將用戶端幀轉發回無線基礎設施（僅 Wireless）。
- **Mikrotik-Wireless-Skip-Dot1x** - 如果設定為非零值，則停用特定無線用戶端的 802.1x 認證（僅 Wireless）。
- **Mikrotik-Wireless-Enc-Algo** - WEP 加密演算法：0 - 不加密，1 - 40 位 WEP，2 - 104 位 WEP（僅 Wireless）。
- **Mikrotik-Wireless-Enc-Key** - 用戶端的 WEP 加密金鑰（僅 Wireless）。
- **Mikrotik-Wireless-VLANID** - 用戶端的 VLAN ID（僅 Wireless）。
- **Mikrotik-Wireless-VLANID-type** - 用戶端的 VLAN ID 型別。0 - 802.1q 標籤，1 - 802.1ad 標籤（僅 Wireless）。
- **Mikrotik-Switching-Filter** - 允許在使用 dot1x 伺服器對用戶端進行認證時建立動態交換規則。
- **Mikrotik-Rate-Limit** - 用戶端的資料速率限制。格式為：rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]（從路由器角度而言，因此 “rx” 是用戶端上傳，“tx” 是用戶端下載）。所有速率都應為數字，並可帶有可選的 'k'（1,000s）或 'M'（1,000,000s）。如果未指定 tx-rate，則 rx-rate 也作為 tx-rate。tx-burst-rate、tx-burst-threshold 和 tx-burst-time 同理。如果同時未指定 rx-burst-threshold 和 tx-burst-threshold（但指定了 burst-rate），則使用 rx-rate 和 tx-rate 作為突發閾值。如果同時未指定 rx-burst-time 和 tx-burst-time，則預設使用 1s。Priority 取值為 1..8，其中 1 表示最高優先順序，8 表示最低優先順序。如果未指定 rx-rate-min 和 tx-rate-min，則使用 rx-rate 和 tx-rate 值。rx-rate-min 和 tx-rate-min 的值不能超過 rx-rate 和 tx-rate 的值。
- **Mikrotik-Group** - 本地使用者的路由器本地使用者組名稱（在 `/user/group` 中定義）；HotSpot 使用者的 HotSpot 預設配置檔案；PPP 使用者的 PPP 預設配置檔名稱。
- **Mikrotik-Advertise-URL** - 應向用戶端顯示的廣告頁面 URL。如果指定了此屬性，則會自動啟用廣告（包括透明代理），即使在相應使用者配置檔案中已顯式停用廣告也是如此。RADIUS 伺服器可以傳送多個屬性例項來指定其他 URL，這些 URL 會以輪詢方式選擇。
- **Mikrotik-Advertise-Interval** - 兩個相鄰廣告之間的時間間隔。RADIUS 伺服器可以傳送多個屬性例項來指定其他間隔。所有間隔值都視為一個列表，並在每次成功廣告時逐個取用。如果到達列表末尾，則繼續使用最後一個值。
- **WISPr-Redirection-URL** - 用戶端在成功登入後將重定向到的 URL。
- **WISPr-Bandwidth-Min-Up** - 為用戶端上傳提供的最小資料速率（CIR）。
- **WISPr-Bandwidth-Min-Down** - 為用戶端下載提供的最小資料速率（CIR）。
- **WISPr-Bandwidth-Max-Up** - 為用戶端上傳提供的最大資料速率（MIR）。
- **WISPr-Bandwidth-Max-Down** - 為用戶端下載提供的最大資料速率（MIR）。
- **WISPr-Session-Terminate-Time** - 應斷開使用者的時間；格式為 “YYYY-MM-DDThh:mm:ssTZD”，其中 Y - 年；M - 月；D - 日；T - 分隔符（必須寫在日期和時間之間）；h - 小時（24 小時制）；m - 分鐘；s - 秒；TZD - 時區，採用以下形式之一：“+hh:mm”、“+hhmm”、“-hh:mm”、“-hhmm”。

收到的屬性會覆蓋預設屬性（在預設配置檔案中設定），但如果未從 RADIUS 伺服器收到某個屬性，則使用預設屬性。Rate-Limit 優先於為用戶端指定資料速率的所有其他方式。Ascend 資料速率屬性次之；WISPr 屬性優先順序最低。

以下是一些 Rate-Limit 示例：

- **128k** - rx-rate=128000，tx-rate=128000（無突發）。
- **64k/128M** - rx-rate=64000，tx-rate=128000000。
- **64k 256k** - rx/tx-rate=64000，rx/tx-burst-rate=256000，rx/tx-burst-threshold=64000，rx/tx-burst-time=1s。
- **64k/64k 256k/256k 128k/128k 10/10** - rx/tx-rate=64000，rx/tx-burst-rate=256000，rx/tx-burst-threshold=128000，rx/tx-burst-time=10s。

### Accounting-Request 封包 {#accounting-request-packet}

計費請求攜帶與 Access Request 相同的屬性，另加以下屬性：

- **Acct-Status-Type** - Start、Stop 或 Interim-Update。
- **Acct-Authentic** - 由 RADIUS 或本地授權方認證（僅 PPPs）。
- **Class** - RADIUS 伺服器 cookie，如在 Access-Accept 中收到的那樣。
- **Acct-Delay-Time** - 路由器嘗試傳送此 Accounting-Request 封包的時長。

### Stop 和 Interim-Update Accounting-Request 封包 {#stop-and-interim-update-accounting-request-packet}

除計費開始請求外，以下訊息還將包含以下屬性：

- **Acct-Session-Time** - 連線正常執行時間，以秒為單位。
- **Acct-Input-Octets** - 從用戶端接收的位元組數。
- **Acct-Input-Gigawords** - 從用戶端接收的 4G（2^32）位元組部分（位 32..63，其中位 0..31 在 Acct-Input-Octets 中傳遞）。
- **Acct-Input-Packets** - 從用戶端接收的封包數量。
- **Acct-Output-Octets** - 傳送到用戶端的位元組數。
- **Acct-Output-Gigawords** - 傳送到用戶端的 4G（2^32）位元組部分（位 32..63，其中位 0..31 在 Acct-Output-Octets 中傳遞）。
- **Acct-Output-Packets** - 傳送到用戶端的封包數量。

:::warning
RouterOS 中的 RADIUS 計費訊息從用戶端角度將 output 表示為流量，例如，對於 VPN 使用者 “test”，output 是使用者上傳。

:::

### **Stop Accounting-Request 封包** {#stop-accounting-request-packet}

這些封包除 Interim Update 封包外，還將包含：

- **Acct-Terminate-Cause** - 會話終止原因（參見 RFC 2866 第 5.10 章）
  
  ### **授權變更**

RADIUS 斷開和 Change of Authorization（根據 RFC3576）也受支援。以下屬性可以透過來自 RADIUS 伺服器的 CoA 請求進行更改：

- **Mikrotik-Group**
- **Mikrotik-Recv-Limit**
- **Mikrotik-Xmit-Limit**
- **Mikrotik-Rate-Limit**
- **Ascend-Data-Rate**（僅當不存在 Mikrotik-Rate-Limit 時）
- **Ascend-XMit-Rate**（僅當不存在 Mikrotik-Rate-Limit 時）
- **Mikrotik-Mark-Id**
- **Filter-Id**
- **Mikrotik-Advertise-Url**
- **Mikrotik-Advertise-Interval**
- **Session-Timeout**
- **Idle-Timeout**
- **Port-Limit**

請注意，無法透過這種方式更改 IP 地址、池或路由——要進行此類更改，必須先斷開使用者連線。

## MikroTik 特定 RADIUS 屬性數值 {#mikrotik-specific-radius-attribute-numeric-values}

| 名稱                                   | VendorID | 值 | RFC                           |
| :-- | :-- | :-- | :-- |
| <strong>MIKROTIK_RECV_LIMIT</strong> | 14988 | 1 |  |
| <strong>MIKROTIK_XMIT_LIMIT</strong> | 14988 | 2 |  |
| <strong>MIKROTIK_GROUP</strong> | 14988 | 3 |  |
| <strong>MIKROTIK_WIRELESS_FORWARD</strong> | 14988 | 4 |  |
| <strong>MIKROTIK_WIRELESS_SKIPDOT1X</strong> | 14988 | 5 |  |
| <strong>MIKROTIK_WIRELESS_ENCALGO</strong> | 14988 | 6 |  |
| <strong>MIKROTIK_WIRELESS_ENCKEY</strong> | 14988 | 7 |  |
| <strong>MIKROTIK_RATE_LIMIT</strong> | 14988 | 8 |  |
| <strong>MIKROTIK_REALM</strong> | 14988 | 9 |  |
| <strong>MIKROTIK_HOST_IP</strong> | 14988 | 10 |  |
| <strong>MIKROTIK_MARK_ID</strong> | 14988 | 11 |  |
| <strong>MIKROTIK_ADVERTISE_URL</strong> | 14988 | 12 |  |
| <strong>MIKROTIK_ADVERTISE_INTERVAL</strong> | 14988 | 13 |  |
| <strong>MIKROTIK_RECV_LIMIT_GIGAWORDS</strong> | 14988 | 14 |  |
| <strong>MIKROTIK_XMIT_LIMIT_GIGAWORDS</strong> | 14988 | 15 |  |
| <strong>MIKROTIK_WIRELESS_PSK</strong> | 14988 | 16 |  |
| <strong>MIKROTIK_TOTAL_LIMIT</strong> | 14988 | 17 |  |
| <strong>MIKROTIK_TOTAL_LIMIT_GIGAWORDS</strong> | 14988 | 18 |  |
| <strong>MIKROTIK_ADDRESS_LIST</strong> | 14988 | 19 |  |
| <strong>MIKROTIK_WIRELESS_MPKEY</strong> | 14988 | 20 |  |
| <strong>MIKROTIK_WIRELESS_COMMENT</strong> | 14988 | 21 |  |
| <strong>MIKROTIK_DELEGATED_IPV6_POOL</strong> | 14988 | 22 |  |
| <strong>MIKROTIK_DHCP_OPTION_SET</strong> | 14988 | 23 |  |
| <strong>MIKROTIK_DHCP_OPTION_PARAM_STR1</strong> | 14988 | 24 |  |
| <strong>MIKROTIK_DHCP_OPTION_PARAM_STR2</strong> | 14988 | 25 |  |
| <strong>MIKROTIK_WIRELESS_VLANID</strong> | 14988 | 26 |  |
| <strong>MIKROTIK_WIRELESS_VLANIDTYPE</strong> | 14988 | 27 |  |
| <strong>MIKROTIK_WIRELESS_MINSIGNAL</strong> | 14988 | 28 |  |
| <strong>MIKROTIK_WIRELESS_MAXSIGNAL</strong> | 14988 | 29 |  |
| <strong>Mikrotik-Switching-Filter</strong> | 14988 | 30 |  |

## 所有支援的屬性數值 {#all-supported-attribute-numeric-values}

| 名稱                                   | VendorID | 值 | RFC                           |
|:-- |:-- | --:|:-- |
| **Acct-Authentic**                     |          | 45    | RFC 2866                      |
| **Acct-Delay-Time**                    |          | 41    | RFC 2866                      |
| **Acct-Input-Gigawords**               |          | 52    | RFC 2869                      |
| **Acct-Input-Octets**                  |          | 42    | RFC 2866                      |
| **Acct-Input-Packets**                 |          | 47    | RFC 2866                      |
| **Acct-Interim-Interval**              |          | 85    | RFC 2869                      |
| **Acct-Output-Gigawords**              |          | 53    | RFC 2869                      |
| **Acct-Output-Octets**                 |          | 43    | RFC 2866                      |
| **Acct-Output-Packets**                |          | 48    | RFC 2866                      |
| **Acct-Session-Id**                    |          | 44    | RFC 2866                      |
| **Acct-Session-Time**                  |          | 46    | RFC 2866                      |
| **Acct-Status-Type**                   |          | 40    | RFC 2866                      |
| **Acct-Terminate-Cause**               |          | 49    | RFC 2866                      |
| **Ascend-Client-Gateway**              | 529      | 132   |                               |
| **Ascend-Data-Rate**                   | 529      | 197   |                               |
| **Ascend-Xmit-Rate**                   | 529      | 255   |                               |
| **Called-Station-Id**                  |          | 30    | RFC 2865                      |
| **Calling-Station-Id**                 |          | 31    | RFC 2865                      |
| **CHAP-Challenge**                     |          | 60    | RFC 2866                      |
| **CHAP-Password**                      |          | 3     | RFC 2865                      |
| **Class**                              |          | 25    | RFC 2865                      |
| **Filter-Id**                          |          | 11    | RFC 2865                      |
| **Framed-Compression**                 |          | 13    | RFC 2865                      |
| **Framed-IP-Address**                  |          | 8     | RFC 2865                      |
| **Framed-IP-Netmask**                  |          | 9     | RFC 2865                      |
| **Framed-IPv6-Prefix**                 |          | 97    | RFC 3162                      |
| **Framed-Mtu**                         |          | 12    | RFC 2865                      |
| **Framed-Pool**                        |          | 88    | RFC 2869                      |
| **Framed-Protocol**                    |          | 7     | RFC 2865                      |
| **Framed-Route**                       |          | 22    | RFC 2865                      |
| **Framed-Routing**                     |          | 10    | RFC 2865                      |
| **Idle-Timeout**                       |          | 28    | RFC 2865                      |
| **MS-CHAP-Challenge**                  | 311      | 11    | RFC 2548                      |
| **MS-CHAP-Domain**                     | 311      | 10    | RFC 2548                      |
| **MS-CHAP-Response**                   | 311      | 1     | RFC 2548                      |
| **MS-CHAP2-Response**                  | 311      | 25    | RFC 2548                      |
| **MS-CHAP2-Success**                   | 311      | 26    | RFC 2548                      |
| **MS-MPPE-Encryption-Policy**          | 311      | 7     | RFC 2548                      |
| **MS-MPPE-Encryption-Types**           | 311      | 8     | RFC 2548                      |
| **MS-MPPE-Recv-Key**                   | 311      | 17    | RFC 2548                      |
| **MS-MPPE-Send-Key**                   | 311      | 16    | RFC 2548                      |
| **NAS-Identifier**                     |          | 32    | RFC 2865                      |
| **NAS-Port**                           |          | 5     | RFC 2865                      |
| **NAS-IP-Address**                     |          | 4     | RFC 2865                      |
| **NAS-Port-Id**                        |          | 87    | RFC 2869                      |
| **NAS-Port-Type**                      |          | 61    | RFC 2865                      |
| **Port-Limit**                         |          | 62    | RFC 2865                      |
| **Redback-Agent-Remote-Id**            | 2352     | 96    |                               |
| **Redback-Agent-Circuit-Id**           | 2352     | 97    |                               |
| **Service-Type**                       |          | 6     | RFC 2865                      |
| **Session-Timeout**                    |          | 27    | RFC 2865                      |
| **User-Name**                          |          | 1     | RFC 2865                      |
| **User-Password**                      |          | 2     | RFC 2865                      |
| **WISPr-Bandwidth-Max-Down**           | 14122    | 8     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Bandwidth-Max-Up**             | 14122    | 7     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Bandwidth-Min-Down**           | 14122    | 6     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Bandwidth-Min-Up**             | 14122    | 5     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Location-Id**                  | 14122    | 1     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Location-Name**                | 14122    | 2     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Logoff-URL**                   | 14122    | 3     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Redirection-URL**              | 14122    | 4     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Session-Terminate-Time**       | 14122    | 9     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Session-Terminate-End-Of-Day** | 14122    | 10    | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Billing-Class-Of-Service**     | 14122    | 11    | [wi-fi.org](https://www.wi-fi.org/) |
|  |  |  |  |
