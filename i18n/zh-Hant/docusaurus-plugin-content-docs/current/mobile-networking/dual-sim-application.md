---
sidebar_key: "mobile-networking/dual-sim-application"
sidebar_position: 2
title: "雙 SIM 卡應用"
sidebar_label: "雙 SIM 卡應用"
description: "本頁介紹如何在 MikroTik RouterOS 中為雙 SIM LTE 裝置配置並自動化 SIM 卡切換，包括初始設定步驟、漫遊狀態檢查，以及根據 LTE 連線狀態在歸屬/漫遊網路之間切換的示例指令碼。"
tags:
  - 'ltm'
  - 'scripting'
source: https://manual.mikrotik.com/docs/mobile-networking/dual-sim-application
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 概述 {#summary}

第一個指令碼示例展示了在 LtAP mini 裝置檢測到移動漫遊時如何在 SIM 卡槽之間切換。這對於移動車輛應用可能很有用，例如汽車、公交車或火車可能駛往國外，並且應使用兩張 SIM 卡（一張用於歸屬網路，另一張用於漫遊網路）。由於 RouterOS 在 LTE monitor 中提供漫遊狀態（僅在漫遊時顯示），我們可以在 RouterOS 指令碼中使用它來相應地更換 SIM 卡。

第二個指令碼示例展示了在當前所選 SIM 卡上的移動連線丟失時如何在 SIM 卡之間切換。

**注意：** 請記住，這些只是如何使用雙 SIM 卡槽的示例。對於實際生產環境，應進行充分測試，因此請嘗試根據需求最佳化它們並新增新功能。

### 初始設定 {#initial-settings}

首先，確保已為每張 SIM 卡正確設定 LTE 網路引數（由行動網路運營商提供）。你可以使用預設 APN 配置檔案，也可以建立兩個單獨的配置檔案，請參閱此連結 -  [LTE/5G#Quicksetupexample](./lte-5g.md#quick-setup-example)。本示例使用預設 APN 配置檔案。

然後，使用以下命令啟用資料漫遊，以便連線到其他國家的資料提供商。這樣我們就可以跟蹤漫遊狀態。

```
/interface/lte/set [find name=lte1] allow-roaming=yes

```

然後，選擇哪個 SIM 卡槽用於歸屬網路和漫遊網路。本示例中，我們使用 "down" 卡槽用於歸屬網路，使用 "up" 卡槽用於漫遊網路。某些裝置型號（如 SXT）的 SIM 卡槽名稱為 "a" 和 "b"，而不是 "up" 和 "down"。使用以下命令在活動卡槽之間切換。

### RouterOS v6 版本中的命令 {#command-in-routeros-v6-version}

```
/system/routerboard/modem/set sim-slot=down

```

### RouterOS v7 版本中的命令 {#command-in-routeros-v7-version}

```
/interface/lte/settings/set sim-slot=down

```

更改 SIM 卡槽後，LTE 調變解調器將重啟。完全初始化可能需要一些時間（取決於調變解調器和板卡，大約 30 秒），因此請務必測試調變解調器。

### 漫遊指令碼示例 {#roaming-script-example}

現在建立一個將由排程器執行的指令碼。此指令碼將檢查幾個關鍵點：

- 檢查 LTE 介面是否已初始化（顯示在 `/interface/lte` 中），否則嘗試電源重設。
- 檢查是否已建立 LTE 連線（介面處於 "running" 狀態），否則建立日誌條目並等待下一次排程器執行。
- 讀取當前使用的 LTE 卡槽，並根據漫遊狀態決定是否切換 SIM 卡槽。

我們將此指令碼命名為 "roamingScript"，其原始碼如下：

```
{
# Setup and read current values, "up" SIM slot will be used for roaming, "down" for home network
:global simSlot [/interface/lte/settings/get sim-slot]
:global timeoutLTE 60
:global timeoutConnect 60

# Wait for LTE to initialize for maximum "timeoutLTE" seconds
:local i 0
:local isLTEinit false
:while ($i<$timeoutLTE) do={
    :foreach n in=[/interface/lte/find] do={:set $isLTEinit true}
    :if ($isLTEinit=true) do={
        :set $i $timeoutLTE
    }
    :set $i ($i+1)
    :delay 1s
}

# Check if LTE is initialized, or try power-reset the modem
:if ($isLTEinit=true) do={
    # Wait for LTE interface to connect to mobile network for maximum "timeoutConnect" seconds
    :local isConnected false
    :set $i 0
    :while ($i<$timeoutConnect) do={
        :if ([/interface/lte/get [find name="lte1"] running]=true) do={
            :set $isConnected true
            :set $i $timeoutConnect
        }
        :set $i ($i+1)
        :delay 1s
    }
    # Check if LTE is connected
    if ($isConnected=true) do={
        :local Info [/interface/lte/monitor lte1 once as-value]
        :local isRoaming ($Info->"roaming")
        # Check which SIM slot is used
        :if ($simSlot="down") do={
            # If "down" (home) slot, check roaming status
            :if ($isRoaming=true) do={
                :log info message="Roaming detected, switching to SIM UP (Roaming)"
                /interface/lte/settings/set sim-slot=up
            }
        } else={
            # Else "up" (roaming) slot, check roaming status
            :if (!$isRoaming=true) do={
                :log info message="Not roaming, switching to SIM DOWN (Home)"
                /interface/lte/settings/set sim-slot=down
            }
        }
    } else={
        :log info message="LTE interface did not connect to network, wait for next scheduler"
    }
} else={
    :log info message="LTE modem did not appear, trying power-reset"
    /system/routerboard/usb/power-reset duration=5s
}
}

```

### 故障轉移指令碼示例 {#failover-script-example}

現在建立一個將由排程器執行的指令碼。此指令碼將檢查幾個關鍵點：

- 檢查 LTE 介面是否已初始化（顯示在 `/interface/lte` 中），否則嘗試電源重設。
- 檢查是否已建立 LTE 連線（介面處於 "running" 狀態），否則建立日誌條目並等待下一次排程器執行。
- 讀取當前使用的 LTE 卡槽，並根據介面狀態決定是否切換 SIM 卡槽。

**注意：** 請記住，僅噹噹前 SIM 卡槽無法連線到網路時才會更改 SIM 卡槽。如果需要切回主 SIM 卡，需要排程另一個操作在特定時間執行此操作。如果不切換回另一張 SIM 卡，就無法知道它是否可用。

我們將此指令碼命名為 "failoverScript"，其原始碼如下：

```
{
# Setup and read current values
:global simSlot [/interface/lte/settings/get sim-slot]
:global timeoutLTE 60
:global timeoutConnect 60

# Wait for LTE to initialize for maximum "timeoutLTE" seconds
:local i 0
:local isLTEinit false
:while ($i<$timeoutLTE) do={
    :foreach n in=[/interface/lte/find] do={:set $isLTEinit true}
    :if ($isLTEinit=true) do={
        :set $i $timeoutLTE
    }
    :set $i ($i+1)
    :delay 1s
}

# Check if LTE is initialized, or try power-reset the modem
:if ($isLTEinit=true) do={
    # Wait for LTE interface to connect to mobile network for maximum "timeoutConnect" seconds
    :local isConnected false
    :set $i 0
    :while ($i<$timeoutConnect) do={
        :if ([/interface/lte/get [find name="lte1"] running]=true) do={
            :set $isConnected true
            :set $i $timeoutConnect
        }
        :set $i ($i+1)
        :delay 1s
    }
    # Check if LTE is connected
    if ($isConnected=false) do={
    # Check which SIM slot is used
        :if ($simSlot="down") do={
            # If "down" slot, switch to up
        :log info message="LTE down, switching slot to UP"
            /interface/lte/settings/set sim-slot=up
    }
        :if ($simSlot="up") do={
            # If "up" slot, switch to down
        :log info message="LTE down, switching slot to DOWN"
            /interface/lte/settings/set sim-slot=down
            }
        } else={
            # Else "running"
            :if ($isConnected=true) do={
                :log info message="LTE UP"
            } else={
        :log info message="LTE interface did not connect to network, wait for next scheduler"
        }
    } 
    } else={
    :log info message="LTE modem did not appear, trying power-reset"
    /system/routerboard/usb/power-reset duration=5s
}
}
```

### 設定排程器 {#setting-up-scheduler}

最後，建立排程器來執行之前建立的指令碼。選擇合適的排程器間隔，以免兩個或更多事件相互重疊。對於上面的示例，3 分鐘就足夠了。

```
/system/scheduler/add interval=3m on-event=roamingScript name=Roaming

```

```
/system/scheduler/add interval=3m on-event=failoverScript name=Failover

```

請注意，“home” SIM 卡會消耗一些漫遊資料，因為切換 SIM 卡槽不會立即完成。
