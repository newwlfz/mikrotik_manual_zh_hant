---
sidebar_key: "cli-reference/system/routerboard/settings"
sidebar_position: 3
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/cli-reference/system/routerboard/settings
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/routerboard/settings {#systemrouterboardsettings}
**條件：** !i386
**型別：** 設定目錄

此子選單用於配置 RouterBOOT 韌體設定。這些設定控制裝置在硬體層面的啟動和執行方式。

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

:::info
device-mode 設定會限制雙啟動裝置的 SwOS/RouterOS 切換。要啟用它，請執行：
`/system/device-mode/update routerboard=yes`
:::

:::danger
對 CPU 或記憶體進行超頻不在保修範圍內。如果你懷疑超頻導致效能問題，請在聯絡支援之前將兩個頻率都恢復到標稱值。
:::

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="auto-upgrade" typ="bool">是否在 RouterOS 升級後自動升級韌體。最新韌體會在額外重啟一次後應用。</ArgTableRow>
<ArgTableRow arg="baud-rate" typ="enum (115200 | 57600 | 38400 | 19200 | 9600 | 4800 | 2400 | 1200) { 115200:0, 57600:1, 38400:2, 19200:3, 9600:4, 4800:5, 2400:6, 1200:7 }">如果已安裝，請選擇板載 RS232 的速度（單位為位元每秒）。**off** 選項會停用序列埠介面。</ArgTableRow>
<ArgTableRow arg="boot-delay" typ="time">啟動時等待按鍵的時間。</ArgTableRow>
<ArgTableRow arg="init-delay" typ="time">僅用於 RB9xx 系列裝置上的 mPCIe 調變解調器。如果軟重啟後無法識別調變解調器，請設定 USB 埠初始化前的延遲。</ArgTableRow>
<ArgTableRow arg="enter-setup-on" typ="enum (any-key | delete-key) { any-key:0, delete-key:1 }">指定在啟動延遲期間按下哪個鍵會使 BIOS 進入配置模式。當序列埠控制檯在啟動過程中輸出符號並自行進入 RouterBOOT 選單時，此設定很有用。在某些序列埠終端程式中，無法使用 <kbd>Delete</kbd> 鍵進入設定。在這種情況下，請改用 <kbd>Backspace</kbd> 鍵。</ArgTableRow>
<ArgTableRow arg="boot-device" typ="enum">
選擇 RouterBOOT 載入作業系統的方式：
- **ethernet** — 讓裝置以 Etherboot 模式啟動。
- **flash-boot** — 啟動時啟用 Flashfig 模式。在配置更改成功後，或使用者登入到板卡後，此設定會恢復為 NAND。
- **flash-boot-once-then-nand** — 僅在單次啟動時啟用 Flashfig 模式。之後，該設定會重設為 `nand-if-fail-then-ethernet`。
- **nand-if-fail-then-ethernet** — 從 NAND 啟動 RouterOS。如果 RouterOS 無法啟動，裝置會自動進入 Etherboot。這是裝置開箱即用時的預設模式。
- **nand-only** — 從 NAND 啟動 RouterOS。
- **try-ethernet-once-then-nand** — 讓裝置以 Etherboot 模式啟動一次。如果沒有可用的伺服器，裝置會直接從 NAND 或裝置所使用的儲存型別啟動。

Etherboot 模式是 MikroTik 裝置的一種特殊狀態。你可以使用它透過 Netinstall 重新安裝裝置。  
你可以根據所使用的裝置，透過多種方式讓裝置進入 Etherboot 模式：
1. 按住 Reset 按鈕，然後給裝置通電。等待 USR LED 閃爍、然後常亮，再熄滅。鬆開 Reset 按鈕。裝置會以 bootp 模式啟動，以便使用 Netinstall 重新安裝 RouterOS。
2. 使用序列埠控制檯。裝置啟動時，按住 <kbd>Control</kbd>+<kbd>E</kbd>，直到裝置顯示正在嘗試 bootp 協定。
3. 使用序列埠控制檯。在裝置啟動時按任意鍵，然後依次按 <kbd>O</kbd>、<kbd>1</kbd> 和 <kbd>X</kbd>。
</ArgTableRow>
<ArgTableRow arg="preboot-etherboot" typ="alt { symbolic-names: enum (disabled) { disabled:0 }
, timeout: time [1 .. 30]
 }">啟用 preboot-etherboot，它會在常規啟動裝置之前執行。其工作方式與 `boot-device=etherboot` 相同，但多了一個超時值。如果在超時到期前未從 Netinstall 伺服器收到 IP 地址，常規啟動過程就會開始。preboot-etherboot 配置儲存在 BIOS 中，因此將 RouterOS 降級到較早版本不會停用它。你可以從 RouterOS 選單中停用它，或透過重設 BIOS 來停用它。由於 etherboot 會接受來自任何 BOOTP/DHCP 伺服器的 IP 地址，請使用 preboot-etherboot-server，僅在從指定 Netinstall 伺服器收到地址時才啟動 etherboot。</ArgTableRow>
<ArgTableRow arg="preboot-etherboot-server" typ="alt { symbolic-names: enum (any) { any:0 }
, ip: ipAddr
 }">將 preboot-etherboot 設定為僅接受來自指定 Netinstall 伺服器的 IP 地址。此設定可防止從其他 BOOTP/DHCP 伺服器意外觸發 etherboot。</ArgTableRow>
<ArgTableRow arg="etherboot-port" typ="enum (ether1 | ether2) { ether1:0, ether2:1 }">選擇 Etherboot/Netinstall 介面。僅適用於 CRS520、CRS804 和 CRS812。預設埠取決於型號。</ArgTableRow>
<ArgTableRow arg="boot-os" typ="enum (router-os | swos) { router-os:0, swos:1 }">更改 CRS3xx 系列交換器的啟動作業系統。</ArgTableRow>
<ArgTableRow arg="regulatory-domain-ce" typ="bool">為高天線增益裝置啟用超低 TX 功率（需要重啟）。</ArgTableRow>
<ArgTableRow arg="cpu-mode" typ="enum (power-save | regular) { power-save:0, regular:1 }">CPU 是否在 HLT 指令下進入掛起模式。大多數作業系統在 CPU 空閒週期使用 HLT 指令。當 CPU 處於掛起模式時，功耗更低。在低溫條件下，應選擇 regular 模式，以便提高系統整體溫度。</ArgTableRow>
<ArgTableRow arg="cpu-frequency" typ="enum">使用此選項可更改裝置的 CPU 頻率。可用值取決於型號。要檢視可用選項，請在此提示符下，於 RouterOS 版本 6 中按 <kbd>?</kbd>，或在 RouterOS 版本 7 中按 <kbd>F1</kbd>。</ArgTableRow>
<ArgTableRow arg="memory-frequency" typ="enum">使用此選項可更改裝置的記憶體頻率。可用值取決於型號。要檢視可用選項，請在此提示符下，於 RouterOS 版本 6 中按 <kbd>?</kbd>，或在 RouterOS 版本 7 中按 <kbd>F1</kbd>。</ArgTableRow>
<ArgTableRow arg="memory-data-rate" typ="enum">使用此選項可更改裝置的記憶體資料速率。可用值取決於型號。要檢視可用選項，請在此提示符下，於 RouterOS 版本 6 中按 <kbd>?</kbd>，或在 RouterOS 版本 7 中按 <kbd>F1</kbd>。</ArgTableRow>
<ArgTableRow arg="preferred-architecture" typ="enum (arm32 | arm64) { arm32:0, arm64:1 }">L009 裝置的專用設定。將裝置更新為使用 ARM64 架構。</ArgTableRow>
<ArgTableRow arg="boot-protocol" typ="enum (bootp | dhcp) { bootp:0, dhcp:1 }">要使用的啟動協定：- **bootp** — 啟動 RouterOS 的預設選項。- **dhcp** — 用於 OpenWrt，也可能用於其他作業系統。</ArgTableRow>
<ArgTableRow arg="enable-jumper-reset" typ="bool">停用此選項可防止透過板載跳線意外重設設定。</ArgTableRow>
<ArgTableRow arg="force-backup-booter" typ="bool">是否使用備份 RouterBOOT。僅當主載入器損壞且無法修復時，此設定才有用。你可以使用此設定在每次啟動時載入備份載入器，而不必在按住 Reset 按鈕的情況下啟動裝置（後者會載入備份載入器）。</ArgTableRow>
<ArgTableRow arg="silent-boot" typ="bool">此選項會停用啟動期間的蜂鳴聲（不會停用 RouterOS 的 `beep` 命令）。</ArgTableRow>
<ArgTableRow arg="disable-pci" typ="bool">配備 MT7621 晶片的裝置的專用設定。停用 PCI。</ArgTableRow>
<ArgTableRow arg="gpio-function" typ="ubit (serial1)">M33 裝置的專用設定。預設情況下，引腳 12、13、15 和 16 配置為使用第二個 `serial1` 埠。你可以在 `/iot/gpio/digital` 選單中重新分配它們以供 GPIO 使用。</ArgTableRow>
<ArgTableRow arg="protected-routerboot" typ="enum (disabled | enabled)">
停用透過序列埠控制檯訪問 RouterBOOT 配置，並阻止 Reset 按鈕更改啟動模式（Netinstall 被停用）。只能使用具有管理員許可權的已知 RouterOS 使用者賬戶訪問 RouterOS。只能從 RouterOS 內部停用此設定。如果丟失 RouterOS 密碼，恢復需要透過 Reset 按鈕時序操作對裝置進行完整重新格式化。
- **enabled** — 安全模式。僅可使用有效的管理員級賬戶訪問 RouterOS。序列埠輸入會被忽略，Etherboot 被停用，並且無法更改 RouterBOOT 設定。
- **disabled** — 正常執行。可透過序列埠控制檯訪問 RouterBOOT 設定，並且可以使用 Reset 按鈕進入 Netinstall 模式。
</ArgTableRow>
<ArgTableRow arg="reformat-hold-button" typ="time">
定義在通電時必須按住 Reset 按鈕以觸發裝置完整重新格式化的最短時間。按住時間必須長於該值，但短於 `reformat-hold-button-max`。觸發後，裝置會執行完整的重設操作：
- RouterOS、所有檔案和配置都會被永久擦除（NAND 重新格式化）。
- 所有 RouterBOOT 設定都會重設為預設值。
- 裝置會重啟。
- 由於 NAND 啟動失敗，裝置會自動進入 Etherboot。
- 需要使用 Netinstall 重新安裝 RouterOS。

此操作極其危險。僅當所有其他訪問方法都不可用時才使用。在某些 RouterBOARD 裝置上，重新格式化過程可能耗時超過 5 分鐘。重新格式化完成後，裝置即可用於 Netinstall。
</ArgTableRow>
<ArgTableRow arg="reformat-hold-button-max" typ="time">
定義在觸發重新格式化期間可以按住 Reset 按鈕的最長時間。它與 `reformat-hold-button` 配合建立一個精確的時間視窗。  
例如，設定 `reformat-hold-button=60s` 和 `reformat-hold-button-max=65s` 要求按住按鈕的時間嚴格介於 60 到 65 秒之間。這會提高安全性，使意外或猜測的重設幾乎不可能發生。該功能在 RouterBOOT 3.38.3 中引入。
</ArgTableRow>
</ArgTable>
