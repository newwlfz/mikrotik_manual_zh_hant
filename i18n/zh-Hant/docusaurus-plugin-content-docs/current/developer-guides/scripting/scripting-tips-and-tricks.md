---
sidebar_key: "developer-guides/scripting/scripting-tips-and-tricks"
sidebar_position: 2
title: "指令碼技巧與竅門"
sidebar_label: "指令碼技巧與竅門"
description: "本頁提供 MikroTik RouterOS 的指令碼編寫技巧，強調使用內部 ID 而不是字面值的重要性，以避免物件重新編號時出錯。它說明了如何透過 `find` 和型別轉換等命令正確引用介面路由、IP 地址和其他網路元素。"
tags:
  - 'scripting'
source: https://manual.mikrotik.com/docs/developer-guides/scripting/scripting-tips-and-tricks
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

讓我們從基礎開始。在終端中工作時，你習慣使用以下語法來訪問引數：

```text
[admin@r1] /interface> print
Flags: D - dynamic, X - disabled, R - running, S - slave
 #     NAME                                TYPE       ACTUAL-MTU L2MTU  MAX-L2MTU
 0  R  ether1                              ether            1500  1580      1022
[admin@r1] /interface> set 0 name=LAN

```

`print` 命令會臨時儲存一個緩衝區，其中的 id 編號引用內部 ID 編號，所以顯然，如果你嘗試使用不存在的值，指令碼就會失敗，例如下面這個指令碼：

```ros
/system script add name=script1 source={
  /ip route set 1 gateway=3.3.3.3
}

```

指令碼不知道 “1” 指的是什麼，並會丟擲錯誤。正確的方法是使用內部 ID 編號，這些編號可以在執行 `print as-value` 時看到，或者由 find 命令返回，例如：

```ros
[admin@r1] /ip route> :put [find where dst-address="10.0.0.0/8"]
*1

```

因此，在這種情況下，正確的指令碼應為：

```ros
/system script add name=script1 source={
  /ip route set *1 gateway=3.3.3.3
}

```

請注意，不建議直接使用內部編號，因為條目可能被刪除並重新新增；內部 ID 隨後會變化，指令碼就會失敗。請改為在程式碼中使用 `find` 命令：

```ros
/system script add name=script1 source={
  /ip route set [find dst-address="0.0.0.0/0"] gateway=3.3.3.3
}

```

## 為什麼即使指定了正確的值，find 仍不工作？ {#why-find-does-not-work-even-if-correct-value-is-specified}

假設我們想列印某個特定地址：

```text
[admin@r1] /ip address> print where address=111.111.1.1/24
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE

```

我們知道這樣的地址是存在的，那為什麼沒有輸出？

因為指令碼引擎會盡可能積極地進行變數型別轉換，但它並不總能成功。讓我們仔細看看這個特定示例為什麼會失敗。首先，檢查 `address` 是什麼變數型別：

```text
[admin@r1] /ip address> :put [:typeof ([print as-value]->0->"address")]
str

```

所以顯然我們是在把字串與 ip-prefix 進行比較，而從 ip-prefix 到字串的轉換不會自動發生。要解決此問題，我們需要將變數轉換為正確的格式：

```text
[admin@r1] /ip address> print where address=[:tostr 111.111.1.1/24]

Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   111.111.1.1/24     111.111.1.0     ether2

```

或者將查詢值放在雙引號中，直接使用字串：

```text
[admin@r1] /ip address> print where address="111.111.1.1/24"

Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   111.111.1.1/24     111.111.1.0     ether2

```

顯然，如果你從變數中獲取 IP 字首，第二種方法就不適用；在這種情況下，請按第一個示例所示進行轉換，或者用 `"$myVar"` 將變數寫入字串。

## 如何定義空陣列 {#how-to-define-empty-array}

RouterOS 不允許以你認為應該的方式定義空陣列：

```ros
[admin@1p_DUT_wAP ac] /interface> :global array {}
syntax error (line 1 column 17)

```

解決辦法是將空字串轉換為陣列：

```ros
[admin@r1] > :global array [:toarray ""]
[admin@r1] > :environment print
array={}
```

從這裡開始，我們可以使用這個陣列來設定元素：

```ros
[admin@r1] > :set ($array->"el0") "el0_val"
[admin@r1] > :environment print
array={el0="el0_val"}
```

## 如何刪除變數 {#how-to-remove-variables}

你可以使用 `/system script environment remove` 刪除未使用的變數；不過，更推薦的方法是取消設定該變數。

為現有引數不設定任何值會取消設定它；例如：

```ros
[admin@MikroTik] /system script environment> :global myVar 1
[admin@MikroTik] /system script environment> print
 # NAME               VALUE
 0 myVar              1
[admin@MikroTik] /system script environment> :set myVar
[admin@MikroTik] /system script environment> print
 # NAME               VALUE
[admin@MikroTik] /system script environment>

```

## 當 'get' 命令不可用時如何獲取屬性值 {#get-values-for-properties-if-get-command-is-not-available}

某些選單（例如互動式 `info` 命令）沒有 `get` 子命令 —— 請使用 `as-value` 引數來獲取可用於指令碼的值。

下面的示例使用舊版 `wireless` 軟體包（`/interface wireless info`），該軟體包僅在具有舊版無線協定棧的裝置上可用。使用較新 `wifi` 軟體包（例如 hAP ax²）的裝置沒有這些選單：

```ros
[admin@1p_DUT_wAP ac] /interface wireless info> :put [hw-info wlan1 as-value ]
ranges=2312-2732/5/b;g;gn20;gn40;2484-2484/5/b;g;gn20;gn40;rx-chains=0;1;tx-chains=0;1

```

輸出是一個一維陣列，因此你可以輕鬆獲取你感興趣的屬性值。

```ros
[admin@1p_DUT_wAP ac] /interface wireless info> :put ([hw-info wlan1 as-value ]->"tx-chains")
0;1

```

## 始終檢查命令返回的值和型別 {#always-check-what-value-and-type-command-returns}

假設我們嘗試使用 `as-value` 獲取某條特定路由的閘道器，但指令碼沒有返回任何內容：

```ros
[admin@r1] /ip address> :put ([/ip route print as-value where gateway="ether1"]->"gateway")

```

首先，讓我們檢查 `print` 是否真的找到了任何內容：

```ros
[admin@r1] /ip address> :put ([/ip route print as-value where gateway="ether1"])

.id=*400ae12f;distance=255;dst-address=111.111.111.1/32;gateway=ether1;pref-src=111.111.111.1

```

該命令假定輸出將是一個一維陣列，我們可以從中提取名為 `gateway` 的元素。顯然，變數或其型別有問題。讓我們更仔細地檢查一下：

```ros
[admin@r1] /ip address> :global aa ([/ip route print as-value where gateway="ether1"])
[admin@r1] /ip address> :environment print

aa={{.id=*400ae12f; distance=255; dst-address=111.111.111.1/32; gateway={"ether1"}; pref-src=111.11
1.111.1}}

```

現在清楚了，返回值是一個包含一個元素的二維陣列。因此，提取 gateway 的正確順序應該是：

- 獲取二維陣列
- 獲取第一個元素
- 從選中的元素中獲取 `gateway`

```ros
[admin@r1] /ip address> :put ([:pick [/ip route print as-value where gateway="ether1"] 0]->"gateway")

ether1

```

## 將陣列新增到字串時要小心 {#be-careful-when-adding-an-array-to-a-string}

如果你列印陣列或將其追加到現有字串，請務必小心，因為結果可能出乎意料。例如，對於包含兩個元素的陣列：

```ros
[admin@1p_DUT_wAP ac] /> :global array {"cccc", "ddddd"}
[admin@1p_DUT_wAP ac] /> :put ("array value is: " . $array )

array value is: cccc;array value is: ddddd

```

連線運算子（`.`）會將字串新增到每個陣列元素，然後列印輸出。要解決此問題，我們需要先轉換為字串：

```ros
[admin@1p_DUT_wAP ac] /> :put ("array value is: " . [:tostr  $array] )

array value is: cccc;ddddd

```

## 獲取/設定陣列中的未命名元素 {#getset-unnamed-elements-in-an-array}

假設我們有一個包含三個元素的陣列 `{ "el1"; "el2"; "el3" }`。你可以使用 `pick` 命令選取元素，但更好的方法是直接透過索引訪問元素：

```ros
[admin@1p_DUT_wAP ac] /> :global test { "el1"; "el2"; "el3" }
[admin@1p_DUT_wAP ac] /> :put ($test->1)

el2

```

同樣的語法也可用於設定值：

```ros
[admin@1p_DUT_wAP ac] /> :set ($test->2) "el3_changed"
[admin@1p_DUT_wAP ac] /> :environment print

test={"el1"; "el2"; "el3_changed"}

```

## 在二維陣列中設定元素值 {#set-element-value-in-2d-array}

你也可以在二維陣列中直接按索引設定值：

```ros
[admin@1p_DUT_wAP ac] /> :global test {{"11";"12";"13"};{"21";"22";"23"}}
[admin@1p_DUT_wAP ac] > :set ($test->1->1) "22_changed"
[admin@1p_DUT_wAP ac] > :put [($test->1->1)]
22_changed
[admin@1p_DUT_wAP ac] > :environment print
test={{"11"; "12"; "13"}; {"21"; "22_changed"; "23"}}

```

## 讀取另一個指令碼中定義的全域性變數的值 {#read-the-value-of-a-global-variable-defined-in-another-script}

假設我們有一個指令碼聲明瞭一個變數並設定了它的值：

```ros
/system script add name=script1 source={
  :global myVar "hello!"
}
```

全域性變數會在同一使用者的所有指令碼之間共享。其他指令碼即使不先宣告，也可以讀取 `myVar` 的值：

```ros
/system script add name=script2 source={
  :log info "value is: $myVar"
}
```

在使用變數之前先宣告它（`:global myVar;`）仍然是良好的做法 —— 這樣可以讓依賴關係更明確。無論哪種情況，只有在 `script1` 至少執行過一次之後，變數才會有值；讀取從未設定過的變數會返回空值。

要從指令碼中**更改**全域性變數的值，必須先宣告該變數 —— 請參見下一節中的示例。

## 從函式訪問全域性變數 {#accessing-global-variable-from-function}

函式可以讀取在同一會話或指令碼中先前定義的全域性變數（或呼叫另一個函式），而無需在函式內部宣告它：

```ros
:global myVar "test"
:global myFunc do={
  :put "global var=$myVar"
}
[$myFunc]
```

輸出：

```text
global var=test
```

只有在想要**更改**變數的值時，才需要在函式內部宣告該變數：

```ros
:global myVar "test"
:global myFunc do={
  :global myVar;
  :set myVar "new value";
  :put "global var=$myVar"
}
[$myFunc]
```

輸出：

```text
global var=new value
```

為函式中未宣告的變數賦值（沒有 `:global myVar;` 而直接 `:set myVar "new value"`）會導致編譯錯誤。

## 從另一個函式中呼叫函式 {#running-a-function-from-another-function}

在當前會話或指令碼中先前定義的函式，可以直接從另一個函式中呼叫，而無需事先宣告：

```ros
:global addOne do={
  :return ($1 + 1)
}

:global addOneAndReport do={
  :local x 5
  :local y [$addOne $x]
  :put "typeof = $[:typeof $y]"
  :put "result=$y"
}

$addOneAndReport
```

輸出：

```text
typeof = num
result=6
```

當被呼叫的函式定義在同一使用者的另一個指令碼中時，情況也是如此——只要該指令碼至少執行過一次，就可以透過名稱使用該函式。在呼叫函式內部宣告名稱（`:global addOne;`）是可選的，只是讓依賴關係更加明確。

## 始終使用唯一的變數名 {#always-use-unique-variable-names}

最常見的錯誤之一就是使用不唯一的變數名。例如，在函式中定義的變數可能與全域性變數同名，從而導致意外結果：

```ros
:global my2 "123"

:global myFunc do={ :global my2; :put $my2; :set my2 "lala"; :put $my2 }
$myFunc my2=1234
:put "global value $my2"

```

輸出將是：

```text
1234
lala
global value 123

```

另一個常見問題發生在使用者定義的變數與 RouterOS 內建屬性同名時。例如，要列印一條 `dst-address` 在變數中定義的路由：

```ros
[admin@1p_DUT_wAP ac] /ip route> :global "dst-address" "0.0.0.0/0"
[admin@1p_DUT_wAP ac] /ip route> print where dst-address=$"dst-address"
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme,
B - blackhole, U - unreachable, P - prohibit
 #      DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
 0 ADS  0.0.0.0/0                          10.155.136.1              1
 1 ADC  10.155.136.0/24    10.155.136.41   ether1                    0

```

顯然結果不符合預期，簡單的解決辦法是使用唯一的變數名：

```ros
[admin@1p_DUT_wAP ac] /ip route> :global myDst "0.0.0.0/0"
[admin@1p_DUT_wAP ac] /ip route> print where dst-address=$myDst
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme,
B - blackhole, U - unreachable, P - prohibit
 #      DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
 0 ADS  0.0.0.0/0                          10.155.136.1              1

```

## 從類似 "monitor" 的迴圈互動式命令中獲取值 {#get-values-from-looped-interactive-commands-like-monitor}

一個常見問題是如何在指令碼中獲取由 `monitor` 等互動式命令返回的值。第一個問題是這些命令會無限執行，直到使用者干預，而指令碼無法做到這一點。應改用 `once` 引數執行它們，該引數會使命令執行一次然後停止。另一個問題是獲取返回的變數：沒有 `as-value`，也沒有 `get`，但有 `do`。它允許你訪問命令返回的變數。例如：

```ros
[admin@1p_DUT_wAP ac] /interface> monitor-traffic ether1 once do={:global myBps $"rx-bits-per-second" }
...
[admin@1p_DUT_wAP ac] /interface> :environment print

myBps=71464

```

## 獲取 fetch 工具接收的檔案內容 {#get-file-content-received-by-fetch-tool}

fetch 工具可以輕鬆地將檔案內容下載到記憶體中，並從指令碼訪問它。為此，請將 `as-value` 引數與 `output=user` 一起使用：

```ros
[admin@rack1_b34_CCR1036] > :put ([/tool fetch ftp://admin:@10.155.136.41/test.txt
 output=user as-value ]->"data")

my file content

```

## 檢查指令碼許可權 {#check-script-permissions}

假設我們有一個建立檔案並向其寫入內容的指令碼：

```ros
/system script add name=script1 policy=ftp,read,write source={
        /file print file=test;
        /file set test.txt contents="my content"
}

```

現在讓我們新增一個排程器，它將嘗試執行此指令碼：

```ros
/system scheduler
add interval=10s name=test on-event=script1 policy=read,write

```

等待 10 秒後，我們可以看到檔案沒有被建立。如果你仔細觀察，指令碼需要 "ftp" 策略才能建立檔案，但排程器只有 "read" 和 "write" 策略。要解決此問題，請將排程器設定為使用正確的策略 "read,write,ftp" 執行。

當你從 netwatch、ppp `on-event` 以及類似鉤子執行指令碼時，這也適用，這些鉤子僅限於 `read,write,test,reboot` 策略。在這種情況下，你無法執行建立備份或檔案之類的高階指令碼。

你可以使用 `dont-require-permissions` 解決此限制，但在授予指令碼不受限制的許可權時要非常小心。

## 使用 dont-require-permissions 時要小心 {#be-careful-when-using-dont-require-permissions}

可以使用 `dont-require-permissions` 引數設定指令碼。基本上，它允許任何沒有足夠許可權的人執行該指令碼。例如，如果指令碼具有策略 "read,write,test,sensitive"，但執行該指令碼的使用者或應用程式許可權較少（例如只有 "read,write"），那麼透過設定 `dont-require-permissions=yes`，我們仍將允許執行指令碼。

這可能會允許使用指令碼更改敏感資訊，即使執行該指令碼的使用者沒有足夠的許可權。
