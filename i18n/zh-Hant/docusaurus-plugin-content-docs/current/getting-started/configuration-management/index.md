---
sidebar_key: "getting-started/configuration-management"
title: "配置管理"
sidebar_label: "配置管理"
description: "本頁介紹 MikroTik RouterOS 中的配置管理，詳細說明如何使用 `/system/history` 介面或 CLI 命令撤銷和重做操作，並附有防火牆規則修改的示例。"
tags:
  - 'configuration-management'
  - 'system-backup'
  - 'safe-mode'
source: https://manual.mikrotik.com/docs/getting-started/configuration-management
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本文介紹一組用於配置管理的命令。

## 配置撤銷與重做 {#configuration-undo-and-redo}

在 GUI 中執行的任何操作或從 CLI 執行的任何命令都會記錄在 `/system/history` 中。你可以透過在 CLI 中執行 undo 或 redo 命令，或單擊 GUI 中的 Undo 和 Redo 按鈕，來撤銷或重做任何操作。

以下簡單示例演示新增防火牆規則以及如何撤銷和重做該操作：

```ros
[admin@v7_ccr_bgp] /ip/firewall/filter> add chain=forward action=drop 

[admin@v7_ccr_bgp] /ip/firewall/filter> print 
Flags: X - disabled, I - invalid; D - dynamic 
0 X chain=input action=drop protocol=icmp src-address=10.155.101.1 log=no 
log-prefix=""

1 chain=forward action=drop

[admin@v7_ccr_bgp] /ip/firewall/filter> /system/history/print 
Flags: U - undoable, R - redoable, F - floating-undo
Columns: ACTION, BY, POLICy
ACTION BY POLIC
F filter rule added admin write
U --- write
[admin@v7_ccr_bgp] /ip/firewall/filter>
```

我們添加了一條防火牆規則，並且在 `/system/history` 中可以看到所執行的所有操作。

讓我們撤銷所有操作：

```ros
[admin@v7_ccr_bgp] /ip/firewall/filter> /undo 
[admin@v7_ccr_bgp] /ip/firewall/filter> print 
Flags: X - disabled, I - invalid; D - dynamic 
0 X chain=input action=drop protocol=icmp src-address=10.155.101.1 log=no 
log-prefix=""

[admin@v7_ccr_bgp] /ip/firewall/filter>
```

如你所見，防火牆規則消失了。  
現在重做上一次更改：

```ros
[admin@v7_ccr_bgp] /ip/firewall/filter> /redo 
[admin@v7_ccr_bgp] /ip/firewall/filter> print 
Flags: X - disabled, I - invalid; D - dynamic 
0 X chain=input action=drop protocol=icmp src-address=10.155.101.1 log=no 
log-prefix=""

1 chain=forward action=drop 

[admin@v7_ccr_bgp] /ip/firewall/filter>
```

系統歷史能夠顯示在“Undo”或“Redo”操作期間將執行的準確 CLI 命令，即使我們是從 GUI 執行該操作也是如此；例如，從 WinBox 新增一條 TCP 接受規則後的詳細歷史輸出：

```ros
[admin@v7_ccr_bgp] /system/history> print detail 
Flags: U - undoable, R - redoable, F - floating-undo 
 F redo=
      /ip/firewall/filter/add action=accept chain=forward disabled=no log=no \
          log-prefix="" protocol=tcp
    undo=/ip/firewall/filter/remove *4 action="filter rule added" by="admin" 
    policy=write time=2019-10-10 18:51:05 

 F redo=/ip/firewall/filter/add action=accept chain=forward 
    undo=/ip/firewall/filter/remove *3 action="filter rule added" by="admin" 
    policy=write time=2019-10-10 18:49:03 

U redo="" undo="" action="---" by="" policy=write time=2019-09-27 13:07:35 
[admin@v7_ccr_bgp] /system/history> 
```

## 安全模式 {#safe-mode}

有時可能會以某種方式更改路由器配置，導致路由器無法訪問（本地控制檯除外）。這通常是意外造成的，但當與路由器的連線已經斷開時，就無法撤銷上一次更改。可以使用安全模式來儘量降低這種風險。

Winbox GUI 中的 **"Safe Mode"** 按鈕允許你進入安全模式；而在 CLI 中，你可以使用鍵盤快速鍵 <kbd>F4</kbd> 或按 **[CTRL]+[X]** 來進入。要退出而不儲存在 CLI 中所做的更改，請按 **[CTRL]+[D].**

![](/img/dccbcfe9483d3bf9.webp)

```ros
[admin@MikroTik] /ip/route>[CTRL]+[X] 
[Safe Mode taken] 
[admin@MikroTik] /ip/route<SAFE>
```

系統會顯示 **Safe Mode taken** 訊息，並且提示符會發生變化，以表明該會話現在處於安全模式。當路由器處於安全模式時，所做的所有配置更改（包括來自其他登入會話的更改）都會在安全模式會話異常終止時自動撤銷。你可以在系統歷史中看到所有此類將被自動撤銷並標記為 **F** 標誌的更改：

```ros
[admin@MikroTik] /ip/route> 
[Safe Mode taken] 
[admin@MikroTik] /ip/route<SAFE> add 
[admin@MikroTik] /ip/route<SAFE> /system/history/print 
Flags: U, F - FLOATING-UNDO 
Columns:
 ACTION, BY, POLICY ACTION BY POLICY 
F route 0.0.0.0/0 added admin write 
```

現在，如果 telnet 連線（或 WinBox 終端）被切斷，那麼過一段時間後（TCP 超時為 **9** 分鐘），在安全模式下所做的所有更改都將被撤銷。透過 **[Ctrl]+[D]** 退出會話也會撤銷所有安全模式更改，而 **/quit** 則不會。

如果另一個使用者嘗試進入安全模式，他將收到以下訊息：

```ros
[admin@MikroTik] >
Hijacking Safe Mode from someone - unroll/release/don't take it [u/r/d]:
```

- [u] - 撤銷所有安全模式更改，並將當前會話置於安全模式。
- [r] - 保留所有當前安全模式更改，並將當前會話置於安全模式。安全模式的前任所有者會收到有關此操作的通知。

```ros
[admin@MikroTik] >
[Safe mode released by another user]
```

- [d] - 保持一切原樣。

如果在安全模式下所做的更改過多，並且歷史記錄中沒有空間容納所有更改（目前歷史記錄最多保留 100 個最近操作），那麼會話會自動退出安全模式，並且不會自動撤銷任何更改。因此，最好在安全模式下以小步驟更改配置。按兩次 **[Ctrl]**+**[X]** 是清空安全模式操作列表的一種簡便方法。

## 系統備份與恢復 {#system-backup-and-restore}

[系統備份](./backup.md) 是以二進位制格式完整克隆路由器配置的方式。

## 配置匯出與匯入 {#configuration-export-and-import}

RouterOS 允許以純文字格式匯出和匯入部分配置。此方法可用於在不同裝置之間複製部分配置，例如將整個防火牆從一臺路由器克隆到另一臺路由器。

可以從每個選單執行 export 命令（僅匯出該特定選單及其所有子選單中的配置），也可以從根選單執行以匯出完整配置，並且僅適用於 CLI。

:::danger
該 Export 命令不會匯出系統使用者密碼、已安裝證書、SSH 金鑰、Dude 或 User-manager 資料庫。

[已安裝證書](../../authentication-authorization-accounting/certificates.md#export-certificate)、[Dude](../../management-tools/dude.md) 和 [使用者管理器](../../authentication-authorization-accounting/user-manager.md#database) 資料庫必須手動匯出並匯入到新裝置中。

系統使用者密碼和使用者 SSH 金鑰無法匯出。

**警告：** 在匯入配置期間，我們建議使用與匯出配置時相同的 RouterOS 版本，以防止某些命令在某個 RouterOS 版本中不存在的情況。
:::

### 配置匯出 {#configuration-export}

接受以下命令引數：

| 屬性 | 描述 |
| :-- | :-- |
| **compact** | 僅輸出修改過的配置。從 v6rc1 開始，“export compact”成為預設行為，因此“export”和“export compact”現在產生相同的輸出。 |
| **file** | 將配置匯出到指定檔案。如果未指定檔案，export 輸出將列印到終端 |
| **path** | 該引數允許從路由器的整個配置中包括或排除特定配置選單 |
| **show-sensitive** | 顯示敏感資訊，例如密碼、金鑰等。預設情況下，敏感資訊會被隱藏。[具有敏感引數的選單列表](./list-of-menus-with-sensitive-parameters.md) |
| **terse** | 使用此引數時，export 命令會將配置輸出為各自獨立的完整命令列，每行都包含相應的選單路徑。 |
| **verbose** | 使用此引數時，export 命令將輸出整個配置引數和條目，包括預設值。 |

例如，從 `/ip/address` 選單匯出配置並將其儲存到檔案：

```ros
    [admin@MikroTik] > /ip/address/print
    Flags: X - disabled, I - invalid, D - dynamic
    #   ADDRESS            NETWORK         BROADCAST       INTERFACE
    0   10.1.0.172/24      10.1.0.0        10.1.0.255      bridge1
    1   10.5.1.1/24        10.5.1.0        10.5.1.255      ether1
    [admin@MikroTik] > /ip/address/export file=address
    [admin@MikroTik] > /file/print
    # NAME                            TYPE         SIZE       CREATION-TIME
    0  address.rsc                     script       315        2003-12-23 13:21:48
    [admin@MikroTik] >
```

預設情況下，export 命令僅寫入使用者編輯過的配置，並省略 RouterOS 預設值。

例如，IPSec 預設策略不會被匯出；如果我們更改一個屬性，則只會匯出我們的更改：

```ros
    [admin@rack1_b4] /ip/ipsec/policy> print
    Flags: T - template, X - disabled, D - dynamic, I - inactive, * - default
    0 T * group=default src-address=::/0 dst-address=::/0 protocol=all
          proposal=default template=yes
    [admin@rack1_b4] /ip/ipsec/policy> export
    # 1970-04-02 17:59:14 by RouterOS 6.22
    # software id = DB0D-LK67
    #
    [admin@rack1_b4] /ip/ipsec/policy> set 0 protocol=gre
    [admin@rack1_b4] /ip/ipsec/policy> export
    # 1970-04-02 17:59:30 by RouterOS 6.22
    # software id = DB0D-LK67
    #
    /ip/ipsec/policy
    set 0 protocol=gre
```

匯出整個 `/ip/firewall` 配置（`/ip/firewall/nat` 除外）的示例

```routeros
/export path=/ip/firewall,!/ip/firewall/nat

/ip/firewall/address-list
add address=1.1.1.1 list=dns
/ip/firewall/filter
add action=passthrough chain=unused-hs-chain comment="place hotspot rules here" disabled=yes
add action=add-src-to-address-list address-list=12345 address-list-timeout=15s chain=input disabled=yes
add action=accept chain=output dst-port=80,443 log=yes protocol=tcp
/ip/firewall/mangle
add chain=prerouting
add action=accept chain=prerouting
add action=accept chain=prerouting dst-address=192.168.88.0/24 in-interface=ether2
```

:::info
注意：

**\*** 標誌表示該條目是系統預設條目，無法手動刪除。
:::

以下是包含預設系統條目的所有選單列表

| 選單 | 預設條目 |
| :-- | :-- |
| `/interface/wireless/security-profiles` | default |
| `/ppp/profile` | "default", "default-encryption" |
| `/ip/hotspot/profile` | default |
| `/ip/hotspot/user/profile` | default |
| `/ip/ipsec/policy` | default |
| `/ip/ipsec/policy/group` | default |
| `/ip/ipsec/proposal` | default |
| `/ip/ipsec/mode-conf` | 只讀 |
| `/ip/smb/shares` | pub |
| `/ip/smb/users` | guest |
| `/ipv6/nd` | any |
| `/mpls/interface` | all |
| `/routing/bfd/interface` | all |
| `/routing/bgp/instance` | default |
| `/routing/ospf/instance` | default |
| `/routing/ospf/area` | backbone |
| `/routing/ospf-v3/instance` | default |
| `/routing/ospf-v3/area` | backbone |
| `/snmp/community` | public |
| `/tool/mac-server/mac-winbox` | all |
| `/tool/mac-server` | all |
| `/system/logging` | "info", "error", "warning", "critical" |
| `/system/logging/action` | "memory", "disk", "echo", "remote" |
| `/queue/type` | "default", "ethernet-default", "wireless-default", "synchronous-default", "hotspot-default", "only-hardware-queue", "multi-queue-ethernet-default", "default-small" |

:::danger
如果某個特定選單無法響應 export 命令，從 RouterOS v7.11 開始，超時後會在 export 命令輸出中列印錯誤訊息（"#error exporting "/xxx" (timeout)"），然後程式將繼續處理下一個選單。
:::

從 RouterOS 7.13 開始，可以匯出特定選單的部分內容。例如，可以匯出路由器上多個地址列表中的某個特定地址列表。

```
[admin@MikroTik] > ip firewall address-list export where list=mylist

```

### 配置匯入 {#configuration-import}

根選單命令 import 允許從指定檔案執行配置指令碼。指令碼檔案（副檔名為“.rsc”）可以包含任何控制檯命令，包括複雜指令碼。

例如，載入已儲存的配置檔案

```ros
[admin@MikroTik] > import address.rsc
Opening script file address.rsc

Script file loaded and executed successfully
[admin@MikroTik] >
```

透過 import 命令可以指定以下引數：

| 屬性 | 描述 |
| :-- | :-- |
| **from-line** | 從指定行號開始執行指令碼。此選項僅在 verbose 模式下可用。 |
| **file-name** | 要執行的指令碼（.rsc）檔名。 |
| **verbose** | 逐行讀取檔案並單獨執行，從而更容易偵錯語法或其他錯誤。 |
| **dry-run** | 模擬 import 而不進行任何配置更改。這有助於捕獲語法錯誤。此選項僅在 verbose 模式下可用。 |

:::tip
如果裝置具有需要替換的預設配置或現有配置，則必須啟動配置重設。

這涉及使用命令 `/system/reset-configuration` no-defaults=yes 應用乾淨的空配置，然後重啟裝置。
:::

### 自動匯入 {#auto-import}

還可以在透過 FTP 或 SFTP 將指令碼上傳到路由器後**自動**執行指令碼。指令碼檔案的副檔名必須為 \*.auto.rsc。檔案中的命令執行後，會建立一個新的 \*.auto.log 檔案，其中包含匯入成功或失敗的資訊。

:::tip
檔名中的 ".auto.rsc" 是檔案自動執行的必要條件。
:::

### 匯入故障排除 {#import-troubleshooting}

#### 匯出的 .rsc 檔案中需要注意的配置部分 {#configuration-parts-to-watch-out-for-in-exported-rsc-files}

在嘗試向新裝置匯入之前，應從使用 "/export" 建立的匯出檔案中刪除以下內容：

- 介面重新命名與預設乙太網命名方案衝突。

```ros
/interface/ethernet
set [ find default-name=ether5 ] auto-negotiation=no name=ether1-gateway
set [ find default-name=ether6 ] name=ether2
set [ find default-name=ether7 ] name=ether3
set [ find default-name=ether8 ] name=ether4
set [ find default-name=ether1 ] name=ether5
set [ find default-name=ether2 ] name=ether6
set [ find default-name=ether3 ] name=ether7
set [ find default-name=ether4 ] name=ether8
```

- 在較舊版本中，"export" 預設條目可能會以 "add" 而不是 "set" 命令顯示。應在匯入前編輯，以避免錯誤。
- 檢查物理介面總數是否與新、舊裝置匹配。如果缺少某些介面，將導致 .rsc 匯入期間出錯。

如果匯入出現問題，請嘗試以下操作：

- 使用 **dry-run** 引數模擬 import 而不進行任何配置更改。這有助於捕獲語法錯誤。此選項僅在 verbose 模式下可用。
- 重設該裝置上的配置。
- 使用 "verbose=yes" 引數再次執行 import 命令。它還會在遇到你已經遇到的問題時停止匯入過程，但也會顯示匯出失敗的位置。這樣可以向你顯示 .rsc 匯入檔案中需要編輯的位置。

#### 啟動延遲 {#startup-delay}

如果你的配置依賴於在命令執行時可能尚未啟動的介面，建議引入延遲或監控直到所有所需介面都可用。此示例指令碼允許你設定期望的介面數量，以及等待它們變為可用的時長：

```ros
{
:local i 0
#接口数量。必须为每个设备重新配置此数字（/interface/print count-only）
:local x 10
#最长等待时间
:local t 30
while ($i < $t && [:len [/interface/find]] < $x) do={
:put $i
:set $i ($i + 1)
:delay 1
}
if ($i = $t) do={
:log warning message="Could not load all physical interfaces"
} else={
#脚本的其余部分
}
}
```

上述指令碼將等待直到有 10 個介面可見，或等待 30 秒。如果此時沒有 10 個介面，它會在日誌中放入一條訊息。請根據你的需要修改變數。

## 配置重設 {#configuration-reset}

RouterOS 允許使用 `/system/reset-configuration` 命令重設配置

此命令會清除路由器的所有配置，並將其設定為出廠預設值，包括登入名和密碼（使用者名稱為 'admin'，密碼為空；或者對於某些型號，為貼紙上的使用者密碼和無線密碼）。有關預設配置的更多詳細資訊，[請參閱列表](./default-configurations.md)。

執行配置重設命令後，路由器將重啟並載入預設配置。從 7.13 版本開始，重設後會顯示許可證提示，並提供檢視終端使用者許可協定的選項。

:::tip
重設前會儲存現有配置的備份檔案。這樣，如果誤執行了重設，你可以輕鬆恢復任何以前的配置。

**注意：** 如果路由器是使用 [網路安裝](../installation-and-upgrade/netinstall/index.md) 安裝的，並且指定了指令碼作為初始配置，則重設命令會在清除配置後執行此指令碼。要阻止其這樣做，你必須重新安裝路由器。
:::

可以使用以下引數覆蓋預設的重設行為：

| 屬性 | 描述 |
| :-- | :-- |
| **keep-users** | 不從配置中刪除現有使用者 |
| **no-defaults** | 不載入預設配置，只清除配置 |
| **skip-backup** | 跳過重設前自動生成備份檔案 |
| **run-after-reset** | 重設後執行指定的 .rsc 檔案。這樣你可以載入自定義配置。**警告：** 如果特定 .rsc 檔案執行超過 2 分鐘，指令碼將失敗，並且 LOG 將包含 *"runtime limit exceeded"*，或在少數情況下包含 *"std failure: timeout"* 錯誤。 |
| **caps-mode** | 配置重設後執行 *caps-mode* 指令碼。 |

例如，在不載入預設配置並跳過備份檔案的情況下硬重設配置：

```ros
[admin@MikroTik] > /system/reset-configuration no-defaults=yes skip-backup=yes
Dangerous! Reset anyway? [y/N]: y
```

使用 Winbox 執行相同操作的示例如下：

![](/img/62a5962444b7942d.webp)

## 相關主題 {#related-topics}

<DocCardList />
