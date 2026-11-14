---
sidebar_key: "developer-guides/scripting/index"
sidebar_position: 1
title: "指令碼"
sidebar_label: "指令碼"
description: "RouterOS 指令碼透過使用者定義的指令碼實現自動化，這些指令碼由系統排程或流量監控等事件觸發。指令碼使用帶有可選字首、命名引數和物理行格式的命令列語法，支援單行和多行執行。"
tags:
  - 'scripting'
  - 'management'
source: https://manual.mikrotik.com/docs/7.25/developer-guides/scripting
captured_at: '2026-11-04T11:15:08+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 內建一門強大的指令碼語言，用於自動化維護任務。你可以建立使用者自定義指令碼，並將它們繫結到事件上。

你可以把指令碼儲存在 Script repository 中，也可以直接在 CLI 中編寫。常見的觸發器包括 System Scheduler、Traffic Monitoring Tool 和 Netwatch Tool 事件。

如果你已經熟悉 RouterOS 中的指令碼編寫，可以檢視我們的 [技巧與提示](./scripting-tips-and-tricks.md)。

## 行結構 {#line-structure}

RouterOS 指令碼被劃分為若干命令列。命令列會逐條執行，直到指令碼結束或發生執行時錯誤。

### 命令列 {#command-line}

RouterOS CLI 使用以下命令語法：

`[prefix] [path] command [uparam] [param=[value]] .. [param=[value]]`

- [prefix] - `:` 或 `/` 字元表示其後的詞是[全域性命令](#global-commands)還是路徑。從根選單呼叫時，或從相對於所呼叫路徑/命令的選單呼叫時，不需要字首。
- [path] - 指向目標選單級別的相對路徑。可能不是必需的。
- command - 指定選單級別下可用的[命令](#commands)之一。
- [uparam] - 未命名引數，如果命令需要它則必須指定。
- [params] - 一系列命名引數及其後跟的值（如果引數需要值）。

命令列的結束由標記 `;` 或 *NEWLINE* 表示。
用 `()`、`[]` 或 `{}` 括起來的命令不需要任何命令結束字元。命令的結束由整個指令碼的內容決定

```ros
:if ( true ) do={ :put "lala" }
```

巢狀在另一個命令列中的每個命令列都以方括號 `[]` 開始和結束[（命令連線運算子）](#other-operators)。

```ros
:put [/ip route get [find gateway=1.1.1.1]];
```

注意，上面的程式碼包含三個命令列：

- `:put`
- `/ip route get`
- `find gateway=1.1.1.1`

注意，選單專用的 `find` 命令不需要完整路徑，因為路徑是從父命令的路徑推匯出來的。

遵循[行連線規則](#line-joining)，一個命令列可以由多個物理行構成。

### 物理行 {#physical-line}

物理行是一串以行結束（**EOL**）序列終止的字元。可以使用任何標準平臺的行終止序列：

- **Unix** – ASCII LF；
- **Windows** – ASCII CR LF；
- **mac** – ASCII CR；

可以使用標準的 C 換行符約定（`\n`、`\r\n` 字元）。

### 註釋 {#comments}

註釋適用以下規則：

- 註釋以井號字元 `#` 開始，並在物理行末尾結束。
- RouterOS 不支援多行註釋。
- 如果 `#` 字元出現在字串內部，則不會被視為註釋。

```ros
# 这是一条注释
# 注释在下一行继续
:global a; # comment describing variable

:global myStr "part of the string # is not a comment"
```

### 行連線 {#line-joining}

可以使用**反斜槓**字元（`\`）將兩個或多個物理行連線成邏輯行。
將反斜槓用作行連線工具時，適用以下規則：

- 以反斜槓結尾的行不能帶註釋。
- 反斜槓不能延續註釋。
- 除字串字面量外，反斜槓不能延續標記（token）。
- 在字串字面量之外，反斜槓出現在行中其他位置是非法的。

```ros
:if ($a = true \
	and $b=false) do={ :put "$a $b"; }
:if ($a = true \ # bad comment (syntax error)
	and $b=false) do={ :put "$a $b"; }
# comment \
	continued is invalid (syntax error)
```

### 標記之間的空白 {#whitespace-between-tokens}

空白可用於分隔標記。只有當兩個標記的連線可能被解釋為另一個標記時，才需要在它們之間加空白。示例：

```ros
{  
	:local a true; :local b false;
# 不需要空白
	:put (a&&b);
# 需要空白
	:put (a and b);
}

```

以下位置不允許出現空白字元：

- 在 `<parameter>=` 之間。
- 在 `from=`、`to=`、`step=`、`in=`、`do=`、`else=` 之間。

示例：

```ros
#incorrect:
:for i from = 1 to = 2 do = { :put $i }

#正确语法：
:for i from=1 to=2 do={ :put $i }
:for i from= 1 to= 2 do={ :put $i }

#incorrect
/ip route add gateway = 3.3.3.3

#correct
/ip route add gateway=3.3.3.3
```

### 作用域 {#scopes}

變數只能在指令碼中稱為作用域的特定區域內使用。這些區域決定了變數的可見性。在某個塊中宣告的變數只能在該塊及其巢狀塊內、且只能在宣告點之後訪問。

作用域有兩種型別——**全域性**和**區域性**。

#### 全域性作用域 {#global-scope}

全域性作用域（或稱根作用域）是指令碼的預設作用域。它會被自動建立，且無法關閉。

由另一個指令碼設定的全域性變數，可以透過在不賦值的情況下宣告它來訪問。

例如，第一個指令碼把 myVar 的值設為 3：

```ros
:global myVar 3
```

要從另一個指令碼訪問該變數：

```ros
:global myVar
:put "myVar=$myVar"
```

輸出：

```
myVar=3
```

#### 區域性作用域 {#local-scope}

你可以定義用於限制變數訪問的組，這些組稱為區域性作用域。每個區域性作用域都用花括號（`{}`）括起來。

```ros
{  
    :local a 3;
    {  
	:local b 4;  
	:put ($a+$b);
    } #line below will show variable b in light red color since it is not defined in this scope  
    :put ($a+$b);
}

```

變數 `b` 在區域性作用域中宣告，在右花括號之後不可訪問。

在 CLI 中寫入的每一行都被視為一個區域性作用域。
例如，已定義的區域性變數在下一命令列中不可見，並會產生語法錯誤

```ros
[admin@MikroTik] > :local myVar a;
[admin@MikroTik] > :put $myVar
syntax error (line 1 column 7)

```

:::danger
不要在**區域性**作用域內定義**全域性**變數。
:::

即使變數可以被定義為全域性，它也只能在其作用域內可用，除非它被引用為在作用域外可見。

```ros
{  
    :local a 3;
    {  
        :global b 4;
    }  
    :put ($a+$b);
}
```

該程式碼輸出 3，因為 `b` 在作用域外不可見。

下面的程式碼修復了該問題，並按預期輸出 7：

```ros
{  
    :local a 3;
    {  
        :global b 4;
    }
    :global b;  
    :put ($a+$b);
}
```

## 關鍵字 {#keywords}

下列詞是關鍵字，不能用作變數名和函式名：

```
and       or       in

```

## 分隔符 {#delimiters}

下列標記在語法中充當分隔符：

```
()  []  {}  :   ;   $   /

```

## 資料型別 {#data-types}

RouterOS 指令碼語言具有以下資料型別：

| 型別                 | 描述                                           |
|:--|:--|
| **num (number)**     | 64 位有符號整數，可輸入十六進位制；     |
| **bool (boolean)**   | 值可以是 `true` 或 `false`。                     |
| **str (string)**     | 字元序列。                                   |
| **ip**               | IP 地址。                                           |
| **ip-prefix**        | IP 字首。                                            |
| **ip6**              | IPv6 地址。                                         |
| **ip6-prefix**       | IPv6 字首。                                          |
| **id (internal ID)** | 以 `*` 字元為字首的十六進位制值。每個選單項都有一個分配的唯一編號——內部 ID。 |
| **time**             | 日期和時間值。                                  |
| **array**            | 以陣列形式組織的值序列。             |
| **nil**              | 未賦值時的預設變數型別。        |

## 常量轉義序列 {#constant-escape-sequences}

以下轉義序列可用於在字串中定義某些特殊字元：

|  |  |
|:--|:--|
| **\"**  | 插入雙引號。                                               |
| **\\**  | 插入反斜槓。                                                  |
| **\n**  | 插入換行符。                                                    |
| **\r**  | 插入回車符。                                            |
| **\t**  | 插入水平製表符。                                             |
| **\$**  | 輸出 $ 字元。否則，$ 用於連結變數。     |
| **\\_** | 空格。                                                             |
| **\a**  | BEL (0x07)。                                                        |
| **\b**  | 退格 (0x08)。                                                  |
| **\f**  | 換頁 (0x0C)。                                                  |
| **\v**  | 插入垂直製表符。                                               |
| **\xx** | 由十六進位制值表示的列印字元。十六進位制數字應使用大寫字母。 |

例如：

```ros
:put "\48\45\4C\4C\4F\r\nThis\r\nis\r\na\r\ntest";

```

將輸出：

```
HELLO
This
is
a
test
```

## 運算子 {#operators}

### 算術運算子 {#arithmetic-operators}

RouterOS 指令碼語言支援常見的算術運算子：

| 運算子   | 描述           | 示例                        |
|:--|:--|:--|
| **`+`**    | 二元加法       | `:put (3+4);`                  |
| **`-`**    | 二元減法    | `:put (1-6);`                  |
| **`*`**    | 二元乘法 | `:put (4*5);`                  |
| **`/`**    | 二元除法       | `:put (10 / 2); :put ((10)/2)` |
| **`%`**    | 取模運算      | `:put (5 % 3);`                |
| **`-`**    | 一元取負        | `{ :local a 1; :put (-a); }`   |

注意，為使除法正常工作，必須在被除數兩側使用花括號或空格，以免它被誤認為 IP 地址。

### 關係運算符 {#relational-operators}

| 運算子   | 描述      | 示例       |
|:--|:--|:--|
| **`<`**    | 小於             | `:put (3<4);` |
| **`>`**    | 大於          | `:put (3>4);` |
| **`=`**    | 等於            | `:put (2=2);` |
| **`<=`**   | 小於或等於    |               |
| **`>=`**   | 大於或等於 |               |
| **`!=`**   | 不等於        |               |

要對錶達式取反，可以使用 `<expression>=false`。例如，要列印所有不是 "ethernet" 的介面，可以這樣使用表示式取反：

```ros
/interface/print where (name~"ether")=false
```

或者相反地，可以使用 `<expression>=true`：

```ros
/interface/print where (name~"ether")=true
```

### 邏輯運算子 {#logical-operators}

| 運算子         | 描述   | 示例                           |
|:--|:--|:--|
| **`!`**          | 邏輯非   | `:put (!true);`                   |
| **`&&`, `and`**  | 邏輯與   | `:put (true&&true)`               |
| **`\|\|`, `or`** | 邏輯或    | `:put (true\|\|false);`           |
| **`in`**         |               | `:put (1.1.1.1/32 in 1.0.0.0/8);` |

### 位運算子 {#bitwise-operators}

位運算子僅適用於 IP 和 IPv6 地址[資料型別](#data-types)。

| 運算子   | 描述      | 示例                                      |
|:--|:--|:--|
| **`~`**    | 按位取反。   | `:put (~0.0.0.0)` `:put (~::ffff)`           |
| **`\|`**   | 按位或對每一對對應位執行邏輯或運算。在每一對中，如果其中一個位或兩個位為“1”，結果為“1”，否則結果為“0”。 | `:put (192.168.88.0\|0.0.0.255)` `:put (2001::1\|::ffff)` |
| **`^`**    | 按位異或與或相同，但每個位置的結果在兩個位不相等時為“1”，相等時為“0”。 | `:put (1.1.1.1^255.255.0.0)` `:put (2001::ffff:1^::ffff:0)` |
| **`&`**    | 如果第一個位和第二個位都為“1”，按位與的結果為“1”，否則結果為“0”。 | `:put (192.168.88.77&255.255.255.0)` `:put (2001::1111&ffff::)` |
| **`<<`**   | 按給定位數左移，IPv6 地址資料型別不支援。 | `:put (192.168.88.77<<8)` |
| **`>>`**   | 按給定位數右移，IPv6 地址資料型別不支援。 | `:put (192.168.88.77>>24)` |

例如，使用 `&` 運算子根據給定的 IP 和 CIDR 掩碼計算子網地址：

```ros
{
:local IP 192.168.88.77;
:local CIDRnetmask 255.255.255.0;
:put ($IP&$CIDRnetmask);
}
```

獲取給定 IP 地址的最後 8 位：

```ros
 :put (192.168.88.77&0.0.0.255);
```

使用 `|` 運算子和取反的 CIDR 掩碼計算廣播地址：

```ros
{
:local IP 192.168.88.77;
:local Network 192.168.88.0;
:local CIDRnetmask 255.255.255.0;
:local InvertedCIDR (~$CIDRnetmask);
:put ($Network|$InvertedCIDR)
}
```

### 連線運算子 {#concatenation-operators}

| 運算子   | 描述          | 示例                                  |
|:--|:--|:--|
| **`.`**    | 連線兩個字串。| `:put ("concatenate" . " " . "string");` |
| **`,`**    | 連線兩個陣列或向陣列新增一個元素。 | `:put ({1;2;3} , 5 );` |

可以在不使用連線運算子的情況下，將變數值直接新增到字串中：

```ros
:global myVar "world";

# 可以使用连接运算符添加值
:put ("Hello " . $myVar);
# 或不使用运算符
:put "Hello $myVar";
```

使用 `$[]` 和 `$()` 可以執行表示式並把結果值插入字串中：

```ros
:local a 5;
:local b 6;
:put " 5x6 = $($a * $b)";

:put " We have $[ :len [/ip route find] ] routes";
```

### 其他運算子 {#other-operators}

| 運算子 | 描述 | 示例 |
|:--|:--|:--|
| <strong><code>[]</code></strong> | 命令替換隻能包含單條命令列` \| <code>:put [&nbsp;:len "my test string"; ];</code> \|
| <strong><code>()</code></strong> | 子表示式或分組運算子。 | <code>:put ( "value is " . (4+5));</code> |
| <strong><code>$</code></strong> | 替換運算子。 | <code>:global a 5;&nbsp;:put $a;</code> |
| <strong><code>~</code></strong> | 用於將值與 POSIX 擴充套件正則表示式匹配的二元運算子。 | 列印所有閘道器以 202 結尾的路由：<code>/ip/route/print where gateway~"^[0-9 \\.]*202\$"</code> |
| <strong><code>-&gt;</code></strong> | 按鍵獲取陣列元素。 | <br/><code>[admin@x86] &gt;:global aaa &#123;a=1;b=2&#125;</code><br/><code>[admin@x86] &gt;&nbsp;:put ($aaa-&gt;"a")</code><br/><code>1</code><br/><code>[admin@x86] &gt;&nbsp;:put ($aaa-&gt;"b")</code><br/><code>2</code><br/> |

## 變數 {#variables}

指令碼語言有兩種型別的變數：

- **global** - 當前使用者建立的所有指令碼都可訪問，由 [`global`](#global-scope) 關鍵字定義。
- **local** - 僅在當前[作用域](#local-scope)內可訪問，由 `local` 關鍵字定義。

變數可能未定義。此時，解析器會查詢由應用程式提供的內建變數。例如，DHCP 的 `lease-script` 提供了若干內建變數：

```ros
/system script
add name=myLeaseScript policy=\
	ftp,reboot,read,write,policy,test,winbox,password,sniff,sensitive,api \
	source=":log info \$leaseActIP\r\
	\n:log info \$leaseActMAC\r\
	\n:log info \$leaseServerName\r\
	\n:log info \$leaseBound"

/ip dhcp-server set myServer lease-script=myLeaseScript
```

除 RouterOS 內建變數外，每個變數在使用前都必須用 `local` 或 `global` 關鍵字宣告。使用未宣告的變數會導致編譯錯誤。例如：

```ros
# 以下代码将导致编译错误，因为 myVar 在未声明的情况下被使用
:set myVar "my value";
:put $myVar
```

正確的程式碼：

```ros
:local myVar;
:set myVar "my value";
:put $myVar;
```

變數名中的有效字元是字母和數字。如果變數名包含字母或數字以外的任何字元（包括運算子），請用雙引號（`""`）將其括起來。示例：

```ros
#有效变量名
:local myVar;
#无效变量名
:local my-var;
#有效，因为使用了双引号
:global "my-var";
```

如果變數最初定義時沒有賦值，則[變數資料型別](#data-types)會被設為 ***nil***；否則，指令碼引擎會自動確定資料型別。有時需要在一種資料型別與另一種之間進行轉換。這可以透過[資料轉換命令](#global-commands)實現。示例：

```ros
#将字符串转换为数组
:local myStr "1,2,3,4,5";
:put [:typeof $myStr];
:local myArr [:toarray $myStr];
:put [:typeof $myArr]
```

變數名區分大小寫。

```ros
:local myVar "hello"
# 以下行将产生错误，因为变量 myVAr 未定义
:put $myVAr
# 正确代码
:put $myVar
```

不帶值的 `set` 命令會取消變數的定義：

```ros
#从环境中移除变量
:global myVar "myValue"
:set myVar;
```

### 保留變數名 {#reserved-variable-names}

所有內建的 RouterOS 屬性都是保留變數。以與 RouterOS 內建屬性相同的名稱定義的變數可能導致錯誤。為避免此問題，請選擇不同的名稱。

例如，以下指令碼將無法正常工作：

```ros
{
:local type "ether1";
/interface print where name=$type;
}
```

但使用不同的變數定義即可正常工作：

```ros
 {
:local customname "ether1";
/interface print where name=$customname;
}
```

## 命令 {#commands}

### 全域性命令 {#global-commands}

每個全域性命令都應以 **`:`** 標記開頭；否則它會被當作變數處理。

| 命令         | 語法     | 描述          | 示例                |
|:--|:--|:--|:--|
| **/**           |            | 轉到根選單。 |                        |
| **..**          |            | 返回上一級選單。 |                  |
| **?**           |            | 列出所有可用選單命令及簡要說明。 |  |
| **global**      | `:global <var> [<value>]` | 定義全域性變數。 | `:global myVar "something"; :put $myVar;` |
| **local**       | `:local <var> [<value>]` | 定義區域性變數。 | `{ :local myLocalVar "I am local"; :put $myLocalVar; }` |
| **beep**        | `:beep frequency=[num] length=[num]` | 使內建蜂鳴器發聲。 |  |
| **convert** | `:convert from=[arg] to=[arg] transform=[arg]` | 將指定值從一種格式轉換為另一種格式。如果未指定 <code>from</code> 格式，則預設使用自動解析的值（例如，“001”變為“1”，“10.1”變為“10.0.0.1”，等等）。 <ul><li><strong><code>from</code></strong> - 指定值的格式：<em>base32, base64, bit-array-lsb, bit-array-msb, byte-array, hex, num, raw, url</em>。 </li><li><strong><code>to</code></strong> - 指定輸出值的格式：<em>base32, base64, bit-array-lsb, bit-array-msb, byte-array, hex, num, raw, url</em>。 </li><li><strong><code>transform</code></strong> - 指定如何轉換值：<em>lc（將值轉換為小寫）、uc（轉為大寫）、lcfirst（首值轉為小寫）、ucfirst（首值轉為大寫）、crlf、ed25519-private-to-x25519-private、none、rot 13、x25519-private-to-x25519-public、ed25519-private-to-ed25519-public、ed25519-public-to-x25519-public、md5、reverse（反轉文字）、sha512。</em></li></ul> | <code>:put [:convert 001 to=hex ]</code><br/><code>31</code><br/><code>:put [:convert [/ip dhcp-client/option/get hostname raw-value] from=hex to=raw ]</code><br/><code>MikroTik</code><br/><code>:put [:convert transform=lc "AAA"]</code><br/><code>aaa</code> |
| **delay**       | `:delay <time>` | 在給定時間段內不執行任何操作。 |  |
| **environment** | `:environment print <start>` | 列印已初始化變數的資訊。 | `:global myVar true; :environment print;` |
| **error**       | `:error <output>` | 生成控制檯錯誤並停止執行指令碼。 |  |
| **execute** | `:execute <expression>` | 在後臺執行指令碼。可透過設定 <code>file</code> 引數將結果寫入檔案，或透過設定 <code>as-string</code> 將結果列印到 CLI。 <br/> 使用 <code>as-string</code> 引數時，執行的指令碼會被阻塞（不會在後臺執行）。 <br/> 執行的指令碼不能大於&nbsp;64 kB。 | `{ :local j [:execute {/interface print follow where [:log info ~Sname~]}]; :delay 10s; :onerror e {/system script job remove $j}}` |
| **find**        | `:find <arg> <arg> <start>` | 返回子字串或陣列元素的位置。 | `:put [:find "abc" "a" -1];` |
| **grep**        | `:grep script=[str] pattern=[expression] after=[num] before=[num] filename=[str]` | 在終端中執行提供的 `script`，並列印與給定 `pattern` 匹配的行。引數 `after` 和 `before` 設定匹配行前後額外列印多少行。結果可透過 `filename` 引數直接儲存到檔案中。 | `:grep script="/interface print" pattern="ether" after=1 before=1 filename=results.txt` |
| **jobname**     | :jobname   | 返回當前指令碼名稱。 | **將指令碼執行限制為單例項**  ` :if ([/system script job print count-only as-value where script=[:jobname] ] > 1) do={  :error "script instance already running"  }`|
| **len**         | `:len <expression>` | 返回字串長度或陣列元素數量。 | `:put [:len "length=8"];` |
| **log**         | `:log <topic> <message>` | 向[系統日誌](../../diagnostics-monitoring-and-troubleshooting/log/index.md)寫入訊息。可用主題為 `debug`、`error`、`info` 和 `warning`。 | `:log info "Hello from script";` |
| **onerror** | `:onerror <var_name> in={<command>} do={<expression>}` | 捕獲錯誤並獲取錯誤詳情。當 <strong><code>in=&#123;...&#125;</code></strong> 塊發生錯誤時，會執行 <strong><code>do=&#123;...&#125;</code></strong> 塊，&nbsp;並將錯誤詳情寫入 <code>&lt;var_name&gt;</code> 變數。&nbsp; <br/> 引數順序很重要。必須在 <code>do</code> 塊之前設定 <code>error</code> 引數，否則 <code>do</code> 塊將看不到該區域性變數。 <br/><code>:onerror</code> 將返回 <code>false</code>（如果沒有錯誤）和 <code>true</code>（如果有錯誤），除非另有指定（使用 <code>:return</code> 或 <code>:error</code> 等命令），因此可用於&nbsp;<strong><code>:if</code></strong> 條件語句指令碼中。 | `:onerror errorName in={ :error "failure" } do={ :put "Critical $errorName" }` |
| **parse**       | `:parse <expression>` | 解析字串並返回解析後的控制檯命令。可用作函式。 | `:global myFunc [:parse ":put hello!"]; $myFunc;` |
| **pick** | `:pick <var> <start> [<end>]` | 返回元素範圍或子字串。如果未指定數量，則僅從陣列中返回一個元素。 <br/><ul><li><code>var</code> - 要從中選取元素的值。</li><li><code>start</code> - 開始選取的元素（第一個元素索引為 0）。</li><li><code>end</code> - 結束索引（不包含此索引處的元素）。</li></ul> | <code>[admin@MikroTik] &gt; :put [:pick "abcde" 1 3]</code><br/><code>bc</code> |
| **put**         | `:put <expression>` | 將提供的引數列印到終端。 | `:put "Hello world"` |
| **range**       | `:range <var> <var>` | 從指定範圍建立陣列。 | `:put [:range 2 8] 2;3;4;5;6;7;8` |
| **resolve** | `:resolve <arg> [<domain-name>][<server>][<server-port>][<type>]` | 返回給定 DNS 名稱的 IP 地址 <br/><ul><li><code>domain-name</code> - 需要解析的 DNS 名稱。</li><li><code>server</code> - 用於解析 DNS 名稱的特定伺服器（返回的結果不會被快取）。</li><li><code>server-port</code> - 要連線的伺服器埠。</li><li><code>type</code> - any/any6/ipv4/ipv6：<ul><li><code>any</code> - 嘗試解析 IPv4，失敗後嘗試 IPv6。</li><li><code>any6</code> - 嘗試解析 IPv6，失敗後嘗試 IPv4。</li><li><code>ipv4</code> - 僅嘗試解析 IPv4。</li><li><code>ipv6</code> - 僅嘗試解析 IPv6。</li></ul></li></ul> | <code>:put [:resolve "www.mikrotik.com"];</code><br/><code>:put [:resolve domain-name="www.mikrotik.com"];</code><br/><code>:put [:resolve domain-name="www.mikrotik.com" server=192.168.88.1 server-port=53];</code><br/><code>:put [:resolve domain-name="www.mikrotik.com" type=ipv6];</code> |
| **retry**       | `:onerror e {:retry command=<expr> delay=[num] max=[num]} do={<expr>}` | 嘗試執行給定命令 `max` 次，每次嘗試之間使用給定的 `delay`（秒）。失敗時，執行 `do={}` 塊中的命令。 | `:onerror e {:retry command={abc} delay=1 max=2} do={:put "got error"}` |
| **typeof**      | `:typeof <var>` | 返回給定變數的資料型別。 | `:put [:typeof 4];` |
| **rndnum**      | `:rndnum from=[num] to=[num]` | 隨機數生成器。 | `:put [:rndnum from=1 to=99];` |
| **rndstr** | `:rndstr from=[str] length=[num]` | 隨機字串生成器。 <br/><strong><code>from</code></strong> 指定用於構造字串的字元，預設為所有 ASCII 字母和數字。 <br/><strong><code>length</code></strong> 指定要建立的字串長度，預設為 16。 | `:put [:rndstr from="abcdef%^&``" length=33];` |
| **set**         | `:set <var> [<value>]` | 為已宣告的變數賦值。 | `:global a; :set a true;` |
| **serialize** | `:serialize [<value>] to=[arg]` | 將指定值/陣列序列化為 JSON 或 dsv（分隔符分隔值）格式。 <br/><strong><code>value</code></strong> 指定要處理的值。 <br/><strong><code>to</code></strong> 指定格式 -&nbsp;<em>json, dsv</em><br/><strong><code>delimiter</code></strong> 設定“分隔符”。 <br/><strong><code>order</code></strong> 指定變數的順序。 <br/><strong><code>options</code></strong> 指定附加選項*:* <br/><ul><li><em>json.pretty</em>&nbsp; - 使 JSON 輸出在視覺上更美觀<em>；</em></li><li><em>json.no-string-conversion</em> - 防止從控制檯字串型別到 JSON 數字型別的隱式轉換；</li><li><em>dsv.wrap-strings</em> - 將字串值包裹在引號內；</li><li><em>dsv.ignore-size -&nbsp;</em>如果陣列值大小不同，例如&nbsp;<code>a=(1,2);b=(3,4);c=(5,6,7)</code>，此選項會繞過 <code>array size mismatch</code> 錯誤，並在這些槽位中設定“空”值。</li><li><em>dsv.remap</em> - 將字典數組合併為單個字典（在使用“<code>print as-value</code>”時很有用）</li></ul><strong>file-name</strong> 啟用將命令輸出生成到檔案中的選項（可在“/files”部分下載）。 | <code>:put [:serialize value=a,b,c to=json]</code><br/><code>["a","b","c"]</code><br/><br/><code>:local test &#123;a=(1,2,3);b=(4,5,6);c=(7,"text",9)&#125;; :put [ :serialize to=dsv delimiter=";" value=$test order=("c","a","b") ]</code><br/><code>c;a;b</code><br/><code>7;1;4</code><br/><code>text;2;5</code><br/><code>9;3;6</code><br/><br/><code>:global var (&#123; "string"="1234"; "number"=1234 &#125;);:put [ :serialize to=json value=$var ]</code><br/><code>&#123;"number":1234,"string":1234.000000&#125;</code><br/><code>:put [ :serialize to=json value=$var options=json.no-string-conversion ]</code><br/><code>&#123;"number":1234,"string":"1234"&#125;</code><br/><br/><code>:put [:serialize to=dsv options=dsv.remap delimiter="#" [/ip/address/print as-value]]</code><br/><code>.id#address#comment#interface#network</code><br/><code>*1#192.168.88.1/24#defconf#bridge#192.168.88.0</code><br/><code>*2#192.168.69.190/24##ether1#192.168.69.0</code> |
| **deserialize** | `:deserialize [<value>] from=[arg]` | 將指定值/陣列從 JSON 或 dsv（分隔符分隔值）格式反序列化。 <br/><strong><code>from</code></strong> 指定格式 -&nbsp;<em>json, dsv</em><br/><strong><code>delimiter</code></strong> 設定“分隔符”。 <br/><strong><code>options</code></strong> 指定附加選項*:* <br/><ul><li><em>dsv.plain</em> - 將每一行反序列化為陣列（輸入沒有表頭或列名）；</li><li><em>dsv.array</em> - 期望有表頭（列名），並返回字典陣列，其中值對映到表頭中提供的列名。</li><li><em>json.no-string-conversion</em> - 防止從 JSON 字串型別到控制檯值（數字、IP 等）的隱式轉換。</li></ul> | <code>:put [:deserialize from=json value="[\"a\",\"b\",\"c\"]"]</code><br/><code>a;b;c</code><br/><br/><code>:put ([ :deserialize from=dsv delimiter=";" value="a;b;c\n1;findme;3" options=dsv.plain ]-&gt;1-&gt;1)</code><br/><code>findme</code><br/><br/><code>:put ([ :deserialize from=dsv delimiter=";" value="a;b;c\n1;findme;3" options=dsv.plain ]-&gt;0-&gt;1) </code><br/><code>b</code><br/><br/><code>:put ([:deserialize from=dsv "a;b;c\n1;2;3\n4;5;6" delimiter=";" options=dsv.array]-&gt;1-&gt;"b") </code><br/><code>5</code><br/><br/><code>:put ([:deserialize from=dsv "a;b;c\n1;2;3\n4;5;6" delimiter=";" options=dsv.array]-&gt;0-&gt;"c") </code><br/><code>3</code><br/><br/><code>:put [typeof ([:deserialize "&#123; \"str\": \"123\" &#125;" from=json options=json.no-string-conversion]-&gt;"str")]</code><br/><code>str</code><br/><br/><code>:deserialize [/file/get file.json contents] from=json</code> |
| **time**        | `:time <expression>` | 返回執行所提供表示式所需的時間間隔。 | `:put [:time {:for i from=1 to=10 do={ :delay 100ms }}];` |
| **timestamp**   | `:timestamp [use-tz]` | 返回自 `epoch` 以來的時間，其中 `epoch` 為 1970 年 1 月 1 日（星期四），不計閏秒。預設以 UTC 返回時間。使用 `use-tz` 引數可返回按路由器上配置的時區調整後的時間戳。 | `[admin@MikroTik] > :put [:timestamp]``2735w21:41:43.481891543`或`[admin@MikroTik] > :put [:timestamp]``2735w1d21:41:43.481891543`帶日期偏移。 |
| **toarray**     | `:toarray <var>` | 將變數轉換為陣列。 |       |
| **tobool**      | `:tobool <var>` | 將變數轉換為布林值。 |       |
| **toid**        | `:toid <var>` | 將變數轉換為內部 ID。 |       |
| **toip**        | `:toip <var>` | 將變數轉換為 IP 地址。 |     |
| **toip6**       | `:toip6 <var>` | 將變數轉換為 IPv6 地址。 |  |
| **tonum**       | `:tonum <var>` | 將變數轉換為整數。 |       |
| **tostr**       | `:tostr <var>` | 將變數轉換為字串。 |         |
| **totime**      | `:totime <var>` | 將變數轉換為時間。 |            |
| **tonsec**      | `:tonsec <var>` | 將時間轉換為納秒。 | `:put [:tonsec value=10:00]                36000000000000` |
| **tocrlf** | `:tocrlf <var>` | 將行尾轉換為 CRLF。 | <code>:put [:tocrlf "AAA\r\nBBB\r\nCCC" ]</code><br/><code>AAA</code><br/><code>BBB</code><br/><code>CCC</code><br/> |
| **tolf**        | `:tolf <var>` | 將行結束符轉換為 LF。 | `:put [:tolf  "AAA\nBBB\nCCC" ]``AAA``   BBB``      CCC`|
| **nothing**     | `:nothing`  | 返回空值（nothing）。 | `:if ([:nothing] = 0) do={:put true} else={:put false} false :if ([:nothing] > 0) do={:put true} else={:put false}  false :if ([:nothing] < 0) do={:put true} else={:put false}` |

如果變數型別轉換函式無法將新格式應用到所提供的資料，則輸出為空。

例如，如果對值為 "23.8" 或 "cow&chicken" 這類非整數的變數執行 `:tonum <var>` 命令，結果將為空，其資料型別將顯示為 `nil`。

### 通用命令 {#common-commands}

以下命令在大多數子選單中都可用：

| 命令   | 語法 | 描述 |
|:--|:--|:--|
| **add**     | `add <param>=<value>..<param>=<value>`      | 新增新專案。該命令通常具有與 **set** 相同的引數，只是沒有專案編號引數。它會用你指定的值新增一個新專案，通常位於專案列表末尾，在專案順序有意義的位置。有些必需屬性必須提供，例如新地址的介面，而其他屬性除非顯式指定，否則設為預設值。返回所新增專案的內部編號。通用引數：*copy-from* - 複製現有專案。它從另一個專案獲取新專案屬性的預設值。如果你不想做完全相同的副本，可以為某些屬性指定新值。複製有名稱的專案時，通常需要為副本指定新名稱。*place-before* - 將新專案放置在具有指定位置的現有專案之前。因此，將專案新增到列表後無需使用 move 命令。*disabled* - 控制新新增專案的停用/啟用狀態。*comment* - 儲存新建專案的描述。 |
| **remove**  | `remove <id>`                               | 刪除所選專案。 |
| **enable**  | `enable <id>`                               | 啟用所選專案。 |
| **disable** | `disable <id>`                              | 停用所選專案。  |
| **set**     | `set <id> <param>=<value>..<param>=<value>` | 更改所選專案的引數，可以同時指定多個引數。可以透過在引數前指定 '!' 來取消設定該引數。  示例：`/ip firewall filter add chain=blah action=accept protocol=tcp port=123 nth=4,2 print set 0 !port chain=blah2 !nth protocol=udp` |
| **get**     | `get <id> <param>=<value>`                  | 獲取所選專案的引數值。預設不在終端中顯示。如果與 :put 命令結合使用，它會在終端中顯示檢索到的值，例如：`:put [/system/resource/get version]` 將顯示裝置上安裝的 RouterOS 版本。 |
| **print**   | `print <param><param>=[<value>]`            | 列印選單項。輸出取決於所指定的[列印引數](#print-parameters)。顯示可從特定命令級別訪問的所有資訊。因此，`/system/clock/print` 顯示系統日期和時間，`/ip/route/print` 顯示所有路由，等等。如果當前級別中有專案列表且它們不是隻讀的，print 命令還會分配供所有操作該列表專案的命令使用的編號。 |
| **export**  | `export [file=<value>]`                     | 匯出當前選單及其子選單（如果存在）的配置。如果指定了 `file` 引數，則輸出將寫入副檔名為 '.rsc' 的檔案，否則輸出將列印到終端。匯出的命令可以透過 [import 命令](#import)匯入。 |
| **edit**    | `edit <id> <param>`                         | 在內建文字編輯器中編輯所選專案的屬性。可用於編輯包含大量文字的屬性值，例如指令碼，但它適用於所有可編輯屬性。根據終端的能力，會啟動全屏編輯器或單行編輯器。控制檯指令碼的編輯欄位限制為 3 萬個字元。 |
| **find**    | `find <expression>`                         | 返回與給定表示式匹配的專案的內部編號列表。其引數與 **set** 相同，另外還有 *disabled* 或 *active* 之類的標誌引數，它們根據相應標誌的值取 *yes* 或 *no*。要檢視所有標誌及其名稱，請檢視 **print** 命令輸出的頂部。 |
| **move**    | `move <id> [<id>]`                          | 更改列表中專案的順序。第一個引數指定要移動的專案。第二個引數指定將所有要移動的專案放在哪個專案之前（如果省略第二個引數，則放在列表末尾）。 |
| **reset**   | `reset <id> [<param>=<value>]`              | 將引數重設為預設值。你也可以在同一命令中包含帶引數的引數，從而同時重設和配置設定。 |
| **comment** | `comment <id> <value>`                      | 允許為所選專案添加註釋。 |

#### import {#import}

從根選單可以訪問 import 命令，它用於從 [export](#common-commands) 命令建立的檔案或手工編寫的檔案匯入配置。

```ros
[admin@admin] > do { import test.rsc } on-error={ :put "Failure" }
Failure
```

可以使用 `onerror` 引數來捕獲錯誤：

```ros
[admin@admin] > onerror e in={ import test.rsc } do={ :put "Failure - $e" }
Failure - Script Error: bad command name this (line 1 column 1)
```

此外，*`import`* 命令在 *`verbose`* 模式下有新選項——*`dry-run`* 引數用於偵錯，可用於在不更改配置的情況下查詢錯誤。

```ros
[admin@admin] > import test.rsc verbose=yes dry-run
#line 1
this
bad command name this (line 1 column 1)
...
Script Error: found 5 error(s) in import file
```

#### print 引數 {#print-parameters}

`print` 命令有幾個可用的通用引數：

| 引數          | 描述          | 示例      |
|:--|:--|:--|
| **append**         |                      |              |
| **as-value**       | 以引數及其值的陣列形式列印輸出。 | `:put [/ip address print as-value]`        |
| **brief**          | 簡要輸出通常是最簡化的，並表示為包含最常用引數的條目表格。 |  |
| **detail**         | 列印詳細描述，輸出不如簡要輸出易讀，但可能有助於檢視所有引數。 |  |
| **count-only**     | 僅列印當前選單中的條目數量。 |  |
| **file**           | 將輸出寫入檔案。 |  |
| **follow**         | 列印所有當前條目並跟蹤新條目，直到按下 <kbd>ctrl</kbd>-<kbd>c</kbd>。例如在檢視日誌條目時可以使用。 | `/log print follow` |
| **follow-only**    | 僅列印並跟蹤新條目，直到按下 <kbd>ctrl</kbd>-<kbd>c</kbd>。例如在嘗試檢視新日誌條目時可以使用。 | `/log print follow-only` |
| **from**           | 僅從指定項開始列印引數。 | `/user print from=admin` |
| **interval**       | 按選定時間間隔連續列印輸出，適用於跟蹤 `follow` 不可接受時的變化 | `/interface print interval=2` |
| **terse**          | 以緊湊且機器友好的格式顯示詳細資訊。 |  |
| **value-list**     | 資料以表格形式顯示，其中引數按行拆分，可用項按列拆分（可用於解析目的）。 |  |
| **order-by** | 按一個或多個屬性對輸出排序。屬性名前加 `-` 表示降序。最多可指定三個排序欄位。 | <code>/ip/arp/print order-by=address</code><br/><code>/interface/print order-by=-link-downs proplist=name,link-downs</code><br/><code>/interface/ethernet/print stats order-by=-driver-rx-packet where running</code> |
| **without-paging** | 如果輸出無法適應控制檯螢幕，則一次性列印所有資訊而不暫停。 |  |
| **where**          | 後跟 `where` 引數的表示式可用於篩選出匹配的條目。 | `/ip route print where interface="ether1"` |
| **about**          | 返回帶有 `about` 引數的條目，例如 "managed by CAPsMAN " 資訊或警告 | `/interface wifi print where about` |
| **!comments**          | 返回沒有註釋的條目 | `/interface firewall filter print !comments` |

可以一次指定多個引數，例如 `/ip route print count-only interval=1 where interface="ether1"`

## 迴圈與條件語句 {#loops-and-conditional-statements}

### 迴圈 {#loops}

| 命令       | 語法   | 描述  |
|:--|:--|:--|
| **`do..while`** | `:do { <commands> } while=( <conditions> ); :while ( <conditions> ) do={ <commands> };` | 執行命令直到滿足給定條件。 |
| **`for`**       | `:for <var> from=<int> to=<int> step=<int> do={ <commands> }` | 執行命令指定的迭代次數 |
| **`foreach`**   | `:foreach <var> in=<array> do={ <commands> };` | 對列表中的每個元素執行命令。 |

### 條件語句 {#conditional-statement}

| 命令   | 語法 | 描述 |
|:--|:--|:--|
| **`if`**    | `:if (<condition>) do={<commands>} else={<commands>}` | 如果給定條件為 `true`，則執行 `do` 塊中的命令，否則執行 `else` 塊中的命令（如果指定）。 |

示例：

```ros
{  
	:local myBool true;  
	:if ($myBool = false) do={ :put "value is false" } else={ :put "value is true" }
}
```

## 函式 {#functions}

函式的定義方式與全域性變數類似，使用 `global` 關鍵字後跟 `do=` 運算子，其後函式體用花括號（`{}`）括起來。

有兩種傳遞引數的方式：

- 使用特定名稱傳遞引數。
- 不指定引數名直接傳值，此時使用引數 "1"、"2" .. "n" 來引用該值。

```ros
#定义函数并运行它
:global myFunc do={:put "hello from function"}
$myFunc

output:
hello from function

#向函数传递参数
:global myFunc do={:put "arg a=$a"; :put "arg '1'=$1"}
$myFunc a="this is arg a value" "this is arg1 value"

output:
arg a=this is arg a value
arg '1'=this is arg1 value
```

可以使用 **`:return`** 命令返回函式值。

```ros
:global myFunc do={ :return ($a + $b)}
:put [$myFunc a=6 b=2]

output:
8
```

你甚至可以從指令碼環境克隆現有指令碼並將其用作函式。

```ros
#添加脚本
/system script add name=myScript source=":put \"Hello \$myVar !\""

:global myFunc [:parse [/system script get myScript source]]
$myFunc myVar=world

output:
Hello world !
```

指令碼語言也允許透過 `:parse` 命令間接建立函式。

如果函式中包含已定義的全域性變數，且其名稱與傳入引數的名稱匹配，則為相容為舊版本編寫的指令碼，全域性定義的變數會被忽略。**避免使用與全域性變數同名的引數。**

例如：

```ros
:global my2 "123"

:global myFunc do={ :global my2; :put $my2; :set my2 "lala"; :put $my2 }
$myFunc my2=1234
:put "global value $my2"
```

輸出將是：

```
1234
lala
global value 123

```

要從一個函式呼叫另一個函式（巢狀函式），請像宣告變數那樣宣告其名稱：

```ros
:global funcA do={ :return 5 }
:global funcB do={  
	:global funcA;  
	:return ([$funcA] + 4)
}
:put [$funcB]
```

```
Output:
9
```

## 捕獲執行時錯誤 {#catch-run-time-errors}

RouterOS 指令碼允許捕獲執行時錯誤，否則這些錯誤會導致指令碼意外退出。例如，如果失敗，`:resolve` 命令會丟擲錯誤並中斷指令碼。

```
[admin@MikroTik] > { :put [:resolve www.example.com]; :put "lala";}
failure: dns name does not exist

```

你可以捕獲此錯誤並繼續執行指令碼：

```ros
:onerror e {:put [:resolve www.example.com]} do={:put "resolver failed"}
:put "print after failure"

output:

resolver failed
print after failure
```

## 陣列操作 {#operations-with-arrays}

如果陣列中的鍵名包含除小寫字元以外的任何字元，則應將其放在引號中。
例如：

```ros
[admin@ce0] > {:local a { "aX"=1; ay=2 }; :put ($a->"aX")}
1
```

可以使用 `foreach` 命令遍歷鍵和元素：

```ros
[admin@ce0] > :foreach k,v in={2; "aX"=1; y=2; 5} do={:put ("$k=$v")}

0=2
1=5
aX=1
y=2
```

如果 `foreach` 命令只帶一個引數呼叫，則返回元素值：

```ros
[admin@ce0] > :foreach v in={2; "aX"=1; y=2; 5} do={:put ("$v")}

2
5
1
2
```

如果陣列元素帶鍵，則這些元素按字母順序排序；不帶鍵的元素放在帶鍵元素之前，並保持其順序（如上一個示例所示）。

可以使用鍵名更改單個元素的值：

```
[admin@MikroTik] > :global a {x=1; y=2}
[admin@MikroTik] > :set ($a->"x") 5
[admin@MikroTik] > :environment print
a={x=5; y=2}

```

## 指令碼許可權 {#script-permissions}

根據指令碼的呼叫方式，它可能：

- 使用自己的許可權。
- 繼承呼叫者的許可權。

例如，考慮一個擁有完整許可權的使用者和一個未設定許可權的指令碼：

```
/user/print
Columns: NAME, GROUP, LAST-LOGGED-IN, INACTIVITY-POLICY
# NAME   GROUP  LAST-LOGGED-IN       INACTIVITY-POLICY
;;; system default user
0 admin  full   2025-07-22 17:09:59  none
```

```ros
/system script
add dont-require-permissions=no name=add-dhcp-no-perms owner=admin policy="" sour
ce="/ip dhcp-client add interface=ether2; put \"Added DHCP client on ether2!\""

```

讓我們看看在帶和不帶 `use-script-permissions` 引數的情況下執行指令碼會發生什麼：

```ros
[admin@MikroTik] > system/script/run add-dhcp-no-perms  use-script-permissions
not enough permissions (9)
[admin@MikroTik] > system/script/run add-dhcp-no-perms
Added DHCP client on ether2!
```

排程器遵循相同的規則。在 `on-event` 中按名稱呼叫的指令碼，或使用 `/system script run` 呼叫的指令碼，會以排程器條目的許可權（其 `policy`）執行。只有 `use-script-permissions` 才會使指令碼以自己的許可權執行。

為進行比較，請建立兩個以不同方式運行同一指令碼的排程器條目：

```ros
/system scheduler
add interval=10s name=run-script-use-script-perms on-event="/system script run add-dhcp-no-perms use-script-permissions" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
add interval=10s name=run-script-by-name on-event=add-dhcp-no-perms policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
```

日誌顯示，帶有 `use-script-permissions` 的條目失敗，因為指令碼沒有許可權。按名稱呼叫指令碼的條目則使用排程器的許可權新增 DHCP 用戶端：

```ros
/log print
 2026-09-25 17:54:29 script,error executing script add-dhcp-no-perms
 2026-09-25 17:54:29 script,error,debug not enough permissions (9) (/ip/dhcp-client/add; line 1)
 2026-09-25 17:54:29 script,error executing script
 2026-09-25 17:54:29 script,error,debug (scheduler:run-script-use-script-perms) not enough permissions (9) (/ip/dhcp-client/add; line 1)
 2026-09-25 17:54:30 system,info dhcp client added by scheduler:run-script-by-name/script:add-dhcp-no-perms (*2 = /ip dhcp-client add interface=ether2)
```

呼叫者無法執行其策略包含呼叫者不具備的許可權的指令碼：一個具有 `policy=read` 的排程器條目按名稱呼叫具有 `policy=read,write` 的指令碼時，會失敗並顯示 `not enough permissions`。`use-script-permissions` 標誌不會覆蓋此行為。

## 另請參閱 {#see-also}

- [指令碼示例](./scripting-examples.md)
- [指令碼技巧與提示](./scripting-tips-and-tricks.md)
