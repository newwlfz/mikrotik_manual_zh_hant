---
sidebar_key: "cli-reference/interface/veth"
sidebar_position: 35
title: "veth"
sidebar_label: 'veth'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/veth
captured_at: '2026-11-01T21:23:03+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/veth {#interfaceveth}
**條件：** !smips
**系統能力：** container
**型別：** 目錄

將容器連線到 RouterOS 的虛擬乙太網介面。veth 的一端是此 RouterOS 介面；另一端是使用它的容器的網路介面，其名稱為 veth 的名稱，MAC 地址為 `container-mac-address`。地址、閘道器和 DHCP 設定都在容器內部應用。veth 僅在使用它的容器執行時才執行。請參閱 [VETH](../../containers/veth.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用：veth 未被使用。</ArgTableRow>
<ArgTableRow arg="R" typ="running">執行中：使用該 veth 的容器正在執行。若未執行，MAC 地址會顯示為 `00:00:00:00:00:00`，並且在 veth 上配置的路由器地址無效。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">veth 的名稱。在容器內部，該介面的名稱相同。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">veth 在路由器一端的 MAC 地址。對於 `dhcp=yes` 的 veth，DHCP 伺服器看到的就是這個地址，因此為容器配置靜態租約時使用的就是它。若為空，則在容器啟動時自動設定。</ArgTableRow>
<ArgTableRow arg="container-mac-address" typ="macAddr">veth 在容器一端的 MAC 地址，即容器內部介面的地址。若為空，則在容器啟動時自動設定。</ArgTableRow>
<ArgTableRow arg="address" typ="multi { address: address (flags=46/)
 }">容器介面的 IPv4 和 IPv6 地址，多個地址以逗號分隔，例如 `172.17.0.2/24,2001:db8:17::2/64`。路由器需要在 veth 上（或 veth 作為埠的網橋上）擁有同一子網內的自身地址，才能訪問該容器。</ArgTableRow>
<ArgTableRow arg="gateway" typ="address (flags=4)">容器內部的 IPv4 預設閘道器，通常是路由器在 veth 上的地址。</ArgTableRow>
<ArgTableRow arg="gateway6" typ="address (flags=6)">容器內部的 IPv6 預設閘道器。</ArgTableRow>
<ArgTableRow arg="dhcp" typ="bool">設為 `yes` 時，RouterOS 會在 veth 上為容器執行 DHCP 用戶端，並將租約（地址和預設路由）應用到容器內部。DHCP 伺服器看到的是 veth 的 `mac-address` 以及主機名 `<identity>-<veth name>`。容器的 DNS 伺服器來自容器設定，而不是來自 DHCP。預設值：no。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="dhcp-address" typ="address (flags=46/)">當 `dhcp=yes` 時，DHCP 用戶端為容器租用到的地址。</ArgTableRow>
</ArgTable>
