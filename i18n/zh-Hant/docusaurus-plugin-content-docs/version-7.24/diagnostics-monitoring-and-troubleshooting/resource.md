---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/resource"
sidebar_position: 14
title: "資源"
sidebar_label: "資源"
description: "RouterOS 中的 Resource 選單提供系統統計資訊概覽，包括 uptime、記憶體、磁碟使用情況，以及 CPU 型號和頻率等硬體詳情。它還提供子選單，用於檢視詳細的每個 CPU 使用率、IRQ 和磁碟統計資訊。"
tags:
  - 'system-resource'
  - 'cpu'
  - 'hardware'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/resource
captured_at: '2026-11-04T11:28:01+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 常規 {#general}

**子選單：** `/system/resource`

常規資源選單顯示整體資源使用情況和路由器統計資訊，例如 uptime、記憶體使用情況、磁碟使用情況、版本等。

它還包含幾個子選單，用於顯示更詳細的硬體統計資訊，例如 CPU、IRQ 和硬體。

```ros
[admin@MikroTik] > /system/resource/print 
                   uptime: 29s
                  version: 7.11.2 (stable)
               build-time: 2023-08-31 13:55:47
         factory-software: 7.6
              free-memory: 94.2MiB
             total-memory: 224.0MiB
                      cpu: ARM
                cpu-count: 2
            cpu-frequency: 800MHz
                 cpu-load: 2%
           free-hdd-space: 93.5MiB
          total-hdd-space: 128.5MiB
  write-sect-since-reboot: 85
         write-sect-total: 222100
               bad-blocks: 0%
        architecture-name: arm
               board-name: hAP ax lite LTE6
                 platform: MikroTik

```

所有屬性均為只讀

| 屬性 | 描述 |
| :-- | :-- |
| **architecture-name** (*string*) | CPU 架構 |
| **bad-blocks** (*percent*) | 顯示 NAND 上壞塊的百分比。 |
| **board-name** (*string*) | RouterBOARD 型號名稱 |
| **build-time**(*string*) | 已安裝 RouterOS 版本的構建時間 |
| **cpu** (*string*) | 板載的 CPU 型號 |
| **cpu-count** (*integer*) | 系統中存在的 CPU 數量。每個核心都是獨立的 CPU，Intel HT 也是獨立的 CPU。 |
| **cpu-frequency** (*string*) | 當前 CPU 頻率 |
| **cpu-load** (*percent*) | 已使用 CPU 資源的百分比。彙總所有 CPU。每核 CPU 使用率可在 [CPU 子選單](#cpu) 中檢視 |
| **factory-software**(*string*) | 最低 RouterOS 版本 |
| **free-hdd-space** (*string*) | 硬碟或 NAND 上的可用空間 |
| **free-memory** (*string*) | 未使用的 RAM 容量 |
| **platform** (*string*) | 平臺名稱 |
| **total-hdd-space** (*string*) | 硬碟或 NAND 的大小 |
| **total-memory** (*string*) | 已安裝的 RAM 容量 |
| **uptime** (*time*) | 自啟動以來經過的時間間隔 |
| **version** (*string*) | 已安裝的 RouterOS 版本號 |
| **write-sect-since-reboot** (*integer*) | 自路由器上次重啟以來，HDD 或 NAND 中的扇區寫入次數 |
| **write-sect-total** (*integer*) | 扇區寫入總次數 |

### CPU {#cpu}

**子選單：** `/system/resource/cpu`

此子選單顯示每個 CPU 的使用率，以及 IRQ 和磁碟使用率。

```ros
[admin@RB1100test] /system/resource/cpu> print 
CPU LOAD IRQ DISK 
0 5% 0% 0% 
[admin@RB1100test] /system/resource/cpu> 

```

## 屬性 {#properties}

### 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **cpu** (*integer*) | 顯示其使用率的 CPU 標識號。 |
| **load** (*percent*) | CPU 使用率百分比 |
| **irq** (*percent*) | IRQ 使用率百分比 |
| **disk** (*percent*) | 磁碟使用率百分比 |

### IRQ {#irq}

**子選單：** `/system/resource/irq`

該選單顯示路由器上所有已使用的 IRQ。可以在多核系統上透過將 IRQ 分配給特定核心來設定 [IRQ 負載均衡](#irq)。IRQ 分配由硬體完成，無法從 RouterOS 更改。例如，如果所有乙太網介面都分配給同一個 IRQ，則必須處理硬體問題：升級主機板的 BIOS，在 BIOS 中手動重新分配 IRQ；如果以上方法都無效，則更換硬體。

#### 屬性 {#properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **cpu** (*auto \| integer*; 預設值： ) | 指定將哪個 CPU 分配給 IRQ。auto - 根據中斷數量選擇 CPU。使用 NAPI 最佳化中斷。 |

**只讀屬性**

| 屬性 | 描述 |
| :-- | :-- |
| **active-cpu** (*integer*) | 顯示多核系統中的活動 CPU。 |
| **count** (*integer*) | 中斷數量。在乙太網介面上，interrupt=packet。 |
| **irq** (*integer*) | IRQ 標識號 |
| **users** (*string*) | 分配給 IRQ 的程式 |

### RPS {#rps}

**子選單：** `/system/resource/irq/rps`

**子選單：** `/system/resource/irq/rps`  
  
Receive Packet Steering (RPS) 與 Receive Side Scaling (RSS) 類似，都是用於將封包定向到特定 CPU 進行處理。但是，RPS 在軟體層面實現，有助於防止單個網路介面卡的硬體佇列成為網路流量中的瓶頸。  
RPS 在封包需要額外處理且消耗相對大量 CPU 時間時很有用，例如 PPP 隧道終止、VPLS 或防火牆處理。RPS 在將封包分類並轉發到另一個 CPU 上花費的 CPU 資源，會被所需的額外處理所抵消。不幸的是，RPS 並不總能替代乙太網驅動程式中的若干行程式碼，因為將封包轉發到另一個 CPU 本身開銷就很大。
  
對於具有多個佇列的網路裝置，通常同時配置 RPS 和 RSS 沒有好處，因為預設情況下 RSS 會配置為將 CPU 對映到每個接收佇列。但是，如果硬體佇列數少於 CPU 數，則 RPS 仍可能有益，具體取決於裝置處理的流量。

#### 屬性 {#properties-2}

| 屬性 | 描述 |
| :-- | :-- |
| **disable***(number)* | 為選定條目停用 RPS |
| **edit** *(number)* | 編輯現有條目的屬性 |
| **enable** *(number)* | 為選定條目啟用 RPS |
| **reset***(number)* | 將屬性重設為預設值 |

### **硬體** {#hardware}

顯示透過 PCI、USB 或 SCSI 匯流排連線的已檢測硬體裝置。

標誌：

```ros
I - inactive   Device is present but not active
```

**子選單：** `/system/resource/hardware`

#### 屬性 {#properties-3}

| 屬性 | 描述 |
| :-- | :-- |
| **location** (*string*) | 裝置在系統拓撲中的位置 |
| **parent** (*enum*) | 父匯流排或控制器 |
| **type** (usb\|pci\|scsi\|serial) | 裝置的匯流排型別 |
| **vendor** (*string*) | 裝置供應商名稱 |
| **name** (*string*) | 裝置名稱或型號 |
| **serial-number** (*string*) | 裝置序列號 |
| **vendor-id**(string) | 供應商識別符號 (VID) |
| **device-id** (string) | 裝置識別符號 (PID / Device ID) |
| **speed** (*string*) | 協商後的裝置速度 |
| **ports***(number)* | 裝置提供的埠數 |
| **usb-version** (*string*) | 支援的 USB 版本 |
| **owner** (*string*) | 擁有該裝置的子系統或驅動程式 |
| **device-path** (*string*) | 從根匯流排到端點的裝置路徑 |

**只讀屬性**

| 屬性 | 描述 |
| :-- | :-- |
| **category** (*string*) | 裝置類別 |
| **irq** (*number*) | 分配的中斷號 |

### 裝置授權 {#device-authorization}

控制硬體裝置的授權狀態。

**子選單：** `/system/resource/hardware/authorize`

#### 屬性 {#properties-4}

| 屬性 | 描述 |
| :-- | :-- |
| **allow** (*yes\|no*) | 啟用或停用 USB 裝置授權 |

### 全域性 USB 子系統設定 {#global-usb-subsystem-settings}

**子選單：** `/system/resource/hardware/usb-settings`

#### 屬性 {#properties-5}

| 屬性 | 描述 |
| :-- | :-- |
| **authorization** (*yes\|no*) | 啟用或停用 USB 裝置授權 |
| **數字** (*number*) |  |

**子選單：** `/system/resource/hardware/usb-power-reset`

#### 屬性 {#properties-6}

| 屬性 | 描述 |
| :-- | :-- |
| **duration** (time) | 重新啟用 USB 前的斷電持續時間 |
| **bus**(number) | USB 匯流排號 |
| **slot**(number) | 總線上的 USB 埠/插槽號 |
