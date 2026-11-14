---
sidebar_key: "getting-started/software-specifications/feature-support-based-on-architecture"
sidebar_position: 1
title: "基於架構的功能支援"
sidebar_label: "基於架構的功能支援"
description: "本頁面概述了 MikroTik RouterOS 各架構之間在功能支援上的差異，列出了對於 ARM、MIPS 和 PPC 等每個平臺，哪些功能不受支援或為獨佔可用。頁面還提供了有關 WiFi、L3 offloading、PTP 以及交換晶片能力的其他資源參考。"
tags:
  - 'arm'
  - 'mips'
  - 'x86'
source: https://manual.mikrotik.com/docs/7.24/getting-started/software-specifications/feature-support-based-on-architecture
captured_at: '2026-11-04T11:29:04+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 按架構劃分的功能支援 {#feature-support-by-architecture}

大多數功能支援情況在所有裝置架構上保持一致，僅有少數例外。下表說明了每種架構不支援或專屬支援的功能：

| 架構 | 不支援 | 專屬支援 |
| :-- | :-- | :-- |
| **ARM (ARM32)** | — | ZeroTier, Container, BTH |
| **ARM64** | — | ZeroTier, Container, BTH |
| **MIPSBE** | ZeroTier, Dude Server | — |
| **MMIPS** | ZeroTier | — |
| **SMIPS** | ZeroTier, DOT1X, BGP, MPLS, PIMSM, Dude Server, User Manager, Reverse Proxy | — |
| **TILE** | ZeroTier | BTH |
| **PPC** | ZeroTier, Dude Server | — |
| **x86 PC** | ZeroTier, Cloud | Container |
| **CHR（雲託管路由器）** | — | 容器 |

除功能差異外，硬體能力也因裝置型號而異。有關更多資訊，請參閱以下資源：

- **WiFi** — 面向 802.11ax 裝置及受支援的舊裝置的新驅動實現
- **L3 硬體解除安裝** — 裝置支援詳情
- **PTP (Precision Time Protocol)** — 概述與配置
- **交換晶片功能** — 能力與限制
