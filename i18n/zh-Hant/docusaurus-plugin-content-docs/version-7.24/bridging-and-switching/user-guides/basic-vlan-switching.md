---
sidebar_key: "bridging-and-switching/user-guides/basic-vlan-switching"
sidebar_position: 1
title: "基礎 VLAN 交換"
sidebar_label: "基礎 VLAN 交換"
description: "本頁概述了 MikroTik RouterOS 上基本的 VLAN 交換配置，涵蓋採用 Marvell Prestera 和 RTL8367/CRS 系列交換晶片的裝置的設定方法，包括硬體解除安裝的 VLAN 過濾以及埠配置示例。"
tags:
  - 'vlan'
  - 'switch-chip'
  - 'bridging'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/basic-vlan-switching
captured_at: '2026-11-04T11:27:19+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

---

許多 MikroTik 裝置帶有支援硬體級 VLAN 交換的內建交換晶片。只要採用適當的配置方法，這就能在使用 VLAN 時實現線速效能。由於不同型號的配置方法各不相同，本指南重點介紹在採用正確配置的不同裝置上，設定一個基本的 trunk/access 埠，並從 trunk 埠提供管理埠，以實現最佳效能並充分利用可用的硬體元件。

![Basic VLAN Switching](/img/13be983760d55ff0.webp)

## 配備 Marvell Prestera 交換晶片以及 RTL8367、88E6393X、88E6191X、88E6190、MT7621、MT7531 和 EN7523 交換晶片的 MikroTik 裝置 {#mikrotik-devices-with-marvell-prestera-switch-and-rtl8367-88e6393x-88e6191x-88e6190-mt7621-mt7531-and-en7523-switch-chips}

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

更詳細的示例可以在[這裡](../index.md#bridge-vlan-filtering)找到。

:::info
從 RouterOS v7 開始，RTL8367、88E6393X、88E6191X、88E6190、MT7621、MT7531 和 EN7523 交換晶片可以使用硬體解除安裝的 VLAN 過濾。
:::

:::warning
將 `frame-types` 設定為 `admit-all` 或 `admit-only-untagged-and-priority-tagged` 的網橋埠會自動新增為 `pvid` VLAN 的未標記埠。
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

更詳細的示例可以在[這裡](./crs1xx-2xx-series-switches-examples.md#vlan)找到。

## 其他帶有內建交換晶片的裝置 {#other-devices-with-a-built-in-switch-chip}

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

更詳細的示例可以在[這裡](../switch-chip-features.md#setup-examples)找到。

:::info 適用範圍
此配置適用於 RouterBOARD 系列裝置（RB4xx、RB9xx、RB2011、RB3011、hAP、hEX、cAP 等）。

並非所有帶有交換晶片的裝置都支援硬體級 VLAN 交換。如果裝置支援 `VLAN table`，則可以使用內建交換晶片。使用 `/interface/ethernet/switch/print` 或[相容性表](../switch-chip-features.md)檢查晶片的能力。
:::

:::warning 硬體限制與配置規則

* **多個交換晶片：** 在具有多個晶片的裝置上（例如 RB2011、RB3011、RB1100），VLAN 流量僅在*同一*晶片上的埠之間進行硬體交換。跨不同晶片橋接埠意味著 VLAN 不會在硬體級別進行過濾。要繞過此限制，可以在晶片之間連線物理網線，或使用 Bridge VLAN Filtering（這會停用硬體解除安裝）。
* **QCA8337 與 Atheros8327 晶片：** 必須保留預設的 `vlan-header=leave-as-is` 屬性。交換晶片使用 `default-vlan-id` 屬性（該屬性只應應用於 access/hybrid 埠）將未標記的入口流量分配到 VLAN。
* **RSTP 衝突：** 預設情況下，網橋介面使用 `protocol-mode=rstp`。在某些裝置上，這會停用硬體解除安裝。請檢視 [Bridge Hardware Offloading](../index.md#bridge-hardware-offloading) 部分了解支援的功能。
:::

## 其他沒有內建交換晶片的裝置 {#other-devices-without-a-built-in-switch-chip}

---

可以使用 CPU 進行 VLAN 過濾；有多種方法可以做到這一點，但強烈建議使用 bridge VLAN filtering。

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

更詳細的示例可以在[這裡](../index.md#bridge-vlan-filtering)找到。
