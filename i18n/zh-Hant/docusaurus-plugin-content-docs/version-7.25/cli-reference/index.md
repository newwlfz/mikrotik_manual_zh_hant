---
sidebar_key: "cli-reference/index"
sidebar_position: 32
title: "CLI 參考"
sidebar_label: "CLI 參考"
description: "CLI 參考按控制檯路徑記錄 RouterOS 命令選單和屬性。使用本節可查閱命令語法、配置物件以及 RouterOS 各項功能的操作命令。"
source: https://manual.mikrotik.com/docs/7.25/cli-reference/
captured_at: '2026-11-01T13:53:14+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

CLI 參考按控制檯路徑記錄 RouterOS 命令選單和屬性。使用本節可查詢 RouterOS 功能的命令語法、配置物件和操作命令。

## 引數型別 {#argument-types}

- **address** — 通用地址引數，呈現為 `address (flags=...)`；請參閱下面的[地址標誌](#address-flags)
- **alt** — 備選型別，可接受幾種不同值型別之一
- **as** — 自治系統編號（用於 BGP 路由）
- **bool** — 布林值（true/false、yes/no）
- **cfg** — 配置條目識別符號
- **composite** — 多個引數的組合，作為一個組處理
- **date** — 日期和時間值
- **enum** — 列舉器，具有列在括號中的預定義值
- **expr** — 表示式或條件（用於路由過濾器和指令碼）
- **file** — 檔案路徑或名稱引用
- **iface_enum** — 介面選擇列表，通常可以接受介面名稱，或諸如 `all`、`none`、`dynamic`、`slave` 之類的預定義值；值列在花括號中
- **ipAddr** — IPv4 地址
- **ip6Addr** — IPv6 地址
- **ipPrefix** — 帶字首長度的 IPv4 地址
- **ip6Prefix** — 帶字首長度的 IPv6 地址
- **ipRange** — IPv4 地址範圍
- **macAddr** — MAC 地址（可指定完整地址或使用萬用字元）
- **meter** — 訊號質量級別，通常以 dBm 表示
- **multi** — 多值引數，接受來自已定義集合的多個值
- **num** — 無符號整數，可用範圍限制（例如 `[3 .. 20]`、`[.. 10]`、`[4 ..]`）；如未明確指定，則為 32 位範圍
- **numericon** — 帶單位字尾顯示的數字值
- **object** — 結構化值列表（例如地址表或配置項表）
- **pic** — 圖片/點陣圖值
- **range** — 數字範圍（例如一組埠）
- **remote** — 對遠端物件的引用（例如路由過濾器規則）
- **script** — 指令碼原始碼；呈現為 `alt { script: string }` 的引數既接受來自 `/system script` 的現有指令碼名稱，也接受內聯指令碼原始碼
- **string** — 文字字串
- **super** — 複合型別，接受多種不同的引數型別；子型別列在花括號中，例如 `super { bool, time }`
- **switch** — 開/關切換，無需顯式值引數
- **time** — 持續時間或間隔，通常以秒為單位，可包含 `s`、`m`、`h`、`d` 等單位
- **timezone** — 時區或 UTC 偏移值
- **ubit** — 帶命名位的位域，支援的位名稱列在括號中，例如 `ubit (ip, ipv6)`
- **value** — 獨立值識別符號（通常作為複合型別或列舉的一部分使用）
- **varName** — 變數名引用（用於指令碼）

引數型別可以巢狀，例如 `super {num, time, super {bool, ip}}`。

## 標準列表條目屬性 {#standard-list-entry-properties}

列表選單（其條目可新增、刪除和重新排序的選單）共享一組在各處行為相同的屬性和命令，因此不會在每個選單頁面的引數表中重複列出：

- **`comment`** — 條目的自由格式文字註釋
- **`disabled`** — 當為 `yes` 時，該條目處於非活動狀態但仍保留在配置中；此類條目在列表中用 `X` 標記。`enable` 和 `disable` 命令切換此狀態
- **`copy-from`** — `add` 命令的引數：將新條目建立為現有條目的副本
- **`place-before`** — `add` 和 `move` 命令的引數：將條目放在列表中另一個條目前面

## 標準 print 修飾符 {#standard-print-modifiers}

`print` 命令接受輸出修飾符，這些修飾符同樣不會列在每個選單頁面上：

- **`detail`** — 列印每個條目的所有屬性，而不是簡要摘要
- **`as-value`** — 將輸出作為值返回，而不是格式化字串，以便在指令碼中使用

## address-flags {#address-flags}

**address** 型別呈現為 `address (flags=...)`，其中標誌定義接受哪些地址格式：

| 標誌 | 含義 |
|------|---------|
| 4    | IPv4 地址 |
| 6    | IPv6 地址 |
| D    | DNS 名稱（主機名） |
| i    | 介面名稱本身作為值，替代地址（例如將點對點介面用作路由閘道器） |
| /    | 帶子網掩碼的地址（CIDR 字首） |
| v    | VRF（虛擬路由轉發例項） |
| %    | 地址上的介面字尾（區域說明符），例如 `fe80::1%ether1` 或 `00:11:22:33:44:55%ether1` |
| R    | 路由區分符 |
| S    | 自由格式字首（例如 EVPN 字首） |
| \+   | 地址列表 |
| :    | 埠或區域說明符 |
| L    | 鏈路本地地址 |
| m    | 組播地址 |

`i` 和 `%` 標誌的區別在於介面出現的位置。使用 `i` 時，裸介面名稱替代地址。使用 `%` 時，介面只是附加到完整地址後的限定符，用於區分在整個路由器範圍內不唯一的地址，例如 IPv6 鏈路本地地址。

請注意，`%interface` 字尾是 IPv6 鏈路本地定址本身的一部分：沒有區域說明時，鏈路本地地址是有歧義的，因此任何接受 IPv6 地址的引數（標誌 `6`）都接受 `link-local%interface`，即使其標誌列表不包含 `%`。`%` 標誌表示該引數更廣泛地支援此後綴，例如用於為 MAC ping 選擇出介面。
