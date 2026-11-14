---
title: "Intercell"
slug: /intercell
source: https://manual.mikrotik.com/hardware/intercell
captured_at: '2026-11-04T09:51:04+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![Intercell 10 B38+B39 outdoor LTE base station.](/img/16dc8e4c820a14bb.jpg)

Intercell 10 B38+B39 是一款室外雙載波時分雙工 LTE（TDD-LTE）基站。每個載波支援 2×2 MIMO，每個射頻（RF）通道的輸出功率為 10 W，四個射頻通道的總輸出功率為 40 W。

## 快速開始 {#quick-start}

- 將外接天線和乙太網線連線到 **擴充套件插槽與埠** 一節所述的聯結器。
- 按 **供電** 一節所述連線 48 V DC 電源。
- 將筆記型電腦連線到裝置以進行配置。裝置支援 DHCP 和靜態 IP 地址分配。
- 如需透過預設維護 IP 地址訪問，請將筆記型電腦的 IP 地址設定為 192.168.200.100/24，並在網頁瀏覽器中開啟 https://192.168.200.200。
- 使用使用者名稱 admin 和密碼 MikroTik 登入。
- 按 **配置** 一節所述配置網路、回傳和射頻引數。

## 供電 {#powering}

電源聯結器接受 **48 V DC**。包裝內包含電源線和聯結器，但 **不包含電源**。最大負載下功耗可達 **200 W**。

- 將隨附的線纜連線到你的 48 V DC 電源。
- 將線纜聯結器連線到裝置。

乙太網連線請使用隨附的 RBGESP 浪湧保護器。

## 配置 {#configuration}

透過 Web 介面配置裝置。安裝和配置必須由合格人員執行。

### 網路架構 {#network-architecture}

![Small-cell network architecture with an LTE base station, management system, HeNB gateway, and EPC.](/img/21c6e7c105370179.webp)

各網路元件的作用如下：

- **Home eNodeB（HeNB）：** LTE 基站為使用者裝置（UE）提供服務。
- **網路管理系統（NMS）/ HeNB 管理系統（HeMS）：** 管理系統提供小基站生命週期管理，並支援 TR-181 和 TR-196 資料模型。
- **HeNB-GW：** HeNB 與移動性管理實體（MME）之間的閘道器，負責匯聚控制面與使用者面流量，並提供 S1/X2 代理功能。

### 配置流程 {#configuration-flow}

先配置網路接入，然後配置回傳和射頻引數。完成配置後再啟用射頻發射。

![Configuration sequence: sign in to the web interface, configure backhaul parameters, then configure radio parameters.](/img/e5900ccff294301a.webp)

**WAN** 介面是 SFP 埠，在網路配置中標識為 **ID1**。**LAN** 介面是乙太網埠，標識為 **ID2**。如果裝置透過 DHCP 獲取 IP 地址，可使用 MAC 掃描來查詢它。

靜態 IP 地址分配：

-

將計算機的 IP 地址設定為 192.168.200.100/24。

-

直接連線到 HeNB 的 WAN 介面並開啟 https://192.168.200.200。使用使用者名稱 admin 和密碼 MikroTik 登入。

-

在網路配置中，將 **Address Type** 設為 **Static**，然後輸入你的網路的 **IPv4 address** 和 **Mask**。

![Network configuration with static IPv4 address and mask fields.](/img/01a219db677e79dc.webp)

-

檢查已配置的介面和 IP 地址。

![IP interface list showing DHCP and static address assignments.](/img/28b49dd898601c00.webp)

-

選擇 **Submit**。HeNB 會重啟以應用配置。

-

將 HeNB 的 WAN 介面重新連線到你的網路，並透過 HTTPS 在其配置的 IP 地址上登入。

### 回傳引數 {#backhaul-parameters}

開啟 **Management → Cell**，將 **S1SigLinkServer** 設定為你的 MME 或 HeNB 閘道器的 IP 地址。

![Cell configuration with the S1SigLinkServer backhaul address highlighted.](/img/3baf82dbfd4fe798.webp)

### 射頻引數 {#radio-parameters}

本節中的數值僅為示例。請按照你的 LTE 網路設定網路標識和射頻引數。

#### 計算發射功率 {#calculate-transmit-power}

根據 **ReferenceSignalPower** 和與頻寬相關的基準值計算發射功率：

- **單副天線：** ReferenceSignalPower + Base，單位為 dBm。
- **兩副天線合計：** ReferenceSignalPower + Base + 3，單位為 dBm。

<table><thead><tr><th>頻寬</th><th>基準值（dB）</th></tr></thead><tbody><tr><td>1 MHz</td><td>19</td></tr><tr><td>3 MHz</td><td>23</td></tr><tr><td>5 MHz</td><td>25</td></tr><tr><td>10 MHz</td><td>28</td></tr><tr><td>15 MHz</td><td>30</td></tr><tr><td>20 MHz</td><td>31</td></tr></tbody></table>

:::warning warning

每副天線 **不得超過 40 dBm**。在啟用射頻發射前先計算發射功率；功率過高可能損壞功率放大器。

:::

在 20 MHz 下，**ReferenceSignalPower** 為 -14 時，每副天線為 -14 + 31 = 17 dBm。值為 9 時為 9 + 31 = 40 dBm，即本產品的最大值。

在 **Management → Cell** 中配置通用引數：

<table><thead><tr><th>引數</th><th>示例值</th></tr></thead><tbody><tr><td>Duplex Mode</td><td>TDD</td></tr><tr><td>TAC</td><td>10</td></tr><tr><td>PLMNID</td><td>00666</td></tr></tbody></table>

![Common cell configuration with duplex mode, TAC, and PLMNID.](/img/05fffcdd62825b0a.webp)

#### 配置 Cell 1 射頻引數 {#configure-cell-1-radio-parameters}

開啟 **Cell1** 標籤頁並配置以下示例值：

<table><thead><tr><th>引數</th><th>示例值</th></tr></thead><tbody><tr><td>CellIdentity</td><td>257</td></tr><tr><td>CandidateARFCNList</td><td>38400</td></tr><tr><td>CandidatePCIList</td><td>0..503</td></tr><tr><td>FreqBandIndicator</td><td>39</td></tr><tr><td>DL Bandwidth</td><td>100</td></tr><tr><td>UL Bandwidth</td><td>100</td></tr><tr><td>ReferenceSignalPower</td><td>-14</td></tr></tbody></table>

![Cell1 radio parameters for LTE band 39.](/img/6dc0e27d1efa168b.webp)

**CandidateARFCNList** 指定下行 E-UTRA 絕對射頻通道號（EARFCN）；HeNB 會自動配置上行 EARFCN。HeNB 從 **CandidatePCIList** 中選擇物理小區標識（PCI），範圍為 0..503。

頻寬欄位使用資源塊數值：**20 MHz → 100**、**15 MHz → 75**、**10 MHz → 50**、**5 MHz → 25**。**UL Bandwidth** 應設定為與 **DL Bandwidth** 相同。

#### 配置 Cell 2 射頻引數 {#configure-cell-2-radio-parameters}

開啟 **Cell2** 標籤頁並配置以下示例值。EARFCN、PCI 和頻寬的約定與 Cell1 相同。

<table><thead><tr><th>引數</th><th>示例值</th></tr></thead><tbody><tr><td>CellIdentity</td><td>258</td></tr><tr><td>CandidateARFCNList</td><td>37900</td></tr><tr><td>CandidatePCIList</td><td>0..503</td></tr><tr><td>FreqBandIndicator</td><td>38</td></tr><tr><td>DL Bandwidth</td><td>100</td></tr><tr><td>UL Bandwidth</td><td>100</td></tr><tr><td>ReferenceSignalPower</td><td>-14</td></tr></tbody></table>

![Cell2 radio parameters for LTE band 38.](/img/6afda40fe0976bfb.webp)

配置完兩個小區並檢查發射功率後，啟用 **AdminState** 以開啟射頻發射。選擇 **Submit**；HeNB 會重啟以應用配置。

#### 檢查射頻狀態 {#checking-the-rf-status}

開啟 **Management → Cell**，在 **Cell1** 和 **Cell2** 標籤頁上檢查 **OpState**。值為 **True** 表示無線小區已成功建立。

![Cell status showing OpState and the radio parameters in use.](/img/da38d2ba9ac1851c.webp)

## 安裝 {#mounting}

本裝置專為室外使用而設計，防護等級為 **IP66**。安裝時請使線纜入口朝下，並使用遮蔽 Cat6 線纜。隨附的安裝五金件支援壁掛安裝或抱杆安裝，抱桿直徑為 **50–120 mm**。

:::warning warning

裝置重 **25 kg**。安裝必須由合格人員執行。

:::

-

拆開安裝支架和附件的包裝。

![Intercell chassis and separate mounting frame.](/img/677940ea2aad1457.webp)

-

進行抱杆安裝時，用四個固定板、四個 M12 螺栓和四個 M12 螺母固定支架。將每個螺栓依次穿過安裝支架、固定板和抱箍，然後擰緊。

![Mounting frame attached to a pole with fixing plates and M12 bolts.](/img/9ce330e0e7350b7d.webp)

-

在機箱下側附近的四顆固定螺釘下方留出 **3 mm** 的間隙，以便它們卡入安裝支架。

![Chassis fixing screws with a 3 mm gap for the mounting frame.](/img/6a8b4a8083d988a8.webp)

-

將機箱放置到支架上，使兩側的螺釘卡入固定孔。

![Intercell chassis seated in the mounting frame.](/img/bbc68dda840ffadc.webp)

-

擰緊並固定全部八顆螺釘，完成安裝。

![Secured chassis with the mounting screw positions marked.](/img/65cd7238d2893837.webp)

## 接地 {#grounding}

既要對安裝基礎設施（包括鐵塔和桅杆）接地，也要對裝置接地。將接地線連線到裝置的接地螺釘，另一端連線到已接地的桅杆。

電源介面防雷標準：**GB/T 17626.5** 和 **IEC 61000-4-5**。

## 擴充套件插槽與埠 {#expansion-slots-and-ports}

圖中數字標識各聯結器和指示燈：

![Intercell connector panel with numbered power, antenna, indicator, Ethernet, and SFP positions.](/img/bc9e352c53b5b238.webp)

- 電源聯結器。
- 天線聯結器。
- 電源指示燈。
- 活動指示燈。
- GPS 天線聯結器。
- SNIFF 天線聯結器。
- 乙太網聯結器。
- SFP 聯結器。

## 硬體規格 {#hardware-specifications}

<table><thead><tr><th>規格</th><th>值</th></tr></thead><tbody><tr><td>LTE 頻段</td><td>TDD B38：2570–2620 MHz。TDD B39：1880–1920 MHz。</td></tr><tr><td>通道頻寬</td><td>5、10、15 或 20 MHz。</td></tr><tr><td>20 MHz 下單載波峰值速率</td><td>下行：140 Mbps（256QAM，SF2）。上行：30 Mbps（64QAM，SF1）。</td></tr><tr><td>20 MHz 下載波聚合峰值速率</td><td>下行：280 Mbps（256QAM，SF2）。上行：60 Mbps（64QAM，SF1）。</td></tr><tr><td>使用者容量</td><td>2 × 196 個 RRC 連線使用者和 2 × 96 個活躍使用者。</td></tr><tr><td>同步</td><td>GPS、IEEE 1588v2 和網路監聽。</td></tr><tr><td>回傳介面</td><td>一個 RJ45 千兆乙太網埠和一個光 SFP 埠。</td></tr><tr><td>射頻聯結器</td><td>六個：四個天線聯結器、一個嗅探聯結器和一個 GPS/北斗聯結器。</td></tr><tr><td>最大輸出功率</td><td>每副天線 40 ± 1 dBm。配置發射功率時應保持在 40 dBm 限值以內。</td></tr></tbody></table>

## 配件 {#accessories}

包裝內包含：

- 帶插頭的電源線。不含電源。
- [S-31DLC20D SFP 模組](https://mikrotik.com/product/S-31DLC20D-181)。
- [RBGESP 乙太網浪湧保護器](https://mikrotik.com/product/rbgesp)。
- N/SMA-JK 轉接器。
- 用於 GPS 和嗅探聯結器的防雷保護。
- 安裝支架。
- 大杆安裝附件。

有關 SFP 模組相容性，請參閱 [MikroTik 有線介面相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## 升級示例 {#upgrade-example}

<a href="/assets/files/intercell-upgrade-example-5ece1656a406f6ae31224ea25803dc93.pdf" target="_blank" rel="noopener">下載韌體升級示例（PDF）</a>，其中包含檢查韌體版本、選擇映象和驗證升級的截圖。

## B38 配置示例 {#b38-configuration-example}

<a href="/assets/files/intercell-b38-cfg-example-2078e289f3e5aef6e28fbbe0196d7f12.pdf" target="_blank" rel="noopener">下載 B38 配置示例（PDF）</a>，其中包含將小區配置調整為頻段 38 並重啟裝置的截圖。

## Intercell 內建 EPC {#intercell-built-in-epc}

<a href="/assets/files/intercell-built-in-epc-75f9a8dc8ba16b3652fef99419e9caee.pdf" target="_blank" rel="noopener">下載內建 EPC 配置文件（PDF）</a>，內容涵蓋網路拓撲、演進分組核心網（EPC）引數和使用者配置。

## 透過序列埠控制檯重設配置 {#reset-configuration-through-the-serial-console}

<a href="/assets/files/intercell-reset-serial-console-a68ab7a25f27ea98bd8a568d1f3f9239.pdf" target="_blank" rel="noopener">下載序列埠控制檯重設說明（PDF）</a>，包括拆開機箱、序列埠連線和刪除配置檔案。

:::warning warning

序列埠控制檯操作會刪除配置檔案，並在重啟後恢復預設配置。

:::

## 配置匯入 {#configuration-import}

<a href="/assets/files/intercell-cfg-import-6bea2be2b015b0d4b56eb4ed5763fd49.pdf" target="_blank" rel="noopener">下載配置匯入示例（PDF）</a>，內容涵蓋資料模型版本匹配以及 Device 和 Cndata 配置檔案的匯入。

## 監控 {#monitoring}

<a href="/assets/files/intercell-monitoring-e1bb86c0453d3c8c7d5bc77d71765444.pdf" target="_blank" rel="noopener">下載協定棧日誌檢視器文件（PDF）</a>，內容涵蓋監控工具和日誌分析。

## 完整雙載波配置 {#full-dual-carrier-configuration}

<a href="/assets/files/intercell-dual-carrier-configuration-d2a48f833ca10c90ac192e01e2f96bee.pdf" target="_blank" rel="noopener">下載完整雙載波配置文件（PDF）</a>，內容涵蓋初始設定、網路與射頻配置以及維護。

## 作業系統支援 {#operating-system-support}

裝置執行 Intercell HeNB 軟體。不支援 RouterOS。
