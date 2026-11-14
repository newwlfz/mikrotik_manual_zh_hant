---
sidebar_key: "cli-reference/ip/nat-pmp"
title: "nat-pmp"
sidebar_label: 'nat-pmp'
source: https://manual.mikrotik.com/docs/cli-reference/ip/nat-pmp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/nat-pmp {#ipnat-pmp}
**型別：** 設定目錄

NAT 埠對映協定（NAT-PMP，[RFC 6886](https://www.rfc-editor.org/rfc/rfc6886)）服務設定。啟用後，該服務會在 UDP 埠 5351 上等待來自內部介面的對映請求，並在 `/ip/service` 中顯示為動態的 `natpmp` 條目。配置示例見 [NAT-PMP 指南頁面](../../../firewall-and-quality-of-service/nat-pmp.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">啟用 NAT-PMP 服務。預設值：no。</ArgTableRow>
</ArgTable>
