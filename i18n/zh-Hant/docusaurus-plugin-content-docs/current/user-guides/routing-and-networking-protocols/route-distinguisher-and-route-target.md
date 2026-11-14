---
sidebar_key: "user-guides/routing-and-networking-protocols/route-distinguisher-and-route-target"
sidebar_position: 9
title: "路由區分符和路由目標"
sidebar_label: "路由區分符和路由目標"
description: "路由區分符（RD）為客戶地址新增唯一字首，以便區分不同的 VRF，而路由目標則控制各例項之間 BGP 路由資訊的交換。"
tags:
  - 'bgp'
  - 'routing'
  - 'vrf'
source: https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/route-distinguisher-and-route-target
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 路由區分符 {#route-distinguisher}

路由區分符是一個唯一字首，新增到客戶的目標地址，以區分否則可能看起來相同的通告。例如，重疊的 VRF 子網可以透過唯一的路由區分符來區分。

RD 是一個 64-bit（8-byte）整數，分為三部分：

- Type（始終為 2 bytes）。
- 管理員子欄位。
- 值或 service-provider 子欄位。

目前定義了三種格式型別。

| **2 位元組**   |            |              |
|:--|:--|:--|
| **Type 0**    | 2 位元組 ASN | 4 位元組值 |
| **Type 1**    | 4 位元組 IP  | 2 位元組值 |
| **Type 2**    | 4 位元組 ASN | 2 位元組值 |

## 路由目標 {#route-targets}

路由目標是一種 BGP 擴充套件社群，用於控制路由例項之間路由資訊的匯入和匯出。
