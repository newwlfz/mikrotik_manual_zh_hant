---
sidebar_key: "cli-reference/interface/pppoe-server/server"
sidebar_position: 2
title: "server"
sidebar_label: 'server'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/pppoe-server/server
captured_at: '2026-11-01T21:22:57+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/pppoe-server/server {#interfacepppoe-serverserver}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">伺服器配置是否無效。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="service-name" typ="string">PPPoE 服務名稱。伺服器接受傳送的 PADI 訊息中 service-names 與此設定匹配的用戶端，或者 PADI 訊息中的 service-name 欄位未設定時也接受。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum { <l2tp>:0xfffffffe }" mandatory="1">用戶端連線到的介面。</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大傳輸單元。最佳值是在隧道所執行的介面 MTU 基礎上減去 20（因此，對於 1500 位元組的乙太網鏈路，將 MTU 設定為 1480 以避免封包分片）。</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">最大接收單元。最佳值是在隧道所執行的介面 MTU 基礎上減去 20（因此，對於 1500 位元組的乙太網鏈路，將 MTU 設定為 1480 以避免封包分片）。</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">鏈路上可接收的最大封包大小。如果封包大於隧道 MTU，則會被拆分為多個數據包，從而允許透過隧道傳送全尺寸 IP 或乙太網封包。</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">伺服器接受的身份驗證方法。</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">定義時間段（以秒為單位），超過該時間後，路由器開始每秒傳送 keepalive 封包。如果在 `keepalive-timeout` 的兩倍時間內沒有流量到達，也沒有 keepalive 響應到達，則斷開無響應的用戶端。設定為 `disabled` 可關閉 echo 封包。</ArgTableRow>
<ArgTableRow arg="one-session-per-host" typ="bool">每個主機僅允許一個會話（由 MAC 地址確定）。如果主機嘗試建立新會話，則關閉舊會話。</ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num">AC 可服務的最大用戶端數量。`0` 表示無限制。</ArgTableRow>
<ArgTableRow arg="pado-delay" typ="num">傳送 PADO 響應前的延遲（毫秒）。</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">指定建立隧道時使用哪個 PPP 配置檔案。</ArgTableRow>
<ArgTableRow arg="accept-empty-service" typ="bool">如果沒有匹配的 PPPoE 服務可用，則接受服務名稱為空的 PADI。</ArgTableRow>
<ArgTableRow arg="pppoe-over-vlan-range" typ="multi { vlan-range: range [1 .. 4094]
 }">
此設定允許 PPPoE 伺服器在 802.1Q VLAN 上執行。支援 VLAN ID 範圍以及使用逗號分隔值指定的單個 VLAN，例如：`100-115,120,122,128-130`。  

指定 VLAN ID 後，PPPoE 伺服器將接受來自用戶端的 802.1Q 標記封包，並使用同一 VLAN 進行回覆。然後，您可以選擇使用 `accept-untagged` 屬性在同一介面上接受或丟棄未標記的 PPPoE 用戶端。  
您甚至可以在 VLAN 介面上使用 `pppoe-over-vlan-range` 設定配置 PPPoE 伺服器，從而也啟用 QinQ 設定。但請記住，內層 VLAN 標記應為 802.1Q。
</ArgTableRow>
<ArgTableRow arg="accept-untagged" typ="bool">指定 `pppoe-over-vlan-range` 時，是否在介面上接受未標記（非 VLAN）的 PPPoE 封包。</ArgTableRow>
</ArgTable>
