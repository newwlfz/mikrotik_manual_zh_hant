---
sidebar_key: "containers/user-guides/container-homeassistant"
sidebar_position: 4
title: "容器 - HomeAssistant"
sidebar_label: "容器 - HomeAssistant"
description: "本頁介紹 MikroTik RouterOS 中的容器功能，使使用者能夠直接在路由器上執行 HomeAssistant 等伺服器。它提供了分步說明，涵蓋啟用容器模式、配置網路、設定掛載和環境變數，以及獲取 HomeAssistant Docker 映象。"
tags:
  - 'container'
  - 'homeassistant'
source: https://manual.mikrotik.com/docs/7.25/containers/user-guides/container-homeassistant
captured_at: '2026-11-04T11:14:59+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 中引入 **container** 功能後，就可以直接在路由器上執行各種伺服器。對於希望儘量減少網路中裝置數量的使用者來說，這一點尤其有價值。現在無需在單獨的機器上部署伺服器，你可以將其託管在路由器內部。

在本指南中，我們將演示如何在 RouterOS 上安裝並執行 **Home‑Assistant** 伺服器。

Home‑Assistant 是一個流行的平臺，用於從大量感測器收集資料，並對廣泛的 **整合** 提供全面支援。

## 概述 {#summary}

在繼續配置之前，請確保已學習我們的 [container](../index.md) 指南。此外，請檢視 [免責宣告](../index.md#disclaimer) 和 [要求](../index.md#requirements) 部分，以瞭解所有相關風險以及你可能需要採取的必要步驟。

你可以在[連結](https://hub.docker.com/r/homeassistant/home-assistant/tags)中找到支援的架構。

本指南釋出時，**home-assistant** 映象適用於 ARM64 和 AMD64（CHR 和 x86）裝置。

根據 [Home Assistant 網站](https://www.home-assistant.io/installation/linux/) 的資訊，推薦要求如下：

- 2 GB RAM
- 32 GB 儲存

但我們將嘗試在配置更低的裝置上執行它。

## 容器配置 {#container-configuration}

**子選單：** `/container`

***注意**:* 需要 **container** 軟體包。

### 容器模式 {#container-mode}

啟用容器模式：

```ros
/system/device-mode/update container=yes
```

如果要在 X86 上使用 container，你需要透過按下復位按鈕或冷重啟來確認 device-mode。

### 網路 {#networking}

新增 veth 介面：

```ros
/interface/veth/add name=veth2 address=172.19.0.2/24 gateway=172.19.0.1
```

為 container 建立網橋，並將 veth 介面新增到其中：

```ros
/interface/bridge/add name=ha
/ip/address/add address=172.19.0.1/24 interface=ha
/interface/bridge/port/add bridge=ha interface=veth2
```

如果需要 NAT（可選），轉發 TCP 8123 以進行 home-assistant 管理（其中 192.168.88.1 是裝置的 LAN IP 地址）：

```ros
/ip/firewall/nat/add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=8123 protocol=tcp to-addresses=172.19.0.2 to-ports=8123
```

### 環境變數和掛載 {#environment-variables-and-mounts}

根據 home-assistant 文件，為配置檔案定義掛載（其中 `/usb1` 是我們的外部 USB 儲存資料夾）：

```ros
/container/mounts/add dst=/config list=ha_config src=/usb1/ha_config
```

為 home-assistant 建立環境變數：

```ros
/container/envs/add key=TZ list=ha_env value=America/Los_Angeles
```

### 獲取映象 {#getting-image}

為簡化配置，我們將從外部庫獲取映象。

確保已相應設定 "Registry URL"，限制 RAM 使用量（如有必要），併為映象設定目錄：

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=/usb1/pull
```

拉取 home-assistant 映象並等待其解壓完成：

```ros
/container/add remote-image=homeassistant/home-assistant:latest interface=veth2 root-dir=/usb1/ha mountlists=ha_config envlists=ha_env logging=yes
```

執行該命令後，RouterOS 應開始“解壓”軟體包。檢查“File System”中新建的資料夾，並使用命令 `/container/print` 監控容器狀態。

### 啟動容器 {#starting-the-container}

在使用 `/container/print` 確認 container 已新增且狀態變為 `status=stopped` 後 → 即可啟動它：

```ros
/container/start 0
```

### Home-Assistant 設定 {#home-assistant-setup}

開啟你首選的 Web 瀏覽器，並透過指定管理埠 ":8123" 訪問 Home-Assistant 管理門戶：

![](/img/c36eaec2e33c6a0b.webp)

繼續完成設定。更多資訊在 [Home-Assistant 入門指南](https://www.home-assistant.io/getting-started/onboarding/) 中有說明。

## 資源 {#resources}

僅執行 **Home Assistant**（沒有任何負載/流量）就會佔用約 300-400 MB 的 RAM：

```ros
/system/resource/print
                   uptime: 4m27s
                  version: 7.13.3 (stable)
               build-time: 2024-01-24 13:16:46
         factory-software: 7.10
              free-memory: 143.0MiB
             total-memory: 448.0MiB
```
