---
title: "使用者管理員"
description: "RouterOS 中的 User Manager 為 DHCP、Hotspot 與 PPP 等服務提供集中式 RADIUS 驗證與授權，並支援多種驗證方法。它包含可用於通道設定與工作階段管理的自訂 RADIUS 屬性，授權則會影響作用中的工作階段。"
tags:
  - 'radius'
  - 'authentication'
  - 'authorization'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/user-manager
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

## 概觀 {#overview}

User Manager 是 RouterOS 中的 RADIUS 伺服器實作，可為特定服務提供集中式使用者驗證與授權。集中式使用者資料庫可更有效地追蹤系統使用者與客戶。User Manager 做為獨立套件，可在除 SMIPS 以外的所有架構上使用；不過，由於可用空間有限，必須特別留意。它支援多種驗證方法，包括 PAP、CHAP、MS-CHAP、MS-CHAPv2、EAP-TLS、EAP-TTLS 與 EAP-PEAP。在 RouterOS 中，DHCP、Dot1x、Hotspot、IPsec、PPP 與 Wireless 是最能從 User Manager 獲益的功能。每位使用者都可以透過 WEB 介面查看其帳戶統計資料，並管理可用的設定檔。此外，使用者可以使用最受歡迎的付款閘道 PayPal 購買自己的資料方案（profiles），使其成為服務供應商的絕佳系統。可以產生自訂報表，以簡化帳務部門的處理作業。User Manager 依據 [RFC2865](https://tools.ietf.org/html/rfc2865) 與 [RFC3579](https://tools.ietf.org/html/rfc3579) 中定義的 RADIUS 標準運作。

User Manager 是受 RouterOS 授權等級限制的 RouterOS 功能之一。視 [License level](/docs/getting-started/routeros-licensing/x86#routeros-license-key-levels) 而定，有效工作階段數會受到限制，包括每位使用者的多重連線（而非不重複帳戶）。

![](/img/074aaadffaa40983.webp)

## Attributes

**子選單：** `/user-manager/attribute`

RADIUS 屬性是定義在 RADIUS 伺服器與用戶端之間傳遞的授權、資訊與設定參數。User Manager 允許傳送在「attributes」選單中定義的自訂屬性。RouterOS 已有一組預先定義的屬性，但必要時也可以新增其他屬性。預先定義的屬性：

| 屬性 | 供應商 ID | 類型 ID | 值類型 | 封包類型 | 說明 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Framed-IP-Address | 0 (standard) | 8 | ip address | Access-Accept | <a href="https://tools.ietf.org/html/rfc2865#section-5.8" target="_blank" rel="noopener noreferrer">RFC2865 section 5.8</a> |
| Framed-IP-Netmask | 0 (standard) | 9 | <code>/ip/address</code> | Access-Accept | <a href="https://tools.ietf.org/html/rfc2865#section-5.9" target="_blank" rel="noopener noreferrer">RFC2865 section 5.9</a> |
| Session-Timeout | 0 (standard) | 27 | integer (maximum value: 21474720) | Access-Accept, Access-Challenge | <a href="https://tools.ietf.org/html/rfc2865#section-5.27" target="_blank" rel="noopener noreferrer">RFC2865 section 5.27</a> |
| Idle-Timeout | 0 (standard) | 28 | integer | Access-Accept, Access-Challenge | <a href="https://tools.ietf.org/html/rfc2865#section-5.28" target="_blank" rel="noopener noreferrer">RFC2865 section 5.28</a> |
| Tunnel-Type | 0 (standard) | 64 |  | Value | Description |
| Value | Description |  |  |  |  |
| 1 | Point-to-Point Tunneling Protocol (PPTP) |  |  |  |  |
| 2 | Layer Two Forwarding (L2F) |  |  |  |  |
| 3 | Layer Two Tunneling Protocol (L2TP) |  |  |  |  |
| 4 | Ascend Tunnel Management Protocol (ATMP) |  |  |  |  |
| 5 | Virtual Tunneling Protocol (VTP) |  |  |  |  |
| 6 | IP Authentication Header in the Tunnel-mode (AH) |  |  |  |  |
| 7 | IP-in-IP Encapsulation (IP-IP) |  |  |  |  |
| 8 | Minimal IP-in-IP Encapsulation (MIN-IP-IP) |  |  |  |  |
| 9 | IP Encapsulating Security Payload in the Tunnel-mode (ESP) |  |  |  |  |
| 10 | Generic Route Encapsulation (GRE) |  |  |  |  |
| 11 | Bay Dial Virtual Services (DVS) |  |  |  |  |
| 12 | IP-in-IP Tunneling |  |  |  |  |
| 13 | Virtual LAN |  |  |  |  |
| Tunnel-Medium-Type | 0 (standard) | 65 |  | Value | Description |
| Value | Description |  |  |  |  |
| 1 | IPv4 (IP version 4) |  |  |  |  |
| 2 | IPv6 (IP version 6) |  |  |  |  |
| 3 | NSAP |  |  |  |  |
| 4 | HDLC (8-bit multidrop) |  |  |  |  |
| 5 | BBN 1822 |  |  |  |  |
| 6 | 802 (includes all 802 media plus Ethernet "canonical format") |  |  |  |  |
| 7 | E.163 (POTS) |  |  |  |  |
| 8 | E.164 (SMDS, Frame Relay, ATM) |  |  |  |  |
| 9 | F.69 (Telex) |  |  |  |  |
| 10 | X.121 (X.25, Frame Relay) |  |  |  |  |
| 11 | IPX |  |  |  |  |
| 12 | Appletalk |  |  |  |  |
| 13 | Decnet IV |  |  |  |  |
| 14 | Banyan Vines |  |  |  |  |
| 15 | E.164 with NSAP format subaddress |  |  |  |  |
| Tunnel-Private-Group-ID | 0 (standard) | 81 | string | Access-Accept | <a href="https://tools.ietf.org/html/rfc2868#section-3.6" target="_blank" rel="noopener noreferrer">RFC2868 section 3.6</a> |
| Framed-Pool | 0 (standard) | 88 | string | Access-Accept | <a href="https://tools.ietf.org/html/rfc2869#section-5.18" target="_blank" rel="noopener noreferrer">RFC2869 section 5.18</a> |
| Framed-IPv6-Prefix | 0 (standard) | 97 | ipv6 prefix | Access-Accept | <a href="https://tools.ietf.org/html/rfc3162#section-2.3" target="_blank" rel="noopener noreferrer">RFC3162 section 2.3</a> |
| Framed-IPv6-Pool | 0 (standard) | 100 | string | Access-Accept | <a href="https://tools.ietf.org/html/rfc3162#section-2.6" target="_blank" rel="noopener noreferrer">RFC3162 section 2.6</a> |
| Delegated-IPv6-Prefix | 0 (standard) | 123 | ipv6 prefix | Access-Accept | <a href="https://tools.ietf.org/html/rfc4818" target="_blank" rel="noopener noreferrer">RFC4818</a> |
| Framed-IPv6-Address | 0 (standard) | 168 | ip address | Access-Accept | <a href="https://tools.ietf.org/html/rfc6911#section-3.1" target="_blank" rel="noopener noreferrer">RFC6911 section 3.1</a> |
| Mikrotik-Recv-Limit | 14988 (Mikrotik) | 1 | integer | Access-Accept | 用戶端的接收總量限制，單位為位元組。 |
| Mikrotik-Xmit-Limit | 14988 (Mikrotik) | 2 | integer | Access-Accept | 用戶端的傳送總量限制，單位為位元組。 |
| Mikrotik-Group | 14988 (Mikrotik) | 3 | string | Access-Accept | 本機使用者的使用者群組。 <br/> HotSpot 使用者的 HotSpot 設定檔。 <br/> PPP 使用者的 PPP 設定檔。 |
| Mikrotik-Wireless-Forward | 14988 (Mikrotik) | 4 | integer | Access-Accept | 若此屬性設為「0」，則不會將用戶端的訊框轉送回無線基礎架構（僅限 wireless）。 |
| Mikrotik-Wireless-Skip-Dot1x | 14988 (Mikrotik) | 5 | integer | Access-Accept | 若設為非零值，則停用特定無線用戶端的 802.1x 驗證（僅限 wireless）。 |
| Mikrotik-Wireless-Enc-Algo | 14988 (Mikrotik) | 6 |  | Value | Description |
| Value | Description |  |  |  |  |
| 0 | No-encryption |  |  |  |  |
| 1 | 40-bit-WEP |  |  |  |  |
| 2 | 104-bit-WEP |  |  |  |  |
| 3 | AES-CCM |  |  |  |  |
| 4 | TKIP |  |  |  |  |
| Mikrotik-Wireless-Enc-Key | 14988 (Mikrotik) | 7 | string | Access-Accept | 用戶端的 WEP 加密金鑰（僅限 wireless）。 |
| Mikrotik-Rate-Limit | 14988 (Mikrotik) | 8 | string | Access-Accept | 用戶端的資料速率限制。格式為：rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]，以路由器的角度來看（因此「rx」是用戶端上傳，「tx」是用戶端下載）。所有速率都應為數字，並可選擇加上 'k'（1,000 倍）或 'M'（1,000,000 倍）。若未指定 tx-rate，則 rx-rate 也會做為 tx-rate 使用。tx-burst-rate、tx-burst-threshold 與 tx-burst-time 也是如此。若 rx-burst-threshold 與 tx-burst-threshold 都未指定（但指定了 burst-rate），則 rx-rate 與 tx-rate 會做為突發臨界值。若 rx-burst-time 與 tx-burst-time 都未指定，則預設使用 1s。Priority 的值為 1..8，其中 1 表示最高優先順序，8 表示最低。若未指定 rx-rate-min 與 tx-rate-min，則使用 rx-rate 與 tx-rate 的值。rx-rate-min 與 tx-rate-min 的值不能超過 rx-rate 與 tx-rate 的值。 |
| Mikrotik-Realm | 14988 (Mikrotik) | 9 | string | Access-Request | 若是在 /radius 選單中設定，則會在每個 RADIUS 要求中包含為 Mikrotik-Realm 屬性。若未設定，則會傳送與 MS-CHAP-Domain 屬性相同的值（若缺少 MS-CHAP-Domain，也不會包含 Realm）。 |
| Mikrotik-Host-IP | 14988 (Mikrotik) | 10 | ip address | Access-Request | Universal Client 轉換前 HotSpot 用戶端的 IP 位址（用戶端的原始 IP 位址）。 |
| Mikrotik-Mark-Id | 14988 (Mikrotik) | 11 | string | Access-Accept | 防火牆 mangle chain 名稱（僅限 HotSpot）。MikroTik RADIUS 用戶端收到此屬性後，會建立動態防火牆 mangle 規則，其 action=jump、chain=hotspot，且 jump-target 等於屬性值。Mangle chain 名稱可以有 .in 或 .out 後綴，這會只針對傳入或傳出流量安裝規則。可以提供多個 Mark-id 屬性，但只會使用傳入與傳出的最後一個。 |
| Mikrotik-Advertise-URL | 14988 (Mikrotik) | 12 | string | Access-Accept | 應顯示給用戶端的廣告頁面 URL。若指定此屬性，則會自動啟用廣告，包括透明代理，即使在對應的使用者設定檔中已明確停用也是如此。RADIUS 伺服器可以傳送多個屬性執行個體，以指定其他 URL，並以輪詢方式選擇。 |
| Mikrotik-Advertise-Interval | 14988 (Mikrotik) | 13 | integer | Access-Accept | 兩個相鄰廣告之間的時間間隔。RADIUS 伺服器可以傳送多個屬性執行個體，以指定其他間隔。所有間隔值都會視為清單，並在每次成功播放廣告時逐一採用。若已到達清單末端，則會繼續使用最後一個值。 |
| Mikrotik-Recv-Limit-Gigawords | 14988 (Mikrotik) | 14 | integer | Access-Accept | 接收總量限制的 4G (2^32) 位元組（位元 32..63，位元 0..31 由 Mikrotik-Recv-Limit 傳遞）。 |
| Mikrotik-Xmit-Limit-Gigawords | 14988 (Mikrotik) | 15 | integer | Access-Accept | 傳送總量限制的 4G (2^32) 位元組（位元 32..63，位元 0..31 由 Mikrotik-Xmit-Limit 傳遞）。 |
| Mikrotik-Wireless-PSK | 14988 (Mikrotik) | 16 | string | Access-Accept |  |
| Mikrotik-Total-Limit | 14988 (Mikrotik) | 17 | integer | Access-Accept |  |
| Mikrotik-Total-Limit-Gigawords | 14988 (Mikrotik) | 18 | integer | Access-Accept |  |
| Mikrotik-Address-List | 14988 (Mikrotik) | 19 | string | Access-Accept |  |
| Mikrotik-Wireless-MPKey | 14988 (Mikrotik) | 20 | string | Access-Accept |  |
| Mikrotik-Wireless-Comment | 14988 (Mikrotik) | 21 | string | Access-Accept |  |
| Mikrotik-Delegated-IPv6-Pool | 14988 (Mikrotik) | 22 | string | Access-Accept | 用於 Prefix Delegation 的 IPv6 集區。 |
| Mikrotik-DHCP-Option-Set | 14988 (Mikrotik) | 23 | string | Access-Accept |  |
| Mikrotik-DHCP-Option-Param-STR1 | 14988 (Mikrotik) | 24 | string | Access-Accept |  |
| Mikrotik-DHCP-Option-Param-STR2 | 14988 (Mikrotik) | 25 | string | Access-Accept |  |
| Mikrotik-Wireless-VLANID | 14988 (Mikrotik) | 26 | integer | Access-Accept | 用戶端的 VLAN ID（僅限 Wireless）。 |
| Mikrotik-Wireless-VLANIDtype | 14988 (Mikrotik) | 27 |  | Value | Description |
| Value | Description |  |  |  |  |
| 0 | 802.1q |  |  |  |  |
| 1 | 802.1ad |  |  |  |  |
| Mikrotik-Wireless-Minsignal | 14988 (Mikrotik) | 28 | string | Access-Accept |  |
| Mikrotik-Wireless-Maxsignal | 14988 (Mikrotik) | 29 | string | Access-Accept |  |
| Mikrotik-Switching-Filter | 14988 (Mikrotik) | 30 | string | Access-Accept | 使用 dot1x 伺服器驗證用戶端時，允許建立動態交換器規則。 |

**Properties**

| 屬性 | 說明 |
| :-- | :-- |
| **name** (*string*; Default: ) | 屬性的名稱。 |
| **packet-types** (*string*; Default: **access-accept**) | <ul><li>access-accept - 在 RADIUS Access-Accept 訊息中使用此屬性</li><li>access-challenge - 在 RADIUS Access-Challenge 訊息中使用此屬性</li></ul> |
| **type-id** (*integer:1..255*; Default: ) | 來自特定供應商屬性資料庫的屬性識別編號。 |
| **value-type** (*string*; Default: ) | <ul><li>hex</li><li>ip-address - IPv4 或 IPv6 IP 位址</li><li>ip6-prefix - IPv6 前綴</li><li>macro</li><li>string</li><li>uint32</li></ul> |
| **vendor-id** (*integer*; Default: **0**) | IANA 配置的特定企業識別編號。 |

## Database

**子選單：** `/user-manager/database`

所有與 RADIUS 相關的資訊都儲存在獨立的 User Manager 資料庫中，可在「database」子選單下設定。「Enabled」與「db-path」是唯一不儲存在 User Manager 資料庫中的參數，而是儲存在 RouterOS 主要設定表中，這表示這些參數會受到 RouterOS 設定重設的影響。其餘設定、工作階段與付款資料則儲存在設備 FLASH 儲存空間上的獨立 SQLite 資料庫中。對資料庫執行任何操作時，建議在活動前後都進行備份。

### 屬性 {#properties}

| Property | Description |
| :-- | :-- |
| **db-path** (*string*; Default: ) | 資料庫檔案將儲存位置的路徑。 |

### 唯讀屬性 {#read-only-properties}

| Property | Description |
| :-- | :-- |
| **db-size** | 資料庫目前的大小。 |
| **free-disk-space** | 儲存資料庫的磁碟上剩餘的可用空間。 |

### 指令 {#commands}

| Property | Description |
| :-- | :-- |
| **load** (*name*) | 還原先前建立的 .umb 格式備份檔案。 |
| **migrate-legacy-db** (*database-path; overwrite*) | 將舊版 User Manager（RouterOS v6 或更早版本）轉換為新標準。可以覆寫目前的資料庫。 |
| **optimize-db** () |  |
| **save** (name; overwrite) | 儲存 User Manager 資料庫的目前狀態。 |

## Limitations

**子選單：** `/user-manager/limitation`

限制由 Profiles 使用，並透過 Profile-Limitations 相互連結。必須啟用 RADIUS accounting 與 Interim updates，才能在達到 *download-limit*、*upload-limit* 或 *uptime-limit* 時，順暢地在多個限制之間切換，或中斷作用中的連線。

若要從 User Manager 中斷已作用中的連線，必須在 RADIUS 用戶端將 *accept* 設為 *yes*。如果同時連線數限制不是無限（shared-users），且已達到允許的最大數量，路由器會先嘗試中斷較早的使用者連線。

User-Manager 會在接受新使用者之前嘗試中斷作用中的連線（已設定適當限制時）。因此，在此類設定中，建議對 `/radius/client/timeout` 使用 1s。

:::danger
RouterOS 中的 IPsec 服務不支援速率限制。
:::

## 屬性 {#properties-1}

| Property | Description |
| :-- | :-- |
| **comment** (*string*; Default: ) | 限制的簡短描述。 |
| **download-limit** (*integer*; Default: **0**) | 使用者可下載的流量總量，單位為 Bytes。 |
| **name** (*string*; Default: ) | 限制的唯一名稱。 |
| **rate-limit-burst-rx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](/docs/firewall-and-quality-of-service/queues)。 |
| **rate-limit-burst-threshold-rx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](/docs/firewall-and-quality-of-service/queues)。 |
| **rate-limit-burst-threshold-tx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](/docs/firewall-and-quality-of-service/queues)。 |
| **rate-limit-burst-time-rx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](/docs/firewall-and-quality-of-service/queues)。 |
| **rate-limit-burst-time-tx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](/docs/firewall-and-quality-of-service/queues)。 |
| **rate-limit-burst-tx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](/docs/firewall-and-quality-of-service/queues)。 |
| **rate-limit-min-rx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](/docs/firewall-and-quality-of-service/queues)。 |
| **rate-limit-min-tx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](/docs/firewall-and-quality-of-service/queues)。 |
| **rate-limit-priority** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](/docs/firewall-and-quality-of-service/queues)。 |
| **rate-limit-rx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](/docs/firewall-and-quality-of-service/queues)。 |
| **rate-limit-tx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](/docs/firewall-and-quality-of-service/queues)。 |
| **reset-counters-interval** (*hourly* \| *daily* \| *weekly* \| *monthly* \| *disabled*); Default: **disabled**) | 從 *reset-counters-start-time* 起算的間隔，到期後會清除所有相關的使用者統計資料。 |
| **reset-counters-start-time** (*datetime*; Default: ) | 用來計算 *reset-counters-interval* 的固定日期與時間值。 |
| **transfer-limit** (*integer*; Default: **0**) | 彙總流量（下載+上傳）的總量，單位為 Bytes。 |
| **upload-limit** (*integer*; Default: **0**) | 使用者可上傳的流量總量，單位為 Bytes。 |
| **uptime-limit** (*time*; Default: **00:00:00**) | 使用者可保持作用中的連線時間總量。 |

## Payments

**子選單：** `/user-manager/payment`

本節提供所有已收到付款的資訊。

**唯讀屬性**

| 屬性 | 說明 |
| :-- | :-- |
| **currency** (*string*) | 交易中使用的貨幣。 |
| **method** (*string*) | 用於交易的服務（目前僅 PayPal）。 |
| **price** (*decimal*) | 使用者支付的金額。 |
| **profile** (*profile*) | 使用者購買的 profile 名稱。 |
| **trans-end** (*datetime*) | 交易結束的日期與時間。 |
| **trans-start** (*datetime*) | 交易開始的日期與時間。 |
| **trans-status** (*string*) | 交易狀態。可能的狀態為 *started*、*pending*、*approved*、*declined*、*error*、*timeout*、*aborted*、*user approved*。只有 *approved* 應視為完成的交易。 |
| **user** (*string*; Default: ) | 執行交易的使用者名稱。 |
| **user-message** (*string*; Default: ) |  |

## Profiles

**子選單：** `/user-manager/profile`

### 屬性 {#properties-2}

| 屬性 | 說明 |
| :-- | :-- |
| **comment** (*string*; Default: ) | 項目的簡短說明。 |
| **name** (*string*; Default: ) | profile 的唯一名稱。 |
| **name-for-users** (*string*; Default: ) | 將在 Web 頁面上向使用者顯示的 profile 名稱。 |
| **override-shared-users** (*decimal \| off \| unlimited*; Default: **off**) | 是否允許具有相同使用者名稱的多個工作階段。這會覆蓋 *shared-users* 設定。 |
| **price** (*decimal*; Default: **0.00**) |  |
| **starts-when** (*assigned* \| *first-auth*; Default: **assigned**) | profile 生效的時間。*Assigned*：建立 User Profile 項目時立即生效。*First-auth*：在使用者第一次驗證請求時生效。 |
| **validity** (*time \| unlimited*; Default: **unlimited**) | 使用者可使用此 profile 的總時間。 |

## Profile 限制 {#profile-limitations}

**子選單：** `/user-manager/profile-limitation`

Profile-Limitations 表格將 Limitations 與 Profiles 連結在一起，並定義其有效期間。當多個 Limitations 指派給同一個 Profile 時，使用者必須符合所有 Limitations，工作階段才會建立。這可用於建立更複雜的設定，例如分別設定每月與每日的頻寬限制。

### 屬性 {#properties-3}

| 屬性 | 說明 |
| :-- | :-- |
| **comment** (*string*; Default: ) | 項目的簡短說明。 |
| **from-time** (*time*; Default: **00:00:00**) | 限制開始生效的一天中的時間。 |
| **limitation** (*limitation*; Default: ) | 已建立的 **Limitation** 名稱。 |
| **profile** (*profile*; Default: ) | 已建立的 **Profile** 名稱。 |
| **till-time** (*time*; Default: **23:59:59**) | 限制結束的一天中的時間。 |
| **weekdays** (*day of week*; Default: **Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday**) | 限制生效的星期幾。 |

## Routers

**子選單：** `/user-manager/router`

您可以在此定義可將 User Manager 作為 RADIUS 伺服器使用的 NAS 設備。

### 屬性 {#properties-4}

| 屬性 | 說明 |
| :-- | :-- |
| **coa-port** (*integer:1..65535*; Default: **3799**) | CoA (Change of Authorization) 通訊的埠號。 |
| **address** (*IP/IPv6***;** Default: ) | RADIUS 用戶端的 IP 位址。 |
| **comment** (*string*; Default: ) | NAS 的簡短說明。 |
| **disabled** (*yes \| no*; Default: **no**) | 控制項目目前是否啟用。 |
| **name** (*string*; Default: ) | RADIUS 用戶端的唯一名稱。 |
| **protocol**(*radsec*\| *udp*;Default udp) | 與路由器搭配使用的通訊協定。 |
| **shared-secret** (*string*; Default: ) *[敏感資訊](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 用於保護 RADIUS 伺服器與 RADIUS 用戶端之間的通訊。 |

### 指令 {#commands-1}

| 屬性 | 說明 |
| :-- | :-- |
| **reset-counters** () | 清除特定 RADIUS 用戶端的所有統計資料。 |

## Sessions

**子選單：** `/user-manager/session`

只有在 NAS 啟用 accounting 時，才會記錄工作階段。

**唯讀屬性**

| 屬性 | 說明 |
| :-- | :-- |
| **acct-session-id** (*string*) | accounting 工作階段的唯一識別碼。 |
| **active** (*yes \| no*) | 工作階段目前是否正在使用。 |
| **calling-station-id** (*string*) | 使用者識別碼，通常是 IP 位址或 MAC 位址。 |
| **download** (*Bytes*) | 已下載的流量。 |
| **ended** (*datetime*) | 工作階段關閉的日期與時間。作用中的工作階段為空白。 |
| **last-accounting-packet** (*datetime*) | 收到最後一次 accounting 更新的日期與時間。 |
| **nas-ip-address** (*IP address*) | NAS 的 IP 位址。 |
| **nas-port-id** (*string*) | 正在驗證使用者的 NAS 埠識別碼。 |
| **nas-port-type** (*string*) | 正在驗證使用者的埠類型（*physical* 或 *virtual*）。 |
| **started** (*datetime*) | 工作階段建立的日期與時間。 |
| **status** (*list of statuses*) | 工作階段可能的可用狀態：*start -* 已收到 accounting 訊息 *Start*，*stop -* 已收到 accounting 訊息 *Stop*，*interim - Interim update* 已收到，*close-acked* - 工作階段已成功關閉，*expired.* |
| **terminate-cause** (*string*) | 工作階段關閉的原因。 |
| **upload** (*Bytes*) | 已上傳的流量。 |
| **uptime** (*time*) | 工作階段記錄的總上線時間。 |
| **user** (*string*) | 使用者名稱。 |
| **user-address** (*IP address*) | 提供給使用者的 IP 位址。 |

## 設定 {#settings}

**子選單：** `/user-manager`

**Properties**

| 屬性 | 說明 |
| :-- | :-- |
| **accounting-port** (*integer*; Default: **1813**) | 用來監聽 RADIUS accounting 請求的埠。 |
| **authentication-port**(*integer*; Default: **1812**) | 用來監聽 RADIUS 驗證請求的埠。 |
| ***certificate*** (*certificate*; Default: ) | 用於 EAP TLS 類型驗證方法的憑證。 |
| ***enabled*** (*yes \| no*; Default: **no**) | 是否啟用 User Manager 功能。 |
| **radsec-certificate**(certificate; Default:) | 用於 RadSec 協定的憑證。 |
| **use-profiles**(*yes \| no*; Default: **no**) | 是否使用 **Profiles** 與 **Limitations**。設為 *no* 時，執行 User Manager 只需要 **User** 設定。 |

### Advanced

**子選單：** `/user-manager/advanced`

**Properties**

| 屬性 | 說明 |
| :-- | :-- |
| **paypal-allow** (*yes \| no*; 預設: **no**) | 是否為 User Manager 啟用 PayPal 功能。 |
| **paypal-currency** (*string*; 預設: **USD**) | 與 *price* 設定相關的貨幣，使用者將以此貨幣計費。 |
| **paypal-password** (*string*; 預設: ) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | PayPal API 帳號的密碼。 |
| **paypal-signature** (*string*; 預設: ) | PayPal API 帳號的簽章。 |
| **paypal-use-sandbox** (*yes \| no*; 預設: **no**) | 是否使用 PayPal 的 sandbox 環境進行測試。 |
| **paypal-user** (*string*; 預設: ) | PayPal API 帳號的使用者名稱。 |
| **web-private-password** (*string*; 預設: ) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 透過 HTTP 存取 */um/PRIVATE/* 區段所需的密碼。 |
| **web-private-username** (*string*; 預設: ) | 透過 HTTP 存取 */um/PRIVATE/* 區段所需的使用者名稱。 |

## Users

**子選單:** `/user-manager/user`

### 屬性 {#properties-5}

| 屬性 | 說明 |
| :-- | :-- |
| **attributes** (*array of attributes*; 預設: ) | 自訂的 **Attributes** 與其值，將額外加入 Access-Accept 訊息。 |
| **caller-id**(*string*; 預設: ) | 允許使用者以特定的 *Calling-Station-Id* 值進行驗證。 |
| **comment** (*string*; 預設: ) | 使用者的簡短說明。 |
| **disabled** (*yes \| no*; 預設: **no**) | 控制使用者是否可使用。 |
| **group** (*group*; 預設: **default**) | 使用者所屬 **Group** 的名稱。 |
| **name** (*string*; 預設: ) | 工作階段驗證的使用者名稱。 |
| **otp-secret** (*string*; 預設: ) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 附加在密碼上的一次性密碼權杖。 |
| **password** (*string*; 預設: ) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 使用者用於工作階段驗證的密碼。 |
| **shared-users** (*integer \| unlimited*; 預設: **1**) | 使用者可同時建立的工作階段總數。 |

### 指令 {#commands-2}

| 屬性 | 說明 |
| :-- | :-- |
| **add-batch-users** () | 此指令可根據各種參數產生多個使用者帳號。 |
| **generate-voucher** () | 根據 *voucher-template* 產生檔案，可提供給終端使用者。 |
| **monitor** () | 顯示使用者的總統計資料。統計資料包括 *total-uptime*、*total-download*、*total-upload*、*active-sessions*、*actual-profile*、*attributes-details*。 |

## 使用者群組 {#user-groups}

**子選單:** `/user-manager/user/group`

使用者群組定義多個使用者的共同特性，例如允許的驗證方法與 RADIUS 屬性。User Manager 中已有兩個群組，分別為 *default* 與 *default-anonymous*。

### 屬性 {#properties-6}

| Property | Description |
| :-- | :-- |
| **attributes** (*array of attributes*; Default: ) | 自訂的 **Attributes** 及其值，會額外加入此群組使用者的 Access-Accept 訊息中。 |
| **comment** (*string*; Default: ) | 群組的簡短描述。 |
| **inner-auths** (*list of auths*; Default: ) | 通道式（outer）驗證方法所允許的內部驗證方法清單。支援的內部驗證方法包括 *ttls-pap*、*ttls-chap*、*ttls-mschap1*、*ttls-mschap2*、*peap-mschap2*。 |
| **name** (*string*; Default: ) | 群組的唯一名稱。 |
| **outer-auths** (*list of auths*; Default: ) | 允許的驗證方法清單。支援的外部驗證方法包括 *pap*、*chap*、*mschap1*、*mschap2*、*eap-tls*、*eap-ttls*、*eap-peap*、*eap-mschap2*。 |

## 使用者設定檔 {#user-profiles}

**子選單：** `/user-manager/user-profile`

此選單會為使用者指派 profile，並追蹤 profile 的狀態。單一使用者可以指派多個 profile；不過，同一時間只能使用一個。當目前使用的 profile 到期時，使用者會無縫切換到下一個 profile，而不會中斷使用者的工作階段。

### 屬性 {#properties-7}

| Property | Description |
| :-- | :-- |
| **profile** (*profile*; Default: ) | 要指派給使用者的 profile 名稱。 |
| **user**(*user*; Default: ) | 要使用特定 profile 的使用者名稱。 |

### 唯讀屬性 {#read-only-properties-1}

| 屬性 | 說明 |
| :-- | :-- |
| **end-time** (*datetime*) | **User Profile** 將失效的日期與時間。 |
| **state** (*running active* \| running \| *used*) | **User Profile** 的目前狀態。*Running active*：使用者目前正在使用的設定檔。*Running*：已準備好可供使用的設定檔。*Used*：已過期且無法再啟用的設定檔。 |

### 指令 {#commands-3}

| 屬性 | 說明 |
| :-- | :-- |
| **activate-user-profile** () | 立即讓 **User Profile** 項目生效。 |

## WEB 介面 {#web-interface}

每位使用者都可以透過 WEB 介面存取其個人設定檔。只要在路由器 IP 或網域加上「/um/」目錄，即可存取 WEB 介面，例如 `http://example.com/um/`。請注意，WEB 介面會受到 IP Services「www」與「www-ssl」影響。WEB 介面可以使用 CSS、JavaScript 與 HTML 自訂。

### 可自訂檔案參考 {#customizable-file-reference}

| 檔案 | 說明 |
| :-- | :-- |
| **css/login.css** | 用於登入提示頁面的階層式樣式表檔案。 |
| **css/user.css** | 用於使用者設定檔頁面的階層式樣式表檔案。 |
| **img/PayPal\_mark\_37x23.gif** | PayPal 標誌圖片。 |
| **img/ajax-loader.gif** | 處理頁面切換時顯示的載入 gif。 |
| **img/mikrotik\_logo.png** | 顯示於所有頁面的 MikroTik 標誌。 |
| **js/generic.js** | 用於所有頁面的 Javascript 檔案。 |
| **js/login.js** | 用於登入提示頁面的 Javascript 檔案。 |
| **js/user.js** | 用於使用者設定檔頁面的 Javascript 檔案。 |
| **user/login\_dynamic.html** | 登入提示頁面的版面配置。 |
| **user/user\_dynamic.html** | 使用者設定檔頁面的版面配置。 |

## 應用程式指南 {#application-guides}

### 批次建立使用者 {#batch-user-creation}

可以建立多個新使用者，並隨機產生使用者名稱與密碼。例如，下列指令會產生 3 個新使用者，使用者名稱為 6 個小寫符號，密碼則由 6 個小寫字母、大寫字母與數字組成。

```ros
/user-manager/user
add-batch-users number-of-users=3 password-characters=lowercase,numbers,uppercase password-length=6 username-characters=lowercase username-length=6
```

指令所產生的使用者可以透過列印使用者表來查看：

```ros
/user-manager/user/print 
Flags: X - disabled 
 0   name="olsgkl" password="86a6zH" otp-secret="" group=default shared-users=1 attributes="" 

 1   name="lkbwss" password="jaKY5V" otp-secret="" group=default shared-users=1 attributes="" 

 2   name="cwxbwu" password="a62yZd" otp-secret="" group=default shared-users=1 attributes="" 

```

### 為 NAS 提供自訂 RADIUS 屬性 {#providing-nas-with-custom-radius-attributes}

可以在驗證程序中傳送額外的 RADIUS 屬性，以提供 NAS 關於工作階段的自訂資訊，例如應指派給 supplicant 的 IP 位址，或用於位址指派的位址集區。

#### 使用者的靜態 IP 位址 {#static-ip-address-for-a-user}

若要指派終端使用者一個靜態 IP 位址，可以使用 *Framed-IP-Address* 屬性。使用靜態 IP 位址指派時，*shared-sessions* 必須設為 1，以避免使用者同時有多個工作階段，但只有一個 IP 位址的情況。例如：

```ros
/user-manager/user
set [find name=username] shared-users=1 attributes=Framed-IP-Address:192.168.1.4
```

#### 為一組使用者指定位址集區 {#specifying-address-pool-for-a-group-of-users}

我們可以將多個相似使用者分組，並一次指派 RADIUS 屬性給所有成員。首先，建立新群組：

```ros
/user-manager/user/group
add name=location1 outer-auths=chap,eap-mschap2,eap-peap,eap-tls,eap-ttls,mschap1,mschap2,pap \
inner-auths=peap-mschap2,ttls-chap,ttls-mschap1,ttls-mschap2,ttls-pap attributes=Framed-Pool:pool1
```

下一步是將使用者指派至群組：

```ros
/user-manager/user
 set [find name=username] group=location1
```

在此情況下，使用者驗證時會從 *pool1* 指派一個 IP 位址，請確認 *pool1* 已在 NAS 設備上建立。

### 使用 TOTP（time-based one-time password）進行使用者驗證 {#using-totp-time-based-one-time-password-for-user-authentication}

User Manager 支援在使用者密碼欄位中加入以時間為基礎的驗證權杖，該權杖每 30 秒重新產生一次。

:::danger
OTP 依賴時鐘，因此請確認時間設定正確。
:::

TOTP 的運作方式是在 supplicant（用戶端）與驗證伺服器（User Manager）上保有共用秘密。若要在 RouterOS 上設定 TOTP，只要為使用者設定 *otp-secret* 即可。例如：

```ros
/user-manager/user
set [find name=username] password=mypass otp-secret=mysecret

```

若要在 supplicant 端計算 TOTP 權杖，可使用許多常見應用程式，例如 Google Authenticator 或 [https://totp.app/](https://totp.app/)。將 mysecret 加入 TOTP 權杖產生器後，會產生一組新的唯一 6 位數代碼，必須將其附加在使用者密碼中。

![](/img/41241175d691e7c4.webp)

下列範例會接受使用者的驗證，方法是將計算出的 TOTP 權杖附加至一般密碼，直到產生新的 TOTP 權杖為止。

```text
User-Name=username
User-Password=mypass620872
```

### 匯出使用者憑證 {#exporting-user-credentials}

#### **單一使用者可列印的登入憑證** {#printable-login-credentials-for-a-single-user}

若要產生單一使用者可列印的憑證卡，只需使用 *generate-voucher* 指令。指定使用者的 RouterOS ID 編號，或使用 *find* 指令指定使用者名稱。User Manager 安裝時已包含一個範本，可在設備的「檔案」區段中取得。你可以依需求自訂範本。

```ros
/user-manager/user
generate-voucher voucher-template=printable_vouchers.html [find where name=username]
```

產生的憑證卡可透過 WEB 瀏覽器存取路由器，並瀏覽至 */um/PRIVATE/GENERATED/vouchers/gen\_printable\_vouchers.html* 來取得。

預設情況下，可列印卡片如下所示：

![](/img/f77afb5d13302de9.webp)

:::warning
若要透過 WEB 瀏覽器存取 /um/ 目錄的 PRIVATE 路徑，必須設定 *private-username* 與 *private-password*。請參閱 **Settings** 區段。
:::

產生憑證時可以使用不同的變數。目前支援的變數如下：

$(username) - 代表 User Manager 使用者名稱  
$(password) - 該使用者名稱的密碼  
$(userprofname) - 特定使用者目前生效的設定檔  
$(userprofendtime) - 若有指定，表示設定檔的有效期限結束時間

#### 多位使用者憑證匯出 {#multiple-user-credential-export}

可以使用 *export.xml* 或 *export.csv* 作為 *voucher-template*，一次產生包含多位或所有使用者憑證的 CSV 或 XML 檔案。

```ros
/user-manager/user
generate-voucher voucher-template=export.xml [find]
```

此命令會產生 XML 檔案 *um5files/PRIVATE/GENERATED/vouchers/gen\_export.xml*，可透過 WEB 瀏覽器或任何其他檔案存取工具存取。

```text
<?xml version="1.0" encoding="UTF-8"?>
<users>
    <user>
        <username>olsgkl</username>
        <password>86a6zH</password>
    </user>
    <user>
        <username>lkbwss</username>
        <password>jaKY5V</password>
    </user>
    <user>
        <username>cwxbwu</username>
        <password>a62yZd</password>
    </user>
    <user>
        <username>username</username>
        <password>secretpassword</password>
    </user>

</users>
```

### 產生使用量報表 {#generating-usage-report}

當公司的帳務或法務團隊需要可呈現的網路使用資訊時，可以使用 *generate-report* 命令建立自動化工作階段匯出。此命令需要輸入報表範本，範本範例可在 *um5files/PRIVATE/TEMPLATES/reports/report\_default.html* 取得。報表產生範例：

```ros
/user-manager
generate-report report-template=report_default.html columns=username,uptime,download,upload
```

產生的報表可透過 WEB 瀏覽器存取路由器，並瀏覽至 */um/PRIVATE/GENERATED/reports/gen\_report\_default.html* 取得。

*![](/img/1a6f9e70c884c21f.webp)*

### 購買設定檔 {#purchasing-a-profile}

使用 WEB 瀏覽器存取路由器的 */um/* 目錄（例如 http://example.com/um/）登入使用者的私人設定檔後，即可在對應選單中看到所有可用的 **Profiles**。已指定 *price* 值的設定檔會提供 *Buy this Profile* 按鈕。

![](/img/a947415d24d11d74.webp)

按下 *Buy this Profile* 按鈕後，系統會要求使用者從可用的交易服務提供者中選擇（目前僅提供 PayPal），接著重新導向至 PayPal 的付款處理頁面。

![](/img/368b0af05bc7f389.webp)

付款完成後，User Manager 會要求 PayPal 核准交易。核准後，設定檔會指派給使用者並可立即使用。![](/img/39c330686cc9db0e.webp)

### 從 RouterOS v6 遷移 {#migrating-from-routeros-v6}

當你將 User Manager 路由器從 RouterOS v6 升級至 v7 時，新的 User Manager 會使用新的資料庫檔案與設定。若要繼續使用舊的使用者、路由器、設定檔等設定，你必須手動執行 migrate 指令。為此，你必須具備舊 User Manager 伺服器資料夾 "user-manager" 中的檔案。該資料夾可以重新命名，但舊安裝中的所有內容都必須轉移至新的 v7 安裝（你可以將舊設定從一部路由器移至另一部搭載 v7 的路由器，但必須複製 "user-manager" 資料夾）。之後，你只需執行此指令：`/user-manager/database/migrate-legacy-db database-path=<path_to_old_user_manager_folder>`。

匯入程序會嘗試轉換這類設定：使用者、設定檔、使用者設定檔、限制、設定檔限制、使用者計數器、路由器與工作階段。

## 應用程式範例 {#application-examples}

### 使用 User Manager 驗證的基本 L2TP/IPsec 伺服器 {#basic-l2tpipsec-server-with-user-manager-authentication}

![](/img/5cb98b1471afb086.webp)

#### User Manager 設定 {#user-manager-configuration}

先啟用 User Manager 功能。

```ros
/user-manager
set enabled=yes
```

允許接收來自 localhost 的 RADIUS 要求（路由器本身）。

```ros
/user-manager/router
add address=127.0.0.1 comment=localhost name=local shared-secret=test
```

接著，新增使用者及其憑證，供用戶端用來向伺服器進行驗證。

```ros
/user-manager/user
add name=user1 password=password
```

#### 設定 RADIUS 用戶端 {#configuring-radius-client}

若要讓路由器使用 RADIUS 伺服器進行使用者驗證，必須新增一個 RADIUS 用戶端，且其 shared secret 與我們已在 User Manager 中設定的相同。

```ros
/radius
add address=127.0.0.1 secret=test service=ipsec
```

#### L2TP/IPsec 伺服器設定 {#l2tpipsec-server-configuration}

設定要指派給使用者的 IP 位址所使用的 IP pool，並將其指派給 PPP Profile。

```ros
/ip/pool
add name=vpn-pool range=192.168.99.2-192.168.99.100

/ppp/profile
set default-encryption local-address=192.168.99.1 remote-address=vpn-pool
```

啟用 RADIUS 用於 PPP 驗證。

```ros
/ppp/aaa
set use-radius=yes
```

啟用具備 IPsec 加密的 L2TP 伺服器。

```ros
/interface/l2tp-server/server
set enabled=yes use-ipsec=required ipsec-secret=mySecret
```

就這樣。您的路由器現在已準備好接受 L2TP/IPsec 連線，並向內部 User Manager 進行驗證。

### RouterOS 使用者登入的雙因素驗證（MFA/2FA） {#two-factor-authentication-for-routeros-user-login-mfa2fa}

由於 User-Manager 支援 TOTP（time-based-one-time password），因此可以設定所謂的 MFA 驗證，用於不同服務。在這裡，我們將探討透過 User Manager（radius）搭配每 30 秒變更一次的時間型密碼，進行 RouterOS 使用者驗證。

**以下是您的 MikroTik 路由器上必要的設定選項。**

啟用 RADIUS 用於 `/user` 選單，並從 `/user/group` 選單設定 default-group。請記住，系統會先檢查本機 `/user` 資料庫，然後才連絡 RADIUS。

```
/user/aaa/set use-radius=yes default-group=full
```

為登入服務啟用 radius 用戶端。由於我們在同一台路由器上執行 User Manager，因此使用 127.0.0.1，

```
/radius/add address=127.0.0.1 service=login secret=mystrongsecret
```

**以下是 User Manager 的設定步驟**，

請確認你已將受管理設備新增至「Routers」選單，

```
/user-manager/router/add name=myrouter address=127.0.0.1 shared-secret=mystrongsecret
```

在 User-Manager 使用者表中新增一位使用者，並設定 OTP secret 參數。正確設定 OTP 還需要幾個步驟。  
挑選一個 OTP-secret 名稱，並將其轉換為 base32 格式（有許多線上工具可將 utf-8 轉換為 base32 格式）。在我的設定中，我使用「mysupersecret」，其 base32 結果為 NV4XG5LQMVZHGZLDOJSXI===

```
/user-manager/user/add name=mikrotik password=mysuperpassword otp-secret="NV4XG5LQMVZHGZLDOJSXI==="
```

請注意，在你慣用的驗證器應用程式中，新增時間密碼實例時，需要為該使用者手動設定此金鑰「NV4XG5LQMVZHGZLDOJSXI===」。

若要登入 MikroTik 設備，請開啟 Winbox/Console 並連線至路由器位址，然後使用 login:mikrotik 與 password:mysuperpasswordxxxxxx，其中 xxxxxx 是你慣用驗證應用程式產生的 6 位數代碼。

密碼每 30 秒變更一次，並可在你慣用的應用程式中取得。

![](/img/73454df958b000d2.jpg)
