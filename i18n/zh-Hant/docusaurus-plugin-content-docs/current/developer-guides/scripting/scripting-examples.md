---
sidebar_key: "developer-guides/scripting/scripting-examples"
sidebar_position: 1
title: "指令碼示例"
sidebar_label: "指令碼示例"
description: "本頁面提供 MikroTik RouterOS 的指令碼示例，演示如何使用 RouterOS 指令碼命令建立和修改檔案、追加文字、檢查 IP 變化、去除網路掩碼以及解析主機名。"
tags:
  - 'scripting'
source: https://manual.mikrotik.com/docs/developer-guides/scripting/scripting-examples
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

無法直接建立檔案；不過，可以使用以下變通方法：

```ros
/file print file=myFile
/file set myFile.txt contents=""
```

## 在新行中向檔案追加文字 {#append-text-to-a-file-in-a-new-line}

沒有直接向檔案追加文字的方法；可以儲存舊內容，然後追加一行包含新增文字的內容：

```ros
:local oldText [/file get myFile.txt contents as-string]
:local addText "test append"
:local newText ($oldText."\n".$addText)
/file set myFile.txt contents=$newText
```

## 檢查介面上的 IP 是否已更改 {#check-if-ip-on-the-interface-has-changed}

某些提供商會分配動態 IP 地址。此指令碼會將新地址與當前地址進行比較。

```ros
:global currentIP;

:local newIP [/ip address get [find interface="ether1"] address];

:if ($newIP != $currentIP) do={
    :put "ip address $currentIP changed to $newIP";
    :set currentIP $newIP;
}
```

## 去除子網掩碼 {#strip-netmask}

此指令碼在需要不帶子網掩碼的 IP 地址時很有用（例如，在防火牆中使用），因為 `/ip address get [id] address` 會同時返回地址及其子網掩碼。

```ros
:global ipaddress 10.1.101.1/24

:for i from=( [:len $ipaddress] - 1) to=0 do={
	:if ( [:pick $ipaddress $i] = "/") do={
		:put [:pick $ipaddress 0 $i]
	}
}
```

更簡單的方法是：

```ros
:global ipaddress 10.1.101.1/24
:put [:pick $ipaddress 0 [:find $ipaddress "/"]]
```

## 解析主機名 {#resolve-host-name}

許多使用者請求能夠對 RADIUS 伺服器、防火牆規則等使用 DNS 名稱而不是 IP 地址。

以下示例會解析 RADIUS 伺服器的 IP。

假設 RADIUS 伺服器配置如下：

```ros
/radius
add address=3.4.5.6 comment=myRad
```

以下指令碼會解析伺服器的 IP 地址，將結果與配置值進行比較，如果不同則替換：

```ros
/system script add name="resolver" source= {

:local resolvedIP [:resolve "server.example.com"];
:local radiusID [/radius find comment="myRad"];
:local currentIP [/radius get $radiusID address];

:if ($resolvedIP != $currentIP) do={
   /radius set $radiusID address=$resolvedIP;
   /log info "radius ip updated";
}

}
```

例如，將此指令碼新增到排程器，使其每五分鐘執行一次。

```ros
/system scheduler add name=resolveRadiusIP on-event="resolver" interval=5m
```

## 將簡單佇列統計資訊寫入多個檔案 {#write-simple-queue-stats-in-multiple-files}

假設佇列名稱使用 `some text.1` 格式，這樣你就可以按點號後的數字進行搜尋。

```ros
:local entriesPerFile 10;
:local currentQueue 0;
:local queuesInFile 0;
:local fileContent "";
#确定所需文件数量
:local numQueues [/queue simple print count-only] ;
:local fileCount ($numQueues / $entriesPerFile);
:if ( ($fileCount * $entriesPerFile) != $numQueues) do={
   :set fileCount ($fileCount + 1);
}

#移除旧文件
/file remove [find name~"stats"];

:put "fileCount=$fileCount";

:for i from=1 to=$fileCount do={
#创建文件
   /file print file="stats$i.txt";
#清空内容
   /file set [find name="stats$i.txt"] contents="";

   :while ($queuesInFile < $entriesPerFile) do={
     :if ($currentQueue < $numQueues) do={
         :set currentQueue ($currentQueue +1);
         :put $currentQueue ;
         /queue simple
         :local internalID [find name~"\\.$currentQueue\$"];
         :put "internalID=$internalID";
         :set fileContent ($fileContent . [get $internalID target-address] . \
           " " . [get $internalID total-bytes] . "\r\n");
     }
     :set queuesInFile ($queuesInFile +1);

   }
   /file set "stats$i.txt" contents=$fileContent;
   :set fileContent "";
   :set queuesInFile 0;

}

```

## 生成備份並透過電子郵件傳送 {#generate-backup-and-send-it-by-e-mail}

此指令碼會生成備份檔案，並將其傳送到指定的電子郵件地址。郵件主題包含路由器名稱、當前日期和時間。

請注意，在使用此指令碼之前，必須先配置 SMTP 伺服器。有關配置選項，請參閱 [電子郵件](../../system-information-and-utilities/e-mail.md)。

```ros
/system backup save name=email_backup
/tool e-mail send file=email_backup.backup to="me@test.com" body="See attached file" \
   subject="$[/system identity get name] $[/system clock get time] $[/system clock get date] Backup"
```

:::warning
備份檔案包含密碼等敏感資訊。因此，指令碼或排程器必須具有 'sensitive' 策略才能訪問生成的備份檔案。
:::

## 將字串用作函式 {#use-string-as-a-function}

```ros
:global printA [:parse ":local A; :put \$A;" ];
$printA
```

## 檢查頻寬並新增限制 {#check-bandwidth-and-add-limitations}

此指令碼檢查介面上的下載速度是否超過 512 kbps；如果超過，指令碼會新增一個將速度限制為 256 kbps 的佇列。

```ros
:foreach i in=[/interface find] do={
    /interface monitor-traffic $i once do={
        :if ($"received-bits-per-second" > 0 ) do={
            :local tmpIP [/ip address get [/ip address find interface=$i] address] ;
#            :log warning $tmpIP ;
            :for j from=( [:len $tmpIP] - 1) to=0 do={
                :if ( [:pick $tmpIP $j] = "/") do={
                    /queue simple add name=$i max-limit=256000/256000 dst-address=[:pick $tmpIP 0 $j] ;
                }
            }
        }
    }
}
```

## 阻止訪問特定網站 {#block-access-to-specific-websites}

當你希望在不使用 Web 代理的情況下阻止某些網站時，此指令碼很有用。

此示例會檢視 DNS 快取中的 "Rapidshare" 和 "youtube" 條目，並將 IP 新增到名為 "restricted" 的地址列表中。開始之前，必須將路由器設定為捕獲所有 DNS 請求：

```ros
/ip firewall nat
add action=redirect chain=dstnat comment=DNS dst-port=53 protocol=tcp to-ports=53
add action=redirect chain=dstnat dst-port=53 protocol=udp to-ports=53
```

然後新增防火牆規則：

```ros
/ip firewall filter
add chain=forward dst-address-list=restricted action=drop
```

編寫一個指令碼，並安排它每 30 秒執行一次。

指令碼程式碼：

```ros
:foreach i in=[/ip dns cache find] do={
    :local bNew "true";
    :local cacheName [/ip dns cache all get $i name] ;
#    :put $cacheName;

    :if (([:find $cacheName "rapidshare"] >= 0) || ([:find $cacheName "youtube"] >= 0)) do={

        :local tmpAddress [/ip dns cache get $i address] ;
#	:put $tmpAddress;

# 如果 address list 为空，则不要检查
        :if ( [/ip firewall address-list find list="restricted" ] = "") do={
            :log info ("added entry: $[/ip dns cache get $i name] IP $tmpAddress");
            /ip firewall address-list add address=$tmpAddress list=restricted comment=$cacheName;
        } else={
            :foreach j in=[/ip firewall address-list find list="restricted"] do={
                :if ( [/ip firewall address-list get $j address] = $tmpAddress ) do={
                    :set bNew "false";
                }
            }
            :if ( $bNew = "true" ) do={
                :log info ("added entry: $[/ip dns cache get $i name] IP $tmpAddress");
                /ip firewall address-list add address=$tmpAddress list=restricted comment=$cacheName;
            }
        }
    }
}
```

:::note 替代方案
不必掃描 DNS 快取，你可以直接在防火牆中匹配主機名。對於 HTTPS 流量，請使用基於 SNI 的 `tls-host` 匹配器，它要求 `protocol=tcp`：

```ros
/ip firewall filter
add chain=forward protocol=tcp tls-host=*.youtube.com action=drop
```

對於明文 HTTP，使用 `content` 引數匹配有效載荷：

```ros
/ip firewall filter
add chain=forward content=youtube.com action=drop
```

這些匹配器會檢查流量本身，因此它們不依賴路由器解析用戶端的 DNS 查詢，也不依賴 DNS 快取已被填充——上面的 DNS 快取方法只能捕獲最近透過路由器查詢過的站點。

`tls-host=*.youtube.com` 匹配子域，例如 `www.youtube.com`；要匹配 `youtube.com` 本身，需新增第二條規則，使用 `tls-host=youtube.com`。`tls-host` 僅能看到基於 TCP 的 TLS：透過 QUIC（UDP 埠 443 上的 HTTP/3）訪問站點的瀏覽器不會被匹配。當 UDP 埠 443 被阻止時，瀏覽器會回退到 TCP。
:::

## 解析檔案以新增 ppp secrets {#parse-file-to-add-ppp-secrets}

此指令碼要求檔案中的條目採用以下格式：

username,password,local\_address,remote\_address,profile,service

:::note
檔案必須使用 CR/LF 行尾（Windows 格式），因為指令碼會搜尋行間的 `\r\n` 序列。使用裸 `\n` 行尾的檔案（例如以 Unix 格式上傳的檔案，或由使用 `\n` 的指令碼寫入的檔案）將不匹配。
:::

例如：

```ros
janis,123,1.1.1.1,2.2.2.1,ppp_profile,myService
juris,456,1.1.1.1,2.2.2.2,ppp_profile,myService
aija,678,1.1.1.1,2.2.2.3,ppp_profile,myService
```

```ros
:global content [/file get [/file find name=test.txt] contents] ;
:global contentLen [ :len $content ] ;

:global lineEnd 0;
:global line "";
:global lastEnd 0;

:do {
       :set lineEnd [:find $content "\r\n" $lastEnd ] ;
       :set line [:pick $content $lastEnd $lineEnd] ;
       :set lastEnd ( $lineEnd + 2 ) ;

       :local tmpArray [:toarray $line] ;
	:if ( [:pick $tmpArray 0] != "" ) do={
	:put $tmpArray;
         /ppp secret add name=[:pick $tmpArray 0] password=[:pick $tmpArray 1] \
             local-address=[:pick $tmpArray 2] remote-address=[:pick $tmpArray 3] \
             profile=[:pick $tmpArray 4] service=[:pick $tmpArray 5];
}
} while ($lineEnd < $contentLen)
```

## 檢測新的日誌條目 {#detect-new-log-entry}

此指令碼檢查是否已向特定緩衝區新增新的日誌條目。

在此示例中，使用 PPPoE 日誌：

```ros
/system logging action
add name="pppoe"
/system logging
add action=pppoe topics=pppoe,info,!ppp,!debug
```

日誌緩衝區如下所示：

```ros
[admin@mainGW] > /log print where buffer=pppoe
13:11:08 pppoe,info PPPoE connection established from 00:0C:42:04:4C:EE
```

以下指令碼會檢測何時添加了新條目。

```ros
:global lastTime;

:global currentBuf [ :toarray [ /log find buffer=pppoe  ] ] ;
:global currentLineCount [ :len $currentBuf ] ;
:global currentTime [ :totime [/log get [ :pick $currentBuf ($currentLineCount -1) ] time   ] ];

:global message "";

:if ( $lastTime = "" ) do={
	:set lastTime $currentTime ;
	:set message [/log get [ :pick $currentBuf ($currentLineCount-1) ] message];

} else={
	:if ( $lastTime < $currentTime ) do={
		:set lastTime $currentTime ;
		:set message [/log get [ :pick $currentBuf ($currentLineCount-1) ] message];
	}
}
```

檢測後，新條目會儲存在 `message` 變數中；之後你可以解析此變數以獲取詳細資訊，例如 PPPoE 用戶端的 MAC 地址。

## 允許 NTP 使用 [ntp.org](http://ntp.org) 池服務 {#allow-use-of-ntporg-pool-service-for-ntp}

此指令碼會解析兩個 NTP 伺服器的主機名，將結果與當前 NTP 設定進行比較，如果不同則更改地址。由於 RouterOS 不允許在 NTP 配置中使用主機名，因此需要此指令碼。這裡使用了兩個指令碼。第一個指令碼定義系統變數，供執行實際工作的第二個指令碼使用：

```ros
# 系统配置脚本 - "GlobalVars"

:put "Setting system globals";

# 系统名称
:global SYSname [/system identity get name];

# 接收通知的电子邮件地址
:global SYSsendemail "mail@my.address";

# 发送通知所用的电子邮件地址
:global SYSmyemail "routeros@my.address";

# 要使用的邮件服务器
:global SYSemailserver "1.2.3.4";

# 要使用的 NTP 池（请查看 www.pool.ntp.org）
:global SYSntpa "0.uk.pool.ntp.org";
:global SYSntpb "1.uk.pool.ntp.org";
```

```ros
# 检查并设置 NTP 服务器 - "setntppool"

# 我们需要使用以下全局变量，它们必须在此处定义，即使
# 尽管它们也在我们调用以设置它们的脚本中定义。
:global SYSname;
:global SYSsendemail;
:global SYSmyemail;
:global SYSemailserver;
:global SYSntpa;
:global SYSntpb;

# 使用系统默认值加载全局变量
/system script run GlobalVars

# 解析两个 NTP 池主机名
:local ntpipa [:resolve $SYSntpa];
:local ntpipb [:resolve $SYSntpb];

# 获取当前设置
:local ntpcura [:pick [/system/ntp/client/get servers] 0];
:local ntpcurb [:pick [/system/ntp/client/get servers] 1];

# 定义一个变量，以便我们知道是否有任何更改。
:local bChange 0;

# 调试输出
:put ("Old: " . $ntpcura . " New: " . $ntpipa);
:put ("Old: " . $ntpcurb . " New: " . $ntpipb);

# 如有需要，更改服务器
:if ($ntpipa != $ntpcura || $ntpipb != $ntpcurb) do={
    :put "Changing NTP servers";
    /system/ntp/client/set servers="$ntpipa,$ntpipb";
    :set bChange 1;
    }

# 如果我们做了更改，请发送一封电子邮件告知。
:if (($bChange = 1)) do={
    :put "Sending e-mail.";
    /tool e-mail send \
        to=$SYSsendemail \
        subject=($SYSname . " NTP change") \
        from=$SYSmyemail \
        server=$SYSemailserver \
        body=("Your NTP servers have just been changed:\n\nPrimary:\nOld: " . $ntpcura . "\nNew: " \
          . $ntpipa . "\n\nSecondary\nOld: " . $ntpcurb . "\nNew: " . $ntpipb);
    }
```

排程器條目：

```ros
/system scheduler add \
  comment="Check and set NTP servers" \
  disabled=no \
  interval=12h \
  name=CheckNTPServers \
  on-event=setntppool \
  policy=read,write,test \
  start-date=1970-01-01 \
  start-time=16:00:00
```
