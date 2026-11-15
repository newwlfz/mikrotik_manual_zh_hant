---
title: "文件更新 - 2026年11月3日"
date: 2026-11-03T00:00:00.000Z
slug: /changelog-2026-11-03
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

# 文件更新 - 2026年11月3日 {#documentation-updates---november-3-2026}

November 3, 2026

2026年11月3日文件變更摘要。

## 無線 {#wireless}

-   **[配置 EasyMesh](/docs/wireless/wifi/configuring-easymesh)**：Wi-Fi EasyMesh 的新指南，Wi-Fi EasyMesh 是 Wi-Fi Alliance 針對多 AP 網路的標準，可在 `wifi-qcom` 和 `wifi-qcom-ac` 上的 CLI 中使用。它解釋了控制器、代理和控制器兼代理角色以及前傳和回傳網路，然後逐步介紹控制器和代理配置、透過有線回傳或透過無線回傳使用 WPS 按鈕進行入網、`topology`、`bss` 和 `sta` 狀態表以及故障排除。[Wi-Fi](/docs/wireless/wifi#wifi-easymesh) 頁面連結到該指南，並將 `easymesh` 列為 `manager` 值。

## 橋接與交換 {#bridging--switching}

-   **[橋接與交換](/docs/bridging-and-switching#arp-inspection-and-ip-source-guard)**：IP Source Guard 會在不受信任的埠上阻止 MAC Telnet、MAC WinBox 和 MAC ping，因為這些封包攜帶源地址 `0.0.0.0`，且不匹配任何 DHCP snooping 繫結。新的警告和 `ip-source-guard` 描述說明了這一點，[MAC server](/docs/management-tools/mac-server) 頁面也提到了這一點。
-   **[L3 硬體解除安裝](/docs/bridging-and-switching/l3-hardware-offloading#crs3xx-switch-98dx3xxx-and-98dx2xxx-series)**：CRS3xx 98DX3xxx 和 98DX2xxx 章節將 VRRP 解除安裝列為這些交換器晶片缺少的功能之一，現在以警告形式顯示。

## 容器 {#containers}

-   **[Apps](/docs/containers/apps)**：`auto-update` 描述指出，自動更新會在裝置重啟時觸發。

**Tags:**

-   [文件變更日誌](/changelog/tags/changelog "文件更新的每日摘要")
