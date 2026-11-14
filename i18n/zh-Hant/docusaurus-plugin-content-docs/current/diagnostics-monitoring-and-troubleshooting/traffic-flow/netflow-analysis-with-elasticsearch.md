---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/traffic-flow/netflow-analysis-with-elasticsearch"
sidebar_position: 1
title: "使用 Elasticsearch 進行 NetFlow 分析"
sidebar_label: "使用 Elasticsearch 進行 NetFlow 分析"
description: "本指南介紹如何在 MikroTik RouterOS 上使用 Elasticsearch 設定 NetFlow 分析，包括配置從 RouterOS 裝置到 Elasticsearch 伺服器的資料採集，以及整合 Kibana 和部署 Fleet Server，從而實現高效的 NetFlow 資料處理與視覺化。"
tags:
  - 'elasticsearch'
  - 'netflow'
  - 'kibana'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/traffic-flow/netflow-analysis-with-elasticsearch
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Elasticsearch 是一個流行的 NoSQL 資料庫，可用於儲存各種資料，包括 NetFlow 日誌。結合 Kibana，你可以建立一個強大的工具來分析 RouterOS 裝置的 NetFlow 資料。本指南將依賴 Elasticsearch 整合，要使其正常工作，你需要有一個可正常執行的 Elasticsearch 環境。本指南不會涵蓋 Elasticsearch 和 Kibana 的設定說明，但會涵蓋設定 NetFlow 日誌收集與分析的相關步驟。

使用 Elasticsearch 可以進行多種配置，但本指南將採用以下原則：

- RouterOS（10.0.0.1）裝置將 NetFlow 資料傳送到執行 [NetFlow 整合](https://www.elastic.co/docs/current/integrations/netflow) 的伺服器（10.0.0.2）。
- 執行 NetFlow 整合的伺服器（10.0.0.2）接收 NetFlow 資料，處理資料並將其傳送到 [Fleet Server](https://www.elastic.co/guide/en/fleet/current/fleet-server.html)（10.0.0.3）。
- Fleet Server（10.0.0.3）將資料儲存在 [Elasticsearch](https://www.elastic.co/elasticsearch)（10.0.0.4）中。
- [Kibana](https://www.elastic.co/kibana)（10.0.0.5）從 Elasticsearch（10.0.0.4）檢索資料，對其進行分析，並允許你搜尋資料。

![NetFlow topology diagram](/img/d8cffdddf4e03b62.webp)

:::info
本指南不會將 [Logstash](https://www.elastic.co/logstash) 用作分析 NetFlow 資料的一部分；它已被 Fleet Server 取代。

**重要：** 可以將 Elasticsearch、Kibana、Fleet Server 和 NetFlow Records 整合安裝在同一裝置上。
:::

## 先決條件 {#prerequisites}

- [Set up Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html)  
  :::info
  Elasticsearch 在許多平臺上得到廣泛支援。建議設定一個 Elasticsearch 節點叢集。
  :::
- [Set up Kibana](https://www.elastic.co/guide/en/kibana/current/setup.html)  
  :::info
  Kibana 可以安裝在你安裝 Elasticsearch 的同一裝置上，但出於效能原因，也可以安裝在單獨的裝置上。雖然不借助 Kibana 也可以分析 NetFlow 資料，但這需要編寫你自己的 API 請求。Kibana 非常易於使用，並且功能廣泛。
  :::
- [Set up Fleet Server](https://www.elastic.co/guide/en/fleet/current/add-fleet-server-on-prem.html)  
  :::info
  可以在安裝 Elasticsearch 和/或 Kibana 的同一臺裝置上設定 Fleet Server。建議將 Fleet Server 安裝在其他裝置上。有關硬體和拓撲要求的建議，請參閱 Elasticsearch 手冊。
  :::

## 設定 {#set-up}

設定說明分為兩部分：Elastic（有關 Elasticsearch、Kibana 和 Fleet Server 的配置）和 RouterOS（與您的 RouterOS 裝置相關的配置）。

### Elastic {#elastic}

:::warning
某些步驟可能會隨時間而變化，請參閱 Elastic 的手冊以獲取最新步驟。
:::

1. [登入你的 Kibana](https://www.elastic.co/guide/en/kibana/current/access.html)
2. 在主選單下開啟 [Fleet](https://www.elastic.co/guide/en/kibana/current/fleet.html) 部分
3. 開啟“[代理策略](https://www.elastic.co/guide/en/fleet/current/agent-policy.html)”部分
4. 按下“建立代理策略”按鈕以[建立新的代理策略](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#create-a-policy)
5. 為策略命名，例如“NetFlow 策略”，根據需要調整高階設定，然後建立策略
6. 單擊其名稱以開啟你新建的策略
7. 按下“[新增整合](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#add-integration)”
8. 搜尋“[NetFlow Records](https://www.elastic.co/docs/current/integrations/netflow)”並按下“新增 NetFlow Records”
9. 調整配置，確保：  
   - 將“UDP host to listen on”設定為將執行 NetFlow Records 整合的伺服器的 IP 地址；在此示例中，該地址應為“10.0.0.2”
10. 儲存整合
11. 按下“[將 Elastic Agent 新增到你的主機](https://www.elastic.co/guide/en/fleet/current/elastic-agent-installation.html)”按鈕
12. 按照說明將 Elastic Agent 新增到你的主機  
    :::info
  Elastic 官方手冊建議將 Elastic Agent 安裝為 Fleet 管理。建議遵循該建議，因為當代理由 Fleet 管理時，管理代理會更容易。
  :::
13. 確保你已在主機上以及從 RouterOS 裝置（10.0.0.1）到該主機的路徑上的其他位置開啟 NetFlow 埠。預設目標埠是 2055/UDP。
14. 你的 Elastic Agent 現在已準備好接收 NetFlow 資料！

### RouterOS {#routeros}

1. （可選）建立一個[介面列表](../../cli-reference/interface/list/index.md)（例如“NetFlow\_interfaces”），並新增需要進行 NetFlow 資料分析的介面。  

   ```routeros
   /interface/list
   add name=NetFlow_interfaces
   /interface/list/member
   add interface=VLAN3000 list=NetFlow_interfaces
   ```

2. 配置 [流量監控](./index.md) 以將 NetFlow 資料傳送到你的 Elastic Agent（10.0.0.2）。  

   ```routeros
   /ip/traffic-flow
   set enabled=yes interfaces=NetFlow_interfaces
   /ip/traffic-flow/target
   add dst-address=10.0.0.2
   ```

3. 你現在應該開始看到 NetFlow 資料被接收！
4. 繼續閱讀本指南以開始使用 Kibana。

## 使用 Kibana {#using-kibana}

:::warning
某些步驟可能會隨時間而變化，請參閱 Elastic 的手冊以獲取最新步驟。
:::

NetFlow Records 整合提供了一些可用於分析 NetFlow 資料的有用資產。在繼續之前，請確保先[安裝這些資產](https://www.elastic.co/guide/en/fleet/7.17/install-uninstall-integration-assets.html)。以下部分將介紹一些檢視 NetFlow 資料的基本方法。

1. [登入你的 Kibana](https://www.elastic.co/guide/en/kibana/current/access.html)
2. 在主選單中開啟“[儀表板](https://www.elastic.co/kibana/kibana-dashboard)”選單
3. 搜尋儀表板並找到“NetFlow”

你現在應該會看到多個 NetFlow 儀表板。例如，嘗試開啟“[Logs Netflow] Overview”。如果你的 NetFlow 資料已正確接收，那麼你現在應該會看到彙總流量的圖表。

另一個有用的儀表板是“[Logs Netflow] Flow records”，它會顯示精確的 NetFlow 記錄。一個非常有用的功能是過濾選項（頂部的 + 按鈕），它允許你向 NetFlow 資料新增過濾器；例如，你可以過濾記錄以僅顯示單個 IP 地址：

![Kibana NetFlow records view with a filter applied](/img/8bf2a1b59bba05eb.webp)

還有其他選項，例如搜尋特定時間範圍。你應該進一步閱讀有關 [Discover](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#find-the-data-you-want-to-use) 的內容，以更好地瞭解這些可能性。

為便於快速參考，以下是你最有可能用於搜尋 NetFlow 資料的欄位：

- source.ip
- source.port
- destination.ip
- destination.port
- network.transport

如果你想檢查單條記錄，建議使用 [Discover](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#find-the-data-you-want-to-use) 檢視。NetFlow 資料可透過“data\_stream.dataset: netflow.log”找到。

## 日誌保留 {#log-retention}

根據你當地的法律，你可能需要將 NetFlow 資料儲存指定的一段時間。請注意，繁忙的網路可能會生成大量 NetFlow 資料，甚至每天數 TB。你很可能需要調整[生命週期策略](https://www.elastic.co/guide/en/elasticsearch/reference/current/set-up-lifecycle-policy.html)。預設情況下，NetFlow 資料應歸入“logs”策略。如果你有多個 Elasticsearch 節點，你可以利用“[階段](https://www.elastic.co/guide/en/elasticsearch/reference/current/ilm-index-lifecycle.html)”，它允許你將資料儲存在不同型別的儲存介質上；但如果你只有一個 Elasticsearch 節點，你的選擇就有限，你很可能會想要[刪除](https://www.elastic.co/guide/en/elasticsearch/reference/current/ilm-delete.html)舊資料。例如，如果你想在 6 個月後刪除資料，那麼你可以簡單地更改 ILM 策略以在 6 個月後刪除資料，或使用以下 API 請求：

```json
PUT _ilm/policy/logs
{
  "policy": {
    "phases": {
      "hot": {
        "min_age": "0ms",
        "actions": {
          "rollover": {
            "max_age": "30d",
            "max_primary_shard_size": "50gb"
          },
          "set_priority": {
            "priority": 101
          }
        }
      },
      "delete": {
        "min_age": "180d",
        "actions": {
          "delete": {
            "delete_searchable_snapshot": true
          }
        }
      }
    }
  }
}
```

:::danger
如果你更改“logs”策略，這將應用於你的所有日誌，而不僅僅是 NetFlow 資料。如果你需要為其他日誌設定不同的保留期，那麼最好建立一個新的 ILM 策略，並指定 NetFlow 整合使用新建立的 ILM 策略。
:::

### 使用不同的 ILM 策略 {#use-a-different-ilm-policy}

如果你希望 NetFlow 資料具有不同的保留期，那麼你需要執行以下步驟：

1. 建立一個新的 ILM 策略，為其指定新名稱並設定刪除階段所需的期限，或使用以下 API 請求：  

   ```json
   PUT _ilm/policy/netflow-logs
   {
     "policy": {
       "phases": {
         "hot": {
           "min_age": "0ms",
           "actions": {
             "rollover": {
               "max_age": "30d",
               "max_primary_shard_size": "50gb"
             },
             "set_priority": {
               "priority": 101
             }
           }
         },
         "delete": {
           "min_age": "1000d",
           "actions": {
             "delete": {
               "delete_searchable_snapshot": true
             }
           }
         }
       }
     }
   }
   ```

2. 轉到 Kibana，開啟“堆疊管理”，然後轉到“索引管理”，再轉到“元件模板”。
3. 搜尋“logs-netflow.log@custom”，開啟並編輯它。
4. 轉到“索引設定”部分。
5. 貼上以下內容：  

   ```json
   {
     "index": {
       "lifecycle": {
         "name": "netflow-logs"
       }
     }
   }
   ```

6. 按下“下一步”，然後按下“儲存元件模板”。
