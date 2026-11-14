---
sidebar_key: "bridging-and-switching/user-guides/loop-protect"
sidebar_position: 6
title: "環路保護"
sidebar_label: "環路保護"
description: "Loop Protect 透過檢測並停用接收到自身 loop-protect 封包的介面來防止二層環路，並具有可配置的間隔和停用時間。它支援 Ethernet、VLAN、EoIP 和 VxLAN 介面，不過對於網橋建議使用 (R/M)STP。"
tags:
  - 'loop-protect'
  - 'ethernet'
  - 'vlan'
source: https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/loop-protect
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

loop protect 功能可以透過傳送 loop protect 協定封包，並在介面收到源自自身的 loop protect 封包時關閉介面，來防止二層環路。該功能透過將收到的 loop-protect 封包的源 MAC 地址與啟用了 loop-protect 的介面的 MAC 地址進行比對來工作。如果找到匹配項，loop protect 會停用收到該 loop protect 封包的介面。日誌訊息會對此事件發出警告，系統還會用 loop protect 註釋標記該介面。RouterOS 的 loop protect 功能既可用於橋接介面，也可用於在 RouterBoard 交換晶片中設定為交換模式的 Ethernet 介面。

Loop Protect 適用於 Ethernet、VLAN、EoIP、VxLAN 介面，其封包使用 EtherType 0x9003 封裝。  
loop protect 封包間隔和介面停用時間可以調整。配置更改或停用時間到期會重設介面上的環路保護。

:::warning
儘管 loop-protect 可用於已加入網橋的介面，但仍建議使用 (R/M)STP 而不是 loop-protect，因為 (R/M)STP 與大多數交換器相容，並且 STP 變體提供了更多配置選項來微調網路。
:::

**子選單：** `/interface/ethernet, /interface/vlan, /interface/eoip, /interface/eoipv6, /interface/vxlan`

| 屬性 | 描述 |
| :-- | :-- |
| **loop-protect** (*on \| off \| default*; 預設：**default**) | 在所選介面上啟用或停用 loop protect。**default** 相當於關閉。 |
| **loop-protect-send-interval** (*時間間隔*; 預設：**5s**) | 設定所選介面上傳送 loop protect 封包的頻率。 |
| **loop-protect-disable-time** (*時間間隔 \| 0*; 預設：**5m**) | 設定檢測到環路時所選介面被停用的時長。**0** - 永久。 |

### 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **loop-protect-status** (*on \| off \| disable*) | on - loop-protect 功能已開啟，介面正在傳送並監聽 loop protect 封包；off - loop-protect 功能已關閉；disable - loop-protect 功能已開啟，介面已收到 loop protect 封包並停用自身以防止環路。 |
