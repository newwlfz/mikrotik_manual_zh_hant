---
title: "CRS3xx 與 CSS3xx 系列手冊"
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/swos/crs3
captured_at: '2026-11-28T10:19:39.818Z'
pagination_prev: "bridging-and-switching/swos"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

## 摘要 {#summary}

SwOS 是專為管理 MikroTik 交換器產品所設計的作業系統。它提供基本的網管交換器功能，以及連接埠對連接埠轉送、廣播風暴控制、透過 ACL 規則進行 MAC/IP/連接埠過濾、VLAN 設定、流量鏡像與頻寬限制等進階功能。

SwOS 僅能透過 IPv4 上的網頁瀏覽器（HTTP）管理，不支援主控台存取、SSH、API 或其他管理介面。

---

## 連線至交換器 {#connecting-to-the-switch}

開啟網頁瀏覽器，並輸入預設管理 IP 位址。

![Swos login css326](/img/6264ffe6828480e0.webp)

* **預設 IP 位址**: `192.168.88.1`
* **預設使用者名稱**: `admin`
* **預設密碼**: *(空白)*

---

## System 標籤頁 {#system-tab}

System 標籤頁可管理一般設定參數、設備探索選項與管理安全性。

![Swos system css326](/img/704f07a7a77e557f.webp)

### 系統管理設定 {#system-management-settings}

| Property | Description |
| :--- | :--- |
| **Address Acquisition** | 定義透過靜態設定、DHCP 搭配備援，或僅使用 DHCP 指派 IP。 |
| **Static IP Address** | 指定用於管理存取的靜態 IPv4 位址。 |
| **Identity** | 設定交換器識別項目的自訂名稱。 |
| **Allow From** | 將管理 Web 存取限制在指定的 IP 範圍或子網路。 |
| **Allow From Ports** | 將 Web 存取限制在指定的實體交換器介面。 |
| **Allow From VLAN** | 將存取限制在特定的傳入 VLAN ID 設定檔。 |

![SwOS Management](/img/ca29c618018d3a59.webp)

### DHCP 與 PPPoE Snooping {#dhcp--pppoe-snooping}

SwOS 內建安全機制，可在指定的不受信任介面上封鎖未授權或惡意的 DHCP 伺服器與 PPPoE 探索序列。

![CSS326 DHCP Snooping](/img/0f3d52a9da17fa79.webp)

### 設定安全性與維護 {#configuration-security-and-maintenance}

下方區段用於處理備份與管理密碼。

![Swos system3 css326](/img/3ba4a76afdcc03bc.webp)

* **Change Password**：更新設備存取金鑰。
* **Backup Configuration**：將目前設定儲存到本機檔案。
* **Restore Configuration**：上傳並套用現有的設定狀態。

---

## Link 標籤頁 {#link-tab}

Link 標籤可設定每個介面的實體鏈路參數，並監控作用中連線的屬性。

![Swos link css326](/img/8dec2ad5f0c9b5e2.webp)

* **Link Profiles**：管理介面狀態、切換速度／雙工自動協商，並控制流量控制暫停訊框。

---

## PoE 標籤 {#poe-tab}

*(適用於支援 Power over Ethernet 供電功能的設備)*

![SwOS PoE](/img/ca06196fd522c5cd.webp)

* 支援設定供電設定（`auto`、`on`、`off`），並在電力受限事件期間建立埠優先順序。

---

## SFP 標籤 {#sfp-tab}

為已連接的 SFP/SFP+ 光學收發器提供視覺化診斷。

![Swos sfp1 css326](/img/d2e58a862ecccc20.webp)

* 監控內部診斷資訊，例如操作溫度、雷射供應電壓、TX/RX 功率位準，以及硬體序號字串。

---

## 轉送與埠隔離 {#forwarding-and-port-isolation}

管理交換架構中的第 2 層封包轉送表。

![Swos forw css326](/img/cfc3bfc9dda03800.webp)
![Swos ivl system](/img/b0001fc2ceb3b1a6.webp)

### 埠隔離與隔離群組 {#port-isolation-and-isolated-groups}

埠隔離會在內部分割廣播網域，在不新增子網路層級的情況下控制用戶端通訊。

![SwOS Isolated Groups](/img/284614f24611b0f4.webp)
![SwO isolation example3](/img/de28135343d9795b.webp)

---

## LAG (Link Aggregation)

使用動態 LACP 連結或靜態陣列，將實體介面捆綁為單一高吞吐量通道。

![Swos lag css326](/img/42eb242aaffa0ae3.webp)

---

## RSTP (Rapid Spanning Tree Protocol)

提供迴路避免架構與結構性備援參數。

![Swos rstp css326](/img/6e7df850ef26634b.webp)

* 支援使用傳統 short 或現代 long 路徑評估結構，設定自訂橋接器路徑成本。

---

## VLAN 與 VLANs 矩陣設定 {#vlan--vlans-matrix-configuration}

VLAN 路由規則將傳入封包的排序行為與傳出格式化表分開。

### VLAN 索引標籤（傳入控制） {#vlan-tab-ingress-control}

處理傳入流量串流的埠行為。

![Swos vlan css326](/img/871181dce551f5b8.webp)

* **VLAN Modes**：跨 `disabled`、`optional`、`enabled` 與 `strict` 模式設定項目限制。

![Swos strict vlans](/img/d34e6c2d13d78d19.webp)

* **Default VLAN ID**：設定指派給傳入未標記流量的 Port VLAN ID（PVID）。

![Default vlan id](/img/1d9f62b52b3efa1f.webp)

### VLANs 索引標籤（傳出對應） {#vlans-tab-egress-mapping}

定義目標 trunk 埠上的廣播成員資格與處理方式。

![Swos vlans css326](/img/9d38b9ee9d82a8c1.webp)
![Swos vlans menu](/img/e5c63db80488b834.webp)

#### 傳統模式範本 {#traditional-mode-templates}

* **Access 介面**：將標準未標記端點配對至特定目標 VLAN 標籤。

  ![Access ports](/img/dcbdce357964f958.webp)

* **Trunk 與 Hybrid 選項**：在主要核心上行鏈路上混合多個已標記串流，並可選擇未標記的原生路由路徑。

  ![Hybrid ports](/img/90b987271e134d95.webp)
  ![Swos hybrid](/img/2fb81eda61c231cd.webp)
  ![Swos hybrid vlan](/img/330b019789c2b24b.webp)

---

## 私有 VLAN {#private-vlans}

在共享基礎架構空間中強制執行安全的結構化埠通訊設定檔。

![SwOS Private VLAN](/img/606fbb63c2620b62.webp)

---

## Hosts 標籤頁 {#hosts-tab}

顯示透過傳入來源位址探索到的有效硬體轉發資料庫（FDB）動態項目。

![Swos shost css326](/img/24da5f09ba887bf8.webp)

---

## IGMP Snooping

篩選多播散佈，追蹤作用中的群組訂閱，以封鎖多播氾濫。

![IGMP snooping](/img/a5464dca06492640.webp)
![CSSxx IGMP](/img/8404b127eb3f6c84.webp)
![IGMP vlantab](/img/2c8b3d4fcf937b4d.webp)

---

## SNMP 索引標籤 {#snmp-tab}

啟用透過標準 SNMP 結構進行監控。

![Swos snmp2 1](/img/f3b87569bbcad587.webp)

---

## ACL 索引標籤（存取控制清單） {#acl-tab-access-control-lists}

執行硬體卸載的篩選規則，比對 L2/L3/L4 訊框標頭中的模式，以丟棄或重新導向封包。

![CRS326 ACL table](/img/7e4fb4e7daa01ec1.webp)

---

## 診斷：統計資料、錯誤與直方圖 {#diagnostics-stats-errors-and-histograms}

追蹤介面計數器、丟棄的訊框、錯誤模式，以及詳細的結構化連結歷史診斷資訊。

![Swos stat1 css326](/img/bc002e2ae29c54ca.webp)
![Swos stat2 css326](/img/a1256a0deac7e870.webp)
![Swos stat3 css326](/img/4dc5d6afd153aab3.webp)

---

## Health 標籤頁 {#health-tab}

監控硬體操作環境，追蹤系統核心溫度與操作輸入電壓。

![SwOS CRS328 health](/img/c32f28c61507fb8f.webp)

---

## 雙重開機操作 {#dual-boot-operation}

許多 CRS 硬體設備支援雙重開機設計，可在執行 RouterOS 或 SwOS 之間切換。

![Router board settings](/img/206e2364a9ea20ec.webp)
![Router board settings webfig](/img/e5f83f41c903b22e.webp)
![Dual boot option](/img/59c51ae05cc7ea21.webp)

使用 RouterOS CLI 介面將作業系統切換為 SwOS 時，會使用下列系統指令結構：

```bash
/system routerboard settings set boot-os=swos
```

## 重設與重新安裝 {#reset-and-reinstall}

可以使用 System 選單中的「Reset Configuration」按鈕重設 SwOS 設定。如果無法使用 SwOS 網頁管理，仍可使用其他選項重設設定。

CSS326-24G-2S+ 與 CSS318-16G-2S+IN 設備內建備份 SwOS 韌體，可在標準韌體損毀或升級失敗時載入：

* 在 CSS326-24G-2S+ 與 CSS318-16G-2S+IN 開機時按住 Reset 按鈕數秒，會重設設定並載入備份韌體。
* 載入備份韌體後，可以使用網頁瀏覽器連線至 192.168.88.1（或從 DHCP 伺服器取得的位址），並安裝新的 SwOS 韌體。

Dual Boot 設備可以使用 Reset 按鈕開機進入 RouterOS。按住 Reset 按鈕的同時為設備供電，並等待 user LED 開始閃爍（約 5 秒）。這會重設 RouterOS 設定，設備接著會開機進入 RouterOS。設備可透過 RouterOS 存取後，即可升級並重設 SwOS 設定。請參閱文章 - Configuring SwOS using RouterOS。

具有序列主控台的 CRS3xx 設備有額外選項。

若要在 RouterOS 與 SwOS 之間切換，請遵循下列步驟：

1. 使用序列主控台連線至設備
2. 進入 RouterBOOT setup
3. 選擇「j - boot os」
4. 選擇 RouterOS 或 SwOS

若標準韌體損毀或升級失敗，可以載入 SwOS 備份韌體：

1. 使用序列主控台連線至設備
2. 開機進入 SwOS
3. 選擇「p - boot primary SwOS」
4. 載入備份韌體後，可以使用網頁瀏覽器連線至 192.168.88.1（或從 DHCP 伺服器取得的位址），並安裝新的 SwOS 韌體。

若要重設 SwOS 設定：

1. 使用序列主控台連線至設備
2. 開機啟動 SwOS
3. 選擇「r - reset configuration」

![Swos reset](/img/88b172351cb761c2.webp)
