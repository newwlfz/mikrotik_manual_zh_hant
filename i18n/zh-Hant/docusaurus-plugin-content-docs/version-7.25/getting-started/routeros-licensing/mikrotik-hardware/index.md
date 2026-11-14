---
sidebar_key: "getting-started/routeros-licensing/mikrotik-hardware/index"
sidebar_position: 2
title: "MikroTik 硬體許可"
sidebar_label: "MikroTik 硬體許可"
description: "執行 RouterOS 的 MikroTik 硬體路由器附帶預安裝許可證，這些許可證決定隧道限制和使用者會話等功能。許可證級別從試用模式到無限制功能不等，價格因級別而異。使用者可透過 CLI 或管理工具檢視許可證，並透過預付費金鑰或與裝置 ID 繫結的直接購買進行升級。"
tags:
  - 'licensing'
source: https://manual.mikrotik.com/docs/7.25/getting-started/routeros-licensing/mikrotik-hardware
captured_at: '2026-11-04T11:17:04+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 許可證基礎 {#licensing-basics}

執行 RouterOS 的 MikroTik 硬體路由器隨附預裝許可證。如果您已購買基於 RouterOS 的裝置，則無需額外步驟。

## RouterOS 許可證金鑰級別 {#routeros-license-key-levels}

可以從 CLI 系統控制檯獲取許可證資訊：

```text
[admin@MikroTik] > /system/license/print
    software-id: "ABCD-1234"
         nlevel: 6
       features:
[admin@MikroTik] >
```

相同資訊也可在 [WinBox](../../../management-tools/winbox.md) 或 [WebFig](../../../management-tools/webfig.md) 中檢視。

```text
[admin@MikroTik] /system/license/print 
  software-id: TRPC-YYR2
   expires-in: 23h48m24s
```

許可證級別之間的差異如下表所示：

:::info
級別 2 是舊版（2.8 之前）許可證格式的過渡許可證。這些許可證已不再提供。現有的級別 2 許可證將繼續正常工作，但升級需要購買新許可證。級別 3 許可證僅用於無線站點（用戶端/CPE）用途。
:::

<WideTable>

| **級別編號** | **0（試用模式）** | **1（免費演示）** | **3（WISP CPE）** | **4（WISP）** | **5（WISP）** | **6（控制器）** |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **價格** | [無金鑰](https://www.mikrotik.com/download.html) | [免費（需要註冊）](https://mikrotik.com/client/) | 不出售 | $45 | $95 | $250 |
| **Wireless4 AP 模式（PtMP）** | 24 小時試用 | - | no | yes | yes | yes |
| **Wireless6 AP 模式** | - | - | yes | yes | yes | yes |
| **PPPoE 隧道** | 24 小時試用 | 1 | 200 | 200 | 500 | 無限制 |
| **PPTP 隧道** | 24 小時試用 | 1 | 200 | 200 | 500 | 無限制 |
| **L2TP 隧道** | 24 小時試用 | 1 | 200 | 200 | 500 | 無限制 |
| **OVPN 隧道** | 24 小時試用 | 1 | 200 | 200 | 無限制 | 無限制 |
| **HotSpot 活躍使用者** | 24 小時試用 | 1 | 1 | 200 | 500 | 無限制 |
| **User Manager 活躍會話** | 24 小時試用 | 1 | 10 | 20 | 50 | 無限制 |

</WideTable>

:::info
如果某項功能未列出，則不受許可證限制。
:::

:::info
**RouterBOARD Software ID** 繫結到裝置儲存。
:::

### 所有許可證 {#all-licenses}

- 永不過期 — 已獲得許可且正在執行的路由器可無限期使用。
- 支援無限數量的介面。
- 每個許可證僅對單次安裝有效。
- 包含無限制的軟體升級。

:::warning
**wifi-qcom** 驅動支援 PTMP 操作，不受許可證級別限制。**Mode: AP** 在所有 **wifi-qcom** 裝置上普遍可用，可讓多個用戶端站點連線。
:::

## 升級裝置許可證級別 {#upgrading-the-device-license-level}

如果您需要升級裝置許可證級別，必須購買更高級別的許可證，可以作為[預付金鑰](#prepaid-key)購買，也可以直接購買與裝置 **Software ID** 繫結的 [RouterOS 許可證](#how-to-purchase-a-routeros-license-key)。

許可證金鑰以字元塊形式提供。可以從您的 MikroTik 賬戶或購買後收到的電子郵件中複製，然後貼上到路由器中。您可以將金鑰直接貼上到終端，或使用 WinBox 許可證選單中的 **貼上金鑰** 選項。許可證生效需要重啟。

### 預付費金鑰 {#prepaid-key}

預付金鑰是一種可提前為 MikroTik 產品購買的許可證。它允許您獲取許可證而無需立即將其分配給特定裝置。獲取後，預付金鑰可用於升級 CHR 例項，或使用目標 Software ID 轉換為 x86 系統或 RouterBOARD 裝置的許可證金鑰。

## 如何購買 RouterOS 許可證金鑰 {#how-to-purchase-a-routeros-license-key}

1. 前往 [mikrotik.com](https://mikrotik.com) 並登入您的賬戶。
2. 導航到 **“購買 RouterOS 許可證金鑰”** 部分。
3. 選擇所需的許可證金鑰級別。
4. 將金鑰型別設定為 **“License key”**。
5. 在許可證金鑰資訊欄位中，貼上您裝置的 Software ID。
6. 選擇部署所需的任何可選金鑰功能。
7. 點選 **“將金鑰加入購物車”** 按鈕。
8. 點選 **“繼續結賬”** 完成購買。

![Purchase a RouterOS License Key](/img/8bbe36f9bc0a6d5f.png)

## 檢查並完成購買 {#review-and-complete-your-purchase}

請仔細檢查訂單詳情，然後使用 **信用卡**（CC）或 **PayPal** 付款。

![Purchase a RouterOS License Key](/img/bcf666707f80bd5b.png)

恭喜！您已成功購買 RouterOS 許可證金鑰。

## 自定義無線通道（僅適用於 Atheros 92xx 裝置） {#custom-wireless-channels-only-for-atheros-92xx-devices}

高階通道功能為無線介面配置提供了更多可能性：

- **擴充套件掃描列表：** 同時覆蓋多個頻段和通道寬度，以實現全面的無線介面配置。
- **精確頻率自定義：** 在相容硬體上支援非標準通道中心頻率（以 kHz 為粒度指定）。
- **靈活通道寬度：** 在硬體支援的情況下，允許配置非標準通道寬度（以 kHz 為粒度指定）。

## 如何將預付金鑰轉換為 RouterOS 許可證金鑰 {#how-to-convert-a-prepaid-key-to-a-routeros-license-key}

1. **購買 RouterOS [預付金鑰](#prepaid-key)。**

   - 登入您的 [mikrotik.com](https://mikrotik.com) 賬戶。
   - 如果尚未購買，請購買 RouterOS 預付金鑰。

2. **進入“從預付金鑰生成金鑰”部分。**

   - 在您的賬戶中導航到“從預付金鑰生成金鑰”部分。

3. **選擇並轉換預付金鑰。**

   - 從列表中選擇所需的預付金鑰。
   - 輸入要升級許可證級別的路由器的 **Software ID**。

![](/img/e711992d34ff1204.png)

1. **生成許可證金鑰。**

   - 按“Generate”。
   - 將顯示確認訊息：“已成功將預付金鑰轉換為新許可證！”。

![](/img/b2441fab5c176c43.png)

1. **應用許可證金鑰。**

   - 複製生成的許可證金鑰。
   - 將其貼上到裝置中以應用許可證。

您已成功將預付金鑰轉換為路由器的許可證金鑰。

## 獲取和管理許可證 {#obtaining-and-managing-licenses}

### 在哪裡可以購買 RouterOS 許可證金鑰？ {#where-can-i-buy-a-routeros-license-key}

所有 MikroTik 硬體裝置都包含預裝的 RouterOS 許可證。

### 如果裝置上的許可證丟失 {#if-you-have-lost-a-license-on-your-device}

如果您的路由器因任何原因丟失了許可證，請將路由器升級到最新的可用 RouterOS 版本，並使用您的 [mikrotik.com](https://mikrotik.com) 賬戶中的 **“請求許可證金鑰”** 選項。提交請求時，請使用 RouterOS 中 `/system/license` 選單下的 Software ID 和序列號。收到後，將許可證金鑰應用到您的裝置。如果請求功能無法使用，請聯絡 [support@mikrotik.com](mailto:support@mikrotik.com) 尋求幫助。

### 我的路由器丟失了許可證，可以申請替換金鑰嗎？ {#my-router-has-lost-the-license-can-i-request-a-replacement-key}

不可以，替換金鑰僅適用於 x86。

:::warning
*如果許可證丟失是由於非經銷商在保修範圍內進行的維修所致，您將需要以全價購買新的 RouterOS 許可證。*
:::

## 使用許可證 {#using-the-license}

### 我可以轉讓 MikroTik 硬體許可證嗎？ {#can-i-transfer-a-mikrotik-hardware-license}

MikroTik 硬體包含永久繫結到裝置的嵌入式許可證。此許可證在任何情況下都不能轉移到另一系統。此限制也適用於路由器執行期間所應用的所有許可證升級。

### 是否可以將路由器許可證升級或轉移到 x86 系統或 CHR 許可證？ {#is-it-possible-to-upgrade-or-transfer-the-router-license-to-an-x86-system-or-a-chr-license}

無法轉移裝置許可證。

## 相關指南 {#related-guides}

### x86 安裝 {#x86-installation}

介紹 RouterOS x86 系統要求和安裝方法，包括 USB 和 Netinstall 部署。

[x86 安裝指南](../../installation-and-upgrade/install/x86-installation.md)
