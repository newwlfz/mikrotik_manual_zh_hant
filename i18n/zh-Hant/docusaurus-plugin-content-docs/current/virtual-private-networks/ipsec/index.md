---
sidebar_key: "virtual-private-networks/ipsec"
title: "IPsec"
sidebar_label: "IPsec"
description: "本節涵蓋 IPsec 示例與整合。可用它配置 IKEv2、pre-shared-key 和 post-quantum 金鑰工作流，以及第三方 VPN 連線。"
tags:
  - 'ipsec'
  - 'ike'
  - 'diffie-hellman'
source: https://manual.mikrotik.com/docs/virtual-private-networks/ipsec
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節涵蓋 IPsec 示例和整合。可使用它配置 IKEv2、pre-shared-key 和後量子金鑰工作流，以及第三方 VPN 連線。

**Internet Protocol Security (IPsec)** 是由 Internet Engineering Task Force (IETF) 定義的一組協定，用於在 Internet 等未受保護的 IP/IPv6 網路上保護封包交換。

IPsec 協定套件可分為以下幾組：

- **Internet Key Exchange (IKE)** 協定，用於為 AH 和 ESP 動態生成和分發加密金鑰。
- **Authentication Header (AH)** RFC 4302。
- **Encapsulating Security Payload (ESP)** RFC 4303。

## Internet Key Exchange 協定 (IKE) {#internet-key-exchange-protocol-ike}

Internet Key Exchange（IKE）是一種協定，為 Internet Security Association and Key Management Protocol（ISAKMP）框架提供經過認證的金鑰材料。其他金鑰交換方案也可與 ISAKMP 配合使用，但 IKE 是使用最廣泛的一種。二者共同提供了主機認證和安全關聯（SA）自動管理的手段。

IKE daemon 在大多數情況下保持空閒。它會在兩種情況下被啟用：

由策略規則匹配的流量需要加密或認證，但該策略沒有任何 SA。策略會將此情況通知 IKE daemon，隨後 IKE daemon 會向遠端主機發起連線。IKE daemon 也可以響應遠端連線。在兩種情況下，對等方都會建立連線並執行 2 個階段：

- **階段 1**——對等方就後續 IKE 訊息中使用的演算法達成一致，並相互認證。用於為所有 SA 派生金鑰以及保護主機之間後續 ISAKMP 交換的金鑰材料也會生成。此階段應匹配以下設定：
  - 認證方法
  - DH 組
  - 加密演算法
  - 交換模式
  - 雜湊演算法
  - NAT-T
  - DPD 和 lifetime（可選）

- **階段 2**——對等方建立一個或多個供 IPsec 用於加密資料的 SA。IKE daemon 建立的所有 SA 都有 lifetime 值（限制 SA 失效之前的時間、此 SA 可加密的資料量，或兩者兼有）。此階段應匹配以下設定：
  - IPsec 協定
  - 模式（隧道或傳輸）
  - 認證方法
  - PFS（DH）組
  - lifetime

:::warning
存在兩個生命週期值——軟生命週期和硬生命週期。當 SA 達到其軟生命週期閾值時，IKE 守護程式會收到通知，並啟動另一次 phase 2 交換，以用新的 SA 替換此 SA。如果 SA 達到硬生命週期，則會被丟棄。

**注意：** 如果在生命週期到期時 DPD 被停用，Phase 1 不會重新生成金鑰；只有 Phase 2 會重新生成金鑰。要強制 Phase 1 重新生成金鑰，請啟用 DPD。

**注意：** PSK 認證曾已知在 "aggressive" 模式下容易受到離線攻擊，但最近的發現表明，在 "main" 和 "ike2" 交換模式下也可能進行離線攻擊。你應避免使用 PSK 認證方法。
:::

IKE 可選地提供完美前向保密（PFS），這是金鑰交換的一種屬性；對 IKE 而言，這意味著即使長期階段 1 金鑰被洩露，也無法輕易訪問透過此階段 1 建立的 SA 所保護的所有 IPsec 資料。這意味著會為每個階段 2 生成額外的金鑰材料。

金鑰材料的生成在計算上非常昂貴。例如，modp8192 組交換即使在非常快的計算機上也可能需要數秒。它通常每個階段 1 交換執行一次，而階段 1 交換在任意一對主機之間只發生一次，然後會長期保留。PFS 也會將此昂貴操作新增到每次階段 2 交換中。

### Diffie-Hellman 組 {#diffie-hellman-groups}

Diffie-Hellman (DH) 金鑰交換協定允許最初沒有共享金鑰的雙方安全地建立一個共享金鑰。支援以下模指數 (MODP) 和 ECP Diffie-Hellman（也稱為 "Oakley"）組：

| Diffie-Hellman 組 | 名稱 | 參考 |
| :-- | :-- | :-- |
| Group 1 | 768 位 MODP 組 | RFC 2409 |
| Group 2 | 1024 位 MODP 組 | RFC 2409 |
| Group 5 | 1536 位 MODP 組 | RFC 3526 |
| Group 14 | 2048 位 MODP 組 | RFC 3526 |
| Group 15 | 3072 位 MODP 組 | RFC 3526 |
| Group 16 | 4096 位 MODP 組 | RFC 3526 |
| Group 17 | 6144 位 MODP 組 | RFC 3526 |
| Group 18 | 8192 位 MODP 組 | RFC 3526 |
| Group 19 | 256 位隨機 ECP 組 | RFC 5903 |
| Group 20 | 384 位隨機 ECP 組 | RFC 5903 |
| Group 21 | 521 位隨機 ECP 組 | RFC 5903 |

有關標準的更多資訊可在[此處](https://www.iana.org/assignments/ipsec-registry/ipsec-registry.xhtml)找到。

更大的 DH 組提供更強的安全性，但需要更多 CPU 資源。以下是幾個具有不同安全級別和 CPU 影響的常見 DH 組：

DH Group 14（2048 位） - 在安全性和 CPU 使用率之間提供實際平衡。它提供 2048 位金鑰交換，被認為對大多數現代應用是安全的，並得到廣泛支援。

DH Group 5（1536 位） - 提供比 DH Group 14 略低的安全性，但由於金鑰較小，CPU 開銷更低。對於許多場景仍被認為可接受。

DH 組 2（1024 位）——應謹慎使用，因為它在常用組中提供的安全性最低。儘管 CPU 需求較低，但隨著計算能力提升，它更容易受到攻擊。不要將其用於新部署。

為獲得最佳安全性，應使用 **DH 組 19**。它通常被認為既快速又安全。通常應避免使用 DH 組 2，除非需要與舊裝置相容。

:::info
要計算適合你的網路基礎設施的安全級別，首先確定所需的安全位數，並估算解密受保護資料應需要多長時間。根據這些要求，選擇合適的演算法。參考資料見 [https://www.keylength.com/en/4/](https://www.keylength.com/en/4/)。
:::

### IKE 流量 {#ike-traffic}

為避免 IKE 封包命中某些 SPD 規則並需要用尚未建立的 SA 進行加密（該封包可能正試圖建立此 SA）而引發問題，本地發起的、UDP 源埠為 500 的封包不會經過 SPD 處理。同樣，要交付給本地的、UDP 目的埠為 500 的封包也不會在入站策略檢查中處理。

### 設定流程 {#setup-procedure}

要讓 IPsec 使用 IKE-ISAKMP 自動生成金鑰並正常工作，必須配置 policy、peer 和 proposal（可選）條目。

:::danger
IPsec 對時間變化非常敏感。如果 IPsec 隧道兩端的時間同步不一致（例如，不同的 NTP 伺服器未使用相同時間戳更新時間），隧道會中斷，並且必須重新建立。
:::

### EAP 認證方法 {#eap-authentication-methods}

| 外部認證 | 內部認證 |
| :-- | :-- |
| EAP-GTC |  |
| EAP-MD5 |  |
| EAP-MSCHAPv2 |  |
| EAP-PEAPv0 | EAP-MSCHAPv2 EAP-GPSK EAP-GTC EAP-MD5 EAP-TLS |
| EAP-SIM |  |
| EAP-TLS |  |
| EAP-TTLS | PAP  CHAP  MS-CHAP  MS-CHAPv2  EAP-MSCHAPv2 EAP-GTC EAP-MD5 EAP-TLS |

在 Windows 上，**EAP-TLS** 稱為“智慧卡或其他證書”。

:::info
不支援 IKEv2 認證的 AES-GCM 加密。

**重要：** 如果將 IPsec 與證書 X.509 一起使用，證書必須包含 "SubjectKeyIdentifier" 擴充套件，該擴充套件僅在版本 3 中受支援。

**重要：** 不支援使用 ed25519 認證。
:::

## 認證頭 (AH) {#authentication-header-ah}

AH 是一種協定，它透過新增一個根據封包中的值計算出的報頭，對封包的全部或部分內容提供認證。封包的哪些部分用於計算以及報頭的放置位置取決於使用的是隧道模式還是傳輸模式。

AH 報頭的存在允許驗證訊息的完整性，但不會加密訊息。因此，AH 提供認證但不提供隱私。另一種協定 (ESP) 被認為更優越；它提供資料隱私，並且也有自己的認證方法。

RouterOS 支援以下 AH 認證演算法：

- SHA2（256、512）
- SHA1
- MD5

### 傳輸模式 {#transport-mode}

在傳輸模式下，AH 報頭插入到 IP 報頭之後。使用 IP 資料和報頭計算認證值。傳輸過程中可能變化的 IP 欄位（如 TTL 和跳數）在認證前會被設定為零值。

### 隧道模式 {#tunnel-mode}

在隧道模式下，原始 IP 封包被封裝在一個新的 IP 封包中。所有原始 IP 封包都會被認證。

## 封裝安全載荷 (ESP) {#encapsulating-security-payload-esp}

Encapsulating Security Payload (ESP) 使用共享金鑰加密來提供資料隱私。ESP 還支援自己的認證方案，類似 AH 中使用的方案。

ESP 打包其欄位的方式與 AH 非常不同。它不只有一個報頭，而是將欄位分為三個組成部分：

- **ESP Header** - 位於加密資料之前，其放置位置取決於 ESP 是用於傳輸模式還是隧道模式。
- **ESP Trailer** - 此部分位於加密資料之後。它包含用於對齊加密資料的填充。
- **ESP Authentication Data** - 此欄位包含完整性校驗值 (ICV)，其計算方式類似於 AH 協定的工作方式，用於 ESP 的可選認證功能啟用時。

### 傳輸模式 {#transport-mode-1}

在傳輸模式下，ESP 報頭插入到原始 IP 報頭之後。ESP 尾部和認證值新增到封包末尾。在此模式下，僅對 IP 載荷進行加密和認證；IP 報頭不受保護。

![](/img/e820cafb5508d83a.webp)

### 隧道模式 {#tunnel-mode-1}

在隧道模式下，原始 IP 封包被封裝在一個新的 IP 封包中，從而保護 IP 載荷和 IP 報頭。

![](/img/53ccf4c24f574ee8.webp)

### 加密演算法 {#encryption-algorithms}

RouterOS ESP 支援多種加密和認證演算法。

#### 認證 {#authentication}

- **MD5**
- **SHA1**
- **SHA2（256 位、512 位）**

#### 加密 {#encryption}

- **AES** - 128 位、192 位和 256 位金鑰的 AES-CBC、AES-CTR 和 AES-GCM 演算法。
- **Blowfish** - 自 v4.5 起新增。
- **Twofish** - 自 v4.5 起新增。
- **Camellia** - 自 v4.5 起新增的 128 位、192 位和 256 位金鑰 Camellia 加密演算法。
- **DES** - 56 位 DES-CBC 加密演算法。
- **3DES** - 168 位（3 x 56 位）DES 加密演算法。

### 硬體加速 {#hardware-acceleration}

硬體加速透過 CPU 內建的加密引擎實現更快的加密。

具有硬體加速的裝置列表可在[此處](https://mikrotik.com/products?filter&s=c&f=%5B%22ipsec%22%5D)獲取。

<WideTable>

| CPU | DES 和 3DES |  |  |  | AES-CBC |  |  |  | AES-CTR |  |  |  | AES-GCM |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | MD5 | SHA1 | SHA256 | SHA512 | MD5 | SHA1 | SHA256 | SHA512 | MD5 | SHA1 | SHA256 | SHA512 | MD5 | SHA1 | SHA256 | SHA512 |
| 88F7040 | no | yes | yes | yes | no | yes | yes | yes | no | yes | yes | yes | no | yes | yes | yes |
| AL21400 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| AL32400 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| AL52400 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| AL73400 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| IPQ-4018 / IPQ-4019 | no | yes | yes | no | no | yes\* | yes\* | no | no | yes\* | yes\* | no | no | no | no | no |
| IPQ-5018 | yes | yes | yes | no | yes | yes | yes | no | yes | yes | yes | no | no | no | no | no |
| IPQ-6010 | no | no | no | no | no | yes | yes | yes | no | yes | yes | yes | no | yes | yes | yes |
| IPQ-8064 | no | yes | yes | no | no | yes\* | yes\* | no | no | yes\* | yes\* | no | no | no | no | no |
| IPQ-8072 | no | no | no | no | no | yes | yes | yes | no | yes | yes | yes | no | yes | yes | yes |
| MT7621A | yes\*\*\*\* | yes\*\*\*\* | yes\*\*\*\* | no | yes | yes | yes | no | no | no | no | no | no | no | no | no |
| EN7562CT | yes\*\*\*\* | yes\*\*\*\* | yes\*\*\*\* | no | yes | yes | yes | no | yes | yes | yes | no | no | no | no | no |
| P1023NSN5CFB | no | no | no | no | yes\*\* | yes\*\* | yes\*\* | yes\*\* | no | no | no | no | no | no | no | no |
| P202ASSE2KFB | yes | yes | yes | no | yes | yes | yes | yes | no | no | no | no | no | no | no | no |
| PPC460GT | no | no | no | no | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | no | no | no | no |
| TLR4 (TILE) | yes | yes | yes | no | yes | yes | yes | no | yes | yes | yes | no | no | no | no | no |
| x86 (AES-NI) | no | no | no | no | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* | 是\*\*\* |

</WideTable>

\* 僅支援 128 位和 256 位金鑰長度

\*\* 僅 2016 年以後製造，序列號以數字 5 和 7 開頭

\*\*\* 僅 AES-CBC 和 AES-CTR 加密被加速，雜湊在軟體中完成

\*\*\*\* 不支援 DES，僅支援 3DES 和/或 AES-CBC

各種加密和雜湊演算法組合的 IPsec 吞吐量結果釋出在 [MikroTik 產品頁面](https://mikrotik.com/products) 上。

### 帶 NAT 的 RoadWarrior 用戶端 {#roadwarrior-client-with-nat}

考慮如下所示的設定。RouterOS 充當連線到辦公室的 RoadWarrior 用戶端，允許訪問其內部資源。

![](/img/dc6b627dbef3d1f7.webp)

隧道已建立，收到本地 mode-config IP 地址，並生成一組動態策略。

```ros
[admin@mikrotik] > ip ipsec policy print 
Flags: T - template, X - disabled, D - dynamic, I - invalid, A - active, * - default 
0 T * group=default src-address=::/0 dst-address=::/0 protocol=all proposal=default template=yes 

1 DA src-address=192.168.77.254/32 src-port=any dst-address=10.5.8.0/24 dst-port=any protocol=all 
action=encrypt level=unique ipsec-protocols=esp tunnel=yes sa-src-address=10.155.107.8 
sa-dst-address=10.155.107.9 proposal=default ph2-count=1 

2 DA src-address=192.168.77.254/32 src-port=any dst-address=192.168.55.0/24 dst-port=any protocol=all 
action=encrypt level=unique ipsec-protocols=esp tunnel=yes sa-src-address=10.155.107.8 
sa-dst-address=10.155.107.9 proposal=default ph2-count=1 
```

只有源地址為 192.168.77.254/32 的封包才匹配 IPsec 策略。要讓本地網路訪問遠端子網，必須將本地主機的源地址改為動態分配的 mode config IP 地址。源 NAT 規則可以動態生成。建立一個新的地址列表，其中包含應應用 NAT 規則的所有本地網路。在本例中為 192.168.88.0/24。

```ros
/ip/firewall/address-list/add address=192.168.88.0/24 list=local-RW
```

在 mode-config 發起方配置下指定地址列表，會動態生成源 NAT 規則。

```ros
/ip/ipsec/mode-config/set [ find name="request-only" ] src-address-list=local-RW
```

當 IPsec 隧道建立後，會為每個網路顯示動態建立的源 NAT 規則。現在 192.168.88.0/24 中的每臺主機都可以訪問 Office 的內部資源。

```ros
[admin@mikrotik] > ip firewall nat print 
Flags: X - disabled, I - invalid, D - dynamic 
0 D ;;; ipsec mode-config
chain=srcnat action=src-nat to-addresses=192.168.77.254 dst-address=192.168.55.0/24 src-address-list=local-RW

1 D ;;; ipsec mode-config
chain=srcnat action=src-nat to-addresses=192.168.77.254 dst-address=10.5.8.0/24 src-address-list=local-RW
```

### 僅允許 IPsec 封裝流量 {#allow-only-ipsec-encapsulated-traffic}

在某些場景中，出於安全原因，如果傳入/傳出封包未加密，你可能希望阻止對特定網路的訪問。例如，如果你有 L2TP/IPsec 設定，可能希望丟棄未加密的 L2TP 連線嘗試。

可以透過以下幾種方式實現：

- 在防火牆中使用 IPsec 策略匹配器。
- 使用 action 設定為 **drop** 且優先順序較低的通用 IPsec 策略（可用於會生成動態策略的 Road Warrior 設定）。
- 在 mangle 中設定 DSCP 或優先順序，並在解封裝後在防火牆中匹配相同的值。

#### IPsec 策略匹配器 {#ipsec-policy-matcher}

讓我們設定一個 IPsec 策略匹配器，以接受與任何 IPsec 策略匹配的所有封包，並丟棄其餘封包：

```ros
add chain=input comment="ipsec policy matcher" in-interface=WAN ipsec-policy=in,ipsec
add action=drop chain=input comment="drop all" in-interface=WAN log=yes
```

IPsec 策略匹配器接受兩個引數 **direction、policy**。此示例使用入站方向和 IPsec 策略。IPsec 策略選項允許你在解封裝後檢查封包，例如，僅允許來自特定源地址的 GRE 封裝封包並丟棄其餘封包：

```ros
add chain=input comment="ipsec policy matcher" in-interface=WAN ipsec-policy=in,ipsec protocol=gre src-address=192.168.33.1
add action=drop chain=input comment="drop all" in-interface=WAN log=yes
```

對於 L2TP，規則集將是：

```ros
add chain=input comment="ipsec policy matcher" in-interface=WAN ipsec-policy=in,ipsec protocol=udp dst-port=1701
add action=drop chain=input protocol=udp dst-port=1701 comment="drop l2tp" in-interface=WAN log=yes
```

#### 使用通用 IPsec 策略 {#using-generic-ipsec-policy}

此方法透過新增一個 action 為 drop 的預設策略來工作。此示例假設在公網地址 1.1.1.1 上有一個 L2TP/IPsec 伺服器，並丟棄所有未加密的 L2TP：

```ros
/ip/ipsec/policy
add src-address=1.1.1.1 dst-address=0.0.0.0/0 sa-src-address=1.1.1.1 protocol=udp src-port=1701 tunnel=yes action=discard
```

路由器會丟棄任何未加密的 L2TP 入站流量，但在 L2TP/IPsec 連線成功後，會建立一個優先順序高於預設靜態規則的動態策略，匹配該動態規則的封包可以被轉發。

:::warning
策略順序很重要！為此，請確保靜態 drop 策略位於動態策略之下。如有必要，將其移到策略模板下方。
:::

```ros
[admin@rack2_10g1] /ip/ipsec/policy> print
Flags: T - template, X - disabled, D - dynamic, I - inactive, * - default
0 T * group=default src-address=::/0 dst-address=::/0 protocol=all
proposal=default template=yes

1 D src-address=1.1.1.1/32 src-port=1701 dst-address=10.5.130.71/32
dst-port=any protocol=udp action=encrypt level=require
ipsec-protocols=esp tunnel=no sa-src-address=1.1.1.1
sa-dst-address=10.5.130.71

2 src-address=1.1.1.1/32 src-port=1701 dst-address=0.0.0.0/0
dst-port=any protocol=udp action=discard level=unique
ipsec-protocols=esp tunnel=yes sa-src-address=1.1.1.1
sa-dst-address=0.0.0.0 proposal=default manual-sa=none
```

### 在對等體配置下手動指定 local-address 引數 {#manually-specifying-local-address-parameter-under-peer-configuration}

#### 使用不同的路由表 {#using-different-routing-table}

IPsec 與 RouterOS 中的任何其他服務一樣，無論 Peer 配置使用什麼 local-address 引數，都會使用主路由表。必須對 IKE 和 IPSec 流量都應用路由標記。

考慮以下示例。存在兩條預設路由——一條在主路由表中，另一條在“backup”路由表中。必須為 IPsec 站點到站點隧道使用 backup 鏈路。

```ros
[admin@pair_r1] > /ip/route/print detail 
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, B - blackhole, U - unreachable, P - prohibit 
0 A S dst-address=0.0.0.0/0 gateway=10.155.107.1 gateway-status=10.155.107.1 reachable via ether1 distance=1 scope=30 target-scope=10 routing-mark=backup 

1 A S dst-address=0.0.0.0/0 gateway=172.22.2.115 gateway-status=172.22.2.115 reachable via ether2 distance=1 scope=30 target-scope=10 

2 ADC dst-address=10.155.107.0/25 pref-src=10.155.107.8 gateway=ether1 gateway-status=ether1 reachable distance=0 scope=10 

3 ADC dst-address=172.22.2.0/24 pref-src=172.22.2.114 gateway=ether2 gateway-status=ether2 reachable distance=0 scope=10 

4 ADC dst-address=192.168.1.0/24 pref-src=192.168.1.1 gateway=bridge-local gateway-status=ether2 reachable distance=0 scope=10 

[admin@pair_r1] > /ip/firewall/nat/print 
Flags: X - disabled, I - invalid, D - dynamic 
0 chain=srcnat action=masquerade out-interface=ether1 log=no log-prefix="" 

1 chain=srcnat action=masquerade out-interface=ether2 log=no log-prefix="" 
```

IPsec 對等體和策略配置，以及 IPsec 隧道流量的 NAT 繞過規則，都使用備份鏈路的源地址建立。

```ros
/ip/ipsec/peer
add address=10.155.130.136/32 local-address=10.155.107.8 secret=test
/ip/ipsec/policy
add sa-src-address=10.155.107.8 src-address=192.168.1.0/24 dst-address=172.16.0.0/24 sa-dst-address=10.155.130.136 tunnel=yes
/ip/firewall/nat
add action=accept chain=srcnat src-address=192.168.1.0/24 dst-address=172.16.0.0/24 place-before=0
```

日誌顯示“phase1 negotiation failed due to time up”錯誤。這是因為 IPsec 嘗試使用主路由表和錯誤的源地址到達遠端對等方。必須使用 Mangle 標記 UDP/500、UDP/4500 和 ipsec-esp 封包：

```ros
/ip/firewall/mangle
add action=mark-connection chain=output connection-mark=no-mark dst-address=10.155.130.136 dst-port=500,4500 new-connection-mark=ipsec passthrough=yes protocol=udp
add action=mark-connection chain=output connection-mark=no-mark dst-address=10.155.130.136 new-connection-mark=ipsec passthrough=yes protocol=ipsec-esp
add action=mark-routing chain=output connection-mark=ipsec new-routing-mark=backup passthrough=no
```

#### 使用同一路由表和多個 IP 地址 {#using-the-same-routing-table-with-multiple-ip-addresses}

考慮以下示例。公共介面上存在同一子網的多個 IP 地址。out-interface 上配置了偽裝規則。必須顯式使用其中一個 IP 地址。

```ros
[admin@pair_r1] > /ip/address/print 
Flags: X - disabled, I - invalid, D - dynamic 
# ADDRESS NETWORK INTERFACE
0 192.168.1.1/24 192.168.1.0 bridge-local
1 172.22.2.1/24 172.22.2.0 ether1
2 172.22.2.2/24 172.22.2.0 ether1
3 172.22.2.3/24 172.22.2.0 ether1

[admin@pair_r1] > /ip/route/print 
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, B - blackhole, U - unreachable, P - prohibit 
# DST-ADDRESS PREF-SRC GATEWAY DISTANCE
1 A S 0.0.0.0/0 172.22.2.115 1
3 ADC 172.22.2.0/24 172.22.2.1 ether1 0
4 ADC 192.168.1.0/24 192.168.1.1 bridge-local 0

[admin@pair_r1] /ip/firewall/nat> print 
Flags: X - disabled, I - invalid, D - dynamic 
0 chain=srcnat action=masquerade out-interface=ether1 log=no log-prefix="" 
```

IPsec 對等體和策略配置使用其中一個公共 IP 地址建立。

```ros
/ip/ipsec/peer
add address=10.155.130.136/32 local-address=172.22.2.3 secret=test
/ip/ipsec/policy
add sa-src-address=172.22.2.3 src-address=192.168.1.0/24 dst-address=172.16.0.0/24 sa-dst-address=10.155.130.136 tunnel=yes
/ip/firewall/nat
add action=accept chain=srcnat src-address=192.168.1.0/24 dst-address=172.16.0.0/24 place-before=0
```

階段 1 連線使用的源地址與指定地址不同，日誌中會顯示“phase1 negotiation failed due to time up”錯誤。這是因為偽裝正在更改連線的源地址，以匹配已連線路由的 pref-src 地址。請排除來自該公網 IP 地址的連線，使其不被偽裝。

```ros
/ip/firewall/nat
add action=accept chain=srcnat protocol=udp src-port=500,4500 place-before=0
```

## 應用示例 {#application-examples}

### 站點到站點 IPsec (IKEv1) 隧道 {#site-to-site-ipsec-ikev1-tunnel}

考慮如下所示的設定。兩個遠端辦公室路由器連線到 Internet，辦公室工作站位於 NAT 之後。每個辦公室都有自己的本地子網，Office1 為 10.1.202.0/24，Office2 為 10.1.101.0/24。兩個遠端辦公室都需要通向路由器後方本地網路的安全隧道。

![](/img/e82d4ebd9d1188e7.webp)

#### **站點 1 配置** {#site-1-configuration}

首先建立新的階段 1 profile 和階段 2 proposal 條目，使用適合你需求的更強或更弱加密引數。應為每個選單建立單獨的條目，以便在以後需要調整任何設定時，每個 peer 都有唯一的條目。這些引數必須在各站點之間匹配，否則連線無法建立。

```ros
/ip/ipsec/profile
add dh-group=modp2048 enc-algorithm=aes-128 name=ike1-site2
/ip/ipsec/proposal
add enc-algorithms=aes-128-cbc name=ike1-site2 pfs-group=modp2048
```

繼續配置 peer。指定遠端路由器的地址。此地址應可透過 UDP/500 和 UDP/4500 埠訪問，因此請確保針對路由器防火牆採取適當措施。還要指定此 peer 的名稱以及新建立的 profile。

```ros
/ip/ipsec/peer
add address=192.168.80.1/32 name=ike1-site2 profile=ike1-site2
```

下一步是建立 identity。對於基本的使用預共享金鑰保護的隧道，只需設定一個 **強** secret 以及此 identity 所適用的 peer。

```ros
/ip/ipsec/identity
add peer=ike1-site2 secret=thisisnotasecurepsk
```

:::danger
如果安全性很重要，請考慮使用 IKEv2 和其他 auth-method。
:::

最後，建立一個策略來控制應在哪些網路/主機之間加密流量。

```ros
/ip/ipsec/policy
add src-address=10.1.202.0/24 src-port=any dst-address=10.1.101.0/24 dst-port=any tunnel=yes action=encrypt proposal=ike1-site2 peer=ike1-site2
```

#### **站點 2 配置** {#site-2-configuration}

Office 2 的配置與 Office 1 幾乎相同，只需使用正確的 IP 地址配置。首先建立新的 Phase 1 配置檔案和 Phase 2 提議條目：

```ros
/ip/ipsec/profile
add dh-group=modp2048 enc-algorithm=aes-128 name=ike1-site1
/ip/ipsec/proposal
add enc-algorithms=aes-128-cbc name=ike1-site1 pfs-group=modp2048
```

接下來是對等體和身份：

```ros
/ip/ipsec/peer
add address=192.168.90.1/32 name=ike1-site1 profile=ike1-site1
/ip/ipsec/identity
add peer=ike1-site1 secret=thisisnotasecurepsk
```

完成後，建立策略：

```ros
/ip/ipsec/policy
add src-address=10.1.101.0/24 src-port=any dst-address=10.1.202.0/24 dst-port=any tunnel=yes action=encrypt proposal=ike1-site1 peer=ike1-site1
```

此時，隧道應已建立，並且兩個路由器上都應建立兩個 IPsec 安全關聯：

```ros
/ip/ipsec
active-peers print
installed-sa print
```

#### **NAT 和 Fasttrack 繞過** {#nat-and-fasttrack-bypass}

此時如果嘗試透過 IPsec 隧道傳送流量，則無法工作；封包會丟失。這是因為兩臺路由器都有 NAT 規則（偽裝），會在封包加密之前更改源地址。路由器無法加密該封包，因為源地址與 policy 配置中指定的地址不匹配。更多資訊請參閱 IPsec 封包流示例。

要解決此問題，需要設定 IP/Firewall/NAT 繞過規則。

Office 1 路由器：

```ros
/ip/firewall/nat
add chain=srcnat action=accept place-before=0 src-address=10.1.202.0/24 dst-address=10.1.101.0/24
```

Office 2 路由器：

```ros
/ip/firewall/nat
add chain=srcnat action=accept place-before=0 src-address=10.1.101.0/24 dst-address=10.1.202.0/24
```

:::warning
如果你在新增 NAT 繞過規則之前嘗試建立 IP 連線，則必須從連線表中清除現有連線，或重啟兩個路由器。
:::

確保繞過規則位於所有其他 NAT 規則之前。

另一個問題是，如果啟用了 IP/Fasttrack，封包會繞過 IPsec 策略。因此需要在 FastTrack 之前新增 accept 規則。

```ros
/ip/firewall/filter
add chain=forward action=accept place-before=1
src-address=10.1.101.0/24 dst-address=10.1.202.0/24 connection-state=established,related
add chain=forward action=accept place-before=1
src-address=10.1.202.0/24 dst-address=10.1.101.0/24 connection-state=established,related
```

但是，如果有相當數量的隧道並且每個隧道上都有大量流量，這可能會給路由器 CPU 增加顯著負載。

解決方案是使用 IP/Firewall/Raw 繞過連線跟蹤，從而無需上述過濾規則，並將 CPU 負載降低約 30%。

```ros
/ip/firewall/raw
add action=notrack chain=prerouting src-address=10.1.101.0/24 dst-address=10.1.202.0/24
add action=notrack chain=prerouting src-address=10.1.202.0/24 dst-address=10.1.101.0/24
```

### 使用 DNS 的站點到站點 GRE over IPsec (IKEv2) 隧道 {#site-to-site-gre-tunnel-over-ipsec-ikev2-using-dns}

此示例說明當其中一個或兩個站點沒有靜態 IP 地址時，如何在兩臺 RouterOS 裝置之間建立安全且加密的 GRE 隧道。在此之前，必須為其中一臺充當響應方（伺服器）的裝置分配 DNS 名稱。為簡單起見，此示例使用 RouterOS 內建的 DDNS 服務 IP/Cloud。

![](/img/a4224852afe39ede.webp)

#### 站點 1（伺服器）配置 {#site-1-server-configuration}

此側監聽傳入連線並充當響應方。使用 mode config 為第二個站點提供 IP 地址。首先，建立一個 loopback（空白）網橋，併為其分配一個稍後用於建立 GRE 隧道的 IP 地址。

```ros
/interface/bridge 
add name=loopback
/ip/address
add address=192.168.99.1 interface=loopback
```

繼續配置 IPsec，首先建立新的階段 1 profile 和階段 2 proposal 條目，使用適合你需求的更強或更弱加密引數。此配置示例監聽所有傳入的 IKEv2 請求，這意味著該 profile 配置會在所有其他配置（例如 RoadWarrior）之間共享。

```ros
/ip/ipsec/profile
add dh-group=ecp256,modp2048,modp1024 enc-algorithm=aes-256,aes-192,aes-128 name=ike2
/ip/ipsec/proposal
add auth-algorithms=null enc-algorithms=aes-128-gcm name=ike2-gre pfs-group=none
```

接下來，建立一個 responder=yes 的新 mode config 條目。這會為另一站點提供 IP 配置，併為 policy 生成提供主機（loopback 地址）。

```ros
/ip/ipsec/mode-config
add address=192.168.99.2 address-prefix-length=32 name=ike2-gre split-include=192.168.99.1/32 system-dns=no
```

應建立一個新的策略組，將此配置與任何現有或未來的 IPsec 配置分開。

```ros
/ip/ipsec/policy/group
add name=ike2-gre
```

現在設定一個新的策略模板，匹配遠端 peer 的新動態地址和 loopback 地址。

```ros
/ip/ipsec/policy
add dst-address=192.168.99.2/32 group=ike2-gre proposal=ike2-gre src-address=192.168.99.1/32 template=yes
```

下一步是建立監聽所有 IKEv2 請求的 peer 配置。如果已有此類條目，可以跳過此步驟。

```ros
/ip/ipsec/peer
add exchange-mode=ike2 name=ike2 passive=yes profile=ike2
```

最後，設定一個 identity，透過使用特定 secret 的預共享金鑰認證來匹配遠端 peer。

```ros
/ip/ipsec/identity
add generate-policy=port-strict mode-config=ike2-gre peer=ike2 policy-template-group=ike2-gre secret=test
```

伺服器端現在已配置完成，並監聽所有 IKEv2 請求。確保防火牆沒有阻止 UDP/4500 埠。

最後一步是建立 GRE 介面本身。也可以在以後從用戶端建立 IPsec 連線時執行此操作。

```ros
/interface/gre
add local-address=192.168.99.1 name=gre-tunnel1 remote-address=192.168.99.2
```

配置 IP 地址以及透過 GRE 介面到遠端網路的路由。

```ros
/ip/address
add address=172.16.1.1/30 interface=gre-tunnel1
/ip/route
add dst-address=10.1.202.0/24 gateway=172.16.1.2
```

#### 站點 2（用戶端）配置 {#site-2-client-configuration}

與伺服器配置類似，首先建立新的階段 1 profile 和階段 2 proposal 配置。由於此站點是發起方，你可以使用更具體的 profile 配置來控制使用哪些確切的加密引數，只需確保它們與伺服器端配置有重疊。

```ros
/ip/ipsec/profile
add dh-group=ecp256 enc-algorithm=aes-256 name=ike2-gre
/ip/ipsec/proposal
add auth-algorithms=null enc-algorithms=aes-128-gcm name=ike2-gre pfs-group=none
```

接下來，建立一個 responder=no 的新 mode config 條目。這會確保 peer 從伺服器請求 IP 和拆分網路配置。

```ros
/ip/ipsec/mode-config
add name=ike2-gre responder=no
```

還應建立一個新的策略組，將此配置與任何現有或未來的 IPsec 配置分開。

```ros
/ip/ipsec/policy/group
add name=ike2-gre
```

同時在用戶端側建立新的策略模板。

```ros
/ip/ipsec/policy
add dst-address=192.168.99.1/32 group=ike2-gre proposal=ike2-gre src-address=192.168.99.2/32 template=yes
```

繼續配置 peer。在 address 引數下指定伺服器的 DNS 名稱。也可以使用 IP 地址。

```ros
/ip/ipsec/peer
add address=n.mynetname.net exchange-mode=ike2 name=p1.ez profile=ike2-gre
```

最後，為新建立的 peer 建立 identity。

```ros
/ip/ipsec/identity
add generate-policy=port-strict mode-config=ike2-gre peer=p1.ez policy-template-group=ike2-gre secret=test
```

如果一切配置正確，會出現新的動態策略。

```ros
/ip/ipsec/policy/print 
Flags: T - template, X - disabled, D - dynamic, I - invalid, A - active, * - default 
0 T * group=default src-address=::/0 dst-address=::/0 protocol=all proposal=default template=yes

1 T group=ike2-gre src-address=192.168.99.2/32 dst-address=192.168.99.1/32 protocol=all proposal=ike2-gre template=yes

2 DA src-address=192.168.99.2/32 src-port=any dst-address=192.168.99.1/32 dst-port=any protocol=all action=encrypt level=unique ipsec-protocols=esp 
tunnel=yes sa-src-address=192.168.90.1 sa-dst-address=(current IP of n.mynetname.net) proposal=ike2-gre ph2-count=1 
```

現在兩個站點之間已建立安全隧道，它會加密 192.168.99.2 \<=> 192.168.99.1 地址之間的所有流量。使用這些地址建立 GRE 隧道。

```ros
/interface/gre
add local-address=192.168.99.2 name=gre-tunnel1 remote-address=192.168.99.1
```

配置 IP 地址以及透過 GRE 介面到遠端網路的路由。

```ros
/ip/address
add address=172.16.1.2/30 interface=gre-tunnel1
/ip/route
add dst-address=10.1.101.0/24 gateway=172.16.1.1
```

### 使用 IKEv2 和 RSA 認證的 Road Warrior 設定 {#road-warrior-setup-using-ikev2-with-rsa-authentication}

此示例說明如何在連線到 Internet 的裝置（road warrior 用戶端）與執行 RouterOS 並充當伺服器的裝置之間建立安全的 IPsec 連線。

![](/img/15261a1aca9285d4.webp)

#### RouterOS 伺服器配置 {#routeros-server-configuration}

在配置 IPsec 之前，必須設定證書。你可以使用單獨的 Certificate Authority 進行證書管理；但在本例中，自簽名證書會在 RouterOS 的 System/Certificates 選單中生成。要將各種裝置連線到伺服器，必須滿足一些證書要求：

- common name 必須包含伺服器的 IP 或 DNS 名稱。
- SAN（subject alternative name）必須包含伺服器的 IP 或 DNS 名稱。
- 需要 EKU（extended key usage）tls-server 和 tls-client。

考慮到上述要求，生成 CA 和伺服器證書：

```ros
/certificate
add common-name=ca name=ca
sign ca ca-crl-host=2.2.2.2
add common-name=2.2.2.2 subject-alt-name=IP:2.2.2.2 key-usage=tls-server name=server1
sign server1 ca=ca
```

在路由器上建立有效證書後，新增新的階段 1 profile 和階段 2 proposal 條目，並設定 pfs-group=none：

```ros
/ip/ipsec/profile
add name=ike2
/ip/ipsec/proposal
add name=ike2 pfs-group=none
```

Mode config 用於從 IP/Pools 分配地址：

```ros
/ip/pool
add name=ike2-pool ranges=192.168.77.2-192.168.77.254
/ip/ipsec/mode-config
add address-pool=ike2-pool address-prefix-length=32 name=ike2-conf
```

由於必須調整策略模板以僅允許特定網路策略，應建立一個單獨的 policy group 和模板。

```ros
/ip/ipsec/policy/group
add name=ike2-policies
/ip/ipsec/policy
add dst-address=192.168.77.0/24 group=ike2-policies proposal=ike2 src-address=0.0.0.0/0 template=yes
```

建立新的 IPsec peer 條目，監聽所有傳入的 IKEv2 請求。

```ros
/ip/ipsec/peer
add exchange-mode=ike2 name=ike2 passive=yes profile=ike2
```

##### 身份配置 {#identity-configuration}

identity 選單允許匹配特定遠端 peer，併為每個 peer 分配不同配置。首先，建立一個預設 identity，接受所有 peer，但使用 peer 的證書驗證其身份。

```ros
/ip/ipsec/identity
add auth-method=digital-signature certificate=server1 generate-policy=port-strict mode-config=ike2-conf peer=ike2 policy-template-group=ike2-policies
```

:::warning
如果 peer 的 ID（ID\_i）與其傳送的證書不匹配，identity 查詢會失敗。請參閱 identities 部分中的 remote-id。
:::

例如，要為使用證書“rw-client1”向伺服器認證的使用者“A”分配不同的 mode config，首先確保已建立好供該特定使用者使用的新 mode config。

```ros
/ip/ipsec/mode-config
add address=192.168.66.2 address-prefix-length=32 name=usr_A split-include=192.168.55.0/24 system-dns=no
```

使用 match-by=certificate 為使用者“A”應用此配置，並透過 remote-certificate 指定證書。

```ros
/ip/ipsec/identity
add auth-method=digital-signature certificate=server1 generate-policy=port-strict match-by=certificate mode-config=usr_A peer=ike2 policy-template-group=ike2-policies remote-certificate=rw-client1
```

##### （可選）拆分隧道配置 {#optional-split-tunnel-configuration}

拆分隧道是一種方法，允許 road warrior 用戶端僅訪問特定的受保護網路，同時根據其內部路由表傳送其餘流量（而不是透過隧道傳送所有流量）。要配置拆分隧道，請更改 mode config 引數。

例如，允許 road warrior 用戶端僅訪問 10.5.8.0/24 網路。

```ros
/ip/ipsec/mode-conf
set [find name="rw-conf"] split-include=10.5.8.0/24
```

還可以傳送特定的 DNS 伺服器供用戶端使用。預設使用 system-dns=yes，這會發送路由器自身在 IP/DNS 中配置的 DNS 伺服器。使用 static-dns 引數強制用戶端使用不同的 DNS 伺服器。

```ros
/ip/ipsec/mode-conf
set [find name="rw-conf"] system-dns=no static-dns=10.5.8.1
```

雖然可以調整 IPsec 策略模板，僅允許 road warrior 用戶端為 split-include 引數配置的網路生成策略，但這會導致與不同廠商實現的相容性問題（參見已知限制）。與其調整策略模板，不如在 IP/Firewall/Filter 中允許訪問受保護網路，並丟棄其他所有流量。

```ros
/ip/firewall/filter
add action=drop chain=forward src-address=192.168.77.0/24 dst-address=!10.5.8.0/24
```

:::warning
拆分網路不是安全措施。用戶端（發起方）仍然可以請求不同的 Phase 2 流量選擇器。
:::

##### 生成用戶端證書 {#generating-client-certificates}

要為用戶端生成新證書並使用之前建立的 CA 對其進行簽名。

```ros
/certificate
add common-name=rw-client1 name=rw-client1 key-usage=tls-client
sign rw-client1 ca=ca
```

大多數用戶端實現接受 **PKCS12 格式**，因此匯出證書時，請確保指定 PKCS12。

```ros
/certificate
export-certificate rw-client1 export-passphrase=1234567890 type=pkcs12
```

現在，路由器 System/File 部分中有一個名為 *cert\_export\_rw-client1.p12* 的檔案。此檔案應安全地傳輸到用戶端裝置。

PKCS12 包還包含 CA 證書，但某些廠商不會安裝此 CA，因此必須單獨以 PEM 格式匯出自簽名 CA 證書。

```ros
/certificate
export-certificate ca type=pem
```

現在，路由器 System/File 部分中有一個名為 *cert\_export\_ca.crt* 的檔案。此檔案也應安全地傳輸到用戶端裝置。

**PEM** 是另一種證書格式，用於不支援 PKCS12 的用戶端軟體。原理基本相同。

```ros
/certificate
export-certificate ca
export-certificate rw-client1 export-passphrase=1234567890
```

現在，路由器的 Files 部分中有三個檔案：*cert\_export\_ca.crt*、*cert\_export\_rw-client1.crt* 和 *cert\_export\_rw-client1.key*，它們應安全地傳輸到用戶端裝置。

##### 已知限制 {#known-limitations}

以下是流行用戶端軟體 IKEv2 實現的已知限制列表。

- Windows 總是忽略透過 split-include 收到的網路，並請求目的地址為 0.0.0.0/0（TSr）的策略。生成 IPsec-SA 後，Windows 會請求 DHCP option 249，RouterOS 會自動用配置的 split-include 網路進行響應。

- Apple macOS 和 iOS 都只接受第一個 split-include 網路。

- Apple macOS 和 iOS 僅在使用了 0.0.0.0/0 split-include 時，才使用 system-dns 和 static-dns 引數中的 DNS 伺服器。

- 雖然某些實現可以在階段 2 使用不同的 PFS 組，但請使用 proposal 下的 pfs-group=none 以避免任何相容性問題。

#### RouterOS 用戶端配置 {#routeros-client-configuration}

在 RouterOS 中匯入 PKCS12 格式證書。

```ros
/certificate/import file-name=cert_export_RouterOS_client.p12 passphrase=1234567890
```

自簽名 CA 證書和用戶端證書現在會出現在 Certificate 選單中。找到用戶端證書的名稱。

```ros
/certificate/print
```

**cert\_export\_RouterOS\_client.p12\_0** 是用戶端證書。

應建立單獨的階段 1 profile 和階段 2 proposal 配置，以免干擾任何現有 IPsec 配置。

```ros
/ip/ipsec/profile
add name=ike2-rw
/ip/ipsec/proposal
add name=ike2-rw pfs-group=none
```

雖然可以使用預設策略模板進行策略生成，但應建立新的策略組和模板，將此配置與任何其他 IPsec 配置分開。

```ros
/ip/ipsec/policy/group
add name=ike2-rw
/ip/ipsec/policy
add group=ike2-rw proposal=ike2-rw template=yes
```

建立一個 responder=no 的新 mode config 條目，從伺服器請求配置引數。

```ros
/ip/ipsec/mode-config
add name=ike2-rw responder=no
```

最後，建立對等體和身份配置。

```ros
/ip/ipsec/peer
add address=2.2.2.2/32 exchange-mode=ike2 name=ike2-rw-client
/ip/ipsec/identity
add auth-method=digital-signature certificate=cert_export_RouterOS_client.p12_0 generate-policy=port-strict mode-config=ike2-rw peer=ike2-rw-client policy-template-group=ike2-rw
```

驗證連線已成功建立。

```ros
/ip/ipsec
active-peers print
installed-sa print
```

##### 啟用動態源 NAT 規則生成 {#enabling-dynamic-source-nat-rule-generation}

生成的動態策略表明，只有具有特定（由 mode config 接收）源地址的流量才會透過隧道傳送。在大多數情況下，路由器需要將特定裝置或網路路由到隧道中。在這種情況下，使用源 NAT 將封包的源地址改為與 mode config 地址匹配。由於 mode config 地址是動態的，無法建立靜態源 NAT 規則。在 RouterOS 中，可以為 mode config 用戶端生成動態源 NAT 規則。

![](/img/f2c4abd8b00ecd03.webp)

例如，本地網路 192.168.88.0/24 位於路由器之後，來自該網路的所有流量都應透過隧道傳送。首先，建立一個包含該本地網路的新 IP/Firewall/Address list。

```ros
/ip/firewall/address-list
add address=192.168.88.0/24 list=local
```

完成後，將新建立的 IP/Firewall/Address list 分配給 mode config 配置。

```ros
/ip/ipsec/mode-config
set [ find name=ike2-rw ] src-address-list=local
```

驗證隧道建立時是否正確動態生成了源 NAT 規則。

```ros
[admin@MikroTik] > /ip/firewall/nat/print 
Flags: X - disabled, I - invalid, D - dynamic 
0 D ;;; ipsec mode-config
chain=srcnat action=src-nat to-addresses=192.168.77.254 src-address-list=local dst-address-list=!local
```

:::danger
確保動態 mode config 地址不屬於本地網路。
:::

#### Windows 用戶端配置 {#windows-client-configuration}

在 Windows 計算機上開啟 PKCS12 格式證書檔案。按照說明安裝證書。選擇“本地計算機”儲存位置。![](/img/7f0720a59f02c365.webp) 現在可以繼續進入網路和 Internet 設定 -> VPN，並新增新配置。填寫連線名稱、伺服器名稱或地址引數。在 VPN 型別下選擇 IKEv2。完成後，選擇“使用計算機證書”。這可以在網路和共享中心中透過單擊該 VPN 連線的“屬性”選單完成。該設定位於“安全”標籤頁下。

![](/img/d60e9d2292526217.webp)

Windows 10 與以下階段 1（profiles）和階段 2（proposals）proposal 集相容：

| 階段 1 |  |  |
| :-- | :-- | :-- |
| 雜湊演算法 | 加密演算法 | DH 組 |
| SHA1 | 3DES | modp1024 |
| SHA256 | 3DES | modp1024 |
| SHA1 | AES-128-CBC | modp1024 |
| SHA256 | AES-128-CBC | modp1024 |
| SHA1 | AES-192-CBC | modp1024 |
| SHA256 | AES-192-CBC | modp1024 |
| SHA1 | AES-256-CBC | modp1024 |
| SHA256 | AES-256-CBC | modp1024 |
| SHA1 | AES-128-GCM | modp1024 |
| SHA256 | AES-128-GCM | modp1024 |
| SHA1 | AES-256-GCM | modp1024 |
| SHA256 | AES-256-GCM | modp1024 |

| 階段 2 |  |  |
| :-- | :-- | :-- |
| 雜湊演算法 | 加密演算法 | PFS 組 |
| SHA1 | AES-256-CBC | none |
| SHA1 | AES-128-CBC | none |
| SHA1 | 3DES | none |
| SHA1 | DES | none |
| SHA1 | none | none |

#### macOS 用戶端配置 {#macos-client-configuration}

在 macOS 計算機上開啟 PKCS12 格式證書檔案，並將證書安裝到“系統”鑰匙串。由於 CA 證書是自簽名的，請手動將其標記為受信任。在 macOS 鑰匙串訪問 App 的“系統”標籤頁中找到該證書，並將其標記為“始終信任”。

![](/img/ae8f9610163925e0.webp)

現在可以轉到 System Preferences -> Network，並單擊 + 按鈕新增新配置。選擇 Interface: VPN、VPN Type: IKEv2，併為連線命名。Remote ID 必須設定為等於伺服器證書的 common-name 或 subjAltName。Local ID 可以留空。在 Authentication Settings 下選擇 None，並選擇用戶端證書。現在可以測試連線。

![](/img/98ab138f5ea6d75a.webp)

macOS 與以下階段 1（profiles）和階段 2（proposals）proposal 集相容：

| 階段 1 |  |  |
| :-- | :-- | :-- |
| 雜湊演算法 | 加密演算法 | DH 組 |
| SHA256 | AES-256-CBC | modp2048 |
| SHA256 | AES-256-CBC | ecp256 |
| SHA256 | AES-256-CBC | modp1536 |
| SHA1 | AES-128-CBC | modp1024 |
| SHA1 | 3DES | modp1024 |

| 階段 2 |  |  |
| :-- | :-- | :-- |
| 雜湊演算法 | 加密演算法 | PFS 組 |
| SHA256 | AES-256-CBC | none |
| SHA1 | AES-128-CBC | none |
| SHA1 | 3DES | none |

#### iOS 用戶端配置 {#ios-client-configuration}

通常，PKCS12 包還包含 CA 證書，但 iOS 不會安裝此 CA，因此必須單獨以 PEM 格式安裝自簽名 CA 證書。在 iOS 裝置上開啟這些檔案，並按照說明安裝兩個證書。在 iOS 裝置上將自簽名 CA 證書標記為受信任。這可以在“設定”->“通用”->“關於本機”->“證書信任設定”選單中完成。完成後，在“設定”->“通用”->“描述檔案”選單下檢查兩個證書是否都標記為“已驗證”。

![](/img/b5ea33be6cc87db1.webp)

現在可以轉到 Settings -> General -> VPN 選單並新增新配置。Remote ID 必須設定為等於伺服器證書的 common-name 或 subjAltName。Local ID 可以留空。

![](/img/a0ba071bd82f918b.webp)

iOS 與以下階段 1（profiles）和階段 2（proposals）proposal 集相容：

| 階段 1 |  |  |
| :-- | :-- | :-- |
| 雜湊演算法 | 加密演算法 | DH 組 |
| SHA256 | AES-256-CBC | modp2048 |
| SHA256 | AES-256-CBC | ecp256 |
| SHA256 | AES-256-CBC | modp1536 |
| SHA1 | AES-128-CBC | modp1024 |
| SHA1 | 3DES | modp1024 |

| 階段 2 |  |  |
| :-- | :-- | :-- |
| 雜湊演算法 | 加密演算法 | PFS 組 |
| SHA256 | AES-256-CBC | none |
| SHA1 | AES-128-CBC | none |
| SHA1 | 3DES | none |

:::warning
如果你透過 WiFi 連線到 VPN，iOS 裝置可能會進入睡眠模式並與網路斷開連線。
:::

#### Android (strongSwan) 用戶端配置 {#android-strongswan-client-configuration}

Android 沒有原生 IKEv2 支援，但可以使用 Google Play 商店中的 strongSwan，它為 Android 帶來 IKEv2。strongSwan 接受 PKCS12 格式證書，因此在 strongSwan 中設定 VPN 連線之前，請將 PKCS12 包下載到 Android 裝置。完成後，在 strongSwan 中建立新的 VPN 配置檔案，輸入伺服器 IP，並選擇“IKEv2 Certificate”作為 VPN 型別。選擇使用者證書時，按“安裝”，並按照證書提取過程指定 PKCS12 包。儲存配置檔案，並透過按 VPN 配置檔案測試連線。

![](/img/f1154362a91b750c.webp)

可以透過勾選“顯示高階設定”複選框，在 strongSwan 中指定自定義加密設定。strongSwan 預設與以下階段 1（profiles）和階段 2（proposals）proposal 集相容：

| 階段 1 |  |  |
| :-- | :-- | :-- |
| 雜湊演算法 | 加密演算法 | DH 組 |
| SHA\* | AES-\*-CBC | modp2048 |
| SHA\* | AES-\*-CBC | ecp256 |
| SHA\* | AES-\*-CBC | ecp384 |
| SHA\* | AES-\*-CBC | ecp521 |
| SHA\* | AES-\*-CBC | modp3072 |
| SHA\* | AES-\*-CBC | modp4096 |
| SHA\* | AES-\*-CBC | modp6144 |
| SHA\* | AES-\*-CBC | modp8192 |
| SHA\* | AES-\*-GCM | modp2048 |
| SHA\* | AES-\*-GCM | ecp256 |
| SHA\* | AES-\*-GCM | ecp384 |
| SHA\* | AES-\*-GCM | ecp521 |
| SHA\* | AES-\*-GCM | modp3072 |
| SHA\* | AES-\*-GCM | modp4096 |
| SHA\* | AES-\*-GCM | modp6144 |
| SHA\* | AES-\*-GCM | modp8192 |

| 階段 2 |  |  |
| :-- | :-- | :-- |
| 雜湊演算法 | 加密演算法 | PFS 組 |
| none | AES-256-GCM | none |
| none | AES-128-GCM | none |
| SHA256 | AES-256-CBC | none |
| SHA512 | AES-256-CBC | none |
| SHA1 | AES-256-CBC | none |
| SHA256 | AES-192-CBC | none |
| SHA512 | AES-192-CBC | none |
| SHA1 | AES-192-CBC | none |
| SHA256 | AES-128-CBC | none |
| SHA512 | AES-128-CBC | none |
| SHA1 | AES-128-CBC | none |

#### Linux (strongSwan) 用戶端配置 {#linux-strongswan-client-configuration}

下載 PKCS12 證書捆綁包，並將其移動到 `/etc/ipsec`.d/private 目錄。

將匯出的私鑰密碼短語新增到 `/etc/ipsec`.secrets 檔案，其中 "strongSwan\_client.p12" 是檔名，"1234567890" 是密碼短語。

```bash
: P12 strongSwan_client.p12 "1234567890"
```

將新連線新增到 `/etc/ipsec`.conf 檔案

```bash
conn "ikev2"
keyexchange=ikev2
ike=aes128-sha1-modp2048
esp=aes128-sha1
leftsourceip=%modeconfig
leftcert=strongSwan_client.p12
leftfirewall=yes
right=2.2.2.2
rightid="CN=2.2.2.2"
rightsubnet=0.0.0.0/0
auto=add
```

現在可以重新啟動（或啟動）ipsec 守護程式並初始化連線。

```bash
ipsec restart
ipsec up ikev2
```

### 使用 IKEv2 和由 User Manager 處理的 EAP-MSCHAPv2 認證的 Road Warrior 設定（RouterOS v7） {#road-warrior-setup-using-ikev2-with-eap-mschapv2-authentication-handled-by-user-manager-routeros-v7}

此示例說明如何在連線到網際網路的裝置（road warrior 用戶端）與執行 RouterOS 並充當 IKEv2 伺服器和 User Manager 的裝置之間建立安全的 IPsec 連線。可以在網路中的單獨裝置上執行 User Manager，但在本例中，User Manager 和 IKEv2 伺服器都配置在同一裝置（Office）上。

![](/img/15261a1aca9285d4.webp)

#### RouterOS 伺服器配置 {#routeros-server-configuration-1}

##### 要求 {#requirements}

要使此設定正常工作，必須滿足以下前提條件：

1. 路由器的 IP 地址必須有有效的公網 DNS 記錄——IP Cloud 可以提供該記錄。
2. 路由器必須可透過網際網路上的 TCP/80 埠訪問——如果伺服器位於 NAT 之後，請配置埠轉發。
3. 路由器上必須安裝 User Manager 包。

##### 生成 Let's Encrypt 證書 {#generating-lets-encrypt-certificate}

EAP-MSCHAPv2 認證需要 TLS 握手，因此伺服器必須具有用戶端可以驗證的證書。為簡化此步驟，請使用大多數作業系統無需使用者干預即可驗證的 Let's Encrypt 證書。要生成證書，請在 Certificates 選單下啟用 SSL 證書。預設情況下，該命令使用 IP Cloud 提供的動態 DNS 記錄，但也可以指定自定義 DNS 名稱。DNS 記錄應指向該路由器。

```ros
/certificate/enable-ssl-certificate
```

如果證書生成成功，Let's Encrypt 證書會顯示已安裝在 Certificates 選單下。

```ros
/certificate/print detail where name~"letsencrypt"
```

##### 配置 User Manager {#configuring-user-manager}

首先，允許來自 localhost（路由器本身）的 RADIUS 請求：

```ros
/user-manager/router
add address=127.0.0.1 comment=localhost name=local shared-secret=test
```

啟用 User Manager，並指定用於認證使用者的 Let's Encrypt 證書（將證書名稱替換為你裝置上安裝的證書名稱）。

```ros
/user-manager
set certificate="letsencrypt_2021-04-09T07:10:55Z" enabled=yes
```

最後，新增使用者及其憑據，供用戶端向伺服器認證時使用。

```ros
/user-manager/user
add name=user1 password=password
```

##### 配置 RADIUS 用戶端 {#configuring-radius-client}

要讓路由器使用 RADIUS 伺服器進行使用者認證，必須新增新的 RADIUS 用戶端，其共享金鑰與 User Manager 上已配置的相同。

```ros
/radius
add address=127.0.0.1 secret=test service=ipsec
```

##### IPsec (IKEv2) 伺服器配置 {#ipsec-ikev2-server-configuration}

新增 pfs-group=none 的新 Phase 1 配置檔案和 Phase 2 提議條目：

```ros
/ip/ipsec/profile
add name=ike2
/ip/ipsec/proposal
add name=ike2 pfs-group=none
```

Mode config 用於從 IP/Pools 分配地址。

```ros
/ip/pool
add name=ike2-pool ranges=192.168.77.2-192.168.77.254
/ip/ipsec/mode-config
add address-pool=ike2-pool address-prefix-length=32 name=ike2-conf
```

由於必須調整策略模板以僅允許特定網路策略，應建立一個單獨的 policy group 和模板。

```ros
/ip/ipsec/policy/group
add name=ike2-policies
/ip/ipsec/policy
add dst-address=192.168.77.0/24 group=ike2-policies proposal=ike2 src-address=0.0.0.0/0 template=yes
```

建立新的 IPsec peer 條目，監聽所有傳入的 IKEv2 請求。

```ros
/ip/ipsec/peer
add exchange-mode=ike2 name=ike2 passive=yes profile=ike2
```

最後，建立新的 IPsec identity 條目，匹配所有嘗試使用 EAP 認證的用戶端。必須指定生成的 Let's Encrypt 證書。

```ros
/ip/ipsec/identity
add auth-method=eap-radius certificate="letsencrypt_2021-04-09T07:10:55Z" generate-policy=port-strict mode-config=ike2-conf peer=ike2 \
policy-template-group=ike2-policies
```

##### （可選）拆分隧道配置 {#optional-split-tunnel-configuration-1}

拆分隧道是一種方法，允許 road warrior 用戶端僅訪問特定的受保護網路，同時根據其內部路由表傳送其餘流量（而不是透過隧道傳送所有流量）。要配置拆分隧道，請更改 mode config 引數。

例如，允許 road warrior 用戶端僅訪問 10.5.8.0/24 網路。

```ros
/ip/ipsec/mode-conf
set [find name="rw-conf"] split-include=10.5.8.0/24
```

還可以傳送特定的 DNS 伺服器供用戶端使用。預設使用 system-dns=yes，這會發送路由器自身在 IP/DNS 中配置的 DNS 伺服器。使用 static-dns 引數強制用戶端使用不同的 DNS 伺服器。

```ros
/ip/ipsec/mode-conf
set [find name="rw-conf"] system-dns=no static-dns=10.5.8.1
```

:::warning
拆分網路不是安全措施。用戶端（發起方）仍然可以請求不同的 Phase 2 流量選擇器。
:::

##### （可選）為使用者分配靜態 IP 地址 {#optional-assigning-static-ip-address-to-user}

可以透過使用 RADIUS Framed-IP-Address 屬性為任何使用者分配靜態 IP 地址。

```ros
/user-manager/user
set [find name="user1"] attributes=Framed-IP-Address:192.168.77.100 shared-users=1
```

:::danger
為避免任何衝突，應從其他使用者的 IP 池中排除該靜態 IP 地址，並且應為該特定使用者將 shared-users 設定為 1。
:::

##### （可選）計費配置 {#optional-accounting-configuration}

要跟蹤每個使用者的執行時間、下載和上傳統計資訊，可以使用 RADIUS accounting。預設情況下，IPsec 的 RADIUS accounting 已啟用，但應配置 Interim Update 計時器，以定期向 RADIUS 伺服器傳送統計資訊。如果路由器處理許多併發會話，請增加更新計時器以避免 CPU 使用率過高。

```ros
/ip/ipsec/settings
set interim-update=1m
```

### 基本 L2TP/IPsec 設定 {#basic-l2tpipsec-setup}

此示例演示如何在 RouterOS 上輕鬆設定用於 road warrior 連線的 L2TP/IPsec 伺服器（適用於 Windows、Android、iOS、macOS 和其他廠商的 L2TP/IPsec 實現）。

#### RouterOS 伺服器配置 {#routeros-server-configuration-2}

第一步是啟用 L2TP 伺服器：

```ros
/interface/l2tp-server/server
set enabled=yes use-ipsec=required ipsec-secret=mySecret default-profile=default
```

use-ipsec 設定為 **required**，以確保僅接受 IPsec 封裝的 L2TP 連線。

這會啟用 L2TP 伺服器，並使用指定的 secret 建立動態 IPsec peer。

```ros
[admin@MikroTik] /ip/ipsec/peer> print 
0 D address=0.0.0.0/0 local-address=0.0.0.0 passive=yes port=500 
auth-method=pre-shared-key secret="123" generate-policy=port-strict 
exchange-mode=main-l2tp send-initial-contact=yes nat-traversal=yes 
hash-algorithm=sha1 enc-algorithm=3des,aes-128,aes-192,aes-256 
dh-group=modp1024 lifetime=1d dpd-interval=2m dpd-maximum-failures=5 
```

:::warning
如果存在靜態 IPsec 對等體配置，必須小心。
:::

下一步是建立 VPN 池並新增一些使用者。

```ros
/ip/pool/add name=vpn-pool range=192.168.99.2-192.168.99.100

/ppp/profile
set default local-address=192.168.99.1 remote-address=vpn-pool

/ppp/secret
add name=user1 password=123
add name=user2 password=234
```

現在路由器已準備好接受 L2TP/IPsec 用戶端連線。

#### RouterOS 用戶端配置 {#routeros-client-configuration-1}

要讓 RouterOS 作為 L2TP/IPsec 用戶端工作，只需新增新的 L2TP 用戶端即可。

```ros
/interface/l2tp-client
add connect-to=1.1.1.1 disabled=no ipsec-secret=mySecret name=l2tp-out1 \
password=123 use-ipsec=yes user=user1
```

這會自動建立動態 IPsec peer 和 policy 配置。

### 使用 XFRM 介面的基於路由的 IPsec {#route-based-ipsec-with-xfrm-interfaces}

基於策略的 IPsec 透過策略中的源地址和目的地址選擇流量。XFRM 介面增加了基於路由的模式：IPsec 策略組繫結到虛擬介面，流量被路由到該介面，而不是僅由策略選擇器匹配。這樣可以執行基於隧道的動態路由協定，並使用路由表決定哪些流量進入隧道。

XFRM 介面是其組內策略的隧道端點；使用 [`/interface/xfrm`](../../cli-reference/interface/xfrm.md) 進行配置。它的行為類似於常規介面：具有 IP 地址、最大傳輸單元和執行狀態。當使用該介面的 IPsec SA 建立後，會顯示 running 標誌。

考慮兩臺路由器透過 IPsec 隧道連線的設定。R1 使用 underlay 地址 203.0.113.1、LAN 192.168.51.0/28 和 XFRM 地址 192.168.50.1/24。R2 使用 underlay 地址 203.0.113.2、LAN 192.168.52.0/28 和 XFRM 地址 192.168.50.2/24。R1 發起連線，R2 是響應方。請將地址和預共享金鑰替換為你自己的值。

#### 使用場景 {#use-cases}

- 基於 IPsec 的動態路由：分支機構有多個 LAN，並會隨著時間增加新子網。使用基於策略的 IPsec 時，每對本地和遠端子網都需要自己的策略。使用 XFRM 介面時，分支機構透過隧道執行 OSPF，並透過 `xfrm1` 路由總部網路；無需新增 IPsec 策略即可通告和訪問新子網。
- 多 WAN 和策略路由：由於隧道是一條路由，可以使用路由標記或 VRF 將選定流量引導到 `xfrm1`，並且隧道可以在 WAN 鏈路之間故障轉移，而無需更改 IPsec 策略。

#### R1 配置 {#r1-configuration}

首先建立本地網橋、XFRM 介面及其 IP 地址：

```ros
/interface/bridge
add name=lan
/interface/xfrm
add name=xfrm1
/ip/address
add address=192.168.51.1/28 interface=lan
add address=192.168.50.1/24 interface=xfrm1
```

建立階段 1 profile 和階段 2 proposal 條目。這些引數必須在兩臺路由器上匹配：

```ros
/ip/ipsec/profile
add name=xfrm-example hash-algorithm=sha256 enc-algorithm=aes-256 dh-group=modp2048
/ip/ipsec/proposal
add name=xfrm-example auth-algorithms=sha256 enc-algorithms=aes-256-cbc pfs-group=none
```

建立一個專用策略組，並將其繫結到 XFRM 介面。專用組可將這些策略與路由器上的其他 IPsec 策略分開：

```ros
/ip/ipsec/policy/group
add name=xfrm1-group interface=xfrm1
```

配置 peer 和 identity。identity 必須使用與其 `policy-template-group` 相同的策略組：

```ros
/ip/ipsec/peer
add name=xfrm-example address=203.0.113.2/32 local-address=203.0.113.1 exchange-mode=ike2 profile=xfrm-example
/ip/ipsec/identity
add peer=xfrm-example auth-method=pre-shared-key secret=example-secret generate-policy=port-strict policy-template-group=xfrm1-group
```

新增用於 LAN 到 LAN 流量的策略，並透過該介面路由遠端 LAN：

```ros
/ip/ipsec/policy
add peer=xfrm-example group=xfrm1-group tunnel=yes src-address=192.168.51.0/28 dst-address=192.168.52.0/28 protocol=all action=encrypt level=require proposal=xfrm-example
/ip/route
add dst-address=192.168.52.0/28 gateway=xfrm1
```

#### R2 配置 {#r2-configuration}

R2 上的配置與 R1 對應。建立網橋、XFRM 介面及其 IP 地址：

```ros
/interface/bridge
add name=lan
/interface/xfrm
add name=xfrm1
/ip/address
add address=192.168.52.1/28 interface=lan
add address=192.168.50.2/24 interface=xfrm1
```

建立相同的 profile 和 proposal：

```ros
/ip/ipsec/profile
add name=xfrm-example hash-algorithm=sha256 enc-algorithm=aes-256 dh-group=modp2048
/ip/ipsec/proposal
add name=xfrm-example auth-algorithms=sha256 enc-algorithms=aes-256-cbc pfs-group=none
```

建立策略組、peer 和 identity：

```ros
/ip/ipsec/policy/group
add name=xfrm1-group interface=xfrm1
/ip/ipsec/peer
add name=xfrm-example address=203.0.113.1/32 local-address=203.0.113.2 exchange-mode=ike2 passive=yes profile=xfrm-example
/ip/ipsec/identity
add peer=xfrm-example auth-method=pre-shared-key secret=example-secret generate-policy=port-strict policy-template-group=xfrm1-group
```

新增策略和路由：

```ros
/ip/ipsec/policy
add peer=xfrm-example group=xfrm1-group tunnel=yes src-address=192.168.52.0/28 dst-address=192.168.51.0/28 protocol=all action=encrypt level=require proposal=xfrm-example
/ip/route
add dst-address=192.168.51.0/28 gateway=xfrm1
```

#### 驗證 {#verification}

檢查 XFRM 介面是否正在執行：

```ros
/interface/xfrm/print
```

`R` 標誌會在 IPsec SA 建立後出現。在此之前，分配給該介面的 IP 地址會顯示為無效。

檢查策略和活動 peer：

```ros
/ip/ipsec/policy/print detail
/ip/ipsec/active-peers/print detail
```

活動策略會顯示 `active-interface=xfrm1` 和 `ph2-state=established`。透過 ping 遠端 LAN 測試隧道：

```ros
/ping 192.168.52.1 src-address=192.168.51.1
```

#### MTU {#mtu}

`mtu` 屬性設定 XFRM 介面的第 3 層 MTU。預設值為 `1400` 位元組，這為 ESP 開銷留出了空間。只讀的 `actual-mtu` 屬性報告正在使用的值。對 `mtu` 的更改會立即生效。使用 `/interface print detail` 驗證有效值；如果 `actual-mtu` 與配置值不匹配，請再次設定 `mtu`。

#### 基於 XFRM 的 OSPF {#ospf-over-xfrm}

OSPF 可以透過 XFRM 介面執行。IPsec 策略必須匹配 OSPF 流量，包括組播 hello，因此在 XFRM 組中將 LAN 到 LAN 策略替換為 catch-all 策略。兩臺路由器還必須使用相同的有效 MTU；MTU 不匹配會使 OSPF 鄰居保持在 `ExStart`。

在 R1 上，替換策略並新增 OSPF 配置：

```ros
/ip/ipsec/policy
remove [find peer=xfrm-example]
add peer=xfrm-example group=xfrm1-group tunnel=yes src-address=0.0.0.0/0 dst-address=0.0.0.0/0 protocol=all action=encrypt level=require proposal=xfrm-example

/routing/ospf/instance
add name=xfrm-ospf version=2 router-id=192.168.50.1
/routing/ospf/area
add name=backbone instance=xfrm-ospf area-id=0.0.0.0
/routing/ospf/interface-template
add interfaces=xfrm1 area=backbone type=ptp
add networks=192.168.51.0/28 area=backbone
```

在 R2 上，使用 R2 的 router ID 和 LAN 網路進行相同配置：

```ros
/ip/ipsec/policy
remove [find peer=xfrm-example]
add peer=xfrm-example group=xfrm1-group tunnel=yes src-address=0.0.0.0/0 dst-address=0.0.0.0/0 protocol=all action=encrypt level=require proposal=xfrm-example

/routing/ospf/instance
add name=xfrm-ospf version=2 router-id=192.168.50.2
/routing/ospf/area
add name=backbone instance=xfrm-ospf area-id=0.0.0.0
/routing/ospf/interface-template
add interfaces=xfrm1 area=backbone type=ptp
add networks=192.168.52.0/28 area=backbone
```

檢查鄰居狀態：

```ros
/routing/ospf/neighbor/print
```

:::warning
XFRM 介面必須正在執行，流量才能透過它。如果 SA 建立後介面仍未啟動，請重新建立介面或重啟路由器。
:::

:::info
一個策略組只能繫結到一個 XFRM 介面。當你使用專用組時，將該身份的 `policy-template-group` 設定為該組，以便為該組中的策略建立 Phase 2 SA。

示例使用預共享金鑰。在生產環境中使用證書認證。
:::

### 故障排除/FAQ {#troubleshootingfaq}

#### Phase 1 無法獲取有效提議 {#phase-1-failed-to-get-a-valid-proposal}

```ros
[admin@MikroTik] /log> print
(..)
17:12:32 ipsec,error no suitable proposal found. 
17:12:32 ipsec,error 10.5.107.112 failed to get valid proposal. 
17:12:32 ipsec,error 10.5.107.112 failed to pre-process ph1 packet (side: 1, status 1). 
17:12:32 ipsec,error 10.5.107.112 phase1 negotiation failed. 
(..)
```

對等體無法協商加密引數，導致連線斷開。要解決此問題，請啟用 IPSec 偵錯日誌，找出遠端對等體提議的引數，並相應地調整配置。

```ros
[admin@MikroTik] /system/logging> add topics=ipsec,!debug
```

```ros
[admin@MikroTik] /log> print
(..)
17:21:08 ipsec rejected hashtype: DB(prop#1:trns#1):Peer(prop#1:trns#1) = MD5:SHA 
17:21:08 ipsec rejected enctype: DB(prop#1:trns#2):Peer(prop#1:trns#1) = 3DES-CBC:AES-CBC 
17:21:08 ipsec rejected hashtype: DB(prop#1:trns#2):Peer(prop#1:trns#1) = MD5:SHA 
17:21:08 ipsec rejected enctype: DB(prop#1:trns#1):Peer(prop#1:trns#2) = AES-CBC:3DES-CBC 
17:21:08 ipsec rejected hashtype: DB(prop#1:trns#1):Peer(prop#1:trns#2) = MD5:SHA 
17:21:08 ipsec rejected hashtype: DB(prop#1:trns#2):Peer(prop#1:trns#2) = MD5:SHA 
17:21:08 ipsec,error no suitable proposal found. 
17:21:08 ipsec,error 10.5.107.112 failed to get valid proposal. 
17:21:08 ipsec,error 10.5.107.112 failed to pre-process ph1 packet (side: 1, status 1). 
17:21:08 ipsec,error 10.5.107.112 phase1 negotiation failed. 
(..)
```

在此示例中，遠端端要求使用 SHA1 作為雜湊演算法，但本地路由器上配置的是 MD5。冒號符號 (:) 之前的設定配置在本地側，冒號符號 (:) 之後的引數配置在遠端側。

#### "phase1 negotiation failed due to time up" 是什麼意思？ {#phase1-negotiation-failed-due-to-time-up-what-does-it-mean}

對等方之間存在通訊問題。可能原因包括——階段 1 IP 地址配置錯誤；防火牆阻止 UDP 埠 500 和 4500；對等方之間的 NAT 未正確轉換 IPsec 協商封包。當 local-address 引數使用不當時，也可能出現此錯誤訊息。

#### 隨機丟包或隧道連線非常慢，啟用封包嗅探器/torch 後問題解決？ {#random-packet-drops-or-connections-over-the-tunnel-are-very-slow-enabling-packet-sniffertorch-fixes-the-problem}

問題在於，封包在封裝之前被髮送到 Fasttrack/FastPath，從而繞過 IPsec 策略檢查。解決方案是將需要封裝/解封裝的流量從 Fasttrack 中排除。

#### 如何啟用 ike2？ {#how-to-enable-ike2}

要為基本配置啟用 ike2，請將 peer 設定中的 exchange-mode 更改為 ike2。

#### 致命的 NO-PROPOSAL-CHOSEN 通知訊息？ {#fatal-no-proposal-chosen-notify-message}

遠端對等體傳送了一個通知，表示它無法接受提議的演算法。要查詢問題的確切原因，請檢視遠端對等體的偵錯日誌或配置，並驗證用戶端和伺服器是否具有相同的演算法集。

#### 我只能在一個方向 ping 通？ {#i-can-ping-only-in-one-direction}

此類情況下的典型問題是嚴格的防火牆：防火牆規則僅允許在一個方向上建立新連線。解決方案是重新檢查防火牆規則，或顯式接受所有應封裝/解封裝流量。

#### 我可以僅允許加密流量嗎？ {#can-i-allow-only-encrypted-traffic}

可以，請參見“僅允許 IPsec 封裝流量”示例。

#### 我在 StrongSwan 上啟用 IKEv2 REAUTH 並收到錯誤 'initiator did not reauthenticate as requested' {#i-enable-ikev2-reauth-on-strongswan-and-got-the-error-initiator-did-not-reauthenticate-as-requested}

RouterOS 不支援 rfc4478，必須在 StrongSwan 上停用 reauth。

#### XFRM 介面無法啟動 {#xfrm-interface-does-not-come-up}

`R` 標誌僅在使用該介面的 IPsec SA 建立後出現。如果 SA 已建立但介面仍處於 down 狀態，請重新建立介面或重啟路由器。在介面執行之前，介面上的 IP 地址會顯示為無效。

#### XFRM 策略一直處於 no-phase2 {#xfrm-policy-stays-in-no-phase2}

檢查策略組是否繫結到 XFRM 介面，identity 是否使用與其 `policy-template-group` 相同的組，以及流量是否透過 XFRM 介面路由。如果使用預設策略組，請檢查該組中沒有其他策略覆蓋此流量。

#### 基於 XFRM 的 OSPF 一直處於 ExStart {#ospf-over-xfrm-stays-in-exstart}

兩側的 XFRM 介面必須使用相同的有效 MTU。在兩臺路由器上使用 `/interface print detail` 檢查 `actual-mtu`，如果值不同，請再次設定 `mtu`。MTU 不匹配會阻止 OSPF 資料庫描述交換完成。
