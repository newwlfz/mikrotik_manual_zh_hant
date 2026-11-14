---
sidebar_key: "management-tools/flashfig"
sidebar_position: 8
title: "FlashFig"
sidebar_label: "FlashFig"
description: "FlashFig 是一款 Windows 實用工具，用於透過二層網路在數秒內傳輸 RouterOS 設定，從而對 MikroTik RouterBOARD 進行快速、大批次配置。它支援 flash-boot 模式以實現自動化配置，並提供了在較舊型號上啟用該模式的詳細說明以及使用指令碼的方法。"
tags:
  - 'flashfig'
source: https://manual.mikrotik.com/docs/7.24/management-tools/flashfig
captured_at: '2026-11-04T11:32:10+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 描述 {#description}

FlashFig 是一款基於 Windows 的實用工具，專為大批次配置 MikroTik RouterBOARD 而設計。它面向 MikroTik 分銷商、網際網路服務提供商以及其他需要快速向多臺裝置部署 RouterOS 配置的組織。

當 RouterBOARD 進入 flash‑boot 模式，並在承載 FlashFig 的二層廣播域內上電時，應用程式會在約三秒內將目標 RouterOS 配置檔案傳輸到裝置。因此，只需將每個 RouterBOARD 連線到同一二層網路併為啟用了 FlashFig 的裝置供電，就可以併發批次配置路由器。

FlashFig 實用工具可從 MikroTik [下載](https://mikrotik.com/download)頁面下載。

自 2010 年 3 月起生產的所有 RouterBOARD 裝置預設啟用 FlashFig 模式。對於較舊型號，可透過 [路由器主機板](../hardware/routerboard.md#settings) 設定或 RouterOS 控制檯命令將 *boot-device* 設定為 `flash‑boot` 或 `flash‑boot‑once‑then‑nand` 來啟用 FlashFig：*`/system/routerboard/settings/set boot-device=flash-boot-once-then-nand`* 或 *`/system/routerboard/settings/set boot-device=flash-boot`*。

:::info
從 RouterOS/RouterBOOT **v7.16** 開始，在每次由軟體發起的系統重設後，flash boot 模式都會像出廠時一樣被啟用。使用復位按鈕重設路由器時也會啟用相同模式（需要 bootloader 版本 v7.16 或更高）。
請注意，如果你在給路由器上電前按住復位按鈕，則會使用備份 booter。此時，備份 booter 韌體（出廠時安裝）也必須為 v7.16 或更高版本。
:::

全新 RouterBOARD 上的 FlashFig 模式只會在首次成功使用者登入或成功執行 FlashFig 後，在後續啟動時被停用，以避免之後發生不必要的重新配置。要在同一路由器上第二次使用 FlashFig，需要在 [路由器主機板](../hardware/routerboard.md#settings) 設定中啟用 **flash-boot**（成功更改配置後或任何使用者登入到板卡後，此設定將恢復為 NAND）。

如果之後使用 RouterOS *reset-configuration* 命令（或使用 Reset 按鈕重設配置），則會載入 FlashFig 配置。要永久覆蓋，請使用 Netinstall 流程並勾選 *Apply default configuration*，或在基於 Linux 的命令列中使用 *-r* 標誌。

從 RouterOS/FlashFig 7.22 開始，可以使用 Mode 指令碼配置 **device‑mode** 和 **protected‑routerboot** 以及其他設定。Mode 指令碼會在任何自定義或預設配置指令碼之前執行。完成後，該指令碼會自動從裝置中移除。如果指令碼修改了 device-mode，裝置將在執行後立即重啟。

你可以在 MikroTik YouTube 頻道觀看 FlashFig [影片教程](https://www.youtube.com/watch?v=gticPeOdN54)。

### FlashFig 示例 {#flashfig-example}

以下是一個分步示例，說明如何使用 FlashFig 流程將選定的 MikroTik RouterOS 配置應用到“出廠全新”的 RouterBOARD。

##### 要求 {#requirements}

Windows 計算機必須配備以下埠幷包含以下檔案：

- 一個可用的乙太網埠。
- 有效的 *Config* 和/或 *Mode* 指令碼檔案，其中包含與 [匯出/匯入檔案](../getting-started/configuration-management/index.md#configuration-export-and-import) 類似的 MikroTik RouterOS 配置。除了有效的 MikroTik RouterOS CLI 命令外，還可以使用只讀變數 *$defconfPassword* 和 *$defconfWifiPassword* 重新應用出廠密碼；
- 始終使用從 [下載](https://mikrotik.com/download)頁面獲取的最新 FlashFig 程式。
- RouterBOARD 必須處於 flash-boot 模式。如果這是首次啟動，則無需執行任何操作。

:::info
請注意文字編輯器對 CR/LF 字元的處理方式，並在透過 FlashFig 應用之前，先在相同版本的 RouterOS 上正常應用該配置並測試其沒有錯誤，因為執行時錯誤將不可見！
:::

##### 預配置 {#pre-configuration}

###### Windows 計算機 {#windows-computer}

- 執行 FlashFig。
- 準備 *Config* 和/或 *Mode* 指令碼 **.rsc** 檔案。*Config* 和/或 *Mode* 指令碼檔案是[常規/匯入檔案](../getting-started/configuration-management/index.md#configuration-export-and-import)，它接受有效的 MikroTik RouterOS CLI 命令。你可以使用任何文字編輯器程式（Notepad、Notepad++、Text Editor、TextEdit、Microsoft Word、OpenOffice Writer）建立 .rsc 檔案。

![](/img/9ac639cc13e6d13c.png)

- 分配 **Boot Client Address**，該地址應處於*與計算機乙太網介面上配置的子網相同的子網*內。

![](/img/459f357dafb12f62.png)

- **Browse** 選擇 *Config* 和/或 *Mode* 指令碼 **.rsc** 檔案

![](/img/5b58ab491c2a5392.png)

- 高亮 *Config* 指令碼檔案並點選 **Select Config**，高亮 *Mode* 指令碼檔案並點選 **Select Mode**。

![](/img/3f5383fa37a24c0f.png)

- 啟用 FlashFig 伺服器。現在即可進行 FlashFig。注意：當任何 RouterBOARD 在 boot-device 配置為 **flash-boot** 或 **flash-boot-once-then-nand** 的情況下上電時，它都會在網路中接受 FlashFig 處理。

![](/img/1a7ee92b57c059e9.png)

##### RouterBOARD {#routerboard}

- 每臺 RouterBOARD 出廠時預設啟用 FlashFig 模式，這意味著 RouterBOARD 上**無需配置**。

- 如果你的路由器未啟用 FlashFig，請使用 WinBox/Console 訪問 RouterBOARD，並將 [boot-device](../hardware/routerboard.md#settings) 更改為 *flash-boot* 或 *flash-boot-once-then-nand*：

```ros
/system/routerboard/settings/set boot-device=flash-boot
```

或者使用更可取的單次啟動 flash-boot 選項：

```ros
/system/routerboard/settings/set boot-device=flash-boot-once-then-nand
```

你的路由器現在已準備好進行 FlashFig。

##### 連線 {#connect}

將 RouterBOARD 的 ***Boot*** 埠與 FlashFig 計算機連線到同一區域網路。

##### 執行 FlashFig {#run-flashfig}

- 為 RouterBOARD 接通電源。
- 在 FlashFig 程式中檢查狀態。

![](/img/2d128f6e3034cca9.png)

訊息日誌顯示“Flashfigged”，並且 RouterBOARD 應反覆發出字元“/”的摩爾斯電碼聲音（“\_..\_.”並閃爍 LED）——現在可以安全地拔掉電源/關閉路由器：

- FlashFig **配置**已應用到 RouterBOARD，它已**準備好**使用此新配置投入生產。

### 故障排除 {#troubleshoot}

#### FlashFig 找不到路由器 {#flashfig-can-not-find-a-router}

如果 PC 和路由器之間還有另一臺裝置（路由器/交換器），請確保對於該裝置：

- DHCP 伺服器已停用。
- 如果使用的埠位於網橋中，請將網橋 *protocol-mode* 設定為 *none*。
- 已停用所用埠的 HW-offload。

#### FlashFig 找到路由器，但未完成刷寫（沒有 TFTP 請求） {#flashfig-finds-a-router-flashing-is-not-done-no-tftp-request}

確保執行 FlashFig 的計算機只有一個活動的網路介面。

#### FlashFig 已完成，但配置未應用 {#flashfig-is-done-but-a-configuration-is-not-applied}

如果所有步驟都成功，但 .rsc 檔案中的 RouterOS 配置未應用，請向 \*.rsc 配置檔案新增[啟動延遲](../getting-started/configuration-management/index.md#startup-delay)。原因可能是配置指令碼在所有介面啟動之前就被執行。

#### Flash 空間不足，已忽略 {#not-enough-flash-space-ignoring}

FlashFig 配置的最大檔案大小可達 4000 位元組，否則程式將返回如上錯誤。
