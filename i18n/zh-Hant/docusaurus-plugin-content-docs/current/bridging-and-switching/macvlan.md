---
sidebar_key: "bridging-and-switching/macvlan"
sidebar_position: 5
title: "MACVLAN"
sidebar_label: "MACVLAN"
description: "MACVLAN 允許在物理介面上建立多個具有唯一 MAC 地址的虛擬網路介面，從而實現高效的 IP 地址管理和獨立的 PPPoE 連線。它工作在 MAC 層，不使用 VLAN 標記，但存在一些限制，例如封包接收受限，並且在橋接場景中需要謹慎配置。"
tags:
  - 'macvlan'
  - 'arp'
source: https://manual.mikrotik.com/docs/bridging-and-switching/macvlan
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MACVLAN 提供了一種手段，可以在一個物理網路介面上建立多個虛擬網路介面，每個虛擬介面都擁有自己唯一的媒體訪問控制（MAC）地址。該技術用於滿足特定的網路需求，例如從單個物理乙太網介面獲取多個 IP 地址，或在使用不同 MAC 地址的情況下建立各自獨立的 PPPoE 用戶端連線。與依賴帶有 VLAN 標識的乙太網幀的傳統 [VLAN](./vlan.md)（虛擬區域網路）介面不同，MACVLAN 在 MAC 地址層面工作，使其成為針對特定網路場景的一種靈活而高效的解決方案。

:::info
MACVLAN 介面只能接收廣播封包、發往其自身 MAC 地址的封包以及有限數量的組播地址。如果物理介面上配置了 VLAN，則 MACVLAN 介面無法接收來自該 VLAN 的封包。

對於橋接以及涉及 VLAN 的更復雜的二層解決方案，應改用專用的交換器。
:::

## 基本配置示例 {#basic-configuration-example}

設想這樣一種場景：ether1 介面連線到您的 ISP，而您的路由器需要租用兩個 IP 地址，每個地址都使用不同的 MAC 地址。傳統上，這需要使用兩個物理乙太網介面和一臺額外的交換器。然而，更高效的解決方案是建立一個虛擬的 MACVLAN 介面。

要建立 MACVLAN 介面，請選擇所需的乙太網介面。如果未手動指定，將自動分配一個 MAC 地址：

```ros
/interface/macvlan
add interface=ether1 name=macvlan1

/interface/macvlan/print
Flags: R - RUNNING
Columns: NAME, MTU, INTERFACE, MAC-ADDRESS, MODE
#   NAME       MTU  INTERFACE  MAC-ADDRESS        MODE  
0 R macvlan1  1500  ether1     76:81:BF:68:69:83  bridge
```

現在，可以在 ether1 和 macvlan1 介面上建立 DHCP 用戶端：

```ros
/ip/dhcp-client
add interface=ether1
add interface=macvlan1
```

## 屬性參考 {#property-reference}

**子選單：** `/interface/macvlan`

MACVLAN 介面的配置設定。

| 屬性 | 描述 |
| :-- | :-- |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*; 預設：**enabled**) | Address Resolution Protocol 設定<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 介面將不使用 ARP</li><li><span className="ros-icon-success"><code>enabled</code></span> - 介面將使用 ARP</li><li><span className="ros-icon-success"><code>local-proxy-arp</code></span> - 路由器在介面上執行 proxy ARP，並將回覆傳送到同一介面</li><li><span className="ros-icon-success"><code>proxy-arp</code></span> - 路由器在介面上執行 proxy ARP，並將回覆傳送到其他介面</li><li><span className="ros-icon-success"><code>reply-only</code></span> - 介面將僅回覆來自匹配 IP 地址/MAC 地址組合的請求，這些組合作為靜態條目輸入到 IP/ARP 表中。不會自動將動態條目儲存到 IP/ARP 表中。因此，為使通訊成功，必須已存在有效的靜態條目。</li></ul> |
| **arp-timeout** (*auto \| integer*; 預設：**auto**) | 設定當未從 IP 收到封包後，ARP 記錄在 ARP 表中保留多長時間。值 `auto` 等於 `/ip/settings/` 中 `arp-timeout` 的值，預設值為 30s。 |
| **arp-accept** (*yes \| no*; 預設值: **no**) | 定義對於來自尚未存在於 ARP 表中的裝置所傳送的免費 ARP（GARP）幀的接受行為：<ul><li><span className="ros-icon-success"><code>no</code></span> - 不在 ARP 表中建立新條目</li><li><span className="ros-icon-success"><code>yes</code></span> - 在 ARP 表中建立新條目</li></ul> 該設定自 RouterOS 7.25.1 版本起可用。 |
| **comment** (*string*; 預設值: ) | 介面的簡短描述。 |
| **disabled** (*yes \| no*; 預設值: **no**) | 更改介面是否被停用。 |
| **interface** (*name*; 預設：) | MACVLAN 將在其上執行的底層介面的名稱。MACVLAN 介面可在任何具有 MAC 地址的介面上建立。 <br/><br/><strong>警告：</strong><ul><li>不支援在 MACVLAN 介面之上新增 VLAN 介面。</li><li>不支援在已橋接或已繫結的介面上新增 MACVLAN。</li></ul> |
| **loop-protect** (*on \| off \| default*; 預設：**default**) | 啟用或停用介面上的環路保護，**default** 的作用等同於關閉。 |
| **loop-protect-disable-time** (*時間間隔 \| 0*; 預設：**5m**) | 設定檢測到環路時所選介面被停用的時長。**0** - 永久。 |
| **loop-protect-send-interval** (*時間間隔*; 預設：**5s**) | 設定所選介面上傳送 loop protect 封包的頻率。 |
| **mac-address** (*MAC*; 預設值: ) | 介面的靜態 MAC 地址。未指定時將分配一個隨機生成的 MAC 地址。 |
| **mode** (*private \| bridge*; 預設：**bridge**) | 設定 MACVLAN 介面模式： <br/><ul><li><span className="ros-icon-success"><code>private</code></span> - 不允許同一父 **interface** 上的 MACVLAN 例項之間通訊。</li><li><span className="ros-icon-success"><code>bridge</code></span> - 允許同一父 **interface** 上的 MACVLAN 例項之間通訊。</li></ul> |
| **mtu** (*integer*; 預設：**1500**) | 設定第 3 層最大傳輸單元。對於 MACVLAN 介面，其值不能高於父 **interface**。 |
| **name** (*string*; 預設：) | 介面名稱。 |
