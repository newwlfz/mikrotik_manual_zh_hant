---
sidebar_key: "firewall-and-quality-of-service/user-guides/port-knocking"
sidebar_position: 5
title: "埠敲門"
sidebar_label: "埠敲門"
description: "埠敲門是一種安全方法，它要求先按特定順序進行埠連線，然後才授予訪問許可權，以此來保護公網 IP 地址。該文件提供了配置示例，包括用於將 IP 新增到信任列表以及封堵可疑埠的防火牆規則配置，並附有關於資源佔用的警告。"
tags:
  - 'firewall'
  - 'port-knocking'
  - 'security'
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/user-guides/port-knocking
captured_at: '2026-11-04T11:28:24+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

所有可用的公網 IP 地址都在不斷被機器人程式以及 shodan.io 之類的服務進行埠掃描，任何人都可以利用這些資訊來實施暴力破解攻擊並執行任何已知漏洞利用。埠敲門是一種經濟高效的防禦方式：它不暴露任何埠，只監聽連線嘗試——如果按正確順序發起埠連線嘗試，用戶端就會被視為安全，並被加入一個可繞過 WAN 防火牆規則的安全地址列表。

### 配置示例 {#setup-example}

我們假設你已經設定好一個會丟棄來自 WAN 埠的所有連線嘗試的防火牆，因此你需要在此之前新增額外規則。
首先，建立一個防火牆規則，監聽指定埠，並將連線來源 IP 新增到地址列表——這就是第一次敲門。

```ros
/ip/firewall/filter/add action=add-src-to-address-list address-list=888 address-list-timeout=30s chain=input dst-port=888 in-interface-list=WAN protocol=tcp
```

然後新增一個在另一個埠上執行相同操作的規則，但只允許已經位於第一個列表中的 IP。你可以按需重複此步驟任意多次。

```ros
/ip/firewall/filter/add action=add-src-to-address-list address-list=555 address-list-timeout=30s chain=input dst-port=555 in-interface-list=WAN protocol=tcp src-address-list=888
```

最後，最後一次敲門會把來源加入一個受信任的 IP 列表，並且任何輸入流量都會被接受。

```ros
/ip/firewall/filter/add action=add-src-to-address-list address-list=secured address-list-timeout=30m chain=input dst-port=222 in-interface-list=WAN protocol=tcp src-address-list=555
/ip/firewall/filter/add action=accept chain=input in-interface-list=WAN src-address-list=secured
```

### 透過敲門獲得訪問許可權 {#knock-to-gain-access}

要從 WAN 訪問裝置，可以使用埠敲門用戶端，但一個使用 nmap 的簡單 bash 單行命令也能完成這項工作。

```bash
for x in 888 555 222; do nmap -p $x -Pn xx.xx.xx.xx; done
```

### 黑名單 {#blacklists}

除非你使用大量敲門，否則簡單埠掃描可能意外地按正確順序觸發正確埠，因此建議同時新增黑名單。

在防火牆規則棧的最頂部，為黑名單新增一條丟棄規則。

```ros
/ip/firewall/filter/add action=drop chain=input disabled=yes in-interface-list=WAN src-address-list=blacklist
```

然後將可疑 IP 新增到黑名單。

不良埠——受信任使用者永遠不會使用，因此具有較長的超時懲罰。

```ros
/ip/firewall/filter/add action=add-src-to-address-list address-list=blacklist address-list-timeout=1000m chain=input disabled=yes dst-port=666 in-interface-list=WAN protocol=tcp
```

會顯著拖慢埠掃描過程、使其變得毫無意義，但絕不會讓真實使用者被鎖定太久的埠。這可以包括除“敲門”埠之外的每一個埠。關鍵在於源 IP 尚未位於安全列表中，因此這些埠可以在成功敲門後使用。

```ros
/ip/firewall/filter/add action=add-src-to-address-list address-list=blacklist address-list-timeout=1m chain=input disabled=yes dst-port=21,22,23,8291,10000-60000 in-interface-list=WAN protocol=tcp src-address-list=!secured
```

:::warning
本節中的黑名單規則會以 **disabled=yes** 新增，以避免把使用者鎖在外面。待備用訪問方式可用後，再啟用這些過濾規則，或使用 `<Safe Mode>`
:::

### 為每次敲門使用口令 {#use-a-passphrase-for-each-knock}

你還可以更進一步，在每次敲門時傳送口令。

:::info
警告

Layer7 規則非常消耗資源。除非你清楚自己在做什麼，否則不要使用它們。
:::

<details>
<summary>點選開啟程式碼塊</summary>

然後建立一個 layer7 正則檢查，可在敲門規則中請求它。

`/ip/firewall/layer7-protocol/add` name=pass regexp="^passphrase/$"
`/ip/firewall/filter`
add action=add-src-to-address-list address-list=888 address-list-timeout=30s chain=input dst-port=888 in-interface-list=WAN protocol=udp layer7-protocol=pass

</details>

:::warning
如需額外的安全層，請參閱暴力破解防護文章：[暴力破解防護](./bruteforce-prevention.md)
:::
