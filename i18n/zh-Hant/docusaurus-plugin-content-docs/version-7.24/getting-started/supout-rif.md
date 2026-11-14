---
sidebar_key: "getting-started/supout-rif"
sidebar_position: 10
title: "Supout.rif"
sidebar_label: "Supout.rif"
description: "`supout.rif` 檔案是一種 MikroTik 二進位制診斷工具，包含路由器配置、日誌以及可幫助支援團隊高效解決問題的詳細資訊。它可以透過 WinBox、WebFig 或控制檯生成，並可使用 Supout.rif 檢視器在不包含敏感資料的情況下檢視。"
tags:
  - 'supout-rif'
  - 'debugging'
source: https://manual.mikrotik.com/docs/7.24/getting-started/supout-rif
captured_at: '2026-11-04T11:29:20+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 什麼是 supout.rif 檔案？ {#what-is-a-supoutrif-file}

supout.rif 檔案是用於偵錯 RouterOS 並加快問題解決的 MikroTik 支援輸出檔案。此二進位制檔案包含路由器的完整配置、日誌以及其他詳細資訊，可幫助 MikroTik 支援團隊更高效地診斷和解決問題。

該檔案儲存在路由器上，可透過 FTP 或 WinBox 下載。在具有 FLASH 型別記憶體或外部儲存的裝置上，你可以透過指定完整路徑（例如 name=flash/supout.rif）在 /flash 資料夾中生成該檔案。

要檢視檔案內容，請登入你的 MikroTik 賬戶，並使用左側導航欄中的“Supout.rif viewer”工具上傳並分析該檔案。

**注意：** supout.rif 檔案不包含路由器密碼等敏感資訊。

## 建立支援輸出檔案 {#creating-a-support-output-file}

### WinBox {#winbox}

要在 Winbox 中生成此檔案，請點選“Make Supout.rif”。

要將檔案儲存到計算機，請右鍵點選該檔案並選擇“Download”以獲取支援輸出檔案，或直接將檔案拖到桌面。

### ![](/img/32c76482e5bb24ff.webp)WebFig {#webfig}

要在 Webfig 中生成此檔案，請點選“Make Supout.rif”，然後點選“Download”將其下載到計算機。

![](/img/cd25509ae01612e9.webp)

![](/img/24e5e1b472982cb2.webp)

### 控制檯 {#console}

要生成此檔案，請在命令列中輸入：

```ros
/system/sup-output name=supout.rif
```

如果你在 supout viewer 中開啟該檔案，而輸出內容太窄，那麼你可以重新生成 supout 檔案，並使用 output-width 選項手動指定輸出寬度：

```ros
/system/sup-output name=supout.rif output-width=300
```
