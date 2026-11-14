---
sidebar_key: "cli-reference/cmr/device"
title: "device"
source: https://manual.mikrotik.com/docs/cli-reference/cmr/device
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/device {#cmrdevice}
**軟體包:** cmr
**型別:** 目錄

此 CMR 伺服器管理的裝置。裝置一旦連線到伺服器就會出現在列表中，並在配對獲得批准之前帶有 **P** 標記。伺服器本身顯示為帶有 **L** 標記的裝置。使用此選單中的命令對裝置群進行操作，例如 `run-script`、`upgrade`、`reboot` 或 `pair`。有關裝置如何連線和配對，請參閱 [CMR](../../management-tools/cmr.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="P" typ="pending">配對待處理。</ArgTableRow>
<ArgTableRow arg="p" typ="remote-pending">控制器請求配對。</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">裝置處於非活動狀態。</ArgTableRow>
<ArgTableRow arg="S" typ="stale">無連線（陳舊）。</ArgTableRow>
<ArgTableRow arg="L" typ="controller">CMR 伺服器本身（自身用戶端）。</ArgTableRow>
<ArgTableRow arg="C" typ="connected">裝置已連線。</ArgTableRow>
<ArgTableRow arg="U" typ="upgrade-available">裝置的升級通道提供的版本與已安裝版本不同。提供的版本也可能早於已安裝版本。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ids" typ="object { ids: super { his-id: string
, [our-id] [ /string]
 }
 }">受管裝置的身份標識（his-id / our-id）。</ArgTableRow>
<ArgTableRow arg="pairing-requirement" typ="enum (none | password | confirm)">應用於此裝置的配對要求，覆蓋伺服器預設值：`none`、`password` 或 `confirm`。</ArgTableRow>
<ArgTableRow arg="labels" typ="multi { array-id, label: enum
 }" unset="1">分配給裝置的使用者標籤（分組/過濾）。</ArgTableRow>
<ArgTableRow arg="port-labels" typ="object { port-and-labels: super { port: string
, [labels] :multi { array-id, label: string
 }
 }
 }" unset="1">每個埠的標籤。為標籤加引號，例如 `port-labels=ether1:"uplink"`。`/cmr/vlan` 規則可根據這些標籤選擇埠。</ArgTableRow>
<ArgTableRow arg="identity" typ="string">裝置的系統標識（可編輯）。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="peer" typ="enum">此裝置連線到的管理對端。</ArgTableRow>
<ArgTableRow arg="board" typ="string">板卡名稱。</ArgTableRow>
<ArgTableRow arg="version" typ="string">裝置的 RouterOS 版本。</ArgTableRow>
<ArgTableRow arg="minimum-version" typ="string">最低支援版本。</ArgTableRow>
<ArgTableRow arg="allowed-versions" typ="string">安全（safepkg）升級指示器。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">當前連線地址。</ArgTableRow>
<ArgTableRow arg="auto-labels" typ="multi { array-id, label: string
 }" unset="1">自動分配的標籤。</ArgTableRow>
<ArgTableRow arg="packages" typ="multi { array-id, label: string
 }" unset="1">已安裝的軟體包。</ArgTableRow>
<ArgTableRow arg="state" typ="string">裝置狀態。</ArgTableRow>
<ArgTableRow arg="upgrade-rule" typ="enum">覆蓋此裝置的升級規則。在 [`/cmr/upgrade`](/docs/cli-reference/upgrade) 規則列表中，第一條覆蓋該裝置的規則會認領它，因此放在頂部的 `labels=all` 規則會覆蓋所有裝置。</ArgTableRow>
<ArgTableRow arg="channel" typ="alt">當前升級通道/版本。</ArgTableRow>
<ArgTableRow arg="available-version" typ="string">可用的最新升級。</ArgTableRow>
<ArgTableRow arg="connected-time" typ="time" unset="1">裝置已連線的時間。</ArgTableRow>
<ArgTableRow arg="uptime" typ="time" unset="1">裝置執行時間。</ArgTableRow>
<ArgTableRow arg="disconnected-since" typ="date" unset="1">自裝置斷開連線以來的時間。</ArgTableRow>
<ArgTableRow arg="alerts" typ="super { on: num
, [all] /num
, [critical]  num
, [high] /num
, [medium] /num
, [low] /num
 }">按嚴重級別統計的已啟用/總告警計數。</ArgTableRow>
<ArgTableRow arg="serial" typ="string">出廠序列號。</ArgTableRow>
</ArgTable>
