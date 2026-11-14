---
sidebar_key: "mobile-networking/sms"
sidebar_position: 4
title: "簡訊"
sidebar_label: "簡訊"
description: "本頁介紹 MikroTik RouterOS 中的 SMS 功能，可透過 AT 命令實現 GSM 調變解調器通訊，以傳送和接收 SMS 訊息。內容涵蓋傳送方式、port、電話號碼、訊息編碼等引數，以及用於與網路運營商互動的 USSD 訊息支援。"
tags:
  - 'sms'
  - 'at-commands'
  - 'modem'
source: https://manual.mikrotik.com/docs/7.25/mobile-networking/sms
captured_at: '2026-11-04T11:20:32+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

可以將 GSM 調變解調器連線到 RouterOS 裝置，並使用它收發簡訊。RouterOS 會將此類調變解調器列為序列埠，並出現在 `/port/print` 列表中。GSM 標準定義了用於傳送簡訊的 AT 命令，以及在這些命令中訊息應如何編碼。`'/tool/sms/send'` 使用標準 GSM AT 命令傳送簡訊。

## 傳送 {#sending}

**子選單：** `/tool/sms/send`

### **示例** {#example}

為 ppp 介面傳送命令：

```ros
/tool/sms/send usb3 "20000000" \ message="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#\$%^&*(){}[]\"'~"
```

對於 LTE 介面，請在 port 欄位中使用 LTE 介面名稱：

```ros
/tool/sms/send lte1 "20000000" \ message="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#\$%^&*(){}[]\"'~"
```

| 引數 | 說明 |
| :-- | :-- |
| **port** (*string*) | GSM 調變解調器所連線的 `/port` 中的埠名稱。 |
| **phone-number** (*string*) | 接收方電話號碼。允許的字元為 "0123456789\*#abc"。如果第一個字元為 "+"，則電話號碼型別設定為 *international*，否則設定為 *unknown*。 |
| **channel** (*integer*) | 用於傳送的調變解調器通道。 |
| **message** (*string*) | 訊息內容。使用 GSM 7 編碼（當前不支援 UCS2），因此訊息長度限制為 160 個字元。字元 `^{}\\[]~` 是擴充套件的 GSM 7 位字元，每個佔用兩個字元位置，因此出現這些字元時有效上限會低於 160。 |
| **smsc** (*string*) |  |
| **type** (*string*) | 如果設定為 *class-0*，則傳送 class 0 簡訊。該訊息會立即顯示，且不會儲存在手機中。 |
| **sms-storage** (*string*) | 選擇儲存接收簡訊的儲存位置（modem/sim） |
| **status-report-request** (*yes \| no*；預設：yes) | 設定為 "no" 則不請求確認訊息，該確認訊息用於指示簡訊是否已成功傳送給接收方。 |

## USSD 訊息 {#ussd-messages}

USSD（Unstructured Supplementary Service Data，非結構化補充業務資料）訊息可用於與行動網路運營商通訊，以獲取附加資訊、開通附加服務或為預付費卡充值。可以透過 AT 命令處理 USSD 訊息（不同調制解調器的命令可能不同，某些調變解調器甚至可能遮蔽這些命令）。

**要使用此功能，必須啟用 3G 或 GSM 網路模式**，因為僅在 LTE 模式下不支援該功能（**R11e-LTE** 調變解調器會自動切換到 3G 模式以傳送 USSD 訊息）。

PDU（Protocol Data Unit，協定資料單元）訊息及其解密後的版本會列印在 LTE 偵錯日誌中。

### **示例** {#example-1}

檢查 LTE 偵錯日誌是否已啟用：

```ros
/system/logging/print
Flags: X - disabled, I - invalid, * - default 
# TOPICS ACTION PREFIX 
0 * info memory 
1 * error memory 
2 * warning memory 
3 * critical echo 
```

如果沒有日誌條目，請執行以下命令新增：

```ros
/system/logging/add topics=lte,!raw

/system/logging/print
Flags: X - disabled, I - invalid, * - default 
# TOPICS ACTION PREFIX 
0 * info memory 
1 * error memory 
2 * warning memory 
3 * critical echo 
4 lte,!raw memory 
```

從 **\*245#** 獲取賬戶狀態

```ros
/interface/lte/at-chat lte1 input="AT+CUSD=1,\"*245#\",15"
output: OK
/log/print
11:51:20 lte,async lte1: sent AT+CUSD=1,"*245#",15 
11:51:20 lte,async lte1: rcvd OK 
11:51:23 lte,async,event +CUSD: 0,"EBB79B1E0685E9ECF4BADE9E03", 0 
11:51:23 gsm,info USSD: konta atlikums
```

## 接收 {#receiving}

RouterOS 也支援接收簡訊，可以執行指令碼，甚至可以回覆傳送方。

在路由器能夠接收簡訊之前，需要在 `/tool/sms` 選單中進行相關配置。可配置以下引數：

| 引數 | 說明 |
| :-- | :-- |
| **allowed-number** (*string*；預設："") | 允許執行命令的傳送方號碼，必須指定國家程式碼，例如 +371XXXXXXX |
| **channel** (*integer*；預設：**0**) | 用於接收的調變解調器通道。 |
| **keep-max-sms** (*integer*；預設：**0**) | 將儲存的最大訊息數量。如果設定的值超過 SIM 卡支援的數量，則不會接收到新訊息。從 RouterOS v6.44.6 起，該引數已被 `auto-erase` 引數取代 |
| **auto-erase** (*yes \| no*；預設：**no**) | SIM 儲存大小會被自動讀取。當 `auto-erase=no` 時，如果儲存已滿，則不會接收新簡訊。設定 `auto-erase=yes` 可自動刪除最舊的已接收簡訊，為新簡訊騰出空間。從 v6.44.6 起可用 |
| **port** (*string*；預設：(**unknown**)) | 調變解調器埠（調變解調器只能被一個程式使用 "/port> print"） |
| **receive-enabled** (*yes \| no*；預設：**no**) | 必須開啟才能接收訊息 |
| **secret** (*string*；預設："") *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 金鑰密碼，必填 |
| **polling**(*yes \| no*；預設：**no**) | 每 10 秒檢查調變解調器是否有新簡訊，而不是僅在收到來自調變解調器的命令後才更新收件箱。從 v7.16 起可用 |
| **sim-pin**(string；預設：) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | SIM 卡的 PIN 碼。 |

### 能夠檢視已接收訊息的基本示例配置 {#basic-example-configuration-to-be-able-to-view-received-messages}

```ros
/tool/sms/set receive-enabled=yes port=lte1

/tool/sms/print 
           status: running
  receive-enabled: yes
             port: lte1
          channel: 0
           secret: 
   allowed-number: 
       auto-erase: no
          sim-pin: 
        last-ussd: 
```

### **收件箱** {#inbox}

**子選單：** `/tool/sms/inbox`

如果已啟用接收功能，你將在此子選單中看到收到的訊息：

只讀屬性：

| 屬性 | 說明 |
| :-- | :-- |
| **phone** (*string*) | 傳送方的電話號碼。 |
| **message** (*string*) | 訊息正文 |
| **timestamp** (*time*) | 訊息接收時間。該時間是運營商傳送的時間，而非路由器的本地時間。 |
| **type** (*string*) | 訊息型別 |

### **語法** {#syntax}

```ros
 :cmd SECRET script NAME [[ VAR[=VAL] ] ... ]
```

- **SECRET** - 密碼
- **NAME** - 在 `/system/script` 中可用的指令碼名稱
- **VAR** - 將傳遞給指令碼的變數（可以以 VAR 或 VAR=value 形式傳遞），以空格分隔。

其他注意事項：

- \*如有必要，可以將引數放入引號中 "VAR"="VAL"。
- \*不支援對值進行轉義（VAR="\""）。
- \*不支援合併簡訊，每條簡訊都會被單獨處理。
- \* 不支援 16 位 Unicode 訊息。
- \* 簡訊使用標準 GSM7 字元集解碼，因此你不能使用其他編碼傳送，否則會被錯誤解碼。

### **示例** {#examples}

#### 錯誤 {#wrong}

```ros
:cmd script mans_skripts
:cmd slepens script mans skripts
:cmd slepens script mans_skripts var=
:cmd slepens script mans_skripts var= a
:cmd slepens script mans_skripts var=a a
```

#### 正確 {#right}

```ros
:cmd slepens script mans_skripts
:cmd slepens script "mans skripts"
:cmd slepens script mans_skripts var
:cmd slepens script mans_skripts var=a
:cmd slepens script mans_skripts var="a a" 
```

## 偵錯 {#debugging}

`/tool/sms/send` 命令會記錄寫入和讀取的資料。記錄使用的標籤為 *gsm,debug,write* 和 *gsm,debug,read*。更多資訊請參見 `/system/logging`。

## 實現細節 {#implementation-details}

使用 *AT+CMGS* 和 *AT+CMGF* 命令。在執行命令期間會佔用該埠，其他 RouterOS 元件無法同時使用該埠。訊息傳送過程可能耗時較長。在初始 AT 命令交換階段，超時時間為兩秒；之後超時時間為一分鐘。
