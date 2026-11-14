---
sidebar_key: "virtual-private-networks/ipsec/index"
sidebar_position: 3
title: "IPsec"
sidebar_label: "IPsec"
description: "本節涵蓋 IPsec 示例與整合。可用它配置 IKEv2、pre-shared-key 和 post-quantum 金鑰工作流，以及第三方 VPN 連線。"
tags:
  - 'ipsec'
  - 'ike'
  - 'diffie-hellman'
source: https://manual.mikrotik.com/docs/7.24/virtual-private-networks/ipsec
captured_at: '2026-11-04T11:35:59+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節涵蓋 IPsec 示例和整合。可使用它配置 IKEv2、pre-shared-key 和後量子金鑰工作流，以及第三方 VPN 連線。

<DocCardList />

**Internet Protocol Security (IPsec)** 是由 Internet Engineering Task Force (IETF) 定義的一組協定，用於在 Internet 等未受保護的 IP/IPv6 網路上保護封包交換。

IPsec 協定套件可分為以下幾組：

- **Internet Key Exchange (IKE)** 協定，用於為 AH 和 ESP 動態生成和分發加密金鑰。
- **Authentication Header (AH)** RFC 4302。
- **Encapsulating Security Payload (ESP)** RFC 4303。

## Internet Key Exchange 協定 (IKE) {#internet-key-exchange-protocol-ike}

Internet Key Exchange (IKE) 是一種協定，為 Internet Security Association and Key Management Protocol (ISAKMP) 框架提供經過認證的金鑰材料。還有其他金鑰交換方案可與 ISAKMP 配合使用，但 IKE 是使用最廣泛的一種。二者共同提供了主機認證和安全關聯 (SA) 自動管理的手段。

大多數時間裡，IKE 守護程式處於空閒狀態。它被啟用時可能有兩種情況：

存在被策略規則匹配且需要加密或認證的流量，但該策略沒有任何 SA。策略會通知 IKE 守護程式，隨後 IKE 守護程式向遠端主機發起連線。IKE 守護程式也可以響應遠端連線。兩種情況下，對等體都會建立連線並執行 2 個階段：

- **Phase 1** - 對等體就後續 IKE 訊息中使用的演算法達成一致，並相互認證。還會生成用於派生所有 SA 的金鑰以及保護主機間後續 ISAKMP 交換的金鑰材料。此階段應匹配以下設定：
  - 認證方法
  - DH 組
  - 加密演算法
  - 交換模式
  - 雜湊演算法
  - NAT-T
  - DPD 和生命週期（可選）

- **Phase 2** - 對等體建立一個或多個 SA，供 IPsec 用於加密資料。由 IKE 守護程式建立的所有 SA 都具有生命週期值（可以是限制 SA 失效前的時間、此 SA 可加密的資料量，或二者兼有）。此階段應匹配以下設定：
  - IPsec 協定
  - 模式（隧道或傳輸）
  - 認證方法
  - PFS (DH) 組
  - 生命週期

:::warning
有兩種生命週期值 - 軟生命週期和硬生命週期。當 SA 達到軟生命週期閾值時，IKE 守護程式會收到通知，並啟動另一次 Phase 2 交換，用新的 SA 替換此 SA。如果 SA 達到硬生命週期，則會被丟棄。

**注意：** 如果生命週期到期時停用 DPD，則 Phase 1 不會重新生成金鑰；只有 Phase 2 會重新生成金鑰。要強制 Phase 1 重新生成金鑰，請啟用 DPD。

**注意：** 已知 PSK 認證在 "aggressive" 模式下容易受到離線攻擊，但最近的發現表明，在 "main" 和 "ike2" 交換模式下也可能進行離線攻擊。一般建議避免使用 PSK 認證方法。
:::

IKE 可以選擇提供完美前向保密 (PFS)，這是金鑰交換的一種屬性；對 IKE 而言，這意味著即使長期 Phase 1 金鑰被洩露，也無法輕易訪問透過此 Phase 1 建立的 SA 所保護的所有 IPsec 資料。這意味著會為每個 Phase 2 生成額外的金鑰材料。

金鑰材料的生成在計算上非常昂貴。例如，即使在非常快的計算機上，使用 modp8192 組也可能需要數秒。這通常每次 Phase 1 交換髮生一次，而 Phase 1 交換在任意主機對之間只發生一次，然後會保持很長時間。PFS 還會將此昂貴操作新增到每次 Phase 2 交換中。

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

較大的 DH 組提供更強的安全性，但需要更多 CPU 資源。以下是幾種常用的 DH 組，具有不同級別的安全性和 CPU 影響：

DH Group 14（2048 位） - 在安全性和 CPU 使用率之間提供實際平衡。它提供 2048 位金鑰交換，被認為對大多數現代應用是安全的，並得到廣泛支援。

DH Group 5（1536 位） - 提供比 DH Group 14 略低的安全性，但由於金鑰較小，CPU 開銷更低。對於許多場景仍被認為可接受。

DH Group 2（1024 位） - 應謹慎使用，因為它在常用組中提供的安全性最低。儘管 CPU 要求較低，但隨著計算能力提高，它更容易受到攻擊。通常不建議用於新部署。

為獲得最佳安全性，建議使用 **DH Group 19**。它通常被認為既快速又安全。除非需要與舊裝置相容，否則通常應避免使用 DH Group 2。

:::info
為網路基礎設施計算適當安全級別的推薦方法是：首先確定所需的安全位數，並估計解密受保護資料應花費多長時間。根據這些要求，然後可以選擇適當的演算法。參考請見 [https://www.keylength.com/en/4/](https://www.keylength.com/en/4/)。
:::

### IKE 流量 {#ike-traffic}

為避免 IKE 封包命中某些 SPD 規則並需要使用尚未建立的 SA（此封包可能正試圖建立該 SA）進行加密而引發問題，源埠為 UDP 500 的本地發起封包不經過 SPD 處理。同樣，要交付給本地的目的埠為 UDP 500 的封包不會在入站策略檢查中處理。

### 設定流程 {#setup-procedure}

要讓 IPsec 透過 IKE-ISAKMP 自動金鑰交換工作，必須配置 policy、peer 和 proposal（可選）條目。

:::danger
IPsec 對時間變化非常敏感。如果 IPsec 隧道兩端的時間同步不一致（例如，不同的 NTP 伺服器沒有使用相同時間戳更新時間），隧道會中斷，並且必須重新建立。
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
尚不支援 IKEv2 認證的 AES-GCM 加密。

**重要：** 如果使用帶 X.509 證書的 IPsec，證書必須包含 "SubjectKeyIdentifier" 擴充套件，該擴充套件僅在版本 3 中受支援。

**重要：** 尚不支援使用 ed25519 認證。
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

硬體加速透過使用 CPU 內建的加密引擎來執行更快的加密過程。

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

## 策略 {#policies}

策略表用於確定是否應對封包應用安全設定。

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*discard \| encrypt \| none*; 預設：**encrypt**) | 指定對策略匹配的封包執行什麼操作。none - 原樣傳遞封包。discard - 丟棄封包。encrypt - 應用此策略及其 SA 中指定的轉換。 |
| **comment** (*string*; 預設：) | 策略的簡短描述。 |
| **disabled** (*yes \| no*; 預設：**no**) | 策略是否用於匹配封包。 |
| **dst-address** (*IP/IPv6 prefix*; 預設：**0.0.0.0/32**) | 封包中要匹配的目標地址。適用於使用隧道模式（tunnel=yes）或模板（template=yes）時。 |
| **dst-port** (*integer:0..65535 \| any*; 預設：**any**) | 封包中要匹配的目標埠。如果設定為 any，則匹配所有埠。 |
| **group** (*string*; 預設：**default**) | 此模板分配到的策略組名稱。 |
| **ipsec-protocols** (*ah \| esp*; 預設：**esp**) | 指定要應用於匹配流量的 Authentication Header 和 Encapsulating Security Payload 協定組合。 |
| **level** (*require \| unique \| use*; 預設：**require**) | 指定當找不到此策略的某些 SA 時要執行的操作：use - 跳過此轉換，不丟棄封包，也不從 IKE 守護程式獲取 SA；require - 丟棄封包並獲取 SA；unique - 丟棄封包並獲取僅用於此特定策略的唯一 SA。它用於多個用戶端可位於一個公共 IP 地址之後（NAT 後的用戶端）的設定中。 |
| **peer** (*string*; 預設：) | 此策略應用到的 peer 名稱。 |
| **proposal** (*string*; 預設：**default**) | 由 IKE 守護程式傳送以為此策略建立 SA 的 proposal 模板名稱。 |
| **protocol** (*all \| egp \| ggp\| icmp \| igmp \| ...*; 預設：**all**) | 要匹配的 IP 封包協定。 |
| **src-address** (*ip/ipv6 prefix*; 預設：**0.0.0.0/32**) | 封包中要匹配的源地址。適用於使用隧道模式（tunnel=yes）或模板（template=yes）時。 |
| **src-port** (*any \| integer:0..65535*; 預設：**any**) | 封包中要匹配的源埠。如果設定為 any，則匹配所有埠。 |
| **template** (*yes \| no*; 預設：**no**) | 建立一個模板並將其分配給指定的策略組。模板使用以下引數：group - 此模板分配到的策略組名稱；src-address、dst-address - 請求的子網必須在兩個方向上匹配（例如，0.0.0.0/0 表示允許所有）；protocol - 要匹配的協定，如果設定為 all，則接受任何協定；proposal - 此模板使用的 SA 引數；level - 當 NAT 後有多個用戶端的設定中需要 unique 時有用。 |
| **tunnel** (*yes \| no*; 預設：**no**) | 指定是否使用隧道模式。 |

## 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **active** (*yes \| no*) | 此策略當前是否正在使用。 |
| **default** (*yes \| no*) | 此條目是否為預設系統條目。 |
| **dynamic** (*yes \| no*) | 此條目是否為動態新增或生成的條目。 |
| **invalid** (*yes \| no*) | 此策略是否無效 - 可能原因是存在具有相同 src-address 和 dst-address 的重複策略。 |
| **ph2-count** (*integer*) | 與此策略關聯的活動 Phase 2 會話數。 |
| **ph2-state** (*expired \| no-phase2 \| established*) | 金鑰建立進度的指示。 |
| **sa-dst-address** (*ip/ipv6 address*; 預設：**::**) | SA 目標 IP/IPv6 地址（遠端對等體）。 |
| **sa-src-address** (*ip/ipv6 address*; 預設：**::**) | SA 源 IP/IPv6 地址（本地對等體）。 |

:::info
策略順序很重要。它的工作方式類似於防火牆過濾器，策略從上到下執行（priority 引數已移除）。

在隧道模式下，所有封包都會被 IPIP 封裝，並且其新 IP 報頭的 src-address 和 dst-address 會設定為此策略的 sa-src-address 和 sa-dst-address 值。如果不使用隧道模式（即使用傳輸模式），則只有源地址和目標地址與 sa-src-address 和 sa-dst-address 相同的封包才能由此策略處理。傳輸模式只能處理源自主機且目的地為 IPsec 對等體（已建立安全關聯的主機）的封包。要加密網路之間（或網路與主機之間）的流量，必須使用隧道模式。
:::

### 統計資訊 {#statistics}

此選單顯示各種 IPsec 統計資訊和錯誤。

#### 只讀屬性 {#read-only-properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **in-errors** (*integer*) | 所有未由其他計數器匹配的入站錯誤。 |
| **in-buffer-errors** (*integer*) | 無空閒緩衝區。 |
| **in-header-errors** (*integer*) | 報頭錯誤。 |
| **in-no-states** (*integer*) | 未找到狀態，即入站 SPI、地址或 SA 上的 IPsec 協定有誤。 |
| **in-state-protocol-errors** (*integer*) | 轉換協定特定錯誤，例如 SA 金鑰錯誤或硬體加速器無法處理封包數量。 |
| **in-state-mode-errors** (*integer*) | 轉換模式特定錯誤。 |
| **in-state-sequence-errors** (*integer*) | 序列號超出視窗。 |
| **in-state-expired** (*integer*) | 狀態已過期。 |
| **in-state-mismatches** (*integer*) | 狀態具有不匹配的選項，例如 UDP 封裝型別不匹配。 |
| **in-state-invalid** (*integer*) | 狀態無效。 |
| **in-template-mismatches** (*integer*) | 沒有與狀態匹配的模板，例如入站 SA 正確但 SP 規則錯誤。可能原因是 sa-source 或 sa-destination 地址不匹配。 |
| **in-no-policies** (*integer*) | 未找到與狀態對應的策略，例如入站 SA 正確但未找到 SP。 |
| **in-policy-blocked** (*integer*) | 策略丟棄。 |
| **in-policy-errors** (*integer*) | 策略錯誤。 |
| **out-errors** (*integer*) | 所有未由其他計數器匹配的出站錯誤。 |
| **out-bundle-errors** (*integer*) | 捆綁生成錯誤。 |
| **out-bundle-check-errors** (*integer*) | 捆綁檢查錯誤。 |
| **out-no-states** (*integer*) | 未找到狀態。 |
| **out-state-protocol-errors** (*integer*) | 轉換協定特定錯誤。 |
| **out-state-mode-errors** (*integer*) | 轉換模式特定錯誤。 |
| **out-state-sequence-errors** (*integer*) | 序列錯誤，例如序列號溢位。 |
| **out-state-expired** (*integer*) | 狀態已過期。 |
| **out-policy-blocked** (*integer*) | 策略丟棄。 |
| **out-policy-dead** (*integer*) | 策略已失效。 |
| **out-policy-errors** (*integer*) | 策略錯誤。 |

## 提議 {#proposals}

IKE 守護程式為某些策略建立 SA 而傳送的提議資訊。

### 屬性 {#properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **auth-algorithms** (*md5\|null\|sha1\|sha256\|sha512*; 預設：**sha1**) | 允許用於授權的演算法。SHA（Secure Hash Algorithm）更強但更慢。MD5 使用 128 位金鑰，SHA1 使用 160 位金鑰。 |
| **comment** (*string*; 預設：) |  |
| **disabled** (*yes \| no*; 預設：**no**) | 專案是否已停用。 |
| **enc-algorithms** (*null\|des\|3des\|aes-128-cbc\|aes-128-ctr\|aes-128-gcm\|aes-192-cbc\|aes-192-ctr\|aes-192-gcm\|aes-256-cbc\|aes-256-ctr\|aes-256-gcm\|blowfish\|camellia-128\|camellia-192\|camellia-256\|twofish*; 預設：**aes-256-cbc,aes-192-cbc,aes-128-cbc**) | 用於 SA 的允許演算法和金鑰長度。 |
| **lifetime** (*time*; 預設：**30m**) | SA 在被丟棄之前使用多長時間。 |
| **name** (*string*; 預設：) |  |
| **pfs-group** (*ecp256 \| ecp384 \| ecp521 \| modp768 \| modp1024 \| modp1536 \| modp2048 \| modp3072 \| modp4096 \| modp6144 \| modp8192 \| none*; 預設：**modp1024**) | 用於完美前向保密的 Diffie-Hellman 組。 |

### 只讀屬性 {#read-only-properties-2}

| 屬性 | 描述 |
| :-- | :-- |
| **default** (*yes \| no*) | 此條目是否為預設系統條目。 |

## 組 {#groups}

在此選單中，可以建立供策略模板使用的其他策略組。

### 屬性 {#properties-2}

| 屬性 | 描述 |
| :-- | :-- |
| **name** (*string*; 預設：) |  |
| **comment** (*string*; 預設：) |  |

## 對等體 {#peers}

對等體配置設定用於在 IKE 守護程式之間建立連線。然後此連線將用於協商 SA 的金鑰和演算法。交換模式是對等體之間唯一的唯一識別符號，這意味著只要使用不同的 exchange-mode，就可以有多個具有相同 remote-address 的對等體配置。

## 屬性 {#properties-3}

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP/IPv6 Prefix*; 預設：**0.0.0.0/0**) | 如果遠端對等體的地址與此字首匹配，則在對等體認證和 **Phase 1** 建立中使用此對等體配置。如果多個對等體地址匹配多個配置條目，則將使用最具體的一個（即具有最大網路掩碼的條目）。 |
| **comment** (*string*; 預設：) | 對等體的簡短描述。 |
| **disabled** (*yes \| no*; 預設：**no**) | 對等體是否用於匹配遠端對等體的字首。 |
| **exchange-mode** (*aggressive \| base \| main \| ike2*; 預設：**main**) | 根據 RFC [2408](https://datatracker.ietf.org/doc/html/rfc2408#section-4.1) 的不同 ISAKMP Phase 1 交換模式。**main** 模式放寬了 rfc2409 第 5.4 節，以允許在主模式中進行 pre-shared-key 認證。ike2 模式啟用 IKEv2 RFC 7296。IKEv2 會忽略的引數：proposal-check、compatibility-options、lifebytes、dpd-maximum-failures、nat-traversal。 |
| **local-address** (*IP/IPv6 Address*; 預設：) | Phase 1 應繫結到的路由器本地地址。 |
| **name** (*string*; 預設：) |  |
| **passive** (*yes \| no*; 預設：**no**) | 啟用被動模式時，將等待遠端對等體發起 IKE 連線。啟用被動模式還表示該對等體是 xauth 響應方，停用被動模式則表示 xauth 發起方。當被動模式被停用時，如果已配置策略或在 Phase 1 期間建立了策略，對等體將自動嘗試建立 Phase 1 以及 Phase 2。 |
| **port** (*integer:0..65535*; 預設：**500**) | 當路由器作為發起方且遠端對等體使用非預設埠時，用於連線遠端對等體的通訊埠。 |
| **profile** (*string*; 預設：**default**) | IKE 協商期間將使用的 profile 模板名稱。 |
| **send-initial-contact** (*yes \| no*; 預設：**yes**) | 指定是傳送 "initial contact" IKE 封包還是等待遠端側；此封包應觸發移除當前源地址的舊對等體 SA。通常，在 road warrior 設定中，用戶端是發起方，此引數應設定為 no。如果為 ikev1 啟用了 modecfg 或 xauth，則不會發送 initial contact。 |

## 只讀屬性 {#read-only-properties-3}

| 屬性 | 描述 |
| :-- | :-- |
| **dynamic** (*yes \| no*) | 此條目是否由其他服務（例如 L2TP）動態新增。 |
| **responder** (*yes \| no*) | 此對等體是否僅充當響應方（偵聽傳入請求）而不發起連線。 |

### 配置檔案 {#profiles}

配置檔案定義了一組將在 Phase 1 期間用於 IKE 協商的引數。這些引數可能與其他對等體配置共用。

## 屬性 {#properties-4}

| 屬性 | 描述 |
| :-- | :-- |
| **dh-group** (*modp768 \| modp1024  \| modp1536 \| modp2048 \| modp3072 \| modp4096 \| modp6144 \| modp8192 \| ecp256 \| ecp384 \| ecp521*; 預設：**modp1024,modp2048**) | Diffie-Hellman 組（加密強度） |
| **dpd-interval** (*time \| disable-dpd*; 預設：**2m**) | 死對等體檢測間隔。如果設定為 disable-dpd，則不會使用死對等體檢測。 |
| **dpd-maximum-failures** (*integer: 1..100*; 預設：**5**) | 在對等體被視為死亡之前的最大失敗次數。如果啟用 DPD，則適用。 |
| **enc-algorithm** (*3des \| aes-128 \| aes-192 \| aes-256 \| blowfish \| camellia-128 \| camellia-192 \| camellia-256 \| des*; 預設：**aes-128**) | 對等體將使用的加密演算法列表。 |
| **hash-algorithm** (*md5 \| sha1 \| sha256 \| sha512*; 預設：**sha1**) | 雜湊演算法。SHA（Secure Hash Algorithm）更強，但更慢。MD5 使用 128 位金鑰，sha1 使用 160 位金鑰。 |
| **lifebytes** (*Integer: 0..4294967295*; 預設：**0**) | Phase 1 lifebytes 僅作為管理值新增到提議中。用於遠端對等體要求特定 lifebytes 值才能建立 Phase 1 的情況。 |
| **lifetime** (*time*; 預設：**1d**) | Phase 1 生命週期：指定 SA 的有效時長。 |
| **name** (*string*; 預設值： ) |  |
| **nat-traversal** (*yes \| no*; 預設：**yes**) | 使用 Linux NAT-T 機制解決 IPsec 對等體之間 NAT 路由器導致的 IPsec 不相容問題。此方法只能與 ESP 協定一起使用（AH 在設計上不受支援，因為它會對完整封包（包括 IP 報頭）簽名，而 NAT 會更改 IP 報頭，使 AH 簽名無效）。此方法將 IPsec ESP 流量封裝到 UDP 流中，以克服導致 ESP 與 NAT 不相容的一些小問題。 |
| **proposal-check** (*claim \| exact \| obey \| strict*; 預設：**obey**) | Phase 2 生命週期檢查邏輯：claim - 取提議的生命週期和配置的生命週期中最短的一個，並通知發起方；exact - 要求生命週期相同；obey - 接受發起方傳送的任何值；strict - 如果提議的生命週期長於預設值，則拒絕該提議，否則接受提議的生命週期。 |

## 身份 {#identities}

身份是特定於遠端對等體的配置引數。身份的主要目的是處理認證並驗證對等體的完整性。

### 屬性 {#properties-5}

| 屬性 | 描述 |
| :-- | :-- |
| **auth-method** (*digital-signature \| eap \| eap-radius \| pre-shared-key \| pre-shared-key-xauth \| rsa-key \| rsa-signature-hybrid*; 預設：**pre-shared-key**) | 認證方法：digital-signature - 使用一對 RSA 證書進行認證；eap - 發起方（網路掩碼為 /32 的對等體）的 IKEv2 EAP 認證。必須與 eap-methods 一起使用；eap-radius - 響應方的 IKEv2 EAP RADIUS 直通認證（RFC 3579）。在這種情況下需要伺服器證書。如果未指定伺服器證書，則只有支援 EAP-only (RFC 5998) 的用戶端才能連線。請注意，EAP 方法應與 EAP-only 相容；pre-shared-key - 使用對等體之間共享的密碼（預共享金鑰）字串進行認證（不建議使用，因為可能對預共享金鑰進行離線攻擊）；rsa-key - 使用在 keys 選單中匯入的 RSA 金鑰進行認證。僅支援 IKEv1；pre-shared-key-xauth - 使用對等體之間共享的密碼（預共享金鑰）字串 + XAuth 使用者名稱和密碼進行認證。僅支援 IKEv1；rsa-signature-hybrid - 使用發起方 XAuth 進行響應方證書認證。僅支援 IKEv1。 |
| **certificate** (*string*; 預設：) | 在 System/Certificates 中列出的證書名稱（用於對封包簽名；證書必須具有私鑰）。如果使用數字簽名認證方法（auth-method=digital-signature）或 EAP（auth-method=eap），則適用。 |
| **comment** (*string*; 預設：) | 身份的簡短描述。 |
| **disabled** (*yes \| no*; 預設：**no**) | 身份是否用於匹配遠端對等體。 |
| **eap-methods** (*eap-mschapv2 \| eap-peap \| eap-tls \| eap-ttls*; 預設：**eap-tls**) | 所有 EAP 方法都要求在 System/Certificates 選單中存在完整證書鏈，包括中間 CA 證書和根 CA 證書。此外，必須指定使用者名稱和密碼（如果認證伺服器要求）。可以指定多個 EAP 方法，並將按指定順序使用。當前支援的 EAP 方法：eap-mschapv2；eap-peap - 也稱為 PEAPv0/EAP-MSCHAPv2；eap-tls - 要求在 certificate 引數下指定額外的用戶端證書；eap-ttls。 |
| **generate-policy** (*no \| port-override \| port-strict*; 預設：**no**) | 允許此對等體為不存在的策略建立 SA。此類策略會在 SA 生命週期內動態建立。自動策略例如允許建立受 IPsec 保護的 L2TP 隧道，或任何在配置時不知道遠端對等體 IP 地址的其他設定。no - 不生成策略；port-override - 生成策略並強制策略使用任意埠（舊行為）；port-strict - 使用對等體提議中的埠，該埠應與對等體策略匹配。 |
| **key** (*string*; 預設：) | keys 選單中的私鑰名稱。如果使用 RSA 金鑰認證方法（auth-method=rsa-key），則適用。 |
| **match-by** (*remote-id \| certificate*; 預設：**remote-id**) | 定義用於對等體身份驗證的邏輯。remote-id - 將根據 remote-id 設定驗證對等體 ID。certificate 將使用 remote-certificate 設定中指定的內容驗證對等體證書。 |
| **mode-config** (*none \| \*request-only \| string*; 預設：**none**) | mode-config 選單中的配置引數名稱。設定此引數後，將啟用 mode-config。 |
| **my-id** (*auto \| address \| fqdn \| user-fqdn \| key-id*; 預設：**auto**) | 在發起方上，這控制傳送給響應方的 ID\_i。在響應方上，這控制傳送給發起方的 ID\_r。在 IKEv2 中，響應方還期望從發起方收到的 ID\_r 中包含此 ID。auto - 嘗試自動使用正確的 ID：預共享金鑰使用 IP，基於證書的連線使用 SAN（如果不存在則使用 DN）；address - 使用 IP 地址作為 ID；dn - ASN.1 X.500 Distinguished Name 的二進位制 Distinguished Encoding Rules (DER) 編碼；fqdn - 完全限定域名；key-id - 為身份使用指定的金鑰 ID；user fqdn - 指定完全限定的使用者名稱字串，例如 "user@domain.com"。 |
| **notrack-chain** (*string*; 預設：) | 將與 IPsec 策略匹配的 IP/Firewall/Raw 規則新增到指定鏈。與 generate-policy 一起使用。 |
| **password** (*string*; 預設：) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | XAuth 或 EAP 密碼。如果使用帶 XAuth 的預共享金鑰認證方法（auth-method=pre-shared-key-xauth）或 EAP（auth-method=eap），則適用。 |
| **peer** (*string*; 預設：) | 此身份應用到的 peer 名稱。 |
| **policy-template-group** (*none \| string*; 預設：**default**) | 如果啟用 generate-policy，則流量選擇器會與同一組中的模板進行檢查。如果沒有任何模板匹配，則不會建立 Phase 2 SA。 |
| **remote-certificate** (*string*; 預設：) | 用於認證遠端側的證書名稱（列在 System/Certificates 中）（用於驗證封包；不需要私鑰）。如果未指定 remote-certificate，則使用從遠端對等體收到的證書，並與證書選單中的 CA 進行檢查。必須在證書儲存中匯入正確的 CA。如果指定了 remote-certificate 和 match-by=certificate，則僅匹配特定的用戶端證書。如果使用數字簽名認證方法（auth-method=digital-signature），則適用。 |
| **remote-id** (*auto \| fqdn \| user-fqdn \| key-id \| ignore*; 預設：**auto**) | 此引數控制期望從遠端對等體收到的 ID 值。請注意，除 ignore 之外的所有型別都會使用收到的證書驗證遠端對等體 ID。如果對等體將其證書名稱作為 ID 傳送，則會針對證書檢查；否則 ID 會針對 Subject Alt. Name 檢查。auto - 接受所有 ID；address - 使用 IP 地址作為 ID；dn - ASN.1 X.500 Distinguished Name 的二進位制 Distinguished Encoding Rules (DER) 編碼；fqdn - 完全限定域名。僅在 IKEv2 中支援；user fqdn - 完全限定的使用者名稱字串，例如 "user@domain.com"。僅在 IKEv2 中支援；key-id - 身份的特定金鑰 ID。僅在 IKEv2 中支援；ignore - 不驗證收到的 ID 與證書（危險）。\* 萬用字元金鑰 ID 匹配**不支援**，例如 remote-id="key-id:CN=\*.domain.com" |
| **remote-key** (*string*; 預設：) | keys 選單中的公鑰名稱。如果使用 RSA 金鑰認證方法（auth-method=rsa-key），則適用。 |
| **secret** (*string*; 預設：) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 金鑰字串。如果以 '0x' 開頭，則會解析為十六進位制值。如果使用預共享金鑰認證方法（auth-method=pre-shared-key 或 auth-method=pre-shared-key-xauth），則適用。 |
| **username** (*string*; 預設：) | XAuth 或 EAP 使用者名稱。如果使用帶 XAuth 的預共享金鑰認證方法（auth-method=pre-shared-key-xauth）或 EAP（auth-method=eap），則適用。 |

### 只讀屬性 {#read-only-properties-4}

| 屬性 | 描述 |
| :-- | :-- |
| **dynamic** (*yes \| no*) | 此條目是否由其他服務（例如 L2TP）動態新增。 |

## 活動對等體 {#active-peers}

此選單提供有關當前已建立 Phase 1 連線的遠端對等體的各種統計資訊。

### 只讀屬性 {#read-only-properties-5}

| 屬性 | 描述 |
| :-- | :-- |
| **dynamic-address** (*ip/ipv6 address*) | 由 mode config 動態分配的 IP 地址 |
| **last-seen** (*time*) | 自收到此對等體最後一條訊息以來的時長。 |
| **local-address** (*ip/ipv6 address*) | 此對等體使用的路由器本地地址。 |
| **natt-peer** (*yes \| no*) | 此對等體是否使用 NAT-T。 |
| **ph2-total** (*integer*) | 活動 IPsec 安全關聯的總數。 |
| **remote-address** (*ip/ipv6 address*) | 遠端對等體的 IP/IPv6 地址。 |
| **responder** (*yes \| no*) | 連線是否由遠端對等體發起。 |
| **rx-bytes** (*integer*) | 從此對等體接收的總位元組數。 |
| **rx-packets** (*integer*) | 從此對等體接收的總封包數。 |
| **side** (*initiator \| responder*) | 顯示哪一側發起了 Phase 1 協商。 |
| **state** (*string*) | 與對等體的 Phase 1 協商狀態。例如，當 Phase 1 和 Phase 2 協商完成時，將顯示 "established" 狀態。 |
| **tx-bytes** (*integer*) | 傳輸到此對等體的總位元組數。 |
| **tx-packets** (*integer*) | 傳輸到此對等體的總封包數。 |
| **uptime** (*time*) | 對等體處於已建立狀態的時長。 |

### 命令 {#commands}

| 屬性 | 描述 |
| :-- | :-- |
| **kill-connections** () | 手動斷開所有遠端對等體。 |

## 模式配置 {#mode-configs}

此選單配置 ISAKMP 和 IKEv2 配置屬性。

### 屬性 {#properties-6}

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*none \| string*; 預設：) | 為發起方指定單個 IP 地址，而不是指定整個地址池。 |
| **address-pool** (*none \| string*; 預設：) | 如果啟用 mode-config，響應方將嘗試從中分配地址的地址池名稱。 |
| **address-prefix-length** (*integer [1..32]*; 預設：) | 從池中分配的地址的字首長度（網路掩碼）。 |
| **comment** (*string*; 預設：) |  |
| **name** (*string*; 預設：) |  |
| **responder** (*yes \| no*; 預設：**no**) | 指定此配置將作為發起方（用戶端）還是響應方（伺服器）工作。發起方將從響應方請求 mode-config 引數。 |
| **split-dns** (*list of DNS names*; 預設：) | 將使用 system-dns=yes 或 static-dns= 設定解析的 DNS 名稱列表。 |
| **split-include** (*list of IP prefix*; 預設：) | 將以 CIDR 格式透過隧道傳輸的子網列表。子網將使用 CISCO UNITY 擴充套件傳送給對等體。遠端對等體將建立特定的動態策略。 |
| **src-address-list** (*address list*; 預設：) | 指定地址列表將生成動態源 NAT 規則。此引數僅在 responder=no 時可用。帶 NAT 的 roadWarrior 用戶端 |
| **static-dns** (*list of IP*; 預設：) | 要傳送給用戶端的手動指定的 DNS 伺服器 IP 地址。 |
| **system-dns** (*yes \| no*; 預設：) | 啟用此選項後，DNS 地址將從 `/ip/dns` 獲取。 |

### 只讀屬性 {#read-only-properties-6}

| 屬性 | 描述 |
| :-- | :-- |
| **default** (*yes \| no*) | 此條目是否為預設系統條目。 |

:::warning
並非所有 IKE 實現都支援 split-include 選項提供的多個拆分網路。

**警告：** 如果 RouterOS 用戶端是發起方，它將始終傳送 CISCO UNITY 擴充套件，而 RouterOS 僅支援此擴充套件中的 split-include。

Cisco Unity Split DNS（屬性型別 28675）和 RFC8598（屬性型別 25）這兩個屬性都受支援，ROS 會對這些屬性作出響應，但僅作為響應方。

**警告：** 不能同時使用 system-dns 和 static-dns；ROS 只能使用一個 DNS。
:::

## 已安裝的 SA {#installed-sas}

此選單提供有關已安裝安全關聯的資訊，包括金鑰。

### 只讀屬性 {#read-only-properties-7}

| 屬性 | 描述 |
| :-- | :-- |
| **AH** (*yes \| no*) | 此 SA 是否使用 AH 協定。 |
| **ESP** (*yes \| no*) | 此 SA 是否使用 ESP 協定。 |
| **add-lifetime** (*time/time*) | 以 soft/hard 格式表示的 SA 新增生命週期：soft - 在此時間段後 IKE 將嘗試建立新 SA；hard - 在此時間段後 SA 將被刪除。 |
| **addtime** (*time*) | 新增此 SA 的日期和時間。 |
| **auth-algorithm** (*md5 \| null \| sha1 \| ...*) | 當前使用的認證演算法。 |
| **auth-key** (*string*) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 使用的認證金鑰。 |
| **current-bytes** (*64-bit integer*) | 此 SA 已處理的位元組數。 |
| **dst-address** (*IP*) | 此 SA 的目標地址。 |
| **enc-algorithm** (*des \| 3des \| aes-cbc \| ...*) | 當前使用的加密演算法。 |
| **enc-key** (*string*) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 使用的加密金鑰。 |
| **enc-key-size** (*number*) | 使用的加密金鑰長度。 |
| **expires-in** (*time*) | 距離重新生成金鑰剩餘的時間。 |
| **hw-aead** (*yes \| no*) | 此 SA 是否由硬體加速。 |
| **replay** (*integer*) | 重放視窗大小（以封包計）。 |
| **spi** (*string*) | 安全引數索引標識標籤。 |
| **src-address** (*IP*) | 此 SA 的源地址。 |
| **state** (*string*) | 顯示 SA 的當前狀態（"mature"、"dying" 等）。 |

### 命令 {#commands-1}

| 屬性 | 描述 |
| :-- | :-- |
| **flush** () | 手動移除所有已安裝的安全關聯。 |

## 金鑰 {#keys}

此選單列出可用於對等體認證的所有已匯入公鑰和私鑰。此選單有幾個用於處理金鑰的命令。

### 屬性 {#properties-7}

| 屬性 | 描述 |
| :-- | :-- |
| **name** (*string*; 預設：) |  |

### 只讀屬性 {#read-only-properties-8}

| 屬性 | 描述 |
| :-- | :-- |
| **key-size** (*1024 \| 2048 \| 4096*) | 此金鑰的大小。 |
| **private-key** (*yes \| no*) | 這是否為私鑰。 |
| **rsa** (*yes \| no*) | 這是否為 RSA 金鑰。 |

### 命令 {#commands-2}

| 屬性 | 描述 |
| :-- | :-- |
| **export-pub-key** (*file-name; key*) | 從現有私鑰之一匯出公鑰到檔案。 |
| **generate-key** (*key-size; name*) | 生成私鑰。接受兩個引數：新生成金鑰的名稱和金鑰大小 1024、2048 和 4096。 |
| **import** (*file-name; name*) | 從檔案匯入金鑰。 |

## 設定 {#settings}

| 屬性 | 描述 |
| :-- | :-- |
| **accounting** (*yes \| no*; 預設：) | 是否向 RADIUS 伺服器傳送 RADIUS 計費請求。如果使用 EAP Radius（auth-method=eap-radius）或帶 XAuth 的預共享金鑰認證方法（auth-method=pre-shared-key-xauth），則適用。 |
| **interim-update** (*time*; 預設：) | 每次連續 RADIUS 計費 Interim 更新之間的間隔。必須啟用計費。 |
| **xauth-use-radius** (*yes \| no*; 預設：) | 是否為 XAuth 使用者使用 Radius 用戶端。此屬性僅適用於使用 **IKEv1** 交換模式的對等體。 |

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

目前，只有源地址為 192.168.77.254/32 的封包才會匹配 IPsec 策略。為了讓本地網路能夠訪問遠端子網，必須將本地主機的源地址更改為動態分配的 mode config IP 地址。可以動態生成源 NAT 規則。這可以透過建立一個新的地址列表來完成，該列表包含應應用 NAT 規則的所有本地網路。在我們的例子中，是 192.168.88.0/24。

```ros
/ip/firewall/address-list/add address=192.168.88.0/24 list=local-RW
```

透過在 mode-config 發起方配置下指定地址列表，將動態生成一組源 NAT 規則。

```ros
/ip/ipsec/mode-config/set [ find name="request-only" ] src-address-list=local-RW
```

當 IPsec 隧道建立後，我們可以看到為每個網路動態建立的源 NAT 規則。現在 192.168.88.0/24 中的每臺主機都能訪問辦公室的內部資源。

```ros
[admin@mikrotik] > ip firewall nat print 
Flags: X - disabled, I - invalid, D - dynamic 
0 D ;;; ipsec mode-config
chain=srcnat action=src-nat to-addresses=192.168.77.254 dst-address=192.168.55.0/24 src-address-list=local-RW

1 D ;;; ipsec mode-config
chain=srcnat action=src-nat to-addresses=192.168.77.254 dst-address=10.5.8.0/24 src-address-list=local-RW
```

### 僅允許 IPsec 封裝流量 {#allow-only-ipsec-encapsulated-traffic}

在某些場景中，出於安全原因，如果傳入/傳出封包未加密，你可能希望丟棄對特定網路的訪問。例如，如果我們有 L2TP/IPsec 設定，我們會希望丟棄未加密的 L2TP 連線嘗試。

有幾種方法可以實現這一點：

- 在防火牆中使用 IPsec 策略匹配器。
- 使用通用 IPsec 策略，將 action 設定為 **drop** 並降低優先順序（可用於生成動態策略的 Road Warrior 設定）。
- 在 mangle 中設定 DSCP 或優先順序，並在解封裝後在防火牆中匹配相同的值。

#### IPsec 策略匹配器 {#ipsec-policy-matcher}

讓我們設定一個 IPsec 策略匹配器，以接受與任何 IPsec 策略匹配的所有封包，並丟棄其餘封包：

```ros
add chain=input comment="ipsec policy matcher" in-interface=WAN ipsec-policy=in,ipsec
add action=drop chain=input comment="drop all" in-interface=WAN log=yes
```

IPsec 策略匹配器接受兩個引數 **direction、policy**。我們使用了入站方向和 IPsec 策略。IPsec policy 選項允許我們在解封裝後檢查封包，因此例如，如果我們只想允許來自特定源地址的 GRE 封裝封包並丟棄其餘封包，可以設定以下規則：

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

此方法的技巧是新增一個 action 為 drop 的預設策略。假設我們在公共地址 1.1.1.1 上執行 L2TP/IPsec 伺服器，並且希望丟棄所有未加密的 L2TP：

```ros
/ip/ipsec/policy
add src-address=1.1.1.1 dst-address=0.0.0.0/0 sa-src-address=1.1.1.1 protocol=udp src-port=1701 tunnel=yes action=discard
```

現在路由器將丟棄任何未加密的 L2TP 入站流量，但在 L2TP/IPsec 連線成功後，會建立一個優先順序高於預設靜態規則的動態策略，並且匹配該動態規則的封包可以被轉發。

:::warning
策略順序很重要！為使此方法生效，請確保靜態 drop 策略位於動態策略下方。如有必要，將其移到策略模板下方。
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

與 RouterOS 中的任何其他服務一樣，IPsec 使用主路由表，無論 Peer 配置中使用什麼 local-address 引數。必須對 IKE 和 IPsec 流量都應用路由標記。

考慮以下示例。有兩條預設路由 - 一條在主路由表中，另一條在路由表 "backup" 中。IPsec 站點到站點隧道需要使用備份鏈路。

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

目前，我們在日誌中看到 "phase1 negotiation failed due to time up" 錯誤。這是因為 IPsec 嘗試使用主路由表和錯誤的源地址到達遠端對等體。需要使用 Mangle 標記 UDP/500、UDP/4500 和 ipsec-esp 封包：

```ros
/ip/firewall/mangle
add action=mark-connection chain=output connection-mark=no-mark dst-address=10.155.130.136 dst-port=500,4500 new-connection-mark=ipsec passthrough=yes protocol=udp
add action=mark-connection chain=output connection-mark=no-mark dst-address=10.155.130.136 new-connection-mark=ipsec passthrough=yes protocol=ipsec-esp
add action=mark-routing chain=output connection-mark=ipsec new-routing-mark=backup passthrough=no
```

#### 使用同一路由表和多個 IP 地址 {#using-the-same-routing-table-with-multiple-ip-addresses}

考慮以下示例。公共介面上有來自同一子網的多個 IP 地址。在 out-interface 上配置了 masquerade 規則。必須顯式使用其中一個 IP 地址。

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

目前，Phase 1 連線使用的源地址與我們指定的不同，並且日誌中顯示 "phase1 negotiation failed due to time up" 錯誤。這是因為 masquerade 正在更改連線的源地址，以匹配已連線路由的 pref-src 地址。解決方案是排除來自公共 IP 地址的連線，使其不被 masquerade。

```ros
/ip/firewall/nat
add action=accept chain=srcnat protocol=udp src-port=500,4500 place-before=0
```

## 應用示例 {#application-examples}

### 站點到站點 IPsec (IKEv1) 隧道 {#site-to-site-ipsec-ikev1-tunnel}

考慮如下所示的設定。兩個遠端辦公室路由器連線到 Internet，辦公室工作站位於 NAT 之後。每個辦公室都有自己的本地子網，Office1 為 10.1.202.0/24，Office2 為 10.1.101.0/24。兩個遠端辦公室都需要通向路由器後方本地網路的安全隧道。

![](/img/e82d4ebd9d1188e7.webp)

#### **站點 1 配置** {#site-1-configuration}

首先使用適合你需求的更強或更弱加密引數建立新的 Phase 1 配置檔案和 Phase 2 提議條目。建議為每個選單建立單獨的條目，以便它們對每個對等體都是唯一的，以防將來需要調整任何設定。這些引數必須在站點之間匹配，否則連線將無法建立。

```ros
/ip/ipsec/profile
add dh-group=modp2048 enc-algorithm=aes-128 name=ike1-site2
/ip/ipsec/proposal
add enc-algorithms=aes-128-cbc name=ike1-site2 pfs-group=modp2048
```

繼續配置對等體。指定遠端路由器的地址。應能透過 UDP/500 和 UDP/4500 埠訪問此地址，因此請確保針對路由器防火牆採取適當的操作。指定此對等體的名稱以及新建的配置檔案。

```ros
/ip/ipsec/peer
add address=192.168.80.1/32 name=ike1-site2 profile=ike1-site2
```

下一步是建立身份。對於基本的預共享金鑰保護隧道，除了 **強** 金鑰以及此身份應用到的對等體之外，沒有太多需要設定的。

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

此時，如果你嘗試透過 IPsec 隧道傳送流量，將無法工作；封包會丟失。這是因為兩個路由器都有 NAT 規則（masquerade），會在封包加密之前更改源地址。路由器無法加密封包，因為源地址與策略配置中指定的地址不匹配。更多資訊請參見 IPsec 封包流示例。

要解決此問題，我們需要設定 IP/Firewall/NAT 繞過規則。

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

繞過規則放在所有其他 NAT 規則的最頂部非常重要。

另一個問題是，如果啟用了 IP/Fasttrack，封包會繞過 IPsec 策略。因此我們需要在 FastTrack 之前新增接受規則。

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

此示例說明當一個或兩個站點沒有靜態 IP 地址時，如何在兩個 RouterOS 裝置之間建立安全且加密的 GRE 隧道。要使此配置可行，必須為將充當響應方（伺服器）的裝置之一分配 DNS 名稱。為簡單起見，我們將使用 RouterOS 內建的 DDNS 服務 IP/Cloud。

![](/img/a4224852afe39ede.webp)

#### 站點 1（伺服器）配置 {#site-1-server-configuration}

這是將偵聽傳入連線並充當響應方的一側。我們將使用 mode config 為第二個站點提供 IP 地址，但首先建立一個環回（空白）橋，併為其分配一個稍後用於建立 GRE 隧道的 IP 地址。

```ros
/interface/bridge 
add name=loopback
/ip/address
add address=192.168.99.1 interface=loopback
```

繼續 IPsec 配置，首先使用適合你需求的更強或更弱加密引數建立新的 Phase 1 配置檔案和 Phase 2 提議條目。請注意，此配置示例將偵聽所有傳入的 IKEv2 請求，這意味著該配置檔案配置將與其他所有配置（例如 RoadWarrior）共享。

```ros
/ip/ipsec/profile
add dh-group=ecp256,modp2048,modp1024 enc-algorithm=aes-256,aes-192,aes-128 name=ike2
/ip/ipsec/proposal
add auth-algorithms=null enc-algorithms=aes-128-gcm name=ike2-gre pfs-group=none
```

接下來，建立 responder=yes 的新 mode config 條目。這將為另一站點提供 IP 配置，以及用於策略生成的主機（環回地址）。

```ros
/ip/ipsec/mode-config
add address=192.168.99.2 address-prefix-length=32 name=ike2-gre split-include=192.168.99.1/32 system-dns=no
```

建議建立一個新的策略組，將此配置與任何現有或未來的 IPsec 配置分開。

```ros
/ip/ipsec/policy/group
add name=ike2-gre
```

現在是時候設定一個新的策略模板，以匹配遠端對等體的新動態地址和環回地址。

```ros
/ip/ipsec/policy
add dst-address=192.168.99.2/32 group=ike2-gre proposal=ike2-gre src-address=192.168.99.1/32 template=yes
```

下一步是建立將偵聽所有 IKEv2 請求的對等體配置。如果你已經有這樣的條目，可以跳過此步驟。

```ros
/ip/ipsec/peer
add exchange-mode=ike2 name=ike2 passive=yes profile=ike2
```

最後，設定一個身份，透過使用特定金鑰的 pre-shared-key 認證來匹配我們的遠端對等體。

```ros
/ip/ipsec/identity
add generate-policy=port-strict mode-config=ike2-gre peer=ike2 policy-template-group=ike2-gre secret=test
```

伺服器端現在已配置完成並偵聽所有 IKEv2 請求。請確保防火牆未阻止 UDP/4500 埠。

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

與伺服器配置類似，首先建立新的 Phase 1 配置檔案和 Phase 2 提議配置。由於此站點將是發起方，我們可以使用更具體的配置檔案配置來控制使用哪些確切的加密引數，只需確保它們與伺服器端配置的內容重疊。

```ros
/ip/ipsec/profile
add dh-group=ecp256 enc-algorithm=aes-256 name=ike2-gre
/ip/ipsec/proposal
add auth-algorithms=null enc-algorithms=aes-128-gcm name=ike2-gre pfs-group=none
```

接下來，建立 responder=no 的新 mode config 條目。這將確保對等體從伺服器請求 IP 和拆分網路配置。

```ros
/ip/ipsec/mode-config
add name=ike2-gre responder=no
```

還建議建立一個新的策略組，將此配置與任何現有或未來的 IPsec 配置分開。

```ros
/ip/ipsec/policy/group
add name=ike2-gre
```

同時在用戶端側建立新的策略模板。

```ros
/ip/ipsec/policy
add dst-address=192.168.99.1/32 group=ike2-gre proposal=ike2-gre src-address=192.168.99.2/32 template=yes
```

繼續進行對等體配置。現在我們可以在 address 引數下指定伺服器的 DNS 名稱。顯然，你也可以使用 IP 地址。

```ros
/ip/ipsec/peer
add address=n.mynetname.net exchange-mode=ike2 name=p1.ez profile=ike2-gre
```

最後，為我們新建的對等體建立身份。

```ros
/ip/ipsec/identity
add generate-policy=port-strict mode-config=ike2-gre peer=p1.ez policy-template-group=ike2-gre secret=test
```

如果一切操作正確，應該會存在一個新的動態策略。

```ros
/ip/ipsec/policy/print 
Flags: T - template, X - disabled, D - dynamic, I - invalid, A - active, * - default 
0 T * group=default src-address=::/0 dst-address=::/0 protocol=all proposal=default template=yes

1 T group=ike2-gre src-address=192.168.99.2/32 dst-address=192.168.99.1/32 protocol=all proposal=ike2-gre template=yes

2 DA src-address=192.168.99.2/32 src-port=any dst-address=192.168.99.1/32 dst-port=any protocol=all action=encrypt level=unique ipsec-protocols=esp 
tunnel=yes sa-src-address=192.168.90.1 sa-dst-address=(current IP of n.mynetname.net) proposal=ike2-gre ph2-count=1 
```

現在兩個站點之間已建立安全隧道，將加密 192.168.99.2 \<=> 192.168.99.1 地址之間的所有流量。我們可以使用這些地址建立 GRE 隧道。

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

在配置 IPsec 之前，需要設定證書。可以使用單獨的 Certificate Authority 進行證書管理；但是，在此示例中，自簽名證書在 RouterOS System/Certificates 選單中生成。要將各種裝置連線到伺服器，應滿足一些證書要求：

- Common name 應包含伺服器的 IP 或 DNS 名稱。
- SAN（subject alternative name）應包含伺服器的 IP 或 DNS 名稱。
- 需要 EKU（extended key usage）tls-server 和 tls-client。

考慮上述所有要求，生成 CA 和伺服器證書：

```ros
/certificate
add common-name=ca name=ca
sign ca ca-crl-host=2.2.2.2
add common-name=2.2.2.2 subject-alt-name=IP:2.2.2.2 key-usage=tls-server name=server1
sign server1 ca=ca
```

既然路由器上已建立有效證書，新增 pfs-group=none 的新 Phase 1 配置檔案和 Phase 2 提議條目：

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

由於必須調整策略模板以僅允許特定網路策略，建議建立單獨的策略組和模板。

```ros
/ip/ipsec/policy/group
add name=ike2-policies
/ip/ipsec/policy
add dst-address=192.168.77.0/24 group=ike2-policies proposal=ike2 src-address=0.0.0.0/0 template=yes
```

建立一個新的 IPsec 對等體條目，以偵聽所有傳入的 IKEv2 請求。

```ros
/ip/ipsec/peer
add exchange-mode=ike2 name=ike2 passive=yes profile=ike2
```

##### 身份配置 {#identity-configuration}

身份選單允許匹配特定遠端對等體，併為每個對等體分配不同的配置。首先，建立一個預設身份，該身份將接受所有對等體，但會使用其對等體的證書驗證對等體身份。

```ros
/ip/ipsec/identity
add auth-method=digital-signature certificate=server1 generate-policy=port-strict mode-config=ike2-conf peer=ike2 policy-template-group=ike2-policies
```

:::warning
如果對等體的 ID (ID\_i) 與其傳送的證書不匹配，身份查詢將失敗。請參見 identities 部分中的 remote-id。
:::

例如，我們想為使用者 "A" 分配不同的 mode config，該使用者使用證書 "rw-client1" 向伺服器認證自身。首先，確保已建立新的 mode config 並準備好應用於該特定使用者。

```ros
/ip/ipsec/mode-config
add address=192.168.66.2 address-prefix-length=32 name=usr_A split-include=192.168.55.0/24 system-dns=no
```

可以透過使用 match-by=certificate 引數並使用 remote-certificate 指定其證書，將此配置應用於使用者 "A"。

```ros
/ip/ipsec/identity
add auth-method=digital-signature certificate=server1 generate-policy=port-strict match-by=certificate mode-config=usr_A peer=ike2 policy-template-group=ike2-policies remote-certificate=rw-client1
```

##### （可選）拆分隧道配置 {#optional-split-tunnel-configuration}

拆分隧道是一種方法，允許 road warrior 用戶端僅訪問特定的受保護網路，同時根據其內部路由表傳送其餘流量（而不是透過隧道傳送所有流量）。要配置拆分隧道，需要更改 mode config 引數。

例如，我們將允許 road warrior 用戶端僅訪問 10.5.8.0/24 網路。

```ros
/ip/ipsec/mode-conf
set [find name="rw-conf"] split-include=10.5.8.0/24
```

還可以傳送特定的 DNS 伺服器供用戶端使用。預設情況下，使用 system-dns=yes，這會發送在路由器自身的 IP/DNS 中配置的 DNS 伺服器。我們可以使用 static-dns 引數強制用戶端使用不同的 DNS 伺服器。

```ros
/ip/ipsec/mode-conf
set [find name="rw-conf"] system-dns=no static-dns=10.5.8.1
```

雖然可以調整 IPsec 策略模板，以僅允許 road warrior 用戶端為 split-include 引數配置的網路生成策略，但這可能會導致與不同廠商實現的相容性問題（請參見已知限制）。與其調整策略模板，不如在 IP/Firewall/Filter 中允許訪問受保護網路，並丟棄其他所有內容。

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

通常 PKCS12 捆綁包還包含 CA 證書，但某些廠商可能不會安裝此 CA，因此必須使用 PEM 格式單獨匯出自簽名 CA 證書。

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

- Windows 將始終忽略透過 split-include 收到的網路，並請求目標為 0.0.0.0/0 (TSr) 的策略。生成 IPsec-SA 後，Windows 會請求 DHCP 選項 249，RouterOS 將自動使用配置的 split-include 網路響應。

- Apple macOS 和 iOS 都只接受第一個 split-include 網路。

- Apple macOS 和 iOS 僅在使用了 0.0.0.0/0 split-include 時，才會使用 system-dns 和 static-dns 引數中的 DNS 伺服器。

- 雖然某些實現可以在 Phase 2 使用不同的 PFS 組，但建議在 proposals 下使用 pfs-group=none，以避免任何相容性問題。

#### RouterOS 用戶端配置 {#routeros-client-configuration}

在 RouterOS 中匯入 PKCS12 格式證書。

```ros
/certificate/import file-name=cert_export_RouterOS_client.p12 passphrase=1234567890
```

現在 Certificate 選單中應有自簽名 CA 證書和用戶端證書。找出用戶端證書的名稱。

```ros
/certificate/print
```

**cert\_export\_RouterOS\_client.p12\_0** 是用戶端證書。

建議建立單獨的 Phase 1 配置檔案和 Phase 2 提議配置，以免干擾任何現有 IPsec 配置。

```ros
/ip/ipsec/profile
add name=ike2-rw
/ip/ipsec/proposal
add name=ike2-rw pfs-group=none
```

雖然可以使用預設策略模板生成策略，但最好建立新的策略組和模板，將此配置與任何其他 IPsec 配置分開。

```ros
/ip/ipsec/policy/group
add name=ike2-rw
/ip/ipsec/policy
add group=ike2-rw proposal=ike2-rw template=yes
```

建立一個 responder=no 的新 mode config 條目，該條目將從伺服器請求配置引數。

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

如果我們檢視生成的動態策略，會看到只有具有特定源地址（由 mode config 接收）的流量才會透過隧道傳送。但路由器在大多數情況下需要將特定裝置或網路路由到隧道中。在這種情況下，我們可以使用源 NAT 更改封包的源地址，以匹配 mode config 地址。由於 mode config 地址是動態的，因此無法建立靜態源 NAT 規則。在 RouterOS 中，可以為 mode config 用戶端生成動態源 NAT 規則。

![](/img/f2c4abd8b00ecd03.webp)

例如，我們有一個位於路由器後方的本地網路 192.168.88.0/24，並且我們希望來自此網路的所有流量都透過隧道傳送。首先，我們必須建立一個新的 IP/Firewall/Address 列表，其中包含我們的本地網路。

```ros
/ip/firewall/address-list
add address=192.168.88.0/24 list=local
```

完成後，我們可以將新建的 IP/Firewall/Address 列表分配給 mode config 配置。

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
確保動態 mode config 地址不是本地網路的一部分。
:::

#### Windows 用戶端配置 {#windows-client-configuration}

在 Windows 計算機上開啟 PKCS12 格式證書檔案。按照說明安裝證書。確保選擇“本地計算機”儲存位置。![](/img/7f0720a59f02c365.webp) 現在可以轉到“網路和 Internet 設定”-> VPN 並新增新配置。填寫連線名稱、伺服器名稱或地址引數。在 VPN 型別下選擇 IKEv2。完成後，必須選擇“使用計算機證書”。可以在“網路和共享中心”中單擊 VPN 連線的“屬性”選單來完成此操作。該設定位於“安全”標籤頁下。

![](/img/d60e9d2292526217.webp)

目前，Windows 10 與以下 Phase 1（profiles）和 Phase 2（proposals）提議集相容：

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

在 macOS 計算機上開啟 PKCS12 格式證書檔案，並將證書安裝到 "System" 鑰匙串中。由於 CA 證書是自簽名的，因此必須手動將其標記為受信任。在 macOS Keychain Access 應用的 System 標籤頁下找到該證書，並將其標記為 Always Trust。

![](/img/ae8f9610163925e0.webp)

現在可以轉到 System Preferences -> Network，並單擊 + 按鈕新增新配置。選擇 Interface: VPN、VPN Type: IKEv2，併為連線命名。Remote ID 必須設定為等於伺服器證書的 common-name 或 subjAltName。Local ID 可以留空。在 Authentication Settings 下選擇 None，並選擇用戶端證書。現在可以測試連線。

![](/img/98ab138f5ea6d75a.webp)

目前，macOS 與以下 Phase 1（profiles）和 Phase 2（proposals）提議集相容：

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

通常，PKCS12 捆綁包還包含 CA 證書，但 iOS 不會安裝此 CA，因此必須使用 PEM 格式單獨安裝自簽名 CA 證書。在 iOS 裝置上開啟這些檔案，並按照說明安裝兩個證書。必須在 iOS 裝置上將自簽名 CA 證書標記為受信任。可以在 Settings -> General -> About -> Certificate Trust Settings 選單中完成此操作。完成後，在 Settings -> General -> Profiles 選單下檢查兩個證書是否都標記為 "verified"。

![](/img/b5ea33be6cc87db1.webp)

現在可以轉到 Settings -> General -> VPN 選單並新增新配置。Remote ID 必須設定為等於伺服器證書的 common-name 或 subjAltName。Local ID 可以留空。

![](/img/a0ba071bd82f918b.webp)

目前，iOS 與以下 Phase 1（profiles）和 Phase 2（proposals）提議集相容：

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

目前，Android 沒有原生 IKEv2 支援，但是可以使用 Google Play 商店中的 strongSwan，它為 Android 帶來 IKEv2。StrongSwan 接受 PKCS12 格式證書，因此在 strongSwan 中設定 VPN 連線之前，請確保將 PKCS12 捆綁包下載到 Android 裝置。完成後，在 strongSwan 中建立新的 VPN 配置檔案，輸入伺服器 IP，並選擇 "IKEv2 Certificate" 作為 VPN 型別。選擇使用者證書時，按 Install 並按照證書提取過程指定 PKCS12 捆綁包。儲存配置檔案，並透過按 VPN 配置檔案測試連線。

![](/img/f1154362a91b750c.webp)

可以透過勾選 "Show advanced settings" 複選框在 strongSwan 中指定自定義加密設定。目前，strongSwan 預設與以下 Phase 1（profiles）和 Phase 2（proposals）提議集相容：

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

此示例說明如何在連線到 Internet 的裝置（road warrior 用戶端）與執行 RouterOS 並充當 IKEv2 伺服器和 User Manager 的裝置之間建立安全的 IPsec 連線。可以在網路中的單獨裝置上執行 User Manager，但在本示例中，User Manager 和 IKEv2 伺服器都將配置在同一裝置（Office）上。

![](/img/15261a1aca9285d4.webp)

#### RouterOS 伺服器配置 {#routeros-server-configuration-1}

##### 要求 {#requirements}

要使此設定生效，路由器需要滿足幾個先決條件：

1. 路由器的 IP 地址應具有有效的公共 DNS 記錄 - 可以使用 IP Cloud 實現。
2. 應能透過 Internet 上的 TCP/80 埠訪問路由器 - 如果伺服器位於 NAT 之後，則應配置埠轉發。
3. 路由器上應安裝 User Manager 軟體包。

##### 生成 Let's Encrypt 證書 {#generating-lets-encrypt-certificate}

在 EAP-MSCHAPv2 認證期間，必須進行 TLS 握手，這意味著伺服器必須具有可由用戶端驗證的證書。為簡化此步驟，我們將使用 Let's Encrypt 證書，大多數作業系統無需使用者干預即可驗證該證書。要生成證書，只需在 Certificates 選單下啟用 SSL 證書。預設情況下，該命令使用 IP Cloud 提供的動態 DNS 記錄，但也可以指定自定義 DNS 名稱。請注意，DNS 記錄應指向路由器。

```ros
/certificate/enable-ssl-certificate
```

如果證書生成成功，你應該會在 Certificates 選單下看到已安裝的 Let's Encrypt 證書。

```ros
/certificate/print detail where name~"letsencrypt"
```

##### 配置 User Manager {#configuring-user-manager}

首先，允許從 localhost（路由器本身）接收 RADIUS 請求：

```ros
/user-manager/router
add address=127.0.0.1 comment=localhost name=local shared-secret=test
```

啟用 User Manager 並指定將用於認證使用者的 Let's Encrypt 證書（將證書名稱替換為你裝置上安裝的證書名稱）。

```ros
/user-manager
set certificate="letsencrypt_2021-04-09T07:10:55Z" enabled=yes
```

最後新增使用者及其憑據，用戶端將使用這些憑據向伺服器認證。

```ros
/user-manager/user
add name=user1 password=password
```

##### 配置 RADIUS 用戶端 {#configuring-radius-client}

要讓路由器使用 RADIUS 伺服器進行使用者認證，需要新增一個新的 RADIUS 用戶端，其共享金鑰與我們已在 User Manager 上配置的相同。

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

由於必須調整策略模板以僅允許特定網路策略，建議建立單獨的策略組和模板。

```ros
/ip/ipsec/policy/group
add name=ike2-policies
/ip/ipsec/policy
add dst-address=192.168.77.0/24 group=ike2-policies proposal=ike2 src-address=0.0.0.0/0 template=yes
```

建立一個新的 IPsec 對等體條目，以偵聽所有傳入的 IKEv2 請求。

```ros
/ip/ipsec/peer
add exchange-mode=ike2 name=ike2 passive=yes profile=ike2
```

最後，建立一個新的 IPsec 身份條目，以匹配所有嘗試使用 EAP 認證的用戶端。請注意，必須指定生成的 Let's Encrypt 證書。

```ros
/ip/ipsec/identity
add auth-method=eap-radius certificate="letsencrypt_2021-04-09T07:10:55Z" generate-policy=port-strict mode-config=ike2-conf peer=ike2 \
policy-template-group=ike2-policies
```

##### （可選）拆分隧道配置 {#optional-split-tunnel-configuration-1}

拆分隧道是一種方法，允許 road warrior 用戶端僅訪問特定的受保護網路，同時根據其內部路由表傳送其餘流量（而不是透過隧道傳送所有流量）。要配置拆分隧道，需要更改 mode config 引數。

例如，我們將允許 road warrior 用戶端僅訪問 10.5.8.0/24 網路。

```ros
/ip/ipsec/mode-conf
set [find name="rw-conf"] split-include=10.5.8.0/24
```

還可以傳送特定的 DNS 伺服器供用戶端使用。預設情況下，使用 system-dns=yes，這會發送在路由器自身的 IP/DNS 中配置的 DNS 伺服器。我們可以使用 static-dns 引數強制用戶端使用不同的 DNS 伺服器。

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

要跟蹤每個使用者的正常執行時間、下載和上傳統計資訊，可以使用 RADIUS 計費。預設情況下，IPsec 的 RADIUS 計費已啟用，但建議配置 Interim Update 計時器，以定期將統計資訊傳送到 RADIUS 伺服器。如果路由器將處理大量併發會話，建議增加更新計時器以避免 CPU 使用率增加。

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

現在，它會啟用 L2TP 伺服器並使用指定的金鑰建立動態 IPsec 對等體。

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

它將自動建立動態 IPsec 對等體和策略配置。

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

對等體之間存在通訊問題。可能原因包括 - Phase 1 IP 地址配置錯誤；防火牆阻止 UDP 埠 500 和 4500；對等體之間的 NAT 未正確轉換 IPsec 協商封包。當 local-address 引數使用不當時，也可能出現此錯誤訊息。更多資訊可在此處獲取。

#### 隨機丟包或隧道連線非常慢，啟用封包嗅探器/torch 後問題解決？ {#random-packet-drops-or-connections-over-the-tunnel-are-very-slow-enabling-packet-sniffertorch-fixes-the-problem}

問題在於，封包在封裝之前被髮送到 Fasttrack/FastPath，從而繞過 IPsec 策略檢查。解決方案是將需要封裝/解封裝的流量從 Fasttrack 中排除。

#### 如何啟用 ike2？ {#how-to-enable-ike2}

對於基本配置，啟用 ike2 非常簡單。只需將 peer 設定中的 exchange-mode 更改為 ike2。

#### 致命的 NO-PROPOSAL-CHOSEN 通知訊息？ {#fatal-no-proposal-chosen-notify-message}

遠端對等體傳送了一個通知，表示它無法接受提議的演算法。要查詢問題的確切原因，請檢視遠端對等體的偵錯日誌或配置，並驗證用戶端和伺服器是否具有相同的演算法集。

#### 我只能在一個方向 ping 通？ {#i-can-ping-only-in-one-direction}

此類情況下的典型問題是嚴格的防火牆：防火牆規則僅允許在一個方向上建立新連線。解決方案是重新檢查防火牆規則，或顯式接受所有應封裝/解封裝流量。

#### 我可以僅允許加密流量嗎？ {#can-i-allow-only-encrypted-traffic}

可以，請參見“僅允許 IPsec 封裝流量”示例。

#### 我在 StrongSwan 上啟用 IKEv2 REAUTH 並收到錯誤 'initiator did not reauthenticate as requested' {#i-enable-ikev2-reauth-on-strongswan-and-got-the-error-initiator-did-not-reauthenticate-as-requested}

RouterOS 不支援 rfc4478，必須在 StrongSwan 上停用 reauth。
