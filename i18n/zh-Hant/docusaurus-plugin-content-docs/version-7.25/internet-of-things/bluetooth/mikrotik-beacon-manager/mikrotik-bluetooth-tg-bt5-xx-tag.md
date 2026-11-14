---
sidebar_key: "internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-bluetooth-tg-bt5-xx-tag"
sidebar_position: 3
title: "MikroTik 藍牙 TG-BT5-XX 標籤更新日誌"
sidebar_label: "MikroTik 藍牙 TG-BT5-XX 標籤更新日誌"
source: https://manual.mikrotik.com/docs/7.25/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-bluetooth-tg-bt5-xx-tag
captured_at: '2026-11-04T11:17:54+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 2.5.0 {#250}

- 新增廣告型別 “Device Name”。
- 降低裝置在工作期間的功耗。對於短間隔廣告，功耗降低將會比較明顯。
- 如果啟用了帶溫度資料的信標，則降低功耗。
- 降低 WDT（看門狗定時器）的功耗。如果啟用了任何廣告間隔小於 7s 的信標，此改動就會生效。

## 2.4.0 {#240}

- 在所有廣告中包含 ad flags 欄位。
- 新增停用密碼保護的功能。
- 新增停用加速度計的可能性。
- 為 MikroTik 格式載荷新增一個選項，用於檢測加速度計是否被停用（flags 欄位現在可以指示加速度計處於停用狀態）。
- 允許設定非標準廣告間隔。
- 新增用於停用某個廣告通道的配置選項。
- 實現了可配置的可連線廣告，允許在可配置狀態下連線到標籤，而無需一直按住磁鐵。
- 為加速度計新增配置選項，用於設定濾波器型別：HPF、LPF（高通或低通濾波器）。
- 日誌記錄方面的改進。

## 2.3.1 {#231}

- 提升了裝置效能。

## 2.3.0 {#230}

- 升級了藍牙協定棧版本。
- 提升了裝置效能。

## 2.2.0 {#220}

- 新增對非標準廣告間隔的支援。

## 2.1.0 {#210}

- 修復了從出廠睡眠模式喚醒後出現的時序不一致問題。
- 改進了裝置進入配置模式之前的 LED 行為。

## 2.0.0 {#200}

- 限制將喚醒閾值設定為 0g。
- 新增防寫功能。
- 提高了喚醒閾值的最小有效值。
- 升級了藍牙協定棧版本。

## 1.6.0 {#160}

- 提升了 Data Log 的穩定性。
- 新增一個選項，允許使用者手動校準感測器的溫度（偏移量）。

## 1.5.0 {#150}

- 新增觸發器 Impact。
- 新增 Data Logs。

## 1.4.0 {#140}

- 新增一個選項，用於將裝置重設回廣告模式。
- 新增一個選項，用於清除已儲存的日誌訊息。
- 新增 Unix Time 引數。
