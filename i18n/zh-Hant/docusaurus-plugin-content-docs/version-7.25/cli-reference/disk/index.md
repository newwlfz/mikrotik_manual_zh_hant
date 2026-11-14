---
sidebar_key: "cli-reference/disk/index"
sidebar_position: 7
title: "disk"
sidebar_label: 'disk'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/disk
captured_at: '2026-11-01T21:22:06+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk {#disk}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該裝置已停用且未被使用。</ArgTableRow>
<ArgTableRow arg="A" typ="acquired">acquired</ArgTableRow>
<ArgTableRow arg="E" typ="empty">該插槽為空，沒有磁碟。執行 `eject` 後，插槽會保持為空，直到用 `scan` 重新掃描磁碟或重新插拔磁碟。</ArgTableRow>
<ArgTableRow arg="B" typ="block-device">該裝置是塊裝置，也就是說，它可以作為儲存使用：可格式化或用於 RAID 陣列。沒有此標誌的裝置僅描述磁碟佈局。</ArgTableRow>
<ArgTableRow arg="M" typ="mounted">該裝置已掛載，其檔案會顯示在 `/file` 中。</ArgTableRow>
<ArgTableRow arg="F" typ="formatting">該裝置當前正在格式化。</ArgTableRow>
<ArgTableRow arg="S" typ="swap-enabled">該裝置已啟用交換空間（`swap=yes`）；該裝置被用作交換空間，例如供容器使用。</ArgTableRow>
<ArgTableRow arg="f" typ="raid-member-failed">RAID 陣列的某個成員處於故障狀態。</ArgTableRow>
<ArgTableRow arg="r" typ="raid-member">該裝置是 RAID 陣列的成員。</ArgTableRow>
<ArgTableRow arg="c" typ="encrypted">該裝置已加密，例如使用 `type=crypted`（dm-crypt）。</ArgTableRow>
<ArgTableRow arg="g" typ="guid-partition-table">該裝置具有 GUID 分割區表（GPT）。</ArgTableRow>
<ArgTableRow arg="p" typ="partition">該裝置是磁碟的一個分割區。</ArgTableRow>
<ArgTableRow arg="t" typ="nvme-tcp-export">該裝置作為 NVMe-over-TCP 目標匯出。</ArgTableRow>
<ArgTableRow arg="i" typ="iscsi-export">該裝置作為 iSCSI 目標匯出。</ArgTableRow>
<ArgTableRow arg="s" typ="smb-sharing">該裝置透過內建 SMB 伺服器共享。</ArgTableRow>
<ArgTableRow arg="n" typ="nfs-sharing">該裝置透過 NFS 伺服器共享。</ArgTableRow>
<ArgTableRow arg="m" typ="media-sharing">該裝置透過 DLNA 媒體伺服器共享。</ArgTableRow>
<ArgTableRow arg="L" typ="self-encrypted-and-locked">self-encrypted-and-locked</ArgTableRow>
<ArgTableRow arg="O" typ="self-encryption-enabled">該驅動器上的 TCG-Opal 自加密已啟用。</ArgTableRow>
<ArgTableRow arg="o" typ="self-encryption-supported">該驅動器支援 TCG-Opal 自加密，但未啟用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="type" typ="enum (raid | nvme-tcp | iscsi | nfs | smb | partition | tmpfs | ramdisk | crypted | sshfs | file | hardware)" mandatory="1">
專案型別：
- `hardware` - 連線到路由器的物理磁碟，例如位於 USB、SATA 或 NVMe 插槽中的磁碟。
- `partition` - 硬體磁碟上的分割區（參見 `parent`）。
- `file` - 作為塊裝置掛載的檔案（loop），例如 swap 檔案或掛載的 `.iso` / `.squashfs` 映象。
- `tmpfs` - RAM 中的資料夾，參見 [臨時檔案系統（Tmpfs）](../../storage/tmpfs.md)。
- `ramdisk` - 用作塊裝置的 RAM 部分，參見 [記憶體盤](../../storage/ramdisk.md)（storage 軟體包）。
- `raid` - 由多個磁碟組成的 RAID 陣列，參見 [RAID](../../storage/raid/index.md)（storage 軟體包）。
- `crypted` - dm-crypt 加密塊裝置，參見 [加密儲存（dm-crypt）](../../storage/encrypted-storage.md)（storage 軟體包）。
- `nvme-tcp` - 透過 NVMe over TCP 掛載的磁碟，參見 [NVMe over TCP](../../storage/nvme-over-tcp.md)（storage 軟體包）。
- `iscsi` - 作為磁碟掛載的 iSCSI 目標，參見 [iSCSI](../../storage/iscsi.md)（storage 軟體包）。
- `nfs` - 作為磁碟掛載的 NFS 共享，參見 [NFS](../../storage/nfs.md)（storage 軟體包）。
- `smb` - 作為磁碟掛載的 SMB 共享，參見 [SMB](../../storage/smb.md)（storage 軟體包）。
- `sshfs` - 透過 SSH 掛載的遠端資料夾。
</ArgTableRow>
<ArgTableRow arg="slot" typ="string">磁碟專案的名稱，通常基於裝置物理連線的位置，例如 `nvme1` 或 `usb1`。該名稱會自動分配，也可以手動設定。其他命令和 `parent` 透過此名稱引用該磁碟。</ArgTableRow>
<ArgTableRow arg="parent" typ="enum ()">專案的父裝置。在 `type=partition` 專案上，它選擇要在其上建立分割區的硬體磁碟，例如 `add type=partition parent=nvme9 ...`；在 `type=crypted` 上，它是被加密的驅動器或分割區。</ArgTableRow>
<ArgTableRow arg="mount-point-template" typ="string">
掛載點的模板，即檔案系統在 `/file` 中顯示所在的資料夾。以下變數會被替換：
- `[slot]`（預設）- 插槽名稱。
- `[model]` - 裝置型號。
- `[serial]` - 裝置序列號。
- `[fw-version]` - 裝置韌體版本。
- `[fs-label]` - 檔案系統標籤。
- `[fs-uuid]` - 檔案系統 UUID。
- `[fs]` - 檔案系統型別。
變數可以組合使用，例如 `[model]-[fs]`。空模板會被拒絕，`unset mount-point-template` 會恢復預設值 `[slot]`。新新增磁碟的預設值由 [`settings`](./settings.md) 中的 `default-mount-point-template` 設定。參見 [磁碟](../../hardware/disks/index.md)。
</ArgTableRow>
<ArgTableRow arg="mount-filesystem" typ="bool">裝置的檔案系統是否已掛載，從而其檔案可在 `/file` 中訪問。`mount-filesystem=no` 會解除安裝檔案系統，在執行 `/disk check` 或 `/disk repair` 之前必須這樣做。預設值：yes。</ArgTableRow>
<ArgTableRow arg="mount-read-only" typ="bool">掛載的檔案系統是否為只讀。預設值：no。</ArgTableRow>
<ArgTableRow arg="compress" typ="bool">裝置的檔案系統是否以壓縮方式掛載。僅 `btrfs` 檔案系統支援；在其他檔案系統上設定時，RouterOS 會報告 `compression only available for btrfs`。預設值：no。</ArgTableRow>
<ArgTableRow arg="partition-number" typ="num">父磁碟上分割區的編號，例如 `partition-number=1` 表示第一個分割區。</ArgTableRow>
<ArgTableRow arg="partition-offset" typ="num">分割區在磁碟上的起始偏移量，以位元組為單位。可用它調整分割區的起始位置。</ArgTableRow>
<ArgTableRow arg="partition-size" typ="num">分割區大小，以位元組為單位。未設定時，分割區佔用磁碟上的剩餘空間。參見 [磁碟](../../hardware/disks/index.md)。</ArgTableRow>
<ArgTableRow arg="raid-type" typ="enum (0 | 1 | 4 | 5 | 6 | linear) { 0:0, 1:1, 4:4, 5:5, 6:6 }" syscap="storage">
陣列的 RAID 級別：
- `0` - 條帶化：資料均勻分佈到所有磁碟，無容錯能力，效能最佳。
- `1` - 映象：相同資料寫入所有磁碟，容錯能力最佳。
- `4` - 帶專用奇偶校驗盤的塊級條帶化。
- `5` - 帶分散式奇偶校驗的塊級條帶化，可承受一塊磁碟故障。
- `6` - 帶雙奇偶校驗的塊級條帶化，可承受兩塊磁碟故障。
- `linear` - 磁碟合併為一個大磁碟，無冗餘。
參見 [RAID](../../storage/raid/index.md)。
</ArgTableRow>
<ArgTableRow arg="raid-device-count" typ="num" syscap="storage">RAID 陣列中的裝置（磁碟）數量，在建立陣列時設定。</ArgTableRow>
<ArgTableRow arg="raid-max-component-size" typ="num" syscap="storage">RAID 陣列中單個裝置的最大大小。</ArgTableRow>
<ArgTableRow arg="raid-chunk-size" typ="enum (64K | 128K | 256K | 512K | 1M | 2M | 4M) { 64K:64, 128K:128, 256K:256, 512K:512, 1M:1024, 2M:2048, 4M:4096 }" syscap="storage">跨陣列磁碟寫入的塊（條帶）大小，例如 `1M`。</ArgTableRow>
<ArgTableRow arg="raid-master" typ="enum (none)" syscap="storage">磁碟所屬的 RAID 塊裝置。與成員磁碟上的 `raid-role` 一起設定，可將它們新增到用 `add type=raid ...` 建立的陣列。在 RAID 專案本身上為 `none`。</ArgTableRow>
<ArgTableRow arg="raid-role" typ="num" syscap="storage">磁碟在 RAID 陣列中的位置，用 `raid-master` 設定，從 0 開始，或使用 `spare` 將磁碟標記為熱備盤。</ArgTableRow>
<ArgTableRow arg="raid-member-failed" typ="bool" syscap="storage">在 RAID 陣列中將驅動器標記為故障。用於需要替換未故障驅動器時。</ArgTableRow>
<ArgTableRow arg="nvme-tcp-export" typ="bool" syscap="storage">裝置是否匯出為 NVMe-over-TCP 目標，以便其他裝置可以掛載它。預設值：no。參見 [NVMe over TCP](../../storage/nvme-over-tcp.md)。</ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-port" typ="num" syscap="storage">NVMe-over-TCP 伺服器接受發起方連線的埠。參見 [NVMe over TCP](../../storage/nvme-over-tcp.md)。</ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-nqn" typ="string" syscap="storage">匯出裝置的 NVMe Qualified Name (NQN)，發起方使用它進行連線。參見 [NVMe over TCP](../../storage/nvme-over-tcp.md)。</ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-allow-host-name" typ="string" syscap="storage">允許連線到 NVMe-over-TCP 伺服器的主機名，用於基於主機的訪問控制。參見 [NVMe over TCP](../../storage/nvme-over-tcp.md)。</ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-password" typ="string" syscap="storage">NVMe-over-TCP 伺服器要求發起方提供的密碼。參見 [NVMe over TCP](../../storage/nvme-over-tcp.md)。</ArgTableRow>
<ArgTableRow arg="nvme-tcp-address" typ="ipAddr" syscap="storage">在 `nvme-tcp` 用戶端上，要掛載的 NVMe-over-TCP 目標（主機）的 IP 地址。參見 [NVMe over TCP](../../storage/nvme-over-tcp.md)。</ArgTableRow>
<ArgTableRow arg="nvme-tcp-nqn" typ="string" syscap="storage">在 `nvme-tcp` 用戶端上，伺服器上要掛載的目標的 NVMe Qualified Name (NQN)。參見 [NVMe over TCP](../../storage/nvme-over-tcp.md)。</ArgTableRow>
<ArgTableRow arg="nvme-tcp-host-name" typ="string" syscap="storage">`nvme-tcp` 發起方（用戶端）用於標識自身的主機名；用於在伺服器上進行標識和認證。參見 [NVMe over TCP](../../storage/nvme-over-tcp.md)。</ArgTableRow>
<ArgTableRow arg="nvme-tcp-password" typ="string" syscap="storage">用於向伺服器認證 NVMe-over-TCP 連線的密碼。參見 [NVMe over TCP](../../storage/nvme-over-tcp.md)。</ArgTableRow>
<ArgTableRow arg="nvme-tcp-port" typ="num" syscap="storage">NVMe-over-TCP 目標監聽發起方連線的埠。預設值：4420。參見 [NVMe over TCP](../../storage/nvme-over-tcp.md)。</ArgTableRow>
<ArgTableRow arg="iscsi-export" typ="bool" syscap="storage">裝置是否匯出為 iSCSI 目標。預設值：no。參見 [iSCSI](../../storage/iscsi.md)。</ArgTableRow>
<ArgTableRow arg="iscsi-server-port" typ="num" syscap="storage">iSCSI 伺服器監聽的埠。參見 [iSCSI](../../storage/iscsi.md)。</ArgTableRow>
<ArgTableRow arg="iscsi-server-iqn" typ="string" syscap="storage">iSCSI 伺服器的 iSCSI Qualified Name (IQN)，預設值為 `iqn.2000-02.com.mikrotik:<slot>`。參見 [iSCSI](../../storage/iscsi.md)。</ArgTableRow>
<ArgTableRow arg="iscsi-port" typ="num" syscap="storage">iSCSI 目標監聽發起方連線的埠。預設值：3260。參見 [iSCSI](../../storage/iscsi.md)。</ArgTableRow>
<ArgTableRow arg="iscsi-address" typ="ipAddr" syscap="storage">在 `iscsi` 用戶端上，要掛載的 iSCSI 目標（主機）的 IP 地址。參見 [iSCSI](../../storage/iscsi.md)。</ArgTableRow>
<ArgTableRow arg="iscsi-iqn" typ="string" syscap="storage">在 `iscsi` 用戶端上，要掛載的目標的 iSCSI Qualified Name (IQN)。參見 [iSCSI](../../storage/iscsi.md)。</ArgTableRow>
<ArgTableRow arg="nfs-sharing" typ="bool" syscap="storage">裝置是否透過 NFS 共享，以便網路用戶端可以掛載它。預設值：no。參見 [NFS](../../storage/nfs.md)。</ArgTableRow>
<ArgTableRow arg="nfs-address" typ="ipAddr" syscap="storage">在 `nfs` 用戶端上，要掛載的 NFS 伺服器的 IP 地址。參見 [NFS](../../storage/nfs.md)。</ArgTableRow>
<ArgTableRow arg="nfs-share" typ="string" syscap="storage">在 `nfs` 用戶端上，要在 NFS 伺服器上掛載的資料夾。參見 [NFS](../../storage/nfs.md)。</ArgTableRow>
<ArgTableRow arg="smb-sharing" typ="bool">裝置掛載後是否透過內建 SMB 伺服器（`/ip/smb`）共享。當 [`settings`](./settings.md) 中的 `auto-smb-sharing=yes` 時，它會自動啟用。預設值：no。</ArgTableRow>
<ArgTableRow arg="smb-server-user" typ="enum ()">此磁碟自動建立共享的 SMB 使用者；新磁碟的預設值取自 [`settings`](./settings.md) 中的 `auto-smb-user`。</ArgTableRow>
<ArgTableRow arg="smb-server-password" typ="string">自動建立共享的 SMB 使用者的密碼。</ArgTableRow>
<ArgTableRow arg="smb-server-encryption" typ="bool">到此磁碟 SMB 共享的連線是否必須加密。</ArgTableRow>
<ArgTableRow arg="smb-address" typ="ipAddr">在 `smb` 用戶端上，要掛載的 SMB 伺服器的 IP 地址。參見 [SMB](../../storage/smb.md)。</ArgTableRow>
<ArgTableRow arg="smb-share" typ="string">在 `smb` 用戶端上，要在伺服器上掛載的共享名稱。參見 [SMB](../../storage/smb.md)。</ArgTableRow>
<ArgTableRow arg="smb-user" typ="string">在 `smb` 用戶端上，用於認證的 SMB 使用者。參見 [SMB](../../storage/smb.md)。</ArgTableRow>
<ArgTableRow arg="smb-password" typ="string">在 `smb` 用戶端上，SMB 使用者的密碼。</ArgTableRow>
<ArgTableRow arg="smb-encryption" typ="bool">在 `smb` 用戶端上，到遠端 SMB 共享的連線是否加密。</ArgTableRow>
<ArgTableRow arg="media-sharing" typ="bool">裝置掛載後是否透過 DLNA 媒體伺服器（`/ip/media`）共享。當 [`settings`](./settings.md) 中的 `auto-media-sharing=yes` 時，它會自動啟用。預設值：no。</ArgTableRow>
<ArgTableRow arg="media-interface" typ="iface_enum { none }">DLNA 媒體伺服器用於此磁碟共享的介面，與 `media-sharing=yes` 一起設定。</ArgTableRow>
<ArgTableRow arg="tmpfs-max-size" typ="num">`tmpfs` 資料夾的最大大小，使用十進位制單位（`100M` 為 100 000 000 位元組）。該資料夾僅為其中儲存的檔案佔用 RAM。未設定大小（讀取為 `0`）時，資料夾可增長到約一半 RAM。RouterOS 會累加所有 tmpfs 資料夾的最大大小，未設定 `tmpfs-max-size` 的資料夾按一半 RAM 計算；當總計超過路由器可提供的容量（`too much memory requested for tmpfs/ramdisk`）時，會拒絕新的大小。`print` 中的大小會向上取整到完整的 4 KiB 記憶體頁。新值立即生效，對已掛載的資料夾也是如此。`tmpfs` 的內容在重啟或斷電後丟失。參見 [臨時檔案系統（Tmpfs）](../../storage/tmpfs.md)。預設值：未設定。</ArgTableRow>
<ArgTableRow arg="ramdisk-size" typ="num" syscap="storage">使用 `type=ramdisk` 建立的 RAM 塊裝置大小，向上取整到 16 KiB 的倍數。新增 ramdisk 時不會預留 RAM。重啟或斷電會清除它：ramdisk 仍然存在，但為空且沒有檔案系統，因此需要重新格式化。需要 `rose-storage` 軟體包。參見 [記憶體盤](../../storage/ramdisk.md)。</ArgTableRow>
<ArgTableRow arg="crypted-backend" typ="enum (none)" syscap="storage">使用 `type=crypted` 加密的驅動器或分割區。參見 [加密儲存（dm-crypt）](../../storage/encrypted-storage.md)。</ArgTableRow>
<ArgTableRow arg="encryption-key" typ="string" syscap="storage">用於解密 `crypted` 裝置的金鑰。參見 [加密儲存（dm-crypt）](../../storage/encrypted-storage.md)。</ArgTableRow>
<ArgTableRow arg="self-encryption-password" typ="string" syscap="storage">在受支援（SED）驅動器上啟用 TCG-Opal 自加密的密碼；取消設定會停用自加密。參見 [自加密硬碟（SED）](../../storage/self-encrypting-drives.md)。</ArgTableRow>
<ArgTableRow arg="sshfs-address" typ="string">對於 `type=sshfs`，要掛載的 SSH 伺服器的地址（IP 地址或主機名）。參見 [SSHFS](../../storage/sshfs.md)。</ArgTableRow>
<ArgTableRow arg="sshfs-port" typ="num">對於 `type=sshfs`，要連線的 SSH 伺服器埠（預設值：22）。參見 [SSHFS](../../storage/sshfs.md)。</ArgTableRow>
<ArgTableRow arg="sshfs-user" typ="string">對於 `type=sshfs`，用於登入遠端 SSH 伺服器的使用者。參見 [SSHFS](../../storage/sshfs.md)。</ArgTableRow>
<ArgTableRow arg="sshfs-password" typ="string">對於 `type=sshfs`，遠端 SSH 使用者的密碼。參見 [SSHFS](../../storage/sshfs.md)。</ArgTableRow>
<ArgTableRow arg="sshfs-path" typ="string">對於 `type=sshfs`，遠端 SSH 伺服器上要掛載的路徑。參見 [SSHFS](../../storage/sshfs.md)。</ArgTableRow>
<ArgTableRow arg="swap" typ="bool">將裝置用作交換空間。交換空間僅由容器使用，其可用大小限制為裝置 RAM 的 10 倍。它適用於整個磁碟或分割區，或使用 `type=file` 的檔案。參見 [磁碟](../../hardware/disks/index.md)。</ArgTableRow>
<ArgTableRow arg="file-path" typ="file">使用 `type=file` 作為塊裝置掛載的檔案的路徑和名稱，例如交換檔案（`swap=yes`）或掛載的 `.iso` / `.squashfs` 映象。刪除磁碟專案不會刪除該檔案。參見 [磁碟](../../hardware/disks/index.md)。</ArgTableRow>
<ArgTableRow arg="file-size" typ="num">建立 `type=file` 裝置時檔案的大小，例如 `file-size=1G`。</ArgTableRow>
<ArgTableRow arg="file-offset" typ="num">塊裝置在檔案中開始的偏移量，例如 `file-offset=0`。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="slot-default" typ="string">裝置的預設插槽名稱，在未設定自定義 `slot` 名稱時顯示。</ArgTableRow>
<ArgTableRow arg="fs-label" typ="string">檔案系統的標籤。格式化時會自動將其設定為 `<slot>-fs`，除非向 `/disk format` 提供了 `label`。</ArgTableRow>
<ArgTableRow arg="fs-uuid" typ="string">檔案系統的 UUID，例如 `58470fe2-...`。</ArgTableRow>
<ArgTableRow arg="fs" typ="enum (fat32 | ext4 | btrfs | xfs | nfs | smb | wipe | wipe-quick | tmpfs | exfat | ntfs | sshfs | squashfs | iso | discard | discard-secure | -)">裝置的檔案系統：本地檔案系統為 `ext4`、`btrfs`、`xfs`、`fat32`、`exfat` 和 `ntfs`，RAM 資料夾為 `tmpfs`，網路掛載為 `nfs`、`smb` 和 `sshfs`，掛載的映象為 `iso` / `squashfs`。`-` 表示裝置沒有可識別的檔案系統。值 `wipe`、`wipe-quick`、`discard` 和 `discard-secure` 對應於 `/disk format` 的檔案系統。</ArgTableRow>
<ArgTableRow arg="model" typ="string">裝置的型號名稱，例如 `TS1TUTE210T`。</ArgTableRow>
<ArgTableRow arg="serial" typ="string">裝置的序列號。</ArgTableRow>
<ArgTableRow arg="fw-version" typ="string">裝置的韌體版本。</ArgTableRow>
<ArgTableRow arg="size" typ="num">裝置的總大小，以位元組為單位。</ArgTableRow>
<ArgTableRow arg="free" typ="num">已掛載檔案系統上的可用空間，以位元組為單位。</ArgTableRow>
<ArgTableRow arg="total-inodes" typ="num">檔案系統的 inode 總數。</ArgTableRow>
<ArgTableRow arg="free-inodes" typ="num">檔案系統的可用 inode 數。</ArgTableRow>
<ArgTableRow arg="use" typ="num">檔案系統的已用空間百分比，例如 `4%`。</ArgTableRow>
<ArgTableRow arg="mount-point" typ="string">檔案系統的掛載點，即它在 `/file` 中顯示所在的資料夾，由 `mount-point-template` 決定。</ArgTableRow>
<ArgTableRow arg="sector-size" typ="num">裝置的扇區大小，例如 512 位元組。</ArgTableRow>
<ArgTableRow arg="interface" typ="string">裝置連線到的介面，例如 `PCIe 2x8 GT/s` 或 `USB 2.00 480Mbps`。</ArgTableRow>
<ArgTableRow arg="interface-speed" typ="num">裝置連線到的介面速度，例如 `15.7Gbps`。</ArgTableRow>
<ArgTableRow arg="raid-member-state" typ="string" syscap="storage">磁碟作為其 RAID 陣列成員的狀態，例如 `0:in_sync`；當磁碟不屬於已組裝陣列時，則改為顯示在其上找到的 RAID 超級塊詳細資訊。</ArgTableRow>
<ArgTableRow arg="state" typ="string">RAID 陣列的狀態，例如 `clean`。</ArgTableRow>
<ArgTableRow arg="last-seen" typ="string">最後佔用此插槽的磁碟的型號和序列號，在磁碟被彈出或移除後顯示，例如 `TS1TUTE210T J398770033`。</ArgTableRow>
<ArgTableRow arg="raid-uuid" typ="string" syscap="storage">RAID 陣列的 UUID。</ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-secret" typ="string" syscap="storage">NVMe-over-TCP 伺服器用於認證來自發起方連線的金鑰。</ArgTableRow>
<ArgTableRow arg="nvme-tcp-secret" typ="string" syscap="storage">用於認證到 NVMe-over-TCP 伺服器連線的金鑰。</ArgTableRow>
<ArgTableRow arg="sshfs-local-user" typ="string">SSHFS 掛載執行所依據的本地 RouterOS 使用者，例如 `admin`。只讀。</ArgTableRow>
<ArgTableRow arg="io-ops" typ="num">裝置上的 I/O 操作總數，如 [`monitor-traffic`](./monitor-traffic.md) 所示。</ArgTableRow>
<ArgTableRow arg="io-errors" typ="num">裝置上的 I/O 錯誤總數。</ArgTableRow>
<ArgTableRow arg="read-ops" typ="num">讀操作總數。</ArgTableRow>
<ArgTableRow arg="read-ops-per-second" typ="num">每秒讀運算元。</ArgTableRow>
<ArgTableRow arg="read-bytes" typ="num">讀取的總位元組數。</ArgTableRow>
<ArgTableRow arg="read-rate" typ="num">讀取速率，例如以位元組/秒為單位。</ArgTableRow>
<ArgTableRow arg="read-merges" typ="num">合併的相鄰讀運算元。</ArgTableRow>
<ArgTableRow arg="read-time" typ="time">讀操作花費的時間。</ArgTableRow>
<ArgTableRow arg="write-ops" typ="num">寫操作總數。</ArgTableRow>
<ArgTableRow arg="write-ops-per-second" typ="num">每秒寫運算元。</ArgTableRow>
<ArgTableRow arg="write-bytes" typ="num">寫入的總位元組數。</ArgTableRow>
<ArgTableRow arg="write-rate" typ="num">寫入速率，例如以位元組/秒為單位。</ArgTableRow>
<ArgTableRow arg="write-merges" typ="num">合併的相鄰寫運算元。</ArgTableRow>
<ArgTableRow arg="write-time" typ="time">寫操作花費的時間。</ArgTableRow>
<ArgTableRow arg="in-flight-ops" typ="num">當前正在進行的 I/O 運算元。</ArgTableRow>
<ArgTableRow arg="active-time" typ="time">裝置忙於處理請求的時間。</ArgTableRow>
<ArgTableRow arg="wait-time" typ="time">請求在佇列中等待的時間。</ArgTableRow>
<ArgTableRow arg="discard-ops" typ="num">discard（trim）操作總數。</ArgTableRow>
<ArgTableRow arg="discard-bytes" typ="num">已 discard 的總位元組數。</ArgTableRow>
<ArgTableRow arg="discard-merges" typ="num">合併的相鄰 discard 運算元。</ArgTableRow>
<ArgTableRow arg="discard-time" typ="time">discard 操作花費的時間。</ArgTableRow>
<ArgTableRow arg="flush-ops" typ="num">flush 操作總數。</ArgTableRow>
<ArgTableRow arg="flush-time" typ="time">flush 操作花費的時間。</ArgTableRow>
<ArgTableRow arg="temperature" typ="num">驅動器溫度（攝氏度），由 S.M.A.R.T. 報告（storage 軟體包）。參見 [S.M.A.R.T. 資訊](../../hardware/disks/smart.md) 指南和 [`smart-info`](./smart-info.md)。</ArgTableRow>
<ArgTableRow arg="temperatures" typ="multi { array-id, slot: num
 }">驅動器感測器的溫度（攝氏度），每個感測器插槽一項。</ArgTableRow>
<ArgTableRow arg="critical-warning" typ="ubit (spare-space, temperature, reliability-degraded, read-only, volatile-backup-failed)">驅動器報告的嚴重警告位掩碼：`spare-space`（可用備用空間低於 `available-spare-threshold`）、`temperature`（溫度超出範圍）、`reliability-degraded`、`read-only`（裝置進入只讀模式）和 `volatile-backup-failed`。</ArgTableRow>
<ArgTableRow arg="available-spare" typ="num">驅動器的剩餘備用塊百分比，例如 100%。低於 `available-spare-threshold` 時，驅動器會報告警告。</ArgTableRow>
<ArgTableRow arg="available-spare-threshold" typ="num">以百分比表示的閾值，低於該值時驅動器的可用備用空間會被報告為警告。</ArgTableRow>
<ArgTableRow arg="percentage-used" typ="num">根據已消耗的備用塊數量估算的驅動器壽命已使用百分比。</ArgTableRow>
<ArgTableRow arg="host-read-bytes" typ="num">主機從驅動器讀取的總位元組數。</ArgTableRow>
<ArgTableRow arg="host-write-bytes" typ="num">主機寫入驅動器的總位元組數。</ArgTableRow>
<ArgTableRow arg="host-read-cmds" typ="num">主機發送給驅動器的讀命令總數。</ArgTableRow>
<ArgTableRow arg="host-write-cmds" typ="num">主機發送給驅動器的寫命令總數。</ArgTableRow>
<ArgTableRow arg="controller-busy-time" typ="time">驅動器控制器忙於處理命令的總時間。</ArgTableRow>
<ArgTableRow arg="power-cycles" typ="num">驅動器的通電次數。</ArgTableRow>
<ArgTableRow arg="power-on-time" typ="time">驅動器的總通電時間。</ArgTableRow>
<ArgTableRow arg="unsafe-shutdowns" typ="num">驅動器的非安全（意外）關機次數。</ArgTableRow>
<ArgTableRow arg="unrecovered-integrity-errors" typ="num">驅動器的未恢復介質和資料完整性錯誤數。</ArgTableRow>
<ArgTableRow arg="warning-temperature" typ="num">驅動器開始報告警告的溫度（攝氏度）。</ArgTableRow>
<ArgTableRow arg="warning-temperature-time" typ="time">驅動器處於 `warning-temperature` 以上的時間。</ArgTableRow>
<ArgTableRow arg="critical-temperature" typ="num">驅動器報告嚴重狀態的溫度（攝氏度）。</ArgTableRow>
<ArgTableRow arg="critical-temperature-time" typ="time">驅動器處於 `critical-temperature` 以上的時間。</ArgTableRow>
</ArgTable>
