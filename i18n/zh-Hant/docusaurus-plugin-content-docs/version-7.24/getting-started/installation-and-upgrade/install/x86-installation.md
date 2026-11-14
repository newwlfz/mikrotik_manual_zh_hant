---
sidebar_key: "getting-started/installation-and-upgrade/install/x86-installation"
sidebar_position: 2
title: "x86 安裝"
sidebar_label: "x86 安裝"
description: "本頁面提供了在 x86 硬體上使用 USB 或 Netinstall 安裝 RouterOS 的分步指南，涵蓋 Windows/Linux/macOS 方法、BIOS 設定調整以及用於成功安裝的啟動優先順序配置。"
tags:
  - 'usb'
  - 'installation'
  - 'boot-priority'
source: https://manual.mikrotik.com/docs/7.24/getting-started/installation-and-upgrade/install/x86-installation
captured_at: '2026-11-04T11:28:40+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## USB {#usb}

### 分步指南 {#step-by-step-guide}

1. 從下載頁面下載 x86 CD 映象檔案：https://mikrotik.com/download

    - 在 Windows 系統上：

        - 下載 Rufus：https://github.com/pbatard/rufus/releases（使用最新版本）
        - 連線 USB 驅動器並開啟 Rufus
        - 選擇已下載的 ISO 映象並點選 **START**

    - 在 Linux、FreeBSD 或 macOS 系統上：

        :::danger
        警告！請仔細核對正確的裝置地址——`dd` 可能會不可逆地破壞資料。
        :::

        - 連線 USB 驅動器並識別其裝置地址

            macOS：

            ```text
            diskutil list
            ```

            Linux / FreeBSD：

            ```text
            fdisk -l
            ```

        - 在使用 `dd` 命令之前，請確保 USB 驅動器已格式化且所有舊資料已擦除

    使用 `dd` 將映象寫入磁碟：

    ```bash
    dd if=<your_downloaded_routeros_ISO> of=<disk_address> bs=1M status=progress
    ```

    macOS：

    ```bash
    dd if=<your_downloaded_routeros_ISO> of=<disk_address> bs=1m status=progress
    ```

    過程完成後，將 USB 驅動器連線到你的 x86 系統並從中啟動。

    按鍵盤上的 **"i"** 繼續安裝。

    重啟後，RouterOS 將安裝完成。

啟動優先順序應在 BIOS 設定中調整。如果 RouterOS 安裝在 NVMe 驅動器上，則必須以 UEFI 模式啟動 USB。

確保在 BIOS 啟動設定中停用 CSM（相容性支援模組）。

## 使用 Netinstall 安裝 x86 系統 {#install-the-x86-system-using-netinstall}

1. 下載適用於你係統的 Netinstall 工具，並在你的 PC 上執行它
2. 從下載頁面下載 x86 CD 映象檔案：https://mikrotik.com/download
3. 將 PC 的 BIOS 啟動選項設定為 PXE
4. 儲存更改並重啟
5. 按照 Netinstall 工具的步驟繼續操作
