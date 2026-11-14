---
sidebar_key: "system-information-and-utilities/scheduler"
sidebar_position: 13
title: "排程器"
sidebar_label: "排程器"
description: "RouterOS 排程器可在設定時間、按間隔、在啟動時或在選定的工作日執行命令或指令碼：夜間備份、按時間段進行的更改、更新檢查以及通知。"
tags:
  - 'scheduling'
  - 'script-execution'
  - 'time-interval'
source: https://manual.mikrotik.com/docs/system-information-and-utilities/scheduler
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

排程器會在設定時間、按間隔重複、路由器每次啟動時，或在選定的星期幾執行 RouterOS 命令或來自 `/system/script` 的指令碼。可用於夜間備份、按時段切換介面或頻寬限制、通知等任務。`/system/scheduler` 中的每個條目都在 `on-event` 中儲存計劃和要執行的命令。

當[裝置模式](./device-mode.md)為 `home` 時，排程器不可用；當裝置被標記時，無法建立或啟用條目。

## 每天執行指令碼 {#run-a-script-every-day}

將命令儲存為指令碼，然後新增一個每天 03:00 執行該指令碼的條目。以下指令碼會儲存二進位制備份和配置匯出，並覆蓋前一晚的檔案：

```ros
/system/script/add name=nightly-backup source={
    /system/backup/save name=nightly
    /export file=nightly
}
/system/scheduler/add name=nightly-backup start-time=03:00:00 interval=1d \
    on-event=nightly-backup
```

建立 `nightly-backup` 指令碼後，在 WinBox 的 **System > Scheduler > New** 下配置其計劃：

1. 將 **Name** 設為 `nightly-backup`，選擇 **Start Date**，將 **Start Time** 設為 `03:00:00`，並將 **Interval** 設為 `1d` 以每天執行。保持 **Days** 未設定，以允許每天執行。
2. 檢查 **Policy**，並選擇任務所需的許可權。截圖顯示的是新建條目的預設值；請使用許可權部分為你的指令碼選擇合適的許可權。
3. 在 **On Event** 中輸入 `nightly-backup`，保持選中 **Enabled**，然後選擇 **OK**。**On Event** 也可以直接儲存命令。

![WinBox new Scheduler entry with schedule fields, Policy permissions, and On Event commands](/img/f8081f122b7f6ded.webp)

儲存後，在 Scheduler 列表中檢查 **Next Run**，並使用 **Run Count** 檢視該條目是否已執行。截圖顯示的是輸入示例值之前的新建條目。

未指定 `start-date` 時，條目會在添加當天開始。`next-run` 顯示下次執行時間，`run-count` 統計自上次啟動以來的執行次數：

```ros
[admin@MikroTik] > /system/scheduler/print detail
0  name="nightly-backup" start-date=2026-09-25 start-time=03:00:00 interval=1d
   on-event=nightly-backup owner="admin"
   policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
   run-count=0 next-run=2026-09-26 03:00:00
```

要暫停某個條目而不刪除它，可使用 `/system/scheduler/disable nightly-backup` 將其停用。要加密備份檔案，請在 `/system/backup/save` 中新增 `password=`。有關恢復檔案的資訊，請參閱[備份](../getting-started/configuration-management/backup.md)。

## 不透過指令碼執行命令 {#run-commands-without-a-script}

`on-event` 可以直接儲存命令。以下條目會在夜間關閉裝置的所有 LED，並在早晨重新開啟：

```ros
/system/scheduler/add name=leds-off start-time=22:00:00 interval=1d \
    on-event="/system/leds/settings/set all-leds-off=immediate"
/system/scheduler/add name=leds-on start-time=07:00:00 interval=1d \
    on-event="/system/leds/settings/set all-leds-off=never"
```

短命令適合放在 `on-event` 中。較長的任務作為指令碼更易於閱讀和修改。

## 在啟動時執行指令碼 {#run-a-script-at-startup}

帶有 `start-time=startup` 的條目會在路由器每次啟動時執行。它在啟動早期執行，此時介面尚未啟用，DHCP 用戶端也還沒有地址，因此需要網路的指令碼必須等待網路就緒。以下指令碼會等待預設路由變為活動狀態（最多五分鐘），然後傳送電子郵件：

```ros
/system/script/add name=boot-notify source={
    :local tries 0
    :while (([:len [/ip/route/find where dst-address=0.0.0.0/0 active]] = 0) \
            && ($tries < 60)) do={
        :delay 5s
        :set tries ($tries + 1)
    }
    :local name [/system/identity/get name]
    :local version [/system/resource/get version]
    :local uptime [/system/resource/get uptime]
    /tool/e-mail/send to=admin@example.com subject=($name . " restarted") \
        body=("RouterOS " . $version . " started, uptime " . $uptime)
}
/system/scheduler/add name=boot-notify start-time=startup on-event=boot-notify
```

本頁的電子郵件示例需要在 `/tool/e-mail` 中配置好可用的電子郵件伺服器。請參閱[電子郵件](./e-mail.md)。

當 `interval` 非零時，`startup` 條目本身不會在啟動時執行：首次執行會在啟動後經過一個間隔時發生，之後條目會按每個間隔執行。要在啟動時以及按固定間隔運行同一指令碼，請建立兩個條目。

## 在選定的星期幾執行 {#run-on-selected-weekdays}

`days` 可將條目限制在選定的星期幾。以下條目會在週一至週五 08:00 啟用訪客 Wi-Fi 介面，並在 18:00 將其關閉。週末期間它保持關閉：

```ros
/system/scheduler/add name=guest-wifi-on days=mon,tue,wed,thu,fri \
    start-time=08:00:00 on-event="/interface/enable guest-wifi"
/system/scheduler/add name=guest-wifi-off days=mon,tue,wed,thu,fri \
    start-time=18:00:00 on-event="/interface/disable guest-wifi"
```

在週五晚上，接下來的執行時間是週五 18:00 和週一 08:00：

```ros
[admin@MikroTik] > /system/scheduler/print detail where name~"^guest-wifi"
3  name="guest-wifi-on" start-date=2026-09-25 start-time=08:00:00
   days=mon,tue,wed,thu,fri interval=0s on-event=/interface/enable guest-wifi
   owner="admin"
   policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
   run-count=0 next-run=2026-09-28 08:00:00

4  name="guest-wifi-off" start-date=2026-09-25 start-time=18:00:00
   days=mon,tue,wed,thu,fri interval=0s on-event=/interface/disable guest-wifi
   owner="admin"
   policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
   run-count=0 next-run=2026-09-25 18:00:00
```

:::tip
要按時段允許或阻止流量，請使用[防火牆過濾器](../cli-reference/ip/firewall/filter/index.md)的 `time` 匹配器，而不是透過排程器啟用和停用規則，例如 `time=08:00:00-18:00:00,mon,tue,wed,thu,fri`。這樣規則會自動生效，無需排程器條目。
:::

## 計劃如何計算 {#how-the-schedule-is-calculated}

### 開始時間和間隔 {#start-time-and-interval}

首次執行在 `start-date` 和 `start-time` 進行，它們預設為新增條目的時刻。之後，條目每隔 `interval` 執行一次。執行時間始終與開始時間加整數個間隔對齊，因此過去的開始時間會設定節奏：無論條目何時新增，`start-time=00:00:00 interval=1h` 都會在每個整點執行。

使用預設值 `interval=0s` 時，條目只執行一次。它會保留在列表中，`run-count=1` 且沒有 `next-run`。

### 星期幾 {#weekdays}

未設定 `days` 時，不考慮星期幾，間隔會跨午夜繼續：帶有 `start-time=00:00:00 interval=17h` 的條目會在第一天 00:00 和 17:00 執行，並在第二天 10:00 執行。

設定 `days` 後，每個列出的日期都會再次從 `start-time` 開始，條目會每隔 `interval` 重複執行，直到當天結束。下一次執行是在下一個列出日期的 `start-time`。使用 `interval=0s` 時，條目在每個列出的日期執行一次。`days=always` 會將這些規則應用於每一天，`days=never` 會阻止條目執行。

`1d` 或更長的間隔不支援與 `days` 一起使用。此類條目會顯示提示 `multi-day intervals are not supported with active day scheduling`。若要每天執行一次，請使用 `interval=0s`。

### 同一時間到期的條目 {#entries-due-at-the-same-time}

同一時刻到期的條目會一起啟動，順序不固定。當任務必須以特定順序執行時，請從單個指令碼中依次呼叫它們。

### 重啟和時鐘 {#reboots-and-the-clock}

重啟會將 `run-count` 重設為 0。計劃遵循路由器的本地時間和時區，請參閱[時鐘](./clock.md)。請保持時鐘同步，例如使用 [NTP](./ntp.md)；啟動後，在時鐘同步之前，它可能與實際時間不一致。

## 許可權 {#permissions}

每個條目使用 `policy` 中的策略執行其命令。預設情況下，這些是新增條目的使用者的策略，並限於適用於指令碼的策略。`owner` 顯示該使用者。需要條目不具備的策略的命令會失敗，日誌會顯示 `not enough permissions (9)` 以及條目名稱。

當 `on-event` 是指令碼名稱時，該指令碼也會使用條目的策略執行。RouterOS 會拒絕執行自身策略包含條目所沒有的許可權的指令碼。要僅使用指令碼自身的策略執行指令碼，請在 `on-event` 中使用 `/system/script/run <name> use-script-permissions`。請參閱[指令碼許可權](../developer-guides/scripting/index.md#script-permissions)。

## 更多示例 {#more-examples}

### 透過電子郵件傳送每週備份 {#email-a-weekly-backup}

以下指令碼會在每週日 02:00 儲存加密備份，並將其作為電子郵件附件傳送：

```ros
/system/script/add name=email-backup source={
    :local name [/system/identity/get name]
    /system/backup/save name=weekly password=ChangeThisPassword
    /tool/e-mail/send to=admin@example.com file=weekly.backup \
        subject=($name . " backup " . [/system/clock/get date]) \
        body="Weekly configuration backup."
}
/system/scheduler/add name=email-backup start-time=02:00:00 days=sun \
    on-event=email-backup
```

備份包含密碼、金鑰和證書。請選擇你自己的備份密碼，並僅將檔案傳送到你信任的郵箱。

### 獲取新 RouterOS 版本通知 {#get-notified-about-new-routeros-versions}

以下指令碼每天早上 09:00 檢查是否有新的 RouterOS 版本。當有新版本可用時，它會向日志寫入警告併發送電子郵件。檢查在後臺執行，因此指令碼會等待 15 秒後再讀取結果：

```ros
/system/script/add name=update-check source={
    /system/package/update/check-for-updates once
    :delay 15s
    :if ([/system/package/update/get status] = "New version is available") do={
        :local name [/system/identity/get name]
        :local latest [/system/package/update/get latest-version]
        :log warning ("RouterOS " . $latest . " is available")
        /tool/e-mail/send to=admin@example.com \
            subject=($name . ": RouterOS " . $latest . " is available") \
            body="Install it with /system/package/update/install."
    }
}
/system/scheduler/add name=update-check start-time=09:00:00 interval=1d \
    on-event=update-check
```

該指令碼僅報告新版本；請在你選擇的時間安裝，請參閱[升級](../getting-started/installation-and-upgrade/upgrade.md)。

### 每週更改訪客 Wi-Fi 密碼 {#change-the-guest-wi-fi-password-every-week}

以下指令碼會在每週一 06:00 為 [WiFi](../wireless/wifi/index.md) 安全配置檔案 `guest` 設定新的隨機密碼，並透過電子郵件傳送，例如傳送給前臺。字元集排除了容易混淆的字元，例如 `0`、`O`、`1` 和 `l`：

```ros
/system/script/add name=guest-password source={
    :local chars "abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    :local pass [:rndstr length=12 from=$chars]
    /interface/wifi/security/set [find name=guest] passphrase=$pass
    /tool/e-mail/send to=reception@example.com subject="Guest Wi-Fi password" \
        body=("The guest Wi-Fi password for this week is " . $pass)
}
/system/scheduler/add name=guest-password start-time=06:00:00 days=mon \
    on-event=guest-password
```

更改後，訪客需要使用新密碼才能連線。

### 在工作時間限制訪客頻寬 {#limit-guest-bandwidth-during-business-hours}

以下[簡單佇列](../firewall-and-quality-of-service/queues/index.md)會將訪客網路限制為 50 Mbps。在工作日 08:00 到 18:00，限制降至 10 Mbps，這樣訪客就不會拖慢辦公室連線：

```ros
/queue/simple/add name=guest target=10.0.20.0/24 max-limit=50M/50M
/system/scheduler/add name=guest-limit-day days=mon,tue,wed,thu,fri \
    start-time=08:00:00 on-event="/queue/simple/set guest max-limit=10M/10M"
/system/scheduler/add name=guest-limit-evening days=mon,tue,wed,thu,fri \
    start-time=18:00:00 on-event="/queue/simple/set guest max-limit=50M/50M"
```

## 技術細節 {#technical-details}

### 日誌訊息 {#log-messages}

新增、更改和刪除條目會寫入 `system,info` 訊息，例如 `new script scheduled by ...`、`changed scheduled script settings by ...` 和 `script removed from scheduler by ...`。條目所做的配置更改會指明該條目，例如：

```text
system,info device changed by scheduler:guest-wifi-off/action:8 (/interface set guest-wifi disabled=yes)
```

執行失敗會寫入 `script,error` 訊息，其中包含原因和失敗命令所在行：

```text
script,error executing script email-backup
script,error,debug (scheduler:email-backup) failure: error connecting to server (/tool/e-mail/send; line 4)
```

### reset 命令 {#the-reset-command}

`/system/scheduler/reset` 會清除 `on-event` 並將 `interval` 設為 `0s`。它不會重設 `run-count`。

有關所有屬性的資訊，請參閱 CLI 參考中的 [`/system/scheduler`](../cli-reference/system/scheduler.md)。
