---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/packet-sniffer"
sidebar_position: 4
title: "封包嗅探器"
sidebar_label: "封包嗅探器"
description: "RouterOS 封包嗅探器：在路由器上捕獲封包，對其進行過濾，在控制檯中即時檢視，將其儲存到 pcapng 檔案以供 Wireshark 使用，或透過 TZSP 將其流式傳輸到 PC，並瞭解嗅探器無法看到的內容。"
tags:
  - 'packet-sniffer'
  - 'filtering'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/packet-sniffer
captured_at: '2026-11-04T11:15:27+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

封包嗅探器會捕獲路由器接收、傳送和轉發的封包。用它來診斷網路問題：裝置是否傳送請求並收到應答、哪些封包到達某個介面，或者一次協定互動是什麼樣子。你可以在控制檯中即時檢視封包，將它們儲存到檔案供 [Wireshark](https://www.wireshark.org/) 使用，或者在捕獲時將封包流式傳輸到 PC。

嗅探器將捕獲的封包儲存在記憶體中，預設 100 KiB。過濾器決定它捕獲哪些封包；沒有過濾器時，它會捕獲每個介面上的所有內容，在繁忙的路由器上這會很快填滿記憶體。捕獲內容包含使用者的流量，因此請像對待其他私有資料一樣對待這些檔案。

## 捕獲封包並在 Wireshark 中開啟 {#capture-packets-and-open-them-in-wireshark}

192.168.88.50 上的一臺計算機無法開啟網站。在 LAN 網橋上啟動嗅探器，並使用針對該計算機地址的過濾器，復現問題，停止嗅探器並將封包儲存到檔案：

```ros
/tool/sniffer/start interface=bridge ip-address=192.168.88.50/32
/tool/sniffer/stop
/tool/sniffer/save file-name=capture.pcap
```

在 LAN 側捕獲：在 WAN 介面上，源 NAT 已經將計算機的地址替換為路由器的地址。

從路由器的檔案中下載 `capture.pcap`（WinBox 或 WebFig 中的 Files 選單，或 `scp admin@192.168.88.1:capture.pcap .`），並在 Wireshark 中開啟它。無論副檔名是什麼，該檔案都是 pcapng 格式，併為每個封包記錄介面、方向以及納秒級解析度的時間戳。

要在嗅探器執行時將封包寫入檔案，請先設定檔名：

```ros
/tool/sniffer/set file-name=capture.pcap file-limit=10000KiB
/tool/sniffer/start interface=bridge ip-address=192.168.88.50/32
```

每次啟動都會覆蓋該檔案。當檔案達到 `file-limit` 時，嗅探器會停止寫入該檔案，但會繼續執行。對於長時間捕獲，請將檔案寫入 USB 磁碟或 [RAM 磁碟](../storage/tmpfs.md) 而不是路由器的快閃記憶體，並使用類似 `file-name=usb1/capture.pcap` 的路徑。要停止寫入檔案，請設定 `file-name=""`。

## 即時檢視封包 {#watch-packets-live}

`quick` 會在匹配的封包到達時在控制檯中顯示它們，而不更改設定。它會一直執行，直到你按下 <kbd>Q</kbd>，或者執行到 `duration`；`proplist` 選擇列。要檢視 ether1 上路由器的 DHCP 用戶端是否收到應答，請按埠過濾：DHCP 用戶端啟動時沒有地址，因此地址過濾器會漏掉它的最初幾個封包：

```ros
/tool/sniffer/quick interface=ether1 port=bootps,bootpc duration=10s \
    proplist=time,dir,src-address,dst-address,size
```

```text
Columns: TIME, DIR, SRC-ADDRESS, DST-ADDRESS, SIZE
TIME      DIR  SRC-ADDRESS                DST-ADDRESS                SIZE
4.922348  ->   192.168.88.24:68 (bootpc)  192.168.88.1:67 (bootps)    342
4.923657  <-   192.168.88.1:67 (bootps)   192.168.88.24:68 (bootpc)   342
```

`TIME` 計算自開始以來的秒數，`<-` 標記接收的資料包，`->` 標記傳送的封包。沒有 `interface` 時，經過網橋發往路由器或從路由器發出的封包會出現兩次：一次在網橋上，一次在網橋埠上。嗅探器啟動時，`quick` 不會執行。

## 在控制檯中檢視捕獲內容 {#look-at-a-capture-in-the-console}

執行 `stop` 後，捕獲的封包會在記憶體中保留 10 分鐘，或直到下一次 `start`，並且有四個選單顯示它們。將它們儲存到檔案可以保留更長時間：

```ros
/tool/sniffer/packet/print
```

```text
Columns: TIME, INTERFACE, SRC-ADDRESS, DST-ADDRESS, IP-PROTOCOL, SIZE, CPU
#  TIME      INTERFACE  SRC-ADDRESS    DST-ADDRESS    IP-PROTOCOL  SIZE  CPU
0  1.191491  bridge     192.168.88.1   192.168.88.10  icmp           70    3
1  1.191726  bridge     192.168.88.10  192.168.88.1   icmp           70    0
2  2.193866  bridge     192.168.88.1   192.168.88.10  icmp           70    2
3  2.194027  bridge     192.168.88.10  192.168.88.1   icmp           70    0
```

`/tool/sniffer/protocol/print` 按協定、IP 協定和埠統計封包和位元組數，以及它們在捕獲內容中的佔比。`/tool/sniffer/host/print` 顯示每個地址的速率、峰值速率和總位元組數，每一項都是兩個值：發往該地址和從該地址發出。速率在捕獲停止時計算：

```text
Columns: ADDRESS, RATE, PEAK-RATE, TOTAL
#  ADDRESS        RATE           PEAK-RATE      TOTAL
0  192.168.88.1   560bps/560bps  560bps/560bps  280/280
1  192.168.88.10  560bps/560bps  560bps/560bps  280/280
```

`/tool/sniffer/connection/print` 列出 TCP 連線及其每個方向上的位元組數、重傳次數和 MSS：

```text
Columns: SRC-ADDRESS, DST-ADDRESS, BYTES, RESENDS, MSS
# SRC-ADDRESS          DST-ADDRESS              BYTES     RESENDS  MSS
0 192.168.88.1:55042   192.168.88.10:80 (http)  104/1536  0/0      1460/1460
```

要檢視當前哪些主機使用最多頻寬，請改用 [Torch](./torch.md)：它會即時顯示速率。

## 將封包流式傳輸到 Wireshark {#stream-packets-to-wireshark}

嗅探器可以透過 TaZmen Sniffer Protocol (TZSP) 將每個捕獲的封包傳送到 PC，因此 Wireshark 可以在捕獲封包時顯示它們。將 PC 的地址設定為 `streaming-server`（埠預設為 37008），並開啟 `filter-stream`：

```ros
/tool/sniffer/set streaming-enabled=yes streaming-server=192.168.88.10 \
    filter-stream=yes
/tool/sniffer/start interface=ether1
```

僅指定 `interface` 時，嗅探器會流式傳輸 ether1 的所有流量。每個捕獲的封包都會再次以未加密的 UDP 封包形式穿過網路，因此流式傳輸繁忙介面會增加通往 PC 的路徑負載。

`filter-stream=yes` 可防止嗅探器捕獲它自己的流封包。沒有它時（預設值為 `no`），當流經過被嗅探的介面離開時，嗅探器會捕獲這些流封包並再次流式傳輸它們，形成迴圈。使用 `yes` 時，嗅探器還會排除發往 PC 和來自 PC 的 ICMP 封包，即使流式傳輸已關閉也是如此。

在 Wireshark 中，使用捕獲過濾器 `udp port 37008` 在 PC 的網路介面上捕獲，或使用顯示過濾器 `udp.port==37008` 僅顯示該流。Wireshark 會解碼 TZSP 封包，並在其中顯示捕獲的幀：

![Wireshark display filter bar with the filter udp.port==37008](/img/f97b4838589f3f84.webp)

要停止流式傳輸，請設定 `streaming-enabled=no`；該設定會一直保留，直到你更改它。

## 選擇要捕獲的內容 {#choose-what-to-capture}

使用 `/tool/sniffer/set` 設定過濾器，以便在每次捕獲時保留它們，或者將它們提供給 `start` 或 `quick` 以用於一次執行。引數是去掉 `filter-` 的過濾器名稱（`interface`、`ip-address`、`port`），以及用於 `filter-vlan` 的 `vlan-id`。帶引數時，只有給出的過濾器生效：未重複給出的已儲存過濾器在該次執行中會被忽略。不帶引數時，已儲存的過濾器會生效，因此請用 `/tool/sniffer/print` 檢查它們，並用 `/tool/sniffer/reset` 清除所有設定。

- `filter-interface` - 要嗅探的介面。空表示所有介面。
- `filter-ip-address`、`filter-src-ip-address`、`filter-dst-ip-address` 以及 IPv6 和 MAC 地址變體 - 任一方向上的地址，作為源或作為目標。對於流的單個方向，請使用源和目標過濾器。
- `filter-port`、`filter-src-port`、`filter-dst-port` - 埠，按編號或名稱（`ssh`、`dns`、`bootps`）。
- `filter-ip-protocol`、`filter-mac-protocol` - 協定，按名稱或編號。
- `filter-vlan` - 承載帶標籤幀的埠上這些幀的 VLAN ID。地址和協定過濾器匹配標籤內部的封包。在 VLAN 介面本身上，封包是不帶標籤的。
- `filter-direction` - `rx` 表示在被嗅探介面上接收的封包，`tx` 表示傳送的封包，`any`（預設）表示兩者。
- `filter-operator-between-entries` - 使用 `or`（預設）時，匹配過濾器中任一條目的封包即匹配；使用 `and` 時，它必須匹配所有條目，例如 `ip-address=192.168.88.50/32,192.168.88.1/32` 中的兩個地址。

用逗號分隔多個值，並在值前加上 `!` 以排除它。不同過濾器總是組合生效：只有當封包匹配所有已設定的過濾器時才會被捕獲。

嗅探器最多在記憶體中保留 `memory-limit` 個數據包。使用 `memory-scroll=yes`（預設）時，記憶體已滿時新封包會替換最舊的封包，因此記憶體中儲存的是最新封包：問題出現後立即停止嗅探器。使用 `no` 時，嗅探器保留最初的封包，不再儲存更多封包。`only-headers=yes` 僅保留並儲存封包頭，這樣同樣的記憶體或檔案可以容納更多封包。請讓 `memory-limit` 遠低於路由器的可用記憶體（`/system/resource/print`）。

有關所有設定，請參閱 CLI 參考中的 [`/tool/sniffer`](../cli-reference/tool/sniffer/index.md)。

## 嗅探器能看到什麼 {#what-the-sniffer-sees}

- 嗅探器在防火牆和 NAT 之前捕獲接收的封包，在它們之後捕獲傳送的封包。它會顯示隨後被防火牆丟棄的封包，但僅作為接收的封包顯示，並且會按封包在網路線上的原樣顯示地址和埠。
- 嗅探器執行時，路由器會關閉 IPv4 [快速路徑](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path)，並隨之關閉 FastTrack，因此轉發的流量會佔用更多 CPU。
- 網橋在硬體中轉發（硬體解除安裝）的封包永遠不會到達路由器的 CPU，也不會被捕獲；泛洪的封包，例如廣播、組播和未知單播，則可以被捕獲。
- 啟用了用戶端到用戶端轉發的無線用戶端之間的單播流量不會經過嗅探器。
- 除非設定了 [流量生成器](./traffic-generator.md) 的 `fast-path` 引數，否則在同一介面上看不到它的封包。

## 技術細節 {#technical-details}

- 封包列表顯示自捕獲開始以來的時間（秒），精確到微秒。
- 從 RouterOS 7.20 起，`save` 和 `file-name` 寫入 pcapng 檔案；更早的版本寫入 pcap。流量生成器的 `inject-pcap` 從 RouterOS 7.21 起讀取 pcapng 檔案。
- TZSP 流使用 TZSP 版本 1 和乙太網封裝，並完整承載每個捕獲的幀。
