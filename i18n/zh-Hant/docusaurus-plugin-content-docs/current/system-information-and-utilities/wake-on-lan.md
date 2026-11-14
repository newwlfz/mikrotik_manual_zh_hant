---
sidebar_key: "system-information-and-utilities/wake-on-lan"
sidebar_position: 17
title: "網路喚醒"
sidebar_label: "網路喚醒"
description: "使用 RouterOS 發出的 Wake on LAN 魔術包喚醒區域網路中的計算機：可按需喚醒、從網路外部透過路由器喚醒、按計劃喚醒，或用一條命令喚醒多臺計算機。"
tags:
  - 'wol'
  - 'ip-broadcast'
  - 'mac'
source: https://manual.mikrotik.com/docs/system-information-and-utilities/wake-on-lan
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Wake on LAN (WoL) 透過傳送魔術包來開啟已關機或休眠的計算機：該封包包含六個 `FF` 位元組，後跟計算機的 MAC 地址重複 16 次。路由器始終開機並連線到 LAN，因此它可以在你不在時或指定時間喚醒計算機。

計算機必須支援 Wake on LAN，並在其韌體（BIOS 或 UEFI）和網路介面卡設定中啟用該功能。大多數計算機只能透過有線乙太網連線喚醒。不支援 SecureOn 密碼。

## 在 LAN 中喚醒計算機 {#wake-a-computer-on-the-lan}

給出計算機的 MAC 地址以及它所連線的介面，例如 LAN 網橋：

```ros
/tool/wol mac=FE:4B:71:05:EA:8B interface=bridge
```

路由器在該介面上廣播魔術包。當介面是網橋時，封包會到達其所有埠；對於位於 VLAN 中的計算機，請指定 VLAN 介面。該命令不輸出任何內容。要確認計算機已喚醒，請在它有足夠時間啟動後對它執行 [ping](../diagnostics-monitoring-and-troubleshooting/ping.md)。

請始終指定 `interface`。若不指定，路由器會透過其預設路由以 IP 廣播方式傳送魔術包，而在大多數路由器上，預設路由是網際網路連線，而不是 LAN。

請在計算機開機時記錄其 MAC 地址。[DHCP 伺服器租約](../network-management/dhcp/server.md#leases)會連同主機名一起顯示它，而 ARP 表則可按地址顯示：

```ros
/ip/arp/print where address=192.168.88.20
```

計算機關機後，ARP 表項會在一段時間後消失，因此請儲存好 MAC 地址，例如儲存在靜態 DHCP 租約中。

## 在 WinBox 中傳送喚醒封包 {#send-a-wake-packet-in-winbox}

開啟 **Tools > WoL**：

1. 輸入目標裝置的 **MAC Address**。截圖中使用的是命令示例中的地址。
2. 在 **Interface** 中，選擇可到達該計算機的介面，例如預設配置中的 `bridge`。截圖中顯示的是 `ether1`。

![WinBox Wake on LAN dialog with target MAC Address and outgoing Interface](/img/6fa60a159e9dc978.webp)

選擇 **Wake on LAN** 傳送封包，或選擇 **Cancel** 關閉對話方塊而不傳送。目標裝置必須在自身的硬體和作業系統中啟用 Wake on LAN。

## 從網路外部喚醒計算機 {#wake-a-computer-from-outside-the-network}

透過 VPN 連線到路由器，例如 [Back To Home（遠端回家）](../network-management/cloud/back-to-home.md) 或 [WireGuard](../virtual-private-networks/wireguard.md)。然後透過該 VPN 開啟 WinBox、WebFig 或到路由器的 SSH 會話，並在其中執行該命令。路由器會在 LAN 上傳送魔術包，計算機便能在那裡收到它。

## 在指定時間喚醒計算機 {#wake-a-computer-at-a-set-time}

要每天早上 07:45 開啟辦公計算機，請新增一條 [scheduler](./scheduler.md) 條目。scheduler 使用路由器的時鐘，因此請在 [時鐘](./clock.md) 中檢查其時間和時區：

```ros
/system/scheduler/add name=wake-office-pc interval=1d \
    start-time=07:45:00 \
    on-event="/tool/wol mac=FE:4B:71:05:EA:8B interface=bridge"
```

## 喚醒多臺計算機 {#wake-several-computers}

要用一條命令喚醒一組計算機，請列出它們的 MAC 地址：

```ros
:foreach m in={"FE:4B:71:05:EA:8B";"FE:4B:71:05:EA:8C"} do={
    /tool/wol mac=$m interface=bridge
}
```

若只在工作日喚醒該組計算機，請把迴圈放進指令碼，並在 scheduler 中使用 `days` 執行它：

```ros
/system/script/add name=wake-office-pcs source={
    :foreach m in={"FE:4B:71:05:EA:8B";"FE:4B:71:05:EA:8C"} do={
        /tool/wol mac=$m interface=bridge
    }
}
/system/scheduler/add name=wake-office days=mon,tue,wed,thu,fri \
    start-time=07:45:00 on-event=wake-office-pcs
```

## 技術細節 {#technical-details}

魔術包包含 6 個位元組的 `FF`，後跟重複 16 次的目標 MAC 地址。RouterOS 以兩種形式之一發送它：

- 指定 `interface` 時：一個 EtherType 為 `0x0842`（Wake on LAN）的乙太網幀，從該介面的 MAC 地址發往廣播 MAC 地址 `FF:FF:FF:FF:FF:FF`。它不需要 IP 配置，並且停留在該二層網段內。
- 不指定 `interface` 時：一個發往 `255.255.255.255` 埠 9 的 UDP 封包，從路由器的地址發出，經由預設路由的介面傳送。

有關引數，請參閱 [`/tool/wol` CLI 參考](../cli-reference/tool/wol.md)。
