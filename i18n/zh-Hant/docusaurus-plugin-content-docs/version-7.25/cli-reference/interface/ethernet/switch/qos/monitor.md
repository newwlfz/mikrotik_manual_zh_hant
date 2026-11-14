---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/monitor"
sidebar_position: 2
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/qos/monitor
captured_at: '2026-11-01T21:22:38+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/monitor {#interfaceethernetswitchqosmonitor}
**系統能力：** rbswitch 和 crs_prestera
**型別：** Command

監控硬體 QoS 資源。

```ros
[admin@crs312] /interface/ethernet/switch/qos> monitor once
           total-packet-cap: 11 480   
           total-packet-use: 0        
             total-byte-cap: 2648.0KiB
             total-byte-use: 0        
       multicast-packet-cap: 1 148    
       multicast-packet-use: 0        
         multicast-byte-cap: 264.8KiB 
         multicast-byte-use: 0        
  mirror-ingress-packet-cap: 1 148    
  mirror-ingress-packet-use: 0        
    mirror-ingress-byte-cap: 264.8KiB 
    mirror-ingress-byte-use: 0        
   mirror-egress-packet-cap: 1 148    
   mirror-egress-packet-use: 0        
     mirror-egress-byte-cap: 264.8KiB 
     mirror-egress-byte-use: 0        
      lossy-pool-packet-cap: 2 301    
      lossy-pool-packet-use: 0        
   lossless-pool-packet-cap: 2 301    
   lossless-pool-packet-use: 0        
        lossy-pool-byte-cap: 530.0KiB 
        lossy-pool-byte-use: 0        
     lossless-pool-byte-cap: 530.0KiB 
     lossless-pool-byte-use: 0 
```

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="total-packet-cap" typ="num" syscap="!prestera-cpss">封包總容量。裝置可在所有佇列中儲存的硬體封包描述符的最大數量。</ArgTableRow>
<ArgTableRow arg="total-packet-use" typ="num" syscap="!prestera-cpss">封包總使用量。當前駐留在硬體記憶體中的封包描述符數量。</ArgTableRow>
<ArgTableRow arg="total-byte-cap" typ="num">tx 記憶體總容量。</ArgTableRow>
<ArgTableRow arg="total-byte-use" typ="num">tx 記憶體總使用量。所有 tx 佇列中的封包當前佔用的位元組數。</ArgTableRow>
<ArgTableRow arg="multicast-packet-cap" typ="num" syscap="!prestera-cpss">組播封包容量。組播/廣播流量可使用的硬體封包描述符的最大數量。取決於 `multicast-buffers` 設定。</ArgTableRow>
<ArgTableRow arg="multicast-packet-use" typ="num" syscap="!prestera-cpss">組播封包使用量。硬體會為每個組播目的地複製封包描述符。</ArgTableRow>
<ArgTableRow arg="multicast-byte-cap" typ="num" syscap="!prestera-ac3">組播位元組容量。</ArgTableRow>
<ArgTableRow arg="multicast-byte-use" typ="num" syscap="prestera-bc2">組播位元組使用量。</ArgTableRow>
<ArgTableRow arg="mirror-ingress-packet-cap" typ="num" syscap="!prestera-cpss">入向映象封包容量。入向映象流量可使用的硬體封包描述符的最大數量。取決於 `mirror-buffers` 設定。</ArgTableRow>
<ArgTableRow arg="mirror-ingress-packet-use" typ="num" syscap="!prestera-cpss">入向映象封包使用量。</ArgTableRow>
<ArgTableRow arg="mirror-ingress-byte-cap" typ="num" syscap="prestera-bc2">入向映象位元組容量。取決於 `mirror-buffers` 設定。</ArgTableRow>
<ArgTableRow arg="mirror-ingress-byte-use" typ="num" syscap="prestera-bc2">入向映象位元組使用量。</ArgTableRow>
<ArgTableRow arg="mirror-egress-packet-cap" typ="num" syscap="!prestera-cpss">出向映象封包容量。出向映象流量可使用的硬體封包描述符的最大數量。取決於 `mirror-buffers` 設定。</ArgTableRow>
<ArgTableRow arg="mirror-egress-packet-use" typ="num" syscap="!prestera-cpss">出向映象封包使用量。</ArgTableRow>
<ArgTableRow arg="mirror-egress-byte-cap" typ="num" syscap="prestera-bc2">出向映象位元組容量。取決於 `mirror-buffers` 設定。</ArgTableRow>
<ArgTableRow arg="mirror-egress-byte-use" typ="num" syscap="prestera-bc2">出向映象位元組使用量。</ArgTableRow>
<ArgTableRow arg="shared-packet-cap" typ="num" syscap="prestera-ac3">共享封包容量。可在埠和 tx 佇列之間共享的硬體封包描述符的最大數量。取決於 `shared-buffers` 設定。</ArgTableRow>
<ArgTableRow arg="shared-packet-use" typ="num" syscap="prestera-ac3">共享封包使用量。所有 tx 隊列當前使用的共享封包描述符數量。</ArgTableRow>
<ArgTableRow arg="shared-byte-cap" typ="num" syscap="prestera-ac3">共享 tx 記憶體容量。取決於 `shared-buffers` 設定。</ArgTableRow>
<ArgTableRow arg="shared-byte-use" typ="num" syscap="prestera-ac3">共享 tx 記憶體使用量。所有 tx 佇列中的封包當前佔用的共享緩衝區數量。</ArgTableRow>
<ArgTableRow arg="lossy-pool-packet-cap" typ="num" syscap="prestera-bc2">有損池的共享封包容量。</ArgTableRow>
<ArgTableRow arg="lossy-pool-packet-use" typ="num" syscap="prestera-bc2">有損池的共享封包使用量。</ArgTableRow>
<ArgTableRow arg="lossless-pool-packet-cap" typ="num" syscap="!prestera-ac3">無損池的共享封包容量。</ArgTableRow>
<ArgTableRow arg="lossless-pool-packet-use" typ="num" syscap="!prestera-ac3">無損池的共享封包使用量。</ArgTableRow>
<ArgTableRow arg="lossy-pool-byte-cap" typ="num" syscap="!prestera-ac3">有損池位元組容量。</ArgTableRow>
<ArgTableRow arg="lossy-pool-byte-use" typ="num" syscap="!prestera-ac3">有損池位元組使用量。</ArgTableRow>
<ArgTableRow arg="lossless-pool-byte-cap" typ="num" syscap="!prestera-ac3">無損池位元組容量。</ArgTableRow>
<ArgTableRow arg="lossless-pool-byte-use" typ="num" syscap="!prestera-ac3">無損池位元組使用量。</ArgTableRow>
<ArgTableRow arg="wred-packet-cap" typ="num" syscap="prestera-bc2">佇列可超出共享上限使用的、用於觸發隨機尾丟棄的最大封包數量（`queueX-shared-packet-cap` 在 `/in/eth/sw/qos/port/print` 用法中）。例如，如果 `queue1-shared-packet-cap=3072` 且 `wred-packet-cap=512`，則當 `queue1-packet-use` 超過 3072 時 WRED 會觸發，並在 3072+512=3584 個數據包時達到 100% 丟棄率。</ArgTableRow>
<ArgTableRow arg="wred-byte-cap" typ="num" syscap="prestera-bc2">佇列可在共享上限之上使用以觸發隨機尾部丟棄的最大位元組數（`queueX-shared-byte-cap`）。例如，如果 `queue1-shared-byte-cap=768KiB` 且 `wred-byte-cap=128KiB`，則當 `queue1-packet-use` 超過 768KiB 時觸發 WRED，並在 768+128=896KiB 時達到 100% 丟棄率。</ArgTableRow>
</ArgTable>
