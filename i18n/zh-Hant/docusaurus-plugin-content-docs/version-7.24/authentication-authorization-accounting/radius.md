---
title: "RADIUS"
description: "RADIUS 透過 UDP 或 RadSec 協定連線至 RADIUS 伺服器，為 MikroTik RouterOS 中的 PPP、HotSpot 與其他服務提供集中式驗證與計費，並可設定埠、共用金鑰與各服務專屬設定。"
tags:
  - 'radius'
  - 'authentication'
  - 'vpn'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/radius
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

RADIUS 是 Remote Authentication Dial-In User Service 的簡稱，是一種遠端伺服器，可為各種網路裝置提供驗證與計費功能。RADIUS 驗證與計費可讓 ISP 或網路管理員從單一伺服器管理整個大型網路中的 PPP 使用者存取與計費。MikroTik RouterOS 具有 RADIUS 用戶端，可驗證 [路由器本機](/docs/authentication-authorization-accounting/user) [使用者](/docs/authentication-authorization-accounting/user)、[HotSpot](/docs/authentication-authorization-accounting/hotspot-captive-portal)、[PPP](/docs/mobile-networking/ppp) 與 ISDN 連線。從 RADIUS 伺服器收到的屬性會覆寫預設設定檔中設定的屬性，但若未收到某些參數，則會從對應的預設設定檔取得。

只有在路由器本機資料庫中找不到相符的使用者存取記錄時，才會查詢 RADIUS 伺服器資料庫。

若啟用 RADIUS 計費，計費資訊也會傳送至該服務的預設 RADIUS 伺服器。

## RADIUS 用戶端 {#radius-client}

**子選單：** `/radius`

此子選單可新增與移除 RADIUS 用戶端。

:::warning
此清單中新增項目的順序很重要。
:::

### 屬性 {#properties}

| Property | Description |
| :-- | :-- |
| **accounting-backup** (*yes \| no*; Default: **no**) | 此設定是否用於備份 RADIUS 伺服器 |
| **accounting-port** (*integer [1..65535]*; Default: **1813**) | 用於計帳的 RADIUS 伺服器埠 |
| **address** (*IPv4/IPv6 address*; Default: **0.0.0.0**) | RADIUS 伺服器的 IPv4 或 IPv6 位址。<br/> 接受下列格式：<br/> - <em>ipv4</em> - <em>ipv4</em><code>@</code><em>vrf</em> - <em>ipv6</em> - <em>ipv6</em><code>@</code><em>vrf</em> |
| **authentication-port** (*integer [1..65535]*; Default: **1812**) | 用於驗證的 RADIUS 伺服器埠。 |
| **called-id** (*string*; Default: ) | 值取決於點對點通訊協定：PPPoE 為服務名稱，PPTP 為伺服器 IP 位址，L2TP 為伺服器 IP 位址。 |
| **certificate** (*string*; Default: ) | 啟用 RadSec 時，用於與 RADIUS Server 通訊的憑證檔案。 |
| **comment** (*string*; Default: ) |  |
| **disabled** (*yes \| no*; Default: **no**) |  |
| **domain** (*string*; Default: ) | 傳遞給需要網域驗證的 RADIUS 伺服器的用戶端 Microsoft Windows 網域。 |
| **protocol** (*radsec \| udp*; Default: **udp**) | 指定與 RADIUS Server 通訊時使用的通訊協定。 |
| **radsec-timeout**(*time,* Default: **3300ms**) | 逾時後，要求應透過 RadSec 通訊協定重新傳送。 |
| **require-message-auth** (*no \| yes-for-request-resp* Default: **yes-for-request-resp**) | 指定是否需要 Message-Authenticator 屬性。 |
| **realm** (*string*; Default: ) | 明確指定 realm（使用者網域），讓使用者不必在使用者名稱中提供正確的 ISP 網域名稱。 |
| **secret** (*string*; Default: ) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 用於存取 RADIUS 伺服器的共用金鑰。 |
| **service** (*ppp\|login\|hotspot\|wireless\|dhcp\|ipsec\|dot1x*; Default: ) | 將使用此 RADIUS 伺服器的路由器服務：<ul><li>hotspot - HotSpot 驗證服務</li><li>login - 路由器本機使用者驗證</li><li>ppp - 點對點用戶端驗證</li><li>wireless - 無線用戶端驗證</li><li>dhcp - DHCP 通訊協定用戶端驗證（用戶端的 MAC 位址會以 User-Name 傳送）</li><li>ipsec - ipsec 用戶端驗證</li><li>dot1x - dot1x 驗證</li></ul> |
| **src-address** (*ipv4/ipv6 address*; Default: **0.0.0.0**) | 傳送至 RADIUS 伺服器的封包來源 IP/IPv6 位址 |
| **timeout** (*time*; Default: **1100ms**) | 逾時後，要求應重新傳送。 |

:::warning
當 RADIUS 伺服器使用 CHAP、MS-CHAPv1、MS-CHAPv2 驗證使用者時，不會使用共用金鑰；金鑰僅用於驗證回覆，而路由器（RADIUS 用戶端）會驗證該回覆。因此，如果共用金鑰錯誤，RADIUS 伺服器會接受要求，但路由器不會接受回覆。你可以使用 "*`/radius/monitor`*" 指令查看，每當有人嘗試連線時，"bad-replies" 數字應該會增加。
:::

:::danger
如果已啟用 RadSec，請確認你的 RADIUS Server 使用 "**radsec**" 作為共用金鑰，否則 RADIUS Server 將無法正確解密資料（不可列印字元）。使用 RadSec 時，RouterOS 會強制共用金鑰為 "radsec"，不論手動設定為何。如需詳細資訊，請參閱 RFC6614。
:::

:::info
如果使用 RadSec，RouterOS 會覆蓋為使用 TCP 埠 2083
:::

### 範例 {#example}

若要設定用於 HotSpot 與 PPP 服務的 RADIUS Client，並向 RADIUS Server（10.0.0.3）進行驗證，請執行下列操作：

```ros
[admin@MikroTik] > /radius/add service=hotspot,ppp address=10.0.0.3 secret=ex
[admin@MikroTik] > /radius/print
Flags: X - disabled
# SERVICE CALLED-ID DOMAIN ADDRESS SECRET
0 ppp,hotspot 
```

若要設定使用 RadSec 的 RADIUS Client，請執行下列操作：

```ros
[admin@MikroTik] > /radius/add service=hotspot,ppp address=10.0.0.3 secret=radsec protocol=radsec certificate=client.crt
[admin@MikroTik] > /radius/print
Flags: X - disabled
# SERVICE CALLED-ID DOMAIN ADDRESS SECRET
0 ppp,hotspot 10.0.0.3 radsec
```

:::warning
請確認指定的憑證受信任，且兩端的 common-name 驗證都能正常運作。
:::

以下是可用於 RADIUS RadSec 設定的簡單憑證範例：

```ros
On server:

#CN should be RADIUS server IP
/certificate/add name=radsec_server common-name=10.155.114.91
/certificate/sign radsec_server

#CN should be RADIUS client IP
/certificate/add name=radsec_client1 common-name=10.155.114.92
/certificate/sign radsec_client1
/user-manager/set radsec-certificate=radsec_server

#Export certificates on the server in order to apply them on client
/certificate/export-certificate type=pkcs12 export-passphrase=verystrongpassword radsec_client1
/certificate/export-certificate type=pkcs12 radsec_server

On client:

#Download both files and upload them to the client
/certificate/import file-name=cert_export_radsec_client1.p12 passphrase=verystrongpassword
/certificate/import file-name=cert_export_radsec_server.p12
/radius/set <radius_client_id_in_list> certificate=cert_export_radsec_client1.p12_0

#After that when RADIUS client tries to connect to the server you should see on status fileld: status="TLS connected".
```

若要檢視 RADIUS Client 統計資料，請執行下列操作：

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

請確認已為所需服務啟用 RADIUS 驗證：

```ros
/ppp/aaa/set use-radius=yes
/ip/hotspot/profile/set default use-radius=yes
```

## 由 RADIUS 終止連線 {#connection-terminating-from-radius}

**子選單：** `/radius/incoming`

此功能支援由 RADIUS 伺服器傳送的非請求訊息。非請求訊息擴充了 RADIUS 協定命令，可讓 RADIUS 伺服器終止已連線的工作階段。為此會使用 DM（Disconnect-Messages）。Disconnect 訊息會讓使用者工作階段立即終止。

:::warning
RouterOS 不支援 POD（Packet of Disconnect），這是另一種執行類似 Disconnect Messages 功能的 RADIUS access request 封包
:::

### 屬性 {#properties-1}

| Property | Description |
| :-- | :-- |
| **accept** (*yes \| no*; Default: **no**) | 是否接受未請求的訊息 |
| **port** (*integer*; Default: **1700**) | 用來監聽要求的埠號 |
| **vrf** (*VRF name*; default value: **main**) | 設定服務監聽傳入連線的 VRF |

## 支援的 RADIUS 屬性 {#supported-radius-attributes}

您可以在此下載 [RADIUS reference dictionary.txt](pathname:///assets/319783010_RADIUS_reference_dictionary.txt)，其中包含 MikroTik 設備支援的所有 RADIUS 屬性。此檔案是為 FreeRADIUS 設計，但其他 RADIUS 伺服器也可能使用。請注意，它可能會與 RADIUS 伺服器的預設設定檔衝突。請修正設定，而不要修改 dictionary，因為 MikroTik RouterOS 不支援其他屬性。另有 [MikroTik Vendor attributes.txt](pathname:///assets/319783011_MikroTik_Vendor_attributes.txt)，可包含在現有 dictionary 中，以支援 MikroTik 廠商專屬屬性。

以下說明屬性，以及 MikroTik 設備與 RADIUS 通訊時如何使用這些屬性。

### Definitions

- **PPPs** - PPP、PPTP、PPPoE
- **default configuration** - 預設設定檔中的設定（適用於 PPP）或 HotSpot 伺服器設定（適用於 HotSpot）

### Access-Request 封包 {#access-request-packet}

- **Service-Type** - 一律為「Framed」（僅適用於 PPP）。
- **Framed-Protocol** - 一律為「PPP」（僅適用於 PPP）。
- **NAS-Identifier** - 路由器的識別名稱。
- **NAS-IP-Address** - 路由器本身的 IP 位址。
- **NAS-Port** - 此屬性指出正在驗證使用者的 NAS 實體埠號。
- **Acct-Session-Id** - 唯一工作階段 ID。工作階段 ID 的前兩個字元代表服務（PPP、Hotspot 等）。下一個字元會在每次重新開機時遞增。最後一組字元會在每個新工作階段時遞增。這表示，在同一開機期間，針對相同 RADIUS 類型服務，即使重新連線 100 萬次，也無法取得相同的 ID。如果你遺失工作階段停止訊息，而 RADIUS 伺服器仍保持工作階段開啟，但隨後收到另一則工作階段開始訊息，則它必須知道停止訊息已遺失，並關閉舊工作階段、啟動新工作階段。
- **NAS-Port-Type** - Async PPP -「Async」；PPTP 與 L2TP -「Virtual」；PPPoE -「Ethernet」；ISDN -「ISDN Sync」；HotSpot -「Ethernet | Cable | Wireless-802.11」（依 `/ip/hotspot/profile` 中 nas-port-type 參數的值而定）。
- **Calling-Station-Id** - PPPoE 與 HotSpot - 大寫的用戶端 MAC 位址；PPTP 與 L2TP - 用戶端公用 IP 位址。
- **Called-Station-Id** - PPPoE - 服務名稱；PPTP 與 L2TP - 伺服器 IP 位址；HotSpot - HotSpot 伺服器名稱。
- **NAS-Port-Id** - Async PPP - 序列埠名稱；PPPoE - 執行伺服器的乙太網路介面名稱；HotSpot - 實體 HotSpot 介面名稱（若已橋接，此處會顯示橋接埠名稱）；ISDN、PPTP 與 L2TP 則不存在。
- **Framed-IP-Address** - Universal Client 轉換後的 HotSpot 用戶端 IP 位址。
- **Mikrotik-Host-IP** - Universal Client 轉換前的 HotSpot 用戶端 IP 位址（用戶端原始 IP 位址）。
- **User-Name** - 用戶端登入名稱。
- **MS-CHAP-Domain** - 使用者網域（若存在）。
- **Mikrotik-Realm** - 若已在 /radius 選單中設定，則會在每個 RADIUS 要求中包含為 Mikrotik-Realm 屬性。若未設定，則會傳送與 MS-CHAP-Domain 屬性相同的值（若缺少 MS-CHAP-Domain，也不會包含 Realm）。
- **WISPr-Location-ID** - HotSpot 伺服器的 radius-location-id 屬性中指定的文字字串。
- **WISPr-Location-Name** - HotSpot 伺服器的 radius-location-name 屬性中指定的文字字串。
- **WISPr-Logoff-URL** - 登出頁面的完整連結（例如，**[](http://10.48.0.1/lv/logout)**）。

視驗證方法而定（注意：HotSpot 預設使用 CHAP，若啟用未加密密碼，也可能使用 PAP，但無法使用 MSCHAP）：

- **User-Password** - 加密密碼（搭配 PAP 驗證使用）。
- **CHAP-Password**, **CHAP-Challenge** - 加密密碼與 challenge（搭配 CHAP 驗證使用）。
- **MS-CHAP-Response**, MS-CHAP-Challenge - 加密密碼與 challenge（搭配 MS-CHAPv1 驗證使用）。
- **MS-CHAP2-Response**, **MS-CHAP-Challenge** - 加密密碼與 challenge（搭配 MS-CHAPv2 驗證使用）。

### Access-Accepts 封包 {#access-accepts-packet}

- **Framed-IP-Address** - 指派給用戶端的 IP 位址。若該位址屬於 127.0.0.0/8 或 224.0.0.0/3 網路，則會使用預設設定檔中的 IP pool 配置用戶端 IP 位址。若指定 Framed-IP-Address，則會忽略 Framed-Pool。
- **Framed-IP-Netmask** - 用戶端網路遮罩。PPP：若指定，將會建立一條通往 Framed-IP-Address 所屬網路的路由，並以 Framed-IP-Address 作為閘道；HotSpot：由 HotSpot 忽略。
- **Framed-Pool** - 路由器上的 IP pool 名稱，用於取得用戶端的 IP 位址。若指定 Framed-IP-Address，則會忽略此屬性。
- **Framed-IPv6-Prefix** - 指派給用戶端的 IPv6 前綴。
- **Mikrotik-Delegated-IPv6-Pool** - 用於 Prefix Delegation 的 IPv6 pool。
- **Delegated-IPv6-Prefix** - IPv6 前綴。
- **Delegated-IPv6-Prefix-Pool** - 用於 Prefix Delegation 的 IPv6 前綴 pool。

注意：若指定 Framed-IP-Address 或 Framed-Pool，將會覆蓋預設設定中的 remote-address。

- **Idle-Timeout** - 覆蓋預設設定中的 idle-timeout。
- **Session-Timeout** - 覆蓋預設設定中的 session-timeout。
- **Port-Limit** - 使用相同使用者名稱同時連線的最大數目（覆蓋 HotSpot 使用者設定檔的 shared-users 屬性）。
- **Class** - Cookie。將會原樣包含在 Accounting-Request 中。
- **Framed-Route** - 要在伺服器上新增的路由。格式請參閱 RFC 2865（Ch. 5.22）。可依需要指定多次。
- **Filter-Id** - 防火牆 filter chain 名稱。用於建立動態防火牆規則。防火牆 chain 名稱可有後綴 .in 或 .out，只會針對傳入或傳出流量安裝規則。可提供多個 Filter-id，但只會使用最後一個傳入與最後一個傳出的規則。對 PPP 而言，filter 規則位於 ppp chain 中，當封包進出用戶端時會跳至指定的 chain（這表示你應先建立 ppp chain，並建立 jump 規則，將實際流量導向此 chain）。HotSpot 亦適用相同做法，但規則會建立在 hotspot chain 中。
- **Mikrotik-Mark-Id** - 防火牆 mangle chain 名稱（僅 HotSpot）。MikroTik RADIUS 用戶端收到此屬性後，會建立一條動態防火牆 mangle 規則，動作為 action=jump、chain=hotspot，且 jump-target 等於此屬性值。Mangle chain 名稱可有後綴 .in 或 .out，只會針對傳入或傳出流量安裝規則。可提供多個 Mark-id 屬性，但只會使用最後一個傳入與最後一個傳出的規則。
- **Acct-Interim-Interval** - RADIUS 用戶端的 interim-update。PPP：若為 0，則使用 RADIUS 用戶端中指定的值。HotSpot：只有在 HotSpot server profile 中設定 radius-interim-update=received 時才會生效。
- **MS-MPPE-Encryption-Policy** - Require-encryption 屬性（僅 PPP）。
- **MS-MPPE-Encryption-Types** - Use-encryption 屬性。非零值表示使用加密（僅 PPP）。
- **Ascend-Data-Rate** - Tx/rx 資料速率限制。若提供多個屬性，第一個限制 tx 資料速率，第二個限制 rx 資料速率。若與 Ascend-Xmit-Rate 一起使用，則指定 rx 速率。0 表示不限速。若存在 Rate-Limit 屬性，則忽略此屬性。
- **Ascend-Xmit-Rate** - Tx 資料速率限制。可用於只指定 tx 限制，而不必傳送兩個連續的 Ascend-Data-Rate 屬性（在這種情況下，Ascend-Data-Rate 會指定接收速率）。0 表示不限速。若存在 Rate-Limit 屬性，則忽略此屬性。
- **MS-CHAP2-Success** - 使用 MS-CHAPv2 時的驗證回應（僅 PPP）。
- **MS-MPPE-Send-Key, MS-MPPE-Recv-Key** - 加密 PPP 的加密金鑰，只有在 MS-CHAPv2 用作驗證時才會由 RADIUS 伺服器提供（僅 PPP）。
- **Ascend-Client-Gateway** - DHCP-pool HotSpot 登入方式的用戶端閘道（僅 HotSpot）。
- **Mikrotik-Recv-Limit** - 用戶端的總接收限制，單位為位元組。
- **Mikrotik-Recv-Limit-Gigawords** - 總接收限制的 4G（2^32）位元組（位元 32..63，位元 0..31 由 Mikrotik-Recv-Limit 傳遞）。
- **Mikrotik-Xmit-Limit** - 用戶端的總傳送限制，單位為位元組。
- **Mikrotik-Xmit-Limit-Gigawords** - 總傳送限制的 4G（2^32）位元組（位元 32..63，位元 0..31 由 Mikrotik-Xmit-Limit 傳遞）。
- **Mikrotik-Wireless-Forward** - 若此屬性設為「0」，則不會將用戶端的訊框轉送回無線基礎架構（僅 Wireless）。
- **Mikrotik-Wireless-Skip-Dot1x** - 若設為非零值，則停用特定無線用戶端的 802.1x 驗證（僅 Wireless）。
- **Mikrotik-Wireless-Enc-Algo** - WEP 加密演算法：0 表示不加密，1 表示 40-bit WEP，2 表示 104-bit WEP（僅 Wireless）。
- **Mikrotik-Wireless-Enc-Key** - 用戶端的 WEP 加密金鑰（僅 Wireless）。
- **Mikrotik-Wireless-VLANID** - 用戶端的 VLAN ID（僅 Wireless）。
- **Mikrotik-Wireless-VLANID-type** - 用戶端的 VLAN ID 類型。0 表示 802.1q tag，1 表示 802.1ad tag（僅 Wireless）。
- **Mikrotik-Switching-Filter** - 使用 dot1x 伺服器驗證用戶端時，允許建立動態交換器規則。
- **Mikrotik-Rate-Limit** - 用戶端的資料速率限制。格式為：rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]，以路由器的角度來看（因此「rx」是用戶端上傳，「tx」是用戶端下載）。所有速率應為數字，並可搭配選用的 'k'（1,000 倍）或 'M'（1,000,000 倍）。若未指定 tx-rate，則 rx-rate 也會作為 tx-rate。tx-burst-rate、tx-burst-threshold 與 tx-burst-time 亦同。若 rx-burst-threshold 與 tx-burst-threshold 皆未指定（但指定了 burst-rate），則會使用 rx-rate 與 tx-rate 作為 burst threshold。若 rx-burst-time 與 tx-burst-time 皆未指定，則預設使用 1s。Priority 的值為 1..8，其中 1 表示最高優先權，8 表示最低。若未指定 rx-rate-min 與 tx-rate-min，則使用 rx-rate 與 tx-rate 的值。rx-rate-min 與 tx-rate-min 的值不得超過 rx-rate 與 tx-rate 的值。
- **Mikrotik-Group** - 本機使用者的路由器本機使用者群組名稱（定義於 `/user/group`）；HotSpot 使用者的 HotSpot 預設設定檔；PPP 使用者的 PPP 預設設定檔名稱。
- **Mikrotik-Advertise-URL** - 應向用戶端顯示廣告的頁面 URL。若指定此屬性，廣告會自動啟用，包括透明代理，即使已在對應的使用者設定檔中明確停用。RADIUS 伺服器可傳送多個屬性執行個體，以指定其他 URL，並以 round robin 方式選擇。
- **Mikrotik-Advertise-Interval** - 兩個相鄰廣告之間的時間間隔。RADIUS 伺服器可傳送多個屬性執行個體，以指定其他間隔。所有間隔值會視為一份清單，並在每次成功播放廣告時逐一取值。若已到達清單結尾，則繼續使用最後一個值。
- **WISPr-Redirection-URL** - 用戶端成功登入後將被重新導向的 URL。
- **WISPr-Bandwidth-Min-Up** - 提供給用戶端上傳的最小資料速率（CIR）。
- **WISPr-Bandwidth-Min-Down** - 提供給用戶端下載的最小資料速率（CIR）。
- **WISPr-Bandwidth-Max-Up** - 提供給用戶端上傳的最大資料速率（MIR）。
- **WISPr-Bandwidth-Max-Down** - 提供給用戶端下載的最大資料速率（MIR）。
- **WISPr-Session-Terminate-Time** - 使用者應被中斷連線的時間；格式為「YYYY-MM-DDThh:mm:ssTZD」，其中 Y 表示年；M 表示月；D 表示日；T 表示分隔符號（必須寫在日期與時間之間）；h 表示小時（24 小時制）；m 表示分鐘；s 表示秒；TZD 表示時區，格式為下列其中之一：「+hh:mm」、「+hhmm」、「-hh:mm」、「-hhmm」。

接收到的屬性會覆蓋預設屬性（在預設設定檔中設定），但若未從 RADIUS 伺服器收到某個屬性，則會使用預設值。Rate-Limit 優先於所有其他指定用戶端資料速率的方式。Ascend 資料速率屬性的優先順序次之；WISPr 屬性的優先順序最低。

以下是一些 Rate-Limit 範例：

- **128k** - rx-rate=128000, tx-rate=128000（無 burst）。
- **64k/128M** - rx-rate=64000, tx-rate=128000000。
- **64k 256k** - rx/tx-rate=64000, rx/tx-burst-rate=256000, rx/tx-burst-threshold=64000, rx/tx-burst-time=1s。
- **64k/64k 256k/256k 128k/128k 10/10** - rx/tx-rate=64000, rx/tx-burst-rate=256000, rx/tx-burst-threshold=128000, rx/tx-burst-time=10s。

### Accounting-Request 封包 {#accounting-request-packet}

Accounting 請求攜帶與 Access Request 相同的屬性，另外還包含下列屬性：

- **Acct-Status-Type** - Start、Stop 或 Interim-Update。
- **Acct-Authentic** - 由 RADIUS 或本機授權驗證（僅限 PPP）。
- **Class** - RADIUS 伺服器 cookie，如同在 Access-Accept 中收到的一樣。
- **Acct-Delay-Time** - 路由器嘗試傳送此 Accounting-Request 封包的時間長度。

### Stop 與 Interim-Update Accounting-Request 封包 {#stop-and-interim-update-accounting-request-packet}

除了 accounting start 請求之外，下列訊息還會包含下列屬性：

- **Acct-Session-Time** - 連線正常運作的秒數。
- **Acct-Input-Octets** - 從用戶端接收的位元組數。
- **Acct-Input-Gigawords** - 從用戶端接收的 4G（2^32）位元組（位元 32..63，位元 0..31 會在 Acct-Input-Octets 中傳送）。
- **Acct-Input-Packets** - 從用戶端接收的封包數。
- **Acct-Output-Octets** - 傳送給用戶端的位元組數。
- **Acct-Output-Gigawords** - 傳送給用戶端的 4G（2^32）位元組（位元 32..63，位元 0..31 會在 Acct-Output-Octets 中傳送）。
- **Acct-Output-Packets** - 傳送給用戶端的封包數。

:::warning
RouterOS 中的 RADIUS accounting 訊息是以用戶端角度呈現 output，例如，對 VPN 使用者「test」而言，output 就是使用者上傳流量。
:::

### **Stop Accounting-Request 封包** {#stop-accounting-request-packet}

除了 Interim Update 封包之外，這些封包還會包含：

- **Acct-Terminate-Cause** - 工作階段終止原因（請參閱 RFC 2866 第 5.10 節）
  
  ### **變更授權**

亦支援 RADIUS disconnect 與 Change of Authorization（依據 RFC3576）。RADIUS 伺服器傳送的 CoA 要求可以變更下列屬性：

- **Mikrotik-Group**
- **Mikrotik-Recv-Limit**
- **Mikrotik-Xmit-Limit**
- **Mikrotik-Rate-Limit**
- **Ascend-Data-Rate**（僅在沒有 Mikrotik-Rate-Limit 時）
- **Ascend-XMit-Rate**（僅在沒有 Mikrotik-Rate-Limit 時）
- **Mikrotik-Mark-Id**
- **Filter-Id**
- **Mikrotik-Advertise-Url**
- **Mikrotik-Advertise-Interval**
- **Session-Timeout**
- **Idle-Timeout**
- **Port-Limit**

請注意，無法以這種方式變更 IP 位址、集區或路由；若要進行這類變更，必須先中斷使用者連線。

## MikroTik 特定 RADIUS 屬性數值 {#mikrotik-specific-radius-attribute-numeric-values}

| 名稱 | VendorID | 值 | RFC |
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

| Name                                   | VendorID | Value | RFC                           |
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
|                      |          |       |                               |
