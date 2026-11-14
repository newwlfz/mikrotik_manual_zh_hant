---
sidebar_key: "system-information-and-utilities/partitions"
sidebar_position: 11
title: "分割區"
sidebar_label: "分割區"
description: "RouterOS 允許在相容裝置上重新分割區 NAND 快閃記憶體，以支援多個作業系統安裝並具備自動回退功能，從而確保升級期間的系統可靠性。該功能最多支援 8 個分割區，要求最低儲存容量，幷包含用於管理活動分割區、克隆配置和恢復備份的命令。"
tags:
  - 'partitions'
  - 'storage'
source: https://manual.mikrotik.com/docs/system-information-and-utilities/partitions
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

分割區功能在 ARM、ARM64、MIPS、TILE 和 PowerPC 且使用 NAND 快閃記憶體的 RouterBOARD 裝置上受支援。

RouterOS 允許對 NAND 快閃記憶體重新分割區，從而支援：

- 每個分割區上獨立的 RouterOS 安裝。
- 能夠指定主分割區和回退分割區。

如果某個分割區啟動失敗（由於升級失敗、配置問題或軟體錯誤），下一個分割區將自動啟動，提供回退。此功能充當互動式備份，使你能夠保留已驗證且可正常工作的安裝，並僅在輔助分割區上執行升級。

確認新配置穩定後，你可以使用 "Save Config To" 功能將其複製到其他分割區。

:::warning
NAND 重新分割區需要最新的載入程式版本
:::

#### 要求和限制 {#requirements-and-limits}

- 從 RouterOS 7.20beta2 開始，重新分割區的最小儲存大小為 128 MiB。
- 重新分割區期間 RouterOS 分割區最小大小：60 MiB。
- 允許的最大分割區數為 8。

對於本應隱藏 Partitions 選單但之前已重新分割區的裝置：

- 可以將裝置重新分割區為單個分割區。

- 重啟後 Partitions 選單將隱藏。

#### 示例 {#example}

對於 NAND 為 128 MiB、之前具有 4\*32 MiB 分割區且 RouterOS 可容納在 32 MiB 內的裝置，從 RouterOS 7.20beta2 開始，升級後的行為如下：

- 它將繼續使用全部 4 個分割區，並具備完整分割區選項，與重新分割區前一樣。
- 如果進行重新分割區，唯一可用的選項將是 1\*128 MiB 或 2\*64 MiB 分割區，並且完整分割區功能仍將可用。

```ros
[admin@MikroTik] > /partitions/print
Flags: A - ACTIVE; R - RUNNING
Columns: NAME, FALLBACK-TO, VERSION, SIZE
# NAME FALL VERSION SIZE 
0 AR part0  next         RouterOS v7.18.2 2025-03-11 11:59:04  128MiB
```

:::warning
從 RouterOS 7.17 版本開始，你需要更新 [device-mode](./device-mode.md) 才能使用分割區。
:::

## 在 WinBox 中檢查分割區 {#inspect-partitions-in-winbox}

在左側選單中開啟 **Partition**：

1. 在列表中檢查分割區名稱、**Fallback To** 和已安裝的 RouterOS 版本。`A` 標誌標識活動啟動分割區，`R` 標識正在執行的分割區。截圖顯示了一個分割區 `part0`，它同時具有這兩個標誌。
2. 右側面板包含 **Repartition**、**Copy To**、**Save Config To** 和 **Restore Config From**。這些操作會更改儲存或配置；請使用命令描述來選擇你打算執行的操作。

![WinBox Partition overview with partition details and available actions](/img/1ae61fb9deda8d20.webp)

檢視列表不會對路由器重新分割區。**Repartition** 會重新格式化儲存並重啟裝置，而 **Copy To** 會替換其目標分割區的內容。在計劃更改分割區之前，請檢查硬體支援和裝置模式。

## 命令 {#commands}

| 屬性 | 描述 |
| :-- | :-- |
| **activate** (*partition*) | 將另一個分割區指定為 Active。如果在裝置模式中啟用了 "partitions" 設定（自 RouterOS 7.17 起），則此選項可用。 |
| **repartition** (*integer*) | 將重啟路由器並重新格式化 NAND，只保留活動分割區。 |
| **copy-to** (*partition*) | 將帶有配置的 **running** OS 克隆到指定分割區。該分割區上先前儲存的資料將被擦除。 |
| **save-config-to** (*partition*) | 將 **running-config** 克隆到指定分割區。其他所有內容保持不變。 |
| **restore-config-from** (*partition*) | 將配置從指定分割區複製到 **running** 分割區 |

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **name** (*string*; 預設值： ) | 分割區名稱 |
| **fallback-to** (*etherboot \| next \| partition-name*; 預設值： **next**) | 當活動分割區啟動失敗時的操作：etherboot - 切換到 etherboot；next - 嘗試下一個分割區；回退到指定分割區 |

### 只讀 {#read-only}

| 屬性 | 描述 |
| :-- | :-- |
| **active** (*yes \| no*) | 分割區處於活動狀態 |
| **running** (*yes \| no*) | 當前正在執行的分割區 |
| **size** (*integer[MiB]*) | 分割區大小 |
| **version** (*string*) | 分割區上安裝的當前 RouterOS 版本 |
