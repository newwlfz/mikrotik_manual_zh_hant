---
title: "迴路保護"
description: "Loop Protect 透過偵測並停用接收自身 loop-protect 封包的介面，防止 Layer2 迴圈，並可設定間隔與停用時間。它支援 Ethernet、VLAN、EoIP 與 VxLAN 介面，不過橋接器建議使用 (R/M)STP。"
tags:
  - 'loop-protect'
  - 'ethernet'
  - 'vlan'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/loop-protect
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

loop protect 功能可透過傳送 loop protect 協定封包，並在介面收到源自自身的 loop protect 封包時關閉介面，以避免 Layer2 迴圈。此功能會檢查收到的 loop-protect 封包來源 MAC 位址，與啟用 loop-protect 的介面 MAC 位址進行比對。若找到相符項目，loop protect 會停用收到 loop protect 封包的介面。系統會記錄警告訊息，並以 loop protect 註記標示該介面。RouterOS loop protect 功能可用於橋接介面，也可用於在 RouterBoard 交換器晶片上設定為交換模式的 Ethernet 介面。

Loop Protect 可用於 Ethernet、VLAN、EoIP、VxLAN 介面，其封包會以 EtherType 0x9003 封裝。  
loop protect 封包間隔與介面停用時間可調整。設定變更或停用時間期滿會重設介面上的 loop protection。

:::warning
即使 loop-protect 可用於加入 bridge 的介面，仍建議使用 (R/M)STP 而非 loop-protect，因為 (R/M)STP 與大多數交換器相容，且 STP 變體提供更多設定選項，可供您微調網路。
:::

**子選單：** `/interface/ethernet, /interface/vlan, /interface/eoip, /interface/eoipv6, /interface/vxlan`

| 屬性 | 說明 |
| :-- | :-- |
| **loop-protect** (*on \| off \| default*；預設：**default**) | 啟用或停用所選介面的 loop protect。**default** 等同於關閉。 |
| **loop-protect-send-interval** (*time interval*；預設：**5s**) | 設定在所選介面上傳送 loop protect 封包的頻率。 |
| **loop-protect-disable-time** (*time interval \| 0*；預設：**5m**) | 設定偵測到迴圈時，所選介面被停用的時間。**0** 表示永久。 |

### 唯讀屬性 {#read-only-properties}

| 屬性 | 說明 |
| :-- | :-- |
| **loop-protect-status** (*on \| off \| disable*) | <ul><li><strong>on</strong> - loop-protect 功能已開啟，介面正在傳送並監聽 loop protect 封包</li><li><strong>off</strong> - loop-protect 功能已關閉</li><li><strong>disable</strong> - loop-protect 功能已開啟，介面已收到 loop protect 封包並停用自身以防止迴圈。</li></ul> |
