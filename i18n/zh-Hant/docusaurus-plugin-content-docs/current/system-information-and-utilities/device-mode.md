---
sidebar_key: "system-information-and-utilities/device-mode"
sidebar_position: 2
title: "裝置模式"
sidebar_label: "裝置模式"
description: "Device-mode 限制 RouterOS 功能以保護路由器免遭濫用；更改它需要物理確認。涵蓋各種模式、按功能劃分的開關、允許的版本以及被標記的狀態。"
tags:
  - 'device-mode'
source: https://manual.mikrotik.com/docs/system-information-and-utilities/device-mode
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**device-mode** 限制對特定配置選項的訪問。它保護路由器和網路，防止獲得未授權訪問的攻擊者將裝置用作攻擊其他網路的閘道器。

可用模式為 `advanced`、`home`、`basic` 和 `rose`。新裝置出廠時已配置模式：CCR 和 1100 系列裝置為 `advanced`（原為 `enterprise`），家用路由器為 `home`，其他裝置為 `basic`。在出廠模式引入之前生產的裝置使用 `advanced`，升級 RouterOS 會保持該模式。

在 [`/system/device-mode`](../cli-reference/system/device-mode/index.md) 選單中檢視當前設定。

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
          routerboard: no          
        attempt-count: 0   
```

授權使用者可以更改 device-mode 引數，但需要物理接觸才能批准更改。使用裝置上的 reset 或 mode 按鈕確認，或透過“冷重啟”——拔掉電源——來確認。普通重啟不會確認更改，而是會取消更改。確認後，無論採用哪種方法，**裝置都會重啟**。

## 在 WinBox 中檢查裝置模式 {#check-device-mode-in-winbox}

開啟 **System > Device Mode** 以檢視限制：

1. **Mode** 和 **Allowed Versions** 標識已配置的模式和允許的 RouterOS 版本。
2. 各工具欄位顯示允許執行哪些操作。例如，當 **Scheduler**、**Fetch** 或 **Email** 其中之一報告 device-mode 限制時，檢查對應項。

![WinBox Device Mode overview with the current mode and per-tool restrictions](/img/8bc9340a46cf09de.webp)

截圖顯示的是具有現有 `rose` 配置的路由器；這不是出廠預設配置。概覽為只讀。**Update** 操作會啟動模式更改，這需要物理確認並會重啟裝置（見下一節）。

## 更改 device-mode {#change-device-mode}

使用 [`update`](../cli-reference/system/device-mode/update.md) 命令更改模式或單個功能。

將模式更改為 `home`：

```ros
[admin@MikroTik] > /system/device-mode/update mode=home
  update: turn off power or reboot by pressing reset or mode button in 5m to activate changes
```

如果更新未及時確認，模式變更將被取消。要自行取消待處理的更新，請執行不帶引數的 `/system/device-mode/update`；它會報告 `canceled previous update`。當另一個更新待處理時，帶引數的 `update` 會取消該待處理更新，並且自身不會被應用；請再次執行它以啟動新的更新。

:::note
某些 EOL 產品僅透過斷電重啟來確認模式更改，而不是透過按下按鈕。
:::

擁有訪問許可權的攻擊者可以準備 device-mode 變更並使其保持待處理狀態。該變更會在下次按下按鈕或電源迴圈時啟用，即使管理員並不知道它是什麼。為限制該風險，在沒有重設的情況下只允許三次更新嘗試。每個帶引數的 `update` 請求都會遞增 **attempt-count** 計數器，包括被拒絕的請求；取消待處理更新的請求不會遞增。當計數器達到 3 時，後續請求會被拒絕，並開啟一個等於該請求 `activation-timeout` 的重設視窗。計數器在確認更新後重設，或在重設視窗內按下按鈕或電源迴圈後重設。過期請求和普通重啟不會重設它。

```ros
[admin@MikroTik] > /system/device-mode/update container=yes 
  update: too many unsuccessful attempts, turn off power or reboot by pressing reset or mode button in 5m to reset attempt-count
```

指定 `mode` 的命令會替換整個 device-mode 配置：除同一命令中給出的設定外，所有按功能設定都會丟失。`print config` 輸出只顯示與模式預設值不同的設定。

```ros
[admin@MikroTik] > /system/device-mode/update mode=home email=yes fetch=yes
  update: turn off power or reboot by pressing reset or mode button in 5m to activate changes
-- reboot --
[admin@MikroTik] > /system/device-mode/print config
              mode: home
  allowed-versions: 7.13+,6.49.8+
             fetch: yes
             email: yes
[admin@MikroTik] > /system/device-mode/update mode=advanced sniffer=no
  update: turn off power or reboot by pressing reset or mode button in 5m to activate changes
-- reboot --
[admin@MikroTik] > /system/device-mode/print config
              mode: advanced
  allowed-versions: 7.13+,6.49.8+
           sniffer: no
```

`fetch` 和 `email` 覆蓋項已不存在，因為第二次模式變更替換了它們。僅指定按功能設定的命令只會更改這些設定：

```ros
[admin@MikroTik] > /system/device-mode/update hotspot=no
  update: turn off power or reboot by pressing reset or mode button in 5m to activate changes
-- reboot --
[admin@MikroTik] > /system/device-mode/print config
              mode: advanced
  allowed-versions: 7.13+,6.49.8+
           sniffer: no
           hotspot: no
```

已停用的功能會拒絕互動式命令：

```ros
[admin@MikroTik] > /system/device-mode/print config
              mode: advanced
  allowed-versions: 7.13+,6.49.8+
           sniffer: no
           hotspot: no
[admin@MikroTik] > /tool/sniffer/quick 
failure: not allowed by device-mode
```

仍可為已停用的功能新增配置；該條目會以停用狀態建立，並帶有註釋說明 device-mode 不允許它：

```ros
[admin@MikroTik] > /ip/hotspot/add interface=ether1 
[admin@MikroTik] > /ip/hotspot/print 
Flags: X - DISABLED
Columns: NAME, INTERFACE, PROFILE, IDLE-TIMEOUT
#   NAME      INTERFACE  PROFILE  IDLE-TIMEOUT
;;; inactivated, not allowed by device-mode
0 X hotspot1  ether1     default  5m          
```

## 使用 Netinstall 或 FlashFig 配置 device-mode {#configure-device-mode-with-netinstall-or-flashfig}

Netinstall 和 FlashFig 可以在預配裝置時設定 **device-mode**、**protected-routerboot** 和其他設定。

詳情請參閱 [網路安裝](../getting-started/installation-and-upgrade/netinstall/index.md) 和 [FlashFig](../management-tools/flashfig.md) 文件。

## 可用的 device-mode 模式 {#available-device-mode-modes}

有四種模式可用（`advanced` 是預設模式）；每種模式都會停用一部分功能。沒有任何模式會啟用所有功能——即使在 `advanced` 模式下，某些功能也必須顯式啟用。`rose` 與 `advanced` 類似，面向 RDS 以及具有廣泛磁碟用途和出廠容器支援的類似裝置。下表列出了每項功能控制的內容。**traffic-gen**、**container**、**partitions** 和 **routerboard** 在每種模式下都會被停用，除非顯式啟用。

| 功能 / 屬性 | 操作/不可用選單 | Home | Basic | Advanced | ROSE |
| :-- | :-- | :-- | :-- | :-- |  :-- |
| [**頻寬測試**](../diagnostics-monitoring-and-troubleshooting/bandwidth-test.md) | `/tool/bandwidth-test`, `/tool/bandwidth-server`, `/tool/speed-test` | no | no | yes | yes |
| [**容器**](../containers/index.md) | 所有容器功能。 | no | no | no | yes |
| [**電子郵件**](./e-mail.md) | `/tool/e-mail` | no | yes | yes | yes |
| [**獲取**](./fetch.md) | `/tool/fetch` | no | yes | yes | yes |
| [**熱點**](../authentication-authorization-accounting/hotspot-captive-portal/index.md) | `/ip/hotspot` | no | no | yes | yes |
| **安裝任意版本** | RouterOS 將不再允許安裝 **allowed-versions** 列表之外的版本。 | no | no | no | no |
| [**IPsec**](../virtual-private-networks/ipsec/index.md) | `/ip/ipsec` | yes | yes | yes | yes |
| [**L2TP**](../virtual-private-networks/l2tp/index.md) | `/interface/l2tp-server`, `/interface/l2tp-client` | yes | yes | yes | yes |
| [**分割區**](./partitions.md) | `/partitions` — 不允許更改分割區數量。如果你的路由器無法啟動，它仍然能夠啟動到你的其他分割區。崩潰恢復沒有限制。 | no | no | no | no |
| [**PPTP**](../virtual-private-networks/pptp.md) | `/interface/pptp-server`, `/interface/pptp-client` | yes | yes | yes | yes |
| [**代理**](../network-management/proxy/web-proxy.md) | `/ip/proxy` | no | no | yes | yes |
| [**RoMon**](../management-tools/romon.md) | `/tool/romon` | no | yes | yes | yes |
| [**Routerboard 設定**](../hardware/routerboard.md) | `/system/routerboard/settings`（自動升級選項除外） | no | no | no | no |
| [**排程器**](./scheduler.md) | `/system/scheduler` | no | yes | yes | yes |
| [**SMB**](../storage/smb.md) | `/ip/smb` | yes | yes | yes | yes |
| [**嗅探器**](../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) | `/tool/sniffer` | no | yes | yes | yes |
| [**SOCKS 代理**](../network-management/socks/index.md) | `/ip/socks` | no | no | yes | yes |
| [**流量生成器**](../diagnostics-monitoring-and-troubleshooting/traffic-generator.md) | `/tool/traffic-generator`, `/tool/flood-ping`, `/tool/ping-speed` | no | no | no | no |
| [**ZeroTier**](../virtual-private-networks/zerotier.md) | `/zerotier` | no | no | yes | yes |

由 device-mode 控制的每項功能都可以單獨啟用或停用。

例如，停用 **scheduler** 後，`/system/scheduler` 無法執行任何操作。如果裝置執行在 `home` 模式下，但你的設定需要 `zerotier`，請執行 `/system/device-mode/update zerotier=yes`，並透過物理訪問裝置來確認。在雙啟動裝置上，device-mode 會限制 SwOS/RouterOS 切換；請使用 `/system/device-mode/update routerboard=yes` 啟用它。

## 允許的版本 {#allowed-versions}

**allowed-versions** 引數列出了 MikroTik 認為安全、沒有攻擊者可利用的嚴重漏洞的 RouterOS 版本。

該列表作為獨立的保護層發揮作用，與已安裝版本無關，用於防止攻擊者逐步降級到已知存在漏洞的版本。升級到帶有較新 **allowed-versions** 列表的版本會覆蓋舊列表；降級則不會更改該列表。啟用 **install-any-version** 時，該列表會被忽略。

## Flagged 狀態 {#flagged-status}

RouterOS 在啟動時會分析整個配置，以查詢未經授權訪問的跡象。如果發現可疑配置，裝置會將其停用，並將 **flagged** 設定為 *yes*，從而強制執行額外的限制。

```ros
[admin@MikroTik] > /system/device-mode/print 
     mode: advanced
  flagged: yes
...
```

在 flagged 狀態下，當前配置會繼續工作，但無法執行以下操作：

- bandwidth-test、traffic-generator 和 sniffer
- 在 system scheduler、SOCKS proxy、PPTP、L2TP、IPsec、proxy 和 SMB 中啟用或建立條目的配置操作（停用或刪除它們仍然有效）。

嘗試執行這些操作會返回錯誤：

```ros
[admin@MikroTik] > /tool/sniffer/quick 
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
[admin@MikroTik] > /interface/l2tp-client/add connect-to=192.0.2.1 user=user1
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
```

要退出 flagged 狀態，請執行 `/system/device-mode/update flagged=no`，並透過按下按鈕或斷電重啟來確認：切斷電源，或對虛擬機器執行硬重啟。

:::danger
儘管系統已停用任何觸發了被標記狀態的看似惡意規則，在退出被標記狀態之前，請檢查所有配置中是否存在其他未知條目。如果系統已被標記，請假定它已遭入侵，並在重新啟用前審計所有設定。審計後，更改所有系統密碼並升級到最新 RouterOS 版本。
:::
