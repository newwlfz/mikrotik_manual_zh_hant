---
title: "WMM 與 VLAN 優先順序"
description: "本頁說明 MikroTik RouterOS 如何實作 WMM（Wi-Fi MultiMedia）與 VLAN priority 以進行 QoS，並詳細說明流量如何分類為 access categories（background、best effort、video、voice）、VLAN priority 的處理方式，以及使用 IP firewall mangle 規則或 bridge filters 設定封包優先順序的方法。"
tags:
  - 'wmm'
  - 'vlan-priority'
  - 'qos'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/wmm-and-vlan-priority
captured_at: '2026-11-28T10:19:39.818Z'
pagination_next: "network-management"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

## WMM 的運作方式 {#how-wmm-works}

---

WMM 會將流量劃分為 4 個存取類別：background、best effort、video、voice。QoS 政策（對存取類別採取不同的處理方式）會套用至傳送的封包，因此傳送設備會以不同方式處理不同封包，例如 AP 無法控制用戶端如何傳送封包，用戶端也無法控制 AP 如何傳送封包。

MikroTik AP 與用戶端會根據指派給封包的優先順序進行分類，依據下表（根據 WMM 規格）：1,2 - background；0,3 - best effort；4,5 - video；6,7 - voice。

若要使用多個 WMM 存取類別，而不只是讓所有預設優先順序為 0 的封包都進入 best effort，必須為這些封包設定優先順序。預設情況下，路由器內的所有封包（傳入與本機產生）優先順序皆為 0。

封包的「較佳」存取類別不一定代表它會在所有具有「較差」存取類別的封包之前透過無線方式傳送。WMM 的運作方式是針對每個存取類別使用不同設定執行 DCF 媒介存取方法（EDCF），這表示「較佳」存取類別有較高的機會取得媒介存取權，啟用 WMM 的工作站可視為 4 個工作站，每個存取類別各一個，而具有「較佳」存取類別的工作站會使用讓它們更容易取得傳送機會的設定（當所有工作站都在競爭媒介時，使用較短的 backoff timeout）。詳細內容可參考 802.11e 與 WMM 規格。

:::info
可使用 `wmm-support` 設定啟用 WMM 支援。此設定僅適用於 B 與 G 頻段。其他頻段不論此設定為何，都會啟用 WMM。
:::

## VLAN 優先順序的運作方式 {#how-vlan-priority-works}

---

VLAN 優先順序是 VLAN 標記標頭中名為 Priority Code Point（PCP）的 3 位元欄位，值介於 0 與 7 之間。它用於在橋接器與交換器上實作 QoS。MikroTik 設備預設會傳送優先順序為 0 的 VLAN 封包（本機產生或封裝）。RouterOS 橋接器會原樣轉送 VLAN 標記封包，這表示具有特定 VLAN 優先順序的傳入 VLAN 標記封包，會以相同的 VLAN 優先順序離開橋接器。唯一的例外是橋接器移除封包的 VLAN 標記；在此情況下，由於缺少 VLAN 標頭，VLAN 優先順序不會保留。

更多細節可參考 IEEE 802.1p 規格。

## 如何設定優先順序 {#how-to-set-priority}

---

封包的優先順序可以使用 IP firewall mangle 規則或 bridge filter/nat 規則中的 `action=set-priority` 來設定。優先順序可以設為特定值，或使用 `from-ingress` 設定從入口優先順序取得。入口優先順序是傳入封包上偵測到的優先順序值（若有的話）。目前入口優先順序有 2 個來源：VLAN 標頭中的優先順序，以及透過無線介面接收的 WMM 封包中的優先順序。對於所有其他封包，入口優先順序為 0。

請注意，入口優先順序值不會自動複製到 IP mangle 的 `priority` 值。必須設定正確的規則來執行此動作。

控制優先順序有 2 種方式：使用具有特定比對條件（協定、位址等）的規則指派優先順序，或從入口優先順序設定。兩種方式都需要設定正確的規則。

這基本上表示，如果無法或不希望依規則分類封包，則網路設定必須讓路由器能從傳入訊框擷取入口優先順序。請記得目前有 2 個來源：封包中的 VLAN 標籤，以及接收到的 WMM 封包。

:::info
請勿將佇列的優先順序與指派給封包的優先順序混為一談。佇列優先順序獨立運作，用於指定佇列的「重要性」，且僅在特定佇列設定中具有意義。可以將封包優先順序視為由規則附加到封包上的某種標記。另請注意，此標記目前僅用於透過啟用 WMM 的鏈路傳送的傳出封包，以及傳送 VLAN 標記封包時（不論該封包是在本機標記或橋接）。
:::

### 根據特定比對條件設定 VLAN 或 WMM 優先順序 {#set-vlan-or-wmm-priority-based-on-specific-matchers}

可以根據 IP mangle 或 bridge filter/nat 規則中的特定比對條件，變更 VLAN 與 WMM 優先權。在此範例中，所有傳出的 ICMP 封包都會透過 IP mangle 規則，以 VLAN 或 WMM 優先權傳送：

```ros
/ip/firewall/mangle
add action=set-priority chain=output new-priority=2 protocol=icmp
```

### 自訂優先權對應 {#custom-priority-mapping}

有時需要變更特定 VLAN 或 WMM 優先權，或將其清除為預設值。我們可以在 IP mangle 或 bridge firewall/nat 規則中使用 `ingress-priority` 比對條件，只篩選所需的優先權，再透過 `new-priority` 動作設定變更為不同值。例如，透過橋接器轉送且優先權為 5 的 VLAN 標記封包，需要變更為 0。

```ros
/interface/bridge/filter
add action=set-priority chain=forward ingress-priority=5 new-priority=0
```

### 在橋接器內將 WMM 優先權轉換為 VLAN 優先權 {#translating-wmm-priority-to-vlan-priority-inside-a-bridge}

當接收到已設定 WMM 優先權的無線封包時，RouterOS 橋接器不會自動將其轉換為 VLAN 標頭。這表示，接收到具有 WMM 優先權的無線封包，若由橋接器加上 VLAN 標記，轉送時 VLAN 優先權會是 0。不過，我們可以使用具有 `from-ingress` 設定的 bridge filter 規則，在 VLAN 封包中保留優先權。例如，我們希望透過 ether2 轉送無線封包，並加上 VLAN 10 標頭，同時保留已設定的 WMM 優先權（由無線用戶端設定）。

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=wlan2 pvid=10
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 vlan-ids=10

# translates WMM priority to VLAN priority 
/interface/bridge/filter
add action=set-priority chain=forward new-priority=from-ingress out-interface=ether2
```

當無線介面使用 `vlan-mode=use-tag` 與 `vlan-id` 設定為無線封包加上 VLAN 標記時，也適用相同的情況。你仍然需要使用相同的 bridge filter 規則，將 WMM 優先權轉換為 VLAN 優先權：

```ros
/interface/wireless
set [ find default-name=wlan2 ] vlan-mode=use-tag vlan-id=10

/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=wlan2

 # translates WMM priority to VLAN priority 
/interface/bridge/filter
add action=set-priority chain=forward new-priority=from-ingress out-interface=ether2
```

:::info
相同的原理也適用於反向情況。RouterOS 不會自動將 VLAN 優先權轉換為 WMM 優先權；你可以使用 `new-priority=from-ingress` 規則來執行這項轉換。

RouterOS 橋接器會原樣轉送具有 VLAN 標記的封包，也就是封包離開橋接器時，會保有進入時的相同優先權。唯一的例外是橋接器移除封包的 VLAN 標記時，因為移除 VLAN 標頭後，優先權資訊也會遺失。
:::

## 從 DSCP 取得優先權 {#priority-from-dscp}

---

另一種設定 VLAN 或 WMM 優先順序的方式，是使用 IP 標頭中的 DSCP 欄位。這只能透過 IP 防火牆 mangle 規則搭配 `new-priority=``from-dscp` 或 `new-priority=from-dscp-high-3-bits` 設定，以及 `set-priority` 動作屬性來完成。請注意，IP 標頭中的 DSCP 值可以是 0-63，但優先順序只有 0-7。使用 `new-priority=``from-dscp` 設定時，優先順序會是 DSCP 值的低 3 位元；但使用 `new-priority=from-dscp-high-3-bits` 時，優先順序會是 DSCP 值的高 3 位元。

請記住，DSCP 只能在 IP 封包上存取，且 IP 標頭中的 DSCP 值應在某處設定（由用戶端設備或 IP mangle 規則設定）。

最好在某些邊界路由器（例如，用於連線至網際網路的主要路由器）上，根據流量類型設定封包 IP 標頭中的 DSCP 值，例如，將來自網際網路且屬於 SIP 連線的封包 DSCP 值設為 7，其餘設為 0。如此一來，封包只需要在一個地方標記。然後網路中的所有 AP 都可以只用一條規則，從 DSCP 值設定封包優先順序。

### 從 DSCP 設定 VLAN 或 WMM 優先順序 {#set-vlan-or-wmm-priority-from-dscp}

在此範例中，當封包透過無線介面路由時，AP 設備會從 DSCP 設定 WMM 優先順序。

```ros
/ip/firewall/mangle
add action=set-priority chain=forward new-priority=from-dscp out-interface=wlan2
```

:::info
當封包透過 bridge 轉送時，可以在 bridge 設定中使用 `use-ip-firewall=yes`，讓封包通過 IP mangle 規則。
:::

## 從優先順序產生 DSCP {#dscp-from-priority}

---

同樣地，如果接收到的封包含有 VLAN 或 WMM 優先順序，也可以設定 DSCP 值。這可透過 IP mangle 規則搭配 `new-dscp=from-priority` 或 `new-dscp=from-priority-to-high-3-bits` 設定，以及 `change-dscp` 動作屬性來達成。請注意，VLAN 或 WMM 封包中的優先順序值可以是 0-7，但 IP 標頭中的 DSCP 是 0-63。使用 `new-dscp=from-priority` 設定時，優先順序值會設定 DSCP 的低 3 位元；但使用 `new-dscp=from-priority-to-high-3-bits` 時，優先順序值會設定 DSCP 的高 3 位元。

不過，此設定無法直接使用從接收到的 VLAN 或 WMM 封包取得的 ingress priority。你必須先使用 IP mangle 或 bridge filter/nat 規則設定優先順序（在此情況下可使用 ingress priority），然後才套用 DSCP 規則。

### 從 VLAN 或 WMM 優先順序設定 DSCP {#set-dscp-from-vlan-or-wmm-priority}

在此範例中，AP 設備需要在封包被路由時，從 WMM 優先順序設定 DSCP。首先，新增一條規則來設定優先順序。DSCP 規則需要這條規則才能正確變更 DSCP 值。這條規則可以從 ingress 取得優先順序。接著新增 DSCP 規則來變更其值。

```ros
/ip/firewall/mangle
add action=set-priority chain=prerouting in-interface=wlan2 new-priority=from-ingress
add action=change-dscp chain=prerouting in-interface=wlan2 new-dscp=from-priority
```

:::info
當封包透過橋接器轉送時，可以在 bridge 設定中使用 `use-ip-firewall=yes`，讓封包通過 IP mangle 規則。
:::

## 結合優先順序設定與處理方案 {#combining-priority-setting-and-handling-solutions}

---

複雜網路與不同情況可以透過結合不同的優先順序資訊傳遞方式來處理，以確保 QoS 並根據上述「建置區塊」最佳化資源使用。以下為幾項建議：

- 整個網路中的過濾規則越少越好（越快）。盡量只在必要時分類封包，並優先於快速路由器上執行，因為很可能會需要連線追蹤。
- 使用 DSCP 在你的網路中轉送的 IP 封包內攜帶優先順序資訊。如此一來，你可以在需要時使用該資訊。
- 在必要處使用 VLAN，因為 VLAN 也會攜帶優先順序資訊。請確認路徑上的 Ethernet bridge 與交換器不會清除 VLAN tag 中的優先順序資訊。
- 請記得 QoS 不會提升鏈路的吞吐量；它只是以不同方式處理不同封包，此外，無線鏈路上的 WMM 流量會在空氣中歧視一般流量。

## 另請參閱 {#see-also}

---

- [Packet Flow in RouterOS](/docs/firewall-and-quality-of-service/packet-flow-in-routeros)
- [IP mangle](/docs/firewall-and-quality-of-service/firewall/mangle)
- [Bridge firewall](/docs/bridging-and-switching#bridge-firewall)
