---
title: "Hotspot 自訂"
description: "透過覆寫路由器 FTP 伺服器上儲存的預設 HTML 檔案，並在 HotSpot 設定檔中透過 `html-directory-override` 指定自訂目錄，即可自訂 HotSpot 驗證頁面。可從 login.html、status.html 與 logout.html 等預先定義的頁面中選擇，或建立含有 $(username) 與 $(password) 等變數的自訂頁面。"
tags:
  - 'hotspot'
  - 'servlet-pages'
  - 'radius'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/hotspot-captive-portal/hotspot-customisation
captured_at: '2026-11-28T10:19:39.818Z'
pagination_prev: "authentication-authorization-accounting/hotspot-captive-portal"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

#### 簡介 {#introduction}

你可以為每個 HotSpot 伺服器建立完全不同的一組 servlet 頁面，並在 HotSpot 伺服器設定檔 `/ip/hotspot/profile` 的 "html-directory-override" 屬性中指定目錄。預設 servlet 頁面會在建立伺服器設定檔後立即複製到 "hotspot" 目錄。你可以透過使用 FTP 用戶端連線到路由器來存取此目錄。你可以複製此目錄，並使用本手冊此章節的資訊修改頁面。請注意，建議手動編輯檔案，因為自動化 HTML 編輯工具可能會移除變數或其他重要部分，導致頁面損毀。完成內容修改後，你需要將修改後的內容上傳到 HotSpot 路由器上的某個自訂目錄，並將前述屬性 "html-directory-override" 的值指向這個新的自訂 HTML 目錄路徑。

**注意：** 如果 "html-directory-override" 的值路徑不存在或為空，HotSpot 伺服器將會回復使用預設 HTML 檔案。

#### 可用頁面 {#available-pages}

顯示給使用者的主要 HTML servlet 頁面：

- **redirect.html** - 將使用者重新導向到另一個 URL（例如登入頁面）。
- **login.html** - 顯示給使用者的登入頁面，用來要求使用者名稱與密碼。此頁面可接受以下參數：
  - **username** - 使用者名稱。
  - **password** - 純文字密碼（使用 PAP 驗證時），或 chap-id 變數、密碼與 CHAP challenge 的 MD5 雜湊值（使用 CHAP 驗證時）。此值會作為試用使用者的電子郵件地址。
  - **dst** - 重新導向前要求的原始 URL。登入成功後將會開啟此 URL。
  - **popup** - 登入成功時是否彈出狀態視窗。
  - **radius\<id>** - 以文字字串形式將 \<id> 識別的屬性傳送至 RADIUS 伺服器（使用 RADIUS 驗證時；否則會遺失）。
  - **radius\<id>u** - 以無正負號整數形式將 \<id> 識別的屬性傳送至 RADIUS 伺服器（使用 RADIUS 驗證時；否則會遺失）。
  - **radius\<id>-\<vnd-id>** - 以文字字串形式將 \<id> 識別的屬性與供應商 ID \<vnd-id> 傳送至 RADIUS 伺服器（使用 RADIUS 驗證時；否則會遺失）。
  - **radius\<id>-\<vnd-id>u** - 以無正負號整數形式將 \<id> 識別的屬性與供應商 ID \<vnd-id> 傳送至 RADIUS 伺服器（使用 RADIUS 驗證時；否則會遺失）。
- **md5.js** - 用於 MD5 密碼雜湊的 JavaScript。與 http-chap 登入方法搭配使用。
- **alogin.html** - 用戶端登入後顯示的頁面。它會彈出狀態頁面，並將瀏覽器重新導向到原本要求的頁面（在其被重新導向到 HotSpot 登入頁面之前）。
- **status.html** - 狀態頁面，顯示用戶端的統計資訊。它也能自動顯示廣告。
- **logout.html** - 登出頁面，在使用者登出後顯示。顯示已完成工作階段的最終統計資訊。此頁面可接受以下額外參數：
  - **erase-cookie** - 登出時是否從 HotSpot 伺服器清除 cookie（使下次從同一瀏覽器無法使用 cookie 登入，在多使用者環境中可能很有用）。
- **error.html** - 錯誤頁面，僅在發生嚴重錯誤時顯示。

如果需要更多控制，也可以使用一些其他頁面：

- **rlogin.html** - 當需要驗證用戶端才能存取某個 URL 時，將用戶端從其他 URL 重新導向到登入頁面的頁面
- **rstatus.html** - 類似於 rlogin.html，僅適用於用戶端已登入且原始 URL 未知的情況
- **radvert.html** - 將用戶端重新導向到已排程的廣告連結
- **flogin.html** - 當發生某些錯誤時（例如使用者名稱或密碼無效），用來取代 login.html 顯示
- **fstatus.html** - 當要求狀態頁面但用戶端未登入時，用來取代重新導向顯示
- **flogout.html** - 當要求登出頁面但用戶端未登入時，用來取代重新導向顯示

#### 提供 Servlet 頁面 {#serving-servlet-pages}

HotSpot servlet 會辨識 5 種不同的請求類型：

1. **對遠端主機的請求**
   - 如果使用者已登入，且預計顯示廣告，則會顯示 radvert.html。此頁面會重新導向至排定的廣告頁面。
   - 如果使用者已登入，且未為該使用者排定廣告，則會提供所要求的頁面。
   - 如果使用者未登入，但目的地主機已由 walled garden 允許，則也會提供該請求。
   - 如果使用者未登入，且目的地主機未由 walled garden 允許，則會顯示 rlogin.html；如果找不到 rlogin.html，則會使用 redirect.html 重新導向至登入頁面。
2. **對 HotSpot 主機上 "/" 的請求**
   - 如果使用者已登入，則會顯示 rstatus.html；如果找不到 rstatus.html，則會使用 redirect.html 重新導向至狀態頁面。
   - 如果使用者未登入，則會顯示 rlogin.html；如果找不到 rlogin.html，則會使用 redirect.html 重新導向至登入頁面。
3. **對 "/login" 頁面的請求**
   - 如果使用者已成功登入（或已經登入），則會顯示 alogin.html；如果找不到 alogin.html，則會使用 redirect.html 重新導向至原本要求的頁面或狀態頁面（如果未提供原始目的地頁面）。
   - 如果使用者未登入（未提供使用者名稱，且沒有出現錯誤訊息），則會顯示 login.html。
   - 如果登入程序失敗（提供錯誤訊息），則會顯示 flogin.html；如果找不到 flogin.html，則會使用 login.html。
   - 如果發生嚴重錯誤，則會顯示 error.html。
4. **對 "/status" 頁面的請求**
   - 如果使用者已登入，則會顯示 status.html。
   - 如果使用者未登入，則會顯示 fstatus.html；如果找不到 fstatus.html，則會使用 redirect.html 重新導向至登入頁面。
5. **對 '/logout' 頁面的請求**
   - 如果使用者已登入，則會顯示 logout.html。
   - 如果使用者未登入，則會顯示 flogout.html；如果找不到 flogout.html，則會使用 redirect.html 重新導向至登入頁面。

**注意：** 如果無法使用路由器 FTP 伺服器上儲存的頁面來滿足請求，則會顯示 Error 404。

有許多方式可以自訂 HotSpot 驗證頁面的外觀：

- 這些頁面很容易修改。它們儲存在路由器 FTP 伺服器中，目錄是您為對應的 HotSpot server profile 所選擇的目錄。
- 藉由變更用戶端傳送給 HotSpot servlet 的變數，可以將關鍵字數量減少為一個（使用者名稱或密碼；例如，可使用用戶端的 MAC 位址作為另一個值），甚至減少為零（License Agreement；可使用對所有使用者通用的部分預先定義值或用戶端的 MAC 位址作為使用者名稱與密碼）。
- 註冊可以在不同的伺服器上進行（例如，在能夠收取信用卡費用的伺服器上）。可以將用戶端的 MAC 位址傳遞給它，因此不必手動輸入此資訊。註冊完成後，伺服器應變更 RADIUS 資料庫，讓用戶端能夠登入一段時間。

若要在 HTML 檔案中的某個位置插入變數，會使用 $(var\_name) 語法，其中 "var\_name" 是變數名稱（不含引號）。此結構可用於任何以 '/', '/login', '/status' 或 '/logout' 存取的 HotSpot HTML 檔案，以及儲存在 HotSpot 伺服器上的任何文字或 HTML（.txt、.htm 或 .html）檔案（流量計數器除外，其僅在狀態頁面中可用；以及 **error**、**error-orig**、**chap-id**、**chap-challenge** 與 **popup** 變數，其僅在登入頁面中可用）。例如，若要顯示連往登入頁面的連結，可以使用下列結構：

```
login

```

#### Variables

所有 Servlet HTML 頁面都會使用變數來顯示使用者特定的值。變數名稱只會出現在 servlet 頁面的 HTML 原始碼中，它們會由 HotSpot Servlet 自動取代為對應的值。對於大多數變數，括號中會包含其可能值的範例。所有所述的變數在所有 servlet 頁面中都有效，但其中有些變數在存取時可能只是空白（例如，在使用者登入之前沒有上線時間）。

##### 可用變數清單 {#list-of-available-variables}

**注意：** 部分變數使用硬編碼的 http URL，如果你使用 https，可以用其他方式建立連結，例如針對 $link-status，可以使用 https://$(hostname)/$(target-dir)status

**常見伺服器變數：**

- **hostname** - HotSpot Servlet 的 DNS 名稱或 IP 位址（若未提供 DNS 名稱）（「[hotspot.example.net](http://hotspot.example.net)」）。
- **identity** - RouterOS 識別名稱（「MikroTik」）。
- **login-by** - 使用者使用的驗證方法。
- **plain-passwd** - 以「yes/no」表示是否允許 HTTP-PAP 登入方法（「no」）。
- **server-address** - HotSpot 伺服器位址（「10.5.50.1:80」）。
- **ssl-login** - 以「yes/no」表示是否使用 HTTPS 方法存取該 servlet 頁面（「no」）。
- **server-name** - HotSpot 伺服器名稱（在 `/ip/hotspot` 功能表中設定，作為 name 屬性）。

**Links:**

- **link-login** - 登入頁面連結，包含原始要求的 URL（「[http://10.5.50.1/login?dst=http://www.example.com/](http://10.5.50.1/login?dst=http://www.example.com/)」）
- **link-login-only** - 登入頁面連結，不包含原始要求的 URL（「[http://10.5.50.1/login](http://10.5.50.1/login)」）
- **link-logout** - 登出頁面連結（「[http://10.5.50.1/logout](http://10.5.50.1/logout)」）
- **link-status** - 狀態頁面連結（「[http://10.5.50.1/status](http://10.5.50.1/status)」）
- **link-orig** - 原始要求的 URL（「[http://www.example.com/](http://www.example.com/)」）

**一般用戶端資訊：**

- **domain** - 使用者的網域名稱（「[example.com](http://example.com)」）。
- **interface-name** - HotSpot 實體介面名稱（若為橋接介面，這會傳回實際的橋接埠名稱）。
- **ip** - 用戶端的 IP 位址（「10.5.50.2」）。
- **logged-in** - 若使用者已登入則為「yes」，否則為「no」（「yes」）。
- **mac** - 使用者的 MAC 位址（「01:23:45:67:89:AB」）。
- **trial** - 以「yes/no」表示使用者是否可存取試用時間。若使用者的試用時間已過期，值為「no」。
- **username** - 使用者名稱（「John」）。
- **host-ip** - 來自 `/ip/hotspot/host` 表的用戶端 IP 位址。
- **vlan-id** - 表示用戶端所連接 VLAN 介面的 ID。

**使用者狀態資訊：**

- **idle-timeout** - 閒置逾時（"20m"，若無則為 ""）。
- **idle-timeout-secs** - 以秒為單位的閒置逾時（"88"，若無此逾時則為 "0"）。
- **limit-bytes-in** - 傳送的位元組限制（"1000000"，若無限制則為 "---"）。
- **limit-bytes-out** - 接收的位元組限制（"1000000"，若無限制則為 "---"）。
- **refresh-timeout** - 狀態頁面重新整理逾時（"1m30s"，若無則為 ""）。
- **refresh-timeout-secs** - 以秒為單位的狀態頁面重新整理逾時（"90s"，若無則為 "0"）。
- **session-timeout** - 使用者的工作階段剩餘時間（"5h"，若無則為 ""）。
- **session-timeout-secs** - 使用者的工作階段剩餘時間，以秒為單位（"3475"，若無此逾時則為 "0"）。
- **session-time-left** - 使用者的工作階段剩餘時間（"5h"，若無則為 ""）。
- **session-time-left-secs** - 使用者的工作階段剩餘時間，以秒為單位（"3475"，若無此逾時則為 "0"）。
- **uptime** - 目前工作階段的運行時間（"10h2m33s"）。
- **uptime-secs** - 以秒為單位的目前工作階段運行時間（"125"）。

**僅在狀態頁面上可用的流量計數器：**

- **bytes-in** - 從使用者接收的位元組數（"15423"）。
- **bytes-in-nice** - 從使用者接收的位元組數的易讀格式（"15423"）。
- **bytes-out** - 傳送給使用者的位元組數（"11352"）。
- **bytes-out-nice** - 傳送給使用者的位元組數的易讀格式（"11352"）。
- **packets-in** - 從使用者接收的封包數（"251"）。
- **packets-out** - 傳送給使用者的封包數（"211"）。
- **remain-bytes-in** - 達到 limit-bytes-in 前剩餘的位元組數（"337465"，若無限制則為 "---"）。
- **remain-bytes-out** - 達到 limit-bytes-out 前剩餘的位元組數（"124455"，若無限制則為 "---"）。

**其他變數：**

- **session-id** - 上次要求中 'session-id' 參數的值。
- **var** - 上次要求中 'var' 參數的值。
- **error** - 錯誤訊息，若發生失敗（"invalid username or password"）。
- **error-orig** - 原始錯誤訊息（不含從 errors.txt 擷取的翻譯），若發生失敗（"invalid username or password"）。
- **chap-id** - chap ID 的值（"\371"）。
- **chap-challenge** - chap challenge 的值（"\357\015\330\013\021\234\145\245\303\253\142\246\133\175\375\316"）。
- **popup** - 是否快顯核取方塊（"true" 或 "false"）。
- **advert-pending** - 是否有廣告等待顯示（"yes" 或 "no"）。
- **http-status** - 允許設定 http 狀態碼與訊息。
- **http-header** - 允許設定 http 標頭。

**RADIUS 相關變數：**

- **radius\<id>** - 以文字字串形式顯示由 \<id> 識別的屬性（若使用 RADIUS 驗證；否則為 ""）
- **radius\<id>u** - 以無正負號整數形式顯示由 \<id> 識別的屬性（若使用 RADIUS 驗證；否則為 "0"）
- **radius\<id>-\<vnd-id>** - 以文字字串形式顯示由 \<id> 與廠商 ID \<vnd-id> 識別的屬性（若使用 RADIUS 驗證；否則為 ""）
- **radius\<id>-\<vnd-id>u** - 以無正負號整數形式顯示由 \<id> 與廠商 ID \<vnd-id> 識別的屬性（若使用 RADIUS 驗證；否則為 "0"）

##### 使用變數 {#working-with-variables}

在這些頁面中可以使用 `$(if \<var\_name>)` 陳述式。若 `\<var\_name>` 的值不是空字串，就會包含下列內容。這等同於 `$(if \<var\_name> != "")`。也可以進行相等比較：`$(if \<var\_name> == \<value>)`。這些陳述式會一直生效，直到出現 `$(elif \<var\_name>)`、`$(else)` 或 `$(endif)` 為止。一般情況如下所示：

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

這些運算式中只會顯示其中一個。顯示哪一個取決於每個用戶端對這些變數的值。

##### 重新導向與自訂標頭 {#redirects-and-custom-headers}

```
	$(if http-status == 302)Hotspot login required$(endif)
	$(if http-header == "Location")$(link-redirect)$(endif)

```

**注意：** 雖然上述內容看起來像是使用條件運算式「if」，但實際上是將「http-status」設定為「302」，而不是進行測試。變數「http-header」也是如此。同樣地，即使使用了「if」，實際上是將變數設定為「Location」，後面接著由變數「link-redirect」設定的 URL。

例如，若 `$(link-redirect)` 求值為「[http://192.168.88.1/login](http://192.168.88.1/login)」，則傳回給用戶端的 HTTP 回應會變更為：

```
HTTP/1.0 302 Hotspot login required
<regular HTTP headers>
Location: http://192.168.88.1/login

```

**http-status 語法**：

```
	$(if http-status == XYZ)HTTP_STATUS_MESSAGE$(endif)

```

- *XYZ* - 您希望傳回的狀態碼。應為 3 位十進位數字，第一位不得為 0。
- *HTTP\_STATUS\_MESSAGE* - 您希望傳回給用戶端的任何文字，會接在上述 HTTP 回應中的狀態碼之後。

在任何 HTTP 回應中，它會位於第一行，格式如下：

```
HTTP/1.0 XYZ HTTP_STATUS_MESSAGE

```

**http-header 語法：**

```
$(if http-header == HTTP_HEADER_NAME)HTTP_HEADER_VALUE$(endif)

```

- *HTTP\_HEADER\_NAME* - 要在回應中傳送的 HTTP 標頭名稱
- *HTTP\_HEADER\_VALUE* - 要在回應中傳送、名稱為 HTTP\_HEADER\_NAME 的 HTTP 標頭值

HTTP 回應將如下所示：

```
HTTP_HEADER_NAME: HTTP_HEADER_VALUE

```

HTTP\_HEADER\_VALUE 與 HTTP\_STATUS\_MESSAGE 中的所有變數與條件運算式都會照常處理。

若新增多個同名標頭，只會使用最後一個（先前的標頭會被捨棄）。這讓系統可以覆寫一般的 HTTP 標頭（例如 Content-Type 與 Cache-Control）。

#### 自訂錯誤訊息 {#customizing-error-messages}

所有錯誤訊息都儲存在對應 HotSpot servlet 目錄中的 errors.txt 檔案內。你可以變更並將這些訊息翻譯成你的母語。若要這麼做，請編輯 errors.txt 檔案。你也可以在訊息中使用變數。所有指示都列在該檔案中。

#### 多個版本的 HotSpot 頁面 {#multiple-versions-of-hotspot-pages}

同一個 HotSpot 伺服器支援多組 HotSpot 頁面集。使用者可以自行選擇（以挑選語言），或由 JavaScript 自動選擇（以挑選 PDA／一般版本的 HTML 頁面）。

若要使用此功能，請在 HotSpot HTML 目錄中建立子目錄，並將不同的 HTML 檔案放入該子目錄。例如，若要將所有內容翻譯成 Latvian，可以建立子目錄「lv」，並在其中放入已翻譯成 Latvian 的 login.html、logout.html、status.html、alogin.html、radvert.html 與 errors.txt 檔案。如果在要求的子目錄中找不到要求的 HTML 頁面，則會使用主目錄中對應的 HTML 檔案。主 login.html 檔案會包含一個指向「/lv/login?dst=$(link-orig-esc)」的連結，接著會顯示 Latvian 版本的登入頁面：Latviski。而 Latvian 版本會包含一個指向英文版本的連結：English

另一種參考目錄的方式是指定 'target' 變數：

```
        Latviski
        English

```

選取偏好的目錄後（例如「lv」），所有指向本機 HotSpot 頁面的連結都會包含該路徑（例如 $(link-status) = "[http://hotspot.mt.lv/lv/status](http://hotspot.mt.lv/lv/status)"）。因此，如果所有 HotSpot 頁面都使用 "$(link-xxx)" 變數來參考連結，就不需要再進行其他變更，每個用戶端都會一直停留在所選取的目錄中。

#### Misc

如果要使用 HTTP-CHAP 驗證方法，必須在登入表單的 **Submit action** 之前加入 **doLogin()** 函式（該函式會參考 **md5.js**，而 md5.js 必須已載入）。否則，CHAP 登入會失敗。

在 HTTP-CHAP 方法中，要傳送至 HotSpot 閘道器的最終密碼，是透過對以下內容的串接進行 MD5 雜湊所形成：chap-id、使用者密碼與 chap-challenge（依給定順序）。

如果要在連結中直接使用變數，則必須據此進行跳脫。例如，在登入頁面中，若使用者名稱是「123&456=1 2」，**link** 將無法如預期般運作。在此情況下，必須使用 $(user) 的跳脫版本：$(user-esc): **link**。現在，相同的使用者名稱會被轉換為「123%26456%3D1+2」，這是「123&456=1 2」在 URL 中的有效表示方式。此技巧可搭配任何變數使用，不限於 $(username)。

登出頁面有一個布林參數「erase-cookie」，其值可以是「on」或「true」，用於在登出時刪除使用者 cookie（如此一來，使用者下次開啟瀏覽器時就不會自動登入）。

#### 範例 {#examples}

具備基本 HTML 語言知識與下列範例後，應可輕鬆實作上述概念：

- 若要提供預先定義的值作為使用者名稱，請在 login.html 中變更：

```
<input type="text" name="username" value="$(username)">

```

改為這一行：

```
<input type="hidden" name="username" value="hsuser">

```

（其中 hsuser 是您提供的使用者名稱）

- 若要提供預先定義的值作為密碼，請在 login.html 中變更：

```
<input type="password">

```

改為這一行：

```
<input type="hidden" name="password" value="hspass">

```

（其中 hspass 是您提供的密碼）

- 以下列格式將用戶端的 MAC 位址傳送至註冊伺服器：

[https://www.example.com/register.html?mac=XX:XX:XX:XX:XX:XX](https://www.example.com/register.html?mac=XX:XX:XX:XX:XX:XX)

將 `login.html` 中的 Login 按鈕連結變更為：

```
https://www.example.com/register.html?mac=$(mac)

```

（你應該修正連結，使其指向你的伺服器）

- 若要在使用者登入後顯示橫幅，請在 `alogin.html` 中的 後方加入。

若 `popup == 'true'`，請加入下列這行：

```
open('http://www.example.com/your-banner-page.html', 'my-banner-name','');

```

（您應該修正連結，使其指向要顯示的頁面）

- 若要選擇登入後顯示的不同頁面，請在 login.html 中變更：

```
<input type="hidden" name="dst" value="$(link-orig)">

```

這一行：

```
<input type="hidden" name="dst" value="http://www.example.com">

```

（你應該修正連結，使其指向你的伺服器）

- 若要在登出時清除 cookie，請在含有登出連結的頁面中變更（例如 status.html）。

```
open('$(link-logout)', 'hotspot_logout', ...

```

變更為：

```
open('$(link-logout)?erase-cookie=on', 'hotspot_logout', ...

```

或者也可以加入這一行：

```
<input type="hidden" name="erase-cookie" value="on">

```

在此行之前：

```
<input type="submit" value="log off">

```

##### 外部驗證 {#external-authentication}

另一個範例是讓 HotSpot 在遠端伺服器上進行驗證（例如，該伺服器可執行信用卡扣款）：

- 在 walled-garden 中允許直接存取外部伺服器（可使用 HTTP 或 IP 方式）。
- 修改 HotSpot servlet 的登入頁面，使其重新導向至外部驗證伺服器。外部伺服器應視需要修改 RADIUS 資料庫。

以下是這類登入頁面的範例，可放在 HotSpot 路由器上（它會重新導向至 [https://auth.example.com/login.php](https://auth.example.com/login.php)，請取代為外部驗證伺服器的實際位址）：

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

- 外部伺服器可以透過將 HotSpot 用戶端重新導向回原始的 HotSpot servlet 登入頁面，並指定正確的使用者名稱與密碼，來登入 HotSpot 用戶端。

以下是這類頁面的範例（它會重新導向至 [https://hotspot.example.com/login](https://hotspot.example.com/login)，請取代為 HotSpot 路由器的實際位址；此外，它會在登入成功後顯示 [www.mikrotik.com](http://www.mikrotik.com)，請取代為所需的內容）：

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

- Hotspot 會詢問 RADIUS 伺服器是否允許登入。若允許，將顯示 alogin.html 頁面（可修改為執行任何操作）。若不允許，將顯示 flogin.html（或 login.html）頁面，該頁面會將用戶端重新導向回外部驗證伺服器。

**注意：** 如這些範例所示，可使用 HTTPS 通訊協定與 POST 方法來保護通訊。

##### HTTP 標頭偵測 {#http-header-detection}

Hotspot 登入頁面可透過 **$(http-header-name);** 存取 HTTP 標頭。

例如，可以檢查使用者代理程式（或瀏覽器），並在需要時傳回其他內容，而非一般登入頁面。例如，這可用於停用手機中的自動快顯視窗。

例如，若要針對特定 Firefox 行動版本的使用者輸出「SUCCESS」，而非登入頁面，可以在 hotspot 目錄中 **rlogin.html** 頁面頂端加入以下幾行：

```
$(if user-agent == "Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0" ) 
<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML> 
$(else)
---- regular content of rlogin.html page  ----
$(endif)

```

這會停用 Android Firefox 40 使用者的登入快顯視窗。

##### 一鍵登入 {#one-click-login}

可以建立修改過的 captive portal，用於不需要使用者名稱或密碼的場景，以進行快速的一鍵登入。

你需要做的是：

- 為此目的建立一個使用者。例如，使用者為「notsosecretuser」，密碼為「notsosecretpass」。
- 將此使用者指派給允許特定／無限數量同時作用中使用者的使用者設定檔。
- 複製路由器檔案選單中根層級已產生的原始 hotspot 目錄。
- 修改此複製目錄中的內容。
  - 只需修改一個檔案即可運作，即「login.html」。

Original:

```

  login
      <input style={{width: '80px'}} name="username" type="text" value="$(username)"/>
  
  password
      <input style={{width: '80px'}} name="password" type="password"/>
  
   
      <input type="submit" value="OK" />
  

```

Modified:

```

  login
    <input style={{width: '80px'}} name="username" type="text" value="notsosecretuser"/>
  
  password
    <input style={{width: '80px'}} name="password" type="password" value="notsosecretpass"/>
  
   
    <input type="submit" value="Proceed to Internet!" />
  

```

變更內容：

- - - 隱藏 User 與 Password 欄位。
    - User 與 Password 欄位值都包含預先定義的值。
    - 將「OK」按鈕值（name）變更為更合適的內容。

- 現在將這個新的 hotspot 資料夾上傳回路由器，最好使用不同的名稱。
- 變更 hotspot server profile 中的設定，以使用這個新的 html 目錄。

```
/ip/hotspot/profile/set (profile number or name) html-directory-override=(dir path/name)

```

### 防火牆自訂 {#firewall-customizations}

#### 摘要 {#summary}

除了 `/ip/hotspot` 子選單本身中明顯的動態項目（例如 hosts 與 active users）之外，啟用 HotSpot 服務時，也會在防火牆表中新增一些額外規則。

#### NAT

從 **`/ip/firewall/nat/print` dynamic** 指令，你可以取得類似以下的內容（註解接在每條規則之後）：

```
 0 D chain=dstnat action=jump jump-target=hotspot hotspot=from-client

```

將來自所有 HotSpot 用戶端的封包之所有 HotSpot 相關工作，放入獨立的 chain。

```
 1 I chain=hotspot action=jump jump-target=pre-hotspot

```

任何應在 HotSpot 規則套用前執行的動作，都應放在 pre-hotspot chain 中。此 chain 完全由管理員控制，且不包含任何由系統設定的規則，因此會有無效的 jump 規則（因為此 chain 預設沒有任何規則）。

```
 2 D chain=hotspot action=redirect to-ports=64872 dst-port=53 protocol=udp 
 3 D chain=hotspot action=redirect to-ports=64872 dst-port=53 protocol=tcp 

```

將所有 DNS 要求重新導向至 HotSpot 服務。64872 埠為所有 HotSpot 使用者提供 DNS 服務。如果你希望 HotSpot 伺服器接聽其他埠，請以相同方式在此新增規則，並變更 dst-port 屬性。

```
 4 D chain=hotspot action=redirect to-ports=64873 hotspot=local-dst dst-port=80
     protocol=tcp

```

將所有 HTTP 登入要求重新導向至 HTTP 登入 servlet。64873 是 HotSpot HTTP servlet 埠。

```
 5 D chain=hotspot action=redirect to-ports=64875 hotspot=local-dst dst-port=443
     protocol=tcp

```

將所有 HTTPS 登入要求重新導向至 HTTPS 登入 servlet。64875 是 HotSpot HTTPS servlet 埠。

```
 6 D chain=hotspot action=jump jump-target=hs-unauth hotspot=!auth protocol=tcp

```

除了來自未授權用戶端的 DNS 與登入要求之外，其餘封包都應通過 hs-unauth 鏈。

```
 7 D chain=hotspot action=jump jump-target=hs-auth hotspot=auth protocol=tcp

```

而來自已授權用戶端的封包則通過 hs-auth 鏈。

```
 8 D ;;; www.mikrotik.com
     chain=hs-unauth action=return dst-address=66.228.113.26 dst-port=80 protocol=tcp

```

首先，在 **hs-unauth** 鏈中放入所有會影響 TCP 通訊協定、且位於 `/ip/hotspot/walled-garden/ip` 子選單中的項目（也就是所有未設定 protocol，或設定為 TCP 的項目）。在這裡，我們排除 [www.mikrotik.com](http://www.mikrotik.com)，使其不會被重新導向至登入頁面。

```
 9 D chain=hs-unauth action=redirect to-ports=64874 dst-port=80 protocol=tcp

```

所有其他 HTTP 要求都會被重新導向至 Walled Garden 伺服器，該伺服器監聽埠 64874。如果 HTTP 要求在 `/ip/hotspot/walled-garden` 選單中有「allow」項目，就會被轉送至目的地。否則，要求會自動重新導向至 HotSpot 登入 servlet（埠 64873）。

```
10 D chain=hs-unauth action=redirect to-ports=64874 dst-port=3128 protocol=tcp 
11 D chain=hs-unauth action=redirect to-ports=64874 dst-port=8080 protocol=tcp 

```

HotSpot 預設假設只有這些埠可用於 HTTP proxy 要求。這兩個項目用來「擷取」用戶端對未知 proxy 的要求（你可以為其他埠在此新增更多規則），也就是讓具有未知 proxy 設定的用戶端能夠與 HotSpot 系統搭配運作。這項功能稱為「Universal Proxy」。如果偵測到用戶端正在使用某個 proxy 伺服器，系統會自動以 HTTP hotspot 標記標註這些封包，以解決未知 proxy 的問題，我們稍後會看到。請注意，所使用的埠（64874）與規則 #9 中 HTTP 要求的埠相同（因此 HTTP 與 HTTP proxy 要求都由相同的程式碼處理）。

```
12 D chain=hs-unauth action=redirect to-ports=64875 dst-port=443 protocol=tcp

```

HTTPS proxy 監聽埠 64875。

```
13 I chain=hs-unauth action=jump jump-target=hs-smtp dst-port=25 protocol=tcp

```

SMTP 協定的重新導向也可以在 HotSpot 設定中定義。若有定義，系統會將重新導向規則放入 **hs-smtp** 鏈。這樣做是為了讓 SMTP 設定未知的使用者，能透過服務提供者（你）的 SMTP 伺服器寄送郵件，而不是連到使用者在電腦上設定的 SMTP 伺服器（在原始網路之外可能無法使用）。此鏈預設為空，因此會有無效的跳轉規則。

```
14 D chain=hs-auth action=redirect to-ports=64874 hotspot=http protocol=tcp

```

為已授權使用者提供 HTTP proxy 服務。已驗證使用者的請求可能需要進行透明代理（「Universal Proxy」技術與廣告功能）。HotSpot HTTP proxy（監聽埠 64874 的服務）偵測到對伺服器的 HTTP proxy 請求時，會自動將此 HTTP 標記套用在這些請求上，作為對未知 proxy 伺服器的 HTTP proxy 請求。這樣做是為了讓具有某些 proxy 設定的使用者改用 HotSpot 閘道，而不是使用者在電腦上設定的 proxy 伺服器（在原始網路之外可能無法使用）。當需要向使用者顯示廣告時，以及來自設定為透明代理其請求的設定檔之使用者的任何 HTTP 請求，也都會套用此標記。

```
15 I chain=hs-auth action=jump jump-target=hs-smtp dst-port=25 protocol=tcp

```

為已授權使用者提供 SMTP proxy（與規則 #13 相同）。

#### 封包過濾 {#packet-filtering}

從 **`/ip/firewall/filter/print` dynamic** 指令，你會得到類似以下的內容（註解接在每條規則之後）：

```
 0 D chain=forward action=jump jump-target=hs-unauth hotspot=from-client,!auth

```

任何從未授權用戶端通過路由器的封包，都會被傳送至 **hs-unauth** 鏈。hs-unauth 實作以 IP 為基礎的 Walled Garden 過濾器。

```
 1 D chain=forward action=jump jump-target=hs-unauth-to hotspot=to-client,!auth

```

所有透過路由器送達用戶端的內容，都會被重新導向至另一個名為 **hs-unauth-to** 的鏈。此鏈應拒絕對用戶端的未授權請求。

```
 2 D chain=input action=jump jump-target=hs-input hotspot=from-client

```

所有從用戶端送至路由器本身的內容，都會進入另一個名為 **hs-input** 的鏈。

```
 3 I chain=hs-input action=jump jump-target=pre-hs-input

```

在繼續處理 [predefined] 動態規則之前，封包會進入由管理員控制的 **pre-hs-input** 鏈，該鏈預設為空，因此 jump 規則處於無效狀態。

```
 4 D chain=hs-input action=accept dst-port=64872 protocol=udp 
 5 D chain=hs-input action=accept dst-port=64872-64875 protocol=tcp 

```

允許用戶端存取本機驗證與 Proxy 服務（如先前所述）。

```
 6 D chain=hs-input action=jump jump-target=hs-unauth hotspot=!auth

```

所有其他從未授權用戶端前往路由器本身的流量，都會以與流經路由器的流量相同的方式處理。

```
 7 D chain=hs-unauth action=return protocol=icmp
 8 D ;;; www.mikrotik.com
     chain=hs-unauth action=return dst-address=66.228.113.26 dst-port=80 protocol=tcp

```

與 NAT 表只新增 TCP 協定相關的 Walled Garden 項目不同，在封包過濾器中，**hs-unauth** 鏈會新增至你在 `/ip/hotspot/walled-garden/ip` 選單中設定的所有內容。這就是為什麼雖然你在 NAT 表中只看到一項，但這裡會有兩條規則。

```
 9 D chain=hs-unauth action=reject reject-with=tcp-reset protocol=tcp
10 D chain=hs-unauth action=reject reject-with=icmp-net-prohibited

```

所有其他未被 Walled Garden 列入白名單的內容都會被拒絕。請注意，此處使用 TCP Reset 拒絕 TCP 連線。

```
11 D chain=hs-unauth-to action=return protocol=icmp
12 D ;;; www.mikrotik.com
     chain=hs-unauth-to action=return src-address=66.228.113.26 src-port=80 protocol=tcp

```

對於目的地為用戶端的封包（鏈 **hs-unauth-to**），也會執行與規則 #7 和 #8 相同的動作。

```
13 D chain=hs-unauth-to action=reject reject-with=icmp-host-prohibited

```

以 ICMP reject 訊息拒絕所有前往用戶端的封包。
