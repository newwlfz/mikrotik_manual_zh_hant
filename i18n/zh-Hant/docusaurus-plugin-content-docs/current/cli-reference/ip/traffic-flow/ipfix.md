---
sidebar_key: "cli-reference/ip/traffic-flow/ipfix"
sidebar_position: 1
title: "ipfix"
sidebar_label: 'ipfix'
source: https://manual.mikrotik.com/docs/cli-reference/ip/traffic-flow/ipfix
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/traffic-flow/ipfix {#iptraffic-flowipfix}
**型別：** 設定目錄
選擇 IPFIX 流記錄中包含的欄位。設定為 `yes` 的行會按流匯出該欄位。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="nat-events" typ="bool">包含該流的 NAT 位掩碼（事件標誌）</ArgTableRow>
<ArgTableRow arg="first-forwarded" typ="bool">包含該流第一個轉發封包的時間戳</ArgTableRow>
<ArgTableRow arg="last-forwarded" typ="bool">包含該流最後一個轉發封包的時間戳</ArgTableRow>
<ArgTableRow arg="sys-init-time" typ="bool">包含該流的系統啟動時間參考值</ArgTableRow>
<ArgTableRow arg="packets" typ="bool">包含該流的封包數量</ArgTableRow>
<ArgTableRow arg="bytes" typ="bool">包含該流的總位元組數</ArgTableRow>
<ArgTableRow arg="src-port" typ="bool">包含該流的源埠號</ArgTableRow>
<ArgTableRow arg="dst-port" typ="bool">包含該流的目標埠號</ArgTableRow>
<ArgTableRow arg="in-interface" typ="bool">包含接收該流的介面</ArgTableRow>
<ArgTableRow arg="out-interface" typ="bool">包含傳送該流所用的介面</ArgTableRow>
<ArgTableRow arg="protocol" typ="bool">包含 IP 協定號（TCP、UDP、ICMP 等）</ArgTableRow>
<ArgTableRow arg="tos" typ="bool">包含 IP 首部 TOS（服務型別）欄位</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="bool">包含該流的累計 TCP 標誌（SYN、ACK 等）</ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="bool">包含該流的目標 MAC 地址</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="bool">包含該流的源 MAC 地址</ArgTableRow>
<ArgTableRow arg="src-address" typ="bool">包含該流的源 IP 地址</ArgTableRow>
<ArgTableRow arg="dst-address" typ="bool">包含流的目的 IP 地址</ArgTableRow>
<ArgTableRow arg="src-address-mask" typ="bool">包含源網路掩碼長度（彙總）</ArgTableRow>
<ArgTableRow arg="dst-address-mask" typ="bool">包含目的網路掩碼長度</ArgTableRow>
<ArgTableRow arg="gateway" typ="bool">包含流被路由到的閘道器 IP 地址</ArgTableRow>
<ArgTableRow arg="ttl" typ="bool">包含封包的 TTL</ArgTableRow>
<ArgTableRow arg="ip-header-length" typ="bool">包含 IP 頭長度</ArgTableRow>
<ArgTableRow arg="is-multicast" typ="bool">標記組播流</ArgTableRow>
<ArgTableRow arg="ip-total-length" typ="bool">包含 IP 封包總長度（以位元組為單位）</ArgTableRow>
<ArgTableRow arg="nat-src-address" typ="bool">包含該流的 NAT 後源地址</ArgTableRow>
<ArgTableRow arg="nat-dst-address" typ="bool">包含該流的 NAT 後目的地址</ArgTableRow>
<ArgTableRow arg="nat-src-port" typ="bool">包含該流的 NAT 後源埠</ArgTableRow>
<ArgTableRow arg="nat-dst-port" typ="bool">包含該流的 NAT 後目的埠</ArgTableRow>
<ArgTableRow arg="nat-src-address6" typ="bool"></ArgTableRow>
<ArgTableRow arg="nat-dst-address6" typ="bool"></ArgTableRow>
<ArgTableRow arg="ipv6-flow-label" typ="bool">包含 IPv6 流標籤欄位</ArgTableRow>
<ArgTableRow arg="udp-length" typ="bool">包含 UDP 有效載荷長度</ArgTableRow>
<ArgTableRow arg="tcp-seq-num" typ="bool">包含 TCP 序列號</ArgTableRow>
<ArgTableRow arg="tcp-ack-num" typ="bool">包含 TCP 確認號</ArgTableRow>
<ArgTableRow arg="tcp-window-size" typ="bool">包含 TCP 視窗大小</ArgTableRow>
<ArgTableRow arg="igmp-type" typ="bool">包含 IGMP 訊息型別</ArgTableRow>
<ArgTableRow arg="icmp-type" typ="bool">包含 ICMP 型別</ArgTableRow>
<ArgTableRow arg="icmp-code" typ="bool">包含 ICMP 程式碼</ArgTableRow>
</ArgTable>
