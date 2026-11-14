---
sidebar_key: "mobile-networking/bg77-modem-at-commands"
title: "BG77 調變解調器 AT 命令"
sidebar_label: "BG77 調變解調器 AT 命令"
source: https://manual.mikrotik.com/docs/mobile-networking/bg77-modem-at-commands
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

#

# 概述 {#overview}

本簡短指南將幫助您瞭解如何排查 CAT-M/NB-IoT 連線的問題/故障。使用調變解調器的 “AT” 命令可以獲取大量有關連線的資訊。按定義，“AT” 表示“attention”（注意）。每個命令字串都以 “AT” 為字首，並且在 “AT” 之後可以拼接多個獨立命令。

請檢視下面的示例，以更好地瞭解如何發起這些命令以及可以使用它們獲取哪些資訊。

:::info
 行動網路由 ISP 管理。如果連接出現任何問題，我們建議先聯絡 ISP，並首先確認他們支援/允許該連線或該設定。如果您決定（在未諮詢 ISP 的情況下）使用 AT 命令更改配置，則需自行承擔風險。
:::

## 發起 AT 命令 {#initiating-at-commands}

### 選項 A {#option-a}

要傳送命令，您必須使用 CLI。

開啟終端並輸入以下內容：

```ros
[admin@MikroTik] > system serial-terminal port=modem channel=2
```

請注意所使用的埠和通道。選擇 PPP-OUT 介面所使用的埠和通道。在我們的示例中，埠為 “modem”，資料通道為 “2”。

命令發起後，應顯示以下輸出，此時您可以輸入 AT 命令：

```ros
[admin@MikroTik] > system serial-terminal port=modem channel=2

[Ctrl-A is the prefix key]

at+cpin?
+CPIN: READY

OK 
```

在上面的示例中，使用了 AT 命令 “at+cpin?”，並收到應答 “+CPIN: READY”。

### 選項 B {#option-b}

傳送 AT 命令的第二種方式是透過 ppp-client 介面：

```ros
[admin@MikroTik] > interface ppp-client at-chat input="AT+CPIN\?"
number: 0
  output: +CPIN: READY
```

您可以獲得與 **選項 A** 相同的結果。

## AT 命令 {#at-commands}

### at {#at}

簡單的 ***at*** 命令用於檢查模組（裝置）與應用程式之間的通訊。

```ros
[Ctrl-A is the prefix key]

at

OK 
```

當返回 “OK” 時，表示模組已成功響應。

### at+cpin? {#atcpin}

此命令用於檢查 SIM 卡的狀態。

```ros
[Ctrl-A is the prefix key]

at+cpin?
+CPIN: READY

OK 
```

狀態 “+CPIN: READY” 表示 SIM 卡已正確安裝。

如果使用了 SIM PIN，您應收到應答 “+CPIN: SIM PIN” → 在這種情況下，您可以透過命令 ***at+cpin="xxxx"*** 解鎖，其中 ***xxxx*** 是 PIN 碼。

如果收到響應 “+CME ERROR: SIM not inserted” → 請再次確認 SIM 卡已正確安裝到 SIM 卡槽中。

### at+cfun? {#atcfun}

“CFUN” 命令用於檢查功能模式。此命令可能會有不同的響應。

```ros
[Ctrl-A is the prefix key]   

at+cfun?
+CFUN: 1

OK
```

當狀態為 “+CFUN: 1” 時，表示裝置已設定為完全功能模式。建議使用此模式。

在眾多其他響應中，例如，您可能會收到 “+CFUN: 4”，這表示裝置已設定為飛航模式，其中 Tx、Rx、LTE 和 GNSS 服務均被停用。

您可以使用命令 ***at+cfun=1*** 手動將模式設定為完全功能。

### at+cops? {#atcops}

**at+cops?** 命令用於檢查當前網路連線。

```ros
[Ctrl-A is the prefix key]      

at+cops?
+cops: 0,0,"LMT",8

OK
```

以以上示例為參考，我們可以看到收到了響應 “0,0,"LMT",8”。

響應中的第一個值決定使用的是“自動”還是“手動”模式。當 ISP 連線設定為“自動”時，該值將顯示為 “0”。當 ISP 連線設定為“手動”時，該值將顯示為 “1”。

響應中的第二個值表示 ISP 名稱格式。如果為 “0”，表示 ISP 名稱採用“長格式字母數字”。如果為 “1”，表示 ISP 名稱採用“短格式字母數字”。

響應的第三部分是 ISP 名稱本身。

響應的第四部分表示所使用的技術。“8” 代表 eMTC (CAT-M)，“9” 代表 NB-IoT。

### at+cops=? {#atcops-1}

**at+cops=?** 用於獲取所有可用 ISP 的列表。此命令可能需要一些時間（最多約 1 分鐘）才能顯示結果。

```ros
[Ctrl-A is the prefix key]      

at+cops=?
+cops: (1,"LMT","LMT","24701",9),(2,"LMT","LMT","24701",8),,(0,1,2,3,4),(0,1,2)

OK
```

您可以透過命令 ***at+cops=mode,format,"provider"*** 手動設定希望連線的 ISP，其中 ***mode*** 是所使用的模式（0→ 自動網路選擇；1→ 手動網路選擇），**format** 是 ISP 名稱格式（0→ 長字母數字格式；1→ 短字母數字格式；2→ 數字格式），而 “***provider***” 是 ISP 名稱（採用所選格式）。例如，要從列表中選擇網路，請使用命令 ***at+cops=1,1,"LMT"***。

要自動選擇 ISP，請使用命令 ***at+cops=0***。

### at+creg? {#atcreg}

***at+creg?*** 命令用於檢查網路註冊狀態。

```ros
[Ctrl-A is the prefix key]              

at+creg?
+CREG: 0,1

OK
```

第一個值顯示網路註冊非請求結果碼是啟用還是停用（0→ 停用，1→ 啟用；2→ 啟用 + 位置資訊）。第二個值顯示電路模式註冊狀態（0→ 未註冊/裝置未搜尋要註冊的運營商；1→ 已註冊/歸屬網路；2→ 未註冊，但正在嘗試搜尋要註冊的運營商；3→ 註冊被拒絕；4→ 未知；5→ 已註冊並漫遊）。

如果返回的值超過 2 個，表示網路註冊和位置資訊非請求結果碼已啟用。第二個值將以十六進位制格式顯示兩位元組的位置區碼，第三個值將以十六進位制格式顯示四位元組的 GERANE/E-UTRAN 小區 ID，最後一個值將顯示服務小區的接入技術（“8” 表示 CAT-M，“9” 表示 NB-IoT）。

### at+csq {#atcsq}

***at+csq*** 命令返回接收訊號強度指示（RSSI）和通道誤位元速率（BER）值。只有在網路註冊完成後，此命令才會返回正確的值。

```ros
[Ctrl-A is the prefix key]           

at+csq
+csq: 25,99

OK
```

第一個值是 RSSI (dBm)：

| 值 | RSSI |
| --- | --- |
| 0 | -113 dBm 或更低 |
| 1 | -111 dBm |
| 2-30 | -109 至 -53 dBm |
| 31 | -51 dBm 或更高 |
| 99 | 未知/無法檢測（未找到網路） |

第二個值是 BER (%)：

| 值 | BER |
| --- | --- |
| 0 | &lt; 0,2 % |
| 1 | 0,2 % &lt; 0,4 % |
| 2 | 0,4 % &lt; 0,8 % |
| 3 | 0,8 % &lt; 1,6 % |
| 4 | 1,6 % &lt; 3,2 % |
| 5 | 3,2 % &lt; 6,4 % |
| 6 | 6,4 % &lt; 12,8 % |
| 7 | 12,8 % &lt; |
| 99 | 未知/無法檢測 |

根據示例/輸出 “***+csq: 25,99***”，結果對應 RSSI~63 dBm，BER 引數無法檢測。

### at+qnwinfo {#atqnwinfo}

此命令返回有關接入技術、ISP 和所選頻段的資訊。只有在網路註冊完成後，此命令才會返回正確的資訊。

```ros
[Ctrl-A is the prefix key]              

at+qnwinfo
+QNWINFO: "eMTC","24701","LTE BAND 20",6300

OK
```

根據上面的示例，可以看到當前模組使用 “eMTC” (CAT-M)，ISP 為 “24701”（數字格式，代表 “LMT”），LTE Band 20，通道 ID 為 “6300”。

### at+qcsq {#atqcsq}

**at+qcsq** 命令返回有關當前 ISP 連線訊號強度以及所用技術的資訊。

```ros
[Ctrl-A is the prefix key]                 

at+qcsq
+QCSQ: "eMTC",-62,-87,111,-12

OK
```

返回的第一個引數是 “eMTC”，表示模組所使用的技術（CAT-M）。如果無法確定網路（不確定）→ 將返回 “NOSERVICE”。

其餘引數顯示連線的訊號強度。

當技術被識別為 “NBIoT” 或 “eMTC” (CAT-M) 時：

- 第一個數值顯示接收訊號強度（LTE RSSI）；
- 第二個值顯示參考訊號接收功率（LTE RSRP）；
- 第三個值顯示訊號與干擾加噪聲比（LTE SINR）→ 該值以 SINR 的對數值顯示，並且該值為 1/5 dB（結果可能在 0-250 範圍內，對應 -20 dB 至 +30 dB 範圍）；
- 第四個值顯示參考訊號接收質量（LTE RSRQ）。
根據上面的示例，RSSI=-62 dBm，RSRP=-87 dBm，SINR=111(111/5-20)~2 dB，RSRQ=-12 dB。

### at+qcfg="iotopmode"? {#atqcfgiotopmode}

此命令用於檢查連線 ISP 時使用哪種技術。調變解調器可以僅在 CAT-M 模式下工作、僅在 NB-IoT 模式下工作，或同時支援兩者。

```ros
[Ctrl-A is the prefix key]   

at+qcfg="iotopmode"?
+QCFG: "iotopmode",2

OK
```

您可以使用命令 ***at+qcfg="iotopmode"****,****mode***,***effect*** 將 SIM 卡鎖定為僅在特定模式下工作，其中 ***mode*** 是模式（0→ 僅 CAT-M；1→ 僅 NB-IoT；2→ 兩者），而 ***effect*** 是何時生效（0→ 重啟後生效；1→ 立即生效）。

為加快網路搜尋，建議執行命令 ***at+cfun=0***（關閉射頻），然後使用上述命令。之後，執行 ***at+cfun=1,1***（重新開啟射頻並重設模組以使其生效）。

### at+qcfg="band"? {#atqcfgband}

此命令用於檢查當前接受哪些頻段/頻率。

```ros
[Ctrl-A is the prefix key]   

at+qcfg="band"?
+QCFG: "band",0x0,0x100002000000000f0e189f,0x10004200000000090e189f

OK
```

“qcfg” 響應中的第一個值顯示一個十六進位制值，用於指定 **GSM 頻段**。此值與 Quectel BG77 模組無關。可以忽略此值。

第二個十六進位制值指定 **CAT-M 頻段**（即 0x100002000000000f0e189f）。如果設定為 0，表示不更改頻段。例如，如果為 0x15，則表示 → 0x01(LTE Band 1)+0x04(LTE Band 3)+0x10(LTE Band 5)。

| 值 | 頻段 |
| --- | --- |
| 0 | 不變 |
| 0x1 | LTE 頻段 1 |
| 0x2 | LTE 頻段 2 |
| 0x4 | LTE 頻段 3 |
| 0x8 | LTE 頻段 4 |
| 0x10 | LTE 頻段 5 |
| 0x80 | LTE 頻段 8 |
| 0x800 | LTE 頻段 12 |
| 0x1000 | LTE 頻段 13 |
| 0x20000 | LTE 頻段 18 |
| 0x40000 | LTE 頻段 19 |
| 0x80000 | LTE 頻段 20 |
| 0x1000000 | LTE 頻段 25 |
| 0x2000000 | LTE 頻段 26 |
| 0x4000000 | LTE 頻段 27 |
| 0x8000000 | LTE 頻段 28 |
| 0x20000000000000000 | LTE 頻段 66 |
| 0x1000000000000000000000 | LTE 頻段 85 |
| 0x100002000000000F0E189F | 上述所有受支援的頻段 |

最後一個十六進位制值指定 **NB-IoT 頻段**（即 0x10004200000000090e189f）。如果設定為 0，表示不更改頻段。例如，如果為 0x15，則表示 → 0x01(LTE Band 1)+0x04(LTE Band 3)+0x10(LTE Band 5)。

| 值 | 頻段 |
| --- | --- |
| 0 | 不變 |
| 0x1 | LTE 頻段 1 |
| 0x2 | LTE 頻段 2 |
| 0x4 | LTE 頻段 3 |
| 0x8 | LTE 頻段 4 |
| 0x10 | LTE 頻段 5 |
| 0x80 | LTE 頻段 8 |
| 0x800 | LTE 頻段 12 |
| 0x1000 | LTE 頻段 13 |
| 0x20000 | LTE 頻段 18 |
| 0x40000 | LTE 頻段 19 |
| 0x80000 | LTE 頻段 20 |
| 0x1000000 | LTE 頻段 25 |
| 0x8000000 | LTE 頻段 28 |
| 0x20000000000000000 | LTE 頻段 66 |
| 0x400000000000000000 | LTE 頻段 71 |
| 0x1000000000000000000000 | LTE 頻段 85 |
| 0x10004200000000090E189F | 上述所有受支援的頻段 |

您可以使用命令 ***at+qcfg="band",GSM_band,CAT_M_band,NB_IoT_band,effect*** 更改頻段，其中 ***GSM_band*** 是 GSM 頻段（可保留為 0x0），***CAT_M_band*** 是 CAT-M 頻段，***NB_IoT_band*** 是 NB-IoT 頻段，而 ***effect*** 表示是立即生效（1）還是在模組重啟後生效（0）。

要將模組設定為支援所有頻段，請使用以下命令：

```ros
[Ctrl-A is the prefix key]     

at+qcfg="band",0x0,0x100002000000000f0e189f,0x10004200000000090e189f,1

OK
```

為加快網路搜尋，建議執行命令 ***at+cfun=0***（關閉射頻），然後使用上述命令。之後，執行 ***at+cfun=1,1***（重新開啟射頻並重設模組以使其生效）。

### at+qgpscfg="priority",(0-1) {#atqgpscfgpriority0-1}

需要了解的是，透過 CAT-M/NB-IoT 進行的資料傳輸與 GNSS 無法同時工作（BG77 模組中的 WWAN 和 GNSS 接收鏈路共享某些硬體模組，這意味著該模組不支援 WWAN 和 GNSS 的併發操作。）。這就是引入 ***at+qgpscfg="priority",(0-1)*** 命令的原因。

可以使用以下命令更改優先順序：

```ros
[Ctrl-A is the prefix key]    

at+qgpscfg="priority",0

OK

at+qgpscfg="priority",1

OK
```

***at+qgpscfg="priority",0*** 命令將 **GNSS 優先順序設為最高**。

***at+qgpscfg="priority",1*** 命令將 **LTE (WWAN) 優先順序設為最高**。

當裝置處於 **LTE (WWAN) 優先順序模式** 時，只有在 RRC 釋放（Radio Resource Control 協定有許多功能，但主要負責連線建立及其釋放功能）且 LTE (WWAN) 進入空閒休眠模式時，GNSS 定位請求才能成功完成。只有在 eDRX 受支援且未被 ISP 阻止的條件下，LTE (WWAN) 和 GNSS 才能在 **LTE (WWAN) 優先順序模式** 下共存。如果網路連線建立（RRC 處於連線狀態）且資料開始流向伺服器 → GNSS 將被推遲，直到資料傳輸結束並且 RCC 釋放。如果 eDRX 受支援且模組進入此模式（資料傳輸結束）→ 將傳送 GNSS 座標。一旦資料再次開始流向伺服器，GNSS 將被推遲，直到裝置再次進入 eDRX 模式。

當裝置處於 **GNSS 優先順序模式** 時，GNSS 定位請求在所有 WWAN 狀態下都能成功。如果裝置處於 RCC 連線狀態 → 它將釋放 RCC 連線並啟動 GNSS 會話。之後，如果有 WWAN 資料要傳送 → 將再次發起 RCC 連線。
