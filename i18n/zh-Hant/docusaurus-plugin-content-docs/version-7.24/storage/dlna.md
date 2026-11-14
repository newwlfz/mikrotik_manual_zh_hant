---
sidebar_key: "storage/dlna"
sidebar_position: 2
title: "DLNA 媒體伺服器"
sidebar_label: "DLNA 媒體伺服器"
description: "該頁面介紹 MikroTik RouterOS 中的 DLNA 媒體伺服器功能，說明其如何使聯網裝置能夠使用 UPnP 協定共享數字媒體。頁面詳細介紹了允許的主機、IP 限制和友好名稱等伺服器設定，並提供了配置多個例項及訪問限制的示例。"
tags:
  - 'dlna'
  - 'media-server'
  - 'upnp'
source: https://manual.mikrotik.com/docs/7.24/storage/dlna
captured_at: '2026-11-04T11:33:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

DLNA（Digital Living Network Alliance，數字生活網路聯盟）是一組網路協定，使裝置能夠共享影片、照片和音樂等數字媒體。DLNA 構建在 UPnP（Universal Plug and Play，通用即插即用）架構之上，該架構提供裝置發現和控制能力。

UPnP 允許裝置在網路中發現彼此並交換控制訊息。它使用 SSDP（Simple Service Discovery Protocol，簡單服務發現協定）進行發現，使用 SOAP（Simple Object Access Protocol，簡單物件訪問協定）傳輸控制訊息，並使用 XML 描述裝置和服務。這使電視、計算機和移動裝置等裝置能夠無縫連線並共享媒體內容。

在 RouterOS 中，你可以啟用媒體伺服器，與電視等家庭裝置或計算機上的 VLC 等播放器應用共享電影或音樂。

:::danger
SMIPS 裝置不支援媒體共享（DLNA）。
:::

## 伺服器設定 {#server-settings}

| 屬性 | 描述 |
| :-- | :-- |
| **allowed-hostname** | 用於限制對特定主機名的訪問。 |
| **allowed-ip** | 用於限制對指定 IP 地址的訪問 |
| **friendly-name** | 將在網路上為 DLNA 伺服器顯示的名稱。 |
| **interface** | 指定 DLNA 伺服器將使用的網路介面 |
| **path** | 儲存媒體內容並從中提供服務的檔案路徑。 |
| **disabled** | 指定條目是否被停用 |

### 建立 DLNA 伺服器 {#creating-a-dlna-server}

要在 MikroTik 路由器上啟用 DLNA 媒體流，請使用 `/ip media add` 命令。該命令配置一個媒體伺服器，使網路中的 DLNA 相容裝置能夠發現並訪問儲存在已連線 USB 儲存上的媒體檔案。將 `Mikrotik` 替換為你的媒體伺服器的描述性名稱，將 `bridge1` 替換為你希望用於媒體發現的橋接介面，將 `usb1` 替換為媒體檔案所在的 USB 儲存路徑。

```ros
/ip/media/add friendly-name=Mikrotik interface=bridge1 path=usb1
```

### 建立帶訪問限制的多個 DLNA 伺服器例項 {#creating-multiple-dlna-server-instances-with-access-limitations}

此示例演示如何配置具有特定訪問限制的獨立 DLNA 伺服器例項。使用場景：限制兒童電視只能訪問儲存在 "usb1/kids" 資料夾中的兒童友好媒體。

```ros
/ip/media/add friendly-name=adults interface=bridge1 path=usb1/adults allowed-hostname=ADULTS_TV
/ip/media/add friendly-name=kids interface=bridge1 path=usb1/kids allowed-hostname=KIDS_TV
```
