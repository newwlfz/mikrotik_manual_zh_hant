---
sidebar_key: "cli-reference/ip/smb/shares"
sidebar_position: 1
title: "shares"
sidebar_label: 'shares'
source: https://manual.mikrotik.com/docs/cli-reference/ip/smb/shares
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/smb/shares {#ipsmbshares}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">該條目是自動建立的。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">該共享已停用，用戶端無法訪問。</ArgTableRow>
<ArgTableRow arg="*" typ="default">該條目是系統建立的預設條目。</ArgTableRow>
<ArgTableRow arg="r" typ="read-only">該共享僅允許用戶端讀取；寫入訪問會被拒絕。</ArgTableRow>
<ArgTableRow arg="c" typ="require-encryption">該共享僅接受加密連線。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">用戶端連線的 SMB 共享名稱。</ArgTableRow>
<ArgTableRow arg="directory" typ="file">該共享指向的路由器上的目錄。未設定時，使用根目錄中 `name` 的值。如果目錄不存在，則會自動建立。</ArgTableRow>
<ArgTableRow arg="read-only" typ="bool">用戶端是否只能讀取該共享。也可以透過在 [`users`](./users.md) 中為每個使用者設定 `read-only` 來限制訪問。預設值：no.</ArgTableRow>
<ArgTableRow arg="require-encryption" typ="bool">是否僅允許加密連線訪問該共享；建議 macOS 用戶端使用。預設值：no。</ArgTableRow>
<ArgTableRow arg="valid-users" typ="multi { array-id, user: enum
 }">允許訪問該共享的 SMB 使用者列表。當列表為空時，所有使用者都可以訪問。</ArgTableRow>
<ArgTableRow arg="invalid-users" typ="multi { array-id, user: enum
 }">被明確拒絕訪問該共享的 SMB 使用者列表。</ArgTableRow>
</ArgTable>
