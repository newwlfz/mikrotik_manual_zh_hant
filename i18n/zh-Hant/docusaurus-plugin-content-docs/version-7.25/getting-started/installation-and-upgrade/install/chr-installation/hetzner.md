---
sidebar_key: "getting-started/installation-and-upgrade/install/chr-installation/hetzner"
sidebar_position: 3
title: "CHR：Hetzner Cloud 安裝"
sidebar_label: "CHR：Hetzner Cloud 安裝"
description: "本頁面概述瞭如何在 Hetzner Cloud 上部署 MikroTik RouterOS Cloud Hosted Router (CHR)，詳細介紹了安裝過程，包括建立伺服器、啟用救援系統、透過 SSH 部署 CHR 映象以及重啟說明，同時強調了安全最佳實踐。"
tags:
  - 'chr'
  - 'vpn'
source: https://manual.mikrotik.com/docs/7.25/getting-started/installation-and-upgrade/install/chr-installation/hetzner
captured_at: '2026-11-04T11:16:19+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#overview}

**[Hetzner Cloud](https://www.hetzner.com/cloud)** 是一個雲計算平臺，提供可擴充套件的虛擬機器基礎設施以及一系列預配置的 Linux 發行版。對於需要高階網路功能的使用者，Hetzner Cloud 也是部署 **RouterOS Cloud Hosted Router (CHR)** 的合適平臺。

Cloud Hosted Router (CHR) 是 MikroTik RouterOS 的一個版本，專為在 x86_64 虛擬化環境中執行而設計。它提供與 MikroTik 硬體裝置相同的核心路由、防火牆、VPN 和管理功能，適合基於雲的聯網、VPN 服務和常規網路管理。

在 Hetzner Cloud 上部署時，CHR 可受益於可擴充套件的虛擬基礎設施，同時保持完整的 RouterOS 功能，使使用者能夠構建靈活且強大的網路解決方案。

## 建立 CHR 虛擬機器 {#create-a-chr-virtual-machine}

1. **建立 Hetzner Cloud 伺服器**  
   在 Hetzner Cloud 上開始建立新伺服器。所有可用的伺服器選項都可以使用。
2. **啟用救援系統**
   - 在 Hetzner Cloud 管理介面中，透過選擇 **ENABLE RESCUE & POWER CYCLE** 來啟用 **Enable Rescue** 系統。
   - 選擇 `linux64` 作為救援作業系統。
   - 系統將顯示使用者名稱和密碼。使用這些憑據透過 SSH 登入救援系統。
3. **安裝 Cloud Hosted Router (CHR)**
   - 登入救援系統後，下載 CHR **RAW** 磁碟映像，並使用以下命令將其寫入雲伺服器的系統磁碟：

   ```bash
   curl -L https://download.mikrotik.com/routeros/7.21.4/chr-7.21.4.img.zip | funzip | dd of=/dev/sda bs=1M
   ```

   >`/dev/sda` 裝置名稱可能因雲服務提供商配置而異。

:::warning
   將 URL 替換為 MikroTik [下載頁面](https://mikrotik.com/download) 上可用的最新 CHR 版本的連結。
   :::

## 重啟伺服器 {#reboot-the-server}

安裝完成後，透過執行 `reboot` 命令重啟伺服器。
:::warning
立即[保護你的 RouterOS](../../../securing-your-router.md) 安裝至關重要！
:::

請務必保持 RouterOS 更新，並遵循最佳安全實踐，以維護伺服器的安全性和效能。
