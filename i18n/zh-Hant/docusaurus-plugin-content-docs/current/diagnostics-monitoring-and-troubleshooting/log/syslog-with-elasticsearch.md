---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/log/syslog-with-elasticsearch"
sidebar_position: 2
title: "使用 Elasticsearch 的 Syslog"
sidebar_label: "使用 Elasticsearch 的 Syslog"
description: "本指南介紹如何使用 Elasticsearch、Kibana 和 Fleet Server 配合 MikroTik RouterOS 裝置來配置 Syslog 資料收集與分析。內容涵蓋前提條件、Elastic 與 RouterOS 兩個元件的設定步驟，包括建立 agent policy 以及配置 Custom UDP logs 整合。"
tags:
  - 'syslog'
  - 'elasticsearch'
  - 'kibana'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/log/syslog-with-elasticsearch
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

Elasticsearch 是一種流行的 NoSQL 資料庫，可用於儲存各種資料，包括 Syslog 資料。配合 Kibana，你可以建立一個強大的工具來分析來自 RouterOS 裝置的 Syslog 資料。本指南將依賴 Elasticsearch 整合，要使其正常工作，你需要有一個可用的 Elasticsearch 環境。本指南不會涵蓋 Elasticsearch 和 Kibana 的安裝說明，但會涵蓋設定 Syslog 資料收集與分析的相關步驟。

使用 Elasticsearch 可以進行多種配置，但本指南將採用以下原則：

- 一臺 RouterOS (10.0.0.1) 裝置將 Syslog 資料傳送到執行 [Custom UDP logs](https://www.elastic.co/docs/current/integrations/udp) 的伺服器 (10.0.0.2)。
- 執行 Custom UDP logs 整合的伺服器 (10.0.0.2) 接收 Syslog 資料，處理資料並將其傳送到 [Fleet Server](https://www.elastic.co/guide/en/fleet/current/fleet-server.html) (10.0.0.3)。
- Fleet Server (10.0.0.3) 將資料儲存在 [Elasticsearch](https://www.elastic.co/elasticsearch) (10.0.0.4) 中。
- [Kibana](https://www.elastic.co/kibana) (10.0.0.5) 從 Elasticsearch (10.0.0.4) 檢索資料，進行分析，並允許你搜尋這些資料。

:::info
本指南不會使用 [Logstash](https://www.elastic.co/logstash) 作為分析 Syslog 資料的一部分；它已被 Fleet Server 取代。

:::

:::info
可以將 Elasticsearch、Kibana、Fleet Server 和 Custom UDP logs 整合安裝在同一臺裝置上。

:::

## 先決條件 {#prerequisites}

- [設定 Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html)。  
  :::info
  Elasticsearch 在許多平臺上得到廣泛支援。建議設定一個 Elasticsearch 節點叢集。
  :::
- [設定 Kibana](https://www.elastic.co/guide/en/kibana/current/setup.html)。  
  :::info
  Kibana 可以安裝在與 Elasticsearch 相同的裝置上，但出於效能原因，也可以安裝在單獨的裝置上。雖然不使用 Kibana 也可以分析 Syslog 資料，但這需要編寫你自己的 API 請求；不過 Kibana 非常易於使用，並且具有廣泛的功能。
  :::
- [Set up Fleet Server](https://www.elastic.co/guide/en/fleet/current/add-fleet-server-on-prem.html).  
  :::info
  可以在安裝 Elasticsearch 和/或 Kibana 的同一臺裝置上設定 Fleet Server。建議將 Fleet Server 安裝在其他裝置上。有關硬體和拓撲要求的建議，請參閱 Elasticsearch 手冊。
  :::

## 設定 {#set-up}

設定說明分為兩部分：Elastic（有關 Elasticsearch、Kibana 和 Fleet Server 的配置）和 RouterOS（與您的 RouterOS 裝置相關的配置）。

### Elastic {#elastic}

:::warning
某些步驟可能會隨時間而變化。請參閱 Elastic 的手冊以獲取最新步驟。

:::

1. [登入到你的 Kibana](https://www.elastic.co/guide/en/kibana/current/access.html)。
2. 在主選單下開啟 [Fleet](https://www.elastic.co/guide/en/kibana/current/fleet.html) 部分。
3. 開啟“[Agent policies](https://www.elastic.co/guide/en/fleet/current/agent-policy.html)”部分。
4. 按下“建立 Agent 策略”按鈕以[建立新的 Agent 策略](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#create-a-policy)。
5. 為該策略命名，例如“Syslog policy”，根據需要調整高階設定，然後建立策略。或者你可以使用下面的 API 請求：  

   ```text
   POST kbn:/api/fleet/agent_policies
   {
     "name": "Syslog policy",
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

6. 單擊其名稱，開啟你新建的策略。
7. 按下“[新增整合](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#add-integration)”。
8. 搜尋“[Custom UDP logs](https://www.elastic.co/docs/current/integrations/udp)”並按下“新增 Custom UDP logs”。
9. 調整配置，並確保：  
   - 將“Listen Address”設定為將要執行 Custom UDP logs 整合的伺服器的 IP 地址，在本示例中該地址應為“10.0.0.2”。  
   - 將“Listen Port”設定為“5514”。  
   - 將“Dataset name”設定為“routeros”。  
   - 將“Ingest Pipeline”設定為“logs-routeros@custom”。  
   - 將“Syslog Parsing”設定為“Yes”。
10. 儲存該整合。
11. 按下“[將 Elastic Agent 新增到你的主機](https://www.elastic.co/guide/en/fleet/current/elastic-agent-installation.html)”按鈕。
12. 按照說明將 Elastic Agent 新增到你的主機。  
    :::info
    Elastic 官方手冊建議將 Elastic Agent 安裝為 Fleet 管理。建議遵循該建議，因為當代理由 Fleet 管理時，管理代理會更容易。
    :::
13. 轉到主選單上的“堆疊管理”，然後開啟“[攝取管道](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html)”。
14. 透過按下“[建立管道](https://www.elastic.co/guide/en/fleet/current/data-streams-pipeline-tutorial.html#data-streams-pipeline-one)”，然後選擇“新建管道”來建立新的 Ingest Pipeline。
15. 將“Name”設定為“logs-routeros@custom”。
16. 按下“匯入處理器”並貼上以下處理器：  

    ```json
    {
    	"processors": [
    		{
    			"grok": {
    			"field": "message",
    			"patterns": [
    				"^first L2TP UDP packet received from %{IP:source.ip}$",
    				"^login failure for user %{USERNAME:user.name} from %{IP:source.ip} via %{DATA:service.name}$",
    				"^%{USERNAME:user.name} logged in, %{IP:client.ip} from %{IP:source.ip}$",
    				"^dhcp alert on %{DATA}: discovered unknown dhcp server, mac %{MAC:source.mac}, ip %{IP:source.ip}$",
    				"in:%{DATA} out:%{DATA}, ?(connection-state:%{DATA},|)?(src-mac %{MAC:source.mac},|) proto %{DATA:network.transport} \\(%{DATA}\\), %{IP:source.ip}:?(%{INT:source.port}|)->%{IP:destination.ip}:?(%{INT:destination.port}|), len %{INT:network.bytes}$",
    				"in:%{DATA} out:%{DATA}, ?(connection-state:%{DATA},|)?(src-mac %{MAC:source.mac},|) proto %{DATA:network.transport}, %{IP:source.ip}:?(%{INT:source.port}|)->%{IP:destination.ip}:?(%{INT:destination.port}|), len %{INT:network.bytes}$",
    				"^%{DATA:network.name} (deassigned|assigned) %{IP:client.ip} for %{MAC:client.mac} %{DATA}$",
    				"^%{DATA:user.name} logged out, %{INT:event.duration} %{INT} %{INT} %{INT} %{INT} from %{IP:client.ip}$",
    				"^user %{DATA:user.name} logged out from %{IP:source.ip} via %{DATA:service.name}$",
    				"^user %{DATA:user.name} logged in from %{IP:source.ip} via %{DATA:service.name}$",
    				"^%{DATA:network.name} client %{MAC:client.mac} declines IP address %{IP:client.ip}$",
    				"^%{DATA:network.name} link up \\(speed %{DATA}\\)$",
    				"^%{DATA:network.name} link down$",
    				"^user %{DATA:user.name} authentication failed$",
    				"^%{DATA:network.name} fcs error on link$",
    				"^phase1 negotiation failed due to time up %{IP:source.ip}\\[%{INT:source.port}\\]<=>%{IP:destination.ip}\\[%{INT:destination.port}\\] %{DATA}:%{DATA}$",
    				"^%{DATA:network.name} (learning|forwarding)$",
    				"^user %{DATA:user.name} is already active$",
    				"^%{GREEDYDATA}$"
    			]
    			}
    		},
    		{
    			"lowercase": {
    			"field": "network.transport",
    			"ignore_missing": true
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.category",
    			"description": "Enrich logon events",
    			"allow_duplicates": false,
    			"value": [
    				"authentication"
    			],
    			"if": "ctx.message =~ /(login failure for user|logged in from|logged in,)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.outcome",
    			"description": "Enrich successful login events",
    			"allow_duplicates": false,
    			"value": [
    				"success"
    			],
    			"if": "ctx.message =~ /(logged in from|logged in,)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.outcome",
    			"description": "Enrich failed login events",
    			"allow_duplicates": false,
    			"value": [
    				"failure"
    			],
    			"if": "ctx.message =~ /(login failure for user)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.category",
    			"description": "Enrich network events",
    			"allow_duplicates": false,
    			"value": [
    				"network"
    			],
    			"if": "ctx.message =~ /( fcs error on link| link down| link up)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.outcome",
    			"description": "Enrich network failures",
    			"allow_duplicates": false,
    			"value": [
    				"failure"
    			],
    			"if": "ctx.message =~ /( fcs error on link)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.category",
    			"allow_duplicates": false,
    			"value": [
    				"session"
    			],
    			"if": "ctx.message =~ /(logged out)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.category",
    			"allow_duplicates": false,
    			"value": [
    				"threat"
    			],
    			"if": "ctx.message =~ /(from address that has not seen before)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "service.name",
    			"value": [
    				"l2tp"
    			],
    			"if": "ctx.message =~ /(^L2TP\\/IPsec VPN)/"
    			}
    		},
    		{
    			"geoip": {
    			"ignore_failure": true,
    			"ignore_missing": true,
    			"field": "source.ip",
    			"target_field": "source.geo"
    			}
    		},
    		{
    			"geoip": {
    			"ignore_failure": true,
    			"ignore_missing": true,
    			"field": "destination.ip",
    			"target_field": "destination.geo"
    			}
    		},
    		{
    			"geoip": {
    			"ignore_failure": true,
    			"ignore_missing": true,
    			"field": "client.ip",
    			"target_field": "client.geo"
    			}
    		}
    	]
    }
    ```

17. 按下“儲存管道”。
18. 轉到主選單上的“堆疊管理”，然後選擇“索引管理”，再選擇“元件模板”。
19. 透過按下“建立元件模板”來建立新模板。
20. 將“Name”設定為“logs-routeros@custom”。
21. 在“索引設定”部分下，貼上以下內容：  

    ```json
    {
      "index": {
        "lifecycle": {
          "name": "logs"
        },
        "default_pipeline": "logs-routeros@custom"
      }
    }
    ```

    :::info
    將 ILM 策略更改為你所需的策略名稱。“logs”策略是預設策略，可能正用於其他日誌。
    :::
22. 在“對映”部分下，按下“載入 JSON”並貼上以下內容：  

    ```json
    {
      "dynamic_templates": [],
      "properties": {
        "service": {
          "type": "object",
          "properties": {
            "name": {
              "type": "keyword"
            }
          }
        },
        "destination": {
          "type": "object",
          "properties": {
            "port": {
              "type": "long"
            },
            "ip": {
              "type": "ip"
            }
          }
        },
        "host": {
          "type": "object",
          "properties": {
            "ip": {
              "type": "ip"
            }
          }
        },
        "client": {
          "type": "object",
          "properties": {
            "ip": {
              "type": "ip"
            },
            "mac": {
              "type": "keyword"
            }
          }
        },
        "source": {
          "type": "object",
          "properties": {
            "geo": {
              "type": "object",
              "properties": {
                "continent_name": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "region_iso_code": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "city_name": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "country_iso_code": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "country_name": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "location": {
                  "type": "geo_point"
                },
                "region_name": {
                  "ignore_above": 1024,
                  "type": "keyword"
                }
              }
            },
            "as": {
              "type": "object",
              "properties": {
                "number": {
                  "type": "long"
                },
                "organization": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "ignore_above": 1024,
                      "type": "keyword",
                      "fields": {
                        "text": {
                          "type": "match_only_text"
                        }
                      }
                    }
                  }
                }
              }
            },
            "address": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "port": {
              "type": "long"
            },
            "domain": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "ip": {
              "type": "ip"
            },
            "mac": {
              "type": "keyword"
            }
          }
        },
        "event": {
          "type": "object",
          "properties": {
            "duration": {
              "type": "long"
            },
            "category": {
              "type": "keyword"
            },
            "outcome": {
              "type": "keyword"
            }
          }
        },
        "message": {
          "type": "match_only_text"
        },
        "user": {
          "type": "object",
          "properties": {
            "name": {
              "type": "keyword"
            }
          }
        },
        "network": {
          "type": "object",
          "properties": {
            "bytes": {
              "type": "long"
            },
            "name": {
              "type": "keyword"
            },
            "transport": {
              "type": "keyword"
            }
          }
        },
        "tags": {
          "ignore_above": 1024,
          "type": "keyword"
        }
      }
    }
    ```

23. 按下“下一步”，然後按下“儲存元件模板”。  
    :::warning
    如果已存在具有該名稱的元件模板，請改為編輯現有模板。
    :::
24. 轉到主選單上的“堆疊管理”，然後選擇“索引管理”，再選擇“索引模板”。
25. 透過按下“建立模板”來建立新模板。
26. 將“Name”設定為“logs-routeros”。
27. 將“Index patterns”設定為“logs-routeros-\*”。
28. 在“元件模板”部分下，將以下模板新增到新的 Index template：  

    ```text
    logs@settings
    logs-routeros@custom
    ecs@mappings
    ```

29. 按下“下一步”，然後按下“儲存模板”。
30. 確保你已在主機上以及從 RouterOS 裝置 (10.0.0.1) 路徑中的其他位置開啟 5514/UDP 埠。
31. 你的 Elastic Agent 現在已準備好接收 Syslog 資料！

### RouterOS {#routeros}

1. 在您的 RouterOS 裝置 (10.0.0.1) 上配置[遠端日誌記錄動作](./index.md#send-the-log-to-a-syslog-server)：

   ```ros
   /system/logging/action
   set [find where name="remote"] remote-log-format=syslog \
       remote=10.0.0.2 remote-port=5514 syslog-facility=syslog
   ```

2. 為你希望從 RouterOS 裝置（10.0.0.1）接收的每個[主題](./index.md#topics)新增一條規則，例如：

   ```ros
   /system/logging
   add action=remote topics=info
   add action=remote topics=error
   add action=remote topics=critical
   add action=remote topics=warning
   add action=remote topics=bridge,stp
   ```

3. 你現在應該開始看到 Syslog 資料被攝取。
4. 繼續閱讀本指南以開始使用 Kibana。

## 使用 Kibana {#using-kibana}

Kibana 允許你搜尋已攝取的 Syslog 資料。要檢視已攝取的日誌，請執行以下操作：

1. [登入到您的 Kibana](https://www.elastic.co/guide/en/kibana/current/access.html)。
2. 從主選單開啟“Discover”。
3. [新增篩選器](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#explore-fields-in-your-data)，並使用以下引數：  

   ```text
   Select a field: data_stream.dataset
   Select operator: IS
   Select a value: routeros
   ```

4. 為簡單起見，我們建議在 Discover 選單中[搜尋欄位](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#explore-fields-in-your-data)，搜尋 "message"，然後將其新增到檢視中。
5. 我們還建議搜尋 "log.syslog.hostname" 欄位，並將其也新增到檢視中。
6. 考慮[儲存搜尋](https://www.elastic.co/guide/en/kibana/current/save-open-search.html#_save_a_search)以便以後更輕鬆地訪問。
7. 完成。

:::tip
雖然搜尋日誌可能很有用，但你更可能是在尋找一種方式，為某些活動建立[告警](https://www.elastic.co/guide/en/kibana/current/alerting-getting-started.html)，並建立[聯結器](https://www.elastic.co/guide/en/kibana/current/action-types.html)以將告警傳送到電子郵件、webhook、聊天和其他選項。考慮啟用[登入失敗事件激增](https://www.elastic.co/guide/en/security/current/spike-in-failed-logon-events.html)規則，以便在登入失敗嘗試過多時發出告警。你還可以建立[閾值規則](https://www.elastic.co/guide/en/observability/current/metrics-threshold-alert.html)，並將其設定為在固定數量的登入失敗後發出告警。

:::
