---
title: "文件更新 - 2026年10月2日"
date: 2026-10-02
slug: /changelog-2026-10-02
source: https://manual.mikrotik.com/changelog/changelog-2026-10-02
captured_at: '2026-11-04T06:08:56+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 10 月 2 日文件變更摘要。

## 診斷與監控 {#diagnostics--monitoring}

- **[Log](/docs/diagnostics-monitoring-and-troubleshooting/log)**：已重寫，並在 RouterOS 7.25 上針對 syslog、TLS 和 SMTP 伺服器進行了測試。兩個屬性表已移至 CLI Reference。更正內容：條目始終顯示完整日期，disk-lines-per-file 預設為 1000，TCP 和 TLS 可與所有格式配合使用，critical 條目會在下次登入時列印一次，而不是每次登入都列印。新增章節：

- 閱讀日誌：按 topic、message 和時間過濾，僅跟隨（follow-only），使用 with-extra-info 獲取額外欄位，儲存到檔案，以及查明是誰修改了配置。
- 將某個功能的偵錯訊息記錄到其獨立的記憶體緩衝區，並警告 SSH 偵錯訊息包含會話金鑰和會話內容。
- 使用 disk 動作在重啟後保留日誌：檔案輪轉、位於其他磁碟上的資料夾，以及讀取較舊的檔案。
- 將日誌傳送到 syslog 伺服器：default、syslog（RFC 3164）和 cef 格式，UDP、TCP 和 TLS，TCP 緩衝區，為什麼在 TCP 和 TLS 上使用 CEF，以及使用受信任 CA 的 TLS（check-certificate 不檢查證書名稱）。
- 透過電子郵件傳送日誌訊息，以及在收到日誌訊息時執行指令碼（示例會把登入失敗的來源地址收集到 address list 中）。
- 規則如何匹配條目（列出的所有 topic 都必須匹配、!、regex、prefix）、topic 列表、故障排查，以及每種遠端格式的線上格式。

- **[CEF 與 Elasticsearch](/docs/diagnostics-monitoring-and-troubleshooting/log/cef-with-elasticsearch)**、**[Syslog 與 Elasticsearch](/docs/diagnostics-monitoring-and-troubleshooting/log/syslog-with-elasticsearch)**：修復了指向重寫後的 Log 頁面的連結，並對 RouterOS 命令進行了換行。CEF 指南不再重複新增相同的規則。Kibana 和 JSON 程式碼塊不再標記為 RouterOS 程式碼。
- **[頻寬測試](/docs/diagnostics-monitoring-and-troubleshooting/bandwidth-test)**：已重寫，並在 hAP ax²、CCR2116 和一臺 64 核伺服器之間進行了測試。屬性表已移至 CLI Reference。新增章節：

- 前提條件：伺服器、兩臺路由器上的 device 模式、具有 test 和 winbox 策略的測試使用者、防火牆埠，以及為什麼 UDP 接收測試在 NAT 後面會失敗。
- 以固定速率測試鏈路、測量最大吞吐量、使用固定速率的 UDP 檢查鏈路的丟包情況，以及逐個測試無線方向。
- 解讀結果：UDP 統計完整的 IP 包，而 TCP 只統計資料；lost-packets 統計的是最後一秒而非總數；CPU 負載欄位。
- 透過由三臺路由器組成的鏈測試路由器的轉發能力，包括封包大小以及何時使用流量發生器。
- 使用 allowed-addresses4 和 allowed-addresses6 保護伺服器，而不是關閉身份驗證；max-sessions 統計測試數量。
- 按 status 進行故障排查，以及 Technical details 中的埠和連線。

## CLI 參考 {#cli-reference}

- **[/log](/docs/cli-reference/log)**、**[/system/logging](/docs/cli-reference/system/logging)**、**[/system/logging/action](/docs/cli-reference/system/logging/action)**、**[clear](/docs/cli-reference/system/logging/action/clear)**：描述了每個引數。預設值、範圍和行為的檢查均在路由器上完成。topics 行列出了所有 topic。email-start-tls 被描述為未使用：email 動作遵循 /tool/e-mail 的 tls 設定。
- **[/tool/bandwidth-test](/docs/cli-reference/tool/bandwidth-test)**、**[/tool/bandwidth-server](/docs/cli-reference/tool/bandwidth-server)**、**[session](/docs/cli-reference/tool/bandwidth-server/session)**：描述了每個引數和結果欄位，例如預設值、52 位元組的最小 UDP 大小、status 值，以及 max-sessions 統計的內容。
- **[/disk/btrfs/filesystem](/docs/cli-reference/disk/btrfs/filesystem)**、**[/disk/btrfs/subvolume](/docs/cli-reference/disk/btrfs/subvolume)**、**[/disk/btrfs/transfer](/docs/cli-reference/disk/btrfs/transfer)**：補充了 Btrfs 命令和引數的描述。
- **[/disk](/docs/cli-reference/disk)**：描述了 sshfs-address、sshfs-port、sshfs-user、sshfs-password、sshfs-path 和 sshfs-local-user 引數。
- **[/ip/smb](/docs/cli-reference/ip/smb)**、**[shares](/docs/cli-reference/ip/smb/shares)**、**[users](/docs/cli-reference/ip/smb/users)**：補充了 SMB 伺服器、共享和使用者的描述。
- **[/file/sync](/docs/cli-reference/file/sync)**、**[/file/rsync-daemon](/docs/cli-reference/file/rsync-daemon)**：描述了 sync 條目（mode、local-path、remote-path、user、flags）以及 rsync 守護程式。

## 儲存 {#storage}

- **[Storage package](/docs/storage)**：章節索引現在使用該軟體包的當前名稱 Storage package（在 /system/package/print 中為 rose-storage）來稱呼它，而不再使用 ROSE。
- **[Btrfs](/docs/storage/btrfs)**、**[Btrfs RAID](/docs/storage/btrfs/raid)**、**[Btrfs 維護](/docs/storage/btrfs/maintenance)**、**[Btrfs 快照](/docs/storage/btrfs/snapshots)**：已重做。概述了三個 Btrfs 選單、預設的 &lt;disk&gt;-fs 檔案系統標籤，以及在轉換為 RAID1 時 add-device 和 balance 的作用。RAID 命令現在透過 devs 而不是 present-devs 來查詢檔案系統。已移除版本說明。
- **[SSHFS](/docs/storage/sshfs)**：新頁面。使用 /disk/add type=sshfs 把 SSH 伺服器上的資料夾掛載為磁碟，包括掛載狀態以及如何更改或移除掛載。
- **[SMB](/docs/storage/smb)**：伺服器、共享和使用者屬性表已移至 CLI Reference。頁面說明了新增第一個共享時伺服器會自動啟動。
- **[RAID](/docs/storage/raid)**、**[熱備盤](/docs/storage/raid/hot-spare)**、**[移動陣列](/docs/storage/raid/moving-array)**：RAID 屬性表已移至 CLI Reference，示例已成為頂級章節，熱備盤頁面說明了備用盤的配置方式。
- **[加密儲存](/docs/storage/encrypted-storage)**、**[自加密硬碟](/docs/storage/self-encrypting-drives)**：重寫了簡介和示例，並移除了屬性表。RAID1 陣列上的加密儲存。自加密硬碟需要直接連線符合 Opal 規範的硬碟（不透過 USB 橋接器），並解釋了 o 和 O 標誌。
- **[iSCSI](/docs/storage/iscsi)**、**[NFS](/docs/storage/nfs)**、**[NVMe over TCP](/docs/storage/nvme-over-tcp)**、**[Rsync](/docs/storage/rsync)**：移除了屬性表，並改進了簡介和示例：預設埠（iSCSI TCP 3260、NFS TCP 2049、NVMe over TCP 4420）、預設 iSCSI IQN，以及埠被阻止時 NFS 的狀態。

## 硬體 {#hardware}

- **[PoE-Out](/docs/hardware/poe-out)**：添加了 poe-out-status 的 no_valid_psu、lldp-power-off、low-voltage-pd-detected 和 power-limiting 值。
