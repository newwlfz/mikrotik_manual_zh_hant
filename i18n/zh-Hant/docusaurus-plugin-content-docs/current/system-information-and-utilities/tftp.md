---
sidebar_key: "system-information-and-utilities/tftp"
sidebar_position: 15
title: "TFTP"
sidebar_label: "TFTP"
description: "RouterOS TFTP 伺服器：向裝置提供啟動檔案、韌體和配置檔案，接受上傳，將請求的檔名與訪問規則和正則表示式進行匹配，並排查塊大小、大檔案和錯誤問題。"
tags:
  - 'tftp'
  - 'ip-addresses'
  - 'settings'
source: https://manual.mikrotik.com/docs/system-information-and-utilities/tftp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 內建 TFTP 伺服器。簡單檔案傳輸協定（TFTP）是一種基於 UDP 的簡單檔案傳輸協定，無需認證，網路裝置在啟動時就會使用它：IP 電話和接入點透過它獲取配置或韌體，網路啟動的計算機用它載入載入程式，交換器則用它上傳配置備份。該伺服器從路由器儲存中提供檔案，並在規則允許時接受上傳。

只要 `/ip/tftp` 中至少有一條已啟用的訪問規則，伺服器就會執行。每個請求都會按順序與規則逐一比對：第一條同時匹配用戶端地址和所請求檔名的規則做出決定，而沒有規則匹配的請求會被拒絕。要從其他 TFTP 伺服器下載檔案，請使用 `mode=tftp` 的 [`/tool/fetch`](./fetch.md)。

裝置通常透過 DHCP 獲知 TFTP 伺服器和檔名。在 RouterOS DHCP 伺服器上，請在 [`/ip/dhcp-server/network`](../cli-reference/ip/dhcp-server/network.md) 中設定 `next-server`（TFTP 伺服器地址）和 `boot-file-name`；期望 DHCP 選項 66 或 150 的裝置會從 [DHCP 選項](../network-management/dhcp/server.md)中獲得它們。

:::warning
TFTP 沒有密碼：規則 `ip-addresses` 中的每個用戶端都能讀取該規則 `req-filename` 所匹配的每一個名稱，並且在 `read-only=no` 時還能寫入這些名稱。請把 `ip-addresses` 限制為真正需要該規則的裝置，並讓 `req-filename` 只匹配你要提供的名稱：在提供某個資料夾或所請求名稱的規則中，諸如 `.*` 這樣的模式或為空的 `req-filename` 也會匹配那些指向所服務資料夾之外的名稱。本頁示例使用 `[^/.][^/]*`，即不含斜槓且不以點開頭的名稱。
:::

## 為裝置提供檔案 {#serve-files-to-devices}

建立一個資料夾（此處為 `tftp`），把檔案複製進去（參見 [檔案](./files.md)），然後把它提供給區域網路。作為 `real-filename` 的資料夾會被放在所請求名稱之前，因此請求 `phone.cfg` 會返回 `tftp/phone.cfg`；該模式接受帶可選前導斜槓的名稱（某些用戶端會這樣傳送），且不接受子資料夾：

```ros
/file/add name=tftp type=directory
/ip/tftp/add ip-addresses=192.168.88.0/24 \
    req-filename="/\?[^/.][^/]*" real-filename=tftp
```

要在 WinBox 中配置規則，請開啟 **IP > TFTP** 並選擇 **New**：

1. 使用 **IP Addresses** 旁的 **+** 控制元件輸入允許的用戶端地址或子網，例如示例中的 `192.168.88.0/24`。
2. 將 **Req. Filename** 設為請求名稱模式，將 **Real Filename** 設為路由器上的檔案或資料夾。對於資料夾示例，請將 **Real Filename** 設為 `tftp`，並使用命令中的模式。
3. 保持 **Allow** 和 **Read Only** 處於選中狀態，以便只提供檔案而不接受上傳。在單擊 **OK**（即建立啟用狀態的規則）之前，請檢查地址限制和模式。

![WinBox new TFTP rule with address, filename, and access settings](/img/d950bb0f6f1145a0.webp)

截圖顯示的是空白的新建規則對話方塊。請在儲存前填寫限制條件；不受限制的規則可能會暴露路由器檔案。使用 **Files** 上傳你打算提供的檔案。

若要讓每個用戶端無論請求什麼名稱都得到同一個檔案，請設定 `req-filename=".*"`，並把 `real-filename` 設為某個檔案。僅對只獲取單個檔案的用戶端使用此方式；如果載入程式在獲取第一個檔案後還要獲取更多檔案，它只會再次得到同一個檔案：

```ros
/ip/tftp/add ip-addresses=192.168.88.0/24 req-filename=".*" \
    real-filename=tftp/boot.img
```

用一個檔案響應兩個名稱：

```ros
/ip/tftp/add ip-addresses=192.168.88.0/24 \
    req-filename="(aaa|bbb)\\.bin" real-filename=tftp/ccc.bin
```

其他磁碟上的檔案透過其路徑來提供，例如 `real-filename=usb1/tftp/boot.img`。

## 接受上傳 {#accept-uploads}

規則預設是隻讀的：上傳會收到 `illegal operation` 錯誤。要讓交換器把配置備份上傳到 `backups` 資料夾，需要允許寫入，併為以相同名稱重複出現的備份允許覆蓋。交換器會上傳到 `backups/<name>`，何時上傳由它們自身的設定決定：

```ros
/file/add name=backups type=directory
/ip/tftp/add ip-addresses=192.168.88.2-192.168.88.9 \
    req-filename="backups/[^/.][^/]*" read-only=no allow-overwrite=yes
```

- 如果沒有 `allow-overwrite=yes`，向已存在名稱的上傳會以 `file exists` 失敗。
- 同一條規則也會讓其用戶端下載已上傳的檔案，而這些檔案通常包含密碼，因此請把 `ip-addresses` 限制為這些交換器。
- 請把上傳規則放在任何同樣匹配 `backups/` 名稱的只讀規則之前，例如 `req-filename` 為空或為 `.*` 的規則；否則只讀規則會先做出響應。
- 上傳會佔用路由器的儲存空間；請不時刪除舊的備份。

## 拒絕部分請求 {#refuse-some-requests}

`allow=no` 的規則會拒絕它匹配的請求。請把它放在本會允許這些請求的規則之前，因為第一條匹配的規則做出決定。`req-filename` 匹配用戶端請求的名稱，而不是路由器上的路徑。例如，要拒絕某個更寬泛規則會提供的資料夾中的某一個檔案：

```ros
/ip/tftp/add ip-addresses=192.168.88.0/24 \
    req-filename="/\?secret\\.cfg" allow=no \
    place-before=[find real-filename=tftp]
```

把任何用戶端都不應讀取的檔案放在所服務資料夾之外。

## 檢查與故障排除 {#check-and-troubleshoot}

只要存在至少一條規則，伺服器就會監聽 UDP 埠 69，`hits` 統計每條規則應答的請求數：

```ros
/ip/service/print where name=tftpd
/ip/tftp/print
```

路由器會在 `tftp` 主題中記錄被拒絕和失敗的傳輸，例如 `ERROR code:0 string:permission denied!`。要檢視每個請求及其用戶端、檔名和結果，以及超時的傳輸，請同時記錄 `tftp,debug` 主題：

```ros
/system/logging/add topics=tftp,debug
/log/print where topics~"tftp"
```

偵錯資訊會顯示諸如 `requested (binary) file: phone.cfg access: allowed` 和 `connection timeout` 之類的內容。

用戶端會收到相同的 TFTP 錯誤：

| 錯誤 | 原因 |
| :-- | :-- |
| `permission denied!`（程式碼 0） | 沒有規則匹配用戶端地址和檔名，或者第一條匹配的規則設定了 `allow=no`。 |
| `file not found`（程式碼 1） | 有規則匹配，但它指向的檔案不存在。請檢查 `real-filename` 以及該檔案的路徑。 |
| `illegal operation`（程式碼 4） | 向只讀規則上傳，或在沒有 `allow-rollover=yes` 的情況下傳輸超過 65535 個數據塊。 |
| `file exists`（程式碼 6） | 在沒有 `allow-overwrite=yes` 的情況下向已存在的檔案上傳。 |
| 無應答 | 路由器沒有已啟用的 TFTP 規則，或者防火牆丟棄了 UDP 埠 69：預設防火牆只接受來自 `LAN` 介面列表中介面的請求。 |

:::tip
如果路由器收到了請求，但用戶端在傳輸過程中超時，請檢查塊大小：某些嵌入式用戶端會請求較大的塊大小，隨後卻無法處理分片封包。請把用戶端的塊大小設為路徑上最小的 MTU 減去 32 位元組（20 位元組為 IP 頭，8 位元組為 UDP，4 位元組為 TFTP），如果網路使用 IP 選項則還要更小：對於 1500 位元組的 MTU 即 1468 位元組。在路由器上，把 `max-block-size` 設為其提供的下一個更低值，例如 `/ip/tftp/settings/set max-block-size=1454`，或 `512`，後者同樣適用於 IPv6 和隧道。較小的塊大小會降低一次傳輸所能承載的最大檔案；參見[大檔案](#large-files)。
:::

## 規則如何匹配 {#how-rules-match}

- `ip-addresses` 列出用戶端：IPv4 地址、範圍（`192.168.88.2-192.168.88.9`）或字首，或 IPv6 字首。為空表示任意用戶端。
- `req-filename` 是以正則表示式表示的所請求檔名，區分大小寫。為空則匹配任意名稱。
- `real-filename` 決定提供什麼內容。為空時提供所請求的名稱本身，設為檔案時提供該檔案，設為資料夾時則放在所請求名稱之前。該值按原樣使用：不支援透過 `\1` 之類的引用來引用 `req-filename` 的各個部分。

`req-filename` 必須匹配整個所請求名稱：`phone\.cfg` 只匹配 `phone.cfg`，而 `.*\.cfg` 匹配所有以 `.cfg` 結尾的名稱。RouterOS 會在整個值前後新增錨點，因此請把備選項放在一個分組中：`(aaa|bbb)\.bin` 匹配 `aaa.bin` 和 `bbb.bin`，但 `(aaa.bin)|(bbb.bin)` 會匹配所有以 `aaa.bin` 開頭或以 `bbb.bin` 結尾的名稱。以 `^` 開頭的值會按原樣使用，因此 `^boot` 匹配所有以 `boot` 開頭的名稱，除非你在末尾加上 `$`。

正則表示式元素：

| 元素 | 含義 | 示例 |
| :-- | :-- | :-- |
| `.` | 任意一個字元 | `boo.` 匹配 `boot` 和 `boox` |
| `*` | 前一元素出現零次或多次 | `.*\.bin` 匹配所有 `.bin` 名稱 |
| `+` | 前一元素出現一次或多次 | `bo+t` 匹配 `bot` 和 `boot` |
| `?` | 前一元素出現一次或不出現 | `x?boot` 匹配 `boot` 和 `xboot` |
| `[ ]` | 所列字元中的任意一個 | `boo[tx]` 匹配 `boot` 和 `boox` |
| `( \| )` | 分組與備選項 | `(aaa\|bbb)\.bin` 匹配 `aaa.bin` 和 `bbb.bin` |
| `\` | 將下一個字元按字面處理 | `\.` 匹配一個點 |
| `^`、`$` | 名稱的開頭和結尾 | `^boot` 匹配以 `boot` 開頭的名稱 |

在終端中，雙引號內的值要用兩個反斜槓表示一個（`"(aaa|bbb)\\.bin"`），用 `\$` 表示美元符號，用 `\?` 表示問號，因為控制檯自身會處理 `\`、`$` 和 `?`（`?` 顯示幫助）。

## 技術細節 {#technical-details}

### 傳輸 {#transfers}

- 預設情況下，用戶端和伺服器一次交換一個數據塊，每個資料塊在下一次傳送之前都會被確認。
- 用戶端可以請求更大的塊大小（`blksize`）；路由器最多同意 `/ip/tftp/settings` 中 `max-block-size` 所允許的值：`512`、`1454`、`4096`（預設）或 `8192`。路由器也會應答傳輸大小選項（`tsize`）。它不協商視窗大小（`windowsize`）。
- 在規則上設定 `reading-window-size=pipelining` 時，路由器會在等待確認前先發送下載的多個數據塊，從而加快下載速度。預設值為 `none`。
- 伺服器在 `/ip/tftp/settings` 中由 `vrf` 設定的 VRF 中監聽（預設為 `main`）。

### 大檔案 {#large-files}

TFTP 用 16 位對傳輸的資料塊編號，因此一次傳輸在 65535 個數據塊處結束：512 位元組塊時約為 32 MiB，1454 位元組塊時約為 90 MiB，4096 位元組塊時約為 256 MiB。設定 `allow-rollover=yes` 後，路由器會在第 65535 個數據塊之後從第 0 個數據塊繼續，從而完成更大的檔案；用戶端必須支援這種迴繞。若不啟用，傳輸會在達到上限時以 `illegal operation` 失敗。要在資料夾規則上允許該行為：

```ros
/ip/tftp/set [find real-filename=tftp] allow-rollover=yes
```

有關所有屬性，請參閱 CLI 參考中的 [`/ip/tftp`](../cli-reference/ip/tftp/index.md) 和 [`/ip/tftp/settings`](../cli-reference/ip/tftp/settings.md)。
