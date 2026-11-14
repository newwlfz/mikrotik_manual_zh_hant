---
sidebar_key: "cli-reference/interface/ethernet/switch/l3hw-settings/advanced/index"
sidebar_position: 1
title: "advanced"
sidebar_label: 'advanced'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/l3hw-settings/advanced
captured_at: '2026-11-01T21:22:35+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/l3hw-settings/advanced {#interfaceethernetswitchl3hw-settingsadvanced}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 設定目錄

此選單允許針對特定使用場景調整 l3hw 設定。

除非獲得 MikroTik 支援人員或 MikroTik 認證路由工程師的指示，否則不建議更改高階 L3HW 設定。應用不正確的設定可能會破壞 L3HW 執行。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="route-queue-limit-high" typ="num" syscap="!prestera-cpss">當 [`route-queue-size`](../monitor.md#route-queue-size) 超過此值時，交換器驅動會停止路由索引。降低此值可加快路由處理，但會增加路由在 RouterOS 中出現與其在硬體記憶體中出現之間的延遲。設定 **0** 會在處理佇列中有任何路由時停用路由索引——CPU 使用效率最高，但硬體解除安裝前的延遲最長。僅當存在靜態路由時有用。當路由表頻繁變化時，不建議與路由協定（如 BGP 或 OSPF）一起使用。</ArgTableRow>
<ArgTableRow arg="route-queue-limit-low" typ="num" syscap="!prestera-cpss">當 [`route-queue-size`](../monitor.md#route-queue-size) 降至該值時，重新啟用路由索引。不得超過上限。設定 **0** 會告訴交換器驅動在下一次 hw-offloading 嘗試之前處理所有待處理路由。雖然這是期望的行為，但在持續的 BGP 路由更新下，它可能會完全阻塞 hw-offloading。</ArgTableRow>
<ArgTableRow arg="shwp-reset-counter" typ="num">
在路由表發生此數量的更改後，重設最短硬體字首（SHWP），並嘗試進行完整路由表解除安裝。  
在部分解除安裝時，當整個路由表無法放入硬體記憶體，且較短字首被重定向到 CPU 時，理論上無需嘗試解除安裝比 SHWP 更短的路由字首，因為這些字首無論如何都會被重定向到 CPU。但是，路由表的重大變化可能會導致不同的索引布局，從而改變可被 hw-offloaded 的路由數量。這就是為什麼建議偶爾執行完整的表重新索引。
降低此值可能會允許更多路由被 hw-offloaded，但會增加 CPU 使用率，反之亦然。設定 `shwp-reset-counter=0` 會在每次路由表更改後始終執行完整重新索引。
此設定僅在部分解除安裝（Partial Offloading）期間使用，並且當 [`ipv4-shortest-hw-prefix`](./monitor.md#ipv4-shortest-hw-prefix)=0（以及 IPv6 的相應情況）時不起作用。
</ArgTableRow>
<ArgTableRow arg="partial-offload-chunk" typ="num" syscap="prestera-bc2">
在部分解除安裝（Partial Offloading）中增量新增的最小路由數。  
取決於交換器晶片型號，路由要麼按原樣解除安裝（RouterOS 中的每個路由條目對應硬體記憶體中的一個條目），要麼進行索引，寫入硬體記憶體的是索引條目。此設定僅在部分解除安裝期間用於後者。
取決於索引碎片化情況，單條 IPv4 路由新增可能佔用 -3 到 +6 個 LPM HW 記憶體塊（由於索引碎片整理，某些路由新增可能會降低所需的 HW 記憶體量）。因此，無法預測可能適合硬體記憶體的確切路由數量。交換器驅動使用二分拆分演算法來查詢適合硬體的最大路由數量。  
假設有 128k 條路由，它們都無法放入硬體記憶體。演算法會將數量減半，並嘗試解除安裝 64k 條路由。假設解除安裝成功。在下一次迭代中，演算法選擇 96k，假設失敗；然後 80k——再次失敗，72k——成功，76k，等等，直到成功與失敗數量之間的差值低於 partial-offload-chunk 值。
降低 partial-offload-chunk 值會增加可被 hw-offloaded 的路由數量，但也會提高 CPU 使用率，反之亦然。
</ArgTableRow>
<ArgTableRow arg="route-index-delay-min" typ="time" syscap="!prestera-cpss">
路由處理與其解除安裝之間的最小延遲。該延遲允許一起處理更多路由並一次性解除安裝它們，從而節省 CPU 使用率。  
它還透過減少每條路由的處理工作來加快整個路由表的解除安裝。另一方面，它會減慢單個路由的解除安裝。  
如果在延遲期間收到額外路由，則延遲會重設為 `route-index-delay-min` 值。在延遲期間新增越來越多的路由會不斷重設計時器，直到達到 `route-index-delay-max`。
</ArgTableRow>
<ArgTableRow arg="route-index-delay-max" typ="time">路由處理與其解除安裝之間的最大延遲。當達到最大延遲時，即使還有更多路由待處理，已處理的路由也會被解除安裝。但是，`route-queue-limit-high` 的優先順序高於此設定，這意味著當達到特定佇列大小時，索引/解除安裝仍會暫停。</ArgTableRow>
<ArgTableRow arg="neigh-keepalive-interval" typ="time" syscap="!prestera-cpss">鄰居（主機）保活間隔。當主機被 hw-offloaded 後，來自/發往它的所有流量都由交換器晶片路由，RouterOS 可能會認為該鄰居不活動並將其刪除。為防止這種情況，交換器驅動必須透過向 RouterOS 傳送週期性重新整理來保持已解除安裝鄰居的存活。</ArgTableRow>
<ArgTableRow arg="neigh-discovery-interval" typ="time" syscap="!prestera-cpss">
傳送 ARP (IPv4) 或 Neighbor Discovery (IPv6) 請求以檢查已解除安裝主機是否仍處於活動狀態的間隔。  
遺憾的是，交換晶片不提供每個鄰居的統計資訊。因此，檢查已解除安裝主機是否仍處於活動狀態的唯一方法是向所連線的網路偶爾傳送 ARP (IPv4) / Neighbor Discovery (IPv6) 請求。  
Neighbor discovery 會在鄰居 keepalive 工作中觸發。因此，發現時間會向上取整到下一個 keepalive 會話。請為 `neigh-discovery-interval` 選擇一個不能被 `neigh-keepalive-interval` 整除的值，以便在不同會話中傳送 ARP/ND 請求，從而防止廣播突發。
</ArgTableRow>
<ArgTableRow arg="neigh-discovery-burst-limit" typ="num" syscap="!prestera-cpss">一次可以傳送的 ARP/ND 請求的最大數量。</ArgTableRow>
<ArgTableRow arg="neigh-discovery-burst-delay" typ="time" syscap="!prestera-cpss">如果請求數量超過 `neigh-discovery-burst-limit`，則 ARP/ND 後續突發之間的延遲。</ArgTableRow>
<ArgTableRow arg="neigh-dump-retries" typ="num" syscap="!prestera-cpss">在失敗情況下解除安裝鄰居表的最大重試次數。</ArgTableRow>
</ArgTable>
