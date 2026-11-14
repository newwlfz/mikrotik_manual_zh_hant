---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/downgrading-routeros"
sidebar_position: 20
title: "降級 RouterOS"
sidebar_label: "降級 RouterOS"
description: "瞭解如何將 RouterOS 降級到以前的版本，包括降級前檢查、架構驗證和分步說明。"
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/downgrading-routeros
captured_at: '2026-11-04T11:15:13+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

你可以降級 RouterOS，**但只能降級到出廠安裝版本**，可透過以下命令檢查：

```ros
/system/resource/print

          uptime: 1w1d11h11m1s
         version: 7.23.1 (stable)
      build-time: Jan/01/2026 11:11:11
factory-software: 7.20.8
```

:::warning
factory-software 版本是硬體載入程式支援的絕對最舊版本。嘗試安裝比此更舊的版本可能導致嚴重的系統不穩定或使裝置變磚。
:::

## 降級前檢查清單 {#pre-downgrade-checklist}

- **備份所有內容。** 主版本之間配置語法會發生變化。直接降級可能會損壞設定。繼續操作前，請務必生成[二進位制備份（`.backup`）](../getting-started/configuration-management/backup.md)和[匯出檔案（`.rsc`）](../getting-started/configuration-management/index.md#configuration-export)。
- **安全性和穩定性。** 請記住，回退到舊版本會使你的路由器暴露於較舊的軟體缺陷和已修復的安全漏洞。

## 分步降級流程 {#step-by-step-downgrade-procedure}

1. **驗證架構。** 透過 `/system/resource/print` 檢查裝置的架構型別（查詢 `architecture` 欄位，例如 `arm64`、`mipsbe`、`mmips`）。
2. **下載軟體包。** 從 [MikroTik 下載頁面](https://mikrotik.com/download)下載與該確切架構以及你的目標舊版本對應的 "Extra packages" 或主捆綁包 zip。
3. **上傳檔案。** 透過 WinBox、WebFig 或 FTP 用戶端連線到路由器，開啟 Files 選單，並上傳所有必需的 `.npk` 檔案。
4. **執行降級。** 在終端中執行降級命令序列：

   ```ros
   /system/package/downgrade
   ```

5. **重啟。** 出現提示時確認該操作。執行 `/system/reboot` 重啟路由器——它將解包舊版本，並在降級完成後重新上線。

重啟後，透過執行 `/system/resource/print` 並確認 `version` 欄位反映預期的降級目標版本，來驗證新版本。
