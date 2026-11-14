---
sidebar_key: "firewall-and-quality-of-service/firewall/layer7"
sidebar_position: 4
title: "Layer7"
sidebar_label: "Layer7"
description: "MikroTik RouterOS 中的 Layer7 協定檢測會搜尋網路流量流中的模式，收集初始封包資料以識別特定協定。它需要針對雙向流量進行仔細配置，並且資源消耗較大，同時警告不要過度使用。示例配置演示了在管理記憶體使用情況的同時匹配 RDP 和 Telnet 協定。"
tags:
  - 'layer7'
  - 'firewall'
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/firewall/layer7
captured_at: '2026-11-04T11:28:09+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Layer7-protocol 是一種在 ICMP/TCP/UDP 流中搜尋模式的方法。

:::warning
L7 匹配器非常消耗資源。僅將此功能用於非常特定的流量。不建議將 L7 匹配器用於通用流量，例如用於阻止網頁。這幾乎永遠不會正常工作，並且你的裝置會耗盡資源，試圖捕獲所有流量。請使用其他功能按 URL 阻止網頁。
:::

L7 匹配器會收集連線的前 **10 個數據包** 或連線的前 **2KB** 資料，並在收集到的資料中搜尋該模式。如果在收集到的資料中未找到該模式，匹配器會停止進一步檢查。已分配的記憶體會被釋放，並且該協定被視為 **unknown**。你應該考慮到，大量連線會顯著增加記憶體和 CPU 使用率。為避免這種情況，請新增常規防火牆匹配器，以減少反覆傳遞給 layer-7 過濾器的資料量。

另一個要求是 layer7 匹配器必須看到兩個方向的流量（傳入和傳出）。為滿足此要求，l7 規則應設定在 **forward** 鏈中。如果規則設定在 **input/prerouting** 鏈中，則同一規則 **必須** 也設定在 **output/postrouting** 鏈中，否則收集到的資料可能不完整，從而導致模式匹配不正確。

:::danger
Layer 7 匹配器不區分大小寫！
:::

相容 RouterOS 的 L7 模式示例可在 [l7-filter 專案頁面](https://l7-filter.sourceforge.net/Pattern-HOWTO) 上找到。

:::warning
在某些情況下，當無法執行 layer 7 正則表示式時，RouterOS 會記錄 *topic=firewall, warning*，並在訊息中附帶說明問題的錯誤訊息！
:::

## 示例 {#examples}

#### 簡單的 L7 使用示例 {#simple-l7-usage-example}

首先，將 Regexp 字串新增到 protocols 選單中，以定義你要查詢的字串。在此示例中，我們將使用一個模式來匹配 RDP 封包。

```ros
/ip/firewall/layer7-protocol
add name=rdp regexp="rdpdr.*cliprdr.*rdpsnd"
```

然後，在防火牆中使用已定義的協定。

```ros
/ip/firewall/filter

# 添加少量已知协议以减少内存占用
add action=accept chain=forward comment="" disabled=no port=80 protocol=tcp
add action=accept chain=forward comment="" disabled=no port=443 protocol=tcp

# 添加 l7 匹配器
add action=accept chain=forward comment="" disabled=no layer7-protocol=\
    rdp protocol=tcp
```

如你所見，在 l7 規則之前，我們添加了幾條常規規則來匹配已知流量，從而減少記憶體使用量。

#### input 鏈中的 L7 {#l7-in-the-input-chain}

在此示例中，我們將嘗試匹配連線到我們路由器的 telnet 協定。

```ros
/ip/firewall/layer7-protocol/add comment="" name=telnet regexp="^\\xff[\\xfb-\\xfe].\\xff[\\xfb-\\xfe].\\xff[\\xfb-\\xfe]"
```

請注意，我們需要兩個方向，這就是為什麼我們還需要在 output 鏈中設定能看到傳出封包的 l7 規則。

```ros
/ip/firewall/filter

add action=accept chain=input comment="" disabled=no layer7-protocol=telnet \
    protocol=tcp

add action=passthrough chain=output comment="" disabled=no layer7-protocol=telnet \
    protocol=tcp
```

#### YouTube 匹配器 {#youtube-matcher}

:::warning
當用戶已登入時，YouTube 將使用 HTTPS，這意味著 L7 將無法匹配此流量。只能匹配未加密的 HTTP。
:::

```ros
/ip/firewall/layer7-protocol
add name=youtube regexp="(GET \\/videoplayback\\\?|GET \\/crossdomain\\.xml)"
```
