---
sidebar_key: "network-management/arp"
sidebar_position: 1
title: "ARP"
sidebar_label: "ARP"
description: "本頁介紹 MikroTik RouterOS 中的 ARP（Address Resolution Protocol）功能，說明 IP 地址如何對映到 MAC 地址。內容涵蓋 ARP 表屬性、只讀標誌、VRF 關聯以及 ARP 模式（disabled、enabled、proxy ARP），幷包含靜態條目和介面特定設定的配置示例。"
tags:
  - 'arp'
source: https://manual.mikrotik.com/docs/7.24/network-management/arp
captured_at: '2026-11-07T17:11:03.548Z'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/ip/arp`

儘管 IP 封包使用 IP 地址進行定址，但主機之間傳輸資料時必須使用硬體地址。地址解析協定用於將 OSI 第 3 層 IP 地址對映到 OSI 第 2 層 MAC 地址。路由器維護著一張當前使用的 ARP 條目表。通常該表是動態建立的，但為了增強網路安全性，可以透過新增靜態條目來部分或完全地靜態構建該表。

## 屬性 {#properties}

本節介紹 ARP 表的配置選項。

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP*；預設值：) | 要對映的 IP 地址 |
| **interface** (*string*；預設值：) | 分配該 IP 地址的介面名稱 |
| **mac-address** (*MAC*；預設值：**00:00:00:00:00:00**) | 要對映到的 MAC 地址 |
| **published** (*yes \| no*；預設值：**no**) | 針對單個 IP 地址的靜態 proxy-arp 條目。當收到針對特定 IP 地址的 ARP 查詢時，裝置將用自己的 MAC 地址進行應答。無需在介面本身上為所有要代理的 MAC 地址設定 proxy-arp。僅當裝置存在通往目的地的活動路由時，介面才會響應 ARP 請求 |

**只讀屬性：**

| 屬性 | 描述 |
| :-- | :-- |
| **complete** (*yes \| no*) | 當 ARP `status` 為 permanent、reachable、stale、probe 或 delay 時，ARP 條目中包含 complete 標誌 |
| **dhcp**(*yes \| no*) | ARP 條目是否由 DHCP server 新增 |
| **disabled**(*yes \| no*) | ARP 條目是否被停用 |
| **dynamic** (*yes \| no*) | 條目是否為動態建立 |
| **invalid** (*yes \| no*) | 條目是否無效 |
| **status**(*delay \| failed \| incomplete \| permanent \| probe \| reachable \| stale* ) | 顯示 ARP 條目狀態：<br/><ul><li><span className="ros-icon-success"><code>delay</code></span> - 鄰居條目驗證當前處於延遲狀態</li><li><span className="ros-icon-success"><code>failed</code></span> - ARP 解析失敗，系統無法獲取給定 IP 地址的 MAC 地址</li><li><span className="ros-icon-success"><code>incomplete</code></span> - 系統沒有該 IP 地址的 MAC 地址資訊，尚未解析</li><li><span className="ros-icon-success"><code>permanent</code></span> - ARP 條目被視為永久條目，即使它未處於活躍使用狀態，也不會從表中移除。此狀態為手動配置的 ARP 條目設定</li><li><span className="ros-icon-success"><code>probe</code></span> - 正在探測鄰居</li><li><span className="ros-icon-success"><code>reachable</code></span> - ARP 解析成功，且與該 IP 地址關聯的 MAC 地址已知，該條目在可達性超時到期前有效</li><li><span className="ros-icon-success"><code>stale</code></span> - 條目仍然有效，但已老化。這意味著系統最近未與關聯該 IP 地址的裝置通訊。</li></ul> |
| **VRF** (string) | 指示此 ARP 條目與哪個 VRF 關聯。 |

:::warning
ARP 條目的預設最大數量取決於已安裝的 RAM 容量。可透過命令 "`/ip/settings/set max-neighbor-entries=`x" 進行調整，更多詳情請參閱 [IPv4 設定](../cli-reference/ip/settings.md)。
:::

## ARP 模式 {#arp-modes}

可以在介面配置中設定多種 ARP 模式：

- `disabled` — 該介面不使用 ARP。
- `enabled` — 該介面使用 ARP。
- `local-proxy-arp` — 路由器在該介面上執行代理 ARP，並向同一介面傳送回覆。
- `proxy-arp` — 路由器在該介面上執行代理 ARP，並向其他介面傳送回覆。
- `reply-only` — 該介面僅回覆那些源自與 IP/ARP 表中靜態條目相匹配的 IP 地址/MAC 地址組合的請求。不會有動態條目被自動儲存到 IP/ARP 表中。因此，為使通訊成功，必須已存在有效的靜態條目。

### 已停用 {#disabled}

如果介面上的 ARP 功能被關閉，即使用 `arp=disabled`，路由器將不應答來自用戶端的 ARP 請求。因此，也應在用戶端上新增靜態 ARP 條目。例如，應使用 arp 命令將路由器的 IP 和 MAC 地址新增到 Windows 工作站上：

```text
C:\> arp -s 10.5.8.254  00-aa-00-62-c6-09
```

### 已啟用 {#enabled}

該模式在所有介面上預設啟用。ARP 會被自動發現，新的動態條目會被新增到 ARP 表中。

### 代理 ARP {#proxy-arp}

配置了正確代理 ARP 功能的路由器可在不同網路之間充當透明的 ARP 代理。

這種行為可能很有用，例如，當你希望為撥入（ppp、pptp、pppoe）用戶端分配的 IP 地址與所連線 LAN 上使用的地址空間相同時。

可以透過命令 `arp=proxy-arp` 在每個介面上單獨啟用代理 ARP：

#### 設定代理 ARP {#setup-proxy-arp}

```ros
 [admin@MikroTik] /interface/ethernet> set 1 arp=proxy-arp

 [admin@MikroTik] /interface/ethernet> print

 Flags: X - disabled, R - running
   #    NAME                 MTU   MAC-ADDRESS         ARP
   0  R ether1              1500  00:30:4F:0B:7B:C1 enabled
   1  R ether2              1500  00:30:4F:06:62:12 proxy-arp
```

### 僅回覆 {#reply-only}

如果介面上的 ARP 屬性設定為 `reply-only`，那麼路由器只回復 ARP 請求。鄰居 MAC 地址將僅使用 `/ip/arp` 選單中靜態配置的條目來解析，但無需像 ARP 被停用時那樣將路由器的 MAC 地址新增到其他主機的 ARP 表中。

### 本地代理 ARP {#local-proxy-arp}

如果介面上的 ARP 屬性設定為 `local-proxy-arp`，那麼路由器僅針對該介面執行代理 ARP，即對於進入和離開同一介面的流量。在普通 LAN 中，預設行為是兩個網路主機直接相互通訊，而不經過路由器。

啟用 `local-proxy-arp` 後，路由器將以自己的介面 MAC 地址（而非其他主機的 MAC 地址）應答所有用戶端主機。

例如，如果主機 A（192.168.88.2/24）查詢主機 B（192.168.88.3/24）的 MAC 地址，路由器將用自己的 MAC 地址進行應答。換言之，如果啟用了 `local-proxy-arp`，路由器將承擔在主機 A 192.168.88.2 與主機 B 192.168.88.3 之間轉發流量的責任。主機 A 和 B 上的所有 ARP 快取條目都將引用路由器的 MAC 地址。在這種情況下，路由器正在為整個子網 192.168.88.0/24 執行 `local-proxy-arp`。

RouterOS `local-proxy-arp` 的一個示例可以是帶有 DHCP 伺服器和隔離橋接埠的橋接設定，其中同一子網內的主機只能透過橋接 IP 在第三層相互通訊。

```ros
/interface/bridge
add arp=local-proxy-arp name=bridge1
/interface/bridge/port
add bridge=bridge1 horizon=1 interface=ether2
add bridge=bridge1 horizon=1 interface=ether3
add bridge=bridge1 horizon=1 interface=ether4
```

## 免費 ARP {#gratuitous-arp}

可以在 RouterOS 中建立 Gratuitous ARP 請求。為此，你必須使用 Traffic-Generator 工具。下面是一個示例，說明如何生成 Gratuitous ARP 請求以更新遠端裝置上的 ARP 表：

```ros
/tool/traffic-generator/inject interface=ether2 \
data="ffffffffffff4c5e0c14ef78080600010800060400014c5e0c14ef780a057a01ffffffffffff0a057a01000000000000000000000000000000000000"
```

你必須將 MAC 地址（4c5e0c14ef78）和 IP 地址（0a057a01）改為你路由器的地址。IP 地址和 MAC 地址必須來自請求更新 ARP 表的裝置。你還需要指定透過哪個介面（ether2）傳送 Gratuitous ARP 請求。請確保接收裝置支援 Gratuitous ARP 請求。
