---
sidebar_key: "hardware/routerboard"
sidebar_position: 10
title: "路由器主機板"
sidebar_label: "路由器主機板"
description: "本頁面介紹 MikroTik RouterOS 中的 `/system/routerboard` 選單，提供型號、序列號以及當前/升級韌體版本等硬體和韌體資訊。其中包含 RouterBOOT 韌體的升級說明，以及在硬體層面配置啟動行為的設定。"
tags:
  - 'routerboard'
  - 'firmware-upgrades'
  - 'settings'
source: https://manual.mikrotik.com/docs/7.24/hardware/routerboard
captured_at: '2026-11-04T11:29:43+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

在 RouterBOARD 裝置上，你可以從 `/system/routerboard` 選單檢視基本的硬體和韌體資訊。

要顯示這些資訊，請執行以下命令：

```ros
[admin@demo.mt.lv] /system/routerboard/print 
       routerboard: yes                                                      
             model: CCR2116-12G-4S+                                                                                                
     serial-number: MT123456789                                              
     firmware-type: al64v3                                                   
  factory-firmware: 7.8                                                      
  current-firmware: 7.22.2
  upgrade-firmware: 7.22.2                          
```

輸出包含以下詳細資訊：

## 屬性 {#properties}

**只讀屬性：**

| 屬性 | 描述 |
| :-- | :-- |
| **routerboard** (*yes \| no*) | 指示該裝置是否為 RouterBOARD 單元。 |
| **model** (*string*) | RouterBOARD 型號。 |
| **serial-number** (*string*) | 裝置的唯一序列號。 |
| **firmware-type** (*string*) | 裝置使用的引導載入程式韌體型別。 |
| **factory-firmware** (*string*) | 出廠時安裝的韌體版本。 |
| **current-firmware** (*string*) | 當前使用的 RouterBOOT 載入程式版本。不要將其與 RouterOS 作業系統版本混淆。 |
| **upgrade-firmware** (*string*) | RouterOS 升級可能包含新的 RouterBOOT 版本檔案，但必須手動應用。此行指示裝置上是否已找到新的 RouterBOOT 檔案。該檔案可能隨最近的 RouterOS 升級一起提供，也可能作為 FWF 檔案手動上傳。無論哪種情況，此處都會顯示可用的最新版本。 |

## 升級 RouterBOOT {#upgrading-routerboot}

RouterBOOT 升級通常包含對 RouterBOARD 整體執行的細微改進。建議保持韌體為最新版本。

要檢查是否有可用的升級，請比較 `/system/routerboard` 下的 **current-firmware** 和 **upgrade-firmware** 值。如果 **upgrade-firmware** 顯示的版本高於 **current-firmware**，則說明有較新版本可供應用。

### 升級步驟 {#upgrade-steps}

1. 執行升級命令：

   ```ros
   [admin@mikrotik] /system/routerboard> upgrade
   Do you really want to upgrade firmware? [y/n]
   y
   echo: system,info,critical Firmware upgraded successfully, please reboot for changes to take effect!
   ```

2. 出現提示時，輸入 **y** 進行確認。

3. 重啟裝置以應用更改：

   ```ros
   /system/reboot
   ```

重啟後，驗證 **current-firmware** 與 **upgrade-firmware** 一致，確認升級已成功應用。

## 設定 {#settings}

**路徑：** `/system/routerboard/settings`

此子選單用於配置 RouterBOOT 韌體設定，這些設定控制裝置在硬體層面的啟動和執行方式。

```ros
[admin@MikroTik] /system/routerboard/settings> print 
              auto-upgrade: no
                 baud-rate: 115200
                boot-delay: 2s
            enter-setup-on: any-key
               boot-device: nand-if-fail-then-ethernet
         preboot-etherboot: disabled
             cpu-frequency: 1200MHz
          memory-frequency: 1066DDR
             boot-protocol: bootp
       enable-jumper-reset: yes
       force-backup-booter: no
               silent-boot: yes
      protected-routerboot: disabled
      reformat-hold-button: 20s
  reformat-hold-button-max: 10m
```

:::warning
從 RouterOS 7.17 版本開始，device-mode 設定會限制雙啟動裝置的 SwOS/RouterOS 切換。要啟用此功能，請執行：
`/system/device-mode/update routerboard=yes`
:::

### 屬性參考 {#property-reference}

| 屬性 | 描述 |
| :--- | :--- |
| **auto-upgrade** (*yes \| no*；預設值：**no**) | 是否在 RouterOS 升級後自動升級韌體。最新韌體將在額外重啟後應用。 |
| **baud-rate** (*integer*；預設值：**115200**) | 如果安裝了板載 RS232，選擇其速度（以位元每秒為單位）。Off 選項允許停用序列介面。 |
| **boot-delay** (*time*；預設值：**2s**) | 啟動時等待按鍵的時間。 |
| **boot-device** (*nand-if-fail-then-ethernet ...*；預設值：**nand-if-fail-then-ethernet**) | 選擇 RouterBOOT 載入作業系統的方式：- **ethernet** — 以 Etherboot 模式啟動裝置；- **flash-boot** — 啟動時啟用 Flashfig 模式。成功更改配置後或任何使用者登入板卡後，此設定將恢復為 NAND；- **flash-boot-once-then-nand** — 僅在單次啟動時啟用 Flashfig 模式，之後恢復為 nand-if-fail-then-ethernet；- **nand-if-fail-then-ethernet** — 從 NAND 啟動 RouterOS，如果 RouterOS 無法啟動，則自動進入 Etherboot。這是開箱即用裝置的預設模式；- **nand-only** — 從 NAND 啟動 RouterOS；- **try-ethernet-once-then-nand** — 以 Etherboot 模式啟動裝置一次，如果沒有可用的伺服器，則直接從 NAND 或裝置所使用的儲存型別啟動。**重要：** 注意Etherboot 模式是 MikroTik 裝置的一種特殊狀態，允許你使用 Netinstall 重新安裝裝置。根據所使用的裝置，有幾種方法可以將裝置置於 Etherboot 模式：1. 按住 Reset 按鈕並給裝置上電（等待 "USR" LED 閃爍然後穩定 "On"，當 "USR" LED 變為 "Off" 時鬆開 Reset 按鈕）——裝置將以 bootp 模式啟動，以便使用 Netinstall 重新安裝 RouterOS。2. 使用序列控制檯，在裝置啟動時持續按鍵盤上的 CTRL+E，直到裝置顯示正在嘗試 bootp 協定。3. 使用序列控制檯，在裝置啟動時按任意鍵，然後選擇 "o"，再選擇 "1" 和 "x"。 |
| **boot-os** (*router-os \| swos*；預設值：**router-os**) | 更改 CRS3xx 系列交換器的啟動作業系統。 |
| **boot-protocol** (*bootp \| dhcp ...*；預設值：**bootp**) | 要使用的啟動協定：- **bootp** — 啟動 RouterOS 的預設選項；- **dhcp** — 用於 OpenWRT 以及可能的其他作業系統。 |
| **cpu-frequency** (*取決於型號*；預設值：**取決於型號**) | 此選項允許更改裝置的 CPU 頻率。可選值取決於型號，要檢視可用選項，請在此提示符處按鍵盤上的 RouterOS 版本 6 中的 [?] 按鈕或 RouterOS 版本 7 中的 [F1] 按鈕。 |
| **cpu-mode** (*power-save \| regular*；預設值：**power-save**) | 是否在 HLT 指令中進入 CPU 掛起模式。大多數作業系統在 CPU 空閒週期使用 HLT 指令。當 CPU 處於掛起模式時，功耗較低，但在低溫條件下，建議選擇 regular 模式，以便整體系統溫度更高。 |
| **enable-jumper-reset** (*yes \| no*；預設值：**yes**) | 停用此項可避免透過板載跳線意外重設設定。 |
| **enter-setup-on** (*any-key \| delete-key*；預設值：**any-key**) | 在啟動延遲期間，哪個鍵會使 BIOS 進入配置模式。當序列控制檯在啟動過程中列印符號並自行進入 RouterBOOT 選單時，此選項很有用。請注意，在某些序列終端程式中，無法使用 Delete 鍵進入設定——在這種情況下，可能可以使用 Backspace 鍵來完成。 |
| **force-backup-booter** (*yes \| no*；預設值：**no**) | 是否使用備份 RouterBOOT。這僅在主載入程式以某種方式損壞且無法修復時有用。這樣你就不必透過按住 reset 按鈕（會載入備份載入程式）來啟動裝置，你可以使用此設定使其每次都載入備份載入程式：- **yes** — 始終使用備份載入程式；- **no** — 使用主載入程式。 |
| **init-delay** (*timeout interval 0s..9s*；預設值：) | 僅用於帶 RB9xx 系列裝置的 mPCIe 調變解調器。如果軟重啟後調變解調器無法被識別，則可能需要在 USB 埠初始化之前新增延遲。 |
| **memory-frequency** (*取決於型號*；預設值：**取決於型號**) | 此選項允許更改裝置的記憶體頻率。可選值取決於型號，要檢視可用選項，請在此提示符處按鍵盤上的 RouterOS 版本 6 中的 [?] 按鈕或 RouterOS 版本 7 中的 [F1] 按鈕。 |
| **memory-data-rate** (*取決於型號*；預設值：**取決於型號**) | 此選項允許更改裝置的記憶體資料速率。可選值取決於型號，要檢視可用選項，請在此提示符處按鍵盤上的 RouterOS 版本 6 中的 [?] 按鈕或 RouterOS 版本 7 中的 [F1] 按鈕。 |
| **preboot-etherboot** (*timeout interval 1s..30s*；預設值：**disabled**) | 啟用預啟動 etherboot，它在常規啟動裝置之前執行。其工作方式與 boot-device=etherboot 相同，但具有額外的超時值。如果在超時到期之前未從 Netinstall 伺服器收到 IP 地址，則將開始常規啟動過程。**重要：** 注意preboot-etherboot 配置儲存在 BIOS 中，將 RouterOS 降級到較舊版本不會停用它。可以從 RouterOS 選單或透過重設 BIOS 來停用此功能。由於 etherboot 接受來自任何 BOOTP/DHCP 伺服器的 IP 地址，請使用 preboot-etherboot-server 僅在從指定 Netinstall 伺服器收到地址時才啟動 etherboot。 |
| **preboot-etherboot-server** (*IP address, any*；預設值：**any**) | 將 preboot-etherboot 設定為僅接受來自指定 Netinstall 伺服器 IP 地址的 IP 地址。透過啟用此功能，可以防止來自其他 BOOTP/DHCP 伺服器的意外 etherboot。 |
| **regulatory-domain-ce** (*yes \| no*；預設值：**no**) | 為高天線增益裝置啟用超低 TX 功率（需要重啟）。 |
| **silent-boot** (*yes \| no*；預設值：**no**) | 此選項停用啟動期間的蜂鳴聲：- **yes** — 無啟動蜂鳴聲（不會停用 RouterOS: beep 命令）；- **no** — 常規啟動聲音。 |
| **disable-pci** (*yes \| no*；預設值：**no**) | 針對 MT7621 晶片裝置的特定設定。允許停用 PCI。 |
| **preferred-architecture** (*arm32 \| arm64*；預設值：**arm32**) | 針對 L009 裝置的特定設定。允許更新裝置以使用 ARM64 架構。 |
| **etherboot-port** (*interface*；預設值：) | 允許選擇 Etherboot/Netinstall 介面，僅適用於 CRS520、CRS804、CRS812。預設埠取決於型號。 |
| **gpio-function** (*port*；預設值：**serial1**) | 針對 M33 裝置的特定設定。預設情況下，引腳 12、13、15、16 配置為第二個 "serial1" 埠使用，可以在 `/iot/gpio/digital` 選單中將其改用於 GPIO 用途。 |

:::danger
對 CPU 或記憶體進行超頻不在保修範圍內。如果懷疑效能問題是由超頻引起的，請在聯絡支援之前將兩個頻率恢復為其標稱值。
:::

## 預啟動 Etherboot {#preboot-etherboot}

**preboot-etherboot** 是一項功能，它指示 RouterOS 裝置在每次啟動時，在開始常規啟動過程（例如 RouterOS）之前，在指定時間內搜尋 Netinstall 伺服器。此功能對於遠端重新安裝特別有用，因為它允許裝置在每次啟動時嘗試 Etherboot。

**preboot-etherboot-server** 指定 preboot-etherboot 過程應僅接受來自具有特定 IP 地址的 Netinstall 伺服器的 IP 地址。預設情況下，Etherboot 接受來自任何 BOOTP/DHCP 伺服器的地址。此設定允許你將其限制為特定的 Netinstall 伺服器，以便裝置可以在不從網路中移除的情況下重新安裝。

## 遠端重新安裝 {#remote-reinstallation}

當兩個功能都啟用時，可以在不訪問 RouterOS 或使用 reset 按鈕的情況下遠端重新安裝裝置。

例如，要啟動遠端重新安裝：

1. 給 RouterOS 裝置斷電再上電（例如，使用 PoE 交換器或電源控制器）。
2. 設備嘗試 Etherboot 並連線到 Netinstall 伺服器。
3. 安裝完成後，停用 Netinstall 伺服器。
4. 再次給裝置斷電再上電以完成該過程。

## 要求 {#requirements}

要啟用 **preboot-etherboot** 和 **preboot-etherboot-server**：

1. 安裝 RouterOS 7.9 或更新版本。
2. 升級 RouterBOOT：

要啟用該功能，請執行：

```ros
/system/routerboard/settings/set preboot-etherboot=9s preboot-etherboot-server=10.10.10.100
```

在每次重啟或斷電再上電時，裝置將嘗試在 **9 秒**內從 IP 為 **10.10.10.100** 的 Netinstall 伺服器接收 IP 地址。如果沒有此類伺服器可用，裝置將繼續正常啟動過程。

:::warning
如果未指定 **preboot-etherboot-server**，裝置將接受來自任何 Netinstall 伺服器的 IP 地址並進入 Etherboot 模式，等待重新安裝過程。僅當 RouterBOOT 的 **boot-protocol** 設定為 **dhcp**（預設值為 **bootp**）時，才會使用 DHCP 伺服器。
:::

RouterOS 重新安裝不會影響 BIOS 設定。如果啟用了 preboot-etherboot，裝置將在每次啟動時繼續嘗試進入 Etherboot。

要在不訪問 RouterOS 的情況下避免意外啟用 Etherboot，請停用任何已連線的 Netinstall 或 DHCP 伺服器。

## 受保護的 RouterBOOT {#protected-routerboot}

受保護的 RouterBOOT 功能允許透過停用 Etherboot 並限制對引導載入程式的訪問，來保護 RouterOS 裝置免受物理訪問。

此功能只能在登入後從 RouterOS 內部啟用或停用。沒有可直接控制它的 RouterBOOT 設定。這些附加選項僅在特定條件下出現。

:::warning
如果在啟用受保護的 RouterBOOT 時忘記了 RouterOS 管理員密碼，則裝置無法在不執行完全重新格式化的情況下恢復。
:::

## 啟用後的行為 {#behavior-when-enabled}

當此功能處於活動狀態時：

- reset 按鈕和 reset 針孔被停用。
- 無法透過序列控制檯訪問 RouterBOOT 選單。
- Etherboot（Netinstall）被停用。
- 只能使用有效的管理員密碼透過 RouterOS 訪問裝置。
- 此設定只能從 RouterOS 內部啟用或停用（不存在 RouterBOOT 級別的選項）。

:::warning
如果你啟用了受保護的 RouterBOOT 並忘記了 RouterOS 密碼，**裝置無法**透過常規方式恢復。
:::

## 啟用或停用 {#enabling-or-disabling}

從 RouterOS v7 開始，啟用或修改此功能需要透過按下 reset 或 mode 按鈕進行確認。

你有 **60 秒**的時間來確認更改。

### 啟用（示例） {#enable-example}

```ros
[admin@450] > /system/routerboard/settings/set protected-routerboot=enabled
[admin@450] > /system/routerboard/settings/print
                        ;;; press button within 60 seconds to confirm
                            protected routerboot enable
              auto-upgrade: no
                 baud-rate: 115200
                boot-delay: 2s
            enter-setup-on: any-key
               boot-device: nand-if-fail-then-ethernet
             cpu-frequency: auto
             boot-protocol: bootp
       enable-jumper-reset: yes
       force-backup-booter: no
               silent-boot: yes
      protected-routerboot: enabled
      reformat-hold-button: 20s
  reformat-hold-button-max: 10m
```

### 停用（示例） {#disable-example}

```ros
/system/routerboard/settings/set protected-routerboot=disabled
```

:::warning
如果在超時時間內未按下按鈕，則更改不會應用。
:::

## 緊急重新格式化（恢復方法） {#emergency-reformat-recovery-method}

作為緊急恢復選項，可以透過在開機時按住 reset 按鈕的時間長於 reformat-hold-button 時間但短於 reformat-hold-button-max 來重設裝置。

:::danger
極其危險。僅在你已失去對裝置的所有訪問許可權時使用。
:::

觸發時，將執行以下操作：

- RouterOS、所有檔案和配置被完全且不可逆地擦除（NAND 重新格式化）。
- 所有 RouterBOOT 設定重設為預設值。
- 裝置重啟。
- 由於從 NAND 啟動失敗，裝置自動進入 Etherboot 模式
需要 Netinstall 來重新安裝 RouterOS。

:::note
在某些 RouterBOARD 裝置上，重新格式化可能需要超過 5 分鐘。
:::

### 屬性參考 {#property-reference-1}

| 屬性 | 描述 |
| :--- | :--- |
| **protected-routerboot** (*enabled \| disabled*；預設值：**disabled**) | 停用透過序列控制檯訪問 RouterBOOT 配置，並阻止 reset 按鈕更改啟動模式（Netinstall 被停用）。只能使用具有管理許可權的已知 RouterOS 使用者賬戶訪問 RouterOS。此設定只能從 RouterOS 內部停用。如果 RouterOS 密碼丟失，恢復需要使用 reset 按鈕時序過程對裝置進行完全重新格式化。- **enabled** — 安全模式。只能使用有效的管理員級別使用者訪問 RouterOS。序列輸入被忽略。Etherboot 被停用，且無法更改 RouterBOOT 設定。- **disabled** — 正常執行。可透過序列控制檯訪問 RouterBOOT 設定，並且可以使用 reset 按鈕進入 Netinstall 模式。 |
| **reformat-hold-button** (*5s..300s*；預設值：**20s**) | 定義在開機時觸發裝置完全重新格式化必須按住 reset 按鈕的最短時間。按住時間必須長於此值但短於 `reformat-hold-button-max`。觸發時，裝置執行完全重設操作：- RouterOS、所有檔案和配置被永久擦除（NAND 重新格式化）。- 所有 RouterBOOT 設定重設為預設值。- 裝置重啟。- 由於 NAND 啟動失敗，裝置自動進入 Etherboot。- 需要 Netinstall 來重新安裝 RouterOS。⚠️ **警告：** 這是一項極其危險的操作，僅應在所有其他訪問方法均不可用時使用。在某些 RouterBOARD 裝置上，重新格式化過程可能需要超過 5 分鐘。完成後裝置即可用於 Netinstall。 |
| **reformat-hold-button-max** (*15s..600s*；預設值：**10m**) | 定義在觸發重新格式化期間允許按住 reset 按鈕的最長時間。與 `reformat-hold-button` 配合使用以建立精確的時間視窗。例如，設定 `reformat-hold-button=60s` 和 `reformat-hold-button-max=65s` 要求按鈕嚴格按住 60 到 65 秒之間。這透過使意外或猜測的重設幾乎不可能來增強安全性。在 RouterBOOT 3.38.3 中引入。 |

### LED 指示燈 {#led-indicator}

當啟用受保護的 RouterBOOT 時，LED 每秒閃爍一次以幫助計時：

- LED 熄滅一秒
- LED 點亮一秒

### 對較舊 MikroTik 硬體的支援 {#support-on-older-mikrotik-hardware}

> **重要：** 本節僅適用於顯示下述特定錯誤訊息的較舊裝置。除非該訊息指示，否則不要修改引導載入程式。

受保護的 RouterBOOT 功能在所有現代 MikroTik 裝置上均受支援。但是，如果你使用的是出廠韌體版本低於 **7.19.3** 的較舊裝置，則在嘗試啟用該功能時可能會看到以下訊息：

> *'protected routerboot' 功能需要 backup-routerboot 升級*

如果你看到此訊息，請按照以下步驟操作。

### RouterOS v7 — 升級步驟 {#routeros-v7--upgrade-steps}

1. 將裝置[升級或降級](../getting-started/installation-and-upgrade/upgrade.md#manual-upgrade)到 RouterOS **7.19.3**。你可以在 [MikroTik 下載頁面](https://mikrotik.com/download)找到此版本。

2. 透過執行 `/system/routerboard/upgrade` 升級 RouterBOOT 韌體，然後重啟裝置。重啟後，驗證 `/system/routerboard/print` 中顯示的 **current-firmware** 值與 `/system/resource/print` 中顯示的已安裝 RouterOS 版本一致——兩者都應為 **7.19.3**。

3. 將 [v7 通用包（所有架構）](https://box.mikrotik.com/f/991c3e94984c4e18b8d6/?dl=1)上傳到裝置並再次重啟。這會將 **factory-firmware** 版本更新為 **7.19.3**，這是啟用受保護的 RouterBOOT 功能所必需的。

4. 完成上述步驟後，你可以將裝置升級到更新的 RouterOS 版本。

### RouterOS v6 — 升級步驟 {#routeros-v6--upgrade-steps}

如果你的裝置執行 RouterOS **v6** 並遇到相同的訊息，請按照上述相同步驟操作，但有以下區別：

- 目標版本：**6.49.7**（而不是 7.19.3）
- 使用 [v6 通用包（所有架構）](https://box.mikrotik.com/f/b062a26b4bd34c55aa52/?dl=1)（而不是 v7 包）

## Mode 和 Reset 按鈕 {#mode-and-reset-buttons}

所有執行 RouterOS 的 MikroTik 裝置都支援 **Reset** 按鈕的附加功能。部分 RouterBOARD 裝置還包含 **Mode** 按鈕，可配置為在按下時執行自定義指令碼。

:::warning
由 Mode 或 Reset 按鈕觸發的指令碼以 `ftp`、`reboot`、`read`、`write`、`test` 和 `romon` 策略執行。有關更多資訊，請參閱[指令碼許可權](../developer-guides/scripting/index.md#script-permissions)。
:::

---

### 支援的裝置（Mode 按鈕） {#supported-devices-mode-button}

以下裝置支援 Mode 按鈕：

- RBcAP-2nD (cAP)
- RBcAPGi-5acD2nD (cAP ac)
- RBwsAP5Hac2nD (wsAP ac lite)
- RB750Gr3 (hEX)
- RB760iGS (hEX S)
- RB912R-2nD (LtAP mini, LtAP mini LTE/4G kit)
- RBD52G-5HacD2HnD (hAP ac²)
- RBLHGR (LHG LTE/4G kit)
- RBSXTR (SXT LTE/4G kit)
- CRS328-4C-20S-4S+RM
- CRS328-24P-4S+RM
- CCR1016-12G r2
- CCR1016-12S-1S+ r2
- CCR1036-12G-4S r2
- CCR1036-8G-2S+ r2
- RBD53G-5HacD2HnD (Chateau)
- RBD53GR-5HacD2HnD (hAP ac³)
- E50UG (hEX)
- L41G-2axD (hAP ax lite)
- L009UiGS-RM, L009UiGS-2HaxD-IN
- cAPGi-5HaxD2HaxD (cAP ax)
- C53UiG+5HPaxD2HPaxD (hAP ax³)
- S53UG+5HaxD2HaxD (Chateau ax)
- H53UiG-5HaxQ2HaxQ (Chateau PRO ax)
- CCR2116-12G-4S+
- RDS2216-2XG-4S+4XS-2XQ

---

### 配置屬性 {#configuration-properties}

| 屬性 | 描述 |
| :--- | :--- |
| **enabled** (*no \| yes*；預設值：**no**) | 啟用或停用按鈕功能。 |
| **hold-time** (*time interval Min..Max*；預設值：—) | 僅當按鈕按住的持續時間在指定範圍內時才觸發按鈕操作。`Min` 和 `Max` 均接受從 `0s` 到 `1m` 的值。*（從 RouterOS 6.47beta60 及更高版本可用。）* |
| **on-event** (*string*；預設值：—) | 按下按鈕時要執行的指令碼名稱。指令碼必須在[指令碼](../developer-guides/scripting/index.md)選單中建立並命名。 |

:::info
Mode、Reset 和 WPS 按鈕的 on-event 指令碼使用 `read,write,reboot,ftp,romon,test` 許可權執行。
:::

---

### 基本 Mode 按鈕示例 {#basic-mode-button-example}

以下示例建立一個指令碼並將其分配給 Mode 按鈕。按下按鈕時，會向系統日誌寫入一條訊息。

```ros
/system/script/add name=test-mode-button source={:log info message=("mode button pressed");}
/system/routerboard/mode-button/set on-event=test-mode-button enabled=yes
```

---

### 使用 Hold-Time 選項（RouterOS 6.47 及更高版本） {#using-the-hold-time-option-routeros-647-and-later}

:::info
`hold-time` 選項和擴充套件的 Reset 按鈕功能在 RouterOS 6.47 中引入。
:::

你可以配置按鈕僅在按住特定持續時間時觸發。以下示例在 Mode 按鈕按住 3 到 5 秒之間時啟用指令碼：

```ros
/system/script/add name=test-mode-button source={:log info message=("mode button pressed");}
/system/routerboard/mode-button/set on-event=test-mode-button hold-time=3..5 enabled=yes
```

---

### Reset 按鈕配置 {#reset-button-configuration}

Reset 按鈕的配置方式與 Mode 按鈕相同，但使用不同的選單路徑：`/system/routerboard/reset-button`。

```ros
/system/script/add name=test-reset-button source={:log info message=("reset button pressed");}
/system/routerboard/reset-button/set on-event=test-reset-button hold-time=0..10 enabled=yes
```

---

### 示例：使用 Mode 按鈕切換 LED 暗模式 {#example-toggle-led-dark-mode-with-the-mode-button}

以下指令碼在每次按下 Mode 按鈕時切換 [LED 暗模式](./leds.md#led-settings)的開啟和關閉：

```ros
/system/script/add name=dark-mode source={
   :if ([system leds settings get all-leds-off] = "never") do={
      /system/leds/settings/set all-leds-off=immediate
   } else={
      /system/leds/settings/set all-leds-off=never
   }
}
/system/routerboard/mode-button/set enabled=yes on-event=dark-mode
```

---

### WPS 按鈕（D53、C53、S53 和 H53 系列） {#wps-button-d53-c53-s53-and-h53-series}

D53、C53、S53 和 H53 系列的 RouterBoard 包含可配置的 **WPS 按鈕**。其工作方式與 Mode 和 Reset 按鈕相同——按下時執行指令碼。

**基本 WPS 按鈕示例：**

```ros
/system/script/add name=test-wps-button source={:log info message=("wps button pressed");}
/system/routerboard/wps-button/set on-event=test-wps-button hold-time=0..10 enabled=yes
```

**透過 WPS 按鈕或 Mode 按鈕觸發 WPS 配對：**

以下指令碼在所有活動的 Wi-Fi 接入點介面上啟動 WPS 按鈕配對。你可以將其分配給 WPS 按鈕或 Mode 按鈕（或兩者）。

```ros
/system/script/add name=wps-accept source={
    :foreach iface in=[/interface/wifi/find where (configuration.mode="ap" && disabled=no)] do={
        /interface/wifi/wps-push-button $iface;
    }
}

/system/routerboard/wps-button/set enabled=yes on-event=wps-accept
/system/routerboard/mode-button/set enabled=yes on-event=wps-accept
```
