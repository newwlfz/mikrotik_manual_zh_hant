---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/flood-ping"
sidebar_position: 7
title: "泛洪 Ping"
sidebar_label: "泛洪 Ping"
description: "Flood ping 在一次執行中最多傳送 1000 個 ICMP echo 請求，並且只顯示彙總資訊：傳送的請求數、收到的回覆數，以及最短、平均和最長往返時間。它需要 traffic-gen 裝置模式功能。"
tags:
  - 'icmp'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/flood-ping
captured_at: '2026-11-04T11:15:16+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Flood ping 向一臺主機發送一串 ICMP 回顯請求，並且不像 [ping](./ping.md) 那樣為每個應答列印一行，而是隻顯示總計：傳送了多少請求、收到了多少應答，以及最短、平均和最長往返時間。可用它透過傳送大量請求來檢查鏈路的丟包情況，例如無線鏈路或 VPN 隧道。它支援 IPv4 和 IPv6 地址，在 SMIPS 架構的裝置上不可用。

Flood ping 會給鏈路和目標主機帶來負載，因此只在你自己管理的鏈路和主機上使用。

## 啟用 flood ping {#enable-flood-ping}

Flood ping 屬於 [裝置模式](../system-information-and-utilities/device-mode.md) 的 `traffic-gen` 功能，該功能在所有 device mode 下預設關閉。在未啟用該功能的路由器上，命令會失敗並提示 `failure: not allowed by device-mode`。要啟用它，請執行更新命令，並在路由器顯示的時間內，在路由器本機上透過按下 reset 或 mode 按鈕，或者關閉再開啟電源來完成確認。隨後路由器會重啟。[裝置模式](../system-information-and-utilities/device-mode.md) 頁面介紹了確認方式及其限制：

```ros
/system/device-mode/update traffic-gen=yes
```

## 測試鏈路丟包 {#test-a-link-for-packet-loss}

要向鏈路對端傳送 1000 個 `size=1400` 的請求：

```ros
/tool/flood-ping address=10.0.0.2 count=1000 size=1400
```

執行結束後，路由器會顯示總計：`sent` 和 `received` 請求數，以及往返時間 `min-rtt`、`avg-rtt` 和 `max-rtt`。`sent` 與 `received` 之間的差異就是丟包，可能發生在鏈路上或目標主機處：許多主機會限制其應答的 ICMP 請求數量，因此要針對你確定不會做此限制的裝置進行測試。要查詢路徑上的 MTU 問題，請改用帶 `do-not-fragment` 的 [ping](./ping.md#find-the-path-mtu)：flood ping 沒有此類選項。

對於 IPv6 主機，請提供 IPv6 地址：

```ros
/tool/flood-ping address=2001:db8::2 count=500
```

## 限制 {#limits}

- `count` - 每次執行最多 1000 個請求。
- `size` - 每個請求的大小，10 到 1500。
- `timeout` - 等待每個應答的時間，10 ms 到 5 s。
- `interval` - 請求之間的間隔，20 ms 到 5 s。

如需更多請求、更長的測試，或源地址、VRF 之類的選項，請使用帶 `count` 和 `interval` 的 [ping](./ping.md)。

有關所有引數，請參閱 [`/tool/flood-ping` CLI reference](../cli-reference/tool/flood-ping.md)。
