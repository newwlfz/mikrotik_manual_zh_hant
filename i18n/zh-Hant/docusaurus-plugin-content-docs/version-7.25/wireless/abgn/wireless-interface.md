---
sidebar_key: "wireless/abgn/wireless-interface"
sidebar_position: 7
title: "無線介面"
sidebar_label: "無線介面"
description: "RouterOS 無線介面支援 IEEE 802.11 標準，具備全面的功能，包括多種模式（client、AP、bridge）、加密協定、通道寬度調整以及高階傳輸設定，以實現最佳無線網路效能。"
tags:
  - 'wireless'
  - 'arp'
  - 'channel-width'
source: https://manual.mikrotik.com/docs/7.25/wireless/abgn/wireless-interface
captured_at: '2026-11-04T11:24:00+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

---

## 概述 {#overview}

**包：** wireless

RouterOS 無線遵循 IEEE 802.11 標準。它提供對 802.11a、802.11b、802.11g、802.11n 和 802.11ac 的完整支援，以及 WPA、WEP、AES 加密、無線分佈系統（WDS）、動態頻率選擇（DFS）、虛擬接入點、Nstreme 和 Nv2 專有協定等附加功能，以及更多功能。

無線可以工作在多種模式下：用戶端（站）、接入點、無線網橋等。用戶端/站也可以工作在不同的模式下。支援的完整模式列表見 [無線站模式](../user-guides/wireless-station-modes.md)。

## 常規介面屬性 {#general-interface-properties}

**子選單：** `/interface/wireless`

| 屬性 | 描述 |
| :-- | :-- |
| **adaptive-noise-immunity** (*ap-and-client-mode \| client-mode \| none*; 預設值：**none**) | 此屬性僅對基於 Atheros 晶片組的卡有效。 |
| **allow-sharedkey** (*yes \| no*; 預設值：**no**) | 允許 WEP 共享金鑰用戶端連線。注意，這些用戶端不會進行身份驗證（WEP 共享金鑰不會與任何內容進行比較）——它們會被立即接受（如果訪問列表允許）。 |
| **ampdu-priorities** (*list of integer [0..7]*; 預設值：**0**) | 應協商並使用 AMPDU 傳送（聚合幀並使用塊確認傳送）的幀優先順序。使用 AMPDU 將提高吞吐量，但可能增加延遲，因此可能不適合即時流量（語音、影片）。因此，預設情況下 AMPDU 僅對盡力而為流量啟用。 |
| **amsdu-limit** (*integer [0..8192]*; 預設值：**8192**) | 協商時允許裝置準備的最大 AMSDU。AMSDU 聚合可顯著提高吞吐量，尤其是對小幀，但在因重傳聚合幀而丟包時可能增加延遲。傳送和接收 AMSDU 也會增加 CPU 使用率。 |
| **amsdu-threshold** (*integer [0..8192]*; 預設值：**8192**) | 允許包含在 AMSDU 中的最大幀大小。 |
| **antenna-gain** (*integer [0..4294967295]*; 預設值：**0**) | 天線增益，單位為 dBi，用於根據 **country** 法規計算最大發射功率。 |
| **antenna-mode** (*ant-a \| ant-b \| rxa-txb \| txa-rxb*; 預設值： ) | 選擇用於傳送和接收的天線*ant-a* - 僅使用 'a' 天線*ant-b* - 僅使用 'b' 天線*txa-rxb* - 使用天線 'a' 傳送，天線 'b' 接收*rxa-txb* - 使用天線 'b' 傳送，天線 'a' 接收 |
| **area** (*string*; 預設值： ) | 標識無線網路組。此值由 AP 通告，並可在  [connect-list](./wireless-interface.md#connect-list)  中透過 **area-prefix** 匹配。這是一個專有擴充套件。 |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; 預設值：**enabled**) | [ARP](../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together) |
| **arp-timeout** (*auto \| integer*; 預設值：**auto**) | ARP 超時是指在一段時間內未從 IP 收到封包後，ARP 記錄在 ARP 表中保留的時長。值 **auto** 等於 **/ip/settings** 中 **arp-timeout** 的值，預設為 30s |
| **band** (*2ghz-b \| 2ghz-b/g \| 2ghz-b/g/n \| 2ghz-onlyg \| 2ghz-onlyn \| 5ghz-a \| 5ghz-a/n \| 5ghz-onlyn \| 5ghz-a/n/ac \| 5ghz-onlyac \| 5ghz-n/ac*; 預設值： ) | 定義使用的資料速率、通道頻率和寬度集合。 |
| **basic-rates-a/g** (*12Mbps \| 18Mbps \| 24Mbps \| 36Mbps \| 48Mbps \| 54Mbps \| 6Mbps \| 9Mbps*; 預設值：**6Mbps**) | 與 **basic-rates-b** 屬性類似，但用於 5ghz、5ghz-10mhz、5ghz-5mhz、5ghz-turbo、2.4ghz-b/g、2.4ghz-onlyg、2ghz-10mhz、2ghz-5mhz 和 2.4ghz-g-turbo 頻段。 |
| **basic-rates-b** (*11Mbps \| 1Mbps \| 2Mbps \| 5.5Mbps*; 預設值：**1Mbps**) | 基礎速率列表，用於 2.4ghz-b、2.4ghz-b/g 和 2.4ghz-onlyg 頻段。用戶端僅在支援 AP 通告的所有基礎速率時才會連線到 AP。AP 僅當支援另一 AP 的所有基礎速率時才會建立 WDS 鏈路。此屬性僅在 AP 模式下以及配置 **rate-set** 的值時生效。 |
| **bridge-mode** (*disabled \| enabled*; 預設值：**enabled**) | 允許使用 station-bridge 模式。 [無線站模式](../user-guides/wireless-station-modes.md) |
| **burst-time** (*integer \| disabled*; 預設值：**disabled**) | 用於不停頓傳送資料的時間，單位為微秒。注意，在該 burst-time 微秒期間，該網路中的其他無線卡將無法傳送資料。此設定僅適用於基於 AR5000、AR5001X 和 AR5001X+ 晶片組的卡。 |
| **channel-width** (*20/40/80/160mhz-Ceeeeeee \| 20/40/80/160mhz-XXXXXXXX \| 20/40/80/160mhz-eCeeeeee \| 20/40/80/160mhz-eeCeeeee \| 20/40/80/160mhz-eeeCeeee \| 20/40/80/160mhz-eeeeCeee \| 20/40/80/160mhz-eeeeeCee \| 20/40/80/160mhz-eeeeeeCe \| 20/40/80/160mhz-eeeeeeeC \| 20/40/80mhz-Ceee \| 20/40/80mhz-eCee \| 20/40/80mhz-eeCe \| 20/40/80mhz-eeeC \| 20/40/80mhz-XXXX \| 20/40mhz-Ce \| 20/40mhz-eC \| 20/40mhz-XX \| 40mhz-turbo \| 20mhz \| 10mhz \| 5mhz*; 預設值：**20mhz**) | 使用擴充套件通道（例如 Ce、eC 等）允許額外的 20MHz 擴充套件通道，並指定其應位於控制（主）通道的下方還是上方。擴充套件通道使 802.11n 裝置總共可使用高達 40MHz（802.11ac 高達 160MHz）的頻譜，從而提高最大吞吐量。帶有 XX 和 XXXX 擴充套件的通道寬度會根據每個頻率上執行的併發裝置數量自動掃描較不擁擠的控制通道頻率，並自動選擇“C”——控制通道頻率。 |
| **comment** (*string*; Default: ) | 介面的簡短描述 |
| **compression** (*yes \| no*; 預設值：**no**) | 將此屬性設定為 *yes* 將允許使用硬體壓縮。無線介面必須支援硬體壓縮。與不使用壓縮的裝置之間的連線仍可正常工作。 |
| **country** (*name of the country \| no\_country\_set*; 預設值：**etsi**) | 限制可用頻段、頻率以及每個頻率的最大發射功率。還指定 **scan-list** 的預設值。值 *no\_country\_set* 是符合 FCC 的通道集合。 |
| **default-ap-tx-limit** (*integer [0..4294967295]*; 預設值：**0**) | 對於不匹配  [access-list](./wireless-interface.md#access-list) 中任何條目的用戶端，這是 **ap-tx-limit** 的值。0 表示無限制。 |
| **default-authentication** (*yes \| no*; 預設值：**yes**) | 對於 AP 模式，這是不匹配  [access-list](./wireless-interface.md#access-list) 中任何條目的用戶端的 **authentication** 值。對於站模式，這是不匹配  [connect-list](./wireless-interface.md#connect-list) 中任何條目的 AP 的 **connect** 值 |
| **default-client-tx-limit** (*integer [0..4294967295]*; 預設值：**0**) | 對於不匹配  [access-list](./wireless-interface.md#access-list) 中任何條目的用戶端，這是 **client-tx-limit** 的值。0 表示無限制 |
| **default-forwarding** (*yes \| no*; 預設值：**yes**) | 對於不匹配  [access-list](./wireless-interface.md#access-list) 中任何條目的用戶端，這是 **forwarding** 的值 |
| **disable-running-check** (*yes \| no*; 預設值：**no**) | 當設定為 **yes** 時，介面將始終具有 running 標誌。如果值設定為 **no**，路由器將確定卡是否已啟動並執行——對於 AP，必須有一個或多個用戶端註冊到它；對於站，它應連線到 AP。 |
| **disabled** (*yes \| no*; 預設值：**yes**) | 介面是否已停用 |
| **disconnect-timeout** (*time [0s..15s]*; 預設值：**3s**) | 此間隔從最低資料速率下第三次傳送失敗開始計算。此時，在最低資料速率下已有 3 \* (**hw-retries** + 1) 個幀傳送失敗。在 **disconnect-timeout** 期間，將按 **on-fail-retry-time** 間隔重試封包傳輸。如果在 **disconnect-timeout** 期間無法成功傳輸任何幀，則連線關閉，並將此事件記錄為 "extensive data loss"。成功傳輸幀會重設此計時器。 |
| **distance** (*integer \| dynamic \| indoors*; 預設值：**dynamic**) | 等待單播幀確認（**ACKs**）多久後才認為傳輸不成功，或簡稱 **ACK-Timeout**。Distance 值具有以下行為：*Dynamic* - 使 AP 檢測並使用對所有已連線用戶端都有效的最小超時。*Indoor* - 使用硬體晶片製造商設定的預設 ACK 超時值。*Number* - 使用公式中的輸入值：ACK-timeout = ((**distance** * 1000) + 299) / 300 us；Nstreme/Nv2 協定中不使用確認。 |
| **frame-lifetime** (*integer [0..4294967295]*; 預設值：**0**) | 丟棄排隊等待發送時間超過 **frame-lifetime** 的幀。預設情況下，當此屬性的值為 *0* 時，幀僅在連線關閉後才會被丟棄。 |
| **frequency** (*integer [0..4294967295]*; 預設值： ) | AP 將執行的通道頻率值，單位為 MHz。允許值取決於所選頻段，並受 **country** 設定和無線卡能力限制。如果介面處於任何 **station** 模式、*wds-slave* 模式，或 DFS 處於活動狀態，則此設定**無效**。*注意*：如果使用 "superchannel" 模式，卡支援的任何頻率都將被接受，但在 RouterOS 用戶端上，任何非標準頻率都必須在  [scan-list](http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates) 中配置，否則它不會掃描非標準範圍。在 WinBox 中，scanlist 頻率以*粗體*顯示，任何其他頻率意味著用戶端需要配置 scan-list。 |
| **frequency-mode** (*manual-txpower \| regulatory-domain \| superchannel*; 預設值：**regulatory\_domain**) | 有三種頻率模式可用：*regulatory-domain* - 根據 **country** 的值限制可用通道和每個通道的最大發射功率*manual-txpower* - 同上，但不限制最大發射功率。*superchannel* - 一致性測試模式。允許卡支援的所有通道。每個頻段的可用通道列表可在 **/interface/wireless/info/allowed-channels** 中檢視。此模式允許您測試預設 scan-list 和/或法規域之外的無線通道。此模式僅應在受控環境中使用，或您擁有在所在地區使用它的特殊許可。 |
| **frequency-offset** (*integer [-2147483648..2147483647]*; 預設值：**0**) | 如果使用的無線卡工作頻率與 RouterOS 中顯示的不同（例如卡中使用了頻率轉換器），則允許指定偏移。因此，如果您的卡工作在 4000MHz 但 RouterOS 顯示 5000MHz，將偏移設定為 1000MHz，它就會正確顯示。該值以 MHz 為單位，可以為正或負。 |
| **guard-interval** (*any \| long*; 預設值：**any**) | 是否允許使用短保護間隔（請參閱 802.11n MCS 規範以瞭解這如何影響吞吐量）。"any" 將根據資料速率使用短或長，"long" 將使用長。 |
| **hide-ssid** (*yes \| no*; 預設值：**no**) | *yes* - AP 不在 beacon 幀中包含 SSID，並且不回覆具有廣播 SSID 的探測請求。*no* - AP 在 beacon 幀中包含 SSID，並回復具有廣播 SSID 的探測請求。此屬性僅在 AP 模式下生效。將其設定為 *yes* 可以將此網路從某些用戶端軟體顯示的無線網路列表中移除。更改此設定不會提高無線網路的安全性，因為 SSID 包含在 AP 傳送的其他幀中。 |
| **ht-basic-mcs** (*list of (mcs-0 \| mcs-1 \| mcs-2 \| mcs-3 \| mcs-4 \| mcs-5 \| mcs-6 \| mcs-7 \| mcs-8 \| mcs-9 \| mcs-10 \| mcs-11 \| mcs-12 \| mcs-13 \| mcs-14 \| mcs-15 \| mcs-16 \| mcs-17 \| mcs-18 \| mcs-19 \| mcs-20 \| mcs-21 \| mcs-22 \| mcs-23)*; 預設值：**mcs-0; mcs-1; mcs-2; mcs-3; mcs-4; mcs-5; mcs-6; mcs-7**) | 每個連線用戶端都必須支援的 [調製和編碼方案](http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates)。有關 MCS 規範，請參閱 802.11n。 |
| **ht-supported-mcs** (*list of (mcs-0 \| mcs-1 \| mcs-2 \| mcs-3 \| mcs-4 \| mcs-5 \| mcs-6 \| mcs-7 \| mcs-8 \| mcs-9 \| mcs-10 \| mcs-11 \| mcs-12 \| mcs-13 \| mcs-14 \| mcs-15 \| mcs-16 \| mcs-17 \| mcs-18 \| mcs-19 \| mcs-20 \| mcs-21 \| mcs-22 \| mcs-23)*; 預設值：**mcs-0; mcs-1; mcs-2; mcs-3; mcs-4; mcs-5; mcs-6; mcs-7; mcs-8; mcs-9; mcs-10; mcs-11; mcs-12; mcs-13; mcs-14; mcs-15; mcs-16; mcs-17; mcs-18; mcs-19; mcs-20; mcs-21; mcs-22; mcs-23**) | 此裝置通告為支援的 [調製和編碼方案](./wireless-interface.md#frame-protection-support-rtscts)。有關 MCS 規範，請參閱 802.11n。 |
| **hw-fragmentation-threshold** (*integer[256..3000] \| disabled*; 預設值：**disabled**) | 指定在無線介質上傳輸時的最大分片大小（位元組）。802.11 標準封包（802.11 術語中的 MSDU）分片允許封包在透過無線介質傳輸之前進行分片，以提高成功傳輸的機率（僅重傳未正確傳輸的分片）。注意，由於協定開銷以及傳送方和接收方資源使用增加，傳輸分片封包比傳輸未分片封包效率更低。 |
| **hw-protection-mode** (*cts-to-self \| none \| rts-cts*; 預設值：**none**) | 幀保護支援屬性  [幀保護支援](./wireless-interface.md#frame-protection-support-rtscts) |
| **hw-protection-threshold** (*integer [0..65535]*; 預設值：**0**) | 幀保護支援屬性 [幀保護支援](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md) |
| **hw-retries** (*integer [0..15]*; 預設值：**7**) | 傳送幀重試次數，超過後視為傳輸失敗。失敗時資料速率會降低，並再次傳送該幀。在最低支援速率上連續三次失敗後，將暫停向該目標傳輸 **on-fail-retry-time** 指定的時長。之後再次傳送該幀。幀會一直重傳，直到傳輸成功，或在 **disconnect-timeout** 後用戶端斷開連線。如果超過 **frame-lifetime**，幀可能在此期間被丟棄。 |
| **installation** (*any \| indoor \| outdoor*; 預設值：**any**) | 調整 scan-list，以使用所設定國家/地區的室內、室外或所有頻率。 |
| **interworking-profile** (*enabled \| disabled*; 預設值：**disabled**) |  |
| **keepalive-frames** (*enabled \| disabled*; 預設值：**enabled**) | 僅當無線介面處於 mode=**ap-bridge** 時適用。如果用戶端約 20 秒未通訊，AP 會發送 "keepalive-frame"。**注意：** 停用此功能可能導致登錄檔中出現“幽靈”用戶端。 |
| **l2mtu** (*integer [0..65536]*; 預設值：**1600**) |  |
| **mac-address** (*MAC*; 預設值： ) |  |
| **master-interface** (*string*; 預設值： ) | 具有 *virtual-ap* 能力的無線介面名稱。僅當主介面處於 *ap-bridge*、*bridge*、*station* 或 *wds-slave* 模式時，虛擬 AP 介面才會工作。此屬性僅適用於虛擬 AP 介面。 |
| **max-station-count** (*integer [1..2007]*; 預設值：**2007**) | 關聯用戶端的最大數量。WDS 鏈路也計入此限制。 |
| **mode** (*station \| station-wds \| ap-bridge \| bridge \| alignment-only \| nstreme-dual-slave \| wds-slave \| station-pseudobridge \| station-pseudobridge-clone \| station-bridge*; 預設值：**station**) | 在不同站和接入點（AP）模式之間選擇。[站模式](./wireless-interface.md#info)：*station* - 基本站模式。查詢並連線到可接受的 AP。*station-wds* - 與 *station* 相同，但使用專有擴充套件與 AP 建立 WDS 鏈路。AP 配置必須允許與此裝置建立 WDS 鏈路。注意，此模式不使用 wds 中的條目。*station-pseudobridge* - 與 *station* 相同，但額外對所有流量執行 MAC 地址轉換。允許介面被橋接。*station-pseudobridge-clone* - 與 *station-pseudobridge* 相同，但使用 **station-bridge-clone-mac** 地址連線到 AP。station-bridge - 在站裝置上提供對透明、協定無關的 L2 橋接的支援。RouterOS AP 在透過 bridge-mode 引數啟用時接受處於 station-bridge 模式的用戶端。在此模式下，AP 維護一個轉發表，其中包含哪些 MAC 地址可透過哪個站裝置到達的資訊。僅適用於 RouterOS AP。使用 station-bridge 模式時，無法連線到由 CAPsMAN 控制的 CAP。🛈 **重要：** `wireless` station-bridge 模式與執行較新 `wifi` 包的 AP 不相容，反之亦然。   AP 模式：*ap-bridge* - 基本接入點模式。*bridge* - 與 *ap-bridge* 相同，但限制為一個關聯用戶端。*wds-slave* - 與 *ap-bridge* 相同，但掃描具有相同 **ssid** 的 AP 並建立 WDS 鏈路。如果此鏈路丟失或無法建立，則繼續掃描。如果 **dfs-mode** 為 *radar-detect*，則掃描期間將找不到啟用了 **hide-ssid** 的 AP。特殊模式：*alignment-only* - 將介面置於連續傳送模式，用於對準遠端天線。*nstreme-dual-slave* - 允許此介面用於 nstreme-dual 設定。偽橋模式中的 MAC 地址轉換透過檢查封包並構建相應 IP 和 MAC 地址表來工作。所有封包都以偽橋使用的 MAC 地址傳送到 AP，接收到的封包的 MAC 地址則從地址轉換表中恢復。地址轉換表中對所有非 IP 封包只有一個條目，因此橋接網路中多於一個主機無法可靠地使用非 IP 協定。**注意：** IPv6 無法透過 pseudobridge 工作  |
| **mtu** (*integer [0..65536]*; 預設值：**1500**) |  |
| **multicast-buffering** (*disabled \| enabled*; 預設值：**enabled**) | 對於具有省電功能的用戶端，緩衝組播封包直到下一個 beacon 時間。用戶端應喚醒以接收 beacon，透過接收 beacon 它看到有組播封包待發送，並應等待組播封包被髮送。 |
| **multicast-helper** (*default \| disabled \| full*; 預設值：**default**) | 當設定為 **full** 時，組播封包將使用單播目標 MAC 地址傳送，從而解決無線鏈路上的組播問題。此選項應僅在接入點上啟用，用戶端應配置為 **station-bridge** 模式。disabled - 停用 helper 並使用組播目標 MAC 地址傳送組播封包dhcp - 在傳送出去之前，DHCP 封包 MAC 地址會改為單播 MAC 地址full - 在傳送出去之前，所有組播封包 MAC 地址都會改為單播 MAC 地址default - 預設選擇，當前設定為 *dhcp*。該值可能在將來版本中更改。 |
| **name** (*string*; 預設值： ) | 介面名稱 |
| **noise-floor-threshold** (*default \| integer [-128..127]*; 預設值：**default**) | 僅供高階使用，因為它可能嚴重影響介面效能。可以手動設定噪聲底閾值。預設情況下，它是動態計算的。此屬性還會影響接收訊號強度。此屬性僅對非 AC 晶片有效。 |
| **nv2-cell-radius** (*integer [10..200]*; 預設值：**30**) | 該設定影響 AP 為用戶端發起連線分配的競爭時隙大小，以及用於估計到用戶端距離的時隙大小。當設定太小時，較遠的用戶端可能難以連線和/或斷開連線並出現 "ranging timeout" 錯誤。儘管在正常操作期間此設定的影響應可忽略不計，但為了保持最大效能，建議非必要不要增加此設定，這樣 AP 不會保留實際從未使用的時間，而是將其分配給實際資料傳輸。在 AP 上：到最遠用戶端的距離，單位為 km；在站上：無影響 |
| **nv2-noise-floor-offset** (*default \| integer [0..20]*; 預設值：**default**) |  |
| **nv2-preshared-key** (*string*; 預設值： ) *[敏感](./wireless-interface.md#security-profiles)* |  |
| **nv2-qos** (*default \| frame-priority*; 預設值：**default**) | 設定封包優先順序機制，首先發送高優先順序佇列的資料，然後傳送較低佇列優先順序的資料，直到達到 0 佇列優先順序。當鏈路充滿高優先順序佇列資料時，低優先順序資料不會發送。請非常謹慎使用，該設定作用於 AP**frame-priority** - 可透過 Mangle 規則調整的手動設定。**default** - 預設設定，其中小封包獲得優先順序以獲得最佳延遲 |
| **nv2-queue-count** (*integer [2..8]*; 預設值：**2**) |  |
| **nv2-security** (*disabled \| enabled*; 預設值：**disabled**) |  |
| **on-fail-retry-time** (*time [100ms..1s]*; 預設值：**100ms**) | 在最低資料速率上第三次傳送失敗後，等待指定時間間隔後再重試。 |
| **periodic-calibration** (*default \| disabled \| enabled*; 預設值：**default**) | 設定 *default* 會在  [info](../../system-information-and-utilities/identity.md)  的 **default-periodic-calibration** 屬性為 *enabled* 時啟用週期性校準。該屬性的值取決於無線卡的型別。此屬性僅對基於 Atheros 晶片組的卡有效。 |
| **periodic-calibration-interval** (*integer [1..10000]*; 預設值：**60**) | 此屬性僅對基於 Atheros 晶片組的卡有效。 |
| **preamble-mode** (*both \| long \| short*; 預設值：**both**) | 短前導碼模式是 802.11b 標準的一個選項，可減少每幀開銷。在 AP 上：*long* - 不使用短前導碼。*short* - 通告短前導碼能力。不接受不具備此能力的用戶端連線。*both* - 通告短前導碼能力。在站上：*long* - 不使用短前導碼。*short* - 如果 AP 不支援短前導碼，則不連線到該 AP。*both* - 如果 AP 支援，則使用短前導碼。 |
| **prism-cardtype** (*100mW \| 200mW \| 30mW*; 預設值： ) | 指定已安裝 Prism 無線卡的型別。 |
| **proprietary-extensions** (*post-2.9.25 \| pre-2.9.25*; 預設值：**post-2.9.25**) | RouterOS 在管理幀的資訊元素中包含專有資訊。此引數控制如何包含此資訊。*pre-2.9.25* - 這是較舊的方法。它可以與較新版本的 RouterOS 互操作。此方法與某些用戶端不相容，例如基於 Centrino 的用戶端。*post-2.9.25* - 這使用標準化方式包含廠商特定資訊，與較新的無線用戶端相容。 |
| **radio-name** (*string*; 預設值：**MAC address of an interface**) | 裝置的描述性名稱，顯示在遠端裝置的登錄檔條目中。這是一個專有擴充套件。 |
| **rate-selection** (*advanced \| legacy*; 預設值：**advanced**) | 預設值為 **advanced**；**legacy** 模式效率低下，僅保留用於向後相容。 |
| **rate-set** (*configured \| default*; 預設值：**default**) | 有兩個選項可用：*default* - 使用預設的基礎和支援速率集。**basic-rates** 和 **supported-rates** 引數中的值無效。*configured* - 使用 **basic-rates**、**supported-rates**、**basic-mcs**、**mcs** 中的值。[基礎速率和 MCS 速率表](./wireless-interface.md#station-roaming)。 |
| **rx-chains** (*list of integer [0..3]*; 預設值：**0**) | 用於接收的天線。在當前 MikroTik 路由器中，RX 和 TX 鏈都必須啟用，該鏈才會啟用。 |
| scan-list (*Comma separated list of frequencies and frequency ranges \| default. The type also supports the range:step option*; 預設值：**default**) | *default* 值是從所選頻段中由卡支援並受 **country** 和 **frequency-mode** 設定允許的所有通道（此列表可在  [info](../../bridging-and-switching/user-guides/wmm-and-vlan-priority.md) 中檢視）。對於 *5ghz* 頻段的預設 scan list，通道以 20MHz 步進選取；在 *5ghz-turbo* 頻段中，以 40MHz 步進；對於所有其他頻段，以 5MHz 步進。如果手動指定 **scan-list**，則採用所有匹配的通道。（示例：**scan-list**=*default,5200-5245,2412-2427* - 這將使用當前頻段的 scan list 預設值，並向其中新增來自 5200-5245 或 2412-2427 範圍的受支援頻率。）   在 WinBox 或 Webfig 中，將每個頻率或頻率範圍作為單獨的 scan-list 條目輸入；那裡不支援逗號分隔列表。scan-list 還支援步進，您可以手動指定掃描步進。示例：**scan-list**=*5500-5600:20* 將生成如下 scan-list 值 *5500,5520,5540,5560,5580,5600* |
| **security-profile** (*string*; 預設值：**default**) | 來自  [安全配置檔案](./wireless-interface.md#wps-server)  的配置檔名稱 |
| **secondary-channel** (*integer*; 預設值：**""**) | 指定輔助通道，啟用 80+80MHz 傳輸所需。要停用 80+80MHz 功能，請將 secondary-channel 設定為 "" 或透過 CLI/GUI 取消該值。 |
| **ssid** (*string (0..32 chars)*; 預設值：**[/system/identity](../../system-information-and-utilities/identity.md) 的值**) | SSID（服務集識別符號）是標識無線網路的名稱。 |
| **skip-dfs-channels** (*string \| 10min-cac \| all \| disabled*; 預設值：**disabled**) | 這些值用於跳過所有 DFS 通道，或專門跳過 5600-5650MHz 範圍內的 DFS CAC 通道，其檢測可能長達 10min。 |
| **station-bridge-clone-mac** (*MAC*; 預設值： ) | 此屬性僅在 *station-pseudobridge-clone* 模式下生效。連線到 AP 時使用此 MAC 地址。如果此值為 *00:00:00:00:00:00*，站最初將使用無線介面的 MAC 地址。一旦需要傳送具有另一裝置 MAC 地址的封包，站將使用該地址重新連線到 AP。 |
| **station-roaming** (*disabled \| enabled*; 預設值：**disabled**) | 站漫遊功能僅適用於 802.11 無線協定，且僅適用於站模式。  [站漫遊](./wireless-interface.md#station-roaming) |
| **supported-rates-a/g** (*list of rates [12Mbps \| 18Mbps \| 24Mbps \| 36Mbps \| 48Mbps \| 54Mbps \| 6Mbps \| 9Mbps]*; 預設值：**6Mbps; 9Mbps; 12Mbps; 18Mbps; 24Mbps; 36Mbps; 48Mbps; 54Mbps**) | 支援的速率列表，用於除 *2ghz-b* 之外的所有頻段。 |
| **supported-rates-b** (*list of rates [11Mbps \| 1Mbps \| 2Mbps \| 5.5Mbps]*; 預設值：**1Mbps; 2Mbps; 5.5Mbps; 11Mbps**) | 支援的速率列表，用於 *2ghz-b*、*2ghz-b/g* 和 *2ghz-b/g/n* 頻段。兩臺裝置將僅使用雙方都支援的速率進行通訊。此屬性僅在 **rate-set** 的值為 *configured* 時生效。 |
| **tdma-period-size** (*integer [1..10]*; 預設值：**2**) | 指定 TDMA 週期，單位為毫秒。它可能有助於較長距離的鏈路，可能略微增加頻寬，但延遲也會增加。 |
| **tx-chains** (*list of integer [0..3]*; 預設值：**0**) | 用於傳送的天線。在當前 MikroTik 路由器中，RX 和 TX 鏈都必須啟用，該鏈才會啟用。 |
| **tx-power** (*integer [-30..40]*; 預設值： ) | 對於 802.11ac 無線介面，這是總功率；但對於 802.11a/b/g/n，這是每鏈功率。 |
| **tx-power-mode** (*default, card-rates, all-rates-fixed, manual-table*; 預設值：**default**) | 設定無線卡的 tx-power 模式default - 使用卡中儲存的值all-rates-fixed - 對所有資料速率使用相同的發射功率。如果發射功率設定高於所用速率的卡的額定值，可能會損壞卡。manual-table - 為每個速率單獨定義發射功率。如果發射功率設定高於所用速率的卡的額定值，可能會損壞卡。card-rates - 根據 **tx-power** 引數的值計算每個速率的發射功率。舊模式僅與當前已停產的產品相容。 |
| **update-stats-interval** (; 預設值： ) | 向用戶端請求更新訊號強度和 ccq 值的頻率。訪問  [登錄檔](./wireless-interface.md#registration-table)  也會觸發這些值的更新。這是一個專有擴充套件。 |
| **vht-basic-mcs** (*none \| MCS 0-7 \| MCS 0-8 \| MCS 0-9*; 預設值：**MCS 0-7**) | 每個連線用戶端都必須支援的 [調製和編碼方案](http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed)。有關 MCS 規範，請參閱 802.11ac。您可以為每個空間流設定 MCS 區間 *none* - 不使用所選空間流*MCS 0-7* - 用戶端必須支援 MCS-0 至 MCS-7*MCS 0-8* - 用戶端必須支援 MCS-0 至 MCS-8*MCS 0-9* - 用戶端必須支援 MCS-0 至 MCS-9 |
| **vht-supported-mcs** (*none \| MCS 0-7 \| MCS 0-8 \| MCS 0-9*; 預設值：**MCS 0-9**) | 此裝置通告為支援的 [調製和編碼方案](http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed)。有關 MCS 規範，請參閱 802.11ac。您可以為每個空間流設定 MCS 區間 *none* - 不使用所選空間流*MCS 0-7* - 裝置將通告支援 MCS-0 至 MCS-7*MCS 0-8* - 裝置將通告支援 MCS-0 至 MCS-8*MCS 0-9* - 裝置將通告支援 MCS-0 至 MCS-9 |
| **wds-cost-range** (*start [-end] integer[1..200000000]*; 預設值：**50-150**) | WDS 鏈路的橋埠開銷會根據測得的鏈路吞吐量自動調整。埠開銷每 5 秒重新計算和調整一次，前提是變化超過 10%，或距上次調整已超過 20 秒。將此屬性設定為 *0* 可停用自動開銷調整。自動調整不適用於手動配置為橋埠的 WDS 鏈路。 |
| **wds-default-bridge** (*string \| none*; 預設值：**none**) | 當 WDS 鏈路建立且 wds 介面狀態變為 *running* 時，它將作為橋埠新增到此屬性指定的橋介面。當 WDS 鏈路丟失時，wds 介面會從橋中移除。如果 WDS 鏈路啟用時 wds 介面已包含在橋接設定中，則不會將其新增到由  指定的橋中，並且將（需要編輯） |
| **wds-default-cost** (*integer [1..200000000]*; 預設值：**100**) | WDS 鏈路的初始橋埠開銷。 |
| **wds-ignore-ssid** (*yes \| no*; 預設值：**no**) | 預設情況下，兩個 AP 之間的 WDS 鏈路只能在工作頻率相同且 SSID 值相同時建立。如果此屬性設定為 *yes*，則不會檢查遠端 AP 的 SSID。此屬性對來自處於 *station-wds* 模式的用戶端連線沒有影響。如果 **wds-mode** 為 *static-mesh* 或 *dynamic-mesh*，它也不起作用。 |
| **wds-mode** (*disabled \| dynamic \| dynamic-mesh \| static \| static-mesh*; 預設值：**disabled**) | 控制如何與其他裝置（AP 和處於 *station-wds* 模式的用戶端）建立 WDS 鏈路。*disabled* 不允許 WDS 鏈路。*static* 僅允許在 WDS 中手動配置的 WDS 鏈路*dynamic* 還允許與未在 WDS 中配置的裝置建立 WDS 鏈路，透過動態建立所需條目。此類動態 WDS 條目會在與另一 AP 的連線丟失後自動移除。-mesh 模式使用不同（更好）的方法在 AP 之間建立鏈路，該方法與非 mesh 模式下的 AP 不相容。此方法可避免僅由兩個 AP 之一建立的單邊 WDS 鏈路。此類鏈路無法傳遞任何資料。當 AP 或站與另一 AP 建立 WDS 連線時，它使用 connect-list 檢查是否允許此連線。如果處於 station-wds 模式的站與 AP 建立連線，AP 使用 access-list 檢查是否允許此連線。如果模式為 station-wds，則此屬性無效。 |
| **wireless-protocol** (*802.11 \| any \| nstreme \| nv2 \| nv2-nstreme \| nv2-nstreme-802.11 \| unspecified*; 預設值：**any**) | 指定無線介面上使用的協定；*unspecified* - 在以前 RouterOS 版本（v3.x、v4.x）中使用的協定模式。Nstreme 由舊的 enable-nstreme 設定啟用，無法配置 Nv2。*any*：在 AP 上 - 常規 802.11 接入點或 Nstreme 接入點；在站上 - 選擇接入點時不使用特定順序，可由 connect-list 規則更改。*nstreme* - 啟用 Nstreme 協定（與舊的 enable-nstreme 設定相同）。*nv2* - 啟用 Nv2 協定。*nv2 nstreme*：在 AP 上 - 使用第一個 wireless-protocol 設定，始終為 Nv2；在站上 - 先搜尋 Nv2 接入點，然後搜尋 Nstreme 接入點。*nv2 nstreme 802.11* - 在 AP 上 - 使用第一個 wireless-protocol 設定，始終為 Nv2；在站上 - 先搜尋 Nv2 接入點，然後搜尋 Nstreme 接入點，然後搜尋常規 802.11 接入點。⚠️ **警告：** Nv2 不支援虛擬 AP |
| **wmm-support** (*disabled \| enabled \| required*; 預設值：**disabled**) | 指定是否啟用  [WMM](../../bridging-and-switching/user-guides/wmm-and-vlan-priority.md)。  僅適用於 B 和 G 頻段。其他頻段將無論此設定如何都會啟用 |
| **wps-mode** (*disabled \| push-button \| push-button-virtual-only*; 預設值：**取決於裝置型號**) | [WPS 伺服器](./wireless-interface.md#wps-server) |

### 重設物理介面 MAC 地址 {#reset-physical-interface-mac-address}

物理介面 MAC 地址可透過命令 `reset-mac-address` 重設為預設值。

```ros
/interface/wireless/reset-mac-address wlan1
```

### 發射功率表示方式 {#transmit-power-representation}

802.11n 無線晶片組表示每鏈功率。802.11ac 無線晶片組表示總功率。

| 無線晶片組 | 啟用的鏈數 | 每鏈功率 | 總功率 |
| :-- | --: | :-- | :-- |
| 802.11n | 1 | 等於所選 Tx Power | 等於所選 Tx Power |
| 802.11n | 2 | 等於所選 Tx Power | +3dBm |
| 802.11n | 3 | 等於所選 Tx Power | +5dBm |
| 802.11ac | 1 | 等於所選 Tx Power | 等於所選 Tx Power |
| 802.11ac | 2 | -3dBm | 等於所選 Tx Power |
| 802.11ac | 3 | -5dBm | 等於所選 Tx Power |
| 802.11ac | 4 | -6dBm | 等於所選 Tx Power |

### 基礎速率和 MCS 速率表 {#basic-and-mcs-rate-table}

預設基礎速率和支援速率，取決於所選頻段

| 頻段 | 基礎速率 | basic-HT-mcs | basic-VHT-mcs | VHT-mcs | HT-mcs | 支援的速率 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 2.4ghz-b | 1 | - | - | - | - | 1-11 |
| 2.4ghz-onlyg | 6 | - | - | - | - | 1-11,6-54 |
| 2.4ghz-onlyn | 6 | 0-7 | - | - | 0-23 | 1-11,6-54 |
| 2.4ghz-b/g | 1-11 | - | - | - | - | 1-11,6-54 |
| 2.4ghz-b/g/n | 1-11 | none | - | - | 0-23 | 1-11,6-54 |
| 2.4ghz-g/n | 6 | none | - | - | 0-23 | 6-54 |
| 2.4ghz-g-turbo | 6 | - | - | - | - | 6-54 |
| 5ghz-a | 6 | - | - | - | - | 6-54 |
| 5ghz-a/n | 6 | none | - | - | 0-23 | 6-54 |
| 5ghz-onlyn | 6 | 0-7 | - | - | 0-23 | 6-54 |
| 5ghz-a/n/ac | 6 | none | none | 0-9 | 0-23 | 6-54 |
| 5ghz-onlyac | 6 | none | 0-7 | 0-9 | 0-23 | 6-54 |

當 **rate-set=configured** 時使用的設定

| 頻段 | 使用的設定 |
| :-- | :-- |
| 2.4ghz-b | basic-b, supported-b |
| 2.4ghz-b/g, 2.4ghz-onlyg | basic-b, supported-b, basic-a/g, supported-a/g |
| 2.4ghz-onlyn, 2.4ghz-b/g/n | basic-b, supported-b, basic-a/g, supported-a/g, ht-basic-mcs, ht-supported-mcs |
| 2.4ghz-g/n | basic-a/g,supported-a/g,ht-basic-mcs,ht-supported-mcs |
| 5ghz-a | basic-a/g,supported-a/g |
| 5ghz-a/n, 5ghz-onlyn | basic-a/g,supported-a/g,ht-basic-mcs,ht-supported-mcs |
| 5ghz-a/n/ac, 5ghz-onlyac | basic-a/g,supported-a/g,ht-basic-mcs,ht-supported-mcs,vht-basic-mcs,vht-supported-mcs |

獨立於 **rate-set** 的設定：

1. 根據鏈數允許的 MCS：
   - 1 鏈：0-7
   - 2 鏈：0-15
   - 3 鏈：0-23
2. 如果未使用標準通道寬度（20MHz），則 2GHz 模式（2.4GHz-b 除外）不使用 b 速率（1-11）

### 幀保護支援（RTS/CTS） {#frame-protection-support-rtscts}

802.11 標準透過使用 RTS/CTS 協定提供保護傳輸免受其他裝置傳輸影響的方法。幀保護有助於應對“隱藏節點”問題。有幾種保護型別：

- 基於 RTS/CTS 的保護 - 願意傳送幀的裝置首先發送 RequestToSend 幀，並等待來自預期目標的 ClearToSend 幀。透過“看到”RTS 或 CTS 幀，符合 802.11 的裝置知道有人即將傳送，因此自身不發起傳輸。
- 基於 "CTS to self" 的保護 - 願意傳送幀的裝置傳送一個“發給自身”的 CTS 幀。與 RTS/CTS 協定一樣，每個接收到此幀的符合 802.11 的裝置都知道不要傳送。基於 "CTS to self" 的保護開銷較小，但必須考慮到這僅能防止接收到 CTS 幀的裝置傳送（例如，如果有 2 個“隱藏”站，使用 "CTS to self" 保護對它們沒有用處，因為它們將無法接收另一站傳送的 CTS——在這種情況下，站必須使用 RTS/CTS，以便另一站透過看到 AP 傳送的 CTS 知道不要傳送）。

保護模式由無線介面的 **hw-protection-mode** 設定控制。可能的值：**none** - 無保護（預設），**rts-cts** 用於基於 RTS/CTS 的保護，或 **cts-to-self** 用於基於 "CTS to self" 的保護。

應使用保護時的幀大小閾值由無線介面的 **hw-protection-threshold** 設定控制。

例如，要在 AP 上對所有幀啟用基於 "CTS-to-self" 的幀保護（不取決於大小），請使用命令：

```
[admin@MikroTik] /interface/wireless> set 0 hw-protection-mode=cts-to-self hw-protection-threshold=0
```

要在用戶端上啟用基於 RTS/CTS 的保護，請使用命令：

```
[admin@MikroTik] /interface/wireless> set 0 hw-protection-mode=rts-cts hw-protection-threshold=0
```

### Nv2 {#nv2}

MikroTik 開發了一種基於 TDMA 技術（分時多重進接）的新無線協定 -（Nstreme 版本 2）。請參閱 Nv2 文件：[Nv2](./nv2.md)

TDMA 是一種用於共享介質網路的通道接入方法。它允許多個使用者透過將訊號劃分為不同的時隙來共享同一頻率通道。使用者一個接一個地快速連續傳送，每個使用者使用自己的時隙。這允許多個站共享同一傳輸介質（例如無線電頻率通道），同時僅使用其通道容量的一部分。

Nv2 最重要的優勢是：

- 提高速度。
- PTM 環境中更多的用戶端連線。
- 更低延遲。
- 無距離限制。
- 長距離無懲罰。

Nv2 協定限制為 511 個用戶端。

:::warning
 Nv2 不支援虛擬 AP
:::

#### Nv2 故障排查 {#nv2-troubleshooting}

透過 **tdma-period-size** 提高長距離鏈路的吞吐量。在每個“週期”中，接入點留出一部分時間不用於資料傳輸（等於*往返時間*——即幀可以從用戶端傳送和接收的時間），用於確保用戶端在向接入點發送自己的封包之前能夠接收到來自接入點的最後一個幀。距離越長，未使用的時間段越長。

例如，接入點與用戶端之間的距離為 30km。幀在一個方向上傳送耗時 100us；因此往返時間約為 200us。**tdma-period-size** 預設值為 2ms，這意味著 10% 的時間未使用。當 tdma-period-size 增加到 4ms 時，只有 5% 的時間未使用。對於 60km 的無線鏈路，往返時間為 400us，預設 tdma-period-size 2ms 時未使用時間為 20%，4ms 時為 10%。更大的 tdma-period-size 值會增加鏈路延遲。

## 訪問列表 {#access-list}

**子選單：** `/interface/wireless/access-list`

接入點使用訪問列表來限制來自其他裝置的允許連線，並控制連線引數。

訪問列表規則會逐條處理，直到找到匹配規則。然後執行匹配規則中的操作。如果操作指定應接受用戶端，則接受該用戶端，並可能用訪問列表規則中指定的引數覆蓋其預設連線引數。

訪問列表規則有以下引數：

- 用戶端匹配引數：
  - address - 用戶端的 MAC 地址。
  - interface - 可選介面，用於與用戶端實際連線的介面進行比較。
  - time - 規則匹配的當天時間和星期幾。
  - signal-range - 用戶端訊號必須處於該範圍內，規則才會匹配。
  - allow-signal-out-of-range - 允許用戶端訊號始終或在一定時間間隔內超出範圍的選項。
- 連線引數：
  - ap-tx-limit - 到用戶端方向的 TX 速率限制。
  - client-tx-limit - 到 AP 方向的 TX 速率限制（僅適用於 RouterOS 用戶端）。
  - private-passphrase - 如果使用某種 PSK 認證演算法，則用於此用戶端的 PSK 密碼短語。
  - vlan-mode - VLAN 標記模式，指定來自用戶端的流量是否應被標記（並在發往用戶端時取消標記）。
  - vlan-id - 執行 VLAN 標記時使用的 VLAN ID。

操作：

- 訪問列表規則按順序檢查。
- 停用的規則始終被忽略。
- 僅應用第一個匹配的規則。
- 如果遠端連線沒有匹配規則，則使用無線介面配置中的預設值。
- 如果遠端裝置匹配的規則具有 **authentication**=*no* 值，則來自該遠端裝置的連線被拒絕。

:::warning
如果 ACL 中沒有關於連線到 AP 的用戶端的條目（wireless,debug wlan2: A0:0B:BA:D7:4D:B2 not in local ACL, by default accept），則該用戶端的 ACL 在整個連線期間將被忽略。
:::

例如，如果用戶端在連線期間的訊號為 -41，並且我們有 ACL 規則

```
/interface/wireless/access-list
add authentication=yes forwarding=yes interface=wlan2 signal-range=-55..0
```

那麼該連線會匹配到 ACL 規則，但如果訊號降到 -55 以下，用戶端不會斷開。

如果在無線介面上設定了 `default-authentication=yes`，即使沒有匹配的訪問列表條目，用戶端也可以加入。  
為了正確執行，用戶端必須匹配其中一個 ACL 規則。

如果我們把上一個示例中的 ACL 規則修改為：

```
/interface/wireless/access-list
add interface=wlan2 signal-range=-55..0
add authentication=no forwarding=no interface=wlan2 signal-range=-120..-56
```

那麼如果訊號降到 -56，用戶端將被斷開。

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **ap-tx-limit** (*integer [0..4294967295]*; 預設值：**0**) | 限制向此用戶端傳輸資料的速率。值 *0* 表示無限制。值單位為位元每秒。 |
| **authentication** (*yes \| no*; 預設值：**yes**) | *no* - 用戶端關聯將始終失敗。*yes* - 使用介面的 [**security-profile**](../../cli-reference/interface/list/index.md) 中指定的認證過程。 |
| **client-tx-limit** (*integer [0..4294967295]*; 預設值：**0**) | 請求用戶端限制資料傳輸速率。值 *0* 表示無限制。這是一個專有擴充套件，受 RouterOS 用戶端支援。值單位為位元每秒。 |
| **comment** (*string*; 預設值： ) | 條目的簡短描述 |
| **disabled** (*yes \| no*; 預設值：**no**) |  |
| **forwarding** (*yes \| no*; 預設值：**yes**) | *no* - 用戶端無法向連線到同一接入點的其他站傳送幀。*yes* - 用戶端可以向同一接入點上的其他站傳送幀。 |
| **interface** (*string \| any \| all*; 預設值：**any**) | **interface**=*any* 的規則用於任何無線介面，而 **interface**=*all* 定義 [介面列表](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md) 的“all”名稱。要使規則僅適用於一個無線介面，請將該介面指定為此屬性的值。 |
| **mac-address** (*MAC*; 預設值：**00:00:00:00:00:00**) | 規則匹配具有指定 MAC 地址的用戶端。值 *00:00:00:00:00:00* 始終匹配。 |
| **management-protection-key** (*string*; 預設值：**""**) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* |  |
| **private-algo** (*104bit-wep \| 40bit-wep \| aes-ccm \| none \| tkip*; 預設值：**none**) | 僅用於 WEP 模式。 |
| **private-key** (*string*; 預設值：**""**) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 僅用於 WEP 模式。 |
| **private-pre-shared-key** (*string*; 預設值：**""**) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於 WPA PSK 模式。 |
| **signal-range** (*NUM..NUM - both NUM are numbers in the range -120..120*; 預設值：**-120..120**) | 如果站的訊號強度在範圍內，則規則匹配。如果站的訊號強度超出規則中指定的範圍，接入點將斷開該站。 |
| **time** (*TIME-TIME,sun,mon,tue,wed,thu,fri,sat - TIME is time interval 0..86400 seconds; all day names are optional; value can be unset*; 預設值： ) | 規則僅在指定時間內匹配。站將在指定時間結束後斷開。開始時間和結束時間均表示為自午夜 00:00 起的時間。規則僅在指定的星期幾匹配。 |

## 對齊 {#align}

**子選單：** `/interface/wireless/align`

Align 工具用於幫助對準執行此工具的裝置。

| 屬性 | 說明 |
| :-- | :-- |
| **active-mode** (*yes \| no*; 預設值：**yes**) | 如果處於活動模式，將傳送用於對準的幀。 |
| **audio-max** (*integer [-2147483648..2147483647]*; 預設值：**-20**) | 蜂鳴器的最大訊號強度 |
| **audio-min** (*integer [-2147483648..2147483647]*; 預設值：**-100**) | 蜂鳴器的最小訊號強度 |
| **audio-monitor** (*MAC*; 預設值：**00:00:00:00:00:00**) | 用於音訊監控的 MAC 地址 |
| **filter-mac** (*MAC*; 預設值：**00:00:00:00:00:00**) | 將在監控螢幕中顯示的過濾掉的 MAC 地址。 |
| **frame-size** (*integer [200..1500]*; 預設值：**300**) | 監控器使用的幀大小。 |
| **frames-per-second** (*integer [1..100]*; 預設值：**25**) | 幀傳送間隔 |
| **receive-all** (*yes \| no*; 預設值：**no**) | 如果設定為 "yes"，監控器將找到所有可用裝置。 |
| **ssid-all** (*yes \| no*; 預設值：**no**) | 是否在監控器中顯示所有 SSID，還是僅顯示無線設定中配置的一個。 |

### 選單專用命令 {#menu-specific-commands}

| 屬性 | 說明 |
| :-- | :-- |
| **monitor** (*interface name*) | 啟動對準監控 |
| **test-audio** (*integer [-2147483648..2147483647]*) | 測試蜂鳴器 |

## 連線列表 {#connect-list}

**子選單：** `/interface/wireless/connect-list`

connect-list 用於為與遠端接入點的連線分配優先順序和安全設定，並限制允許的連線。connect-list 是有序規則列表。connect-list 中的每條規則都附加到特定無線介面，由該規則的 `interface` 屬性指定（這與 [access-list](./wireless-interface.md#access-list) 不同，後者的規則可適用於所有介面）。規則可以匹配遠端接入點的 MAC 地址、其訊號強度以及許多其他引數。

操作：

- connect-list 規則始終從第一條開始按順序檢查。
- 停用的規則始終被忽略。
- 僅應用第一個匹配的規則。
- 如果在無線介面配置中提供了 SSID 或確切的無線協定，則連線列表中未包含在無線介面配置中的 SSID 或無線協定將被忽略。
- 如果 connect-list 沒有匹配遠端接入點的規則，則使用無線介面配置中的預設值。
- 如果接入點匹配的規則具有 **connect**=*no* 值，則不會嘗試與該接入點連線。
- 如果接入點匹配的規則具有 **connect**=*yes* 值，則將嘗試與該接入點連線。
  - 在站模式下，如果有多個遠端接入點匹配具有 **connect**=*yes* 值的連線列表規則，則將嘗試與 connect-list 中位置更高的規則所匹配的接入點連線。
  - 如果沒有遠端接入點匹配具有 **connect**=*yes* 值的 connect-list 規則，則 **default-authentication** 介面屬性的值決定站是否會嘗試連線任何接入點。如果 **default-authentication**=*yes*，站將選擇訊號最佳且安全相容的接入點。
- 在接入點模式下，connect-list 在建立與遠端裝置的 WDS 鏈路之前檢查。如果接入點不匹配連線列表中的任何規則，則 **default-authentication** 的值決定是否建立 WDS 鏈路。

### 屬性 {#properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **3gpp** (*string*; 預設值： ) |  |
| **area-prefix** (*string*; 預設值： ) | 如果 AP 的 area 值（專有擴充套件）以指定值開頭，則規則匹配。**area** 值是專有擴充套件。 |
| **comment** (*string*; 預設值： ) | 條目的簡短描述 |
| **connect** (*yes \| no*; 預設值：**yes**) | 可用選項：*yes* - 連線到匹配此規則的接入點。*no* - 不連線到任何匹配此規則的接入點。 |
| **disabled** (*yes \| no*; 預設值：**no**) |  |
| **mac-address** (*MAC*; 預設值：**00:00:00:00:00:00**) | 規則僅匹配具有指定 MAC 地址的 AP。值 *00:00:00:00:00:00* 始終匹配。 |
| **security-profile** (*string \| none*; 預設值：**none**) | 連線到匹配接入點時使用的 [安全配置檔案](./wireless-interface.md#security-profiles) 名稱。如果此屬性的值為 *none*，則使用介面配置中指定的安全配置檔案。在站模式下，規則僅匹配支援指定安全配置檔案的接入點。值 *none* 將匹配支援介面配置中指定安全配置檔案的接入點。在接入點模式下，此屬性的值不會用於匹配遠端裝置。 |
| **signal-range** (*NUM..NUM - both NUM are numbers in the range -120..120*; 預設值：**-120..120**) | 如果接入點的訊號強度在範圍內，則規則匹配。如果站與匹配此規則的接入點建立連線，當訊號強度超出指定範圍時，它將從該接入點斷開。 |
| **ssid** (*string*; 預設值：**""**) | 規則匹配具有此 SSID 的接入點。空值匹配任何 SSID。此屬性僅在站模式介面的 **ssid** 為空，或接入點模式介面的 **wds-ignore-ssid**=*yes* 時生效 |
| **wireless-protocol** (*802.11 \| any \| nstreme \| tdma*; 預設值：**any**) |  |
| **interface** (*string*; 預設值： ) | connect list 中的每條規則僅適用於此設定指定的一個無線介面。 |

### 用法 {#usage}

#### 僅允許站連線到特定接入點 {#restrict-station-connections-only-to-specific-access-points}

- 將 **default-authentication** 介面屬性的值設定為 *no*。

```ros
/interface/wireless/set station-wlan default-authentication=no
```

- 建立匹配允許的接入點的規則。這些規則必須具有 **connect**=*yes*，並且 **interface** 等於站無線介面的名稱。

```ros
/interface/wireless/connect-list/add interface=station-wlan connect=yes mac-address=00:11:22:33:00:01
/interface/wireless/connect-list/add interface=station-wlan connect=yes mac-address=00:11:22:33:00:02
```

#### 禁止連線到特定接入點 {#disallow-connections-to-specific-access-points}

- 將 **default-authentication** 介面屬性的值設定為 *yes*。

```ros
/interface/wireless/set station-wlan default-authentication=yes
```

- 建立 **connect**=*no* 規則，匹配站不應連線的那些接入點。這些規則必須具有 **connect**=*no*，並且 **interface** 等於站無線介面的名稱。

```ros
/interface/wireless/connect-list/add interface=station-wlan connect=no mac-address=00:11:22:33:44:55
```

#### 選擇首選接入點 {#select-preferred-access-points}

- 建立匹配首選接入點的規則。這些規則必須具有 **connect**=*yes*，並且 **interface** 等於站無線介面的名稱。
- 將匹配首選接入點的規則按優先順序順序放在 connect-list 中更高的位置。

#### 限制 WDS 鏈路建立 {#restrict-wds-link-establishment}

- 將匹配允許的接入點的規則放在頂部。
- 在連線列表末尾新增 deny-all 規則。

## 資訊 {#info}

**子選單：** `/interface/wireless/info`

| 屬性 | 說明 |
| :-- | :-- |
| **2ghz-10mhz-power-channels** () |  |
| **2ghz-11n-channels** () |  |
| **2ghz-5mhz-power-channels** () |  |
| **2ghz-b-channels** () |  |
| **2ghz-g-channels** () |  |
| **2ghz-g-turbo-channels** () |  |
| **5ghz-10mhz-power-channels** () |  |
| **5ghz-11n-channels** () |  |
| **5ghz-5mhz-power-channels** () |  |
| **5ghz-channels** () |  |
| **5ghz-turbo-channels** () |  |
| **allowed-channels** | 每個頻段的可用通道列表 |
| **capabilities** () |  |
| **country-info**() | 以國家/地區名稱作為引數，顯示可用頻段、頻率以及每個頻率的最大發射功率。 |
| **chip-info** () |  |
| **default-periodic-calibration** () |  |
| **firmware** () |  |
| **ht-chains** () |  |
| **interface-type** () |  |
| **name** () |  |
| **pci-info** () |  |
| **supported-bands** () |  |

## 手動 TX 功率表 {#manual-tx-power-table}

**子選單：** `/interface/wireless/manual-tx-power-table`

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*; 預設值： ) | 條目的簡短描述 |
| **manual-tx-powers** (*list of [Rate:TxPower];* Rate ::= 11Mbps \| 12Mbps \| 18Mbps \| 1Mbps \| 24Mbps \| ... *TxPower ::= integer [-30..30]*; 預設值： ) |  |
| **name** (*string*) | 將應用 TX 功率的無線介面名稱。 |

## 無線硬體表 {#wireless-hardware-table}

:::danger
您必須遵守所在國家/地區的法規域要求。如果允許您使用其他頻率，請注意天線增益和發射功率可能因板和頻率而異。裝置僅針對法規頻率進行校準。使用非標準頻率風險自負。該列表僅指定無線晶片接受的頻率，這些頻率可能由於產品內建天線、裝置設計、濾波器和其他因素而並不總是有效。嚴格風險自負
:::
可以從產品頁面推斷支援的通道寬度。為此，您需要檢查以下引數：**鏈數**和**最大資料速率**。瞭解這些引數後，您需要檢查調製和編碼方案（MCS）表，例如這裡：https://mcsindex.com/。

以 hAP ac 為例，我們可以看到鏈數為 3，MCS 表中的最大資料速率為 1300。在 MCS 表中，我們需要找到 3 個空間流——鏈——的條目以及相應的資料速率，這在此例中表明 80MHz 是支援的最大通道寬度。

**整合無線介面頻率表：**

| 板名稱 | 無線介面 | 頻率範圍 [MHz] | 支援的通道寬度 [MHz] |
| :-- | --: | :-- | :-- |
| 2011UAS-2HnD | 1 | 2312-2732 | 20,40 |
| 751G-2HnD | 1 | 2200-2700 | 20,40 及高階通道支援 |
| 751U-2HnD | 1 | 2200-2700 | 20,40 及高階通道支援 |
| 911-2Hn | 1 | 2312-2732 | 20,40 |
| 911-5HacD | 1 | 4920-6100 | 20,40,80 |
| 911-5Hn | 1 | 4920-6100 | 5,10,20,40 |
| 911-5HnD | 1 | 4920-6100 | 20,40 |
| 911G-2HPnD | 1 | 2312-2732 | 20,40 |
| 911G-5HPacDr2 /-NB /-QRT | 1 | 4920-6100 | 5,10,20,40,80 |
| 911G-5HPnD /-QRT | 1 | 4920-6100 | 5,10,20,40 |
| 912UAG-2HPnD /-OUT | 1 | 2312-2732 | 20,40 |
| 912UAG-5HPnD /-OUT | 1 | 4920-6100 | 5,10,20,40 |
| 912UAG-6HPnD /-OUT | 1 | 5500-6500 | 20,40 |
| 921GS-5HPacD-15S /-19S | 1 | 4920-6100 | 5<sup>1</sup>,10<sup>1</sup>,20,40,80 |
| 22UGS-5HPacD2HnD | 2 | 4920-5925,2412-2482 | 20,40,80 及 20,40 |
| 921UAGS-5SHPacD-NM | 1 | 4920-6100 | 20,40,80 |
| 921UAGS-5SHPacT-NM | 1 | 4920-6100 | 20,40,80 |
| 922UAGS-5HPacD /-NM | 1 | 4920-6100 | 20,40,80 |
| 922UAGS-5HPacT /-NM | 1 | 4920-6100 | 20,40,80 |
| 941-2nD /-TC | 1 | 2312-2732 | 20,40 |
| 951G-2HnD | 1 | 2312-2732 | 20,40 |
| 951Ui-2HnD | 1 | 2312-2732 | 20,40 |
| 951Ui-2nD | 1 | 2312-2732 | 20,40 |
| 952Ui-5ac2nD /-TC | 2 | 2312-2732,4920-6100 | 20,40 及 20,40,80 |
| 953GS-5HnT /-RP | 1 | 4920-6100 | 5,10,20,40 |
| 962UiGS-5HacT2HnT | 2 | 2312-2732,4920-6100 | 20,40 及 20,40,80 |
| cAP2n | 1 | 2312-2732 | 20,40 |
| cAP2nD | 1 | 2312-2732 | 20,40 |
| cAPL-2nD | 1 | 2312-2732 | 20,40 |
| CRS109-8G-1S-2HnD-IN | 1 | 2312-2732 | 20,40 |
| CRS125-24G-1S-2HnD-IN | 1 | 2312-2732 | 20,40 |
| Disc-5nD | 1 | 4920-6100 | 20,40 |
| DynaDishG-5HacD | 1 | 4920-6100 | 5<sup>1</sup>,10<sup>1</sup>,20,40,80 |
| DynaDishG-6HnD | 1 | 5500-6500 | 20,40 |
| Groove52HPn | 1 | 4920-6100,2312-2732 | 5,10,20,40 及 5,10,20,40 |
| GrooveA-52HPn | 1 | 4920-6100,2312-2732 | 5,10,20,40 及 5,10,20,40 |
| GrooveG-52HPacn | 1 | 4920-6100,2312-2732 | 20,40,80 及 20,40 |
| GrooveGA-52HPacn | 1 | 4920-6100,2312-2732 | 20,40,80 及 20,40 |
| LDF-5nD | 1 | 4920-6100 | 20,40 |
| LHG-5nD | 1 | 4920-6100 | 20,40 |
| mAP2n | 1 | 2312-2732 | 20,40 |
| mAP2nD | 1 | 2312-2732 | 20,40 |
| mAPL-2nD | 1 | 2312-2732 | 20,40 |
| Metal2SHPn | 1 | 2200-2700 | 20,40 及高階通道支援 |
| Metal5SHPn | 1 | 4800-6100 | 5,10,20,40 及高階通道支援 |
| Metal9HPn | 1 | 902-928 | 5,10,20 |
| MetalG-52SHPacn | 1 | 4920-6100,2312-2732 | 20,40,80 及 20,40 |
| OmniTikG-5HacD | 1 | 4920-6100 | 20,40,80 |
| OmniTikPG-5HacD | 1 | 4920-6100 | 20,40,80 |
| OmniTIKU-5HnD | 1 | 4800-6100 | 5,10,20,40 |
| OmniTIKUPA-5HnD | 1 | 4800-6100 | 5,10,20,40 |
| QRTG-2SHPnD | 1 | 2312-2732 | 20,40 |
| SEXTANTG-5HPnD | 1 | 4920-6100 | 20,40 |
| SXT2nDr2 | 1 | 2312-2732 | 20,40 |
| SXT5HacD2n | 2 | 2312-2732,4920-6100 | 5<sup>1</sup>,10<sup>1</sup>,20,40 及 5<sup>1</sup>,10<sup>1</sup>,20,40,80 |
| SXT5HPnDr2 | 1 | 4920-6100 | 20,40 |
| SXT5nDr2 | 1 | 4920-6100 | 20,40 |
| SXTG-2HnD | 1 | 2200-2700 | 20,40 |
| SXTG-2HnDr2 | 1 | 2300-2700 | 20,40 |
| SXTG-5HPacD | 1 | 4920-6100 | 5<sup>1</sup>,10<sup>1</sup>,20,40,80 |
| SXTG-5HPacD-HG /-SA | 1 | 4920-6100 | 5<sup>1</sup>,10<sup>1</sup>,20,40,80 |
| SXTG-5HPnD-HGr2 /-SAr2 | 1 | 4920-6100 | 20,40 |
| SXTG-6HPnD | 1 | 5500-6500 | 20,40 |
| SXTsq2nD | 1 | 2312-2484 | 20,40 |
| wAP2nD /-BE | 1 | 2312-2732 | 20,40 |
| wAPG-5HacT2HnD /-BE | 2 | 2312-2732,4920-6100 | 20,40 及 20,40,80 |
| R11e-2HnD | 1 | 2312-2732 | 20,40 |
| R11e-2HPnD | 1 | 2312-2732 | 20,40 |
| R11e-5HacD | 1 | 4920-6100 | 20,40,80 |
| R11e-5HacT | 1 | 4920-6100 | 20,40,80 |
| R11e-5HnD | 1 | 4920-6100 | 20,40 |
| R2SHPn | 1 | 2200-2700 | 20,40 及高階通道支援 |
| R52H | 1 | 4920-6100,2192-2507 | 20 及 20 |
| R52HnD | 1 | 4800-6100,2200-2700 | 20,40 及 20,40 |
| R52nM | 1 | 4800-6100,2200-2700 | 20,40 及 20,40 及高階通道支援 |
| R5SHPn | 1 | 4800-6100 | 20,40 及高階通道支援 |

**注意：**

1. 僅適用於 802.11a/n 標準。

## 高階通道 {#advanced-channels}

高階通道功能為無線介面配置提供了更多可能性：

- 覆蓋多個頻段和通道寬度的 scan-list。
- 對於允許的硬體，支援非標準通道中心頻率（以 kHz 為粒度指定）。
- 對於允許的硬體，支援非標準通道寬度（以 kHz 為粒度指定）。

### 硬體支援 {#hardware-support}

非標準中心頻率和寬度通道只能與支援它們的介面一起使用。

只有基於 **Atheros AR92xx** 的晶片支援非標準中心頻率和寬度，範圍如下：

- 中心頻率範圍：2200 MHz-2500 MHz，步進 0.5 MHz（500 kHz），寬度範圍：2.5 MHz-30 MHz，步進 0.5 MHz（500 kHz）。
- 中心頻率範圍：4800 MHz-6100 MHz，步進 0.5 MHz（500 kHz），寬度範圍：2.5 MHz-30 MHz，步進 0.5 MHz（500 kHz）。

AR93xx 不支援此功能。

## 配置高階通道 {#configuring-advanced-channels}

高階通道在 **interface wireless channels** 選單中配置。此選單包含使用者定義通道的有序列表，可透過 **list** 屬性進行分組。通道具有以下屬性：

- **name** - 可用於引用此通道的名稱。如果在新增通道時未指定 **name**，則會根據通道頻率和寬度自動生成。
- **list** - 此通道所屬列表的名稱。列表可用於對通道進行分組。
- **frequency** - 通道中心頻率，單位為 MHz，允許指定小數 MHz 部分，例如 **5181.5**。
- **width** - 通道寬度，單位為 MHz，允許指定小數 MHz 部分，例如 **14.5**。
- **band** - 定義使用此通道時的預設資料速率集合。
- **extension-channel** - 指定 11n 擴充套件通道的位置。

## 使用高階通道 {#using-advanced-channels}

要在無線介面配置中使用高階通道，有幾個介面設定接受通道名稱或列表名稱作為引數。可以為介面配置其不支援的頻道。在這種情況下，介面將無法執行。管理員完全負責以正確方式配置通道。

### frequency {#frequency}

要為無線介面使用特定的高階通道（適用於使用介面 **frequency** 設定的模式），請在介面 **frequency** 設定中指定通道名稱。例如，要將介面配置為以 5500MHz 中心頻率和 14MHz 通道寬度執行，請使用以下命令：

```
[admin@MikroTik] /interface/wireless> channels add name=MYCHAN frequency=5500 width=14 band=5ghz-onlyn
 list=MYLIST
[admin@MikroTik] /interface/wireless> set wlan1 frequency=MYCHAN 
```

### scan-list {#scan-list}

介面 **scan-list** 用於多種模式，這些模式要麼收集通道列表資訊（例如互動式 **scan** 命令），要麼選擇要工作的通道（例如任何 **station** 模式或執行 DFS 的 AP 模式）。介面 **scan-list** 可以配置為以下各項的逗號分隔列表：

- **default** - 給定國家/地區、介面頻段和通道寬度的預設 .11 通道列表。
- 以 MHz 為單位的數字頻率範圍。
- 按名稱引用的高階通道。
- 按列表名稱引用的高階通道列表。

例如，要將介面配置為首先使用 20MHz 通道寬度掃描 5180MHz、5200MHz 和 5220MHz，然後使用 10MHz 通道寬度，可以發出以下命令：

```
[admin@MikroTik] /interface/wireless> channels add frequency=5180 width=20 band=5ghz-a list=20MHz-list
[admin@MikroTik] /interface/wireless> channels add frequency=5200 width=20 band=5ghz-a list=20MHz-list
[admin@MikroTik] /interface/wireless> channels add frequency=5220 width=20 band=5ghz-a list=20MHz-list
[admin@MikroTik] /interface/wireless> channels add frequency=5180 width=10 band=5ghz-a list=10MHz-list
[admin@MikroTik] /interface/wireless> channels add frequency=5200 width=10 band=5ghz-a list=10MHz-list
[admin@MikroTik] /interface/wireless> channels add frequency=5220 width=10 band=5ghz-a list=10MHz-list
[admin@MikroTik] /interface/wireless> set wlan1 scan-list=20MHz-list,10MHz-list
```

## Nstreme {#nstreme}

**子選單：** `/interface/wireless/nstreme`

此選單允許將無線卡切換到 nstreme 模式。在這種情況下，該卡將僅與 nstreme 用戶端配合工作。

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*; 預設值： ) | 條目的簡短描述 |
| **disable-csma** (*yes \| no*; 預設值：**no**) | 使用輪詢時停用 CSMA/CA（效能更好） |
| **enable-nstreme** (*yes \| no*; 預設值：**no**) | 是否將卡切換到 nstreme 模式 |
| **enable-polling** (*yes \| no*; 預設值：**yes**) | 是否對用戶端使用輪詢 |
| **framer-limit** (*integer [100..4000]*; 預設值：**3200**) | 最大幀大小 |
| **framer-policy** (*best-fit \| dynamic-size \| exact-size \| none*; 預設值：**none**) | 合併幀的方法。可以將多個幀合併為更大的幀，以減少協定開銷（從而提高速度）。卡不會等待幀，但如果有多 個數據包排隊等待發送，它們可以被合併。有幾種組幀方法：**none** - 不做特殊處理，不合並封包（停用組幀）**best-fit** - 在達到 framer-limit 限制之前，儘可能多地將封包放入一個幀中，但不分片封包**exact-size** - 在達到 framer-limit 限制之前，儘可能多地將封包放入一個幀中，即使需要分片（最佳效能）**dynamic-size** - 動態選擇最佳幀大小 |
| **name** (*string*) | 將應用設定的介面名稱。只讀。 |

:::note
這裡的設定（啟用 Nstreme 除外）僅與接入點相關，對用戶端裝置將被忽略。用戶端會自動適配 AP 設定。  
Nstreme 協定的 WDS 需要在其中一個對端使用 station-wds 模式。AP 模式（bridge 和 ap-bridge）之間的 WDS 配置將無法工作。
:::

## Nstreme Dual {#nstreme-dual}

**子選單：** `/interface/wireless/nstreme-dual`

兩個處於 nstreme-dual-slave 模式的無線電可以組合在一起，形成 nstreme2 點對點連線。要將無線介面放入 nstreme2 組，應將其模式設定為 nstreme-dual-slave。使用 nstreme2 時，/interface/wireless 選單中的許多引數會被忽略，但以下引數除外：

- frequency-mode
- country
- antenna-gain
- tx-power
- tx-power-mode
- antenna-mode

| 屬性 | 描述 |
| :-- | :-- |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; 預設值：**enabled**) | [ARP](../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together) |
| **comment** (*string*; 預設值： ) | 條目的簡短描述 |
| **disable-csma** (*yes \| no*; 預設值：**no**) | 停用 CSMA/CA（效能更好） |
| **disable-running-check** (*yes \| no*; 預設值：**no**) | 即使沒有連線到遠端對端，是否也應始終將介面視為正在執行 |
| **disabled** (*yes \| no*; 預設值：**yes**) |  |
| **framer-limit** (*integer [64..4000]*; 預設值：**2560**) | 最大幀大小 |
| **framer-policy** (*best-fit \| exact-size \| none*; 預設值：**none**) | 合併幀的方法。可以將多個幀合併為一個更大的幀，以減少協定開銷（從而提高速度）。卡不會等待幀，但如果有多 個數據包排隊等待發送，它們可以被合併。有幾種組幀方法：**none** - 不做特殊處理，不合並封包**best-fit** - 在達到 framer-limit 限制之前，儘可能多地將封包放入一個幀中，但不分片封包**exact-size** - 在達到 framer-limit 限制之前，儘可能多地將封包放入一個幀中，即使需要分片（最佳效能） |
| **ht-channel-width** (*2040mhz \| 20mhz \| 40mhz*; 預設值：**20mhz**) |  |
| **ht-guard-interval** (*both \| long \| short*; 預設值：**long**) |  |
| **ht-rates** (*list of rates [1,2,3,4,5,6,7,8]*; 預設值：**1,2,3,4,5,6,7,8**) |  |
| **ht-streams** (*both \| double \| single*; 預設值：**single**) |  |
| **l2mtu** (*integer [0..65536]*; 預設值： ) |  |
| **mtu** (*integer [0..65536]*; 預設值：**1500**) |  |
| **name** (*string*; 預設值： ) | 條目名稱 |
| **rates-a/g** (*list of rates [6Mbps,9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps]*; 預設值：**6Mbps,9Mbps,12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps**) | 802.11a 或 802.11g 標準中要支援的速率 |
| **rates-b** (*list of rates [1Mbps, 2Mbps, 5.5Mbps, 11Mbps]*; 預設值：**1Mbps, 2Mbps, 5.5Mbps, 11Mbps**) | 802.11b 標準中要支援的速率 |
| **remote-mac** (*MAC*; 預設值：**00:00:00:00:00:00**) | 要連線到的 MAC 地址（這將是遠端接收卡的 MAC 地址） |
| **rx-band** (*2ghz-b \| 2ghz-g \| 2ghz-n \| 5ghz-a \| 5ghz-n*; 預設值： ) | 接收無線電的工作頻段 |
| **rx-channel-width** (*20mhz \| 40mhz \| 10mhz \| 5mhz*; 預設值：**20mhz**) |  |
| **rx-frequency** (*integer [0..4294967295]*; 預設值： ) | RX 卡工作頻率，單位為 Mhz。 |
| **rx-radio** (*string*; 預設值： ) | 用於接收的介面名稱。 |
| **tx-band** (*2ghz-b \| 2ghz-g \| 2ghz-n \| 5ghz-a \| 5ghz-n*; 預設值： ) | 發射無線電的工作頻段 |
| **tx-channel-width** (*20mhz \| 40mhz \| 10mhz \| 5mhz*; 預設值：**20mhz**) |  |
| **tx-frequency** (*integer [0..4294967295]*; 預設值： ) | TX 卡工作頻率，單位為 Mhz。 |
| **tx-radio** (*string*; 預設值： ) | 用於傳送的介面名稱。 |

:::warning
WDS 不能用於 Nstreme-dual 鏈路。
:::

:::note
**tx-freq** 與 **rx-freq** 之間的差值應為約 200 MHz 或更大，因為可能存在干擾。
:::

:::note
您可以為 RX 和 TX 鏈路使用不同頻段。例如，在 2ghz-g 中傳送，並使用 2ghz-b 頻段接收資料。
:::

## 登錄檔 {#registration-table}

**子選單：** `/interface/wireless/registration-table`

在登錄檔中，您可以檢視當前已連線用戶端的各種資訊。它僅用於接入點。

所有屬性均為只讀。

| 屬性 | 說明 |
| :-- | :-- |
| **802.1x-port-enabled** (*yes \| no*) | 是否允許與該對端進行資料交換（即，如果需要，802.1x 認證是否已完成） |
| **ack-timeout** (*integer*) | ack-timeout 的當前值 |
| **ap** (*yes \| no*) | 顯示已註冊裝置是否配置為接入點。 |
| **ap-tx-limit** (*integer*) | AP 上的傳輸速率限制，單位為位元每秒 |
| **authentication-type** () | 用於該對端的認證方法 |
| **bridge** (*yes \| no*) |  |
| **bytes** (*integer , integer*) | 已傳送和已接收的封包位元組數 |
| **client-tx-limit** (*integer*) | 用戶端上的傳輸速率限制，單位為位元每秒 |
| **comment** (*string*) | 條目的描述。如果指定，註釋取自相應的 [訪問列表](./wireless-interface.md#access-list) 條目。 |
| **compression** (*yes \| no*) | 此對端是否使用資料壓縮 |
| **distance** (*integer*) |  |
| **eap-identity**(*string*) | 用戶端向 RADIUS 伺服器認證時使用的 EAP 身份。 |
| **encryption** (*aes-ccm \| tkip*) | 使用的單播加密演算法 |
| **evm-ch0** () |  |
| **evm-ch1** () |  |
| **evm-ch2** () |  |
| **frame-bytes** (*integer,integer*) | 已傳送和已接收的資料位元組數，不包括頭部資訊 |
| **frames** (*integer,integer*) | 需要透過無線鏈路傳送的幀數。此值可與 **hw-frames** 比較，以檢查無線重傳。  |
| **framing-current-size** (*integer*) | 當前合併幀的大小 |
| **framing-limit** (*integer*) | 合併幀的最大大小 |
| **framing-mode** () | 合併幀的方法 |
| **group-encryption** () | 使用的組加密演算法 |
| **hw-frame-bytes** (*integer,integer*) | 已傳送和已接收的資料位元組數，包括頭部資訊 |
| **hw-frames** (*integer,integer*) | 驅動程式透過無線鏈路傳送的幀數。此值可與 **frames** 比較，以檢查無線重傳。  |
| **interface** (*string*) | 無線用戶端關聯到的無線介面名稱 |
| **last-activity** (*time*) | 介面最後一次資料 tx/rx 活動 |
| **last-ip** (*IP Address*) | 從已註冊用戶端收到的最後一個 IP 封包中找到的 IP 地址 |
| **mac-address** (*MAC*) | 已註冊用戶端的 MAC 地址 |
| **management-protection** (*yes \| no*) |  |
| **nstreme** (*yes \| no*) | 顯示是否啟用了 [Nstreme](./wireless-interface.md#nstreme) |
| **p-throughput** (*integer*) | 考慮到有效傳輸速率和硬體重試，預期到給定對端的估計近似吞吐量。每 5 秒計算一次 |
| **packed-bytes** (*integer, integer*) | 為傳送/接收（組幀）打包到較大幀中的位元組數 |
| **packed-frames** (*integer, integer*) | 為傳送/接收（組幀）打包到較大幀中的幀數 |
| **packets** (*integer,integer*) | 已傳送和已接收的網路層封包數 |
| **radio-name** (*string*) | 對端的 radio name |
| **routeros-version** (*string*) | 已註冊用戶端的 RouterOS 版本 |
| **rx-ccq** () | 接收方向的用戶端連線質量（CCQ）。  |
| **rx-rate** (*integer*) | 接收資料速率 |
| **signal-strength** (*integer*) | AP 接收到的用戶端訊號平均強度 |
| **signal-strength-ch0** () |  |
| **signal-strength-ch1** () |  |
| **signal-strength-ch2** () |  |
| **signal-to-noise** () |  |
| **strength-at-rates** () | 不同速率下的訊號強度水平，以及使用這些速率的時間 |
| **tdma-retx** () |  |
| **tdma-rx-size** () |  |
| **tdma-timing-offset** () | tdma-timing-offset 與 **distance** 成正比，約為傳播延遲的兩倍。AP 測量此值，以便告訴用戶端其傳輸應使用的偏移量——然後用戶端從目標傳輸時間中減去此偏移量，從而考慮傳播延遲，使傳輸在預期時間到達 AP。對於近距離用戶端，您可能偶爾會看到小的負值（例如幾 usec），這是由於傳送器或接收器硬體中可能產生的額外未計入延遲，不同晶片組有所不同。 |
| **tdma-tx-size** (*integer*) | 以位元組為單位的值，指定裝置傳送的可檢測丟失的資料單元大小（計算 CRC 的資料單元）。一般來說——越大越好，因為開銷更少。另一方面，此設定中的小值不能總被視為連線質量差的訊號——如果裝置沒有足夠多待處理資料以使用更大的資料單元（例如，如果您只是透過鏈路 ping），此值不會上升。 |
| **tdma-windfull** () |  |
| **tx-ccq** () | 傳送方向的用戶端連線質量（CCQ）。  |
| **tx-evm-ch0** () |  |
| **tx-evm-ch1** () |  |
| **tx-evm-ch2** () |  |
| **tx-frames-timed-out** () |  |
| **tx-rate** () |  |
| **tx-signal-strength** () |  |
| **tx-signal-strength-ch0** () |  |
| **tx-signal-strength-ch1** () |  |
| **tx-signal-strength-ch2** () |  |
| **uptime** (*time*) | 用戶端與接入點關聯的時間 |
| **wds** (*yes \| no*) | 已連線用戶端是否使用 WDS |
| **wmm-enabled** (*yes \| no*) | 顯示是否啟用了 [WMM](../../bridging-and-switching/user-guides/wmm-and-vlan-priority.md)。 |

## 安全配置檔案 {#security-profiles}

**子選單：** `/interface/wireless/security-profiles`

安全配置檔案在控制檯的 **/interface/wireless/security-profiles** 路徑下配置，或在 WinBox 的“Wireless”視窗的“Security Profiles”標籤頁中配置。安全配置檔案由無線介面的 [security-profile](./wireless-interface.md#general-interface-properties) 屬性和連線列表的 [security-profile](./wireless-interface.md#general-interface-properties) 屬性引用。

### 基本屬性 {#basic-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **mode** (*none \| static-keys-optional \| static-keys-required \| dynamic-keys*; 預設值：**none**) | 安全配置檔案的加密模式。none - 不使用加密。不接受加密幀。static-keys-required - WEP 模式。不接受也不傳送未加密幀。處於 *static-keys-required* 模式的站不會連線到處於 *static-keys-optional* 模式的接入點。static-keys-optional - WEP 模式。支援加密和解密，但也允許接收和傳送未加密幀。如果加密演算法指定為 *none*，裝置將傳送未加密幀。處於 *static-keys-optional* 模式的站不會連線到處於 *static-keys-required* 模式的接入點。另請參閱：[static-sta-private-algo](./wireless-interface.md#properties-1)、[static-transmit-key](./wireless-interface.md#properties-1)。dynamic-keys - WPA 模式。 |
| **name** (*text*; 預設值： ) | 安全配置檔案的名稱 |

### WPA 屬性 {#wpa-properties}

這些屬性僅在 **mode** 設定為 *dynamic-keys* 時生效。

| 屬性 | 描述 |
| :-- | :-- |
| **authentication-types** (*wpa-psk \| wpa2-psk \| wpa-eap \| wpa2-eap*; 預設值： ) | 支援的認證型別集合，可選擇多個值。接入點將通告支援的認證型別，用戶端僅在支援任何通告的認證型別時才會連線到接入點。 |
| **disable-pmkid** (*no \| yes*; 預設值：**no**) | 是否將 PMKID 包含在接入點發送的 EAPOL 幀中。停用 PMKID 可能導致與使用 PMKID 連線到接入點的裝置出現相容性問題。yes - 從 EAPOL 幀中移除 PMKID（提高安全性，降低相容性）。no - 將 PMKID 包含在 EAPOL 幀中（降低安全性，提高相容性）。此屬性僅對接入點有效。 |
| **unicast-ciphers** (*tkip \| aes-ccm*; 預設值：**aes-ccm**) | 接入點通告其支援指定加密套件，可選擇多個值。用戶端僅嘗試連線到至少支援指定加密套件之一的接入點。其中一個加密套件將用於加密接入點和站之間傳送的單播幀。 |
| **group-ciphers** (*tkip \| aes-ccm*; 預設值：**aes-ccm**) | 接入點通告這些加密套件之一，可選擇多個值。接入點使用它來加密所有廣播和組播幀。用戶端僅嘗試連線到使用指定組加密套件之一的接入點。tkip - 臨時金鑰完整性協定 - 一種加密協定，與舊版 WEP 裝置相容，但經過增強以糾正一些 WEP 缺陷。aes-ccm - 更安全的 WPA 加密協定，基於可靠的 AES（高階加密標準）。沒有 WEP 遺留問題的網路應僅使用此加密套件。 |
| **group-key-update** (*time: 30s..1d*; 預設值：**5m**) | 控制接入點更新組金鑰的頻率。此金鑰用於加密所有廣播和組播幀。此屬性僅對 Access Points 有效。 |
| **wpa-pre-shared-key** (*text*; 預設值： ) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | WPA 預共享金鑰模式要求 BSS 中的所有裝置具有公共秘密金鑰。此金鑰的值可以是任意文字。通常稱為 WPA 模式的網路密碼。此屬性僅在 *wpa-psk* 新增到 **authentication-types** 時生效。 |
| **wpa2-pre-shared-key** (*text*; 預設值： ) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | WPA2 預共享金鑰模式要求 BSS 中的所有裝置具有公共秘密金鑰。此金鑰的值可以是任意文字。通常稱為 WPA2 模式的網路密碼。此屬性僅在 *wpa2-psk* 新增到 **authentication-types** 時生效。 |

:::note
 RouterOS 還允許使用 [private-pre-shared-key](./wireless-interface.md#access-list) 屬性或 RADIUS MAC 認證響應中的 [Mikrotik-Wireless-Psk](./wireless-interface.md#radius-mac-authentication) 屬性覆蓋特定用戶端的預共享金鑰值。這是一個擴充套件。
:::

#### WPA EAP 屬性 {#wpa-eap-properties}

這些屬性僅在 **authentication-types** 包含 *wpa-eap* 或 *wpa2-eap*，且 **mode** 設定為 *dynamic-keys* 時生效。

| 屬性 | 描述 |
| :-- | :-- |
| **eap-methods** (*eap-tls \| eap-ttls-mschapv2 \| passthrough \| peap*; 預設值：**passthrough**) | 允許的認證方法型別，可選擇多個值。此屬性僅對 Access Points 有效。eap-tls - 使用內建 EAP TLS 認證。支援用戶端和伺服器證書。請參閱 **tls-mode** 和 **tls-certificate** 屬性的描述。eap-ttls-mschapv2 - 使用帶 MS-CHAPv2 認證的 EAP-TTLS。passthrough - 接入點將把認證過程轉發到 RADIUS 伺服器。peap - 使用受保護的 EAP 認證。 |
| **supplicant-identity** (*text*; 預設值：**[身份](../../system-information-and-utilities/identity.md)**) | 用戶端在 EAP 認證開始時傳送的 EAP 身份。此值用作 RADIUS EAP 計費和 RADIUS EAP 直通認證傳送的 RADIUS 訊息中 User-Name 屬性的值。 |
| **mschapv2-username** (*text*; 預設值： ) | 使用 *eap-ttls-mschapv2* 或 *peap* 認證方法時用於認證的使用者名稱。此屬性僅對 Stations 有效。 |
| **mschapv2-password** (*text*; 預設值： ) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 使用 *eap-ttls-mschapv2* 或 *peap* 認證方法時用於認證的密碼。此屬性僅對 Stations 有效。 |
| **tls-mode** (*verify-certificate \| dont-verify-certificate \| no-certificates \| verify-certificate-with-crl*; 預設值：**no-certificates**) | 此屬性僅在 **eap-methods** 包含 *eap-tls* 時生效。verify-certificate - 要求遠端裝置具有有效證書。檢查它是否由已知證書頒發機構簽名。不進行額外的身份驗證。證書可能包含有關其有效期的資訊。如果路由器的時間和日期不正確，它可能拒絕有效證書，因為路由器的時鐘不在該期間內。另請參閱 [證書](../../authentication-authorization-accounting/certificates.md) 配置。dont-verify-certificate - 不檢查遠端裝置的證書。接入點不會要求用戶端提供證書。no-certificates - 不使用證書。TLS 會話使用 2048 位匿名 Diffie-Hellman 金鑰交換建立。verify-certificate-with-crl - 與 *verify-certificate* 相同，但還會透過檢查證書吊銷列表來檢查證書是否有效。 |
| **tls-certificate** (*none \| name*; 預設值：**none**) | 當配置了接入點且 **tls-mode** 設定為 *verify-certificate* 或設定為 *dont-verify-certificate* 時，接入點始終需要證書。用戶端僅在接入點配置為 **tls-mode** 設定為 *verify-certificate* 時才需要證書。在這種情況下，用戶端需要由接入點已知的 CA 簽名的有效證書。此屬性僅在 **tls-mode** 未設定為 *no-certificates* 且 **eap-methods** 包含 *eap-tls* 時生效。 |

:::note
`eap-methods` 中允許的認證方法順序很重要，傳送給 Station 的認證方法提議將使用相同順序。示例：接入點使用安全配置檔案，其中 **eap-methods** 設定為 *eap-tls*、*passthrough*；1) 接入點向用戶端提供 EAP-TLS 方法；2) 用戶端拒絕；3) 接入點開始將 EAP 通訊轉發到 RADIUS 伺服器。
:::
:::note
 當 AP 用於直通時，AP 本身不需要證書，AP 裝置作為透明網橋工作，並將 EAP-TLS 關聯資料從 RADIUS 伺服器轉發到終端用戶端。
:::
:::note
 當 `tls-mode` 使用 `verify-certificate` 或 `dont-verify-certificate` 時，遠端裝置必須支援 *RC4-MD5*、*RC4-SHA* 或 *DES-CBC3-SHA* TLS 加密套件之一。使用 `no-certificates` 模式時，遠端裝置必須支援 "ADH-DES-CBC3-SHA" 加密套件。
:::

#### RADIUS 屬性 {#radius-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **radius-mac-authentication** (*yes \| no*; 預設值：**no**) | 此屬性影響接入點處理未在 [訪問列表](./wireless-interface.md#radius-mac-authentication) 中找到的用戶端的方式。no - 根據無線介面的 [default-authentication](./wireless-interface.md#general-interface-properties) 屬性的值允許或拒絕用戶端認證。yes - 使用用戶端的 MAC 地址作為使用者名稱查詢 RADIUS 伺服器。使用此設定時，[default-authentication](./wireless-interface.md#general-interface-properties) 的值無效。 |
| **radius-mac-accounting** (*yes \| no*; 預設值：**no**) |  |
| **radius-eap-accounting** (*yes \| no*; 預設值：**no**) |  |
| **radius-called-format** (*mac \| mac:ssid \| ssid*; 預設值：**mac:ssid**) |  |
| **interim-update** (*time*; 預設值：**0**) | 使用 RADIUS 計費時，接入點會定期向 RADIUS 伺服器傳送計費資訊更新。此屬性指定預設更新間隔，可由 RADIUS 伺服器使用 [Acct-Interim-Interval](./wireless-interface.md#radius-mac-authentication) 屬性覆蓋。 |
| **radius-mac-format** (*XX:XX:XX:XX:XX:XX \| XXXX:XXXX:XXXX \| XXXXXX:XXXXXX \| XX-XX-XX-XX-XX-XX \| XXXXXX-XXXXXX \| XXXXXXXXXXXX \| XX XX XX XX XX XX \| lower case;* 預設值：**XX:XX:XX:XX:XX:XX**) | 控制接入點在 MAC 認證和 MAC 計費 RADIUS 請求的 User-Name 屬性中如何編碼用戶端的 MAC 地址。 |
| **radius-mac-mode** (*as-username \| as-username-and-password*; 預設值：**as-username**) | 預設情況下，接入點在 MAC 認證期間傳送 Access-Request 時使用空密碼。當此屬性設定為 *as-username-and-password* 時，接入點將把與 User-Name 屬性相同的值用於 User-Password 屬性。 |
| **radius-mac-caching** (*disabled \| time*; 預設值：**disabled**) | 如果此值設定為時間間隔，接入點將快取 RADIUS MAC 認證響應指定時間，並且如果已存在匹配的快取條目，則不會聯絡 RADIUS 伺服器。值 *disabled* 將停用快取，接入點將始終聯絡 RADIUS 伺服器。 |

#### WEP 屬性 {#wep-properties}

這些屬性僅在 **mode** 設定為 *static-keys-required* 或 *static-keys-optional* 時生效。

| 屬性 | 說明 |
| :-- | :-- |
| **static-key-0 \| static-key-1 \| static-key-2 \| static-key-3** (*hex*; 預設值： ) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 金鑰的十六進位制表示。金鑰長度必須適合所選演算法。請參閱 [靜態配置的 WEP 金鑰](./wireless-interface.md#statically-configured-wep-keys) 部分。 |
| **static-algo-0 \| static-algo-1 \| static-algo-2 \| static-algo-3** (*none \| 40bit-wep \| 104bit-wep \| tkip \| aes-ccm*; 預設值：**none**) | 與相應金鑰一起使用的加密演算法。 |
| **static-transmit-key** (*key-0 \| key-1 \| key-2 \| key-3*; 預設值：**key-0**) | 接入點將使用指定金鑰為不使用私有金鑰的用戶端加密幀。接入點還將使用此金鑰加密廣播和組播幀。如果 **static-sta-private-algo** 設定為 *none*，用戶端將使用指定金鑰加密幀。如果相應的 **static-algo-N** 屬性的值設定為 *none*，則幀將以未加密方式傳送（當 **mode** 設定為 *static-keys-optional* 時），或者根本不會發送（當 **mode** 設定為 *static-keys-required* 時）。 |
| **static-sta-private-key** (*hex*; 預設值： ) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 金鑰長度必須適合所選演算法，請參閱 [靜態配置的 WEP 金鑰](./wireless-interface.md#statically-configured-wep-keys) 部分。此屬性僅在 Stations 上使用。接入點使用來自 [private-key](./wireless-interface.md#access-list) 屬性或 [Mikrotik-Wireless-Enc-Key](./wireless-interface.md#radius-mac-authentication) 屬性的相應金鑰。 |
| **static-sta-private-algo** (*none \| 40bit-wep \| 104bit-wep \| tkip \| aes-ccm*; 預設值：**none**) | 與站私有金鑰一起使用的加密演算法。值 *none* 停用私有金鑰的使用。此屬性僅在 Stations 上使用。接入點必須從 [private-algo](./wireless-interface.md#access-list) 屬性或 [Mikrotik-Wireless-Enc-Algo](./wireless-interface.md#radius-mac-authentication) 屬性獲取相應值。站私有金鑰會替換單播幀的金鑰 0。站不會使用私有金鑰解密廣播幀。 |

### 管理幀保護 {#management-frame-protection}

***用於**：防止去認證攻擊、MAC 地址克隆問題。*

RouterOS 實現了一種基於共享秘密的專有管理幀保護演算法。管理幀保護意味著 RouterOS 無線裝置能夠驗證管理幀的來源，並確認特定幀不是惡意的。此功能允許抵禦針對基於 RouterOS 的無線裝置的去認證和解除關聯攻擊。

管理保護模式在安全配置檔案中透過 **management-protection** 設定配置。可能的值為：**disabled** - 管理保護已停用（預設），**allowed** - 如果遠端方支援，則使用管理保護（對於 AP - 允許非管理保護和管理保護用戶端，對於用戶端 - 連線到支援和不支援管理保護的 AP），**required** - 僅與支援管理保護的遠端裝置建立關聯（對於 AP - 僅接受支援管理保護的用戶端，對於用戶端 - 僅連線到支援管理保護的 AP）。

管理保護共享秘密透過安全配置檔案 **management-protection-key** 設定配置。

當介面處於 AP 模式時，預設管理保護金鑰（在安全配置檔案中配置）可由訪問列表或 RADIUS 屬性中指定的金鑰覆蓋。

```
[admin@mikrotik] /interface/wireless/security-profiles> print 
 0 name="default" mode=none authentication-types="" unicast-ciphers="" 
  group-ciphers="" wpa-pre-shared-key="" wpa2-pre-shared-key="" 
  supplicant-identity="n-str-p46" eap-methods=passthrough 
  tls-mode=no-certificates tls-certificate=none static-algo-0=none 
  static-key-0="" static-algo-1=none static-key-1="" static-algo-2=none 
  static-key-2="" static-algo-3=none static-key-3="" 
  static-transmit-key=key-0 static-sta-private-algo=none 
  static-sta-private-key="" radius-mac-authentication=no 
  radius-mac-accounting=no radius-eap-accounting=no interim-update=0s 
  radius-mac-format=XX:XX:XX:XX:XX:XX radius-mac-mode=as-username 
  radius-mac-caching=disabled group-key-update=5m 
  management-protection=disabled management-protection-key=""  
```

```
[admin@mikrotik] /interface/wireless/security-profiles> set default management-protection=    
                                                        allowed  disabled  required  
```

![](/img/b5298b7432544ff5.webp)

### 操作詳情 {#operation-details}

#### RADIUS MAC 認證 {#radius-mac-authentication}

:::note
RADIUS MAC 認證由接入點用於未在 [access-list](./wireless-interface.md#access-list) 中找到的用戶端，類似於無線介面的 **default-authentication** 屬性。它控制是否允許用戶端繼續認證，還是立即拒絕。
:::
當 **radius-mac-authentication**=*yes* 時，接入點透過傳送具有以下屬性的 Access-Request 來查詢 RADIUS 伺服器：

- User-Name - 用戶端 MAC 地址。按照 **radius-mac-format** 設定指定的方式進行編碼。預設編碼為 "XX:XX:XX:XX:XX:XX"。
- Nas-Port-Id - 無線介面的 **name**。
- User-Password - 當 **radius-mac-mode**=*as-username-and-password* 時，設定為與 User-Name 相同的值。否則此屬性為空。
- Calling-Station-Id - 用戶端 MAC 地址，編碼為 "XX-XX-XX-XX-XX-XX"。
- Called-Station-Id - 接入點的 MAC 地址和 SSID，編碼為 "XX-XX-XX-XX-XX-XX:SSID"（由減號分隔的 MAC 地址數字對，後跟冒號，再後跟 SSID 值）。
- Acct-Session-Id - 當 **radius-mac-accounting**=*yes* 時新增。

當接入點收到來自 RADIUS 伺服器的 Access-Accept 或 Access-Reject 響應時，它會儲存響應並允許或拒絕用戶端。接入點使用 Access-Accept 響應中的以下 RADIUS 屬性：

- Ascend-Data-Rate。
- Ascend-Xmit-Rate。
- Mikrotik-Wireless-Forward - 與 [access-list](./wireless-interface.md#access-list) 的 **forwarding** 相同。
- Mikrotik-Wireless-Enc-Algo - 與 [access-list](./wireless-interface.md#access-list) 的 **private-algo** 相同。
- Mikrotik-Wireless-Enc-Key - 與 [access-list](./wireless-interface.md#access-list) 的 **private-key** 相同。
- Mikrotik-Wireless-Psk - 與 [access-list](./wireless-interface.md#access-list) 的 **private-pre-shared-key** 相同。
- Mikrotik-Wireless-Mpkey - 與訪問列表中的 Management-protection-key 相同。
- Session-Timeout - 在此時間後用戶端將斷開連線。
- Acct-Interim-Interval - 覆蓋 **interim-update** 的值。
- Class - 如果存在，此屬性的值將被儲存幷包含在 Accounting-Request 訊息中。

**快取**：

新增 RADIUS MAC 認證快取是為了支援那些需要接入點非常快速響應關聯請求的用戶端的 RADIUS 認證。此類用戶端在收到 RADIUS 伺服器響應之前就會超時。接入點會快取認證響應一段時間，並可以立即回覆來自同一用戶端的重複關聯請求。

#### RADIUS EAP 直通認證 {#radius-eap-pass-through-authentication}

使用 WPA EAP 認證型別時，已透過 MAC 認證的用戶端需要執行 EAP 認證，然後才被授權在無線網路上傳遞資料。使用直通 EAP 方法時，接入點將把認證轉發到 RADIUS 伺服器，並在 Access-Request RADIUS 訊息中使用以下屬性：

- User-Name - EAP 請求者身份。此值在用戶端安全配置檔案的 **supplicant-identity** 屬性中配置。
- Nas-Port-Id - 無線介面的 **name**。
- Calling-Station-Id - 用戶端 MAC 地址，編碼為 "XX-XX-XX-XX-XX-XX"。
- Called-Station-Id - 接入點的 MAC 地址和 SSID，編碼為 "XX-XX-XX-XX-XX-XX:SSID"（由減號分隔的 MAC 地址數字對，後跟冒號，再後跟 SSID 值）。
- Acct-Session-Id - 當 **radius-eap-accounting**=*yes* 時新增。
- Acct-Multi-Session-Id - 接入點和用戶端的 MAC 地址，以及一個唯一的 8 位元組值，該值在所有共享單個 EAP 認證的計費會話之間共享。編碼為 *AA-AA-AA-AA-AA-AA-CC-CC-CC-CC-CC-CC-XX-XX-XX-XX-XX-XX-XX-XX。* 當 radius-eap-accounting=yes 時新增。

接入點使用 Access-Accept 伺服器響應中的以下 RADIUS 屬性：

- Class - 如果存在，此屬性的值將被儲存幷包含在 Accounting-Request 訊息中。
- Session-Timeout - 在此時間後用戶端將斷開連線。此外，接入點將記住認證結果，如果在此期間用戶端重新連線，它將立即被授權，而無需重複 EAP 認證。
- Acct-Interim-Interval - 覆蓋 **interim-update** 的值。

#### 靜態配置的 WEP 金鑰 {#statically-configured-wep-keys}

不同演算法需要不同長度的金鑰：

- *40bit-wep* - 10 個十六進位制數字（40 位）。如果金鑰更長，則僅使用前 40 位。
- *104bit-wep* - 26 個十六進位制數字（104 位）。如果金鑰更長，則僅使用前 104 位。
- *tkip* - 至少 64 個十六進位制數字（256 位）。
- *aes-ccm* - 至少 32 個十六進位制數字（128 位）。

金鑰必須包含偶數個十六進位制數字。

#### WDS 安全配置 {#wds-security-configuration}

WDS 鏈路可以使用所有可用的安全功能。但是，它們需要仔細配置安全引數。

可以為所有用戶端使用一個安全配置檔案，併為 WDS 鏈路使用不同的安全配置檔案。WDS 鏈路的安全配置檔案在 [connect-list](./wireless-interface.md#connect-list) 中指定。接入點在與另一接入點建立 WDS 鏈路之前始終檢查連線列表，並使用匹配的連線列表條目中的安全設定。當每個接入點都有匹配另一裝置的連線列表條目、具有 **connect**=*yes* 並指定相容的 **security-profile** 時，WDS 鏈路將工作。

**WDS 和 WPA/WPA2：**

如果接入點使用 **mode**=*dynamic-keys* 的安全配置檔案，則所有 WDS 鏈路都將使用加密。由於 WPA 認證和金鑰交換不是對稱的，其中一個接入點將充當用戶端以建立安全連線。這類似於 *static-mesh* 和 *dynamic-mesh* WDS 模式的工作方式。如果啟用 WPA 加密，則不會出現某些問題，例如兩個配置不當且使用非 *mesh* 模式的接入點之間出現單邊 WDS 鏈路。但是，使用 WPA 的非 *mesh* 模式仍有其他問題（例如配置不匹配時不斷嘗試重新連線），這些問題可透過使用 *-mesh* WDS 模式解決。

一般來說，建立受 WPA 保護的 WDS 鏈路的兩個接入點上的 WPA 屬性必須匹配。這些屬性是 **authentication-types**、**unicast-ciphers**、**group-ciphers**。對於非 *mesh* WDS 模式，這些屬性需要在兩個裝置上具有相同的值。在 *mesh* WDS 模式下，每個接入點必須支援另一個接入點作為用戶端。

理論上可以為 WDS 鏈路使用 RADIUS MAC 認證和其他 RADIUS 服務。但是，只有一個接入點會與 RADIUS 伺服器互動，另一個接入點將表現為用戶端。

RouterOS 中 *eap-tls* EAP 方法的實現特別適合 WDS 鏈路加密。**tls-mode**=*no-certificates* 不需要額外配置，並提供非常強的加密。

**WDS 和 WEP：**

分配給 WDS 鏈路的安全配置檔案中的 **mode**、**static-sta-private-key** 和 **static-sta-private-algo** 引數需要在建立 WEP 加密 WDS 鏈路的兩個接入點上具有相同的值。

#### 連線列表中的安全配置檔案與接入點匹配 {#security-profile-and-access-point-matching-in-the-connect-list}

用戶端使用 [connect-list](./wireless-interface.md#connect-list) 的 **security-profile** 屬性值來僅匹配支援必要安全的接入點。

- **mode**=*static-keys-required* 和 **mode**=*static-keys-optional* 僅匹配介面 **security-profile** 中具有相同 **mode** 的接入點。
- 如果 **mode**=*dynamic-keys*，則如果 **authentication-types**、**unicast-ciphers** 和 **group-ciphers** 都至少包含一個接入點通告的值，則連線列表條目匹配。

## 虛擬介面 {#virtual-interfaces}

### 虛擬 AP {#virtual-ap}

可以使用無線選單中的 *add* 命令建立虛擬接入點。您必須指定虛擬介面所屬的 *master-interface*。如果 "master-interface" 模式為 "station"，則虛擬 AP 僅在 "master-interface" 活動時工作。虛擬 AP 可以有自己的 SSID 和安全配置檔案。

虛擬 AP 介面僅在主介面處於 *ap-bridge*、*bridge*、*station* 或 wds-slave 模式時工作。它僅與 802.11 協定工作，但不支援 Nv2。

此功能可用於為不同型別的使用者分離訪問。您可以為使用者分配不同的頻寬級別和密碼，並指示使用者連線到特定的虛擬網路。對無線用戶端而言，它會顯示為不同的 SSID 或不同的裝置。例如，使用 QuickSet 配置訪客網路時，後臺會使用 VirtualAP 功能。

**要建立新的 virtual-ap：** `/interface> wireless add mode=ap-bridge master-interface=wlan1 ssid=guests security-profile=guests`（*此類安全配置檔案需要先建立*）

:::note
每個物理介面最多可建立 127 個虛擬介面。不建議建立超過 30 個，因為效能將開始下降。
:::

### 虛擬用戶端 {#virtual-clients}

也可以建立虛擬用戶端，並在同一物理介面上同時擁有 AP 和用戶端。這允許您僅使用一張硬體卡進行中繼設定。配置過程與上述完全相同，但使用 **station** 模式：

**要建立新的 virtual-client：** `/interface> wireless add mode=station master-interface=wlan1 ssid=where-to-connect security-profile=your-profile`（*此類安全配置檔案需要先建立*）

:::note
 虛擬介面將始終使用 Master 介面的無線頻率。如果 Master 介面啟用了 `auto` 頻率，它們將使用 Master 介面所選的無線頻率。
:::

## 嗅探器 {#sniffer}

**子選單：** `/interface/wireless/sniffer`

無線嗅探器允許捕獲包括 Radio 頭、802.11 頭和其他無線相關資訊的幀。

| 屬性 | 說明 |
| :-- | :-- |
| **channel-time** (; 預設值：**200ms**) | 每個通道的嗅探時長。僅在 **multiple-channels=yes** 時使用 |
| **file-limit** (*integer [10..4294967295]*; 預設值：**10**) | 用於儲存捕獲資料的分配檔案大小（位元組）。適用於指定了 **file-name** 的情況。 |
| **file-name** (*string*; 預設值： ) | 儲存捕獲資料的檔名。 |
| **memory-limit** (*integer [10..4294967295]*; 預設值：**10**) | 用於儲存捕獲資料的分配記憶體緩衝區，單位為千位元組。 |
| **multiple-channels** (*yes \| no*; 預設值：**no**) | 是嗅探多個通道還是單個通道。**No** 表示所有通道設定將從 **/interface/wireless** 獲取。**Yes** 表示所有通道設定將從 **/interface/wireless** 下的 **scan-list** 獲取。 |
| **only-headers** (*yes \| no*; 預設值：**no**) | 如果設定為 yes，則嗅探器將僅捕獲儲存在幀頭中的資訊。 |
| **receive-errors** (*yes \| no*; 預設值：**no**) | 是否處理根據 FCS 判斷為接收時帶錯誤的的封包。 |
| **streaming-enabled** (*yes \| no*; 預設值：**no**) | 是否將捕獲資料流式傳輸到指定的流伺服器 |
| **streaming-max-rate** (*integer [0..4294967295]*; 預設值：**0**) | 允許的每秒最大封包數。**0** 等於無限制 |
| **streaming-server** (*IPv4*; 預設值：**0.0.0.0**) | 流伺服器的 IP 地址。 |

:::note
當 `multiple-channels=yes` 時，使用 `/interface/wireless/info/scan-list` 命令來驗證在 `/interface/wireless/channels` 下定義的 `scan-list`。
:::

### 封包 {#packets}

**子選單：** `/interface/wireless/sniffer/packet`

子選單顯示捕獲的封包。

## 掃描 {#scan}

Scan 命令允許您檢視 scan-list 中定義的頻率範圍內的可用 AP。使用 scan 命令時，介面操作會被停用（掃描操作期間無線鏈路會斷開）。還支援後臺掃描，可在無線介面操作期間使用而不會斷開無線鏈路。後臺掃描僅在使用 802.11 無線協定時受支援。

scan 工具將繼續掃描 AP，直到使用者停止掃描過程。可以使用 scan 工具的 `rounds` 設定來對 scan-list 條目進行特定次數的掃描。這在透過指令碼執行 scan 工具時很有用。單輪 scan 命令示例：

```
/interface/wireless/scan wlan1 rounds=1
```

`save-file` 選項允許執行指令碼化/計劃掃描，並將結果儲存到檔案中以供將來分析。此外，此功能與 rounds 設定一起允許從遠端無線用戶端獲取掃描結果——執行該命令將啟動 scan 工具，斷開無線鏈路，掃描 scan-list 中的頻率，將結果儲存到檔案，退出掃描並重新連線無線鏈路。示例：

```
/interface/wireless/scan wlan1 rounds=1 save-file=scan1
```

要使用後臺無線掃描，應提供 `background=yes` 設定。示例：

```
/interface/wireless/scan wlan1 background=yes
```

後臺掃描功能在以下條件下工作：

- 無線介面應已啟用。
- 對於處於 AP 模式的無線介面——當它工作於 802.11 協定模式並且處於固定通道時（即通道選擇和初始雷達檢查已完成）。
- 對於處於 Station 模式的無線介面——當它連線到 802.11 協定 AP 時。

Scan 命令在虛擬無線介面上也受支援，但有以下限制：

- 當虛擬介面及其 master 固定在一個通道上時可行（master AP 正在執行，或 master station 已連線到 AP）。
- 掃描僅在 master 介面所在的通道上進行。
- `background=yes|no` 無關緊要——在虛擬介面上掃描不會斷開用戶端/AP，因此它始終是“後臺”掃描。

## Snooper {#snooper}

此工具監控周圍頻率使用情況，並顯示哪些裝置佔用每個頻率。它在控制檯和 WinBox 中均可用。Snooper 將使用 scan-list 中的頻率。

**子選單：** `/interface/wireless/snooper`

![](/img/4f1988b92537fbed.webp)

![](/img/fd8ec072bb88c200.webp)

### 設定 {#settings}

![](/img/e9bdf175bc8c36cd.webp)

## 頻譜掃描 {#spectral-scan}

- 請參閱單獨的文件 [頻譜掃描](./spectral-scan.md)。

## WDS {#wds}

**子選單：** `/interface/wireless/wds`

**屬性：**

| 屬性 | 說明 |
| :-- | :-- |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; 預設值：**enabled**) |  |
| **comment** (*string*; 預設值： ) |  |
| **disable-running-check** (*yes \| no*; 預設值：**no**) |  |
| **disabled** (*yes \| no*; 預設值：**yes**) |  |
| **l2mtu** (*integer [0..65536]*; 預設值： ) |  |
| **master-interface** (*string*; 預設值： ) |  |
| **mtu** (*integer [0..65536]*; 預設值：**1500**) |  |
| **name** (*string*; 預設值： ) |  |
| **wds-address** (*MAC*; 預設值：**00:00:00:00:00:00**) |  |

**只讀屬性：**

| 屬性 | 說明 |
| :-- | :-- |
| **dynamic** (*yes \| no*) |  |
| **mac-address** (*MAC*) |  |
| **running** (*yes \| no*) |  |

## WPS {#wps}

無線介面同時支援 WPS 伺服器和 WPS 用戶端。

### WPS 伺服器 {#wps-server}

WPS 伺服器允許支援 WPS 的無線用戶端連線到受預共享金鑰保護的 AP，而無需在用戶端配置中指定該金鑰。

可以透過更改無線介面的 WPS Mode 設定來啟用 WPS 伺服器。示例：

```
 /interface/wireless/set wlan1 wps-mode=push-button
```

Wps-mode 有 3 個選項

- disabled
- push-button - WPS 透過按下板上的物理按鈕啟用（少數板卡在機殼/標籤上標有此類按鈕）
- push-button-virtual-only - WPS 透過從 RouterOS 無線介面選單按下 "WPS Accept" 按鈕啟用

透過按下 WPS 物理/虛擬按鈕，AP 啟用 WPS 功能。如果 2 分鐘內未啟動 WPS 過程，WPS Accept 功能將停止。

在少數標有物理 WPS 按鈕的板卡上，WPS 伺服器預設啟用。例如 hap lite、hap、hap ac lite、hap ac、map lite。

WPS 伺服器僅在無線 AP 介面啟用了預共享金鑰認證（PSK）時活動。也可以為虛擬 AP 介面配置此模式。

### WPS 用戶端 {#wps-client}

WPS 用戶端功能允許無線用戶端獲取已啟用 WPS 伺服器的 AP 的預共享金鑰配置。WPS 用戶端可透過以下命令啟用：

```
 /interface/wireless/wps-client/wlan1
```

WPS 用戶端命令會在螢幕上輸出有關已啟用 WPS 的 AP 的所有資訊。示例：

```
[admin@MikroTik] /interface/wireless> wps-client wlan1
          status: disconnected, success
            ssid: MikroTik
     mac-address: E4:8D:8C:D6:E0:AC
      passphrase: presharedkey
  authentication: wpa2-psk
      encryption: aes-ccm
```

可以為 WPS-Client 命令指定其他設定：

- create-profile - 建立具有指定名稱的無線安全配置檔案，使用從 WPS AP 接收的安全詳細資訊進行配置，並指定無線介面使用新建立的安全配置檔案。
- ssid - 僅從具有指定 SSID 的 AP 獲取 WPS 資訊。
- mac-address - 僅從具有指定 mac-address 的 AP 獲取 WPS 資訊。

## 中繼器 {#repeater}

無線中繼器允許從 AP 接收訊號，並使用同一物理介面在本地重複訊號，以連線其他用戶端。這將允許為無線用戶端擴充套件無線服務。無線中繼器功能將配置無線介面以使用 station-bridge 或 station-pseudobridge 選項連線到 AP，建立虛擬 AP 介面，建立橋接介面，並將兩個介面（主介面和虛擬介面）都新增到橋埠。

如果您的 AP **支援按鍵啟用的 WPS** 模式，可以使用自動設定命令：

```
/interface/wireless/setup-repeater wlan1
```

setup-repeater 執行以下步驟：

- 搜尋已按下按鈕的 WPS AP。
- 從 AP 獲取 SSID、金鑰、通道。
- 重設主 master 介面配置（與 reset-configuration 相同）。
- 移除此 master 上新增的虛擬介面所新增的所有橋埠（以便之後沒有懸空無效的橋埠）。
- 移除此 master 上新增的所有虛擬介面。
- 建立名為 "`<interfacename>-<ssid>-repeater`" 的安全配置檔案，如果此類安全配置檔案已存在，則不建立新的，只更新設定。
- 配置 master 介面，介面模式選擇如下：如果 AP 支援橋接模式，使用 station-bridge；否則如果 AP 支援 WDS，使用 station-wds；否則使用 station-pseudobridge。
- 建立具有與 master 相同 SSID 和安全配置檔案的虛擬 AP 介面。
- 如果 master 介面不在某個橋中，則建立新的橋介面並將 master 介面新增到其中。
- 將虛擬 AP 介面新增到 master 介面所在的同一橋中。

如果您的 AP **不支援 WPS**，可以使用以下引數手動指定設定：

- **address** - 要為其設定中繼器的 AP 的 MAC 地址（可選）
- **ssid** - 要為其設定中繼器的 AP 的 SSID（可選）
- **passphrase** - 要用於 AP 的金鑰——如果指定了此項，命令將僅掃描 AP，並根據 beacon 中的資訊和此密碼短語建立安全配置檔案。如果未指定此項，命令將執行 WPS 以找出密碼短語。

## 漫遊 {#roaming}

### 站漫遊 {#station-roaming}

站漫遊功能僅適用於 802.11 無線協定，且僅適用於站模式。當 RouterOS 無線用戶端使用 802.11 無線協定連線到 AP 時，它將按特定時間間隔定期執行後臺掃描。當後臺掃描找到訊號更好的 AP 時，它將嘗試漫遊到該 AP。當無線訊號變差時，後臺掃描之間的時間間隔將變短；當無線用戶端訊號變好時，後臺掃描間隔將變長。

## VLAN 標記 {#vlan-tagging}

**子選單：** `/interface/wireless`

使用 VLAN 標記，可以在“本地轉發”AP（無線介面與乙太網橋接的 AP）的乙太網側分離虛擬 AP 流量。這對於在 AP 的乙太網側分離例如“管理”和“訪客”網路流量是必要的。

VLAN 分配給無線介面，因此來自無線的所有資料都會使用此標記進行標記，並且只有帶有此標記的資料才會透過無線傳送出去。這適用於所有無線協定，但在 Nv2 上不支援虛擬 AP。

您可以配置 RADIUS 認證伺服器，以便在使用者或使用者組向網路認證時為其分配特定 VLAN。要使用此選項，您需要使用 [RADIUS 屬性](../../authentication-authorization-accounting/radius.md)。

| 屬性 | 描述 |
| :-- | :-- |
| **vlan-mode** (*no-tag \| use-service-tag \| use-tag*; 預設值：**no-tag**) | 有三種 VLAN 模式可用：*no-tag* - AP 不使用 VLAN 標記*use-service-tag* - VLAN ID 使用 802.1ad 標記型別*use-tag* - VLAN ID 使用 802.1q 標記型別 |
| **vlan-id** (*integer [1..4095]*; 預設值：**1**) | VLAN 標識號 |

### VLAN 標記覆蓋 {#vlan-tag-override}

可以透過訪問列表和 RADIUS 屬性（對於常規無線和無線控制器均適用）基於每個用戶端覆蓋每介面 VLAN 標記。

這樣，即使在同一個介面上，也可以分離無線用戶端之間的流量，但必須謹慎使用——只會傳送“介面 VLAN”廣播/組播流量。如果其他（被覆蓋的）VLAN 也需要正常工作的廣播/組播，目前可以使用 multicast-helper（這會將每個組播封包改為單播，然後僅傳送給具有匹配 VLAN ID 的用戶端）。

## WinBox {#winbox}

[WinBox](../../management-tools/winbox.md) 是一個小型實用程式，允許使用快速簡單的 GUI 管理 MikroTik RouterOS。

:::note
 Current Tx Power 顯示特定資料速率下使用的發射功率。Atheros 802.11ac 晶片（例如 QCA98xx）不支援此功能。
:::

## Interworking Realms 設定 {#interworking-realms-setting}

有關 interworking 配置檔案的更多資訊，請參閱 [互通配置檔案](./interworking-profiles.md)。

**realms-raw** - 一個包含十六進位制值的字串列表。每個字串指定 "NAI Realm Tuple" 的內容，不包括 "NAI Realm Data Field Length" 欄位。

每個十六進位制編碼字串必須由以下欄位組成：

```
- NAI Realm Encoding (1 byte)
- NAI Realm Length (1 byte)
- NAI Realm (variable)
- EAP Method Count (1 byte)
- EAP Method Tuples (variable)
```

例如，值 "00045465737401020d00" 解碼為：

```
- NAI Realm Encoding: 0 (rfc4282)
- NAI Realm Length: 4
- NAI Realm: Test
- EAP Method Count: 1
- EAP Method Length: 2
- EAP Method Tuple: TLS, no EAP method parameters
```

設定 "realms-raw=00045465737401020d00" 產生的通告內容與設定 "realms=Test:eap-tls" 相同。

有關完整的 NAI Realm 編碼，請參閱 802.11-2016 第 9.4.5.10 節。

## 遷移說明 {#migration-notes}

以下術語和打包在較舊的 RouterOS 版本中發生了變化。此處僅作為參考，供遷移非常舊配置的人員使用——在當前 RouterOS 上，這些都不需要任何操作。

- **Superchannel / `frequency-mode`。** `superchannel` 頻率模式以前稱為 *Custom Frequency Upgrade*，需要特殊許可證金鑰。自 RouterOS v4.3 起，它已在所有安裝中無需金鑰即可使用。
- **無線驅動程式包。** RouterOS v6 將無線功能拆分到單獨的 `wireless-rep`、`wireless-cm2` 和 `wireless-fp` 包中。RouterOS v7 將這些合併到單個 `wireless` 包中，因此曾經需要這些包之一的功能——虛擬用戶端、後臺掃描、WPS 用戶端、RADIUS VLAN 分配以及 `scan-list` step 選項——現在都是標準 `wireless` 包的一部分。
