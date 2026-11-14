---
sidebar_key: "firewall-and-quality-of-service/upnp"
sidebar_position: 7
title: "UPnP"
sidebar_label: "UPnP"
description: "RouterOS 中的 Universal Plug and Play (UPnP)：一種 Internet Gateway Device 服務，允許 LAN 應用請求埠對映。路由器會為所請求的埠建立動態目標 NAT 規則。涵蓋啟用該服務、標記外部和內部介面以及安全影響。"
tags:
  - 'upnp'
  - 'nat'
source: https://manual.mikrotik.com/docs/firewall-and-quality-of-service/upnp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

通用即插即用（UPnP）允許本地網路中的應用程式向路由器請求埠對映。當用戶端請求對映時，RouterOS 會建立一條動態目標 NAT 規則，將請求的外部埠轉發到該用戶端。接受傳入連線的應用程式（例如遊戲、點對點用戶端以及語音或視訊通話）隨後即可在 NAT 後方正常工作，無需手動進行埠轉發。

RouterOS 為 IPv4 實現 UPnP 網際網路閘道器裝置（IGD）配置檔案。用戶端透過 SSDP 發現路由器，並透過 WANIPConnection 服務請求對映。UPnP 服務預設處於停用狀態。RouterOS 還支援 [NAT-PMP](./nat-pmp.md)，這是一種在 Apple 裝置上常見的類似協定。

UPnP 只負責目標 NAT 這一側。外部介面仍然需要常規的源 NAT（masquerade）規則，以便回覆流量能夠到達用戶端。

## 安全注意事項 {#security-considerations}

任何能夠訪問內部介面上 UPnP 服務的用戶端都可以在無需身份驗證的情況下建立埠對映，而且不僅限於為其自身地址建立：對映中的內部地址可以是任意地址，甚至可以與內部介面處於不同子網。請僅在用戶端可信的介面上啟用 UPnP。

:::warning
僅當網路確實需要時，才將 `allow-disable-external-interface` 設定為 `yes`：這樣任何本地用戶端都能在無需身份驗證的情況下停用路由器的外部介面，並且其埠對映會被移除。
:::

不使用時請保持 UPnP 服務處於停用狀態，如[保護路由器安全](../getting-started/securing-your-router.md)中所述。

## 配置示例 {#configuration-example}

![Network diagram: the router connects to the Internet on ether1 (10.0.0.1/24) and to a LAN switch on ether2 (192.168.88.1/24); two computers, PC1 (192.168.88.10/24) and PC2 (192.168.88.11/24), are on the 192.168.88.0/24 LAN](/img/a8f12d6db929635a.webp)

啟用該服務，並把面向 Internet 的介面標記為 external、把面向用戶端的介面標記為 internal：

```ros
/ip/upnp/set enabled=yes
/ip/upnp/interfaces/add interface=ether1 type=external
/ip/upnp/interfaces/add interface=ether2 type=internal
```

當 LAN 上的用戶端（例如位於 192.168.88.10 的 PC1）請求 TCP 和 UDP 埠 55000 的對映時，路由器會建立動態目標 NAT 規則：

```ros
[admin@MikroTik] /ip/firewall/nat> print where dynamic
Flags: D - DYNAMIC
0 D ;;; upnp 192.168.88.10: ApplicationX
    chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=55000
    protocol=tcp dst-address=10.0.0.1 in-interface=ether1 dst-port=55000

1 D ;;; upnp 192.168.88.10: ApplicationX
    chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=55000
    protocol=udp dst-address=10.0.0.1 in-interface=ether1 dst-port=55000
```

規則註釋會記錄請求該對映的用戶端地址及其傳送的描述。這些規則會一直保留，直到用戶端移除對映或重新配置 UPnP 服務。用戶端也可以請求對映到與其自身不同的內部地址；此時 `to-addresses` 會儲存該地址。

如果外部介面有多個地址，請在介面條目上設定 `forced-ip`，以選擇用於對映並向用戶端報告的是哪個地址。

:::warning
在包含 VLAN 的環境中，請將 VLAN 介面本身指定為內部介面：用戶端流量（包括 UPnP 發現）會到達該介面。
:::

## 技術細節 {#technical-details}

### 發現與服務埠 {#discovery-and-service-ports}

該服務會從每個內部介面向組播組 `239.255.255.250` 的 UDP 埠 1900 傳送 SSDP 通告，用戶端也會在該埠傳送發現請求。裝置描述透過 `http://<internal interface address>:2828/gateway.xml` 提供，用戶端透過同一個 TCP 埠 2828 控制路由器。控制服務僅監聽內部介面的地址。

在服務啟用期間，這兩個埠都會作為動態條目顯示在 `/ip/service` 中。

### 埠對映 {#port-mappings}

- 每個對映都會為每種協定建立一條動態 `dstnat` 規則。用戶端使用 `AddPortMapping` 動作請求對映，並使用 `DeletePortMapping` 移除對映。
- 僅支援永久對映：帶有有限租期的請求會被拒絕，並返回錯誤 `725 OnlyPermanentLeasesSupported`。
- 使用 `NewEnabled=0` 請求的對映會以停用狀態建立規則。
- 更改 `/ip/upnp` 或介面列表中的任何設定都會重啟服務並移除所有動態埠對映；用戶端必須重新請求其對映。
- 預設情況下，當用戶端列舉對映時，該服務會將一個非活動的佔位對映作為第一條記錄報告，以規避某些用戶端應用程式在沒有對映時出現異常行為的問題。可透過 `show-dummy-rule=no` 停用此行為。
- 每個外部介面都會作為獨立的 WAN 連線裝置進行通告，因此多個外部介面可以同時提供對映服務。

有關所有屬性，請參閱 CLI 參考中的 [`/ip/upnp`](../cli-reference/ip/upnp/index.md) 和 [`/ip/upnp/interfaces`](../cli-reference/ip/upnp/interfaces.md)。
