---
sidebar_key: "firewall-and-quality-of-service/firewall/mangle"
sidebar_position: 5
title: "Mangle"
sidebar_label: "Mangle"
description: "RouterOS 中的 Mangle 使用特殊標記來標記封包，以便進行高階處理，從而支援 queue trees 和 NAT 等功能。它會修改 IP 報頭欄位，並透過五個預定義鏈（PREROUTING、INPUT、OUTPUT、FORWARD、POSTROUTING）執行，以根據封包標記或連線狀態應用規則。"
tags:
  - 'firewall-mangle'
  - 'ip-header-modification'
  - 'packet-marking'
source: https://manual.mikrotik.com/docs/7.25/firewall-and-quality-of-service/firewall/mangle
captured_at: '2026-11-04T11:15:43+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Mangle 是一種“標記器”，用於為封包打上標記，以便後續使用特殊標記進行處理。RouterOS 中的許多其他功能都會使用這些標記，例如佇列樹、NAT、路由。它們根據封包上的標記來識別封包，並據此進行處理。mangle 標記僅存在於路由器內部，不會透過網路傳輸。

此外，mangle 功能還用於修改 IP 頭中的某些欄位，例如 TOS（DSCP）和 TTL 欄位。

防火牆 mangle 規則由五個預定義鏈組成，這些鏈無法刪除：

![](/img/741de7e87a2a3707.webp)

- **PREROUTING** 鏈：此鏈中的規則應用於封包剛到達網路介面時。
- **INPUT** 鏈：此鏈中的規則應用於封包即將交給本地程式之前。
- **OUTPUT** 鏈：此處的規則應用於封包剛由程式生成之後。
- **FORWARD** 鏈：此處的規則應用於任何通過當前主機路由的封包。
- **POSTROUTING** 鏈：此鏈中的規則應用於封包剛離開網路介面時。

## 配置示例 {#configuration-example}

### 更改 MSS {#change-mss}

眾所周知，由於封裝開銷，VPN 鏈路的封包大小較小。如果大型封包的 MSS 超過 VPN 鏈路的 MSS，則應在透過此類連線傳送之前進行分片。但是，如果封包設定了 *Don't Fragment* 標誌，則無法對其進行分片，應將其丟棄。在路徑 MTU 發現（PMTUD）損壞的鏈路上，這可能會導致許多問題，包括 FTP 和 HTTP 資料傳輸以及電子郵件服務的問題。

對於 PMTUD 損壞的鏈路，減小透過 VPN 鏈路的封包的 MSS 可以解決該問題。以下示例演示如何透過 mangle 減小 MSS 值：

```ros
/ip/firewall/mangle/add out-interface=pppoe-out protocol=tcp tcp-flags=syn action=change-mss new-mss=1300 chain=forward tcp-mss=1301-65535
```

### 標記連線 {#marking-connections}

有時需要對屬於特定連線的封包執行某些操作（例如，為佇列標記來自/發往特定主機的封包），但檢查每個封包的 IP 頭是一項相當昂貴的任務。我們可以使用連線標記來稍微最佳化設定。

```ros
/ip/firewall/mangle
add chain=forward in-interface=local src-address=192.168.88.123 connection-state=new action=mark-connection new-connection-mark=client_conn
add chain=forward connection-mark=client_conn action=mark-packet new-packet-mark=client_p
```

:::danger
警告：封包標記最多限制為 4096 個唯一條目。超過此限制將導致錯誤 "bad new packet mark"。
:::
