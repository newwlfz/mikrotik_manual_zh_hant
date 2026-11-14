---
sidebar_key: "internet-of-things/gpio"
title: "GPIO"
sidebar_label: "GPIO"
description: "GPIO 允許在 MikroTik 路由器上配置數字和模擬輸入/輸出引腳，用於電壓測量、幹接點檢測和繼電器控制等任務。設定透過 CLI 在 /iot/gpio 下管理，帶有用於模擬和數字引腳的子選單，包括電壓偏移調整。"
tags:
  - 'gpio'
  - 'iot'
source: https://manual.mikrotik.com/docs/internet-of-things/gpio
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

***注意**：為了訪問 GPIO 設定，請確保事先安裝了 **iot** [軟體包](../../getting-started/installation-and-upgrade/packages.md)。*

你可以透過以下[連結](https://en.wikipedia.org/wiki/General-purpose_input/output)找到有關 GPIO 的更多資訊。

GPIO 代表通用輸入/輸出（General-Purpose Input/Output）。它是路由器板上的一個/多個數字訊號引腳，允許你傳送/接收訊號。它在不同場景中很有用，例如：

1. 透過 ADC 輸入測量電壓。
2. 讀取從其他裝置接收的 0 和 1 訊號——“幹接點”。
3. 透過向引腳傳送邏輯 0 或 1 訊號來控制已連線的繼電器。

:::info
[KNOT](https://help.mikrotik.com/docs/spaces/UM/pages/41680915/RB924i-2nD-BT5+BG77)、[KNOT Embedded LTE4](https://mikrotik.com/product/knot_embedded_lte4) 和 [RBM33G](https://help.mikrotik.com/docs/spaces/UM/pages/14222434/RBM33G) 支援 GPIO 功能。

- [KNOT 引腳定義可在此處找到](https://help.mikrotik.com/docs/spaces/UM/pages/41680915/RB924i-2nD-BT5+BG77#RB924i2nDBT5%26BG77-GPIOpinout)。
- [KNOT Embedded LTE4 引腳定義，見此處。](https://help.mikrotik.com/docs/spaces/UM/pages/366477381/KNOT+Embedded+LTE4+EC25-EU+KNe#KNOTEmbeddedLTE4EC25EU%26KNe-GPIOpinout)
- [RBM33G 引腳定義，見此處](https://help.mikrotik.com/docs/spaces/UM/pages/14222434/RBM33G#RBM33G-GPIOpinout)。
:::

### RouterOS 配置 {#routeros-configuration}

**GPIO 設定僅可透過 CLI 使用。**

**子選單：** `/iot/gpio`

GPIO 設定分為：

- 模擬 (/iot/gpio/analog)
- 數字 (/iot/gpio/digital)

:::warning
在我們的示例中，我們使用 [KNOT](https://mikrotik.com/product/knot) 作為參考裝置（具有 2 個模擬輸入引腳、2 個數字輸出引腳和 1 個數字輸入引腳）。其他裝置可能具有不同的引腳定義，但適用相同的原理。
:::

#### 模擬引腳 {#analog-pin}

**子選單：** `/iot/gpio/analog`

***注意**：* 請檢視產品頁面，確認你的硬體是否支援模擬輸入。

在 "analog" 設定中，你可以測量模擬輸入/ADC 輸入引腳上的電壓：

```ros
[admin@device] /iot/gpio/analog> print
 # NAME                                                                                     VALUE       OFFSET
 0 pin2                                                                                       0mV          0mV
 1 pin3                                                                                      32mV          0mV
```

"OFFSET" 可用於手動補償導線上的電壓降。"VALUE" 透過 `value = adc_input + offset` 測量，其中 adc\_input 是引腳上的電壓。

"OFFSET" 配置示例如下：

```ros
[admin@device] /iot/gpio/analog> set pin2 offset  

Offset ::= [-]Num[mV]
  Num ::= -2147483648..2147483647    (integer number)

[admin@device] /iot/gpio/analog> set pin2 offset 2   
[admin@device] /iot/gpio/analog> print            
 # NAME                                                                                           VALUE       OFFSET
 0 pin2                                                                                             2mV          2mV
 1 pin3                                                                                             0mV          0mV 
```

#### 數字引腳 {#digital-pin}

**子選單：** `/iot/gpio/digital`

在 "digital" 部分，你可以使用數字輸出/輸入引腳傳送/接收邏輯 0 或 1 訊號（輸出引腳為 "開漏"）：

```ros
[admin@device] /iot/gpio/digital> print             
Flags: X - disabled 
 #   NAME                                        DIRECTION OUTPUT INPUT SCRIPT                                   
 0   pin5                                        input     0      0    
 1   pin4                                        output    0     
 2   pin6                                        output    0     
```

引腳的 "DIRECTION" 可以是 "input"（可接收訊號的引腳）或 "output"（可傳送訊號的引腳）。

:::info
[KNOT](https://mikrotik.com/product/knot) 的 pin4 和 pin6 引腳的 "DIRECTION" 無法更改。這兩個引腳只能用作 "output" 引腳。
:::

當引腳的方向設定為 "output" 時，你可以配置 "OUTPUT" 值。更改 "OUTPUT" 值會將訊號傳送到引腳。

```ros
[admin@device] /iot/gpio/digital> set pin4 output=

Output ::= 0 | 1

[admin@device] /iot/gpio/digital> set pin4 output=1        
[admin@device] /iot/gpio/digital> print            
Flags: X - disabled 
 #   NAME                                        DIRECTION OUTPUT INPUT SCRIPT                                      
 0   pin5                                        input     0      0    
 1   pin4                                        output    1     
 2   pin6                                        output    0     
```

"script" 欄位允許你配置一個指令碼，每當 "INPUT" 或 "OUTPUT" 值發生變化（從 0 到 1 或從 1 到 0）時就會啟動該指令碼。

```ros
[admin@device] /iot/gpio/digital> set pin4 script=script1
[admin@device] /iot/gpio/digital> set pin5 script="/system .."   
[admin@device] /iot/gpio/digital> print                       
Flags: X - disabled 
 #   NAME                                        DIRECTION OUTPUT INPUT SCRIPT                                      
 0   pin5                                        input     0      0     /system ..                                  
 1   pin4                                        output    1            script1                                     
 2   pin6                                        output    0     
```

### 不同場景 {#different-scenarios}

#### 控制繼電器 {#controlling-relays}

GPIO 實現的一種場景是使用數字輸出引腳“控制其他繼電器”。基本上，就是向連線到該引腳的單元傳送 "0" 或 "1" 訊號。要自動化此過程，你可以使用[排程器](../../system-information-and-utilities/scheduler.md)，它將在特定時間執行指令碼。

例如，你可以新增第一個[指令碼](../../developer-guides/scripting/index.md)（如下所示的一行）並將其命名為 "output=0"：

```ros
/iot/gpio/digital set pin4 output=0
```

然後新增第二個指令碼（如下所示的一行）並將其命名為 "output=1"：

```ros
/iot/gpio/digital set pin4 output=1
```

建立這兩個指令碼後，你可以配置一個排程：

```ros
[admin@device] /system/scheduler> add name=run-30s interval=30s on-event="output=0"
```

上面顯示的排程配置將每隔 30 秒執行名為 "output=0" 的指令碼。

```ros
[admin@device] /system/scheduler> add name=run-45s interval=45s on-event="output=1"
```

上面顯示的排程配置將每隔 45 秒執行名為 "output=1" 的指令碼。

因此，裝置將每隔 30 秒自動向第 4 個引腳（數字輸出引腳）傳送 output value=0 的訊號，並每隔 45 秒傳送 output value=1 的訊號。

你可以根據需要自行更改排程時間。

#### 監控輸入訊號 {#monitoring-input-signal}

另一種場景是使用數字輸入引腳“監控輸入訊號”。你需要一個指令碼，當方向為 direction="input" 的引腳的 "INPUT" 值發生變化時（即每當 RouterOS 裝置從連線到該引腳的另一臺裝置收到訊號 "0 或 1" 時），該指令碼將啟動電子郵件通知或 MQTT/HTTPS (fetch) 釋出。

*電子郵件通知指令碼：*

```ros
/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name]" body="$[/iot/gpio/digital/get pin5 input]"
```

建立指令碼後，將其應用/設定到 "input" 引腳：

```ros
[admin@device] /iot/gpio/digital> set pin5 script=script1 
[admin@device] /iot/gpio/digital> print                  
Flags: X - disabled 
 #   NAME                     DIRECTION OUTPUT INPUT SCRIPT                    
 0   pin5                     input     0      0     script1                   
 1   pin4                     output    0            script1                   
 2   pin6                     output    0     
```

在上面的示例中，電子郵件通知指令碼名為 "script1"。

因此，每當輸入值發生變化（從 0 到 1 或從 1 到 0）時，指令碼會自動啟動電子郵件通知，並在郵件正文中顯示輸入值。

不要忘記更改指令碼行，並相應地配置電子郵件設定（[/tool/e-mail](../../system-information-and-utilities/e-mail.md)）：

```ros
/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name]"  body="$[/iot/gpio/digital/get pin5 input]"
```

配置你實際使用的電子郵件地址。你也可以根據需要更改郵件主題和正文。

*MQTT 釋出指令碼：*

```ros
:local broker "name"
:local topic "topic"
:local message "\{\"inputVALUE\":$[/iot/gpio/digital/get pin5 input]}"  
/iot/mqtt/publish broker=$broker topic=$topic message=$message
```

此指令碼的工作方式與“*電子郵件通知*”指令碼相同，只是當輸入值變化時，指令碼會啟動 MQTT 釋出（而不是電子郵件通知），並以 JSON 格式傳送在引腳上接收到的輸入值。

不要忘記事先設定 MQTT broker (*`/iot/mqtt/brokers/add` ..*) 並修改幾行指令碼：

```ros
:local broker "name"
```

broker 的 "name" 應相應地更改（你可以使用 CLI 命令 /*iot mqtt brokers print* 檢視所有已建立的 broker 及其名稱）。

```ros
:local topic "topic"
```

topic 也應更改。topic 本身是在伺服器端配置的，因此請確保使用正確的 topic。

不要忘記將指令碼應用/設定到 pin5（/iot/gpio/digital/set pin5 script=script\_name），如上面的 "電子郵件通知" 示例所示。

如果使用機械開關向 GPIO 引腳傳送訊號，建議改用以下指令碼（以防在引腳上接收到訊號時指令碼被多次啟動）：

```ros
:global gpioscriptrunning;  
if (!$gpioscriptrunning) do=\{:set $gpioscriptrunning true;  
:log info "script started - GPIO changed";  
:do \{if ([/iot/gpio/digital/get pin5 input] = "0") do=\{/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name]" body="pin5 received logical 0"} else \{/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name]"  body="pin5 received logical 1"};  
:delay 1s;  
:set $gpioscriptrunning false} on-error=\{:set $gpioscriptrunning false;  
:log info "e-mail error, resetting script state..."}}
```

如果 GPIO 引腳狀態在毫秒/微秒內變化多次——上面的指令碼將確保電子郵件通知不會發送多次。

#### 監控電壓 {#monitoring-voltage}

最後但同樣重要的是使用模擬引腳“監控電壓”。你需要一個指令碼，按計劃讀取/監控電壓，然後透過電子郵件、MQTT 或 HTTPS (fetch) 傳送資料。

建立如下所示的指令碼。在此示例中，我們將使用 MQTT 釋出（但你可以建立類似的指令碼，使用 "/tool/e-mail .." 來發送電子郵件通知）：

```ros
:local broker "name"
:local topic "topic"
:local message "\{\"voltage(mV)\":$[/iot/gpio/analog/get pin3 value]}"  
/iot/mqtt/publish broker=$broker topic=$topic message=$message
```

該指令碼將讀取/測量 pin3 上的電壓，並將資料釋出到 MQTT broker。

不要忘記事先設定 MQTT broker (*`/iot/mqtt/brokers/add` ..*) 並修改幾行指令碼：

```ros
:local broker "name"
```

broker 的 "name" 應相應地更改（你可以使用 CLI 命令 `/iot/mqtt/brokers/print` 檢視所有已建立的 broker 及其名稱）。

```ros
:local topic "topic"
```

topic 也應更改。topic 本身是在伺服器端配置的，因此請確保使用正確的 topic。

儲存指令碼並將其命名為例如 "voltagepublish"。要自動化此過程，你可以使用[排程器](../../system-information-and-utilities/scheduler.md)。

```ros
[admin@device] /system/scheduler> add name=run-45s interval=45s on-event="voltagepublish"
```

上面顯示的排程配置將每隔 45 秒執行該指令碼。
