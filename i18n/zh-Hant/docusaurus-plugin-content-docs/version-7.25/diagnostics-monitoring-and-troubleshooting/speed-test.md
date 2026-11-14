---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/speed-test"
sidebar_position: 6
title: "速度測試"
sidebar_label: "速度測試"
description: "Speed test 在一次執行中，透過遠端路由器的 bandwidth test server，測量兩臺 MikroTik 路由器之間的 ping、jitter 以及雙向 TCP 和 UDP 吞吐量。"
tags:
  - 'speed-test'
  - 'bandwidth'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/speed-test
captured_at: '2026-11-04T11:15:33+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

速度測試用一條命令測量此路由器與另一臺 MikroTik 路由器之間的鏈路：先透過 ping 測量延遲和抖動，然後測量兩個方向上的 TCP 和 UDP 吞吐量。它會連線到另一臺路由器的頻寬測試伺服器，並在吞吐量結果旁顯示路由器的 CPU 負載。可用它檢查站點間鏈路、無線回傳或 VPN 隧道能提供多少效能。要測試單一協定或單一方向，或要設定封包大小和速度限制，請改用[頻寬測試](./bandwidth-test.md)。

## 先決條件 {#prerequisites}

- 頻寬測試伺服器執行在遠端路由器上。它預設啟用，並帶有 `authenticate=yes`（`/tool/bandwidth-server`）。
- 遠端路由器有一個用於測試的使用者，該使用者屬於具有 `test` 和 `winbox` 策略的組。預設的 `read` 和 `full` 組都具備這兩個策略。
- 防火牆允許測試透過：遠端路由器接受來自測試路由器的 ICMP（預設防火牆會接受）、TCP 埠 2000 和 UDP 埠 2000-65535，測試路由器接受來自遠端路由器的 UDP。
- [裝置模式](../system-information-and-utilities/device-mode.md) 在兩臺路由器上都允許 `bandwidth-test`。用 `/system/device-mode/print` 檢查（`bandwidth-test: yes`）。大多數隨 RouterOS 7.17 或更高版本出廠的路由器處於 `home` 或 `basic` 模式，這些模式會關閉它（CCR 和 1100 系列路由器處於 `advanced`）。啟用它需要物理接觸路由器。

要限制哪些路由器可以對某臺路由器執行測試，請設定其頻寬測試伺服器的 `allowed-addresses4` 和 `allowed-addresses6`。測試使用者的 `address` 設定不會限制頻寬測試登入。不要在網際網路可訪問的路由器上設定 `authenticate=no`。

## 測試到另一臺路由器的鏈路 {#test-the-link-to-another-router}

要檢查從路由器 A（192.168.88.1）到路由器 B（192.168.88.2）的鏈路能提供多少效能，請在路由器 B 上新增一個用於測試的使用者。僅具有 `test` 和 `winbox` 策略的組就足夠了：

```ros
/user/group/add name=speedtest policy=test,winbox
/user/add name=speedtest group=speedtest password=YourStrongPassword
```

在路由器 A 上執行測試。使用路由器 B 在你要測量的路徑上的地址：對於 VPN，使用路由器 B 的隧道地址。測試在整個持續時間內會佔滿鏈路，因此鏈路上的使用者會察覺到。`test-duration=5s` 讓測試的每個部分持續 5 秒，這對於快速檢查已經足夠。使用預設值時，整個測試大約需要一分鐘；在高延遲鏈路上，請使用預設值或更長的持續時間：

```ros
/tool/speed-test address=192.168.88.2 test-duration=5s \
    user=speedtest password=YourStrongPassword
```

路由器會在測試期間更新結果。測試結束時，它會顯示：

```ros
              status: done
      time-remaining: 0s
    ping-min-avg-max: 225us / 265us / 432us
  jitter-min-avg-max: 0s / 29us / 164us
                loss: 0% (0/100)
        tcp-download: 930Mbps local-cpu-load:71%
          tcp-upload: 932Mbps local-cpu-load:61% remote-cpu-load:79%
        udp-download: 924Mbps local-cpu-load:46% remote-cpu-load:52%
          udp-upload: 953Mbps local-cpu-load:56% remote-cpu-load:43%
```

當不再需要測試使用者時，請在路由器 B 上刪除該使用者及其組：

```ros
/user/remove speedtest
/user/group/remove speedtest
```

## 為透過網際網路進行的測試開放防火牆 {#open-the-firewall-for-a-test-over-the-internet}

當遠端路由器只能透過網際網路訪問，並且位於預設防火牆之後時，兩臺路由器都需要為測試新增規則。在此示例中，路由器 A（198.51.100.10）執行測試，路由器 B（203.0.113.20）是遠端路由器。

在路由器 B 上，接受來自路由器 A 的 TCP 埠 2000 和測試使用的 UDP 埠：

```ros
/ip/firewall/filter/add chain=input action=accept protocol=tcp \
    src-address=198.51.100.10 dst-port=2000 \
    comment="Speed test from router A" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
/ip/firewall/filter/add chain=input action=accept protocol=udp \
    src-address=198.51.100.10 dst-port=2000-65535 \
    comment="Speed test from router A" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

在路由器 A 上，接受來自路由器 B 的 UDP。沒有此規則，路由器 A 的預設防火牆會丟棄路由器 B 傳送的 UDP 流量，結果中就不會有 `udp-download` 行：

```ros
/ip/firewall/filter/add chain=input action=accept protocol=udp \
    src-address=203.0.113.20 comment="Speed test to router B" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

測試後，在路由器 B 上刪除規則：

```ros
/ip/firewall/filter/remove [find comment="Speed test from router A"]
```

在路由器 A 上：

```ros
/ip/firewall/filter/remove [find comment="Speed test to router B"]
```

## 解讀結果 {#read-the-results}

| 行 | 顯示內容 |
| :-- | :-- |
| `ping-min-avg-max` | ping 的最短、平均和最長往返時間。 |
| `jitter-min-avg-max` | ping 之間往返時間的變化：最小、平均和最大。 |
| `loss` | 丟失 ping 的百分比，然後是丟失和傳送的 ping 數：`(0/100)` 表示 100 個 ping 中沒有丟失。 |
| `tcp-download`, `udp-download` | 從遠端路由器到此路由器的吞吐量。 |
| `tcp-upload`, `udp-upload` | 從此路由器到遠端路由器的吞吐量。 |
| `local-cpu-load`, `remote-cpu-load` | 在該部分測試期間，此路由器和遠端路由器的 CPU 負載。`tcp-download` 僅顯示本地負載。 |

下載和上傳是從執行測試的路由器的角度看的。

ping 在吞吐量部分之前、在空閒鏈路上執行，因此它們不顯示負載下的延遲。

吞吐量是測試所有連線的總和：預設 20 個 TCP 連線（CPU 核心數超過 20 的路由器會更多），UDP 部分也使用多個流。單個連線可能獲得更少，例如在 bonding 或按連線負載均衡中，每個連線走一條路徑。

## 受 CPU 限制的結果 {#results-limited-by-the-cpu}

當測試期間路由器的 CPU 接近滿負載時，結果會以以下行開頭：

```text
;;; results can be limited by cpu, note that traffic generation/termination performance might not be representative of forwarding
;;; performance
```

生成和接收測試流量比轉發相同流量更消耗路由器的 CPU。出現該警告時，測試顯示的是作為流量源和目的地的路由器的限制。鏈路以及路由器僅轉發的流量可以承載更多。要將路由器或交換器作為被測裝置進行測量，請在另外兩臺路由器之間執行測試，讓這兩臺路由器分別位於裝置兩側，從而使測試流量經過該裝置。

在兩個站點之間，結果還取決於兩條網際網路連線：一個站點的上傳就是另一個站點的下載。透過 VPN 時，加密也會增加兩臺路由器的 CPU 負載。

## 故障排除 {#troubleshoot}

- 每條吞吐量行都出現 `authentication failed`：使用者名稱或密碼錯誤，測試使用者所在的組缺少 `test` 或 `winbox` 策略，或者未提供 `user`。沒有 `user` 時，命令不傳送使用者名稱，只有設定了 `authenticate=no` 的伺服器才會接受。ping 部分仍會執行，測試仍會耗費其完整時長。
- `loss: 100%`：遠端路由器不回應 ping。檢查地址以及到它的路徑。如果吞吐量行仍然出現，則說明路徑上或遠端路由器上過濾了 ICMP。
- 只出現 ping 結果，沒有吞吐量行：遠端路由器的頻寬測試伺服器已關閉，其防火牆丟棄 TCP 埠 2000，或者其 `allowed-addresses4` 或 `allowed-addresses6` 不包含此路由器。測試仍會執行完所有部分。
- 出現 TCP 行，但一條或兩條 UDP 行缺失：遠端路由器或此路由器的防火牆丟棄了測試的 UDP 流量。本頁的防火牆部分給出了兩臺路由器的規則。
- 命令失敗並提示 `not allowed by device-mode`：裝置模式在此路由器上關閉了 `bandwidth-test`。請參閱[裝置模式](../system-information-and-utilities/device-mode.md)。

## 技術細節 {#technical-details}

### 測試階段 {#test-phases}

測試按以下順序執行五個部分，並在 `status` 中顯示：`ping`、`tcp download`、`tcp upload`、`udp download` 和 `udp upload`，然後是 `done`。`test-duration` 設定每個部分的長度：預設 10 秒，至少 5 秒。路由器在各部分之間暫停約一秒，因此使用預設值的測試大約需要 55 秒。

### Ping 階段 {#ping-phase}

ping 部分發送 ICMP 回顯請求，每秒 20 個：使用預設 `test-duration` 時為 200 個 ping，使用 `test-duration=5s` 時為 100 個。

### 連線和埠 {#connections-and-ports}

TCP 部分使用 `connection-count` 個 TCP 連線，範圍為 1 到 255。預設值為 20，或者當執行測試的路由器 CPU 核心數超過 20 時，使用其 CPU 核心數：64 核路由器會使用 64，即使對端伺服器的核心數更少也是如此。遠端伺服器的會話列表（`/tool/bandwidth-server/session/print detail`）會以 `tcp-connection-count` 顯示該數字。TCP 連線發往遠端路由器的埠 2000。UDP 部分使用遠端路由器上從 `allocate-udp-ports-from`（預設為 2000）起始的埠。

有關所有引數，請參閱 [`/tool/speed-test`](../cli-reference/tool/speed-test.md) 和 [`/tool/bandwidth-server`](../cli-reference/tool/bandwidth-server/index.md) CLI 參考。
