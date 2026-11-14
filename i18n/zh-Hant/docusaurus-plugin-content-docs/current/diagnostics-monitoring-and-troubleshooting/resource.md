---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/resource"
sidebar_position: 14
title: "資源"
sidebar_label: "資源"
description: "/system/resource 選單顯示路由器的標識和資源使用情況：uptime、RouterOS 版本、記憶體、disk/NAND、CPU 型號和負載；子選單可按核心 (cpu) 細分負載、按中斷 (irq) 細分負載、在核心之間引導封包處理 (irq/rps)、列出 PCI/USB/SCSI 硬體 (hardware)，並允許進行 USB 電源控制。"
tags:
  - 'system-resource'
  - 'cpu'
  - 'hardware'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/resource
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

[`/system/resource`](../cli-reference/system/resource/index.md) 選單顯示路由器的整體資源使用情況和標識：uptime、version、memory、disk、CPU 型號、架構以及 NAND 的壞塊百分比。所有值均為只讀。

```ros
[admin@MikroTik] > /system/resource/print
                   uptime: 2h31m3s
                  version: 7.26beta1
               build-time: 2026-10-01 13:29:47
          minimum-version: 7.0.9
              free-memory: 678.7MiB
             total-memory: 1024.0MiB
                      cpu: ARM64
                cpu-count: 4
            cpu-frequency: 864MHz
                 cpu-load: 0%
           free-hdd-space: 91.9MiB
          total-hdd-space: 128.0MiB
  write-sect-since-reboot: 437
         write-sect-total: 263060
               bad-blocks: 0%
        architecture-name: arm64
               board-name: hAP ax^2
                 platform: MikroTik
```

屬性（uptime、version、build-time、memory、hdd space、write-sector 和 bad-block 計數器、board 和 platform 名稱）在 [`/system/resource`](../cli-reference/system/resource/index.md) CLI 參考頁面中描述。

## 即時檢視使用情況 {#watch-usage-live}

`/system/resource/monitor` 會輸出一個即時更新的檢視，顯示每個核心的 CPU 使用率和空閒記憶體（該表格會持續重新整理；用 `duration` 限制其時長）：

```ros
[admin@MikroTik] > /system/resource/monitor duration=2
           cpu-used: 0%
  cpu-used-per-core: 1%
                     0%
                     0%
                     0%
        free-memory: 694948KiB
```

`free-memory` 在這裡以 KiB 為單位（694948 KiB ≈ 678.7 MiB，如 `print` 所示）。

## 檢視每核心明細 {#read-per-core-breakdown}

`/system/resource/cpu` 顯示每個核心的使用率，分為使用者負載（`load`）、中斷處理（`irq`）和磁碟 I/O（`disk`）：

```ros
[admin@MikroTik] > /system/resource/cpu/print
Columns: CPU, LOAD, IRQ, DISK
#  CPU   LOAD  IRQ  DISK
0  cpu0  0%    0%   0%
1  cpu1  0%    0%   0%
2  cpu2  1%    0%   0%
3  cpu3  0%    0%   0%
```

## 中斷（IRQ） {#interrupts-irq}

[`/system/resource/irq`](../cli-reference/system/resource/irq/index.md) 選單顯示路由器上使用的所有 IRQ，包括 IRQ 分配到的 CPU，以及每個裝置的中斷計數器行：

```ros
[admin@MikroTik] > /system/resource/irq/print where count>0
Flags: o - READ-ONLY
Columns: IRQ, USERS, CPU, ACTIVE-CPU, COUNT
 #   IRQ  USERS                                CPU   ACTIVE-CPU   COUNT
 0     6  bam_dma                              auto           0      68
 1     8  78b5000.spi                          auto           2     157
 2     9  glink-native                         auto           3     116
```

使用 `cpu=auto` 的 IRQ 分配由中斷路由（使用 [NAPI](https://docs.kernel.org/networking/napi.html) 中斷合併）完成。`o` 標誌標記硬體固定的 IRQ，其 CPU 分配無法更改。

要將 IRQ 固定到特定核心：

```ros
/system/resource/irq/set [find irq=6] cpu=2
```

### 接收封包轉向 {#receive-packet-steering}

[`/system/resource/irq/rps`](../cli-reference/system/resource/irq/rps.md) 是接收封包轉向（RPS），類似於接收端縮放（RSS），但以軟體方式實現：它將介面的封包處理工作引導到選定的 CPU。當封包需要額外處理且佔用相對大量 CPU 時間時（例如 PPP 隧道終結、VPLS 或防火牆處理），RPS 很有用：RPS 轉向的開銷會被將繁重工作分散到各核心所帶來的收益所抵消。

RPS 並不總是划算。如果網路裝置有多個硬體佇列，其接收端縮放（RSS）已經將佇列對映到 CPU，那麼 RPS 轉向的開銷大於收益。當硬體佇列數少於 CPU 數，或 RSS 未覆蓋該路徑（例如從隧道介面解封裝後的封包）時，配置 RPS。

## 硬體對映 {#hardware-map}

`/system/resource/hardware` 列出透過 PCI、USB 和 SCSI 匯流排連線的裝置，包括其匯流排位置、供應商/裝置識別符號、韌體報告的名稱、驅動所有者、協商速度、USB 版本等。沒有支援列舉的匯流排的板卡（例如 hAP ax²）會輸出空列表。

### USB 裝置授權 {#usb-device-authorization}

當全域性開啟 USB 裝置授權（在 [`/system/resource/hardware/usb-settings`](../cli-reference/system/resource/hardware/usb-settings.md) 中設定 `authorization=yes`）時，新接入的 USB 裝置會保持停用狀態，直到管理員在 [`/system/resource/hardware/authorize`](../cli-reference/system/resource/hardware/authorize.md) 中允許它們。

### 重設 USB 裝置 {#reset-usb-devices}

要在不重啟路由器的情況下重設工作異常的 USB 調變解調器或驅動器，請使用 [`/system/resource/hardware/usb-power-reset`](../cli-reference/system/resource/hardware/usb-power-reset.md) 對其 USB 埠進行斷電重啟（`bus` 和 `slot` 來自裝置的 `/system/resource/hardware` 行）：

```ros
/system/resource/hardware/usb-power-reset bus=1 slot=2 duration=5s
```

## 技術細節 {#technical-details}

- `cpu-load` 彙總 CPU 所有核心的使用率；使用 `/system/resource/cpu` 或 `monitor` 檢視各核心的明細。
- `write-sect-since-reboot`/`write-sect-total` 和 `bad-blocks` 有助於發現 NAND 裝置上的快閃記憶體磨損（結合 [健康](./health.md) 讀數和 `.65` 風格的早期警告）。

有關所有引數及其預設值，請參閱 [`/system/resource`](../cli-reference/system/resource/index.md)、[`cpu`](../cli-reference/system/resource/cpu.md)、[`irq`](../cli-reference/system/resource/irq/index.md)、[`irq/rps`](../cli-reference/system/resource/irq/rps.md)、[`hardware`](../cli-reference/system/resource/hardware/index.md)、[`usb-settings`](../cli-reference/system/resource/hardware/usb-settings.md)、[`authorize`](../cli-reference/system/resource/hardware/authorize.md) 和 [`usb-power-reset`](../cli-reference/system/resource/hardware/usb-power-reset.md) CLI 參考頁面。
