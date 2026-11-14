---
sidebar_key: "internet-of-things/mqtt/mqtt-and-thingsboard-configuration"
sidebar_position: 2
title: "MQTT 與 ThingsBoard 配置"
sidebar_label: "MQTT 與 ThingsBoard 配置"
description: "本頁指導 MikroTik RouterOS 使用者配置向 ThingsBoard 釋出 MQTT 資料，涵蓋裝置設定、身份驗證場景（訪問令牌、基本憑據、SSL/TLS）以及用於安全通訊的證書管理。"
tags:
  - 'mqtt'
  - 'thingsboard'
  - 'ssl'
source: https://manual.mikrotik.com/docs/internet-of-things/mqtt/mqtt-and-thingsboard-configuration
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 簡介 {#introduction}

你可以用來監控 MQTT 釋出者傳送的資訊的眾多雲服務之一是 [Thingsboard](https://thingsboard.io/)。本文將演示如何配置 Thingsboard 和 RouterOS，以使用 MQTT 協定釋出資料。在此場景中，RouterOS 將充當閘道器，並將資料從 RouterBoard 釋出到 Thingsboard 伺服器。在此場景中，Thingsboard 將充當 MQTT broker（接收資料的伺服器）。

在繼續設定之前，你需要先執行以下任一操作：

- a) 在 Thingsboard 系統中建立賬號。你可以透過此[連結](https://thingsboard.cloud/signup)完成。這將允許你在有限/測試時間段內免費使用 ThingsBoard 雲解決方案。
- b) 按照[指南](https://thingsboard.io/docs/user-guide/install/installation-options/)搭建你自己的伺服器。有一個社群版可以免費安裝和使用。

:::warning
請考慮使用 **SSL MQTT（TCP 埠 8883 和證書）**，而不是非 SSL MQTT（TCP 埠 1883）。如果你使用非 SSL MQTT，用戶端（MQTT 釋出者）與伺服器（MQTT broker）之間的通訊很容易被嗅探/抓包，這會危及身份驗證資料（例如 client-id、使用者名稱和密碼）。
:::

### Thingsboard 配置 {#thingsboard-configuration}

:::info
在本指南中，我們將展示本地例項/伺服器安裝配置，但相同的原則也適用於雲選項。
:::

透過瀏覽器訪問登入頁面並登入。轉到 "**Devices**" 選單。

透過點選新增按鈕 "+" 和 "Add new device" 來建立新裝置：

![](/img/c5f98d9f4917b259.webp)

輸入裝置名稱，然後點選 "Add"：

![](/img/3c519af589b57557.webp)

預設情況下，新建立的裝置會選擇訪問令牌身份驗證。

#### 訪問令牌場景 {#access-token-scenario}

你可以點選已建立的裝置，並進入 "**Manage Credentials**" 設定（在 "**Details**" 部分中）來更改令牌：

![](/img/24761f96b4bfa335.webp)

此令牌將用作 MQTT 釋出者的 "username"（在 RouterOS 設定中）。

你可以透過此[連結](https://thingsboard.io/docs/reference/mqtt-api/)瞭解更多資訊。

#### MQTT Basic 場景 {#mqtt-basic-scenario}

你可以為特定裝置在 "**Device Credentials**" 部分中更改憑據型別：

![](/img/37f2d21a3498da9f.webp)

MQTT Basic 場景允許你指定用於 MQTT 身份驗證的 Client ID、Username 和 Password。

你可以透過此[連結](https://thingsboard.io/docs/user-guide/basic-mqtt/)瞭解更多資訊。

#### 單向 SSL 通訊場景 {#one-way-ssl-communication-scenario}

:::warning
推薦使用此場景！

**重要：** 此類身份驗證要求你使用伺服器證書進行 SSL 通訊。必須生成伺服器證書並將其上傳到 ThingsBoard 例項。

要生成伺服器證書，請參考[此指南](https://thingsboard.io/docs/user-guide/mqtt-over-ssl/) → 生成證書（例如，使用 OPENSSL 工具），將其安裝/上傳到正確的資料夾，並在 ThingsBoard 配置檔案中啟用 MQTT SSL。
:::

配置將與上面顯示的 **訪問令牌** 和 **MQTT Basic 場景** 相同。因此，任選其一即可。

在這種情況下，唯一區別是裝置與伺服器之間的通訊（你只需稍作更改 RouterOS 設定中的 MQTT broker 配置，稍後會展示）。

**使用此場景時，通訊將被加密（使用 SSL）**。

#### X.509（雙向 SSL 通訊）場景 {#x509-two-way-ssl-communication-scenario}

:::info
此類身份驗證要求你使用伺服器證書和用戶端證書進行 SSL 通訊。必須生成伺服器證書並將其上傳到 ThingsBoard 例項。

要生成伺服器證書，請參考[此指南](https://thingsboard.io/docs/user-guide/mqtt-over-ssl/) → 生成證書（例如，使用 OPENSSL 工具），將其安裝/上傳到正確的資料夾，並在 ThingsBoard 配置檔案中啟用 MQTT SSL。

要生成用戶端證書，請參考[此指南](https://thingsboard.io/docs/user-guide/certificates/)。
:::

你可以為特定裝置在 "**Device Credentials**" 部分中更改憑據型別：

![](/img/c4806e3946f1968c.webp)

X.509 場景使用用戶端證書進行身份驗證。

證書生成後（例如，使用 OpenSSL），將 RSA 公鑰複製到該欄位中，然後點選 "Save" 按鈕。

### RouterOS 配置 {#routeros-configuration}

***注意**：為了配置 MQTT，請確保事先已安裝 **iot** [軟體包](../../getting-started/installation-and-upgrade/packages.md)。*

#### MQTT 代理 {#mqtt-broker}

##### 訪問令牌場景 {#access-token-scenario-1}

如下所示新增 MQTT broker：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=1883 username=access_token
```

- 將 `address` 更改為你的 ThingsBoard 伺服器的實際 IP/域名地址。
- 將 `username` 更改為你在 ThingsBoard 設定中使用的訪問令牌。

##### MQTT Basic 場景 {#mqtt-basic-scenario-1}

如下所示新增 MQTT broker：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x client-id=clientid password=password username=username
```

- 將 `address` 更改為你的 ThingsBoard 伺服器的實際 IP/域名地址；
- 將 `username`、`password` 和 `client-id` 更改為你在 ThingsBoard 設定中使用的實際值。

##### 單向 SSL 通訊場景 {#one-way-ssl-communication-scenario-1}

:::warning
推薦使用此場景！
:::

在此場景中，RouterOS 需要將伺服器證書匯入其系統。

將已安裝到 ThingsBoard 中的伺服器證書拖放到路由器的 "File List" 選單中：

![](/img/ad8d2ba814a621e2.webp)

匯入伺服器證書：

```ros
/certificate/import file-name=mqttserver.pem passphrase=""
```

使用 **SSL 單向通訊** 和 **訪問令牌場景** 時，如下所示新增 MQTT broker：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=8883 username=access_token ssl=yes
```

- 將 `address` 更改為你的 ThingsBoard 伺服器的實際 IP/域名地址。
- 將 `username` 更改為你在 ThingsBoard 設定中使用的訪問令牌。
- 確保使用 `port=8883`（伺服器監聽的 MQTT SSL 埠）。
- 確保啟用 `ssl=yes`。

使用 **SSL 單向通訊** 和 **MQTT Basic 場景** 時，如下所示新增 MQTT broker：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=8883 client-id=clientid password=password username=username ssl=yes
```

- 將 `address` 更改為你的 ThingsBoard 伺服器的實際 IP/域名地址。
- 將 `username`、`password` 和 `client-id` 更改為你在 ThingsBoard 設定中使用的實際值。
- 確保使用 `port=8883`（伺服器監聽的 MQTT SSL 埠）。
- 確保啟用 `ssl=yes`。

##### X.509（雙向 SSL 通訊）場景 {#x509-two-way-ssl-communication-scenario-1}

將證書拖放到路由器的 "Files/File List" 選單中 →  *伺服器證書、用戶端證書及其私鑰。*

逐個匯入證書：

```ros
/certificate/import file-name=mqttserver.pem passphrase=""
/certificate/import file-name=cert.pem passphrase=""
/certificate/import file-name=key.pem passphrase=""
```

如下所示新增 MQTT broker：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=8883 certificate=cert.pem_0 ssl=yes
```

- 將 `address` 更改為你的 ThingsBoard 伺服器的實際 IP/域名地址。
- 將所選的 `certificate` 更改為你已匯入的實際用戶端證書名稱。
- 確保使用 `port=8883`（伺服器監聽的 MQTT SSL 埠）。
- 確保啟用 `ssl=yes`。

#### MQTT 釋出 {#mqtt-publish}

a) 使用靜態值進行快速 MQTT 釋出測試：

```ros
/iot/mqtt/publish broker="tb" topic="v1/devices/me/telemetry" message="{\"cpu\":\"7\"}"
```

b) 為了將 RouterOS 中的相關資料釋出到 Thingsboard，你可以參考下面所示的指令碼。該指令碼從 RouterOS 裝置收集資料（型號名稱、序列號、RouterOS 版本、當前 CPU、已用記憶體、空閒記憶體和執行時間），並以 JSON 格式將訊息（資料）釋出到 broker：

```ros
# 所需软件包：iot
################################ Configuration ################################  
# 用于发布的现有 MQTT broker 的名称
:local broker "tb"
# 消息应发布到的 MQTT 主题
:local topic "v1/devices/me/telemetry"
#################################### System ###################################  
:put ("[\*] Gathering system info...")  
:local cpuLoad [/system/resource/get cpu-load]  
:local freeMemory [/system/resource/get free-memory]  
:local usedMemory ([/system/resource/get total-memory] - $freeMemory)  
:local rosVersion [/system/package/get value-name=version \  
[/system/package/find where name ~ "^routeros"]]  
:local model [/system/routerboard/get value-name=model]  
:local serialNumber [/system/routerboard/get value-name=serial-number]  
:local upTime [/system/resource/get uptime]
#################################### MQTT #####################################  
:local message \  
"{\"model\":\"$model\",\  
\"sn\":\"$serialNumber\",\  
\"ros\":\"$rosVersion\",\  
\"cpu\":$cpuLoad,\  
\"umem\":$usedMemory,\  
\"fmem\":$freeMemory,\  
\"uptime\":\"$upTime\"}"
:log info "$message";  
:put ("[\*] Total message size: $[:len $message] bytes")  
:put ("[\*] Sending message to MQTT broker...")  
/iot/mqtt/publish broker=$broker topic=$topic message=$message  
:put ("[\*] Done")
```

應注意 2 行指令碼。

```ros
:local broker "tb"
```

行，你應在引號 "" 內指定 broker 的名稱。

```ros
:local topic "v1/devices/me/telemetry"
```

行，你應在引號 "" 內指定正確的 topic（請檢視 Thingsboard 的[文件](https://thingsboard.io/docs/reference/mqtt-api/)，瞭解需要使用的確切 topic）。

指令碼其餘配置取決於整體需求。

將上面的指令碼複製並貼上到記事本中，然後再次複製。導航到 System>Scripts 選單，在其中新增新指令碼，並貼上上面顯示的指令碼。例如，將其命名為 script1。

要執行指令碼，您可以使用命令列：

```ros
/system/script/run script1
```

### 驗證 {#verification}

你可以在 "Latest telemetry" 部分下檢查裝置接收/釋出的資料：

![](/img/d496ec481ae7566f.webp)
