---
sidebar_key: "cli-reference/routing/igmp-proxy/interface"
sidebar_position: 1
title: "interface"
sidebar_label: "interface"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/igmp-proxy/interface
captured_at: '2026-11-01T21:29:32+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/igmp-proxy/interface {#routingigmp-proxyinterface}
**型別：** 目錄

配置哪些介面將作為路由器上的 IGMP 代理介面參與工作。如果某個介面未配置為 IGMP 代理介面，則從該介面收到的所有 IGMP 流量都會被忽略。

可以使用 `print status` 命令獲取每個介面的詳細狀態資訊。

```ros
[admin@MikroTik] /routing/igmp-proxy/interface/print status 
Flags: X - disabled, I - inactive, D - dynamic; U - upstream 
 0  U interface=ether2 threshold=1 alternative-subnets="" upstream=yes source-ip-address=192.168.10.10 rx-bytes=3018487500 rx-packets=2012325 tx-bytes=0 tx-packets=0 

 1    interface=ether3 threshold=1 alternative-subnets="" upstream=no querier=yes source-ip-address=192.168.20.10 rx-bytes=0 rx-packets=0 tx-bytes=2973486000 tx-packets=1982324 

 2    interface=ether4 threshold=1 alternative-subnets="" upstream=no querier=yes source-ip-address=192.168.30.10 rx-bytes=0 rx-packets=0 tx-bytes=152019000 tx-packets=101346 
```

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="U" typ="upstream">上游</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum { all:0 }">介面的名稱。</ArgTableRow>
<ArgTableRow arg="threshold" typ="num">最小 TTL。收到的 TTL 值低於該值的報文將被忽略。</ArgTableRow>
<ArgTableRow arg="alternative-subnets" typ="multi { numbers: super { as: ipAddr
, [netmask] /num
 }
 }">預設情況下，只接受來自直連子網的報文。此引數可用於指定一份備用的有效報文源子網列表，對封包文和 IGMP 報文均適用。僅對上游介面生效。當組播資料的源經常位於不同的 IP 網路時應使用此引數。</ArgTableRow>
<ArgTableRow arg="upstream" typ="bool">如果介面位於組播樹的根方向，則該介面被稱為 "upstream"（上游）介面。IGMP 轉發路由器必須配置且僅配置一個上游介面。上游介面用於傳送 IGMP 成員關係請求。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="querier" typ="bool">該介面是否充當 IGMP 查詢器。</ArgTableRow>
<ArgTableRow arg="source-ip-address" typ="ipAddr">檢測到的該介面源 IP。</ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num">該介面上接收的組播流量總量。</ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num">該介面上接收的組播報文總數。</ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num">該介面上傳送的組播流量總量。</ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num">該介面上傳送的組播報文總數。</ArgTableRow>
</ArgTable>
