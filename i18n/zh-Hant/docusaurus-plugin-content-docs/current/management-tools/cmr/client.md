---
sidebar_key: "management-tools/cmr/client"
sidebar_position: 1
title: "CMR-用戶端"
sidebar_label: "CMR-用戶端"
description: "CMR 用戶端是裝置側元件，它連線到 CMR 伺服器並由其集中管理。"
tags:
  - 'cmr'
  - 'management'
source: https://manual.mikrotik.com/docs/management-tools/cmr/client
captured_at: '2026-11-09T11:35:47.715Z'
pagination_prev: "management-tools/cmr"
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

CMR 用戶端是一臺連線到 CMR 伺服器並由其集中管理的 RouterOS 裝置。CMR 用戶端功能包含在 RouterOS 主軟體包中。

:::warning
在採用 **smips** 和 **powerpc** 架構的裝置上不支援 CMR-client。
:::

[`CMR-Client CLI Reference`](../../cli-reference/cmr/client.md) 提供了 `/cmr/client` 選單中每個引數和命令的詳細說明。

## 啟用 CMR 用戶端 {#enable-the-cmr-client}

用戶端必須能夠透過 TCP 埠 `54321` 訪問 CMR 伺服器。請在伺服器的防火牆中以及用戶端與伺服器之間的任何防火牆中允許連線到此埠。

啟用用戶端並指定它應連線的 CMR 伺服器：

```ros
[admin@MikroTik] > /cmr/client set enabled=yes controller-addresses=192.168.88.1 pairing-requirement=password
```

`controller-addresses` 不是必需的，但當你希望用戶端連線到特定的 CMR 伺服器，或者用戶端無法透過鄰居發現或 DNS 自動發現伺服器時，建議設定它（CMR 指南的 [工作原理](../cmr.md#how-it-works) 部分對兩者都有說明）。

用戶端聯絡伺服器並報告其配對狀態。當前狀態及其連線的伺服器顯示在只讀引數 `status`、`controller-address` 和 `controller-identity` 中：

```ros
[admin@MikroTik] > /cmr/client print
  enabled: yes
  pairing-requirement: password
  controller-addresses: 192.168.88.1
  status: paired,connected
  controller-identity: CMR-1
  controller-address: 192.168.88.1
```

用戶端使用 `cmr` 主題記錄其 `status` 的每次變化，例如 `client status changed: paired,connected 192.168.88.1`，後跟伺服器地址。當與伺服器的連線斷開時，例如伺服器上的 CMR 重啟期間，用戶端會使用其現有配對重新連線。

## 將用戶端與伺服器配對 {#pair-the-client-to-the-server}

配對會將用戶端與 CMR 伺服器關聯起來。無論用戶端配置的 `pairing-requirement` 是什麼，在本地執行 `pair` 命令始終會從用戶端側批准配對：

```ros
[admin@MikroTik] > /cmr/client/pair username=admin password=secret
Columns: ADDRESS, STATUS
ADDRESS         STATUS
192.168.88.1    paired
```

用戶端與位於 `controller-addresses` 的伺服器配對。僅當伺服器配置為 `pairing-requirement=password` 時，才需要使用者名稱和密碼來滿足伺服器的要求。它們是伺服器上 RouterOS 使用者的憑據；CMR 沒有單獨的配對密碼。透過提供這些憑據，用戶端可遠端滿足伺服器的要求。

用戶端在 `/cmr/client` 選單中也有自己的 `pairing-requirement`，它定義了在用戶端接受配對之前伺服器必須執行的操作。與 CMR 伺服器一樣，用戶端支援 `none`、`password` 和 `confirm`，預設值為 `password`。使用 `confirm` 時，只有在用戶端上執行 `/cmr/client/pair` 後配對才會完成。[配對](../cmr.md#pairing) 部分說明了兩個裝置上的要求如何組合。

## 斷開用戶端連線 {#disconnect-the-client}

要忘記配對並斷開用戶端與伺服器的連線：

```ros
[admin@MikroTik] > /cmr/client/forget
```

停用用戶端（`/cmr/client set enabled=no`）會移除 CMR 在裝置上預配的配置。再次啟用它會使用現有配對重新連線用戶端。

## 故障排除 {#troubleshooting}

`/cmr/client print` 中的 `status` 和 `pairing-status` 值顯示連線或配對停止的位置。`pairing-status` 列出伺服器地址、伺服器的配對狀態（`cmr:`）以及用戶端自身的配對狀態（`device:`）。

- `status: searching` - 用戶端尚未找到 CMR 伺服器。請將 `controller-addresses` 設定為該伺服器的 IP 地址，或檢查用戶端能否透過 TCP 埠 `54321` 訪問該伺服器，以及防火牆是否允許該連線。
- `status: waiting-for-pairing,connected` 且 `pairing-status: 192.168.88.1: cmr:waiting confirmation, device:ok` - 用戶端已接受配對並處於已連線狀態，伺服器正在等待本地批准，因為其 `pairing-requirement` 為 `confirm`。在伺服器上，該裝置會列在 `/cmr/device` 中，並帶有 **P**（pending，待處理）標誌。請在伺服器上為該裝置執行 [`/cmr/device/pair`](../../cli-reference/cmr/device/pair.md)。
- `status: paired,disconnected`，且該裝置未列在伺服器上 - 用戶端仍保留著與一個已無法訪問的伺服器（例如先前的某個 CMR 伺服器）的配對。作為變通方法，請忘記該配對並重新啟用用戶端，使其與 `controller-addresses` 中的伺服器進行配對：

  ```ros
  [admin@MikroTik] > /cmr/client/forget
  [admin@MikroTik] > /cmr/client set enabled=yes controller-addresses=192.168.88.1
  ```

在 CMR 伺服器本身上，`/cmr/client print` 會顯示註釋 "settings ignored because used by local controller"。該伺服器透過其本地控制器管理自身，因此伺服器上的 `/cmr/client` 設定不會生效。
