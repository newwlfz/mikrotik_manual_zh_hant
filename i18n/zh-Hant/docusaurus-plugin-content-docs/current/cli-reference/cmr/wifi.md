---
sidebar_key: "cli-reference/cmr/wifi"
title: "wifi"
source: https://manual.mikrotik.com/docs/cli-reference/cmr/wifi
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/wifi {#cmrwifi}
**軟體包：** cmr
**型別：** 目錄

複製到所選裝置的 WiFi 網路定義。這些引數擴充套件了標準的 RouterOS `/interface/wifi` 配置引數。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">WiFi 網路已停用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="labels" typ="object" unset="1">選擇使用標籤將 WiFi 網路複製到的裝置。分別支援 + 和 - 符號作為 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1">應用於網路的 VLAN ID：none（預設）或 1-4095。</ArgTableRow>
<ArgTableRow arg="mlo" typ="bool" unset="1">啟用 MLO（多鏈路操作）。</ArgTableRow>
<ArgTableRow arg="ssid" typ="string" unset="1">網路 SSID。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ap | station | station-bridge | station-pseudobridge)" unset="1">網路執行模式。</ArgTableRow>
<ArgTableRow arg="hide-ssid" typ="bool" unset="1">在信標幀中隱藏 SSID。</ArgTableRow>
<ArgTableRow arg="beacon-interval" typ="time" unset="1">信標間隔。</ArgTableRow>
<ArgTableRow arg="dtim-period" typ="num" unset="1">DTIM 週期。</ArgTableRow>
<ArgTableRow arg="multicast-enhance" typ="enum (disabled | enabled) { disabled:0, enabled:1 }" unset="1">組播增強：`disabled` 或 `enabled`。</ArgTableRow>
<ArgTableRow arg="qos-classifier" typ="enum (priority | dscp-high-3-bits) { priority:0, dscp-high-3-bits:1 }" unset="1">QoS 分類器：`priority` 或 `dscp-high-3-bits`。</ArgTableRow>
<ArgTableRow arg="station-roaming" typ="bool" unset="1">啟用站點漫遊。</ArgTableRow>
<ArgTableRow arg="max-clients" typ="num" unset="1">已連線用戶端的最大數量。</ArgTableRow>
<ArgTableRow arg="hw-protection-mode" typ="enum (none | rts-cts | cts-to-self)" unset="1">硬體保護模式：`none`、`rts-cts`、`cts-to-self`。</ArgTableRow>
<ArgTableRow arg="security.encryption" typ="ubit (tkip, ccmp, gcmp, ccmp-256, gcmp-256)" unset="1">允許的加密演算法。</ArgTableRow>
<ArgTableRow arg="security.group-encryption" typ="enum (tkip | ccmp | gcmp | ccmp-256 | gcmp-256)" unset="1">組加密演算法。</ArgTableRow>
<ArgTableRow arg="security.group-key-update" typ="time" unset="1">組金鑰更新間隔。</ArgTableRow>
<ArgTableRow arg="security.passphrase" typ="string" unset="1">網路密碼短語。</ArgTableRow>
<ArgTableRow arg="security.multi-passphrase-group" typ="enum" unset="1">多密碼短語組。</ArgTableRow>
<ArgTableRow arg="security.disable-pmkid" typ="bool" unset="1">停用 PMKID。</ArgTableRow>
<ArgTableRow arg="security.management-protection" typ="enum (disabled | allowed | required)" unset="1">管理幀保護：`disabled`、`allowed`、`required`。</ArgTableRow>
<ArgTableRow arg="security.beacon-protection" typ="enum (disabled | enabled)" unset="1">信標保護：`disabled` 或 `enabled`。</ArgTableRow>
<ArgTableRow arg="security.management-encryption" typ="enum (cmac | gmac | cmac-256 | gmac-256)" unset="1">管理幀加密密碼演算法。</ArgTableRow>
<ArgTableRow arg="security.wps" typ="enum (disable | push-button)" unset="1">WPS 模式：`disable` 或 `push-button`。</ArgTableRow>
<ArgTableRow arg="security.dh-groups" typ="ubit (19, 20, 21)" unset="1">SAE Diffie-Hellman 組。</ArgTableRow>
<ArgTableRow arg="security.sae-anti-clogging-threshold" typ="num" unset="1">SAE 防擁塞閾值。</ArgTableRow>
<ArgTableRow arg="security.sae-max-failure-rate" typ="num" unset="1">SAE 最大失敗率。</ArgTableRow>
<ArgTableRow arg="security.sae-pwe" typ="enum (hunting-and-pecking | hash-to-element | both)" unset="1">SAE PWE 派生方式：`hunting-and-pecking`、`hash-to-element`、`both`。</ArgTableRow>
<ArgTableRow arg="security.owe-transition-interface" typ="iface_enum { auto }" unset="1">OWE 過渡介面。</ArgTableRow>
<ArgTableRow arg="security.eap-methods" typ="multi { array-id, method: enum (tls | ttls | peap) { tls:13, ttls:21, peap:25 }
 }" unset="1">允許的 EAP 方法。</ArgTableRow>
<ArgTableRow arg="security.eap-certificate-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)" unset="1">EAP 證書驗證模式。</ArgTableRow>
<ArgTableRow arg="security.eap-tls-certificate" typ="enum" unset="1">EAP-TLS 證書。</ArgTableRow>
<ArgTableRow arg="security.eap-username" typ="string" unset="1">EAP 使用者名稱。</ArgTableRow>
<ArgTableRow arg="security.eap-anonymous-identity" typ="string" unset="1">EAP 匿名身份。</ArgTableRow>
<ArgTableRow arg="security.eap-password" typ="string" unset="1">EAP 密碼。</ArgTableRow>
<ArgTableRow arg="security.eap-accounting" typ="bool" unset="1">啟用 EAP 計費。</ArgTableRow>
<ArgTableRow arg="security.ft" typ="bool" unset="1">啟用快速轉換（802.11r）。</ArgTableRow>
<ArgTableRow arg="security.ft-mobility-domain" typ="num" unset="1">FT 移動域。</ArgTableRow>
<ArgTableRow arg="security.ft-over-ds" typ="bool" unset="1">透過分散式系統進行 FT。</ArgTableRow>
<ArgTableRow arg="security.ft-reassociation-deadline" typ="time" unset="1">FT 重新關聯截止時間。</ArgTableRow>
<ArgTableRow arg="security.ft-nas-identifier" typ="string" unset="1">FT NAS 識別符號。</ArgTableRow>
<ArgTableRow arg="security.ft-r0-key-lifetime" typ="time" unset="1">FT R0 金鑰生存期。</ArgTableRow>
<ArgTableRow arg="security.ft-preserve-vlanid" typ="bool" unset="1">FT 保留 VLAN ID。</ArgTableRow>
<ArgTableRow arg="security.connect-group" typ="string" unset="1">連線組。</ArgTableRow>
<ArgTableRow arg="security.connect-priority" typ="super { connect-accept-priority: num
, [connect-hold-priority] /num
 }" unset="1">連線優先順序。</ArgTableRow>
<ArgTableRow arg="security.authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, wpa3-psk-gd, owe, wpa3-eap, wpa3-eap-192)" unset="1">支援的認證型別。</ArgTableRow>
</ArgTable>
