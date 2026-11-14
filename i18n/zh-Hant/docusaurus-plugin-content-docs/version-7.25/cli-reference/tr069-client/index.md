---
sidebar_key: "cli-reference/tr069-client/index"
sidebar_position: 1
title: "tr069-client"
sidebar_label: 'tr069-client'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tr069-client
captured_at: '2026-11-01T21:26:05+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tr069-client {#tr069-client}
**軟體包：** tr069-client
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="enum (yes | no)">啟用或停用 CWMP 協定。</ArgTableRow>
<ArgTableRow arg="acs-url" typ="string">自動配置伺服器 (ACS) 的 URL。如果透過 HTTPS 訪問 ACS，則必須在用戶端證書儲存中匯入 Root CA，以驗證 ACS 伺服器證書。</ArgTableRow>
<ArgTableRow arg="username" typ="string">CPE 用於向 ACS 進行身份驗證的 HTTP 認證使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string">CPE 用於向 ACS 進行身份驗證的 HTTP 認證密碼。</ArgTableRow>
<ArgTableRow arg="periodic-inform-enabled" typ="bool">啟用或停用 CPE 週期性發起會話。每次成功會話後，定時器啟動。當按週期間隔啟動會話時，Inform RPC 包含一個 "2 PERIODIC" 事件。對映到 `Device.ManagementServer.PeriodicInformEnable`。</ArgTableRow>
<ArgTableRow arg="periodic-inform-interval" typ="time">週期性 Inform 的定時器間隔。對映到 `Device.ManagementServer.PeriodicInformInterval`。</ArgTableRow>
<ArgTableRow arg="connection-request-username" typ="string">ACS 在連線請求中用於向 CPE 進行身份驗證的使用者名稱。</ArgTableRow>
<ArgTableRow arg="connection-request-password" typ="string">ACS 在連線請求中用於向 CPE 進行身份驗證的密碼。</ArgTableRow>
<ArgTableRow arg="connection-request-port" typ="num">CPE 監聽來自 ACS 的連線請求所用的埠。</ArgTableRow>
<ArgTableRow arg="provisioning-code" typ="string">裝置的配置程式碼。</ArgTableRow>
<ArgTableRow arg="client-certificate" typ="enum (none)">證書儲存中的證書，可供 ACS 用於額外身份驗證。</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum (yes | no)">是否檢查 ACS 伺服器證書。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="enum (disabled | initializing | error | waiting-url | running)">CWMP 用戶端的資訊性狀態。Disabled 表示協定已停用，waiting-url 表示協定已啟用但未配置 ACS URL，running 表示 CWMP 已正確配置，並會在事件發生時與 ACS 通訊。</ArgTableRow>
<ArgTableRow arg="last-session-error" typ="string">使用者友好的錯誤描述，說明上一個會話為何未能成功完成。</ArgTableRow>
<ArgTableRow arg="retry-count" typ="num">連續未成功會話數。如果大於 0，last-session-error 應指出該錯誤。在會話成功、協定被停用或重啟後重設為 0。</ArgTableRow>
</ArgTable>
