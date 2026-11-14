---
sidebar_key: "firewall-and-quality-of-service/user-guides/bruteforce-prevention"
sidebar_position: 1
title: "SSH 暴力破解防護"
sidebar_label: "SSH 暴力破解防護"
description: "使用防火牆規則保護 RouterOS 上面向網際網路的 SSH 服務，這些規則按源地址統計新連線數，並在某個源在短時間內建立過多連線時將其阻止。內容涵蓋在暴露 SSH 之前應做哪些準備、如何將規則放入預設防火牆、豁免受信任的地址、IPv6、檢查與解除阻止，以及這些規則仍允許多少次密碼猜測。"
tags:
  - 'ssh'
  - 'bruteforce-prevention'
  - 'security'
  - 'firewall'
source: https://manual.mikrotik.com/docs/7.25/firewall-and-quality-of-service/user-guides/bruteforce-prevention
captured_at: '2026-11-04T11:15:58+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

每個公網 IP 地址都會持續收到自動化的登入嘗試。RouterOS 會延遲對每次失敗登入的應答，從而減慢猜測速度，但並不會封鎖來源地址。如果路由器上的 SSH 可從網際網路訪問，機器人就可以隨意地持續猜測密碼。

本頁的防火牆規則會統計來自每個源地址的新 SSH 連線數，並在某個源在短時間內建立過多連線時將其封鎖。在使用[預設配置](../../getting-started/configuration-management/default-configurations.md)的情況下，防火牆會丟棄來自 WAN 側的所有管理訪問，因此你不需要這些規則。

## 首先減少暴露面 {#reduce-the-exposure-first}

速率限制只能拖慢攻擊者。以下措施可以消除風險，在向網際網路開放 SSH 之前請先考慮它們：

- 透過 VPN 訪問路由器，例如 [WireGuard](../../virtual-private-networks/wireguard.md)，並在 WAN 側保持 SSH 關閉。
- 只允許來自你管理路由器所用地址的 SSH 連線，參見[保護你的路由器](../../getting-started/securing-your-router.md#opening-management-access-from-wan-advanced)。
- 使用 [SSH 金鑰](../../management-tools/ssh.md#log-in-with-a-public-key)登入，並透過 `/ip/ssh/set password-authentication=no` 關閉密碼登入。這樣密碼猜測就無從下手。在預設設定 `yes-if-no-key` 下，只有沒有金鑰的使用者才能使用密碼登入。
- 透過[埠敲門](./port-knocking.md)隱藏埠，讓 SSH 只對知道敲門序列的用戶端開放。

當 SSH 必須保持可從網際網路訪問時，或者在上述措施之上再加一層防護時，請使用本頁的規則。

## 封鎖反覆建立 SSH 連線的來源 {#block-sources-that-open-repeated-ssh-connections}

這些規則讓源地址經過三個地址列表，每建立一個新的 SSH 連線就推進一個階段，並在第四個連線時將其加入黑名單：

| 來自該源的連線 | 條件 | 結果 |
|---|---|---|
| 第一個 | 無 | 加入 `connection1`，保留 5 分鐘 |
| 第二個 | 在上一個連線後 5 分鐘內 | 加入 `connection2`，保留 15 分鐘 |
| 第三個 | 在上一個連線後 15 分鐘內 | 加入 `connection3`，保留 1 小時 |
| 第四個 | 在上一個連線後 1 小時內 | 加入 `bruteforce_blacklist`，保留 1 天，並丟棄連線 |

該示例假設使用預設配置：面向網際網路的介面位於 `WAN` 介面列表中，且 input 鏈以規則 `defconf: drop all not coming from LAN` 結尾。這些規則必須位於該規則之前，否則來自 WAN 側的連線永遠不會到達它們；`place-before` 會把每條規則放到該位置：

```ros
/ip/firewall/filter
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=22 connection-state=new \
    in-interface-list=WAN src-address-list=connection3 \
    address-list=bruteforce_blacklist address-list-timeout=1d \
    comment="SSH brute force: blacklist" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=22 connection-state=new \
    in-interface-list=WAN src-address-list=connection2 \
    address-list=connection3 address-list-timeout=1h \
    comment="SSH brute force: third connection" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=22 connection-state=new \
    in-interface-list=WAN src-address-list=connection1 \
    address-list=connection2 address-list-timeout=15m \
    comment="SSH brute force: second connection" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=22 connection-state=new \
    in-interface-list=WAN \
    address-list=connection1 address-list-timeout=5m \
    comment="SSH brute force: first connection" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=accept \
    protocol=tcp dst-port=22 in-interface-list=WAN \
    src-address-list=!bruteforce_blacklist \
    comment="SSH brute force: accept" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=drop \
    protocol=tcp dst-port=22 in-interface-list=WAN \
    comment="SSH brute force: drop blacklisted" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

規則的工作方式：

- 前四條規則只是把源地址加入某個列表；`add-src-to-address-list` 不會終止封包，因此封包會繼續走向下一條規則。這些規則按相反順序排列，因此每個連線都會把源地址推進一個階段。
- `accept` 規則會放行連線，除非源地址在黑名單中；最後一條規則則將其丟棄。如果沒有最後一條規則，被列入黑名單的連線會繼續沿鏈往下走，而在不會稍後將其丟棄的防火牆上，黑名單就什麼也攔不住。
- 這些規則統計新連線（`connection-state=new`）。已經開啟的會話會保持開啟，因為預設配置會在鏈的更早位置接受已建立的連線。
- `in-interface-list=WAN` 使這些規則不作用於來自你 LAN 的連線。
- 如果 SSH 監聽在其他埠，請修改每條規則中的 `dst-port`。
- 如果某條命令報錯 `no such item`，說明路由器上沒有帶 `defconf: drop all not coming from LAN` 註釋的規則。在沒有預設防火牆的路由器上，請省略 `place-before`，或者把這些規則放到你自己的丟棄規則之前。

:::warning
你可能會把自己封鎖。這些規則統計的是連線數，而不是失敗登入數：成功登入也會被計入，而且成功登入不會把源地址從列表中移除。當指令碼或備份工具再多建立一個連線時，一個 SSH 會話、一次用 `scp` 的檔案複製再加第二個會話就足以觸發封鎖，而該地址隨後會被封鎖一天。請按下一節的說明，把你管理路由器所用的地址排除在外。
:::

### 豁免可信地址 {#exempt-trusted-addresses}

在計數規則之前接受來自可信地址的 SSH。列表名 `secured` 是[埠敲門](./port-knocking.md)示例中用於正確完成敲門的用戶端的列表名，因此當它的 accept 規則位於這些規則之前時，就已經豁免了這些用戶端。請把固定地址加入同一個列表：

```ros
/ip/firewall/address-list/add list=secured address=198.51.100.7 \
    comment="Office"
/ip/firewall/filter/add chain=input action=accept \
    protocol=tcp dst-port=22 src-address-list=secured \
    comment="SSH brute force: trusted" \
    place-before=[find comment="SSH brute force: blacklist"]
```

### IPv6 {#ipv6}

這些規則適用於 IPv4。當 SSH 可透過 IPv6 訪問時，請把相同的規則加入 `/ipv6/firewall/filter`，放在丟棄來自 LAN 外部的 IPv6 輸入的規則之前。

## 檢查與解除封鎖 {#check-and-unblock}

列出規則正在跟蹤的源地址及其每個條目的剩餘時間，並檢視有多少封包到達了每條規則：

```ros
/ip/firewall/address-list/print where list~"^connection|^bruteforce"
/ip/firewall/filter/print stats where comment~"SSH brute force"
```

失敗登入會以 `login failure for user <name> from <address> via ssh` 的形式出現在日誌中：

```ros
/log/print where message~"login failure"
```

被封鎖的地址會一直保持封鎖，直到它一天內都沒有嘗試連線：來自黑名單源的新連線嘗試會續期其條目。要解除對某個地址的封鎖，請從全部四個列表中移除其條目，例如在控制檯中或從另一個地址執行：

```ros
/ip/firewall/address-list/remove \
    [find list~"^connection|^bruteforce" address=203.0.113.10]
```

## 這些規則允許多少次猜測 {#how-many-guesses-the-rules-allow}

RouterOS SSH 伺服器在一個連線上最多接受九次密碼嘗試，然後關閉該連線。使用示例中的超時時間：

- 快速連線的源可以獲得三個連線，最多 27 次密碼猜測，然後被封鎖一天。
- 連線間隔超過 5 分鐘的源永遠不會離開第一階段，也永遠不會被封鎖：每 5 分鐘最多 9 次猜測，每天約 2,600 次猜測。

逐漸延長的超時時間正是這些規則有效的原因。如果三個列表都使用 1 分鐘超時，源就可以每分鐘建立三個連線而不被封鎖，即每分鐘最多 27 次猜測。要進一步拖慢有耐心的攻擊者，請提高 `connection1` 的超時時間：設為 30 分鐘時，限制就降到每 30 分鐘 9 次猜測。第一階段越長，你也越容易把自己封鎖。

即使有這些規則，弱密碼隨著時間推移仍可能被猜出。金鑰或長且唯一的密碼才是真正的保護。

## 相關主題 {#related-topics}

- [DDoS 防護](./ddos-protection.md)使用相同的地址列表技術配合 `dst-limit` 來檢測湧向路由器後方主機的新連線洪水。
- [埠敲門](./port-knocking.md)讓 SSH 保持關閉，直到用戶端傳送正確的連線嘗試序列。
- [連線速率](./connection-rate.md)匹配器測量單個連線的吞吐量；它不統計連線數。

有關所有規則屬性，請參見 CLI 參考中的 [`/ip/firewall/filter`](../../cli-reference/ip/firewall/filter/index.md) 和 [`/ip/firewall/address-list`](../../cli-reference/ip/firewall/address-list.md)。
