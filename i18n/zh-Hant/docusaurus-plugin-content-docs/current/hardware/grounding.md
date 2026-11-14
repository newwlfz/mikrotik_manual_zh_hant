---
sidebar_key: "hardware/grounding"
sidebar_position: 2
title: "接地"
sidebar_label: "接地"
description: "MikroTik RouterOS 裝置的接地要求強調正確安裝遮蔽電纜、避雷器和可靠的接地基礎設施，使用 2.5-4 mm² Cu 導線和耐腐蝕聯結器，包括 RouterBOARD 單元上的特定連線點。"
tags:
  - 'grounding'
source: https://manual.mikrotik.com/docs/hardware/grounding
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

遮蔽電纜安裝基礎設施（塔架和桅杆）以及天線和路由器本身都必須正確接地。必須在所有外部天線電纜上（靠近天線處或天線自身上）安裝避雷器，以防止裝置損壞和人身傷害。請注意，如果避雷器沒有正確接地，就不會有效。

接地時請使用 2.5-4 mm² 銅（AWG 11–13）導線和耐腐蝕聯結器。確保所使用的接地基礎設施完全有效（而不只是擺設，正如在某些安裝中所見）：

1. 對於遮蔽聯結器，請使用遮蔽電纜，因為它們具有更好的抗干擾能力。
2. 如果提供了 RouterBOARD 接地線連線點，則應將接地線連線到該連線點。然後，該導線應連線到塔架底部，確保連線符合接地標準。天線的接地線應連線在 RouterBOARD 室外機箱附近，並且可以與用於 RouterBOARD 的同一接地線連線。

## 遮蔽 RJ45 埠與非遮蔽 RJ45 埠 {#shielded-rj45-port-vs-unshielded-rj45-port}

### 帶遮蔽埠的裝置 {#device-with-shielded-ports}

![shielded.png](/img/48f8692224741bf1.webp)
![](/img/530cf2c71e14e527.png)

### 帶非遮蔽埠的裝置 {#device-with-unshielded-ports}

![unshielded.png](/img/7b2658fdb11cb76d.webp)

### 帶遮蔽聯結器的 PoE 注入器 {#poe-injector-with-shielded-connectors}

![poeinjector.png](/img/deaecaccb525b0c4.webp)

## RouterBOARD 接地線連線點 {#routerboard-grounding-wire-attachment-points}

![](/img/c43fbb0b3ab9927f.webp)

![screw1.png](/img/01c1bd7ce52982e8.webp)

![screw2.png](/img/0d587a5baaa43769.webp)

:::info
如果為 MikroTik 裝置供電，則不應使用正極連線到保護接地（PE）的供電裝置（PSE）。這可能導致短路，對您和您的裝置造成傷害。

:::
