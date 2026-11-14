---
sidebar_key: "internet-of-things/bluetooth/user-guides/email-notification-mikrotik-ble-tag-s"
sidebar_position: 2
title: "MikroTik BLE 標籤加速度計觸發時的電子郵件通知"
sidebar_label: "MikroTik BLE 標籤加速度計觸發時的電子郵件通知"
source: https://manual.mikrotik.com/docs/7.25/internet-of-things/bluetooth/user-guides/email-notification-mikrotik-ble-tag-s
captured_at: '2026-11-04T11:18:07+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 簡介 {#introduction}

在本指南中，我們將展示一個快速的分步流程，說明如何設定 KNOT，使其在檢測到由 [TG-BT5-IN](https://mikrotik.com/product/tg_bt5_in) 或 [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out) 標籤上報的“已觸發”條件時傳送電子郵件通知。

兩個標籤都內建加速度計，能夠檢測自由落體、喚醒/移動和傾斜狀態。當標籤設定為廣播 [MikroTik 格式](../mikrotik-beacon-manager/mikrotik-tag-advertisement-formats.md)載荷，並且啟用了加速度計觸發器（使用 MikroTik Beacon Manager 應用程式）→ 每當將要檢測到觸發器時，標籤就會立即廣播一個廣播載荷/報告。

對於 [iOS](../mikrotik-beacon-manager/mikrotik-beacon-manager-for-ios-devices.md)，觸發器設定如下所示（處於停用狀態/預設設定）：

![](/img/bc61dd8531591e00.webp)

對於 [Android](../mikrotik-beacon-manager/mikrotik-beacon-manager-android-devices.md)，觸發器設定如下所示（處於停用狀態/預設設定）：

![](/img/afeda0f2e01597f6.webp)

要啟用觸發器檢測，只需勾選相應的“複選框”。

標籤廣播 Bluetooth 載荷後 → 載荷的第 21 個八位組將指示檢測到的確切觸發器。你可以在 **IoT>Bluetooth>Advertisng reports** 標籤頁下檢視這些載荷：

![](/img/5e0d840a80057596.webp)

如上圖所示，第 21 個八位組是“04”，這表示該載荷是在標籤檢測到自由落體條件時傳送的（這些載荷是在我們“不小心”掉落或扔出標籤時廣播的）。

完成所有配置後，將發生以下情況：

- KNOT 將按計劃執行指令碼。
- 指令碼將“讀取/掃描”**IoT>Bluetooth>Advertising reports** 標籤頁中顯示的載荷。
- 如果儲存/捕獲的載荷的第 21 個八位組值等於任何“已觸發”值 → 將傳送電子郵件通知。

換句話說，當 KNOT 掃描這些載荷並找到一個第 21 個八位組指示觸發器已啟用的載荷時 → 你將收到一封檢測到觸發器的電子郵件通知。

### TG-BT5 標籤配置 {#tg-bt5-tag-configuration}

在這個具體示例中，我們需要將標籤設定為在 **MikroTik 格式**下工作。在 MikroTik 格式中，每個載荷的第 21 個八位組將指示其被觸發的原因。

你可以按照 [iOS](../mikrotik-beacon-manager/mikrotik-beacon-manager-for-ios-devices.md) 和/或 [Android](../mikrotik-beacon-manager/mikrotik-beacon-manager-android-devices.md) 指南（**"Advertisement"/Beacon settings** 部分）找到有關如何啟用觸發器的說明。

為了更輕鬆地“啟用”觸發器，我們還可以按照 iOS 和/或 Android 指南（**Free Fall Threshold and Duration** 部分）更改觸發器設定。為了測試目的，並且基本上只是讓檢測更快地被“觸發”，我們可以將“**Free Fall Duration**”引數改為“0”秒（這將確保所有軸上處於閾值範圍內的任何加速度都會被立即檢測為“自由落體”事件）。

### RouterOS 配置 {#routeros-configuration}

:::info
**iot** 軟體包是必需的。你可以從我們的下載頁面獲取它——在 "Extra packages" 下。
:::
配置可以透過 4 個步驟完成：

- 啟用掃描器（並且最好確認當檢測到觸發器時標籤正在廣播載荷）；
- 設定電子郵件伺服器；
- 匯入指令碼（並根據需求修改少量指令碼行）；
- 設定排程器。

#### Bluetooth 掃描器 {#bluetooth-scanner}

轉到 [IoT>Bluetooth>Scanners](../index.md) 標籤頁，並確保它已啟用：

![](/img/0f166b184bb52a00.webp)

轉到 **Advertising reports** 標籤頁，並使用 MAC 地址過濾選項過濾列表（你可以在標籤本身的標籤紙上找到 MikroTik 標籤的 MAC 地址）。

嘗試“觸發”已配置的檢測，並透過檢查第 21 個八位組的值來確認。

在我們的示例中，我們為標籤配置了“自由落體”檢測，並且**將其掉落**。我們收到了來自標籤的報告，指示“下落”狀態（第 21 個八位組 = **04**）：

![](/img/d60ecc0f246ac416.webp)

我們已經確認，標籤正在正確上報觸發器。

#### 電子郵件 {#email}

轉到 [電子郵件](../../../system-information-and-utilities/e-mail.md) 部分，並設定你選擇的電子郵件伺服器。

本指南中我們將使用所示的 **GMAIL** 示例。

![](/img/b0b11d0862735ec3.webp)

嘗試傳送一封測試電子郵件，以確保設定正確。

#### 指令碼 {#scripts}

##### 選項 (a) {#option-a}

轉到 [System>Scripts](../../../developer-guides/scripting/index.md) 選單，並在其中新增一個新指令碼。

你可以複製下面的指令碼。將下面的指令碼複製到“記事本”中，然後再次將其複製到指令碼的“**Source:**”欄位中。

```ros
## 在 "" 内输入标签的 MAC 地址
:local addressRegex "2C:C8:1B:E2:15:29"

#在 "" 内输入电子邮件主题
:local emailsubject "RouterOS report!"

#在 "" 内输入电子邮件地址
:local emailaddress "YOUR_EMAIL@gmail.com"

#Script:
################################## Bluetooth ##################################
:local flagStr do={
    :local str ""

    :if ($1 & 0x01) do={ :set $str " switch" }
    :if ($1 & 0x02) do={ :set $str "$str tilt" }
    :if ($1 & 0x04) do={ :set $str "$str free_fall" }
    :if ($1 & 0x08) do={ :set $str "$str impact_x" }
    :if ($1 & 0x10) do={ :set $str "$str impact_y" }
    :if ($1 & 0x20) do={ :set $str "$str impact_z" }

    :if ([:len $str] = 0) do={ :return "" }

    :return [:pick $str 1 [:len $str]]
}

:local triggernameF "free_fall"
:local triggernameT "tilt"
:local triggernameX "impact_x"
:local triggernameY "impact_y"
:local triggernameZ "impact_z"
:local triggernameS "switch"

## 查找新的蓝牙广播
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # First time this script has been run since booting, need to initialize
    # persistent variables
    :set $btOldestAdvertisementTimestamp 0
}
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex
]
:local advCount 0
:local lastAdvTimestamp 0
:local triggerlist ""

:local triggerF
:local triggerT
:local triggerX
:local triggerY
:local triggerZ
:local triggerS

:local messageF ""
:local messageT ""
:local messageX ""
:local messageY ""
:local messageZ ""
:local messageS ""

:local 21st ""

:foreach adv in=$advertisements do={
    :local address ($adv->"address")
    :local rssi ($adv->"rssi")
    :local epoch ($adv->"epoch")
    :local rtime ($adv->"time")
    :local ad ($adv->"data")
    :local flags [:tonum "0x$[:pick $ad 40 42]"]
    :local obj "$[$flagStr $flags]"

    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $epoch
    :set $triggerlist "$triggerlist$obj"

:set triggerF [:pick $triggerlist ([find $triggerlist "free_fall"]-0) ([find $triggerlist "free_fall"]+9)]
:if ($triggerF=$triggernameF) do={:set messageF "$triggernameF";:set 21st "not00";}
:set triggerT [:pick $triggerlist ([find $triggerlist "tilt"]-0) ([find $triggerlist "tilt"]+4)]
:if ($triggerT=$triggernameT) do={:set messageT "$triggernameT";:set 21st "not00";}
:set triggerX [:pick $triggerlist ([find $triggerlist "impact_x"]-0) ([find $triggerlist "impact_x"]+8)]
:if ($triggerX=$triggernameX) do={:set messageX "$triggernameX";:set 21st "not00";}
:set triggerY [:pick $triggerlist ([find $triggerlist "impact_y"]-0) ([find $triggerlist "impact_y"]+8)]
:if ($triggerY=$triggernameY) do={:set messageY "$triggernameY";:set 21st "not00";}
:set triggerZ [:pick $triggerlist ([find $triggerlist "impact_z"]-0) ([find $triggerlist "impact_z"]+8)]
:if ($triggerZ=$triggernameZ) do={:set messageZ "$triggernameZ";:set 21st "not00";}
:set triggerS [:pick $triggerlist ([find $triggerlist "switch"]-0) ([find $triggerlist "switch"]+6)]
:if ($triggerS=$triggernameS) do={:set messageS "$triggernameS";:set 21st "not00";}

}
:if ($advCount > 0) do={
    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp
}

#消息结构：
:local message "$messageF
$messageT
$messageX
$messageY
$messageZ
$messageS
--trigger(s) reported by the tag!"

:if ($21st="not00") do={/tool e-mail send to=$emailaddress subject="$emailsubject" body="$message"} else={:put "21st octet does not have triggers detected!"}
```

以下 3 行需要留意：

```
:local addressRegex "2C:C8:1B:E2:15:29"
```

這一行，我們在此輸入要監視的標籤的 MAC 地址；

```
:local emailsubject "RouterOS report!"
```

這一行，你可以在此修改電子郵件的主題；

```
:local emailaddress "YOUR_EMAIL@gmail.com"
```

電子郵件地址行，你需要在此輸入電子郵件地址。即你希望將報告發送到哪裡。

你還可以使用以下行更改電子郵件訊息的結構：

```ros
#消息结构：
:local message "$messageF
$messageT
$messageX
$messageY
$messageZ
$messageS
--trigger(s) reported by the tag!"
```

你可以隨意命名指令碼，例如 **triggernotification**。點選 **Apply** 和 **OK**。

:::info
此外，在本示例中，我們專門展示了一個電子郵件通知場景。**但是！** 如果您想使用其他方法傳送通知，只需修改下面這一行：

```
:if ($21st="not00") do={/tool e-mail send to=$emailaddress subject="$emailsubject" body="$message"}
```

你可以將該行中的 `do={/tool e-mail...` 部分改為，例如 `do={/tool fetch...` 或 `do={/iot mqtt publish...`。這樣，你就可以改為傳送 HTTP POST 或 MQTT 釋出訊息。

如果你希望在檢測到觸發器時收到手機通知，也可以使用 IFTTT 服務（向 IFTTT webhook 傳送 HTTP post），正如我們在[此處](./ifttt-app-notifications-ble-tag.md)的另一篇指南中所述。
:::
你可以透過命令“**/system script run triggernotification**”手動執行指令碼，或點選 **Script List** 部分下的“**Run Script**”按鈕。

手動啟動指令碼後，你應確認已收到電子郵件通知。

當指令碼 **(a)** 啟動時，RouterOS 將檢查每個已接收/儲存的 Bluetooth 載荷，如果在載荷列表中找到任何觸發器 → 就會構造併發送一封電子郵件訊息。這封電子郵件訊息只會指示列表中檢測到了哪些觸發器，不包含額外資訊。

##### 選項 (b) {#option-b}

```ros
## 在 "" 内输入标签的 MAC 地址
:local addressRegex "2C:C8:1B:E2:15:29"

## 用于根据蓝牙广播数据过滤蓝牙广播的 POSIX 正则表达式。与
## 使用 'addressRegex' 时的用法相同。
:local advertisingDataRegex ""

## 信号强度过滤器。例如，-40 将只包括蓝牙广播
## 其信号强度强于 -40dBm。
## 要禁用此过滤器，请将其设置为 ""
:local rssiThreshold ""

#在 "" 内输入电子邮件主题
:local emailsubject "RouterOS report!"

#在 "" 内输入电子邮件地址
:local emailaddress "YOUR_GMAIL@gmail.com"

#Script:
################################## Bluetooth ##################################
:local flagStr do={
    :local str ""

    :if ($1 & 0x01) do={ :set $str " switch" }
    :if ($1 & 0x02) do={ :set $str "$str tilt" }
    :if ($1 & 0x04) do={ :set $str "$str free_fall" }
    :if ($1 & 0x08) do={ :set $str "$str impact_x" }
    :if ($1 & 0x10) do={ :set $str "$str impact_y" }
    :if ($1 & 0x20) do={ :set $str "$str impact_z" }

    :if ([:len $str] = 0) do={ :return "" }

    :return [:pick $str 1 [:len $str]]
}

:local triggernameF "free_fall"
:local triggernameT "tilt"
:local triggernameX "impact_x"
:local triggernameY "impact_y"
:local triggernameZ "impact_z"
:local triggernameS "switch"

## 查找新的蓝牙广播
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # First time this script has been run since booting, need to initialize
    # persistent variables
    :set $btOldestAdvertisementTimestamp 0
}
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex and \
        data ~ $advertisingDataRegex and \
        rssi > $rssiThreshold
]
:local advCount 0
:local lastAdvTimestamp 0
:local triggerlist ""

:local triggerF
:local triggerT
:local triggerX
:local triggerY
:local triggerZ
:local triggerS

:local messageF ""
:local messageT ""
:local messageX ""
:local messageY ""
:local messageZ ""
:local messageS ""

:local 21st ""

:foreach adv in=$advertisements do={
    :local address ($adv->"address")
    :local rssi ($adv->"rssi")
    :local epoch ($adv->"epoch")
    :local rtime ($adv->"time")
    :local ad ($adv->"data")
    :local flags [:tonum "0x$[:pick $ad 40 42]"]
    :local fflags "$[$flagStr $flags]"
    :if ($fflags="") do={:set $fflags "none - periodically broadcasted payload"}

    :local obj "# $advCount:
                             time: $rtime
                             trigger: $fflags

"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $epoch
    :set $triggerlist "$triggerlist$obj"

:set triggerF [:pick $triggerlist ([find $triggerlist "free_fall"]-0) ([find $triggerlist "free_fall"]+9)]
:if ($triggerF=$triggernameF) do={:set messageF "$triggernameF";:set 21st "not00";}
:set triggerT [:pick $triggerlist ([find $triggerlist "tilt"]-0) ([find $triggerlist "tilt"]+4)]
:if ($triggerT=$triggernameT) do={:set messageT "$triggernameT";:set 21st "not00";}
:set triggerX [:pick $triggerlist ([find $triggerlist "impact_x"]-0) ([find $triggerlist "impact_x"]+8)]
:if ($triggerX=$triggernameX) do={:set messageX "$triggernameX";:set 21st "not00";}
:set triggerY [:pick $triggerlist ([find $triggerlist "impact_y"]-0) ([find $triggerlist "impact_y"]+8)]
:if ($triggerY=$triggernameY) do={:set messageY "$triggernameY";:set 21st "not00";}
:set triggerZ [:pick $triggerlist ([find $triggerlist "impact_z"]-0) ([find $triggerlist "impact_z"]+8)]
:if ($triggerZ=$triggernameZ) do={:set messageZ "$triggernameZ";:set 21st "not00";}
:set triggerS [:pick $triggerlist ([find $triggerlist "switch"]-0) ([find $triggerlist "switch"]+6)]
:if ($triggerS=$triggernameS) do={:set messageS "$triggernameS";:set 21st "not00";}

}
:if ($advCount > 0) do={
    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp
}

:if ($21st="not00") do={/tool e-mail send to=$emailaddress subject="$emailsubject" body="$triggerlist"} else={:put "21st octet does not have triggers detected!"}
```

當指令碼 **(b)** 啟動時，RouterOS 將檢查每個已接收/儲存的 Bluetooth 載荷，如果在載荷列表中找到任何觸發器 → 就會構造併發送一封電子郵件訊息。與指令碼 **(a)** 相比，這封電子郵件訊息包含更詳細一些的資訊。在這種情況下，訊息將指示每個載荷的接收時間。

#### 排程器 {#scheduler}

要自動化此過程，請在 **System>Scheduler** 標籤頁下新增一個新排程器：

![](/img/46ba140217f063f1.webp)

在“**On Event:**”欄位下輸入“**/system script run triggernotification**”，並設定你希望執行指令碼以檢查/掃描廣播報告的 **interval**（例如，10 秒）。

點選 **Apply** 和 **OK**。

#### 結果驗證 {#result-verification}

1) 確認標籤廣播廣告報告，並且標籤的觸發器被檢測到：

![](/img/d60ecc0f246ac416.webp)

1) 確認你的電子郵件伺服器設定正確，並且你能夠從 KNOT（RouterOS）傳送電子郵件。

2) 在你手動執行指令碼或為指令碼應用排程器後，電子郵件通知應該會成功傳送，如下所示：

     指令碼 **(a)**：

![](/img/50b59795a8f27586.webp)

     指令碼 **(b)**：

![](/img/9e3705cb3b496f35.webp)
