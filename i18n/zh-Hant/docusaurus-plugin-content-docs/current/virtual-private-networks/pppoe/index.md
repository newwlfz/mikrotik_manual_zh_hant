---
sidebar_key: "virtual-private-networks/pppoe"
title: "PPPoE"
sidebar_label: "PPPoE"
description: "PPPoE 支援透過 PPP 和 MLPPP 跨乙太網鏈路進行 IPv6 字首委派，同時支援用戶端到伺服器和伺服器到用戶端兩種配置。它分發現階段和會話階段執行，使用 LCP/CHAP 身份驗證，並透過 IPCP 分配 IP 地址。MTU 相關考量可確保正確封裝，而身份驗證方法和按需撥號等用戶端屬性則增強了靈活性。"
tags:
  - 'pppoe'
  - 'discovery-phase'
  - 'mtu'
source: https://manual.mikrotik.com/docs/virtual-private-networks/pppoe
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 PPPoE 示例。可使用這些示例透過 PPP 配置 IPv6 字首委派，以及透過一條或多條鏈路配置 MLPPP。

乙太網上的點對點協定（PPPoE）是一種將 PPP 封包封裝到乙太網幀中的方法。PPPoE 是標準點對點協定（PPP）的擴充套件，也是 PPPoA 的後繼者。PPPoE 標準定義在 [RFC 2516](https://tools.ietf.org/html/rfc2516) 中。PPPoE 用戶端和伺服器可在路由器的任何二層乙太網級介面上工作——例如 Wireless、Ethernet、EoIP 等。PPPoE 用於根據使用者名稱認證（以及在需要時根據工作站認證）向用戶端分配 IP 地址，而不是使用僅工作站認證（其中使用靜態 IP 地址或 DHCP）。出於安全原因，不要在 PPPoE 所在的同一介面上使用靜態 IP 地址或 DHCP。

## 簡介 {#introduction}

PPPoE 能夠透過簡單的橋接接入裝置將一組主機連線到遠端接入集中器。

支援的連線：

- MikroTik RouterOS PPPoE 用戶端連線到任意 PPPoE 伺服器。
- MikroTik RouterOS 伺服器（接入集中器）連線到多個 PPPoE 用戶端（用戶端幾乎適用於所有作業系統和大多數路由器）。

## PPPoE 工作過程 {#pppoe-operation}

PPPoE 有兩個不同的階段：

1. 發現階段。
2. 會話階段。

### 發現階段 {#discovery-phase}

發現階段有四步。完成時，雙方都知道 PPPoE *SESSION\_ID* 和對端的乙太網地址，這兩者共同唯一標識 PPPoE 會話：

1. **PPPoE 主動發現初始化（PADI）——** PPPoE 用戶端向廣播地址傳送 *PADI* 封包。如果已在 PPPoE 用戶端的撥號網路屬性中輸入服務名，此封包也可以填充 "service-name" 欄位。如果未輸入服務名，則不填充此欄位。
2. **PPPoE 主動發現提供（PADO）——** 如果訪問集中器能夠服務於 *PADI* 封包中列出的 "service-name" 欄位，則 PPPoE 伺服器（即訪問集中器）應使用 *PADO* 響應 *PADI*。如果未列出 "service-name" 欄位，訪問集中器會響應一個 *PADO* 封包，其中 "service-name" 欄位填充該訪問集中器可提供的服務名。*PADO* 封包傳送到 PPPoE 用戶端的單播地址。
3. **PPPoE 主動發現請求（PADR）——** 收到 *PADO* 封包後，PPPoE 用戶端使用 *PADR* 封包響應。此封包傳送到訪問集中器的單播地址。用戶端可能收到多個 *PADO* 封包，但用戶端會響應其收到的第一個有效 *PADO*。如果初始 *PADI* 封包的 "service-name" 欄位為空，則用戶端會用 *PADO* 封包中返回的第一個服務名填充 *PADR* 封包的 "service-name" 欄位。
4. **PPPoE 主動發現會話確認（PADS）——** 收到 *PADR* 後，訪問集中器為點對點協定（PPP）會話生成唯一的會話標識（ID），並在 *PADS* 封包中將此 ID 返回給 PPPoE 用戶端。此封包傳送到用戶端的單播地址。

### PPPoE 會話終止 {#pppoe-session-termination}

- **PPPoE 主動發現終止（PADT）——** 可在會話建立後的任何時間傳送，以指示 PPPoE 會話已終止。伺服器或用戶端均可傳送。

### 會話階段 {#session-phase}

發現階段完成後，雙方都知道 *PPPoE Session ID* 和對端的 *Ethernet（MAC）地址*，這兩者共同定義 PPPoE 會話。PPP 幀封裝在 PPPoE 會話幀中，這些幀的乙太網幀型別為 **0x8864**。
當伺服器傳送確認且用戶端收到後，PPP 會話按以下階段啟動：

1. **LCP 協商**階段。
2. **認證（CHAP/PAP）**階段。
3. **IPCP 協商**階段——在此階段為用戶端分配 IP 地址。

:::warning
如果任一過程失敗，將重新開始 LCP 協商建立階段。
:::

PPPoE 伺服器向用戶端傳送 *Echo-Request* 封包以確定會話狀態。否則，如果用戶端在不傳送 *Terminate-Request* 封包的情況下終止會話，伺服器無法確定會話已終止。

## MTU {#mtu}

通常，可在不分片的情況下傳輸的最大乙太網幀為 1500 位元組。PPPoE 增加 6 位元組開銷，PPP 欄位再增加 2 位元組，留給 IP 封包的為 1492 位元組。因此，PPPoE 的最大 MRU 和 MTU 值不得大於 1492。

TCP 棧會盡量避免分片，因此使用 MSS（最大段大小）。預設情況下，MSS 選擇為出介面的 MTU 減去 TCP 和 IP 報頭的通常大小（40 位元組），對於乙太網介面，結果為 1460 位元組。MTU 較低的中間鏈路可能導致分片。在這種情況下，TCP 棧會執行路徑 MTU 發現。無法在不分片的情況下轉發封包的路由器應丟棄該封包，並向源主機發送 *ICMP-Fragmentation-Required*。當主機收到此類 ICMP 封包時，會嘗試降低 MTU。這在理想情況下應該可行；然而，在現實世界中，許多路由器不生成需要分片的封包，並且許多防火牆會丟棄所有 ICMP 封包。

解決此問題的方法是在 MSS 過大時[調整 MSS](../../firewall-and-quality-of-service/firewall/mangle.md#change-mss)。

## MRRU {#mrru}

指定 MRRU 意味著在單條鏈路上啟用 MP（多鏈路 PPP）。此協定用於將大封包拆分為較小的封包。MRRU 硬編碼為 1614。此設定有助於克服 PathMTU 發現失敗。MP 設定應在兩個對等方上啟用。  
在 Windows 上，可以在“網路”標籤頁的“設定”按鈕中啟用“為單鏈路連線協商多鏈路”。

## 訪問集中器 {#access-concentrator}

PPPoE 伺服器（訪問集中器）支援每個介面有多個伺服器——使用不同的服務名。用戶端使用訪問集中器名稱和 PPPoE 服務名來標識要註冊的訪問集中器。訪問集中器名稱與命令提示符前顯示的路由器身份相同。身份在 *`/system/identity`* 子選單中設定。

訪問集中器在 [`/interface/pppoe-server/server`](../../cli-reference/interface/pppoe-server/server.md) 選單中配置。

:::tip
不要為接收 PPPoE 請求的介面分配 IP 地址。
:::

:::warning
預設的 `keepalive-timeout` 值 10s 在大多數情況下沒問題。如果將其設定為 0，路由器不會斷開用戶端，直到用戶端顯式登出或路由器重啟。要解決此問題，可以使用 `one-session-per-host` 屬性。
:::

## 快速示例 {#quick-example}

![](/img/a34ca577e7a80a70.jpg)

### PPPoE 用戶端 {#pppoe-client}

要將 MikroTik RouterOS 配置為 PPPoE 用戶端，請使用以下引數新增 PPPoE 用戶端：

```ros
[admin@MikroTik] > interface pppoe-client add interface=ether2 password=StrongPass service-name=pppoeservice name=PPPoE-Out disabled=no user=MT-User
[admin@MikroTik] > interface pppoe-client print
Flags: X - disabled, I - invalid, R - running 
 0  R name="PPPoE-Out" max-mtu=auto max-mru=auto mrru=disabled interface=ether2 user="MT-User" 
      password="StrongPass" profile=default keepalive-timeout=10 service-name="pppoeservice" ac-name="" 
      add-default-route=no dial-on-demand=no use-peer-dns=no allow=pap,chap,mschap1,mschap2
```

### PPPoE 伺服器 {#pppoe-server}

要將 MikroTik RouterOS 配置為接入集中器（PPPoE 伺服器）：

- 為用戶端新增 IP 地址池，範圍為 10.0.0.2-10.0.0.5。
- 新增 PPP 配置檔案。
- 新增 PPP secret（使用者名稱/密碼）。
- 新增 PPPoE 伺服器本身。

:::warning
對於 Windows，某些連線說明可能使用這樣的形式：指定“電話號碼”，例如 "MikroTik\_AC\mt1"，以表示 "MikroTik\_AC" 是訪問集中器名稱，而 "mt1" 是服務名。
:::

```ros
[admin@MikroTik] > /ip/pool
add name=pppoe-pool ranges=10.0.0.2-10.0.0.5
[admin@MikroTik] > /ppp/profile
add local-address=10.0.0.1 name=for-pppoe remote-address=pppoe-pool
[admin@MikroTik] > /ppp/secret
add name=MT-User password=StrongPass profile=for-pppoe service=pppoe
[admin@MikroTik] > /interface/pppoe-server/server
add default-profile=for-pppoe disabled=no interface=ether3 service-name=pppoeservice
```

## PPPoE 跨 VLAN 範圍 {#pppoe-over-vlan-range}

避免在介面上配置帶有 `pppoe-over-vlan-range` 的伺服器，同時還建立使用落入該範圍內 VLAN ID 的 VLAN 介面。  
例如：
```
/interface/vlan
add interface=ether2 name=vlan15 vlan-id=15
/interface/pppoe-server/server
add disabled=no interface=ether2 pppoe-over-vlan-range=10-20
```
如果你需要這種設定，請從 `pppoe-over-vlan-range` 中移除重疊的 VLAN ID，並直接在 VLAN 介面上建立單獨的 PPPoE 伺服器例項，如下所示：
```
/interface/vlan
add interface=ether2 name=vlan15 vlan-id=15
/interface/pppoe-server/server
add disabled=no interface=ether2 pppoe-over-vlan-range=10-14,16-20
add disabled=no interface=vlan15
```

## 說明 {#notes}

不要在一臺裝置上使用大量 PPPoE 用戶端。
