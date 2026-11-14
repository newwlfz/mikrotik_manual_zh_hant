---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/port/index"
sidebar_position: 1
title: "port"
sidebar_label: 'port'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/qos/port
captured_at: '2026-11-01T21:22:40+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/port {#interfaceethernetswitchqosport}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 目錄

此子選單用於配置單個交換器埠的 QoS 設定。它允許您為到達特定埠的入站封包分配 QoS 配置檔案。如果埠配置為受信任，則分配的配置檔案可能會被基於封包報頭值的匹配規則覆蓋。

預設情況下，所有埠都不受信任，並接收預設 QoS 配置檔案（Best-Effort，PCP=0，DSCP=0）。在此預設狀態下，優先順序欄位會從出站封包中清除。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="profile" typ="enum" syscap="crs_prestera">預設分配給入向封包的 QoS 配置檔案。</ArgTableRow>
<ArgTableRow arg="map" typ="enum" syscap="crs_prestera">QoS 封包到配置檔案的對映。</ArgTableRow>
<ArgTableRow arg="trust-l2" typ="enum (ignore | trust | keep) { ignore:0, trust:1, keep:2 }" syscap="crs_prestera">信任二層頭部（PCP）以用於 QoS 對映。</ArgTableRow>
<ArgTableRow arg="trust-l3" typ="enum (ignore | trust | keep) { ignore:0, trust:1, keep:2 }" syscap="crs_prestera">信任三層頭部（DSCP）以用於 QoS 對映。</ArgTableRow>
<ArgTableRow arg="tx-manager" typ="enum" syscap="crs_prestera">用於此埠出向流量的 QoS 傳送管理器。</ArgTableRow>
<ArgTableRow arg="pfc" typ="enum" syscap="!prestera-ac3">用於此埠入向流量的優先順序流控配置檔案。</ArgTableRow>
<ArgTableRow arg="egress-rate-queue0" typ="num" syscap="switch-rate">佇列 0 的出向速率限制。</ArgTableRow>
<ArgTableRow arg="egress-rate-queue1" typ="num" syscap="switch-rate">佇列 1 的出向速率限制。</ArgTableRow>
<ArgTableRow arg="egress-rate-queue2" typ="num" syscap="switch-rate">佇列 2 的出向速率限制。</ArgTableRow>
<ArgTableRow arg="egress-rate-queue3" typ="num" syscap="switch-rate">佇列 3 的出向速率限制。</ArgTableRow>
<ArgTableRow arg="egress-rate-queue4" typ="num" syscap="switch-rate">佇列 4 的出向速率限制。</ArgTableRow>
<ArgTableRow arg="egress-rate-queue5" typ="num" syscap="switch-rate">佇列 5 的出向速率限制。</ArgTableRow>
<ArgTableRow arg="egress-rate-queue6" typ="num" syscap="switch-rate">佇列 6 的出向速率限制。</ArgTableRow>
<ArgTableRow arg="egress-rate-queue7" typ="num" syscap="switch-rate">佇列 7 的出向速率限制。</ArgTableRow>
</ArgTable>
**埠統計**

```ros
[admin@Mikrotik] /interface/ethernet/switch/qos/port> print stats where name=ether2
                  name:     ether2
             tx-packet:      2 887
               tx-byte:  3 938 897
           drop-packet:      1 799
             drop-byte:  2 526 144
      tx-queue0-packet:         50
      tx-queue1-packet:      1 871
      tx-queue3-packet:        774
      tx-queue5-packet:        192
        tx-queue0-byte:      3 924
        tx-queue1-byte:  2 468 585
        tx-queue3-byte:  1 174 932
        tx-queue5-byte:    291 456
    drop-queue1-packet:      1 799
      drop-queue1-byte:  2 526 144
```

**埠資源/使用情況**

:::danger
由於硬體限制，某些交換晶片型號在訪問 QoS 埠 `usage` 資料時可能會中斷流量。埠 `usage` 僅用於診斷/故障排除。若要監控，請改用 QoS `monitor` 或埠 `stats`。
:::

```ros
[admin@crs326] /interface/ethernet/switch/qos/port> print usage where name=ether2
                 name:  ether2
           packet-cap:     136
           packet-use:       5
             byte-cap:  35 840
             byte-use:   9 472
    queue0-packet-cap:     130
    queue0-packet-use:       1
    queue1-packet-cap:       5
    queue1-packet-use:       4
    queue3-packet-cap:      65
    queue3-packet-use:       2
      queue0-byte-cap:  24 576
      queue0-byte-use:     256
      queue1-byte-cap:   7 680
      queue1-byte-use:   6 144
      queue3-byte-cap:  14 080
      queue3-byte-use:   3 072
```

**埠 PFC 統計資訊（上一代）**
```ros
[admin@crs317] /interface/ethernet/switch/qos/port> print pfc interval=1 where running
                 name:  sfp-sfpplus1 sfp-sfpplus2   ether1
                  pfc:          roce     disabled disabled
               pfc-tx:            46            
        pfc-paused-tc:             3            
 pfc3-pause-threshold:     1 048 576            
pfc3-resume-threshold:        10 240            
             pfc3-use:     1 075 200
```

**埠 PFC 統計資訊（新一代）**
```routeros
[admin@crs812] /interface/ethernet/switch/qos/port> print pfc interval=1 where pfc=roce
                 name:       sfp56-5 
                  pfc:          roce
             rx-pause:           287              
             tx-pause:            46             
             pfc3-use:     2 184 200 
```

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">埠名稱。</ArgTableRow>
<ArgTableRow arg="switch" typ="enum">交換晶片名稱。</ArgTableRow>
<ArgTableRow arg="tx-packet" typ="multi { counter: num
 }">透過此埠傳送的封包總數。</ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="multi { counter: num
 }">透過此埠傳送的位元組總數。</ArgTableRow>
<ArgTableRow arg="packet-use" typ="num" syscap="!prestera-cpss">埠的封包使用量。當前在所有埠佇列中排隊的封包數量。</ArgTableRow>
<ArgTableRow arg="byte-use" typ="num">埠的位元組使用量。當前為已排隊封包分配的硬體緩衝區大小（以位元組為單位）。由於緩衝區按塊分配（通常每塊 256B），分配的緩衝區大小可能大於實際載荷。</ArgTableRow>
<ArgTableRow arg="queue0-shared-packet-cap" typ="num" syscap="prestera-bc2">佇列 0 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue1-shared-packet-cap" typ="num" syscap="prestera-bc2">佇列 1 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue2-shared-packet-cap" typ="num" syscap="prestera-bc2">佇列 2 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue3-shared-packet-cap" typ="num" syscap="prestera-bc2">佇列 3 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue4-shared-packet-cap" typ="num" syscap="prestera-bc2">佇列 4 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue5-shared-packet-cap" typ="num" syscap="prestera-bc2">佇列 5 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue6-shared-packet-cap" typ="num" syscap="prestera-bc2">佇列 6 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue7-shared-packet-cap" typ="num" syscap="prestera-bc2">佇列 7 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue0-shared-byte-cap" typ="num" syscap="!prestera-ac3">佇列 0 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue1-shared-byte-cap" typ="num" syscap="!prestera-ac3">佇列 1 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue2-shared-byte-cap" typ="num" syscap="!prestera-ac3">佇列 2 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue3-shared-byte-cap" typ="num" syscap="!prestera-ac3">佇列 3 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue4-shared-byte-cap" typ="num" syscap="!prestera-ac3">佇列 4 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue5-shared-byte-cap" typ="num" syscap="!prestera-ac3">佇列 5 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue6-shared-byte-cap" typ="num" syscap="!prestera-ac3">佇列 6 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue7-shared-byte-cap" typ="num" syscap="!prestera-ac3">佇列 7 的共享佇列容量（單獨佇列容量 + 共享緩衝區）。</ArgTableRow>
<ArgTableRow arg="queue0-packet-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 0 的最大封包數量。</ArgTableRow>
<ArgTableRow arg="queue1-packet-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 1 的最大封包數量。</ArgTableRow>
<ArgTableRow arg="queue2-packet-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 2 的最大封包數量。</ArgTableRow>
<ArgTableRow arg="queue3-packet-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 3 的最大封包數量。</ArgTableRow>
<ArgTableRow arg="queue4-packet-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 4 的最大封包數量。</ArgTableRow>
<ArgTableRow arg="queue5-packet-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 5 的最大封包數量。</ArgTableRow>
<ArgTableRow arg="queue6-packet-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 6 的最大封包數量。</ArgTableRow>
<ArgTableRow arg="queue7-packet-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 7 的最大封包數量。</ArgTableRow>
<ArgTableRow arg="queue0-byte-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 0 的最大位元組數。</ArgTableRow>
<ArgTableRow arg="queue1-byte-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 1 的最大位元組數。</ArgTableRow>
<ArgTableRow arg="queue2-byte-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 2 的最大位元組數。</ArgTableRow>
<ArgTableRow arg="queue3-byte-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 3 的最大位元組數。</ArgTableRow>
<ArgTableRow arg="queue4-byte-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 4 的最大位元組數。</ArgTableRow>
<ArgTableRow arg="queue5-byte-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 5 的最大位元組數。</ArgTableRow>
<ArgTableRow arg="queue6-byte-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 6 的最大位元組數。</ArgTableRow>
<ArgTableRow arg="queue7-byte-cap" typ="num" syscap="!prestera-cpss">單獨佇列容量。可排隊到佇列 7 的最大位元組數。</ArgTableRow>
<ArgTableRow arg="queue0-packet-use" typ="num" syscap="!prestera-cpss">佇列封包使用量。佇列 0 中已排隊的封包數量。</ArgTableRow>
<ArgTableRow arg="queue1-packet-use" typ="num" syscap="!prestera-cpss">佇列封包使用量。佇列 1 中已排隊的封包數量。</ArgTableRow>
<ArgTableRow arg="queue2-packet-use" typ="num" syscap="!prestera-cpss">佇列封包使用量。佇列 2 中已排隊的封包數量。</ArgTableRow>
<ArgTableRow arg="queue3-packet-use" typ="num" syscap="!prestera-cpss">佇列封包使用量。佇列 3 中已排隊的封包數量。</ArgTableRow>
<ArgTableRow arg="queue4-packet-use" typ="num" syscap="!prestera-cpss">佇列封包使用量。佇列 4 中已排隊的封包數量。</ArgTableRow>
<ArgTableRow arg="queue5-packet-use" typ="num" syscap="!prestera-cpss">佇列封包使用量。佇列 5 中已排隊的封包數量。</ArgTableRow>
<ArgTableRow arg="queue6-packet-use" typ="num" syscap="!prestera-cpss">佇列封包使用量。佇列 6 中已排隊的封包數量。</ArgTableRow>
<ArgTableRow arg="queue7-packet-use" typ="num" syscap="!prestera-cpss">佇列封包使用量。佇列 7 中已排隊的封包數量。</ArgTableRow>
<ArgTableRow arg="queue0-byte-use" typ="num">佇列 0 的佇列緩衝區使用量（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue1-byte-use" typ="num">佇列 1 的佇列緩衝區使用量（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue2-byte-use" typ="num">佇列 2 的佇列緩衝區使用量（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue3-byte-use" typ="num">佇列 3 的佇列緩衝區使用量（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue4-byte-use" typ="num">佇列 4 的佇列緩衝區使用量（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue5-byte-use" typ="num">佇列 5 的佇列緩衝區使用量（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue6-byte-use" typ="num">佇列 6 的佇列緩衝區使用量（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue7-byte-use" typ="num">佇列 7 的佇列緩衝區使用量（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="byte-max" typ="num" syscap="prestera-bc2">埠緩衝區的最大填充水平（以位元組為單位）。使用 reset-counters 命令重設數值。</ArgTableRow>
<ArgTableRow arg="queue0-byte-max" typ="num" syscap="!prestera-ac3">佇列 0 的佇列緩衝區最大填充水平（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue1-byte-max" typ="num" syscap="!prestera-ac3">佇列 1 的佇列緩衝區最大填充水平（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue2-byte-max" typ="num" syscap="!prestera-ac3">佇列 2 的佇列緩衝區最大填充水平（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue3-byte-max" typ="num" syscap="!prestera-ac3">佇列 3 的佇列緩衝區最大填充水平（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue4-byte-max" typ="num" syscap="!prestera-ac3">佇列 4 的佇列緩衝區最大填充水平（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue5-byte-max" typ="num" syscap="!prestera-ac3">佇列 5 的佇列緩衝區最大填充水平（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue6-byte-max" typ="num" syscap="!prestera-ac3">佇列 6 的佇列緩衝區最大填充水平（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="queue7-byte-max" typ="num" syscap="!prestera-ac3">佇列 7 的佇列緩衝區最大填充水平（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="pfc0-pause-threshold" typ="num" syscap="prestera-bc2">流量類別 0 的暫停閾值。</ArgTableRow>
<ArgTableRow arg="pfc1-pause-threshold" typ="num" syscap="prestera-bc2">流量類別 1 的暫停閾值。</ArgTableRow>
<ArgTableRow arg="pfc2-pause-threshold" typ="num" syscap="prestera-bc2">流量類別 2 的暫停閾值。</ArgTableRow>
<ArgTableRow arg="pfc3-pause-threshold" typ="num" syscap="prestera-bc2">流量類別 3 的暫停閾值。</ArgTableRow>
<ArgTableRow arg="pfc4-pause-threshold" typ="num" syscap="prestera-bc2">流量類別 4 的暫停閾值。</ArgTableRow>
<ArgTableRow arg="pfc5-pause-threshold" typ="num" syscap="prestera-bc2">流量類別 5 的暫停閾值。</ArgTableRow>
<ArgTableRow arg="pfc6-pause-threshold" typ="num" syscap="prestera-bc2">流量類別 6 的暫停閾值。</ArgTableRow>
<ArgTableRow arg="pfc7-pause-threshold" typ="num" syscap="prestera-bc2">流量類別 7 的暫停閾值。</ArgTableRow>
<ArgTableRow arg="pfc0-resume-threshold" typ="num" syscap="prestera-bc2">流量類別 0 的恢復閾值。</ArgTableRow>
<ArgTableRow arg="pfc1-resume-threshold" typ="num" syscap="prestera-bc2">流量類別 1 的恢復閾值。</ArgTableRow>
<ArgTableRow arg="pfc2-resume-threshold" typ="num" syscap="prestera-bc2">流量類別 2 的恢復閾值。</ArgTableRow>
<ArgTableRow arg="pfc3-resume-threshold" typ="num" syscap="prestera-bc2">流量類別 3 的恢復閾值。</ArgTableRow>
<ArgTableRow arg="pfc4-resume-threshold" typ="num" syscap="prestera-bc2">流量類別 4 的恢復閾值。</ArgTableRow>
<ArgTableRow arg="pfc5-resume-threshold" typ="num" syscap="prestera-bc2">流量類別 5 的恢復閾值。</ArgTableRow>
<ArgTableRow arg="pfc6-resume-threshold" typ="num" syscap="prestera-bc2">流量類別 6 的恢復閾值。</ArgTableRow>
<ArgTableRow arg="pfc7-resume-threshold" typ="num" syscap="prestera-bc2">流量類別 7 的恢復閾值。</ArgTableRow>
<ArgTableRow arg="pfc0-use" typ="num" syscap="!prestera-ac3">流量類別 0 的當前緩衝區使用量（以位元組為單位）。換言之，它是指從本埠接收、且當前在所有埠上排隊的所有封包的總大小。僅顯示已啟用 PFC 的流量類別。</ArgTableRow>
<ArgTableRow arg="pfc1-use" typ="num" syscap="!prestera-ac3">流量類別 1 的當前緩衝區使用量（以位元組為單位）。換言之，它是指從本埠接收、且當前在所有埠上排隊的所有封包的總大小。僅顯示已啟用 PFC 的流量類別。</ArgTableRow>
<ArgTableRow arg="pfc2-use" typ="num" syscap="!prestera-ac3">流量類別 2 的當前緩衝區使用量（以位元組為單位）。換言之，它是指從本埠接收、且當前在所有埠上排隊的所有封包的總大小。僅顯示已啟用 PFC 的流量類別。</ArgTableRow>
<ArgTableRow arg="pfc3-use" typ="num" syscap="!prestera-ac3">流量類別 3 的當前緩衝區使用量（以位元組為單位）。換言之，它是指從本埠接收、且當前在所有埠上排隊的所有封包的總大小。僅顯示已啟用 PFC 的流量類別。</ArgTableRow>
<ArgTableRow arg="pfc4-use" typ="num" syscap="!prestera-ac3">流量類別 4 的當前緩衝區使用量（以位元組為單位）。換言之，它是指從本埠接收、且當前在所有埠上排隊的所有封包的總大小。僅顯示已啟用 PFC 的流量類別。</ArgTableRow>
<ArgTableRow arg="pfc5-use" typ="num" syscap="!prestera-ac3">流量類別 5 的當前緩衝區使用量（以位元組為單位）。換言之，它是指從本埠接收、且當前在所有埠上排隊的所有封包的總大小。僅顯示已啟用 PFC 的流量類別。</ArgTableRow>
<ArgTableRow arg="pfc6-use" typ="num" syscap="!prestera-ac3">流量類別 6 的當前緩衝區使用量（以位元組為單位）。換言之，它是指從本埠接收、且當前在所有埠上排隊的所有封包的總大小。僅顯示已啟用 PFC 的流量類別。</ArgTableRow>
<ArgTableRow arg="pfc7-use" typ="num" syscap="!prestera-ac3">流量類別 7 的當前緩衝區使用量（以位元組為單位）。換言之，它是指從本埠接收、且當前在所有埠上排隊的所有封包的總大小。僅顯示已啟用 PFC 的流量類別。</ArgTableRow>
<ArgTableRow arg="pfc-paused-tc" typ="multi { array-id, tc: num
 }" syscap="prestera-bc2">應被暫停的流量類別列表。PFC 暫停幀（XOFF）會按從此埠設定的所列定時器定期傳送。</ArgTableRow>
<ArgTableRow arg="pfc-unknown" typ="multi { counter: num
 }" syscap="prestera-bc2">未知 PFC 幀計數。</ArgTableRow>
<ArgTableRow arg="pfc-rx" typ="multi { counter: num
 }" syscap="prestera-bc2">接收的 PFC 幀計數。</ArgTableRow>
<ArgTableRow arg="pfc-tx" typ="num" syscap="prestera-bc2">傳送的 PFC 幀計數。</ArgTableRow>
<ArgTableRow arg="rx-pause" typ="multi { counter: num
 }" syscap="prestera-cpss">接收的暫停幀計數。</ArgTableRow>
<ArgTableRow arg="tx-pause" typ="multi { counter: num
 }" syscap="prestera-cpss">傳送的暫停幀計數。</ArgTableRow>
<ArgTableRow arg="tx-queue0-packet" typ="multi { counter: num
 }">從此埠的佇列 0 傳送的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-queue0-byte" typ="multi { counter: num
 }">從此埠的佇列 0 傳送的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-queue1-packet" typ="multi { counter: num
 }">從此埠的佇列 1 傳送的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-queue1-byte" typ="multi { counter: num
 }">從此埠的佇列 1 傳送的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-queue2-packet" typ="multi { counter: num
 }">從此埠的佇列 2 傳送的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-queue2-byte" typ="multi { counter: num
 }">從此埠的佇列 2 傳送的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-queue3-packet" typ="multi { counter: num
 }">從此埠的佇列 3 傳送的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-queue3-byte" typ="multi { counter: num
 }">從此埠的佇列 3 傳送的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-queue4-packet" typ="multi { counter: num
 }">從此埠的佇列 4 傳送的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-queue4-byte" typ="multi { counter: num
 }">從此埠的佇列 4 傳送的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-queue5-packet" typ="multi { counter: num
 }">從此埠的佇列 5 傳送的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-queue5-byte" typ="multi { counter: num
 }">從此埠的佇列 5 傳送的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-queue6-packet" typ="multi { counter: num
 }">從此埠的佇列 6 傳送的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-queue6-byte" typ="multi { counter: num
 }">從此埠的佇列 6 傳送的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-queue7-packet" typ="multi { counter: num
 }">從此埠的佇列 7 傳送的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-queue7-byte" typ="multi { counter: num
 }">從此埠的佇列 7 傳送的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-drop-packet" typ="multi { counter: num
 }">被丟棄的傳送封包總數。</ArgTableRow>
<ArgTableRow arg="tx-drop-byte" typ="multi { counter: num
 }">被丟棄的傳送位元組總數。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-packet" typ="multi { counter: num
 }">從佇列 0 丟棄的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-byte" typ="multi { counter: num
 }">從佇列 0 丟棄的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-packet" typ="multi { counter: num
 }">從佇列 1 丟棄的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-byte" typ="multi { counter: num
 }">從佇列 1 丟棄的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-packet" typ="multi { counter: num
 }">從佇列 2 丟棄的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-byte" typ="multi { counter: num
 }">從佇列 2 丟棄的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-packet" typ="multi { counter: num
 }">從佇列 3 丟棄的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-byte" typ="multi { counter: num
 }">從佇列 3 丟棄的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-packet" typ="multi { counter: num
 }">從佇列 4 丟棄的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-byte" typ="multi { counter: num
 }">從佇列 4 丟棄的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-packet" typ="multi { counter: num
 }">從佇列 5 丟棄的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-byte" typ="multi { counter: num
 }">從佇列 5 丟棄的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-packet" typ="multi { counter: num
 }">從佇列 6 丟棄的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-byte" typ="multi { counter: num
 }">從佇列 6 丟棄的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-packet" typ="multi { counter: num
 }">從佇列 7 丟棄的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-byte" typ="multi { counter: num
 }">從佇列 7 丟棄的位元組數。</ArgTableRow>
</ArgTable>
