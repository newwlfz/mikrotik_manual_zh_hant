---
title: "橋接 VLAN 表"
description: "本頁介紹 MikroTik RouterOS 的 Bridge VLAN Table 功能，說明如何使用 tagged/untagged 埠、PVID 與 ingress/egress 規則，在橋接器中設定 VLAN 過濾。其中包含 trunk 與 access 埠的設定範例，並強調透過管理存取控制與 EtherType 過濾來強化安全性。"
tags:
  - 'bridge-vlan-filtering'
  - 'vlan'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/bridge-vlan-table
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

---

你可以使用橋接器篩選網路中的 VLAN。若要達成此目的，請使用 [Bridge VLAN Filtering](/docs/bridging-and-switching#bridge-vlan-filtering) 功能。此功能應取代許多常見的 VLAN 設定錯誤，而這些錯誤很可能會造成連線效能或連線問題。你可以閱讀 [VLAN in a bridge with a physical interface](/docs/bridging-and-switching/user-guides/layer2-misconfiguration#vlan-in-a-bridge-with-a-physical-interface) 章節，瞭解其中一種最常見的設定錯誤。橋接器 VLAN 篩選功能最重要的部分是橋接器 VLAN 表，它會指定每個埠允許哪些 VLAN，但如果你嘗試進行更進階的設定，設定可能會變得相當複雜。對於一般設定，你應該可以使用 [Trunk and Access ports](/docs/bridging-and-switching#vlan-example-trunk-and-access-ports) 範例來設定設備，但本指南的目的是提供深入說明，並指出使用 bridge VLAN Filtering 時的一些行為特性。

## Background

---

在深入說明橋接器 VLAN 篩選之前，你應該先瞭解幾個與橋接器 VLAN 篩選相關的基本概念。

- **Tagged/Untagged** - 在 `/interface/bridge/vlan` 選單下，你可以指定一個包含 tagged 與 untagged 埠的項目。一般而言，tagged 埠應該是 trunk 埠，而 untagged 埠應該是 access 埠。指定 tagged 埠時，橋接器一律會為透過該埠傳送出去的封包設定 VLAN 標籤（egress）。指定 untagged 埠時，橋接器一律會移除 egress 封包上的 VLAN 標籤。

- **VLAN-ids** - 在 `/interface/bridge/vlan` 選單下，你可以指定一個項目，讓特定 VLAN 允許通過特定埠。系統會在 egress 埠檢查 VLAN ID。如果封包包含的 VLAN ID 不存在於該 egress 埠的橋接器 VLAN 表中，則封包會在送出前被丟棄。

- **PVID** - Port VLAN ID 用於 access 埠，以特定 VLAN ID 標記所有 ingress 流量。系統會為每個使用的 PVID 在橋接器 VLAN 表中新增一個動態項目，並自動將該埠新增為 untagged 埠。

- **Ingress filtering** - 預設情況下，不存在於橋接器 VLAN 表中的 VLAN 會在送出前被丟棄（egress），但此屬性可讓你在封包接收時（ingress）將其丟棄。

- **Management access** - 橋接器原本只是單純在橋接器埠之間轉送封包，對其他設備而言，看起來就像兩者之間只有一條線。透過橋接器 VLAN 篩選，你可以限制哪些封包可以存取已設定橋接器的設備。最常見的做法是只允許使用非常特定的 VLAN ID 存取設備，但也有其他方式可以授權存取設備。當透過橋接器埠存取設備時，Management access 是增加另一層安全性的好方法；這種存取方式有時稱為 management port。對於支援使用硬體卸載進行 VLAN 篩選的設備，這也與橋接器的 CPU 埠有關。

- **CPU port** - 每台具有交換器晶片的設備都有一個特殊用途的埠，稱為 CPU 埠，用於與設備的 CPU 通訊。對於支援使用硬體卸載進行 VLAN 篩選的設備，此埠就是橋接器介面本身。此埠主要用於建立 management access，但也可用于其他用途，例如在不同 VLAN 之間路由流量、標記封包，以及套用佇列。

- **frame-type** - 你可以根據封包是否具有 VLAN 標籤來篩選；這有助於為 bridge 埠增加額外的安全層。

- **EtherType** - 預設情況下，支援 VLAN 的 bridge 會透過檢查 C-TAG（0x8100）來篩選 VLAN；所有其他 VLAN 標籤類型都會被視為未標記封包（沒有 VLAN 標籤）。所選的 EtherType 將用於 VLAN 篩選以及 VLAN 標記／取消標記。

- **VLAN Tunnelling** - 如果封包的 EtherType 與 bridge 所設定的 EtherType 不符，則 ingress 封包會被視為未標記封包；此行為可將 VLAN 封裝到另一個不同的 VLAN 中。這也讓你能透過網路中的不同設備導向特定流量。

- **Tag stacking** - 如果封包具有與 EtherType 相符的 VLAN 標籤，則該封包會被視為已標記封包，但你可以不論封包內容為何，強制加上另一個 VLAN 標籤。在 bridge 埠上設定 `tag-stacking=yes` 時，所有 ingress 封包都會在任何其他標籤之上，加上一個使用 PVID 值的 VLAN 標籤。

## Trunk/Access 埠設定 {#trunkaccess-port-setup}

---

以下是一個非常常見的設定範例示意圖，由一個 trunk 埠與多個 access 埠組成：

![Trunk and Access Setup](/img/20938aff1d4b205b.webp)

這種設定非常常見，因為它讓你能在使用單一交換器，甚至可能只使用單一路由器時，將網路劃分為多個區段。對於想要區隔多個部門的公司來說，這類需求相當常見。透過 VLAN，你可以使用不同的 DHCP 伺服器，根據 VLAN ID 從不同子網路發出 IP 位址，這讓建立防火牆規則與 QoS 變得容易許多。

在這類設定中，你會將一些一般設備（例如桌上型電腦）連接到 **ether2** 與 **ether3**。這些設備可視為工作站，通常只使用未標記流量（雖然可以強制一般工作站送出的所有流量都加上 VLAN 標籤，但這並不常見）。若要將某些工作站與其他工作站隔離，你必須為所有進入 **ether2** 或 **ether3** 的封包加上 VLAN 標籤；但若要決定封包應取得哪個 VLAN ID，你需要使用稱為 **Port-based VLANs** 的概念。在此概念中，封包會根據設備所連接的 bridge 埠取得具有對應 VLAN ID 的 VLAN 標籤。例如，在此設定中，**ether2** 上的設備會取得具有 **VLAN20** 的 VLAN 標籤，而 **ether3** 上的設備會取得具有 **VLAN30** 的 VLAN 標籤。只要 bridge 埠足夠，這個概念就具有良好的擴充性。這應能讓你理解，bridge 與 **ether2/ether3** 後方設備之間的流量是未標記的（因為沒有 VLAN 標籤，因此得名）。

當我們已決定未標記埠後，接著可以決定標記埠。標記埠將作為 trunk 埠（承載多個 VLAN 的埠），通常這個埠會連接到路由器或另一台交換器／橋接器。你也可以有多個 trunk 埠。標記埠一律承載帶有 VLAN 標記的封包（因此得名），而且你必須針對希望此埠轉送的每個 VLAN ID **一律**指定標記埠。同一個埠可能對某個 VLAN ID 是標記埠，而對另一個 VLAN ID 是未標記埠，但這屬於不同類型的設定（Hybrid 埠設定）。

必須特別說明 `PVID` 屬性。此屬性應使用於 access 埠，但也可使用於 trunk 埠（在 Hybrid 埠設定中）。使用 `PVID` 屬性時，你會對在該橋接埠上接收的所有**未標記**封包，加上一個新的 VLAN 標記，其 VLAN ID 指定於 `PVID`。`PVID` 對已標記封包沒有任何影響，這表示例如若在具有 `PVID=20` 的 **ether2** 上接收到帶有 **VLAN40** VLAN 標記的封包，則 VLAN 標記**不會**變更，轉送將取決於橋接 VLAN 表中的項目。

若要設定 trunk／access 埠，你需要先建立橋接器：

```ros
/interface/bridge
add name=bridge1
```

:::danger
請勿啟用 VLAN 過濾，否則可能因為缺少管理存取而無法連上設備，管理存取會在最後設定。
:::

新增橋接埠，並為每個 access 埠指定 `PVID`：

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2 pvid=20
add bridge=bridge1 interface=ether3 pvid=30
```

:::warning
在啟用 VLAN 過濾之前，`PVID` 不會生效。
:::

在橋接 VLAN 表中新增適當項目：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 untagged=ether2 vlan-ids=20
add bridge=bridge1 tagged=ether1 untagged=ether3 vlan-ids=30
```

你可能會認為可以用單一項目簡化這些設定，例如：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 untagged=ether2,ether3 vlan-ids=20,30
```

請**不要**在 access 埠上使用多個 VLAN ID。這會不小心讓 **VLAN20** 與 **VLAN30** 同時通過兩個 access 埠。在上述範例中，**ether3** 應該要為所有 ingress 封包設定 VLAN 標籤以使用 **VLAN30**（因為 `PVID=30`），但當 VLAN 透過此埠傳送出去時，這並不會限制此埠允許的 VLAN。橋接器 VLAN 表負責決定是否允許 VLAN 透過特定埠傳送。上述項目指定 **VLAN20** 與 **VLAN30** 都允許透過 **ether2** 與 **ether3** 傳送出去，此外該項目也指定封包應該在沒有 VLAN 標籤的情況下傳送出去（封包會以 untagged 封包傳送出去）。因此，你可能會造成封包從 VLAN 洩漏到根本不應該接收此類流量的埠，請見下圖。

![Trunk and Access Setup Bad](/img/a7093a0683d04f73.webp)

設定錯誤的 VLAN 表允許 VLAN20 透過 ether3 傳送；它也將允許 VLAN30 透過 ether2 傳送

:::danger
請勿在橋接器 VLAN 表項目中為 access 埠指定一個以上的 VLAN ID；你應該只為 trunk 埠指定多個 VLAN ID。
:::

不需要將橋接器埠新增為 untagged 埠，因為每個橋接器埠都會以 `PVID` 屬性中指定的 VLAN ID 動態新增為 untagged 埠。這是因為有一項功能會為了便利性與效能，自動在橋接器 VLAN 表中新增適當的項目。這項功能確實有一些你必須注意的事項。所有具有相同 PVID 的埠都會被新增到對應 VLAN ID 的單一項目中作為 untagged 埠，但請注意，**Bridge 介面**也有 VLAN ID。

為了進行測試，我們將啟用 VLAN 過濾，但請注意，這可能會讓你失去對設備的存取，因為設備尚未設定管理存取（我們稍後會設定）。始終建議在使用序列主控台時設定 VLAN 過濾，不過你也可以透過未加入橋接器的埠來設定設備。請確認你正在使用序列主控台，或透過不同的埠（不在橋接器中的埠）連線，然後啟用 VLAN 過濾：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

:::warning
啟用 VLAN 過濾後，你可能不會立即失去對設備的存取，但可能會連線中斷，因為橋接器必須重設自身，VLAN 過濾才會生效，這會強制你重新連線（這主要與使用 MAC-telnet 有關）。你仍有可能使用 untagged 流量存取設備。下列章節會說明此情境。
:::

如果你現在已啟用 VLAN 過濾並列印出目前的 VLAN 表，你會看到這樣的表格：

```text
[admin@MikroTik] > /interface/bridge/vlan/print
Flags: X - disabled, D - dynamic 
 #   BRIDGE                     VLAN-IDS  CURRENT-TAGGED       CURRENT-UNTAGGED
 0   bridge1                    20        ether1               ether2
 1   bridge1                    30        ether1               ether3
 2 D bridge1                    1                              bridge1
                                                               ether1
```

由於所有橋接器埠（包括我們的 trunk 埠 **ether1**）預設都會設定 `PVID=1`，因此會為 **VLAN1** 新增一個動態項目，但你也應該注意到 **bridge1** 介面（CPU 埠）也會被動態新增。你應該知道 **bridge1** 也是橋接器埠，因此可能會被動態新增到橋接器 VLAN 表中。由於這項功能，你有可能會不小心允許存取設備。例如，如果你遵循本指南，並讓 trunk 埠（**ether1**）保持 **PVID=1**，同時也沒有變更 CPU 埠（**bridge1**）的 PVID，那麼就會允許透過 **ether1** 使用 untagged 流量存取設備。這在列印橋接器 VLAN 表時也可見。下圖說明了此情境：

![Trunk and Access Setup Unintentional Management](/img/f93fac4718d29a3f.webp)

不小心允許未標記流量透過 trunk 埠進行管理存取

:::danger
請務必檢查 bridge VLAN 表，確認你是否不小心允許特定 VLAN 或未標記流量存取特定埠，尤其是 CPU 埠（bridge）。
:::

有一種簡單的方法可以防止 bridge（CPU 埠）被新增為未標記埠。你只要將 trunk 埠的 PVID 設定為與 bridge 的 PVID 不同（或變更 bridge 的 PVID）即可，不過還有另一個更直觀且建議採用的選項。由於你預期 trunk 埠應該只接收標記流量（在此範例中，應該只接收 **VLAN20/VLAN30**），而不接收任何未標記流量，因此可以使用 ingress-filtering 搭配 frame-type 來篩選不需要的封包；但若要完整理解 ingress filtering 的行為，必須先瞭解管理存取的細節。

管理存取用於建立一種方式，讓使用者可以透過已啟用 VLAN filtering 的 bridge 存取設備。你可以直接允許未標記存取，而且做法相當簡單。假設你希望 **ether3** 後方的工作站可以存取設備。我們先前假設該工作站是一般電腦，不會使用標記封包，因此只會傳送未標記封包。這表示我們應該將 CPU 埠（**bridge1**）以未標記介面的形式新增到 bridge VLAN 表中；若要這麼做，只要對 **bridge1** 與 **ether3** 埠使用相同的 PVID 值，並將兩個埠都設定為該 VLAN ID 的未標記成員即可。在此情況下，你將從具有 `PVID=30` 的 **ether3** 連線，因此請據此變更設定：

```ros
/interface/bridge/set [find name=bridge1] pvid=30
/interface/bridge/vlan/set [find vlan-ids=30] untagged=bridge1,ether3
```

:::warning
你可以使用動態新增具有相同 PVID 值之未標記埠的功能，也可以直接變更 PVID，讓 **ether3** 與 **bridge1** 相符。
:::

允許使用未標記流量存取設備並不是良好的安全做法。更好的方式是允許使用非常特定的 VLAN 存取設備，這有時稱為管理 VLAN。在我們的案例中，這會是 **VLAN99**。這增加了顯著的安全層級，因為攻擊者必須先猜出用於管理用途的 VLAN ID，然後再猜出登入憑證。除此之外，你甚至可以只允許特定 IP 位址存取設備，以再加入一層安全防護。本指南的目的在於提供深入說明。因此，我們會在設定中增加一層複雜度，以瞭解你必須考量的一些注意事項。我們將允許從 access 埠使用標記流量進行存取（如下圖所示）。若要允許從 **ether3** 使用 **VLAN99** 存取設備，必須在 bridge VLAN 表中新增適當的項目。此外，連接到 ether3 的網路設備必須支援 VLAN 標記。

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,ether3 vlan-ids=99
```

![Trunk and Access Setup Management Access](/img/2e50b643c921b4f2.webp)

透過 access 埠使用標記流量進行管理存取（這會使其成為 hybrid 埠）

:::warning
如果 ether1 與 bridge1 的 PVID 相符（預設會相符，皆為 1），則由於動態將未標記埠新增到 bridge VLAN 表的功能，系統會允許使用來自 ether1 的未標記流量存取設備。
:::

不過，你可能會發現此時使用 **VLAN99** 的存取無法運作。這是因為你需要一個會接聽標記流量的 VLAN 介面。你可以直接為適當的 VLAN ID 建立此介面，也可以為該介面設定 IP 位址：

```ros
/interface/vlan
add interface=bridge1 name=VLAN99 vlan-id=99
/ip/address
add address=192.168.99.2/24 interface=VLAN99
```

:::warning
此時，我們的存取埠（**ether3**）會同時預期接收標記與未標記流量；這類埠稱為 **hybrid port**。
:::

此時，我們可以善用 `ingress-filtering` 與 `frame-type`。首先，我們將專注於 `frame-type`，它會限制允許的封包類型（tagged、untagged、both），但為了讓 `frame-type` 正常運作，必須啟用 `ingress-filtering`，否則它不會有任何效果。在我們的範例中，我們希望允許一般工作站透過 **ether3** 使用標記流量（**VLAN99**）存取網路，同時也允許存取網路，因此可推論此埠需要允許標記與未標記封包，但 **ether1** 與 **ether2** 應該只接收特定類型的封包，基於這些原因，我們可以強化網路的安全性。由於 **ether1** 是我們的 trunk 埠，它應該只承載標記封包，但 **ether2** 是我們的存取埠，因此不應該承載任何標記封包，根據這些結論，我們可以丟棄無效封包：

```ros
/interface/bridge/port
set [find where interface=ether1] ingress-filtering=yes frame-types=admit-only-vlan-tagged
set [find where interface=ether2] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
```

假設你忘記啟用 ingress-filtering，並變更 **ether1** 上的 frame-type 屬性，這會不小心允許透過 **ether1** 使用未標記流量存取設備，因為 **bridge1** 與 **ether1** 的 PVID 相符，但你預期只有標記流量能夠存取設備。你可以丟棄所有目的地為 **CPU port** 的未標記封包：

```ros
/interface/bridge
set bridge1 frame-types=admit-only-vlan-tagged ingress-filtering=yes
```

這不只會丟棄未標記封包，也會停用將未標記埠動態新增至 bridge VLAN 表的功能。如果你列印目前的 bridge VLAN 表，你會發現 **bridge1** 並未以未標記埠的形式動態新增：

```text
[admin@MikroTik] > /interface/bridge/vlan/print 
Flags: X - disabled, D - dynamic 
 #   BRIDGE       VLAN-IDS  CURRENT-TAGGED        CURRENT-UNTAGGED
 0   bridge1      20        ether1
 1   bridge1      30        ether1                ether3
 2 D bridge1      1                               ether1
 3   bridge1      99        bridge1
                            ether3  
```

:::warning
當在埠上使用 `frame-type=admit-only-vlan-tagged` 時，該埠不會以 PVID 的未標記埠形式動態新增。
:::

雖然 `frame-type` 可用於丟棄特定類型的封包，但 `ingress-filtering` 可用於在封包送出前將其過濾掉。若要完整理解 ingress filtering 的必要性，請考量以下情境：**VLAN99** 在 **ether3** 與 **bridge1** 上是允許的，但你仍然可以將 **VLAN99** 流量從 **ether1** 傳送到 **ether3**。這是因為 bridge VLAN 表只會在 egress 埠上檢查埠是否允許承載特定 VLAN。在我們的案例中，**ether3** 被允許承載 **VLAN99**，因此封包會被轉送。若要避免這種情況，你**必須**使用 ingress-filtering。啟用 ingress filtering 後，ingress 封包也會被檢查。在我們的案例中，bridge VLAN 表沒有包含 **ether1** 允許 **VLAN99** 的項目，因此封包會立即被丟棄。當然，在我們沒有 ingress filtering 的情境中，連線無法建立，因為 **VLAN99** 只能從 **ether1** 轉送到 **ether3**，而不能從 **ether3** 轉送到 **ether1**，不過在這種錯誤設定下，仍有可能被用於攻擊（例如 ARP poisoning）。封包丟棄行為如下圖所示：

![Trunk and Access Setup Ingress](/img/7749e7dc360a6532.webp)

有與沒有 ingress filtering 的 trunk/access 埠設定。Ingress filtering 可避免不必要的流量被轉送。請注意，bridge VLAN 表不允許 ether1 承載 VLAN99。

:::danger
請盡可能在所有可使用 `ingress-filtering` 的地方啟用它。它會增加一層重要的安全性。
:::

`ingress-filtering` 也可以用於 **CPU 埠**（bridge）。這可用於防範某些可能的攻擊途徑，並限制可存取 CPU 的 VLAN。相較於在 egress 埠丟棄封包，在 ingress 埠丟棄封包會更好。這可降低 CPU 負載，而當你搭配 bridge VLAN filtering 使用硬體卸載時，這一點相當關鍵。

:::warning
`ingress-filtering` 屬性只會影響 ingress 流量，但 `frame-type` 會同時影響 egress 與 ingress 流量。
:::

即使你可以限制連接埠上允許的 VLAN 與封包類型，允許透過 access 埠存取設備仍然不是良好的安全做法，因為攻擊者可能擷取封包並取得管理 VLAN 的 ID。你應該只允許從 trunk 埠（**ether1**）存取設備，因為 trunk 埠通常有較佳的實體安全。你應該移除先前的項目，並允許透過連接到路由器的埠存取設備（如下圖所示）：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,ether1 vlan-ids=99
```

![Basic VLAN Switching](/img/3d52e43430750024.webp)

## VLAN 通道設定 {#vlan-tunnelling-setup}

---

在某些情況下，你可能希望將已標記的流量轉送通過特定交換器。這在骨幹基礎架構中是相當常見的設定，因為它提供了一種方式，可封裝例如來自邊緣路由器的流量，並無縫地透過骨幹轉送至另一台邊緣路由器。以下為 VLAN tunneling 拓撲範例：

![Provider Bridge](/img/e772ab697f2fae91.webp)

提供者橋接拓撲

SVID 代表 Service VID，表示標記類型以及 VID。

:::warning
若要完整瞭解如何正確設定 VLAN 隧道，請先閱讀 Trunk/Access 埠設定章節，再繼續後續操作。
:::

有兩種方式可以達成此目的，一種是標準化的 IEEE 802.1ad 方式，另一種是使用 **Tag stacking**。我們會先說明標準化方式，因為兩種方式的原理相同，只需變更幾個參數即可改用另一種方法。VLAN 隧道的運作方式是，bridge 會檢查外層 VLAN tag 是否使用 ether-type 中指定的 VLAN tag。若 VLAN tag 相符，封包會被視為 tagged 封包，否則會被視為 untagged 封包。

:::warning
bridge 只會檢查外層 tag（最接近 MAC 位址的 tag）；在 bridge 設定中，任何其他 tag 都會被忽略。bridge 不會感知封包內容；即使封包中可能有另一個 VLAN tag，也只會檢查第一個 VLAN tag。
:::

ether-type 屬性可讓你為 VLAN tag 選擇下列 EtherType：

- 0x88a8 - IEEE 802.1ad，Service Tag。
- 0x8100 - IEEE 802.1Q，Customer VLAN（一般 VLAN tag）。
- 0x9100 - 非官方 tag 類型（很少使用）。

若要正確設定 bridge VLAN filtering，你必須瞭解 bridge 如何區分 tagged 與 untagged 封包。如前所述，bridge 會檢查 EtherType 是否與封包中的外層 VLAN tag 相符。例如，請看下列封包：

```text
FFFFFFFFFFFF 6C3B6B7C413E 8100 6063 9999
----------------------------------------
DST-MAC = FFFFFFFFFFFF
SRC-MAC = 6C3B6B7C413E
Outer EtherType = 8100 (IEEE 802.1Q VLAN tag)
VLAN priority = 3
VLAN ID = 99 (HEX = 63)
Inner EtherType = 9999
```

假設我們已設定 **`ether-type=0x88a8`**，在此情況下，上述封包會被視為 untagged，因為 bridge 正在尋找不同的 VLAN tag。現在請看下列封包：

```text
FFFFFFFFFFFF 6C3B6B7C413E 88A8 6063 8100 5062 9999
----------------------------------------
DST-MAC = FFFFFFFFFFFF
SRC-MAC = 6C3B6B7C413E
Outer EtherType = 88A8 (IEEE 802.1ad VLAN tag)
VLAN priority = 3
VLAN ID = 99 (HEX = 63)
Inner EtherType 1 = 8100 (IEEE 802.1Q VLAN tag)
VLAN priority = 2
VLAN ID = 98 (HEX = 62)
Inner EtherType 2 = 9999
```

這次假設我們已設定 **`ether-type=0x8100`**。在此情況下，上述封包同樣會被視為 untagged，因為外層 tag 使用的是 IEEE 802.1ad VLAN tag。相同的原理也適用於其他 VLAN 相關功能，例如，`PVID` 屬性會在 access 埠上新增 VLAN tag，而該 VLAN tag 會使用 ether-type 中指定的 EtherType。

**SW1** 與 **SW2** 都使用相同的設定：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes ether-type=0x88a8
/interface/bridge/port
add interface=ether1 bridge=bridge1 pvid=200
add interface=ether2 bridge=bridge1 pvid=300
add interface=ether3 bridge=bridge1
/interface/bridge/vlan
add bridge=bridge1 tagged=ether3 untagged=ether1 vlan-ids=200
add bridge=bridge1 tagged=ether3 untagged=ether2 vlan-ids=300
```

在此範例中，我們假設所有路由器都在傳遞使用一般／客戶 VLAN 標籤的流量。這類流量在交換器上會依上述原則被視為未標記流量。交換器會使用 Service VLAN 標籤（外層 802.1ad 標籤）封裝這類流量，而 **SW1** 與 **SW2** 之間的流量會被視為已標記。在流量抵達目的地之前，交換器會解封裝外層標籤，並轉送原始的 802.1Q 標記訊框。請參閱下列封包範例：

![Service VLAN 802.1ad](/img/b77a2f1f9e4171e9.webp)A packet example before and after 802.1ad VLAN encapsulation

:::warning
所有適用於使用 IEEE 802.1Q 的一般 trunk／access 埠設定的原則，也適用於 VLAN 隧道設定。請務必使用 bridge VLAN 表與 ingress filtering 正確限制 VLAN 與封包類型。
:::

若你想建立從 **ether3** 到設備的管理存取，並使用 **VLAN99**，則可使用下列指令：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,ether3 vlan-ids=99
/interface/vlan
add interface=bridge1 name=VLAN99 use-service-tag=yes vlan-id=99
/ip/address
add address=192.168.99.2/24 interface=VLAN99
```

如你所見，唯一的差異是 VLAN 介面使用了 `use-service-tag=yes`；這會讓 VLAN 介面監聽 IEEE 802.1ad VLAN 標籤。這會要求你使用 IEEE 802.1ad VLAN 標籤，透過管理 VLAN 存取設備；當 bridge VLAN filtering 啟用時，你將無法使用一般 VLAN 標籤連線到設備。ether-type 是全域設定，會影響所有 bridge VLAN filtering 功能。

:::danger
搭載 Marvell-98DX3257 交換器晶片的設備（例如 CRS354 系列）不支援在 1Gbps Ethernet 介面上，對其他 VLAN 類型（`0x88a8` 與 `0x9100`）進行 VLAN filtering。
:::

### 標記堆疊 {#tag-stacking}

在 VLAN Tunnelling 設定中，我們新增了一個與原 VLAN 標籤不同的 VLAN 標籤，但其實不論封包內容為何，都可以新增 VLAN 標籤。與一般 VLAN 隧道設定的差異在於，bridge 不會檢查封包是已標記或未標記，它會假設在特定埠上接收的所有封包都是未標記封包，並且不論是否存在 VLAN 標籤，都會新增一個新的 VLAN 標籤。這稱為 **Tag Stacking**，因為它會在先前的標籤之上「堆疊」VLAN 標籤，而不論 VLAN 標籤類型為何。對於不支援 IEEE 802.1ad 標準，但仍希望將 VLAN 流量封裝進新 VLAN 的網路來說，這是非常常見的設定。

將要新增的 VLAN 標籤取決於 `ether-type` 與 `PVID`。例如，如果連接埠上有 `ether-type=0x8100` 與 `PVID=200`，則 bridge 會在任何既有標籤之上新增一個 IEEE 802.1Q VLAN 標籤。相同的 VLAN 過濾原則仍然適用。您必須判斷哪些連接埠要作為 trunk 埠，並將其標記為 tagged 埠，判斷哪些是 access 埠，並將其新增為 untagged 埠。

為了說明標籤堆疊如何進行 VLAN 標記與移除標記，讓我們使用先前相同的網路拓撲：

![Basic VLAN Switching 2](/img/02a6439c12aa7838.webp)

我們想要達成的是，無論 **ether2** 與 **ether3** 接收到什麼內容，都會新增一個 VLAN 標籤來封裝來自這些連接埠的流量。`Tag-stacking` 會強制新增 VLAN 標籤，因此我們可以使用此屬性來達成所需的設定。我們將使用與 Trunk/Access 連接埠設定相同的組態，但在 access 埠上啟用 `tag-stacking`：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes ether-type=0x8100
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2 tag-stacking=yes pvid=20
add bridge=bridge1 interface=ether3 tag-stacking=yes pvid=30
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 untagged=ether2 vlan-ids=20
add bridge=bridge1 tagged=ether1 untagged=ether3 vlan-ids=30
```

:::warning
新增的 VLAN 標籤會使用指定的 `ether-type`。所選的 EtherType 也會用於 VLAN 過濾。系統只會檢查外層標籤，但啟用 tag-stacking 後，會略過標籤檢查，並假設無論如何都必須新增一個新標籤。
:::

假設 **ether2** 與 **ether3** 後方的設備正在傳送帶有標籤的 **VLAN40** 流量。在此設定下，**所有**封包都會被封裝一個新的 VLAN 標籤，但您必須確認已將外層標籤的 VLAN ID 新增到 bridge VLAN 表中。**VLAN40** 不會新增到 bridge VLAN 表，因為它是內層標籤且不會被檢查；我們只關心外層標籤，也就是依連接埠而定為 **VLAN20** 或 **VLAN30**。

與其他設定類似，bridge VLAN 表會用來判斷是否需要移除 VLAN 標籤。例如，當 **ether1** 收到帶有標籤的 **VLAN20** 封包時，bridge 會檢查 **ether2** 是否允許攜帶 **VLAN20**，因此準備透過 **ether2** 送出，但它也會檢查 bridge VLAN 表，判斷是否應移除 VLAN 標籤；由於 **ether2** 被標記為 untagged 埠，bridge 會將這些封包從 **ether1** 轉送至 **ether2**，且不含 **VLAN20** VLAN 標籤。

從 access 埠的角度來看，適用與 Trunk/Access 連接埠設定相同的原則。所有在 **ether2** 上接收到的封包都會取得一個新的 VLAN 標籤，其 VLAN ID 為 PVID 中指定的值；在此案例中，會新增一個帶有 **VLAN20** 的新 VLAN 標籤，且此 VLAN 會受到 VLAN 過濾。請參閱下方的封包範例：

![Tag Stacking](/img/ef2698e5bd946e5c.webp)

標籤堆疊前後的封包範例
