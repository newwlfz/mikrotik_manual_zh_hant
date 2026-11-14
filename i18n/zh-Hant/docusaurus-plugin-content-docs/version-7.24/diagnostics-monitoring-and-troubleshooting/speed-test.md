---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/speed-test"
sidebar_position: 6
title: "速度測試"
sidebar_label: "速度測試"
description: "Speed Test 工具使用地址、連線數、密碼、測試時長和使用者憑據等可配置屬性，測量 MikroTik 裝置之間的 ping、抖動和 TCP/UDP 吞吐量。它提供詳細的效能指標，包括測試期間的 CPU 利用率。"
tags:
  - 'speed-test'
  - 'bandwidth'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/speed-test
captured_at: '2026-11-04T11:28:01+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Speed Test 是一個簡便的測試工具，用於測量從一臺 MikroTik 裝置到另一臺裝置的 ping、抖動、TCP 和 UDP 吞吐量。"speed-test" 命令基於 Ping Tool 和 Bandwidth Test。要使用此命令，需要能夠訪問 Bandwidth test 伺服器。

## 常規介面屬性 {#general-interface-properties}

speed-test 基於五個可配置屬性：

- address - 主機的 IP 地址。
- connection-count - 如果裝置的核心數超過 20，則使用該核心數（預設值為 20）。
- password - 遠端裝置的密碼。
- test-duration - 每次測試的持續時間（*預設值：5 次測試 \* 每次 10 秒 + 每次測試之間 1 秒暫停 = 54 秒*）。
- user - 遠端裝置的使用者名稱。

## 配置示例 {#configuration-example}

頻寬和速度測試應透過裝置進行，而不是在裝置上進行，以確保貼近真實場景的模擬，並避免因流量生成過程而使被測裝置（DUT）的 CPU 過載。

要從裝置 A（192.168.88.1）到裝置 B（192.168.88.2）執行一個簡單的測試：

```ros
[admin@MikroTik] > /tool/speed-test address=192.168.88.2
              status: done
      time-remaining: 0s
    ping-min-avg-max: 541us / 609us / 3.35ms
  jitter-min-avg-max: 0s / 76us / 2.76ms
                loss: 0% (0/100)
        tcp-download: 921Mbps local-cpu-load:30%
          tcp-upload: 920Mbps local-cpu-load:30% remote-cpu-load:25%
        udp-download: 917Mbps local-cpu-load:6% remote-cpu-load:21%
          udp-upload: 916Mbps local-cpu-load:20% remote-cpu-load:6%
```

如果測試期間任一裝置的 CPU 利用率達到 100%，將會顯示一條警告訊息：

```ros
[admin@MikroTik]] > /tool/speed-test address=192.168.88.2
                  ;;; results can be limited by cpu, note that traffic generation/termination 
                      performance might not be representative of forwarding performance
              status: done
      time-remaining: 0s
    ping-min-avg-max: 541us / 609us / 3.35ms
  jitter-min-avg-max: 0s / 76us / 2.76ms
                loss: 0% (0/100)
        tcp-download: 721Mbps local-cpu-load:78%
          tcp-upload: 820Mbps local-cpu-load:100% remote-cpu-load:84%
        udp-download: 906Mbps local-cpu-load:10% remote-cpu-load:54%
          udp-upload: 895Mbps local-cpu-load:55% remote-cpu-load:12%
```

"test-duration" 引數允許更改全部 5 項測試的持續時間：

1) 帶 50ms 延遲的 Ping 測試。
2) TCP 接收。
3) TCP 傳送。
4) UDP 接收。
5) UDP 傳送。
