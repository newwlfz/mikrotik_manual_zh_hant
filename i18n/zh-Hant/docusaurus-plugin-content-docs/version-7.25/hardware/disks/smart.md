---
sidebar_key: "hardware/disks/smart"
sidebar_position: 1
title: "S.M.A.R.T. 資訊"
sidebar_label: "S.M.A.R.T. 資訊"
description: "RouterOS 中的 S.M.A.R.T. 驅動器健康監控：使用 `/disk smart-info` 命令讀取驅動器健康狀態、溫度、使用情況和錯誤計數器，以及所報告屬性的含義。"
tags:
  - 'storage'
  - 'smart'
  - 'cli'
source: https://manual.mikrotik.com/docs/7.25/hardware/disks/smart
captured_at: '2026-11-04T11:17:18+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

[*S.M.A.R.T. 資訊 CLI 參考*](../../cli-reference/disk/smart-info.md)

S.M.A.R.T.（Self-Monitoring, Analysis and Reporting Technology）是內置於現代儲存驅動器中的監控系統。它可用於讀取驅動器診斷資訊：總體健康狀況、溫度、使用情況、錯誤計數器，對於 NVMe 驅動器還包括 SMART/Health 屬性。

:::info
S.M.A.R.T. 資訊需要 [儲存](../../storage/index.md) 軟體包。
:::

對於任何支援 S.M.A.R.T. 的已連線儲存裝置，可使用 `/disk/smart-info` 命令讀取診斷資訊：

```ros
[admin@MikroTik] > /disk/smart-info nvme1
```

```ros
[admin@R2DUTRDS22162XG4S4XS2XQ20DISKS] > disk/smart-info nvme1
Columns: OUTPUT
OUTPUT                                                                     
smartctl 7.1 2019-12-30 r5022 [aarch64-linux-5.6.3] (local build)          
Copyright (C) 2002-19, Bruce Allen, Christian Franke, www.smartmontools.org
=== START OF INFORMATION SECTION ===                                       
Model Number:                       U.2 SSD 4TG2-P                         
Serial Number:                      <S/N>                      
Firmware Version:                   E21T4C                                 
PCI Vendor/Subsystem ID:            0x1bc0                                 
IEEE OUI Identifier:                0x24693e                               
Controller ID:                      0                                      
Number of Namespaces:               1                                      
Namespace 1 Size/Capacity:          960,197,124,096 [960 GB]               
Namespace 1 Formatted LBA Size:     512                                    
Namespace 1 IEEE EUI-64:            <EUI-64>                  
Firmware Updates (0x02):            1 Slot                                 
Optional Admin Commands (0x0017):   Security Format Frmw_DL Self_Test      
Optional NVM Commands (0x0054):     DS_Mngmt Sav/Sel_Feat Timestmp         
Maximum Data Transfer Size:         512 Pages                              
Warning  Comp. Temp. Threshold:     100 Celsius                            
Critical Comp. Temp. Threshold:     110 Celsius                            
Supported Power States                                                     
St Op     Max   Active     Idle   RL RT WL WT  Ent_Lat  Ex_Lat             
 0 +    20.00W       -        -    0  0  0  0        5       5             
Supported LBA Sizes (NSID 0x1)                                             
Id Fmt  Data  Metadt  Rel_Perf                                             
 0 +     512       0         0                                             
=== START OF SMART DATA SECTION ===                                        
SMART overall-health self-assessment test result: PASSED                   
SMART/Health Information (NVMe Log 0x02)                                   
Critical Warning:                   0x00                                   
Temperature:                        33 Celsius                             
Available Spare:                    100%                                   
Available Spare Threshold:          10%                                    
Percentage Used:                    0%                                     
Data Units Read:                    5,774,165 [2.95 TB]                    
Data Units Written:                 10,770,860 [5.51 TB]                   
Host Read Commands:                 75,868,764                             
Host Write Commands:                61,379,337                             
Controller Busy Time:               22                                     
Power Cycles:                       579                                    
Power On Hours:                     4,203                                  
Unsafe Shutdowns:                   105                                    
Media and Data Integrity Errors:    0                                      
Error Information Log Entries:      0                                      
Warning  Comp. Temperature Time:    0                                      
Critical Comp. Temperature Time:    0                                      
Temperature Sensor 1:               45 Celsius                             
Temperature Sensor 2:               33 Celsius                             
Temperature Sensor 3:               33 Celsius                             
Temperature Sensor 4:               34 Celsius                             
Temperature Sensor 5:               34 Celsius                             
Temperature Sensor 6:               35 Celsius                             
Temperature Sensor 7:               32 Celsius                             
Temperature Sensor 8:               31 Celsius                             
Error Information (NVMe Log 0x01, max 64 entries)                          
No Errors Logged      
```

## 讀取輸出 {#reading-the-output}

驅動器健康的重要指標：

- `SMART overall-health self-assessment test result`  -  驅動器會報告其是否認為自身健康。報告 `FAILED` 的驅動器應予以更換。
- `Temperature`  -  驅動器的當前溫度。警告和嚴重閾值列在資訊部分中。
- `Available Spare`  -  驅動器在無法重對映壞塊之前仍有多少備用容量。當其降至 `Available Spare Threshold` 時，驅動器已接近壽命終點。
- `Percentage Used`  -  基於製造商額定耐久度估算的驅動器使用壽命。達到 100% 時，驅動器已達到其額定壽命。
- `Unsafe Shutdowns` 和 `Media and Data Integrity Errors`  -  驅動器意外斷電的頻率以及檢測到的資料錯誤數量。反覆發生不安全關機事項會增加損壞風險。

輸出與 Linux 上 `smartctl` 報告的內容相同，因此適用驅動器廠商的 S.M.A.R.T. 文件。

:::note
某些 USB 硬碟盒無法透傳 S.M.A.R.T. 資訊。如果驅動器位於此類硬碟盒之後，即使驅動器本身支援 S.M.A.R.T.，`/disk/smart-info` 也會報告錯誤。
:::

## 相關內容 {#related}

- [磁碟](./index.md)  -  格式化、掛載和管理驅動器。
