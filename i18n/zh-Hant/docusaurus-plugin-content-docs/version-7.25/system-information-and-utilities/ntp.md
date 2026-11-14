---
sidebar_key: "system-information-and-utilities/ntp"
sidebar_position: 10
title: "NTP"
sidebar_label: "NTP"
description: "RouterOS 在主軟體包中包含 NTP 用戶端和伺服器：可將路由器時鐘與 NTP 伺服器同步、向其他裝置提供時間、使用對稱金鑰認證，並監控同步狀態。"
tags:
  - 'ntp'
  - 'time-synchronization'
source: https://manual.mikrotik.com/docs/7.25/system-information-and-utilities/ntp
captured_at: '2026-11-04T11:22:11+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 在主軟體包中包含網路時間協定（NTP，[RFC 5905](https://www.rfc-editor.org/rfc/rfc5905.html)）用戶端和伺服器。用戶端會將路由器時鐘與 NTP 伺服器同步，伺服器則會將路由器時間分發給網路中的其他裝置。兩者預設均處於停用狀態。NTP 交換的是協調世界時 (UTC)；顯示時間所用的時區和夏令時規則在 [`/system/clock`](./clock.md) 中配置。

## 同步路由器時鐘 {#synchronize-the-routers-clock}

啟用用戶端，並設定一個或多個伺服器：

```ros
[admin@MikroTik] > /system/ntp/client/set enabled=yes servers=192.168.88.1
[admin@MikroTik] > /system/ntp/client/print
         enabled: yes
            mode: unicast
         servers: 192.168.88.1
             vrf: main
      freq-drift: 0 PPM
          status: synchronized
   synced-server: 192.168.88.1
   synced-stratum: 3
   system-offset: 13.937 ms
```

要在 WinBox 中配置用戶端，請開啟 **System > NTP Client**：

1. 選擇 **Enabled**，對於直接查詢的伺服器，將 **Mode** 保留為 `unicast`。
2. 在 **NTP Servers** 中輸入伺服器地址，例如，如果該裝置提供 NTP，則填寫 `192.168.88.1`。使用 **+** 控制元件新增更多伺服器，然後選擇 **Apply**。
3. 檢查 **Status**。當其顯示 `synchronized` 時，**Synced Server**、**Synced Stratum** 和 **System Offset** 會顯示所選源及其計時資訊。選擇 **OK** 關閉對話方塊。

![WinBox NTP Client dialog synchronized to 192.168.88.1](/img/d415d6c80c25c29b.webp)

`status` 欄位顯示用戶端狀態：用戶端停用時為 `stopped`，沒有可用伺服器時為 `waiting`，時鐘跟隨 `synced-server` 時為 `synchronized`。有多個伺服器時，用戶端會輪詢所有伺服器並選擇最佳的一個。

伺服器可以是 IPv4 或 IPv6 地址，也可以是域名（透過 [`/ip/dns`](../network-management/dns.md) 解析；結果顯示為 `resolved-address`）。伺服器在 [`/system/ntp/client/servers`](../cli-reference/system/ntp/client/servers.md) 列表中管理。當 DHCP 用戶端設定了 `use-peer-ntp=yes`（預設值）時，透過 DHCP 收到的伺服器會作為動態條目出現在列表中，這些條目無法編輯：

```ros
[admin@MikroTik] > /system/ntp/client/servers/print
Flags: D - DYNAMIC
0   address=192.168.88.1 min-poll=6 max-poll=10 iburst=yes auth-key=none

1 D address=217.198.224.12 min-poll=6 max-poll=10 iburst=yes auth-key=none

2 D address=195.244.128.12 min-poll=6 max-poll=10 iburst=yes auth-key=none
```

用戶端以介於 `min-poll` 和 `max-poll` 之間的間隔查詢伺服器，該間隔以秒為單位，取 2 的冪（預設在 64 秒到 1024 秒之間）。伺服器剛新增後，用戶端會立即以每秒一次的頻率快速傳送一組查詢（iburst），以便快速獲得初始估計。

用戶端預設以 unicast 模式工作，直接查詢每個伺服器。`broadcast`、`multicast` 和 `manycast` 模式則從在本地網路上通告時間的伺服器獲取時間。在 manycast 模式下，用戶端會透過組播查詢自行發現伺服器。

## 向其他裝置提供時間 {#serve-time-to-other-devices}

啟用伺服器，以應答來自網路的時間查詢：

```ros
[admin@MikroTik] > /system/ntp/server/set enabled=yes
```

在 WinBox 中，開啟 **System > NTP Server**：

1. 選擇 **Enabled** 並選擇 **OK**，以允許用戶端查詢路由器時間。請單獨配置 NTP 用戶端，以便路由器擁有已同步的時間源。
2. 在啟用回退到路由器未同步時鐘之前，請檢查 **Use Local Clock** 和 **Local Clock Stratum**。當你需要外部時間源時，請保持 **Use Local Clock** 未選中。

![WinBox NTP Server dialog with local clock fallback settings](/img/fa68dfc1500bb0b8.webp)

隨後，伺服器會分發路由器自身的已同步時間。使用 `broadcast=yes` 時，時間還會發送到 `broadcast-addresses` 中的地址；`multicast=yes` 會透過組播分發時間；`manycast=yes` 會參與 manycast 發現。

:::warning
使用 `use-local-clock=yes` 時，如果沒有可用的 NTP 源，路由器的未同步時鐘會被用作時間參考（使用 `local-clock-stratum`，預設為 5）。在沒有外部同步的情況下，路由器時鐘會發生漂移，因為其頻率會隨電源管理、溫度和硬體差異而變化，因此不要為精確計時提供本地時鐘。應優先使用網路時間源。
:::

當本地時鐘是唯一參考時，處於此狀態的用戶端會顯示 `status: using-local-clock` 和 `synced-server: 127.127.1.0`。

## 對用戶端和伺服器進行身份驗證 {#authenticate-clients-and-servers}

在 [`/system/ntp/key`](../cli-reference/system/ntp/key.md) 中配置的對稱金鑰用於對時間交換進行身份驗證。建立金鑰，並透過 `auth-key` 在用戶端的伺服器條目上選擇它：

```ros
[admin@MikroTik] > /system/ntp/key/add key-id=10 key-val=mysecret
[admin@MikroTik] > /system/ntp/client/servers/set 0 auth-key=10
```

金鑰值是敏感資訊：`print` 和 `export` 永遠不會顯示它。未透過身份驗證的回覆會被拒絕，日誌會顯示 `peer rejected auth (crypto NAK)`，用戶端會保持 `waiting` 狀態。

## 監控同步 {#monitor-synchronization}

`/system/ntp/monitor-peers` 顯示用戶端對其時間源的檢視，並持續重新整理：

```ros
[admin@MikroTik] > /system/ntp/monitor-peers
 type="ucast-client" address=192.168.88.1 refid="195.244.128.12" stratum=3
 hpoll=6 ppoll=6 root-delay=15.96 ms root-disp=65.368 ms offset=13.937 ms
 delay=0.566 ms disp=0.123 ms jitter=0.02 ms
```

`refid` 是對等體自身同步到的源。`stratum` 為 16 表示該對等體未同步。

路由器時鐘的估計頻率校正值在用戶端設定中顯示為 `freq-drift`；可使用 [`/system/ntp/client/reset-freq-drift`](../cli-reference/system/ntp/client/reset-freq-drift.md) 重設它。

## 技術細節 {#technical-details}

### NTP 日誌記錄 {#ntp-logging}

為 `ntp` 主題新增日誌記錄規則，以檢視用戶端的決策和封包交換：

```ros
[admin@MikroTik] > /system/logging/add topics=ntp
```

啟動和同步期間的典型訊息：

```text
ntp,debug tx dst:192.168.88.1
ntp,debug rx src:192.168.88.1 dst:192.168.88.24
ntp,debug Message offset:0.027406 delay:0.000597 disp:0.000002
ntp,debug Resolved address: time.cloudflare.com -> 162.159.200.1
ntp,debug Checking peer (195.244.128.12). Peer is: NOT FIT, because p->leap == NOSYNC
ntp,debug No survivors for clock sync
ntp,debug System peer changed to: 195.244.128.12
ntp,debug peer rejected auth (crypto NAK)
```

一個 `NOT FIT, because p->leap == NOSYNC` 的對等體正在應答，但其自身未同步。`rootDist` 拒絕表示源距離根時鐘太遠。

### 用戶端和伺服器作用域 {#client-and-server-scopes}

用戶端和伺服器獨立配置；啟用其中一個並不要求啟用另一個。兩者都有 `vrf` 設定（預設為 `main`），用於限定 NTP 流量使用哪個路由表。

有關所有屬性，請參閱 CLI 參考中的 [`/system/ntp/client`](../cli-reference/system/ntp/client/index.md)、[`/system/ntp/client/servers`](../cli-reference/system/ntp/client/servers.md)、[`/system/ntp/server`](../cli-reference/system/ntp/server.md)、[`/system/ntp/key`](../cli-reference/system/ntp/key.md) 和 [`/system/ntp/monitor-peers`](../cli-reference/system/ntp/monitor-peers.md)。
