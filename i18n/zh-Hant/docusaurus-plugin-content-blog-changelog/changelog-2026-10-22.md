---
title: "文件更新 - 2026年10月22日"
date: 2026-10-22T00:00:00.000Z
slug: /changelog-2026-10-22
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

# 文件更新 - 2026年10月22日 {#documentation-updates---october-22-2026}

October 22, 2026

2026年10月22日所做文件更改的摘要。

## 高可用性解決方案 {#high-availability-solutions}

-   **[多機箱鏈路聚合組](/docs/high-availability-solutions/multi-chassis-link-aggregation-group)**：新增了共享系統 ID 的說明。MLAG 將主節點的系統 ID 同時用於 RSTP 橋 ID 和雙連線 bond 的 LACP 系統 ID。當主節點重啟時，從節點會將其 bond 恢復為自身的 LACP 系統 ID，LACP 對端會重新協商該 bond，期間會出現短暫丟包；`mlag-lacp-fallback=no` 在對等鏈路丟失後仍保留共享 ID。重啟後，`mlag-init-delay` 會使 bond 從屬介面在 MLAG 系統 ID 同步之前不加入 bond。[`/interface/bridge`](/docs/cli-reference/interface/bridge) 參考文件描述了 `mlag-init-delay`（預設 1 分鐘）和 `mlag-lacp-fallback`（預設 `yes`）。同時還新增到了 7.25 手冊中。

## 診斷與監控 {#diagnostics--monitoring}

-   **[Netwatch](/docs/diagnostics-monitoring-and-troubleshooting/netwatch)**：恢復瞭如何執行需要超出 Netwatch 指令碼策略的命令：將其放入具有自身 `policy` 和 `dont-require-permissions=yes` 的 `/system/script` 條目中，並從 Netwatch 指令碼使用 `/system/script/run` 呼叫它。保持該指令碼簡短，並且只賦予它所需的策略。

## 管理工具 {#management-tools}

-   **[RoMON](/docs/management-tools/romon)**：更正：封包嗅探器和 Torch 僅顯示路由器傳送的 RoMON 幀（`tx`）。接收到的 RoMON 幀不會顯示，即使使用 `mac-protocol=romon` 或 `direction=rx` 也不會顯示；要檢視兩個方向，請在兩個路由器之間的裝置上抓包，例如透過交換器的映象埠。

## 開發者指南 {#developer-guides}

-   **[指令碼](/docs/developer-guides/scripting)**：再次更正了作用域規則：在互動式 CLI 中鍵入的每一行都是其自己的區域性作用域，因此某一行的區域性變數在下一行會被讀取為空值（型別 `nothing`）。請將命令放在一行中或 `{ }` 塊中。全域性變數示例現在在頂層宣告全域性變數，並且提示說明了為什麼在塊內宣告全域性變數會使指令碼更難閱讀。

**Tags:**

-   [文件變更日誌](/changelog/tags/changelog "文件更新的每日摘要")
