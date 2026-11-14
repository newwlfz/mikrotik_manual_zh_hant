---
sidebar_key: "getting-started/configuration-management/list-of-menus-with-sensitive-parameters"
sidebar_position: 4
title: "帶敏感引數的選單列表"
sidebar_label: "帶敏感引數的選單列表"
description: "本頁列出了 RouterOS 中用於配置密碼、金鑰和機密等敏感引數的各選單，並提供了每個選單的詳細文件連結。"
tags:
  - 'sensitive'
  - 'passwords'
  - 'secrets'
source: https://manual.mikrotik.com/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

敏感引數——密碼、金鑰和機密——除非使用 [`show-sensitive`](./index.md#configuration-export) 標誌，否則不會包含在 `export` 和 `print` 輸出中。啟用 "Hide password" 選項時，WinBox 會隱藏它們。唯一的例外是 `user` 密碼：它們以雜湊形式儲存，且永遠不會被匯出，即使使用 `show-sensitive` 也不會。

下表列出了可配置敏感引數的選單、引數名稱，以及指向選單文件的連結。

| 選單 | 引數名稱 | 頁面連結 |
| :-- | :-- | :-- |
| `/container` | password | [Container#Container 配置](../../containers/index.md) |
| `/ip/hotspot` | mac-auth-password, password, otp-secret | [HotSpot - 強制門戶#HotSpot 使用者](../../authentication-authorization-accounting/hotspot-captive-portal/index.md) |
| `/iot` | password, key | password - [MQTT#代理](../../internet-of-things/mqtt/index.md)<br/> key - [Lora#伺服器](../../internet-of-things/lora/general-properties.md#servers) |
| <code>/interface/gre</code><br/><code>/interface/gre6</code> | ipsec-secret | [GRE#屬性](../../virtual-private-networks/gre.md) |
| <code>/interface/ipip</code><br/><code>/interface/ipipv6</code> | ipsec-secret | [IPIP#屬性](../../virtual-private-networks/ipip.md) |
| <code>/interface/eoip</code><br/><code>/interface/eoipv6</code> | ipsec-secret | [EoIP#屬性描述](../../virtual-private-networks/eoip.md) |
| `/interface/6to4` | ipsec-secret | [6to4#6to4-屬性描述](../../virtual-private-networks/6to4.md) |
| `/interface/ppp-client` | password, pin | 進行中 [PPP](../../mobile-networking/ppp.md) |
| `/interface/sstp-client` | password | [SSTP#屬性](../../virtual-private-networks/sstp.md) |
| <code>/interface/l2tp-server</code><br/><code>/interface/l2tp-client</code><br/><code>/interface/l2tp-ether</code> | ipsec-secret, password | ipsec-secret, password - <a href="/zh-Hans/docs/7.24/virtual-private-networks/l2tp#l2tp-client">L2TP#L2TPClient</a><br/> ipsec-secret - <a href="/zh-Hans/docs/7.24/virtual-private-networks/l2tp#l2tp-server">L2TP#L2TPServer</a><br/> ipsec-secret - <a href="/zh-Hans/docs/7.24/virtual-private-networks/l2tp#l2tp-ether">L2TP#L2TPEther</a> |
| `/interface/ovpn-client` | password | [OpenVPN#OVPNClient](../../virtual-private-networks/openvpn.md) |
| `/interface/pptp-client` | password | [PPTP#PPTPClient](../../virtual-private-networks/pptp.md) |
| `/interface/pppoe-client` | password | [PPPoE#PPPoEClient](../../virtual-private-networks/pppoe/index.md) |
| `/ppp/secret` | password | [PPP AAA#UserDatabase](../../authentication-authorization-accounting/ppp-aaa.md) |
| `/ppp/l2tp-secret` | secret | 進行中 |
| <code>/ip/ssh/export-host-key</code><br/><code>/ip/ssh/import-host-key</code> | passphrase | [SSH](../../management-tools/ssh.md#server-host-key) |
| `/ip/ipsec` | auth-key, enc-key, ppk-secret, secret, password, passphrase, key | auth-key, enc-key - [IPsec InstalledSA](../../cli-reference/ip/ipsec/installed-sa/index.md)<br/> secret, password - [IPsec Identity](../../cli-reference/ip/ipsec/identity.md)<br/> ppk-secret - 進行中 [IPsec Peer](../../cli-reference/ip/ipsec/peer.md)<br/> key, passphrase - 進行中 IPsec Keys |
| `/system/ssh-exec` | password | [SSH](../../management-tools/ssh.md#run-remote-commands-from-scripts) |
| `/user` | password | [使用者](../../authentication-authorization-accounting/user.md) |
| `/disk` | nvme-tcp-server-password, nvme-tcp-password, smb-server-password, smb-password, self-encryption-password, encryption-key, sshfs-password | nvme-tcp-server-password, nvme-tcp-password - [NVMe over TCP](../../storage/nvme-over-tcp.md)<br/> sshfs-password - 進行中 <br/> smb-server-password, smb-password - [SMB](../../storage/smb.md)<br/> self-encryption-password, encryption-key - [自加密硬碟（SED）](../../storage/self-encrypting-drives.md) |
| `/interface/vrrp` | password | [VRRP#引數](../../high-availability-solutions/vrrp.md) |
| `/interface/dot1x` | password | [Dot1X#用戶端](../../authentication-authorization-accounting/dot1x.md) |
| `/interface/macsec` | cak | [MACsec#PropertyReference](../../bridging-and-switching/macsec.md) |
| `/interface/wireguard` | private-key, preshared-key, \**show-client-config* | [WireGuard](../../virtual-private-networks/wireguard.md) |
| `/interface/lte` | pin, password | [LTE/5G#LTEClient](../../mobile-networking/lte-5g.md#lte-client) |
| `/ip/socks/users` | password | [SOCKS](../../network-management/socks/index.md) |
| `/ip/cloud` | vpn-private-key, vpn-peer-private-key, private-key | [Back To Home（遠端回家）](../../network-management/cloud/back-to-home.md) |
| `/ip/smb` | password | [SMB#使用者設定](../../storage/smb.md) |
| `/password` | old-password, new-password, confirm-new-password | 密碼更改命令；沒有專門的文件頁面。 |
| `/radius` | secret | [RADIUS#RADIUSClient](../../authentication-authorization-accounting/radius.md) |
| `/routing` | password, tcp-md5-key, auth-key, key | password,key - <a href="/zh-Hans/docs/7.24/cli-reference/routing/rip/instance">/routing/rip</a><br/> tcp-md5-key - <a href="/zh-Hans/docs/7.24/cli-reference/routing/bgp/connection">/routing/bgp/connection</a><br/> auth-key - <a href="/zh-Hans/docs/7.24/cli-reference/routing/ospf/interface-template">/routing/ospf</a> |
| `/snmp/community` | authentication-password, encryption-password | [SNMP#CommunityProperties](../../diagnostics-monitoring-and-troubleshooting/snmp.md) |
| `/system/backup` | password | [備份](./backup.md) |
| `/system/ntp/key` | key-val | 進行中 [NTP](../../system-information-and-utilities/ntp.md) |
| `/system/swos/password` | new-password, confirm-new-password | SwOS 密碼更改命令；沒有專門的文件頁面。 |
| `/system/package/local-update` | password | [軟體包#LocalUpdate](../installation-and-upgrade/packages.md) |
| `/system/license` | password | [RouterOS 許可證金鑰#CHRLicenseLevels](../routeros-licensing/chr/chr-licensing.md#chr-license-levels) |
| `/tool/romon` | secrets | [RoMON#配置](../../management-tools/romon.md) |
| `/tool/sms` | sim-pin, secret | [SMS#接收](../../mobile-networking/sms.md) |
| `/tool/email` | password | [電子郵件](../../system-information-and-utilities/e-mail.md) |
| `/tr069-client` | connection-request-password, password | [TR-069#ConfigurationSettings](../../management-tools/tr-069.md) |
| `/user-manager` | web-private-password, paypal-password, shared-secret, password, otp-secret | shared-secret - <a href="/zh-Hans/docs/7.24/authentication-authorization-accounting/user-manager#routers">使用者管理器#路由器</a><br/> paypal-password, web-private-password - <a href="/zh-Hans/docs/7.24/authentication-authorization-accounting/user-manager#advanced">使用者管理器#高階</a><br/> password, otp-secret - <a href="/zh-Hans/docs/7.24/authentication-authorization-accounting/user-manager#users">使用者管理器#使用者</a> |
| `/interface/wifi` | passphrase, eap-password | [WiFi#SecurityProperties](../../wireless/wifi/index.md) |
| `/caps-man` | private-passphrase, passphrase | private-passphrase - <a href="/zh-Hans/docs/7.24/wireless/abgn/capsman#capsman-access-list">CAPsMAN#CAPsMANAccess-list</a><br/> passphrase - <a href="/zh-Hans/docs/7.24/wireless/abgn/capsman#capsman-configuration">CAPsMAN#CAPsMANconfiguration</a> |
| `/interface/wireless` | static-key-0, static-key-1, static-key-2, static-key-3, static-sta-private-key, management-protection-key, nv2-preshared-key, private-key, private-pre-shared-key, wpa-pre-shared-key, wpa2-pre-shared-key, mschapv2-password | static-key-0, static-key-1, static-key-2, static-key-3, static-sta-private-key - [無線介面#WEPproperties](../../wireless/index.md)<br/> management-protection-key, private-key, private-pre-shared-key - [無線介面#Properties](../../wireless/index.md)<br/> wpa-pre-shared-key, wpa2-pre-shared-key - [無線介面#WPAproperties](../../wireless/index.md)<br/> mschapv2-password - [無線介面#WPAEAPproperties](../../wireless/index.md)<br/> nv2-preshared-key - [無線介面#Generalinterfaceproperties](../../wireless/index.md) |
| `/interface/w60g` | password | [W60G#通用介面屬性](../../wireless/w60g/index.md) |
| `/zerotier` | identity | [ZeroTier#引數](../../virtual-private-networks/zerotier.md) |
| `/certificate` | export-passphrase, passphrase, challenge-password, pin, key-passphrase, challenge-passphrase | pin - 用於 card-reinstall 和 card-verify 命令，沒有專門的文件頁面。 <br/> export-passphrase - [Certificates#ExportCertificate](../../authentication-authorization-accounting/certificates.md#export-certificate)<br/> passphrase - [Certificates#ImportCertificate](../../authentication-authorization-accounting/certificates.md#import-certificate)<br/> challenge-password, key-passphrase, challenge-passphrase - 進行中 |
