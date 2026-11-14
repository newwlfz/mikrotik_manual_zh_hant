---
sidebar_key: "management-tools/branding"
sidebar_position: 15
title: "品牌定製"
sidebar_label: "品牌定製"
description: "RouterOS Branding 軟體包支援自定義系統元素，包括路由器名稱、公司 URL、ASCII 徽標和 WebFig 介面。它支援為登入頁面、皮膚和熱點徽標包含自定義檔案，同時提供隱藏 SNMP 名稱等特定版本選項。"
tags:
  - 'branding'
  - 'webfig'
  - 'customization'
source: https://manual.mikrotik.com/docs/management-tools/branding
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 允許藉助品牌定製包進行少量系統自定義（修改預設配置、LCD 徽標、WebFig 主頁等）。

這是一個特殊的系統包，可在你的 [mikrotik.com](https://mikrotik.com) 賬戶中的 "Branding maker" 部分生成。生成的檔案將具有 .dpk 副檔名，並且可以透過與 .npk 包完全相同的所有方式安裝。

要在路由器上安裝該包，必須將品牌定製包上傳到路由器，然後路由器必須重啟。也可以使用 Netinstall 工具達到相同效果。

生成的包可以安裝在任何 RouterOS 版本中。

:::info
請注意，特定的品牌定製功能從特定的 RouterOS 版本開始才可用。

:::

## 選項 {#options}

可使用品牌定製包配置的選項：

- **路由器名稱** - 品牌定製包名稱、裝置身份以及 RouterOS 中的[平臺名稱](../diagnostics-monitoring-and-troubleshooting/resource.md)，只能是一個詞，不要使用空格或特殊字元。
- **公司 URL** - 連線到 RouterOS 裝置時在控制檯中顯示的值。
- **手動 URL** - 可在 [WebFig](./webfig.md) 中開啟的文件連結。
- **ASCII 徽標** - 登入命令列介面（即 Telnet、SSH、WinBox Terminal）時顯示的文字徽標。可以在 [branding maker](https://mikrotik.com/client/branding) 中建立徽標，或從任何其他純文字編輯器複製。徽標高度不能超過 8 行，寬度不受限制，但請注意，在狹窄的終端視窗中徽標可能會變形。
- **從 SNMP 資訊中隱藏 "Mikrotik"** - MikroTik 名稱將在 SNMP 資訊中隱藏。
- **安裝時不執行指令碼** - 安裝品牌定製包時不執行預設配置指令碼。
- **隱藏預設配置提示** - 在配置重設後隱藏預設配置提示 *（從 RouterOS 7.15 開始可用）*。
- **隱藏預設 caps-mode-script** - 隱藏預設 caps-mode-script *（從 RouterOS 7.15 開始可用）*。

## 自定義檔案 {#custom-files}

WebFig 登入頁面、WebFig 徽標、hotspot、skins、預設配置、LCD 徽標和 CAPs 模式指令碼等自定義檔案可以包含在品牌定製包中。

:::warning
任何復位按鈕模式都將從品牌定製包恢復預設配置。

:::

#### WebFig 登入頁面 {#webfig-login-page}

WebFig 登入頁面是訪問路由器 IP 地址時顯示的自定義預設 RouterOS 登入介面。可以自定義此頁面以滿足品牌定製或功能需求。

- **自定義檔案：**

  - **`/index2.html`**：登入頁面的主模板。
  - **`/assets/style.css`**：MikroTik RouterOS 樣式表。
  - **`/assets/script.js`** 負責處理登入功能，幷包含使按鈕具有互動性的程式碼。
- **`script.js` 的必需元素：**

  1. **登入表單：**  
     `<form id="login">`
  2. **使用者名稱欄位：**  
     `<input id="name" data-defaultuser="admin">`
     - `admin` 值可以更改為其他使用者名稱，也可以留空。
  3. **密碼欄位：**  
     `<input id="password">`
  4. **錯誤顯示部分：**  
      ``
- 以下是一個使用者自定義登入頁面的示例，其中包含一個“顯示密碼”按鈕，透過修改後的 **`[index2.html](pathname:///assets/295239801_index2.html)`** 以及額外的 [toggle_button.css](pathname:///assets/295239803_toggle_button.css) 和 [show_password.js](pathname:///assets/295239802_show_password.js) 檔案實現。  
  HTML 檔案必須命名為 "index2.html"，並且應使用正確巢狀的 HTML 以確保與所有瀏覽器相容。
- 上傳的影像或 JavaScript 檔案必須引用與索引檔案相同的路徑。不能使用自定義資料夾名稱。

---

#### WebFig 徽標 {#webfig-logo}

RouterOS WebFig 頁面（配置頁面）徽標。要覆蓋 WebFig 登入頁面上的 MikroTik 徽標，請上傳名為 "mikrotik\_logo.png" 的自定義徽標。

#### hotspot {#hotspot}

Hotspot 登入頁面徽標。檔案必須命名為 "logobottom.png"。

#### skins {#skins}

名為 "your\_file\_name.json" 的 skin 檔案。要將特定 skin 應用到特定使用者組，無需登入路由器。可以透過上傳預設配置檔案，使用品牌定製來實現。

#### 預設配置 {#default-configuration}

一個 RouterOS 預設配置檔案，將覆蓋 RouterOS 預設配置。此配置即使在 RouterOS 重設後也會保留。可以使用只讀變數 *$defconfPassword* 和 *$defconfWifiPassword* 重新應用出廠密碼（對出廠密碼的訪問從 RouterOS 7.10 開始可用）。

:::warning
如果預設配置或 CAPs 模式指令碼執行超過 2 分鐘，指令碼將失敗，並且 LOG 將包含 *"runtime limit exceeded"* 錯誤，或在極少數情況下包含 *"std failure: timeout"* 錯誤。

:::

#### LCD 徽標 {#lcd-logo}

LCD 徽標將顯示在配備 LCD 螢幕的裝置上。徽標大小不能超過 160px 寬和 72px 高。CCR1xxx 系列具有白色 (0xffffff) 背景，2011 系列具有黑色 (0x000000) 背景。

#### 自定義檔案 {#custom-files-1}

自定義檔案將被複制到名為 "branding" 的資料夾中，並可從 RouterOS 內部訪問。

#### CAPs 模式指令碼 {#caps-mode-script}

一個 RouterOS CAPs 模式指令碼，將覆蓋 RouterOS 預設 CAPs 模式指令碼。可以透過使用只讀變數 *$defconfPassword* 和 *$defconfWifiPassword* 重新應用出廠密碼（從 RouterOS 7.15 開始可用）。

:::warning
任何復位按鈕模式都將從品牌定製包恢復預設配置。CAPs 模式指令碼只能在裝置完全啟動後，透過 GUI 或 CLI 執行[配置重設](../getting-started/configuration-management/index.md#configuration-reset)來應用。

:::

:::warning
如果預設配置或 CAPs 模式指令碼執行超過 2 分鐘，指令碼將失敗，並且 LOG 將包含 *"runtime limit exceeded"* 錯誤，或在極少數情況下包含 *"std failure: timeout"* 錯誤。

:::
