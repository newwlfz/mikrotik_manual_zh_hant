---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/watchdog"
sidebar_position: 19
title: "看門狗"
sidebar_label: "看門狗"
description: "RouterOS 配置中的 Watchdog 頁面允許設定由無響應的 IP 地址或軟體卡死觸發的系統重啟，並提供 ping 監控和透過電子郵件自動生成支援輸出檔案的選項。"
tags:
  - 'watchdog'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/watchdog
captured_at: '2026-11-04T11:28:06+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/system/watchdog`

此選單允許將系統配置為在特定 IP 地址無響應時，或在檢測到軟體卡死時進行重啟。檢測透過兩種方式完成：

- 軟體看門狗定時器（通常由硬體故障引起）：裝置可以透過重啟自行恢復。
- Ping 看門狗可以監視與特定 IP 地址的連通性，並觸發重啟功能。

:::info
**注意：** 這是兩種不同的看門狗功能，各自擁有獨立的設定。預設情況下軟體看門狗已啟用，而 ping 看門狗已停用。你可以透過指定 IP 地址來啟用 ping 看門狗，也可以透過取消 Watchdog Timer 選項來停用軟體看門狗。

**重要：** **注意：** 看門狗重啟並非系統故障。此類重啟也不會生成 autosupout 檔案。看門狗重啟是由作業系統在某些服務未能按其應有速度響應時自動觸發的 `/system/reboot`。其原因可能多種多樣，包括硬體損壞、某些服務的軟體實現緩慢、DDoS 攻擊、配置錯誤等。
:::

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **auto-send-supout** (*yes \| no*；預設值：**no**) | 支援輸出檔案自動生成後，可透過電子郵件傳送。 |
| **automatic-supout** (*yes \| no*；預設值：**yes**) | 當發生軟體故障時，會自動生成名為 "autosupout.rif" 的檔案。先前的 "autosupout.rif" 檔案會被重新命名為 "autosupout.old.rif"。 |
| **no-ping-delay** (*time*；預設值：5m) | 指定在嘗試訪問 watch-address 之前等待多長時間。 |
| **ping-timeout** (*time*；預設值：60s) | 指定在該時間間隔內裝置將被 ping 6 次（在 "no-ping-delay" 之後）。 |
| **send-email-from** (*string*；預設值：) | 用於傳送支援輸出檔案的電子郵件地址。如果未設定，則使用 `/tool/e-mail` 中設定的值。 |
| **send-email-to** (*string*；預設值：) | 接收支援輸出檔案的電子郵件地址。 |
| **send-smtp-server** (*string*；預設值：) | 用於傳送支援輸出檔案的 SMTP 伺服器地址。如果未設定，則使用 `/tool/e-mail` 中設定的值。 |
| **watch-address** (*IP*；預設值：) | 如果連續 6 次 ping 給定 IP 地址均失敗，系統將重啟。如果設定為 none，則此功能被停用。預設情況下，如果設定了 watch-address 且其不可達，路由器將每 6 分鐘重啟一次。 |
| **watchdog-timer** (*yes \| no*；預設值：**yes**) | 系統在一分鐘內無響應時是否重啟。 |

## 快速示例 {#quick-example}

要讓系統在發生軟體崩潰時生成支援輸出檔案，並透過 192.0.2.1 自動傳送到 support@example.com：

```ros
[admin@MikroTik] /system/watchdog/set auto-send-supout=yes \
\... send-email-to=support@example.com send-smtp-server=192.0.2.1
[admin@MikroTik] /system/watchdog> print
      watch-address: none
     watchdog-timer: yes
      no-ping-delay: 5m
   automatic-supout: yes
   auto-send-supout: yes
   send-smtp-server: 192.0.2.1
      send-email-to: support@example.com
```
