---
title: "Dot1X"
description: "本頁說明 MikroTik RouterOS 的 Dot1X 實作，涵蓋使用 TLS、TTLS 與 PEAP 等 EAP 方法，進行 IEEE 802.1X 連接埠型網路存取控制的用戶端與伺服器設定。"
tags:
  - 'dot1x'
  - 'radius'
  - 'authentication'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/dot1x
captured_at: '2026-11-28T10:19:39.818Z'
pagination_next: "authentication-authorization-accounting/hotspot-captive-portal"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

Dot1X 是 RouterOS 中 IEEE 802.1X 標準的實作。主要目的是使用 EAP over LAN（也稱為 EAPOL）提供以埠為基礎的網路存取控制。802.1X 由 supplicant（用戶端）、authenticator（伺服器）與 authentication server（RADIUS 伺服器）組成。RouterOS 支援 authenticator 與 supplicant 兩端，安裝 [User Manager](/docs/authentication-authorization-accounting/user-manager) 套件時也支援 authentication server。supplicant 支援的 EAP 方法包括 EAP-TLS、EAP-TTLS、EAP-MSCHAPv2 與 PEAPv0/EAP-MSCHAPv2。

:::warning
此功能不支援 SMIPS 設備（hAP lite、hAP lite TC 與 hAP mini）。
:::

## 用戶端 {#client}

Supplicant 設定。

**子選單：** `/interface/dot1x/client`

| Property | Description |
| :-- | :-- |
| **anon-identity** (*string*; Default: ) | 外層 EAP 驗證的識別資訊。僅搭配 `eap-ttls` 與 `eap-peap` 方法使用。若未設定，外層 EAP 驗證會使用 `identity` 參數的值。 |
| **client-certificate** (*string*; Default: ) | 列於 [System/Certificates](/docs/authentication-authorization-accounting/certificates) 中的憑證名稱。使用 `eap-tls` 方法時必要。 |
| **comment** (*string*; Default: ) | 此項目的簡短描述。 |
| **disabled** (*yes \| no*; Default: **no**) | 用戶端是否啟用。 |
| **eap-methods** (*eap-tls \| eap-ttls \| eap-peap \| eap-mschapv2*; Default: ) | 用於驗證的 EAP 方法有序清單。 |
| **identity** (*string*; Default: ) | 用於 EAP 驗證的 supplicant 識別資訊。 |
| **interface** (*string*; Default: ) | 用戶端執行所在的介面名稱。 |
| **password** (*string*; Default: ) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | supplicant 的明文密碼。 |

### 唯讀屬性 {#read-only-properties}

| Property | Description |
| :-- | :-- |
| **status** (*authenticated \| authenticating \| disabled*) | 可能的狀態：<ul><li>authenticated - 用戶端已成功完成驗證。</li><li>authenticating - 已連線至伺服器，驗證程序正在進行。</li><li>disabled - 用戶端已停用。</li><li>error - 發生內部錯誤。</li><li>interface is down - 上層介面未執行。</li><li>rejected - 伺服器拒絕驗證。</li></ul> |

## Server

---

RouterOS dot1x 伺服器會作為驗證器。啟用 dot1x 伺服器的介面會封鎖所有流量，但用於驗證的 EAPOL 封包除外。用戶端成功驗證後，該介面會接受該埠上收到的所有流量。如果介面連接到具有多部主機的共享媒介，只要至少有一個用戶端成功驗證，就會接受所有主機的流量。不過，可以[設定動態交換器規則](/docs/authentication-authorization-accounting/dot1x#dynamic-switch-rule-configuration)，只接受已驗證使用者的來源 MAC 位址，並捨棄所有其他來源 MAC 位址。若驗證失敗，可以使用專用的埠 VLAN ID 接受流量。

:::warning
在 bridge 埠上建立 dot1x 伺服器時，bridge 應執行 (R/M)STP，否則來自用戶端的 EAP 封包將無法被正確接受。bridge 介面預設會以 `protocol-mode=rstp` 建立。如果 bridge 埠不應傳送任何 BPDU，或應忽略任何收到的 BPDU，請在 bridge 埠上使用 `edge=yes` 設定。
:::

**子選單：** `/interface/dot1x/server`

| 屬性 | 說明 |
| :-- | :-- |
| **accounting** (*yes \| no*；預設：**yes**) | 是否將 RADIUS 計費要求傳送至驗證伺服器。 |
| **auth-timeout** (*time*；預設：**1m**) | EAP 驗證可用的總時間。 |
| **auth-types** (*dot1x \| mac-auth*；預設：**dot1x**) | 伺服器介面上使用的驗證類型。同時選取兩個選項時，伺服器會優先使用 `dot1x` 驗證類型，且只有在 3 個 `retrans-timeout` 週期後，驗證類型才會回退到 `mac-auth`。為了讓 `mac-auth` 驗證類型運作，伺服器介面應收到至少一個包含用戶端設備來源 MAC 位址的訊框。 |
| **comment** (*string*；預設：) | 項目的簡短說明。 |
| **disabled** (*yes \| no*；預設：**no**) | 伺服器設定是否啟用。 |
| **guest-vlan-id** (*integer: 1..4094*；預設：**!guest-vlan-id**) | 當終端設備不支援 `dot1x` 驗證且未設定 `mac-auth` 回退時所指派的 VLAN。此設定會在 3 個 `retrans-timeout` 週期後套用。一旦建立已啟用 dot1x 的用戶端並成功重新驗證，該埠就會從 guest VLAN 中移除。此設定自 RouterOS 7.2 版本起可用，且只有在 bridge `vlan-filtering` 啟用時才會生效。預設會停用 guest VLAN。 |
| **interface** (*string*；預設：) | 伺服器將執行所在的介面或介面清單名稱。 |
| **interim-update** (*time*；預設：**0s**) | 排定的 RADIUS Interim-Update 訊息之間的間隔。 |
| **mac-auth-mode** (*mac-as-username \| mac-as-username-and-password*；預設：**mac-as-username**) | 使用 MAC 驗證時，可控制 User-Name 與 User-Password RADIUS 屬性。 |
| **radius-mac-format** (*XX-XX-XX-XX-XX-XX \| XX:XX:XX:XX:XX:XX \| XXXXXXXXXXXX \| xx-xx-xx-xx-xx-xx \| xx:xx:xx:xx:xx:xx \| xxxxxxxxxxxx*；預設：**XX:XX:XX:XX:XX:XX**) | 使用 MAC 驗證時，控制用戶端 MAC 位址在 User-Name 與 User-Password 屬性中的編碼方式。 |
| **reauth-period**(*time*；預設：**!reauth-period**) | 啟用伺服器埠重新驗證。與 `dot1x` 驗證類型一起啟用時，伺服器會透過傳送 EAP-Request Identity 給用戶端，嘗試重新驗證用戶端。與 `mac-auth` 驗證類型一起啟用時，伺服器會使用最後看到的 MAC 位址向 RADIUS 伺服器重新驗證用戶端。此設定自 RouterOS 7.2 版本起可用。預設會停用重新驗證。 |
| **reject-vlan-id** (*integer: 1..4094*；預設：**!reject-vlan-id**) | 當驗證失敗且 RADIUS 伺服器以 Access-Reject 訊息回應時所指派的 VLAN。如果 RADIUS 伺服器完全沒有回應，此屬性不會套用，用戶端驗證只會逾時，服務將無法使用。此屬性只有在 bridge `vlan-filtering` 啟用時才會生效。預設會停用 reject VLAN。 |
| **retrans-timeout** (*time*；預設：**30s**) | 若未收到 supplicant 的回應，訊息重新傳送之間的時間間隔。 |
| **server-fail-vlan-id** (*integer: 1..4094*；預設：**!server-fail-vlan-id**) | 當 RADIUS 伺服器沒有回應且要求逾時已過時所指派的 VLAN。此設定自 RouterOS 7.2 版本起可用，且只有在 bridge `vlan-filtering` 啟用時才會生效。預設會停用 server-fail VLAN。 |

目前已驗證的用戶端會列在 active 選單中（唯讀屬性）。

**子選單：** `/interface/dot1x/server/active`

| 屬性 | 說明 |
| :-- | :-- |
| **auth-info** (*string*) | 驗證資訊：<br/><ul><li>dot1x</li><li>dot1x (guest vlan)</li><li>dot1x (reject vlan)</li><li>dot1x (server fail vlan)</li><li>mac-auth</li><li>mac-auth (reject vlan)</li><li>mac-auth (server fail vlan)</li></ul> |
| **client-mac** (*mac-address*) | supplicant 的 MAC 位址。 |
| **interface** (*string*) | 介面名稱。 |
| **session-id** (*string*) | 唯一工作階段識別碼。 |
| **username** (*string*) | supplicant 的識別資訊。 |
| **vlan-id** (*string*) | 指派給介面的未標記 VLAN ID。必須在 bridge 上啟用 VLAN ID 篩選。 |

所有作用中 dot1x 伺服器介面的狀態會列在 state 選單中（唯讀屬性）。

**子選單：** `/interface/dot1x/server/state`

| 屬性 | 說明 |
| :-- | :-- |
| **interface** (*string*) | 介面名稱。 |
| **status** (*string*) | 可能的介面狀態：<ul><li>authorized - 已授予介面存取權；</li><li>iface-down - 介面未執行；</li><li>rejected-holding - 存取遭 RADIUS 伺服器拒絕；</li><li>un-authorized - 未授予介面存取權。</li></ul> |

## 範例 {#examples}

以下說明 dot1x 伺服器與用戶端最常見的設定範例。

### RouterOS Authenticator 設定 {#routeros-authenticator-configuration}

![](/img/dab2179e067f1308.webp)

先新增 RADIUS 用戶端。驗證伺服器（RADIUS）不一定要與 authenticator 位於同一個 LAN，但必須可從 authenticator 連線，因此必須考量防火牆限制。

```ros
/radius 
add address=10.1.2.3 secret=radiussecret service=dot1x
```

:::warning
如果 RADIUS 通訊是透過公用網路進行，建議使用 RadSec 進行 RADIUS 通訊。詳細資訊：[RADIUS](/docs/authentication-authorization-accounting/radius)
:::

新增 dot1x 伺服器實例。

```ros
/interface/dot1x/server
add interface=ether2 interim-update=30s comment=accounted
add interface=ether12 accounting=no comment=notaccounted
```

#### 以埠為基礎的 VLAN ID 指派 {#port-based-vlan-id-assignment}

可以使用 bridge VLAN filtering 將已驗證的介面指派至特定 VLAN ID。這可透過 RADIUS 的 Tunnel-Type、Tunnel-Medium-Type 與 Tunnel-Private-Group-ID 屬性完成。請注意，只有具備硬體卸載 VLAN filtering 的設備，才能在交換器晶片上執行此操作。

首先，請確認介面已加入已啟用 VLAN filtering 的 bridge。

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether12
```

必須新增靜態 VLAN 設定，才能透過 ether1 介面傳送標記的 VLAN 流量。

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 vlan-ids=2
add bridge=bridge1 tagged=ether1 vlan-ids=12
```

啟用 RADIUS 除錯日誌後，可以查看完整的 RADIUS 訊息封包及其所有屬性。在我們的範例中，Tunnel 屬性是從 RADIUS 伺服器的 Access-Accept 訊息接收：

```text
09:51:45 radius,debug,packet received Access-Accept with id 64 from 10.1.2.3:1812
09:51:45 radius,debug,packet     Tunnel-Type = 13 
09:51:45 radius,debug,packet     Tunnel-Medium-Type = 6 
09:51:45 radius,debug,packet     Tunnel-Private-Group-ID = "12" 
(..)
09:51:45 radius,debug,packet     User-Name = "dot1x-user" 
```

VLAN ID 現在會出現在作用中工作階段清單中，且未標記的埠會加入先前建立的靜態 VLAN 設定。

```ros
/interface/dot1x/server/active/print 
  0 interface=ether12 username="dot1x-user" client-mac=00:0C:42:EB:71:F6 session-id="86b00006" vlan-id=12
```

```ros
/interface/bridge/vlan/print detail 
Flags: X - disabled, D - dynamic 
 0 D bridge=bridge1 vlan-ids=1 tagged="" untagged="" current-tagged="" current-untagged=bridge1,ether3 

 1   bridge=bridge1 vlan-ids=2 tagged=ether1 untagged="" current-tagged=ether1 current-untagged=ether2 

 2   bridge=bridge1 vlan-ids=12 tagged=ether1 untagged="" current-tagged=ether1 current-untagged=ether12 
```

#### 動態交換器規則設定 {#dynamic-switch-rule-configuration}

在某些網路設定中，需要針對特定 supplicant 增加存取規則，以限制或允許特定網路服務。這可透過 Mikrotik-Switching-Filter 屬性完成，請參閱 [RADIUS vendor dictionary](/docs/authentication-authorization-accounting/radius)。當用戶端成功通過驗證伺服器的驗證後，伺服器可以回傳 Mikrotik-Switching-Filter 屬性。根據接收到的資訊，驗證器會在用戶端所在的交換器埠上建立動態存取規則。只要用戶端工作階段仍處於作用中且介面正在執行，這些規則就會保持生效。正確實作交換器規則時，有特定的順序與限制：

- 支援 `mac-protocol`、`src-mac-address`（僅自 RouterOS 7.2 版本起可用）、`src-address`（IPv4/mask，僅自 RouterOS 7.2 版本起可用）、`dst-address`（IPv4/mask）、`protocol`（IPv4）、`src-port`（L4，僅自 RouterOS 7.2 版本起可用）、`dst-port`（L4）條件參數。
- `mac-protocol` 與 `protocol` 參數可使用十六進位或十進位表示法（例如 `protocol 17` 或 `protocol 0x11`）。
- `src-port` 與 `dst-port` 支援單一值或範圍值（例如 `src-port 10` 或 `src-port 10-20`）。
- `src-mac-address` 支援 "xx:xx:xx:xx:xx:xx" 或 "xxxxxxxxxxxx" 格式，且可使用 "none" 關鍵字設定沒有任何來源 MAC 位址的交換器規則（例如 `src-mac-address none`）。
- `src-mac-address`（若尚未由屬性設定）、`switch` 與 `ports` 條件參數會為每條規則自動設定
- 每條規則都應以 action 屬性結尾，支援的值為 **drop** 或 **allow**。若未設定 action 屬性，將使用預設的 **allow** 值。
- 單一 supplicant 支援多條規則，且必須以逗號 "," 分隔。

以下為一些 Mikrotik-Switching-Filter 屬性及其所建立動態交換器規則的範例：

```ros
# Drop ARP frames (EtherType: 0x0806 or 2054)
Mikrotik-Switching-Filter = "mac-protocol 2054 action drop"

/interface/ethernet/switch/rule/print
Flags: X - disabled, I - invalid, D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF mac-protocol=arp copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports=""

# Allow UDP (IP protocol: 0x11 or 17) destination port 100 and drop all other packets
Mikrotik-Switching-Filter = "protocol 17 dst-port 100 action allow, action drop"

/interface/ethernet/switch/rule/print
Flags: X - disabled, I - invalid, D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF protocol=udp dst-port=100 copy-to-cpu=no redirect-to-cpu=no mirror=no 

 1  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports=""

# Allow only authenticated source MAC address, drop all other packets
Mikrotik-Switching-Filter = "action allow, src-mac-address none action drop"

/interface/ethernet/switch/rule/print 
Flags: X - disabled, I - invalid; D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:01:6D:EB/FF:FF:FF:FF:FF:FF copy-to-cpu=no redirect-to-cpu=no mirror=no 

 1  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports="" 
```

在我們的範例中，ether2 上的 Supplicant2 僅允許存取 192.168.50.0/24 網路，且 UDP 目的埠為 50；所有其他流量都應捨棄。首先，請確認橋接埠上的硬體卸載正常運作，否則交換器規則可能無法正常運作。

```ros
/interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                   BRIDGE                   HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0   H ether1                      bridge1                  yes    1     0x80         10                 10       none
 1   H ether2                      bridge1                  yes    1     0x80         10                 10       none
 2   H ether12                     bridge1                  yes    1     0x80         10                 10       none
```

啟用 RADIUS 除錯日誌後，可以查看包含所有屬性的完整 RADIUS 訊息封包。在我們的範例中，Mikrotik-Switching-Filter 屬性是從 Radius 伺服器傳來的 Access-Accept 訊息中接收：

```text
02:35:38 radius,debug,packet received Access-Accept with id 121 from 10.1.2.3:1812 
(..)
02:35:38 radius,debug,packet     MT-Switching-Filter = "mac-protocol 2048 dst-address 192.168.50.0/24 dst-port 50 protocol 17 action allow,action drop"
```

動態交換器規則現在會出現在 switch 選單下：

```ros
/interface/ethernet/switch/rule/print 
Flags: X - disabled, I - invalid; D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether2 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF mac-protocol=ip dst-address=192.168.50.0/24 protocol=udp dst-port=50 copy-to-cpu=no redirect-to-cpu=no mirror=no 

 1  D ;;; dot1x dynamic
      switch=switch1 ports=ether2 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports="" 
```

:::warning
動態交換器規則僅適用於支援交換器規則的 RouterBoard：配備 Marvell Prestera 交換器的 MikroTik 設備，以及配備 QCA8337、Atheros8327 和 Atheros8316 交換器晶片的設備。CRS1xx/2xx 系列交換器不支援此功能。請考量每部設備的規則數量上限，請參閱 [MikroTik devices with Marvell Prestera switch](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#models) 與 [basic switch chip table](/docs/bridging-and-switching/switch-chip-features)
:::

### RouterOS Supplicant 設定 {#routeros-supplicant-configuration}

`eap-tls, eap-ttls` 與 `eap-peap` 驗證方法需要 CA 憑證。此外，`eap-tls` 方法需要用戶端憑證。在此範例中，我們已匯入一個 P12 憑證套件，其中包含自我簽署的用戶端憑證與 CA 憑證。如需更多關於在 RouterOS 中匯入憑證的資訊，請參閱 [System/Certificates](/docs/authentication-authorization-accounting/certificates)。

```ros
/certificate/print 
Flags: K - private-key, L - crl, C - smart-card-key, A - authority, I - issued, R - revoked, E - expired, T - trusted 
 #         NAME                                            COMMON-NAME                                         SUBJECT-ALT-NAME                             FINGERPRINT                                        
 0 K  A  T dot1x-client                                    ez_dot1x-client                                     IP:10.1.2.34
 1  L A  T dot1x CA                                        ca            
```

只要新增一個 `dot1x` 用戶端實例，即可啟動驗證程序。

```ros
/interface/dot1x/client
add anon-identity=anonymous client-certificate=dot1x-client eap-methods=eap-tls identity=dot1x-user interface=ether1 password=dot1xtest
```

如果驗證成功，介面狀態應為 `authenticated`。

```ros
/interface/dot1x/client/print 
Flags: I - inactive, X - disabled 
  0   interface=ether1 eap-methods=eap-tls identity="dot1x-user" password="dot1xtest" anon-identity="anonymous" client-certificate=dot1x-client status="authenticated"
```
