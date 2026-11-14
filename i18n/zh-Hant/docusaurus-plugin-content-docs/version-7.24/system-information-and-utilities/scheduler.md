---
sidebar_key: "system-information-and-utilities/scheduler"
sidebar_position: 14
title: "排程器"
sidebar_label: "排程器"
description: "MikroTik RouterOS 排程器支援定時執行指令碼，可精確控制任務執行的時間以及執行頻率。它支援基於間隔或一次性執行，並具有啟動時間、間隔時長和指令碼事件名稱等屬性。"
tags:
  - 'scheduling'
  - 'script-execution'
  - 'time-interval'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/scheduler
captured_at: '2026-11-04T11:33:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 概述 {#summary}

排程器可以在特定時間點、經過指定時間間隔後或同時按兩者觸發指令碼執行。

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **days** (*always* \| *sun* \| *mon* \| *tue* \| *wed* \| *thu* \| *fri* \| *sat*; 預設：**always**) | 任務可以執行的一週中的日期。多個日期用逗號分隔（例如 `mon,wed,fri`）。使用 `always` 表示每天執行。 |
| **interval** (*time*; 預設：**0s**) | 兩次指令碼執行之間的間隔。設定為零時，指令碼僅在開始時間執行一次。 |
| **name** (*string*; 預設： ) | 任務名稱。 |
| **on-event** (*string*; 預設： ) | 要執行的指令碼。 |
| **policy** (*ftp \| reboot \| read \| write \| policy \| test \| password \| sniff \| sensitive \| romon*; 預設： ) | 應用於計劃指令碼的策略，用於控制執行期間的許可權。 |
| **start-date** (*date*; 預設： ) | 指令碼首次執行的日期。 |
| **start-time** (*time \| startup*; 預設： ) | 指令碼首次執行的時間。使用 `startup` 在系統啟動 3 秒後執行。 |
| **run-count** (*read-only: integer*) | 每次指令碼執行時遞增的計數器。重啟後重設。 |

## 說明 {#notes}

重啟路由器會重設 run-count 計數器。

如果需要同時執行多個指令碼，它們會按照在排程器配置中出現的順序執行。如果一個計劃指令碼用於停用另一個指令碼，這一點可能很重要。

如果需要更復雜的執行模式，通常可以透過排程多個指令碼，並讓它們相互啟用和停用來實現。

當同時設定了 `days`、特定的 `start-time` 和 `interval` 時，任務會在匹配日期的指定開始時間啟動，並按給定間隔重複執行，直到當天結束。

:::note
如果排程項的 start-time 設定為 startup，則其行為等同於將 start-time 和 start-date 設定為控制檯啟動後 3 秒的時間。帶有 `start-time=startup` 和 `interval=0` 的指令碼會在每次路由器啟動時執行一次。如果 interval 設定為非 0 值，則排程器在啟動時**不會**執行。
:::

### 示例 {#examples}

我們將新增一個每小時執行指令碼 log-test 的任務：

```ros
[admin@MikroTik] /system/script> add name=log-test source=":log info message=test" 
[admin@MikroTik] /system/script> print 
Flags: I - invalid 
0 name="log-test" owner="admin" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon dont-require-permissions=no run-count=0 
source=:log info message=test 
[admin@MikroTik] /system/script> .. /scheduler 
[admin@MikroTik] /system/scheduler> add name=run-1h interval=1h 
on-event=log-test 
[admin@MikroTik] /system/scheduler> print 
Flags: X - disabled 
# NAME ON-EVENT START-DATE START-TIME INTERVAL RUN-COUNT 
0 run-1h log-test 2004-03-30 06:11:35 1h 0 
[admin@MikroTik] /system/scheduler>
```

以下示例僅在工作日執行任務：

```ros
[admin@MikroTik] /system/script> add name=business-log source=":log info message=workday"
[admin@MikroTik] /system/script> .. scheduler
[admin@MikroTik] /system/scheduler> add name=workday-task interval=1d on-event=business-log days=mon,tue,wed,thu,fri start-time=8:00:00
[admin@MikroTik] /system/scheduler> print
Flags: X - disabled
# NAME ON-EVENT START-DATE START-TIME INTERVAL DAYS RUN-COUNT
0 workday-task business-log 2026-07-16 08:00:00 1d mon,tue,wed,thu,fri 0
[admin@MikroTik] /system/scheduler>
```

在另一個示例中，將新增兩個指令碼，用於更改佇列規則 "Cust0" 的頻寬設定。每天上午 9 點將佇列設定為 64Kb/s，下午 5 點將佇列設定為 128Kb/s。佇列規則、指令碼和排程任務如下：

```ros
[admin@MikroTik] /queue/simple> add name=Cust0 interface=ether1 \ 
\... dst-address=192.168.0.0/24 limit-at=64000
 [admin@MikroTik] /queue/simple> print
 Flags: X - disabled, I - invalid 0 name="Cust0" target-address=0.0.0.0/0 dst-address=192.168.0.0/24
 interface=ether1 limit-at=64000 queue=default priority=8 bounded=yes 
[admin@MikroTik] /queue/simple> /system/script 
[admin@MikroTik] /system/script> add name=start_limit source={/queue/simple/set \
 \... Cust0 limit-at=64000} 
[admin@MikroTik] /system/script> add name=stop_limit source={/queue/simple/set \ 
\... Cust0 limit-at=128000} 
[admin@MikroTik] /system/script> print 
0 name="start_limit" source="/queue/simple/set Cust0 limit-at=64000" 
owner=admin run-count=0 
1 name="stop_limit" source="/queue/simple/set Cust0 limit-at=128000" 
owner=admin run-count=0 
[admin@MikroTik] /system/script> .. scheduler 
[admin@MikroTik] /system/scheduler> add interval=24h name="set-64k" \ 
\... start-time=9:00:00 on-event=start_limit 
[admin@MikroTik] /system/scheduler> add interval=24h name="set-128k" \
 \... start-time=17:00:00 on-event=stop_limit 
[admin@MikroTik] /system/scheduler> print
 Flags: X - disabled 
# NAME ON-EVENT START-DATE START-TIME INTERVAL RUN-COUNT
 0 set-64k start... 2008-10-30 09:00:00 1d 0 
1 set-128k stop_... 2008-10-30 17:00:00 1d 0 
[admin@MikroTik] /system/scheduler>
```

以下示例排程一個指令碼，每週透過電子郵件傳送路由器配置備份。

```ros
[admin@MikroTik] /system/script> add name=e-backup source={/system/backup 
{... save name=email; /tool/e-mail/send to="root@host.com" subject=([/system 
{... /identity/get name] . " Backup") file=email.backup} 
[admin@MikroTik] /system/script> print 
0 name="e-backup" source="/system/backup/save name=ema... owner=admin run-count=0 

[admin@MikroTik] /system/script> ../scheduler 
[admin@MikroTik] /system/scheduler> add interval=7d name="email-backup" \
 \... on-event=e-backup 
[admin@MikroTik] /system/scheduler> print
 Flags: X - disabled
 # NAME ON-EVENT START-DATE START-TIME INTERVAL RUN-COUNT 
0 email-... e-backup 2008-10-30 15:19:28 7d 1 
[admin@MikroTik] /system/scheduler>
```

不要忘記在 `/tool/e-mail` 下設定電子郵件設定，即 SMTP 伺服器和 From: 地址。例如：

```ros
[admin@MikroTik] /tool/e-mail> set server=159.148.147.198 from=SysAdmin@host.com 
[admin@MikroTik] /tool/e-mail> print
 server: 159.148.147.198 
from: SysAdmin@host.com 
[admin@MikroTik] /tool/e-mail>
```

下面的示例會從午夜到中午每小時將 'x' 放入日誌中：

```ros
[admin@MikroTik] /system/script> add name=enable-x source={/system/scheduler 
{... enable x} 
[admin@MikroTik] /system/script> add name=disable-x source={/system/scheduler 
{... disable x} 
[admin@MikroTik] /system/script> add name=log-x source={:log info message=x} 
[admin@MikroTik] /system/script> .. scheduler 
[admin@MikroTik] /system/scheduler> add name=x-up start-time=00:00:00 \ 
\... interval=24h on-event=enable-x 
[admin@MikroTik] /system/scheduler> add name=x-down start-time=12:00:00
 \... interval=24h on-event=disable-x 
[admin@MikroTik] /system/scheduler> add name=x start-time=00:00:00 interval=1h \ 
\... on-event=log-x 
[admin@MikroTik] /system/scheduler> print 
Flags: X - disabled
 # NAME ON-EVENT START-DATE START-TIME INTERVAL RUN-COUNT 
0 x-up enable-x 2008-10-30 00:00:00 1d 0 
1 x-down disab... 2008-10-30 12:00:00 1d 0 
2 x log-x 2008-10-30 00:00:00 1h 0 
[admin@MikroTik] /system/scheduler>
```
