---
sidebar_key: "containers/user-guides/claire-homeassistant"
sidebar_position: 1
title: "將 Claire 與 hAP be³ Media 上的 Home Assistant 配對"
sidebar_label: "將 Claire 與 hAP be³ Media 上的 Home Assistant 配對"
description: "在 hAP be³ Media 上安裝支援 Thread 的 Home Assistant 應用，並使用 Home Assistant Companion 應用配對一個 Claire 空氣質量感測器。"
tags:
  - 'container'
  - 'homeassistant'
  - 'matter'
  - 'thread'
source: https://manual.mikrotik.com/docs/containers/user-guides/claire-homeassistant
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

將您的 Claire 或 Claire Lite 空氣質量感測器與 **hAP be³ Media** 上的 Home Assistant 配對，以便在手機或網頁瀏覽器中檢視感測器讀數，並在自動化和提醒中使用這些讀數。

Claire 透過 **Matter over Thread** 連線。路由器內建的 Thread 無線模組提供無線連線，而 **`homeassistant-thread`** 應用包含 Home Assistant、OpenThread Border Router 和 Matter server。

:::note
在較早的 RouterOS 版本中，此應用名為 **`ha-otbr-matter`**。請選擇路由器應用目錄中可用的、支援 Thread 的應用。
:::

## 開始之前 {#before-you-begin}

開箱即用時，hAP be³ Media 已配置 Apps，已安裝所需軟體包，並在 device-mode 中啟用了容器支援。您可以直接繼續進行 Home Assistant 應用安裝。

請準備以下內容：

- 一臺可訪問網際網路的 hAP be³ Media。
- 一個連線到路由器、用於應用儲存的 USB 驅動器。如果該驅動器尚未在 RouterOS 中準備好使用，請遵循[磁碟設定說明](../../storage/index.md)。
- 已通電且位於路由器範圍內的 Claire 或 Claire Lite。
- 一部已安裝 Home Assistant Companion 應用、已啟用藍牙並可訪問路由器 Wi-Fi 網路的手機。

將您的計算機和手機連線到路由器的本地網路，以便進行設定和配對。

如果您重新安裝了 RouterOS 或重設了裝置，請檢查是否已安裝 `container` 軟體包，並且已在 [device-mode](../../system-information-and-utilities/device-mode.md) 中啟用容器支援。如有必要，請恢復這些設定。確認 device-mode 更改需要物理接觸路由器。如果缺少應用配置，請執行 Apps 設定嚮導。

## 安裝 Home Assistant 應用 {#install-the-home-assistant-app}

1. 使用 WinBox 或 WebFig 連線到 hAP be³ Media，並開啟 **App** 選單。
2. 如果您尚未配置應用儲存和網路，請選擇 **Setup**。選擇 USB 驅動器、您的 LAN 網橋以及路由器的 LAN IP 地址。詳情請參閱 [Apps 設定嚮導](../apps/index.md#setup-wizard)。

   ![WinBox App setup wizard with usb1 selected as the Apps Disk.](/img/5a42992dfe165dd4.webp)

3. 選擇 **`homeassistant-thread`**，或在較早的 RouterOS 版本中選擇 **`ha-otbr-matter`**，然後選擇 **Enable**。

   ![WinBox app catalog showing homeassistant-thread with Home Assistant, OpenThread Border Router, and Matter server.](/img/b37796d295e13187.webp)

4. 等待應用下載、解壓並啟動。該應用包含多個容器映象，因此安裝可能需要幾分鐘。
5. 開啟應用的 **UI URL** 連結以訪問 Home Assistant。

Apps 系統會自動配置容器及其網路。

## 在手機上設定 Home Assistant {#set-up-home-assistant-on-your-phone}

1. 在 Home Assistant 歡迎頁面上，建立您的管理員賬戶並完成初始設定。
2. 在手機上開啟 Home Assistant Companion 應用。
3. 選擇您的 Home Assistant 例項。如果未自動發現，請輸入您從 **UI URL** 開啟的相同 URL。
4. 使用您在 Home Assistant 中建立的使用者名稱和密碼登入。
5. 允許配對請求的許可權，包括藍牙和相機訪問許可權。

使用手機上的 Companion 應用配對 Claire。配對後，您可以從 Companion 應用或 Home Assistant 網頁介面檢視其讀數。

## 配對 Claire {#pair-claire}

1. 在 Home Assistant Companion 應用中，開啟 **Settings → Devices & services** 並選擇 **Matter**。
2. 選擇 **Add device**。如果詢問該裝置是否已在使用，對於未配對的 Claire，請選擇 **No, it's new**。按照提示開啟二維條碼掃描器。
3. 在 Claire 上，按住側邊按鈕 **3 秒** 以開啟設定選單。
4. 使用短按按鈕在 **Pairing code** 上高亮。
5. 按住按鈕 **1 秒** 以顯示 Matter 配對二維條碼。
6. 使用 Companion 應用掃描 Claire 螢幕上的二維條碼，並等待配對完成。設定期間請將手機靠近 Claire。
7. 為裝置命名並將其分配到一個區域，例如 **客廳**。

在沒有按鈕輸入 30 秒後，Claire 會返回主螢幕。如果二維條碼在您掃描前消失，請再次開啟 **Pairing code**。

## 檢視感測器讀數 {#view-sensor-readings}

在 Home Assistant 中，開啟 **Settings → Devices & services → Matter** 並選擇 Claire。其裝置頁面會顯示可用的感測器讀數。顯示的感測器取決於您的 Claire 型號。

您可以將讀數新增到儀表板，或建立自動化，例如當 CO₂ 超過您選擇的閾值時傳送通知。請保持 Claire 通電並處於 Thread 覆蓋範圍內，以便 Home Assistant 能夠接收更新。

## 如果配對未完成 {#if-pairing-does-not-finish}

### 手機和二維條碼 {#phone-and-qr-code}

- 請透過手機上的 **Home Assistant Companion 應用** 進行配對。配對後使用網頁介面檢視讀數。
- 啟用藍牙，並在系統請求時允許應用的相機、藍牙或附近裝置以及本地網路許可權。配對期間請將手機靠近 Claire。
- 如果 iPhone 反覆拒絕配對，請重啟 iPhone，重新開啟 Companion 應用，然後重試。
- 如果二維條碼消失，請再次在 Claire 上開啟 **Pairing code**。在沒有按鈕輸入 30 秒後，其螢幕會返回主檢視。

### Home Assistant 和 Thread {#home-assistant-and-thread}

- 確認 **`homeassistant-thread`** 應用（或在較早的 RouterOS 版本中為 **`ha-otbr-matter`**）已完成啟動，並且其 **UI URL** 可以開啟。
- 讓手機保持在路由器的本地 Wi-Fi 網路上。啟用了用戶端隔離的訪客網路或手機上的 VPN 可能會阻止本地發現和通訊，即使 Home Assistant 網頁可以開啟也是如此。請斷開手機的 VPN，並使用主 LAN 進行配對。
- Matter 使用本地 IPv6 和組播發現。如果您自定義了路由器的網路或防火牆配置，請檢查是否允許 IPv6 以及 Home Assistant、手機和 Thread 邊界路由器之間所需的本地通訊。
- 在 Home Assistant 中檢查 **Settings → Devices & services** 裡的 **Matter**、**Thread** 和 **OpenThread Border Router** 整合。在重試之前，請解決任何報告的設定錯誤。
- 如果手機提示需要 Thread 邊界路由器，請檢查 Thread 整合，並確認 hAP be³ Media 的 Thread 網路可用。如果您有多個 Thread 網路，請檢查首選的是哪一個。在重試之前，請完成 Home Assistant 和 Companion 應用中的任何 Thread 憑據傳輸或同步提示。
- 設定期間，請將 Claire 移近 hAP be³ Media。配對後，請使其保持在 Thread 覆蓋範圍內，以便讀數持續可用。

### 現有配對和感測器更新 {#existing-pairing-and-sensor-updates}

- 如果 Claire 已配對到另一個家庭，而您想替換該配對，請先使用 Claire 設定選單中的 **Unpairing**，然後重複這些步驟。這會移除其現有配對。
- 通電後，請留出最多 10 分鐘讓 Claire 的感測器穩定。讀數以不同間隔更新：CO₂ 每 30 秒更新一次，顆粒物每 5 分鐘更新一次。讀數在短時間內保持不變不一定表示存在連線問題。

有關按鈕控制和取消配對說明，請參閱 [Claire 硬體手冊](/hardware/iaqm-thc2pv-w-and-iaqm-thc2pv-g)。
