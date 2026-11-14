---
sidebar_key: "authentication-authorization-accounting/dot1x"
sidebar_position: 2
title: "Dot1X"
sidebar_label: "Dot1X"
description: "本頁介紹 MikroTik RouterOS 的 Dot1X 實現，涵蓋基於 IEEE 802.1X 埠的網路訪問控制的用戶端和伺服器配置，使用 TLS、TTLS 和 PEAP 等 EAP 方法。"
tags:
  - 'dot1x'
  - 'radius'
  - 'authentication'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/dot1x
captured_at: '2026-11-04T11:27:04+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Dot1X 是 IEEE 802.1X 標準在 RouterOS 中的實現。主要目的是使用基於區域網路的 EAP（也稱為 EAPOL）提供基於埠的網路訪問控制。802.1X 由請求方（用戶端）、認證器（伺服器）和認證伺服器（RADIUS 伺服器）組成。RouterOS 同時支援認證器和請求方兩端，並且在安裝 [使用者管理器](./user-manager.md) 軟體包時也支援認證伺服器。請求方支援的 EAP 方法有 EAP-TLS、EAP-TTLS、EAP-MSCHAPv2 和 PEAPv0/EAP-MSCHAPv2。

:::warning
該功能在 SMIPS 裝置（hAP lite、hAP lite TC 和 hAP mini）上不受支援。

:::

## 用戶端 {#client}

請求方配置設定。

**子選單：** `/interface/dot1x/client`

| 屬性 | 描述 |
| :-- | :-- |
| **anon-identity** (*string*; 預設： ) | 用於外層 EAP 認證的身份。僅與 `eap-ttls` 和 `eap-peap` 方法一起使用。如果未設定，則外層 EAP 認證將使用 `identity` 引數中的值。 |
| **client-certificate** (*string*; 預設： ) | 在 [System/Certificates](./certificates.md) 中列出的證書名稱。使用 `eap-tls` 方法時必需。 |
| **comment** (*string*; 預設： ) | 條目的簡短描述。 |
| **disabled** (*yes \| no*; 預設： **no**) | 用戶端是否啟用。 |
| **eap-methods** (*eap-tls \| eap-ttls \| eap-peap \| eap-mschapv2*; 預設： ) | 用於認證的 EAP 方法有序列表。 |
| **identity** (*string*; 預設： ) | 用於 EAP 認證的請求方身份。 |
| **interface** (*string*; 預設： ) | 用戶端將執行的介面名稱。 |
| **password** (*string*; 預設： ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 請求方的明文密碼。 |

### 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **status** (*authenticated \| authenticating \| disabled*) | 可能的狀態：authenticated - 用戶端已成功認證。authenticating - 已連線到伺服器，認證過程正在進行。disabled - 用戶端已停用。error - 發生內部錯誤。interface is down - 父介面未執行。rejected - 伺服器拒絕了認證。 |

## 伺服器 {#server}

---

RouterOS dot1x 伺服器充當認證器。啟用了 dot1x 伺服器的介面會阻止所有流量，但用於認證的 EAPOL 封包除外。用戶端成功認證後，介面將接受該埠上收到的所有流量。如果介面連線到包含多個主機的共享介質，則當至少一個用戶端成功認證後，將接受來自所有主機的流量。不過，可以[配置動態交換器規則](./dot1x.md#dynamic-switch-rule-configuration)以僅接受已認證使用者的源 MAC 地址，並丟棄所有其他源 MAC 地址。如果認證失敗，則可以使用專用埠 VLAN ID 接受流量。

:::warning
在網橋埠上建立 dot1x 伺服器時，網橋應執行 (R/M)STP，否則來自用戶端的 EAP 封包將無法被正確接受。網橋介面預設使用 `protocol-mode=rstp` 建立。如果網橋埠不應傳送任何 BPDU，或應忽略任何收到的 BPDU，請在網橋埠上使用 `edge=yes` 配置。

:::

**子選單：** `/interface/dot1x/server`

| 屬性 | 描述 |
| :-- | :-- |
| **accounting** (*yes \| no*; 預設： **yes**) | 是否向認證伺服器傳送 RADIUS 計費請求。 |
| **auth-timeout** (*time*; 預設： **1m**) | EAP 認證可用的總時間。 |
| **auth-types** (*dot1x \| mac-auth*; 預設： **dot1x**) | 伺服器介面上使用的認證型別。當同時選擇兩個選項時，伺服器將優先使用 `dot1x` 認證型別，並且只有在 3 個 `retrans-timeout` 週期後，認證型別才會回退到 `mac-auth`。為了使 `mac-auth` 認證型別正常工作，伺服器介面應至少收到一個包含用戶端裝置源 MAC 地址的幀。 |
| **comment** (*string*; 預設： ) | 條目的簡短描述。 |
| **disabled** (*yes \| no*; 預設： **no**) | 伺服器配置是否啟用。 |
| **guest-vlan-id** (*integer: 1..4094*; 預設： **!guest-vlan-id**) | 當終端裝置不支援 `dot1x` 認證且未配置 `mac-auth` 回退時分配的 VLAN。該設定將在 3 個 `retrans-timeout` 週期後生效。一旦建立了啟用 dot1x 的用戶端併成功完成重新認證，該埠就會從訪客 VLAN 中移除。此設定從 RouterOS 7.2 版本起可用，並且在網橋啟用 `vlan-filtering` 時生效。預設情況下，訪客 VLAN 處於停用狀態。 |
| **interface** (*string*; 預設： ) | 伺服器將執行的介面或介面列表名稱。 |
| **interim-update** (*time*; 預設： **0s**) | 計劃傳送的 RADIUS Interim-Update 訊息之間的間隔。 |
| **mac-auth-mode** (*mac-as-username \| mac-as-username-and-password*; 預設： **mac-as-username**) | 允許在使用 MAC 認證時控制 User-Name 和 User-Password RADIUS 屬性。 |
| **radius-mac-format** (*XX-XX-XX-XX-XX-XX \| XX:XX:XX:XX:XX:XX \| XXXXXXXXXXXX \| xx-xx-xx-xx-xx-xx \| xx:xx:xx:xx:xx:xx \| xxxxxxxxxxxx*; 預設： **XX:XX:XX:XX:XX:XX**) | 控制使用 MAC 認證時，用戶端 MAC 地址在 User-Name 和 User-Password 屬性中的編碼方式。 |
| **reauth-period**(*time*; 預設： **!reauth-period**) | 啟用伺服器埠重新認證。與 `dot1x` 認證型別一起啟用時，伺服器將透過向用戶端傳送 EAP-Request Identity 來嘗試重新認證用戶端。與 `mac-auth` 認證型別一起啟用時，伺服器將使用最後看到的 MAC 地址嘗試透過 RADIUS 伺服器重新認證用戶端。此設定從 RouterOS 7.2 版本起可用。預設情況下，重新認證處於停用狀態。 |
| **reject-vlan-id** (*integer: 1..4094*; 預設： **!reject-vlan-id**) | 當認證失敗且 RADIUS 伺服器響應 Access-Reject 訊息時分配的 VLAN。如果 RADIUS 伺服器完全無響應，則此屬性不會生效，用戶端認證只會超時，服務將不可用。此屬性僅在網橋啟用 `vlan-filtering` 時生效。預設情況下，拒絕 VLAN 處於停用狀態。 |
| **retrans-timeout** (*time*; 預設： **30s**) | 如果未收到請求方的響應，則訊息重新傳輸之間的時間間隔。 |
| **server-fail-vlan-id** (*integer: 1..4094*; 預設： **!server-fail-vlan-id**) | 當 RADIUS 伺服器無響應且請求超時時間已過時分配的 VLAN。此設定從 RouterOS 7.2 版本起可用，並且在網橋啟用 `vlan-filtering` 時生效。預設情況下，伺服器故障 VLAN 處於停用狀態。 |

當前已認證的用戶端列在 active 選單中（只讀屬性）。

**子選單：** `/interface/dot1x/server/active`

| 屬性 | 描述 |
| :-- | :-- |
| **auth-info** (*string*) | 認證資訊：dot1xdot1x (guest vlan)dot1x (reject vlan)dot1x (server fail vlan)mac-authmac-auth (reject vlan)mac-auth (server fail vlan) |
| **client-mac** (*mac-address*) | 請求方的 MAC 地址。 |
| **interface** (*string*) | 介面名稱。 |
| **session-id** (*string*) | 唯一會話識別符號。 |
| **username** (*string*) | 請求方的身份。 |
| **vlan-id** (*string*) | 分配給介面的未標記 VLAN ID。必須在網橋上啟用 VLAN ID 過濾。 |

所有活動 dot1x 伺服器介面的狀態列在 state 選單中（只讀屬性）。

**子選單：** `/interface/dot1x/server/state`

| 屬性 | 描述 |
| :-- | :-- |
| **interface** (*string*) | 介面名稱。 |
| **status** (*string*) | 可能的介面狀態：authorized - 已授予介面訪問許可權；iface-down - 介面未執行；rejected-holding - RADIUS 伺服器拒絕了訪問；un-authorized - 未授予介面訪問許可權。 |

## 示例 {#examples}

下面介紹 dot1x 伺服器和用戶端最常見的配置示例。

### RouterOS 認證器配置 {#routeros-authenticator-configuration}

![](/img/dab2179e067f1308.webp)

首先新增一個新的 RADIUS 用戶端。認證伺服器（RADIUS）不一定必須與認證器位於同一 LAN 中，但必須能夠從認證器訪問，因此必須考慮任何防火牆限制。

```ros
/radius 
add address=10.1.2.3 secret=radiussecret service=dot1x
```

:::warning
如果 RADIUS 通訊透過公共網路進行，建議使用 RadSec 進行 RADIUS 通訊。更多資訊：[RADIUS](./radius.md)

:::

新增新的 dot1x 伺服器例項。

```ros
/interface/dot1x/server
add interface=ether2 interim-update=30s comment=accounted
add interface=ether12 accounting=no comment=notaccounted
```

#### 基於埠的 VLAN ID 分配 {#port-based-vlan-id-assignment}

可以使用網橋 VLAN 過濾將已認證的介面分配到特定 VLAN ID。這可以透過 RADIUS Tunnel-Type、Tunnel-Medium-Type 和 Tunnel-Private-Group-ID 屬性來完成。請注意，只有具備硬體解除安裝 VLAN 過濾的裝置才能在交換晶片中執行此操作。

首先，確保介面已新增到啟用了 VLAN 過濾的網橋中。

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether12
```

必須新增靜態 VLAN 配置，以便帶標記的 VLAN 流量透過 ether1 介面傳送。

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 vlan-ids=2
add bridge=bridge1 tagged=ether1 vlan-ids=12
```

啟用 RADIUS 偵錯日誌後，可以檢視包含所有屬性的完整 RADIUS 訊息封包。在我們的示例中，從 RADIUS 伺服器收到的 Access-Accept 訊息中包含 Tunnel 屬性：

```text
09:51:45 radius,debug,packet received Access-Accept with id 64 from 10.1.2.3:1812
09:51:45 radius,debug,packet     Tunnel-Type = 13 
09:51:45 radius,debug,packet     Tunnel-Medium-Type = 6 
09:51:45 radius,debug,packet     Tunnel-Private-Group-ID = "12" 
(..)
09:51:45 radius,debug,packet     User-Name = "dot1x-user" 
```

VLAN ID 現在會出現在活動會話列表中，並且未標記埠會新增到之前建立的靜態 VLAN 配置中。

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

#### 動態交換器規則配置 {#dynamic-switch-rule-configuration}

在某些網路配置中，需要為特定請求方新增額外的訪問規則，以限制或允許某些網路服務。這可以使用 Mikrotik-Switching-Filter 屬性來完成，請參閱 [RADIUS 廠商字典](./radius.md)。當用戶端透過認證伺服器成功認證後，伺服器可以回傳 Mikrotik-Switching-Filter 屬性。根據收到的資訊，認證器將在用戶端所在的交換器埠上建立動態訪問規則。只要用戶端會話處於活動狀態且介面正在執行，這些規則就會保持活動。正確實現交換器規則存在一定的順序和限制：

- 支援 `mac-protocol`、`src-mac-address`（僅從 RouterOS 7.2 版本起可用）、`src-address`（IPv4/mask，僅從 RouterOS 7.2 版本起可用）、`dst-address`（IPv4/mask）、`protocol`（IPv4）、`src-port`（L4，僅從 RouterOS 7.2 版本起可用）、`dst-port`（L4）條件引數。
- `mac-protocol` 和 `protocol` 引數可以使用十六進位制或十進位制表示（例如 `protocol 17` 或 `protocol 0x11`）。
- `src-port` 和 `dst-port` 支援單個值或範圍值（例如 `src-port 10` 或 `src-port 10-20`）。
- `src-mac-address` 支援 "xx:xx:xx:xx:xx:xx" 或 "xxxxxxxxxxxx" 格式，並且可以使用 "none" 關鍵字設定不帶任何源 MAC 地址的交換器規則（例如 `src-mac-address none`）。
- 每條規則都會自動設定 `src-mac-address`（如果尚未由該屬性設定）`, switch` 和 `ports` 條件引數
- 每條規則應以 action 屬性結尾，支援的值為 **drop** 或 **allow**。如果未設定 action 屬性，則使用預設值 **allow**。
- 單個請求方支援多條規則，並且必須用逗號“,”分隔。

以下是一些 Mikrotik-Switching-Filter 屬性示例以及它們建立的動態交換器規則：

```ros
# 丢弃 ARP 帧（EtherType: 0x0806 或 2054）
Mikrotik-Switching-Filter = "mac-protocol 2054 action drop"

/interface/ethernet/switch/rule/print
Flags: X - disabled, I - invalid, D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF mac-protocol=arp copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports=""

# 允许 UDP（IP protocol: 0x11 或 17）目标端口 100，并丢弃所有其他数据包
Mikrotik-Switching-Filter = "protocol 17 dst-port 100 action allow, action drop"

/interface/ethernet/switch/rule/print
Flags: X - disabled, I - invalid, D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF protocol=udp dst-port=100 copy-to-cpu=no redirect-to-cpu=no mirror=no 

 1  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports=""

# 仅允许已验证的源 MAC 地址，丢弃所有其他数据包
Mikrotik-Switching-Filter = "action allow, src-mac-address none action drop"

/interface/ethernet/switch/rule/print 
Flags: X - disabled, I - invalid; D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:01:6D:EB/FF:FF:FF:FF:FF:FF copy-to-cpu=no redirect-to-cpu=no mirror=no 

 1  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports="" 
```

在我們的示例中，ether2 上的 Supplicant2 僅允許訪問 192.168.50.0/24 網路，並使用 UDP 目標埠 50；所有其他流量都應被丟棄。首先，確保網橋埠上的硬體解除安裝正常工作，否則交換器規則可能無法正常工作。

```ros
/interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                   BRIDGE                   HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0   H ether1                      bridge1                  yes    1     0x80         10                 10       none
 1   H ether2                      bridge1                  yes    1     0x80         10                 10       none
 2   H ether12                     bridge1                  yes    1     0x80         10                 10       none
```

啟用 RADIUS 偵錯日誌後，可以檢視包含所有屬性的完整 RADIUS 訊息封包。在我們的示例中，從 RADIUS 伺服器收到的 Access-Accept 訊息中包含 Mikrotik-Switching-Filter 屬性：

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
動態交換器規則僅適用於支援交換器規則的 RouterBOARD - 採用 Marvell Prestera 交換器的 MikroTik 裝置，以及採用 QCA8337、Atheros8327 和 Atheros8316 交換晶片的裝置。CRS1xx/2xx 系列交換器不支援此功能。請考慮每臺裝置的最大規則數，請參閱[採用 Marvell Prestera 交換器的 MikroTik 裝置](../bridging-and-switching/marvell-prestera-switch-chip-features.md#models)和[基本交換器晶片表](../bridging-and-switching/switch-chip-features.md)

:::

### RouterOS 請求方配置 {#routeros-supplicant-configuration}

`eap-tls, eap-ttls` 和 `eap-peap` 認證方法需要 CA 證書。此外，`eap-tls` 方法還需要用戶端證書。對於此示例，我們已經匯入了包含自簽名用戶端證書和 CA 證書的 P12 證書捆綁包。有關如何在 RouterOS 中匯入證書的更多資訊，請訪問 [System/Certificates](./certificates.md)。

```ros
/certificate/print 
Flags: K - private-key, L - crl, C - smart-card-key, A - authority, I - issued, R - revoked, E - expired, T - trusted 
 #         NAME                                            COMMON-NAME                                         SUBJECT-ALT-NAME                             FINGERPRINT                                        
 0 K  A  T dot1x-client                                    ez_dot1x-client                                     IP:10.1.2.34
 1  L A  T dot1x CA                                        ca            
```

只需新增一個新的 dot1x 用戶端例項，它就會啟動認證過程。

```ros
/interface/dot1x/client
add anon-identity=anonymous client-certificate=dot1x-client eap-methods=eap-tls identity=dot1x-user interface=ether1 password=dot1xtest
```

如果認證成功，介面狀態應為 authenticated。

```ros
/interface/dot1x/client/print 
Flags: I - inactive, X - disabled 
  0   interface=ether1 eap-methods=eap-tls identity="dot1x-user" password="dot1xtest" anon-identity="anonymous" client-certificate=dot1x-client status="authenticated"
```
