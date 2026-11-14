---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/dynamic-dns"
sidebar_position: 18
title: "DNS 更新"
sidebar_label: "DNS 更新"
description: "DNS 更新工具會向某個區域的權威 DNS 伺服器傳送一條 RFC 2136 動態更新，該更新使用 TSIG hmac-md5 金鑰進行簽名，用於將某個名稱指向一個 IPv4 地址。"
tags:
  - 'dns-updates'
  - 'dynamic-ip'
  - 'hmac-md5'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/dynamic-dns
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

`/tool/dns-update` 命令會向某個區域的權威 DNS 伺服器傳送一條動態更新（RFC 2136），並把該區域中的某個名稱指向一個 IPv4 地址。該更新使用 TSIG 金鑰（RFC 8945）簽名，因此伺服器可以驗證該更新來自你，就像安全動態更新（RFC 3007）那樣。請把它用於你自己執行的區域，例如 BIND 伺服器上的區域。

在以下兩種常見情況下，你並不需要此命令：

- 如果某個名稱需要跟隨路由器自身的公網地址，而又不想執行 DNS 伺服器，請使用 [雲](../network-management/cloud/index.md#ddns) 的 DDNS 服務。
- 透過 HTTP 接收更新的動態 DNS 服務（例如 DynDNS）則應使用 [獲取](../system-information-and-utilities/fetch.md) 來更新。

## 先決條件 {#prerequisites}

- 一臺對該區域具有權威性、並透過 TCP 埠 53 接受動態更新的 DNS 伺服器。
- 伺服器接受用於更新該區域的 TSIG 金鑰，演算法為 hmac-md5。RouterOS 僅使用 hmac-md5 簽名；該命令沒有演算法設定。
- 金鑰的名稱及其 base64 編碼的金鑰值，與伺服器上的配置一致。例如在 BIND 上，使用 `tsig-keygen -a hmac-md5 dns-update-key` 建立金鑰，因為 BIND 預設使用另一種演算法建立金鑰；並只允許該金鑰更新它所需的名稱（`update-policy`）。
- 路由器時鐘與伺服器時鐘的偏差小於 5 分鐘。簽名允許 300 秒的偏差，因此請保持時鐘與 [NTP](../system-information-and-utilities/ntp.md) 同步。
- 伺服器側的防火牆允許來自路由器的 TCP 埠 53。

## 讓名稱指向某個地址 {#point-a-name-at-an-address}

在 DNS 伺服器 192.0.2.53 上，使用金鑰 `dns-update-key` 把 `office.example.com` 指向 198.51.100.20。請把 `key` 的值替換為你金鑰的 base64 金鑰值，並保留引號，因為 base64 值可能以 `=` 結尾：

```ros
/tool/dns-update dns-server=192.0.2.53 zone=example.com \
    name=office address=198.51.100.20 ttl=300 \
    key-name=dns-update-key key="c2VjcmV0LWtleS1mb3ItZXhhbXBsZQ=="
```

`ttl=300` 會在其他 DNS 伺服器的快取中保留該記錄 5 分鐘，因此它們能很快獲知地址變更。不指定 `ttl` 時，記錄的有效期為一天。

當伺服器接受更新時，該命令不輸出任何內容。當伺服器不接受時，命令會以 `failure:` 訊息停止；“故障排查”一節列出了每條訊息的含義。

各引數的工作方式：

- `name` 相對於 `zone`：`name=office` 配合 `zone=example.com` 會更新 `office.example.com`。若寫完整名稱則會被重複拼接：`name=office.example.com` 會更新 `office.example.com.example.com`。帶結尾點的名稱會被拒絕，並返回 `failure: bad name`。
- 該更新會先刪除該名稱的所有 A 記錄，然後新增新記錄，因此它是替換地址，而不是再新增一個地址。
- `ttl` 以秒為單位設定記錄的生存時間。不指定 `ttl` 時，記錄獲得 86400 秒（一天），對於會變化的地址來說這太長了。
- `address` 只接受一個 IPv4 地址。提供兩個地址會失敗並返回 `failure: only one address allowed`，IPv6 地址會被拒絕。該命令只更新 A 記錄。

## 保持名稱最新 {#keep-the-name-current}

該命令每次執行只發送一條更新。要讓名稱始終指向會變化的地址，可在地址變化時從指令碼中執行它，例如在 WAN 介面上 [DHCP 用戶端](../network-management/dhcp/client.md) 的租約指令碼中執行，或透過 [scheduler](../system-information-and-utilities/scheduler.md) 條目定期執行。指令碼讀取當前地址，去掉字首長度（參見 [去除網路掩碼](../developer-guides/scripting/scripting-examples.md#strip-netmask)），然後把地址傳給 `/tool/dns-update`。

編寫此類指令碼時需要注意的事項：

- 每次更新都會改動伺服器上的區域。請把地址與該名稱當前的地址（`:resolve`）進行比較，只在二者不同時才傳送更新。
- 啟動時，請等待 [NTP](../system-information-and-utilities/ntp.md) 同步時鐘，以便伺服器接受該簽名。
- 在 NAT 或運營商級 NAT 之後，WAN 介面上的地址並非公網地址。路由器的公網地址位於 [雲](../network-management/cloud/index.md) 的 `public-address` 中。
- 金鑰是命令的一部分，因此任何能讀取該指令碼的使用者都能讀取金鑰。

## 故障排除 {#troubleshoot}

| 訊息 | 含義 |
| :-- | :-- |
| `failure: update send failed` | 路由器無法與伺服器的埠 53 建立 TCP 連線：伺服器已停機、未監聽 TCP，或防火牆將其阻斷。 |
| `failure: reply not signed` | 伺服器拒絕了簽名，例如金鑰名稱或金鑰有誤。 |
| `failure: refused` | 伺服器拒絕該更新，例如該金鑰沒有更新此區域的許可權，或該更新在傳送時未附帶金鑰。 |
| `failure: name not within zone` | 該名稱不在該區域內。請檢查 `zone` 和 `name`。 |
| `failure: bad name` | `name` 無效，例如因為它以點結尾。 |

## 技術細節 {#technical-details}

### 協定 {#protocol}

該更新發往 `dns-server` 的 TCP 埠 53。訊息是針對該區域的 DNS UPDATE（區域段為 `example.com. IN SOA`）。其更新段會刪除該名稱的 A 記錄（`office.example.com. ANY A`），並新增新記錄（`office.example.com. 86400 IN A 198.51.100.20`）。

### 簽名 {#signature}

同時指定 `key-name` 和 `key` 時，訊息會攜帶一條 TSIG 記錄，演算法為 `hmac-md5.sig-alg.reg.int`，並將 fudge 設為 300 秒，即允許的時鐘偏差。`key` 是該金鑰的 base64 金鑰值。不指定 `key-name` 和 `key` 時，更新將以未簽名方式傳送，大多數伺服器會拒絕。

有關所有引數，請參閱 [`/tool/dns-update`](../cli-reference/tool/dns-update.md) CLI 參考。
