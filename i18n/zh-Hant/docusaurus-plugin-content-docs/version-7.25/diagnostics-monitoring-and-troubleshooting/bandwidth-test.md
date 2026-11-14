---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/bandwidth-test"
sidebar_position: 5
title: "頻寬測試"
sidebar_label: "頻寬測試"
description: "頻寬測試用於測量兩臺 MikroTik 路由器之間的 TCP 或 UDP 吞吐量：/tool/bandwidth-test 中的用戶端向另一臺路由器的頻寬測試伺服器傳送資料或從中接收資料。內容涵蓋前提條件、以固定速率或最大速率進行測試、讀取結果以及保護伺服器安全。"
tags:
  - 'bandwidth'
  - 'throughput'
  - 'tcp'
  - 'udp'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/bandwidth-test
captured_at: '2026-11-04T11:15:14+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

頻寬測試用於測量兩臺 MikroTik 路由器之間的吞吐量。一臺路由器上的用戶端（`/tool/bandwidth-test`）連線到另一臺路由器的頻寬測試伺服器（`/tool/bandwidth-server`），傳送或接收 TCP 或 UDP 流量，並每秒顯示速率。可用它檢查無線鏈路或 WAN 鏈路，或找出路徑上的瓶頸。

若要在一次執行中測量延遲、抖動以及兩個方向上的 TCP 和 UDP 吞吐量，請使用 [速度測試](./speed-test.md)。

:::warning
不設速度限制的測試會佔用路徑能提供的全部頻寬以及路由器很大一部分 CPU 時間，鏈路上的其他流量、路由協定和管理訪問都會受到影響。在正在使用的鏈路上，請設定速度限制，或在鏈路空閒時測試。
:::

## 先決條件 {#prerequisites}

在執行伺服器的那臺路由器上：

- 頻寬測試伺服器已開啟。它預設開啟，並啟用身份驗證：

  ```ros
  [admin@MikroTik] > /tool/bandwidth-server/print
                    enabled: yes
               authenticate: yes
    allocate-udp-ports-from: 2000
               max-sessions: 100
         allowed-addresses4:
         allowed-addresses6:
  ```

- [裝置模式](../system-information-and-utilities/device-mode.md)允許頻寬測試，伺服器和用戶端都是如此：`/system/device-mode/print` 顯示 `bandwidth-test: yes`。大多數隨 RouterOS 7.17 或更高版本交付的路由器處於 `home` 或 `basic` 模式，這些模式會關閉該功能（CCR 和 1100 系列路由器處於 `advanced`）。開啟它需要物理接觸路由器，因此在將路由器安裝到遠端站點之前請先檢查。
- 伺服器上有一個供用戶端登入的使用者，其所在組同時具有 `test` 和 `winbox` 策略；伺服器會檢查這兩項。預設的 `read` 和 `full` 組都具備這兩項，因此現有管理員賬戶也可以使用。只具有這兩項策略的組就足夠了：

  ```ros
  /user/group/add name=btest policy=test,winbox
  /user/add name=btest group=btest password=change-this-password
  ```

- 防火牆接受來自用戶端的 TCP 埠 2000 和 UDP 埠 2000-65535。預設防火牆會從 WAN 側丟棄這些流量；當伺服器只能透過網際網路訪問時，請為測試新增規則，如[為透過網際網路進行的測試開放防火牆](./speed-test.md#open-the-firewall-for-a-test-over-the-internet)中所述，並在測試後移除它們。

在用戶端上，`receive` 和 `both` 方向的 UDP 測試需要伺服器的 UDP 封包能夠到達：位於 NAT 或防火牆之後且防火牆丟棄這些封包的用戶端將收不到任何內容。這種情況下請使用 TCP，或在用戶端上接受來自伺服器的 UDP。

測試完成後，請刪除測試使用者（`/user/remove btest` 和 `/user/group/remove btest`）以及你新增的任何防火牆規則。

## 測試鏈路 {#test-a-link}

若要檢查一條無線鏈路在兩個方向上都能承載 50 Mbit/s 而又不佔滿它，請為兩個方向設定速度限制：

```ros
[admin@MikroTik] > /tool/bandwidth-test address=10.0.0.2 user=btest \
    password=change-this-password protocol=tcp direction=both \
    local-tx-speed=50M remote-tx-speed=50M duration=10s
                status: done testing
              duration: 11s
            tx-current: 50.3Mbps
  tx-10-second-average: 49.9Mbps
      tx-total-average: 49.9Mbps
            rx-current: 51.3Mbps
  rx-10-second-average: 49.8Mbps
      rx-total-average: 49.8Mbps
           random-data: no
             direction: both
      connection-count: 20
        local-cpu-load: 9%
       remote-cpu-load: 0%
```

`local-tx-speed` 限制用戶端傳送的內容，`remote-tx-speed` 限制伺服器傳送的內容。如果不設定 `duration`，測試會一直執行，直到你按下 <kbd>Control</kbd>+<kbd>C</kbd>。

### 檢查鏈路是否丟包 {#check-a-link-for-packet-loss}

若要檢查鏈路能否以某個速率傳輸而不丟包，請以該速率傳送 UDP 並觀察 `lost-packets`：

```ros
[admin@MikroTik] > /tool/bandwidth-test address=10.0.0.2 user=btest \
    password=change-this-password direction=receive \
    remote-tx-speed=500M duration=10s
                status: done testing
              duration: 11s
            rx-current: 491.1Mbps
  rx-10-second-average: 486.2Mbps
      rx-total-average: 486.2Mbps
          lost-packets: 3
           random-data: no
             direction: receive
               rx-size: 1500
      connection-count: 20
        local-cpu-load: 3%
       remote-cpu-load: 6%
```

在 491 Mbit/s 的 1500 位元組封包下，每秒大約有 41,000 個數據包到達，因此最後一秒丟失 3 個數據包的丟包率不到 0.01%。如果一條鏈路在低於其容量的速率下仍丟失一部分封包，則說明它存在問題，例如無線鏈路上的干擾。TCP 不會顯示這種丟包：它會重新發送丟失的資料並只是降低速度。

大多數無線鏈路在兩個方向之間共享空口時間。請分別測試每個方向（`direction=transmit`，然後 `direction=receive`）以檢視每個方向獲得的速率，並用 `direction=both` 檢視鏈路總共承載的速率。

### 測量最大吞吐量 {#measure-the-maximum-throughput}

不設速度限制時，測試會盡可能多地傳送資料：

```ros
[admin@MikroTik] > /tool/bandwidth-test address=10.0.0.2 user=btest \
    password=change-this-password protocol=tcp direction=both \
    duration=10s
                status: done testing
              duration: 10s
            tx-current: 920.3Mbps
  tx-10-second-average: 918.0Mbps
      tx-total-average: 918.0Mbps
            rx-current: 748.4Mbps
  rx-10-second-average: 674.0Mbps
      rx-total-average: 674.0Mbps
           random-data: no
             direction: both
      connection-count: 20
        local-cpu-load: 16%
       remote-cpu-load: 4%
```

TCP 顯示的是 TCP 應用在該路徑上獲得的效能：當封包丟失或延遲時，TCP 會降低速度。使用預設的 20 個連線時，結果是許多連線的總和；單個連線（`connection-count=1`）更接近單次下載，而單次下載更受路徑延遲的限制。UDP 顯示當傳送端不降速時路徑能提供多少頻寬，以及會丟失多少。預設測試是 UDP，由伺服器傳送（`direction=receive`）1500 位元組的封包：

```ros
[admin@MikroTik] > /tool/bandwidth-test address=10.0.0.2 user=btest \
    password=change-this-password duration=10s
                status: done testing
              duration: 11s
            rx-current: 957.3Mbps
  rx-10-second-average: 943.9Mbps
      rx-total-average: 943.9Mbps
          lost-packets: 18632
           random-data: no
             direction: receive
               rx-size: 1500
      connection-count: 20
        local-cpu-load: 5%
       remote-cpu-load: 7%
```

若要使用其他封包大小進行測試，請設定 `local-udp-tx-size`（用戶端）和 `remote-udp-tx-size`（伺服器）。該大小是整個 IP 封包的大小，在 IPv4 下為 52 到 64000 位元組；大於路徑上最小 MTU 的封包會被分片。小封包測試路徑每秒轉發多少個數據包，大封包測試每秒轉發多少位元。

若要測試到路由器的 IPv6 鏈路本地地址，請新增介面：`address=fe80::34:23ff:fe6a:570c%ether1`。

## 解讀結果 {#read-the-results}

- `tx-` 值表示用戶端傳送的內容，`rx-` 值表示它接收的內容。
- `current` 是最後一秒，`10-second-average` 是最後 10 秒，`total-average` 是整個測試期間。
- UDP 統計整個 IP 封包，包括報頭。TCP 只統計資料，因此 TCP 結果會比鏈路上的流量低幾個百分點，而且返回的確認封包根本不計入。在無線鏈路上，它們還會佔用空口時間。
- `lost-packets`（UDP）是最後一秒內未到達的封包數量，不是總數。用戶端顯示它接收到的內容（`receive` 和 `both`）；對於用戶端傳送的內容，伺服器的會話列表會顯示。
- `local-cpu-load` 和 `remote-cpu-load` 是測試期間用戶端和伺服器的 CPU 負載。接近 100% 的負載意味著限制結果的是路由器，而不是鏈路。較低的值並不能排除這一點：一個繁忙的 CPU 核心可能會限制測試，而其他核心空閒，因此請檢查 `/system/resource/cpu/print` 中的各個核心。
- `connection-count` 是 TCP 連線數，或具有各自埠的 UDP 流數：20，或在核心數超過 20 的路由器上為 CPU 核心數。多個連線會將負載分散到各個 CPU 核心上。

不設速度限制時，UDP 傳送端在大約第一秒內會以全速傳送，之後傳送量會超過接收端報告的數量。因此在比傳送端慢的鏈路上，`lost-packets` 會一直大於零，而 `rx-` 值就是鏈路的吞吐量。若要檢查鏈路是否丟包，請將速度設為其容量以下，如檢查鏈路是否丟包中所述。

若要測試會對資料進行壓縮的鏈路，請設定 `random-data=yes`：測試隨後會發送無法壓縮的資料。這會在兩臺路由器上消耗更多 CPU 時間，在 CPU 較慢的路由器上可能會限制結果。

## 測試路由器的轉發能力 {#test-a-routers-forwarding-capacity}

生成和接收測試流量會消耗用戶端和伺服器上的 CPU 時間。若要測量路由器轉發多少流量，請不要從該路由器上或向該路由器執行測試：將三臺路由器連成一條鏈，在一端執行伺服器，在另一端執行用戶端，並透過中間的路由器進行測試。將兩端路由器的子網透過中間路由器路由，並觀察 `local-cpu-load` 和 `remote-cpu-load`：當某一端路由器接近 100% 時，限制結果的是它，而不是中間的路由器。兩端路由器必須能夠傳送和接收比中間路由器轉發的更多的流量。使用 1500 位元組的封包測量位元率，使用小的 UDP 封包（`local-udp-tx-size=64`）測量封包速率，後者對大多數路由器來說會先成為限制。當一對路由器無法壓滿被測路由器時，請使用更多對，或使用[流量生成器](./traffic-generator.md)。

## 保護伺服器安全 {#secure-the-server}

伺服器會響應每個能訪問 TCP 埠 2000 的用戶端。在 `authenticate=yes`（預設值）下，用戶端必須使用具有 `test` 和 `winbox` 策略的使用者登入。不要在不可信網路能夠訪問的路由器上設定 `authenticate=no`：否則任何人都可能使該路由器及其鏈路過載。預設防火牆會從 WAN 側丟棄 TCP 埠 2000；請保持這種設定，或僅從已知地址接受它。

若僅接受來自已知地址的測試，請列出這些地址；其他用戶端會得到 `can not connect`。使用者自身的 `address` 設定不會限制頻寬測試登入，因此請使用這些列表。當路由器有 IPv6 地址時，也要設定 `allowed-addresses6`：

```ros
/tool/bandwidth-server/set allowed-addresses4=192.0.2.0/24 \
    allowed-addresses6=2001:db8::/32
```

若要關閉伺服器：

```ros
/tool/bandwidth-server/set enabled=no
```

`max-sessions` 限制同時執行多少個測試（預設為 100），無論它們有多少個連線。單個測試也不能使用超過 `max-sessions` 的連線數，因此請使其保持大於或等於用戶端的 `connection-count`。

伺服器在 `/tool/bandwidth-server/session` 中列出正在執行的測試，從伺服器的視角顯示（`send` 表示伺服器傳送）：

```ros
[admin@MikroTik] > /tool/bandwidth-server/session/print \
    proplist=protocol,direction,user,tx-current,rx-current
Columns: PROTOCOL, DIRECTION, USER, TX-CURRENT, RX-CURRENT
#  PROTOCOL  DIRECTION  USER   TX-CURRENT  RX-CURRENT
0  tcp       both       admin  624.1Mbps   917.2Mbps
```

## 故障排除 {#troubleshoot}

| 狀態或症狀 | 原因與解決方法 |
| :-- | :-- |
| `authentication failed` | 使用者名稱或密碼錯誤，或者當伺服器設定了 `authenticate=yes` 時沒有提供使用者。該使用者必須存在於伺服器上，並且位於同時具有 `test` 和 `winbox` 策略的組中（在伺服器上執行 `/user/group/print`）。 |
| `can not connect` | 伺服器已關閉或無法在 TCP 埠 2000 上訪問，用戶端不在 `allowed-addresses4`/`allowed-addresses6` 中，或者伺服器已經運行了 `max-sessions` 個測試。 |
| `disconnected` | 測試期間連線丟失，或者測試使用的連線數超過伺服器的 `max-sessions`。 |
| `not allowed by device-mode` | 執行測試的路由器上的裝置模式中 `bandwidth-test: no`。 |
| UDP `receive` 測試顯示 0 bps。 | 伺服器的 UDP 封包無法到達用戶端：用戶端位於 NAT 或防火牆之後。請使用 TCP，或允許來自伺服器的 UDP。UDP `transmit` 測試可在 NAT 之後正常工作。 |
| 結果低於鏈路速度，且 CPU 負載接近 100%。 | 路由器限制了測試；請改為透過該路由器進行測試（請參閱測試路由器的轉發能力）。 |

## 技術細節 {#technical-details}

### 埠與連線 {#ports-and-connections}

用戶端會開啟一個到伺服器埠 2000 的 TCP 連線（`/ip/service` 中的 `btest` 服務），登入並透過它交換結果。UDP 測試資料在兩臺路由器上都使用從 `allocate-udp-ports-from`（預設為 2000）向上的埠：伺服器每個測試使用一個埠，用戶端每個流使用一個埠。每臺路由器都會佔用空閒埠，因此在其他測試執行時埠號會向上移動。TCP 測試使用 `connection-count` 個到埠 2000 的 TCP 連線。伺服器以 IPv4 對映的 IPv6 形式顯示 IPv4 用戶端（IPv4 地址位於 `::ffff:` 之後），例如 `::ffff:192.0.2.1`。

### 封包大小與計數 {#packet-size-and-counting}

`local-udp-tx-size` 和 `remote-udp-tx-size` 設定 IP 封包大小：1500 位元組即 1472 位元組的 UDP 資料。UDP 速率統計 IP 封包，TCP 速率統計 TCP 資料。介面計數器還包括乙太網報頭，因此它們顯示的值會略高於測試結果。

有關所有引數，請參閱 [`/tool/bandwidth-test`](../cli-reference/tool/bandwidth-test.md)、[`/tool/bandwidth-server`](../cli-reference/tool/bandwidth-server/index.md) 和 [`/tool/bandwidth-server/session`](../cli-reference/tool/bandwidth-server/session.md) CLI 參考。
