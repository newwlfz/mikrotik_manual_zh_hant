---
sidebar_key: "cli-reference/ip/ipsec/peer"
sidebar_position: 6
title: "peer"
sidebar_label: 'peer'
source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/peer
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/peer {#ipipsecpeer}
**型別：** 目錄

對等方配置設定用於在 IKE 守護程式之間建立連線。此連線隨後用於為 SA 協商金鑰和演算法。交換模式是各對等方之間的唯一識別符號，這意味著只要使用不同的 exchange-mode，就可以存在多個具有相同 remote-address 的對等方配置。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該項是否已停用。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">該項是否是動態建立的。</ArgTableRow>
<ArgTableRow arg="R" typ="responder">該對等方是否僅充當響應方（監聽傳入請求）而不發起連線。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">對等方名稱。</ArgTableRow>
<ArgTableRow arg="address" typ="alt { prefix6: ip6Prefix
, prefix4: ipPrefix
, dns: string
 }">對等方的遠端地址。如果遠端對等方的地址與此字首匹配，則該對等方配置將用於階段 1 的身份驗證和建立。如果多個對等方地址與多個配置條目匹配，則將使用最具體的一項（即具有最大子網掩碼的那一項）。</ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">用於連線的本地地址。</ArgTableRow>
<ArgTableRow arg="passive" typ="bool">被動對等方不發起連線。啟用被動模式還表示該對等方是 xauth 響應方，而停用被動模式則表示它是 xauth 發起方。</ArgTableRow>
<ArgTableRow arg="port" typ="num">當路由器作為發起方且遠端對等方使用非預設埠時，用於連線到遠端對等方的通訊埠。</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">要使用的 IPsec 配置檔案。</ArgTableRow>
<ArgTableRow arg="exchange-mode" typ="enum (main | aggressive | ike2)">
根據 [RFC 2408](https://datatracker.ietf.org/doc/html/rfc2408#section-4.1) 的 ISAKMP 階段 1 交換模式。`main` 模式放寬了 [rfc2409 第 5.4 節](https://datatracker.ietf.org/doc/html/rfc2409#section-5.4)，以允許在 `main` 模式下進行 pre-shared-key 認證。`ike2` 模式啟用 Ikev2 [RFC 7296](https://datatracker.ietf.org/doc/html/rfc7296)。  

IKEv2 會忽略的引數：`proposal-check`、`compatibility-options`、`lifebytes`、`dpd-maximum-failures`、`nat-traversal`。
</ArgTableRow>
<ArgTableRow arg="send-initial-contact" typ="bool">指定是傳送“初始聯絡”IKE 封包還是等待遠端；該封包應觸發移除當前源地址的舊對等方 SA。通常，在 road warrior 部署中，用戶端是發起方，此引數應設定為 no。如果為 ikev1 啟用了 modecfg 或 xauth，則不會發送初始聯絡。</ArgTableRow>
<ArgTableRow arg="ppk-secret" typ="string">當此對等方不存在一次性金鑰/psk 時，使用的帶有 "static-ppk-secret" ID 的靜態 PPK 金鑰；請確保該金鑰具有 256 bits 的熵。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="current-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">對等方當前的遠端地址。</ArgTableRow>
</ArgTable>
