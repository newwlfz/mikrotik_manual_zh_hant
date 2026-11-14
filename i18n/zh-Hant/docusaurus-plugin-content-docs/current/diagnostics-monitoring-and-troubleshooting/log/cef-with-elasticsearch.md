---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/log/cef-with-elasticsearch"
sidebar_position: 1
title: "帶 Elasticsearch 的 CEF"
sidebar_label: "帶 Elasticsearch 的 CEF"
description: "本指南說明如何使用 Elasticsearch、Kibana 和 Fleet Server 配合 MikroTik RouterOS 裝置配置 CEF 日誌收集與分析。內容涵蓋前提條件、Elastic 與 RouterOS 兩側元件的設定步驟，包括代理策略建立和 CEF 整合配置。"
tags:
  - 'elasticsearch'
  - 'cef-logging'
  - 'kibana'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/log/cef-with-elasticsearch
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

Elasticsearch 是一個流行的 NoSQL 資料庫，可用於儲存各種資料，包括 CEF 日誌。結合 Kibana，您可以建立一個強大的工具來分析來自 RouterOS 裝置的 CEF 日誌。本指南將依賴 Elasticsearch 整合，要使其正常工作，您需要有一個可用的 Elasticsearch 環境。本指南不會涵蓋 Elasticsearch 和 Kibana 的安裝說明，但會涵蓋設定 CEF 日誌收集和分析的相關步驟。

使用 Elasticsearch 可以進行多種配置，但本指南將採用以下原則：

- RouterOS (10.0.0.1) 裝置將 CEF 日誌傳送到執行 [CEF 整合](https://www.elastic.co/docs/reference/integrations/cef) 的伺服器 (10.0.0.2)。
- 執行 CEF 整合的伺服器 (10.0.0.2) 接收 CEF 日誌、處理資料，並將其傳送到 [Fleet Server](https://www.elastic.co/guide/en/fleet/current/fleet-server.html) (10.0.0.3)。
- Fleet Server (10.0.0.3) 將資料儲存在 [Elasticsearch](https://www.elastic.co/elasticsearch) (10.0.0.4) 中。
- [Kibana](https://www.elastic.co/kibana) (10.0.0.5) 從 Elasticsearch (10.0.0.4) 檢索資料、進行分析，並允許您搜尋資料。

:::info
本指南不會將 [Logstash](https://www.elastic.co/logstash) 用作分析 CEF 日誌的一部分；它已被 Fleet Server 取代。

:::

:::info
可以將 Elasticsearch、Kibana、Fleet Server 和 CEF 日誌整合安裝在同一臺裝置上。

:::

## 先決條件 {#prerequisites}

- [設定 Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html)。  
  :::info
  Elasticsearch 在許多平臺上得到廣泛支援。建議設定一個 Elasticsearch 節點叢集。
  :::
- [設定 Kibana](https://www.elastic.co/guide/en/kibana/current/setup.html)。  
  :::info
  Kibana 可以安裝在安裝 Elasticsearch 的同一臺裝置上，但出於效能原因，也可以安裝在單獨的裝置上。雖然不借助 Kibana 也可以分析 CEF 日誌，但這需要編寫自己的 API 請求。Kibana 非常易於使用，並且具有廣泛的功能。
  :::
- [Set up Fleet Server](https://www.elastic.co/guide/en/fleet/current/add-fleet-server-on-prem.html).  
  :::info
  可以在安裝 Elasticsearch 和/或 Kibana 的同一臺裝置上設定 Fleet Server。建議將 Fleet Server 安裝在其他裝置上。有關硬體和拓撲要求的建議，請參閱 Elasticsearch 手冊。
  :::

## 設定 {#set-up}

設定說明分為兩部分：Elastic（有關 Elasticsearch、Kibana 和 Fleet Server 的配置）和 RouterOS（與您的 RouterOS 裝置相關的配置）。

### Elastic {#elastic}

:::warning
某些步驟可能會隨時間而變化，請參閱 Elastic 的手冊以獲取最新步驟。
:::

- [登入到您的 Kibana](https://www.elastic.co/guide/en/kibana/current/access.html)。
- 在主選單下開啟 [Fleet](https://www.elastic.co/guide/en/kibana/current/fleet.html) 部分。
- 開啟“[Agent policies](https://www.elastic.co/guide/en/fleet/current/agent-policy.html)”部分。
- 按“Create agent policy”按鈕以[建立新的代理策略](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#create-a-policy)。
- 為策略命名，例如“CEF policy”，根據需要調整高階設定，然後建立策略。或者您可以使用下面的 API 請求：  

  ```text
  POST kbn:/api/fleet/agent_policies
  {
    "name": "CEF policy",
    "description": "",
    "namespace": "default",
    "monitoring_enabled": [
      "logs",
      "metrics"
    ],
    "inactivity_timeout": 1209600,
    "is_protected": false
  }
  ```

- 單擊其名稱，開啟新建的策略。
- 按“[新增整合](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#add-integration)”按鈕。
- 搜尋“[Common Event Format (CEF)](https://www.elastic.co/docs/reference/integrations/cef)”並按下“新增 Common Event Format (CEF)”。
- 調整配置，確保：  
  - 在“Collect CEF application logs (input: udp)”部分下，將“Syslog Host”設定為“0.0.0.0”，並保留預設監聽埠 9003/UDP。  
  - 在“Collect CEF application logs (input: tcp)”部分下，將“Syslog Host”設定為“0.0.0.0”。
- 儲存該整合。
- 按“[將 Elastic Agent 新增到你的主機](https://www.elastic.co/guide/en/fleet/current/elastic-agent-installation.html)”按鈕。
- 按照說明將 Elastic Agent 新增到你的主機。  
  :::info
  Elastic 官方手冊建議將 Elastic Agent 安裝為 Fleet 管理。建議遵循該建議，因為當代理由 Fleet 管理時，管理代理會更容易。
  :::
- 轉到主選單中的“Stack Management”，然後開啟“[Ingest Pipelines](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html)”。
- 按“[Create pipeline](https://www.elastic.co/guide/en/fleet/current/data-streams-pipeline-tutorial.html#data-streams-pipeline-one)”然後“New pipeline”來建立新的 Ingest Pipeline。
- 將“Name”設定為“logs-cef.log@custom”。
- 按“Import processors”並貼上以下處理器：  

  ```json
  {
  	"processors": [
  		{
  			"set": {
  			"ignore_empty_value": true,
  			"field": "host.name",
  			"copy_from": "cef.extensions.deviceHostName"
  			}
  		},
  		{
  			"set": {
  			"ignore_empty_value": true,
  			"field": "host.ip",
  			"copy_from": "cef.extensions.deviceAddress"
  			}
  		}
  	]
  }
  ```

  :::info
  “logs-cef.log@custom”管道不是必需的，但當您還將 Elasticsearch 用於其他型別的日誌時，它可以讓搜尋日誌更容易。
  :::
- 按“Save pipeline”。
- 確保您已在主機上以及從 RouterOS 裝置 (10.0.0.1) 路徑中的其他位置開啟 9003/UDP 埠。
- 您的 Elastic Agent 現已準備好接收 CEF 日誌。

### RouterOS {#routeros}

1. 在你的 RouterOS 裝置（10.0.0.1）上配置[遠端日誌記錄動作](./index.md#send-the-log-to-a-syslog-server)：

   ```ros
   /system/logging/action
   add cef-event-delimiter="\n" name=cef remote=10.0.0.2 \
       remote-log-format=cef remote-port=9003 \
       syslog-time-format=iso8601 target=remote
   ```

   名稱可以是任意由字母和數字組成的名稱（例如 `cef`）；路由器會將日誌傳送到您設定的 `remote` 地址和埠。

2. 為你希望從 RouterOS 裝置（10.0.0.1）接收的每個[主題](./index.md#topics)新增一條規則，例如：

   ```ros
   /system/logging
   add action=cef topics=info
   add action=cef topics=error
   add action=cef topics=critical
   add action=cef topics=warning
   add action=cef topics=bridge,stp
   ```

3. 您現在應該開始看到 CEF 日誌被接收。
4. 繼續閱讀本指南以開始使用 Kibana。

### 使用 Kibana {#using-kibana}

Kibana 允許您搜尋已接收的 CEF 日誌。要檢視已接收的日誌，請執行以下操作：

1. [登入到您的 Kibana](https://www.elastic.co/guide/en/kibana/current/access.html)。
2. 從主選單開啟“Discover”。
3. [新增篩選器](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#explore-fields-in-your-data)，並使用以下引數：  

   ```text
   Select a field: data_stream.dataset
   Select operator: IS
   Select a value: cef.log
   ```

4. 為簡單起見，我們建議在 Discover 選單中[搜尋欄位](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#explore-fields-in-your-data)，搜尋“message”，然後將其新增到檢視中。
5. 我們還建議搜尋“host.name”欄位，並將其也新增到檢視中。
6. 考慮[儲存搜尋](https://www.elastic.co/guide/en/kibana/current/save-open-search.html#_save_a_search)，以便以後更輕鬆地訪問。
7. 完成！
