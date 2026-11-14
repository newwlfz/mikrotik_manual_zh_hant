---
sidebar_key: "system-information-and-utilities/note"
sidebar_position: 10
title: "備註"
sidebar_label: "備註"
description: "RouterOS 中的系統備註功能允許使用者分配在登入時顯示的自定義文字訊息，並可選擇在 CLI 或 FTP 登入時顯示這些訊息，以及透過 `/system/note` 選單或上傳的檔案配置其內容。"
tags:
  - 'system-note'
  - 'cli'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/note
captured_at: '2026-11-04T11:33:34+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 概述 {#summary}

**子選單：** `/system/note`

系統備註功能允許你指定任意文字備註或訊息，這些內容會在每次登入時緊跟在橫幅之後顯示。例如，你可以透過這種方式在系統管理員之間分發警告，或描述該路由器實際負責的功能。要配置系統備註，你可以在路由器的 FTP 伺服器上上傳一個名為 **sys-note.txt** 的純文字檔案，或者額外在此選單中編輯設定

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **note** (*string*; 預設：) | 將顯示的備註。 |
| **show-at-login** (*yes \| no*; 預設：**yes**) | 是否在每次登入時顯示系統備註 |
| **show-at-cli-login** (*yes \| *no*, 預設：**no**) | 是否在 telnet 登入提示符之前顯示系統備註。 |

### 示例 {#example}

可以使用嵌入式文字編輯器（*`/system/note/edit` note*）新增多行備註，例如，為你的家用路由器新增 ASCII 藝術圖：

```
/system/note/set note=
```

```
                                       .&                                         
                                     @&   @&                                      
                                     @@   @#                                      
                                       @@&                                        
                                ,      @@@      .                                 
                                @@@@@@@@@@@@@@@@@                                 
                                       @@@                                        
                                       @@@                                        
                                       @@@                                        
                          ,@           @@@           &                            
                         @@@@          @@@          @@@@                          
                          @@           @@@           @(                           
                           &@@         @@@         @@@                            
                             @@@@@     @@@     &@@@&                              
                                &@@@@@@@@@@@@@@@&                                 
                                      @@@@@             
```
