---
title: "無法升級 SwOS"
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/swos/troubleshooting
captured_at: '2026-11-28T10:19:39.818Z'
pagination_next: "bridging-and-switching/user-guides"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

---

## 概觀 {#overview}

支援 SwOS 的 MikroTik 交換器會在快閃記憶體中儲存兩個獨立的韌體映像：**primary**（作用中）映像與 **backup** 映像。在正常運作下，設備會從 primary 映像開機。當啟動韌體升級時，無論是透過網頁介面自動進行，或透過檔案上傳手動進行，設備都會將新映像寫入 primary 插槽，並重新開機進入該映像。

升級失敗通常是由下列其中一項原因造成：

- 選錯韌體檔案（型號或韌體分支不正確）
- 寫入作業中斷，導致 primary 映像損毀
- 網路連線問題，使自動下載無法連線至 MikroTik 伺服器
- 在雙開機設備上：device-mode 政策限制 OS 切換（RouterOS 7.17+）

僅支援 SwOS 的設備與雙開機設備需要不同的復原程序，以下分別說明。

---

## 開始之前 {#before-you-begin}

> **警告：** 本文所述的重設按鈕程序會清除作用中設定，並載入原廠預設值。繼續之前，請從 **System** 分頁匯出設定備份。

在嘗試手動升級之前，請確認所需的韌體檔案。每個交換器系列都使用專屬的韌體二進位檔，跨系列的韌體檔案無法互換，且會被拒絕或導致開機失敗。適用於您設備的正確檔案可在下列位置找到：

[mikrotik.com Software download centre](https://mikrotik.com/download)

---

## Resolution

### 僅限 SwOS 的設備（CSS 系列） {#swos-only-devices-css-series}

這些設備不執行 RouterOS，也沒有序列主控台開機選單。復原程序依賴儲存在受保護快閃分割區中的硬體備援韌體。

**步驟 1 — 嘗試手動上傳韌體**

在 SwOS 網頁介面中前往 **Upgrade** 標籤，選取適用於設備型號的正確 `.swos` 韌體檔案，然後按一下 **Upgrade**。寫入過程中請勿中斷電源。上傳完成後，設備會自動重新啟動。重新載入網頁介面，並確認 **System** 標籤中顯示的韌體版本。

**步驟 2 — 透過硬體重設開機進入備援韌體**

如果手動上傳失敗，或設備在嘗試升級後無法連線，可以使用重設按鈕強制載入備援（主要）韌體：

1. 中斷設備電源。
2. 按住 **Reset** 按鈕，然後重新接上電源。
3. 繼續按住按鈕約 5 秒，直到設備完成開機程序。
4. 放開按鈕。

設備會載入備援韌體並套用原廠預設設定。可透過 **192.168.88.1** 或 DHCP 指派的位置存取設備。

**步驟 3 — 重試手動韌體上傳**

一旦設備可使用備份韌體存取，請重複步驟 1 的手動升級程序。備份韌體環境提供乾淨的狀態，可讓升級更有可能成功。

---

### 雙啟動設備（CRS 系列） {#dual-boot-devices-crs-series}

雙啟動設備會同時儲存 SwOS 與 RouterOS，並可啟動任一作業系統。這提供了額外的復原路徑，包括透過 RouterOS CLI 升級。

**步驟 1 — 嘗試手動韌體上傳**

與僅支援 SwOS 的設備一樣，請先透過 SwOS 網頁介面中的 **Upgrade** 索引標籤，使用適用於您設備的正確韌體檔案嘗試手動升級。

**步驟 2 — 透過序列主控台啟動至備份 SwOS**

如果手動上傳失敗，請使用序列主控台纜線連接設備，並使用下列參數：

| 參數 | 值 |
| --- | --- |
| 鮑率 | 115200 |
| 資料位元 | 8 |
| 停止位元 | 1 |
| 同位元 | None |
| 流量控制 | None |

在開機選單提示字元處，選取：

```
p - boot primary SwOS
```

這會載入原廠備份的 SwOS 映像檔。設備可存取後，請依照步驟 1 所述重新嘗試手動上傳韌體。

**步驟 3 — 透過 Reset 按鈕開機進入 RouterOS（無主控台存取）**

如果沒有序列主控台埠，或手邊沒有纜線，可以使用 Reset 按鈕強制設備進入 RouterOS：

1. 在設備通電時，按住 **Reset** 按鈕。
2. 持續按住，直到使用者 LED 開始閃爍（約 5 秒）。
3. 放開按鈕。

設備會將 RouterOS 設定重設為原廠預設值，並開機進入 RouterOS。

> **警告：** 此程序會重設 RouterOS 設定。如果設備先前執行 RouterOS，請在繼續之前確認已有 RouterOS 設定備份。

**步驟 4 — 從 RouterOS CLI 升級 SwOS**

開機進入 RouterOS 後，可以直接升級 SwOS，無需使用網頁介面。下列命令會從 MikroTik 的更新伺服器擷取並安裝適用於該設備的最新 SwOS 韌體：

```
/system swos upgrade
```

此命令需要網際網路連線，才能從 MikroTik 的更新伺服器解析並下載正確的韌體套件。執行前請先確認連線正常。

**步驟 5 — device-mode 限制（RouterOS 7.17 與更新版本）**

從 RouterOS **v7.17** 開始，`device-mode` 政策會限制雙開機硬體上 SwOS 與 RouterOS 之間的作業系統切換。如果升級命令失敗或作業系統切換遭到封鎖，請明確允許該切換：

```
/system/device-mode/update routerboard=yes
```

此命令必須在 RouterOS 中執行，然後才能重試 SwOS 升級或切換回 SwOS。

**步驟 6 — 返回 SwOS**

從 RouterOS 成功更新 SwOS 韌體後，將預設開機目標設回 SwOS，並重新啟動設備：

```
/system routerboard settings set boot-os=swos
/system reboot
```

設備將重新啟動並載入新安裝的 SwOS 韌體。
