---
sidebar_key: "network-management/proxy/index"
sidebar_position: 2
title: "代理"
sidebar_label: "代理"
description: "MikroTik RouterOS 代理功能可啟用 HTTP 和 FTP 快取、透明代理、透過源/目標列表進行訪問控制、URL 過濾和日誌記錄。它支援直接連線、父代理和用於安全的內容掃描，並提供配置示例，包括常規代理和透明代理設定。"
tags:
  - 'proxy'
  - 'firewall'
  - 'caching'
source: https://manual.mikrotik.com/docs/7.24/network-management/proxy
captured_at: '2026-11-04T11:32:49+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹代理功能。可使用它配置反向代理行為及相關的 RouterOS 代理服務。

<DocCardList />

MikroTik RouterOS 會代理 HTTP 和 HTTP-proxy（用於 FTP 和 HTTP 協定）請求。代理伺服器透過將請求的 Internet 物件（即可透過 HTTP 和 FTP 協定獲取的資料）儲存在更靠近接收方的系統上，來執行 Internet 物件快取功能，從而以區域網路速度從代理快取向客戶交付所請求的檔案副本，加快客戶瀏覽速度。MikroTik RouterOS 實現以下代理伺服器功能：

- 常規 HTTP 代理——客戶（自身）指定該代理伺服器為其做什麼。
- 透明代理——客戶不知道已啟用代理，並且用戶端的 Web 瀏覽器無需任何額外配置。
- 按源、目標、URL 和請求方法設定的訪問列表（HTTP 防火牆）。
- 快取訪問列表，用於指定哪些物件要快取、哪些不快取。
- 直接訪問列表——用於指定哪些資源應直接訪問，哪些應透過另一個代理伺服器訪問。
- 日誌功能——允許獲取並存儲有關代理操作的資訊。
- 父代理支援——允許指定另一個代理伺服器，*（如果它們沒有所請求的物件，則向它們的父代理或原始伺服器請求）。*

代理伺服器通常放置在 Internet 上使用者與目標伺服器（*也稱為源伺服器*）之間的各個位置。

![](/img/0a86ba2a141c09fa.webp)

一個 *Web 代理（快取）* 會監視來自用戶端的請求，併為自己儲存響應的副本。然後，如果對同一 URL 有另一個請求，它可以使用自己已有的響應，而不是再次向源伺服器請求該內容。如果代理尚未請求過某個檔案，它會從原始伺服器下載該檔案。

代理伺服器可能有很多潛在用途：

- 提高對資源的訪問速度（用戶端獲取物件所需時間更少）。
- 用作 HTTP 防火牆（拒絕對不良網頁的訪問）。

允許過濾 Web 內容（按特定引數，如源地址、目標地址、埠、URL、HTTP 請求方法），並掃描出站內容，例如用於資料洩漏防護。

:::warning
當你只想將 Web 代理用作類似 HTTP 和 FTP 防火牆（例如，拒絕對不期望網頁的訪問，或拒絕特定型別的檔案，如 .mp3 檔案），或透明地將請求重定向到外部代理（可能是具有快取功能的代理）時，即使沒有快取，執行 Web 代理也可能很有用。
:::

## 配置示例 {#configuration-examples}

**子選單：** `/ip/proxy`

在 MikroTik RouterOS 中，代理配置在 *`/ip/proxy`* 選單中完成。下面介紹如何在埠 8080 上啟用代理，並將 192.168.88.254 設定為代理源地址：

```ros
[admin@MikroTik] > /ip/proxy/set enabled=yes port=8080 src-address=192.168.88.254
[admin@MikroTik] > /ip/proxy/print 
                 enabled: yes
             src-address: 192.168.88.254
                    port: 8080
               anonymous: no
            parent-proxy: ::
       parent-proxy-port: 0
     cache-administrator: webmaster
          max-cache-size: unlimited
   max-cache-object-size: 2048KiB
           cache-on-disk: no
  max-client-connections: 600
  max-server-connections: 600
          max-fresh-time: 3d
   serialize-connections: no
       always-from-cache: no
          cache-hit-dscp: 4
              cache-path: web-proxy
```

:::tip
設定常規代理服務時，請確保它僅為你的用戶端提供服務，並透過建立只允許你的用戶端使用代理的防火牆來防止未經授權的訪問；否則，它可能被用作開放代理。
:::

### 透明代理配置示例 {#transparent-proxy-configuration-example}

RouterOS 還可以充當透明快取伺服器，且無需在客戶的 Web 瀏覽器中進行任何配置。透明代理不會修改所請求的 URL 或響應。RouterOS 會接管所有 HTTP 請求並將它們重定向到本地代理服務。此過程對使用者完全透明（使用者可能完全不知道位於他們與原始伺服器之間的代理伺服器），對他們而言唯一的不同就是瀏覽速度提高了。

要啟用透明模式，必須在目標 NAT 中新增防火牆規則，指定哪些連線（到哪些埠）應被透明重定向到代理。檢查上面的代理設定，並將我們的使用者（192.168.1.0/24）重定向到代理伺服器：

```ros
[admin@MikroTik] /ip/firewall/nat> add chain=dstnat protocol=tcp src-address=192.168.1.0/24 dst-port=80 action=redirect to-ports=8080
[admin@MikroTik] /ip/firewall/nat> print
Flags: X - disabled, I - invalid, D - dynamic
 0   chain=dstnat protocol=tcp src-address=192.168.1.0/24 dst-port=80 action=redirect to-ports=8080
```

 該 Web 代理可以同時用作透明 Web 代理和普通 Web 代理。在透明模式下，也可以將其用作標準 Web 代理。然而，在這種情況下，代理使用者可能無法訪問那些透過透明方式訪問的網頁。

### 基於代理的防火牆——訪問列表 {#proxy-based-firewall--access-list}

訪問列表的實現方式與 MikroTik 防火牆規則相同，均從上到下處理。第一條匹配的規則指定對該連線採取什麼操作。連線可以按其源地址、目標地址、目標埠、所請求 URL（統一資源定位符）的子字串或請求方法來匹配。如果未指定這些引數中的任何一個，則每個連線都會匹配此規則。

如果某個連線被某條規則匹配，則該規則的 action 屬性指定該連線是允許還是不允許（deny）。如果某個連線不匹配任何規則，則它將被允許。

在此示例中，假設我們已經配置了透明代理伺服器。它將阻止網站 [http://www.facebook.com](http://www.facebook.com/)。我們始終可以透過指定 src-address 來為不同網路阻止相同內容：

```ros
/ip/proxy/access/add src-address=192.168.1.0/24 dst-host=www.facebook.com action=deny
```

來自網路 192.168.1.0/24 的使用者將無法訪問網站 [www.facebook.com](http://www.facebook.com/)。

你也可以阻止 URL 中包含特定詞語的網站：

```ros
/ip/proxy/access/add dst-host=:mail action=deny
```

此語句將阻止 URL 中包含“mail”一詞的所有網站，例如 [www.mail.com](http://www.mail.com/)、[www.hotmail.com](http://www.hotmail.com/)、[mail.yahoo.com](http://mail.yahoo.com) 等。

***我們還可以阻止下載特定型別的檔案，如 .flv、.avi、.mp4、.mp3、.exe、.dat 等。***

```ros
 /ip/proxy/access
 add path=*.flv action=deny
 add path=*.avi action=deny
 add path=*.mp4 action=deny
 add path=*.mp3 action=deny
 add path=*.zip action=deny
 add path=*.rar action=deny
```

這裡還提供了不同的萬用字元字元，用於建立特定條件並透過代理訪問列表進行匹配。萬用字元屬性（dst-host 和 path）匹配完整字串（即，如果設定為 "example"，則不會匹配 "[example.com](http://example.com)"）。可用萬用字元為 '\*'（匹配任意數量的任意字元）和 '?'（匹配任意一個字元）。

這裡也接受正則表示式，但如果應將屬性視為正則表示式，則它應以冒號（':'）開頭。

為了表示給定模式之前不允許有任何符號，我們在模式開頭使用 ^ 符號。

為了指定給定模式之後不允許有任何符號，我們在模式末尾使用 $ 符號。

## 啟用基於 RAM 或儲存的快取 {#enabling-ram-or-store-based-caching}

在此示例中，我們假設你已經配置好代理並且代理正在工作，而你只想啟用快取。如果需要詳細的命令/引數說明，請檢視位於示例部分正下方的參考部分。

- 基於 RAM 的快取：
  - 如果你的裝置有相當數量的 RAM 可用於快取，那麼這很好。在 RAM 為 256MB 或更少的裝置上啟用此功能不會給你的網路帶來任何好處。
  - 快取寫入/讀取速度比儲存在 USB 或 SATA 連線介質上的快取快得多。

- 基於儲存的快取：
  - 由於介質容量差異，可以獲得更大的代理快取。

### **RAM 代理快取：** {#ram-proxy-cache}

## 重要命令 {#important-commands}

- max-cache-size=
- max-cache-object-size=
- cache-on-disk=

```ros
[admin@MikroTik] /ip/proxy> set max-cache-size=unlimited max-cache-object-size=50000KiB cache-on-disk=no 
...
[admin@MikroTik] /ip/proxy> print 
                 enabled: yes
             src-address: ::
                    port: 8080
               anonymous: no
            parent-proxy: 0.0.0.0
       parent-proxy-port: 0
     cache-administrator: webmaster
          max-cache-size: unlimited  <-------
   max-cache-object-size: 50000KiB  <-------
           cache-on-disk: no  <-------
  max-client-connections: 600
  max-server-connections: 600
          max-fresh-time: 3d
   serialize-connections: no 
       always-from-cache: no
          cache-hit-dscp: 4
              cache-path: proxy-cache
```

### **儲存代理快取：** {#store-proxy-cache}

重要命令：

- max-cache-size=
- max-cache-object-size=
- cache-on-disk=
- cache-path=

```ros
[admin@MikroTik] > /ip/proxy set cache-on-disk=yes cache-path=/usb1/proxy/cache

[admin@MikroTik] > /ip/proxy print                                                
                 enabled: yes
             src-address: ::
                    port: 8080
               anonymous: no
            parent-proxy: 0.0.0.0
       parent-proxy-port: 0
     cache-administrator: webmaster
          max-cache-size: unlimited  <-------
   max-cache-object-size: 50000KiB  <-------
           cache-on-disk: yes  <-------
  max-client-connections: 600
  max-server-connections: 600
          max-fresh-time: 3d
   serialize-connections: no
       always-from-cache: no
          cache-hit-dscp: 4
              cache-path: usb1/proxy/cache  <-------

[admin@MikroTik] > /file/print                                                    
 # NAME                                                           TYPE              
 0 skins                                                          directory        
 5 usb1/proxy                                                     directory           
 6 usb1/proxy/cache                                               web-proxy store   <-------      
 7 usb1/lost+found                                                directory  
```

### 檢查快取是否工作 {#check-if-a-cache-is-working}

```ros
[admin@MikroTik] > /ip/proxy/monitor 
                 status: running
                 uptime: 2w20h28m25s
     client-connections: 15
     server-connections: 7
               requests: 79772
                   hits: 30513
             cache-used: 481KiB
         total-ram-used: 1207KiB
  received-from-servers: 4042536KiB
        sent-to-clients: 4399757KiB
   hits-sent-to-clients: 176934KiB
```

## 參考 {#reference}

按選單列出的所有可用引數和命令。

#### 常規 {#general}

**子選單：** `/ip/proxy`

| 屬性 | 描述 |
| :-- | :-- |
| **always-from-cache** (*yes \| no*; 預設值：**no**) | 如果內容被視為新鮮，則忽略用戶端重新整理請求 |
| **anonymous** (*yes \| no*; 預設值：**no**) | 如果未設定，用戶端的 IP 地址將傳入 X-Forwarded-For 頭（可在遠端伺服器中使用 HTTP_X_FORWARDED_FOR 環境變數訪問） |
| **cache-administrator** (*string*; 預設值：**webmaster**) | 代理錯誤頁面上顯示的管理員電子郵件 |
| **cache-hit-dscp** (*integer: 0..63*; 預設值：**4**) | 使用提供的 DSCP 值自動標記快取命中 |
| **cache-on-disk** (*yes \| no*; 預設值：**no**) | 是否將快取儲存在磁碟上 |
| **cache-path** (*string*; 預設值：**web-proxy**) | 啟用 cache-on-disk 時儲存快取的路徑。 |
| **max-cache-object-size** (*integer: 0..4294967295[KiB]*; 預設值：**2048KiB**) | 指定最大快取物件大小，以千位元組為單位 |
| **max-cache-size** (*none \| unlimited \| integer: 0..4294967295[KiB]*; 預設值：**unlimited**) | 指定最大快取大小，以千位元組為單位 |
| **max-client-connections** (*integer: Dynamic*; 預設值：**600**) | 從用戶端接受的最大連線數（任何進一步的連線都將被拒絕） |
| **max-fresh-time** (*time*; 預設值：**3d**) | 儲存快取物件的最長時間。物件的有效期通常由物件本身定義，但如果設定得過高，你可以覆蓋該最大值 |
| **max-server-connections** (*integer: Dynamic*; 預設值：**600**) | 與伺服器建立的最大連線數（來自用戶端的任何進一步連線都將被掛起，直到某些伺服器連線終止） |
| **parent-proxy** (*Ip4 \| ip6*; 預設值：**0.0.0.0**) | 要將所有請求重定向到的另一個 HTTP 代理的 IP 地址。如果設定為 **0.0.0.0**，則不使用父代理。 |
| **parent-proxy-port** (*integer: 0..65535*; 預設值：**0**) | 父代理正在監聽的埠。 |
| **port** (*integer: 0..65535*; 預設值：**8080**) | 代理伺服器將監聽的 TCP 埠。所有希望將該伺服器用作 HTTP 代理的用戶端都必須指定此埠。可以透過在 IP 防火牆中使用目標 NAT 功能將 HTTP 請求重定向到此埠，來建立透明（對用戶端零配置）代理設定 |
| **serialize-connections** (*yes \| no*; 預設值：**no**) | 如果可能（即伺服器支援持久 HTTP 連線），不要為多個用戶端連線建立多個到伺服器的連線。將按 FIFO 原則服務用戶端；當對前一個用戶端的響應傳輸完成後，才會處理下一個用戶端。如果某個用戶端空閒時間過長（預設最多 5 秒），它將放棄等待並開啟另一個到伺服器的連線 |
| **src-address** (*Ip4 \| Ip6*; 預設值：**0.0.0.0**) | 代理在連線到父代理或網站時將使用指定地址。如果設定為 **0.0.0.0**，則將從路由表中獲取適當的 IP 地址。 |

#### 訪問列表 {#access-list}

**子選單：** `/ip/proxy/access`

訪問列表的配置方式與常規防火牆規則類似。規則從上到下處理。第一條匹配的規則指定對該連線採取什麼操作。總共有 6 個分類器用於指定匹配約束。如果未指定這些分類器中的任何一個，則該特定規則將匹配每個連線。

如果某個連線被某條規則匹配，則該規則的 action 屬性指定該連線是否被允許。如果該特定連線不匹配任何規則，則它將被允許。

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*allow \| deny*; 預設值：**allow**) | 指定是放行還是拒絕匹配的封包 |
| **dst-address** (*Ip4[-Ip4 \| /0..32] \| Ip6/0..128*; 預設值： ) | 目標伺服器的目標地址。 |
| **dst-host** (*string*; 預設值： ) | 用於連線到目標伺服器的 IP 地址或 DNS 名稱（這是使用者在瀏覽器中指定某個網頁的埠和路徑之前所寫的字串） |
| **dst-port** (*integer[-integer[,integer[,...]]]: 0..65535*; 預設值： ) | 封包目標埠的列表或範圍 |
| **local-port** (*integer: 0..65535*; 預設值： ) | 指定接收該封包的 Web 代理埠。此值應與 Web 代理正在監聽的埠之一匹配。 |
| **method** (*any \| connect \| delete \| get \| head \| options \| post \| put \| trace*; 預設值： ) | 請求中使用的 HTTP 方法（請參閱本文件末尾的 HTTP 方法部分） |
| **path** (*string*; 預設值： ) | 目標伺服器中所請求頁面的名稱（即特定網頁或文件的名稱，不包含其所在伺服器的名稱） |
| **redirect-to** (*string*; 預設值： ) | 如果訪問被此規則拒絕，則使用者將被重定向到此處指定的 URL |
| **src-address** (*Ip4[-Ip4 \| /0..32] \| Ip6/0..128*; 預設值： ) | 連線發起方的源地址。 |

只讀屬性：

| 屬性 | 描述 |
| :-- | :-- |
| **hits** (*integer*) | 被此規則匹配的請求數 |

萬用字元屬性（dst-host 和 dst-path）匹配完整字串（即，如果設定為 "example"，則不會匹配 "[example.com](http://example.com)"）。可用萬用字元為 '\*'（匹配任意數量的任意字元）和 '?'（匹配任意一個字元）。這裡也接受正則表示式，但如果應將屬性視為正則表示式，則它應以冒號（':'）開頭。

使用正則表示式的小提示：

- \\ 符號序列用於在控制檯中輸入 \ 字元；
- \. 模式僅表示（在正則表示式中，模式中的單個點表示任意符號）；
- 為了表示給定模式之前不允許有任何符號，我們在模式開頭使用 ^ 符號。
- 為了指定給定模式之後不允許有任何符號，我們在模式末尾使用 $ 符號。
- 要輸入 [ 或 ] 符號，應使用反斜槓 "\["};

強烈建議拒絕除路由器後面的地址之外的所有 IP 地址，因為代理仍可能被用來訪問你的僅限內部使用（內聯網）Web 伺服器。另外，請參閱防火牆手冊中的示例，瞭解如何保護你的路由器。

#### 直接訪問 {#direct-access}

**子選單：** `/ip/proxy/direct`

如果指定了 **parent-proxy** 屬性，則可以告訴代理伺服器是嘗試將請求傳遞給父代理，還是透過直接連線到所請求的伺服器來解析它。直接訪問列表的管理方式與上一章所述的代理訪問列表相同，只是 action 引數不同。與訪問列表不同，直接代理訪問列表的預設 action 等於 deny。當未指定任何規則或特定請求不匹配任何規則時，將採用該預設 action。

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*allow \| deny*; 預設值：**allow**) | 指定對匹配封包執行的操作：allow - 始終繞過父代理直接解析匹配的請求；deny - 透過父代理解析匹配的請求。如果未指定任何操作，則與 allow 具有相同的效果。 |
| **dst-address** (*Ip4[-Ip4 \| /0..32] \| Ip6/0..128*; 預設值： ) | 目標伺服器的目標地址。 |
| **dst-host** (*string*; 預設值： ) | 用於連線到目標伺服器的 IP 地址或 DNS 名稱（這是使用者在瀏覽器中指定某個網頁的埠和路徑之前所寫的字串） |
| **dst-port** (*integer[-integer[,integer[,...]]]: 0..65535*; 預設值： ) | 連線到目標伺服器所使用的埠列表或範圍。 |
| **local-port** (*integer: 0..65535*; 預設值： ) | 指定接收該封包的 Web 代理埠。此值應與 Web 代理正在監聽的埠之一匹配。 |
| **method** (*any \| connect \| delete \| get \| head \| options \| post \| put \| trace*; 預設值： ) | 請求中使用的 HTTP 方法（請參閱本文件末尾的 [HTTP 方法](#http-methods) 部分） |
| **path** (*string*; 預設值： ) | 目標伺服器中所請求頁面的名稱（即特定網頁或文件的名稱，不包含其所在伺服器的名稱） |
| **src-address** (*Ip4[-Ip4 \| /0..32] \| Ip6/0..128*; 預設值： ) | 連線發起方的源地址。 |

只讀屬性：

| 屬性 | 描述 |
| :-- | :-- |
| **hits** (*integer*) | 被此規則匹配的請求數 |

#### 快取管理 {#cache-management}

**子選單：** `/ip/proxy/cache`

快取訪問列表指定 Web 代理必須在本地快取哪些請求（域、伺服器、頁面），以及哪些不快取。此列表的實現方式與 Web 代理訪問列表完全相同。預設 action 是快取物件（如果未找到匹配規則）。

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*allow \| deny*; 預設值：**allow**) | 指定對匹配封包執行的操作：allow - 快取來自匹配請求的物件；deny - 不快取來自匹配請求的物件 |
| **dst-address** (*Ip4[-Ip4 \| /0..32] \| Ip6/0..128*; 預設值： ) | 目標伺服器的目標地址 |
| **dst-host** (*string*; 預設值： ) | 用於連線到目標伺服器的 IP 地址或 DNS 名稱（這是使用者在瀏覽器中指定某個網頁的埠和路徑之前所寫的字串） |
| **dst-port** (*integer[-integer[,integer[,...]]]: 0..65535*; 預設值： ) | 封包目標埠的列表或範圍。 |
| **local-port** (*integer: 0..65535*; 預設值： ) | 指定接收該封包的 Web 代理埠。此值應與 Web 代理正在監聽的埠之一匹配。 |
| **method** (*any \| connect \| delete \| get \| head \| options \| post \| put \| trace*; 預設值： ) | 請求中使用的 HTTP 方法（請參閱本文件末尾的 HTTP 方法部分） |
| **path** (*string*; 預設值： ) | 目標伺服器中所請求頁面的名稱（即特定網頁或文件的名稱，不包含其所在伺服器的名稱） |
| **src-address** (*Ip4[-Ip4 \| /0..32] \| Ip6/0..128*; 預設值： ) | 連線發起方的源地址 |

只讀屬性：

| 屬性 | 描述 |
| :-- | :-- |
| **hits** (*integer*) | 被此規則匹配的請求數 |

#### 連線 {#connections}

**子選單：** `/ip/proxy/connections`

此選單包含代理當前正在服務的連線列表。

只讀屬性：

| 屬性 | 描述 |
| :-- | :-- |
| **client** () |  |
| **dst-address** (*Ip4 \| Ip6*) | 連線的 IPv4/Ipv6 目標地址 |
| **protocol** (*string*) | 協定名稱 |
| **rx-bytes** (*integer*) | 用戶端接收的位元組數 |
| **server** () |  |
| **src-address** (*Ip4 \| Ip6*) | 連線發起方的 Ipv4/ipv6 地址 |
| **state** (*closing \| connecting \| converting \| hotspot \| idle \| resolving \| rx-header \| tx-body \| tx-eof \| tx-header \| waiting*) | 連線狀態：closing - 資料傳輸已結束，連線正在最終確定；connecting - 正在建立連線；converting - 替換響應或請求封包中的頭部和尾部欄位；hotspot - 檢查熱點認證是否允許繼續（用於熱點代理）；idle - 保持空閒；resolving - 解析伺服器的 DNS 名稱；rx-header - 接收 HTTP 頭部；tx-body - 向用戶端傳輸 HTTP 正文；tx-eof - 寫入塊結束（當轉換為分塊響應時）；tx-header - 向用戶端傳輸 HTTP 頭部；waiting - 等待對端傳輸 |
| **tx-bytes** (*integer*) | 用戶端傳送的位元組數 |

#### 快取插入 {#cache-inserts}

**子選單：** `/ip/proxy/inserts`

此選單顯示有關儲存在快取中的物件的統計資訊（快取插入）。

只讀屬性：

| 屬性 | 描述 |
| :-- | :-- |
| **denied** (*integer*) | 被快取列表拒絕的插入數量。 |
| **errors** (*integer*) | 磁碟或其他系統相關錯誤數 |
| **no-memory** (*integer*) | 因記憶體不足而未儲存的物件數量 |
| **successes** (*integer*) | 成功快取插入的數量。 |
| **too-large** (*integer*) | 因過大而無法儲存的物件數量 |

#### 快取查詢 {#cache-lookups}

**子選單：** `/ip/proxy/lookup`

此選單顯示有關從快取讀取的物件（快取查詢）的統計資訊。

只讀屬性：

| 屬性 | 描述 |
| :-- | :-- |
| **denied** (*integer*) | 被訪問列表拒絕的請求數。 |
| **expired** (*integer*) | 在快取中找到但已過期、因而從外部伺服器請求的請求數 |
| **no-expiration-info** (*integer*) | 收到了針對某個頁面的條件請求，但該頁面沒有可用於比較該請求的資訊 |
| **non-cacheable** (*integer*) | 無條件從外部伺服器請求的請求數（因為其快取被快取訪問列表拒絕） |
| **not-found** (*integer*) | 在快取中未找到、因而從外部伺服器（或按相應配置從父代理）請求的請求數 |
| **successes** (*integer*) | 在快取中找到的請求數。 |

#### 快取內容 {#cache-contents}

**子選單：** `/ip/proxy/cache-contents`

此選單顯示快取內容。

只讀屬性：

| 屬性 | 描述 |
| :-- | :-- |
| **file-size** (*integer*) | 快取物件大小 |
| **last-accessed** (*time*) |  |
| **last-accessed-time** (*time*) |  |
| **last-modified** (*time*) |  |
| **last-modified-time** (*time*) |  |
| **uri** (*string*) | 快取物件的統一資源識別符號 |

## HTTP 方法 {#http-methods}

##### Options {#options}

此方法請求獲取有關用戶端與由 **Request-URI** 標識的伺服器之間鏈路上可用的通訊選項的資訊。該方法允許用戶端在不啟動任何資源檢索的情況下確定與資源關聯的選項和（或）要求。

##### GET {#get}

此方法檢索由 Request-URI 標識的任何資訊。如果 Request-URI 指向資料處理過程，則對 GET 方法的響應應包含該過程產生的資料，而不是該過程程式的原始碼，除非原始碼就是該過程的結果。

如果請求訊息包含 If-Modified-Since、If-Unmodified-Since、If-Match、If-None-Match 或 If-Range 頭欄位，則 GET 方法可以成為條件 GET。條件 GET 方法用於透過指定僅在條件頭欄位所描述的情況下才傳輸實體來減少網路流量。

如果請求訊息包含 Range 頭欄位，則 GET 方法可以成為部分 GET。部分 GET 方法旨在透過僅請求實體的部分內容而不傳輸用戶端已持有的資料，來減少不必要的網路使用。

對 GET 請求的響應當且僅當滿足 HTTP 快取要求時才可快取。

##### HEAD {#head}

此方法具有 GET 方法的所有特性，不同之處在於伺服器不得在響應中返回訊息正文。這會檢索請求所隱含實體的元資訊，因此它被廣泛用於測試超文字連結的有效性、可訪問性和最近修改情況。

對 HEAD 請求的響應可能以這樣的方式可快取：響應中包含的資訊可用於更新由該 Request-URI 標識的先前快取實體。

##### POST {#post}

此方法請求源伺服器接受請求中包含的實體，作為由 Request-URI 標識的資源的新從屬資源。

POST 方法執行的實際操作由源伺服器確定，並且通常取決於 Request-URI。

對 POST 方法的響應不可快取，除非響應包含適當的 Cache-Control 或 Expires 頭欄位。

##### PUT {#put}

此方法請求將包含的實體儲存在提供的 Request-URI 下。如果指定 Request-URI 下存在另一個實體，則應將包含的實體視為源伺服器上現有實體的更新（較新）版本。如果 Request-URI 未指向現有資源，則源伺服器應建立具有該 URI 的資源。

如果請求經過快取，並且 Request-URI 標識一個或多個當前快取的實體，則這些條目應被視為過期。對此方法的響應不可快取。

##### TRACE {#trace}

此方法會呼叫請求訊息的遠端應用層環回。請求的最終接收者應將收到的訊息作為 200（OK）響應的實體正文反射回用戶端。最終接收者是源伺服器，或者是請求中收到 Max-Forwards 值為 0 的第一個代理或閘道器。TRACE 請求不得包含實體。

對此方法的響應不得快取。
