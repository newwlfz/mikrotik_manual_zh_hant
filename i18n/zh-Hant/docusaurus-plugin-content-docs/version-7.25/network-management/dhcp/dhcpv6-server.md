---
sidebar_key: "network-management/dhcp/dhcpv6-server"
sidebar_position: 5
title: "DHCPv6 伺服器"
sidebar_label: "DHCPv6 伺服器"
description: "RouterOS DHCPv6 伺服器委派 IPv6 字首（DHCPv6-PD），併為用戶端分配 IPv6 地址，支援靜態繫結、RADIUS 以及按繫結限速。"
tags:
  - 'dhcpv6'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/7.25/network-management/dhcp/dhcpv6-server
captured_at: '2026-11-04T11:21:01+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/ipv6/dhcp-server`

**標準：** RFC 8415

DHCPv6 伺服器委派 IPv6 字首（DHCPv6-PD）並向用戶端分配 IPv6 地址。它通常由向級聯路由器分發字首的路由器使用，例如向 ISP 的客戶路由器分發字首。伺服器從 `prefix-pool` 中設定的 IPv6 池獲取字首，並從 `address-pool` 中設定的 IPv6 池獲取地址，後者的字首長度必須為 128。繫結也可以是靜態的，或由 RADIUS 伺服器分配。

每個繫結由用戶端的 DUID 和 IAID 標識。當用戶端繫結到某個字首時，伺服器會透過該用戶端新增一條到該字首的動態路由（`route-distance`），以便委派字首的流量到達用戶端路由器。

大多數主機僅當其網路上的路由器通告設定了 managed 標誌時，才會使用 DHCPv6 請求地址，如下面的地址委派示例所示。RouterOS 的 DHCPv6 伺服器和用戶端使用相同的 DUID。有關 DHCPv6 的工作原理，請參閱 [DHCP 概念](./index.md)。

## 配置示例 {#configuration-example}

### 啟用 IPv6 字首委派 {#enabling-ipv6-prefix-delegation}

要啟用 IPv6 字首委派，首先建立一個 IPv6 池：

```ros
/ipv6/pool/add name=myPool prefix=2001:db8:7501::/60 prefix-length=62
```

使用 `prefix-length=62` 時，用戶端會從 /60 池中收到 /62 字首。

然後使用此池新增 DHCPv6 伺服器：

```ros
/ipv6/dhcp-server/add name=myServer prefix-pool=myPool interface=local
```

要測試伺服器，可以使用 RouterOS DHCPv6 用戶端（請參閱 [DHCPv6 用戶端](./dhcpv6-client.md)），或者像本示例中一樣，在 Linux 主機上使用 wide-dhcpv6 用戶端：

1. 安裝 wide-dhcpv6-client。
2. 配置 `/etc/wide-dhcpv6/dhcp6c.conf`，以便在 eth2 上請求字首，並從中為 eth3 分配地址：

   ```text
   interface eth2{
   send ia-pd 0;
   };

   id-assoc pd {
   prefix-interface eth3{
   sla-id 1;
   sla-len 2;
   };
   };
   ```

3. 執行用戶端：

   ```bash
   sudo dhcp6c -d -D -f eth2
   ```

4. 檢查 eth3 是否從委派字首獲得了地址：

   ```text
   mrz@bumba:/media/aaa$ ip -6 addr
   ...
   2: eth3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qlen 1000
       inet6 2001:db8:7501:1:200:ff:fe00:0/64 scope global
          valid_lft forever preferred_lft forever
       inet6 fe80::224:1dff:fe17:81f7/64 scope link
          valid_lft forever preferred_lft forever
   ```

伺服器會顯示該繫結。要讓此用戶端每次都獲得相同的字首，請將該繫結設為靜態：

```ros
[admin@MikroTik] > /ipv6/dhcp-server/binding/print
Flags: D - DYNAMIC
Columns: ADDRESS, DUID, SERVER, STATUS
#   ADDRESS             DUID                    SERVER    STATUS
0 D 2001:db8:7501::/62  0x0003000100241d1781f7  myServer  bound
[admin@MikroTik] > /ipv6/dhcp-server/binding/make-static 0
```

伺服器還會透過用戶端的鏈路本地地址新增一條到委派字首的路由：

```ros
[admin@MikroTik] > /ipv6/route/print where dst-address=2001:db8:7501::/62
Flags: D - DYNAMIC; A - ACTIVE; d - DHCP
Columns: DST-ADDRESS, GATEWAY, ROUTING-TABLE, DISTANCE
    DST-ADDRESS         GATEWAY                          ROUTING-TABLE  DISTANCE
DAd 2001:db8:7501::/62  fe80::224:1dff:fe17:81f7%local   main                  1
```

### 啟用 IPv6 地址委派 {#enabling-ipv6-address-delegation}

地址伺服器的配置與字首伺服器類似，不同之處在於它使用 `address-pool` 而不是 `prefix-pool`，並且其池必須分配 /128 字首。僅提供靜態繫結的伺服器不需要池。

```ros
[admin@MikroTik] > /ipv6/pool/print detail 
Flags: D - dynamic 
 0   name="myAddressPool" prefix=2001:db8:7501::/120 prefix-length=128 
[admin@MikroTik] > /ipv6/dhcp-server/print detail                                 
Flags: D - dynamic; X - disabled, I - invalid 
 0    name="myDHCP" interface=ether2 prefix-pool=static-only 
      address-pool=myAddressPool lease-time=3d rapid-commit=yes use-radius=no 
      preference=255 dhcp-option="" route-distance=1 use-reconfigure=no 
      address-lists="" duid="0x00030001b813f4840556" 
```

對於 DHCPv6 用戶端（例如 RouterOS DHCPv6 用戶端）來說，這就足夠了：

```ros
[admin@MikroTik] > /ipv6/dhcp-client/print detail 
Flags: D - dynamic; X - disabled, I - invalid 
 0    interface=ether2 status=bound duid="0x00030001b123f48407f0" 
      dhcp-server-v6=fe80::ba69:f4af:fe14:558 request=address 
      add-default-route=no use-peer-dns=yes allow-reconfigure=no 
      dhcp-options="" pool-name="" pool-prefix-length=64 prefix-hint=::/0 
      prefix-address-lists="" dhcp-options="" 
      address=2001:db8:7501::, 2d23h59m51s
```

計算機等主機不會自行查詢 DHCPv6 伺服器：其網路上的路由器通告會告訴它們是否使用 DHCPv6。要讓主機使用 DHCPv6 請求地址，請在介面的路由器通告中設定 managed 地址配置標誌（`managed-address-configuration`）。這不需要為 SLAAC 通告字首：

```ros
[admin@MikroTik] > /ipv6/nd/print detail 
Flags: X - disabled, I - invalid; * - default 
 0    interface=ether2 ra-interval=3m20s-10m ra-delay=3s mtu=unspecified 
      reachable-time=unspecified retransmit-interval=unspecified 
      ra-lifetime=30m ra-preference=medium hop-limit=unspecified 
      advertise-mac-address=yes advertise-dns=yes 
      managed-address-configuration=yes other-configuration=no
[admin@MikroTik] > /ipv6/nd/prefix/print detail 
Flags: X - disabled, I - invalid; D - dynamic 
 0    prefix=::/64 6to4-interface=none interface=ether2 on-link=yes 
      autonomous=yes valid-lifetime=4w2d preferred-lifetime=1w 
```

連線到 ether2 的計算機隨後會收到設定了 managed 標誌的路由器通告，在大多數主機上，這會啟動一個請求地址的 DHCPv6 用戶端。

完整的伺服器配置（含註釋）：

```ros
# 桥接网络的地址池；前缀长度必须为 128
/ipv6/pool
add name=myLocalLan prefix=2001:db8::/100 prefix-length=128
# 从地址池中分配地址的 DHCPv6 服务器
/ipv6/dhcp-server
add address-pool=myLocalLan interface=bridge name=myLocalServer
# 在路由器通告中设置 managed 标志 (M)，以便桥接上的主机使用 DHCPv6
/ipv6/nd
add interface=bridge managed-address-configuration=yes
# 在桥上启用路由器通告；不需要前缀，只需要 managed 标志
/ipv6/nd/prefix
add interface=bridge
```

:::warning
用戶端在此配置下的行為會有所不同。例如，macOS 在啟動時會獲取地址，但在休眠後如果沒有通告字首，可能不會續租，因為 macOS 在沒有 SLAAC 地址時不會使用其 DHCPv6 用戶端。其他用戶端可能需要在通告的字首上設定 `autonomous=no` 後才會使用 DHCPv6。請根據您網路中的用戶端調整配置。
:::

## 屬性 {#properties}

DHCPv6 伺服器的所有屬性都在 [`/ipv6/dhcp-server`](../../cli-reference/ipv6/dhcp-server/index.md) CLI 參考中描述。以下行為需要更多說明。

### 伺服器發起的續租 {#server-initiated-renewal}

使用 `use-reconfigure=yes` 時，接受 Reconfigure 訊息的用戶端（例如設定了 `allow-reconfigure=yes` 的 RouterOS DHCPv6 用戶端）會獲得一個 reconfigure 金鑰。當伺服器的 `address-pool`、`lease-time` 或 `dhcp-option` 發生變化，或者其繫結的設定發生變化時，伺服器會自行向它們傳送 Reconfigure 訊息，以便用戶端立即續約並採用更改。繫結的 `send-reconfigure` 命令可手動傳送一條 Reconfigure 訊息。

### 用戶端的 DNS 條目 {#dns-entries-for-clients}

使用 `add-dns-entries=yes` 時，伺服器會為每個地址繫結新增一條動態 DNS 條目（型別 AAAA）。名稱是用戶端傳送的 FQDN，後跟 `add-dns-entries-suffix`（預設為 `lan`），條目的 TTL 為租期。字首繫結不會獲得 DNS 條目。

## 繫結 {#bindings}

**子選單：** `/ipv6/dhcp-server/binding`

動態繫結與用戶端的 DUID 關聯，因此 DUID 發生變化的用戶端會獲得與之前不同的字首。靜態繫結為透過其 DUID 和 IAID 標識的用戶端提供固定的字首或地址。所有繫結屬性、狀態值和命令都在 [`/ipv6/dhcp-server/binding`](../../cli-reference/ipv6/dhcp-server/binding/index.md) CLI 參考中描述。

例如，動態分配的 /62 字首

```ros
[admin@RB493G] /ipv6/dhcp-server/binding> print detail
Flags: X - disabled, D - dynamic
 0 D address=2001:db8:7501:ff00::/62 duid="1605fcb400241d1781f7" iaid=0
     server=local-dhcp life-time=3d status=bound expires-after=2d23h40m10s
     last-seen=19m50s

 1 D address=2001:db8:7501:ff04::/62 duid="0019d1393535" iaid=2
     server=local-dhcp life-time=3d status=bound expires-after=2d23h43m47s
     last-seen=16m13s
```

### 速率限制 {#rate-limiting}

可以使用繫結的 `rate-limit` 屬性限制用戶端的頻寬。然後，伺服器會為該繫結的字首或地址新增一個動態簡單佇列。

:::warning
佇列不適用於 FastTracked 流量。請確保防火牆不會對您想要限制的流量執行 FastTrack。
:::

首先，將繫結設為靜態：

```ros
[admin@MikroTik] > /ipv6/dhcp-server/binding/print
Flags: X - disabled, D - dynamic
 #   ADDRESS                   DUID            SERVER         STATUS
 0 D fdb4:4de7:a3f8:418c::/66  0x6c3b6b7c413e  DHCPv6_Server  bound

[admin@MikroTik] > /ipv6/dhcp-server/binding/make-static 0

[admin@MikroTik] > /ipv6/dhcp-server/binding/print
Flags: X - disabled, D - dynamic
 #   ADDRESS                   DUID            SERVER         STATUS
 0   fdb4:4de7:a3f8:418c::/66  0x6c3b6b7c413e  DHCPv6_Server  bound
```

然後設定速率限制。伺服器會為該繫結建立一個動態簡單佇列：

```ros
[admin@MikroTik] > /ipv6/dhcp-server/binding/set 0 rate-limit=10M/10M
[admin@MikroTik] > /queue/simple/print
Flags: X - disabled, I - invalid, D - dynamic
 0  D name="dhcp<6c3b6b7c413e fdb4:4de7:a3f8:418c::/66>" target=fdb4:4de7:a3f8:418c::/66 parent=none packet-marks="" priority=8/8
      queue=default-small/default-small limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s
      bucket-size=0.1/0.1
```

:::note
`allow-dual-stack-queue` 預設啟用，因此同一用戶端的 DHCPv6 繫結和 DHCP 租約會共享一個動態簡單佇列。若不啟用它，伺服器會為 IPv6 和 IPv4 建立單獨的佇列。
:::

共享佇列同時包含 IPv4 和 IPv6 地址：

```ros
[admin@MikroTik] > /queue/simple/print
Flags: X - disabled, I - invalid, D - dynamic
 0  D name="dhcp-ds<6C:3B:6B:7C:41:3E>" target=192.168.1.200/32,fdb4:4de7:a3f8:418c::/66 parent=none packet-marks="" priority=8/8
      queue=default-small/default-small limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s
      bucket-size=0.1/0.1
```

## RADIUS 支援 {#radius-support}

RADIUS 伺服器可以使用 Mikrotik-Rate-Limit 屬性為每個 DHCPv6 繫結分配速率限制。首先，將 DHCPv6 伺服器設定為使用 RADIUS：

```ros
/radius 
add address=10.0.0.1 secret=VERYsecret123 service=dhcp 
/ipv6/dhcp-server 
set dhcp1 use-radius=yes
```

然後配置 RADIUS 伺服器傳送 Mikrotik-Rate-Limit 屬性。對於使用 MySQL 的 FreeRADIUS，請為用戶端的 `radcheck` 和 `radreply` 表新增條目，例如：

```sql
INSERT INTO `radcheck` (`username`, `attribute`, `op`, `value`) VALUES
('000c4200d464', 'Auth-Type', ':=', 'Accept');

INSERT INTO `radreply` (`username`, `attribute`, `op`, `value`) VALUES
('000c4200d464', 'Delegated-IPv6-Prefix', '=', 'fdb4:4de7:a3f8:418c::/66'),
('000c4200d464', 'Mikrotik-Rate-Limit', '=', '10M');
```

:::note
僅當伺服器將 DHCP 租約和 DHCPv6 繫結識別為同一用戶端時，才會建立共享佇列：透過租約的 MAC 地址識別，或者當 DHCP 用戶端傳送基於 DUID 的用戶端識別符號（RFC 4361）時透過其 DUID 識別，以及透過繫結的 DUID 識別。DHCPv6 用戶端會按裝置生成其 DUID，而不一定根據其執行所在介面的 MAC 地址生成，因此伺服器可能會改為建立單獨的佇列。
:::
