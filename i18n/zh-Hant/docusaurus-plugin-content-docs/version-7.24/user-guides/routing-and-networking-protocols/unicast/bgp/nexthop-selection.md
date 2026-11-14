---
sidebar_key: "routing-and-networking-protocols/unicast/bgp/nexthop-selection"
sidebar_position: 3
title: "下一跳選擇"
sidebar_label: "下一跳選擇"
description: "輸入和輸出時的 BGP 下一跳選擇過程。"
tags:
  - 'routing'
  - 'bgp'
slug: /user-guides/routing-and-networking-protocols/unicast/bgp/nexthop-selection
source: https://manual.mikrotik.com/docs/7.24/user-guides/routing-and-networking-protocols/unicast/bgp/nexthop-selection
captured_at: '2026-11-04T11:34:07+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 不會在 BGP 輸入上執行嚴格的下一跳檢查；而是依賴使用者建立的[過濾規則](../../../../cli-reference/routing/filter/rule.md)。

對輸入執行的操作：

- 從 BGP **NEXT_HOP** 屬性讀取下一跳。
- 對於多協定 NLRI，檢查下一跳是否具有有效長度：
  - 如果長度無效，則傳送 Update 錯誤通知並退出。
  - 儲存下一跳值。
  - 如果更新訊息中出現鏈路本地下一跳：
    - 確定連線介面。
    - 儲存鏈路本地地址和介面。
- 應用來自輸入過濾規則的下一跳動作。
- 將路由傳送到主 calc 程式，在該程式中確定下一跳可達性。

## BGP 輸出 {#bgp-output}

- 如果 [`nexthop-choice`](../../../../cli-reference/routing/bgp/connection.md#nexthop-choice) 不是 `force-self`，或者路由 AFI 不是 IPv4 或 IPv6：
  - 如果對端是路由反射器，或者 [`nexthop-choice`](../../../../cli-reference/routing/bgp/connection.md#nexthop-choice) 是 `propagate`，或者對端不是 eBGP：
    - 檢查下一跳 AFI，並嘗試設定出站鏈路本地下一跳。
    - 檢查下一跳 AFI，並嘗試設定出站下一跳。
  - 如果出站下一跳仍未設定，且 BGP 對端不是 multihop：
    - 遍歷可用的直連下一跳，並嘗試設定出站下一跳和 LL 下一跳。
  - 如果出站下一跳等於遠端 [`router-id`](../../../../cli-reference/routing/bgp/instance.md#router-id)，則取消設定出站下一跳。
  - 如果出站下一跳等於遠端對端地址，則取消設定出站下一跳。
  - 如果對端地址的介面不等於 LL 下一跳的介面，則取消設定出站 LL 下一跳。
  - 如果出站 LL 下一跳等於遠端對端地址，則取消設定出站 LL 下一跳。
- 如果出站下一跳仍未設定，則檢查 AFI 並設定對端的 local-address。
- 如果出站下一跳仍未設定，且路由 AFI 是 IPv6 或 L2VPN：
  - 如果對端的本地地址是 IPv4，則將出站下一跳設定為 IPv6 對映的對端本地地址。
