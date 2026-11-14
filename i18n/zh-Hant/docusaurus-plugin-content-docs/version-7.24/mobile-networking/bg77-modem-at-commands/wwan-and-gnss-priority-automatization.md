---
sidebar_key: "mobile-networking/bg77-modem-at-commands/wwan-and-gnss-priority-automatization"
sidebar_position: 1
title: "WWAN 與 GNSS 優先順序自動化"
sidebar_label: "WWAN 與 GNSS 優先順序自動化"
source: https://manual.mikrotik.com/docs/7.24/mobile-networking/bg77-modem-at-commands/wwan-and-gnss-priority-automatization
captured_at: '2026-11-04T11:32:24+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

# 概述 {#overview}

蜂窩連線和 GNSS 無法同時工作（BG77 模組中的 WWAN 和 GNSS 接收鏈路共享某些硬體模組，這意味著該模組不支援 WWAN 和 GNSS 的併發執行。）。這就是引入 ***at+qgpscfg="priority",(0-1)*** 命令的原因。藉助該命令，你可以手動更改任一方的優先順序。

***at+qgpscfg="priority",0*** 命令將 **GNSS 優先順序設為最高**。

***at+qgpscfg="priority",1*** 命令將 **LTE (WWAN) 優先順序設為最高**。

在實際應用中，手動更改優先順序不太方便，因此，為了自動更改優先順序，我們建議使用下面展示的方法。

:::info
從 7.1rc3 韌體版本開始，可以檢查裝置上次獲取 NMEA 資料（GPS 資料）的時間。此資訊可用於故障排除。你可以在 CLI 中使用命令 "system gps monitor once" 檢查此引數。"data-age" 引數表示裝置上次收到 NMEA 訊息的時間。
:::

## 未檢測到出站流量時自動切換到 GNSS {#automatic-switch-to-gnss-when-no-outgoing-traffic-is-detected}

可以使用 ppp 配置檔案的 "**on-down**" 指令碼、"**idle-timeout**" 功能和 PPP 介面的 "**dial on demand**" 設定來實現自動化。

實施後，當存在網際網路流量時，BG77 調變解調器將使用蜂窩資料（在此期間不會收到 GNSS 座標），而當未檢測到網際網路流量時，將自動啟用 GPS 接收。

**Idle-timeout** 引數指定在沒有活動的情況下，鏈路將在多長時間後終止。

**On-down** 指令碼欄位允許你配置一個指令碼，該指令碼將在每次 PPP 介面關閉時執行（包括在 **idle-timeout** 不活動之後）。該指令碼會將調變解調器的優先順序設定為 GNSS 接收。

**Dial-on-demand** 將確保 PPP 介面僅在存在出站流量時嘗試建立連線（此外，調變解調器將自動設定 WWAN/蜂窩連線優先順序）。這將確保在發生 **idle-timeout** 後，除非檢測到出站封包，否則連線不會自動重新建立。

透過組合這三個功能，你可以實現以下場景：

- 如果有出站流量，PPP 介面將處於執行狀態（因為 "**dial on demand**"），並且優先順序將設定為蜂窩連線。將傳送 PPP 介面的調變解調器初始化 AT 命令（配置在 PPP 介面的 `modem-init="AT+QGPSCFG="priority",1"` 設定下）以設定 WWAN 優先順序。在此期間，不會收到 GPS 座標。
- 如果在 "**idle-timeout**" 不活動視窗後未檢測到流量，PPP 介面將關閉，並且由於 "**dial on demand**" 設定，在檢測到出站封包之前不會建立連線。此時將執行 "**on-down**" 指令碼，將 WWAN 優先順序切換為 GNSS 優先順序。
為了實現這一點，只需新增一個新的 PPP 配置檔案：

```ros
/ppp profile add idle-timeout=30s name=BG77 on-down="/interface ppp-client at-chat [find where modem-init=\"AT+QGPSCFG=\\\"priority\\\",1\"] input=\"AT+QGPSCFG=\\\"priority\\\",0\""
```

上面的示例建立了一個名為 "BG77" 的新配置檔案，將 **idle-timeout** 設定為 30 秒，並啟用 **on-down** 指令碼，該指令碼將傳送 GNSS 優先順序 AT 命令。

之後，請確保將此新建立的配置檔案應用到 PPP 介面：

```ros
/interface ppp-client set profile=BG77 0
```

並確認它已應用（`profile=BG77`）：

```ros
/interface ppp-client print
Flags: X - disabled; R - running 
0 R name="ppp-out1" max-mtu=1500 max-mru=1500 mrru=disabled port=modem data-channel=2 info-channel=2 
apn="internet" pin="" user="" password="" profile=BG77 phone="" dial-command="ATDT" 
modem-init="AT+QGPSCFG="priority",1" null-modem=no dial-on-demand=yes add-default-route=yes 
default-route-distance=1 use-peer-dns=yes keepalive-timeout=30 allow=pap,chap,mschap1,mschap2 
```

## 使用指令碼和排程器切換到 GNSS {#switch-to-gnss-using-scripts-and-scheduler}

應為下面的指令碼配置排程器。排程器將確保指令碼每隔 ***x*** 小時/分鐘（或你需要的任何時間）啟動。

```
:global lat
:global lon
:global spd
:global alt
/interface ppp-client set ppp-out1 disabled=yes
log info ("disabling WWAN to get GPS coordinates")
/interface ppp-client at-chat ppp-out1 input="AT+QGPSCFG=\"priority\",0"
log info ("enabling priority for GPS")
###the time in the delay below is the time that the device will wait for to get the coordinate fix
delay 32000ms
log info ("reading GPS coordinates")
/system gps monitor once do={
:set $lat $("latitude")
:set $lon $("longitude")
:set $spd $("speed")
:set $alt $("altitude")
}
:set $spd [:pick $spd 0 [find $spd " km"]]
:set $alt [:pick $alt 0 [find $alt "m"]]
if ($lat != "none") do={\
log info ("enabling priority back to WWAN")
/interface ppp-client at-chat ppp-out1 input="AT+QGPSCFG=\"priority\",1"
log info ("enabling WWAN")
/interface ppp-client set ppp-out1 disabled=no
delay 1000ms
###if dial on demand is enabled
###/ping 1.1.1.1 count=1
#the delay below waits for 5 seconds for the ppp connection to get established - this time can differ based on the signal strength
delay 5000ms
log info ("posting coordinates via fetch")
/tool fetch http-method=post output=user http-header-field="content-type:application/json" http-data="[\
{\
                \"payload\":{\
                             \"lat\":$lat,\
                              \"lng\":$lon,\
                               \"speed\":$spd,\
                                \"altitude\":$alt\
                                    }\
    }\
]" url="https://change-this-URL-accordingly"}\
else={
log info ("could not read GPS coordinates...enabling back WWAN")
/interface ppp-client at-chat ppp-out1 input="AT+QGPSCFG=\"priority\",1"
/interface ppp-client set ppp-out1 disabled=no
delay 1000ms
###if dial on demand is enabled
###/ping 1.1.1.1 count=1
}
```

如果啟用了 "dial on demand"，請取消註釋（刪除 "###"）指令碼中的 ping 行 "/ping 1.1.1.1 count=1"，因為如果沒有出站流量 → ppp 介面將不會建立連線。

該指令碼將停用 ppp 介面，傳送 GNSS 優先順序命令，並等待 32 秒，直到裝置獲取座標（這是建議 Quectel 調變解調器獲取定位鎖定的時間/週期）。你可以根據偏好和訊號強度更改此時間。每個單獨的情況可能都是獨特的。在 32 秒延遲之後，如果座標成功接收（如果緯度不等於 "none" 而是等於任何其他值），指令碼將傳送 WWAN 優先順序命令，重新啟用 ppp 介面，並使用 "/tool fetch" 將座標釋出到配置的 HTTP 伺服器。如果在 32 秒延遲後未收到座標（如果緯度將為 "none"），指令碼將傳送 WWAN 優先順序命令並重新啟用 ppp 介面，而不釋出任何結果。

不要忘記根據你的 HTTP 伺服器配置/要求相應地修改指令碼中的 "/tool fetch" 部分。

你也可以使用 MQTT 代替 HTTP post。為此，請將配置中的 "/tool fetch" 部分從：

```
/tool fetch http-method=post output=user http-header-field="content-type:application/json" http-data="[\
{\
                \"payload\":{\
                             \"lat\":$lat,\
                              \"lng\":$lon,\
                               \"speed\":$spd,\
                                \"altitude\":$alt\
                                    }\
    }\
]" url="https://change-this-URL-accordingly"}\
```

改為 MQTT：

```
/iot mqtt publish broker="AWS" topic="my/test/topic" message="{\
                                 \"lat\":$lat,\
                                  \"lng\":$lon,\
                                   \"speed\":$spd,\
                                    \"altitude\":$alt \                                
  }"}\
```

按你認為合適的方式修改 broker、topic 和 message。你可以透過連結找到有關如何配置 MQTT 的更多資訊。

例如，如果 MQTT 伺服器/broker 是 AWS，釋出的結果將如下所示：

![](/img/f483ecce75148524.webp)

## 使用指令碼和排程器在未檢測到出站流量時切換到 GNSS {#switch-to-gnss-when-no-outgoing-traffic-is-detected-using-scripts-and-scheduler}

第 1 個指令碼用於檢查是否有任何流量，並據此來回切換優先順序。

第 2 個指令碼可用於啟用 WWAN 優先順序，並將 GPS 座標釋出到你選擇的伺服器。你可以使用任何支援的協定，例如 HTTPS post（fetch）或 MQTT 來發布座標。

### 第 1 個指令碼 {#1st-script}

下面的指令碼將自動建立一個排程器：

```
/system scheduler
add name="GPS/WWAN enabler" on-event=":delay 30s\r\
    \n\r\
    \n:local pppName ppp-out1\r\
    \n:local pppModemInitInit \"AT+QGPSCFG=\\\"priority\\\",1\"\r\
    \n:local gpsCmd \"AT+QGPSCFG=\\\"priority\\\",0\"\r\
    \n:local idleCount 5\r\
    \n\r\
    \n\r\
    \n:local pppStats\r\
    \n:local pppStatsPrev\r\
    \n:local pppStatsReset\r\
    \n:local idleCounter\r\
    \n\r\
    \n:while (true) do={\r\
    \n\r\
    \n:if ( \\\r\
    \n  [/interface ppp-client get \$pppName running] \\\r\
    \n  && [/system gps get enabled] \\\r\
    \n  && [/interface ppp-client get \$pppName dial-on-demand] \\\r\
    \n  && \$pppModemInitInit=[/interface ppp-client get \$pppName modem-init]\
    \_) \\\r\
    \n  do={\r\
    \n    :set pppStats [:toarray ([/interface print stats as-value where name\
    =ppp-out1]->0)] \r\
    \n    :if ( \\\r\
    \n      \$pppStats->\"rx-packet\"=\$pppStatsPrev->\"rx-packet\" \\\r\
    \n      && \$pppStats->\"tx-packet\"=\$pppStatsPrev->\"tx-packet\" ) \\\r\
    \n      do={\r\
    \n        :set idleCounter (\$idleCounter+1)\r\
    \n:put (\"debug: idle \".\$idleCounter)\r\
    \n        :if ( \\\r\
    \n          \$idleCounter>=\$idleCount \\\r\
    \n          && \$pppStats->\"rx-packet\"!=\$pppStatsReset->\"rx-packet\" \
    \\\r\
    \n          && \$pppStats->\"tx-packet\"!=\$pppStatsReset->\"tx-packet\" )\
    \_\\\r\
    \n          do={\r\
    \n            :set pppStatsReset \$pppStats\r\
    \n            :set idleCounter 0\r\
    \n            :log info (\$pppName.\" idling - reseting dial-on-demand, pr\
    ioritizing GPS\")\r\
    \n            /interface ppp-client set \$pppName disabled=yes\r\
    \n            :do { /interface ppp-client at-chat \$pppName input=\$gpsCmd\
    \_} \\\r\
    \n                on-error={\r\
    \n:put (\"debug: GPS at-chat error\")                \r\
    \n                  :set idleCounter 0\r\
    \n                  :set pppStatsReset ({})\r\
    \n                  }\r\
    \n            /interface ppp-client set \$pppName disabled=no\r\
    \n            }\r\
    \n          :delay 1s\r\
    \n        } \\\r\
    \n      else={\r\
    \n:put (\"debug: no idle\")      \r\
    \n        :set idleCounter 0\r\
    \n        :set pppStatsPrev \$pppStats\r\
    \n        :delay 1s \r\
    \n        }\r\
    \n    } \\\r\
    \n  else={\r\
    \n:put (\"debug: unsupported config\")\r\
    \n    :set idleCounter 0\r\
    \n    :set pppStatsReset ({})\r\
    \n    :delay 1s\r\
    \n    }\r\
    \n}" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-time=startup
```

複製上面的所有行並將它們貼上到新指令碼中。執行該指令碼，你將建立一個 "scheduler"。你可以在 System>Scheduler>"GPS/WWAN enabler" 下檢查 "scheduler"。

原始指令碼如下所示：

```
:local pppName ppp-out1
:local pppModemInitInit "AT+QGPSCFG=\"priority\",1"
:local gpsCmd "AT+QGPSCFG=\"priority\",0"
:local idleCount 5
:local pppStats
:local pppStatsPrev
:local pppStatsReset
:local idleCounter
:while (true) do={
:if ( \
  [/interface ppp-client get $pppName running] \
  && [/system gps get enabled] \
  && [/interface ppp-client get $pppName dial-on-demand] \
  && $pppModemInitInit=[/interface ppp-client get $pppName modem-init] ) \
  do={
    :set pppStats [:toarray ([/interface print stats as-value where name=ppp-out1]->0)] 
    :if ( \
      $pppStats->"rx-packet"=$pppStatsPrev->"rx-packet" \
      && $pppStats->"tx-packet"=$pppStatsPrev->"tx-packet" ) \
      do={
        :set idleCounter ($idleCounter+1)
:put ("debug: idle ".$idleCounter)
        :if ( \
          $idleCounter>=$idleCount \
          && $pppStats->"rx-packet"!=$pppStatsReset->"rx-packet" \
          && $pppStats->"tx-packet"!=$pppStatsReset->"tx-packet" ) \
          do={
            :set pppStatsReset $pppStats
            :set idleCounter 0
            :log info ($pppName." idling - reseting dial-on-demand, prioritizing GPS")
            /interface ppp-client set $pppName disabled=yes
            :do { /interface ppp-client at-chat $pppName input=$gpsCmd } \
                on-error={
:put ("debug: GPS at-chat error")                
                  :set idleCounter 0
                  :set pppStatsReset ({})
                  }
            /interface ppp-client set $pppName disabled=no
            }
          :delay 1s
        } \
      else={
:put ("debug: no idle")      
        :set idleCounter 0
        :set pppStatsPrev $pppStats
        :delay 1s 
        }
    } \
  else={
:put ("debug: unsupported config")
    :set idleCounter 0
    :set pppStatsReset ({})
    :delay 1s
    }
}
```

為了讓指令碼正常工作，必須滿足幾個條件。

第一個條件是 ppp 介面（Interfaces>Interface）和 GPS（System>GPS）都必須啟用並同時工作。你可能需要在啟用 GPS 之前停用 ppp，因為它們都使用同一個序列埠。當 GPS 和 ppp 都啟用後，請確保滿足第二個條件。

第二個條件是 AT 命令 "***AT+QGPSCFG="priority",1***" 已為 ppp 介面配置在 "Modem Init" 欄位下：

![](/img/9ee14b1061e7bca1.webp)

這樣做的效果是，每當 ppp 連線成功建立時，就傳送 WWAN 優先順序命令。

最後，第三個條件是 ppp 介面啟用了 "dial on demand"：

![](/img/95433141e4a71f06.webp)

這是必需的，因為否則當 "dial on demand" 被停用時 → 每當埠重新啟用時，ppp 介面都會自動傳送帶有 WWAN 優先順序設定的 AT 命令（嘗試建立連線）。當 "dial on demand" 啟用時 → 在介面重新啟用後，不會建立 ppp 連線，並且在檢測到出站封包之前不會發送用於 WWAN 優先順序的 AT 命令。

當滿足所有 3 個條件時 → 指令碼將執行以下操作：

指令碼將比較 "counters"，以判斷是否存在流量（基於 ppp 介面的 Tx 封包和 Rx 封包）。如果沒有流量，"counter" 會增加，當它達到 "idleCount" 時，ppp 介面會被停用、重新啟用，併發送 GNS 優先順序命令。在此期間，如果仍然沒有出站流量，GPS 座標應更新（在 System>GPS 下）。一旦檢測到任何流量，"counter" 將被重設，並透過建立 ppp 連線傳送 WWAN 優先順序命令。

一旦滿足所有 3 個條件且排程器準備就緒，請重啟裝置，以便指令碼生效。

### 第 2 個指令碼 {#2nd-script}

第二個指令碼用於收集 GPS 座標並將它們進一步傳送到伺服器。

```
:global lat
:global lon
:global spd
:global alt
/system gps monitor once do={
:set $lat $("latitude")
:set $lon $("longitude")
:set $spd $("speed")
:set $alt $("altitude")
}
:set $spd [:pick $spd 0 [find $spd " km"]]
:set $alt [:pick $alt 0 [find $alt "m"]]
:if ($lat != "none") do={
/ping 1.1.1.1 count=1
:delay 3000ms;
/tool fetch http-method=post output=user http-header-field="content-type:application/json" http-data="[\
{\
                \"payload\":{\
                             \"lat\":$lat,\
                              \"lng\":$lon,\
                               \"speed\":$spd,\
                                \"altitude\":$alt\
                                    }\
    }\
]" url="https://change-this-URL"}\
else={log info ("could not read GPS coordinates")}
```

該指令碼將 "讀取" GPS 座標，如果緯度可以成功 "讀取"（如果緯度不等於 "none" 而是等於任何其他值），則 ping "1.1.1.1" 一次（以生成出站流量），等待 3 秒以便建立 ppp 連線，並啟動 "/tool fetch"（HTTP post）。否則，如果無法確定緯度（在指令碼啟動時），則不會發生任何事（你將看到一條日誌訊息，表明裝置無法讀取 GPS 座標）。

你可以將指令碼中的 "delay" 行更改為你的裝置成功與 ISP 建立 ppp（CAT-M/NB-IoT）連線所需的實際時間。

你可以設定排程器，在任意需要時執行該指令碼。

指令碼中的 "/tool fetch" 部分應根據你的伺服器設定進行配置。

你也可以使用 MQTT 代替 HTTP post。如果你希望這樣做，請將 "/tool fetch" 部分從：

```
/tool fetch http-method=post output=user http-header-field="content-type:application/json" http-data="[\
{\
                \"payload\":{\
                             \"lat\":$lat,\
                              \"lng\":$lon,\
                               \"speed\":$spd,\
                                \"altitude\":$alt\
                                    }\
    }\
]" url="https://change-this-URL-accordingly"}\
```

改為：

```
/iot mqtt publish broker="AWS" topic="my/test/topic" message="&#123;\
                                 \"lat\":$lat,\
                                  \"lng\":$lon,\
                                   \"speed\":$spd,\
                                    \"altitude\":$alt \                                  
  }"}\
```

不要忘記按你認為合適的方式修改 broker、topic 和 message。你可以透過連結找到有關如何配置 MQTT 的更多資訊。

例如，如果 MQTT 伺服器是 AWS，結果將如下所示：

![](/img/f483ecce75148524.webp)
