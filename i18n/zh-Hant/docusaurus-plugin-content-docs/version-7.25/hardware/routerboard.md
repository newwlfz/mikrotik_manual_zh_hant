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
source: https://manual.mikrotik.com/docs/7.25/hardware/routerboard
captured_at: '2026-11-04T11:17:30+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
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
  minimum-firmware: 7.8                                                      
  current-firmware: 7.22.2
  upgrade-firmware: 7.22.2                          
```

每個引數的詳細說明可在 [CLI 參考](./routerboard.md) 中找到。

## 升級 RouterBOOT {#upgrading-routerboot}

RouterBOOT 升級通常包含對 RouterBOARD 整體執行的細微改進。你應保持韌體為最新版本。

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

重啟後，請驗證 **current-firmware** 與 **upgrade-firmware** 是否一致。值一致即表示升級已成功應用。

## 預啟動 Etherboot {#preboot-etherboot}

預啟動 etherboot 會指示 RouterOS 裝置在每次啟動時，在開始常規啟動過程（例如啟動 RouterOS）之前，在指定時間內搜尋 Netinstall 伺服器。

預設情況下，Etherboot 接受來自任何 BOOTP/DHCP 伺服器的地址，但可以透過 [`preboot-etherboot-server`](../cli-reference/system/routerboard/settings.md#preboot-etherboot-server) 引數，將預啟動 etherboot 過程鎖定到具有特定 IP 地址的特定 Netinstall 伺服器。

當這兩個選項都啟用時，你可以在不訪問 RouterOS 或按下復位按鈕的情況下遠端重新安裝裝置。

例如：
1. 對 RouterOS 裝置進行斷電重啟（例如，透過 PoE 交換器或電源控制器）。
2. 設備嘗試 Etherboot 並連線到 Netinstall 伺服器。
3. 安裝完成後，停用 Netinstall 伺服器。
4. 再次對裝置進行斷電重啟以完成該過程。

執行：

```ros
/system/routerboard/settings/set preboot-etherboot=9s preboot-etherboot-server=10.10.10.100
```

在每次重啟或斷電重啟時，裝置會在 **9 秒**內嘗試從 IP 地址為 **10.10.10.100** 的 Netinstall 伺服器獲取 IP 地址。如果沒有這樣的伺服器可用，裝置將繼續正常的啟動過程。

:::warning
如果未指定 `preboot-etherboot-server`，裝置將接受來自任何 Netinstall 伺服器的 IP 地址並進入 Etherboot 模式，等待重新安裝過程。僅當 RouterBOOT 的 `boot-protocol` 設定為 **dhcp** 時才會使用 DHCP 伺服器（預設值為 **bootp**）。
:::

RouterOS 重新安裝不會影響 BIOS 設定。如果啟用了預啟動 etherboot，裝置會在每次啟動時繼續嘗試 Etherboot。

要在不訪問 RouterOS 的情況下防止意外啟用 Etherboot，請停用任何已連線的 Netinstall 或 DHCP 伺服器。

## 受保護的 RouterBOOT {#protected-routerboot}

受保護的 RouterBOOT 設定透過停用 Etherboot 並限制對引導載入程式的訪問，來保護 RouterOS 裝置免受物理訪問。

你只能在登入後從 RouterOS 內部啟用或停用此設定。沒有任何 RouterBOOT 設定可以直接控制它。這些附加選項僅在特定條件下出現。

:::warning
如果在啟用受保護的 RouterBOOT 時忘記了 RouterOS 管理員密碼，則裝置無法在不執行完全重新格式化的情況下恢復。
:::

### 啟用後的行為 {#behavior-when-enabled}

當此設定處於活動狀態時：

- 復位按鈕和復位針孔被停用。
- 無法透過序列控制檯訪問 RouterBOOT 選單。
- Etherboot（Netinstall）被停用。
- 你只能透過 RouterOS 並使用有效的管理員密碼訪問裝置。
- 你只能從 RouterOS 內部啟用或停用此設定。不存在 RouterBOOT 級別的選項。

:::warning
如果你啟用了受保護的 RouterBOOT 並忘記了 RouterOS 密碼，**裝置無法**透過常規方式恢復。
:::

### 啟用或停用 {#enabling-or-disabling}

從 RouterOS v7 開始，啟用或修改此設定需要透過按下復位按鈕或模式按鈕進行確認。

你有 **60 秒**的時間來確認更改。

#### 啟用（示例） {#enable-example}

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

#### 停用（示例） {#disable-example}

```ros
/system/routerboard/settings/set protected-routerboot=disabled
```

:::warning
如果在超時時間內未按下按鈕，則更改不會應用。
:::

### 緊急重新格式化（恢復方法） {#emergency-reformat-recovery-method}

作為緊急恢復選項，你可以在開機時按住復位按鈕，時間超過 `reformat-hold-button` 但短於 `reformat-hold-button-max`，從而重設裝置。

:::danger
極其危險。僅在你已失去對裝置的所有訪問許可權時使用。
:::

觸發時，將執行以下操作：

- RouterOS、所有檔案和配置將被完全且不可逆地擦除（NAND 重新格式化）。
- 所有 RouterBOOT 設定將重設為預設值。
- 裝置重啟。
- 由於從 NAND 啟動失敗，裝置會自動進入 Etherboot 模式。需要 Netinstall 來重新安裝 RouterOS。

:::note
在某些 RouterBOARD 裝置上，重新格式化可能需要超過 5 分鐘。
:::

### LED 指示燈 {#led-indicator}

當啟用受保護的 RouterBOOT 時，LED 每秒閃爍一次以幫助計時：

- LED 熄滅一秒。
- LED 點亮一秒。

### 對較舊 MikroTik 硬體的支援 {#support-on-older-mikrotik-hardware}

:::warning
本節僅適用於顯示下文所述特定錯誤訊息的較舊裝置。除非該訊息指示你這樣做，否則請勿修改引導載入程式。
:::

受保護的 RouterBOOT 設定在所有現代 MikroTik 裝置上均受支援。但是，如果你使用的是最低韌體版本早於 **7.19.3** 的較舊裝置，則在嘗試啟用它時可能會看到以下訊息：

> *'protected routerboot' 功能需要 backup-routerboot 升級*

如果你看到此訊息，請按照適用於你的 RouterOS 版本的步驟操作。

#### RouterOS v7 — 升級步驟 {#routeros-v7--upgrade-steps}

1. 將裝置[升級或降級](../getting-started/installation-and-upgrade/upgrade.md#manual-upgrade)到 RouterOS **7.19.3**。你可以在 [MikroTik 下載頁面](https://mikrotik.com/download)找到此版本。

2. 透過執行 `/system/routerboard/upgrade` 升級 RouterBOOT 韌體，然後重啟裝置。重啟後，驗證 `/system/routerboard/print` 中顯示的 **current-firmware** 值與 `/system/resource/print` 中顯示的已安裝 RouterOS 版本一致——兩者都應為 **7.19.3**。

3. 將 [v7 通用軟體包（所有架構）](https://box.mikrotik.com/f/991c3e94984c4e18b8d6/?dl=1) 上傳到裝置並再次重啟。這會將 **minimum-firmware** 版本更新為 **7.19.3**，這是啟用受保護的 RouterBOOT 設定所必需的。

4. 完成上述步驟後，你可以將裝置升級到更高版本的 RouterOS。

#### RouterOS v6 — 升級步驟 {#routeros-v6--upgrade-steps}

如果你的裝置執行的是 RouterOS **v6** 並且遇到相同的訊息，請按照上一節中的步驟操作，但有以下不同：

- 目標版本：**6.49.7**（而不是 7.19.3）
- 使用 [v6 通用包（所有架構）](https://box.mikrotik.com/f/b062a26b4bd34c55aa52/?dl=1)（而不是 v7 包）

## Mode 和 Reset 按鈕 {#mode-and-reset-buttons}

所有執行 RouterOS 的 MikroTik 裝置都支援 **Reset** 按鈕的附加選項。部分 RouterBOARD 裝置還包含 **Mode** 按鈕，你可以將其配置為在按下時執行自定義指令碼。

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

### 基本 Mode 按鈕示例 {#basic-mode-button-example}

以下示例建立一個指令碼並將其分配給 Mode 按鈕。按下按鈕時，會向系統日誌寫入一條訊息。

```ros
/system/script/add name=test-mode-button source={:log info message=("mode button pressed");}
/system/routerboard/mode-button/set on-event=test-mode-button enabled=yes
```

---

### 按住時間選項 {#hold-time-option}

你可以配置按鈕僅在按住特定時長時才觸發。以下示例在 Mode 按鈕被按住 3 到 5 秒時啟用指令碼：

```ros
/system/script/add name=test-mode-button source={:log info message=("mode button pressed");}
/system/routerboard/mode-button/set on-event=test-mode-button hold-time=3..5 enabled=yes
```

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

D53、C53、S53 和 H53 系列的 RouterBOARD 裝置包含一個可配置的 **WPS 按鈕**。它的工作方式與 Mode 和 Reset 按鈕相同：在按下時執行指令碼。

#### 基本 WPS 按鈕示例 {#basic-wps-button-example}

```ros
/system/script/add name=test-wps-button source={:log info message=("wps button pressed");}
/system/routerboard/wps-button/set on-event=test-wps-button hold-time=0..10 enabled=yes
```

#### 使用 WPS 按鈕或 Mode 按鈕觸發 WPS 配對 {#trigger-wps-pairing-with-the-wps-button-or-mode-button}

以下指令碼會在所有活動的 Wi-Fi 接入點介面上啟動 WPS 按鈕配對。你可以將其分配給 WPS 按鈕、Mode 按鈕或兩者。

```ros
/system/script/add name=wps-accept source={
    :foreach iface in=[/interface/wifi/find where (configuration.mode="ap" && disabled=no)] do={
        /interface/wifi/wps-push-button $iface;
    }
}

/system/routerboard/wps-button/set enabled=yes on-event=wps-accept
/system/routerboard/mode-button/set enabled=yes on-event=wps-accept
```
