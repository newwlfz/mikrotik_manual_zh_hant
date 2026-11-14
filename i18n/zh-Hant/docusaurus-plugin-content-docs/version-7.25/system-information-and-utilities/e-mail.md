---
sidebar_key: "system-information-and-utilities/e-mail"
sidebar_position: 3
title: "電子郵件"
sidebar_label: "電子郵件"
description: "從 RouterOS 透過 SMTP 伺服器傳送郵件：TLS 模式與埠、證書驗證、Gmail 應用專用密碼、附件、定時匯出配置，以及各條錯誤資訊的含義。"
tags:
  - 'email'
  - 'smtp'
  - 'tls'
source: https://manual.mikrotik.com/docs/7.25/system-information-and-utilities/e-mail
captured_at: '2026-11-04T11:21:57+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

路由器透過 SMTP 伺服器傳送郵件：可以是你的郵件服務商的伺服器，也可以是你自己的郵件伺服器。指令碼和 [scheduler](./scheduler.md) 用它傳送告警、備份和配置匯出，[watchdog](../diagnostics-monitoring-and-troubleshooting/watchdog.md) 用它傳送支援輸出檔案。

路由器使用 AUTH PLAIN 登入伺服器。加密方面，它從連線一開始就使用 TLS（`tls=yes`），或者用 STARTTLS 升級明文連線（`tls=starttls`）。不使用 TLS 時，使用者名稱和密碼會以未加密的方式穿越網路，因此對於任何不在你自己網路中的伺服器，都應使用 TLS。

## 配置 SMTP 伺服器 {#configure-the-smtp-server}

伺服器設定位於 [`/tool/e-mail`](../cli-reference/tool/e-mail/index.md)。選擇與伺服器埠相匹配的 `tls`：

| 埠 | `tls` | 用途 |
| :-- | :-- | :-- |
| 587 | `starttls` | 使用 STARTTLS 的郵件提交，大多數郵件服務商都提供。 |
| 465 | `yes` | 隱式 TLS：連線從開始就加密。 |
| 25 | `no` | 明文 SMTP，僅用於你自己網路中接受明文的中繼。 |

兩者不能混用：在埠 587 上使用 `tls=yes` 會以 `TLS handshake failed` 失敗，在埠 465 上使用 `tls=starttls` 會以 `timeout occured` 失敗。

例如，要透過 Gmail 使用 STARTTLS 並驗證證書傳送郵件：

```ros
/tool/e-mail/set server=smtp.gmail.com port=587 tls=starttls \
    certificate-verification=yes from=you@gmail.com \
    user=you@gmail.com password="xxxx xxxx xxxx xxxx"
```

:::info
Gmail 不接受來自路由器等裝置的 Google 賬號密碼。為你的 Google 賬號開啟兩步驗證，建立一個應用專用密碼（在你的 Google 賬號中依次進入 **Security**、**App passwords**），並使用生成的 16 位密碼作為 `password`。
:::

`certificate-verification` 預設為 `no`：路由器會加密連線，但不檢查伺服器證書。將其設為 `yes` 以根據路由器的信任庫檢查證書。內建信任庫預設覆蓋電子郵件，因此 Gmail 等公共提供商的證書無需額外設定即可驗證透過。當證書與伺服器名稱不匹配時，傳送會以 `TLS handshake failed (ssl: name verification failed for: ...)` 失敗。

在 WinBox 中，開啟 **Tools > Email** 配置 SMTP 連線：

1. 將 **Server**、**Port** 和 **TLS** 設定為你的郵件服務商提供的值。截圖顯示的是未配置的值，並非可用郵件伺服器的設定。
2. 在 **From** 中輸入發件人地址。如果伺服器要求身份驗證，使用 **+** 控制元件設定 **User** 和 **Password**。
3. 檢查 TLS 連線的 **Certificate Verification**，然後選擇 **OK** 儲存配置。有關驗證選項和證書要求的伺服器設定，請參閱 CLI 參考。

![WinBox Email Settings dialog for the SMTP connection](/img/f031512534090b28.webp)

## 傳送訊息 {#send-a-message}

使用 [`/tool/e-mail/send`](../cli-reference/tool/e-mail/send.md) 傳送訊息：

```ros
/tool/e-mail/send to=admin@example.com subject="Router alert" \
    body="The backup link is down."
```

該命令使用 `/tool/e-mail` 的設定。傳遞給該命令的任何設定，例如 `server`、`port`、`tls` 或 `from`，只對本條訊息覆蓋相應設定。

- 在 `to` 和 `cc` 中用逗號分隔多個收件人。路由器會向他們所有人傳送一條訊息。
- `body` 中的 `\n` 表示換行。
- `file` 會附加路由器檔案列表中的檔案，多個檔案用逗號分隔。不存在的檔案會在訊息傳送前被拒絕，並提示 `input does not match any value of file`。
- 始終設定 `from`。不設定時，路由器會以空發件人（`<>`）傳送訊息，許多伺服器會拒絕這種訊息。

`/tool/e-mail/print` 在 `last-status` 中顯示最後一條訊息的結果：`succeeded` 或 `failed`。

要在 WinBox 中傳送訊息，開啟 **Tools > Email** 並在右側面板中選擇 **Send Email**：

1. 設定 **To** 和 **Subject**。使用 **Cc** 新增其他收件人，需要時使用 **From** 覆蓋已配置的發件人。
2. 在 **Body** 中輸入訊息。使用 **Files** 旁的 **+** 控制元件附加路由器上已儲存的檔案。

![WinBox Send Email dialog with recipient, subject, body, and attachments](/img/ea09716bb4b6bb51.webp)

檢查 SMTP 設定和收件人，然後選擇 **Send Email** 傳送訊息。**Cancel** 會關閉對話方塊而不傳送。如果投遞失敗，請在 Email Settings 中檢查 **Last Status**。

## 每天透過郵件傳送配置匯出 {#email-the-configuration-export-every-day}

每天晚上將路由器的配置匯出傳送給管理員。

1. 配置 SMTP 伺服器，例如你網路中的一箇中繼：

   ```ros
   /tool/e-mail/set server=192.0.2.25 port=25 from=router@example.com
   ```

2. 新增一個名為 `export-email` 的 [script](../developer-guides/scripting/index.md)，用於寫入匯出檔案併發送它：

   ```ros
   /export file=export
   /tool/e-mail/send to=config@example.com file=export.rsc \
       subject="$[/system/identity/get name] export" \
       body="$[/system/clock/get date] configuration file"
   ```

3. 新增一個 [scheduler](./scheduler.md) 條目，每 24 小時執行該指令碼：

   ```ros
   /system/scheduler/add name=export-email on-event=export-email \
       start-time=00:00:00 interval=24h
   ```

匯出預設會隱藏密碼和其他敏感值，參見 [配置匯出](../getting-started/configuration-management/index.md#configuration-export)。

## 故障排除 {#troubleshoot}

當訊息無法傳送時，命令會以 `failure:` 訊息停止，並且 `last-status` 為 `failed`：

| 訊息 | 含義 |
| :-- | :-- |
| `TLS handshake failed (timeout)` | 對 STARTTLS 埠（如 587）使用 `tls=yes`。請改用 `tls=starttls`。 |
| `TLS not supported by server` | 使用了 `tls=starttls`，但伺服器不提供 STARTTLS。路由器不會回退到未加密的連線。 |
| `timeout occured` | 伺服器無應答，例如對隱式 TLS 埠（如 465）使用 `tls=no` 或 `tls=starttls`。 |
| `invalid FROM address` | 伺服器拒絕了發件人。對於未使用 TLS 的連線，Gmail 也會這樣應答，因此除了 `from` 之外還要檢查 `tls`。 |
| `AUTH failed` | `user` 或 `password` 錯誤。Gmail 需要應用專用密碼。 |
| `recipient address required` | 缺少 `to`。 |
| `TLS handshake failed (ssl: name verification failed for: ...)` | 在 `certificate-verification=yes` 時，伺服器證書與伺服器名稱不匹配。 |

當 `server` 是名稱時，`/tool/e-mail/print` 中的 `last-address` 顯示路由器連線到的地址。

## 技術細節 {#technical-details}

### SMTP 會話 {#smtp-session}

路由器用方括號中的自身地址向伺服器致意（例如 `EHLO [192.0.2.1]`），並使用 AUTH PLAIN 登入。每條訊息都有一個按路由器時區生成的 `Date` 頭，以及一個以路由器標識結尾的 `Message-ID`。

### 文字與附件 {#text-and-attachments}

不帶附件的訊息沒有 MIME 頭：路由器按原樣傳送主題和正文，不宣告字元集。帶附件時，訊息為 `multipart/mixed`，文字部分宣告為 US-ASCII，每個檔案以 `application/octet-stream` 連同其檔名附加。兩種情況下 Gmail 都能正確顯示 UTF-8 文字。對於必須在所有郵件用戶端中正確顯示的告警，請使用純 ASCII 文字。

### VRF {#vrf}

`/tool/e-mail` 中的 `vrf` 選擇路由器開啟到伺服器的連線所使用的 VRF。

有關所有引數，請參閱 [`/tool/e-mail`](../cli-reference/tool/e-mail/index.md) 和 [`/tool/e-mail/send`](../cli-reference/tool/e-mail/send.md) 的 CLI 參考。
