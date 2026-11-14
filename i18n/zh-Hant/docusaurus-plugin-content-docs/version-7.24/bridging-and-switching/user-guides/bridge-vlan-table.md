---
sidebar_key: "bridging-and-switching/user-guides/bridge-vlan-table"
sidebar_position: 3
title: "網橋 VLAN 表"
sidebar_label: "網橋 VLAN 表"
description: "本頁介紹 MikroTik RouterOS 的 Bridge VLAN Table 功能，說明如何使用 tagged/untagged 埠、PVID 以及 ingress/egress 規則在網橋中配置 VLAN filtering。文中包含 trunk 和 access 埠的設定示例，強調透過管理訪問控制和 EtherType filtering 來提升安全性。"
tags:
  - 'bridge-vlan-filtering'
  - 'vlan'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/bridge-vlan-table
captured_at: '2026-11-04T11:27:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

---

可以使用網橋來過濾網路中的 VLAN。為此，應使用[網橋 VLAN 過濾](../index.md#bridge-vlan-filtering)功能。應使用此功能來替代許多已知的 VLAN 錯誤配置，這些配置很可能導致效能問題或連線問題。你可以在[帶有物理介面的網橋中的 VLAN](./layer2-misconfiguration.md#vlan-in-a-bridge-with-a-physical-interface)一節中瞭解一種最常見的錯誤配置。網橋 VLAN 過濾功能最重要的部分是網橋 VLAN 表，它指定每個埠允許哪些 VLAN；但如果你要嘗試更高階的設定，配置它可能會變得相當複雜。對於通用設定，你應該能夠使用 [Trunk 和 Access 埠](../index.md#vlan-example-trunk-and-access-ports)示例來配置裝置，但本指南的目的是提供深入說明，並指出使用網橋 VLAN 過濾時的一些行為特徵。

## 背景 {#background}

---

在深入解釋網橋 VLAN 過濾之前，你應該瞭解網橋 VLAN 過濾涉及的幾個基本概念。

- **Tagged/Untagged** - 在 `/interface/bridge/vlan` 選單下，你可以指定一個包含帶標籤埠和不帶標籤埠的條目。通常，帶標籤埠應是你的 Trunk 埠，不帶標籤埠應是你的 Access 埠。透過指定帶標籤埠，網橋會始終為此埠發出的封包（出方向）設定 VLAN 標籤。透過指定不帶標籤埠，網橋會始終從出方向封包中移除 VLAN 標籤。

- **VLAN-ids** - 在 `/interface/bridge/vlan` 選單下，你可以指定一個條目，在其中允許特定埠上使用某些 VLAN。VLAN ID 會在出方向埠上檢查。如果封包包含的 VLAN ID 在該出方向埠的網橋 VLAN 表中不存在，那麼該封包會在發出之前被丟棄。

- **PVID** - 埠 VLAN ID 用於 Access 埠，為所有入方向流量打上特定 VLAN ID 的標籤。每使用一個 PVID，都會在網橋 VLAN 表中新增一個動態條目，並且該埠會自動作為不帶標籤埠新增。

- **入方向過濾** - 預設情況下，網橋 VLAN 表中不存在的 VLAN 會在發出（出方向）之前被丟棄，但此屬性允許你在封包被接收（入方向）時將其丟棄。

- **管理訪問** - 網橋本應只是在網橋埠之間轉發封包，對其他裝置來說，就好像它們之間只有一根線纜。使用網橋 VLAN 過濾，你可以限制哪些封包允許訪問配置了該網橋的裝置。最常見的做法是隻允許透過一個非常特定的 VLAN ID 訪問裝置，但還有其他授予裝置訪問許可權的方式。管理訪問是透過網橋埠訪問裝置時增加另一層安全性的好方法；這種訪問有時稱為管理埠。對於支援帶硬體解除安裝的 VLAN 過濾的裝置，它還與網橋的 CPU 埠相關。

- **CPU 埠** - 每個帶有交換晶片的裝置都有一個稱為 CPU 埠的專用埠，用於與裝置的 CPU 通訊。對於支援帶硬體解除安裝的 VLAN 過濾的裝置，此埠就是網橋介面本身。此埠主要用於建立管理訪問，但也可用於其他目的，例如在 VLAN 之間路由流量、標記封包以及應用佇列。

- **frame-type** - 你可以根據封包是否帶有 VLAN 標籤來過濾封包；這對於為網橋埠增加額外一層安全性很有用。

- **EtherType** - 預設情況下，支援 VLAN 的網橋會透過檢查 C-TAG (0x8100) 來過濾 VLAN；所有其他 VLAN 標籤型別都會被視為不帶標籤的封包（沒有 VLAN 標籤）。選定的 EtherType 將用於 VLAN 過濾以及 VLAN 打標籤/移除標籤。

- **VLAN 隧道** - 如果封包的 EtherType 與網橋配置的 EtherType 不匹配，那麼入方向封包會被視為不帶標籤的封包；這種行為使得可以將 VLAN 封裝到另一個不同的 VLAN 中。這也使得可以在網路中將特定流量引導透過不同的裝置。

- **標籤堆疊** - 如果封包帶有與 EtherType 匹配的 VLAN 標籤，那麼該封包會被視為帶標籤的封包，但你可以不顧封包內容而強制新增另一個 VLAN 標籤。透過在網橋埠上設定 `tag-stacking=yes`，你會為所有入方向封包在任意其他標籤之上再新增一個使用 PVID 值的 VLAN 標籤。

## Trunk/Access 埠設定 {#trunkaccess-port-setup}

---

下面是一個非常常見的示意圖，展示了一種非常典型的設定，由一個 Trunk 埠和多個 Access 埠組成：

![Trunk and Access Setup](/img/20938aff1d4b205b.webp)

這種設定非常常見，因為它允許你在使用單臺交換器（也許還有單臺路由器）的同時，將網路劃分為多個網段。對於希望分隔多個部門的公司來說，這種需求非常常見。使用 VLAN，你可以使用不同的 DHCP 伺服器，這些伺服器可以根據 VLAN ID 從不同子網分配 IP 地址，從而使建立防火牆規則和 QoS 容易得多。

在這樣的設定中，你會將一些通用裝置（例如臺式 PC）連線到 **ether2** 和 **ether3**。這些裝置可以視為工作站，它們通常只使用不帶標籤的流量（可以強制從通用工作站發出的所有流量都帶 VLAN 標籤，不過這並不常見）。要將某些工作站與其他工作站隔離，你必須為進入 **ether2** 或 **ether3** 的所有封包新增 VLAN 標籤，但要決定封包應獲得哪個 VLAN ID，你需要使用一種稱為 **基於埠的 VLAN** 的概念。在此概念中，封包會根據裝置所連線的網橋埠獲得帶有相應 VLAN ID 的 VLAN 標籤。例如，在此設定中，**ether2** 上的裝置將獲得帶有 **VLAN20** 的 VLAN 標籤，而 **ether3** 上的裝置將獲得帶有 **VLAN30** 的 VLAN 標籤。只要你有足夠的網橋埠，此概念就非常具有可擴充套件性。這應讓你理解：網橋與 **ether2/ether3** 後面的裝置之間的流量是不帶標籤的（因為沒有 VLAN 標籤，名稱也由此而來）。

在確定不帶標籤埠之後，我們現在可以確定帶標籤埠。帶標籤埠將是 Trunk 埠（承載多個 VLAN 的埠），通常此埠連線到路由器或另一臺交換器/網橋。你也可以有多個 Trunk 埠。帶標籤埠始終承載帶有 VLAN 標籤的封包（名稱也由此而來），並且對於你希望該埠轉發的每個 VLAN ID，你**必須始終**指定帶標籤埠。一個埠可能對某個 VLAN ID 是帶標籤埠，而同一埠對另一個 VLAN ID 是不帶標籤埠，但這屬於另一種型別的設定（Hybrid 埠設定）。

需要特別說明 PVID 屬性。此屬性應在 Access 埠上使用，但也可以用於 Trunk 埠（在 Hybrid 埠設定中）。透過使用 PVID 屬性，你會為在該特定網橋埠上接收到的所有 **不帶標籤** 封包新增一個帶有 PVID 中指定 VLAN ID 的新 VLAN 標籤。PVID 對帶標籤封包沒有任何影響，這意味著，例如，如果 **ether2** 上接收到一個帶有 **VLAN40** 標籤的封包，而該埠具有 `PVID=20`，那麼 VLAN 標籤**不會**改變，轉發將取決於網橋 VLAN 表中的條目。

要配置 Trunk/Access 埠設定，你需要先建立一個網橋：

```ros
/interface/bridge
add name=bridge1
```

:::danger
暫時不要啟用 VLAN 過濾，否則你可能會因為缺少管理訪問（將在最後配置）而被鎖定在裝置之外。
:::

新增網橋埠，併為每個 Access 埠指定 PVID：

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2 pvid=20
add bridge=bridge1 interface=ether3 pvid=30
```

:::warning
在啟用 VLAN 過濾之前，PVID 不會生效。
:::

在網橋 VLAN 表中新增相應條目：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 untagged=ether2 vlan-ids=20
add bridge=bridge1 tagged=ether1 untagged=ether3 vlan-ids=30
```

你可能認為可以用單個條目簡化這些條目，類似這樣：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 untagged=ether2,ether3 vlan-ids=20,30
```

**不要**在 Access 埠上使用多個 VLAN ID。這會無意中在兩個 Access 埠上都允許 **VLAN20** 和 **VLAN30**。在上面的示例中，**ether3** 本應為所有入方向封包設定使用 **VLAN30** 的 VLAN 標籤（因為 `PVID=30`），但當 VLAN 透過此埠發出時，這並不會限制該埠上允許的 VLAN。網橋 VLAN 表負責決定是否允許某個 VLAN 透過特定埠傳送。上面的條目指定允許 **VLAN20** 和 **VLAN30** 都透過 **ether2** 和 **ether3** 發出，而且該條目還指定封包應在不帶 VLAN 標籤的情況下發出（封包作為不帶標籤的封包發出）。結果，你可能會造成 VLAN 封包洩漏到甚至不應接收此類流量的埠，見下圖。

![Trunk and Access Setup Bad](/img/a7093a0683d04f73.webp)

配置錯誤的 VLAN 表允許 VLAN20 透過 ether3 傳送；它也會允許 VLAN30 透過 ether2 傳送

:::danger
對於 Access 埠，不要在單個網橋 VLAN 表條目中指定多個 VLAN ID；只應為 Trunk 埠指定多個 VLAN ID。
:::

沒有必要將網橋埠新增為不帶標籤埠，因為每個網橋埠都會根據 PVID 屬性中指定的 VLAN ID 動態新增為不帶標籤埠。這是因為有一項功能會出於便利性和效能原因自動在網橋 VLAN 表中新增相應條目。此功能確實有一些你必須瞭解的注意事項。所有具有相同 PVID 的埠都會作為不帶標籤埠新增到相應 VLAN ID 的單個條目中，但請注意，**網橋介面**也有一個 VLAN ID。

出於測試目的，我們將啟用 VLAN 過濾，但請注意，這可能會讓你失去對裝置的訪問許可權，因為尚未配置管理訪問（我們稍後會配置）。始終建議在使用序列控制檯時配置 VLAN 過濾，不過你也可以透過未新增到網橋的埠來配置裝置。請確保你正在使用序列控制檯，或透過其他埠（不在網橋中）連線，然後啟用 VLAN 過濾：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

:::warning
啟用 VLAN 過濾後，你可能不會立即失去對裝置的訪問許可權，但可能會斷開連線，因為網橋必須重設自身才能使 VLAN 過濾生效，這會迫使你重新連線（這主要與使用 MAC-telnet 時相關）。你仍有可能透過不帶標籤的流量訪問裝置。下面將描述這種情況。
:::

如果你現在已啟用 VLAN 過濾並列印當前 VLAN 表，你會看到類似這樣的表：

```text
[admin@MikroTik] > /interface/bridge/vlan/print
Flags: X - disabled, D - dynamic 
 #   BRIDGE                     VLAN-IDS  CURRENT-TAGGED       CURRENT-UNTAGGED
 0   bridge1                    20        ether1               ether2
 1   bridge1                    30        ether1               ether3
 2 D bridge1                    1                              bridge1
                                                               ether1
```

由於預設情況下所有網橋埠（包括我們的 Trunk 埠 **ether1**）都設定了 `PVID=1`，因此會為 **VLAN1** 新增一個動態條目，但你也應該注意到 **bridge1** 介面（CPU 埠）也被動態添加了。你應該意識到 **bridge1** 也是一個網橋埠，因此可能會被動態新增到網橋 VLAN 表中。由於此功能，你可能會有意無意地允許訪問裝置。例如，如果你遵循了本指南，併為 Trunk 埠（**ether1**）保留了 **PVID=1**，同時也沒有更改 CPU 埠（**bridge1**）的 PVID，那麼就允許透過 **ether1** 使用不帶標籤的流量訪問裝置。列印網橋 VLAN 表時也可以看到這一點。下圖說明了這種情況：

![Trunk and Access Setup Unintentional Management](/img/f93fac4718d29a3f.webp)

透過 Trunk 埠使用不帶標籤流量無意中允許的管理訪問

:::danger
始終檢查網橋 VLAN 表，確認你沒有無意中允許某些 VLAN 或不帶標籤流量訪問特定埠，尤其是 CPU 埠（網橋）。
:::

有一種簡單方法可以防止網橋（CPU 埠）被新增為不帶標籤埠。你可以簡單地將 Trunk 埠上的 PVID 設定為不同於網橋 PVID 的值（或更改網橋的 PVID），但還有另一個更直觀且推薦的選擇。由於你期望 Trunk 埠只接收帶標籤流量（在此示例中，它應只接收 **VLAN20/VLAN30**），而不接收不帶標籤流量，你可以結合使用 ingress-filtering 和 frame-type 來過濾掉不需要的封包，但要完全理解入方向過濾的行為，我們必須先了解管理訪問的細節。

管理訪問用於建立一種透過啟用了 VLAN 過濾的網橋訪問裝置的方式。你可以直接允許不帶標籤訪問，這樣做相當簡單。假設你希望 **ether3** 後面的工作站能夠訪問裝置。我們之前假設該工作站是一臺通用計算機，不會使用帶標籤封包，因此只會發出不帶標籤封包。這意味著我們應該將 CPU 埠（**bridge1**）作為不帶標籤介面新增到網橋 VLAN 表中；為此，只需為 **bridge1** 和 **ether3** 埠使用相同的 PVID 值，並將兩個埠都設定為該 VLAN ID 的不帶標籤成員。在這種情況下，你將透過具有 `PVID=30` 的 **ether3** 連線，因此相應地更改配置：

```ros
/interface/bridge/set [find name=bridge1] pvid=30
/interface/bridge/vlan/set [find vlan-ids=30] untagged=bridge1,ether3
```

:::warning
你可以使用自動將具有相同 PVID 值的埠新增為不帶標籤埠的功能，也可以簡單地更改 PVID，使 **ether3** 和 **bridge1** 的 PVID 相匹配。
:::

使用不帶標籤流量允許訪問裝置並不被認為是一種良好的安全實踐。更好的方式是使用一個非常特定的 VLAN（有時稱為管理 VLAN）來允許訪問裝置。在我們的情況下，這將是 **VLAN99**。這增加了一層顯著的安全性，因為攻擊者必須猜測用於管理目的的 VLAN ID，然後再猜測登入憑據。除此之外，你甚至可以透過僅允許來自特定 IP 地址的訪問來增加另一層安全性。本指南的目的是提供深入說明。因此，我們正在為設定增加一定複雜度，以瞭解你必須考慮的一些可能注意事項。我們將允許從 Access 埠使用帶標籤流量進行訪問（如下圖所示）。要允許從 **ether3** 使用 **VLAN99** 訪問裝置，我們必須在網橋 VLAN 表中新增一個正確的條目。此外，連線到 ether3 的網路裝置必須支援 VLAN 標籤。

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,ether3 vlan-ids=99
```

![Trunk and Access Setup Management Access](/img/2e50b643c921b4f2.webp)

透過 Access 埠使用帶標籤流量進行管理訪問（這使其成為 Hybrid 埠）

:::warning
如果 ether1 和 bridge1 的 PVID 相同（預設情況下確實與 1 相同），那麼由於會自動將不帶標籤埠新增到網橋 VLAN 表的功能，允許從 ether1 使用不帶標籤流量訪問裝置。
:::

但你可能注意到，此時使用 **VLAN99** 的訪問還無法工作。這是因為你需要一個監聽帶標籤流量的 VLAN 介面。你可以簡單地為相應 VLAN ID 建立此介面，並且還可以為該介面設定 IP 地址：

```ros
/interface/vlan
add interface=bridge1 name=VLAN99 vlan-id=99
/ip/address
add address=192.168.99.2/24 interface=VLAN99
```

:::warning
此時我們的 Access 埠（**ether3**）同時期望帶標籤和不帶標籤流量；這樣的埠稱為 **混合埠**。
:::

此時，我們可以受益於使用 `ingress-filtering` 和 `frame-type`。首先，我們將重點關注 `frame-type`，它限制允許的封包型別（帶標籤、不帶標籤、兩者），但要讓 `frame-type` 正常工作，必須啟用 `ingress-filtering`，否則它不會產生任何效果。在我們的示例中，我們希望允許從 **ether3** 使用帶標籤流量（**VLAN99**）訪問，同時允許通用工作站訪問網路，因此可以得出結論：此埠需要允許帶標籤和不帶標籤封包，但 **ether1** 和 **ether2** 應只接收特定型別的封包；基於這些原因，我們可以增強網路的安全性。由於 **ether1** 是我們的 Trunk 埠，它應只承載帶標籤封包，而 **ether2** 是我們的 Access 埠，因此它不應承載任何帶標籤封包；基於這些結論，我們可以丟棄無效封包：

```ros
/interface/bridge/port
set [find where interface=ether1] ingress-filtering=yes frame-types=admit-only-vlan-tagged
set [find where interface=ether2] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
```

假設你忘記在 **ether1** 上啟用 ingress-filtering 並更改 frame-type 屬性，由於 **bridge1** 和 **ether1** 的 PVID 相同，這會無意中允許透過 **ether1** 使用不帶標籤流量訪問裝置，而你期望只有帶標籤流量才能訪問裝置。可以丟棄所有發往 **CPU 埠** 的不帶標籤封包：

```ros
/interface/bridge
set bridge1 frame-types=admit-only-vlan-tagged ingress-filtering=yes
```

這不僅會丟棄不帶標籤封包，還會停用自動將不帶標籤埠新增到網橋 VLAN 表的功能。如果你列印當前網橋 VLAN 表，你會注意到 **bridge1** 沒有被動態新增為不帶標籤埠：

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
在埠上使用 `frame-type=admit-only-vlan-tagged` 時，該埠不會為 PVID 動態新增為不帶標籤埠。
:::

雖然 `frame-type` 可用於丟棄某種型別的封包，但 `ingress-filtering` 可用於在封包發出之前將其過濾掉。要完全理解入方向過濾的必要性，請考慮以下場景：**VLAN99** 在 **ether3** 和 **bridge1** 上被允許，但你仍然可以將 **VLAN99** 流量從 **ether1** 傳送到 **ether3**。這是因為網橋 VLAN 表只在出方向埠上檢查某個埠是否允許承載特定 VLAN。在我們的情況下，**ether3** 被允許承載 **VLAN99**，因此它會被轉發。要防止這種情況，你**必須**使用 ingress-filtering。使用入方向過濾時，入方向封包也會被檢查。在我們的情況下，網橋 VLAN 表不包含允許 **VLAN99** 在 **ether1** 上的條目，因此該封包會立即被丟棄。當然，在沒有入方向過濾的場景中，連線無法建立，因為 **VLAN99** 只能從 **ether1** 轉發到 **ether3**，而不能從 **ether3** 轉發到 **ether1**，不過在這種錯誤配置下仍可能存在一些攻擊（例如 ARP 欺騙）。下圖說明了封包丟棄行為：

![Trunk and Access Setup Ingress](/img/7749e7dc360a6532.webp)

使用和不使用入方向過濾的 Trunk/Access 埠設定。入方向過濾可以防止不需要的流量被轉發。注意，在網橋 VLAN 表中，ether1 不被允許承載 VLAN99。

:::danger
只要可能，就始終嘗試使用 `ingress-filtering`。它會增加一層顯著的安全性。
:::

`ingress-filtering` 也可以用在 **CPU 埠**（網橋）上。這可用於防止一些可能的攻擊向量，並限制可訪問 CPU 的允許 VLAN。最好在入方向埠而不是出方向埠丟棄封包。這會降低 CPU 負載，這在使用帶網橋 VLAN 過濾的硬體解除安裝時非常關鍵。

:::warning
`ingress-filtering` 屬性隻影響入方向流量，而 `frame-type` 同時影響出方向和入方向流量。
:::

即使你可以限制埠上允許的 VLAN 和封包型別，透過 Access 埠允許訪問裝置也從來都不是良好的安全實踐，因為攻擊者可以嗅探封包並提取管理 VLAN 的 ID。你應只允許從 Trunk 埠（**ether1**）訪問裝置，因為 Trunk 埠通常具有更好的物理安全性。你應刪除之前的條目，並允許透過連線到路由器的埠訪問裝置（如下圖所示）：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,ether1 vlan-ids=99
```

![Basic VLAN Switching](/img/3d52e43430750024.webp)

## VLAN 隧道設定 {#vlan-tunnelling-setup}

---

在某些情況下，你可能希望透過某些交換器轉發已經帶有標籤的流量。這對於骨幹基礎設施來說是一種相當常見的設定，因為它提供了一種可能性：將來自（例如）邊緣路由器的流量封裝起來，並無縫地透過骨幹網轉發到另一個邊緣路由器。下面是一個 VLAN 隧道拓撲示例：

![Provider Bridge](/img/e772ab697f2fae91.webp)

提供商網橋拓撲

SVID 代表 Service VID，表示標籤型別以及 VID。

:::warning
要完全理解如何正確配置 VLAN 隧道，你應先閱讀 Trunk/Access 埠設定一節，然後再繼續。
:::

有兩種可行的方法：一種是標準化的 IEEE 802.1ad 方式，另一種是使用 **標籤堆疊**。我們將先回顧標準化方式，因為兩種方式適用相同的原則，使用另一種方法只需更改幾個引數。VLAN 隧道的工作方式是：網橋檢查外層 VLAN 標籤是否使用與 ether-type 中指定的相同 VLAN 標籤。如果 VLAN 標籤匹配，則該封包被視為帶標籤封包；否則，它被視為不帶標籤封包。

:::warning
網橋只檢查外層標籤（最靠近 MAC 地址的標籤）；在網橋配置的任何位置都會忽略其他標籤。網橋並不瞭解封包內容；即使可能存在另一個 VLAN 標籤，也只檢查第一個 VLAN 標籤。
:::

ether-type 屬性允許你為 VLAN 標籤選擇以下 EtherType：

- 0x88a8 - IEEE 802.1ad，Service Tag。
- 0x8100 - IEEE 802.1Q，Customer VLAN（常規 VLAN 標籤）。
- 0x9100 - 非官方標籤型別（很少使用）。

要正確配置網橋 VLAN 過濾，你必須理解網橋如何區分帶標籤和不帶標籤封包。如前所述，網橋會檢查 EtherType 是否與封包中的外層 VLAN 標籤匹配。例如，考慮以下封包：

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

假設我們設定了 **`ether-type=0x88a8`**，在這種情況下，上面的封包將被視為不帶標籤，因為網橋在查詢不同的 VLAN 標籤。現在考慮以下封包：

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

這次假設我們設定了 **`ether-type=0x8100`**。在這種情況下，上面的封包也會被視為不帶標籤，因為外層標籤使用的是 IEEE 802.1ad VLAN 標籤。相同的原則適用於其他與 VLAN 相關的功能，例如，`PVID` 屬性會在 Access 埠上新增新的 VLAN 標籤，而該 VLAN 標籤將使用 ether-type 中指定的 EtherType。

**SW1** 和 **SW2** 都使用相同的配置：

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

在此示例中，我們假設所有路由器都在傳遞使用常規/客戶 VLAN 標籤的流量。基於上述原則，交換器上的此類流量將被視為不帶標籤流量。交換器會使用 Service VLAN 標籤（外層 802.1ad 標籤）封裝此流量，而 **SW1** 和 **SW2** 之間的流量將被視為帶標籤。在流量到達目的地之前，交換器會解封裝外層標籤，並轉發原始的 802.1Q 帶標籤幀。請參見下面的封包示例：

![Service VLAN 802.1ad](/img/b77a2f1f9e4171e9.webp)802.1ad VLAN 封裝前後的封包示例

:::warning
適用於使用 IEEE 802.1Q 的常規 Trunk/Access 埠設定的所有原則也適用於 VLAN 隧道設定。請確保你使用網橋 VLAN 表和入方向過濾正確限制 VLAN 和封包型別。
:::

如果你希望從（比如說）**ether3** 到裝置建立管理訪問，並希望使用 **VLAN99**，那麼你會使用如下命令：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,ether3 vlan-ids=99
/interface/vlan
add interface=bridge1 name=VLAN99 use-service-tag=yes vlan-id=99
/ip/address
add address=192.168.99.2/24 interface=VLAN99
```

你可能注意到，唯一的區別是 VLAN 介面使用了 `use-service-tag=yes`；這會將 VLAN 介面設定為監聽 IEEE 802.1ad VLAN 標籤。這將要求你使用 IEEE 802.1ad VLAN 標籤來透過管理 VLAN 訪問裝置——在啟用網橋 VLAN 過濾時，你將無法使用常規 VLAN 標籤連線到裝置。ether-type 是全域性設定的，會影響所有網橋 VLAN 過濾功能。

:::danger
配備 Marvell-98DX3257 交換器晶片的裝置（例如 CRS354 系列）不支援在 1Gbps 乙太網介面上對其他 VLAN 型別（`0x88a8` 和 `0x9100`）進行 VLAN 過濾。
:::

### 標籤堆疊 {#tag-stacking}

在 VLAN 隧道設定中，我們新增的是不同於原 VLAN 標籤的新 VLAN 標籤，但實際上可以不顧封包內容而新增新的 VLAN 標籤。與常規 VLAN 隧道設定的區別在於，網橋不檢查封包是帶標籤還是不帶標籤；它假設在特定埠上接收到的所有封包都是不帶標籤封包，並且無論是否存在 VLAN 標籤都會新增新的 VLAN 標籤。這稱為 **標籤堆疊**，因為它會將 VLAN 標籤“堆疊”在前一個標籤之上，而不考慮 VLAN 標籤型別。對於不支援 IEEE 802.1ad 標準但仍希望將 VLAN 流量封裝到新 VLAN 中的網路來說，這是一種非常常見的設定。

將要新增的 VLAN 標籤取決於 `ether-type` 和 `PVID`。例如，如果你在某個埠上設定了 `ether-type=0x8100` 和 `PVID=200`，那麼網橋會在任何其他標籤（如果存在）之上新增一個新的 IEEE 802.1Q VLAN 標籤。相同的 VLAN 過濾原則仍然適用。你必須確定哪些埠將成為你的 Trunk 埠並將它們標記為帶標籤埠，確定你的 Access 埠並將它們新增為不帶標籤埠。

為了解釋標籤堆疊下 VLAN 打標籤和移除標籤如何工作，我們使用與之前相同的網路拓撲：

![Basic VLAN Switching 2](/img/02a6439c12aa7838.webp)

我們想要實現的是：無論 **ether2** 和 **ether3** 上接收到什麼，都會新增一個新的 VLAN 標籤，以封裝來自這些埠的流量。`Tag-stacking` 會強制新增新的 VLAN 標籤，因此我們可以使用此屬性來實現所需的設定。我們將使用與 Trunk/Access 埠設定相同的配置，但在 Access 埠上啟用 `tag-stacking`：

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
新增的 VLAN 標籤將使用指定的 `ether-type`。選定的 EtherType 也將用於 VLAN 過濾。只檢查外層標籤，但在啟用標籤堆疊的情況下，會跳過標籤檢查，並假定無論如何都必須新增新標籤。
:::

假設 **ether2** 和 **ether3** 後面的裝置正在傳送帶標籤的 **VLAN40** 流量。使用此配置，**所有**封包都會被新的 VLAN 標籤封裝，但你必須確保已將外層標籤中的 VLAN ID 新增到網橋 VLAN 表。**VLAN40** 不會新增到網橋 VLAN 表，因為它是內層標籤且不會被檢查；我們只關心外層標籤，根據埠不同，它要麼是 **VLAN20**，要麼是 **VLAN30**。

與其他設定類似，網橋 VLAN 表將用於確定是否需要移除 VLAN 標籤。例如，當 **ether1** 接收到帶標籤的 **VLAN20** 封包時，網橋會檢查 **ether2** 是否被允許承載 **VLAN20**，因此它準備透過 **ether2** 將其發出，但它還會檢查網橋 VLAN 表以確定是否應移除 VLAN 標籤；由於 **ether2** 被標記為不帶標籤埠，網橋會將這些封包從 **ether1** 轉發到 **ether2**，並移除 **VLAN20** VLAN 標籤。

從 Access 埠的角度來看，適用與 Trunk/Access 埠設定相同的原則。在 **ether2** 上接收到的所有封包都會獲得帶有 PVID 中指定 VLAN ID 的新 VLAN 標籤；在這種情況下，將新增帶有 **VLAN20** 的新 VLAN 標籤，並且此 VLAN 將受到 VLAN 過濾的約束。請參見下面的封包示例：

![Tag Stacking](/img/ef2698e5bd946e5c.webp)

標籤堆疊前後的封包示例
