---
sidebar_key: "internet-of-things/bluetooth/user-guides/ifttt-app-notifications-ble-tag"
sidebar_position: 4
title: "當 BLE 標籤出現在 KNOT 範圍內時透過 IFTTT 應用傳送通知"
sidebar_label: "當 BLE 標籤出現在 KNOT 範圍內時透過 IFTTT 應用傳送通知"
source: https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/ifttt-app-notifications-ble-tag
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 簡介 {#introduction}

我們的 Bluetooth 標籤和 KNOT 可用於 IoT 資產跟蹤的不同場景。

本指南將展示的場景是：一旦標籤進入 KNOT 的 Bluetooth 範圍，以及一旦標籤離開 Bluetooth 工作範圍，你的手機就會收到通知。

該場景可以藉助 [IFTTT](https://ifttt.com/explore) 服務實現。IFTTT 會為你生成一個 URL。然後，你可以從 RouterOS 使用 [獲取](../../../system-information-and-utilities/fetch.md)，向 IFTTT 生成的 URL 傳送 HTTP/Web 請求，這將觸發向你的手機發送 APP 通知。

一旦 IFTTT 服務設定完成且 KNOT 已相應配置，你就可以將 Bluetooth 標籤（[TG-BT5-IN](https://mikrotik.com/product/tg_bt5_in) 或 [OUT](https://mikrotik.com/product/tg_bt5_out) 型號）安裝到你想要跟蹤的任何裝置上。

假設你將標籤安裝在一臺昂貴的機器上，或者只是……你的鑰匙上。然後，你安裝並放置 KNOT，使標籤處於 KNOT 的 Bluetooth 範圍內。接下來會發生什麼，它又將如何工作？

KNOT 將按計劃（使用你選擇的間隔）執行指令碼。根據指令碼中配置的標籤 MAC 地址 → 指令碼將檢查最近收到的 Bluetooth 封包的時間（即最近一次收到封包的時間）。如果：

- 封包的接收時間與 **/system clock** 時間相差在 1 分鐘以內（例如，**/system clock** 時間為 **16:02:00**，而標籤的 payload 在 **16:01:50** 收到）→ 將觸發一條“標籤在範圍內”通知，併發送到你的手機。
- 封包的接收時間比 **/system clock** 時間早 1 分鐘以上（例如，**/system clock** 時間為 **16:02:00**，而標籤的 payload 在 **16:00:50** 收到）→ 將觸發一條“標籤不在範圍內”通知併發送到你的手機。

由於沒有其他方法可以知道標籤實際上是在工作範圍內還是範圍外，指令碼使用 "time" 引數來確認。因此，當 payload 的接收時間不斷重新整理 → 這意味著標籤存在，並且 KNOT 成功接收封包。當 KNOT 自上次收到封包起已過去 1 分鐘 → 這意味著 KNOT 整整一分鐘都沒有收到標籤的任何更新，這確認標籤不在範圍內。

### IFTTT 設定 {#ifttt-setup}

第一步是註冊 IFTTT 賬戶，或透過[連結](https://ifttt.com/join)登入現有賬戶。

為你的手機下載 IFTTT 應用，你可以透過 APP 或瀏覽器配置後續步驟。

登入後，點選右上角的 "Create" 按鈕：

![](/img/8718c2b859fc9059.webp)

這將帶你進入 Applet 建立介面：

![](/img/e7da398226841fc0.webp)

在 "**If This**" 欄位中選擇 "**Add**" 按鈕。選擇名為 "**Webhooks**" 的服務。然後，選擇名為 "**Receive a web request**" 的選項。

輸入 "**Event Name**"，例如 `**{The_tag_IS_within_range}**`，然後選擇 "**Create trigger**"。這將帶你返回：

![](/img/8a2ccef59e60aa1f.webp)

在 "**Then That**" 欄位中選擇 "**Add**" 按鈕，並找到名為 "**Notifications**" 的操作。選擇名為 "**Send a notification from the IFTTT app**" 的選項，然後點選 "**Create Action**" 確認。

點選 "**Continue**" 並檢查 Applet。點選 "**Finish**"。

現在，再次執行相同步驟以建立第二個 Applet，但對於第二個 Applet，輸入另一個 "**Event Name**"，例如 `**{The_tag_is_NOT_in_range}**`。

建立兩個 Applet 後 → 檢查為你生成的 Web 請求 URL。前往[連結](https://ifttt.com/maker_webhooks)並點選 "**Documentation**" 按鈕：

![](/img/e2277dbb2090d7d3.webp)

頁面將顯示你需要使用的 URL：

![](/img/b3c3c04ebaffc7cb.webp)

複製此 URL——稍後你需要在指令碼中使用它。

### Bluetooth 標籤配置 {#bluetooth-tag-configuration}

透過[連結](../mikrotik-beacon-manager/index.md)檢視我們的標籤配置指南（iOS 和 Android）。

在此特定用例中，KNOT 將檢查收到的 Bluetooth payload 的時間，因此標籤配置為哪種封包型別並不重要。

唯一重要的設定是 "Advertisement interval"。確保已配置此引數。

或者你可以**直接讓標籤保持預設設定**，不做任何更改。

### RouterOS 配置 {#routeros-configuration}

:::info
請注意，需要 **iot** 軟體包。你可以從我們的[下載頁面](https://mikrotik.com/download)獲取。
:::
確保已配置網際網路訪問，以便 KNOT 能夠訪問 IFTTT webhooks。

#### Bluetooth 掃描器 {#bluetooth-scanner}

導航到 **IoT>Bluetooth>Scanners**。如果掃描器已停用，請確保將其啟用，然後編輯掃描器設定：

![](/img/6ee0035443c5a8b8.webp)

選擇 **Filter duplicates**=**keep-newest**。

**keep-newest** 設定將確保僅在 "Advertising reports" 部分保留最新報告。掃描器捕獲的新封包（針對每個單獨的 MAC 地址）將覆蓋較舊的封包。

#### 指令碼 {#script}

導航到 **System>Scripts** 選單，並在其中新增新指令碼。

你可以複製下面的指令碼。將下面的指令碼複製到“記事本”中，然後再次將其複製到指令碼的“**Source:**”欄位中。

```ros
#### User params
:local addressRegex    "DC:2C:6E:91:D6:F3"
:local urlNotInRange   "https://maker.ifttt.com/trigger/{The_tag_is_NOT_in_range}/json/with/key/-xxxx"
:local urlInRange      "https://maker.ifttt.com/trigger/{The_tag_IS_within_range}/json/with/key/-xxxx"
:local missingInterval 60000

###Time

:local realtime [/system clock get time]
:local realdate [/system clock get date]
:local tonumtime [:tonum [:totime "$realdate $realtime"]];
:local gmt ([system/clock/print as-value]->"gmt-offset")

###to offset epoch with curretn GMT
:global tonumtimeoffset ($tonumtime-$gmt)

:global Epomili
:set Epomili ([$tonumtimeoffset]."000")

###Bluetooth
:local adver
:local adver2
:local ts
:local clockmin

:set adver [/iot bluetooth scanners advertisements print detail as-value where address ~ $addressRegex]
:set adver2 ($adver->0)
:set ts ($adver2 -> "epoch")
:set clockmin ($Epomili-$missingInterval)

:local counterIN
:local counterOUT

:if ($ts&lt;=$clockmin) do={
    :set $counterIN 0;
    :if ($counterOUT=0 or $counterOUT=null) do={
        :set $counterOUT 0;
        /tool fetch http-method=get output=user url=$urlNotInRange;
        :set counterOUT ($counterOUT+1);
        :log info "IFTTT notification - the tag is OUT OF range!"
    } else={
        :log info "Tag is OUT of range! Notification was already sent before!"
    }
} else={
    :set $counterOUT 0;
    :if ($counterIN=0 or $counterIN=null) do={
        :set $counterIN 0;
        /tool fetch http-method=get output=user url=$urlInRange;
        :set $counterIN ($counterIN+1);
        :log info "IFTTT notification - tag IS WITHIN range!"
    } else={
        :log info "Tag is WITHIN the range! Notification was already sent before!"
    }
}
```

有 3 行需要留意（位於指令碼的 **### User parameters** 部分）。

1) MAC 地址行：

```
:local addressRegex "DC:2C:6E:91:D6:F3"
```

上面這一行，你需要輸入標籤的 MAC 地址（標籤的 MAC 地址印在標籤貼紙上）。

1) 不在範圍內通知 URL 行：

```
:local urlNotInRange "https://maker.ifttt.com/trigger/{The_tag_is_NOT_in_range}/json/with/key/-xxxx"
```

這一行，你需要輸入 IFTTT 服務為你生成的 URL。該 URL 應如下所示 → `https://maker.ifttt.com/trigger/{event}/json/with/key/-xxxxx`。將 URL 中的 `{event}` 部分更改為建立 Applet 時在 IFTTT 門戶中選擇的 `Event Name`，並將 URL 中的 -**xxxxx** 部分更改為 IFTTT 門戶為你生成的金鑰。

1) 在範圍內通知 URL 行：

```
:local urlInRange "https://maker.ifttt.com/trigger/{The_tag_IS_within_range}/json/with/key/-xxxx"
```

這一行，你需要輸入 IFTTT 服務為你生成的 URL。該 URL 應如下所示 → `https://maker.ifttt.com/trigger/{event}/json/with/key/-xxxxx`。將 URL 中的 `{event}` 部分更改為建立第二個 Applet 時在 IFTTT 門戶中選擇的第二個 `Event Name`，並將 URL 中的 -**xxxxx** 部分更改為 IFTTT 門戶為你生成的金鑰。

為指令碼命名，例如 **ifttt**，然後儲存（"Apply" 和 "OK"）。

**指令碼將如何工作？**

我們將一個計劃任務應用到指令碼，指令碼將按設定的間隔執行。計劃任務設定將在本指南後面展示。

指令碼的 **###Time** 部分會獲取 **/system clock** 時間並計算 "**epoch**" 時間。當我們獲得當前 **/system clock** 時間的 "**epoch**" 值後，就可以從中減去 1 分鐘。得到“減去一分鐘”後的 epoch 時間值，將幫助指令碼將封包的接收時間與之比較，以判斷封包是延遲 1 分鐘以上，還是處於當前時間的 1 分鐘區間內。

如果標籤移出範圍（封包早於 1 分鐘）→ KNOT 將向 IFTTT webhook 傳送 HTTP post（使用表示其超出範圍的 "**Event Name**"），並將該事件記錄到 **System>Log**。

如果收到標籤的 payload 且其不早於 1 分鐘 → KNOT 將向 IFTTT webhook 傳送 HTTP post（使用表示其處於範圍內的 "**Event Name**"），並將其記錄到 **System>Log**。

“counter”引數將確保指令碼每次由計劃任務執行時不會向你傳送大量通知，並確保當標籤進入範圍時你只收到 1 次通知，當標籤離開範圍時也只收到 1 次通知。

#### 排程器 {#scheduler}

導航到 **System>Scheduler**，並在其中新增新的計劃任務。

為其命名，例如 **scheduler1**，並設定你希望 KNOT 檢查封包的間隔。

![](/img/d6caa5f3fcc3d481.webp)

在 "**On Event:**" 欄位中新增一行 "/system script run **ifttt**"（其中 **ifttt** 是所建立指令碼的名稱），然後點選 "**Apply**" 和 "**OK**"。

### 結果驗證 {#result-verification}

確保你已在手機上登入 IFTTT 應用。

將標籤放置在 KNOT 的 Bluetooth 範圍內，一旦計劃任務執行指令碼，你應該會收到通知，如下所示：

![](/img/8d9d97307880d8f5.webp)

將標籤移出 KNOT 的範圍（等待 1 分鐘），你將收到另一條通知：

![](/img/2e5a381d4487a412.webp)
