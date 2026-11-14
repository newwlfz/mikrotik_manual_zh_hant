---
sidebar_key: "getting-started/routeros-licensing/chr/chr-licensing"
sidebar_position: 1
title: "CHR：許可"
sidebar_label: "CHR：許可"
description: "CHR 提供四種許可證級別——Free、P1 (Perpetual-1)、P10 (Perpetual-10) 和 P-Unlimited——付費選項可享受試用期。許可證為永久性質，與 CHR 系統 ID 繫結，並需要透過 MikroTik 賬戶伺服器定期續訂。試用許可證可在到期前升級，而過期的例項"
tags:
  - 'licensing'
  - 'chr'
source: https://manual.mikrotik.com/docs/7.24/getting-started/routeros-licensing/chr/chr-licensing
captured_at: '2026-11-04T11:29:39+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#overview}

Cloud Hosted Router (CHR) 提供四個許可證級別。許可證是永久性的，意味著只需購買一次即可無限期使用。如有需要，永久許可證也可以轉移到另一個 CHR 例項。
CHR 預設包含完整的 RouterOS 功能集。不過，與其他 RouterOS 版本相比，它採用不同的許可模式。

### CHR 許可證級別 {#chr-license-levels}

CHR 是 RouterOS 的一個版本，設計用於以虛擬機器方式執行。它有四個許可證級別，以及一個 Trial 選項，可讓你免費測試任意付費許可級別 60 天。

所有付費許可級別均提供 60 天免費試用。要獲取 Trial 許可證，你必須在 [MikroTik.com](https://mikrotik.com/) 上擁有已註冊的賬戶，因為所有 CHR 許可證管理都透過 MikroTik 賬戶系統處理。

永久許可證是終身許可證——購買一次即可無限期使用。如有需要，這些許可證也可以轉移到另一個 CHR 例項。

許可證直接繫結到 CHR 系統 ID。

執行中的 CHR 例項會定期連線 MikroTik 賬戶伺服器以續訂其許可證狀態。系統會顯示必須完成續訂的截止時間。如果 CHR 例項無法在截止時間之前續訂許可證，它的行為將與試用期已過期相同，並且不再允許將 RouterOS 升級到更新版本。

要在執行 Free 許可級別的 CHR 例項上啟用 Trial 許可證，你**必須**手動執行 `/system/license/renew` 命令，並將該 CHR 例項註冊到你的 MikroTik.com 賬戶。

| 許可證 | 速度限制 | 價格 | 描述 |
| :-- | :-- | :-- | :-- |
| Free | 1Mbit | 免費 | Free 許可證級別允許 CHR 無限期執行，每個介面的上傳限制為 1 Mbps。所有其他 RouterOS 功能均可無限制使用。要開始使用，請下載磁碟映像並將其部署為虛擬機器或雲實例。|
| P1 (Perpetual-1) | 1Gbit | $45 | P1 (Perpetual-1) 允許 CHR 無限期執行。每個介面的上傳限制為 1 Gbps。所有其他 RouterOS 功能均可無限制使用。可以從 P1 升級到 P10 或 P-Unlimited。以全價購買升級後，之前的許可證會在你的 MikroTik 賬戶中重新可用。|
| P10 (Perpetual-10) | 10Gbit | $95 | P10 (Perpetual-10) 允許 CHR 無限期執行。每個介面的上傳限制為 10 Gbps。所有其他 RouterOS 功能均可無限制使用。P10 可以升級到 P-Unlimited。以全價購買升級後，之前的許可證會在你的 MikroTik 賬戶中重新可用。|
| P-Unlimited | 無限制 | $250 | P-Unlimited (Perpetual-Unlimited) 允許 CHR 無限期執行。它是最高級別的許可證，沒有強制限制。|
| 60 天試用 | | 免費 | 除 Free 許可證外，你還可以使用 60 天試用評估更高效能級別（P1、P10 或 P-Unlimited）。需要已註冊的 [MikroTik.com](https://mikrotik.com) 賬戶。你可以從 CHR 例項申請試用許可證。這會把該例項的系統 ID 與你的 MikroTik 賬戶關聯，並啟用許可證管理和購買。所有付費許可級別均可試用。試用期自啟用起有效期為 60 天。過期後，許可證狀態將變為 **"Limited upgrades"**，這意味著 RouterOS 無法升級。**注意：**如果你打算購買該許可證，請在試用到期前完成購買。如果到期後 2 個月內未進行購買，該 CHR 例項將從你的 MikroTik 賬戶中移除。此時需要重新安裝 CHR。要申請試用許可證，請在 CHR 例項上執行以下命令：`/system license renew` 系統將提示你輸入 MikroTik.com 賬戶的使用者名稱和密碼。（*[sensitive](../../configuration-management/list-of-menus-with-sensitive-parameters.md)*）。|

:::warning
如果你想把永久許可證升級到更高級別，請先將現有許可證轉移到另一個 CHR 例項。這樣可以避免許可證在升級過程中丟失。
:::

### 許可說明 {#licensing-notes}

你可以克隆或複製正在執行的 CHR 系統，但克隆出的例項會保留原有的試用狀態。這意味著無法透過建立副本延長試用期。不過，每個系統仍然可以獨立獲得許可。

要開始新的試用期，請執行全新的 CHR 安裝並重新配置 RouterOS。

## 系統 ID 與克隆注意事項 {#system-id-and-cloning-considerations}

從同一磁碟映象部署多個 CHR 例項時，某些雲服務商（例如 Linode）可能會為多臺機器分配相同的系統 ID。
為避免這種情況，請在首次啟動後、申請試用許可證之前執行以下命令：`/system/license/generate-new-id`

:::warning
此命令只能用於執行 Free 許可級別的 CHR。在應用 Trial 或付費許可證之後請勿使用，因為它可能會阻止後續的許可證更新。
:::

## 部署多個例項 {#deploying-multiple-instances}

要執行多個 CHR 例項：

1. 從 MikroTik 網站下載 CHR 磁碟映象。
2. 為每臺虛擬機器建立映象的獨立副本。
3. 在虛擬機器管理程式或雲平臺中將每個副本部署為獨立的 VM。

請確保在啟動或註冊映象**之前**建立副本。

## 永久許可證要求 {#perpetual-license-requirements}

執行中的 CHR 例項必須定期連線 MikroTik 賬戶伺服器以續訂其許可證狀態。系統會指示必須完成此操作的截止時間。

> **重要：**如果 CHR 例項無法在截止時間之前連線到賬戶伺服器，它的行為將與試用期已過期相同。在此狀態下，你將無法把 RouterOS 升級到更新版本或修改軟體包（例如啟用或停用它們）。

## IP/Cloud 要求 {#ipcloud-requirement}

IP/Cloud 功能需要**付費的永久 CHR 許可證**。

## 許可證過期 {#expired-license}

當 CHR 例項在 "deadline-at" 時間之前未能聯絡 MikroTik 伺服器完成許可證續訂，或者 60 天試用期結束時，就會出現 CHR 許可證過期。

許可證過期後，路由器會繼續以相同級別執行，但軟體更新和軟體包更改將被停用。

**要為過期的 CHR 例項授權：**必須使用 Prepaid key。

如果過期例項在一定時間內未連線到許可證伺服器，它們將自動從你的 MikroTik 賬戶中移除。

## 為 CHR 許可購買 Prepaid key {#purchasing-a-prepaid-key-for-chr-licensing}

### 什麼是 Prepaid key？ {#what-is-a-prepaid-key}

Prepaid key 是你為 MikroTik 產品（包括 Cloud Hosted Router (CHR)）預先購買的許可證金鑰。該金鑰允許你在不立即將其分配給特定裝置的情況下購買許可證。

擁有 Prepaid key 後，你可以使用它升級現有的 CHR 系統 ID，或者透過提供裝置的 Software ID 將其轉換為完整的許可證金鑰。

### 購買 Prepaid key {#purchasing-a-prepaid-key}

按以下步驟購買 Prepaid key：

1. 訪問 [mikrotik.com](https://mikrotik.com/) 並登入你的賬戶。
2. 轉到 **Purchase a RouterOS License Key** 部分。
3. 選擇所需的許可證級別。
4. 選擇 **Prepaid key** 作為金鑰型別。
5. 輸入要購買的預付金鑰數量。
6. （可選）選擇金鑰所需的任何附加功能。
7. 點選 **Place key in the cart**。
8. 點選 **Proceed to checkout** 完成購買。

![Prepaid Key Purchase](/img/f4486a42a4b502b8.png)

### 完成購買 {#completing-your-purchase}

1. 檢查你的訂單詳情。
2. 使用**信用卡**（CC）或 **PayPal** 完成支付。

![Prepaid Key Purchase Complete](/img/bcf666707f80bd5b.png)

恭喜！你已成功購買 Prepaid key。

![Prepaid Key](/img/90b7ec9f73f89c97.png)

## 註冊 CHR 例項 {#registering-a-chr-instance}

首次設定 Cloud Hosted Router (CHR) 例項時，它會自動獲得 Free 許可證。要獲取更高級別的許可證，你必須將該 CHR 例項註冊到你的 MikroTik 賬戶。

該註冊會把 CHR 系統 ID 與你的 MikroTik.com 賬戶關聯，併為所選許可證級別啟用 60 天的試用期。

### 開始 Trial 許可證 {#starting-a-trial-license}

#### 使用 WinBox {#using-winbox}

1. 開啟 WinBox 並連線到你的 CHR 例項。
2. 導航到 `/system/license` 並點選 **Renew License**。

![Free to Trial upgrade](/img/1ece3433b0f958d3.png)
![Free to Trial upgrade](/img/1406e98c414a2426.png)

1. 輸入你的 MikroTik.com 賬戶憑據並選擇所需的許可證級別。

![Free to Trial upgrade](/img/49c64ffd70ac6937.png)

1. 確認升級。

![Free to Trial upgrade](/img/17c5392525189eba.png)

#### 使用命令列介面（CLI） {#using-the-command-line-interface-cli}

1. 檢查你當前的許可證狀態：

```
[admin@MikroTik] > /system/license/print
  system-id: HDlXorQ3f7L
      level: free
```

1. 使用你的賬戶憑據和所需級別執行續訂命令：

```
[admin@MikroTik] > /system/license/renew
account: mymikrotikcomaccount
password: *********************
level: p1
  status: done
```

1. 驗證升級是否成功：

```
[admin@MikroTik] > /system/license/print
         system-id: HDlXorQ3f7L        
             level: p1                 
  limited-upgrades: no                 
   next-renewal-at: 2026-06-11 10:55:29
       deadline-at: 2026-07-11 10:55:29
```

>輸出確認你的許可證已升級到 P1，並顯示下次續訂日期和 Trial 截止時間。

#### 驗證 CHR 註冊 {#verify-chr-registration}

1. 訪問 [mikrotik.com/client](https://mikrotik.com/client/) 並使用你的 mikrotik.com 憑據登入。
2. 在 **CHR LICENCES** 部分中，選擇 **All CHR keys**。
3. 將顯示你的 CHR 例項列表及其對應的許可證級別。

註冊後，CHR 系統 ID 會出現在你 MikroTik.com 賬戶的 **All CHR keys** 部分中。

### 獲取更高級別的 Trial {#acquiring-a-higher-level-trial}

:::warning
無法在同一例項上升級 Trial 許可級別。
:::

要試用更高級別的許可證，請部署一個新的 CHR 例項，並在註冊時選擇所需的 Trial 許可級別。

## 將 Trial 許可證升級為付費許可證 {#upgrading-a-trial-license-to-a-paid-license}

### 支付與許可證升級 {#payment-and-license-upgrade}

要將 Trial 許可證升級為付費許可證：

1. 訪問 [MikroTik 賬戶伺服器](https://www.mikrotik.com/client)。
2. 在 **CHR LICENCES** 部分中，選擇 **All CHR keys**。

![All CHR Keys](/img/0796c8d96fffb212.png)

1. 將顯示你的 CHR 例項列表及其對應的許可證級別。

![Trial to Paid upgrade](/img/1f7ff45a8b581dc5.png)

1. 在你想要升級的例項旁點選 **Upgrade**。

2. 選擇所需的許可證級別（它可以與你當前的 Trial 許可級別不同）。

![Trial to Paid upgrade](/img/4d67533fee64632e.png)

1. 點選 **Upgrade** 確認。

### 使用 Prepaid key {#using-prepaid-keys}

如果你有可用的 **Prepaid keys**，可以使用它們支付 CHR 許可證費用：

1. 點選 **Pay using Prepaid key**。

![Trial to Paid upgrade](/img/632dab99c602c771.png)

1. 如果你沒有預付金鑰或不想使用它們，請點選 **Proceed to checkout**。

### 支付方式 {#payment-methods}

你可以使用以下任一方式支付：

- 信用卡（CC）。
- PayPal。

![Trial to Paid upgrade](/img/96c08bb88da550cb.png)

## 升級永久許可證級別 {#upgrading-a-perpetual-license-level}

### 前提條件 {#prerequisites}

開始升級之前，請確保你已具備：

- 有效的 MikroTik.com 賬戶（使用者名稱和密碼）。
- 已購買你想要的許可證級別對應的 Prepaid key。

:::warning
如果你想把永久許可證升級到更高級別，請先將現有許可證轉移到另一個 CHR 例項。這樣可以避免許可證在升級過程中丟失。
:::

你可以將 Cloud Hosted Router (CHR) 的**永久**許可證升級到更高級別。支援以下升級：

- **P1 → P10** 或 **P1 → P-Unlimited**。
- **P10 → P-Unlimited**。

當你以全價購買升級時，你之前的許可證仍可在你的賬戶中使用。

:::info
P-Unlimited (perpetual-unlimited) 許可證是最高級別的可用許可證。它允許 CHR 無限期執行，沒有任何強制限制。
:::

### 升級已付費的永久 CHR 許可證級別 {#upgrading-the-paid-perpetual-chr-license-level}

1. 登入你的 MikroTik 賬戶並轉到 **All CHR keys**。
2. 選擇你想要升級的 CHR 例項。
3. 點選 **Upgrade**。

    ![License Upgrade Level](/img/21542650d93ae02a.png)

4. 選擇所需的許可證級別（P10 或 P-Unlimited）並點選 **Upgrade**。

    ![License Upgrade Level Select target](/img/b39f329808146f9b.png)

5. 選擇支付選項：

- **Pay using Prepaid key** — 如果你有可用的預付金鑰

    ![License Upgrade Level](/img/f36142266c66ad06.png)

- **Proceed to checkout** — 如果你希望使用其他方式支付

    ![License Upgrade Level](/img/c7085a9318d31441.png)

1. 選擇你的支付方式：

- 信用卡（CC）。
- PayPal。
    ![許可證升級級別](/img/552157a8db4dc24d.png)

1. 完成支付流程。

你的 CHR 許可證將升級到所選級別，而你之前的許可證仍會保留在你的賬戶中，以供將來使用。

:::warning
你可以升級到除 *p-unlimited* 之外的任何許可證級別。該級別代表可用的最高級別，無法再進一步升級。
:::

## 許可證轉移 {#license-transfer}

每個 Cloud Hosted Router (CHR) 安裝都直接繫結到你的 MikroTik 賬戶。你可以將永久許可證轉移到另一個 CHR 例項，前提是兩個例項都註冊在**同一**賬戶下。

### 轉移限制 {#transfer-restrictions}

| 許可證型別 | 是否可轉移？ | 說明 |
|---|---|---|
| 永久許可證 | yes | 僅可轉移到**同一**賬戶下的另一個 CHR 例項 |
| Prepaid key（已購買） | yes | 可透過 "Transfer prepaid keys" 轉移到其他賬戶 |
| Prepaid key（來自培訓） | no | 這些金鑰不可轉移 |

:::warning
無法將永久許可證轉移到已過期的例項。要為已過期的 CHR 例項授權，必須使用 Prepaid key。
:::

:::info
許可證轉出後的例項將保留相同的許可證級別，但狀態為 **Limited upgrades**（已過期）。它將繼續以該許可證級別執行，但將不再提供 RouterOS 升級。
:::

### 前提條件：所需的 CHR 例項 {#prerequisites-required-chr-instances}

轉移永久許可證之前，你必須具備：

- 帶有要轉出許可證的原始 CHR 例項。
- 註冊在**同一** MikroTik 賬戶下的目標 CHR 例項。

如果你沒有第二個 CHR 例項，請先建立一個，然後將其新增到你的賬戶。

### 轉移許可證 {#transferring-a-license}

按以下步驟轉移你的許可證：

1. **註冊新例項**

  在你的舊 CHR 所註冊的同一 MikroTik 賬戶下注冊新的 CHR 例項。使用 CLI 命令：

   ```
   /system/license/renew
   ```

1. **確認兩個例項都出現在你的賬戶中**

   確認舊的和新的 CHR 機器都顯示在你 MikroTik 賬戶的 **All CHR keys** 部分中。

2. **發起轉移**

- 轉到你賬戶的 **All CHR keys** 部分。

    ![Transfer button location](/img/058eb33e404b299c.png)

  - 為你想要轉移的系統 ID 點選 **Transfer** 按鈕。

1. **選擇目標例項**

   從列表中選擇你要將許可證轉移到其中的系統 ID。

   ![Select target instance](/img/65c83e778685e8ae.png)

2. **確認轉移**

   點選 **Transfer subscription** 完成該過程。

   ![Confirm transfer](/img/d24a244f88c412dd.png)

### 排查轉移錯誤 {#troubleshooting-transfer-errors}

如果你收到以下錯誤：
:::danger
*"此金鑰不符合轉移條件，因為沒有其他有效的 CHR 金鑰可以升級到此金鑰的許可級別。"*
:::
這意味著你沒有處於 Trial 模式的 CHR 例項來接收該許可證。

:::tip
**解決方案：**建立一個新的 CHR 例項並將其新增到你的賬戶。新增後，你就可以將現有許可證轉移到該新例項。
:::

## 許可證續訂 {#license-renewal}

CHR 許可證需要與 MikroTik 許可證伺服器定期通訊以保持許可證有效。

在 **System > License** 選單中，路由器會顯示兩個重要的時間戳：

- **next-renewal-at** — 路由器下次嘗試聯絡 MikroTik 許可證伺服器的時間。
- **deadline-at** — 必須成功與許可證伺服器通訊的最晚時間。

CHR 例項透過以下地址與許可證伺服器通訊：

`licence.mikrotik.com`

### 續訂過程 {#renewal-process}

- 在 **next-renewal-at** 時間過後，路由器每小時嘗試續訂許可證一次。
- 續訂嘗試會一直持續，直到伺服器成功響應。

### 許可證過期 {#license-expiration}

如果路由器無法在 **deadline-at** 時間之前聯絡到許可證伺服器：

- 許可證進入過期狀態。
- 不再允許 RouterOS 升級。
- 不再允許更改軟體包（啟用/停用/安裝/移除）。
- 路由器繼續以當前許可證級別執行。

### 續訂成功 {#successful-renewal}

與許可證伺服器成功通訊後：

- **next-renewal-at** 時間戳會被更新。
- **deadline-at** 時間戳會被更新。
