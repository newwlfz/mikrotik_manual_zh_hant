---
sidebar_key: "management-tools/quick-set"
sidebar_position: 8
title: "快速設定"
sidebar_label: "快速設定"
description: "在 WinBox 中使用 Quick Set 設定 MikroTik 家用路由器：選擇模式、配置 Wi-Fi、選擇網際網路連線型別，並透過帶註釋的截圖檢視本地網路設定。"
tags:
  - 'homeap'
  - 'quickset'
  - 'wireless'
source: https://manual.mikrotik.com/docs/management-tools/quick-set
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

**Quick Set** 將家用路由器的主要設定集中在一個頁面上。在 WinBox 中，連線到路由器並選擇左側選單中的 **Quick Set**。也可以透過路由器的 IP 地址在其 Web 介面中使用 Quick Set，在預設配置中通常是 `192.168.88.1`。

Quickset 適用於所有具有某種出廠預設配置的裝置。沒有配置的裝置必須手動配置。最受歡迎且推薦的模式是 HomeAP（或 HomeAP dual，具體取決於裝置）。此 Quickset 模式為家庭使用者提供最簡單的術語和最常用的選項。

使用 Quick Set 對具有預設配置的路由器進行初始設定。如果你已經在其他 WinBox 選單或 WebFig 中更改了配置，請繼續使用那些選單：Quick Set 可能會覆蓋手動配置的設定。

## 在 WinBox 中查詢主要設定 {#find-the-main-settings-in-winbox}

編號標註顯示了 **Home AP Dual** 的主要區域：

1. **模式** - 選擇路由器的角色預設。Home AP Dual 為 2.4 GHz 和 5 GHz 無線電提供單獨的網路名稱。
2. **無線** - 設定網路名稱和 Wi-Fi 密碼。
3. **網際網路** - 選擇路由器如何獲取其網際網路地址。
4. **本地網路** - 檢視 LAN 地址、DHCP 伺服器和 NAT 設定。
5. **系統** - 開啟更新或路由器密碼對話方塊。
6. **確定 / 應用** - 檢視後儲存配置。**確定** 還會關閉視窗；**取消** 會在不應用未儲存更改的情況下關閉視窗。

![WinBox Quick Set overview with numbered callouts for the mode, wireless settings, internet settings, local network, system controls, and save buttons](/img/7517d253ebe57556.webp)

:::note
截圖顯示的是現有路由器配置，而不是出廠預設值。網路名稱、密碼、裝置識別符號和用戶端詳細資訊均已隱藏。此示例中防火牆、DHCP 伺服器和 NAT 處於關閉狀態；對於將 LAN 連線到網際網路的家用路由器，請遵循網際網路和本地網路部分中描述的設定。可用模式和欄位取決於路由器型號和已安裝的無線軟體包。
:::

## 模式 {#modes}

根據路由器型號，Quickset 下拉選單中提供不同的 Quickset 模式：

- **CAP**：受控接入點，一種由集中式 [CAPsMAN](../wireless/abgn/capsman/index.md) 伺服器管理的 AP 裝置。僅在你已經設定好 CAPsMAN 伺服器時使用。
- **CPE**：用戶端裝置，用於連線到接入點 (AP) 裝置。提供掃描所在區域 AP 裝置的選項。
- **HomeAP**：大多數家庭使用者預設的接入點配置頁面。提供更少的選項和簡化的術語。
- **HomeAP dual**：雙頻裝置（2GHz/5GHz）。大多數家庭使用者預設的接入點配置頁面。提供更少的選項和簡化的術語。
- **Home Mesh**：用於組建更大的 WiFi 網路。在路由器中啟用 CAPsMAN 伺服器，並將本地 WiFi 介面置於 CAPsMAN 控制之下。按住復位按鈕啟動其他 MikroTik WiFi AP，它們會加入此 HomeMesh 網路（詳情請參閱其快速指南）。
- **PTP Bridge AP**：當你需要將兩個遠端位置透明互聯到同一網路時，將一臺裝置設為此模式，並將另一臺裝置設為下一個（PTP Bridge CPE）模式。
- **PTP Bridge CPE**：當你需要將兩個遠端位置透明互聯到同一網路時，將一臺裝置設為此模式，並將另一臺裝置設為上一個（PTP Bridge AP）模式。
- **WISP AP**：類似於 HomeAP 模式，但提供更高階的選項，並使用行業標準術語，例如 SSID 和 WPA。

## HomeAP {#homeap}

這是你應使用來快速配置家庭接入點的模式。

### 無線 {#wireless}

從截圖中標記的兩個控制元件開始：

1. 在 **網路名稱** 中輸入你的裝置應看到的名稱。例如，為兩個無線電使用 `Home`，或使用 `Home` 和 `Home-5GHz` 來區分它們。
2. 在 **WiFi 密碼** 中輸入你的 Wi-Fi 密碼。這是手機和計算機用來加入網路的密碼；它與 **系統** 中的路由器管理員密碼不同。

![WinBox Quick Set wireless settings with arrows to the network name fields and WiFi Password; the existing names and password are hidden](/img/65b5f53b28ef0314.webp)

應用配置時，更改網路名稱或密碼會斷開 Wi-Fi 用戶端。初次設定時，請用乙太網線將計算機連線到 LAN 埠，以便在不丟失 Wi-Fi 連線的情況下完成配置。

在此部分設定您的無線網路：

- **網路名稱**：你的智慧手機如何看到你的網路？在此設定任意你喜歡的名稱。在 HomeAP dual 中，你可以將 2GHz（傳統）和 5GHz（現代）網路設為相同或不同的名稱（見常見問題）。使用任意你喜歡的名稱和格式。
- **頻率**：通常可以保留 "Auto"，這樣路由器會掃描環境，並選擇佔用最少的頻率通道（僅執行一次）。如果需要進行實驗，請使用自定義選擇。
- **頻段**：通常保留預設值（2GHz b/g/n 和 5GHz A/N/AC）。
- **使用訪問列表 (ACL)**：如果你想根據使用者的 MAC（硬體）地址限制誰可以連線到你的 AP，請啟用此選項。要使用此選項，請先允許這些用戶端連線，然後使用 "Copy to ACL" 按鈕。這會將所選用戶端複製到訪問列表。構建訪問列表 (ACL) 後，你可以啟用此選項來禁止其他任何人嘗試連線到你的裝置。通常可以保持不動，因為無線密碼已經提供了所需的限制。
- **WiFi 密碼**：此處最重要的選項。設定一個安全密碼，同時也會加密你的無線通訊，這是連線到無線網路所必需的。
- **WPS accept**：使用此按鈕向支援 WPS 連線模式的特定裝置授予訪問許可權。對於印表機和其他難以輸入密碼的外設很有用。先在用戶端裝置中啟動 WPS 模式，然後在此處選擇一次 WPS 按鈕以允許該裝置。該按鈕會工作幾秒鐘，並且按用戶端逐一操作。
- **訪客網路**：適用於不需要知道你主 WiFi 密碼的家中訪客。在此選項中為他們設定單獨的密碼。訪客使用者無法訪問你 LAN 中的其他裝置和其他訪客裝置。此模式會啟用 Bridge 過濾器來阻止這種情況。
- **無線用戶端**：此表格顯示已連線的用戶端裝置（它們的 MAC 地址、是否在你的訪問列表中、最後使用的 IP 地址、連線時長、以 dBm 和條形圖表示的訊號水平）。

### 網際網路 {#internet}

使用標註來區分網際網路連線和你的本地網路：

1. **地址獲取** - 如果提供商透過 DHCP 提供地址，請選擇 **Automatic**；如果提供固定地址詳細資訊，請選擇 **Static**；如果提供 PPPoE 使用者名稱和密碼，請選擇 **PPPoE**。輸入提供商提供給你的詳細資訊；不要複製截圖中的地址。
2. **防火牆路由器** - 對於將家庭網路連線到網際網路的路由器，請啟用此項。
3. **本地網路 > IP 地址** - 這是路由器在你 LAN 上的地址，與 **網際網路** 部分中的地址不同。
4. **DHCP 伺服器 / NAT** - 對於典型的家用路由器，啟用 DHCP 伺服器以為 LAN 用戶端分配地址，並啟用 NAT 以讓它們共享網際網路連線。

![WinBox Quick Set Internet and Local Network settings with arrows to Address Acquisition, Firewall Router, the LAN IP address, and DHCP Server and NAT](/img/ac3ae884f0c552e9.webp)

截圖選中了 **Automatic**，因此網際網路 IP 地址、子網掩碼和閘道器由上游 DHCP 伺服器提供。未勾選的選項屬於此現有配置，而不是針對家用路由器的建議設定。

- **埠**：選擇哪個埠連線到 ISP（網際網路）調變解調器。通常是 Eth1。
- **地址獲取**：選擇 ISP 如何向您提供 IP 地址。請向您的服務提供商諮詢此選項以及其他選項（IP 地址、子網掩碼、閘道器）。
- **MAC 地址**：通常不應更改，除非您的 ISP 已將您繫結到特定 MAC 地址，並且您已將路由器更換為新路由器。
- **路由器防火牆**：這會為您的路由器和網路啟用安全防火牆。請始終確保選中此複選框，以免從網際網路埠訪問您的裝置。
- **MAC 伺服器 / MAC Winbox**：允許從 LAN 埠側以 MAC 地址模式使用 [Winbox 實用工具](https://mt.lv/winbox) 進行連線。當 IP 模式不可用時，可用於偵錯和恢復。僅供高階使用者使用。
- **發現**：允許其他 RouterOS 裝置透過型號名稱識別此裝置。

### 本地網路 {#local-network}

- **IP 地址**：大多數情況下可以保留預設值 192.168.88.1，除非你的路由器位於另一臺路由器之後。為避免 IP 衝突，請更改為 192.168.89.1 或類似地址。
- **子網掩碼**：大多數情況下可以保留 255.255.255.0。
- **橋接所有 LAN 埠**：允許你的裝置相互通訊，即使例如你的電視透過乙太網 LAN 線纜連線，而你的 PC 透過 WiFi 連線。
- **DHCP 伺服器**：通常，你希望家庭網路中使用自動 IP 地址配置，因此請將 DHCP 設定保持為 ON 並保留其預設值。
- **NAT**：僅當你的 ISP 為路由器和本地網路都提供了公網 IP 地址時，才將其關閉。否則，請保持 NAT 開啟。
- **UPnP**：此選項會為受支援的程式和裝置（例如你的 NAS 磁碟和點對點實用程式）啟用自動埠轉發（有些人稱之為“向本地網路開放埠”）。請謹慎使用，因為此選項有時會在你不知情的情況下將內部裝置暴露到網際網路。僅在特別需要時啟用。

### VPN {#vpn}

如果你想從網際網路訪問你的本地網路（以及你的路由器），請使用安全的 VPN 隧道。此選項會為你提供一個用於連線的域名，並啟用 [PPTP](../virtual-private-networks/pptp.md) 和 [L2TP/IPsec](../virtual-private-networks/l2tp/index.md)（推薦後者）。使用者名稱是 'vpn'，你可以指定自己的密碼。你只需在此處啟用它，然後在筆記型電腦或手機上提供地址、使用者名稱和密碼；連線到 VPN 後，你就能與家庭網路建立安全加密的連線。旅行時也很有用——你可以像從家中連線一樣，透過安全線路瀏覽網際網路。這也有助於避開某些國家/地區設定的地理限制。

### 系統 {#system}

- **檢查更新**：開啟 RouterOS 更新對話方塊以檢查是否有更新的版本，並選擇何時安裝。
- **密碼...**：設定路由器的管理員密碼。這會保護對路由器配置的訪問，並且與 **WiFi 密碼** 不同。

檢視無線、網際網路和 LAN 設定後，選擇 **確定** 儲存並關閉 Quick Set，或選擇 **應用** 儲存並保持視窗開啟。更改 LAN IP 地址可能會斷開基於 IP 的 WinBox 會話；請使用新地址重新連線到路由器。更改 Wi-Fi 後，請使用新的網路名稱和密碼重新連線無線裝置。

普通設定期間不要動 **重設配置**：它會重設路由器配置，而不是儲存你的編輯。

## 常見問題 {#faq}

### 問：Quickset 與 Webfig 標籤頁有何不同？在 Webfig 標籤頁中會出現許多新選單。 {#q-how-is-quickset-different-from-the-webfig-tab-where-a-bunch-of-new-menus-appear}

答：QuickSet 適合只需要讓裝置快速啟動並執行的新使用者。它在一個地方提供最常用的選項。如果你需要更多選項，請完全不要使用任何 QuickSet 設定；選擇 "Webfig" 開啟高階配置介面。完整功能將解鎖。

### 問：我可以同時使用 Quickset 和 Webfig 嗎？ {#q-can-i-use-quickset-and-webfig-together}

答：如果您打算使用 Quickset，就只使用 Quickset，反之亦然。雖然可以透過這種方式配置不衝突的設定，但不建議混用這些選單。Router 模式和 Bridge 模式有什麼區別？Bridge 模式會將所有介面加入網橋，允許轉發二層封包（充當集線器/交換器）。在 Router 模式下，封包透過使用 IP 地址和 IP 路由在三層轉發（充當路由器）。

### 問：在 HomeAP 模式下，2GHz 和 5GHz 網路名稱應該相同還是不同？ {#q-in-homeap-mode-should-the-2ghz-and-5ghz-network-names-be-the-same-or-different}

答：如果你希望所有用戶端裝置（如電視、手機、遊戲主機）自動選擇最合適的網路，請將名稱設為相同。如果你想強制用戶端裝置使用更快的 5GHz 802.11ac 連線，請將名稱設為唯一。

### 問：我可以建立無安全設定的 AP（無密碼），或在使用 QuickSet 時連線到這樣的 AP 嗎？ {#q-can-i-create-an-ap-without-security-settings---no-password-or-connect-to-such-ap-while-using-quickset}

答：QuickSet 預設使用 WPA2 預共享金鑰。這意味著最小密碼長度為 8 個字元，並且裝置只能連線到受 WPA2 保護的 AP，或本身作為 AP 使用。對於無安全設定的配置，你需要使用 WinBox、Webfig 或控制檯手動配置。
