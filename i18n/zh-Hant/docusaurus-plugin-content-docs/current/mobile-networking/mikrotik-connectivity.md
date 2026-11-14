---
sidebar_key: "mobile-networking/mikrotik-connectivity"
sidebar_position: 3
title: "MikroTik 連線性"
sidebar_label: "MikroTik 連線性"
description: "MikroTik Connectivity 推出 eSIM 解決方案，實現無縫裝置連線，無需更換物理 SIM 卡，並提供透過 MikroTik 賬戶門戶和 RouterOS CLI/WinBox 介面進行啟用的步驟。"
tags:
  - 'esim'
  - 'connectivity'
source: https://manual.mikrotik.com/docs/mobile-networking/mikrotik-connectivity
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 概述 {#summary}

MikroTik Connectivity 是我們新的內建 eSIM 解決方案，可確保您的裝置在任何地方保持連線，無需更換物理 SIM 卡或進行外部啟用步驟。更多資訊請訪問 [https://mikrotik.com/connectivity](https://mikrotik.com/connectivity)

### 啟用示例 {#activation-example}

1) 登入您的 MikroTik 賬戶，選擇 "My devices"。

![](/img/e298464df4344576.png)

1) 輸入您裝置的序列號——系統將進行檢測。選擇區域，然後按 "Add to list"。

![](/img/7a833a6166f9b0dd.png)

1) 選擇適合您需求的資料套餐和付款方式。然後將其新增到購物車。

![](/img/c7f14ae2aa5edac1.png)

1) 在購物車中繼續付款。

![](/img/52d12f26caaa6a5c.png)

1) 付款完成後，返回 "My devices"，您將看到訂閱現已處於 Active 狀態。

![](/img/a266f451f8e08e2e.png)

:::info
MikroTik eSIM 配置檔案已預載入，因此啟用期間無需網際網路連線。啟用本身通常需要幾分鐘，但在某些情況下甚至可能需要幾個小時。
:::

1) 在 RouterOS 中檢查您的裝置是否設定為使用 "esim"，以及正確的配置檔案是否處於活動狀態。  
  
CLI:

```
[admin@EG25-G&KNe] > /interface/lte/settings/print 
                 mode: auto    
         esim-channel: auto    
        firmware-path: firmware
  link-recovery-timer: 120     
             sim-slot: sim      
[admin@EG25-G&KNe] > /interface/lte/settings/set sim-slot=esim      
[admin@EG25-G&KNe] > /interface/lte/esim/print
Flags: A - ACTIVE
Columns: INTERFACE, NAME, SPN, ICCID
#   INTERFACE  NAME       SPN                      ICCID
0 A lte1       Profile 1  MikroTik  89358152000001049461
1   lte1       Profile 4  MikroTik  89358152000001349465
```

在 WinBox 中：

 轉到 Interfaces > LTE > Modem 選擇 esim SIM 卡槽：

![](/img/530500251b870002.png)

轉到 Interfaces > LTE > eSIM 檢視哪個是活動的 esim 配置檔案：

![](/img/b8d00f0482c880d6.png)

如果您需要更改 Active 配置檔案，請右鍵單擊該配置檔案並選擇 "Activate"：

![](/img/7ec165b963f9f2b8.png)

#### [影片教程：我們的官方 YT 頻道，MikroTips 系列](https://www.youtube.com/watch?v=2YxHL9A4Ys0) {#video-tutorial-our-official-yt-channel-mikrotips-series}

### 常見問題解答 {#faq}

<details>
<summary>分配給我裝置的 IP 地址是公網 IP 地址嗎？</summary>

不是，該 IP 地址是私有地址。您可以配置 BTH 來遠端訪問您的裝置：[Back To Home（遠端回家）](../network-management/cloud/back-to-home.md)

</details>

<details>
<summary>是否也支援 IPv6？</summary>

僅支援 IPv4。

</details>

<details>
<summary>我應該配置什麼接入點名稱（APN）？</summary>

您可以使用 "use-network-apn=yes" 選項，或將 APN 手動設定為 "[mikrotik.net](http://mikrotik.net "http://mikrotik.net/")"

</details>

<details>
<summary>為什麼使用 MikroTik Connectivity 時，延遲比使用本地運營商的 SIM 卡更高？</summary>

MikroTik Connectivity 作為漫遊服務執行。它透過一組可能位於其他國家的 PDN 閘道器路由資料。額外的距離和額外的網路跳數會增加往返時間，因此與使用本地運營商的服務相比，延遲會顯得更高。

</details>

<details>
<summary>為什麼使用 MikroTik Connectivity 時，下載/上傳速度比使用本地運營商的 SIM 卡更低？</summary>

MikroTik Connectivity 作為漫遊服務執行。它透過一組可能位於其他國家的 PDN 閘道器路由資料。額外的距離和額外的網路跳數會增加往返時間，因此延遲會增加。由於延遲更高，TCP 效能會直接受到影響。TCP 依靠確認來增大其擁塞視窗並提升吞吐量。當往返時間變長時，確認返回需要更多時間，擁塞視窗增長更慢，可達到的吞吐量會下降。

</details>

<details>
<summary>如何暫停、升級或取消我的 MikroTik Connectivity 訂閱？</summary>

要管理您的 eSIM 訂閱套餐，請登入您的 **mikrotik.com** 賬戶並導航到 **"My devices"** 部分。搜尋您裝置的序列號並單擊它。

在那裡，您有兩種方式管理您的套餐：

* **透過 "Plan" 標籤頁：** 在這裡您會找到 **"Unsubscribe"** 選項，或透過選擇不同的資料套餐來升級。
* **透過 "Details" 標籤頁：** 轉到 **"Status"** 欄位，您可以在 **Active**、**Pause data transfer** 或 **Cancel subscription** 之間切換。

</details>
