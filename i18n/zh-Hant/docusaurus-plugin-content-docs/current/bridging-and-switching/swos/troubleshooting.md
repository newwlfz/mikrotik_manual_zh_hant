---
sidebar_key: "bridging-and-switching/swos/troubleshooting"
sidebar_position: 5
title: "無法升級 SwOS"
sidebar_label: "無法升級 SwOS"
source: https://manual.mikrotik.com/docs/bridging-and-switching/swos/troubleshooting
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

---

## 概述 {#overview}

支援 SwOS 的 MikroTik 交換器會在快閃記憶體中儲存兩個獨立的韌體映象：**主**（活動）映象和**備份**映象。正常執行時，裝置從主映象啟動。當啟動韌體升級時——無論是透過 Web 介面自動進行，還是透過檔案上傳手動進行——裝置都會將新映象寫入主映象槽位並重啟進入該映象。

升級失敗通常由以下原因之一導致：

- 選擇了錯誤的韌體檔案（型號或韌體分支不對）
- 寫入操作被中斷，導致主映象損壞
- 網路連線問題導致自動下載無法到達 MikroTik 伺服器
- 在雙啟動裝置上：device-mode 策略限制了作業系統切換（RouterOS 7.17+）

僅支援 SwOS 的裝置和雙啟動裝置需要不同的恢復步驟，下文分別說明。

---

## 開始之前 {#before-you-begin}

> **警告：** 本文所述的復位按鈕操作會清除活動配置並加載出廠預設設定。在繼續操作之前，請從 **System** 標籤頁匯出配置備份。

在嘗試手動升級之前，請確認你需要哪個韌體檔案。每個交換器系列都使用專用的韌體二進位制檔案——跨系列的韌體檔案不可互換，會被拒絕或導致啟動失敗。你裝置的正確檔案可在以下位置找到：

[mikrotik.com 軟體下載中心](https://mikrotik.com/download)

---

## 解決方法 {#resolution}

### 僅支援 SwOS 的裝置（CSS 系列） {#swos-only-devices-css-series}

這些裝置不執行 RouterOS，也沒有序列埠控制檯啟動選單。恢復依賴於儲存在受保護快閃記憶體分割區中的硬體備份韌體。

**第 1 步 — 嘗試手動上傳韌體**

在 SwOS Web 介面中進入 **Upgrade** 標籤頁，選擇適用於你裝置型號的正確 `.swos` 韌體檔案，然後單擊 **Upgrade**。寫入過程中請勿中斷供電。上傳完成後，裝置將自動重啟。重新載入 Web 介面，並確認 **System** 標籤頁中顯示的韌體版本。

**第 2 步 — 透過硬體復位啟動到備份韌體**

如果手動上傳失敗，或升級嘗試後設備無法訪問，可使用復位按鈕強制載入備份（主）韌體：

1. 斷開裝置電源。
2. 按住 **Reset** 按鈕並重新接通電源。
3. 繼續按住按鈕約 5 秒，直到裝置完成啟動過程。
4. 鬆開按鈕。

裝置將載入備份韌體並應用出廠預設配置。可透過 **192.168.88.1** 或 DHCP 分配的地址訪問它。

**第 3 步 — 重新嘗試手動上傳韌體**

裝置在備份韌體上可訪問後，重複第 1 步中的手動升級過程。備份韌體環境提供了一個乾淨的狀態，在此基礎上升級更有可能成功。

---

### 雙啟動裝置（CRS 系列） {#dual-boot-devices-crs-series}

雙啟動裝置同時儲存 SwOS 和 RouterOS，並可啟動進入任一作業系統。這提供了額外的恢復途徑，包括透過 RouterOS CLI 進行升級。

**第 1 步 — 嘗試手動上傳韌體**

與僅支援 SwOS 的裝置一樣，首先透過 SwOS Web 介面中的 **Upgrade** 標籤頁，使用適用於你裝置的正確韌體檔案嘗試手動升級。

**第 2 步 — 透過序列埠控制檯啟動到備份 SwOS**

如果手動上傳失敗，請使用序列埠控制檯線纜按以下引數連線到裝置：

| 引數 | 值 |
| --- | --- |
| 波特率 | 115200 |
| 資料位 | 8 |
| 停止位 | 1 |
| 奇偶校驗 | 無 |
| 流控制 | 無 |

在啟動選單提示符下，選擇：

```
p - boot primary SwOS
```

這會加載出廠備份 SwOS 映象。裝置可訪問後，按第 1 步所述重新嘗試手動上傳韌體。

**第 3 步 — 透過復位按鈕啟動到 RouterOS（無控制檯訪問）**

如果沒有可用的序列埠控制檯埠，或手邊沒有線纜，可使用復位按鈕強制裝置進入 RouterOS：

1. 在裝置通電狀態下，按住 **Reset** 按鈕。
2. 按住直到使用者 LED 開始閃爍（約 5 秒）。
3. 鬆開按鈕。

裝置會將 RouterOS 配置重設為出廠預設設定並啟動進入 RouterOS。

> **警告：** 此操作會重設 RouterOS 配置。如果裝置之前執行的是 RouterOS，請確保在繼續操作之前已存在 RouterOS 配置備份。

**第 4 步 — 從 RouterOS CLI 升級 SwOS**

啟動進入 RouterOS 後，無需使用 Web 介面即可直接升級 SwOS。以下命令會獲取並安裝適用於該裝置的最新可用 SwOS 韌體：

```
/system swos upgrade
```

該命令需要網際網路訪問才能從 MikroTik 的更新伺服器解析並下載正確的韌體包。執行前請驗證連線性。

**第 5 步 — device-mode 限制（RouterOS 7.17 及更高版本）

從 RouterOS **v7.17** 開始，`device-mode` 策略會限制雙啟動硬體上 SwOS 與 RouterOS 之間的作業系統切換。如果升級命令失敗或作業系統切換被阻止，請使用以下命令顯式允許切換：

```
/system/device-mode/update routerboard=yes
```

必須在 RouterOS 中執行該命令，然後才能重新嘗試 SwOS 升級或切換回 SwOS。

**第 6 步 — 返回 SwOS**

在從 RouterOS 成功更新 SwOS 韌體後，將預設啟動目標設回 SwOS 並重啟裝置：

```
/system routerboard settings set boot-os=swos
/system reboot
```

裝置將重新啟動並載入新安裝的 SwOS 韌體。
