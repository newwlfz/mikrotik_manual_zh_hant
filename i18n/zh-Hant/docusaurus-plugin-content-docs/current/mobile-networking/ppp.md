---
sidebar_key: "mobile-networking/ppp"
sidebar_position: 5
title: "PPP"
sidebar_label: "PPP"
description: "RouterOS 中的 PPP 支援點對點協定通訊，用於傳輸多協定封包，包含 LCP 和 NCP 元件。它支援 PPP 用戶端和伺服器配置，並提供按需撥號設定以及相容調變解調器韌體升級等示例。"
tags:
  - 'ppp'
source: https://manual.mikrotik.com/docs/mobile-networking/ppp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#overview}

點對點協定（PPP）提供了一種在點對點鏈路上傳輸多協定封包的標準方法。RouterOS 中的 PPP 基於 [RFC 1661 標準。](https://tools.ietf.org/html/rfc1661)

## 簡介 {#introduction}

此時 PPP 的基本目的是透過資料鏈路層點對點鏈路傳輸三層封包。假定兩個對等體之間的封包按順序交付。

PPP 由三個主要元件組成：

1. 一種封裝多協定封包的方法。
2. 一種鏈路控制協定（LCP），用於建立、配置和測試資料鏈路連線。
3. 一組網路控制協定（NCP），用於建立和配置不同的網路層協定。

有關 RouterOS 中詳細的 PPP 封包處理，請參閱[封包流圖](../firewall-and-quality-of-service/packet-flow-in-routeros.md)。

### PPP 用戶端 {#ppp-client}

**子選單：** `/interface/ppp-client`

### PPP 用戶端示例 {#ppp-client-example}

以下示例展示如何使用 LTE 調變解調器暴露的序列埠新增用戶端。

```ros
/interface/ppp-client/add apn=yourapn dial-on-demand=no disabled=no port=usb2
```

對於持續連線，應將 dial-on-demand 設定為 'no'。

### PPP 服務端 {#ppp-server}

**子選單：** `/interface/ppp-server`

## KNOT RB924i-2nD-BT5&BG77 {#knot-rb924i-2nd-bt5bg77}

如果看到訊息“*A newer version of modem firmware is available!*”並且想要升級 BG77 調變解調器的韌體，請使用以下命令：

```routeros
/interface/ppp-client/firmware-upgrade [find] upgrade=yes
```
