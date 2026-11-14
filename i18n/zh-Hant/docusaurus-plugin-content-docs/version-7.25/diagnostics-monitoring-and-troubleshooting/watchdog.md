---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/watchdog"
sidebar_position: 19
title: "看門狗"
sidebar_label: "看門狗"
description: "Watchdog 會在系統停止響應或某個 IP 地址停止響應 ping 時重啟路由器，並在軟體故障後寫入支援輸出檔案。"
tags:
  - 'watchdog'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/watchdog
captured_at: '2026-11-04T11:15:33+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

當系統停止響應時，watchdog 會自行重啟路由器，共分兩種情況，每種情況在 `/system/watchdog` 中都有各自的設定：

- 當系統停止響應時，軟體看門狗定時器（software watchdog timer）會重啟路由器。這通常由硬體故障引起，重啟可讓裝置自行恢復。該功能預設開啟（`watchdog-timer=yes`）。
- 當某個 IP 地址停止響應 ping 時，ping 看門狗會重啟路由器。該功能預設關閉（`watch-address=none`）。

看門狗重啟是一次自動的 `/system/reboot`，並非軟體故障。看門狗定時器之所以重啟路由器，是因為某項服務沒有按其應有的速度響應。原因可能是硬體損壞、服務的軟體實現緩慢、DDoS 攻擊、配置錯誤等。

## 當某個地址停止響應時重啟 {#reboot-when-an-address-stops-answering}

遠端路由器可能失去其上行鏈路或 VPN，並在有人重啟它之前一直處於不可達狀態，例如安裝在桅杆上的路由器其無線鏈路掛起。當鏈路另一端的某個地址停止響應時，ping 看門狗會重啟這樣的路由器：

```ros
/system/watchdog/set watch-address=192.0.2.1
```

請使用一個穩定線上、且路由器能透過你所關注的鏈路到達的地址，例如上行的閘道器。對於 VPN，請監視隧道內部的地址，例如遠端的隧道地址，而不是其公網地址：隧道斷開時公網地址仍可能響應。一個因自身原因而下線的地址，會重啟一臺本來正常工作的路由器。

路由器會 ping 該地址六次，分佈在 `ping-timeout` 時間內（預設 1 分鐘，即每 10 秒一次 ping），當六次 ping 全部失敗時重啟。啟動後，它會等待 `ping-start-after-boot`（預設 5 分鐘）才發出第一次 ping。在已執行時間超過 `ping-start-after-boot` 的路由器上，設定 `watch-address` 會立即開始 ping。

請將 `ping-start-after-boot` 設定得比鏈路在啟動後建立連線所需的時間更長，例如 VPN 或 LTE 連線。否則路由器會在鏈路建立之前就重啟。每次重啟後，這段時間也是你登入並設定 `watch-address=none` 的視窗。

:::warning
如果該地址一直不可達，路由器會在每次啟動後再次重啟，間隔為 `ping-start-after-boot` 加 `ping-timeout`：使用預設值大約每 6 分鐘一次。請謹慎選擇地址，並保留另一條進入途徑，例如控制檯訪問或從鄰居處使用 MAC Telnet。
:::

要關閉 ping 看門狗：

```ros
/system/watchdog/set watch-address=none
```

只要該地址不響應，ping 看門狗就會一直重啟。若想限制重啟次數，或在地址停止響應時執行其他操作，請使用帶指令碼的 [網路監控](./netwatch.md)。

## 查明路由器重啟的原因 {#see-why-the-router-rebooted}

在 ping 看門狗重啟之後，日誌會顯示以下條目（第一條的主題為 `system,error,critical`）：

```text
System rebooted because of ping watchdog timeout
router rebooted
```

ping 看門狗重啟不會寫入支援輸出檔案（`autosupout.rif`）。

## 崩潰後的支援輸出 {#support-output-after-a-crash}

當軟體發生故障時，路由器會自行寫入 `autosupout.rif`（`automatic-supout=yes`，預設開啟），並將上一個檔案重新命名為 `autosupout.old.rif`。請將這些檔案連同問題描述一起傳送給 MikroTik 支援。有關支援輸出檔案的更多資訊，請參閱 [Supout.rif](../getting-started/supout-rif.md)。

路由器也可以透過電子郵件傳送該檔案。例如，透過 SMTP 伺服器 `192.0.2.1` 將其傳送到 `support@example.com`：

```ros
/system/watchdog/set auto-send-supout=yes \
    send-email-to=support@example.com send-smtp-server=192.0.2.1
```

當 `send-email-from` 或 `send-smtp-server` 未設定時，路由器會使用 [`/tool/e-mail`](../system-information-and-utilities/e-mail.md) 中的值。當 `auto-send-supout=no` 時，`print` 不會顯示電子郵件設定。

## 技術細節 {#technical-details}

### Ping 間隔 {#ping-interval}

兩次 ping 之間的間隔為 `ping-timeout` 除以六：預設 `1m` 時為 10 秒，`2m` 時為 20 秒。重啟會在第六次 ping 失敗後幾秒鐘發生，因此大約在第一次 ping 失敗後 `ping-timeout` 時間發生。

較舊的匯出配置將 `ping-start-after-boot` 稱為 `no-ping-delay`。

### 軟體看門狗定時器 {#software-watchdog-timer}

當 `watchdog-timer=yes` 時，如果系統一分鐘內無響應，路由器就會重啟。設定 `watchdog-timer=no` 可將其關閉。

有關所有引數，請參閱 [`/system/watchdog`](../cli-reference/system/watchdog.md) CLI 參考。
