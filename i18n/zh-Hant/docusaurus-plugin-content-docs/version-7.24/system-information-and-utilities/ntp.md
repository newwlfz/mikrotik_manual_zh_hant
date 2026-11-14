---
sidebar_key: "system-information-and-utilities/ntp"
sidebar_position: 11
title: "NTP"
sidebar_label: "NTP"
description: "RouterOS 的 NTP 文件涵蓋用戶端和伺服器配置，包括啟用的模式、支援 IPv4/IPv6 的伺服器列表、VRF 設定、認證金鑰，以及頻率漂移和同步 stratum 等狀態監控。它還警告不要使用本地時鐘進行精確計時，並列出了 NTP 日誌訊息。"
tags:
  - 'ntp'
  - 'time-synchronization'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/ntp
captured_at: '2026-11-04T11:33:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 主包包含 Network Time Protocol (NTP) 用戶端和伺服器功能，其基於 RFC5905。

### NTP 用戶端屬性 {#ntp-client-properties}

用戶端配置位於 `/system/ntp/client`

| 屬性 | 描述 |
| :-- | :-- |
| **enabled** (*yes、no，預設：no*) | 啟用 NTP 用戶端進行時間同步 |
| **mode** (*broadcast, manycast, multicast, unicast*) | NTP 用戶端將執行的模式 |
| **NTP 伺服器** | NTP 伺服器列表。可以新增靜態條目。接受以下格式：  - FQDN（如果地址已解析，"Resolved Address" 將出現在 "Servers" 視窗的相應列中）或可以使用 IP 地址。如果 DHCP-Client 屬性 **use-peer-ntp=yes** - 由 [DHCP](../network-management/dhcp.md) 通告的動態條目  - *ipv4*  - *ipv4*`@`*vrf*  - *ipv6*  - *ipv6*`@`*vrf*  - *ipv6-linklocal*`%`*interface* |
| **vrf** (*預設：main*) | 虛擬路由轉發 |
| **伺服器** (*按鈕/區域*) | 動態和靜態新增的 NTP 伺服器的詳細表格（Address、Resolved address、Min Poll、Max Poll、iBurst、Auth. Key）  使用其 FQDN 設定 NTP 伺服器。每次傳送 NTP 請求時都會解析域名。路由器必須配置 *`/ip/dns`*。 |
| **對等體** | 當前引數值  `[admin@ntp-example_v7] > /system/ntp/monitor-peers``type="ucast-client" address=x.x.x.x refid="y.y.y.y" stratum=3 hpoll=10 ppoll=10 root-delay=28.869 ms root-disp=50.994 ms``offset=-0.973 ms delay=0.522 ms disp=15.032 ms jitter=0.521 ms``-- [Q quit  D dump  C-z pause]` |
| **金鑰** | NTP 對稱金鑰，用於 NTP 用戶端與伺服器之間的身份驗證。金鑰識別符號 (Key ID) - 一個整數，用於標識生成訊息認證碼所使用的加密金鑰。  |

#### 狀態 {#status}

- **synchronized, stopped, waiting, using-local-clock** - NTP 用戶端的當前狀態。
- **頻率漂移** - 單位時間內的分數頻率漂移。
- **synced-server** - NTP 伺服器的 IP 地址。
- **synced-stratum** - 每臺伺服器的精度由一個稱為 stratum 的數字定義，最頂層（主伺服器）賦值為 1，層次結構中每向下一級（輔助伺服器）賦值為比前一級大 1。
- **system-offset** - 這是一個有符號定點數，表示 NTP 伺服器時鐘相對於本地時鐘的偏移量，單位為秒。

### NTP 用戶端伺服器屬性 {#ntp-client-servers-properties}

用戶端配置位於 `/system/ntp/client/servers`

| 屬性 | 描述 |
| :-- | :-- |
| **enabled** (*yes \| no；預設：yes*) | 啟用 NTP 用戶端伺服器。 |
| **comment** (*string；* 預設： ) | 條目的描述性名稱。 |
| **address** (IPv4 地址 [IPv4]*，IPv6 地址 [IPv6]，* 域名；預設： ) | NTP 伺服器的 IP 地址或域名。 |
| **resolved-address** (IPv4 地址 [IPv4]*，IPv6 地址 [IPv6]；預設：* ) | 域名解析後獲得的 NTP 伺服器實際 IP 地址。 |
| **min-poll** (*integer：* 3..17；預設：6) | 確定 NTP 查詢之間的最短間隔（以秒為單位的 2 的冪）。更多詳細資訊可在 [RFC5905](https://www.rfc-editor.org/rfc/rfc5905.html) 中找到。 |
| **max-poll** (*integer*：3..17；預設：10) | 確定 NTP 查詢之間的最長間隔（以秒為單位的 2 的冪）。更多詳細資訊可在 [RFC5905](https://www.rfc-editor.org/rfc/rfc5905.html) 中找到。 |
| **iburst**(*yes \| no；預設：yes*) | 確定初始突發是停用還是啟用。IBurst 告知 NTP 用戶端僅在啟動時傳送快速封包突發。更多詳細資訊可在 [RFC5905](https://www.rfc-editor.org/rfc/rfc5905.html) 中找到。 |
| **auth-key** (預設值：*none*) | NTP 對稱金鑰，用於 NTP 用戶端與伺服器之間的身份驗證。金鑰識別符號 (Key ID) - 一個整數，用於標識生成訊息認證碼所使用的加密金鑰。 |

### NTP 伺服器設定 {#ntp-server-settings}

伺服器配置位於 `/system/ntp/server`

| 屬性 | 描述 |
| :-- | :-- |
| **enabled** (*yes* 或 *no*；預設值：*no*) | 啟用 NTP 伺服器 |
| **broadcast** (*yes* 或 *no*；預設值：*no*) | 啟用某個 NTP 伺服器模式；要使此模式生效，必須設定 broadcast-addresses 欄位 |
| **multicast** (*yes* 或 *no*；預設值：*no*) | 啟用某個 NTP 伺服器模式 |
| **manycast** (*yes* 或 *no*；預設值：*no*) | 啟用某個 NTP 伺服器模式 |
| **broadcast-addresses** (*IP 地址*；預設值： ) | 設定用於 NTP 伺服器廣播模式的廣播地址 |
| **vrf** (*預設：main*) | 虛擬路由轉發 |
| **use-local-clock** (*yes* 或 *no*；預設值：*no*) | 如果其他時間源不可用，伺服器將提供其本地系統時間作為有效時間。 |
| **local-clock-stratum** | 如果 **use-local-clock=yes**，則手動設定 stratum |
| **auth-key** (預設值：*none*) | NTP 對稱金鑰，用於 NTP 用戶端與伺服器之間的身份驗證。金鑰識別符號 (Key ID) - 一個整數，用於標識生成訊息認證碼所使用的加密金鑰。 |

:::danger
如果使用 use-local-clock，請注意，路由器的內部 CPU 時鐘並非用於精確計時操作的可靠時間源，因為其頻率可能會因電源管理、熱條件和硬體差異而變化，甚至相同型號之間也會不同。這種變化是預期內的，不會影響路由器的正常效能。為了準確計時，建議使用基於網路的時間同步，例如 NTP (Network Time Protocol)。
:::

### 日誌訊息 {#log-messages}

SNTP 用戶端可以生成以下日誌訊息。有關如何設定日誌記錄以及如何檢查日誌，請參閱文章 “[log](../diagnostics-monitoring-and-troubleshooting/log/index.md)”。

- **ntp**、**debug** 按 *OFFS* 逐步調整。
- **ntp**、**debug** 按 *OFFS* 立即調整。
- **ntp**、**debug** 傳送下一條訊息前等待 *N* 秒。
- **ntp**、**debug** 重新啟動前等待 *N* 秒。
- **ntp**、**debug**、**packet** 封包接收出錯，正在重新啟動。
- **ntp**、**debug**、**packet** 收到 *PKT*。
- **ntp**、**debug**、**packet** 忽略收到的 *PKT*。
- **ntp**、**debug**、**packet** 傳送到 *IP* 時出錯，正在重新啟動。
- **ntp**、**debug**、**packet** 正在向 *IP* 傳送 *PKT*。

#### 日誌訊息欄位說明 {#explanation-of-log-message-fields}

- *OFFS* - 兩個 NTP 時間戳值之間的差值，以十六進位制表示。
- *PKT* - NTP 封包的轉儲。如果封包短於最小 48 位元組，則將其轉儲為十六進位制字串。否則，封包將轉儲為欄位名和值列表，每行日誌一個。欄位名遵循 RFC4330。
- *IP* - 遠端 IP 地址。

**注意**：上述日誌規則僅適用於內建 SNTP 用戶端；獨立的 NTP 包沒有任何日誌功能。
