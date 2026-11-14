---
sidebar_key: "network-management/openflow"
sidebar_position: 5
title: "OpenFlow"
sidebar_label: "OpenFlow"
description: "RouterOS 支援 OpenFlow 1.0 和 1.3 協定，用於 SDN 整合，可透過訪問交換器資料路徑的控制器應用實現集中式流量管理。它包含基本統計支援，並且在使用啟用 OpenFlow 的介面時，需要謹慎配置以避免干擾常規網路。"
tags:
  - 'openflow'
  - 'sdn'
source: https://manual.mikrotik.com/docs/7.24/network-management/openflow
captured_at: '2026-11-04T11:32:45+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 支援 OpenFlow [1.0](https://opennetworking.org/wp-content/uploads/2013/04/openflow-spec-v1.0.0.pdf) 和 [1.3](https://opennetworking.org/wp-content/uploads/2014/10/openflow-spec-v1.3.0.pdf)，它允許 OpenFlow 控制器與 OpenFlow 代理之間通訊。

OpenFlow 用於在軟體定義網路（SDN）中集中管理網路裝置。

OpenFlow 控制器上的應用可以訪問交換器的資料路徑，並執行自定義任務，例如流引導、流量監控等。

控制器傳送流以新增到代理的流表中。封包查詢、修改和轉發均基於代理上的流表完成。

RouterOS 在未使用 “goto table” 流的簡單設定中支援 OpenFlow fastpath。

OpenFlow 功能會覆蓋常規封包處理功能——在作為 OpenFlow 交換器埠的介面上接收的封包將不會經過常規網路棧，除非 OpenFlow 控制器設定了允許此操作的流。因此，在配置 OpenFlow 時必須小心，不要停用對裝置的訪問。

OpenFlow 支援以獨立的 openflow 軟體包形式提供。

### 當前支援的基本能力 {#currently-supported-basic-capabilities}

- OFPC\_FLOW\_STATS
- OFPC\_TABLE\_STATS
- OFPC\_PORT\_STATS
- OFPC\_GROUP\_STATS

### 當前不支援的基本能力 {#currently-unsupported-basic-capabilities}

- OFPC\_IP\_REASM
- OFPC\_QUEUE\_STATS
- OFPC\_PORT\_BLOCKED

### 當前不支援的配置引數和動作（版本 1） {#currently-not-supported-configuration-parameters-and-actions-version-1}

- OFPAT\_SET\_NW\_SRC
- OFPAT\_SET\_NW\_DST
- OFPAT\_SET\_NW\_TOS
- OFPAT\_SET\_TP\_SRC
- OFPAT\_SET\_TP\_DST
- OFPAT\_ENQUEUE
- OFPAT\_VENDOR

### 當前不支援的配置引數和動作（版本 1.3） {#currently-not-supported-configuration-parameters-and-actions-version-13}

- OFPT\_SET\_ASYNC
- OFPAT\_SET\_NW\_TTL
- OFPAT\_DEC\_NW\_TTL
- OFPAT\_COPY\_TTL\_OUT
- OFPAT\_COPY\_TTL\_IN

## 配置示例 {#configuration-example}

該示例演示了 sfp-sfplus1-2 埠之間非常基礎的 L2 無標記封包轉發。使用 Faucet 作為控制器。

```routeros
/openflow
add controllers=tcp/10.155.101.182/6653 datapath-id=1/DC:2C:6E:A4:B4:2E disabled=no name=faucet

/openflow/port
add disabled=no interface=sfp-sfpplus1 port-id=1 switch=faucet
add disabled=no interface=sfp-sfpplus2 port-id=2 switch=faucet
```

:::info
如果你還打算使用 Gauge，那麼請將 Gauge 的 IP 和埠新增到 controllers 列表中。示例中 6654 是 Gauge 埠：`controllers=tcp/10.155.101.182/6653,tcp/10.155.101.182/6654`
:::

Faucet 配置。dp\_id 必須與 ROS 配置中的 datapath-id 相同，採用十六進位制格式（ 1/DC:2C:6E:A4:B4:2E →  0x0001dc2c6ea4b42e ）：

```routeros
---
vlans:
    100:
        description: "untagged"

acls:
    1:
        - rule:
            actions:
                allow: 1

dps:
    test_switch:
        dp_id: 0x0001dc2c6ea4b42e
        hardware: "Generic"
        drop_broadcast_source_address: false
        drop_spoofed_faucet_mac: false
        interfaces:
            1:
                name: "h1"
                description: "host1 container"
                native_vlan: 100
                acl_in: 1
            2:
                name: "h2"
                description: "host2 container"
                native_vlan: 100
                acl_in: 1

```

可以從 `/openflow/flow` 選單檢視 Faucet 安裝的流：

```routeros
[admin@CCR2004_2XS_111] /openflow/flow>  print detail 
Flags: I - inactive 
 0   switch=faucet version=4 match=" [ { ethdst_m=01000cccccccffffffffffff } ]" actions=" []" 
     info="priority 8240, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 1   switch=faucet version=4 match=" [ { ethdst_m=01000ccccccdffffffffffff } ]" actions=" []" 
     info="priority 8240, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 2   switch=faucet version=4 match=" [ { ethdst_m=ffffffffffffffffffffffff }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8240, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 3   switch=faucet version=4 match=" [ { ethdst_m=0180c2000000fffffffffff0 } ]" actions=" []" 
     info="priority 8236, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 4   switch=faucet version=4 match=" [ { ethdst_m=0180c2000000ffffff000000 }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8216, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 5   switch=faucet version=4 match=" [ { ethdst_m=01005e000000ffffff000000 }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8216, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 6   switch=faucet version=4 match=" [ { ethdst_m=333300000000ffff00000000 }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8208, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 7   switch=faucet version=4 match=" [ { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8192, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 8   switch=faucet version=4 match=" []" actions=" []" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 9   switch=faucet version=4 match=" []" actions=" [ { goto=4 } ]" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=3 

10   switch=faucet version=4 match=" [ { ethtype=9000 } ]" actions=" []" 
     info="priority 20490, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=2 

11   switch=faucet version=4 match=" [ { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { output={ port=4294967293; max_len=96 } } ] }; { goto=3 } ]" 
     info="priority 4096, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=2 

12   switch=faucet version=4 match=" []" actions=" [ { goto=3 } ]" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=2 

13   switch=faucet version=4 match=" [ { inport=00000001 }; { vlanvid=0000 } ]" 
     actions=" [ { apply-actions= [ { pushvlan={ ethertype=33024 } }; { setfield={ vlanvid=1064 } } ] }; { goto=2 } ]" 
     info="priority 4096, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=1 

14   switch=faucet version=4 match=" [ { inport=00000002 }; { vlanvid=0000 } ]" 
     actions=" [ { apply-actions= [ { pushvlan={ ethertype=33024 } }; { setfield={ vlanvid=1064 } } ] }; { goto=2 } ]" 
     info="priority 4096, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=1 

15   switch=faucet version=4 match=" []" actions=" []" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=1 

16   switch=faucet version=4 match=" [ { inport=00000001 } ]" actions=" [ { goto=1 } ]" 
     info="priority 20480, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=0 

17   switch=faucet version=4 match=" [ { inport=00000002 } ]" actions=" [ { goto=1 } ]" 
     info="priority 20480, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=0 

18   switch=faucet version=4 match=" []" actions=" []" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=0 

19   switch=faucet version=4 match=" [ { ethdst=dc2c6ec5a7ff }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } } ] } ]" 
     info="priority 8192, idletimeout 413, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=3 

20   switch=faucet version=4 match=" [ { inport=00000001 }; { ethsrc=dc2c6ec5a7ff }; { vlanvid=1064 } ]" 
     actions=" [ { goto=3 } ]" info="priority 8191, idletimeout 0, hardtimeout 263, cookie 1524372928, removenotify 0" 
     table-id=2 

21   switch=faucet version=4 match=" [ { ethdst=dc2c6e46f893 }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=2; max_len=0 } } ] } ]" 
     info="priority 8192, idletimeout 417, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=3 

22   switch=faucet version=4 match=" [ { inport=00000002 }; { ethsrc=dc2c6e46f893 }; { vlanvid=1064 } ]" 
     actions=" [ { goto=3 } ]" info="priority 8191, idletimeout 0, hardtimeout 267, cookie 1524372928, removenotify 0" 
     table-id=2 

```

可以使用 **`stats`** 引數檢視流的統計資訊：

```routeros
[admin@CCR2004_2XS_111] /openflow/flow>  print stats 
Columns: SWITCH, MATCH, BYTES, PACKETS, DURATION
 # SWITCH  MATCH                                                                BYTES  PACKETS  DURATION  
 0 faucet   [ { ethdst_m=01000cccccccffffffffffff } ]                            3590       25  6m26s890ms
 1 faucet   [ { ethdst_m=01000ccccccdffffffffffff } ]                               0        0  6m26s890ms
 2 faucet   [ { ethdst_m=ffffffffffffffffffffffff }; { vlanvid=1064 } ]          5552       26  6m26s890ms
 3 faucet   [ { ethdst_m=0180c2000000fffffffffff0 } ]                            4917       25  6m26s890ms
 4 faucet   [ { ethdst_m=0180c2000000ffffff000000 }; { vlanvid=1064 } ]             0        0  6m26s890ms
 5 faucet   [ { ethdst_m=01005e000000ffffff000000 }; { vlanvid=1064 } ]             0        0  6m26s890ms
 6 faucet   [ { ethdst_m=333300000000ffff00000000 }; { vlanvid=1064 } ]          5992       25  6m26s890ms
 7 faucet   [ { vlanvid=1064 } ]                                                  340        5  6m26s890ms
 8 faucet   []                                                                      0        0  6m26s890ms
 9 faucet   []                                                                  20391      106  6m26s890ms
10 faucet   [ { ethtype=9000 } ]                                                    0        0  6m26s890ms
11 faucet   [ { vlanvid=1064 } ]                                                  530        8  6m26s890ms
12 faucet   []                                                                      0        0  6m26s890ms
13 faucet   [ { inport=00000001 }; { vlanvid=0000 } ]                           39135      463  6m26s890ms
14 faucet   [ { inport=00000002 }; { vlanvid=0000 } ]                           37936      459  6m26s890ms
15 faucet   []                                                                  17941      100  6m26s890ms
16 faucet   [ { inport=00000001 } ]                                             48664      515  6m26s890ms
17 faucet   [ { inport=00000002 } ]                                             46348      507  6m26s890ms
18 faucet   []                                                                      0        0  6m26s890ms
19 faucet   [ { ethdst=dc2c6ec5a7ff }; { vlanvid=1064 } ]                       28340      408  6m26s780ms
20 faucet   [ { ethdst=dc2c6e46f893 }; { vlanvid=1064 } ]                       28340      408  6m26s780ms
21 faucet   [ { inport=00000001 }; { ethsrc=dc2c6ec5a7ff }; { vlanvid=1064 } ]  12020      142  2m660ms   
22 faucet   [ { inport=00000002 }; { ethsrc=dc2c6e46f893 }; { vlanvid=1064 } ]  10769      133  1m55s660ms
```

## 統計資訊 {#statistics}

可以從 `/openflow/print fast-path` 檢視 Fastpath 統計資訊。我們可以看到，在此示例中，由於 Faucet 正在安裝的流較複雜，fast path 無法工作。

```routeros
[admin@CCR2004_2XS_111] /openflow> print fast-path 
  openflow-fast-path-packets: 0 0
    openflow-fast-path-bytes: 0 0
```

可以從 `/openflow/port` 選單檢視埠統計資訊

```routeros
[admin@CCR2004_2XS_111] /openflow/port> print stats
Columns: INTERFACE, PORT-ID, RX-BYTES, TX-BYTES, RX-PACKETS, TX-PACKETS
# INTERFACE     PORT-ID  RX-BYTES  TX-BYTES  RX-PACKETS  TX-PACKETS
0 sfp-sfpplus1        1    115668     81180        1223        1035
1 sfp-sfpplus2        2    112200     82188        1215        1037
```

## 參考 {#reference}

### 常規 {#general}

**子選單：** `/openflow`

此選單列出 OpenFlow 用戶端的配置。

| 屬性 | 描述 |
| :-- | :-- |
| **certificate** (*name*) | 證書列表中的證書名稱。與 `verify-peer` 引數一起使用。 |
| **controllers** (*list of [protocol/address/port]*) | 連線到控制器的配置。支援的協定為 **tcp** 和 **tls**。示例：tcp/1.2.3.4/6654 |
| **datapath-id** (*number/mac*) | 由兩部分（整數 [0..65535] 和 MAC 地址）組成的 Datapath ID，以斜槓分隔。 |
| **name** (*string*) | 條目的引用名稱 |
| ****passive-port**** (*disabled \| integer [1..65535]*) |  |
| **verify-peer** (*if-cert-present \| none \| required*) | 使用證書驗證對端身份 |
| ****version**** (*1 \| 1.3 \| default*) | 要使用的 OpenFlow 標準版本。 |

#### 只讀引數 {#read-only-parameters}

| 屬性 | 描述 |
| :-- | :-- |
| **openflow-fast-path-bytes** (*integer*) | 設定為快速路徑的位元組數 |
| **openflow-fast-path-packets** (*integer*) | 傳送到快速路徑的封包數 |

### 流 {#flows}

**子選單：** `/openflow/flow`

此選單列出已安裝的流，這些流負責 OpenFlow 埠之間的封包轉發。

| 屬性 | 描述 |
| :-- | :-- |
| **actions** (*string*) | 動作字串 |
| **bytes** (*integer*) | 規則匹配的位元組數 |
| **duration** (*time*) |  |
| **inactive** (*yes \| no*) |  |
| **info** (*string*) | 資訊字串 |
| **match** (*string*) | 匹配規則字串 |
| **packets** (*integer*) | 規則匹配的封包數 |
| **switch** (*name*) | 安裝該規則的控制器的名稱 |
| **table-id** (*integer*) | 規則所在表的 ID |
| **version** (*integer*) |  |

### 組 {#groups}

**子選單：** `/openflow/group`

| 屬性 | 描述 |
| :-- | :-- |
| **bucket-count** () |  |
| **bucket-stats** () |  |
| **buckets** () |  |
| **bytes** (*integer*) |  |
| **duration** (*time*) |  |
| **flow-count** (*integer*) |  |
| **id** (*integer*) |  |
| **inactive** (*yes \| no*) |  |
| **packets** (*integer*) |  |
| **switch** (*name*) |  |
| **type** () |  |

### 計量器 {#meter}

**子選單：** `/openflow/meter`

 該子選單顯示由控制器安裝的流量計量器。計量器允許在輸出和應用動作指令之前進行速率監控。

| 屬性 | 描述 |
| :-- | :-- |
| **band-count** () |  |
| **bands** () |  |
| **bytes** (*integer*) | 已統計的位元組數 |
| **duration** (*time*) |  |
| **id** (*integer*) |  |
| **inactive** (*yes \| no*) |  |
| **packets** (*integer*) | 已統計的封包數 |
| **switch** (*name*) | 安裝該規則的控制器的名稱 |

### 埠 {#ports}

**子選單：** `/openflow/port`

此選單列出由 OpenFlow 控制的埠。

| 屬性 | 描述 |
| :-- | :-- |
| **interface** (*name*) | 要由 OpenFlow 控制的介面名稱 |
| **port-id** (*integer*) | 用於在流規則中標識介面的埠 ID |
| **switch** (*name*) | 能夠控制該埠的交換器名稱。 |

#### 只讀引數 {#read-only-parameters-1}

| 屬性 | 描述 |
| :-- | :-- |
| **rx-bytes** (*integer*) | 介面上接收的位元組數 |
| **rx-packets** (*integer*) | 介面上接收的封包數 |
| **tx-bytes** (*integer*) | 介面上傳送的位元組數 |
| **tx-packets** (*integer*) | 介面上傳送的封包數 |
