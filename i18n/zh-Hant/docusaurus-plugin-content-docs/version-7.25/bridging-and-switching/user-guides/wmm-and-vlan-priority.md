---
sidebar_key: "bridging-and-switching/user-guides/wmm-and-vlan-priority"
sidebar_position: 9
title: "WMM 與 VLAN 優先順序"
sidebar_label: "WMM 與 VLAN 優先順序"
description: "本頁說明 MikroTik RouterOS 如何為 QoS 實現 WMM（Wi-Fi MultiMedia）和 VLAN 優先順序，詳細介紹了流量如何劃分為接入類別（background、best effort、video、voice）、VLAN 優先順序的處理方式，以及使用 IP firewall mangle 規則或 bridge filter 設定封包優先順序的方法。"
tags:
  - 'wmm'
  - 'vlan-priority'
  - 'qos'
source: https://manual.mikrotik.com/docs/7.25/bridging-and-switching/user-guides/wmm-and-vlan-priority
captured_at: '2026-11-04T11:14:44+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## WMM 工作原理 {#how-wmm-works}

---

WMM 透過將流量劃分為 4 個接入類別來工作：background、best effort、video、voice。QoS 策略（對不同接入類別的不同處理）應用於傳送的封包，因此傳送裝置會對不同封包進行不同處理，例如 AP 無法控制用戶端如何傳送封包，用戶端也無法控制 AP 如何傳送封包。

Mikrotik AP 和用戶端根據分配給封包的優先順序對封包進行分類，如下表所示（依據 WMM 規範）：1,2 - background；0,3 - best effort；4,5 - video；6,7 - voice。

要能夠使用多個 WMM 接入類別，而不僅僅是預設優先順序為 0 的所有封包所在的 best effort，就必須為這些封包設定優先順序。預設情況下，路由器內部的所有封包（傳入的以及本地生成的）優先順序均為 0。

封包的“更好”接入類別並不一定意味著它會在所有其他具有“更差”接入類別的封包之前透過空口傳送。WMM 透過為每個接入類別使用不同設定執行 DCF 介質訪問方法（EDCF）來工作，這意味著“更好”的接入類別有更高的機率獲得介質訪問權——啟用 WMM 的站點可以被視為 4 個站點，每個接入類別一個；當所有站點都在競爭介質時，具有“更好”接入類別的站點使用使其更有可能獲得傳輸機會的設定（透過使用更短的退避超時）。詳細資訊可參閱 802.11e 和 WMM 規範。

:::info
可以使用 `wmm-support` 設定啟用 WMM 支援。它僅適用於 B 和 G 頻段。其他頻段無論此設定如何都會啟用該支援。
:::

## VLAN 優先順序工作原理 {#how-vlan-priority-works}

---

VLAN 優先順序是 VLAN 標記頭內稱為優先順序程式碼點 (PCP) 的 3 位欄位，取值範圍為 0 到 7。它用於在網橋和交換器上實現 QoS。MikroTik 裝置預設傳送優先順序為 0 的 VLAN 封包（本地生成或封裝的）。RouterOS 網橋會原樣轉發 VLAN 標記封包，這意味著收到的具有特定 VLAN 優先順序的 VLAN 標記封包將以相同的 VLAN 優先順序離開網橋。唯一的例外是網橋去除封包的標記；在這種情況下，由於缺少 VLAN 頭，VLAN 優先順序不會被保留。

更多詳細資訊可參閱 IEEE 802.1p 規範。

## 如何設定優先順序 {#how-to-set-priority}

---

可以使用 IP 防火牆 mangle 規則或網橋 filter/nat 規則中的 `action=set-priority` 來設定封包優先順序。可以將優先順序設定為特定值，或使用 `from-ingress` 設定從入口優先順序獲取。入口優先順序是在傳入封包上檢測到的優先順序值（如果可用）。目前，入口優先順序有 2 個來源：VLAN 頭中的優先順序，以及透過無線介面接收到的 WMM 封包中的優先順序。對於所有其他封包，入口優先順序為 0。

請注意，入口優先順序值不會自動複製到 IP mangle 的 `priority` 值。需要設定正確的規則才能做到這一點。

有 2 種控制優先順序的方式：使用帶有特定匹配器（協定、地址等）的規則分配優先順序，或從入口優先順序設定。兩種方式都需要設定正確的規則。

這實質上意味著，如果無法或不想透過規則對封包進行分類，則網路配置必須使路由器能夠從傳入幀中提取入口優先順序。請記住，目前有 2 個來源：封包中的 VLAN 標記和接收到的 WMM 封包。

:::info
不要將佇列的優先順序與分配給封包的優先順序混為一談。佇列的優先順序單獨工作，指定佇列的“重要性”，並且僅在特定佇列設定中才有意義。將封包優先順序視為由規則附加到封包上的某種標記。另請注意，此標記目前僅用於透過啟用了 WMM 的鏈路發出的傳出封包，以及傳送 VLAN 標記封包時（無論該封包是在本地打上標記還是透過網橋轉發）。
:::

### 基於特定匹配器設定 VLAN 或 WMM 優先順序 {#set-vlan-or-wmm-priority-based-on-specific-matchers}

可以基於 IP mangle 或網橋 filter/nat 規則中的特定匹配器來更改 VLAN 和 WMM 優先順序。在此示例中，所有傳出的 ICMP 封包都將使用 IP mangle 規則以 VLAN 或 WMM 優先順序傳送：

```ros
/ip/firewall/mangle
add action=set-priority chain=output new-priority=2 protocol=icmp
```

### 自定義優先順序對映 {#custom-priority-mapping}

有時需要將某些 VLAN 或 WMM 優先順序更改或清除為預設值。我們可以使用 IP mangle 或網橋 firewall/nat 規則中的 `ingress-priority` 匹配器僅篩選所需的優先順序，並使用 `new-priority` 動作設定將其更改為其他值。例如，透過網橋轉發的優先順序為 5 的 VLAN 標記封包需要更改為 0。

```ros
/interface/bridge/filter
add action=set-priority chain=forward ingress-priority=5 new-priority=0
```

### 在網橋內將 WMM 優先順序轉換為 VLAN 優先順序 {#translating-wmm-priority-to-vlan-priority-inside-a-bridge}

當無線封包在接收時已設定 WMM 優先順序，RouterOS 網橋不會自動將其轉換到 VLAN 頭。這意味著接收到的具有 WMM 優先順序的無線封包在被網橋打上 VLAN 標記後，將以 VLAN 優先順序 0 轉發。但是，我們可以使用帶有 `from-ingress` 設定的網橋過濾規則來保留 VLAN 封包中的優先順序。例如，我們希望將無線封包透過 ether2 以 VLAN 10 頭轉發，並保留已設定的 WMM 優先順序（由無線用戶端設定）。

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=wlan2 pvid=10
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 vlan-ids=10

# 将 WMM 优先级转换为 VLAN 优先级
/interface/bridge/filter
add action=set-priority chain=forward new-priority=from-ingress out-interface=ether2
```

當無線封包由無線介面使用 `vlan-mode=use-tag` 和 `vlan-id` 設定打上 VLAN 標記時，情況相同。你仍然需要使用相同的網橋過濾規則將 WMM 優先順序轉換為 VLAN 優先順序：

```ros
/interface/wireless
set [ find default-name=wlan2 ] vlan-mode=use-tag vlan-id=10

/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=wlan2

 # 将 WMM 优先级转换为 VLAN 优先级
/interface/bridge/filter
add action=set-priority chain=forward new-priority=from-ingress out-interface=ether2
```

:::info
相同的原則也適用於相反方向。RouterOS 不會自動將 VLAN 優先順序轉換為 WMM 優先順序；可以使用 `new-priority=from-ingress` 規則執行此轉換。

RouterOS 網橋會原樣轉發 VLAN 標記封包，這意味著它們以進入時的相同優先順序離開網橋。唯一的例外發生在網橋去除封包標記時，因為移除 VLAN 頭時優先順序資訊會丟失。
:::

## 從 DSCP 獲取優先順序 {#priority-from-dscp}

---

設定 VLAN 或 WMM 優先順序的另一種方式是使用 IP 頭中的 DSCP 欄位。這隻能透過帶有 `new-priority=``from-dscp` 或 `new-priority=from-dscp-high-3-bits` 設定以及 `set-priority` 動作屬性的 IP 防火牆 mangle 規則來完成。請注意，IP 頭中的 DSCP 可以取值為 0-63，但優先順序僅為 0-7。使用 `new-priority=``from-dscp` 設定時，優先順序將是 DSCP 值的低 3 位；而使用 `new-priority=from-dscp-high-3-bits` 時，優先順序將是 DSCP 值的高 3 位。

請記住，只能訪問 IP 封包上的 DSCP，並且 IP 頭中的 DSCP 值應在某處設定（由用戶端裝置或 IP mangle 規則設定）。

最好在某個邊界路由器（例如，用於連線 Internet 的主路由器）上根據流量型別設定封包 IP 頭中的 DSCP 值，例如，將從 Internet 傳來的屬於 SIP 連線的封包的 DSCP 值設為 7，其餘設為 0。這樣，只需在一個地方標記封包。然後，網路中的所有 AP 都可以僅用一條規則根據 DSCP 值設定封包優先順序。

### 從 DSCP 設定 VLAN 或 WMM 優先順序 {#set-vlan-or-wmm-priority-from-dscp}

在此示例中，當封包透過無線介面路由時，AP 裝置將根據 DSCP 設定 WMM 優先順序。

```ros
/ip/firewall/mangle
add action=set-priority chain=forward new-priority=from-dscp out-interface=wlan2
```

:::info
當封包透過網橋轉發時，可以透過網橋設定下的 `use-ip-firewall=yes` 讓封包經過 IP mangle 規則。
:::

## 從優先順序獲取 DSCP {#dscp-from-priority}

---

類似地，如果接收到的封包包含 VLAN 或 WMM 優先順序，則可以設定 DSCP 值。這可以透過帶有 `new-dscp=from-priority` 或 `new-dscp=from-priority-to-high-3-bits` 設定以及 `change-dscp` 動作屬性的 IP mangle 規則來實現。請注意，VLAN 或 WMM 封包中的優先順序可以取值為 0-7，但 IP 頭中的 DSCP 為 0-63。使用 `new-dscp=from-priority` 設定時，優先順序值將設定 DSCP 的低 3 位；而使用 `new-dscp=from-priority-to-high-3-bits` 時，優先順序值將設定 DSCP 的高 3 位。

但是，此設定不能直接使用從接收到的 VLAN 或 WMM 封包中獲取的入口優先順序。你需要先使用 IP mangle 或網橋 filter/nat 規則設定優先順序（在這種情況下可以使用入口優先順序），然後才能應用 DSCP 規則。

### 從 VLAN 或 WMM 優先順序設定 DSCP {#set-dscp-from-vlan-or-wmm-priority}

在此示例中，當封包被路由時，AP 裝置需要根據 WMM 優先順序設定 DSCP。首先，新增一條設定優先順序的規則。DSCP 規則需要它來正確更改 DSCP 值。此規則可以從入口獲取優先順序。然後新增 DSCP 規則來更改其值。

```ros
/ip/firewall/mangle
add action=set-priority chain=prerouting in-interface=wlan2 new-priority=from-ingress
add action=change-dscp chain=prerouting in-interface=wlan2 new-dscp=from-priority
```

:::info
當封包透過網橋轉發時，可以透過網橋設定下的 `use-ip-firewall=yes` 讓封包經過 IP mangle 規則。
:::

## 組合優先順序設定與處理方案 {#combining-priority-setting-and-handling-solutions}

---

基於上述“構建塊”，可以透過組合不同的優先順序資訊承載方法來處理複雜網路和不同情況，以確保 QoS 並最佳化資源使用。以下是一些建議：

- 整個網路中的過濾規則越少越好（越快）。儘量僅在必要時對封包進行分類，最好在快速路由器上執行此操作，因為很可能需要連線跟蹤。
- 使用 DSCP 在您網路中轉發的 IP 封包中承載優先順序資訊。這樣，您可以在需要時使用它。
- 在必要時使用 VLAN，因為它們也會承載優先順序資訊。確保路徑上的乙太網網橋和交換器不會清除 VLAN 標記中的優先順序資訊。
- 請記住，QoS 不會提高鏈路吞吐量；它只是以不同方式處理不同封包，並且無線鏈路上的 WMM 流量會在空口上區別對待常規流量。

## 另請參閱 {#see-also}

---

- [RouterOS 中的封包流](../../firewall-and-quality-of-service/packet-flow-in-routeros.md)
- [IP mangle](../../firewall-and-quality-of-service/firewall/mangle.md)
- [網橋防火牆](../index.md#bridge-firewall)
