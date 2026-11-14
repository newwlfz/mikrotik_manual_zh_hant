---
sidebar_key: "authentication-authorization-accounting/user-manager"
sidebar_position: 6
title: "使用者管理器"
sidebar_label: "使用者管理器"
description: "RouterOS 中的 User Manager 為 DHCP、Hotspot 和 PPP 等服務提供集中式 RADIUS 認證與授權，並支援多種認證方式。它包含可自定義的 RADIUS 屬性，用於隧道配置和會話管理，且許可會影響活動會話數量。"
tags:
  - 'radius'
  - 'authentication'
  - 'authorization'
source: https://manual.mikrotik.com/docs/7.25/authentication-authorization-accounting/user-manager
captured_at: '2026-11-04T11:14:31+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#overview}

User Manager 是 RouterOS 中的一種 RADIUS 伺服器實現，可為特定服務提供集中的使用者認證和授權。擁有中央使用者資料庫可以更好地跟蹤系統使用者和客戶。作為一個單獨的軟體包，User Manager 除 SMIPS 外可在所有架構上使用；但是，由於可用空間有限，必須謹慎操作。它支援多種不同的認證方法，包括 PAP、CHAP、MS-CHAP、MS-CHAPv2、EAP-TLS、EAP-TTLS 和 EAP-PEAP。在 RouterOS 中，DHCP、Dot1x、Hotspot、IPsec、PPP 和 Wireless 是從 User Manager 中受益最多的功能。每個使用者都可以使用 WEB 介面檢視其賬戶統計資訊並管理可用的配置檔案。此外，使用者可以使用最流行的支付閘道器 PayPal 購買自己的資料套餐（配置檔案），這使其成為服務提供商的理想系統。可以生成自定義報告，以簡化計費部門的處理工作。User Manager 按照 [RFC2865](https://tools.ietf.org/html/rfc2865) 和 [RFC3579](https://tools.ietf.org/html/rfc3579) 中定義的 RADIUS 標準工作。

User Manager 是受 RouterOS 許可證級別限制的 RouterOS 功能之一。根據[許可證級別](../getting-started/routeros-licensing/x86/index.md#routeros-license-key-levels)，活動會話的數量將受到限制，包括每個使用者的多重連線（而非唯一賬戶）。

![](/img/074aaadffaa40983.webp)

## 屬性 {#attributes}

**子選單：** `/user-manager/attribute`

RADIUS 屬性是定義授權、資訊和配置的引數，在 RADIUS 伺服器和用戶端之間傳遞。User Manager 允許傳送在 "attributes" 選單中定義的自定義屬性。RouterOS 已經提供了一組預定義屬性，但如有必要也可以新增其他屬性。預定義屬性：

| 屬性 | 供應商 ID | 型別 ID | 值型別 | 封包型別 | 描述 |
| :-- | :-- | --: | :-- | :-- | :-- |
| Framed-IP-Address | 0 (標準) | 8 | IP 地址 | Access-Accept | <a href="https://tools.ietf.org/html/rfc2865#section-5.8" target="_blank" rel="noopener noreferrer">RFC2865 第 5.8 節</a> |
| Framed-IP-Netmask | 0 (標準) | 9 | <code>/ip/address</code> | Access-Accept | <a href="https://tools.ietf.org/html/rfc2865#section-5.9" target="_blank" rel="noopener noreferrer">RFC2865 第 5.9 節</a> |
| Session-Timeout | 0 (標準) | 27 | 整數（最大值：21474720） | Access-Accept, Access-Challenge | <a href="https://tools.ietf.org/html/rfc2865#section-5.27" target="_blank" rel="noopener noreferrer">RFC2865 第 5.27 節</a> |
| Idle-Timeout | 0 (標準) | 28 | 整數 | Access-Accept, Access-Challenge | <a href="https://tools.ietf.org/html/rfc2865#section-5.28" target="_blank" rel="noopener noreferrer">RFC2865 第 5.28 節</a> |
| Tunnel-Type | 0 (標準) | 64 |  | 值 | 描述 |
| 值 | 描述 |  |  |  |  |
| 1 | 點對點隧道協定 (PPTP) |  |  |  |  |
| 2 | 第二層轉發 (L2F) |  |  |  |  |
| 3 | 第二層隧道協定 (L2TP) |  |  |  |  |
| 4 | Ascend 隧道管理協定 (ATMP) |  |  |  |  |
| 5 | 虛擬隧道協定 (VTP) |  |  |  |  |
| 6 | 隧道模式下的 IP 認證頭 (AH) |  |  |  |  |
| 7 | IP-in-IP 封裝 (IP-IP) |  |  |  |  |
| 8 | 最小 IP-in-IP 封裝 (MIN-IP-IP) |  |  |  |  |
| 9 | 隧道模式下的 IP 封裝安全載荷 (ESP) |  |  |  |  |
| 10 | 通用路由封裝 (GRE) |  |  |  |  |
| 11 | Bay 撥號虛擬服務 (DVS) |  |  |  |  |
| 12 | IP-in-IP 隧道 |  |  |  |  |
| 13 | 虛擬區域網路 |  |  |  |  |
| Tunnel-Medium-Type | 0 (標準) | 65 |  | 值 | 描述 |
| 值 | 描述 |  |  |  |  |
| 1 | IPv4 (IP 版本 4) |  |  |  |  |
| 2 | IPv6 (IP 版本 6) |  |  |  |  |
| 3 | NSAP |  |  |  |  |
| 4 | HDLC (8 位多點) |  |  |  |  |
| 5 | BBN 1822 |  |  |  |  |
| 6 | 802 (包括所有 802 介質以及 Ethernet "canonical format") |  |  |  |  |
| 7 | E.163 (POTS) |  |  |  |  |
| 8 | E.164 (SMDS、幀中繼、ATM) |  |  |  |  |
| 9 | F.69 (Telex) |  |  |  |  |
| 10 | X.121 (X.25, Frame Relay) |  |  |  |  |
| 11 | IPX |  |  |  |  |
| 12 | Appletalk |  |  |  |  |
| 13 | Decnet IV |  |  |  |  |
| 14 | Banyan Vines |  |  |  |  |
| 15 | 帶 NSAP 格式子地址的 E.164 |  |  |  |  |
| Tunnel-Private-Group-ID | 0 (標準) | 81 | 字串 | Access-Accept | <a href="https://tools.ietf.org/html/rfc2868#section-3.6" target="_blank" rel="noopener noreferrer">RFC2868 第 3.6 節</a> |
| Framed-Pool | 0 (標準) | 88 | 字串 | Access-Accept | <a href="https://tools.ietf.org/html/rfc2869#section-5.18" target="_blank" rel="noopener noreferrer">RFC2869 第 5.18 節</a> |
| Framed-IPv6-Prefix | 0 (標準) | 97 | IPv6 字首 | Access-Accept | <a href="https://tools.ietf.org/html/rfc3162#section-2.3" target="_blank" rel="noopener noreferrer">RFC3162 第 2.3 節</a> |
| Framed-IPv6-Pool | 0 (標準) | 100 | 字串 | Access-Accept | <a href="https://tools.ietf.org/html/rfc3162#section-2.6" target="_blank" rel="noopener noreferrer">RFC3162 第 2.6 節</a> |
| Delegated-IPv6-Prefix | 0 (標準) | 123 | IPv6 字首 | Access-Accept | <a href="https://tools.ietf.org/html/rfc4818" target="_blank" rel="noopener noreferrer">RFC4818</a> |
| Framed-IPv6-Address | 0 (標準) | 168 | IP 地址 | Access-Accept | <a href="https://tools.ietf.org/html/rfc6911#section-3.1" target="_blank" rel="noopener noreferrer">RFC6911 第 3.1 節</a> |
| Mikrotik-Recv-Limit | 14988 (Mikrotik) | 1 | 整數 | Access-Accept | 用戶端的接收總限制，單位為位元組。 |
| Mikrotik-Xmit-Limit | 14988 (Mikrotik) | 2 | 整數 | Access-Accept | 用戶端的傳送總限制，單位為位元組。 |
| Mikrotik-Group | 14988 (Mikrotik) | 3 | 字串 | Access-Accept | 本地使用者的使用者組。 <br/> HotSpot 使用者的 HotSpot profile。 <br/> PPP 使用者的 PPP profile。 |
| Mikrotik-Wireless-Forward | 14988 (Mikrotik) | 4 | 整數 | Access-Accept | 如果此屬性設定為 "0"，則不會將用戶端的幀轉發回無線基礎設施（僅限無線）。 |
| Mikrotik-Wireless-Skip-Dot1x | 14988 (Mikrotik) | 5 | 整數 | Access-Accept | 如果設定為非零值，則對特定無線用戶端停用 802.1x 認證（僅限無線）。 |
| Mikrotik-Wireless-Enc-Algo | 14988 (Mikrotik) | 6 |  | 值 | 描述 |
| 值 | 描述 |  |  |  |  |
| 0 | No-encryption |  |  |  |  |
| 1 | 40-bit-WEP |  |  |  |  |
| 2 | 104-bit-WEP |  |  |  |  |
| 3 | AES-CCM |  |  |  |  |
| 4 | TKIP |  |  |  |  |
| Mikrotik-Wireless-Enc-Key | 14988 (Mikrotik) | 7 | 字串 | Access-Accept | 用戶端的 WEP 加密金鑰（僅限無線）。 |
| Mikrotik-Rate-Limit | 14988 (Mikrotik) | 8 | 字串 | Access-Accept | 用戶端的速率限制。格式為：rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]，從路由器的角度（因此 "rx" 是用戶端上傳，"tx" 是用戶端下載）。所有速率應為數字，可選帶 'k'（1,000s）或 'M'（1,000,000s）。如果未指定 tx-rate，則 rx-rate 也用作 tx-rate。tx-burst-rate、tx-burst-threshold 和 tx-burst-time 同理。如果 rx-burst-threshold 和 tx-burst-threshold 均未指定（但指定了 burst-rate），則 rx-rate 和 tx-rate 用作突發閾值。如果 rx-burst-time 和 tx-burst-time 均未指定，則預設使用 1s。Priority 取值為 1..8，其中 1 表示最高優先順序，8 表示最低優先順序。如果未指定 rx-rate-min 和 tx-rate-min，則使用 rx-rate 和 tx-rate 值。rx-rate-min 和 tx-rate-min 的值不能超過 rx-rate 和 tx-rate 的值。 |
| Mikrotik-Realm | 14988 (Mikrotik) | 9 | 字串 | Access-Request | 如果在 /radius 選單中設定，它會作為 Mikrotik-Realm 屬性包含在每個 RADIUS 請求中。如果未設定，則傳送與 MS-CHAP-Domain 屬性相同的值（如果缺少 MS-CHAP-Domain，則也不包含 Realm）。 |
| Mikrotik-Host-IP | 14988 (Mikrotik) | 10 | IP 地址 | Access-Request | Universal Client 轉換前 HotSpot 用戶端的 IP 地址（用戶端的原始 IP 地址）。 |
| Mikrotik-Mark-Id | 14988 (Mikrotik) | 11 | 字串 | Access-Accept | 防火牆 mangle 鏈名稱（僅限 HotSpot）。MikroTik RADIUS 用戶端收到此屬性後，會建立一個動態防火牆 mangle 規則，其 action=jump、chain=hotspot，且 jump-target 等於該屬性值。Mangle 鏈名稱可以帶有後綴 .in 或 .out，這樣規則將僅針對傳入或傳出流量安裝。可以提供多個 Mark-id 屬性，但僅使用傳入和傳出的最後一個。 |
| Mikrotik-Advertise-URL | 14988 (Mikrotik) | 12 | 字串 | Access-Accept | 應向用戶端顯示的廣告頁面的 URL。如果指定了此屬性，則會自動啟用廣告，包括透明代理，即使在相應的使用者 profile 中已顯式停用。RADIUS 伺服器可以傳送多個屬性例項，以指定額外的 URL，這些 URL 會以輪詢方式選擇。 |
| Mikrotik-Advertise-Interval | 14988 (Mikrotik) | 13 | 整數 | Access-Accept | 兩個相鄰廣告之間的時間間隔。RADIUS 伺服器可以傳送多個屬性例項，以指定額外的時間間隔。所有間隔值被視為一個列表，並在每次成功廣告時逐個取用。如果到達列表末尾，則繼續使用最後一個值。 |
| Mikrotik-Recv-Limit-Gigawords | 14988 (Mikrotik) | 14 | 整數 | Access-Accept | 接收總限制的 4G (2^32) 位元組部分（位 32..63，其中位 0..31 在 Mikrotik-Recv-Limit 中傳遞）。 |
| Mikrotik-Xmit-Limit-Gigawords | 14988 (Mikrotik) | 15 | 整數 | Access-Accept | 傳送總限制的 4G (2^32) 位元組部分（位 32..63，其中位 0..31 在 Mikrotik-Xmit-Limit 中傳遞）。 |
| Mikrotik-Wireless-PSK | 14988 (Mikrotik) | 16 | 字串 | Access-Accept |  |
| Mikrotik-Total-Limit | 14988 (Mikrotik) | 17 | 整數 | Access-Accept |  |
| Mikrotik-Total-Limit-Gigawords | 14988 (Mikrotik) | 18 | 整數 | Access-Accept |  |
| Mikrotik-Address-List | 14988 (Mikrotik) | 19 | 字串 | Access-Accept |  |
| Mikrotik-Wireless-MPKey | 14988 (Mikrotik) | 20 | 字串 | Access-Accept |  |
| Mikrotik-Wireless-Comment | 14988 (Mikrotik) | 21 | 字串 | Access-Accept |  |
| Mikrotik-Delegated-IPv6-Pool | 14988 (Mikrotik) | 22 | 字串 | Access-Accept | 用於字首委派的 IPv6 池。 |
| Mikrotik-DHCP-Option-Set | 14988 (Mikrotik) | 23 | 字串 | Access-Accept |  |
| Mikrotik-DHCP-Option-Param-STR1 | 14988 (Mikrotik) | 24 | 字串 | Access-Accept |  |
| Mikrotik-DHCP-Option-Param-STR2 | 14988 (Mikrotik) | 25 | 字串 | Access-Accept |  |
| Mikrotik-Wireless-VLANID | 14988 (Mikrotik) | 26 | 整數 | Access-Accept | 用戶端的 VLAN ID（僅限無線）。 |
| Mikrotik-Wireless-VLANIDtype | 14988 (Mikrotik) | 27 |  | 值 | 描述 |
| 值 | 描述 |  |  |  |  |
| 0 | 802.1q |  |  |  |  |
| 1 | 802.1ad |  |  |  |  |
| Mikrotik-Wireless-Minsignal | 14988 (Mikrotik) | 28 | 字串 | Access-Accept |  |
| Mikrotik-Wireless-Maxsignal | 14988 (Mikrotik) | 29 | 字串 | Access-Accept |  |
| Mikrotik-Switching-Filter | 14988 (Mikrotik) | 30 | 字串 | Access-Accept | 允許在使用 dot1x 伺服器認證用戶端時建立動態交換規則。 |

**屬性**

| 屬性 | 描述 |
| :-- | :-- |
| **name** (*string*; 預設： ) | 屬性的名稱。 |
| **packet-types** (*string*; 預設：**access-accept**) | access-accept - 在 RADIUS Access-Accept 訊息中使用此屬性；access-challenge - 在 RADIUS Access-Challenge 訊息中使用此屬性 |
| **type-id** (*integer:1..255*; 預設： ) | 來自特定廠商屬性資料庫的屬性標識號。 |
| **value-type** (*string*; 預設： ) | hexip-address - IPv4 或 IPv6 IP 地址；ip6-prefix - IPv6 字首；macro；string；uint32 |
| **vendor-id** (*integer*; 預設：**0**) | IANA 分配的特定企業標識號。 |

## 資料庫 {#database}

**子選單：** `/user-manager/database`

所有與 RADIUS 相關的資訊都儲存在單獨的 User Manager 資料庫中，可在 "database" 子選單下配置。"Enabled" 和 "db-path" 是唯一不儲存在 User Manager 資料庫中，而是儲存在 RouterOS 主配置表中的引數，這意味著這些引數會受到 RouterOS 配置重設的影響。其餘配置、會話和支付資料儲存在裝置 FLASH 儲存上的單獨 SQLite 資料庫中。對資料庫執行任何操作時，建議在操作前後進行備份。

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **db-path** (*string*; 預設： ) | 儲存資料庫檔案的位置路徑。 |

### 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **db-size** | 資料庫的當前大小。 |
| **free-disk-space** | 儲存資料庫所在磁碟上的剩餘空間。 |

### 命令 {#commands}

| 屬性 | 描述 |
| :-- | :-- |
| **load** (*name*) | 恢復之前建立的 .umb 格式備份檔案。 |
| **migrate-legacy-db** (*database-path; overwrite*) | 將舊的 User Manager（來自 RouterOS v6 或更早版本）轉換為新標準。可以覆蓋當前資料庫。 |
| **optimize-db** () |  |
| **save** (name; overwrite) | 儲存 User Manager 資料庫的當前狀態。 |

## 限制 {#limitations}

**子選單：** `/user-manager/limitation`

Limitations 由 Profiles 使用，並透過 Profile-Limitations 關聯在一起。必須啟用 RADIUS 計費和 Interim 更新，以便在多個限制項之間無縫切換，或在達到 *download-limit*、*upload-limit* 或 *uptime-limit* 時斷開活動會話。

要從 User Manager 斷開已經處於活動狀態的會話，必須在 RADIUS 用戶端一側將 *accept* 設定為 *yes*。如果併發會話限制並非無限制（shared-users），且已達到允許的最大數量，則路由器將嘗試先斷開較舊的使用者會話。

User-Manager 會嘗試在新使用者被接受之前斷開活動會話（當設定了相應限制時）。因此，在此類設定中，建議將 `/radius/client/timeout` 設定為 1s。

:::danger
RouterOS 中的 IPsec 服務不支援速率限制。

:::

## 屬性 {#properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*; 預設： ) | 限制項的簡短描述。 |
| **download-limit** (*integer*; 預設：**0**) | 使用者可下載的總流量，單位為位元組。 |
| **name** (*string*; 預設： ) | 限制項的唯一名稱。 |
| **rate-limit-burst-rx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-burst-threshold-rx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-burst-threshold-tx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-burst-time-rx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-burst-time-tx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-burst-tx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-min-rx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-min-tx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-priority** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-rx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-tx** () | *MT-Rate-Limit* RADIUS 屬性的一部分。請參閱 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **reset-counters-interval** (*hourly* \| *daily* \| *weekly* \| *monthly* \| *disabled*); 預設：**disabled**) | 從 *reset-counters-start-time* 開始計算的時間間隔，到達後清除所有關聯的使用者統計資訊。 |
| **reset-counters-start-time** (*datetime*; 預設： ) | 用於計算 *reset-counters-interval* 的靜態日期和時間值。 |
| **transfer-limit** (*integer*; 預設：**0**) | 聚合（下載+上傳）的總流量，單位為位元組。 |
| **upload-limit** (*integer*; 預設：**0**) | 使用者可上傳的總流量，單位為位元組。 |
| **uptime-limit** (*time*; 預設：**00:00:00**) | 使用者可持續活動的總線上時長。 |

## 支付 {#payments}

**子選單：** `/user-manager/payment`

本節提供所有已收到付款的資訊。

**只讀屬性**

| 屬性 | 描述 |
| :-- | :-- |
| **currency** (*string*) | 交易使用的貨幣。 |
| **method** (*string*) | 交易使用的服務（目前僅支援 PayPal）。 |
| **price** (*decimal*) | 使用者支付的金額。 |
| **profile** (*profile*) | 使用者購買的配置檔名稱。 |
| **trans-end** (*datetime*) | 交易結束的日期和時間。 |
| **trans-start** (*datetime*) | 交易開始的日期和時間。 |
| **trans-status** (*string*) | 交易狀態。可能的狀態 - *started*、*pending*、*approved*、*declined*、*error*、*timeout*、*aborted*、*user approved*。只有 *approved* 才應被視為完整交易。 |
| **user** (*string*; 預設： ) | 執行交易的使用者名稱。 |
| **user-message** (*string*; 預設： ) |  |

## 配置檔案 {#profiles}

**子選單：** `/user-manager/profile`

### 屬性 {#properties-2}

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*; 預設： ) | 條目的簡短描述。 |
| **name** (*string*; 預設： ) | 配置檔案的唯一名稱。 |
| **name-for-users** (*string*; 預設： ) | 在網頁上向用戶顯示的配置檔名稱。 |
| **override-shared-users** (*decimal \| off \| unlimited*; 預設：**off**) | 是否允許同一使用者名稱建立多個會話。此項會覆蓋 *shared-users* 設定。 |
| **price** (*decimal*; 預設：**0.00**) |  |
| **starts-when** (*assigned* \| *first-auth*; 預設：**assigned**) | 配置檔案變為活動狀態的時間。*Assigned* - 建立 User Profile 條目時立即生效。*First-auth* - 在使用者首次認證請求時生效。 |
| **validity** (*time \| unlimited*; 預設：**unlimited**) | 使用者可使用此配置檔案的總時長。 |

## 配置檔案限制 {#profile-limitations}

**子選單：** `/user-manager/profile-limitation`

Profile-Limitations 表將限制項和配置檔案關聯在一起，並定義其有效期。當多個限制項分配給同一配置檔案時，使用者必須遵守所有限制項才能建立會話。這樣可以建立更復雜的設定，例如單獨的每月和每日頻寬限制。

### 屬性 {#properties-3}

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*; 預設： ) | 條目的簡短描述。 |
| **from-time** (*time*; 預設：**00:00:00**) | 限制項應開始的一天中的時間。 |
| **limitation** (*limitation*; 預設： ) | 已建立的 **Limitation** 的名稱。 |
| **profile** (*profile*; 預設： ) | 已建立的 **Profile** 的名稱。 |
| **till-time** (*time*; 預設：**23:59:59**) | 限制項應結束的一天中的時間。 |
| **weekdays** (*day of week*; 預設：**Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday**) | 限制項應在一週中生效的日期。 |

## 路由器 {#routers}

**子選單：** `/user-manager/router`

在此可以定義可將 User Manager 用作 RADIUS 伺服器的 NAS 裝置。

### 屬性 {#properties-4}

| 屬性 | 描述 |
| :-- | :-- |
| **coa-port** (*integer:1..65535*; 預設：**3799**) | CoA（授權變更）通訊的埠號。 |
| **address** (*IP/IPv6***;** 預設： ) | RADIUS 用戶端的 IP 地址。 |
| **comment** (*string*; 預設： ) | NAS 的簡短描述。 |
| **disabled** (*yes \| no*; 預設：**no**) | 控制該條目當前是否啟用。 |
| **name** (*string*; 預設： ) | RADIUS 用戶端的唯一名稱。 |
| **protocol**(*radsec*\| *udp*;預設 udp) | 與路由器一起使用的協定。 |
| **shared-secret** (*string*; 預設： ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於保護 RADIUS 伺服器與 RADIUS 用戶端之間的通訊。 |

### 命令 {#commands-1}

| 屬性 | 描述 |
| :-- | :-- |
| **reset-counters** () | 清除特定 RADIUS 用戶端的所有統計資訊。 |

## 會話 {#sessions}

**子選單：** `/user-manager/session`

僅當 NAS 上啟用了計費時，才會記錄會話。

**只讀屬性**

| 屬性 | 描述 |
| :-- | :-- |
| **acct-session-id** (*string*) | 計費會話的唯一標識。 |
| **active** (*yes \| no*) | 該會話當前是否正在使用。 |
| **calling-station-id** (*string*) | 使用者的識別符號，通常是 IP 地址或 MAC 地址。 |
| **download** (*Bytes*) | 已下載的流量。 |
| **ended** (*datetime*) | 會話關閉的日期和時間。活動會話為空。 |
| **last-accounting-packet** (*datetime*) | 收到最後一次計費更新的日期和時間。 |
| **nas-ip-address** (*IP address*) | NAS 的 IP 地址。 |
| **nas-port-id** (*string*) | 正在對使用者進行認證的 NAS 埠識別符號。 |
| **nas-port-type** (*string*) | 正在對使用者進行認證的埠型別（*physical* 或 *virtual*）。 |
| **started** (*datetime*) | 會話建立的日期和時間。 |
| **status** (*list of statuses*) | 會話可能的可用狀態：*start -* 已收到計費訊息 *Start*，*stop -* 已收到計費訊息 *Stop*，*interim - Interim update* 已收到，*close-acked* - 會話已成功關閉，*expired.* |
| **terminate-cause** (*string*) | 會話關閉的原因。 |
| **upload** (*Bytes*) | 已上傳的流量。 |
| **uptime** (*time*) | 會話記錄的總線上時長。 |
| **user** (*string*) | 使用者名稱。 |
| **user-address** (*IP address*) | 提供給使用者的 IP 地址。 |

## 設定 {#settings}

**子選單：** `/user-manager`

**屬性**

| 屬性 | 描述 |
| :-- | :-- |
| **accounting-port** (*integer*; 預設值：**1813**) | 用於偵聽 RADIUS 計費請求的埠。 |
| **authentication-port**(*integer*; 預設值：**1812**) | 用於偵聽 RADIUS 認證請求的埠。 |
| ***certificate*** (*certificate*; 預設值：) | [證書儲存中的證書](./certificates.md)，用於 EAP TLS 型別認證方法。 |
| ***enabled*** (*yes \| no*; 預設值：**no**) | 是否啟用 User Manager 功能。 |
| **radsec-certificate**(certificate; 預設值：) | [證書儲存中的證書](./certificates.md)，用於 RadSec 協定。 |
| **use-profiles**(*yes \| no*; 預設值：**no**) | 是否使用 **Profiles** 和 **Limitations**。設定為 *no* 時，只需 **User** 配置即可執行 User Manager。 |

### 高階 {#advanced}

**子選單：** `/user-manager/advanced`

**屬性**

| 屬性 | 描述 |
| :-- | :-- |
| **paypal-allow** (*yes \| no*; 預設：**no**) | 是否為 User Manager 啟用 PayPal 功能。 |
| **paypal-currency** (*string*; 預設：**USD**) | 與 *price* 設定相關的貨幣，使用者將按此貨幣計費。 |
| **paypal-password** (*string*; 預設： ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | PayPal API 賬戶的密碼。 |
| **paypal-signature** (*string*; 預設： ) | PayPal API 賬戶的簽名。 |
| **paypal-use-sandbox** (*yes \| no*; 預設：**no**) | 是否使用 PayPal 的沙箱環境進行測試。 |
| **paypal-user** (*string*; 預設： ) | PayPal API 賬戶的使用者名稱。 |
| **web-private-password** (*string*; 預設： ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 透過 HTTP 訪問 */um/PRIVATE/* 部分的密碼。 |
| **web-private-username** (*string*; 預設： ) | 透過 HTTP 訪問 */um/PRIVATE/* 部分的使用者名稱。 |

## 使用者 {#users}

**子選單：** `/user-manager/user`

### 屬性 {#properties-5}

| 屬性 | 描述 |
| :-- | :-- |
| **attributes** (*array of attributes*; 預設： ) | 自定義的一組 **Attributes** 及其值，將額外新增到 Access-Accept 訊息中。 |
| **caller-id**(*string*; 預設： ) | 允許使用者使用特定的 *Calling-Station-Id* 值進行認證。 |
| **comment** (*string*; 預設： ) | 使用者的簡短描述。 |
| **disabled** (*yes \| no*; 預設：**no**) | 控制該使用者是否可以使用。 |
| **group** (*group*; 預設：**default**) | 使用者關聯的 **Group** 名稱。 |
| **name** (*string*; 預設： ) | 用於會話認證的使用者名稱。 |
| **otp-secret** (*string*; 預設： ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 附加到密碼的一次性密碼令牌。 |
| **password** (*string*; 預設： ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於會話認證的使用者密碼。 |
| **shared-users** (*integer \| unlimited*; 預設：**1**) | 該使用者可同時建立的會話總數。 |

### 命令 {#commands-2}

| 屬性 | 描述 |
| :-- | :-- |
| **add-batch-users** () | 該命令可根據各種引數生成多個使用者賬戶。 |
| **generate-voucher** () | 根據 *voucher-template* 生成可呈現給終端使用者的檔案。 |
| **monitor** () | 顯示使用者的總統計資訊。統計項包括 *total-uptime*、*total-download*、*total-upload*、*active-sessions*、*actual-profile*、*attributes-details*。 |

## 使用者組 {#user-groups}

**子選單：** `/user-manager/user/group`

使用者組定義了多個使用者的共同特徵，例如允許的認證方法和 RADIUS 屬性。User Manager 中已經存在兩個組，分別稱為 *default* 和 *default-anonymous*。

### 屬性 {#properties-6}

| 屬性 | 描述 |
| :-- | :-- |
| **attributes** (*array of attributes*; 預設： ) | 自定義的一組 **Attributes** 及其值，將額外新增到該組使用者的 Access-Accept 訊息中。 |
| **comment** (*string*; 預設： ) | 使用者組的簡短描述。 |
| **inner-auths** (*list of auths*; 預設： ) | 用於隧道化（外部）認證方法的允許內部認證方法列表。支援的內部認證方法 - *ttls-pap*、*ttls-chap*、*ttls-mschap1*、*ttls-mschap2*、*peap-mschap2*。 |
| **name** (*string*; 預設： ) | 使用者組的唯一名稱。 |
| **outer-auths** (*list of auths*; 預設： ) | 允許的認證方法列表。支援的外部認證方法 - *pap*、*chap*、*mschap1*、*mschap2*、*eap-tls*、*eap-ttls*、*eap-peap*、*eap-mschap2*。 |

## 使用者配置檔案 {#user-profiles}

**子選單：** `/user-manager/user-profile`

此選單為使用者分配配置檔案並跟蹤配置檔案的狀態。單個使用者可以分配多個配置檔案；但是，同一時間只能使用一個。當前活動的配置檔案過期時，使用者將無縫切換到下一個配置檔案，而不會斷開使用者的會話。

### 屬性 {#properties-7}

| 屬性 | 描述 |
| :-- | :-- |
| **profile** (*profile*; 預設： ) | 要分配給使用者的配置檔名稱。 |
| **user**(*user*; 預設： ) | 要使用特定配置檔案的使用者名稱。 |

### 只讀屬性 {#read-only-properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **end-time** (*datetime*) | **User Profile** 將過期的日期和時間。 |
| **state** (*running active* \| running \| *used*) | **User Profile** 的當前狀態。*Running active -* 使用者當前正在使用的配置檔案。*Running* - 配置檔案已準備好可使用。*Used* - 已過期且無法再啟用的配置檔案。 |

### 命令 {#commands-3}

| 屬性 | 描述 |
| :-- | :-- |
| **activate-user-profile** () | 使 **User Profile** 條目立即生效。 |

## WEB 介面 {#web-interface}

每個使用者都可以使用 WEB 介面訪問其個人配置檔案。透過將 "/um/" 目錄新增到路由器的 IP 或域名，即可訪問 WEB 介面，例如 `http://example.com/um/`。請注意，WEB 介面受 IP Services "www" 和 "www-ssl" 影響。WEB 介面可以使用 CSS、JavaScript 和 HTML 進行自定義。

### 可自定義檔案參考 {#customizable-file-reference}

| 檔案 | 描述 |
| :-- | :-- |
| **css/login.css** | 登入提示頁面使用的層疊樣式表文件。 |
| **css/user.css** | 使用者配置檔案頁面使用的層疊樣式表文件。 |
| **img/PayPal\_mark\_37x23.gif** | PayPal 徽標影像。 |
| **img/ajax-loader.gif** | 處理頁面切換時使用的載入 gif。 |
| **img/mikrotik\_logo.png** | 顯示在所有頁面上的 MikroTik 徽標。 |
| **js/generic.js** | 所有頁面使用的 Javascript 檔案。 |
| **js/login.js** | 登入提示頁面使用的 Javascript 檔案。 |
| **js/user.js** | 使用者配置檔案頁面使用的 Javascript 檔案。 |
| **user/login\_dynamic.html** | 登入提示頁面的佈局。 |
| **user/user\_dynamic.html** | 使用者配置檔案頁面的佈局。 |

## 應用指南 {#application-guides}

### 批次建立使用者 {#batch-user-creation}

可以建立多個具有隨機生成使用者名稱和密碼的新使用者。例如，以下命令將生成 3 個新使用者，使用者名稱為 6 個小寫符號，密碼為 6 個小寫字母、大寫字母和數字。

```ros
/user-manager/user
add-batch-users number-of-users=3 password-characters=lowercase,numbers,uppercase password-length=6 username-characters=lowercase username-length=6
```

可透過列印使用者表檢視該命令生成的使用者：

```ros
/user-manager/user/print 
Flags: X - disabled 
 0   name="olsgkl" password="86a6zH" otp-secret="" group=default shared-users=1 attributes="" 

 1   name="lkbwss" password="jaKY5V" otp-secret="" group=default shared-users=1 attributes="" 

 2   name="cwxbwu" password="a62yZd" otp-secret="" group=default shared-users=1 attributes="" 

```

### 為 NAS 提供自定義 RADIUS 屬性 {#providing-nas-with-custom-radius-attributes}

可以在認證過程中傳送額外的 RADIUS 屬性，以便向 NAS 提供有關會話的自定義資訊，例如應向請求方分配哪個 IP 地址，或應使用哪個地址池進行地址分配。

#### 為使用者分配靜態 IP 地址 {#static-ip-address-for-a-user}

要為終端使用者分配靜態 IP 地址，可以使用 *Framed-IP-Address* 屬性。使用靜態 IP 地址分配時，必須將 *shared-sessions* 設定為 1，以防止出現使用者有多個同時會話但只有一個 IP 地址的情況。例如：

```ros
/user-manager/user
set [find name=username] shared-users=1 attributes=Framed-IP-Address:192.168.1.4
```

#### 為一組使用者指定地址池 {#specifying-address-pool-for-a-group-of-users}

我們可以將多個相似使用者分組，並一次性為所有使用者分配 RADIUS 屬性。首先，建立一個新組：

```ros
/user-manager/user/group
add name=location1 outer-auths=chap,eap-mschap2,eap-peap,eap-tls,eap-ttls,mschap1,mschap2,pap \
inner-auths=peap-mschap2,ttls-chap,ttls-mschap1,ttls-mschap2,ttls-pap attributes=Framed-Pool:pool1
```

下一步是將使用者分配到該組：

```ros
/user-manager/user
 set [find name=username] group=location1
```

在這種情況下，認證時將從 *pool1* 向用戶分配一個 IP 地址 - 請確保在 NAS 裝置上已建立 *pool1*。

### 使用 TOTP（基於時間的一次性密碼）進行使用者認證 {#using-totp-time-based-one-time-password-for-user-authentication}

User Manager 支援將基於時間的認證令牌附加到使用者密碼欄位，該令牌每 30 秒重新生成。

:::danger
OTP 依賴於時鐘，因此請確保已正確配置時間設定。

:::

TOTP 的工作原理是在請求方（用戶端）和認證伺服器（User Manager）上使用共享金鑰。要在 RouterOS 上配置 TOTP，只需為使用者設定 *otp-secret*。例如：

```ros
/user-manager/user
set [find name=username] password=mypass otp-secret=mysecret

```

要在請求方一側計算 TOTP 令牌，可以使用許多廣泛可用的應用，例如 Google Authenticator 或 [https://totp.app/](https://totp.app/)。將 mysecret 新增到 TOTP 令牌生成器後將提供一個唯一的新 6 位程式碼，必須將其新增到使用者密碼中。

![](/img/41241175d691e7c4.webp)

以下示例將接受使用者使用附加到普通密碼後的計算所得 TOTP 令牌進行認證，直到生成新的 TOTP 令牌。

```text
User-Name=username
User-Password=mypass620872
```

### 匯出使用者憑據 {#exporting-user-credentials}

#### **單個使用者的可列印登入憑據** {#printable-login-credentials-for-a-single-user}

要生成單個使用者的可列印憑據卡，只需使用 *generate-voucher* 命令。指定使用者的 RouterOS ID 號，或使用 *find* 命令指定使用者名稱。User Manager 的安裝中已經包含一個模板，可在裝置的 Files 部分中找到。您可以根據需要自定義模板。

```ros
/user-manager/user
generate-voucher voucher-template=printable_vouchers.html [find where name=username]
```

透過 WEB 瀏覽器訪問路由器並導航到 */um/PRIVATE/GENERATED/vouchers/gen\_printable\_vouchers.html* 即可獲取生成的憑據卡。

預設情況下，可列印卡片如下所示：

![](/img/f77afb5d13302de9.webp)

:::warning
要透過 WEB 瀏覽器訪問 /um/ 目錄的 PRIVATE 路徑，必須配置 *private-username* 和 *private-password*。請參閱 **Settings** 部分。

:::

生成憑據時可以使用不同的變數。當前支援的變數包括：

$(username) - 表示 User Manager 使用者名稱  
$(password) - 該使用者名稱的密碼  
$(userprofname) - 該使用者當前活動的配置檔案  
$(userprofendtime) - 配置檔案的失效結束時間（如果指定）

#### 匯出多個使用者憑據 {#multiple-user-credential-export}

透過將 *export.xml* 或 *export.csv* 用作 *voucher-template*，可以一次生成包含多個或所有使用者憑據的 CSV 或 XML 檔案。

```ros
/user-manager/user
generate-voucher voucher-template=export.xml [find]
```

該命令會生成 XML 檔案 *um5files/PRIVATE/GENERATED/vouchers/gen\_export.xml*，可透過 WEB 瀏覽器或任何其他檔案訪問工具訪問。

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

### 生成使用情況報告 {#generating-usage-report}

在公司計費或法務團隊需要可呈現的網路使用資訊時，可以使用 *generate-report* 命令建立自動化的會話匯出。該命令需要輸入報告模板 - 模板示例位於 *um5files/PRIVATE/TEMPLATES/reports/report\_default.html*。報告生成示例：

```ros
/user-manager
generate-report report-template=report_default.html columns=username,uptime,download,upload
```

透過 WEB 瀏覽器訪問路由器並導航到 */um/PRIVATE/GENERATED/reports/gen\_report\_default.html* 即可獲取生成的報告。

*![](/img/347a8e944793bdb6.webp)*

### 購買配置檔案 {#purchasing-a-profile}

使用者使用 WEB 瀏覽器訪問路由器的 */um/* 目錄（例如 http://example.com/um/）登入其私人配置檔案後，將能夠在相應選單中看到所有可用的 **Profiles**。指定了 *price* 值的配置檔案將提供 *Buy this Profile* 按鈕。

![](/img/a947415d24d11d74.webp)

按下 *Buy this Profile* 按鈕後，使用者將被要求從可用交易服務提供商中選擇（目前僅提供 PayPal），隨後會重定向到 PayPal 的支付處理頁面。

![](/img/368b0af05bc7f389.webp)

付款完成後，User Manager 會請求 PayPal 批准該交易。批准後，配置檔案會分配給使用者並可供使用。![](/img/39c330686cc9db0e.webp)

### 從 RouterOS v6 遷移 {#migrating-from-routeros-v6}

當您將 User Manager 路由器從 RouterOS v6 升級到 v7 時，新的 User Manager 將使用新的資料庫檔案和配置。要繼續使用舊的使用者、路由器、配置檔案等配置，必須手動執行 migrate 命令。為此，必須存在舊 User Manager 伺服器資料夾 "user-manager" 中的檔案。該資料夾可以重新命名，但舊安裝中的所有內容都必須傳輸到新的 v7 安裝中（您可以將舊配置從一臺路由器移動到另一臺執行 v7 的路由器，但必須複製 "user-manager" 資料夾）。之後，只需執行以下命令 - `/user-manager/database/migrate-legacy-db database-path=<path_to_old_user_manager_folder>`。

匯入過程將嘗試轉換以下配置 - 使用者、配置檔案、user-profiles、限制項、profile-limitations、user-counters、路由器和會話。

## 應用示例 {#application-examples}

### 使用 User Manager 認證的基本 L2TP/IPsec 伺服器 {#basic-l2tpipsec-server-with-user-manager-authentication}

![](/img/5cb98b1471afb086.webp)

#### User Manager 配置 {#user-manager-configuration}

首先啟用 User Manager 功能。

```ros
/user-manager
set enabled=yes
```

允許接收來自 localhost（路由器本身）的 RADIUS 請求。

```ros
/user-manager/router
add address=127.0.0.1 comment=localhost name=local shared-secret=test
```

接下來，新增使用者及其憑據，用戶端將使用這些憑據向伺服器認證。

```ros
/user-manager/user
add name=user1 password=password
```

#### 配置 RADIUS 用戶端 {#configuring-radius-client}

為了讓路由器使用 RADIUS 伺服器進行使用者認證，需要新增一個新的 RADIUS 用戶端，併為其配置與 User Manager 上已配置的相同共享金鑰。

```ros
/radius
add address=127.0.0.1 secret=test service=ipsec
```

#### L2TP/IPsec 伺服器配置 {#l2tpipsec-server-configuration}

配置將向用戶分配 IP 地址的 IP 地址池，並將其分配給 PPP Profile。

```ros
/ip/pool
add name=vpn-pool range=192.168.99.2-192.168.99.100

/ppp/profile
set default-encryption local-address=192.168.99.1 remote-address=vpn-pool
```

啟用 RADIUS 用於 PPP 認證。

```ros
/ppp/aaa
set use-radius=yes
```

啟用帶 IPsec 加密的 L2TP 伺服器。

```ros
/interface/l2tp-server/server
set enabled=yes use-ipsec=required ipsec-secret=mySecret
```

就是這樣。您的路由器現在已準備好接受 L2TP/IPsec 連線，並透過內部 User Manager 對其進行認證。

### RouterOS 使用者登入的雙因素認證（MFA/2FA） {#two-factor-authentication-for-routeros-user-login-mfa2fa}

由於 User-Manager 支援 TOTP（基於時間的一次性密碼），因此可以為不同服務設定所謂的 MFA 認證。這裡我們將研究透過 User Manager（radius）進行 RouterOS 使用者認證，並使用每 30 秒更改一次的基於時間的密碼。

**以下是 MikroTik 路由器上必要的配置選項。**

為 /user 選單啟用 RADIUS，並從 `/user/group` 選單設定 default-group。請注意，系統會先檢查本地 /user 資料庫，然後再聯絡 RADIUS。

```
/user/aaa/set use-radius=yes default-group=full
```

為登入服務啟用 radius 用戶端。由於我們在同一臺路由器上執行 User Manager，因此使用 127.0.0.1，

```
/radius/add address=127.0.0.1 service=login secret=mystrongsecret
```

**以下是 User Manager 的配置步驟**，

確保已將受管裝置新增到 "Routers" 選單，

```
/user-manager/router/add name=myrouter address=127.0.0.1 shared-secret=mystrongsecret
```

將使用者新增到 User-Manager 使用者表，並設定 OTP secret 引數。要正確配置 OTP，還需要幾個步驟。  
選擇一個 OTP-secret 名稱並將其轉換為 base32 格式（有許多線上轉換器可將 utf-8 轉換為 base32 格式）。對於我的配置，我使用 "mysupersecret"，其 base32 形式為 NV4XG5LQMVZHGZLDOJSXI===

```
/user-manager/user/add name=mikrotik password=mysuperpassword otp-secret="NV4XG5LQMVZHGZLDOJSXI==="
```

請注意，在你常用的身份驗證器應用中，新增新的時間密碼例項時，需要手動為使用者設定此金鑰 "NV4XG5LQMVZHGZLDOJSXI==="。

要登入 MikroTik 裝置，請開啟 Winbox/Console 並連線到路由器地址，使用登入名：mikrotik，密碼：mysuperpasswordxxxxxx，其中 xxxxxx 是你常用身份驗證應用中的 6 位程式碼。

密碼每 30 秒更改一次，可從你常用的應用中獲取。

![](/img/73454df958b000d2.jpg)
