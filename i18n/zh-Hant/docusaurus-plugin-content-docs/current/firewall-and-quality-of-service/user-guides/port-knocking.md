---
sidebar_key: "firewall-and-quality-of-service/user-guides/port-knocking"
sidebar_position: 5
title: "埠敲門"
sidebar_label: "埠敲門"
description: "埠敲門使 RouterOS 路由器的管理埠保持關閉，直到用戶端連線到一組秘密埠序列；隨後防火牆會將用戶端新增到受信任地址列表。內容涵蓋預設防火牆中的敲門規則、從用戶端進行敲門、針對埠掃描的黑名單、使用第 7 層的口令敲門，以及檢查這些列表。"
tags:
  - 'firewall'
  - 'port-knocking'
  - 'security'
source: https://manual.mikrotik.com/docs/firewall-and-quality-of-service/user-guides/port-knocking
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

每個公網 IP 地址都在被持續掃描，掃描者包括機器人和 Shodan 之類的服務；任何人都可以利用掃描結果，對開放埠嘗試暴力破解或已知漏洞利用。埠敲門則讓這些埠保持關閉：路由器只監視對一串秘密埠的連線嘗試。按正確順序敲擊正確埠的用戶端會被加入 `secured` 地址列表，防火牆會接受其連線。

典型用途是管理遠端站點上的路由器，而你的管理地址會變化，此時固定的允許源地址列表無法使用。

埠敲門是額外的一層防護，不能替代真正的身份驗證。敲門包是明文封包，任何能觀察到你和路由器之間流量的人都可以重放它們。在條件允許時，應透過 [WireGuard](../../virtual-private-networks/wireguard.md) 之類的 VPN 訪問管理服務；其他措施請參閱[保護你的路由器](../../getting-started/securing-your-router.md)。

## 透過敲門序列開放訪問 {#open-access-with-a-knock-sequence}

示例假設使用預設配置：面向網際網路的介面位於 `WAN` 介面列表中，且 input 鏈以規則 `defconf: drop all not coming from LAN` 結束。敲門規則必須位於該規則之前，否則來自 WAN 側的敲門包永遠無法到達這些規則；`place-before` 會把每條規則放到該位置：

```ros
/ip/firewall/filter
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=888 in-interface-list=WAN \
    address-list=888 address-list-timeout=30s \
    comment="Port knocking: first knock" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=555 in-interface-list=WAN \
    src-address-list=888 address-list=555 address-list-timeout=30s \
    comment="Port knocking: second knock" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=222 in-interface-list=WAN \
    src-address-list=555 address-list=secured address-list-timeout=30m \
    comment="Port knocking: last knock" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=accept \
    in-interface-list=WAN src-address-list=secured \
    comment="Port knocking: accept knocked clients" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

規則的工作方式：

- 第一次敲門是對 TCP 埠 888 的連線嘗試，它會把源地址加入 `888` 列表，保留 30 秒。
- 第二次敲門針對埠 555，只有來自 `888` 列表中地址的敲門才會計數，並會把該地址加入 `555` 列表。你可以用同樣的方式串聯任意多次敲門：每條規則都要求地址位於上一次敲門對應的列表中。
- 最後一次敲門針對埠 222，會把地址移入 `secured` 列表，保留 30 分鐘。
- `accept` 規則會接受來自 `secured` 列表中地址的所有輸入。若只想開放管理埠，可向其新增 `protocol=tcp dst-port=22,8291`。
- 順序錯誤的敲門不會授予訪問許可權：只有當地址已在上一跳敲門對應的列表中時，一次敲門才會計數。
- 當地址位於 `secured` 列表時建立的會話，在條目過期後仍會保持開啟，因為預設配置會在鏈中更早的位置接受已建立的連線。新連線需要新的敲門序列。

## 從用戶端敲門 {#knock-from-a-client}

專用的埠敲門用戶端可用，但用 `nmap` 寫一個 shell 單行命令就能完成。每次執行 `nmap` 都會向一個埠傳送連線嘗試；整個序列只需幾秒鐘：

```bash
for x in 888 555 222; do nmap -p $x -Pn 203.0.113.1; done
```

請將 `203.0.113.1` 替換為路由器的公網地址。根據防火牆配置，這些埠在 `nmap` 輸出中會顯示為 closed 或 filtered；這是預期結果，因為沒有任何服務在監聽它們。完成最後一次敲門後，在 30 分鐘內照常連線路由器。

## 新增黑名單 {#add-a-blacklist}

如果埠掃描恰好按正確順序命中敲門埠，就會開放路由器；而只有少量敲門埠時，這種情況並非不可能。黑名單可以在掃描器走到那一步之前阻止它們。以下規則以停用狀態新增，以免你在新增規則時把自己鎖在外面：

```ros
/ip/firewall/filter
add chain=input action=drop \
    in-interface-list=WAN src-address-list=blacklist \
    comment="Port knocking: drop blacklisted" disabled=yes \
    place-before=([find chain=input]->0)
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=666 in-interface-list=WAN \
    address-list=blacklist address-list-timeout=1000m \
    comment="Port knocking: bad port" disabled=yes \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=21,22,23,8291,10000-60000 \
    in-interface-list=WAN src-address-list=!secured \
    address-list=blacklist address-list-timeout=1m \
    comment="Port knocking: slow down scans" disabled=yes \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

- drop 規則會放在 input 鏈的第一條規則之前（`place-before=([find chain=input]->0)`），因此被列入黑名單的地址完全無法敲門或連線。在貼上的命令中，請用 `find` 引用規則：像 `place-before=0` 這樣的純數字只有在同一會話中先執行 `print` 後才有效，否則會失敗並提示 `item referred by 'place-before' does not exist`。
- 壞埠是可信使用者永遠不會使用的埠。任何對它發起的連線嘗試都會把源地址加入黑名單 1000 分鐘。
- 第二條規則會拖慢埠掃描，直到其失去意義，同時不會讓真實使用者被鎖定太久：對所列埠之一的連線嘗試會把源地址加入黑名單一分鐘。該列表可以包含除敲門埠外的所有埠。它會跳過 `secured` 列表中的地址，因此成功敲門後你可以使用這些埠。

:::warning
你可能會把自己封禁。規則啟用後，在敲門之前連線 SSH 或 WinBox 會把你自己地址加入黑名單一分鐘，在此期間你的敲門包會被丟棄。被阻止的用戶端會在一段時間內不斷重試連線，而每次重試都可能續期該條目：被阻止的嘗試之後，請等待一分鐘再重新敲門。只有在你有其他方式訪問路由器時，或處於 [Safe Mode](../../getting-started/configuration-management/index.md#safe-mode) 時，才啟用這些規則。
:::

準備好後，啟用規則：

```ros
/ip/firewall/filter/enable [find comment~"^Port knocking"]
```

## 為每次敲門使用口令 {#use-a-passphrase-for-each-knock}

你可以更進一步，要求敲門時攜帶口令。第 7 層協定條目會匹配封包載荷中的口令，而一條 UDP 敲門規則會要求它。用該 UDP 規則替代第一次 TCP 敲門：

```ros
/ip/firewall/layer7-protocol/add name=pass regexp="^passphrase\$"
/ip/firewall/filter/add chain=input action=add-src-to-address-list \
    protocol=udp dst-port=888 in-interface-list=WAN \
    layer7-protocol=pass address-list=888 address-list-timeout=30s \
    comment="Port knocking: first knock with passphrase" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
/ip/firewall/filter/remove [find comment="Port knocking: first knock"]
```

正則表示式中的 `$` 必須轉義為 `\$`，否則 RouterOS 會把它讀作變數名的開頭；儲存後的表示式為 `^passphrase$`。該表示式只匹配完全一致的載荷：錯誤的口令或末尾換行都不算。用 `printf` 或 `echo -n` 傳送不帶換行的口令，然後敲擊其他埠：

```bash
printf 'passphrase' | nc -u -w1 203.0.113.1 888
for x in 555 222; do nmap -p $x -Pn 203.0.113.1; done
```

:::warning
第 7 層規則非常消耗資源。除非你清楚自己在做什麼，否則不要使用它們。
:::

## 檢查列表 {#check-the-lists}

檢視哪些地址正處於敲門序列中途、哪些已受信任、哪些被阻止，以及每個條目的剩餘時間：

```ros
/ip/firewall/address-list/print \
    where list~"^(888|555|secured|blacklist)\$"
```

要解除對某個地址的封鎖，請將其從黑名單中移除：

```ros
/ip/firewall/address-list/remove \
    [find list=blacklist address=203.0.113.10]
```

## IPv6 {#ipv6}

這些規則適用於 IPv4。當路由器可透過 IPv6 訪問時，請以相同方式把 TCP 敲門規則新增到 `/ipv6/firewall/filter`，放在丟棄來自 LAN 外部的 IPv6 輸入的規則之前。

## 相關主題 {#related-topics}

- [SSH 暴力破解防護](./bruteforce-prevention.md) 會限制來自同一地址的重複 SSH 連線，並使用相同的 `secured` 列表豁免正確完成敲門的用戶端。
- [DDoS 防護](./ddos-protection.md) 會檢測發往路由器後方主機的大量新連線洪泛。

有關所有規則屬性，請參閱 CLI 參考中的 [`/ip/firewall/filter`](../../cli-reference/ip/firewall/filter/index.md)、[`/ip/firewall/address-list`](../../cli-reference/ip/firewall/address-list.md) 和 [`/ip/firewall/layer7-protocol`](../../cli-reference/ip/firewall/layer7-protocol.md)。
