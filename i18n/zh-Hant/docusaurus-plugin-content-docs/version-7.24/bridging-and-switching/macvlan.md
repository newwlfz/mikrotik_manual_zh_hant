---
title: "MACVLAN"
description: "MACVLAN 可在實體介面上建立多個具有唯一 MAC 位址的虛擬網路介面，讓 IP 位址管理更有效率，並可建立不同的 PPPoE 連線。它在 MAC 層級運作，不使用 VLAN 標記，但有封包接收受限等限制，且在橋接情境中需要審慎設定。"
tags:
  - 'macvlan'
  - 'arp'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/macvlan
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

MACVLAN 提供一種方式，可在實體網路介面上建立多個虛擬網路介面，每個介面都有自己唯一的 Media Access Control（MAC）位址。這項技術用於滿足特定網路需求，例如從單一實體 Ethernet 介面取得多個 IP 位址，或使用不同 MAC 位址建立不同的 PPPoE 用戶端連線。傳統 [VLAN](/docs/bridging-and-switching/vlan)（Virtual LAN）介面依賴帶有 VLAN 識別碼標籤的 Ethernet 訊框，而 MACVLAN 則是在 MAC 位址層級運作，因此成為特定網路情境中彈性且有效率的解決方案。

:::info
MACVLAN 介面只能接收廣播封包、目的地位址為自身 MAC 位址的封包，以及有限數量的多播位址。如果實體介面已設定 VLAN，則 MACVLAN 介面無法接收來自該 VLAN 的封包。

若需要橋接或更複雜且涉及 VLAN 的 Layer2 解決方案，應改用專用交換器。
:::

## 基本設定範例 {#basic-configuration-example}

假設 ether1 介面連線到你的 ISP，而路由器需要租用兩個 IP 位址，且每個 IP 位址使用不同的 MAC 位址。傳統上，這需要使用兩個實體 Ethernet 介面與一個額外的交換器。不過，更有效率的作法是建立虛擬 MACVLAN 介面。

若要建立 MACVLAN 介面，請選取所需的 Ethernet 介面。若未手動指定 MAC 位址，系統會自動指派：

```ros
/interface/macvlan
add interface=ether1 name=macvlan1

/interface/macvlan/print
Flags: R - RUNNING
Columns: NAME, MTU, INTERFACE, MAC-ADDRESS, MODE
#   NAME       MTU  INTERFACE  MAC-ADDRESS        MODE  
0 R macvlan1  1500  ether1     76:81:BF:68:69:83  bridge
```

現在，可以在 ether1 與 macvlan1 介面上建立 DHCP 用戶端：

```ros
/ip/dhcp-client
add interface=ether1
add interface=macvlan1
```

## 屬性參考 {#property-reference}

**子選單：** `/interface/macvlan`

MACVLAN 介面的設定。

| 屬性 | 說明 |
| :-- | :-- |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*；預設：**enabled**) | Address Resolution Protocol 設定<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 介面不會使用 ARP</li><li><span className="ros-icon-success"><code>enabled</code></span> - 介面會使用 ARP</li><li><span className="ros-icon-success"><code>local-proxy-arp</code></span> - 路由器會在此介面上執行 proxy ARP，並將回覆傳送至同一介面</li><li><span className="ros-icon-success"><code>proxy-arp</code></span> - 路由器會在此介面上執行 proxy ARP，並將回覆傳送至其他介面</li><li><span className="ros-icon-success"><code>reply-only</code></span> - 介面只會回覆來自符合 IP 位址／MAC 位址組合的要求，這些組合會以靜態項目輸入至 IP/ARP 表。IP/ARP 表不會自動儲存動態項目。因此，若要成功通訊，必須已存在有效的靜態項目。</li></ul> |
| **arp-timeout** (*auto \| integer*；預設：**auto**) | 設定在沒有從 IP 收到任何封包後，ARP 記錄保留在 ARP 表中的時間。值 `auto` 等於 `/ip/settings/` 中的 `arp-timeout` 值，預設為 30s。 |
| **comment** (*string*；預設： ) | 介面的簡短說明。 |
| **disabled** (*yes \| no*；預設：**no**) | 變更介面是否停用。 |
| **interface** (*name*；預設： ) | MACVLAN 將運作所在的底層介面名稱。MACVLAN 介面可以在任何具有 MAC 位址的介面上建立。<br/><br/><strong>警告：</strong><ul><li>不支援在 MACVLAN 介面上新增 VLAN 介面。</li><li>不支援在已橋接或已 bonded 的介面上新增 MACVLAN。</li></ul> |
| **loop-protect** (*on \| off \| default*；預設：**default**) | 啟用或停用介面上的 loop protect，**default** 等同於關閉。 |
| **loop-protect-disable-time** (*time interval \| 0*；預設：**5m**) | 設定偵測到迴路時，所選介面停用的時間。**0** 表示永遠停用。 |
| **loop-protect-send-interval** (*time interval*；預設：**5s**) | 設定在所選介面上傳送 loop protect 封包的頻率。 |
| **mac-address** (*MAC*；預設： ) | 介面的靜態 MAC 位址。若未指定，將指派隨機產生的 MAC 位址。 |
| **mode** (*private \| bridge*；預設：**bridge**) | 設定 MACVLAN 介面模式：<br/><ul><li><span className="ros-icon-success"><code>private</code></span> - 不允許同一父層 <strong>interface</strong> 上的 MACVLAN 執行個體之間通訊。</li><li><span className="ros-icon-success"><code>bridge</code></span> - 允許同一父層 <strong>interface</strong> 上的 MACVLAN 執行個體之間通訊。</li></ul> |
| **mtu** (*integer*；預設：**1500**) | 設定第 3 層最大傳輸單位。對 MACVLAN 介面而言，其值不得高於父層 **interface**。 |
| **name** (*string*；預設： ) | 介面名稱。 |
