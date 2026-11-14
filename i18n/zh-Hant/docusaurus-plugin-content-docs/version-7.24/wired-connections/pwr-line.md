---
sidebar_key: "wired-connections/pwr-line"
sidebar_position: 3
title: "PWR 產品線"
sidebar_label: "PWR 產品線"
description: "PWR-Line 頁面描述了使用 HomePlug AV 標準透過電力線實現類似乙太網連線的 MikroTik RouterOS 裝置，詳細介紹了 ARP 模式和頻寬限制等介面屬性，以及用於網路金鑰管理和裝置配對的配置命令。"
tags:
  - 'pwr-line'
  - 'arp'
  - 'mac-address'
source: https://manual.mikrotik.com/docs/7.24/wired-connections/pwr-line
captured_at: '2026-11-04T11:34:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

PWR-Line 系列裝置允許受支援的裝置透過普通電力線進行類似乙太網的連線。當插入同一電路時，PWR-Line 裝置將使用 HomePlug AV 標準建立連線。

## 屬性 {#properties}

|  |  |
| :-- | :-- |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; Default: **enabled**) | 地址解析協定模式：<ul><li>disabled - 介面將不使用 ARP</li><li>enabled - 介面將使用 ARP</li><li>proxy-arp - 介面將使用 ARP 代理功能</li><li>reply-only - 介面僅回覆來自匹配 IP 地址/MAC 地址組合的請求，這些組合需已作為靜態條目輸入到 <code>/ip/arp</code> 表中。ARP 表中不會自動儲存任何動態條目。因此，為使通訊成功，必須已存在有效的靜態條目。</li></ul> |
| **bandwidth** (*integer/integer*; Default: **unlimited/unlimited**) | 設定介面將處理的最大 rx/tx 頻寬，單位為 kbps。TX 限制在所有 Atheros [switch-chip](../bridging-and-switching/switch-chip-features.md) 埠上受支援。RX 限制僅在 Atheros8327/QCA8337 switch-chip 埠上受支援。 |
| **comment** (*string*; Default: ) | 條目的描述性名稱 |
| **l2mtu** (*integer [0..65536]*; Default: ) | 二層最大傳輸單元。[RouterOS 中的 MTU](../hardware/mtu-in-routeros.md) |
| **mac-address** (*MAC*; Default: ) | 介面的媒體訪問控制編號。 |
| **mtu** (*integer [0..65536]*; Default: **1500**) | 三層最大傳輸單元 |
| **name** (*string*; Default: ) | 介面的名稱 |
| **orig-mac-address** (*MAC*；預設值： ) |  |
| **rx-flow-control** (*on \| off \| auto*; Default: **off**) | 當設定為 on 時，埠將處理收到的暫停幀並在需要時暫停傳送。**auto** 與 **on** 相同，但當 auto-negotiation=yes 時，流控狀態將透過考慮對端通告的內容來確定。該功能在 AR724x、AR9xxx 和 QCA9xxx CPU 埠、所有 CCR 埠以及所有 Atheros switch chip 埠上受支援。 |
| **tx-flow-control** (*on \| off \| auto*; Default: **off**) | 當設定為 on 時，埠將在達到特定緩衝區使用閾值時傳送暫停幀。**auto** 與 **on** 相同，但當 auto-negotiation=yes 時，流控狀態將透過考慮對端通告的內容來確定。該功能在 AR724x、AR9xxx 和 QCA9xxx CPU 埠、所有 CCR 埠以及所有 Atheros switch chip 埠上受支援。 |

## 選單專用命令 {#menu-specific-commands}

| 屬性 | 描述 |
| :-- | :-- |
| **configure** () | 該命令配置所連線 PWR-Line 裝置的 network-key、network-password、plc-cco-selection-mode。 |
| **join** () | 啟動配對序列，該序列將在同一電路中查詢也處於配對模式的其他 PWR-Line 裝置。此模式持續 120 秒。 |
| **leave** () | 啟動離開序列，這基本上會隨機化裝置的 network-key。 |
| **monitor** () | 即時輸出與 PWR-Line 相關的狀態。 |
| **upgrade-firmware** () | 使用指定的 firmware-file 和 pib-file 檔案升級 PWR-Line 裝置。 |

## 配置示例 {#configuration-example}

為使兩臺或更多裝置能夠相互連線，它們必須共享相同的 network-key 值。當前配置的 network-key 可以使用 monitor 命令檢視為 plc-actual-network-key。

```ros
[admin@MikroTik] > /interface/pwr-line/monitor pwr-line1 
name: pwr-line1
connection-to-plc: ok
tx-flow-control: no
rx-flow-control: no
plc-actual-network-key: c973947c200e1540b0f84b571d92bebe
plc-hw-platform: QCA7420
plc-sw-platform: MAC
plc-fw-version: 1.4.0(24-20180515-CS)
plc-line-freq: 50Hz
plc-zero-crossing: detected
plc-mac: B8:69:F4:C4:34:68
```

### 方法 1 {#method-1}

在不同裝置上設定相同 network-key 有兩種方法。你可以使用 network-key 引數（它是 network-password 引數的雜湊版本），或者使用 network-password 引數，讓路由器對可讀字串應用雜湊。

例如：

```ros
/interface/pwr-line/configure pwr-line1 network-password=mynetwork
```

等同於：

```ros
/interface/pwr-line/configure pwr-line1 network-key=cb01fcc6167bf3d1edb1433c2ebde4b3
```

必須在所有希望相互通訊的裝置上設定相同的金鑰或密碼。

### 方法 2 {#method-2}

可以使用 join 和 leave 命令，讓 PWR-Line 裝置自動同步 network-key 值。建議在使用 join 命令之前先使用 leave 命令，以確保隨機生成新的 network-key，並且裝置不屬於任何舊網路。

```ros
/interface/pwr-line/leave pwr-line1
```

然後可以發出 join 命令。執行此操作時，配對序列會啟用 120 秒，這意味著你必須在 120 秒內在另一臺裝置上啟用配對模式，它們才能成功配對。

```ros
/interface/pwr-line/join pwr-line1
```

### 方法 3 {#method-3}

還可以使用 plc-cco-selection-mode 引數為 PWR-Line 裝置設定指定角色（master 或 slave）。

| 屬性 | 描述 |
| :-- | :-- |
| **plc-cco-selection-mode** (*auto \| always \| never*; 預設：**auto**) | 設定 PWR-Line 裝置模式：auto - PWR-Line 在加入 PWR-Line 網路時會根據情況自動決定承擔什麼角色。always - PWR-Line 將始終被強制充當 "central-coordinator" 或主裝置。never - PWR-Line 將始終被強制充當從裝置。 |

示例：

```ros
/interface/pwr-line/configure pwr-line1 plc-cco-selection-mode=auto
```

```ros
/interface/pwr-line/configure pwr-line1 plc-cco-selection-mode=always
```

```ros
/interface/pwr-line/configure pwr-line1 plc-cco-selection-mode=never
```

## 同步按鈕用法 {#sync-button-usage}

- 按住 0.5 – 3 秒以開啟同步模式。它會在 120 秒內嘗試與另一臺 PWR-LINE 裝置通訊。橙色 LED 燈閃爍表示它處於搜尋模式。你還必須在另一臺 PWR-LINE 裝置上執行相同操作，以便它們能夠同步。再次按下按鈕可取消搜尋。你也可以在 RouterOS 設定中手動設定安全金鑰。

- 按住 5 – 8 秒以生成新的安全金鑰。需要這樣做才能將 PWR-LINE 裝置從現有 PWR-LINE 網路中移除。

- 按住 10 – 15 秒以重設所有與 PWR-LINE 相關的設定。

## 支援的硬體 {#supported-hardware}

該裝置與我們 PWR-LINE AP 完全相容，並且具有 MicroUSB 埠的最新產品修訂版（例如 hAP lite、hAP lite tower、hAP mini、mAP 和 mAP lite）具有 pwr-line 介面。只需簡單升級軟體到 v6.44+ 即可啟用此功能（由序列號以 /9xx 結尾的上述裝置支援）。某些以前製造的裝置也支援 PWR-LINE 功能——如果你的裝置序列號以 /8xx 結尾，請升級到 6.44+，然後檢視 pwr-line 介面是否出現。
