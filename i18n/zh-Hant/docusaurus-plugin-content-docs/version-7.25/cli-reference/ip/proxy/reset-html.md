---
sidebar_key: "cli-reference/ip/proxy/reset-html"
sidebar_position: 11
title: "reset-html"
sidebar_label: 'reset-html'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/proxy/reset-html
captured_at: '2026-11-01T21:24:24+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy/reset-html {#ipproxyreset-html}
**型別：** 命令

將代理錯誤頁面的預設模板寫入路由器上的檔案 `webproxy/error.html`，並替換已被修改的副本。代理會根據此檔案構建其錯誤頁面（例如由 [`/ip/proxy/access`](./access/index.md) 拒絕的請求所對應的頁面），因此你可以編輯該檔案；代理會立即使用修改後的檔案。若該檔案不存在，代理則使用內建構建的同一頁面。該模板使用變數 `$(status)`、`$(url)`、`$(error)`、`$(admin)`（即 `cache-administrator` 設定）和 `$(signature)`，以及塊 `$(if error)` ... `$(endif)`。有關概述，請參閱 [Web 代理](../../../network-management/proxy/web-proxy.md)。
