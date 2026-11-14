---
sidebar_key: "getting-started/installation-and-upgrade/upgrade-server"
sidebar_position: 3
title: "升級伺服器"
sidebar_label: "升級伺服器"
description: "瞭解 RouterOS 如何連線到 MikroTik 升級伺服器以檢查並下載新版本，以及如何排查連線問題。"
source: https://manual.mikrotik.com/docs/7.24/getting-started/installation-and-upgrade/upgrade-server
captured_at: '2026-11-07T17:11:03.548Z'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

檢查更新時，RouterOS 會聯絡 `upgrade.mikrotik.com`，以確定適用於你的裝置和許可證級別的最新可用版本。如果無法訪問伺服器或 DNS 名稱無法解析，則升級檢查會失敗或返回過時的資訊。

## 升級檢查的工作方式 {#how-the-upgrade-check-works}

RouterOS 軟體包更新機制會執行以下步驟：

1. 裝置向 `upgrade.mikrotik.com` 傳送請求，其中包含當前 RouterOS 版本、架構和許可證級別。
2. 伺服器將此資訊與你所選擇的釋出鏈（Long term、Stable、Testing 或 Development）進行匹配，並返回最新的相容版本。
3. 如果有更新的版本可用，裝置會直接從同一伺服器下載相應的 `.npk` 軟體包。

## 故障排除 {#troubleshooting}

如果裝置未檢測到可用的升級，請確認它能夠解析並訪問升級伺服器。

### 檢查 DNS 解析 {#check-dns-resolution}

執行以下命令以確認裝置能夠解析伺服器地址：

```ros
:put [:resolve upgrade.mikrotik.com]
```

結果應為 `159.148.147.251`。如果該地址無法解析或解析為其他 IP，請檢查你的 DNS 設定。更多資訊請參閱 [DNS](../../network-management/dns.md) 文章。

### 檢查伺服器可達性 {#check-server-reachability}

確認 DNS 解析正常後，請驗證裝置能夠訪問伺服器：

```ros
/tool/ping address=159.148.147.251
```

如果 ping 失敗，請檢查你的防火牆規則、路由或上游連線。裝置必須能夠透過 443 埠（HTTPS）訪問伺服器才能下載軟體包。
