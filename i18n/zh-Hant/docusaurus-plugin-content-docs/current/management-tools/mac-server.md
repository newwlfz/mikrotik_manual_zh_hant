---
sidebar_key: "management-tools/mac-server"
sidebar_position: 11
title: "MAC 伺服器"
sidebar_label: "MAC 伺服器"
description: "RouterOS MAC 伺服器允許您在同一二層網段上透過路由器的 MAC 地址訪問路由器，無需配置 IP：使用 MAC Telnet 連線，使用 MAC scan 查詢路由器，將 MAC Telnet 和 MAC WinBox 限制為僅受信任的介面可用，並使用 MAC ping。"
tags:
  - 'mac-server'
  - 'mac-telnet'
  - 'mac-winbox'
source: https://manual.mikrotik.com/docs/management-tools/mac-server
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MAC 伺服器讓你可以從同一二層網段上的裝置透過路由器的 MAC 地址訪問它，且兩端都不需要任何 IP 配置。它提供三項功能：

- MAC Telnet - 控制檯會話，類似於基於 IP 的 Telnet。RouterOS 用戶端為 `/tool/mac-telnet`。
- MAC WinBox - [WinBox](./winbox.md) 透過路由器的 MAC 地址進行連線。
- MAC ping - 應答傳送到路由器 MAC 地址的 ping。

當你需要恢復 IP 設定錯誤或缺失的路由器，或對新路由器進行首次設定時，可以使用 MAC 訪問。預設配置僅允許在 `LAN` 介面列表中的介面上使用 MAC Telnet 和 MAC WinBox，該列表包含 LAN 網橋：在大多數路由器上，即除 WAN 埠 `ether1` 之外的所有埠以及 Wi-Fi 介面。如果沒有預設配置，則所有介面上都允許使用它們。MAC ping 伺服器預設開啟。在生產網路中，你應當關閉 MAC 訪問，或將其限制為僅允許受信任的介面；請參閱[保護你的路由器](../getting-started/securing-your-router.md#routeros-mac-access)。若要透過 MAC 地址訪問跨越一個二層網段的路由器，請使用 [RoMON](./romon.md)。

## 使用 MAC Telnet 連線 {#connect-with-mac-telnet}

在計算機上，可以使用 [WinBox](./winbox.md#device-list-section)：**Neighbors** 標籤頁會列出網路中的路由器，選中 MAC 地址即可透過 MAC WinBox 連線。WinBox 還帶有終端。若從另一臺 RouterOS 裝置發起，先用 MAC 掃描或在[鄰居列表](../system-information-and-utilities/neighbor-discovery.md)中找到路由器的 MAC 地址，然後用 MAC Telnet 連線：

```ros
/tool/mac-telnet FE:F1:E6:82:D5:B6
```

```text
Login: admin
Password:
Trying FE:F1:E6:82:D5:B6...
Connected to FE:F1:E6:82:D5:B6

  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

  MikroTik RouterOS 7.25beta5 (c) 1999-2026       https://www.mikrotik.com/

Press F1 for help

[admin@Test2] >
```

MAC Telnet 使用使用者名稱和密碼登入；SSH 金鑰不適用。使用者所屬的組需要具備 `telnet` 策略。登入後，修正 IP 設定，例如在 [`/ip/address`](../cli-reference/ip/address.md) 中操作。當目標不響應或拒絕連線時（例如因為請求到達的介面上不允許 MAC Telnet），用戶端會列印 `Trying ...` 並返回到本地提示符，且不顯示任何錯誤資訊。

如果不指定 `interface`，用戶端會從路由器的每個介面發出連線嘗試。若只從一個介面發出：

```ros
/tool/mac-telnet FE:F1:E6:82:D5:B6 interface=ether1
```

你連線的路由器會列出已開啟的 MAC Telnet 會話，其中包含會話到達的介面和用戶端的 MAC 地址：

```ros
/tool/mac-server/sessions/print
```

```text
Columns: INTERFACE, SRC-ADDRESS, UPTIME
#  INTERFACE  SRC-ADDRESS        UPTIME
0  ether2     DC:2C:6E:E7:10:6A  2s
```

該列表只顯示 MAC Telnet 會話，不顯示 MAC WinBox 連線。這些會話也會出現在 `/user/active` 中，`VIA` 列顯示為 `mac-telnet`。

## 使用 MAC 掃描查詢路由器 {#find-routers-with-mac-scan}

MAC 掃描會列出在某個介面上傳送 MikroTik 鄰居發現（MNDP）通告的裝置，以及它們的 MAC 地址和 IPv4 地址：

```ros
/tool/mac-scan interface=ether2 duration=8s
```

```text
Columns: MAC-ADDRESS, ADDRESS, AGE
MAC-ADDRESS        ADDRESS      AGE
FE:F1:E6:82:D5:B6  203.0.113.1   17
```

`AGE` 是自該裝置上次通告以來經過的秒數。該列表來自[鄰居發現](../system-information-and-utilities/neighbor-discovery.md)，而非 MAC 伺服器：無論裝置的 MAC 伺服器設定如何，它都會出現在列表中；而在該介面上關閉了鄰居發現的裝置則不會出現。該列表包含在掃描開始之前就已被監聽到的裝置，因此 `AGE` 可能大於 `duration`；預設情況下裝置每 30 秒通告一次自身。`/ip/neighbor/print` 會顯示相同的裝置，但包含更多詳細資訊，例如標識和 RouterOS 版本。

對於網橋，請掃描它的某個埠或使用 `interface=all`：網橋介面本身不會顯示任何裝置。如果不指定 `duration`，掃描會一直執行，直到你用 <kbd>Control</kbd>+<kbd>C</kbd> 停止它。採用 SMIPS 架構的裝置不支援 MAC 掃描。

## 僅在受信任的介面上允許 MAC 訪問 {#allow-mac-access-only-on-trusted-interfaces}

MAC Telnet 和 MAC WinBox 各自有獨立的 `allowed-interface-list` 設定：MAC Telnet 使用 `/tool/mac-server`，MAC WinBox 使用 `/tool/mac-server/mac-winbox`。兩者都接受一個[介面列表](../cli-reference/interface/list/index.md)。

若只允許在 LAN 上使用 MAC Telnet 和 MAC WinBox：

```ros
/tool/mac-server/set allowed-interface-list=LAN
/tool/mac-server/mac-winbox/set allowed-interface-list=LAN
```

預設配置已經包含 `LAN` 列表，其中包含 LAN 網橋。在沒有該列表的路由器上，請先建立列表：

```ros
/interface/list/add name=LAN
/interface/list/member/add list=LAN interface=bridge
```

使用 `/tool/mac-server/print` 和 `/tool/mac-server/mac-winbox/print` 檢查當前設定。

請把網橋加入列表，而不是它的埠：列表中的網橋允許透過其任意埠到達的連線，而僅把網橋埠加入列表則不允許這些連線。更改會立即對下一次連線生效；已開啟的會話會保持開啟狀態。

若要排除網橋的某個埠，例如訪客 Wi-Fi 網路的埠，可以用網橋過濾規則在該埠上丟棄 MAC 訪問，或把訪客放到它們自己的網橋上：

```ros
/interface/bridge/filter/add chain=input in-interface=wifi2 \
    mac-protocol=ip ip-protocol=udp dst-port=20561 action=drop
```

若要關閉 MAC Telnet 和 MAC WinBox，請把列表設定為 `none`：

```ros
/tool/mac-server/set allowed-interface-list=none
/tool/mac-server/mac-winbox/set allowed-interface-list=none
```

你建立的不含任何成員的介面列表同樣會阻止 MAC 訪問。

:::note
IP 防火牆無法保護 MAC 訪問：丟棄 UDP 埠 20561 的 IP 過濾規則並不會阻止 MAC Telnet 或 MAC ping。請使用 `allowed-interface-list` 限制 MAC 訪問，或在橋埠上使用橋接過濾規則。關於 RouterOS 使用的其他埠，請參閱[服務](../system-information-and-utilities/services.md)。

在橋上啟用 [IP Source Guard](../bridging-and-switching/index.md#arp-inspection-and-ip-source-guard) 會阻止其不受信任埠上的 MAC Telnet、MAC WinBox 和 MAC ping。
:::

## MAC ping {#mac-ping}

MAC ping 伺服器（`/tool/mac-server/ping`）應答傳送到路由器 MAC 地址的 ping。它預設啟用。要 ping 某個 MAC 地址，請參閱 [Ping MAC 地址](../diagnostics-monitoring-and-troubleshooting/ping.md#ping-a-mac-address)。

若要關閉 MAC ping 伺服器：

```ros
/tool/mac-server/ping/set enabled=no
```

關閉伺服器後，路由器不再應答 MAC ping，也無法傳送 MAC ping：它自己發出的 MAC ping 會失敗，狀態為 `unknown interface`。無論此設定如何，ARP ping 在兩個方向上都能正常工作。

## 技術細節 {#technical-details}

### 傳輸 {#transport}

MAC Telnet、MAC WinBox 和 MAC ping 使用 UDP 埠 20561，其封裝在發往目標 MAC 地址的乙太網幀中。IP 頭中攜帶的地址為 0.0.0.0 和 255.255.255.255，因此這些封包不依賴於 IP 配置。MAC 伺服器直接從介面獲取這些封包，因此 IP 防火牆規則無法阻止它們。

### 安全 {#security}

MAC Telnet 不加密。你輸入的命令和路由器的輸出都以明文形式透過鏈路傳輸。密碼不會以明文傳送：登入採用質詢—應答方式。請在受信任的鏈路上使用 MAC Telnet，例如用於恢復路由器；日常訪問請使用 SSH。

MAC 登入沒有 IP 地址，因此 `/user` 中使用者的 `address` 設定對它不適用：即使某個使用者被限制為只能從特定 IP 地址登入，該使用者仍可透過 MAC Telnet 登入。組策略則依然生效。

有關所有引數，請參閱 CLI 參考中的 [`/tool/mac-server`](../cli-reference/tool/mac-server/index.md)、[`/tool/mac-telnet`](../cli-reference/tool/mac-telnet.md) 和 [`/tool/mac-scan`](../cli-reference/tool/mac-scan.md)。
