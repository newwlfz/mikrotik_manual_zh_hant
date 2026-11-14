---
sidebar_key: "hardware/s-plus-rj10-general-guidance"
sidebar_position: 11
title: "S+RJ10 通用指南"
sidebar_label: "S+RJ10 通用指南"
description: "S+RJ10 是一款 MikroTik 6 速 RJ45 SFP+ 模組，可透過銅纜提供 10 Gbps 速率，並附有關於其在 MikroTik 裝置中使用方式的指導，包括在與光模組同時使用或在高密度 SFP+ 插槽中使用時防止過熱的推薦安裝位置。"
tags:
  - 's-rj10'
  - 'transceiver-cooling'
source: https://manual.mikrotik.com/docs/hardware/s-plus-rj10-general-guidance
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 概述 {#summary}

[MikroTik S+RJ10](https://mikrotik.com/product/s_rj10) 是一款獨特的 6 速 RJ-45 SFP+ 模組，基於 Marvell 88X3310P 收發器。它使用雙絞銅纜可提供高達 10 Gbps 的速度。當前所有帶有 SFP+ 插槽的 MikroTik 裝置均支援 S+RJ10 模組。本文為在具有被動散熱和主動散熱的 MikroTik 裝置中使用 S+RJ10 提供指導。

### 通用指導 {#general-guidance}

#### 產品規格 {#product-specification}

該收發器的平均功耗為 2.7 W（10GBASE-T，30 m 鏈路），與最大功耗為 0.8W 的 [S+85DLC03D](https://mikrotik.com/product/Splus85DLC03D) 光模組相比相對較高。工作溫度為 0 至 +70 C，但收發器本身可能升溫至 90 C。

#### S+RJ10 在裝置中的位置 {#srj10-positioning-in-devices}

由於工作溫度較高，建議在使用 S+RJ10 收發器時，在它們之間放置一個光收發器或未使用的 SFP+ 介面。請檢視收發器可支援距離的[比較表](../wired-connections/mikrotik-wired-interface-compatibility.md#srj10)。

如前所述，S+RJ10 比普通收發器發熱更嚴重，將它們並排放置可能導致過熱，尤其是在具有 4 個線性 SFP 插槽的裝置中。建議每隔一個介面放置一個 S+RJ10，並在它們之間保留一個光收發器或空埠。

![](/img/c4b6662ea4dfd009.webp)

即使使用帶有獨立 SFP+ 插槽的裝置（例如 CRS309-1G-8S+），仍然不建議將 S+RJ10 收發器並排放置。每隔一個介面使用 S+RJ10，以避免收發器過熱，過熱可能導致不可預測的行為。

![](/img/2d992e1b7e676ab7.webp)推薦的 S+RJ10 放置方式![](/img/a6b05df0baa08711.webp)不建議將收發器並排放置

帶有 4 個或 8 個一組 SFP+ 插槽的裝置也不例外。建議每個 4xSFP+ 插槽組使用一個 S+RJ10 收發器，並避免將它們並排放置。插入 S+RJ10 收發器後，至少保留一個垂直行空置（不含 S+RJ10）。

![](/img/ed806fb16ee9ffe7.webp)推薦的 S+RJ10 放置方式![](/img/2bbeed8af60d549a.webp)不建議將收發器並排放置

### 並排使用 S+RJ10 或搭配被動散熱裝置使用 {#using-the-srj10-side-by-side-or-with-passive-cooling-devices}

在某些情況下，可能無法採用推薦的收發器佈局。在兩個或更多 S+RJ10 收發器彼此相鄰插入，或在被動散熱裝置中使用這些模組的情況下，網路管理員必須確保提供額外散熱。應增加裝置周圍的氣流，或降低整體環境溫度，以使收發器溫度保持在推薦範圍內。
