---
sidebar_key: "cli-reference/ip/nat-pmp/index"
sidebar_position: 1
title: "nat-pmp"
sidebar_label: 'nat-pmp'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/nat-pmp
captured_at: '2026-11-01T21:24:17+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
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
