---
sidebar_key: "getting-started/installation-and-upgrade/install/chr-installation/vultr"
sidebar_position: 8
title: "CHR：Vultr 安裝"
sidebar_label: "CHR：Vultr 安裝"
description: "本頁指導使用者如何在 Vultr 上部署 MikroTik CHR：首先搭建 SystemRescue 伺服器，然後使用 wget 和 dd 命令將 CHR 映象寫入磁碟，最後透過 SSH 連線以配置路由器。"
tags:
  - 'chr'
  - 'vultr'
source: https://manual.mikrotik.com/docs/7.25/getting-started/installation-and-upgrade/install/chr-installation/vultr
captured_at: '2026-11-04T11:16:31+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Vultr 擁有[二十多個資料中心位置](https://www.vultr.com/features/datacenter-locations/)，你可以選擇在這些位置部署 MikroTik CHR，以獲得最佳的[吞吐量和延遲](https://nj-us-ping.vultr.com/)。  
按照以下步驟在 Vultr 上安裝 MikroTik CHR。

## 步驟 1：以救援模式部署伺服器 {#step-1-deploy-a-server-in-rescue-mode}

在這一步中，你將使用 SystemRescue（一個可引導的 Linux ISO）在 Vultr 上部署一臺新伺服器。

1. [部署](https://my.vultr.com/deploy/)一個新的 [Cloud Compute](https://www.vultr.com/products/cloud-compute/) 例項。
2. 選擇效能最符合你需求的位置。你可以使用 Vultr 的[網路 looking glass 工具](https://nj-us-ping.vultr.com/)來測試任意位置的吞吐量和延遲。
3. 在 **Server Image** 區域中選擇 **ISO Library** 標籤頁。
4. 選擇 **SystemRescue x64**。
5. 選擇一個[頻寬配額](https://www.vultr.com/resources/faq/?query=bandwidth#bandwidthcalculation)足以滿足你需求的伺服器規格。
6. 為伺服器設定主機名和標籤，然後單擊 **Deploy Now**。

伺服器部署完成後，繼續執行下一步。

## 步驟 2：將 CHR 映象寫入磁碟 {#step-2-write-the-chr-image-to-the-disk}

1. 在網頁瀏覽器中，訪問 [MikroTik 下載頁面](https://mikrotik.com/download)。
2. 找到最新的 Stable RAW CHR 磁碟映象。Vultr 要求版本為 **7.2.3 Stable** 或更高。
3. 右鍵單擊軟盤圖示以複製 URL。現在不要下載映象；你將在後續步驟中把它下載到伺服器上。  
   ![](/img/0f950288ad223006.webp)
4. 在 [Vultr 客戶門戶](https://my.vultr.com/)中導航到伺服器的資訊頁面。
5. 連線到[網頁控制檯](https://www.vultr.com/docs/vultr-web-console-faq/)。  
   ![](/img/be07173a7c22c0f2.webp)
6. 在網頁控制檯中，使用 "wget" 將 CHR 映象下載到伺服器。如果你已將下載 URL 複製到剪貼簿，可以透過網頁控制檯[將其傳送到伺服器](https://www.vultr.com/docs/vultr-web-console-faq/)。

   在下面的示例中，請將 x.x.x 替換為你實際的版本號。

    ```bash
    # wget https://download.mikrotik.com/routeros/x.x.x/chr-x.x.x.img.zip
    ```

7. 解壓下載的檔案。

    ```bash
    # unzip chr-x.x.x.img.zip
    ```

8. 使用 dd 將 MikroTik CHR 映象寫入伺服器磁碟。

    ```bash
    # dd if=chr-x.x.x.img of=/dev/vda
    ```

- - **if** 是你在上一步中解壓出來的映象。
  - **of** 是伺服器的磁碟：`/dev/vda`。

此過程需要幾分鐘；完成後請繼續執行下一步。

## 步驟 3：連線到 MikroTik CHR {#step-3-connect-to-mikrotik-chr}

1. 導航到伺服器的[設定頁面](https://my.vultr.com/)。
2. 選擇 **Custom ISO** 選單，然後單擊 **Remove ISO**。伺服器將重新啟動。
3. 連線到[網頁控制檯](https://www.vultr.com/docs/vultr-web-console-faq/)。
4. 以 admin 身份登入。由於未設定密碼，在提示符處按 <kbd>Enter</kbd> 即可。
5. 檢視軟體許可，然後設定一個新的強密碼。
6. 關閉網頁控制檯，然後在本地計算機上開啟終端。
7. 以 admin 身份透過 SSH 連線到伺服器的 IP 地址。

   ```ros
   ssh admin@192.0.2.2
   ```

8. 輸入你在上一步中設定的強密碼。

至此基本安裝完成。請[保護你的 MikroTik CHR 路由器](../../../securing-your-router.md)，並參閱[文件](../../../first-time-configuration.md)將伺服器配置為生產用途。請訪問 Vultr 網站了解其 [VPC](https://docs.vultr.com/products/network/vpc) 和[防火牆](https://docs.vultr.com/vultr-firewall)功能。
