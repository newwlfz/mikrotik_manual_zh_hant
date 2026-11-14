---
sidebar_key: "wireless/abgn/wireless-troubleshooting"
sidebar_position: 8
title: "無線故障排查"
sidebar_label: "無線故障排查"
description: "本頁介紹如何透過啟用並分析詳細的偵錯日誌來排查 MikroTik RouterOS 中的無線連線問題，這些日誌涵蓋用戶端連線、斷開連線以及 MIC 故障或雷達檢測等安全事件。"
tags:
  - 'wireless'
  - 'debug-logs'
  - 'station-mode'
source: https://manual.mikrotik.com/docs/7.24/wireless/abgn/wireless-troubleshooting
captured_at: '2026-11-04T11:35:36+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 無線偵錯日誌 {#wireless-debug-logs}

使用日誌偵錯無線問題。

預設情況下，RouterOS 無線日誌以簡單條目顯示用戶端連線和斷開：

```ros
22:32:18 wireless,info 00:80:48:41:AF:2A@wlan1: connected
```

對於普通使用者來說，知道 MAC 地址為 "00:80:48:41:AF:2A" 的無線用戶端已連線到無線介面 "wlan1" 就足夠了。但實際上，可用的日誌條目比標準日誌記錄中顯示的更多。它們被稱為 'debug' 日誌，可提供更詳細的資訊。在下面的偵錯日誌示例中，你將看到同一個用戶端連線到 AP 的詳細過程，比典型日誌記錄中看到的資訊更多：

```ros
22:33:20 wireless,debug wlan1: 00:80:48:41:AF:2A attempts to connect
22:33:20 wireless,debug wlan1: 00:80:48:41:AF:2A not in local ACL, by default accept
22:33:20 wireless,info 00:80:48:41:AF:2A@wlan1: connected
```

偵錯日誌會為你提供用戶端無線連線和斷開過程中每個步驟的更具體資訊。第一行顯示無線用戶端嘗試連線到 AP。第二行顯示 AP 檢查該用戶端是否被允許連線到 AP，並顯示結果操作。只有第三行你才會看到用戶端已連線。這只是偵錯日誌訊息的一個示例。所有偵錯條目的說明寫在下面。

要啟用無線偵錯日誌，應執行以下命令：

```ros
[admin@MikroTik] > /system/logging                                            
[admin@MikroTik] /system/logging> add topics=wireless,debug action=memory
```

這將幫助你輕鬆理解和修復無線問題，並減少與支援團隊的互動。

### STATION 模式 {#station-mode}

```ros
<MAC>@<DEV>: lost connection, <REASON>
```

station 因 \<REASON\> 失去了與 AP 的連線。

```ros
<MAC>@<DEV>: failed to connect, <REASON>
```

station 嘗試連線到 AP，但由於 \<REASON\> 而失敗。

```ros
<MAC>@<DEV>: established connection on <FREQ>, SSID <SSID>
```

station 嘗試併成功連線到 SSID 為 \<SSID\>、頻率為 \<FREQ\> 的 AP。

```ros
<MAC>@<DEV>: MIC failure!!!
```

TKIP 訊息完整性檢查失敗，肯定有人試圖入侵或對網路進行 DOS 攻擊。如果在 60 秒內遇到超過 1 次 MIC 失敗，就會進入 "TKIP countermeasures" 狀態。

```ros
<MAC>@<DEV>: enter TKIP countermeasures
```

已進入 TKIP countermeasures 狀態，這意味著 station 將與 AP 斷開連線並保持靜默 60 秒。

### AP 模式 {#ap-mode}

```ros
<DEV>: radar detected on <FREQ>
```

在頻率 \<FREQ\> 上檢測到雷達，AP 將尋找另一個通道。

```ros
<DEV>: data from unknown device <MAC>, sent deauth [(XXX events suppressed, YYY deauths suppressed)]
```

收到了來自未知裝置（即未註冊到此 AP）且 MAC 地址為 \<MAC\> 的資料幀，AP 向其傳送了取消認證幀（按照 802.11）。XXX 是未記錄的事件數量，這樣日誌不會變得過大（在前 5 條之後，日誌限制為每 5 秒 1 條條目），YYY 是本應傳送但未傳送的取消認證幀數量，這樣就不會浪費資源傳送過多取消認證幀（每秒只允許 10 個取消認證幀）。

此類訊息的可能原因是，之前連線到該 AP 的 station 仍在向 AP 傳送資料，而 AP 尚不知道它已從 AP 登錄檔中被移除。取消認證訊息會告訴 station 它不再處於連線狀態。

```ros
<DEV>: denying assoc to <MAC>, failed to setup compression
```

在 AP 上初始化壓縮失敗，最可能是因為嘗試連線並使用壓縮的用戶端太多。

```ros
<DEV>: <MAC> is new WDS master
```

WDS slave 已與 WDS master 建立連線，這意味著 WDS slave 開始接受用戶端並充當 AP。

```ros
<DEV>: <MAC> was WDS master
```

此訊息在失去與 \<MAC\> 的連線後出現，這意味著 WDS slave 將斷開所有用戶端，並開始掃描以尋找新的 WDS master。

```ros
<MAC>@<DEV>: connected [, is AP][, wants WDS]
```

地址為 \<MAC\> 的 station 已連線。如果存在 "is AP"，則遠端裝置是 AP；如果存在 "wants WDS"，則遠端裝置希望建立 WDS 鏈路。

```ros
<MAC>@<DEV>: disconnected, <REASON>
```

與地址為 \<MAC\> 的 station 的連線因 \<REASON\> 而終止。

```ros
<DEV>: TKIP countermeasures over, resuming
```

TKIP countermeasures（60 秒靜默期）已結束，AP 恢復充當 AP。

```ros
<DEV>: starting TKIP countermeasures
```

進入 TKIP countermeasures 狀態（60 秒靜默期），所有用戶端都將丟失連線。

### \<REASON\> {#}

**"joining failed"** - 只會在 station 模式下的 Prism 卡上發生，因某種原因未能連線到 AP。

**"join timeout"** - 在 station 上發生，未能與 AP 同步（接收第一個 beacon 幀）。最可能是訊號弱、遠端關閉、強幹擾，或其他導致通訊無法進行的 RF 相關問題。

**"no beacons"** - 未從 WDS 鏈路的遠端收到 beacon。最可能是訊號弱、遠端關閉、強幹擾，或其他導致通訊無法進行的 RF 相關問題。

**"extensive data loss"** - 本地介面決定斷開與遠端裝置的連線，因為在最低可能速率下多次失敗後仍無法向遠端傳送資料。可能原因 - 訊號太弱、遠端裝置關閉、強幹擾，或其他導致通訊無法進行的 RF 相關問題。

**"decided to deauth, \<802.11 reason\>"** - 本地介面決定使用 802.11 原因 \<802.11 reason\> 對遠端裝置進行取消認證。

**"inactivity"** - 遠端裝置長時間處於非活動狀態。

**"device disabled"** - 本地介面被停用。

**"got deauth, \<802.11 reason\>"** - 從遠端裝置收到取消認證幀，802.11 原因程式碼在 \<802.11 reason\> 中報告。

**"got disassoc, \<802.11 reason\>"** - 從遠端裝置收到解除關聯幀，802.11 原因程式碼在 \<802.11 reason\> 中報告。

**"auth frame from AP"** - 來自已知為 AP 的遠端裝置的認證幀，最可能是遠端裝置從 AP 模式切換到 station 模式。

**"bad ssid"** - WDS 鏈路的 ssid 無效。

**"beacon from non AP"** - 從已知為非 AP 節點的遠端裝置收到 beacon 幀，最可能是遠端裝置從 station 模式切換到 AP 模式。

**"no WDS support"** - 未報告 WDS 支援。

**"failed to confirm SSID"** - 未能確認 WDS 鏈路另一端的 SSID。

**"hardware failure"** - 某些硬體故障或意外行為。不太可能出現。

**"lost connection"** - 只會在 station 模式下的 Prism 卡上發生，因某種原因失去了與 AP 的連線。

**"auth failed \<802.11 status\>"** - 在 station 上發生，AP 拒絕認證，802.11 狀態程式碼在 \<802.11 status\> 中報告。

**"assoc failed \<802.11 status\>"** - 在 station 上發生，AP 拒絕關聯，802.11 狀態程式碼在 \<802.11 status\> 中報告。

**"auth timeout"** - 在 station 上發生，station 未收到認證幀的響應，要麼鏈路不良，要麼 AP 因某種原因忽略此 station。

**"assoc timeout"** - 在 station 上發生，station 未收到關聯幀的響應，要麼鏈路不良，要麼 AP 因某種原因忽略此 station。

**"reassociating"** - 在 AP 上發生，假定連線已丟失，因為被認為已關聯的 station 嘗試再次關聯。必須刪除所有與連線相關的資訊，因為在關聯過程中會協商連線引數（因此為 "disconnected"）。必須在 station 上查詢 station 重新關聯的原因（最可能的原因是 station 因某種原因在未告知 AP 的情況下斷開了連線 - 例如資料丟失、配置更改）。

**"compression setup failure"** - 無法連線，因為沒有足夠資源進行壓縮（已經有太多希望使用壓縮的 station 連線）。

**"control frame timeout"** - AP 無法向用戶端傳輸（類似於你在 802.11 協定中看到的錯誤訊息 - extensive data loss）。

### \<802.11 reason\> 和 \<802.11 status\> {#-and-}

這些是編碼到 802.11 管理訊息中的數字原因/狀態程式碼。日誌訊息包含數字程式碼以及來自 802.11 標準組中相應標準的文字描述。儘管這些描述旨在儘可能具有描述性，但必須考慮到，管理幀中出現的實際原因/狀態程式碼完全取決於裝置或軟體製造商 - 一個裝置傳送的 802.11 管理幀可能包含與導致該幀的情況相對應的正確原因/狀態程式碼，而另一個裝置可能傳送帶有 "unspecified" 原因/狀態程式碼的幀。因此，原因/狀態程式碼只應被視為參考資訊。

隨著 802.11 標準的發展，RouterOS 可能會缺少某些裝置使用的 reason/status 程式碼的文字描述。在這種情況下，應使用數值在 802.11 標準中查詢含義。

為了正確解釋原因/狀態程式碼，必須很好地理解 802.11 組標準。大多數文字描述本身就能說明問題。以下是一些最常見原因/狀態程式碼的說明：

- **class 2 frame received (6)** - 裝置在完成 802.11 認證過程之前收到了 "class 2" 幀（關聯/重關聯管理幀）；

- **class 3 frame received (7)** - 裝置在完成關聯過程之前收到了 "class 3" 幀（資料幀）。

## 無線常見問題 {#wireless-faq}

### 設定 {#settings}

**為什麼我無法使用 Apple Mac 裝置連線到 MikroTik 802.11n AP？**

此問題僅出現在基於 Broadcom 無線晶片組的 Mac 裝置上。要使用此類無線裝置連線到 MikroTik 802.11n AP，請確保不要使用 'short' preamble-mode。使用 'long' 或 'both' preamble-mode，Mac 無線裝置就能連線。

**更改某些無線設定後，無線鏈路工作不穩定。**

有時，當你更改某些無線設定來調優鏈路時，會改到鏈路不再建立或工作不穩定的程度，而且你不記得最初的設定是什麼。在這種情況下，你可以使用無線選單中的 *reset-configuration* 命令 - 它會重設特定無線介面的所有無線設定，你將能夠從頭開始配置該介面。請注意，執行此命令還會停用介面，因此如果你正透過想要重設其配置的那條無線鏈路遠端配置路由器，請小心不要執行此命令。

**什麼是無線重傳，在哪裡檢查它們？**

當介面發出一個幀但沒有收到確認（ACK）時，就會發生無線重傳，導致它再次嘗試傳送該幀，直到收到確認或達到封包允許的最大重傳次數。無線重傳會增加無線鏈路的延遲並降低吞吐量。發生的重傳次數可以透過用登錄檔中給定條目的 **hw-frames** 引數值減去 **frames** 引數值來確定。一定數量的重傳是預期之內的，但如果 **hw-frames** 的值多次超過 **frames** 的值，則無線鏈路存在問題，需要進行故障排除。

**我也可以在 Nstreme 鏈路上比較 frames 與 hw-frames 嗎？**

**frames** 只統計包含實際資料的幀。在 Nstreme 的情況下，如果沒有其他資料要傳送，單個幀中只能傳輸 ACK。這些 ACK 幀不會計入 **frames** 計數，但會出現在 **hw-frames** 中。如果兩個方向都以最大速度有流量（例如不會出現僅含 ACK 的幀），那麼你就不能像普通無線鏈路那樣比較 **frames** 與 **hw-frames**。

**我可以使用哪些 TX-power 值？**

tx-power 預設設定是網路卡可以使用的最大 tx-power，取自網路卡的 eeprom。如果你想使用更大的 tx-power 值，可以設定它們，但 **請自行承擔風險**，因為這最終可能會損壞你的網路卡！通常，應僅使用此引數來降低 tx-power。

一般來說，tx-power 控制屬性應保留為預設設定。更改預設設定在某些情況下可能對某些網路卡有幫助，但如果不進行測試，最常見的結果是範圍和吞吐量下降。可能出現的一些問題包括：

- 網路卡功耗過高可能會使網路卡所在板卡的 3.3V 電源過載，導致電壓下降並重啟，或使板卡溫度過高。

**哪種 TX-power-mode 最好？**

*TX-power-mode* 告訴無線網路卡應使用哪些 tx-power 值。預設情況下，此設定設為 *default*。

- **all-rates-fixed** 表示網路卡將對所有資料速率使用一個 tx-power 值，該值由使用者在 *tx-power* 欄位中指定。

請注意，不建議使用 'all-rates-fixed' 模式，因為無線網路卡在較高資料速率下的 tx-power 較低，強制較高資料速率也使用固定 tx-power 速率可能會導致與上一個關於 tx-power 設定的問題中相同的問題。對於 MikroTik Radio 裝置，功率不會高於寫入 EEPROM 的功率。在大多數情況下，如果你想更改 tx-power 設定，建議使用 *tx-power-mode=card-rates*，並且建議降低而不是提高 tx-power。對於 AR9300 及更新的 Atheros 無線晶片組，"tx-power-mode=all-rates-fixed" 是唯一選項，因為 "card-rates" 選項在這些晶片組上不起作用。

**什麼是 CCQ，這些值如何確定？**

用戶端連線質量（CCQ）是一個百分比值，表示相對於理論最大可用頻寬，頻寬被有效利用的程度。CCQ 是對每個已傳送幀計算出的 Tmin/Treal 值的加權平均值，其中 Tmin 是在無重試的情況下以最高速率傳送給定幀所需的時間，Treal 是實際傳送該幀所用的時間（考慮傳送該幀所需的重試次數和傳送速率）。

**hw-retries 設定是什麼？**

傳送幀重試而不將其視為傳輸失敗的次數。失敗時會降低資料速率並再次傳送該幀。在最低支援速率上連續三次失敗後，會在 *on-fail-retry-time* 期間暫停向該目標傳輸。之後，會再次傳送該幀。該幀會一直重傳，直到傳輸成功，或在 *disconnect-timeout* 之後用戶端斷開連線。在此期間，如果超過 *frame-lifetime*，該幀可能會被丟棄。在 Nstreme 的情況下，不使用 "on-fail-retry-time"、"disconnect-timeout" 和 "frame-lifetime" 設定。因此，在最低支援速率上連續三次失敗後，無線鏈路會斷開並顯示 "extensive data loss" 訊息。

**disconnect-timeout 設定是什麼？**

此間隔從最低資料速率上的第三次傳送失敗開始計算。此時，最低資料速率上的 3 \* (*hw-retries* + 1) 次幀傳輸已經失敗。在 *disconnect-timeout* 期間，將按 *on-fail-retry-time* 間隔重試封包傳輸。如果在 *disconnect-timeout* 期間沒有任何幀能夠成功傳輸，則關閉連線，並將此事件記錄為 "extensive data loss"。成功傳輸幀會重設此計時器。

**adaptive-noise-immunity 設定是什麼？**

自適應噪聲免疫（ANI）會動態調整各種接收器引數，以儘量減少干擾和噪聲對訊號質量的影響。此設定已新增到 Atheros AR5212 及更新晶片組網路卡的無線驅動程式中。

**當使用 access-list 或 connect-list 時，無線裝置如何測量訊號強度？**

報告的訊號電平是平滑因子為 50% 的指數加權移動平均值。

**RouterOS 無線支援哪些糾錯方法？**

Nstreme 協定支援 ARQ 方法。常規 802.11 標準不包括 ARQ - 損壞幀的重傳基於確認協定。RouterOS 支援編位元速率為 1/2、2/3 或 3/4 的前向糾錯編碼（卷積編碼）。

**為 160MHz 使用配置 RouterOS 裝置。**

如果 RouterOS 裝置支援 4x4 傳輸，除了設定 160MHz 通道寬度外，請確保在無線介面上設定 "rate-set=default"，以便所有流都可用

如果用戶端不支援 Extended NSS 且只能執行 2x2 傳輸，請設定 "vht-supported-mcs=mcs0-9,mcs0-9,none"。

### 配置 {#setups}

**放大器會提高我鏈路的速率嗎？**

這取決於你的訊號質量和噪聲。請記住，使用低輸出功率設定和良好的天線，你很可能獲得更好的鏈路。放大器會增加噪聲，只會給鏈路帶來問題。

放大器會同時增強發射 **和** 接收訊號。因此，在“安靜”區域，也就是你獨自使用或“噪聲”/“競爭”很少的地方，你可能會獲得極好的結果。另一方面，在擁擠區域，無線活動很多，你也會增強從其他每個競爭者或噪聲源接收到的訊號，這可能會大幅降低鏈路的整體質量。另外，還要考慮 EIRP，以確認你的鏈路是否仍在合法限制內。

在 "11b only" 無線裝置上，你也可能獲得更好的訊號，這些裝置會將大部分 802.11g 視為 "noise"，從而更好地過濾可用訊號。

**如何使用 hw-retries 微調無線鏈路？**

你應該瞭解，對於 802.11 裝置，可用於調整其行為的資訊（或來自環境的“反饋”）非常有限：

- 透過是否收到已傳送幀的確認。

考慮到使用訊號強度並不可靠，802.11 裝置實際上只剩下一個“反饋”來調整其操作 - 傳輸成功/失敗。當傳輸失敗（未及時收到 ACK）時，傳送方無法查明失敗原因 - 是因為噪聲、多徑、直接干擾（以及干擾的是實際資料幀還是 ACK 本身）- 幀就是沒有成功送達，而且一般來說“為什麼”並不重要。重要的是封包錯誤率。

因此，RouterOS 實現了一種演算法，僅使用這些有限資訊，嘗試在任何環境中最高效地使用介質，同時讓使用者能夠控制該演算法的工作方式，並對該演算法進行描述。並且只有少量使用指南，而不是一套在特定情況下應使用的值。

一般來說 - *hw-retries* 越大，裝置獲得的關於介質以特定速率傳送幀的能力的“反饋”就越好（例如，如果以 54mbps 速率傳送幀失敗 16 次，這比失敗 2 次重試告訴你的資訊更多），並且它就越能找出最佳傳輸速率，但代價是可能給網路引入延遲 - 因為在所有這些失敗重試期間，此通道中的其他裝置無法傳送。因此，對於 ptp 骨幹鏈路（已知鏈路必須始終開啟），可以建議使用**更大**的 *hw-retries*。**更小**的 *hw-retries* 會使速率選擇適應得更快，但會犧牲一些準確性（在大多數情況下低於 2 不合理），這可以建議用於 ptmp 鏈路，在這種鏈路中連線/斷開是正常的，並且保持低延遲很重要。

*on-fail-retry-time* 和 *disconnect-timeout* 控制裝置在多大程度上嘗試將遠端方視為“已連線”。較大的 *disconnect-timeout* 會使裝置即使在最小可能傳輸速率下存在大量丟包，也不“斷開”另一方。這同樣對已知“必須”建立的“弱”鏈路最有用（例如骨幹鏈路）。在 ptmp 網路中，較大的 *disconnect-timeout* 同樣會在例如 AP 嘗試向某個剛被停用的用戶端傳送資料期間增加網路延遲（AP 會在整個 *disconnect-timeout* 期間嘗試這樣做）。

*frame-lifetime* 可用於調整 AP 在認為某個幀不值得傳送之前嘗試使用該幀進行傳輸的時間（例如，如果在最低可能速率下發送幀失敗，則會啟用 *on-fail-retry-time* 計時器。如果在此期間 *frame-lifetime* 到期，則該特定幀會被丟棄，下一次傳輸嘗試將使用下一個幀進行。停用 *frame-lifetime* 意味著無線將確保“所有”資料幀按順序傳送，無論需要多長時間，或者如果一切失敗則“斷開”連線）。這可以針對不同型別的流量進行最佳化，例如，對於即時流量 - 如果無線網路的主要用途是 voip，那麼限制 *frame-lifetime* 可能是合理的，因為 voip 對少量丟包的容忍度高於高延遲。

**是否可以僅使用一個無線介面來使用無線中繼器？**

這種配置可以透過在運行於 ap-bridge 模式的無線介面上使用 WDS 來實現。在較新的 RouterOS 版本中，可以配置無線中繼模式。

**Nv2 無線鏈路經常斷開。**

當 Nv2 無線鏈路出現斷開，並且日誌部分中的大多數訊息都是 'control frame timeout' 時，如果鏈路訊號很強，你可以嘗試降低無線網路卡的發射輸出功率。我們建議使用 tx-power-mode=card-rates 來降低無線網路卡的 tx-power。如果問題仍然存在，請嘗試使用可能干擾更少的其他無線頻率。如果這也沒有幫助，請透過 [support@mikrotik.com](mailto:support@mikrotik.com) 聯絡支援，並提供受影響的 AP 和 station 在那些斷開之後生成的支援輸出檔案。
