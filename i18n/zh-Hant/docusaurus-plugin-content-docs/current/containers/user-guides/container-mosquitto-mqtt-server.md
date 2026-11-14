---
sidebar_key: "containers/user-guides/container-mosquitto-mqtt-server"
sidebar_position: 6
title: "容器 - mosquitto MQTT 伺服器"
sidebar_label: "容器 - mosquitto MQTT 伺服器"
description: "本頁介紹如何使用 MikroTik RouterOS 容器執行 eclipse-mosquitto MQTT 伺服器以支援 IoT 應用，詳細說明容器設定步驟，包括網路、環境變數和掛載，並附有 SSL 支援警告。"
tags:
  - 'mqtt'
  - 'container'
source: https://manual.mikrotik.com/docs/containers/user-guides/container-mosquitto-mqtt-server
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

將容器功能引入 RouterOS 後，就可以在路由器內執行各種用於各類任務的伺服器。這對於希望減少網路中裝置數量的人尤其有用。與其在單獨的裝置/機器上執行伺服器，何不直接在路由器內執行它呢？

在本指南中，我們將展示如何安裝一個名為 [eclipse-mosquitto](https://mosquitto.org/) 的基本 MQTT 代理（換句話說，伺服器）。MQTT 協定是非常流行的選擇，尤其是在 IoT 拓撲中。它是一種開放的 OASIS 和 ISO 標準輕量級釋出-訂閱網路協定，用於在裝置之間傳輸訊息。典型拓撲由 MQTT 釋出者（傳送資訊的裝置）、MQTT 代理（儲存資料的伺服器）和 MQTT 訂閱者（監聽伺服器上釋出的資料的裝置）組成。

RouterOS 支援 [MQTT 釋出、訂閱](../../internet-of-things/mqtt/index.md) 功能，而現在我們也可以執行 MQTT 代理。

我們將要使用的映象可透過以下 hub.docker [連結](https://hub.docker.com/_/eclipse-mosquitto) 找到。

## 概述 {#summary}

在繼續配置之前，請務必學習我們的[容器](../index.md)指南。請務必檢視[免責宣告](../index.md#disclaimer)和[要求](../index.md#requirements)部分，以瞭解所有風險以及您可能需要採取的必要步驟。

您可以透過以下[連結](https://hub.docker.com/_/eclipse-mosquitto/tags)查詢支援的架構。

在本指南釋出時，**eclipse-mosquitto** 映象可用於 ARM32、ARM64 和 AMD64（CHR 和 x86）裝置。在本示例中，我們將在 ARM32 架構裝置 → [RB1100AHx4](https://mikrotik.com/product/rb1100ahx4) 上執行它。

:::warning

將展示一個**非常基礎**且**快速**的配置。請務必檢視 [mosquitto 文件](https://mosquitto.org/documentation/) 頁面，瞭解有關可實施的其他選項和設定的更多資訊。如果要將其用於生產環境，請**務必儘可能強化安全性**：

- [防火牆](../../cli-reference/ip/firewall/filter/index.md)，以便僅允許來自可信 IP 地址訪問容器；
- 從 mosquitto 代理/伺服器端提升安全性 → 使用強密碼、非標準埠等；
- 使用 SSL MQTT。

:::
## 容器配置 {#container-configuration}

**子選單：** `/container`

***注意**:* 需要 **container** 軟體包。

### 容器模式 {#container-mode}

啟用容器模式：

```ros
/system/device-mode/update container=yes
```

如果要在 X86 上使用容器，您需要透過按下重設按鈕或冷重啟來確認 device-mode。

### 網路 {#networking}

為容器新增 veth 介面：

```ros
/interface/veth/add name=veth2 address=172.19.0.2/24 gateway=172.19.0.1
```

為容器建立網橋，並將 veth 新增到其中：

```ros
/interface/bridge/add name=msqt
/ip/address/add address=172.19.0.1/24 interface=msqt
/interface/bridge/port/add bridge=msqt interface=veth2
```

如果需要 NAT，為測試目的轉發非 SSL MQTT 的 TCP 1883 埠（其中 192.168.88.1 是裝置的 LAN IP 地址）（可選）：

```ros
/ip/firewall/nat/add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=1883 protocol=tcp to-addresses=172.19.0.2 to-ports=1883
```

### 環境變數和掛載 {#environment-variables-and-mounts}

根據 eclipse-mosquitto 的 Docker Hub，為配置檔案定義一個掛載。我們不僅會掛載配置檔案，還會掛載整個資料夾，因為對於 SSL MQTT，我們還需要將證書上傳到該資料夾中：

```ros
/container/mounts/add list=msqt_config src=/mosquitto_mounted dst=/mosquitto/config
```

### 獲取映象 {#getting-image}

為簡化配置，我們將從外部映象庫獲取映象，但你也可以透過 [.tar](../index.md#option-b-import-image-from-pc) 檔案匯入它。

在本示例中，我們將使用裝置自身的儲存。RB1100AHx4 有 128 MB 磁碟空間，基本的 mosquitto 安裝佔用不應超過約 15 MB。

確保已相應設定“Registry URL”，限制 RAM 使用量（如有必要），併為映象設定一個目錄：

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=pull
```
### 拉取映象 {#pull-image}

```ros
/container/add remote-image=library/eclipse-mosquitto:latest interface=veth2 root-dir=mosquitto mountlists=msqt_config logging=yes
```

執行該命令後，RouterOS 應開始“解壓”包。檢查 "File System" 中新建的資料夾，並使用 `/container/print` 命令監控容器狀態。
### 設定 mosquitto 配置檔案 {#setting-up-mosquitto-configuration-file}

要獲取 **mosquitto.conf** 檔案，我們需要使用 SFTP（基於 SSH 的檔案傳輸）協定，因此請確保已啟用 SSH [服務](../../system-information-and-utilities/services.md)。您也可以使用 FTP。

開啟命令終端（Windows 使用者以管理員身份開啟“CMD”，Linux 使用者開啟“Linux Shell 或命令終端”），並導航到您要下載配置檔案的目錄。例如，導航到“桌面”上的“Container”資料夾：

```powershell
C:\WINDOWS\system32>cd C:\Users\Administrator\Desktop\Container

C:\Users\Administrator\Desktop\Container>
```

透過裝置的 IP 地址發起 SFTP 連線：

```powershell
C:\Users\Administrator\Desktop\Container>sftp admin@192.168.88.1
The authenticity of host '192.168.88.1 (192.168.88.1)' can't be established.
RSA key fingerprint is SHA256:lfxxs+xMrXlvP7hiHi9ZAEZlPi6/c5US+r6J7ljhkaA.
Are you sure you want to continue connecting (yes/no/[fingerprint])?yes
Warning: Permanently added '192.168.88.1' (RSA) to the list of known hosts.
Connected to 192.168.88.1.
sftp>
```

轉到 mosquitto 配置檔案資料夾（使用 `dir` 或 `ls` 命令檢視當前所在資料夾的內容，使用 `cd` 命令轉到您選擇的資料夾）。預設情況下，配置從“/mosquitto/config/mosquitto.conf”載入，因此請導航到該位置並使用 `get` 命令下載它：

```powershell
sftp> cd mosquitto/mosquitto/config
sftp> dir
mosquitto.conf
sftp> get mosquitto.conf
Fetching /mosquitto/mosquitto/config/mosquitto.conf to mosquitto.conf
/mosquitto/mosquitto/config/mosquitto.conf
```

透過您偏好的文字編輯器（記事本或任何其他編輯器）開啟“**mosquitto.conf**”，並用下面顯示的兩行內容覆蓋它：

:::warning

在本節中，我們將為測試目的配置一個基本的非 SSL MQTT 環境。除非您確定已實施所需的安全措施/限制，否則非 SSL MQTT 對於生產環境並不安全。

對於生產環境，在 MQTT 流量可能被捕獲/嗅探的拓撲中，和/或在 MQTT 流量直接透過網際網路（而非本地）路由的拓撲中，請使用 SSL MQTT。檢視 [SSL MQTT 部分](./container-mosquitto-mqtt-server.md#ssl-mqtt) 瞭解更多資訊。

:::

```text
listener 1883
allow_anonymous true
```

- 第一行 **listener 1883** 將使安裝例項監聽指定埠上的傳入網路連線。
- 第二行 **allow\_anonymous true** 決定是否允許未提供使用者名稱進行連線的用戶端連線。

使用相同的 **mosquitto.conf** 名稱覆蓋該檔案。

建立您自己的自定義配置檔案後，將其上傳到掛載的目錄/資料夾“**mosquitto\_mounted**”。如果您尚未執行容器，則不會有“**mosquitto\_mounted**”資料夾，您可以手動建立它。如果您已執行過（`/container/start 0`），則應已自動建立：

```powershell
sftp> dir
mosquitto           mosquitto_mounted   pub                 pull                skins
```

在編輯後的 mosquitto.conf 檔案所在目錄中使用 SFTP，並用 `put` 將其放入掛載目錄：

```powershell
C:\Users\Administrator\Desktop\Container>dir
 Directory of C:\Users\Administrator\Desktop\Container

02/03/2023  12:09 PM    <DIR>          .
02/03/2023  12:09 PM    <DIR>          ..
02/03/2023  12:09 PM            40,449 mosquitto.conf
               1 File(s)         40,449 bytes
               2 Dir(s)  76,166,430,720 bytes free

C:\Users\Administrator\Desktop\Container>sftp admin@192.168.88.1
Connected to 192.168.88.1.
sftp> dir
mosquitto           mosquitto_mounted   pub                 pull                skins
sftp> cd mosquitto_mounted
sftp> put mosquitto.conf
Uploading mosquitto.conf to /mosquitto_mounted/mosquitto.conf
mosquitto.conf                                                                        100%  162    40.5KB/s   00:00
```

重啟容器：

```ros
[admin@MikroTik] > /container/stop 0
[admin@MikroTik] > /container/start 0
```

在再次啟動容器之前，請確保等待容器停止（使用 `/container/print` 命令後應顯示 `status=stopped`）。
### 啟動容器 {#starting-the-container}

在使用 `/container/print` 確認 container 已新增且狀態變為 `status=stopped` 後 → 即可啟動它：

```ros
/container/start 0
```

如果已啟用容器日誌記錄，您將在 [日誌](../../diagnostics-monitoring-and-troubleshooting/log/index.md) 部分看到類似以下內容：

```text
 12:12:46 container,info,debug 1707214366: mosquitto version 2.0.18 starting
 12:12:46 container,info,debug 1707214366: Config loaded from /mosquitto/config/mosquitto.conf.
 12:12:46 container,info,debug 1707214366: Opening ipv4 listen socket on port 1883.
 12:12:46 container,info,debug 1707214366: Opening ipv6 listen socket on port 1883.
 12:12:46 container,info,debug 1707214366: mosquitto version 2.0.18 running
```

## MQTT 釋出與訂閱 {#mqtt-publish-and-subscribe}

**子選單：** `/iot/mqtt`

***注意**：* 需要 **iot** 軟體包。

新增 MQTT 代理：

```ros
/iot/mqtt/brokers/add name=mosquitto username=test address=172.19.0.2
```

訂閱 MQTT 代理和所需主題：

```ros
/iot/mqtt/subscribe broker=mosquitto topic=test/topic
```

釋出一條靜態 MQTT 訊息：

```ros
/iot/mqtt/publish broker="mosquitto" topic="test/topic" message="{\"test\":\"123\"}"
```

檢查訂閱以檢視收到的訊息：

```ros
/iot/mqtt/subscriptions/recv/print
 0 broker=mosquitto topic="test/topic" data="{"test":"123"}" 
   time=2023-07-12 10:01:40 
```

您還可以檢查容器日誌（如果已啟用），以確認 mosquitto 正常執行：

```text
 12:47:28 container,info,debug 1675421248: New connection from 172.19.0.1:42240 on port 1883.
 12:47:28 container,info,debug 1675421248: New client connected from 172.19.0.1:42240 as MTD8580EC793C4 (p2, c1, k60, u'test').
 12:47:38 container,info,debug 1675421258: Client MTD8580EC793C4 disconnected.
```

## SSL MQTT {#ssl-mqtt}

在生產環境中使用 **非 SSL MQTT** **並不安全**。人們可以輕鬆地[捕獲/嗅探](../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md)代理與釋出者之間的封包交換，從而能夠獲取使用者憑據和其他敏感資訊。

為了提高安全性，請使用 SSL MQTT。

第一步是生成證書。在本示例中，我們將使用簡單的 Root CA 場景（不要求裝置/用戶端證書）。

請使用官方的 [mosquitto-tls 使用者指南](https://mosquitto.org/man/mosquitto-tls-7.html) 瞭解分步操作。

### 伺服器配置 {#server-configuration}

您應已生成 ca.crt（證書頒發機構檔案）、server.crt（伺服器證書）和 server.key（伺服器金鑰）：

```powershell
C:\Users\Administrator\Desktop\Container>dir
 Directory of C:\Users\Administrator\Desktop\Container

07/12/2023  10:58 AM    <DIR>          .
07/12/2023  10:58 AM    <DIR>          ..
07/12/2023  10:56 AM             1,322 ca.crt
07/12/2023  10:56 AM             1,854 ca.key
07/12/2023  09:57 AM                35 mosquitto.conf
07/12/2023  10:58 AM             1,164 server.crt
07/12/2023  10:57 AM               960 server.csr
07/12/2023  10:56 AM             1,704 server.key
               6 File(s)          7,039 bytes
               2 Dir(s)  52,401,184,768 bytes free
```

透過您偏好的文字編輯器（記事本或任何其他編輯器）開啟掛載的“**mosquitto.conf**”，並用下面顯示的行覆蓋它：

```text
tls_version tlsv1.2
port 8883
allow_anonymous true
cafile /mosquitto/config/ca.crt
keyfile /mosquitto/config/server.key
certfile /mosquitto/config/server.crt
```

- **tls\_version** 行設定最低 TLS 版本。
- **port 8883** 將使安裝例項監聽指定埠上的傳入網路連線。
- **allow\_anonymous true** 決定是否允許未提供使用者名稱進行連線的用戶端連線。

:::warning

我們為測試目的使用基本的 SSL 配置。**allow\_anonymous true** 不是生產環境的安全設定。

:::

- **cafile /mosquitto/config/ca.crt** 行指定 CA 證書檔案的路徑。
- **keyfile /mosquitto/config/server.key** 行指定伺服器金鑰檔案的路徑。
- **certfile /mosquitto/config/server.crt** 行指定伺服器證書檔案的路徑。

將證書檔案和更新後的支援 SSL 的 mosquitto.conf 檔案上傳到掛載資料夾“**mosquitto\_mounted**”：

```powershell
C:\Users\Administrator\Desktop\Container>sftp admin@192.168.88.1
Connected to 192.168.88.1.
sftp> cd mosquitto_mounted
sftp> dir
mosquitto.conf
sftp> put ca.crt
Uploading ca.crt to /mosquitto_mounted/ca.crt
ca.crt                                                                                100% 1322   323.0KB/s   00:00
sftp> put server.crt
Uploading server.crt to /mosquitto_mounted/server.crt
server.crt                                                                            100% 1164   227.3KB/s   00:00
sftp> put server.key
Uploading server.key to /mosquitto_mounted/server.key
server.key                                                                            100% 1704   415.7KB/s   00:00
sftp> dir
ca.crt           mosquitto.conf   server.crt       server.key
sftp> put mosquitto.conf
Uploading mosquitto.conf to /mosquitto_mounted/mosquitto.conf
mosquitto.conf                                                                        100%  162    32.2KB/s   00:00
```

重啟容器：

```ros
[admin@MikroTik] > /container/stop 0
[admin@MikroTik] > /container/start 0
```

使用日誌確認代理監聽 8883 埠：

```text
 11:20:41 container,info,debug 1689160841: mosquitto version 2.0.15 starting
 11:20:41 container,info,debug 1689160841: Config loaded from /mosquitto/config/mosquitto.conf.
 11:20:41 container,info,debug 1689160841: Opening ipv4 listen socket on port 8883.
 11:20:41 container,info,debug 1689160841: Opening ipv6 listen socket on port 8883.
 11:20:41 container,info,debug 1689160841: mosquitto version 2.0.15 running
 11:22:24 system,info,account user admin logged in from 10.5.217.34 via local
```

### 測試連線 {#testing-the-connection}

將 CA 證書（**ca.crt**）上傳到 RouterOS 中裝置的“檔案列表”：

```ros
/file/print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME                TYPE             SIZE  CREATION-TIME      
0  skins               directory              1970-01-01 03:00:02
1  pub                 directory              2023-01-04 11:05:04
2  disk7               disk                   2023-07-12 09:52:07
3  mosquitto           container store        2023-07-12 09:52:09
4  mosquitto_mounted   container store        2023-07-25 16:38:37
5  pull                directory              2023-07-12 09:52:09
6  ca.crt              .crt file        1322  2023-07-12 11:28:23
```

匯入證書：

```ros
/certificate/import file-name=ca.crt passphrase=""
```

為 SSL 連線新增 MQTT 代理：

```ros
/iot/mqtt/brokers/add name=mosquittoSSL username=test address=172.19.0.2 port=8883 ssl=yes
```

訂閱 MQTT 代理和所需主題：

```ros
/iot/mqtt/subscribe broker=mosquittoSSL topic=test/topic
```

釋出一條靜態 MQTT 訊息：

```ros
/iot/mqtt/publish broker="mosquittoSSL" topic="test/topic" message="{\"test\":\"123\"}"
```

檢查訂閱以檢視收到的訊息：

```ros
/iot/mqtt/subscriptions/recv/print
 0 broker=mosquittoSSL topic="test/topic" data="{"test":"123"}" 
   time=2023-07-12 10:20:40 
```
