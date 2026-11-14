---
sidebar_key: "containers/user-guides/container-thingsboard-mqtt-http-server"
sidebar_position: 8
title: "容器 - ThingsBoard MQTT/HTTP 伺服器"
sidebar_label: "容器 - ThingsBoard MQTT/HTTP 伺服器"
description: "本頁介紹 MikroTik RouterOS 中的容器功能，使使用者能夠直接在路由器上執行諸如 ThingsBoard MQTT/HTTP IoT 平臺之類的伺服器。它說明了如何配置容器模式、網路介面（veth 和 bridge）、出站流量的 NAT 規則以及儲存要求。本指南強調了 RAM/磁碟空間方面的注意事項，並提供了使用 ThingsBoard 部署的示例，搭配"
tags:
  - 'container'
  - 'thingsboard'
  - 'mqtt'
source: https://manual.mikrotik.com/docs/7.25/containers/user-guides/container-thingsboard-mqtt-http-server
captured_at: '2026-11-04T11:15:12+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

將容器功能引入 RouterOS 後，就可以在路由器內執行各種用於各類任務的伺服器。這對於希望減少網路中裝置數量的人尤其有用。與其在單獨的裝置/機器上執行伺服器，何不直接在路由器內執行它呢？

許多使用者需要一個能夠收集資料、儲存資料並以易於理解的方式顯示資料的伺服器。這時，像 [ThingsBoard](https://thingsboard.io/) 這樣的平臺就可以派上用場。

它主要定位為 IoT 平臺，你可以在[連結](https://thingsboard.io/iot-use-cases/)中找到他們演示的各種用例。

從 RouterOS 使用者的角度來看，最吸引人的部分是它可以被用作 MQTT 伺服器（MQTT broker）或 HTTP 伺服器，這意味著你可以使用 [MQTT publish](../../internet-of-things/mqtt/index.md) 或 [HTTP POST](../../system-information-and-utilities/fetch.md) 來發布資料。你可以透過[此處](https://thingsboard.io/docs/reference/mqtt-api/)的連結找到 ThingsBoard MQTT API 指南，並透過[此處](https://thingsboard.io/docs/reference/http-api/)的連結找到 HTTP API。

簡而言之，你可以利用[指令碼](../../developer-guides/scripting/index.md)收集 RouterOS 統計資訊（如 uptime、GPS 座標、封包統計，以及幾乎任何你列印到終端中的其他內容），然後將這些資訊儲存到變數中，並用這些變數構造一條 JSON 訊息。然後你可以透過[排程器](../../system-information-and-utilities/scheduler.md)（它會在你需要時執行此指令碼）使用 MQTT 或 HTTP post 將此訊息傳送到 ThingsBoard。你可以在[本指南](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md)中找到實現此功能的基礎指令碼示例。

ThingsBoard 會藉助[小部件](https://thingsboard.io/docs/user-guide/ui/widget-library/)儲存並顯示資料，你可以使用這些部件來幫助設定儀表板，以圖表、表格、地圖和其他方式視覺化資料。

例如，下面提到有 2 種可用的 ThingsBoard 例項選項，它們各自使用不同的資料庫：

- [thingsboard/tb-postgres](https://hub.docker.com/r/thingsboard/tb-postgres/)
- [thingsboard/tb-cassandra](https://hub.docker.com/r/thingsboard/tb-cassandra/)

你可以在 ThingsBoard/docker 文件中找到更多資訊。

在我們的示例中，我們將展示 **tb-postgres**——一個用於測試目的的、帶有 PostgreSQL 資料庫的單個 ThingsBoard 例項。

本指南將展示 "in-memory" 佇列型別的服務，但對於生產環境，請考慮使用其他服務型別。你可以在[此處](https://thingsboard.io/docs/user-guide/install/docker/)找到更多資訊。

## 概述 {#summary}

**子選單：** `/container`

***注意**:* **container** 包是必需的。

低於 v7.8 的 RouterOS 版本將無法執行此場景。

在繼續配置之前，請務必閱讀我們的 [容器](../index.md) 指南。請務必檢視[免責宣告](../index.md#disclaimer)和[要求](../index.md#requirements)部分，以瞭解所有風險以及你可能需要執行的必要步驟。

在此示例中，我們將在 [雲託管路由器，CHR](../../getting-started/routeros-licensing/chr/index.md) 上執行它。

在本指南釋出時，**thingsboard/tb-postgres** 映象**僅**適用於 linux/**arm64** 和 linux/**amd64** 作業系統/架構。這意味著你無法在採用 arm32 位架構的 RouterOS 裝置上執行此場景。

有幾個引數需要注意：

- 你需要明白它是一個**伺服器**，因此你需要為儲存在那裡的資料和映象本身預留額外空間。在我們的測試中，8 GB 磁碟空間已經足夠，但是！對於實際應用，你可能需要考慮增加更多空間，尤其是當你計劃執行更多容器時。只需記住 → 留有儲備可能更好。
- 與磁碟空間一樣，RAM 記憶體也很重要。根據 ThingsBoard 文件，在使用帶有 PostgreSQL 資料庫的單個 ThingsBoard 例項時，建議至少分配 1GB 的 RAM，並使用最小負載（每秒幾條訊息）。建議使用 2-4GB RAM。換句話說，如果你想在 RouterBoard 裝置上執行它，請理解，在 RAM 少於 1 GB 的裝置上可能無法實現。這就是為什麼 → 要考慮使用具有更多可用 RAM 記憶體的裝置。

請轉到[提示和技巧](../index.md#tips-and-tricks)部分，瞭解如何限制 RAM。

## 配置 {#configuration}

### 容器模式 {#container-mode}

啟用容器模式：

```ros
/system/device-mode/update container=yes
```

如果要在 X86 上使用 container，你需要透過按下復位按鈕或冷重啟來確認 device-mode。

### 網路 {#networking}

為容器新增 veth 介面

```ros
/interface/veth/add name=veth1 address=172.18.0.2/24 gateway=172.18.0.1
```

為容器建立網橋，為其分配 IP 網路，並將 veth 新增到網橋

```ros
/interface/bridge/add name=dockertb
/ip/address/add address=172.18.0.1/24 interface=dockertb
/interface/bridge/port/add bridge=dockertb interface=veth1
```

為出站流量設定 NAT

```ros
/ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.18.0.0/24
```

轉發 TCP 9090 以用於 HTTP 管理（根據 ThingsBoard 文件，這是預設 HTTP 埠）

:::warning

我們建議僅在本地測試或透過 VPN 訪問時使用 HTTP 訪問（當你確定本地網路安全時）。

當你希望從網際網路（從公共網路/WAN）訪問容器 WEB 管理介面時，請改為考慮使用 **HTTPS**。

:::

```ros
/ip/firewall/nat/add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=9090 protocol=tcp to-addresses=172.18.0.2 to-ports=9090
```

在上方 DNAT（dst-nat）規則中顯示的 `dst-address` 欄位裡，我們使用裝置的本地 IP 地址。首先，**使用本地 IP**（本地訪問）**來** **完成所有設定** **並** **確認一切正常**。

:::info

在完成本指南中展示的其餘步驟並驗證 ThingsBoard 管理門戶可在本地正常工作後 →  **進一步保護設定**：

- (a) 確保所有預設 ThingsBoard 使用者憑據都已更改/刪除，並已實施強密碼（參考 ThingsBoard 文件）；
- (b) **啟用** **HTTPS**（步驟將在本指南後面說明）；
- (c) 最好將 HTTPS 埠更改為非標準埠（參考 ThingsBoard 文件）。

只有當你提高了安全性，並且只有到那時 → 你才可以考慮啟用來自 WAN 的遠端訪問（在上方示例中，在 `dst-address` 欄位中使用你的公網 IP 地址，而不是本地 IP）。此外，為了進一步提高安全性，請使用 `src-address` 或 `src-address-list` 引數，你可以在其中輸入受信任的公網源 IP 地址（已知/受信任地址的列表，例如屬於你的分支機構、你也希望從那裡訪問伺服器的地址）。請理解，只有你需要對安全性負責。如果你留了一扇門開著，就可能有人利用它。在設定此類場景時，你需要具備網路知識並瞭解風險。
:::

轉發 TCP 1883 以用於非 SSL MQTT（根據 ThingsBoard 文件，這是預設 MQTT 埠）

:::warning
我們建議僅在本地測試或透過 VPN 訪問時使用非 SSL MQTT（TCP 1883）通訊（當你確定本地網路安全時）。
>
在實際應用中，當涉及從網際網路（從公共網路）訪問時，請考慮使用 **SSL MQTT（TCP 埠 8883）**，而不是非 SSL MQTT（TCP 埠 1883）。如果使用非 SSL MQTT，用戶端（MQTT publisher）與伺服器（MQTT broker）之間的通訊很容易被嗅探/抓包，從而洩露認證資料（如 client-ids、使用者名稱和密碼）。
:::

```ros
/ip/firewall/nat/add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=1883 protocol=tcp to-addresses=172.18.0.2 to-ports=1883
```

與 HTTP 訪問一樣，在上方 DNAT（dst-nat）規則中顯示的 `dst-address` 欄位裡，我們使用裝置的本地 IP 地址。首先，**使用本地 IP**（本地訪問）**來** **完成所有設定** **並** **確認一切正常**。

:::info
在完成本指南中展示的其餘步驟並驗證 ThingsBoard 非 SSL MQTT 通訊可在本地正常工作後 →  **進一步保護設定**：
>
- (a) 考慮從 ThingsBoard 安裝中移除模板裝置；
- (b) **啟用 SSL MQTT**（步驟將在本指南後面說明）；
- (c) 最好將 MQTT 埠更改為非標準埠（參考 ThingsBoard 文件）。
>
啟用 SSL MQTT 後，你可以考慮從 WAN 開放 TCP 8883（這是預設 SSL MQTT 埠）（在 `dst-address` 欄位中使用你的公網 IP 地址而不是本地 IP，並將 `dst-port` 和 `to-ports` 從 1883 改為 8883）。此外，為了進一步提高安全性，請使用 `src-address` 或 `src-address-list` 引數，你可以在其中設定受信任的公網 IP 地址列表。這樣，只有已配置的受信任 IP 才能與 ThingsBoard broker 建立 MQTT 連線。
:::

### 環境變數和掛載 {#environment-variables-and-mounts}

請檢視 [docker-thingsboard](https://hub.docker.com/r/thingsboard/tb-postgres) 文件，瞭解需要新增的確切掛載和變數。

#### 環境變數 {#environment-variables}

```ros
/container/envs/add list=tb_envs key=TB_QUEUE_TYPE value="in-memory"
```

#### 掛載 {#mounts}

```ros
/container/mounts/add list=mytb-data src=tb/mytb-data dst=/data
/container/mounts/add list=mytb-logs src=tb/mytb-logs dst=/var/log/thingsboard
```

### 獲取映象 {#getting-image}

為簡化配置，我們將從外部映象庫獲取映象，但你也可以透過 [.tar](../index.md#option-b-import-image-from-pc) 檔案匯入它。

確保已相應設定 "Registry URL"，限制 RAM 使用量（如有必要），併為映象設定目錄。

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=pull ram-high=2048.0MiB
```

拉取映象：

```ros
/container/add remote-image=thingsboard/tb-postgres:latest interface=veth1 root-dir=ThingsBoard mountlists=mytb-data,mytb-logs envlists=tb_envs logging=yes
```

執行該命令後，RouterOS 應開始“解壓”軟體包。檢查“File System”中新建的資料夾，並使用命令 `/container/print` 監控容器狀態。

### 啟動容器 {#starting-the-container}

在使用 `/container/print` 確認容器已新增且狀態變為 `status=stopped` 後，即可啟動它：

```ros
/container/start 0
```

等待幾分鐘，讓容器完全載入。

## 驗證 {#verification}

### 管理訪問 {#management-access}

容器啟動並安裝完成後，使用任意瀏覽器訪問 → [http://192.168.88.1:9090](http://192.168.88.1:9090)（其中 IP 地址是 DNAT 規則中使用的地址）：

![](/img/12a1fc50b164a5ac.webp)

預設憑據為（使用者名稱/密碼）：

- **系統管理員**：sysadmin@thingsboard.org / sysadmin
- **租戶管理員**：tenant@thingsboard.org / tenant

登入提示應能確認伺服器正在執行。

### MQTT 測試 {#mqtt-test}

使用 **tenant** 登入並建立一個新裝置。轉到 "**Devices**" 選單，點選 "**+**"（Add Device）按鈕，然後選擇 "**Add new device**" 選項：

![](/img/a0ac782ef9f067db.webp)

 隨心命名，然後點選 "**Add**"：

![](/img/2b65a6517ea2dacf.webp)

點選你剛建立的裝置並選擇 "**Manage credentials**" 設定，以檢查你的裝置訪問令牌（複製生成的訪問令牌或輸入你自己的 →  "YOUR\_TOKEN"）：

![](/img/467d0a4699b4dba5.webp)

完成這些步驟後，轉到 RouterOS 設定（回到 CHR 設定），並建立一個新的 [MQTT broker](../../internet-of-things/mqtt/index.md)（**確保已安裝 IoT 包**，否則你將沒有此選單）：

```ros
/iot/mqtt/brokers/add name=tb address=172.18.0.2 port=1883 username=YOUR_TOKEN
```

以 JSON 格式釋出一條靜態測試 MQTT 訊息：

```ros
/iot/mqtt/publish broker="tb" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

確認訊息已釋出：

![](/img/d80bd832e0a7483f.webp)

## 啟用 HTTPS 和 SSL MQTT {#enabling-https-and-ssl-mqtt}

預設情況下，使用 HTTP 和 MQTT 協定。如前面“網路”部分所述，使用非 SSL HTTP 和非 SSL MQTT 並不是很安全（除非它們在受到嚴格保護、具有配置良好的防火牆/受限訪問的網路中使用），並且**我們建議啟用 HTTPS**和**SSL MQTT**。

請檢視 ThingsBoard 文件以獲取更多資訊 → [HTTP over SSL](https://thingsboard.io/docs/user-guide/ssl/http-over-ssl/) 和 [MQTT over SSL](https://thingsboard.io/docs/user-guide/mqtt-over-ssl/) 指南。

首先，沒有證書就沒有 SSL，因此需要生成（或購買）一個證書。

簡而言之，本節將演示如何為 HTTPS 和 SSL MQTT 生成自簽名證書。然後，你需要將它們上傳到 ThingsBoard 安裝中的正確資料夾，並相應地修改 ThingsBoard 配置檔案。

在本指南中，我們將使用 RouterOS 生成這兩個[證書](../../authentication-authorization-accounting/certificates.md)（但你也可以使用 OpenSSL 或你想要的任何其他工具）。

### 建立證書 {#create-certificates}

為 HTTPS 建立證書：

```ros
/certificate/add name=TBhttps common-name=172.18.0.2
/certificate/sign TBhttps
```

為 MQTT 建立證書：

```ros
/certificate/add name=TBmqtt common-name=172.18.0.2
/certificate/sign TBmqtt
```

使用 `/certificate/print` 命令確認它們已新增：

```ros
[admin@MikroTik] > /certificate/print
Flags: K - PRIVATE-KEY; A - AUTHORITY; T - TRUSTED
Columns: NAME, COMMON-NAME, FINGERPRINT
#     NAME     COMMON-NAME  FINGERPRINT                                                     
0 KAT TBhttps  172.18.0.2   863f4547c74ce3ec70c3e82172502711517b52bbc055d18c24ba4aafec46152c
1 KAT TBmqtt   172.18.0.2   ebf3ff5d03ed4cc73546e058da9bc414cdaf24ce45da29b203348045fbbd21ae
```

使用 PKCS12 格式匯出證書，併為它們設定密碼/口令：

```ros
/certificate/export-certificate file-name=keystore export-passphrase=thingsboard_cert_password type=pkcs12 numbers=0
/certificate/export-certificate file-name=mqttserver export-passphrase=thingsboard_mqttcert_password type=pkcs12 numbers=1
```

使用你自己的 `export-passphrase` 並記住它。

上述命令的輸出將建立證書檔案 **keystore.p12** 和 **mqttserver.p12**，你可以從 "[File List](../../system-information-and-utilities/files.md)" 選單下載它們：

```ros
[admin@MikroTik] > /file/print 
Columns: NAME, TYPE, SIZE, CREATION-TIME
 #  NAME                 TYPE             SIZE       CREATION-TIME       
 0  tb/mytb-data         container store             2023-01-19 13:43:16
 1  container-log.0.txt  .txt file        2240.5KiB  2023-01-27 15:37:41
 2  skins                directory                   2023-01-18 15:12:22
 3  tb/mytb-logs         container store             2023-01-27 12:24:30
 4  pull                 directory                   2023-01-19 13:41:01
 5  pub                  directory                   2023-01-18 16:15:29
 6  tb                   directory                   2023-01-23 15:46:39
 7  tb/data              container store             2023-01-18 16:50:08
 8  tb/logs              container store             2023-01-18 16:50:08
 9  mqttserver.p12       .p12 file        2438       2023-01-27 15:36:26
10  keystore.p12         .p12 file        2448       2023-01-27 15:08:07
11  ThingsBoard          container store             2023-01-19 13:40:50
```

將這兩個檔案從路由器下載到你 PC 上的任意目錄。例如，我們將它們下載到了 `C:\Users\Admin\Desktop\ThingsBoard` 資料夾中。

### 下載 ThingsBoard 的配置檔案 {#download-the-thingsboards-configuration-file}

開啟命令終端（Windows 使用者以管理員身份開啟 "CMD"，Linux 使用者開啟 "Linux Shell or Command Terminal"），並導航到證書所在的目錄：

```powershell
C:\Windows\System32>cd c:\Users\Admin\Desktop\ThingsBoard
C:\Users\Admin\Desktop\ThingsBoard>dir
Directory of C:\Users\Admin\Desktop\ThingsBoard

27.01.2023  15:36    <DIR>          .
27.01.2023  15:36    <DIR>          ..
27.01.2023  15:09             2 448 keystore.p12
27.01.2023  15:36             2 434 mqttserver.p12
               2 File(s)          4 882 bytes
               2 Dir(s)  51 380 154 368 bytes free
```

在此目錄中，你需要透過 SFTP 連線到路由器的 IP（SFTP 允許你使用 SSH 協定傳輸檔案，因此你需要事先確保已啟用 [SSH 服務](../../system-information-and-utilities/services.md)）：

```powershell
c:\Users\Admin\Desktop\ThingsBoard>sftp admin@192.168.88.1
The authenticity of host '192.168.88.1 (192.168.88.1)' can't be established.
RSA key fingerprint is SHA256:/WmmZErqWL51SOlS4EaGvSQ0i4HPnSIHCEjnc8AmP2c.
Are you sure you want to continue connecting (yes/no/[fingerprint])?yes
admin@192.168.88.1's password:
Connected to 192.168.88.1.
sftp>
```

在容器執行時，轉到 ThingsBoard 配置檔案資料夾（使用 `dir` 或 `ls` 命令檢視當前資料夾內容，使用 `cd` 命令轉到我們選擇的資料夾）。預設情況下，它應該是包含 "**thingsboard.yml**" 配置檔案的資料夾。在我們的示例中，我們可以在以下位置找到它：

```powershell
sftp> cd ThingsBoard/usr/share/thingsboard/conf

sftp> dir

banner.txt          i18n                logback.xml         templates           thingsboard.conf    thingsboard.yml     
```

使用 `get` 命令下載 "**thingsboard.yml**" 配置。這會將預設 ThingsBoard 配置檔案下載到你的機器（到你啟動 SFTP 時的目錄）：

```powershell
sftp> get thingsboard.yml
Fetching /ThingsBoard/usr/share/thingsboard/conf/thingsboard.yml to thingsboard.yml
/ThingsBoard/usr/share/thingsboard/conf/thingsboard.yml                               100%   67KB   2.0MB/s   00:00
sftp> quit

c:\Users\Admin\Desktop\ThingsBoard>dir
 Directory of c:\Users\Admin\Desktop\ThingsBoard

30.01.2023  10:59    <DIR>          .
30.01.2023  10:59    <DIR>          ..
27.01.2023  15:09             2 448 keystore.p12
27.01.2023  15:36             2 434 mqttserver.p12
30.01.2023  10:59            68 846 thingsboard.yml
               3 File(s)         73 728 bytes
               2 Dir(s)  50 901 626 880 bytes free
```

### 修改 ThingsBoard 的設定 {#alter-the-thingsboards-settings}

使用你偏好的文字編輯器（notepad 或任何其他編輯器）開啟 "**thingsboard.yml**"，並修改幾行。你可以備份此檔案，並以不同名稱儲存，以便在配置錯誤時擁有預設設定的副本。

#### HTTPS 相關設定 {#https-related-settings}

1. 啟用 SSL →  將 "SSL\_ENABLED:**false**" 改為 "SSL\_ENABLED:**true**"。
2. 更改憑據型別 → 從 "SSL\_CREDENTIALS\_TYPE:**PEM**" 改為 "SSL\_CREDENTIALS\_TYPE:**KEYSTORE**"。
3. 更改路徑 → 從 "SSL\_KEY\_STORE:**classpath:keystore/keystore.p12**" 改為 "SSL\_KEY\_STORE:**keystore.p12**"（可選）。
4. 停用 key alias 設定 → 將其註釋掉 → 只需在 `key_alias: "${SSL_KEY_ALIAS:tomcat}"` 行前放置 "**#**" 符號。
5. 輸入你在 RouterOS 中使用的自己的證書密碼 → 將 "SSL\_KEY\_STORE\_PASSWORD:**thingsboard**" 改為 "SSL\_KEY\_STORE\_PASSWORD:**thingsboard\_cert\_password**"，並將 "SSL\_KEY\_PASSWORD:**thingsboard**" 改為 "SSL\_KEY\_PASSWORD:**thingsboard\_cert\_password**"。

```js
  ssl:
    # Enable/disable SSL support
    enabled: "${SSL_ENABLED:true}"
    # Server SSL credentials
    credentials:
      # Server credentials type (PEM - pem certificate file; KEYSTORE - java keystore)
      type: "${SSL_CREDENTIALS_TYPE:KEYSTORE}"
      # Keystore server credentials
      keystore:
        # Type of the key store (JKS or PKCS12)
        type: "${SSL_KEY_STORE_TYPE:PKCS12}"
        # Path to the key store that holds the SSL certificate
        store_file: "${SSL_KEY_STORE:keystore.p12}"
        # Password used to access the key store
        store_password: "${SSL_KEY_STORE_PASSWORD:thingsboard_cert_password}"
        # Key alias
        #key_alias: "${SSL_KEY_ALIAS:tomcat}"
        # Password used to access the key
        key_password: "${SSL_KEY_PASSWORD:thingsboard_cert_password}"
```

#### MQTT 相關設定 {#mqtt-related-settings}

1. 啟用 SSL →  將 "MQTT\_SSL\_ENABLED:**false**" 改為 "MQTT\_SSL\_ENABLED:**true**"；
2. 更改憑據型別 → 從 "MQTT\_SSL\_CREDENTIALS\_TYPE:**PEM**" 改為 "MQTT\_SSL\_CREDENTIALS\_TYPE:**KEYSTORE**"；
3. 更改金鑰型別 → 從 "MQTT\_SSL\_KEY\_STORE\_TYPE:**JKS**" 改為 "MQTT\_SSL\_KEY\_STORE\_TYPE:**PKCS12**"；
4. 更改路徑（副檔名）→ 從 "MQTT\_SSL\_KEY\_STORE:mqttserver**.jks**" 改為 "MQTT\_SSL\_KEY\_STORE:mqttserver**.p12**"。
5. 停用 key alias 設定 → 將其註釋掉 → 只需在 `key_alias: "${MQTT_SSL_KEY_ALIAS:}"` 行前放置 "**#**" 符號；
6. 輸入你在 RouterOS 中使用的自己的證書密碼 → 將 "MQTT\_SSL\_KEY\_STORE\_PASSWORD:**server\_ks\_password**" 改為 "MQTT\_SSL\_KEY\_STORE\_PASSWORD:**thingsboard\_mqttcert\_password**"，並將 "MQTT\_SSL\_KEY\_PASSWORD:**server\_key\_password**" 改為 "MQTT\_SSL\_KEY\_PASSWORD:**thingsboard\_mqttcert\_password**"。

```js
    ssl:
      # Enable/disable SSL support
      enabled: "${MQTT_SSL_ENABLED:true}"
      # Server SSL credentials
      credentials:
        # Server credentials type (PEM - pem certificate file; KEYSTORE - java keystore)
        type: "${MQTT_SSL_CREDENTIALS_TYPE:KEYSTORE}"
        # Keystore server credentials
        keystore:
          # Type of the key store (JKS or PKCS12)
          type: "${MQTT_SSL_KEY_STORE_TYPE:PKCS12}"
          # Path to the key store that holds the SSL certificate
          store_file: "${MQTT_SSL_KEY_STORE:mqttserver.p12}"
          # Password used to access the key store
          store_password: "${MQTT_SSL_KEY_STORE_PASSWORD:thingsboard_mqttcert_password}"
          # Optional alias of the private key; If not set, the platform will load the first private key from the keystore;
          #key_alias: "${MQTT_SSL_KEY_ALIAS:}"
          # Optional password to access the private key. If not set, the platform will attempt to load the private keys that are not protected with the password;
          key_password: "${MQTT_SSL_KEY_PASSWORD:thingsboard_mqttcert_password}"
```

:::info
將其餘設定保留為預設值。除非你知道自己在做什麼，否則不要刪除/更改上方示例中未顯示的行。
:::

將更改應用到 "**thingsboard.yml**" 檔案（編輯後重新儲存）。

### 上傳修改後的 ThingsBoard 配置檔案 {#upload-altered-thingsboard-configuration-file}

剩下的就是用修改後的檔案覆蓋當前配置檔案，並上傳兩個證書。

再次確保你的終端指向正確的資料夾（其中有 3 個檔案 → 兩個證書和修改後的 "thingsboard.yml" 檔案），然後從那裡透過 SFTP 進入容器的配置檔案目錄：

```powershell
c:\Users\Admin\Desktop\ThingsBoard>dir
 Directory of c:\Users\Admin\Desktop\ThingsBoard

30.01.2023  10:59    <DIR>          .
30.01.2023  10:59    <DIR>          ..
27.01.2023  15:09             2 448 keystore.p12
27.01.2023  15:36             2 434 mqttserver.p12
30.01.2023  10:59            68 846 thingsboard.yml
               3 File(s)         73 728 bytes
               2 Dir(s)  50 901 626 880 bytes free
c:\Users\Admin\Desktop\ThingsBoard>sftp admin@192.168.88.1
admin@192.168.88.1's password:
Connected to 192.168.88.1.
sftp> cd ThingsBoard/usr/share/thingsboard/conf
sftp> dir
banner.txt          i18n                logback.xml         templates           thingsboard.conf    thingsboard.yml     
```

使用 `put` 命令上傳這些檔案：

```powershell
sftp> put thingsboard.yml
Uploading thingsboard.yml to /ThingsBoard/usr/share/thingsboard/conf/thingsboard.yml
thingsboard.yml                                                                       100%   67KB   2.2MB/s   00:00
sftp> put keystore.p12
Uploading keystore.p12 to /ThingsBoard/usr/share/thingsboard/conf/keystore.p12
keystore.p12                                                                          100% 2448     1.2MB/s   00:00
sftp> put mqttserver.p12
Uploading mqttserver.p12 to /ThingsBoard/usr/share/thingsboard/conf/mqttserver.p12
mqttserver.p12                                                                        100% 2434   608.5KB/s   00:00
sftp> dir
banner.txt          i18n                keystore.p12        logback.xml         mqttserver.p12      templates           
thingsboard.conf    thingsboard.yml
```

重啟容器：

```ros
[admin@MikroTik] > /container/stop 0
[admin@MikroTik] > /container/start 0
```

在再次啟動容器之前，務必等待容器停止（使用 `/container/print` 命令後應顯示 `status=stopped`）。

### 確認 HTTPS 訪問 {#confirm-https-access}

現在，你應該能夠訪問 [https://your\_IP:9090](https://192.168.88.1)（其中 IP 地址是 DNAT 規則中使用的地址）：

![](/img/c12800e16c69a30a.webp)

:::info
由於我們使用的是並非由受信任機構簽發的自簽名證書，可能會出現指示連線不安全的錯誤，但你可以透過瀏覽器檢視證書（確認就是該證書），接受風險並繼續。
:::

### 確認 SSL MQTT 連線 {#confirm-ssl-mqtt-connection}

:::info
**不要忘記修改**“網路”部分所示的**埠轉發規則**，將 **`dst-port`** 和 **`to-ports`** 從 1883（標準非 SSL MQTT 埠）**改為 8883**（**SSL MQTT 埠**）。
:::

在此示例中，我們將測試[單向 SSL 通訊訪問令牌場景](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md#one-way-ssl-communication-scenario)。

#### 使用執行容器的裝置進行測試 {#testing-with-the-device-that-is-running-the-container}

:::info
MQTT 證書應該已經安裝到裝置的系統中（因為生成它的正是該裝置）。
:::

新增 MQTT broker：

```ros
/iot/mqtt/brokers/add name=tbssl address=172.18.0.2 port=8883 username=YOUR_TOKEN ssl=yes
```

以 JSON 格式釋出一條靜態測試 MQTT 訊息：

```ros
/iot/mqtt/publish broker="tbssl" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

確認 MQTT broker 已收到它：

![](/img/950e2b020d062eb0.webp)

#### 使用另一臺裝置進行測試 {#testing-with-another-device}

當你有兩臺 RouterOS 裝置時，一臺執行容器（在我們的示例中，它也是生成證書的同一臺裝置），另一臺是你希望從中測試 MQTT 連線的裝置（比如 [LTAP](https://mikrotik.com/product/ltap) 或任何其他已安裝 IoT 包的 RouterOS 裝置）→ 你需要將證書匯入第二臺裝置。

將匯出的證書（**mqttserver.p12**）拖放到裝置的 "File List" 中：

```ros
[admin@LTAP] > /file/print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME            TYPE       SIZE  CREATION-TIME       
0  mqttserver.p12  .p12 file  2438  2023-01-30 13:28:11
1  flash           disk             2021-07-06 14:51:53
2  flash/pub       directory        2021-07-06 14:51:53
3  flash/skins     directory        1970-01-01 02:00:07
[admin@LTAP] > 
```

匯入證書：

```ros
[admin@LTAP] > /certificate/import file-name=mqttserver.p12 passphrase=thingsboard_mqttcert_password
```

新增 MQTT broker，其中地址是 ThingsBoard 容器路由器上 TCP 8883 埠轉發規則中使用的 IP 地址 `dst-address`：

```ros
/iot/mqtt/brokers/add name=tbssl address=192.168.88.1 port=8883 username=YOUR_TOKEN ssl=yes
```

以 JSON 格式釋出一條靜態測試 MQTT 訊息：

```ros
/iot/mqtt/publish broker="tbssl" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

並確認 broker 已收到它 → 在 ThingsBoard 上的 "Latest Telemetry" 部分下。
