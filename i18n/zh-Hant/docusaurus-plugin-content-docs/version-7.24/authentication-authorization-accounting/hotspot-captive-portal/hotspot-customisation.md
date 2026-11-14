---
sidebar_key: "authentication-authorization-accounting/hotspot-captive-portal/hotspot-customisation"
sidebar_position: 1
title: "熱點自定義"
sidebar_label: "熱點自定義"
description: "透過在路由器的 FTP 伺服器上覆蓋預設 HTML 檔案來自定義 HotSpot 認證頁面，並透過 HotSpot 配置檔案中的“html-directory-override”指定自定義目錄。可從 login.html、status.html 和 logout.html 等預定義頁面中選擇，或使用 $(username) 和 $(password) 等變數建立自定義頁面。"
tags:
  - 'hotspot'
  - 'servlet-pages'
  - 'radius'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/hotspot-captive-portal/hotspot-customisation
captured_at: '2026-11-04T11:27:04+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

#### 簡介 {#introduction}

你可以為每個已有的 HotSpot 伺服器建立一套完全不同的 Servlet 頁面，方法是在 HotSpot 伺服器配置檔案 `/ip/hotspot/profile` 的 "html-directory-override" 屬性中指定目錄。建立伺服器配置檔案後，預設的 Servlet 頁面會立即複製到 "hotspot" 目錄中。可以透過使用 FTP 用戶端連線到路由器來訪問此目錄。你可以複製此目錄，並使用本手冊本節中的資訊隨意修改頁面。請注意，建議手動編輯檔案，因為自動化 HTML 編輯工具可能會刪除變數或其他關鍵部分，從而損壞頁面。完成內容修改後，你需要將此修改後的內容上傳到熱點路由器上的某個自定義目錄，並將前面提到的 "html-directory-override" 屬性值指向這個新的自定義 HTML 目錄的路徑。

**注意：** 如果 "html-directory-override" 值路徑缺失或為空，則熱點伺服器將恢復為預設 HTML 檔案。

#### 可用頁面 {#available-pages}

向用戶顯示的主要 HTML Servlet 頁面：

- **redirect.html** - 將使用者重定向到另一個 URL（例如，重定向到登入頁面）。
- **login.html** - 向用戶顯示以要求輸入使用者名稱和密碼的登入頁面。此頁面可使用以下引數：
  - **username** - 使用者名稱。
  - **password** - 明文密碼（在使用 PAP 認證時），或 chap-id 變數、密碼和 CHAP challenge 的 MD5 雜湊（在使用 CHAP 認證時）。對於試用使用者，此值用作電子郵件地址。
  - **dst** - 重定向之前請求的原始 URL。登入成功後將開啟此 URL。
  - **popup** - 登入成功時是否彈出狀態視窗。
  - **radius\<id>** - 將用 \<id> 標識的屬性以文字字串形式傳送到 RADIUS 伺服器（如果使用 RADIUS 認證；否則會丟失）。
  - **radius\<id>u** - 將用 \<id> 標識的屬性以無符號整數形式傳送到 RADIUS 伺服器（如果使用 RADIUS 認證；否則會丟失）。
  - **radius\<id>-\<vnd-id>** - 將用 \<id> 標識且供應商 ID 為 \<vnd-id> 的屬性以文字字串形式傳送到 RADIUS 伺服器（如果使用 RADIUS 認證；否則會丟失）。
  - **radius\<id>-\<vnd-id>u** - 將用 \<id> 標識且供應商 ID 為 \<vnd-id> 的屬性以無符號整數形式傳送到 RADIUS 伺服器（如果使用 RADIUS 認證；否則會丟失）。
- **md5.js** - 用於 MD5 密碼雜湊的 JavaScript。與 http-chap 登入方法一起使用。
- **alogin.html** - 用戶端登入後顯示的頁面。它會彈出狀態頁面，並將瀏覽器重定向到最初請求的頁面（在使用者被重定向到 HotSpot 登入頁面之前請求的頁面）。
- **status.html** - 狀態頁面，顯示用戶端的統計資訊。它還能夠自動顯示廣告。
- **logout.html** - 登出頁面，在使用者登出後顯示。顯示有關已結束會話的最終統計資訊。此頁面可使用以下附加引數：
  - **erase-cookie** - 登出時是否從 HotSpot 伺服器刪除 cookie（使下次無法從同一瀏覽器使用 cookie 登入，在多使用者環境中可能有用）。
- **error.html** - 錯誤頁面，僅在發生致命錯誤時顯示。

如果需要更多控制，還可使用一些其他頁面：

- **rlogin.html** - 如果訪問某個 URL 需要用戶端授權，則將該用戶端從其他 URL 重定向到登入頁面的頁面
- **rstatus.html** - 與 rlogin.html 類似，但僅在用戶端已登入且原始 URL 未知的情況下使用
- **radvert.html** - 將用戶端重定向到計劃廣告連結
- **flogin.html** - 如果發生某種錯誤（例如使用者名稱或密碼無效），則代替 login.html 顯示
- **fstatus.html** - 如果請求狀態頁面但用戶端未登入，則代替重定向顯示
- **flogout.html** - 如果請求登出頁面但用戶端未登入，則代替重定向顯示

#### Servlet 頁面服務 {#serving-servlet-pages}

HotSpot Servlet 識別 5 種不同的請求型別：

1. **對遠端主機的請求**
   - 如果使用者已登入且廣告已到顯示時間，則顯示 radvert.html。此頁面會重定向到計劃廣告頁面。
   - 如果使用者已登入且未為此使用者安排廣告，則提供所請求的頁面。
   - 如果使用者未登入，但目標主機被 Walled Garden 允許，則也會提供該請求。
   - 如果使用者未登入，且目標主機被 Walled Garden 禁止，則顯示 rlogin.html；如果找不到 rlogin.html，則使用 redirect.html 重定向到登入頁面。
2. **對 HotSpot 主機上 "/" 的請求**
   - 如果使用者已登入，則顯示 rstatus.html；如果找不到 rstatus.html，則使用 redirect.html 重定向到狀態頁面。
   - 如果使用者未登入，則顯示 rlogin.html；如果找不到 rlogin.html，則使用 redirect.html 重定向到登入頁面。
3. **對 "/login" 頁面的請求**
   - 如果使用者已成功登入（或已經登入），則顯示 alogin.html；如果找不到 alogin.html，則使用 redirect.html 重定向到最初請求的頁面或狀態頁面（如果未提供原始目標頁面）。
   - 如果使用者未登入（未提供使用者名稱，且未出現錯誤訊息），則顯示 login.html。
   - 如果登入過程失敗（提供了錯誤訊息），則顯示 flogin.html；如果找不到 flogin.html，則使用 login.html。
   - 在發生致命錯誤時，顯示 error.html。
4. **對 "/status" 頁面的請求**
   - 如果使用者已登入，則顯示 status.html。
   - 如果使用者未登入，則顯示 fstatus.html；如果找不到 fstatus.html，則使用 redirect.html 重定向到登入頁面。
5. **對 '/logout' 頁面的請求**
   - 如果使用者已登入，則顯示 logout.html。
   - 如果使用者未登入，則顯示 flogout.html；如果找不到 flogout.html，則使用 redirect.html 重定向到登入頁面。

**注意：** 如果無法使用路由器 FTP 伺服器上儲存的頁面滿足請求，則顯示 Error 404。

有許多方法可以自定義 HotSpot 認證頁面的外觀：

- 這些頁面易於修改。它們儲存在路由器 FTP 伺服器上你為相應 HotSpot 伺服器配置檔案選擇的目錄中。
- 透過更改用戶端傳送到 HotSpot Servlet 的變數，可以將關鍵字數量減少到一個（使用者名稱或密碼；例如，用戶端的 MAC 地址可用作另一個值），甚至減少到零（許可證協定；可使用對所有使用者通用的一些預定義值或用戶端的 MAC 地址作為使用者名稱和密碼）。
- 註冊可以在另一臺伺服器上進行（例如，在能夠進行信用卡扣費的伺服器上）。可以將用戶端的 MAC 地址傳遞給它，這樣就不必手動輸入此資訊。註冊後，伺服器應更改 RADIUS 資料庫，使用戶端能夠在一段時間內登入。

要在 HTML 檔案中的某個位置插入變數，請使用 $(var\_name) 語法，其中 "var\_name" 是變數名（不帶引號）。此構造可用於以 '/', '/login', '/status' 或 '/logout' 訪問的任何 HotSpot HTML 檔案，以及儲存在 HotSpot 伺服器上的任何文字或 HTML（.txt、.htm 或 .html）檔案（流量計數器除外，它們僅在狀態頁面中可用；**error**、**error-orig**、**chap-id**、**chap-challenge** 和 **popup** 變數也除外，它們僅在登入頁面中可用）。例如，要顯示指向登入頁面的連結，可使用以下構造：

```
login

```

#### 變數 {#variables}

所有 Servlet HTML 頁面都使用變數來顯示使用者特定的值。變數名僅出現在 Servlet 頁面的 HTML 原始碼中——HotSpot Servlet 會自動將它們替換為相應的值。對於大多數變數，括號中包含了其可能值的示例。所有描述的變數在所有 Servlet 頁面中都有效，但其中一些在訪問時可能為空（例如，在使用者登入之前沒有 uptime）。

##### 可用變數列表 {#list-of-available-variables}

**注意：** 某些變數使用硬編碼的 http URL，如果你使用 https，可以用其他方式構造連結，例如對於 $link-status，你可以使用 https://$(hostname)/$(target-dir)status

**通用伺服器變數：**

- **hostname** - HotSpot Servlet 的 DNS 名稱或 IP 地址（如果未提供 DNS 名稱）（"[hotspot.example.net](http://hotspot.example.net)"）。
- **identity** - RouterOS 標識名稱（"MikroTik"）。
- **login-by** - 使用者使用的認證方法。
- **plain-passwd** - 以 "yes/no" 表示是否允許 HTTP-PAP 登入方法（"no"）。
- **server-address** - HotSpot 伺服器地址（"10.5.50.1:80"）。
- **ssl-login** - 以 "yes/no" 表示是否使用 HTTPS 方法訪問該 Servlet 頁面（"no"）。
- **server-name** - HotSpot 伺服器名稱（在 `/ip/hotspot` 選單中設定為 name 屬性）。

**連結：**

- **link-login** - 指向登入頁面的連結，包含所請求的原始 URL（"[http://10.5.50.1/login?dst=http://www.example.com/](http://10.5.50.1/login?dst=http://www.example.com/)"）
- **link-login-only** - 指向登入頁面的連結，不包含所請求的原始 URL（"[http://10.5.50.1/login](http://10.5.50.1/login)"）
- **link-logout** - 指向登出頁面的連結（"[http://10.5.50.1/logout](http://10.5.50.1/logout)"）
- **link-status** - 指向狀態頁面的連結（"[http://10.5.50.1/status](http://10.5.50.1/status)"）
- **link-orig** - 所請求的原始 URL（"[http://www.example.com/](http://www.example.com/)"）

**常規用戶端資訊：**

- **domain** - 使用者的域名（"[example.com](http://example.com)"）。
- **interface-name** - 物理 HotSpot 介面名稱（對於橋接介面，將返回實際的橋接埠名稱）。
- **ip** - 用戶端的 IP 地址（"10.5.50.2"）。
- **logged-in** - 如果使用者已登入則為 "yes"，否則為 "no"（"yes"）。
- **mac** - 使用者的 MAC 地址（"01:23:45:67:89:AB"）。
- **trial** - 以 "yes/no" 表示使用者是否有試用時間訪問許可權。如果使用者的試用時間已過期，則該值為 "no"。
- **username** - 使用者的名稱（"John"）。
- **host-ip** - 來自 `/ip/hotspot/host` 表的用戶端 IP 地址。
- **vlan-id** - 表示用戶端所連線的 VLAN 介面的 ID。

**使用者狀態資訊：**

- **idle-timeout** - 空閒超時（"20m"，如果沒有則為 ""）。
- **idle-timeout-secs** - 以秒為單位的空閒超時（"88"，如果沒有此類超時則為 "0"）。
- **limit-bytes-in** - 傳送的位元組限制（"1000000"，如果沒有限制則為 "---"）。
- **limit-bytes-out** - 接收的位元組限制（"1000000"，如果沒有限制則為 "---"）。
- **refresh-timeout** - 狀態頁面重新整理超時（"1m30s"，如果沒有則為 ""）。
- **refresh-timeout-secs** - 以秒為單位的狀態頁面重新整理超時（"90s"，如果沒有則為 "0"）。
- **session-timeout** - 留給使用者的會話時間（"5h"，如果沒有則為 ""）。
- **session-timeout-secs** - 留給使用者的會話時間，以秒為單位（"3475"，如果沒有此類超時則為 "0"）。
- **session-time-left** - 留給使用者的會話時間（"5h"，如果沒有則為 ""）。
- **session-time-left-secs** - 留給使用者的會話時間，以秒為單位（"3475"，如果沒有此類超時則為 "0"）。
- **uptime** - 當前會話的執行時間（"10h2m33s"）。
- **uptime-secs** - 當前會話的執行時間，以秒為單位（"125"）。

**流量計數器，僅在狀態頁面中可用：**

- **bytes-in** - 從使用者接收的位元組數（"15423"）。
- **bytes-in-nice** - 從使用者接收位元組數的使用者友好形式（"15423"）。
- **bytes-out** - 傳送給使用者的位元組數（"11352"）。
- **bytes-out-nice** - 傳送給使用者位元組數的使用者友好形式（"11352"）。
- **packets-in** - 從使用者接收的封包數（"251"）。
- **packets-out** - 傳送給使用者的封包數（"211"）。
- **remain-bytes-in** - 直到達到 limit-bytes-in 前的剩餘位元組數（"337465"，如果沒有限制則為 "---"）。
- **remain-bytes-out** - 直到達到 limit-bytes-out 前的剩餘位元組數（"124455"，如果沒有限制則為 "---"）。

**其他變數：**

- **session-id** - 上次請求中 'session-id' 引數的值。
- **var** - 上次請求中 'var' 引數的值。
- **error** - 錯誤訊息，如果發生失敗（"invalid username or password"）。
- **error-orig** - 原始錯誤訊息（不包含從 errors.txt 獲取的翻譯），如果發生失敗（"invalid username or password"）。
- **chap-id** - chap ID 的值（"\371"）。
- **chap-challenge** - chap challenge 的值（"\357\015\330\013\021\234\145\245\303\253\142\246\133\175\375\316"）。
- **popup** - 是否彈出複選框（"true" 或 "false"）。
- **advert-pending** - 是否有廣告待顯示（"yes" 或 "no"）。
- **http-status** - 允許設定 http 狀態碼和訊息。
- **http-header** - 允許設定 http 標頭。

**RADIUS 相關變數：**

- **radius\<id>** - 以文字字串形式顯示由 \<id> 標識的屬性（如果使用了 RADIUS 認證；否則為 ""）
- **radius\<id>u** - 以無符號整數形式顯示由 \<id> 標識的屬性（如果使用了 RADIUS 認證；否則為 "0"）
- **radius\<id>-\<vnd-id>** - 以文字字串形式顯示由 \<id> 標識且供應商 ID 為 \<vnd-id> 的屬性（如果使用了 RADIUS 認證；否則為 ""）
- **radius\<id>-\<vnd-id>u** - 以無符號整數形式顯示由 \<id> 標識且供應商 ID 為 \<vnd-id> 的屬性（如果使用了 RADIUS 認證；否則為 "0"）

##### 使用變數 {#working-with-variables}

這些頁面中可以使用 $(if \<var\_name>) 語句。如果 \<var\_name> 的值不是空字串，則將包含以下內容。它等價於 $(if \<var\_name> != "")。也可以進行相等比較：$(if \<var\_name> == \<value>)。這些語句生效直到 $(elif \<var\_name>)、$(else) 或 $(endif)。一般情況下如下所示：

```
some content, which will always be displayed
$(if username == john)
Hey, your username is john
$(elif username == dizzy)
Hello, Dizzy! How are you? Your administrator.
$(elif ip == 10.1.2.3)
You are sitting at that old computer, which is so slow...
$(elif mac == 00:01:02:03:04:05)
This is an ethernet card, which was stolen few months ago...
$(else)
I don't know who you are, so lets live in peace.
$(endif)
other content, which will always be displayed

```

這些表示式中只會顯示一個。具體顯示哪一個取決於每個用戶端這些變數的值。

##### 重定向和自定義標頭 {#redirects-and-custom-headers}

```
	$(if http-status == 302)Hotspot login required$(endif)
	$(if http-header == "Location")$(link-redirect)$(endif)

```

**注意：** 儘管上面的內容看起來使用了條件表示式 'if'，但實際上它是在將 'http-status' 設定為 '302'，而不是在測試它。這同樣適用於變數 'http-header'。再次說明，儘管它使用了 'if'，但實際上是在將變數設定為 'Location'，後接由變數 'link-redirect' 設定的 URL。

例如，在 $(link-redirect) 求值為 "[http://192.168.88.1/login](http://192.168.88.1/login)" 的情況下，返回給用戶端的 HTTP 響應將變為：

```
HTTP/1.0 302 Hotspot login required
<regular HTTP headers>
Location: http://192.168.88.1/login

```

**http-status 語法**：

```
	$(if http-status == XYZ)HTTP_STATUS_MESSAGE$(endif)

```

- *XYZ* - 你希望返回的狀態碼。應為 3 個十進位制數字，第一位不能為 0。
- *HTTP\_STATUS\_MESSAGE* - 你希望返回給用戶端的任何文字，它將出現在 HTTP 回覆中上述狀態碼之後。

在任何 HTTP 響應中，它將位於第一行，如下所示：

```
HTTP/1.0 XYZ HTTP_STATUS_MESSAGE

```

**http-header 語法：**

```
$(if http-header == HTTP_HEADER_NAME)HTTP_HEADER_VALUE$(endif)

```

- *HTTP\_HEADER\_NAME* - 要在響應中傳送的 HTTP 標頭的名稱
- *HTTP\_HEADER\_VALUE* - 名為 HTTP\_HEADER\_NAME 的 HTTP 標頭要在響應中傳送的值

HTTP 響應將如下所示：

```
HTTP_HEADER_NAME: HTTP_HEADER_VALUE

```

HTTP\_HEADER\_VALUE 和 HTTP\_STATUS\_MESSAGE 中的所有變數和條件表示式都會照常處理。

如果添加了多個同名標頭，則只會使用最後一個（之前的將被丟棄）。這允許系統覆蓋常規 HTTP 標頭（例如 Content-Type 和 Cache-Control）。

#### 自定義錯誤訊息 {#customizing-error-messages}

所有錯誤訊息都儲存在相應 HotSpot Servlet 目錄中的 errors.txt 檔案內。你可以更改所有這些訊息並將其翻譯為你的母語。為此，請編輯 errors.txt 檔案。你還可以在訊息中使用變數。所有說明都在該檔案中給出。

#### HotSpot 頁面的多個版本 {#multiple-versions-of-hotspot-pages}

支援為同一 HotSpot 伺服器提供多套 HotSpot 頁面。它們可以由使用者選擇（用於選擇語言），或由 JavaScript 自動選擇（用於選擇 PDA/常規版本的 HTML 頁面）。

要使用此功能，請在 HotSpot HTML 目錄中建立子目錄，並將那些不同的 HTML 檔案放入該子目錄。例如，要將所有內容翻譯為拉脫維亞語，可以建立子目錄 "lv"，其中包含已翻譯為拉脫維亞語的 login.html、logout.html、status.html、alogin.html、radvert.html 和 errors.txt 檔案。如果在請求的子目錄中找不到所請求的 HTML 頁面，則將使用主目錄中對應的 HTML 檔案。主 login.html 檔案會包含指向 "/lv/login?dst=$(link-orig-esc)" 的連結，然後顯示拉脫維亞語版本的登入頁面：Latviski。而拉脫維亞語版本會包含指向英語版本的連結：English

引用目錄的另一種方法是指定 'target' 變數：

```
        Latviski
        English

```

選擇首選目錄後（例如 "lv"），所有指向本地 HotSpot 頁面的連結都將包含該路徑（例如，$(link-status) = "[http://hotspot.mt.lv/lv/status](http://hotspot.mt.lv/lv/status)"）。因此，如果所有 HotSpot 頁面都使用 "$(link-xxx)" 變數引用連結，則無需再做更多更改——每個用戶端將始終停留在所選目錄中。

#### 其他 {#misc}

如果你想使用 HTTP-CHAP 認證方法，則需要在登入表單的 **提交操作** 之前包含 **doLogin()** 函式（該函式引用必須已載入的 **md5.js**）。否則，CHAP 登入將失敗。

在 HTTP-CHAP 方法下，傳送到 HotSpot 閘道器的最終密碼由以下內容的拼接進行 MD5 雜湊形成：chap-id、使用者密碼和 chap-challenge（按給定順序）

如果要在連結中直接使用變數，則必須相應地進行轉義。例如，在登入頁面中，如果使用者名稱為 "123&456=1 2"，則 **link** 將無法按預期工作。在這種情況下，必須使用 $(user) 的轉義版本：$(user-esc)：**link**。現在同一使用者名稱將轉換為 "123%26456%3D1+2"，這是 "123&456=1 2" 在 URL 中的有效表示形式。此技巧可用於任何變數，而不僅是 $(username)。

登出頁面有一個布林引數 "erase-cookie"，其值可以是 "on" 或 "true"，用於在登出時刪除使用者 cookie（這樣使用者下次開啟瀏覽器時就不會自動登入）。

#### 示例 {#examples}

具備基本 HTML 語言知識並參考以下示例，應該很容易實現上述想法：

- 要提供預定義值作為使用者名稱，請在 login.html 中將：

```
<input type="text" name="username" value="$(username)">

```

改為以下行：

```
<input type="hidden" name="username" value="hsuser">

```

（其中 hsuser 是你提供的使用者名稱）

- 要提供預定義值作為密碼，請在 login.html 中更改。

```
<input type="password">

```

改為以下行：

```
<input type="hidden" name="password" value="hspass">

```

（其中 hspass 是你提供的密碼）

- 要以以下形式將用戶端的 MAC 地址傳送到註冊伺服器：

[https://www.example.com/register.html?mac=XX:XX:XX:XX:XX:XX](https://www.example.com/register.html?mac=XX:XX:XX:XX:XX:XX)

請將 login.html 中的 Login 按鈕連結改為：

```
https://www.example.com/register.html?mac=$(mac)

```

（你應該修正連結以指向你的伺服器）

- 要在使用者登入後顯示橫幅，請在 alogin.html 中在以下內容之後。

在 $(if popup == 'true') 之後新增以下行：

```
open('http://www.example.com/your-banner-page.html', 'my-banner-name','');

```

（你應該修正連結以指向要顯示的頁面）

- 要選擇登入後顯示的不同頁面，請在 login.html 中更改：

```
<input type="hidden" name="dst" value="$(link-orig)">

```

改為以下行：

```
<input type="hidden" name="dst" value="http://www.example.com">

```

（你應該修正連結以指向你的伺服器）

- 要在登出時刪除 cookie，請在包含登出連結的頁面（例如 status.html）中更改。

```
open('$(link-logout)', 'hotspot_logout', ...

```

改為：

```
open('$(link-logout)?erase-cookie=on', 'hotspot_logout', ...

```

或者，新增以下行：

```
<input type="hidden" name="erase-cookie" value="on">

```

在以下行之前：

```
<input type="submit" value="log off">

```

##### 外部認證 {#external-authentication}

另一個示例是讓 HotSpot 在遠端伺服器上進行認證（例如，該伺服器可能執行信用卡扣費）：

- 在 Walled Garden 中允許直接訪問外部伺服器（基於 HTTP 或基於 IP）。
- 修改 HotSpot Servlet 的登入頁面，以重定向到外部認證伺服器。外部伺服器應按需修改 RADIUS 資料庫。

以下是要放在 HotSpot 路由器上的此類登入頁面示例（它重定向到 [https://auth.example.com/login.php](https://auth.example.com/login.php)，請替換為外部認證伺服器的實際地址）：

```
<html>
<title>...</title>
<body>
<form name="redirect" action="https://auth.example.com/login.php" method="post">
<input type="hidden" name="mac" value="$(mac)">
<input type="hidden" name="ip" value="$(ip)">
<input type="hidden" name="username" value="$(username)">
<input type="hidden" name="link-login" value="$(link-login)">
<input type="hidden" name="link-orig" value="$(link-orig)">
<input type="hidden" name="error" value="$(error)">
</form>
<script language="JavaScript">
<!--
	document.redirect.submit();
//-->
</script>
</body>
</html>
          

```

- 外部伺服器可以透過將 HotSpot 用戶端重定向回原始 HotSpot Servlet 登入頁面並指定正確的使用者名稱和密碼，來使該用戶端登入。

以下是此類頁面的示例（它重定向到 [https://hotspot.example.com/login](https://hotspot.example.com/login)，請將其替換為 HotSpot 路由器的實際地址；另外，它在登入成功後會顯示 [www.mikrotik.com](http://www.mikrotik.com)，請將其替換為所需內容）：

```
<html>
<title>Hotspot login page</title>
<body>
<form name="login" action="https://hotspot.example.com/login" method="post">
<input type="text" name="username" value="demo">
<input type="password" name="password" value="none">
<input type="hidden" name="domain" value="">
<input type="hidden" name="dst" value="http://www.mikrotik.com/">
<input type="submit" name="login" value="log in">
</form>
</body>
</html>
          

```

- Hotspot 將詢問 RADIUS 伺服器是否允許登入。如果允許，則顯示 alogin.html 頁面（可將其修改為執行任何操作）。如果不允許，則顯示 flogin.html（或 login.html）頁面，該頁面會將用戶端重定向回外部認證伺服器。

**注意：** 如這些示例所示，可以使用 HTTPS 協定和 POST 方法來保護通訊。

##### HTTP 標頭檢測 {#http-header-detection}

Hotspot 登入頁面可以透過使用 **$(http-header-name);** 訪問 HTTP 標頭；

例如，有一種能力可以檢查使用者代理（或瀏覽器），如果需要，它將返回任何其他內容而不是常規登入頁面。例如，這可用於停用手機中的自動彈窗。

例如，要為特定 Firefox 移動版本的使用者輸出 "SUCCESS" 而不是登入頁面，你可以在 hotspot 目錄中 **rlogin.html** 頁面的頂部新增以下行：

```
$(if user-agent == "Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0" ) 
<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML> 
$(else)
---- regular content of rlogin.html page  ----
$(endif)

```

這將為 Android Firefox 40 使用者停用登入彈窗。

##### 一鍵登入 {#one-click-login}

可以建立修改後的強制門戶，以便在不需要使用者名稱或密碼的場景中實現快速一鍵登入。

你需要做的是：

- 為此目的建立一個使用者。例如，使用者名稱為 "notsosecretuser"，密碼為 "notsosecretpass"。
- 將此使用者分配給允許特定數量/無限數量併發活動使用者的使用者配置檔案。
- 複製路由器檔案選單根級別已生成的原始 hotspot 目錄。
- 修改此副本目錄的內容。
  - 為此，只需要修改一個檔案，即 "login.html"。

原始內容：

```

  login
      <input style={{width: '80px'}} name="username" type="text" value="$(username)"/>
  
  password
      <input style={{width: '80px'}} name="password" type="password"/>
  
   
      <input type="submit" value="OK" />
  

```

修改後：

```

  login
    <input style={{width: '80px'}} name="username" type="text" value="notsosecretuser"/>
  
  password
    <input style={{width: '80px'}} name="password" type="password" value="notsosecretpass"/>
  
   
    <input type="submit" value="Proceed to Internet!" />
  

```

更改內容：

- - - 使用者和密碼 "" 欄位被隱藏。
    - 使用者和密碼欄位值都包含預定義值。
    - 將 "OK" 按鈕的 value(name) 更改為更合適的內容。

- 現在將此新的 hotspot 資料夾上傳回路由器，最好使用不同的名稱。
- 更改 hotspot 伺服器配置檔案中的設定，以使用此新的 html 目錄。

```
/ip/hotspot/profile/set (profile number or name) html-directory-override=(dir path/name)

```

### 防火牆自定義 {#firewall-customizations}

#### 概述 {#summary}

除了 `/ip/hotspot` 子選單本身中明顯的動態條目（如 hosts 和 active users）之外，啟用 HotSpot 服務時還會在防火牆表中新增一些附加規則。

#### NAT {#nat}

透過 **`/ip/firewall/nat/print` dynamic** 命令，你可以得到類似以下內容（每條規則後附有註釋）：

```
 0 D chain=dstnat action=jump jump-target=hotspot hotspot=from-client

```

將所有來自 HotSpot 用戶端的封包的 HotSpot 相關任務放入一個單獨的鏈中。

```
 1 I chain=hotspot action=jump jump-target=pre-hotspot

```

任何應在 HotSpot 規則應用之前執行的操作都應放入 pre-hotspot 鏈。此鏈完全由管理員控制，不包含系統設定的任何規則，因此該跳轉規則無效（因為預設情況下該鏈沒有任何規則）。

```
 2 D chain=hotspot action=redirect to-ports=64872 dst-port=53 protocol=udp 
 3 D chain=hotspot action=redirect to-ports=64872 dst-port=53 protocol=tcp 

```

將所有 DNS 請求重定向到 HotSpot 服務。64872 埠為所有 HotSpot 使用者提供 DNS 服務。如果你希望 HotSpot 伺服器監聽另一個埠，請以相同方式在此處新增規則，並更改 dst-port 屬性。

```
 4 D chain=hotspot action=redirect to-ports=64873 hotspot=local-dst dst-port=80
     protocol=tcp

```

將所有 HTTP 登入請求重定向到 HTTP 登入 Servlet。64873 是 HotSpot HTTP Servlet 埠。

```
 5 D chain=hotspot action=redirect to-ports=64875 hotspot=local-dst dst-port=443
     protocol=tcp

```

將所有 HTTPS 登入請求重定向到 HTTPS 登入 Servlet。64875 是 HotSpot HTTPS Servlet 埠。

```
 6 D chain=hotspot action=jump jump-target=hs-unauth hotspot=!auth protocol=tcp

```

除來自未授權用戶端的 DNS 和登入請求外，所有其他封包都應經過 hs-unauth 鏈。

```
 7 D chain=hotspot action=jump jump-target=hs-auth hotspot=auth protocol=tcp

```

而來自已授權用戶端的封包則經過 hs-auth 鏈。

```
 8 D ;;; www.mikrotik.com
     chain=hs-unauth action=return dst-address=66.228.113.26 dst-port=80 protocol=tcp

```

在 **hs-unauth** 鏈中，首先放入 `/ip/hotspot/walled-garden/ip` 子選單中所有影響 TCP 協定的內容（即所有未設定協定或設定為 TCP 的內容）。這裡我們將 [www.mikrotik.com](http://www.mikrotik.com) 排除在重定向到登入頁面之外。

```
 9 D chain=hs-unauth action=redirect to-ports=64874 dst-port=80 protocol=tcp

```

所有其他 HTTP 請求都會重定向到監聽 64874 埠的 Walled Garden 代理伺服器。如果 `/ip/hotspot/walled-garden` 選單中存在針對某個 HTTP 請求的 "allow" 條目，則會將其轉發到目標。否則，該請求將自動重定向到 HotSpot 登入 Servlet（埠 64873）。

```
10 D chain=hs-unauth action=redirect to-ports=64874 dst-port=3128 protocol=tcp 
11 D chain=hs-unauth action=redirect to-ports=64874 dst-port=8080 protocol=tcp 

```

預設情況下，HotSpot 假定只有這些埠可用於 HTTP 代理請求。這兩個條目用於“捕獲”用戶端發往未知代理的請求（你可以在此處為其他埠新增更多規則），即讓具有未知代理設定的用戶端也能使用 HotSpot 系統。此功能稱為 "Universal Proxy"。如果檢測到用戶端正在使用某個代理伺服器，系統將自動用 HTTP hotspot 標記這些封包，以規避未知代理問題，我們稍後會看到。請注意，使用的埠（64874）與規則 #9 中用於 HTTP 請求的埠相同（因此 HTTP 請求和 HTTP 代理請求都由同一程式碼處理）。

```
12 D chain=hs-unauth action=redirect to-ports=64875 dst-port=443 protocol=tcp

```

HTTPS 代理監聽 64875 埠。

```
13 I chain=hs-unauth action=jump jump-target=hs-smtp dst-port=25 protocol=tcp

```

SMTP 協定的重定向也可以在 HotSpot 配置中定義。如果定義了，則會將重定向規則放入 hs-smtp 鏈。這樣做的目的是讓具有未知 SMTP 配置的使用者能夠透過服務提供商（你）的 SMTP 伺服器傳送郵件，而不是發往使用者在自己計算機上配置的 [在其原始網路之外可能不可用] SMTP 伺服器。預設情況下該鏈為空，因此該跳轉規則無效。

```
14 D chain=hs-auth action=redirect to-ports=64874 hotspot=http protocol=tcp

```

為已授權使用者提供 HTTP 代理服務。已認證使用者的請求可能需要進行透明代理（"Universal Proxy" 技術和廣告功能）。此 HTTP 標記會自動新增到 HotSpot HTTP 代理（監聽 64874 埠的那個）檢測到的、發往伺服器的 HTTP 代理請求上，將其視為發往未知代理伺服器的 HTTP 代理請求。這樣做的目的是讓具有某些代理設定的使用者使用 HotSpot 閘道器，而不是使用使用者在自己計算機上配置的 [在其原始網路之外可能不可用] 代理伺服器。當廣告需要顯示給使用者時，也會應用此標記，此外還會應用於那些配置檔案配置為透明代理其請求的使用者的任何 HTTP 請求。

```
15 I chain=hs-auth action=jump jump-target=hs-smtp dst-port=25 protocol=tcp

```

為已授權使用者提供 SMTP 代理（與規則 #13 相同）。

#### 封包過濾 {#packet-filtering}

透過 **`/ip/firewall/filter/print` dynamic** 命令，你可以得到類似以下內容（每條規則後附有註釋）：

```
 0 D chain=forward action=jump jump-target=hs-unauth hotspot=from-client,!auth

```

任何從未授權用戶端經過路由器的封包都將傳送到 **hs-unauth** 鏈。hs-unauth 實現基於 IP 的 Walled Garden 過濾。

```
 1 D chain=forward action=jump jump-target=hs-unauth-to hotspot=to-client,!auth

```

所有透過路由器到達用戶端的內容都會重定向到另一個名為 **hs-unauth-to** 的鏈。此鏈應拒絕發往用戶端的未授權請求。

```
 2 D chain=input action=jump jump-target=hs-input hotspot=from-client

```

所有從用戶端發往路由器本身的內容都會進入另一個名為 **hs-input** 的鏈。

```
 3 I chain=hs-input action=jump jump-target=pre-hs-input

```

在處理 [預定義] 動態規則之前，封包會進入由管理員控制的 **pre-hs-input** 鏈，該鏈預設情況下為空，因此該跳轉規則處於無效狀態。

```
 4 D chain=hs-input action=accept dst-port=64872 protocol=udp 
 5 D chain=hs-input action=accept dst-port=64872-64875 protocol=tcp 

```

允許用戶端訪問本地認證和代理服務（如前所述）。

```
 6 D chain=hs-input action=jump jump-target=hs-unauth hotspot=!auth

```

來自未授權用戶端發往路由器本身的所有其他流量都將按照與經過路由器的流量相同的方式處理。

```
 7 D chain=hs-unauth action=return protocol=icmp
 8 D ;;; www.mikrotik.com
     chain=hs-unauth action=return dst-address=66.228.113.26 dst-port=80 protocol=tcp

```

與 NAT 表中只添加了與 TCP 協定相關的 Walled Garden 條目不同，在封包過濾中，**hs-unauth** 鏈會新增你在 `/ip/hotspot/walled-garden/ip` 選單中設定的所有內容。這就是為什麼儘管你在 NAT 表中只看到一個條目，但這裡有兩條規則。

```
 9 D chain=hs-unauth action=reject reject-with=tcp-reset protocol=tcp
10 D chain=hs-unauth action=reject reject-with=icmp-net-prohibited

```

所有未被 Walled Garden 加入白名單的內容都將被拒絕。請注意，拒絕 TCP 連線時使用了 TCP Reset。

```
11 D chain=hs-unauth-to action=return protocol=icmp
12 D ;;; www.mikrotik.com
     chain=hs-unauth-to action=return src-address=66.228.113.26 src-port=80 protocol=tcp

```

對於發往用戶端的封包（鏈 **hs-unauth-to**），也會執行與規則 #7 和 #8 相同的操作。

```
13 D chain=hs-unauth-to action=reject reject-with=icmp-host-prohibited

```

使用 ICMP 拒絕訊息拒絕所有發往用戶端的封包。
