---
sidebar_key: "wireless/abgn/index"
sidebar_position: 4
title: "802.11 a/b/g/n"
sidebar_label: "802.11 a/b/g/n"
description: "MikroTik 802.11 a/b/g/n 裝置使用由 wireless package 提供的傳統 `/interface/wireless` 選單。本節涵蓋無線介面、MikroTik 專有協定（Nstreme、Nv2）、HWMP+ mesh、interworking profiles、spectral scan、`/caps-man` CAPsMAN 控制器以及相關案例研究。"
tags:
  - 'wireless'
  - '802-11abgn'
  - 'nstreme'
source: https://manual.mikrotik.com/docs/7.24/wireless/abgn
captured_at: '2026-11-04T11:35:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節涵蓋 MikroTik **802.11 a/b/g/n** 裝置（以及任何執行 `wireless` 軟體包的 802.11ac 裝置），透過 **`/interface/wireless`** 選單（即 **`wireless`** 驅動程式包）進行配置——這是基於 MIPS 的裝置上唯一可用的選項。

該選單也是 MikroTik 專有的、面向吞吐量的功能所在之處——**Nstreme** 和 **Nv2**（TDMA）、**WDS** 以及 **HWMP+ mesh**——此外還有原有的 **[CAPsMAN](./capsman/ap-controller-capsman.md)**（`/caps-man`）控制器。

:::info
部分 802.11ac 裝置可以透過 `wifi-qcom-ac` 軟體包改用新的 `/interface/wifi` 選單——請參閱 [Wi-Fi 5 (802.11ac)](../wifi-ac/index.md) 進行選擇。WPA3 和快速漫遊只能透過新選單使用。
:::

<DocCardList />
