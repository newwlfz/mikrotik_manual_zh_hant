---
sidebar_key: "system-information-and-utilities/e-mail"
sidebar_position: 3
title: "電子郵件"
sidebar_label: "電子郵件"
description: "RouterOS 中的電子郵件工具支援使用帶明文認證或 TLS 加密的 SMTP 直接從裝置傳送電子郵件，支援計劃備份和可自定義的電子郵件內容。它允許透過 `/tool/e-mail` 子選單配置 SMTP 伺服器、認證詳細資訊、加密設定和附件處理。"
tags:
  - 'email'
  - 'smtp'
  - 'tls'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/e-mail
captured_at: '2026-11-04T11:33:26+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

E-mail 工具是一個內建的 RouterOS 實用工具，使路由器能夠直接從裝置傳送電子郵件。它可用於按計劃自動將配置備份和匯出檔案傳送給網路管理員。

E-mail 工具支援明文認證和 TLS 加密。不支援其他身份驗證或加密方法。

## 屬性 {#properties}

**子選單：** `/tool/e-mail`

此子選單允許設定將要使用的 SMTP 伺服器。

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP/IPv6 address*; 預設：**0.0.0.0**) | SMTP 伺服器的 IP 地址。 |
| **certificate-verification**(*yes* \| *yes-without-crl* \| *no*; 預設：**no**) | 啟用從本地證書儲存進行的信任鏈驗證。*yes-without-crl* 會驗證證書，但不執行 CRL 檢查（證書吊銷列表）。 |
| **from** (*string*; 預設：**\<>**) | 將顯示為發件人的名稱或電子郵件地址。 |
| **password** (*string*; 預設：**""**) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於向 SMTP 伺服器進行身份驗證的密碼。 |
| **port** (*integer[0..65535]*; 預設：**25**) | SMTP 伺服器的埠。 |
| **tls** (*no\|yes\|starttls*; 預設：**no**) | 是否使用 TLS 加密：yes - 傳送 STARTTLS，如果伺服器上無法使用 TLS 則斷開會話；no - 不傳送 STARTTLS；starttls - 傳送 STARTTLS，如果伺服器響應 TLS 不可用，則繼續不使用 TLS |
| **user** (*string*; 預設：**""**) | 用於向 SMTP 伺服器進行身份驗證的使用者名稱。 |
| **vrf** (*VRF name*; 預設值：**main**) | 設定服務建立傳出連線時使用的 VRF。 |

:::warning
**注意：** 所有伺服器配置（如果已指定）都可以被 send 命令覆蓋。
:::

---

## 傳送電子郵件 {#sending-email}

**子選單：** `/tool/e-mail`

Send 命令接受以下引數：

| 屬性 | 描述 |
| :-- | :-- |
| **body** (*string*; 預設： ) | 電子郵件訊息的實際正文 |
| **cc** (*string*; 預設： ) | 向列出的收件人傳送副本。允許使用多個地址，使用 "," 分隔條目 |
| **certificate-verification**(*yes* \| *yes-without-crl* \| *no*; 預設：**no**) | 啟用從本地證書儲存進行的信任鏈驗證。*yes-without-crl,* 會驗證證書，但不執行 CRL 檢查（證書吊銷列表）。 |
| **file** (*File[,File]*; 預設： ) | 將以逗號分隔的、要附加到郵件中的檔名列表。 |
| **from** (*string*; 預設： ) | 將顯示為發件人的名稱或電子郵件地址。如果未指定，則使用伺服器配置中的值。 |
| **password** (*string*; 預設： ) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於向 SMTP 伺服器進行身份驗證的密碼。如果未指定，則使用伺服器配置中的值。 |
| **port** (*integer[0..65535]*; 預設： ) | SMTP 伺服器的埠。如果未指定，則使用伺服器配置中的值。 |
| **server** (*IP/IPv6 address*; 預設： ) | SMTP 伺服器的 IP 或 IPv6 地址。如果未指定，則使用伺服器配置中的值。 |
| **tls** (*yes\|no\|starttls*; 預設：**no**) | 是否使用 TLS 加密：yes - 傳送 STARTTLS，如果伺服器上無法使用 TLS 則斷開會話；no - 不傳送 STARTTLS；starttls - 傳送 STARTTLS，如果伺服器響應 TLS 不可用，則繼續不使用 TLS |
| **subject** (*string*; 預設： ) | 訊息的主題。 |
| **to** (*string*; 預設： ) | 目標電子郵件地址。僅允許單個地址。 |
| **user** (*string*; 預設： ) | 用於向 SMTP 伺服器進行身份驗證的使用者名稱。如果未指定，則使用伺服器配置中的值。 |

---

## 基本示例 {#basic-examples}

**本示例將展示如何每 24 小時傳送一封帶有配置匯出的電子郵件。**

1. 配置 SMTP 伺服器。

```ros
[admin@MikroTik] /tool/e-mail> set server=10.1.1.1 port=25 from="router@mydomain.com"
```

1. 新增一個名為 "export-send" 的新指令碼：

```ros
/export file=export 
/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name] export" \ 
body="$[/system/clock/get date] configuration file" file=export.rsc
```

1. 新增排程器以執行我們的指令碼。

```ros
/system/scheduler/add on-event="export-send" start-time=00:00:00 interval=24h
```

**使用 TLS/SSL 加密向伺服器傳送電子郵件。**

:::info
Google Mail 不允許第三方裝置使用標準 Gmail 密碼進行身份驗證。必須改為生成並使用 App 密碼。

要生成 App 密碼，請導航到 **Security > How you sign in to Google**，啟用 2-Step Verification，然後生成 App 密碼。在下面所示的 `set password=mypassword` 設定中使用生成的值。
:::

1. 配置用戶端以連線到正確的伺服器。

```ros
/tool/e-mail 
set address=smtp.gmail.com
set port=587
set tls=yes 
set from=myuser@gmail.com 
set user=myuser 
set password=mypassword
```

1. 使用 send 命令傳送電子郵件。

```ros
/tool/e-mail/send to=myuser@anotherdomain.com subject="email test" body="email test" 
```
