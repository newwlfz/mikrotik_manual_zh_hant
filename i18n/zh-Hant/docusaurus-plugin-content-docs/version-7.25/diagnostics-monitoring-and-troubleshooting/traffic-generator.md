---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/traffic-generator"
sidebar_position: 9
title: "流量生成器"
sidebar_label: "流量生成器"
description: "Traffic Generator 是一款 MikroTik RouterOS 工具，透過在埠上生成併發送原始封包來評估裝置效能，並收集延遲、抖動、吞吐量和丟包資料。它支援 OOO 檢測和 PCAP 注入等高階功能，並提供可配置的屬性和命令，便於快速完成設定。"
tags:
  - 'traffic-generator'
  - 'packet-generation'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/traffic-generator
captured_at: '2026-11-04T11:16:26+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

流量生成器是一個工具，可用於評估 DUT（被測裝置）或 SUT（被測系統）的效能。

該工具可以透過特定埠生成併發送 RAW 封包。它還會收集延遲和抖動值、TX/RX 速率，統計丟包數，並檢測亂序（OOO）封包。

流量生成器可以像 [頻寬測試](./bandwidth-test.md) 工具一樣使用，也可以生成將被路由回封包生成器以進行高階狀態收集的封包。

:::info
在生成封包的裝置上，無法使用 sniffer 工具、torch 或出介面上的防火牆來捕獲由 traffic-generator 生成的封包。

由於此工具可能被惡意使用，可以透過輸入命令 `/system/device-mode/update traffic-gen=no` 並在之後按住復位按鈕來鎖定此功能。
:::

## 常規 {#general}

**子選單：** `/tool/traffic-generator`

此選單允許設定流量生成器的通用屬性，幷包含快速啟動和停止該工具的命令。

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **latency-distribution-max**（*time*；預設：**100us**） | 延遲分佈測量的最大延遲範圍。RouterOS 將根據此值決定使用何種延遲範圍作為 latency-distribution-measure-interval 屬性 |
| **measure-out-of-order**（*yes \| no*；預設：） | 是否測量亂序封包。預設值取決於 CPU 型別（多核 CPU 預設為 **no**；單核 CPU 預設為 **yes**）。在多核裝置上啟用該屬性時，單個流將只使用一個 CPU 核心 |
| **stats-samples-to-keep**（*integer*；預設：**100**） | 要收集多少個數據樣本 |
| **test-id**（*integer [0..255]*；預設：**0**） |  |

### 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **latency-distribution-samples**（*integer*） | 顯示 latency-distribution-measure-interval 被劃分成多少個單獨的時間段 |
| **latency-distribution-measure-interval**（*time*） | 顯示總延遲測量範圍 |
| **running**（*yes \| no*） | 顯示流量生成器工具是否已啟動。 |

### 命令 {#commands}

| 屬性 | 描述 |
| :-- | :-- |
| **quick** () | 此命令允許你快速啟動封包生成器，並將統計輸出列印到終端。該命令還接受若干引數，用於覆蓋封包模板和流設定中的配置。接受的引數包括 **duration, entries-to-show, freeze-frame-interval, id, interface, mbps, measure-out-of-order, packet-count, packet-size, port, pps, stream, test-id, tx-template** tx-template - 用於生成流量的封包模板（最多 16 個模板） duration - 測試執行時長 entries-to-show - 要列印到終端的狀態行數 freeze-frame-interval - 更新終端狀態的頻率 其餘引數並非命令專用，已在其他地方描述。執行 quick 命令時指定的引數會覆蓋已配置的值。如果某個引數僅為一個頭指定，則該值會（在需要時）複製到所有其他頭。 |
| **start** () | 命令在後臺啟動流量生成器工具。它接受一個引數 **test-id** |
| **stop** () | 命令停止由 **start** 命令啟動的流量生成器工具。 |
| **inject** () | 將原始資料注入介面。 |
| **inject-pcap** () | 直接從 PCAP 或 PCAPNG 檔案注入原始資料。**重要：** 從 RouterOS 7.20 開始，[sniffer 工具](./packet-sniffer.md) 以 PCAPNG 格式儲存捕獲的封包。從 RouterOS 7.21 開始，traffic-generator 的 inject-pcap 功能支援 PCAPNG 格式。 |

## 封包模板 {#packet-template}

**子選單：** `/tool/traffic-generator/packet-template`

此子選單允許根據提供的引數構建封包。根據這些引數，你可以構建帶有 VLAN 標籤的 IP 封包，並設定 UDP 埠。系統會根據提供的引數生成原始封包模板。

如果你需要更底層的封包，或想充分利用流量生成器，請使用 raw-packet-template 構建器來構建封包。

如果同一型別的頭在封包中出現多次，則頭欄位值會以逗號分隔列表的形式傳入。（例如，如果存在兩個 IP 頭，則源地址會寫成 "IP-src=1.1.1.1,2.2.2.2"）。

為了更快地構造頭，許多頭欄位值都是假定的。例如，如果頭棧為 "mac, IP"，則流量生成器可以假定 mac-protocol 值為 "IP"。或者，如果指定了 "port" 或 "interface" 設定，流量生成器可以假定 "mac-src" 為介面的 MAC 地址。假定值具有以 "assumed-" 開頭的獨特名稱，並且是隻讀的。手動指定的值會覆蓋假定值。

:::info
假定值不會自動更新。編輯模板後會重新假定新值。執行 "packet-template set 0" 就足以觸發新的假定值
:::

| 屬性 | 描述 |
| :-- | :-- |
| **comment**（*string*；預設：） | 你正在構建的封包的簡短描述。 |
| **compute-checksum-from-offset**（*no-checksum \| integer[0..4294967295]*；預設：） | 指定從封包中的哪個位元組偏移處開始計算 2 位元組校驗和（示例：設為 14，以便在計算校驗和時跳過封包的乙太網頭） |
| **data**（*incrementing \| random \| specific-byte \| uninitialized*；預設：**uninitialized**） | 指定封包有效載荷的填充方式：uninitialized - 封包資料（頭之後）未初始化，但不為零。最快。specific-byte - 與 data-byte 設定配合使用。incrementing - 封包資料填充為 "00 01 02 03" 等。random - 封包資料填充為隨機位元組。最慢。 |
| **data-byte**（*hex [0..FF]*；預設：**0**） | 用於填充封包有效載荷的位元組。 |
| **interface**（*string*；預設：） | 封包模板的可選引數。此引數與 "port" 設定互斥。指定 "interface" 後，使用者無需在 port 選單中為該介面建立 port 條目。實際上，port 條目是動態建立的。這對於執行快速測試很有用。 |
| **ip-dscp**（*integer[0..255] 列表（最多 16 次）*；預設：） | 將在 IP 頭中設定的單個或 DS 欄位列表（DS 欄位包含 DSCP 值和 ECN 值） |
| **ip-dst**（*IP/Netmask 列表（最多 16 次）*；預設：） | 生成 IP 頭時使用的目標 IP 地址列表。 |
| **ip-frag-off**（*integer[0..65535] 列表（最多 16 次）*；預設：） | IP 頭中的分片偏移列表。 |
| **ip-gateway**（*IP*；預設：） | 當傳送方和接收方為同一裝置時，無法根據 **ip-dst** 自動確定下一跳。如果指定了 ip-gateway，封包模板將根據解析後的 ip-gateway 假定目標 MAC 地址。 |
| **ip-id**（*integer [0..65535] 列表*；預設：） |  |
| **ip-protocol**（*IP 協定列表（最多 16 次）*；預設：） |  |
| **ip-src**（*IP/Mask 列表（最多 16 次）*；預設：） |  |
| **ip-ttl**（*integer [0..255] 列表（最多 16 次）*；預設：） |  |
| **mac-dst**（*MAC/MASK 列表（最多 16 次）*；預設：） |  |
| **mac-protocol**（*MAC 協定列表（最多 16 次）*；預設：） |  |
| **mac-src**（*MAC/MASK 列表（最多 16 次）*；預設：） |  |
| **name**（*string*；預設：） | 模板的描述性名稱。 |
| **port**（*string*；預設：） | 封包模板的可選引數。它表示使用此模板生成的封包應透過哪個埠傳送。埠也可以在流設定等其他位置指定。此引數與 interface 設定互斥。 |
| **raw-header**（*string（最多 16 次）*；預設：） | 以十六進位制字串格式表示的原始封包頭。 |
| **udp-dst-port**（*埠 [0..65535]/掩碼 [0..FFFF] 列表（最多 16 次）*；預設：） |  |
| **udp-src-port**（*埠 [0..65535]/掩碼 [0..FFFF] 列表（最多 16 次）*；預設：） |  |
| **vlan-id**（；預設：） |  |
| **vlan-priority**（；預設：） |  |
| **vlan-protocol**（；預設：） |  |
| **header-stack**（*ip \| mac \| raw \| udp \| vlan 列表（最多 16 次）*；預設：**ip**） | 生成的封包應具有的頭序列。當前支援：mac - 乙太網頭（14 位元組）vlan - 乙太網 VLAN 標籤（4 位元組）ip - IPv4 頭（20 位元組）udp - UDP 頭（8 位元組）raw - 以十六進位制字串指定的任意位元組 大多數頭型別可以在包頭中多次出現。每個封包只能有 2 個 IP 頭和 1 個 UDP 頭。根據我們在網路協定方面的實踐經驗，對可能的頭序列有一些限制（例如，VLAN 頭只能跟在 mac 頭或另一個 VLAN 頭之後）。流量生成器會為封包模板建議第一個頭（在 port 選單中）。但這並不強制執行。 |

## 埠配置 {#port-configuration}

**子選單：** `/tool/traffic-generator/port`

此選單允許配置埠，這些埠將與特定介面關聯，並用於接收/傳送生成的封包。

**屬性**

| 屬性 | 描述 |
| :-- | :-- |
| **disabled**（*yes \| no*；預設：**no**） | 埠是否已停用，並且不參與接收/傳送封包 |
| **name**（*string*；預設：） | 埠的描述性名稱 |
| **interface**（*string*；預設：） | 與埠關聯的介面名稱。 |

### 只讀屬性 {#read-only-properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **dynamic**（*yes \| no*） | 埠配置是否自動生成。 |
| **first-header**（*ip \| mac \| raw \| udp \| vlan*） | 顯示建議從指定介面傳送的封包所使用的第一個頭。建立封包模板時可以使用此資訊。 |
| **inactive**（*yes \| no*） | 埠是否處於非活動狀態，並且無法參與封包的 TX/RX。 |

## 統計 {#stats}

**子選單：** `/tool/traffic-generator/stats`

如果流量生成器未在 **quick** 模式下執行，則有關測試的所有統計資訊都儲存在此選單中。

### 延遲分佈 {#latency-distribution}

**子選單：** `/tool/traffic-generator/stats/latency-distribution`

此子選單顯示在特定延遲範圍內接收了多少封包。可以按流或按序列檢視延遲範圍（例如，**print stream-num=3**、**print seq=10**）

以下是延遲圖表示例輸出：

```ros
[admin@test-host] /tool/traffic-generator/stats/latency-distribution> print            
 # LATENCY                 COUNT        SHARE GRAPH                                               
 0 0-15.5us                    0           0%
 1 15.5us-31us                 0           0%
 2 31us-46.5us                 0           0%
 3 46.5us-62.1us               0           0%
 4 62.1us-77.6us               0           0%
 5 77.6us-93.1us               0           0%
 6 93.1us-109us                0           0%
 7 109us-124us                 0           0%
 8 124us-140us                 0           0%
 9 140us-155us                 0           0%
10 155us-171us                 0           0%
11 171us-186us                 4           0% *                                                   
12 186us-202us                29           0% *                                                   
13 202us-217us                90       0.001% *                                                   
14 217us-233us               302       0.004% *                                                   
15 233us-248us               630       0.009% *                                                   
16 248us-264us               789       0.011% *                                                   
17 264us-279us             1 384       0.021% -*                                                  
18 279us-295us             1 990        0.03% --*                                                 
19 295us-310us             2 966       0.045% ---*                                                
20 310us-326us             4 089       0.062% -----*                                              
21 326us-341us             4 958       0.075% ------*                                             
22 341us-357us             6 059       0.091% -------*                                            
23 357us-372us             6 660       0.101% --------*                                           
24 372us-388us             8 320       0.126% ----------*                                         
25 388us-403us             9 988       0.151% -------------*                                      
26 403us-419us            11 781       0.178% ---------------*                                    
27 419us-434us            12 512       0.189% ----------------*                                   
28 434us-450us            13 836        0.21% -----------------*                                  
29 450us-465us            15 681       0.238% --------------------*                               
30 465us-481us            17 740       0.269% ----------------------*                             
31 481us-496us            19 913       0.302% --------------------------*                         
32 496us-512us            21 106        0.32% ---------------------------*                        
33 512us-528us            22 848       0.346% -----------------------------*                      
34 528us-543us            25 059        0.38% --------------------------------*                   
35 543us-559us            26 593       0.403% ----------------------------------*                 
36 559us-574us            27 663       0.419% -----------------------------------*                
37 574us-590us            29 351       0.445% -------------------------------------*              
38 590us-605us            31 265       0.474% ----------------------------------------*           
39 605us-621us            33 224       0.504% -------------------------------------------*        
40 621us-636us            34 464       0.523% --------------------------------------------*       
41 636us-652us            35 630        0.54% ----------------------------------------------*     
42 652us-667us            37 245       0.565% ------------------------------------------------*   
43 667us-683us            38 158       0.579% -------------------------------------------------*  
44 683us-698us            38 626       0.586% --------------------------------------------------* 
45 698us-714us            38 985       0.591% --------------------------------------------------* 
46 714us-729us            39 061       0.592% --------------------------------------------------* 
47 729us-745us            39 750       0.603% ---------------------------------------------------*
48 745us-760us            39 145       0.594% --------------------------------------------------* 
49 760us-776us            39 162       0.594% --------------------------------------------------* 
50 776us-791us            38 197       0.579% -------------------------------------------------*  
51 791us-807us            37 811       0.573% -------------------------------------------------*  
52 807us-822us            37 364       0.567% ------------------------------------------------*   
53 822us-838us            36 770       0.558% -----------------------------------------------*    
54 838us-853us            35 831       0.543% ----------------------------------------------*     
55 853us-869us            35 380       0.536% ----------------------------------------------*     
56 869us-884us            34 472       0.523% --------------------------------------------*       
57 884us-900us            33 672       0.511% -------------------------------------------*        
58 900us-915us            33 799       0.513% --------------------------------------------*       
59 915us-931us            32 754       0.497% ------------------------------------------*         
60 931us-946us            32 339        0.49% ------------------------------------------*         
61 946us-962us            32 419       0.492% ------------------------------------------*         
62 962us-977us            32 107       0.487% -----------------------------------------*          
63 977us-993us            31 552       0.478% -----------------------------------------*          
64 0-993us             1 221 523       18.54%
```

## 屬性 {#properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **count**（*integer*） | 當前延遲範圍內的封包數量 |
| **graph**（*string*） | 佔比的圖形表示 |
| **latency**（*string*） | 延遲範圍 |
| **share**（*percent*） | 落入此延遲範圍的封包百分比。 |

### 流統計 {#stream-stats}

**子選單：** `/tool/traffic-generator/stats/stream`

此子選單儲存按流排序的統計資訊。輸出與 **quick** 模式相同。

```ros
[admin@test-host] /tool/traffic-generator/stats/stream> print 
 # SEQ    NUM     TX-PACKET   TX-RATE     RX-PACKET   RX-RATE   LOST-PACKET LOST-RATE
 0 1      3          43 064 499.5Mbps        25 180 292.0Mbps        17 884 207.4Mbps
 1 1      4          43 062 499.5Mbps        39 946 463.3Mbps         3 116  36.1Mbps
 2 1      TOT        86 126 999.0Mbps        65 126 755.4Mbps        21 000 243.6Mbps
 3 2      3          43 544 505.1Mbps        30 449 353.2Mbps        13 095 151.9Mbps
 4 2      4          43 543 505.0Mbps        42 982 498.5Mbps           561   6.5Mbps
 5 2      TOT        87 087 1010.2...        73 431 851.7Mbps        13 656 158.4Mbps

... 

59 20     TOT        87 277 1012.4...        73 755 855.5Mbps        13 522 156.8Mbps
60 21     3          43 546 505.1Mbps        30 605 355.0Mbps        12 941 150.1Mbps
61 21     4          43 546 505.1Mbps        42 682 495.1Mbps           864  10.0Mbps
62 21     TOT        87 092 1010.2...        73 287 850.1Mbps        13 805 160.1Mbps
63 TOT    3         913 942 504.8Mbps       629 210 347.5Mbps       284 732 157.2Mbps
64 TOT    4         913 939 504.8Mbps       898 374 496.2Mbps        15 565   8.5Mbps
65 TOT    TOT     1 827 881 1009.6...     1 527 584 843.8Mbps       300 297 165.8Mbps
```

### 埠統計 {#port-stats}

**子選單：** `/tool/traffic-generator/stats/port`

此子選單儲存按 RX/TX 埠排序的統計資訊。

```ros
[admin@test-host] /tool/traffic-generator/stats/port> print 
 # SEQ    PORT        RX-UNK-PACKET    RX-UNK-BYTE RX-UNK...     TX-PACKET   TX-RATE     RX-PACKET
 0 1      port0:et...             0              0      0bps        43 064 499.5Mbps        39 946
 1 1      port1:et...             0              0      0bps        43 062 499.5Mbps        25 180
 2 1      TOT                     0              0      0bps        86 126 999.0Mbps        65 126
 3 2      port0:et...             0              0      0bps        43 544 505.1Mbps        42 982
 4 2      port1:et...             0              0      0bps        43 543 505.0Mbps        30 449
 5 2      TOT                     0              0      0bps        87 087 1010.2...        73 431
 6 3      port0:et...             0              0      0bps        43 540 505.0Mbps        42 615
 7 3      port1:et...             0              0      0bps        43 540 505.0Mbps        30 191
 8 3      TOT                     0              0      0bps        87 080 1010.1...        72 806
```

### 原始統計 {#raw-stats}

**子選單：** `/tool/traffic-generator/stats/raw`

此子選單儲存原始統計資料。

```ros
[admin@test-host] /tool/traffic-generator/stats/raw> print 
 # SEQ    PORT       NUM     TX-PACKET   TX-RATE     RX-PACKET   RX-RATE   LOST-PACKET LOST-RATE
 0 1      port0:e... 3          43 064 499.5Mbps             0      0bps        43 064 499.5Mbps
 1 1      port1:e... 3               0      0bps        25 180 292.0Mbps       -25 180 292.0Mbps
 2 1      TOT        3          43 064 499.5Mbps        25 180 292.0Mbps        17 884 207.4Mbps
 3 1      port0:e... 4               0      0bps        39 946 463.3Mbps       -39 946 463.3Mbps
 4 1      port1:e... 4          43 062 499.5Mbps             0      0bps        43 062 499.5Mbps
 5 1      TOT        4          43 062 499.5Mbps        39 946 463.3Mbps         3 116  36.1Mbps
 6 1      port0:e... TOT        43 064 499.5Mbps        39 946 463.3Mbps         3 118  36.1Mbps
 7 1      port1:e... TOT        43 062 499.5Mbps        25 180 292.0Mbps        17 882 207.4Mbps
 8 2      port0:e... 3          43 544 505.1Mbps             0      0bps        43 544 505.1Mbps
 9 2      port1:e... 3               0      0bps        30 449 353.2Mbps       -30 449 353.2Mbps
10 2      TOT        3          43 544 505.1Mbps        30 449 353.2Mbps        13 095 151.9Mbps
```

## 流 {#streams}

### 屬性 {#properties-2}

| 屬性 | 描述 |
| :-- | :-- |
| **disabled**（*yes \| no*；預設：**no**） | 流是否已停用 |
| **mbps**（*integer [0..4294967295]*；預設：**0**） | 該流將嘗試生成的速率值，單位為兆位元每秒。 |
| **name**（*string*；預設：） | 流的描述性名稱。 |
| **num**（*integer [0..15]*；預設：**0**） |  |
| **packet-size**（*integer[1..65535] [-integer[1..65535]]*；預設：**0**） | 生成封包的大小，以位元組為單位。可設定為範圍，用於隨機生成封包大小。 |
| **port**（*string*；預設：） | Port 選單中的埠名稱，將用於傳送封包。 |
| **pps**（*integer [0..4294967295]*；預設：**0**） | 該流將嘗試生成的封包每秒數量。 |
| **tx-template**（*string*；預設：） | 來自 packet-template 或 raw-packet-template 選單的封包模板名稱，用作封包內容來源。 |

## 配置示例 {#configuration-examples}

### IPsec 隧道效能測試 {#ipsec-tunnel-performance-test}

考慮以下測試設定

![](/img/5bae37f27f75c657.webp)

被測系統（SUT）由兩臺連線到流量生成器伺服器的路由器組成。兩臺 SUT 路由器之間的連線使用 IPsec 加密。

流量生成器將執行兩個流：

- 方向為從 1.1.1.0/24 網路到 2.2.2.0/24 網路。
- 方向為從 2.2.2.0/24 網路到 1.1.1.0/24 網路。

#### R1 路由和 IPsec 設定 {#r1-routing-and-ipsec-setup}

```ros
/ip/address
add address=192.168.33.1/30 interface=ether1
add address=1.1.1.2/24 interface=ether2

/ip/route 
add dst-address=2.2.2.0/24 gateway=192.168.33.2

/ip/ipsec/proposal
set default enc-algorithms=aes-128

/ip/ipsec/peer
add address=192.168.33.2 secret=123

/ip/ipsec/policy
add sa-src-address=192.168.33.1 sa-dst-address=192.168.33.2 \
    src-address=1.1.1.0/24 dst-address=2.2.2.0/24 tunnel=yes
```

#### R2 路由和 IPsec 設定 {#r2-routing-and-ipsec-setup}

```ros
/ip/address
add address=192.168.33.2/30 interface=ether1
add address=2.2.2.2/24 interface=ether2

/ip/route 
add dst-address=1.1.1.0/24 gateway=192.168.33.1

/ip/ipsec/proposal
set default enc-algorithms=aes-128

/ip/ipsec/peer
add address=192.168.33.1 secret=123

/ip/ipsec/policy
add sa-src-address=192.168.33.2 sa-dst-address=192.168.33.1 \
    src-address=2.2.2.0/24 dst-address=1.1.1.0/24 tunnel=yes
```

#### 流量生成器伺服器設定 {#traffic-generator-server-setup}

```ros
/ip/address
add address=1.1.1.1/24 interface=ether2
add address=2.2.2.1/24 interface=ether3
```

首先，我們將定義哪些埠用作流量生成器的 TX/RX 埠。

```ros
/tool/traffic-generator/port
add disabled=no interface=ether2 name=port0
add disabled=no interface=ether3 name=port1
```

為了構造實際要生成的封包，需要使用 packet-template。

```ros
/tool/traffic-generator/packet-template
add header-stack=mac,ip,udp ip-dst=2.2.2.1/32 ip-gateway=1.1.1.2 ip-src=1.1.1.1/32 \
    name=routing-1 port=port0
add header-stack=mac,ip,udp ip-dst=1.1.1.1/32 ip-gateway=2.2.2.2 ip-src=2.2.2.1/32 \
    name=routing-2 port=port1
```

請注意，未指定 MAC 地址，因為模板生成器可以透過傳送 ARP 訊息自動假定下一跳 MAC 地址。由於我們進行的是路由，且目標 IP 不直接可達，因此我們設定了 **ip-gateway** 引數來確定下一跳 MAC 地址。

執行 **print** 時，可以看到所有假定（檢測到）的值，包括 MAC 地址。

```ros
[admin@test-host] /tool/traffic-generator/packet-template> print 
 0 name="routing-1" header-stack=mac,ip,udp port=port0 
   assumed-mac-dst=00:0C:42:00:38:9D assumed-mac-src=00:0C:42:40:94:25 
   assumed-mac-protocol=ip assumed-ip-dscp=0 assumed-ip-id=0 
   assumed-ip-frag-off=0 assumed-ip-ttl=64 assumed-ip-protocol=udp 
   ip-src=1.1.1.1/32 ip-dst=2.2.2.1/32 assumed-udp-src-port=100 
   assumed-udp-dst-port=200 ip-gateway=1.1.1.2 data=uninitialized data-byte=0 

 1 name="routing-2" header-stack=mac,ip,udp port=port1 
   assumed-mac-dst=00:0C:42:00:38:D1 assumed-mac-src=00:0C:42:40:94:26 
   assumed-mac-protocol=ip assumed-ip-dscp=0 assumed-ip-id=0 
   assumed-ip-frag-off=0 assumed-ip-ttl=64 assumed-ip-protocol=udp 
   ip-src=2.2.2.1/32 ip-dst=1.1.1.1/32 assumed-udp-src-port=100 
   assumed-udp-dst-port=200 ip-gateway=2.2.2.2 data=uninitialized data-byte=0
```

例如，如果 SUT 中的任何路由器發生變化，假定的 MAC 地址不會自動更新。要更新封包模板，只需執行以下命令：

```ros
/tool/traffic-generator/packet-template/set [find]
```

最後一部分是配置流

```ros
/tool/traffic-generator/stream
add disabled=no mbps=500 name=str1 id=3 packet-size=1450 port=port0 pps=0 \
    tx-template=routing-1
add disabled=no mbps=500 name=str3 id=4 packet-size=1450 port=port1 pps=0 \
    tx-template=routing-2
```

請注意，每個流都有一個唯一的 **id** 值。該值用於標識流的封包，否則流量生成器將無法工作。

現在我們準備執行測試。在這種情況下，將使用 **quick** 模式：

```ros
[admin@test-host] /tool/traffic-generator> quick mbps=450
SEQ    NUM     TX-PACKET   TX-RATE     RX-PACKET   RX-RATE        RX-OOO   LOST-PACKET LOST-RATE 
37     4          39 488 458.0Mbps        39 270 455.5Mbps        15 509           218   2.5Mbps 
37     TOT        78 976 916.1Mbps        76 485 887.2Mbps        22 529         2 491  28.8Mbps 
38     3          38 957 451.9Mbps        37 657 436.8Mbps         7 078         1 300  15.0Mbps 
38     4          38 958 451.9Mbps        38 402 445.4Mbps        14 763           556   6.4Mbps 
38     TOT        77 915 903.8Mbps        76 059 882.2Mbps        21 841         1 856  21.5Mbps 
39     3          38 816 450.2Mbps        37 893 439.5Mbps         7 307           923  10.7Mbps 
39     4          38 815 450.2Mbps        38 642 448.2Mbps        15 110           173   2.0Mbps 
39     TOT        77 631 900.5Mbps        76 535 887.8Mbps        22 417         1 096  12.7Mbps 
40     3          39 779 461.4Mbps        37 415 434.0Mbps         7 136         2 364  27.4Mbps 
40     4          39 780 461.4Mbps        39 567 458.9Mbps        15 908           213   2.4Mbps 
40     TOT        79 559 922.8Mbps        76 982 892.9Mbps        23 044         2 577  29.8Mbps 
41     3          39 218 454.9Mbps        37 089 430.2Mbps         7 075         2 129  24.6Mbps 
41     4          39 218 454.9Mbps        38 663 448.4Mbps        15 752           555   6.4Mbps 
41     TOT        78 436 909.8Mbps        75 752 878.7Mbps        22 827         2 684  31.1Mbps 
42     3          39 188 454.5Mbps        37 906 439.7Mbps         6 729         1 282  14.8Mbps 
42     4          39 187 454.5Mbps        38 954 451.8Mbps        15 565           233   2.7Mbps 
42     TOT        78 375 909.1Mbps        76 860 891.5Mbps        22 294         1 515  17.5Mbps 
TOT    3       1 645 468 454.4Mbps     1 568 201 433.1Mbps       280 174        77 267  21.3Mbps 
TOT    4       1 645 464 454.4Mbps     1 626 896 449.3Mbps       627 480        18 568   5.1Mbps 
TOT    TOT     3 290 932 908.9Mbps     3 195 097 882.4Mbps       907 654        95 835  26.4Mbps
```

統計資訊顯示每個流的吞吐量、兩個流的總吞吐量、亂序封包數量、丟包率、延遲和抖動。
