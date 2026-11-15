---
title: "文件更新 - 2026年10月23日"
date: 2026-10-23T00:00:00.000Z
slug: /changelog-2026-10-23
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

# 文件更新 - 2026年10月23日 {#documentation-updates---october-23-2026}

October 23, 2026

2026年10月23日所做文件更改的摘要。

## 認證與 AAA {#authentication--aaa}

-   **[Certificates](/docs/authentication-authorization-accounting/certificates)**、**[User](/docs/authentication-authorization-accounting/user)**：具有弱 RSA 公共指數（7 或更低）的證書和 SSH 金鑰仍可繼續使用，但會在 `/certificate/print`、`/user/ssh-keys` 和 `/user/ssh-keys/private` 輸出中被標記為註釋 `key uses insecure RSA public exponent!`。請將它們替換為更強的金鑰。此內容也已新增到 7.25 手冊中。

## 管理工具 {#management-tools}

-   **[SSH](/docs/management-tools/ssh)**：具有弱公共指數的 RSA 主機金鑰會被自動重新生成，並記錄該事件（`host key uses insecure RSA public exponent! Host key will be regenerated!`）。在任何重新生成之後，固定了舊金鑰的用戶端會報告指紋不匹配。此內容也已新增到 7.25 手冊中。

**Tags:**

-   [文件變更日誌](/changelog/tags/changelog "文件更新的每日摘要")
