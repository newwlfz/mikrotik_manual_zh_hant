---
sidebar_key: "system-information-and-utilities/device-mode"
sidebar_position: 2
title: "裝置模式"
sidebar_label: "裝置模式"
description: "device-mode 功能會限制路由器訪問並限制配置選項以增強安全性，可根據裝置型別和 RouterOS 版本在 advanced、home、basic 或 ros 模式下使用。更改需要透過斷電重啟或按鍵進行物理確認，並且更新嘗試次數有限，以防止未經授權的模式更改。"
tags:
  - 'device-mode'
source: https://manual.mikrotik.com/docs/7.25/system-information-and-utilities/device-mode
captured_at: '2026-11-04T11:21:56+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**device-mode** 是一項功能，用於對裝置設定特定限制，或限制對特定配置選項的訪問。它有助於保護您的路由器和網路，防止攻擊者獲得未授權訪問並將其用作攻擊其他網路的閘道器。

可用的 device-mode 為 `advanced`、`home`、`basic` 和 `rose`。device-mode 配置在路由器上出廠預裝（適用於搭載 RouterOS v7.17 或更高版本的裝置）。`advanced`（以前稱為 `enterprise`）模式配置用於 CCR 和 1100 系列裝置，`home` 模式配置用於家用路由器，`basic` 模式配置用於任何其他型別的裝置。對於執行 RouterOS 7.17 之前版本的裝置，所有裝置都使用 *advanced/enterprise* 模式。

device-mode 從 [`/system/device-mode`](../cli-reference/system/device-mode/index.md) 選單進行配置。

```ros
[admin@MikroTik] > /system/device-mode/print 
                 mode: advanced     
     allowed-versions: 7.13+,6.49.8+
              flagged: no           
     flagging-enabled: yes          
            scheduler: yes          
                socks: yes          
                fetch: yes          
                 pptp: yes          
                 l2tp: yes          
       bandwidth-test: yes          
          traffic-gen: no           
              sniffer: yes          
                ipsec: yes          
                romon: yes          
                proxy: yes          
              hotspot: yes          
                  smb: yes          
                email: yes          
             zerotier: yes          
            container: no           
  install-any-version: no           
           partitions: no           
          routerboard: yes          
        attempt-count: 0   
```

device-mode 引數可以由已授權的 RouterOS 使用者更改，但需要物理接觸裝置才能批准更改。
更改 device-mode 後，你需要透過按下裝置本身的按鈕來確認，或執行“冷重啟”——即拔掉電源。更改被確認後，無論採用哪種確認方式，**裝置都會重啟**。

## 在 WinBox 中檢查裝置模式 {#check-device-mode-in-winbox}

開啟 **System > Device Mode** 以檢視限制：

1. **Mode** 和 **Allowed Versions** 標識已配置的模式和允許的 RouterOS 版本。
2. 各工具欄位顯示允許執行哪些操作。例如，當 **Scheduler**、**Fetch** 或 **Email** 其中之一報告 device-mode 限制時，檢查對應項。

![WinBox Device Mode overview with the current mode and per-tool restrictions](/img/8bc9340a46cf09de.webp)

該截圖顯示的是此路由器現有的 `rose` 配置；它並非每臺裝置的出廠預設值。此概覽為只讀。**Update** 操作會啟動模式更改流程，該流程需要物理確認，並會如下一節所述重啟裝置。

## 更改 device-mode {#changing-device-mode}

可用模式或特定功能可以透過 [`update`](../cli-reference/system/device-mode/update.md) 命令更改。

例如，將模式更改為 `home`：

```ros
[admin@MikroTik] > /system/device-mode/update mode=home 
  update: please activate by turning power off or pressing reset or mode button 
          in 5m00s
-- [Q quit|D dump|C-z pause]
```

如果在指定時間內未執行斷電或按下按鈕，模式更改將被取消。如果並行運行了另一個 update 命令，兩者都會被取消。

:::danger
有若干 EOL 產品無法透過按下復位按鈕來確認模式更改。這些路由器只能透過斷電重啟來確認模式更改。
:::

為了保護裝置免受這樣的攻擊者侵害——他們可能悄無聲息地獲得對路由器的訪問權、用一些指令碼加以濫用，然後只是等著你重啟路由器，而你甚至不知道自己當時正在接受某個入侵者請求的更改——你只能更新模式三次。有一個計數器會跟蹤已進行了多少次更新嘗試，並會阻止任何進一步的更新。此計數器只有在管理員斷電重啟，或在看到模式設定更新嘗試的警告時按下按鈕（與接受任何更新時相同）才會被重設。

```ros
[admin@MikroTik] > /system/device-mode/update container=yes 
  update: too many unsuccessful attempts, turn off power or reboot by pressing reset or mode button in 4m55s to reset attempt-count
```

如果 update 命令指定了任何模式引數，則該更新會替換整個 device-mode 配置。在這種情況下，除該命令中指定的設定外，所有按功能單獨配置的設定都將丟失。例如：

```ros
[admin@MikroTik] > /system/device-mode/update mode=home email=yes fetch=yes
[admin@MikroTik] > /system/device-mode/print config
   mode: home
  fetch: yes
  email: yes
[admin@MikroTik] > /system/device-mode/update mode=advanced sniffer=no
-- reboot --
[admin@MikroTik] > /system/device-mode/print config
     mode: advanced
  sniffer: no

```

可以看到 `fetch` = yes 和 `email` = yes 都不見了，因為它們被模式更改覆蓋了。然而，只指定按功能單獨配置的設定則只會更改這些設定：

```ros
[admin@MikroTik] > /system/device-mode/update hotspot=no
-- reboot --
[admin@MikroTik] > /system/device-mode/print config
     mode: advanced
  sniffer: no
  hotspot: no
```

如果該功能已停用，互動式命令會顯示錯誤訊息：

```ros
[admin@MikroTik] > /system/device-mode/print config
     mode: advanced
  sniffer: no
  hotspot: no
[admin@MikroTik] > /tool/sniffer/quick 
failure: not allowed by device-mode
```

不過，仍然可以向被停用的功能新增配置，但 device-mode 中會出現一段註釋，標明該功能已被停用：

```ros
[admin@MikroTik] > /ip/hotspot/add interface=ether1 
[admin@MikroTik] > /ip/hotspot/print 
Flags: X, S - HTTPS
Columns: NAME, INTERFACE, PROFILE, IDLE-TIMEOUT
#   NAME      INTERFACE  PROFILE  IDLE-TIMEOUT
;;; inactivated, not allowed by device-mode
0 X hotspot1  ether1     default  5m          
```

## 使用 Netinstall 或 FlashFig 更改 device-mode 設定 {#changing-device-mode-settings-using-netinstall-or-flashfig}

從 RouterOS 7.22 開始，可以配置 **device-mode** 和 **protected-routerboot** 以及其他設定。

有關更多資訊，請參閱 [網路安裝](../getting-started/installation-and-upgrade/netinstall/index.md) 和 [FlashFig](../management-tools/flashfig.md) 文件。

## 可用的 device-mode 模式 {#available-device-mode-modes}

有四種可供配置的裝置模式（*advanced* 是預設值），每種模式都有一組在使用時不被允許的功能。沒有任何模式會啟用所有功能——即使啟用了 *advanced* 模式，某些功能也需要手動啟用。ROSE device-mode 與 advanced 模式非常相似，但它是為 RDS 及類似裝置而設計的，具有更廣泛的磁碟使用選項，出廠即支援容器安裝。有關每個功能控制內容的更多細節，請參見下表。如下表所示，**traffic-gen**、**container**、**partitions** 和 **routerboard** 功能始終處於停用狀態，除非由管理員使用者專門啟用。

| 功能 / 屬性 | 操作/不可用的選單 | Home | Basic | Advanced | ROSE |
| :-- | :-- | :-- | :-- | :-- |  :-- |
| [頻寬測試](../diagnostics-monitoring-and-troubleshooting/bandwidth-test.md) | `/tool/bandwidth-test`、`/tool/bandwidth-server`、`/tool/speed-test` | no | no | yes | yes |
| [**Containers**](../containers/index.md) | 所有容器功能。 | no | no | no | yes |
| [電子郵件](./e-mail.md) | `/tool/e-mail` | no | yes | yes | yes |
| [獲取](./fetch.md) | `/tool/fetch` | no | yes | yes | yes |
| [**Hotspot**](../authentication-authorization-accounting/hotspot-captive-portal/index.md) | `/ip/hotspot` | no | no | yes | yes |
| **Install Any Version** | RouterOS 將不再允許安裝低於 **allowed-versions** 列表中的版本。 | no | no | no | no |
| [**IPsec**](../virtual-private-networks/ipsec/index.md) | `/ip/ipsec` | yes | yes | yes | yes |
| [**L2TP**](../virtual-private-networks/l2tp/index.md) | `/interface/l2tp-server`、`/interface/l2tp-client` | yes | yes | yes | yes |
| [分割區](./partitions.md) | `/partitions` —— 不允許更改分割區數量。如果你的路由器無法啟動，它仍然能夠引導進入你的其他分割區。崩潰恢復不受限制。 | no | no | no | no |
| [**PPTP**](../virtual-private-networks/pptp.md) | `/interface/pptp-server`、`/interface/pptp-client` | yes | yes | yes | yes |
| [Web 代理](../network-management/proxy/web-proxy.md) | `/ip/proxy` | no | no | yes | yes |
| [**RoMon**](../management-tools/romon.md) | `/tool/romon` | no | yes | yes | yes |
| [路由器主機板](../hardware/routerboard.md) | `/system/routerboard/settings`（自動升級選項除外） | no | no | no | no |
| [排程器](./scheduler.md) | `/system/scheduler` | no | yes | yes | yes |
| [**SMB**](../storage/smb.md) | `/ip/smb` | yes | yes | yes | yes |
| [封包嗅探器](../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) | `/tool/sniffer` | no | yes | yes | yes |
| [**SOCKS Proxy**](../network-management/socks/index.md) | `/ip/socks` | no | no | yes | yes |
| [流量生成器](../diagnostics-monitoring-and-troubleshooting/traffic-generator.md) | `/tool/traffic-generator`、`/tool/flood-ping`、`/tool/ping-speed` | no | no | no | no |
| [**ZeroTier**](../virtual-private-networks/zerotier.md) | `/zerotier` | no | no | yes | yes |

可以對可用功能進行更具體的控制。device-mode 控制的每個功能都可以專門開啟或關閉。

例如，**scheduler** 將不允許在 `/system/scheduler` 中執行任何操作。所使用的 device-mode 會停用所有列出的功能；例如，如果使用了 **mode**=home，但你的部署需要 **zerotier**，則需要執行 device-mode 更新 `/system/device-mode/update` zerotier=yes，並需物理接觸裝置以按下按鈕或切斷電源。

## 允許的版本 {#allowed-versions}

裝置模式在其引數中列出了一個名為 **allowed-versions** 的引數。這是 MikroTik 認為安全、且不包含任何可被攻擊者利用的嚴重漏洞的版本列表。

此設定不依賴於已安裝的 RouterOS 版本，而是作為單獨的保護層發揮作用，防止攻擊者一步步降級版本，以到達已知存在漏洞的 RouterOS 發行版。當你將 RouterOS 升級到提供更新 **allowed-versions** 列表的發行版時，最舊的列表將被覆蓋。如果你降級 RouterOS，**allowed-versions** 列表不會改變，並會保持更新到最新的列表。如果啟用了 device-mode 的 **install-any-version**，則該列表會被忽略。

## Flagged 狀態 {#flagged-status}

與 device-mode 功能一同，RouterOS 可以在系統啟動時分析整個配置，以判斷是否存在對路由器未經授權訪問的跡象。如果檢測到可疑配置，它將被停用，**flagged** 引數將被設定為 *yes*。此時裝置處於標記狀態，並會強制執行某些限制。

```ros
[admin@MikroTik] > /system/device-mode/print 
     mode: advanced
  flagged: yes
...
```

如果系統具有此 flagged 狀態，當前配置可以工作，但無法執行以下操作：

- bandwidth-test、traffic-generator 和 sniffer
- 以下專案的啟用或建立新條目的配置操作（仍然可以停用或刪除它們）：system scheduler、SOCKS proxy、PPTP、L2TP、IPsec、proxy 和 SMB。

當路由器處於 flagged 狀態時執行上述操作，您將收到錯誤訊息：

```ros
[admin@MikroTik] > /tool/sniffer/quick 
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
[admin@MikroTik] > /int l2tp-client/add connect-to=1.1.1.1 user=user
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
```

要退出標記狀態，你必須執行命令 `/system/device-mode/update flagged=no`。系統會要求你按下按鈕，或執行硬重啟（物理斷電，或對虛擬機器執行硬重啟）。

**重要！** 儘管系統已停用了觸發標記狀態的那些看起來惡意的規則，但在退出標記狀態之前，務必檢查你所有的配置中是否有其他未知內容。如果你的系統已被標記，請假定系統已遭入侵，並在重新啟用系統供使用之前對所有設定進行全面審計。完成審計後，更改所有系統密碼並升級到最新的 RouterOS 版本。

:::warning
從 RouterOS 7.17 版本開始，device-mode 會限制雙啟動裝置的 SwOS/RouterOS 切換。要啟用它：`/system/device-mode/update` routerboard=yes
:::
