---
sidebar_key: "virtual-private-networks/ipsec/qkd-integration-in-routeros-ipsec-ppk"
sidebar_position: 2
title: "RouterOS IPsec 中的 QKD 整合（PPK）"
sidebar_label: "RouterOS IPsec 中的 QKD 整合"
description: "本頁介紹 RouterOS IPsec 的後量子預共享金鑰（PPK）功能，詳細說明其與量子金鑰分發（QKD）的整合、支援的金鑰來源（靜態、PSK、QKD）、安全建議，以及一個雙裝置設定示例。"
tags:
  - 'ipsec'
  - 'qkd'
  - 'ppk'
source: https://manual.mikrotik.com/docs/7.25/virtual-private-networks/ipsec/qkd-integration-in-routeros-ipsec-ppk
captured_at: '2026-11-04T11:23:27+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 1. 簡介 {#1-introduction}

本手冊介紹 RouterOS IPsec 中的後量子預共享金鑰（RFC9867）功能，以及它與量子金鑰分發（QKD）的整合。

PPK 透過使用動態分發或靜態配置的金鑰，提供抵禦量子攻擊的前向安全性。所有 PPK 型別（static、PSK、QKD）都受益於 RFC 8784 的建議：金鑰應至少具有 256 位熵，以提供約 128 位的後量子安全性。

RouterOS 支援三種 PPK 來源：

- Static PPK —— 按對端手動配置的金鑰。
- PSK（預共享金鑰）—— 一次性生成的金鑰，可選擇僅用於初始 IKE SA。
- QKD —— 從 QKD 伺服器動態分發的金鑰。

動態金鑰（PSK/QKD）在使用後即被消耗並失效。靜態金鑰在多次會話間保持有效，但如果重複使用，其安全性較弱。

### ![](/img/7ff77fcd732d67a5.webp) {#}

### 2. 概念 {#2-concepts}

- **PPK（後量子預共享金鑰）：** 在 IKE 協商期間共享的額外金鑰，用於抵禦量子攻擊。
- **QKD：** 基於量子的金鑰分發，透過金鑰管理實體（KME）提供新的對稱金鑰。

#### IKE SA 與 ESP SA {#ike-sa-vs-esp-sa}

- IKE SA：控制隧道協商。
- ESP SA：承載加密的使用者資料。

#### 靜態金鑰與動態金鑰 {#static-vs-dynamic-keys}

- 動態：臨時 PSK 或 QKD 分發的金鑰，使用一次後即丟棄。
- 靜態：按對端手動設定，在多次會話間持久存在。

#### 2.1 RouterOS PPK 來源 {#21-routeros-ppk-sources}

| PPK 來源 | 描述 |
| :-- | :-- |
| Static | 持久化的、手動配置的金鑰。 |
| PSK | 一次性動態生成的預共享金鑰。可選擇僅用於初始 IKE SA（`psk-ike-initial`）。 |
| QKD | 從 QKD 伺服器動態拉取的金鑰，使用後即被消耗。 |

### 3. 安全建議 {#3-security-recommendations}

- 所有 PPK 金鑰都應滿足 RFC 8784 的建議：熵不少於 256 位。
- 靜態 PPK 金鑰如果足夠長，可提升後量子防護能力，但重複使用會降低安全性。
- 動態金鑰（PSK/QKD）由於是一次性使用，可提供更強的安全性。同步失敗可能導致金鑰失步。

### 4. 雙裝置設定概覽 {#4-two-device-setup-overview}

本手冊聚焦於兩臺裝置的最小化設定：

| 角色 | 裝置 | 功能 |
| :-- | :-- | :-- |
| 伺服器 | RouterOS | 承載 IPsec 隧道；提供 QKD/PPK 金鑰 |
| 用戶端 | ROS/LibreSwan | 使用 QKD/PPK 連線到伺服器 |

RouterOS 伺服器可以作為 KME 的 QKD 用戶端，因此不需要第三臺裝置。

```routeros
# 向远程对等体推送配置的示例（IPsec）
/ip ipsec peer
add address=192.168.88.1/32 name=Server exchange-mode=ike2
/ip ipsec proposal
set [ find default=yes ] auth-algorithms=sha256 enc-algorithms=aes-256-gcm
```

### 5. 配置物件 {#5-configuration-objects}

#### 5.1 證書 {#51-certificates}

QKD 需要：

- CA 證書（用於驗證伺服器）。
- SAE 用戶端證書（用於向 QKD 伺服器進行身份驗證）。

```
/certificate/import file-name=ca.crt.pem
/certificate/import file-name=sae-server.crt.pem
/certificate/import file-name=sae-server.key.pem

```

#### 5.2 PSK 示例 {#52-psk-example}

生成供 PPK 使用的一次性 PSK：

```
/ip/ipsec/key/psk/generate count=10 key-size=32

```

- **count** → 要生成的 PSK 數量。
- **key-size** → 每個金鑰的大小（以位元組為單位，32 位元組 = 256 位）。

#### 5.3 QKD 金鑰管理器 {#53-qkd-key-manager}

RouterOS 伺服器可以作為 QKD 用戶端：

```
/ip/ipsec/key/qkd/set address=10.2.3.4:8020 \
    cache-size=1 \
    certificate=sae-server \
    key-size=32 \
    kme-id=server-kme-id \
    peer-sae-id=client-sae-id

```

引數說明：

| 引數 | 描述 |
| :-- | :-- |
| cache-size | IPsec 將從 QKD 伺服器預取的金鑰數量。 |
| cache-state | 當前已快取並可用金鑰的數量。 |
| key-size | 請求的每個金鑰的大小（以位元組為單位，例如 32 位元組 = 256 位）。 |
| kme-id | 用於證書驗證。如果未指定，則不會驗證 KME 身份。 |
| peer-sae-id | 對端 SAE 的識別符號。 |

#### 5.4 配置檔案與對端 {#54-profiles-and-peers}

```
/ip/ipsec/profile/add name=qkd-profile ppk=qkd
/ip/ipsec/peer/add address=10.2.1.2 exchange-mode=ike2 \
    name=peer-client profile=qkd-profile proposal-check=obey
/ip/ipsec/identity/add peer=peer-client profile=qkd-profile

```

配置檔案的 PPK 選項：

| 選項 | 描述 |
| :-- | :-- |
| no | PPK 已停用。 |
| psk | 用於 IKE 和 ESP 重金鑰的一次性 PSK。 |
| psk-ike-initial | 僅用於初始 IKE SA 的 PSK（由 `psk-ike-only` 重新命名而來）。 |
| qkd | 從 QKD 伺服器獲取的金鑰。 |

#### 5.5 提議 / 策略 {#55-proposal--policy}

```
/ip/ipsec/proposal/add name=qkd-proposal auth-algorithms=sha256 \
    enc-algorithms=aes-256-gcm pfs-group=modp2048
/ip/ipsec/policy/add src-address=10.1.0.0/24 dst-address=10.2.0.0/24 \
    peer=peer-client proposal=qkd-proposal tunnel=yes

```

### 6. 行為 {#6-behaviour}

- 動態金鑰：從 `/ip/ipsec/key/psk/` 或 QKD 伺服器拉取，使用一次後即被刪除。
- 靜態金鑰：按對端配置，可重複使用。
- 一次性動態金鑰可確保最強的防護，但需要同步。
- 靜態回退可保證隧道建立，但金鑰應足夠長（熵不少於 256 位）。
- PPK 的使用可以選擇限制為僅 IKE SA（`psk-ike-initial`），以減少金鑰消耗。

### 7. 偵錯與故障排查 {#7-debugging-and-troubleshooting}

要驗證 QKD 整合和金鑰獲取情況，請啟用 IPsec 偵錯日誌：

```
/system/logging/add topics=ipsec,debug action=memory

```

以下是顯示 QKD 金鑰獲取過程的偵錯輸出示例：

```
2025-10-11 17:32:38 ipsec,debug,packet POST
2025-10-11 17:32:38 ipsec,debug,packet Host: 10.2.3.4\r\n
2025-10-11 17:32:38 ipsec,debug,packet {"number":1,"size":16}
2025-10-11 17:32:38 ipsec,debug,packet HTTP/1.1 200 OK\r\n
2025-10-11 17:32:38 ipsec,debug,packet {"keys":[{"key_ID":"37f4c842-dd82-4c49-8dfc-52a3793e5331","key":"m/JIEIUCzAE="}]}
2025-10-11 17:32:38 ipsec,debug,packet qkd: add to cache key 37f4c842-dd82-4c49-8dfc-52a3793e5331: 9bf24
```

如果金鑰未被加入快取，請檢查到 KME 的網路連通性、證書驗證，以及 `kme-id` 和 `peer-sae-id` 配置是否正確。

### 8. 匯出示例（雙裝置設定） {#8-example-export-two-device-setup}

#### RouterOS 伺服器 {#routeros-server}

```
/ip/ipsec/key/qkd
set address=10.2.3.4:8020 cache-size=1 certificate=sae-server key-size=32 \
    kme-id=server-kme-id peer-sae-id=client-sae-id
/ip/ipsec/profile/add name=qkd-profile ppk=qkd
/ip/ipsec/proposal/add name=qkd-proposal auth-algorithms=sha256 enc-algorithms=aes-256-gcm pfs-group=modp2048
/ip/ipsec/peer/add address=10.2.1.2 exchange-mode=ike2 name=peer-client profile=qkd-profile proposal-check=obey
/ip/ipsec/identity/add peer=peer-client profile=qkd-profile
/ip/ipsec/policy/add src-address=10.1.0.0/24 dst-address=10.2.0.0/24 peer=peer-client proposal=qkd-proposal tunnel=yes

```

#### 用戶端裝置 {#client-device}

```
/ip/ipsec/key/qkd
set address=10.2.3.4:8020 cache-size=1 certificate=sae-client key-size=32 \
    kme-id=client-kme-id peer-sae-id=server-sae-id
/ip/ipsec/profile/add name=qkd-profile ppk=qkd
/ip/ipsec/proposal/add name=qkd-proposal auth-algorithms=sha256 enc-algorithms=aes-256-gcm pfs-group=modp2048
/ip/ipsec/peer/add address=10.2.1.1 exchange-mode=ike2 name=peer-server profile=qkd-profile proposal-check=obey
/ip/ipsec/identity/add peer=peer-server profile=qkd-profile
/ip/ipsec/policy/add src-address=10.2.0.0/24 dst-address=10.1.0.0/24 peer=peer-server proposal=qkd-proposal tunnel=yes

```

### 9. 參考資料 {#9-references}

- IETF 草案：IKEv2 Post-Quantum PPK：[https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-qr-alt/](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-qr-alt/)
- [https://datatracker.ietf.org/doc/html/rfc9867](https://datatracker.ietf.org/doc/html/rfc9867)

### 備註 {#notes}

#### QKD 作為分發機制 {#qkd-as-a-distribution-mechanism}

- RouterOS 中的 QKD 本身並不是一種新的加密方法 —— 它是一種**金鑰分發機制**。
- 它透過**金鑰管理實體（KME）**提供動態生成的金鑰，雙方對端都能安全地獲取這些金鑰。

#### 動態與靜態來源 {#dynamic-vs-static-sources}

- *動態來源*：QKD 分發的金鑰、來自 `/ip/ipsec/key/psk/` 的一次性 PSK。
- *靜態來源*：按對端配置的靜態 PPK 金鑰。
- 建議：為獲得長期安全性，優先使用**動態金鑰**；同時保留**靜態回退**，以防動態金鑰耗盡時隧道中斷。

#### 安全指南（RFC 8784） {#security-guidelines-rfc-8784}

- 後量子預共享金鑰應包含**至少 256 位熵**，以提供 128 位的後量子安全性。
- 僅使用一個靜態金鑰保護 IKE SA 是可行的，但如果重複使用則存在風險。

#### 運維注意事項 {#operational-considerations}

- **金鑰耗盡**：在頻繁重金鑰（IKE + ESP）期間，一次性 PSK 會很快被消耗。QKD 透過持續提供新金鑰來避免這一問題。
- **中心輻射型拓撲**：動態 PSK 需要建立對端關聯，以避免各輻射點之間出現失步。
- **回退行為**：確保在動態金鑰不可用時，系統能夠平穩切換到靜態 PPK。

#### 相容性說明 {#compatibility-notes}

- **RouterOS - RouterOS**：同時支援 PSK 和 QKD PPK。
- **RouterOS - LibreSwan**：可用於靜態 PPK；動態 PSK 可能需要自定義構建。
- **RouterOS - StrongSwan**：需要進行適配，因為不同草案版本之間的識別符號存在差異。
