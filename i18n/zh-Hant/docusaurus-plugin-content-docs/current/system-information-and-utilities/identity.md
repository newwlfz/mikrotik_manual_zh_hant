---
sidebar_key: "system-information-and-utilities/identity"
sidebar_position: 6
title: "身份"
sidebar_label: "身份"
description: "`system identity`（系統標識）是路由器的名稱，它顯示在 CLI 提示符中、鄰居發現中，並作為 SNMP 系統名稱和 DHCP 用戶端主機名使用。可在 CLI 中、WinBox 中或透過 SNMP 進行設定。"
tags:
  - 'system-identity'
  - 'snmp'
  - 'configuration'
source: https://manual.mikrotik.com/docs/system-information-and-utilities/identity
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

系統身份是路由器的名稱。預設值為 `MikroTik`。請為每臺路由器指定各自的名稱，以便區分它們。該身份會出現在多個位置，包括：

- 在命令列提示符中，例如 `[admin@Riga-Office-GW] >`，以及 WinBox 連線的標題中。
- 在[鄰居發現](./neighbor-discovery.md)中：相鄰裝置會以路由器的身份列出它，並在下一次通告時更新，預設每 30 秒更新一次。
- 作為 SNMP 系統名稱（`sysName`）。
- 作為 [DHCP 用戶端](../network-management/dhcp/client.md)預設傳送給 DHCP 伺服器的主機名。
- 作為舊版 `wireless` 軟體包（[legacy wireless](../wireless/abgn/wireless-interface.md)）介面的預設 SSID。
- 在指令碼中，作為 `[/system/identity/get name]`。

身份名稱最長可達 64 個字元。更長的名稱會被拒絕，並提示 `could not change identity: too long`。允許使用空格和其他字元，但需要加引號，例如 `name="Riga Office GW"`；由於 DHCP 主機名和 DNS 名稱不允許空格，由字母、數字和連字元組成的名稱可在所有場景中正常工作。

## 設定身份 {#set-the-identity}

當您管理多臺路由器時，一個能說明路由器位置和用途的名稱會很有幫助，例如 `Riga-Office-GW`：

```ros
/system/identity/set name=Riga-Office-GW
/system/identity/print
```

```text
  name: Riga-Office-GW
```

提示符會顯示新名稱：

```text
[admin@Riga-Office-GW] >
```

## 在 WinBox 中設定身份 {#set-the-identity-in-winbox}

在 WinBox 中，開啟 **System > Identity**，在 **Identity** 欄位中輸入路由器名稱（標註 1），然後選擇 **OK**。請使用有助於將這臺路由器與其他裝置區分開的名稱，例如 `Home-Router`。該名稱也會顯示在 WinBox 的連線標題中。

![WinBox Identity dialog with a callout around the Identity field](/img/973c005b796413a2.webp)

## 透過 SNMP 設定身份 {#set-the-identity-over-snmp}

管理系統可以透過對 `sysName.0`（`1.3.6.1.2.1.1.5.0`）發起 SNMP set 請求來設定身份。這需要一個具有寫訪問許可權的 [SNMP](../diagnostics-monitoring-and-troubleshooting/snmp.md) community；預設 community `public` 只能讀取，並會以 `readOnly` 拒絕 SNMPv1 set 請求。具有寫訪問許可權的 community 還可以更改其他設定並重啟路由器，因此請給它起一個難以猜測的名稱，因為該名稱會充當密碼，並將其限制為管理系統的地址：

```ros
/snmp/community/add name=netadmin-7Qx2 addresses=192.168.88.10/32 \
    write-access=yes
/snmp/set enabled=yes
```

在管理系統中，例如在 Linux 或 macOS 上使用 `snmpset`：

```bash
snmpset -v 1 -c netadmin-7Qx2 192.168.88.1 1.3.6.1.2.1.1.5.0 s Branch-GW
```

```text
SNMPv2-MIB::sysName.0 = STRING: Branch-GW
```

SNMPv1 和 SNMPv2c 以明文傳送 community 名稱。只允許來自可信地址的寫訪問，或使用帶身份驗證和加密的 SNMPv3。除非您也限制其地址，否則 `public` community 仍可從任意地址讀取。

有關該引數，請參閱 [`/system/identity` CLI 參考](../cli-reference/system/identity.md)。
