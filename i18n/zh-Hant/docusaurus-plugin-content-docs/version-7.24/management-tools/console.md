---
sidebar_key: "management-tools/console"
sidebar_position: 4
title: "控制檯"
sidebar_label: "控制檯"
description: "控制檯透過文字終端提供對 MikroTik RouterOS 配置和管理功能的基於文字的訪問，既可遠端使用序列埠、telnet、SSH 或 WinBox 內的控制檯螢幕，也可直接使用顯示器和鍵盤。它涵蓋在分層選單級別中執行命令、登入選項、終端自定義、橫幅訊息、快速輸入、安全模式和指令碼。"
tags:
  - 'cli'
  - 'console'
  - 'scripting'
  - 'menu-hierarchy'
  - 'terminal'
source: https://manual.mikrotik.com/docs/7.24/management-tools/console
captured_at: '2026-11-04T11:31:59+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#overview}

控制檯用於透過文字終端訪問 MikroTik 路由器的配置和管理功能，既可以遠端使用序列埠、telnet、SSH 或 [WinBox](./winbox.md) 中的控制檯螢幕，也可以直接使用顯示器和鍵盤。控制檯還用於編寫指令碼。本手冊介紹控制檯的一般操作原理。有關一些高階控制檯命令以及如何編寫指令碼，請參閱[指令碼手冊](../developer-guides/scripting/index.md)。

## 登入選項 {#login-options}

控制檯登入選項可啟用或停用各種控制檯功能，例如顏色、終端檢測以及許多其他功能。

可以在登入名後的 '+' 符號後附加登入引數。

```
    login_name ::= user_name [ '+' parameters ]
    parameters ::= parameter [ parameters ]
    parameter ::= [ number ] 'a'..'z'
    number ::= '0'..'9' [ number ]
```

如果引數不存在，則使用預設值。如果數字不存在，則使用該引數的隱式值。

示例：`admin+ct80w` - 停用控制檯顏色，停用自動檢測，然後將終端寬度設定為 80。

| 引數 | 預設值 | 隱式值 | 描述 |
| :-- | :-- | :-- | :-- |
| **"w"** | auto | auto | 設定終端寬度 |
| **"h"** | auto | auto | 設定終端高度 |
| **"c"** | on | off | 停用/啟用控制檯顏色 |
| **"t"** | off | on | 停用終端能力自動檢測 |
| **"e"** | on | off | 啟用 "dumb" 終端模式 |

## 橫幅和訊息 {#banner-and-messages}

登入過程在驗證使用者名稱和密碼後會顯示 MikroTik 橫幅和簡短幫助。

```ros
  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

  MikroTik RouterOS 7.23.2 (c) 1999-2026       https://www.mikrotik.com/

Press F1 for help
```

橫幅之後還可以列印其他重要資訊，例如另一位管理員設定的 `/system/note`、最近幾條關鍵日誌訊息、演示版升級提醒以及預設配置說明。

例如，會列印演示許可證提示和最近的關鍵訊息：

```ros
UPGRADE NOW FOR FULL SUPPORT
----------------------------
FULL SUPPORT benefits:
- receive technical support
- one year feature support
- one year online upgrades
    (avoid re-installation and re-configuring your router)
To upgrade, register your license "software ID"
on our account server www.mikrotik.com

Current installation "software ID": ABCD-456

Please press "Enter" to continue!

2007-12-10 10:40:06 system,error,critical login failure for user root from 10.0.0.1 via telnet
2007-12-10 10:40:07 system,error,critical login failure for user root from 10.0.0.1 via telnet
2007-12-10 10:40:09 system,error,critical login failure for user test from 10.0.0.1 via telnet
```

## 命令提示符 {#command-prompt}

成功登入序列結束時，登入過程會列印顯示命令提示符的橫幅，並將控制權交給使用者。

預設命令提示符由使用者名稱、系統標識和當前命令路徑組成。

例如，將當前路徑從根路徑切換到 interface，然後返回根路徑：

```ros
  [admin@MikroTik] > interface [enter]
  [admin@MikroTik] /interface> / [enter]
  [admin@MikroTik] >
```

使用 <kbd>↑</kbd> 從命令歷史中調出之前的命令（新增過敏感資料（如密碼）的命令不會出現在歷史中）。如果調出的是多行命令，按 <kbd>F8</kbd> 展開它。使用 <kbd>Tab</kbd> 自動補全命令並檢視可用選項——按兩次 <kbd>Tab</kbd> 會顯示所有可能的補全項。按 <kbd>Enter</kbd> 執行命令，按 <kbd>Control</kbd>+<kbd>C</kbd> 中斷當前正在執行的命令並返回提示符，按 <kbd>F1</kbd> 顯示內建幫助。

最簡便的退出控制檯方式是在命令列處於空狀態時，在命令提示符處按 <kbd>Control</kbd>+<kbd>D</kbd>（可以用 **Control-C** 取消當前命令並獲得空行，因此大多數情況下先按 **Control-C** 再按 <kbd>Control</kbd>+<kbd>D</kbd> 即可退出登入）。

可以編寫由多行組成的命令。當輸入的行不是完整命令且預期還有更多輸入時，控制檯會顯示續行提示符，其中列出所有未閉合的圓括號、花括號、方括號和引號，如果上一行以**反斜槓**加空白結尾，還會顯示末尾反斜槓。

```ros
    [admin@MikroTik] > {
    {... :put (\
    {(\... 1+2)}
    3
```

編輯此類多行輸入時，提示符會顯示當前行號和總行數，而不是通常的使用者名稱和系統名。

```
line 2 of 3> :put (\
```

有時命令會要求使用者提供額外輸入。例如，命令 `/password` 會要求輸入舊密碼和新密碼。在這種情況下，提示符會顯示所請求值的名稱，後跟冒號和空格。

```ros
    [admin@MikroTik] > /password
    old password: ******
    new password: **********
    retype new password: **********
```

## 層次結構 {#hierarchy}

控制檯允許使用文字命令配置路由器的設定。由於可用命令很多，它們被分成組，並組織成層次化的選單級別。選單級別的名稱反映了相關部分中可訪問的配置資訊。

例如，可以執行 `/ip/route/print` 命令：

```ros
[admin@MikroTik] > /ip/route/print 
Flags: X - disabled, A - active, D - dynamic, 
C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme,
B - blackhole, U - unreachable, P - prohibit
 # DST-ADDRESS PREF-SRC G GATEWAY DIS INTE... 
0 A S 0.0.0.0/0 r 10.0.3.1 1 bridge1 
1 ADC 1.0.1.0/24 1.0.1.1 0 bridge1 
2 ADC 1.0.2.0/24 1.0.2.1 0 ether3 
3 ADC 10.0.3.0/24 10.0.3.144 0 bridge1 
4 ADC 10.10.10.0/24 10.10.10.1 0 wlan1 
[admin@MikroTik] >
```

無需在每條命令前鍵入 `/ip/route` 路徑；該路徑只需鍵入一次，即可進入選單層次結構中的這個特定分支。因此，上面的示例也可以這樣執行：

```ros
[admin@MikroTik] > /ip/route 
[admin@MikroTik] /ip/route> print 
Flags: X - disabled, A - active, D - dynamic, 
C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme,
 B - blackhole, U - unreachable, P - prohibit # 
DST-ADDRESS PREF-SRC G GATEWAY DIS INTE... 
0 A S 0.0.0.0/0 r 10.0.3.1 1 bridge1 
1 ADC 1.0.1.0/24 1.0.1.1 0 bridge1 
2 ADC 1.0.2.0/24 1.0.2.1 0 ether3 
3 ADC 10.0.3.0/24 10.0.3.144 0 bridge1 
4 ADC 10.10.10.0/24 10.10.10.1 0 wlan1 
[admin@MikroTik] /ip/route>
```

路徑中的每個單詞可以用**空格**或 `/` 分隔。

請注意，提示符會變化，以反映您當前位於選單層次結構中的位置。要再次移動到頂層，請鍵入 `/`

```ros
[admin@MikroTik] > /ip/route 
[admin@MikroTik] /ip/route> /
[admin@MikroTik] >
```

要上移一個命令級別，請鍵入 `..`

```ros
[admin@MikroTik] /ip/route> .. 
[admin@MikroTik] /ip>
```

還可以使用 `/` 和 `..` 從其他選單級別執行命令，而無需更改當前級別：

```ros
[admin@MikroTik] /ip/route> /ping 10.0.0.1 
10.0.0.1 ping timeout 
2 packets transmitted, 0 packets received, 100% packet loss 
[admin@MikroTik] /ip/firewall/nat> ../service-port/print
Flags: X - disabled, I - invalid 
# NAME PORTS 
0 ftp 21 
1 tftp 69 
2 irc 6667 
3 h323 
4 sip 
5 pptp 
[admin@MikroTik] /ip/firewall/nat>
```

## 專案名稱和編號 {#item-names-and-numbers}

許多命令級別會操作專案陣列：介面、路由、使用者等。此類陣列會顯示為外觀相似的列表。列表中的所有專案都有一個專案編號，後跟標誌和引數值。

要更改專案屬性，必須使用 **set** 命令並指定專案的名稱或編號。

### 專案名稱 {#item-names}

某些列表中的專案各自分配了特定名稱。例如 `/interface` 或 `/user` 級別。在這些級別中，可以使用專案名稱代替專案編號。

透過名稱訪問專案之前，不必使用 **print** 命令；與編號不同，名稱不是控制檯內部分配的，而是專案的屬性。因此，名稱不會自行改變。但是，當多個使用者同時更改路由器配置時，可能會出現各種難以預料的情況。通常，專案名稱比編號更“穩定”，資訊量也更大，因此在編寫控制檯指令碼時，應優先使用名稱而不是編號。

### 專案編號 {#item-numbers}

專案編號由 print 命令分配，並且不是固定的——兩次連續的 print 命令可能以不同順序排列專案。但上次 print 命令的結果會被記住，因此，一旦分配，專案編號即使在 **add**、**remove** 和 **move** 操作之後仍可使用。專案編號按會話分配；在您退出控制檯或執行下一條 print 命令之前，它們將保持不變。此外，編號是按每個專案列表單獨分配的，因此例如 `/ip/address/print` 不會更改 `/interface` 列表的編號。

可以在不執行 **print** 命令的情況下使用專案編號。編號的分配方式將與執行了 **print** 命令時相同。

對於某些命令，可以指定多個專案作為目標。幾乎所有可以寫入專案編號的地方，也可以寫入編號列表。

```ros
[admin@MikroTik] > /interface/print 
Flags: X - disabled, D - dynamic, R - running 
# NAME TYPE MTU 
0 R ether1 ether 1500 
1 R ether2 ether 1500 
2 R ether3 ether 1500 
3 R ether4 ether 1500 
[admin@MikroTik] > /interface/set 0,1,2 mtu=1460 
[admin@MikroTik] > /interface/print
 Flags: X - disabled, D - dynamic, R - running 
# NAME TYPE MTU 
0 R ether1 ether 1460 
1 R ether2 ether 1460 
2 R ether3 ether 1460 
3 R ether4 ether 1500 
[admin@MikroTik] >
```

:::warning
不要在指令碼中使用專案編號。在 **scheduler、scripts** 等中編輯專案時，這不是可靠的方法。請改用 **find** 命令。更多資訊請參閱[指令碼編寫文件](../developer-guides/scripting/index.md)。另請參閱[指令碼示例](../developer-guides/scripting/scripting-examples.md)。
:::

## 常規命令 {#general-commands}

有些命令幾乎通用於所有選單級別，即：**add**、**edit**、**find**、**move**、**print**、**remove**、**set**、**reset**、**export**、**get**、**enable**、**disable** 和 **comment**。這些命令在不同選單級別中的行為類似。有關詳細描述和引數，請參閱[指令碼命令](../developer-guides/scripting/index.md#commands)參考。

:::info
你可以組合命令。以下是同一命令的兩個變體，它們將透過查詢註釋來放置新的防火牆過濾條目：

```ros
/ip/firewall/filter/add chain=forward place-before=[find where comment=CommentX]
/ip/firewall/filter/add chain=forward place-before="CommentX"
```
:::

## 編輯模式 {#edit-modes}

控制檯行編輯器可在多行模式或單行模式下工作。

在多行模式下，行編輯器會顯示完整的輸入行，即使它長於單個終端行。它還使用全屏編輯器編輯大型文字值，例如指令碼。

在單行模式下，僅使用一個終端行進行行編輯，長行會圍繞游標截斷顯示。此模式下不使用全屏編輯器。

模式的選擇取決於檢測到的終端能力。

## 輸入模式 {#input-modes}

可以在幾種輸入模式之間切換：

- **普通模式** - 由普通命令提示符指示。
- **安全模式** - 由命令提示符後的 SAFE 字樣指示。
- **Hot-lock 模式** - 由額外的黃色 > 指示。自動補全命令。

### 安全模式 {#safe-mode}

有時可能以某種方式更改路由器配置，導致路由器無法訪問（本地控制檯除外）。通常這是意外造成的，但當到路由器的連線已經斷開時，無法撤銷上一次更改。安全模式可用於將這種風險降到最低。

WinBox GUI 中的 **"Safe Mode"** 按鈕允許您進入安全模式，而在 CLI 中，可以透過鍵盤快速鍵 <kbd>F4</kbd> 或按 <kbd>Control</kbd>+<kbd>X</kbd> 進入。要在不儲存在 CLI 中所做更改的情況下退出，請按 <kbd>Control</kbd>+<kbd>D</kbd>。

```ros
[admin@MikroTik] /ip/route>[CTRL]+[X] 
[Safe Mode taken] 
[admin@MikroTik] /ip/route<SAFE>
```

![](/img/12123ac32556cc95.png)

顯示 **Safe Mode taken** 訊息，提示符會發生變化，以反映該會話現在處於安全模式。如果安全模式會話異常終止，則在路由器處於安全模式期間所做的所有配置更改（也包括來自其他登入會話的更改）都會自動撤銷。您可以在系統歷史中看到所有此類將被自動撤銷的更改，它們帶有 **F** 標誌：

```ros
[admin@MikroTik] /ip/route> 
[Safe Mode taken]
[admin@MikroTik] /ip/route<SAFE>/add
[admin@MikroTik] /ip/route<SAFE> /system/history/print
Flags: U, F - FLOATING-UNDO
Columns: ACTION, BY, POLICY
  ACTION                 BY     POLICY
F route 0.0.0.0/0 added  admin  write
```

現在，如果 telnet 連線（或 WinBox 終端）被切斷，那麼過一段時間後（TCP 超時為 **9** 分鐘），在安全模式下所做的所有更改都將被撤銷。透過 <kbd>Control</kbd>+<kbd>D</kbd> 退出會話也會撤銷所有安全模式更改，而 **/quit** 不會。

如果另一位使用者嘗試進入安全模式，會收到以下訊息：

```ros
[admin@MikroTik] > 
Hijacking Safe Mode from someone - unroll/release/don't take it [u/r/d]:
```

- [u] - 撤銷所有安全模式更改，並將當前會話置於安全模式。
- [r] - 保留所有當前安全模式更改，並將當前會話置於安全模式。安全模式的前任所有者會收到有關此情況的通知：

```ros
[admin@MikroTik] /ip/firewall/rule/input 
[Safe mode released by another user]
```

- [d] - 保持一切原樣。

如果在安全模式下所做的更改太多，且歷史記錄中沒有足夠空間容納所有更改（目前歷史記錄最多保留 100 個最近操作），則會話會自動退出安全模式，並且不會自動撤銷任何更改。因此，在安全模式下最好以小步方式更改配置。按兩次 <kbd>Control</kbd>+<kbd>X</kbd> 是清空安全模式操作列表的簡便方法。

:::warning
由於“Safe Mode”在使用者會話內執行並存儲配置更改，因此對於需要重新啟動的命令（例如重設配置或從備份恢復），它將被忽略。
:::

### HotLock 模式 {#hotlock-mode}

啟用 HotLock 模式後，命令將自動補全。

要進入/退出 HotLock 模式，請按 <kbd>F7</kbd>。

```ros
[admin@MikroTik] /ip/address> [F7]
[admin@MikroTik] /ip/address>>

```

雙 `>>` 表示已啟用 HotLock 模式。例如，如果鍵入 "`/in et"`，它將自動補全為：

```ros
[admin@MikroTik] /ip/address>> /interface/ethernet/
```

### 鎖定模式 {#lock-mode}

**:lock** 命令會鎖定螢幕。

```ros
[admin@MikroTik] > :lock
...
  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

  MikroTik RouterOS 7.16rc1 (c) 1999-2024       https://www.mikrotik.com/

Session is locked       (Ctrl-D to Quit)

 password for admin: 
```

## 快速輸入 {#quick-typing}

控制檯中的兩個功能有助於更快捷、更輕鬆地輸入命令——<kbd>Tab</kbd> 鍵補全和命令名縮寫。補全的工作方式類似於 UNIX 中的 bash shell。如果在單詞的一部分之後按 <kbd>Tab</kbd> 鍵，控制檯會嘗試在當前上下文中查詢以該單詞開頭的命令。如果只有一個匹配項，則自動追加該匹配項，後跟一個空格：

`/inte` <kbd>Tab</kbd> 變為 `/interface/`

如果有多個匹配項，但它們都有一個共同開頭，且該共同開頭比您已鍵入的內容更長，則將該單詞補全到此共同部分，並且不追加空格：

`/interface/set e` <kbd>Tab</kbd> 變為 `/interface/set ether`

如果您只鍵入了共同部分，按一次 <kbd>Tab</kbd> 沒有效果。但是，第二次按下會以緊湊形式顯示所有可能的補全項：

```ros
[admin@MikroTik] > /interface/set e[Tab]_ 
[admin@MikroTik] > /interface/set ether[Tab]_ 
[admin@MikroTik] > /interface/set ether[Tab]_ 
ether1 ether5 
[admin@MikroTik] > interface set ether_
```

在控制檯可能知道可能值的幾乎所有上下文中，都可以使用 <kbd>Tab</kbd> 鍵——命令名、引數名、只有幾個可能值的引數（例如某些列表中專案的名稱，或防火牆和 NAT 規則中的協定名稱）。不能補全數字、IP 地址和類似值。

鍵入時減少按鍵次數的另一種方法是縮寫命令名和引數名。您可以只鍵入命令名的開頭，如果沒有歧義，控制檯會將其接受為完整名稱。因此，鍵入：

```ros
[admin@MikroTik] > pin 10.1 c 3 si 100
```

等同於：

```ros
[admin@MikroTik] > ping 10.0.0.1 count 3 size 100
```

不僅可以補全名稱的開頭，還可以補全名稱中任何有辨識度的子字串：如果沒有精確匹配，控制檯會開始查詢這樣的單詞——正在補全的字串作為多詞名稱的首字母，或者該單詞僅按相同順序包含此字串的字母。如果找到唯一這樣的單詞，則會在游標位置補全它。例如：

```ros
[admin@MikroTik] > /interface/x[TAB][TAB]_ 
dot1x  vxlan  export
[admin@MikroTik] > /interface/mt[TAB]_
[admin@MikroTik] > /interface/monitor-traffic _

```

## 控制檯搜尋 {#console-search}

控制檯搜尋允許透過 RouterOS 選單列表和歷史記錄執行關鍵字搜尋。可使用 <kbd>Control</kbd>+<kbd>R</kbd> 快速鍵訪問搜尋提示符。

## 內部聊天系統 {#internal-chat-system}

RouterOS 控制檯有一個內建的內部聊天系統。這允許遠端位置的管理員直接在 RouterOS CLI 中互相交談。要開始對話，請在預期訊息前加上 # 符號。傳送訊息時已登入的任何人都將看到該訊息。

```ros
[admin@MikroTik] > # ready to break internet?
[admin@MikroTik] > 
fake_admin: i was born ready
[admin@MikroTik] > 
```

```ros
[fake_admin@MikroTik] > 
admin: ready to break internet?
[fake_admin@MikroTik] > # i was born ready
[fake_admin@MikroTik] > 
```

## 設定 {#settings}

在 `/console/settings` 選單中，可以啟用一個選項，用下劃線替換檔名中的保留字元。

| 屬性 | 描述 |
| :-- | :-- |
| **sanitize-names**  (*yes* *\| no* 預設：**no**) | 將保留字元 (\ / : \* ?  \|) 替換為下劃線 |

## 內建幫助 {#built-in-help}

控制檯具有內建幫助。按 <kbd>F1</kbd> 獲取一般控制檯用法幫助。一般規則是，幫助會顯示在按下 <kbd>F1</kbd> 的位置可以鍵入的內容（類似於按兩次 <kbd>Tab</kbd> 鍵，但以詳細形式並帶有說明）。

## 按鍵列表 {#list-of-keys}

| 按鍵 | 描述 |
| :-- | :-- |
| <kbd>F1</kbd> | 顯示上下文相關幫助 |
| <kbd>F3</kbd> 或 <kbd>Control</kbd>+<kbd>R</kbd> | 搜尋命令歷史 |
| <kbd>F4</kbd> 或 <kbd>Control</kbd>+<kbd>X</kbd> | 切換安全模式 |
| <kbd>F5</kbd> 或 <kbd>Control</kbd>+<kbd>L</kbd> | 重設終端並重繪螢幕 |
| <kbd>F7</kbd> | 切換 HotLock 模式 |
| <kbd>F8</kbd> | 列印整個多行輸入 |
| <kbd>Tab</kbd> | 執行行補全。第二次按下時，顯示可能的補全項。 |
| <kbd>Control</kbd>+<kbd>C</kbd> | 中斷當前操作 |
| <kbd>Control</kbd>+<kbd>D</kbd> | 終止會話（在空提示符下） |
| <kbd>Control</kbd>+<kbd>K</kbd> | 刪除到行尾 |
| <kbd>Control</kbd>+<kbd>U</kbd> | 刪除到行首 |
| <kbd>Control</kbd>+<kbd>T</kbd> | 切換到後臺任務 |
| <kbd>Control</kbd>+<kbd>\\</kbd> | 在游標處拆分行。在游標位置插入換行符。 |
| <kbd>Control</kbd>+<kbd>B</kbd> 或 <kbd>←</kbd> | 將游標向後移動一個字元 |
| <kbd>Control</kbd>+<kbd>F</kbd> 或 <kbd>→</kbd> | 將游標向前移動一個字元 |
| <kbd>Control</kbd>+<kbd>P</kbd> 或 <kbd>↑</kbd> | 轉到上一行。如果這是輸入的第一行，則從歷史記錄中調出上一條輸入。 |
| <kbd>Control</kbd>+<kbd>N</kbd> 或 <kbd>↓</kbd> | 轉到下一行。如果這是輸入的最後一行，則從歷史記錄中調出下一條輸入。 |
| <kbd>Control</kbd>+<kbd>A</kbd> 或 <kbd>Home</kbd> | 將游標移到行首。如果游標已經在開頭，則轉到當前輸入第一行的開頭。 |
| <kbd>Control</kbd>+<kbd>E</kbd> 或 <kbd>End</kbd> | 將游標移到行尾。如果游標已經在末尾，則將其移到當前輸入最後一行的末尾。 |
| <kbd>Delete</kbd> | 刪除游標處的字元 |
| <kbd>Control</kbd>+<kbd>H</kbd> 或 <kbd>Backspace</kbd> | 刪除游標前的字元，並將游標向後移動一個位置 |
| <kbd>#</kbd> | 向內部聊天系統傳送訊息 |
| **/** | 上移到基礎級別 |
| **..** | 上移一級 |
| **/command** | 在基礎級別使用命令 |

<kbd>Up</kbd>、<kbd>Down</kbd> 和拆分鍵會使游標停留在行尾。
