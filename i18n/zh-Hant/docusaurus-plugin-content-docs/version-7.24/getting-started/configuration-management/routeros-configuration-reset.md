---
sidebar_key: "getting-started/configuration-management/routeros-configuration-reset"
sidebar_position: 5
title: "RouterOS 配置重設"
sidebar_label: "RouterOS 配置重設"
description: "本頁提供了重設 MikroTik RouterOS 配置的全面說明，涵蓋物理按鍵方法以及 GUI/CLI 命令。它詳細介紹了每種重設操作對應的 LED 指示燈、backup loader 步驟、舊型號上的跳線孔用法，以及用於無線網路接入的 WPS 功能。"
tags:
  - 'reset-configuration'
  - 'led'
source: https://manual.mikrotik.com/docs/7.24/getting-started/configuration-management/routeros-configuration-reset
captured_at: '2026-11-04T11:28:42+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 如何重設配置 {#how-to-reset-configuration}

要將 RouterOS 重設為出廠預設值（包括移除當前密碼），請按以下步驟操作：

1. 斷開裝置電源。
2. 按住復位按鈕。

![Reset button](/img/5ead5bc05d6b5895.png)

1. 在按住按鈕的同時，重新給裝置通電。
2. 觀察 LED。其中一個 LED（通常是 USR/User LED）將開始閃爍。
3. 當 LED 開始閃爍時，鬆開復位按鈕。

裝置將使用預設配置重新啟動。

## 從 RouterOS 重設 {#reset-from-routeros}

如果仍能訪問裝置，可以直接從 RouterOS 恢復預設配置：

- 在終端中執行以下命令：**`/system/reset-configuration`**

- 或在 **[WinBox](../../management-tools/winbox.md)** 或 **[WebFig](../../management-tools/webfig.md)** 中導航到 **系統 → 重設配置**。

## 使用復位按鈕 {#using-the-reset-button}

MikroTik 裝置配有復位按鈕，根據啟動期間按住時間的長短，它可以執行多種功能。

:::tip
觀看官方 MikroTips 系列：[復位序列](https://youtu.be/6Unz92rABs8)。
:::

### 載入備份 RouterBOOT Loader {#load-the-backup-routerboot-loader}

在通電前按住復位按鈕，約 3 秒後鬆開。這樣會載入備份 RouterBOOT Loader。

如果裝置因 RouterBOOT 升級失敗而無法啟動，這會很有用。使用備份載入器啟動後，你可以在 RouterBOARD 設定中強制使用備份載入器，或從 `.fwf` 檔案重新安裝 RouterBOOT。

### 重設 RouterOS 配置 {#reset-the-routeros-configuration}

按住復位按鈕，直到 LED 開始閃爍，然後鬆開。裝置會將其 RouterOS 配置重設為出廠預設值。

### 啟用 CAPs 模式 {#enable-caps-mode}

在 LED 開始閃爍後，繼續按住按鈕約 **5 秒**。當 LED 變為常亮時，鬆開按鈕以啟用 **[CAPs 模式](../../wireless/abgn/capsman/index.md)**。

**CAPs 模式**也可以透過命令列啟用：`/system/reset-configuration caps-mode=yes`

### 啟動 Netinstall 模式 {#start-netinstall-mode}

在給裝置通電時按住復位按鈕。繼續按住按鈕，直到 LED 序列完成（通常為閃爍 → 常亮 → 熄滅），然後鬆開。

裝置將進入 Netinstall 模式，並開始在網路上搜尋 Netinstall 伺服器。

:::tip
觀看官方 MikroTips 系列：[Netinstall](https://youtu.be/gzlLbIf3Dbk)。
:::

有關詳細的 Netinstall 操作說明，請參閱 **[Netinstall 文件](../installation-and-upgrade/netinstall/index.md)**。

## 復位跳線方法 {#reset-jumper-method}

較舊的 RouterBOARD 型號還配有復位跳線孔。某些裝置可能需要開啟外殼。RB750/RB951/RB751 的跳線孔位於外殼的一個橡膠腳墊下方。

使用金屬螺絲刀短接復位跳線，並啟動板卡，直到配置被清除：  

![](/img/61678bee6d9ce0df.jpg) ![](/img/1427924e57ac32a1.jpg)

### 較舊型號的跳線復位 {#jumper-reset-for-older-models}

下圖顯示了較舊 RouterBOARD（如 RB133C）上覆位跳線的位置：

![](/img/7710f08056600f89.jpg)

:::danger
配置重設後，不要忘記移除跳線，否則每次重啟時配置都會被重設！
:::

### WPS {#wps}

某些裝置配有 WPS 按鈕，或具有 WPS 功能的復位按鈕，可用於簡化無線用戶端連線，無需手動輸入密碼。某些型號還支援裝置之間的 WPS 同步。
有關 WPS 和復位按鈕功能的型號特定資訊，請參閱裝置的[使用者手冊](/hardware/)。
