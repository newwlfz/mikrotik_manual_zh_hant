---
sidebar_key: "cli-reference/ip/ipsec/identity"
sidebar_position: 2
title: "identity"
sidebar_label: 'identity'
source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/identity
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/identity {#ipipsecidentity}
**型別：** 目錄

身份是特定於遠端對等體的配置引數。身份的主要目的是處理認證並驗證對等體的完整性。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">該項是否為動態建立。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">該項是否已停用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="peer" typ="enum" mandatory="1">對端名稱。</ArgTableRow>
<ArgTableRow arg="auth-method" typ="enum (pre-shared-key | digital-signature | eap | eap-radius | pre-shared-key-xauth | rsa-key | rsa-signature-hybrid)">
身份驗證方法：
- digital-signature - 使用一對 RSA 證書進行身份驗證；
- eap - 用於發起方（netmask 為 /32 的對端）的 IKEv2 EAP 身份驗證。必須與 eap-methods 一起使用；
- eap-radius - 用於響應方的 IKEv2 EAP RADIUS 透傳身份驗證（RFC 3579）。這種情況下需要伺服器證書。如果未指定伺服器證書，則只有支援 EAP-only（RFC 5998）的用戶端才能連線。請注意，EAP 方法應與 EAP-only 相容；
- pre-shared-key - 使用對端之間共享的密碼（預共享金鑰）字串進行身份驗證（不建議使用，因為可能對預共享金鑰進行離線攻擊）；
- rsa-key - 使用在 keys 選單中匯入的 RSA 金鑰進行身份驗證。僅在 IKEv1 中支援；
- pre-shared-key-xauth - 使用對端之間共享的密碼（預共享金鑰）字串 + XAuth 使用者名稱和密碼進行身份驗證。僅在 IKEv1 中支援；
- rsa-signature-hybrid - 使用響應方證書身份驗證和發起方 XAuth。僅在 IKEv1 中支援。
</ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, method: enum (eap-tls | eap-ttls | eap-peap | eap-mschapv2)
 }">
所有 EAP 方法都要求 System/Certificates 選單中存在完整的證書鏈，包括中間 CA 和根 CA 證書。此外，必須指定使用者名稱和密碼（如果身份驗證伺服器要求）。可以指定多個 EAP 方法，並按照指定的順序使用。 

支援的 EAP 方法：
- eap-mschapv2;
- eap-peap - 也稱為 PEAPv0/EAP-MSCHAPv2；
- eap-tls - 需要在 certificate 引數下指定額外的用戶端證書；
- eap-ttls.
</ArgTableRow>
<ArgTableRow arg="mode-config" typ="enum (none)">來自 mode-config 選單的配置引數名稱。設定該引數後，mode-config 即啟用。</ArgTableRow>
<ArgTableRow arg="notrack-chain" typ="string">將與 IPsec 策略匹配的 IP/Firewall/Raw 規則新增到指定鏈。與 generate-policy 一起使用。</ArgTableRow>
<ArgTableRow arg="my-id" typ="alt { string: composite { type: enum (fqdn | user-fqdn | key-id)
, data: string
 }
, address: composite { type: enum (address)
, data: alt { ipv6: ip6Addr
, ip: ipAddr
 }
 }
, other: enum (auto | dn)
 }">
在發起方上，這控制傳送給響應方的 ID_i 內容。在響應方上，這控制傳送給發起方的 ID_r 內容。在 IKEv2 中，響應方還期望從發起方收到的 ID_r 中包含此 ID。
- auto - 自動嘗試使用正確的 ID：預共享金鑰使用 IP，基於證書的連線使用 SAN（如果不存在則使用 DN）；
- address - 使用 IP 地址作為 ID；
- dn - ASN.1 X.500 Distinguished Name 的二進位制 Distinguished Encoding Rules (DER) 編碼；
- fqdn - 完全限定域名；
- key-id - 為身份使用指定的金鑰 ID；
- user fqdn - 指定完全限定的使用者名稱字串，例如 "user@domain.com"。
</ArgTableRow>
<ArgTableRow arg="remote-id" typ="alt { string: composite { type: enum (fqdn | user-fqdn | key-id)
, data: string
 }
, address: composite { type: enum (address)
, data: alt { ipv6: ip6Addr
, ip: ipAddr
 }
 }
, auto: enum (auto | ignore | dn)
 }">
此引數控制期望從遠端對端收到的 ID 值。請注意，除 ignore 外的所有型別都會使用收到的證書驗證遠端對端的 ID。如果對端傳送證書名稱作為其 ID，則會對照證書進行檢查；否則，ID 會對照 Subject Alt. Name 進行檢查。
- auto - 接受所有 ID；
- address - 使用 IP 地址作為 ID；
- dn - ASN.1 X.500 Distinguished Name 的二進位制 Distinguished Encoding Rules (DER) 編碼；
- fqdn - 完全限定域名。僅在 IKEv2 中支援；
- user fqdn - 完全限定的使用者名稱字串，例如 "user@domain.com"。僅在 IKEv2 中支援；
- key-id - 用於該身份的特定金鑰 ID。僅在 IKEv2 中支援；
- ignore - 不使用證書驗證收到的 ID（危險）。

\* 不支援萬用字元金鑰 ID 匹配，例如 `remote-id="key-id:CN=*.domain.com"`
</ArgTableRow>
<ArgTableRow arg="match-by" typ="enum (remote-id | certificate)">
定義用於對端身份驗證的邏輯。
- remote-id - 根據 remote-id 設定驗證對端的 ID。
- certificate 會使用 remote-certificate 設定中指定的內容驗證對端的證書。
</ArgTableRow>
<ArgTableRow arg="key" typ="enum ()">來自 keys 選單的私鑰名稱。如果使用 RSA 金鑰身份驗證方法（auth-method=rsa-key），則適用。</ArgTableRow>
<ArgTableRow arg="remote-key" typ="enum ()">來自 keys 選單的公鑰名稱。如果使用 RSA 金鑰身份驗證方法（auth-method=rsa-key），則適用。</ArgTableRow>
<ArgTableRow arg="secret" typ="string">金鑰字串。如果以 '0x' 開頭，則會將其解析為十六進位制值。如果使用預共享金鑰身份驗證方法（`auth-method=pre-shared-key` 或 `auth-method=pre-shared-key-xauth`），則適用。</ArgTableRow>
<ArgTableRow arg="certificate" typ="multi { array-id, certificate: enum
 }">本地證書。如果使用數字簽名身份驗證方法（`auth-method=digital-signature`）或 EAP（`auth-method=eap`），則適用。</ArgTableRow>
<ArgTableRow arg="remote-certificate" typ="enum (none) { none:-1 }">用於驗證遠端端的證書（驗證封包；不需要私鑰）。如果未指定 remote-certificate，則使用從遠端對端收到的證書，並在 certificate 選單中對照 CA 進行檢查。必須在證書儲存中匯入正確的 CA。如果指定了 remote-certificate 和 match-by=certificate，則只會匹配特定的用戶端證書。如果使用數字簽名身份驗證方法（`auth-method=digital-signature`），則適用。</ArgTableRow>
<ArgTableRow arg="username" typ="string">EAP 或 XAuth 使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string">EAP 或 XAuth 密碼。</ArgTableRow>
<ArgTableRow arg="generate-policy" typ="enum (no | port-override | port-strict)">
允許此對端為不存在的策略建立 SA。此類策略會在 SA 的生命週期內動態建立。自動策略允許例如建立受 IPsec 保護的 L2TP 隧道，或任何其他在配置時遠端對端 IP 地址未知的設定。
- no - 不生成策略；
- port-override - 生成策略並強制策略使用任意埠（舊行為）；
- port-strict - 使用對端提議中的埠，這些埠應與對端的策略匹配。
</ArgTableRow>
<ArgTableRow arg="policy-template-group" typ="enum">用於生成的策略的策略模板組。如果沒有任何模板匹配，則不會建立 Phase 2 SA。</ArgTableRow>
</ArgTable>
