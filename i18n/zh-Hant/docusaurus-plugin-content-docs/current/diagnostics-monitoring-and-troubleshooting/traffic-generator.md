---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/traffic-generator"
sidebar_position: 9
title: "流量生成器"
sidebar_label: "流量生成器"
description: "Traffic Generator 是一款 MikroTik RouterOS 工具，透過在埠上生成併發送原始封包來評估裝置效能，並收集延遲、抖動、吞吐量和丟包資料。它支援 OOO 檢測和 PCAP 注入等高階功能，並提供可配置的屬性和命令，便於快速完成設定。"
tags:
  - 'traffic-generator'
  - 'packet-generation'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/traffic-generator
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Traffic Generator 是一款工具，可用於評估 DUT（被測裝置）或 SUT（被測系統）的效能。

該工具可以透過特定埠生成併發送原始封包。它還會收集延遲和抖動值、TX/RX 速率，統計丟失的封包數量，並檢測亂序（OOO）封包。

Traffic Generator 的用法與 [頻寬測試](./bandwidth-test.md) 工具類似，也可用於生成封包，這些封包會被路由回封包生成器，以便進行高階狀態收集。

流量生成器的所有屬性和命令均在 [`/tool/traffic-generator` CLI 參考](../cli-reference/tool/traffic-generator/index.md) 中描述。

:::info
在生成封包的裝置上，流量生成器生成的封包無法透過嗅探工具、torch 或出介面上的防火牆捕獲。

由於該工具可能被惡意使用，它在每種 [裝置模式](../system-information-and-utilities/device-mode.md) 下預設處於停用狀態。當 `traffic-gen` 處於停用狀態時，`quick` 會以 `not allowed by device-mode` 錯誤失敗。執行 `/system/device-mode/print` 可以檢視當前值。若要啟用，請執行 `/system/device-mode/update traffic-gen=yes`，並在啟用超時時間（預設 5 分鐘）內透過裝置上的物理操作確認更改：按下復位按鈕或 mode 按鈕，或拔掉電源。確認後設備會重啟；普通重啟會取消該更改。參見 [更改 device-mode](../system-information-and-utilities/device-mode.md#change-device-mode)。
:::

## 常規 {#general}

**子選單：** `/tool/traffic-generator`

此選單儲存流量生成器的整體設定：當前測量會話的 `test-id`、是否測量亂序（OOO）封包（`measure-out-of-order`）、延遲分佈的最大延遲範圍（`latency-distribution-max`）以及保留多少統計資料樣本（`stats-samples-to-keep`）。它還顯示生成器是否正在執行（`running`）以及當前延遲測量範圍（`latency-distribution-measure-interval`、`latency-distribution-samples`）。

### 命令 {#commands}

| 命令 | 描述 |
| :-- | :-- |
| **quick** | 啟動封包生成器，將統計資訊列印到終端，並彙總延遲/抖動報告。接受可覆蓋封包模板和流設定的引數：**cpu-core, entries-to-show, id, interface, mbps, measure-out-of-order, packet-count, packet-size, port, pps, stream, test-id, tx-template**。執行 quick 命令時指定的引數會覆蓋已配置的值；如果僅為某個頭部指定了引數，則該值會（在需要時）乘到所有其他頭部。 |
| **start** | 在後臺啟動 Traffic Generator。接受的覆蓋引數與 **quick** 相同，但 `entries-to-show` 除外（沒有終端輸出）。 |
| **stop** | 停止透過 **start** 命令啟動的後臺 Traffic Generator。 |
| **inject** | 將原始資料注入介面。 |
| **inject-pcap** | 在介面上重放 PCAP 或 PCAPNG 檔案中的封包。[嗅探工具](./packet-sniffer.md)以 PCAPNG 格式儲存抓包檔案，Traffic Generator 支援這種格式。 |

## 封包模板 {#packet-template}

**子選單：** `/tool/traffic-generator/packet-template`

此子選單根據頭部引數構建流的封包內容。根據這些引數，你可以構建帶 VLAN 標籤的 IP 封包、設定 UDP 或 TCP 埠，或構建 IPv6 封包。系統會根據提供的引數生成原始封包模板。完整引數列表在 [packet-template CLI 參考](../cli-reference/tool/traffic-generator/packet-template.md) 中描述。

如果你需要更底層的封包，或希望充分利用 Traffic Generator，請使用 raw-packet-template 構建器來構建封包。

如果同一型別的頭部在封包中出現多次，頭欄位值會以逗號分隔列表的形式傳遞。例如，如果有兩個 IP 頭部，源地址會像這樣給出：`ip-src=1.1.1.1,2.2.2.2`。

為了更快地構造頭部，許多頭欄位值是被假定的。例如，如果頭部棧為 "mac, ip"，流量生成器會假定 mac-protocol 值為 "ip"。或者，如果指定了 "port" 或 "interface" 設定，流量生成器會假定 "mac-src" 為該介面的 MAC 地址。假定值具有以 "assumed-" 開頭的不同名稱，並且是隻讀的。手動指定的值會覆蓋假定值。

:::info
假設值不會自動更新。編輯模板後會重新計算假設值——執行 `/tool/traffic-generator/packet-template/set [find]` 即可觸發新的假設值。
:::

`header-stack` 屬性定義所生成封包中頭部的順序。它支援 **mac**（Ethernet，14 位元組）、**vlan**（802.1Q 標籤，4 位元組）、**ip**（IPv4，20 位元組）、**udp**（UDP，8 位元組）、**raw**（以十六進位制字串表示的任意位元組）、**ipv6**（IPv6，40 位元組）和 **tcp**（TCP，可變長度）。序列限制遵循協定規則——例如，VLAN 頭部只能跟在 mac 頭部或另一個 VLAN 頭部之後；每個封包最多允許兩個 IP 頭部和一個 UDP 頭部。進一步限制（例如針對重複的 IPv6 或 TCP 頭部）會在建立模板時進行驗證。流量生成器會為封包模板建議第一個頭部（在 port 選單中），但不會強制使用第一個頭部。

## 埠配置 {#port-configuration}

**子選單：** `/tool/traffic-generator/port`

此選單配置將介面繫結到流量生成器以傳送和接收所生成封包的 port。當封包模板僅指定 `interface` 時，會自動建立一個 port 條目（動態）。`disabled` 標誌（參見 CLI 參考）會阻止該 port 傳送和接收；示例將其設定為 `disabled=no` 以明確表示。port 的只讀 `first-header` 屬性顯示從該介面發出的封包所建議的第一個頭部：`mac`、`vlan`、`ip`、`udp`、`raw`、`ipv6` 或 `tcp`。所有屬性和標誌都在 [port CLI 參考](../cli-reference/tool/traffic-generator/port.md) 中描述。

## 統計 {#stats}

**子選單：** `/tool/traffic-generator/stats`

如果流量生成器未在 **quick** 模式下執行，有關測試的所有統計資訊都會儲存在此選單中，而不會列印到終端。

### 延遲分佈 {#latency-distribution}

**子選單：** `/tool/traffic-generator/stats/latency-distribution`

此子選單顯示在特定延遲範圍內接收到了多少個數據包。延遲範圍可按流或按序列檢視，例如 `print stream-id=3` 或 `print seq=10`。

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

這些列在 [latency-distribution CLI 參考](../cli-reference/tool/traffic-generator/stats/latency-distribution.md) 中描述。

### 流統計 {#stream-stats}

**子選單：** `/tool/traffic-generator/stats/stream`

此子選單儲存按流排序的統計資訊。輸出與 **quick** 模式相同。

```ros
[admin@test-host] /tool/traffic-generator/stats/stream> print 
 # SEQ    ID      TX-PACKET   TX-RATE     RX-PACKET   RX-RATE   LOST-PACKET LOST-RATE
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
 # SEQ    PORT       ID      TX-PACKET   TX-RATE     RX-PACKET   RX-RATE   LOST-PACKET LOST-RATE
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

所有統計列（seq、id、tx/rx 計數器與速率、out-of-order、bad-checksum、lost、latency 和 jitter）在 [stream](../cli-reference/tool/traffic-generator/stats/stream.md)、[port](../cli-reference/tool/traffic-generator/stats/port.md) 和 [raw](../cli-reference/tool/traffic-generator/stats/raw.md) CLI 參考頁面中描述。

## 流 {#streams}

**子選單：** `/tool/traffic-generator/stream`

一個 stream 定義生成的流量：使用的封包模板（`tx-template`，必需）及其傳送所經過的埠（`port`，通常取自模板）、傳輸速率（`pps` 和/或 `mbps`）、L2 封包大小（`packet-size`，可為隨機大小的範圍）、要傳送的封包數量（`packet-count`）以及 stream 所繫結到的 CPU 核心（或核心範圍）（`cpu-core`，用於多核測試）。其只讀的 `default-port` 顯示 stream 傳送所用的埠，該埠派生自模板。所有屬性都在 [stream CLI 參考](../cli-reference/tool/traffic-generator/stream.md) 中描述。

每個 stream 都有一個唯一的 `id`（舊屬性名 `num` 不再使用），用於在統計資訊以及 **start** 和 **quick** 命令中標識其封包。

## 配置示例 {#configuration-examples}

### IPsec 隧道效能測試 {#ipsec-tunnel-performance-test}

考慮以下測試設定：

![Traffic generator IPsec test setup](/img/5bae37f27f75c657.webp)

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
set default enc-algorithms=aes-128-cbc

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
set default enc-algorithms=aes-128-cbc

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

首先，定義哪些埠將用作流量生成器的 TX/RX 埠：

```ros
/tool/traffic-generator/port
add disabled=no interface=ether2 name=port0
add disabled=no interface=ether3 name=port1
```

為了構造將要生成的實際封包，使用 packet-template：

```ros
/tool/traffic-generator/packet-template
add header-stack=mac,ip,udp ip-dst=2.2.2.1/32 ip-gateway=1.1.1.2 ip-src=1.1.1.1/32 \
    name=routing-1 port=port0
add header-stack=mac,ip,udp ip-dst=1.1.1.1/32 ip-gateway=2.2.2.2 ip-src=2.2.2.1/32 \
    name=routing-2 port=port1
```

請注意，未指定 MAC 地址，因為模板生成器可以透過傳送 ARP 訊息自動推斷下一跳 MAC 地址。由於執行了路由且目標 IP 不能直接到達，因此設定 **ip-gateway** 引數以確定下一跳 MAC 地址。

執行 **print** 時，可以看到所有假定的（檢測到的）值，包括 MAC 地址：

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

如果 SUT 中的任何路由器發生更改，假定的 MAC 地址將不會自動更新。要更新封包模板，請執行以下命令：

```ros
/tool/traffic-generator/packet-template/set [find]
```

最後一部分是配置流：

```ros
/tool/traffic-generator/stream
add disabled=no mbps=500 name=str1 id=3 packet-size=1450 port=port0 pps=0 \
    tx-template=routing-1
add disabled=no mbps=500 name=str3 id=4 packet-size=1450 port=port1 pps=0 \
    tx-template=routing-2
```

請注意，每個流都有唯一的 **id** 值。該值用於標識流封包；沒有它，流量生成器將無法工作。

現在測試已準備好執行。在本例中，使用 **quick** 模式：

```ros
[admin@test-host] /tool/traffic-generator> quick mbps=450
SEQ    ID      TX-PACKET   TX-RATE     RX-PACKET   RX-RATE        RX-OOO   LOST-PACKET LOST-RATE 
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

統計資訊顯示每個流的吞吐量以及兩個流的總吞吐量、Out-of-Order 封包計數、丟包率、延遲和抖動。
