---
sidebar_key: "cli-reference/zerotier/peer/index"
sidebar_position: 2
title: "peer"
sidebar_label: 'peer'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/zerotier/peer
captured_at: '2026-11-01T21:26:14+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## zerotier/peer {#zerotierpeer}
**軟體包：** zerotier
**型別：** 目錄

ZeroTier 的對等節點是一個資訊性部分，列出你的節點已知的節點。除非節點加入同一網路並獲得授權，否則它們無法相互通訊。

```ros
[admin@Home] > `/zerotier/peer/print` 
Columns: INSTANCE, ZT-ADDRESS, LATENCY, ROLE, PATH
# INSTANCE  ZT-ADDRESS  LATENCY  ROLE    PATH
0 zt1       61d294b9cb  186ms    PLANET  active,preferred,50.7.73.34/9993,recvd:4s526ms                  
1 zt1       62f865ae71  270ms    PLANET  active,preferred,50.7.252.138/9993,recvd:4s440ms,sent:9s766ms   
2 zt1       778cde7190  132ms    PLANET  active,preferred,103.195.103.66/9993,recvd:4s579ms,sent:9s766ms 
3 zt1       992fcf1db7  34ms     PLANET  active,preferred,195.181.173.159/9993,recvd:4s675ms,sent:4s712ms
4 zt1       159924d630  130ms    LEAF    active,preferred,34.121.192.xx/21002,recvd:3s990ms,sent:3s990ms
```

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="B" typ="bonded">對等節點是否已繫結。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum">ZeroTier 例項名稱。</ArgTableRow>
<ArgTableRow arg="zt-address" typ="string">對等節點的 ZeroTier 地址。</ArgTableRow>
<ArgTableRow arg="bonded" typ="bool">對等節點是否已繫結。</ArgTableRow>
<ArgTableRow arg="latency" typ="time">到對等節點的延遲。</ArgTableRow>
<ArgTableRow arg="role" typ="string">對等節點的角色（PLANET、MOON 或 LEAF）。</ArgTableRow>
<ArgTableRow arg="path" typ="multi { array-id, path: string
 }">到對等節點的活動路徑。</ArgTableRow>
</ArgTable>
