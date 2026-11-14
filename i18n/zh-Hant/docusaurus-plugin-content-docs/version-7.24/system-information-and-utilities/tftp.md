---
sidebar_key: "system-information-and-utilities/tftp"
sidebar_position: 16
title: "TFTP"
sidebar_label: "TFTP"
description: "TFTP 頁面介紹 MikroTik RouterOS 對簡單檔案傳輸協定（Trivial File Transfer Protocol）的實現，詳細說明 TFTP 伺服器訪問規則的配置選項，包括 IP 地址範圍、檔名處理、塊大小限制以及對用戶端請求的正則表示式支援。"
tags:
  - 'tftp'
  - 'ip-addresses'
  - 'settings'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/tftp
captured_at: '2026-11-04T11:33:40+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

簡單檔案傳輸協定（Trivial File Transfer Protocol），或簡稱 TFTP，是一種用於傳輸檔案的非常簡單的協定。每個非終結封包都會被單獨確認。

**子選單：** `/ip/tftp`

此選單包含所有 TFTP 訪問規則。如果此選單中沒有規則，則 RouterOS 啟動時不會啟動 TFTP 伺服器。與建立規則時可設定的內容相比，此選單僅多顯示 1 個屬性。

## 引數 {#parameters}

| 屬性 | 描述 |
| :-- | :-- |
| **ip-addresses** *(必填)* | 作為用戶端接受的 IP 地址範圍。如果為空，將使用 *0.0.0.0/0* |
| **allow-rollover** *(預設值：No)* | 如果設定為 *yes*，則當達到最大值時，TFTP 伺服器將允許序列號迴繞。這用於支援透過 TFTP 伺服器進行大型下載。 |
| **req-filename** | 請求的檔名，作為 *正則表示式 (regex)*。如果欄位留空，則預設為 *.\** |
| **real-filename** | 如果 **req-filename** 和 **real-filename** 的值已設定且有效，則請求的檔名將被替換為匹配的檔案。此欄位必須設定。如果在 *req-filename* 中指定了多個 *regex*，則可以使用此欄位設定應匹配哪些正則表示式，以便驗證此規則。使用多個 *regex* 時，*real-filename* 的格式為 **filename\0\5\6** |
| **allow** (*預設值：yes*) | 如果上述欄位已設定，則允許連線。如果為 *no*，連線將被中斷 |
| **read-only** (*預設值：no*) | 設定檔案是否可寫入；如果設定為 "yes"，寫入嘗試將失敗並報錯 |
| **hits** *(read-only)* | 此訪問規則條目已被使用多少次（read-only） |

### 設定 {#settings}

**子選單：** `/ip/tftp/settings`

此選單包含所有 TFTP 設定。

| 屬性 | 描述 |
| :-- | :-- |
| **max-block-size** (*預設值：4096*) | 可接受的最大塊大小值。在傳輸協商階段，RouterOS 裝置不會協商比此值更大的值。 |

## 正則表示式 {#regexp}

Req-filename 欄位允許使用正則表示式，此欄位中允許的正則表示式如下：

### 括號 () - 標記子節 {#brackets----marking-subsection}

```
    example 1 a(sd|fg) will match asd or afg

```

### 星號 "\*" - 匹配前面的符號零次或多次 {#asterisk----match-zero-or-more-times-preceding-symbol}

```
    example 1 a* will match any length name consisting purely of symbols a or no symbols at all
    example 2 .* will match any length name, also, empty field
    example 3 as*df will match adf, asdf, assdf, asssdf etc.

```

### 加號 "+" 將匹配前面的符號一次或多次 {#plus--will-match-one-or-more-times-the-preceding-symbol}

```
    example: as+df will match asdf, assdf etc.

```

### 點號 "." - 匹配任意符號 {#dot----matches-any-symbol}

```
    example as.f will match asdf, asbf ashf etc.

```

### 方括號 [] - 在列出的字元之間任選一個 {#square-brackets----variation-between}

```
    example as[df] will match asd and asf

```

### 問號 "?" 將匹配一個或零個符號 {#question-mark--will-match-one-or-no-symbols}

```
    example asd?f will match asdf and asf

```

### 脫字元 "^" - 用在行首表示該行以某內容開頭 {#caret----used-at-the-beginning-of-the-line-means-that-the-line-starts-with}

### 美元符號 "$" - 表示在行尾 {#dollar----means-at-the-end-of-the-line}

## 示例 {#examples}

如果請求某個檔案，則從名為 sata1 的儲存返回該檔案：

```ros
/ip/tftp/add req-filename=file.txt real-filename=/sata1/file.txt allow=yes read-only=yes
```

如果我們想無論使用者請求什麼都返回同一個特定 *檔案*：

```ros
/ip/tftp/add req-filename=.* real-filename=/sata1/file.txt allow=yes read-only=yes
```

 如果使用者請求 *aaa.bin* 或 *bbb.bin*，則向他們提供 *ccc.bin*：

```ros
/ip/tftp/add req-filename="(aaa.bin)|(bbb.bin)" real-filename="/sata1/ccc.bin\\0" allow=yes read-only=yes
```

:::tip

RouterOS 收到 TFTP 請求，但用戶端卻發生傳輸超時？

某些嵌入式用戶端會請求較大的塊大小，卻不能正確處理分片封包。對於這些用戶端，建議將 RouterOS 側的 "max-block-size" 或用戶端側的 "blksize" 設定為網路中最小 MTU 的值減去 32 位元組（IP 為 20 位元組，UDP 為 8 位元組，TFTP 為 4 位元組）；如果網路中使用了 IP 選項，則還應減去更多。

:::
