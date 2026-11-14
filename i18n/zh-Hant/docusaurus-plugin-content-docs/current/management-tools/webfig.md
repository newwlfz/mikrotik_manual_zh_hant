---
sidebar_key: "management-tools/webfig"
sidebar_position: 1
title: "WebFig"
sidebar_label: "WebFig"
description: "WebFig 是一種基於 Web 的 RouterOS 實用工具，無需額外軟體即可進行監控、配置和故障排除。它支援帶證書管理的 HTTPS，包括萬用字元證書，並透過 SSL/TLS 為路由器配置提供安全訪問。"
tags:
  - 'webfig'
  - 'https'
  - 'terminal'
source: https://manual.mikrotik.com/docs/management-tools/webfig
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

WebFig 是一個基於 Web 的 RouterOS 管理工具，可用於配置、監控和排查路由器故障。它作為 WinBox 的替代方案，提供相似的佈局，並且幾乎可以訪問所有 RouterOS 功能。

作為一個平臺無關的工具，WebFig 可用於從任何帶 Web 瀏覽器的裝置管理路由器，無需安裝平臺專用軟體。

WebFig 支援三項主要功能：

- 配置 - 檢視和修改當前路由器配置。
- 監控 - 監控路由器狀態、路由資訊、介面統計資訊、日誌及其他執行資料。
- 故障排查 - 訪問並使用內建的 RouterOS 診斷工具，如 Ping、Traceroute、Packet Sniffer、Traffic Generator 等。

## 連線到路由器 {#connecting-to-a-router}

如 [首次配置](../getting-started/first-time-configuration.md) 部分所述，預設情況下可使用使用者名稱 **admin** 以及無密碼或裝置標籤上提供的預設密碼（取決於型號）訪問裝置。開啟 Web 瀏覽器，在位址列中輸入裝置 IP 地址；預設地址為 `192.168.88.1`。確保管理裝置配置了同一子網中的 IP 地址（例如 `192.168.88.2`），否則三層連通性將無法正常工作。

![](/img/0f36f8d8724f2e8b.png)

## 啟用 HTTPS {#enable-https}

WebFig 通常僅從本地網路使用：預設情況下，防火牆會阻止 WAN 埠上的路由器 Web 服務，你透過路由器的 LAN 地址（例如 `192.168.88.1`）訪問路由器。啟用 HTTPS 會加密此管理流量，從而避免憑據和配置以明文形式在 LAN 中傳輸。

使用哪種證書取決於你訪問路由器的方式：

- **透過其 LAN IP 地址或內部主機名（常見情況）** — 使用在路由器上生成的自簽名證書。公共證書頒發機構無法為 `192.168.88.1` 等私有地址簽發證書，因此這是預設做法。
- **透過真實的公共域名** — 你可以使用 Let's Encrypt 簽發的公開受信任證書，從而避免瀏覽器警告，而無需分發 CA。僅當你實際使用該域名開啟 WebFig 時這才有幫助，因此它主要適用於透過公共名稱而非 LAN IP 管理的路由器（將在下一節中介紹）。

### 使用自簽名證書 {#use-a-self-signed-certificate}

自簽名證書會立即加密連線。瀏覽器在首次使用時不會信任它，但你可以透過匯出路由器的根 CA，並將其匯入用於管理該路由器的計算機的受信任儲存中，來消除警告。

:::tip
WebFig 支援萬用字元證書。你可以透過在 common-name 屬性中指定萬用字元來生成一個，例如 `common-name=*.mikrotik.com`。
:::

要生成你自己的證書並啟用 HTTPS 訪問，必須配置以下內容：

#### 在路由器上建立你自己的根 CA 併為其簽名 {#create-your-own-root-ca-on-the-router-and-sign-it}

```ros
[admin@MikroTik] > certificate add name=local-cert common-name=local-cert key-usage=key-cert-sign,crl-sign 
[admin@MikroTik] > /certificate/sign local-cert 
  progress: done
```

:::warning
如果你已有證書頒發機構，或正在使用外部服務簽發證書，請在外部建立並簽署證書，然後再將其匯入路由器。匯入證書時，請確保將其標記為受信任。
:::

#### 為 WebFig 建立證書（終端實體證書） {#create-a-certificate-for-webfig-end-entity-certificate}

```ros
[admin@MikroTik] > certificate add name=WebFig common-name=192.168.88.1
[admin@MikroTik] > certificate sign WebFig 
  progress: done
```

證書列表示例：

```ros
[admin@MikroTik] > /certificate/print
Flags: K - private-key; A - authority; T - trusted
Columns:NAME        COMMON-NAME     FINGERPRINT                                                     
0  KAT  local-cert  local-cert      9b6363d033c4b2e6893c340675cfb8d1e330977526dba347a440fabffd983c5d
1  KAT  WebFig      192.168.88.1    9f84ac2979bea65dccd02652056e5559bcdf866f8da5f924139d99453402bd02
```

#### 啟用 HTTPS 服務並分配證書 {#enable-the-https-service-and-assign-the-certificate}

```ros
[admin@MikroTik] > /ip/service/set www-ssl certificate=WebFig disabled=no
```

現在你可以透過 **`https://192.168.88.1`** 訪問 WebFig。

:::warning
大多數 Web 瀏覽器預設不信任自簽名證書，因此首次連線時你需要接受警告或手動信任該證書。或者，匯出根 CA 證書並將其匯入作業系統或瀏覽器的信任儲存。瀏覽器維護自己的信任儲存，這可能與作業系統的信任儲存不同——在作業系統級別信任該證書可能不會影響瀏覽器。
:::

### 使用公共受信任證書（Let's Encrypt） {#use-a-publicly-trusted-certificate-lets-encrypt}

如果你透過真實的公共域名而非 LAN IP 訪問路由器，你可以使用來自 [Let's Encrypt](https://letsencrypt.org/) 的瀏覽器受信任證書，並跳過分發根 CA。RouterOS 為此包含內建的 [ACME 用戶端](../authentication-authorization-accounting/certificates.md#acme-client)。

在選擇此選項之前，請注意它與僅 LAN 環境如何相互影響：

- 公共 CA 不會為私有 IP 地址簽發證書，因此當你透過 `https://192.168.88.1` 開啟 WebFig 時，這 **不會** 消除警告。
- 證書僅對其域名有效，因此你必須透過該名稱瀏覽 WebFig。要使該名稱在 LAN 內解析到路由器，通常需要一條指向 LAN 地址的本地（分離解析）DNS 記錄。
- DNS-01 挑戰——用於 [雲](../network-management/cloud/index.md#ddns) `<id>.sn.mynetname.net` 名稱——不需要入站 WAN 埠，因此即使防火牆阻止來自 WAN 的 WebFig 訪問，它仍然可以工作。

為路由器的 IP Cloud DDNS 名稱請求證書：

```ros
/ip/cloud/set ddns-enabled=yes
/certificate/add-acme domain-names=[/ip/cloud/get dns-name]
```

或為你的自有域名請求證書：

```ros
/certificate/add-acme domain-names=router.example.com
```

簽發的證書以該域名命名，並在 `/certificate/print` 中帶有 `a`（acme-manage）標誌顯示。將其分配給 `www-ssl` 服務，然後透過該域名開啟 WebFig：

```ros
/ip/service/set www-ssl certificate=router.example.com disabled=no
```

有效期過去 80% 後，證書會自動續期。

## 終端 {#terminal}

WebFig 中的 **終端**（命令列介面，CLI）位於右上角。它提供與 WinBox 介面中的 New Terminal 相同的功能。

![WebFig Terminal](/img/98cf6c711e22f464.png)

## 皮膚 {#skins}

WebFig **Design Skin** 是一個用於自定義介面外觀以提升易用性的工具。它不是安全功能。具有足夠許可權的使用者仍可透過其他方式訪問所有可用的配置選項，包括直接 CLI 訪問。

### 設計皮膚 {#designing-skins}

如果使用者具有足夠許可權（使用者組啟用了 `policy` 和 `sensitive` 策略），則 **Design Skin** 按鈕可用。啟用此選項會開啟介面自定義工具。

要限制對 **Design Skin** 選單的訪問，請在使用者組配置中停用 `policy` 和 `sensitive` 許可權。

**可用操作：**

![](/img/0a00e206cc7f6a8f.png)

- **隱藏選單** - 隱藏一個選單及其所有子選單。
- **隱藏子選單** - 隱藏特定子選單。
- **隱藏標籤頁** - 隱藏多標籤頁檢視中的各個標籤頁。
- **重新命名選單和專案** - 更改選單標籤，例如用於本地化或提高畫質晰度。
- **向專案添加註釋** - 在詳細檢視中添加註釋。
- **將專案設為只讀** - 為防止誤操作，阻止編輯所選欄位。
- **隱藏標誌** - 在列表檢視和詳細檢視中隱藏標誌。

![](/img/c8c244ccc36e3ad3.png)

- **新增欄位限制** - 限制詳細檢視中允許的值：
  - **數值區間 (..)** - 定義允許的範圍，例如為 **MTU** 等數值欄位定義 `1..10`。
  - **欄位字首限制** - 限制基於文字的欄位允許的字首。末尾的 `$` 會強制精確字首匹配。例如，`station$` 僅允許值為 **station**。

  ![](/img/a1d18d4f6156955e.png)

- **新增標籤頁** - 在欄位前插入帶標籤的分節符。
- **新增分隔符** - 在欄位前插入水平分隔符。

:::note
數值區間不能超出 RouterOS 為給定欄位定義的限制。
:::

:::note
集合欄位表示可選選項的集合（複選框集合），例如使用者組策略或 RADIUS 服務設定。
:::

:::note
應用於組合框欄位的限制也會限制可用的下拉選項。
:::

### 皮膚設計示例 {#skin-design-example}

要將使用者限制為特定服務，請向 RADIUS Service 欄位新增限制。

![](/img/b8b4b60798134f4d.webp)

生成的配置僅允許 **Limit** 欄位中指定的服務。

![](/img/c39baa1a2067052d.webp)

![](/img/0ff4ec2dab43d50b.webp)

### 自定義皮膚 {#customizing-skins}

可在此處獲取一個可用於皮膚 `*.json` 檔案的 **Status page** 結構示例：[status_main_example.json](pathname:///assets/297795616_status_main_example.json)

狀態內容遵循以下結構：
`{"Status": {"Status": {}}}`

狀態記錄按順序顯示，例如：

```json
"7": {
  "alias": (path to the record),
  "note": (optional; free form text that appears under the record),
  "name": (optional; alternative name for the record),
  "tab": (optional; name of the tab that this and following records belong to),
  "separator": 1 (optional; should a separating line be placed before this record)
},
```

**路徑（別名）結構**

別名路徑（例如：**`"IP:Firewall:Filter Rules:*17:Statistics:Packet Rate Graph"`** 以及對應的 URL：`"router_IP/WebFig/#IP:Firewall.Filter_Rules.17"`）由以冒號分隔的元件組成：

- **組**（如果有）→ `IP:`
- **服務或名稱** → `Firewall:`
- **容器或標籤頁名稱** → `Filter Rules:`
- **星號 (\*) 和物件 ID** → 取自開啟項的 URL（例如 `17`）
- **標籤頁名稱**（如果適用）→ `Statistics`
- **欄位名稱** → `Packet Rate Graph`

![](/img/b164bc74026476ff.png)

### 使用皮膚 {#using-skins}

要應用皮膚，請將其分配給使用者組。分配後，該組中的所有使用者在登入 WebFig 或 WinBox 時都會自動使用所選皮膚。

```ros
/user/group/set your_group_name skin=your_skin
```

要在另一臺路由器上使用皮膚，請將皮膚檔案複製到目標裝置上的 skins 目錄中。複製後，將該皮膚分配給該路由器上的使用者組以啟用它。
