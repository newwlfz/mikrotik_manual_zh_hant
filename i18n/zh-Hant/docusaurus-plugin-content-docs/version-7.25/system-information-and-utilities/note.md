---
sidebar_key: "system-information-and-utilities/note"
sidebar_position: 9
title: "備註"
sidebar_label: "備註"
description: "系統註釋是 RouterOS 在登入時向管理員顯示的文字：路由器的用途、聯絡方式或警告。可在 CLI、WinBox 中或透過 sys-note.txt 檔案設定，並在 Telnet 登入提示符之前顯示。"
tags:
  - 'system-note'
  - 'cli'
source: https://manual.mikrotik.com/docs/7.25/system-information-and-utilities/note
captured_at: '2026-11-04T11:22:04+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

系統備註是 RouterOS 向每位登入的管理員顯示的文字：在命令列中緊跟在登入橫幅之後顯示，在 WinBox 中則於登入後在一個視窗中顯示。可用它說明路由器用途、聯絡人，或說明哪些操作不能做，例如在維護視窗期間。該備註預設為空。

## 設定備註 {#set-a-note}

使用 `note` 設定文字。在雙引號字串中，`\n` 表示換行：

```ros
/system/note/set \
    note="Office gateway. IT: +371 0000000\nNo reboots 08:00-18:00"
```

在下一次互動式登入時（例如透過 SSH 或 MAC Telnet），備註會顯示在登入橫幅之後：

```text
  MikroTik RouterOS 7.25beta5 (c) 1999-2026       https://www.mikrotik.com/

Press F1 for help

Office gateway. IT: +371 0000000
No reboots 08:00-18:00
```

透過 SSH 執行且沒有互動式會話的命令（例如 `ssh admin@router '/system/resource/print'`）不會顯示備註。對於較長的文字，`/system/note/edit note` 會在內建編輯器中開啟備註。若要不刪除備註但停止顯示它，請設定 `show-at-login=no`。

## 在 WinBox 中配置備註 {#configure-the-note-in-winbox}

開啟 **System > Note**：

1. 使用 **Show At Login** 和 **Show At CLI Login** 選擇備註何時顯示。**Show At Login** 會在登入後顯示它；**Show At CLI Login** 還會在 Telnet 登入提示符之前顯示它。
2. 在 **Note** 中輸入訊息，然後選擇 **OK**。例如，記錄路由器的用途和維護聯絡人。文字區域支援多行。

![WinBox System Note dialog with login display options and the Note text area](/img/a61e903df56a5414.webp)

## 在登入前顯示備註 {#show-the-note-before-login}

當 `show-at-cli-login=yes` 時，路由器還會在 Telnet 登入提示符之前列印備註，下面是從另一臺路由器使用 `/system/telnet 192.168.88.1` 看到的效果：

```text
Connecting to 192.168.88.1
Connected to 192.168.88.1
Office gateway. IT: +371 0000000
No reboots 08:00-18:00
Login:
```

此功能獨立於 `show-at-login`。任何連線到 Telnet 埠的人無需登入就能看到此文字，因此不要把僅供管理員檢視的資訊放在備註中。Telnet 預設啟用；請參閱 [服務](./services.md)。SSH 不會在登入前顯示備註，而 MAC Telnet 會在連線前要求輸入使用者名稱和密碼，因此它只在登入後顯示備註。

## 從檔案設定備註 {#set-the-note-from-a-file}

路由器檔案儲存根目錄中名為 `sys-note.txt` 的純文字檔案會在下次啟動時替換備註，隨後路由器會刪除該檔案。要透過這種方式在新路由器上設定備註，請上傳該檔案（例如透過 SFTP 或 FTP），然後重啟路由器。

有關引數，請參閱 [`/system/note` CLI 參考](../cli-reference/system/note.md)。
