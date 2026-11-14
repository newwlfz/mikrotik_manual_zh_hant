---
title: "文件更新 - 2026年10月7日"
date: 2026-10-07
slug: /changelog-2026-10-07
source: https://manual.mikrotik.com/changelog/changelog-2026-10-07
captured_at: '2026-11-04T06:08:58+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 10 月 7 日的文件變更摘要。

## 管理工具 {#management-tools}

- **[SSH](/docs/management-tools/ssh)**、**[ssh-exec](/docs/cli-reference/system/ssh-exec)**：已在實驗路由器上驗證執行細節：多行遠端命令在 RouterOS 7.25 及更高版本上執行（SSH 伺服器仍不提供偽終端）。exit-code 是遠端命令 shell 報告的程式碼，而 RouterOS 命令失敗時會以錯誤文字的形式返回在輸出中。已修正 ssh-exec 示例，改為使用 monitor ... once as-value 讀取鏈路狀態。
- **[CMR](/docs/management-tools/cmr)**：新增“run-script 許可權”章節：透過 /cmr/device/run-script 傳送的指令碼會在每個用戶端上以 read、write、test 和 reboot 策略執行，且沒有使用者會話。需要其他策略的命令會失敗並提示“not enough permissions (9)”——例如 /user add 需要 policy，/tool sniffer 需要 sniff，因此 /export 也會失敗。敏感值會以 * 掩碼顯示，但可以設定。由 run-script 建立的指令碼和 scheduler 條目會以相同的四個策略和 *sys 所有者儲存，更寬泛的策略會被縮減回這四個策略。

## 無線 {#wireless}

- **[Wi-Fi](/docs/wireless/wifi)**：authentication-types 列表現在包含 wpa3-psk-gd，並重寫了預設值說明：配置了 passphrase 後，預設集合取決於 WiFi 標準、band 和 mode——6-7 GHz 的 AP 預設為 WPA3-PSK 和 GD，2.4/5 GHz 的 WiFi 7 AP 預設為 WPA2/WPA3-PSK 和 GD，WiFi 5/6 AP 預設為 WPA2-PSK，station 預設為 WPA/WPA2-PSK。

## 硬體 {#hardware}

- **[PoE](/docs/hardware/poe-out)**：全域性設定和監控表格已與 CLI 參考同步：新增了 poe-in-max-power、jack-max-power 和 2pin-max-power 變體、按電源來源劃分的 poe-out-max-power 行，以及只讀的 PoE 控制器韌體版本。監控部分新增了 port-type 和 poe-voltage 欄位、更新後的 poe-out-status 列表（no-valid-PSU、lldp-power-off、low-voltage-pd-detected 等），並補充了關於透過 PoE-In 供電的裝置上“power-limiting port”狀態的說明。
