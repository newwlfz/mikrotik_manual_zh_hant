---
sidebar_key: "system-information-and-utilities/device-mode"
sidebar_position: 2
title: "裝置模式"
sidebar_label: "裝置模式"
description: "device-mode 功能會限制路由器訪問並限制配置選項以增強安全性，可根據裝置型別和 RouterOS 版本在 advanced、home、basic 或 ros 模式下使用。更改需要透過斷電重啟或按鍵進行物理確認，並且更新嘗試次數有限，以防止未經授權的模式更改。"
tags:
  - 'device-mode'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/device-mode
captured_at: '2026-11-04T11:33:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 描述 {#description}

**device-mode** 是一項功能，用於對裝置設定特定限制，或限制對特定配置選項的訪問。它有助於保護您的路由器和網路，防止攻擊者獲得未授權訪問並將其用作攻擊其他網路的閘道器。

可用的 device-mode 有 *advanced*、*home*、*basic* 和 *ros*。device-mode 配置在路由器上出廠預裝（適用於執行 MikroTik RouterOS v7.17 或更高版本的裝置）。*Advanced（以前稱為 enterprise）* 模式為 CCR 和 1100 系列裝置配置，*home* 模式為家庭路由器配置，basic 模式為任何其他型別的裝置配置。對於執行 RouterOS 7.17 之前版本的裝置，所有裝置都使用 *advanced/enterprise* 模式。

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

device-mode 可由授權的 RouterOS 使用者更改，但更改它需要物理接觸裝置。更改 device-mode 後，您需要透過按下裝置本身的按鈕來確認，或執行“冷重啟”——即拔掉電源。確認更改後，無論採用哪種確認方式，**裝置都將重啟**！

## 更改 device-mode 的模式 {#changing-mode-of-device-mode}

```ros
[admin@MikroTik] > /system/device-mode/update mode=home 
  update: please activate by turning power off or pressing reset or mode button 
          in 5m00s
-- [Q quit|D dump|C-z pause]
```

如果在指定時間內未執行斷電或按下按鈕，模式更改將被取消。如果並行運行了另一個 update 命令，兩者都會被取消。

:::danger
有若干 EOL 產品不會透過按下復位按鈕來“確認”模式更改。這些路由器只能透過斷電重啟來確認模式更改。
:::

為了保護裝置免受攻擊者侵害——攻擊者可能悄悄獲得對您路由器的訪問許可權，用某些指令碼濫用它，並只是試圖等到您重啟路由器，甚至不知道當時您正在接受某個入侵者請求的更改——您只能“update”模式三次。有一個計數器會統計進行了多少次更新嘗試，並且不允許再進行任何更新。只有管理員對路由器執行斷電重啟，或在看到模式設定更新嘗試中出現此類警告時按下按鈕（與接受任何更新時相同），該計數器才能被重設。

## 使用 Netinstall 或 FlashFig 更改 device-mode 設定 {#changing-device-mode-settings-using-netinstall-or-flashfig}

從 RouterOS 7.22 開始，可以配置 **device‑mode**、**protected‑routerboot** 以及其他設定。

有關更多資訊，請參閱 [網路安裝](../getting-started/installation-and-upgrade/netinstall/index.md) 和 [FlashFig](../management-tools/flashfig.md) 文件。

## 啟用 device-mode 功能 {#enabling-device-mode-feature}

```ros
[admin@MikroTik] > /system/device-mode/update container=yes 
  update: too many unsuccessful attempts, turn off power or reboot by pressing reset or mode button in 4m55s to reset attempt-count
```

以下命令可在 /**system/device-mode** 選單中使用：

| 屬性 | 描述 |
| :-- | :-- |
| get | 返回一個值，您可以將其賦給變數或顯示在螢幕上。 |
| print | 顯示活動模式及其屬性。 |
| update | 將更改應用到指定屬性，見下文。 |

## 可用的 device-mode 模式 {#available-device-mode-modes}

有四種可用於配置的裝置模式（mode=advanced 是預設模式），每種模式都有一組在使用時不允許的功能。請注意，沒有一種模式會啟用所有功能。即使您啟用了“advanced”模式，某些功能也需要啟用。ROSE device-mode 與 advanced 模式非常相似，但它是為 RDS 及類似裝置而設計的，這些裝置具有更廣泛的使用磁碟選項，因此從出廠起就支援容器安裝。有關每個選項含義的更多詳細資訊，請參閱“功能說明”一節。因此，從下表可以看出，“traffic-gen、container、partitions、routerboard”功能始終處於停用狀態，除非管理員使用者明確啟用。

| **功能 / 屬性** | **Home** | **Basic** | **Advanced** | **ROSE** |
| :-- | :-- | :-- | :-- | :-- |
| **頻寬測試** (/tool/bandwidth-test) | no | no | yes | yes |
| **容器** (/container) | no | no | no | yes |
| **電子郵件** (/tool/e-mail) | no | yes | yes | yes |
| **Fetch** (/tool/fetch) | no | yes | yes | yes |
| **熱點** (/ip/hotspot) | no | no | yes | yes |
| **安裝任意版本** (`install-any-version`) | no | no | no | no |
| **IPsec** (/ip/ipsec) | yes | yes | yes | yes |
| **L2TP** (/interface/l2tp) | yes | yes | yes | yes |
| **分割區** (/`partitions`) | no | no | no | no |
| **PPTP** (/interface/pptp) | yes | yes | yes | yes |
| **代理** (/ip/proxy) | no | no | yes | yes |
| **RoMon** (/tool/romon) | no | yes | yes | yes |
| **Routerboard 設定** (/system/routerboard) | no | no | no | no |
| **計劃任務** (`scheduler`) | no | yes | yes | yes |
| **SMB** (/ip/smb) | yes | yes | yes | yes |
| **嗅探器** (/tool/sniffer) | no | yes | yes | yes |
| **SOCKS 代理** (/ip/socks) | no | no | yes | yes |
| **流量生成器** (/tool/traffic-gen) | no | no | no | no |
| **ZeroTier** (`zerotier`) | no | no | yes | yes |

## 可用屬性列表 {#list-of-available-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **scheduler, socks, fetch, pptp, l2tp, bandwidth-test, traffic-gen, sniffer, ipsec, romon, proxy, hotspot, smb, email, zerotier, container, install-any-version****, partitions, routerboard** (*yes \| no*) | 可用功能列表，可透過 **device-mode** 選項控制。有關每個選項含義的更多詳細資訊，請參閱“功能說明”一節。 |
| **activation-timeout** (default: **5m**); | 復位按鈕或斷電啟用超時可在 00:00:10 .. 1d00:00:00 範圍內設定。如果在此間隔內未按下復位按鈕（或未執行冷重啟），更新將被取消。 |
| **flagging-enabled** (*yes \| no*; Default: **yes**) | 裝置將執行配置分析，如果發現可疑程式碼的痕跡，將觸發 flagged 模式，設定 **flagged=yes**，啟用 **flagged=yes** 中描述的限制。請參閱“[Flagged 狀態](./device-mode.md#flagged-status)”段落。 |
| **flagged** (*yes \| no*; Default: **no**) | RouterOS 採用各種機制來檢測對其系統檔案的篡改。如果系統檢測到對 RouterOS 的未授權訪問，則狀態“flagged”會設定為 yes。如果“flagged”設定為 yes，為了您的安全，會實施某些限制。有關更多資訊，請參閱下面的章節。 |
| **mode:** (basic, home, advanced, ros; default: **advanced**); | 允許從可用模式中選擇，這些模式將限制裝置功能。預設情況下，**advanced** 模式允許除 **traffic-gen、container、partitions、** **install-any-version****、routerboard** 之外的選項。因此，要使用這些功能，您需要透過執行 device-mode 更新來啟用它。預設情況下，**home** 模式停用以下功能：**scheduler、socks、fetch、bandwidth-test、traffic-gen、sniffer、romon、proxy、hotspot、email、zerotier、container、** **install-any-version****、partitions、routerboard。** |

可以對可用功能進行更具體的控制。device-mode 控制的每個功能都可以專門開啟或關閉。

例如 **scheduler** 將不允許在 `/system/scheduler` 中執行任何操作。所使用的 device-mode 會停用所有列出的功能，例如，如果使用 **mode**=home，但您的設定需要 **zerotier**，則需要透過物理接觸裝置來按下按鈕或切斷電源，以執行 device-mode 更新 `/system/device-mode/update` zerotier=yes。

#### 更改 device-mode 的高階示例 {#advanced-example-of-changing-device-mode}

```ros
[admin@MikroTik] > /system/device-mode/update mode=home email=yes
[admin@MikroTik] > /system/device-mode/update mode=advanced zerotier=no
```

如果 update 命令指定了任何模式引數，此更新將替換整個 device-mode 配置。在這種情況下，除本命令指定的設定外，所有“按功能”設定都將丟失。例如：

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

我們看到 fetch = yes 和 email = yes 缺失了，因為它們被模式更改覆蓋了。但是，僅指定“按功能”設定只會更改那些設定：

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

但是，可以將配置新增到已停用的功能，但在 device-mode 中會有一條註釋顯示該功能已停用：

```ros
[admin@MikroTik] > /ip/hotspot/add interface=ether1 
[admin@MikroTik] > /ip/hotspot/print 
Flags: X, S - HTTPS
Columns: NAME, INTERFACE, PROFILE, IDLE-TIMEOUT
#   NAME      INTERFACE  PROFILE  IDLE-TIMEOUT
;;; inactivated, not allowed by device-mode
0 X hotspot1  ether1     default  5m          
```

## 功能說明 {#feature-clarification}

| 功能 | 哪些選單會變得不可更改的說明 |
| :-- | :-- |
| [bandwidth-test](../diagnostics-monitoring-and-troubleshooting/bandwidth-test.md) | <em><code>/tool/bandwidth-test</code></em><em><code>/tool/bandwidth-server</code></em><br/><em><code>/tool/speed-test</code></em> |
| [routerboard](../hardware/routerboard.md) | *`/system/routerboard/settings`*（自動升級選項除外） |
| [container](../containers/index.md) | 所有容器功能 |
| install-any-version | RouterOS 將不再允許您安裝低於“allowed-versions”屬性下列出的版本的 RouterOS 版本。 |
| [email](./e-mail.md) | *`/tool/e-mail`* |
| [fetch](./fetch.md) | *`/tool/fetch`* |
| [hotspot](../authentication-authorization-accounting/hotspot-captive-portal/index.md) | *`/ip/hotspot`* |
| [ipsec](../virtual-private-networks/ipsec/index.md) | *`/ip/ipsec`* |
| [l2tp](../virtual-private-networks/l2tp/index.md) | <em><code>/interface/l2tp-server</code></em><br/><em><code>/interface/l2tp-client</code></em> |
| [partitions](./partitions.md) | */partitions* 不允許更改分割區數量。如果您的路由器無法啟動，它仍然能夠啟動到其他分割區。崩潰恢復沒有限制。 |
| [pptp](../virtual-private-networks/pptp.md) | <em><code>/interface/pptp-server</code></em><br/><em><code>/interface/pptp-client</code></em> |
| [proxy](../network-management/proxy/index.md) | *`/ip/proxy`* |
| [romon](../management-tools/romon.md) | *`/tool/romon`* |
| [scheduler](./scheduler.md) | *`/system/scheduler`* |
| [smb](../storage/smb.md) | *`/ip/smb`* |
| [sniffer](../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) | *`/tool/sniffer`* |
| [socks](../network-management/socks/index.md) | *`/ip/socks`* |
| [traffic-gen](../diagnostics-monitoring-and-troubleshooting/traffic-generator.md) | <em><code>/tool/traffic-generator</code></em><br/><em><code>/tool/flood-ping</code></em><br/><em><code>/tool/ping-speed</code></em> |
| [zerotier](../virtual-private-networks/zerotier.md) | */zerotier* |

## 允許的版本 {#allowed-versions}

Device mode 在其引數中列出了名為“allowed-versions”的引數。這是一個 MikroTik 認為安全且不包含任何可被攻擊者利用的嚴重漏洞的版本列表。
  
此設定不依賴於已安裝的 RouterOS 版本，並作為單獨的防護層工作，以防止攻擊者逐步降級版本，從而到達任何已知存在漏洞的 RouterOS 發行版。當您將 RouterOS 升級到具有較新“allowed-versions”列表的發行版時，最舊的列表將被覆蓋。如果您降級 RouterOS，“allowed-versions”列表不會改變，並將保持更新為最新列表。如果 device-mode 的“install-any-version”已啟用，則該列表會被忽略。

## Flagged 狀態 {#flagged-status}

除了 device-mode 功能外，RouterOS 現在還可以在系統啟動時分析整個配置，以確定是否存在任何未經授權訪問您路由器的跡象。如果檢測到可疑配置，可疑配置將被停用，並且 **flagged** 引數將設定為“yes”。此時裝置具有 Flagged 狀態，並會強制執行某些限制。

```ros
[admin@MikroTik] > /system/device-mode/print 
     mode: advanced
  flagged: yes
...
```

如果系統具有此 flagged 狀態，當前配置可以工作，但無法執行以下操作：
  
bandwidth-test、traffic-generator、sniffer，以及針對以下程式啟用或建立新配置條目的配置操作（仍然可以停用或刪除它們）：*system scheduler, SOCKS proxy, pptp, l2tp, ipsec, proxy, smb*。  
  
當路由器處於 flagged 狀態時執行上述操作，您將收到錯誤訊息：

```ros
[admin@MikroTik] > /tool/sniffer/quick 
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
[admin@MikroTik] > /int l2tp-client/add connect-to=1.1.1.1 user=user
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
```

要退出 flagged 狀態，您必須執行命令“/system/device-mode/update flagged=no”。系統將要求您按下按鈕，或執行硬重啟（物理切斷電源或對虛擬機器執行硬重啟）。
  
**重要！** 儘管系統已停用觸發 flagged 狀態的任何看似惡意的規則，但在退出 flagged 狀態之前，務必檢查您的所有配置是否存在其他未知內容。如果您的系統已被標記，請假定您的系統已遭到入侵，並在重新啟用系統使用之前對所有設定進行全面審計。完成審計後，請更改所有系統密碼並升級到最新的 RouterOS 版本。

:::warning
從 RouterOS 7.17 版本開始，device-mode 限制雙啟動的 SwOS/RouterOS 切換；要啟用：`/system/device-mode/update routerboard=yes`
:::
