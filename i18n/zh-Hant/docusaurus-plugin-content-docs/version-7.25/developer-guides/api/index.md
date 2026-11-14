---
sidebar_key: "developer-guides/api/index"
sidebar_position: 1
title: "API"
sidebar_label: "API"
description: "API 頁面介紹 RouterOS 的應用程式程式設計介面，用於與路由器進行安全通訊，並詳細說明語法規則、句子結構、編碼方法以及用於配置管理的受支援命令，例如 login 和 cancel。"
tags:
  - 'api'
  - 'management'
source: https://manual.mikrotik.com/docs/7.25/developer-guides/api
captured_at: '2026-11-04T11:15:06+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**應用程式程式設計介面（API）** 允許使用者建立自定義軟體解決方案，以便與 RouterOS 通訊，用於收集資訊、調整配置和管理路由器。API 緊密遵循**命令列介面（CLI）**的語法。你可以使用它建立翻譯後的或自定義的配置工具，使執行和管理 RouterOS 路由器更加容易。

在嘗試建立連線之前，必須啟用 API 服務。預設情況下，API 使用 TCP 埠 **8728** 和 **8729**（安全）。

**API-SSL** 服務可以在兩種模式下執行：使用證書或不使用證書。如果 `/ip service` 設定中未提供證書，用戶端必須使用匿名 Diffie-Hellman 密碼套件來建立連線。如果服務使用證書，用戶端可以建立 TLS 會話。

## 協定 {#protocol}

你透過傳送句子並接收一個或多個句子作為返回來與路由器通訊。句子是由零長度詞終止的詞序列。詞是句子的一部分，以特定方式編碼：編碼長度後跟資料。當路由器收到完整句子（命令詞、一個或多個屬性詞以及零長度詞）時，它會評估並執行該句子，然後形成並返回回覆。

### API 句子 {#api-sentences}

句子是與 API 通訊的主要物件。

- 空句子會被忽略。
- 收到零長度詞後才會處理句子。
- 用戶端在登入前可以傳送的句子數量和大小有限制。
- 不要依賴屬性詞的順序，因為順序和數量可能會被 `.proplist` 屬性改變。

句子結構如下：

- 第一個詞必須包含一個*命令詞*。
- 句子必須包含一個*零長度詞*來終止它。
- 句子可以包含零個或多個*屬性詞*。屬性詞的順序無關緊要。
- 句子可以包含零個或多個*查詢詞*。查詢詞的順序很重要。

:::danger
如果未提供零長度詞，路由器不會開始評估已傳送的詞，並會把後續所有輸入視為同一個句子的一部分。
:::

### API 詞 {#api-words}

- 詞被分組為句子。零長度詞終止一個句子。
- 每個詞都編碼為一個長度，後跟該長度的內容位元組。
- 該方案允許編碼最長 **0xFFFFFFFF** 的長度；僅支援四位元組長度。
- **len** 個位元組按最高有效位元組在前（網路位元組序）傳送。
- 如果詞的第一個位元組 **>= 0xF8**，則它是保留的控制位元組。收到未知控制位元組後，API 用戶端無法繼續，因為它不知道如何解釋後續位元組。
- 目前不使用控制位元組。

詞的長度編碼如下：

| 長度值 | 位元組數 | 編碼 |
|:--|--:|:--|
| <code>0 &lt;= len &lt;= 0x7F</code> | 1 | len，最低位元組 |
| `0x80 <= len <= 0x3FFF`        |            2 | len | 0x8000，兩個低位元組     |
| `0x4000 <= len <= 0x1FFFFF`    |            3 | len | 0xC00000，三個低位元組 |
| <code>0x200000 &lt;= len &lt;= 0xFFFFFFF</code> | 4 | len |
| <code>len &gt;= 0x10000000</code> | 5 | 0xF0 和 len 作為四個位元組 |

一般來說，*詞*可以這樣描述：`<encoded-word-length><word-content>`。
詞內容可以分為五個部分：*[命令詞](#command-word)*、*[屬性詞](#attribute-word)*、*[API 屬性詞](#api-attribute-word)*、*[查詢詞](#query-word)* 和 *[回覆詞](#reply-word)*

#### 命令詞 {#command-word}

句子中的第一個詞必須是命令，後跟屬性詞以及零長度詞或終止詞。命令詞的名稱必須以斜槓（`/`）開頭。命令名稱緊密遵循 CLI。不支援路徑物件之間的空格；必須用斜槓（`/`）替換它們。

某些命令是 API 特有的：

- `login` - 用於登入過程以提供登入憑據。
- `cancel` - 用於取消當前正在執行的命令。

命令詞結構嚴格按以下順序：

- 編碼長度
- 內容字首 */*
- CLI 轉換後的命令

命令詞內容的一些示例：

```ros
/login

```

```ros
/user/active/listen

```

```ros
/interface/vlan/remove

```

```ros
/system/reboot

```

#### 屬性詞 {#attribute-word}

每個*命令詞*都有一個*屬性詞*列表，具體取決於內容。

每個*屬性詞*結構按以下順序由五部分組成：

- 編碼長度
- 內容以等號（`=`）字元為字首
- 屬性名
- 等號（`=`）字元作為名稱和值分隔符
- 屬性值（如果有）

一些屬性示例（不包括編碼長度字首）：

```ros
=address=10.0.0.1

```

```ros
=disable-running-check=yes

```

值可以包含*等號*（`=`）符號：

```
=name=iu=c3Eeg

```

值可以為空：

```ros
=comment=
```

請注意，屬性詞和 **API** 引數的順序並不重要，不應依賴該順序。

#### API 屬性詞 {#api-attribute-word}

API 屬性詞結構嚴格按以下順序：

- 編碼長度
- 內容以點（`.`）字元為字首
- 屬性名
- 等號（`=`）字元作為名稱和值分隔符
- 屬性值

目前，唯一的此類 API 屬性是 [`tag`](#tags)。

#### 查詢詞 {#query-word}

句子可以帶有額外的查詢引數來限制其範圍。詳情請參閱[查詢部分](#queries)。

- 查詢詞以 `?` 開頭。
- 目前，只有 `print` 命令處理查詢詞。

使用查詢詞屬性的句子示例：

```ros
/interface/print
?type=ether
?type=vlan
?#|!

```

:::info
查詢詞的順序很重要
:::

#### 回覆詞 {#reply-word}

它僅由路由器在響應用戶端收到的完整句子時傳送。

- 回覆的第一個詞以 `!` 開頭。
- 傳送的每個句子至少會生成一個回覆（如果連線未被終止）。
- 每個句子的最後一個回覆是第一個詞為 `!done` 的回覆。
- 錯誤和異常情況以 `!trap` 開頭。
- 資料回覆以 `!re` 開頭。
- 沒有資料可回覆的命令的回覆以 `!empty` 開頭。
- 如果必須關閉 **API** 連線，RouterOS 會發送帶有描述中原因的 `!fatal`，然後關閉連線。

## 初始登入 {#initial-login}

- 用戶端在第一條訊息中傳送使用者名稱和密碼。在示例中，我們使用 `admin` 和空密碼：

  ```ros
  /login
  =name=admin
  =password=
  ```

  如果認證成功，路由器會回覆 `!done`。

- 密碼以明文傳送。
- 如果發生錯誤，回覆中包含 `=message=<error message>`。
- 登入成功後，用戶端可以開始發出命令。

## 標籤 {#tags}

**API** 允許同時執行多個命令，而無需等待前一個命令完成。如果 API 用戶端這樣做並且需要區分命令響應，它可以在命令句子中使用 `tag` 引數。

如果句子包含 `tag`，該句子的每個回覆都會攜帶相同的 tag 值。

如果省略 `tag` 引數或將其留空，該命令的響應將不包含 tag 引數。

## 命令說明 {#command-description}

- `/cancel`
  - 可選引數：`=tag=<tag of command to cancel>`；如果沒有該引數，所有正在執行的命令都會被取消。
  - 不會取消自身。
  - 所有被取消的命令都會被中斷，並且通常會生成 `!trap` 和 `!done` 響應。
  - 請注意，`/cancel` 是單獨的命令，可以有自己的唯一 `.tag` 引數，該引數與命令的 `=tag` 引數無關。

- `listen`
  - 凡是有 CLI `print` 命令的地方都可以使用 `listen` 命令，但它可能並非在所有地方都有效。
  - 當特定專案列表發生變化時，會生成 `!re` 句子。
  - 當專案被刪除或消失時，`!re` 句子會包含值 `=.dead=yes`。
  - 此命令不會自行終止；請使用 `/cancel` 命令停止它。

- `getall`
  - 凡是有 CLI `print` 命令的地方都可以使用 `getall` 命令（`getall` 是 `print` 的別名）。
  - 回覆中包含 `=.id=<item internal number>` 屬性。

- `print`
  - API `print` 命令與 CLI 對應命令有以下不同：
    - 不支援 `where` 引數；可以使用[查詢詞](#queries)過濾專案。
    - `.proplist` 引數是一個逗號分隔的屬性名列表，用於指定要包含在返回專案中的屬性。
      - 返回的專案可能包含額外屬性。
      - 返回屬性的順序並不重要，且不能依賴該順序。
      - 如果列表包含重複項，則這些重複項的處理方式未定義。
      - 如果某個屬性出現在 `.proplist` 中，但某個專案沒有該屬性，則該專案的屬性值不存在（對該專案來說，`?name` 求值為 false）。
      - 如果 `.proplist` 不存在，則會按照 `print` 命令的請求包含所有屬性，甚至包括訪問時間較慢的屬性（例如檔案內容和效能計數器）。因此，鼓勵使用 `.proplist`。如果設定了 `=detail=` 引數，省略 `.proplist` 可能會導致較高的效能損失。

### 查詢 {#queries}

`print` 和 `getall` 命令接受查詢詞，用於限制返回的句子集合。

- 查詢詞以 `?` 開頭。
- 查詢詞的順序很重要。查詢從第一個詞開始求值。
- 對列表中的每個專案都會求值查詢。如果查詢成功，則處理該專案；如果查詢失敗，則忽略該專案。
- 查詢使用布林值棧進行求值。初始時，棧中包含無限個 `true` 值。求值結束時，如果棧中至少包含一個 `false` 值，則查詢失敗。
- 查詢詞按以下規則工作：

| 查詢                            | 說明                                |
|:--|:--|
| `?name`                        | 如果專案具有屬性 `name` 的值，則壓入 `true`，否則壓入 `false`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `?-name`                       | 如果專案不具有屬性 `name` 的值，則壓入 `true`，否則壓入 `false`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `?name=x` | 如果屬性 `name` 的值等於 *x*，則壓入 `true`，否則壓入 `false`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `?<name=x`                   | 如果屬性 `name` 的值小於 *x*，則壓入 `true`，否則壓入 `false`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `?>name=x`                   | 如果屬性 `name` 的值大於 *x*，則壓入 `true`，否則壓入 `false`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `?#operations`               | 將操作應用於棧中的值。操作字串從左到右求值。十進位制數字序列後跟任意其他字元或詞尾時，會被解釋為棧索引。棧頂值的索引為 0。後跟字元的索引會把該索引處的值的副本壓入棧。後跟詞尾的索引會用該索引處的值替換所有值。`!` 字元會把棧頂值替換為其相反值。<code>&amp;</code> 彈出兩個值並壓入邏輯 `and` 運算的結果。`\|` 彈出兩個值並壓入邏輯 `or` 運算的結果。索引後的 `.` 不執行任何操作。其他字元後的 `.` 會壓入棧頂值的副本。 |

:::info
API 中不支援正則表示式，因此不要嘗試傳送帶有 **`~`** 符號的查詢
:::

示例：

- 獲取所有乙太網和 VLAN 介面（等價於 CLI 命令 `/interface/print where type=ether || type=vlan`）：

```ros
/interface/print
?type=ether
?type=vlan
?#|

```

- 獲取所有註釋非空的路由（等價於 CLI 命令 `/ip/route/print where comment`）：

```ros
/ip/route/print
?>comment=

```

- 獲取所有 distance 不大於 1 且 gateway 等於 172.16.1.1 的路由（等價於 CLI 命令 `/ip/route/print where !(distance>1 && gateway=172.16.1.1)`）：

```ros
/ip/route/print
?>distance=1
?gateway=172.16.1.1
?#&!

```

### OID {#oid}

`print` 命令可以為 SNMP 中可用的屬性返回 OID 值。

在 CLI 中，可以透過執行 `print oid` 命令檢視 OID 值。在 API 中，這些屬性的名稱以 `.oid` 結尾，可以透過將它們的名稱新增到 `.proplist` 的值中來獲取。示例：

```ros
/system/resource/print
=.proplist=uptime,cpu-load,uptime.oid,cpu-load.oid
```

路由器傳送回覆：

```ros
!re
=uptime=01:22:53
=cpu-load=0
=uptime.oid=.1.3.6.1.2.1.1.3.0
=cpu-load.oid=.1.3.6.1.2.1.25.3.3.1.2.1

!done
```

### !trap {#trap}

當 API 句子因任何原因失敗時，路由器會返回一個 trap，並附帶：

- 一個 `message` 屬性，提供有關失敗的更多詳細資訊。
- 一個 `category` 屬性。如果錯誤是通用錯誤，路由器會返回錯誤類別。該屬性的可能值有：
  - 0 - 缺少專案或命令
  - 1 - 引數值失敗
  - 2 - 命令執行被中斷
  - 3 - 指令碼相關失敗
  - 4 - 通用失敗
  - 5 - API 相關失敗
  - 6 - TTY 相關失敗
  - 7 - 由 :return 命令生成的值

```ros
/ip/address/add
=address=192.168.88.1
=interface=asdf
```

路由器回覆：

```bash
!trap
=category=1
=message=input does not match any value of interface
```

## 修改現有專案 {#modify-existing-items}

與 CLI 對應命令類似，API 有一個 `set` 命令，接受專案 ID 和要設定的引數。
唯一的例外是 API 不允許直接在 `set` 命令中使用查詢。例如，以下 CLI 命令用於在所有乙太網介面上設定 MTU 值：

```ros
/interface set [find where type=ether] mtu=1500
```

要在 API 中實現相同效果，首先需要執行 `print` 查詢來獲取 ID，然後才能執行 `set` 命令。

```ros
/interface/print
=.proplist=.id
?type=ether
```

路由器回覆：

```bash
!re
=.id=*1

!re
=.id=*2
```

現在需要遍歷返回的 ID，併為每個 ID 傳送 `set` 命令：

```ros
/interface/set
=.id=*1
=mtu=1500

/interface/set
=.id=*2
=mtu=1500
```

## 命令示例 {#command-examples}

### `/user/active/listen` {#useractivelisten}

```ros
/user/active/listen

!re
=.id=*68
=radius=no
=when=2006-10-24 08:40:42
=name=admin
=address=0.0.0.0
=via=console

!re
=.id=*68
=.dead=yes

... more !re sentences ...
```

### /cancel，同時執行多個命令 {#cancel-simultaneous-commands}

開始監聽介面變化（tag 為 2）：

```ros
/interface/listen
.tag=2
```

傳送命令以停用介面（tag 為 3）：

```ros
/interface/set
=disabled=yes
=.id=ether1
.tag=3
```

路由器對 `disable` 命令（以 tag 3 執行）回覆 `!done`：

```ros
!done
.tag=3
```

啟用介面（tag 為 4）：

```ros
/interface/set
=disabled=no
=.id=ether1
.tag=4
```

用戶端從路由器收到 `listen` 命令的更新，該更新由第一個 `set` 命令（以 tag 3 執行）所做的更改生成：

```ros
!re
=.id=*1
=disabled=yes
=dynamic=no
=running=no
=name=ether1
=mtu=1500
=type=ether
.tag=2
```

隨後是 `enable` 命令（以 tag 4 執行）的 `done`：

```ros
!done
.tag=4
```

傳送命令以獲取介面列表（tag 為 5）：

```ros
/interface/getall
.tag=5
```

用戶端收到由第二個 `set` 命令（以 tag 4 執行）所做的更改生成的更新：

```ros
!re
=.id=*1
=disabled=no
=dynamic=no
=running=yes
=name=ether1
=mtu=1500
=type=ether
.tag=2
```

用戶端收到對 `getall` 命令（以 tag 5 執行）的回覆：

```ros
!re
=.id=*1
=disabled=no
=dynamic=no
=running=yes
=name=ether1
=mtu=1500
=type=ether
.tag=5

!re
=.id=*2
=disabled=no
=dynamic=no
=running=yes
=name=ether2
=mtu=1500
=type=ether
.tag=5

!done
.tag=5
```

停止監聽 - 請求取消 tag 為 2 的命令，`cancel` 本身使用 tag 7：

```ros
/cancel
=tag=2
.tag=7
```

`listen` 命令被中斷（tag 2）：

```ros
!trap
=category=2
=message=interrupted
.tag=2
```

`cancel` 命令完成（tag 7）：

```ros
!done
.tag=7
```

`listen` 命令完成（tag 2）：

```ros
!done
.tag=2
```

## 示例用戶端 {#example-client}

一個簡單的 [Python3 API 用戶端](./python3-example.md)

使用舊登入方法的示例輸出：

```bash
debian@localhost:~/api-test$ ./api.py 10.0.0.1 admin ''
<<< /login
<<<
>>> !done
>>> =ret=93b438ec9b80057c06dd9fe67d56aa9a
>>>
<<< /login
<<< =name=admin
<<< =response=00e134102a9d330dd7b1849fedfea3cb57
<<<
>>> !done
>>>
/user/getall

<<< /user/getall
<<<
>>> !re
>>> =.id=*1
>>> =disabled=no
>>> =name=admin
>>> =group=full
>>> =address=0.0.0.0/0
>>> =netmask=0.0.0.0
>>>
>>> !done
>>>
```
