---
sidebar_key: "developer-guides/api"
title: "API"
sidebar_label: "API"
description: "API 頁面介紹 RouterOS 的應用程式程式設計介面，用於與路由器進行安全通訊，並詳細說明語法規則、句子結構、編碼方法以及用於配置管理的受支援命令，例如 login 和 cancel。"
tags:
  - 'api'
  - 'management'
source: https://manual.mikrotik.com/docs/developer-guides/api
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**應用程式程式設計介面（API）** 允許使用者建立自定義軟體解決方案，以便與 RouterOS 通訊，用於收集資訊、調整配置和管理路由器。API 緊密遵循**命令列介面（CLI）**的語法。你可以使用它建立翻譯後的或自定義的配置工具，使執行和管理 RouterOS 路由器更加容易。

在嘗試建立連線之前，必須先啟用 API 服務——使用 `/ip/service set api disabled=no` 啟用它。預設情況下，API 使用 TCP 埠 **8728** 和 **8729**（安全）。

**API-SSL** 服務可以在兩種模式下執行：使用證書或不使用證書。如果未為該服務配置證書，服務僅提供匿名 Diffie-Hellman 密碼套件，當前 TLS 用戶端不接受這些套件，因此連線會因握手錯誤而失敗。如果為該服務配置了證書，用戶端可以建立常規 TLS 會話。有關服務設定，請參見 [`ip/service` CLI 參考](../../cli-reference/ip/service/index.md)。

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

- 單詞被分組為句子。零長度單詞終止一個句子。
- 每個單詞編碼為一個長度，後跟該長度的內容位元組。
- 該編碼支援最大 **0xFFFFFFFF** 的長度；五位元組形式（`0xF0` + 四個位元組）編碼最大的長度。
- **len** 位元組按最高有效位在前（網路位元組序）傳送。
- 如果單詞的第一個位元組 **>= 0xF8**，則它是保留的控制位元組。收到未知控制位元組後，API 用戶端無法繼續，因為它不知道如何解釋後續位元組。
- 當前未使用控制位元組。

詞的長度編碼如下：

| 長度值 | 位元組數 | 編碼 |
| :-- | :-- | :-- |
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

```ros
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

`login` 命令支援兩種身份驗證方法：明文方法和舊版 RouterOS 版本的舊式質詢-響應方法。

明文密碼：

```ros
/login
=name=admin
=password=
```

如果身份驗證成功，路由器會回覆 `!done`。密碼以明文傳送。成功登入後，用戶端可以開始發出命令。

如果憑據錯誤或賬戶無法使用 API，路由器會回覆錯誤：

```ros
!trap
=message=invalid user name or password (6)

!done
```

舊式質詢-響應，由較舊 RouterOS 版本使用：

當路由器用 `=ret=<challenge>` 而不是普通的 `!done` 來應答登入時，它期望使用舊版方法。不帶密碼的登入語句會收到質詢應答，例如：

```ros
/login

!done
=ret=93b438ec9b80057c06dd9fe67d56aa9a
```

用戶端在第二條訊息中用使用者名稱和質詢響應進行應答：兩個字元 `00`，後跟對 `0x00` 位元組、密碼和收到的質詢計算得到的小寫十六進位制 MD5 摘要。

```ros
/login
=name=admin
=response=00e134102a9d330dd7b1849fedfea3cb57

!done
```

當前 RouterOS 仍會用質詢來應答不帶密碼的登入語句，但它會以 `invalid user name or password` 拒絕舊版響應。請使用明文方法。

關閉 TCP 連線會結束 API 會話。

## 標籤 {#tags}

**API** 允許同時執行多個命令，而無需等待前一個命令完成。為了區分這些回覆，請將 API 屬性詞 `.tag=<value>` 新增到命令語句中；隨後該語句的每個回覆都會攜帶相同的 `.tag=<value>` 詞。

如果省略 `.tag` 詞或將其值留空，則該命令的回覆不攜帶標籤。

請注意標籤與名為 `tag` 的引數之間的區別：標籤是 API 屬性詞 (`.tag=`)，而諸如 `/cancel` 的 `=tag=` 之類的命令引數是常規屬性詞 (`=name=value`)。

## 命令說明 {#command-description}

- `/cancel`
  - 可選引數：`=tag=<tag of command to cancel>`；如果沒有該引數，所有正在執行的命令都會被取消。
  - 不會取消自身。
  - 所有被取消的命令都會被中斷，並且通常會生成 `!trap` 和 `!done` 響應。
  - 請注意，`/cancel` 是單獨的命令，可以有自己的唯一 `.tag` 引數，該引數與命令的 `=tag` 引數無關。

- `listen`
  - 在 CLI `print` 命令可用的任何地方都可以使用 `listen` 命令，但它可能並非在所有地方都能工作。
  - 當特定專案列表中的內容發生變化時，會生成 `!re` 語句。
  - 當專案被刪除或消失時，`!re` 語句會包含布林值 `=.dead=true`。
  - 此命令不會自行終止；請使用 `/cancel` 命令將其停止。

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

在 CLI 中，可以透過執行 `print oid` 命令檢視 OID 值。在 API 中，帶有 OID 的屬性會透過名稱以 `.oid` 結尾的屬性來暴露；將這些名稱新增到 `.proplist` 的值中即可獲取它們。例如：

```ros
/system/resource/print
=.proplist=uptime,cpu-frequency,uptime.oid,cpu-frequency.oid
```

路由器傳送回覆：

```ros
!re
=uptime=16m44s
=cpu-frequency=864
=uptime.oid=.1.3.6.1.2.1.1.3.0
=cpu-frequency.oid=.1.3.6.1.4.1.14988.1.1.3.14.0

!done
```

並非每個 SNMP 屬性都會透過 API 暴露。帶有 OID 的屬性就是路由器透過 `print oid` 命令顯示的屬性；沒有 OID 的屬性（例如系統資源的 `cpu-load`）沒有對應的 `.oid` 屬性。

### !trap {#trap}

當 API 語句失敗時，路由器會返回一個 trap 語句。該 trap 帶有一個 `message` 屬性，其中包含有關失敗的詳細資訊；某些 trap 還帶有一個 `category` 屬性，表示錯誤類別：

- 0 - 缺少專案或命令
- 1 - 引數值錯誤
- 2 - 命令執行被中斷
- 3 - 與指令碼相關的錯誤
- 4 - 一般錯誤
- 5 - 與 API 相關的錯誤
- 6 - 與 TTY 相關的錯誤
- 7 - 由 :return 命令生成的值

例如，未知命令會返回一個帶有 `=category=0` 的 trap：

```ros
/foobar/print
```

路由器回覆：

```ros
!trap
=category=0
=message=no such command or directory (foobar)

!trap
=message=no such command prefix

!done
```

錯誤的引數值會返回一個僅帶有 `message` 的 trap：

```ros
/ip/address/add
=address=192.168.88.1
=interface=asdf
```

路由器回覆：

```ros
!trap
=message=input does not match any value of interface

!done
```

## 修改現有專案 {#modify-existing-items}

與 CLI 中的對應命令一樣，API 有一個 `set` 命令，它接受專案的 ID 以及要設定的引數。`.id` 屬性的值可以是內部編號（例如 `*1`），或者對於有名稱的專案，可以是名稱（例如 `ether1`）。
唯一的例外是 API 不接受直接使用 `set` 命令進行查詢。例如，用於設定所有乙太網介面上 MTU 的 CLI 命令：

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

路由器對成功的 `set` 以單個 `!done`（無資料）應答，如果未找到該專案，則以 `!trap` 應答。

## 命令示例 {#command-examples}

### listen 通知 {#listen-notifications}

開始監聽介面列表中的變更：

```ros
/interface/listen
```

每當出現或更改某個專案時，路由器會發送一條 `!re` 語句。當某個專案被移除時，`!re` 語句會攜帶布林值 `=.dead=true`：

```ros
!re
=.id=*1
=name=ether1
=disabled=false
=running=true

!re
=.id=*1
=.dead=true
```

使用 `/cancel` 停止監聽。

### /cancel，同時執行多個命令 {#cancel-simultaneous-commands}

開始監聽介面變化（tag 為 2）：

```ros
/interface/listen
.tag=2
```

傳送命令以停用介面（tag 為 3）：

```ros
/interface/set
=disabled=true
=.id=ether1
.tag=3
```

路由器會針對 `disable` 命令（以 tag 3 執行）回覆 `!done`；該變更還會為 `listen` 命令（tag 2）生成一次更新：

```ros
!re
=.id=*1
=disabled=true
=dynamic=false
=running=false
=name=ether1
=mtu=1500
=type=ether
.tag=2

!done
.tag=3
```

啟用介面（tag 為 4）：

```ros
/interface/set
=disabled=false
=.id=ether1
.tag=4
```

該變更會為 `listen` 命令生成另一次更新，隨後為 `enable` 命令返回 `done`：

```ros
!re
=.id=*1
=disabled=false
=dynamic=false
=running=true
=name=ether1
=mtu=1500
=type=ether
.tag=2

!done
.tag=4
```

傳送一個命令以獲取介面列表（標籤為 5）：

```ros
/interface/getall
.tag=5
```

用戶端會收到對 `getall` 命令的回覆（該命令使用標籤 5 執行）：

```ros
!re
=.id=*1
=disabled=false
=dynamic=false
=running=true
=name=ether1
=mtu=1500
=type=ether
.tag=5

!re
=.id=*2
=disabled=false
=dynamic=false
=running=true
=name=ether2
=mtu=1500
=type=ether
.tag=5

!done
.tag=5
```

停止監聽——請求使用標籤 2 取消該命令；`cancel` 本身使用標籤 7：

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

一個簡單的 [Python3 API 用戶端](./python3-example.md)，它支援兩種登入方式，並在終端上列印整個交換過程。
