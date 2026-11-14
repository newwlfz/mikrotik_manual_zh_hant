---
sidebar_key: "cli-reference/interface/ethernet/switch/ingress-vlan-translation"
sidebar_position: 8
title: "ingress-vlan-translation"
sidebar_label: 'ingress-vlan-translation'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/ingress-vlan-translation
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/ingress-vlan-translation {#interfaceethernetswitchingress-vlan-translation}
**系統能力：** musicswitch
**型別：** 目錄

入站 VLAN 轉換表允許每個埠最多 15 個條目。可以從封包頭中選擇一個或多個欄位，以便在入站 VLAN 轉換表中查詢。第一個匹配條目中配置的 S-VLAN 或 C-VLAN 或兩者都會分配給該封包。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="protocol" typ="alt { protocol-name: enum (length | llc-bpdu) { length:1, llc-bpdu:0x4242 }
, protocol-number: num [ .. 65535]
 }">匹配乙太網協定。（僅用於入站 VLAN 轉換）</ArgTableRow>
<ArgTableRow arg="sa-learning" typ="bool">啟用或停用 VLAN 轉換後的源 MAC 學習。（僅用於入站 VLAN 轉換）</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1">匹配 VLAN 轉換規則的交換器埠。</ArgTableRow>
<ArgTableRow arg="service-vlan-format" typ="enum (untagged-or-tagged | priority-tagged-or-tagged | tagged | any) { untagged-or-tagged:0, priority-tagged-or-tagged:1, tagged:2, any:3 }">帶有服務標籤的幀型別，VLAN 轉換規則對其有效。</ArgTableRow>
<ArgTableRow arg="service-vid" typ="num">匹配服務標籤的 VLAN ID。</ArgTableRow>
<ArgTableRow arg="service-pcp" typ="num">匹配服務標籤的 PCP。</ArgTableRow>
<ArgTableRow arg="service-dei" typ="num">匹配服務標籤的 DEI。</ArgTableRow>
<ArgTableRow arg="customer-vlan-format" typ="enum (untagged-or-tagged | priority-tagged-or-tagged | tagged | any) { untagged-or-tagged:0, priority-tagged-or-tagged:1, tagged:2, any:3 }">帶有客戶標籤的幀型別，VLAN 轉換規則對其有效。</ArgTableRow>
<ArgTableRow arg="customer-vid" typ="num">匹配客戶標籤的 VLAN ID。</ArgTableRow>
<ArgTableRow arg="customer-pcp" typ="num">匹配客戶標籤的 PCP。</ArgTableRow>
<ArgTableRow arg="customer-dei" typ="num">匹配客戶標籤的 DEI。</ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="alt { special-vid: enum (customer-vid) { customer-vid:4096 }
, vid: num [ .. 4095]
 }">新的服務 VLAN ID 會替換匹配的服務 VLAN ID。</ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="alt { special-vid: enum (service-vid) { service-vid:4096 }
, vid: num [ .. 4095]
 }">新的客戶 VLAN ID 會替換匹配的客戶 VLAN ID。如果設定為 4095 且使用入站 VLAN 轉換，則流量會被丟棄。</ArgTableRow>
<ArgTableRow arg="pcp-propagation" typ="bool">
啟用或停用 PCP 傳播。
- 如果埠型別為 Edge，則客戶 PCP 從服務 PCP 複製。
- 如果埠型別為 Network，則服務 PCP 從客戶 PCP 複製。
</ArgTableRow>
<ArgTableRow arg="swap-vids" typ="enum (no | assign-cvid-to-svid) { no:0, assign-cvid-to-svid:0 }"></ArgTableRow>
</ArgTable>
下表列出了會觸發具有特定 VLAN 格式設定的規則的流量；請注意，帶有 VLAN ID 0 標籤的流量是一種特殊情況，也會被考慮在內。

| 屬性 | 描述 |
| :-- | :-- |
| **any** | 接受：未標記流量標記流量帶優先順序設定的標記流量VLAN 0 流量帶優先順序設定的 VLAN 0 流量 |
| **priority-tagged-or-tagged** | 接受：標記流量帶優先順序設定的標記流量VLAN 0 流量帶優先順序設定的 VLAN 0 流量 |
| **tagged** | 接受：標記流量帶優先順序設定的標記流量 |
| **untagged-or-tagged** | 接受：未標記流量標記流量帶優先順序設定的標記流量 |

:::danger
如果 `VLAN-format` 設定為 `any`，那麼將 `customer-vid``/``service-vid` 設定為 `0` 會觸發針對 VLAN 0 流量的交換器規則。在這種情況下，交換器規則會查詢未標記流量或帶有 VLAN 0 標籤的流量，只有 `untagged-or-tagged` 會過濾掉 VLAN 0 流量。
:::
