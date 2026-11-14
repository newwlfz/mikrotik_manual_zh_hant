---
sidebar_key: "getting-started/routeros-licensing/x86/index"
sidebar_position: 3
title: "x86 許可"
sidebar_label: "x86 許可"
description: "本頁介紹 MikroTik RouterOS 的 x86 系統授權，涵蓋許可證金鑰獲取、Software ID 要求、系統先決條件，以及許可證級別詳情，包括 trial、free demo、WISP 和 controller 許可證的功能與定價。"
tags:
  - 'licensing'
  - 'software-id'
source: https://manual.mikrotik.com/docs/7.25/getting-started/routeros-licensing/x86
captured_at: '2026-11-04T11:17:20+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 許可證基礎 {#licensing-basics}

對於 x86 系統（基於 PC 的安裝），必須獲取許可證金鑰。每個系統都有一個唯一識別符號，稱為 **Software ID**，用於許可目的。

許可證金鑰以字元塊形式提供。可以從您的 MikroTik 賬戶或購買後收到的電子郵件中複製，然後貼上到路由器中。您可以將金鑰直接貼上到終端，或使用 WinBox 許可證選單中的 **貼上金鑰** 選項。許可證生效需要重啟。

:::info
**x86 Software ID** 繫結到儲存裝置（例如 NAND、SSD、HDD、NVMe）的 MBR。
:::

購買許可證前，請確認重啟後 Software ID 保持不變。

:::danger
如果底層儲存或配置不穩定，Software ID 可能會發生變化。例如，在以下情況下可能發生：

- 使用有缺陷或正在故障的儲存裝置（SSD、HDD、NVMe）。
- RAID 配置設定不正確或無法持久保留。
- 在兩次啟動之間使用了不同的儲存控制器或介面卡。
:::

### 系統要求 {#system-requirements}

- **軟體包版本：** RouterOS v6.34 或更高版本。
- **主機 CPU：** x86-64 架構（64 位）。
- **RAM：** 512 MB 或更多。
- **磁碟：** 128 MB 或更多。
- **RouterOS v6：** 支援的最大硬碟大小為 16 GB。
- **RouterOS v7：** 最大 RAM 和磁碟空間受 Linux 核心 5.6.3 限制，並取決於具體硬體。

所需的最小 RAM 取決於介面數量和 CPU 數量。使用以下公式計算近似值：

- **RouterOS v6：** `RAM = 128 + [ 8 × (CPU_COUNT) × (INTERFACE_COUNT - 1) ]`
- **RouterOS v7：** `RAM = 512 + [ 8 × (CPU_COUNT) × (INTERFACE_COUNT - 1) ]`

## RouterOS 許可證金鑰級別 {#routeros-license-key-levels}

可以從 [`/system/license`](../../../cli-reference/system/license/index.md) 選單獲取許可資訊：

```text
[admin@MikroTik] > /system/license/print
    software-id: "ABCD-1234"
         nlevel: 6
       features:
[admin@MikroTik] >
```

也可以從等效的 [WinBox](../../../management-tools/winbox.md) 或 [WebFig](../../../management-tools/webfig.md) 選單中檢視。

安裝 x86 系統後，RouterOS 以 **Trial mode** 執行，無任何限制。你有 24 小時註冊 **Level 1 (Free Demo)** 許可證，或購買 Level 4、5 或 6 許可證並應用有效金鑰。

```text
[admin@MikroTik] /system/license/print 
  software-id: TRPC-YYR2
   expires-in: 23h48m24s
```

許可證級別之間的差異如下表所示：

<WideTable>

| **級別編號** | **0（試用模式）** | **1（Free Demo）** | **4（WISP）** | **5（WISP）** | **6（Controller）** |
| :-- | :-- | :-- | :-- | :-- |  :-- |
| **價格** | [無金鑰](https://www.mikrotik.com/download.html) | [免費（需要註冊）](https://mikrotik.com/client/) | $45 | $95 | $250 |
| **Wireless4 AP 模式（PtMP）** | 24 小時試用 | - | yes | yes | yes |
| **Wireless6 AP 模式** | - | - | yes | yes | yes |
| **PPPoE 隧道** | 24 小時試用 | 1 | 200 | 500 | 無限制 |
| **PPTP 隧道** | 24 小時試用 | 1 | 200 | 500 | 無限制 |
| **L2TP 隧道** | 24 小時試用 | 1 | 200 | 500 | 無限制 |
| **OVPN 隧道** | 24 小時試用 | 1 | 200 | 無限制 | 無限制 |
| **HotSpot 活躍使用者** | 24 小時試用 | 1 | 200 | 500 | 無限制 |
| **User Manager 活躍會話** | 24 小時試用 | 1 | 20 | 50 | 無限制 |

</WideTable>

:::info
如果某項功能未列出，則不受許可證限制。
:::

:::warning
演示許可證將路由器限制為單個介面。此限制適用於多種介面型別（veth、vlan、vxlan 等），而不僅是表中列出的型別。
:::

:::note
級別 2 是舊版（2.8 之前）許可證格式的過渡許可證。這些許可證已不再提供。現有的級別 2 許可證繼續有效，但升級需要購買新許可證。級別 3 許可證僅用於無線工作站（用戶端/CPE）。*對於 x86 PC，級別 3 不提供單獨購買。*
:::

### 所有許可證 {#all-licenses}

- 永不過期 — 已獲得許可並執行中的路由器可以無限期使用。
- 支援無限數量的介面。
- 每個許可證僅對單次安裝有效。
- 包含無限次軟體升級（例外：從版本 7.8 開始，演示許可證不允許升級 RouterOS 版本）。

### 預付費金鑰 {#prepaid-key}

預付費金鑰是一種可提前為 MikroTik 產品購買的許可證。它允許您獲取許可證而無需立即將其分配給特定裝置。獲得後，預付費金鑰可用於升級 CHR 例項，或透過使用目標 Software ID 轉換為 x86 系統或 RouterBOARD 裝置的許可證金鑰。

## 如何購買 RouterOS 許可證金鑰 {#how-to-purchase-a-routeros-license-key}

1. 前往 [mikrotik.com](https://mikrotik.com) 並登入您的賬戶。
2. 導航到 **"Purchase a RouterOS License Key"** 部分。
3. 選擇所需的許可證 Key Level。
4. 將 Key Type 設定為 **"License key"**。
5. 在 License Key Information 欄位中，貼上裝置的 Software ID。
6. 選擇部署所需的任何可選 Key Features。
7. 選擇 **"Place key in the cart"**。
8. 選擇 **"Proceed to checkout"** 完成購買。

![](/img/8bbe36f9bc0a6d5f.png)

## 檢查並完成購買 {#review-and-complete-your-purchase}

請仔細檢查訂單詳情，然後使用 **信用卡**（CC）或 **PayPal** 付款。

![](/img/bcf666707f80bd5b.png)

您已購買 RouterOS 許可證金鑰。

## 如何將 Prepaid Key 轉換為 x86 的許可證金鑰 {#how-to-convert-a-prepaid-key-to-a-license-key-for-x86}

1. **購買 RouterOS [預付金鑰](./index.md#prepaid-key)。**

   - 登入您的 [mikrotik.com](https://mikrotik.com) 賬戶。
   - 如果尚未購買，請購買 RouterOS 預付金鑰。

2. **進入“從預付金鑰生成金鑰”部分。**

   - 在您的賬戶中導航到“從預付金鑰生成金鑰”部分。

3. **選擇並轉換預付金鑰。**

   - 從列表中選擇所需的 Prepaid Key。
   - 輸入要獲得許可的 x86 裝置的 **Software ID**，或要升級許可證級別的路由器的 **Software ID**。

![](/img/e711992d34ff1204.png)

1. **生成許可證金鑰。**

   - 按 "Generate"。
   - 會出現一條確認訊息：“已成功將預付費金鑰轉換為新許可證！”。

![](/img/b2441fab5c176c43.png)

1. **應用許可證金鑰。**

   - 複製生成的許可證金鑰。
   - 將其貼上到 x86 裝置以應用許可證。

你已成功將 Prepaid Key 轉換為 x86 裝置的許可證金鑰。

## 替換金鑰 {#replacement-key}

Replacement Key 是 MikroTik 支援團隊在 x86 儲存裝置故障，或執行 RouterOS 的 x86 例項丟失許可證時發放的特殊許可證金鑰。其費用為 $10，且每個原始金鑰只能發放一次。

在發放 Replacement Key 之前，MikroTik 支援可能要求提供原始驅動器已故障的證明。在某些情況下，這包括將故障驅動器物理寄送給 MikroTik。

## Replacement Key 申請 {#replacement-key-request}

1. **登入並提交申請**
   - 登入您在 [mikrotik.com](https://mikrotik.com) 的賬戶。
   - 使用“[支援聯絡表單](https://help.mikrotik.com/servicedesk/servicedesk/)”提交申請，或直接傳送電子郵件至 [support@mikrotik.com](mailto:support@mikrotik.com)。
   - 在申請中包含以下資訊：
     - **需要替換金鑰的明確說明。**
     - **舊 Software ID 及其註冊時所用的賬戶。**

2. **等待確認並應用金鑰**
   - 當 MikroTik 支援團隊確認替換金鑰已新增到您的賬戶後，登入並導航到 **"Make a key from replacement key"** 部分。
   - 繼續執行啟用。

![](/img/d9913b7629d99ed3.png)

1. **選擇許可證級別**
   - 選擇你希望應用 Replacement Key 的許可證級別。

2. **輸入新的 Software ID**
   - 輸入目標裝置的 **新 Software ID**。

3. **完成購買**
   - 選擇 **"Add license replacement to cart"** 前往結賬並完成付款。

![](/img/1e388024f0024c24.png)

1. **獲取您的金鑰**
   - 一封包含新許可證金鑰的確認電子郵件會發送到您賬戶的註冊電子郵件地址。
   - 新生成的金鑰也可以在 **"Search and view all keys"** 部分的 **"Purchased YYYY"** 資料夾下找到，其中 **"YYYY"** 代表當前年份。

:::warning
*每個原始金鑰只能發放一個替換金鑰。您不能對同一金鑰使用兩次替換金鑰流程。如果需要第二次替換，則必須為 RouterOS 裝置購買新金鑰。*
:::

## 獲取和管理許可證 {#obtaining-and-managing-licenses}

### 在哪裡可以購買 RouterOS 許可證金鑰？ {#where-can-i-buy-a-routeros-license-key}

要為 **x86 PC 安裝** 購買許可證，您必須註冊一個[我們網站上的賬戶](https://www.mikrotik.com/client)，並使用賬戶門戶中提供的[購買 RouterOS 許可證金鑰](#how-to-purchase-a-routeros-license-key)選項。

### 可以升級 x86 許可證級別嗎？ {#can-i-upgrade-the-x86-license-level}

要升級 x86 許可證級別，你必須以全價購買所需的許可證金鑰。

### 如果你在其他地方購買了金鑰 {#if-you-purchased-your-key-elsewhere}

如果您的許可證是透過第三方供應商購買的，請直接聯絡該供應商尋求支援，因為他們負責為其銷售的許可證提供協助。

### 如果我有許可證並想將其轉移到另一個賬戶 {#if-i-have-a-license-and-want-to-move-it-to-another-account}

應用 x86 許可證金鑰後，它會繫結到您的 MikroTik 賬戶，並且無法轉移到另一個賬戶。唯一可以在賬戶之間轉移的許可證型別是未使用的預付費金鑰。從 Training 收到的贈送預付費金鑰不可轉移。要轉移已購買的預付費金鑰，請導航到 MikroTik 賬戶中 **ROUTEROS KEYS** 部分下的 **Transfer prepaid keys**。

### 如果裝置上的許可證丟失 {#if-you-have-lost-a-license-on-your-device}

如果您的路由器因任何原因丟失了許可證，請將路由器升級到最新的可用 RouterOS 版本，並使用您的 [mikrotik.com](https://mikrotik.com) 賬戶中的 **"Request license key"** 選項。提交申請時，請使用 RouterOS 中 [`/system/license`](../../../cli-reference/system/license/index.md) 選單下的 Software ID 和序列號。收到後，將許可證金鑰應用到您的裝置。如果申請功能無法使用，請聯絡 [support@mikrotik.com](mailto:support@mikrotik.com) 尋求幫助。

:::warning
*如果許可證是由於非經銷商在保修範圍內執行的維修而丟失的，您必須按全價購買新的 RouterOS 許可證。*
:::

## 使用許可證 {#using-the-license}

### 我可以格式化或重新刷寫驅動器嗎？ {#can-i-format-or-re-flash-the-drive}

使用非 MikroTik 工具（例如 `dd` 或 `fdisk`）格式化或重新映像儲存裝置會破壞您的許可證。

在嘗試之前請格外小心，並聯系 MikroTik 支援。此類操作不推薦，Replacement Key 請求可能會被拒絕。

要安全地重新安裝 RouterOS，請使用官方 MikroTik 工具（例如 **Netinstall**），或透過建立可啟動安裝介質（例如 USB 快閃記憶體盤）從磁碟映像安裝。

### 我可以在多少臺計算機上使用該許可證？ {#how-many-computers-can-i-use-the-license-on}

RouterOS 許可證只能用於單個裝置/系統。

在 x86 系統上，許可證繫結到 **Software ID**，而 Software ID 繫結到儲存裝置（MBR）。這允許你將同一儲存裝置移到另一臺計算機而不丟失許可證。但是，許可證不能轉移到不同的儲存裝置。

格式化或覆蓋儲存裝置會永久擦除許可證，需要獲取新許可證。

:::danger
**重要：** 移動或修改儲存裝置時，請謹慎執行所有操作。使用不同的儲存控制器或介面卡，或修改 BIOS/UEFI 設定等更改，可能會改變 Software ID 並導致許可證丟失。
:::

最佳做法是，在任何硬體更改前後生成並儲存 `supout.rif` 檔案。如果 Software ID 發生變化，您可以將這些檔案提供給 MikroTik 支援團隊進行稽核。

如果 Software ID 已更改，你可以申請 Replacement Key。

### 我可以臨時將儲存裝置用於 RouterOS 以外的其他用途嗎？ {#can-i-temporarily-use-the-storage-device-for-something-else-other-than-routeros}

不可以。

### 我可以將許可證移到另一個儲存裝置（例如 SSD、HDD、NVMe）嗎？ {#can-i-move-the-license-to-another-storage-device-for-example-ssd-hdd-nvme}

如果你當前的儲存裝置損壞或無法使用，可以透過申請 Replacement Key 將許可證轉移到新裝置。

替換金鑰的價格為 $10。

### 我必須將整個金鑰輸入路由器嗎？ {#must-i-type-the-whole-key-into-the-router}

不需要，只需複製金鑰並將其貼上到 [`/system/license`](../../../cli-reference/system/license/index.md) 選單的 **Paste Key** 選項中，然後確認重啟。

![](/img/152e9782386d7b57.png)

或者，將金鑰直接貼上到 CLI 中，然後按 **Y** 重啟。

### 我可以先在驅動器上安裝其他作業系統，然後再重新安裝 RouterOS 嗎？ {#can-i-install-another-os-on-my-drive-and-then-reinstall-routeros-later}

不可以。如果您使用格式化、分割區工具或任何其他修改 MBR 的工具，您將丟失許可證，並且必須獲取新許可證。此過程並非免費（請參閱[替換金鑰](#replacement-key)）。

### 我的 RouterBOARD 丟失了 - 我可以將許可證轉移到另一個系統嗎？ {#i-lost-my-routerboard---can-i-transfer-the-license-to-another-system}

MikroTik 硬體包含永久繫結到裝置的嵌入式許可證。此許可證在任何情況下都不能轉移到另一系統。此限制也適用於路由器執行期間所應用的所有許可證升級。

### 從經銷商處購買的許可證 {#licenses-purchased-from-resellers}

你從其他供應商和經銷商處購買的金鑰不在你的賬戶中。你的 [mikrotik.com](https://mikrotik.com) 賬戶僅包含直接從 MikroTik 購買的許可證。

### 我沒有使用該軟體，你們可以終止我的許可證嗎？ {#i-am-not-using-the-software-can-you-terminate-my-license}

許可證是獨立金鑰，MikroTik 無法遠端控制您的裝置。因此，它無法驗證許可證是否正在被積極使用。出於這個原因，MikroTik 無法終止任何已發放的許可證。

### 我可以將 x86 許可證升級或轉移到 CHR 許可證嗎？ {#can-i-upgrade-or-transfer-an-x86-license-to-a-chr-license}

不支援將 x86 或 RouterBOARD 許可證升級或轉移到 CHR 許可證，反之亦然。必須為 CHR 單獨購買許可證。

### 如果我在購買金鑰時輸入了錯誤的 Software ID 怎麼辦？ {#what-if-i-entered-the-wrong-software-id-when-purchasing-a-key}

如果許可證金鑰是使用錯誤的 Software ID 生成的（例如，輸入 `1` 而不是 `I` 這樣的拼寫錯誤），您可以在不聯絡支援的情況下更正金鑰上的 Software ID。此功能允許修正 Software ID 的最多 1-2 個字元：

1. 登入您的 [mikrotik.com](https://mikrotik.com) 賬戶。
2. 導航到 **"Search and view all keys"**。
3. 開啟購買年份資料夾—— **"Purchased YYYY"**，其中 **"YYYY"** 代表當前年份。
4. 選擇相關金鑰，然後選擇 **"Edit"**。
5. 選擇 **"Fix Software ID"**。
6. 在 Software ID 欄位中更正字元並儲存。

## x86 安裝 {#x86-installation}

介紹 RouterOS x86 系統要求和安裝方法，包括 USB 和 Netinstall 部署。

[x86 安裝指南](../../installation-and-upgrade/install/x86-installation.md)
