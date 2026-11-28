---
title: "基本 VLAN 交換"
description: "本頁提供 MikroTik RouterOS 基本 VLAN 交換設定的概觀，涵蓋搭載 Marvell Prestera 與 RTL8367/CRS 系列交換晶片的設備設定，包括硬體卸載 VLAN 過濾與埠設定範例。"
tags:
  - 'vlan'
  - 'switch-chip'
  - 'bridging'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/basic-vlan-switching
captured_at: '2026-11-28T10:19:39.818Z'
pagination_prev: "bridging-and-switching/user-guides"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

---

許多 MikroTik 設備內建交換器晶片，支援硬體層級的 VLAN 交換。只要採用適當的設定方式，即可在使用 VLAN 時達到線速效能。由於設定方式會因不同型號而異，本指南著重於在不同設備上使用正確的設定，建立基本的 trunk/access 埠，並從 trunk 埠提供管理埠，以達到最佳效能並充分運用可用的硬體元件。

![Basic VLAN Switching](/img/13be983760d55ff0.webp)

## 搭載 Marvell Prestera 交換器與 RTL8367、88E6393X、88E6191X、88E6190、MT7621、MT7531 及 EN7523 交換器晶片的 MikroTik 設備 {#mikrotik-devices-with-marvell-prestera-switch-and-rtl8367-88e6393x-88e6191x-88e6190-mt7621-mt7531-and-en7523-switch-chips}

---

```ros
/interface/bridge
add name=bridge1 frame-types=admit-only-vlan-tagged
/interface/bridge/port
add bridge=bridge1 interface=ether1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether2 pvid=20 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether3 pvid=30 frame-types=admit-only-untagged-and-priority-tagged
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 vlan-ids=20
add bridge=bridge1 tagged=ether1 vlan-ids=30
add bridge=bridge1 tagged=ether1,bridge1 vlan-ids=99
/interface/vlan
add interface=bridge1 vlan-id=99 name=MGMT
/ip/address
add address=192.168.99.1/24 interface=MGMT
/interface/bridge
set bridge1 vlan-filtering=yes
```

更詳細的範例請參閱[這裡](/docs/bridging-and-switching#bridge-vlan-filtering)。

:::info
RTL8367、88E6393X、88E6191X、88E6190、MT7621、MT7531 與 EN7523 交換器晶片可從 RouterOS v7 開始使用硬體卸載的 VLAN 過濾。
:::

:::warning
`frame-types` 設為 `admit-all` 或 `admit-only-untagged-and-priority-tagged` 的 Bridge 埠，會自動新增為 `pvid` VLAN 的未標記埠。
:::

## CRS1xx/CRS2xx 系列交換器 {#crs1xxcrs2xx-series-switches}

---

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
/interface/ethernet/switch/ingress-vlan-translation
add ports=ether2 customer-vid=0 new-customer-vid=20
add ports=ether3 customer-vid=0 new-customer-vid=30
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether1 vlan-id=20
add tagged-ports=ether1 vlan-id=30
add tagged-ports=ether1,switch1-cpu vlan-id=99
/interface/ethernet/switch/vlan
add ports=ether1,ether2 vlan-id=20
add ports=ether1,ether3 vlan-id=30
add ports=ether1,switch1-cpu vlan-id=99
/interface/vlan
add interface=bridge1 vlan-id=99 name=MGMT
/ip/address
add address=192.168.99.1/24 interface=MGMT
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether1,ether2,ether3
```

更詳細的範例請參閱[這裡](/docs/bridging-and-switching/user-guides/crs1xx-2xx-series-switches-examples#vlan)。

## 其他內建交換器晶片的設備 {#other-devices-with-a-built-in-switch-chip}

---

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
/interface/ethernet/switch/vlan
add ports=ether1,ether2 switch=switch1 vlan-id=20
add ports=ether1,ether3 switch=switch1 vlan-id=30
add ports=ether1,switch1-cpu switch=switch1 vlan-id=99
/interface/vlan
add interface=bridge1 vlan-id=99 name=MGMT
/ip/address
add address=192.168.99.1/24 interface=MGMT
/interface/ethernet/switch/port
set ether1 vlan-mode=secure vlan-header=add-if-missing
set ether2 vlan-mode=secure vlan-header=always-strip default-vlan-id=20
set ether3 vlan-mode=secure vlan-header=always-strip default-vlan-id=30
set switch1-cpu vlan-header=leave-as-is vlan-mode=secure
```

更詳細的範例請參閱[這裡](/docs/bridging-and-switching/switch-chip-features#setup-examples)。

:::info 適用範圍
此設定適用於 RouterBOARD 系列設備（RB4xx、RB9xx、RB2011、RB3011、hAP、hEX、cAP 等）。

並非所有具備交換器晶片的設備都支援硬體層級的 VLAN 交換。如果設備支援 `VLAN table`，即可使用內建交換器晶片。請使用 `/interface/ethernet/switch/print` 或[相容性對照表](/docs/bridging-and-switching/switch-chip-features)檢查晶片能力。
:::

:::warning 硬體限制與設定規則

* **多個交換器晶片：** 在具備多個晶片的設備上（例如 RB2011、RB3011、RB1100），VLAN 流量只會在*同一*晶片上的埠之間進行硬體交換。將不同晶片上的埠橋接在一起，表示 VLAN 不會在硬體層級進行過濾。若要避開此限制，請在晶片之間連接實體線路，或使用 Bridge VLAN Filtering（這會停用硬體卸載）。
* **QCA8337 與 Atheros8327 晶片：** 必須保留預設的 `vlan-header=leave-as-is` 屬性。交換器晶片會使用 `default-vlan-id` 屬性（此屬性只應套用於 access/hybrid 埠），將未標記的 ingress 流量指派至 VLAN。
* **RSTP 衝突：** 橋接介面預設使用 `protocol-mode=rstp`。在某些設備上，這會停用硬體卸載。請檢查 [Bridge Hardware Offloading](/docs/bridging-and-switching#bridge-hardware-offloading) 一節，以取得支援的功能。
:::

## 其他沒有內建交換器晶片的設備 {#other-devices-without-a-built-in-switch-chip}

---

可以使用 CPU 進行 VLAN 過濾；有多種做法，但強烈建議使用 bridge VLAN filtering。

```ros
/interface/bridge
add name=bridge1 frame-types=admit-only-vlan-tagged
/interface/bridge/port
add bridge=bridge1 interface=ether1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether2 pvid=20 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether3 pvid=30 frame-types=admit-only-untagged-and-priority-tagged
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 vlan-ids=20
add bridge=bridge1 tagged=ether1 vlan-ids=30
add bridge=bridge1 tagged=ether1,bridge1 vlan-ids=99
/interface/vlan
add interface=bridge1 vlan-id=99 name=MGMT
/ip/address
add address=192.168.99.1/24 interface=MGMT
/interface/bridge
set bridge1 vlan-filtering=yes
```

更詳細的範例請參閱[這裡](/docs/bridging-and-switching#bridge-vlan-filtering)。
