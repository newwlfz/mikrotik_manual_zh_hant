---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/downgrading-routeros"
sidebar_position: 20
title: "降級 RouterOS"
sidebar_label: "降級 RouterOS"
description: "瞭解如何將 RouterOS 降級到以前的版本，包括降級前檢查、架構驗證和分步說明。"
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/downgrading-routeros
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS **只能降級到硬體支援的最低版本**。使用以下命令檢查：

```ros
/system/resource/print
                   uptime: 2m18s
                  version: 7.26beta1
               build-time: 2026-10-01 13:29:47
          minimum-version: 7.0.9
              free-memory: 681.8MiB
             total-memory: 1024.0MiB
                      cpu: ARM64
                cpu-count: 4
            cpu-frequency: 864MHz
                 cpu-load: 3%
           free-hdd-space: 91.8MiB
          total-hdd-space: 128.0MiB
  write-sect-since-reboot: 64
         write-sect-total: 266154
               bad-blocks: 0%
        architecture-name: arm64
               board-name: hAP ax^2
                 platform: MikroTik
```

`minimum-version` 欄位是硬體載入程式支援的最舊 RouterOS 版本。確切值取決於裝置。在較早的 RouterOS 版本中，同一值顯示為 `factory-software`——如果你的版本仍會輸出該欄位，請將其視為完全相同。

:::warning
嘗試安裝低於 `minimum-version` 的版本可能導致嚴重的系統不穩定，甚至使裝置變磚。
:::

## 開始之前 {#before-you-start}

- **備份所有內容。** 配置語法在主版本之間會發生變化。直接降級可能會損壞設定。繼續操作前，請生成[二進位制備份 (`.backup`)](../getting-started/configuration-management/backup.md)和[匯出檔案 (`.rsc`)](../getting-started/configuration-management/index.md#configuration-export)。
- **安全與穩定性。** 請記住，回退到舊版本會使你的路由器暴露於較舊的軟體缺陷和已修補的安全漏洞。

## 降級步驟 {#downgrade-procedure}

1. **驗證架構。** 檢查 `/system/resource/print` 的 `architecture-name` 欄位（例如 `arm64`、`arm`、`mipsbe`、`mmips`、`x86`）。
2. **下載軟體包。** 從 [MikroTik 下載頁面](https://mikrotik.com/download) 下載適用於該架構和目標舊版本的 **主捆綁包**——它包含 `routeros-<version>-<architecture>.npk` 系統軟體包。檢查 `/system/package/print` 以瞭解路由器上安裝的其他軟體包，並從 "Extra packages" 捆綁包中下載同一目標版本的每個軟體包。在帶 WiFi 的裝置上，這包括無線驅動包（`wifi-qcom`、`wifi-qcom-ac` 或 `wireless`，具體取決於裝置）；其他常見的額外軟體包有 container、calea 和 cmr。
3. **上傳檔案。** 透過 WinBox、WebFig 或 FTP 用戶端連線到路由器，開啟 Files 選單，並上傳 `.npk` 檔案：主 `routeros` 軟體包以及第 2 步中的每個額外軟體包。
4. **執行降級。** 執行命令並確認提示：

   ```ros
   /system/package/downgrade
   ```

   路由器會提示重啟。在重啟期間，它會檢查上傳的軟體包，並將 RouterOS 降級到這些軟體包所包含的版本。
5. **等待重啟。** 路由器會重新啟動，解包舊版本，並在降級完成後重新上線。

重啟後，使用 `/system/resource/print` 驗證新版本，並確認 `version` 欄位顯示預期的降級目標。
