---
sidebar_key: "hardware/try-before-rma"
sidebar_position: 12
title: "RMA 前試用"
sidebar_label: "RMA 前試用"
description: "一份面向 MikroTik 硬體的 RMA 前診斷檢查清單。在提交保修申請之前，先排除常見的電源、啟動、連線和 LTE 問題。"
tags:
  - 'hardware'
  - 'troubleshooting'
  - 'rma'
source: https://manual.mikrotik.com/docs/7.25/hardware/try-before-rma
captured_at: '2026-11-04T11:17:32+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

在提交裝置進行保修維修（RMA）之前，請先完成以下檢查。許多看似硬體問題的故障實際上是由電源、線纜、軟體版本或配置引起的 —— 無需寄回裝置即可解決。

## 電源與啟動 {#power-and-boot}

| 現象 | 可嘗試的操作 |
| :-- | :-- |
| 裝置無法開機 | 換用其他相容的電源和/或 PoE 注入器。 |
| 裝置無法啟動 | 載入備份 RouterBOOT：按住 **Reset** 按鈕，給裝置上電，並繼續按住 **Reset** 2–3 秒。如果裝置能夠啟動，請使用 `/system/routerboard/upgrade` 升級 bootloader。如果仍然失敗，請使用 [網路安裝](../getting-started/installation-and-upgrade/netinstall/index.md) 重新安裝。 |
| 裝置在負載下重啟 | 嘗試更換電源。將 RouterOS 升級到最新的 Stable 版本。使用 `/system/reset-configuration` 重設配置。 |
| 裝置在無負載時重啟 | 將 RouterOS 升級到最新的 Stable 版本。使用 `/system/reset-configuration` 重設配置。 |

## 乙太網與 SFP {#ethernet-and-sfp}

| 現象 | 可嘗試的操作 |
| :-- | :-- |
| 無法連線到裝置 | 嘗試其他埠 —— 你可能正在使用預設配置中的 WAN 埠。確認網線和埠沒有物理損壞。 |
| 無法進行 [網路安裝](../getting-started/installation-and-upgrade/netinstall/index.md) | 確保使用直連乙太網、處於同一子網，並已停用防火牆。嘗試在 PC 與裝置之間接入一臺交換器。詳情請參閱 [Netinstall 指南](../getting-started/installation-and-upgrade/netinstall/netinstall-windows.md)。 |
| 乙太網埠無法建立鏈路 | 嘗試更換網線。如果使用 PoE-in 供電，請嘗試更換 PoE 注入器。 |
| SFP / SFP+ / QSFP 埠無法建立鏈路或吞吐量低 | 確保鏈路兩端相容。使用正確的光纖型別（單模或多模）。確認所用 SFP 模組受支援。 |

## LTE {#lte}

| 現象 | 可嘗試的操作 |
| :-- | :-- |
| 無法識別 SIM 卡 | 嘗試更換 SIM 卡。檢查卡片方向，並確保其已完全插入或卡入插槽。 |
| LTE 無法連線 | 確認 APN 正確。查閱服務提供商的文件以獲取所需的 APN 值。 |
| LTE 已連線但無資料傳輸 | 確認 APN 正確。確保路由和防火牆規則允許流量透過。 |
| 缺少 LTE 介面 | 確認裝置為 LTE Kit 型號，且調變解調器已實際安裝。 |
| 無法識別 LTE 調變解調器 | 安裝最新的 RouterOS Stable 版本。 |

## 其他 {#other}

| 現象 | 可嘗試的操作 |
| :-- | :-- |
| LED 不亮 | 安裝最新的 RouterOS Stable 版本並應用預設配置。 |
| 外殼彎曲或損壞 | 檢查包裝是否有損壞。運輸損壞應向承運公司報備。 |

:::info
如果上述步驟均未能解決問題，請聯絡 [MikroTik 支援](https://mikrotik.com/support)，並提供問題描述和[支援輸出檔案（`supout.rif`）](../getting-started/supout-rif.md)。
:::
