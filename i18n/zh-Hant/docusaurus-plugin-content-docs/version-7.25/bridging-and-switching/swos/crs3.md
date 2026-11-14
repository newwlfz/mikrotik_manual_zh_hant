---
sidebar_key: "bridging-and-switching/swos/crs3"
sidebar_position: 1
title: "CRS3xx 和 CSS3xx 系列手冊"
sidebar_label: "CRS3xx 和 CSS3xx 系列手冊"
source: https://manual.mikrotik.com/docs/7.25/bridging-and-switching/swos/crs3
captured_at: '2026-11-04T11:15:25+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

SwOS 是專為管理 MikroTik 交換器產品而設計的作業系統。它提供基本的管理型交換器功能，以及埠到埠轉發、廣播風暴控制、透過 ACL 規則進行 MAC/IP/埠過濾、VLAN 配置、流量映象和頻寬限制等高階功能。

SwOS 僅透過 IPv4 上的 Web 瀏覽器（HTTP）進行管理。不支援控制檯訪問、SSH、API 或其他管理介面。

---

## 連線到交換器 {#connecting-to-the-switch}

開啟 Web 瀏覽器並輸入預設管理 IP 地址。

![Swos login css326](/img/6264ffe6828480e0.webp)

* **預設 IP 地址**：`192.168.88.1`
* **預設使用者名稱**：`admin`
* **預設密碼**：*（空）*

---

## 系統標籤頁 {#system-tab}

系統標籤頁管理常規配置引數、裝置發現選項和管理安全。

![Swos system css326](/img/704f07a7a77e557f.webp)

### 系統管理設定 {#system-management-settings}

| 屬性 | 描述 |
| :--- | :--- |
| **地址獲取** | 定義透過靜態設定、帶回退的 DHCP 或僅 DHCP 進行 IP 分配。 |
| **靜態 IP 地址** | 指定用於管理訪問的靜態 IPv4 地址。 |
| **標識** | 設定交換器標識的可自定義名稱。 |
| **允許來源** | 將管理 Web 訪問限制為指定的 IP 範圍或子網。 |
| **允許來源埠** | 將 Web 訪問限制到指定的物理交換器介面。 |
| **允許來源 VLAN** | 將訪問限制到特定的傳入 VLAN ID 配置檔案。 |

![SwOS Management](/img/ca29c618018d3a59.webp)

### DHCP 與 PPPoE 監聽 {#dhcp--pppoe-snooping}

SwOS 具有內建安全機制，可在指定的不受信任介面上阻止未經授權或惡意的 DHCP 伺服器以及 PPPoE 發現序列。

![CSS326 DHCP Snooping](/img/0f3d52a9da17fa79.webp)

### 配置安全與維護 {#configuration-security-and-maintenance}

下半部分處理備份和管理密碼。

![Swos system3 css326](/img/3ba4a76afdcc03bc.webp)

* **更改密碼**：更新裝置訪問金鑰。
* **備份配置**：將當前設定儲存到本地檔案。
* **恢復配置**：上傳並應用現有配置狀態。

---

## 鏈路標籤頁 {#link-tab}

鏈路標籤頁配置物理鏈路引數，並監控每個介面的活動連線屬性。

![Swos link css326](/img/8dec2ad5f0c9b5e2.webp)

* **鏈路配置檔案**：管理介面狀態，切換速度/雙工自動協商，並控制流控暫停幀。

---

## PoE 標籤頁 {#poe-tab}

*（適用於支援乙太網供電分配功能的裝置）*

![SwOS PoE](/img/ca06196fd522c5cd.webp)

* 支援配置供電設定（`auto`、`on`、`off`），並在功率受限事件期間建立埠優先順序。

---

## SFP 標籤頁 {#sfp-tab}

為已連線的 SFP/SFP+ 光收發器提供視覺化診斷。

![Swos sfp1 css326](/img/d2e58a862ecccc20.webp)

* 監控工作溫度、雷射器供電電壓、TX/RX 功率電平和硬體序列號字串等內部診斷資訊。

---

## 轉發與埠隔離 {#forwarding-and-port-isolation}

管理整個交換架構中的第 2 層封包轉發表。

![Swos forw css326](/img/cfc3bfc9dda03800.webp)
![Swos ivl system](/img/b0001fc2ceb3b1a6.webp)

### 埠隔離與隔離組 {#port-isolation-and-isolated-groups}

埠隔離在內部拆分廣播域，在不增加子網層級的情況下控制用戶端通訊。

![SwOS Isolated Groups](/img/284614f24611b0f4.webp)
![SwO isolation example3](/img/de28135343d9795b.webp)

---

## LAG（鏈路聚合） {#lag-link-aggregation}

使用動態 LACP 鏈路或靜態陣列將物理介面捆綁為單個高吞吐量通道。

![Swos lag css326](/img/42eb242aaffa0ae3.webp)

---

## RSTP（快速生成樹協定） {#rstp-rapid-spanning-tree-protocol}

提供環路避免架構和結構冗餘引數。

![Swos rstp css326](/img/6e7df850ef26634b.webp)

* 支援使用經典短路徑或現代長路徑評估結構來配置自定義橋路徑開銷。

---

## VLAN 與 VLANs 矩陣配置 {#vlan--vlans-matrix-configuration}

VLAN 路由規則將入口封包分類行為與出口格式表分離。

### VLAN 標籤頁（入口控制） {#vlan-tab-ingress-control}

處理傳入流量流的埠行為。

![Swos vlan css326](/img/871181dce551f5b8.webp)

* **VLAN 模式**：配置 `disabled`、`optional`、`enabled` 和 `strict` 模式下的入口約束。

![Swos strict vlans](/img/d34e6c2d13d78d19.webp)

* **預設 VLAN ID**：設定分配給傳入未標記流量的埠 VLAN ID（PVID）。

![Default vlan id](/img/1d9f62b52b3efa1f.webp)

### VLANs 標籤頁（出口對映） {#vlans-tab-egress-mapping}

定義目標 trunk 埠上的廣播成員關係和處理方式。

![Swos vlans css326](/img/9d38b9ee9d82a8c1.webp)
![Swos vlans menu](/img/e5c63db80488b834.webp)

#### 傳統模式模板 {#traditional-mode-templates}

* **接入介面**：將標準未標記端點與特定目標 VLAN 標記配對。

  ![Access ports](/img/dcbdce357964f958.webp)

* **Trunk 和 Hybrid 選項**：在主要核心上行鏈路上，將多個帶標籤流量與可選的未標記本徵路由路徑混合。

  ![Hybrid ports](/img/90b987271e134d95.webp)
  ![Swos hybrid](/img/2fb81eda61c231cd.webp)
  ![Swos hybrid vlan](/img/330b019789c2b24b.webp)

---

## 私有 VLAN {#private-vlans}

在共享基礎設施空間中強制執行安全的埠通訊結構配置檔案。

![SwOS Private VLAN](/img/606fbb63c2620b62.webp)

---

## 主機標籤頁 {#hosts-tab}

顯示透過傳入源地址發現的活躍硬體轉發表（FDB）動態條目。

![Swos shost css326](/img/24da5f09ba887bf8.webp)

---

## IGMP 監聽 {#igmp-snooping}

過濾組播分發，跟蹤活躍組訂閱以阻止組播泛洪。

![IGMP snooping](/img/a5464dca06492640.webp)
![CSSxx IGMP](/img/8404b127eb3f6c84.webp)
![IGMP vlantab](/img/2c8b3d4fcf937b4d.webp)

---

## SNMP 標籤頁 {#snmp-tab}

支援透過標準 SNMP 結構進行監控。

![Swos snmp2 1](/img/f3b87569bbcad587.webp)

---

## ACL 標籤頁（訪問控制列表） {#acl-tab-access-control-lists}

執行硬體解除安裝的過濾規則，匹配第 2/3/4 層幀頭中的模式以丟棄或重定向封包。

![CRS326 ACL table](/img/7e4fb4e7daa01ec1.webp)

---

## 診斷：統計、錯誤和直方圖 {#diagnostics-stats-errors-and-histograms}

跟蹤介面計數器、丟棄幀、錯誤模式以及詳細的結構化鏈路歷史診斷資訊。

![Swos stat1 css326](/img/bc002e2ae29c54ca.webp)
![Swos stat2 css326](/img/a1256a0deac7e870.webp)
![Swos stat3 css326](/img/4dc5d6afd153aab3.webp)

---

## 健康標籤頁 {#health-tab}

監控硬體執行環境，跟蹤系統核心溫度和工作輸入電壓。

![SwOS CRS328 health](/img/c32f28c61507fb8f.webp)

---

## 雙啟動操作 {#dual-boot-operation}

許多 CRS 硬體裝置支援雙啟動設計，允許在執行 RouterOS 或 SwOS 之間切換。

![Router board settings](/img/206e2364a9ea20ec.webp)
![Router board settings webfig](/img/e5f83f41c903b22e.webp)
![Dual boot option](/img/59c51ae05cc7ea21.webp)

使用 RouterOS CLI 介面將作業系統切換為 SwOS 時，使用以下系統命令結構：

```bash
/system routerboard settings set boot-os=swos
```

## 重設與重新安裝 {#reset-and-reinstall}

可以使用系統選單中的 "Reset Configuration" 按鈕重設 SwOS 配置。如果 SwOS Web 管理不可用，仍可使用其他選項重設配置。

CSS326-24G-2S+ 和 CSS318-16G-2S+IN 裝置具有內建備份 SwOS 韌體，可在標準韌體損壞或升級失敗時載入：

* 在 CSS326-24G-2S+ 和 CSS318-16G-2S+IN 啟動時按住 Reset 按鈕幾秒鐘，會重設配置並載入備份韌體。
* 載入備份韌體後，可以使用 Web 瀏覽器連線到 192.168.88.1（或 DHCP 伺服器租用的地址）並安裝新的 SwOS 韌體。

雙啟動裝置可以使用重設按鈕啟動 RouterOS。按住重設按鈕為裝置通電，並等待使用者 LED 開始閃爍（約 5 秒）。這會重設 RouterOS 配置，裝置現在將啟動進入 RouterOS。裝置可透過 RouterOS 訪問後，即可升級和重設 SwOS 配置。請參閱文章 - 使用 RouterOS 配置 SwOS。

帶有序列控制檯的 CRS3xx 裝置具有其他選項。

要在 RouterOS 和 SwOS 之間切換，請按照以下步驟操作：

1. 使用序列控制檯連線到裝置
2. 進入 RouterBOOT 設定
3. 選擇 "j - boot os"
4. 選擇 RouterOS 或 SwOS

可以在標準韌體損壞或升級失敗時載入 SwOS 備份韌體：

1. 使用序列控制檯連線到裝置
2. 啟動 SwOS
3. 選擇 "p - boot primary SwOS"
4. 載入備份韌體後，可以使用 Web 瀏覽器連線到 192.168.88.1（或 DHCP 伺服器租用的地址）並安裝新的 SwOS 韌體。

要重設 SwOS 配置：

1. 使用序列控制檯連線到裝置
2. 啟動 SwOS
3. 選擇 "r - reset configuration"

![Swos reset](/img/88b172351cb761c2.webp)
