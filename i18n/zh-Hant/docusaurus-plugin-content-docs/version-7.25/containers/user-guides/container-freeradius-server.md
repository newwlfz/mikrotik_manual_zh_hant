---
sidebar_key: "containers/user-guides/container-freeradius-server"
sidebar_position: 2
title: "容器 - freeradius 伺服器"
sidebar_label: "容器 - freeradius 伺服器"
description: "本頁面介紹 MikroTik RouterOS 中的容器功能，用於在路由器內執行諸如 RADIUS 之類的伺服器，並詳細說明設定步驟，包括啟用容器模式、網路配置以及為 FreeRADIUS 伺服器部署拉取映象。"
tags:
  - 'radius'
  - 'container'
  - 'freeradius'
source: https://manual.mikrotik.com/docs/7.25/containers/user-guides/container-freeradius-server
captured_at: '2026-11-04T11:14:54+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

將容器功能引入 RouterOS 後，就可以在路由器內執行各種用於各類任務的伺服器。這對於希望減少網路中裝置數量的人尤其有用。與其在單獨的裝置/機器上執行伺服器，何不直接在路由器內執行它呢？

[Radius](../../authentication-authorization-accounting/radius.md) 是 Remote Authentication Dial-In User Service 的縮寫。RouterOS 具有 RADIUS 用戶端功能，可為 HotSpot、[PPP](../../mobile-networking/ppp.md)、[PPPoE](../../virtual-private-networks/pppoe/index.md)、[PPTP](../../virtual-private-networks/pptp.md)、[L2TP](../../virtual-private-networks/l2tp/index.md) 和 ISDN 連線進行認證。基本上，此功能允許你將 RouterOS 連線到 Radius 伺服器，然後利用該伺服器中的使用者資料庫進行用戶端認證。

在本示例中，我們將展示 **[freeradius/freeradius-server](https://hub.docker.com/r/freeradius/freeradius-server/tags)** 映象的安裝。

## 概述 {#summary}

**子選單：** `/container`

***注意**：* 需要 **container** 軟體包。

在繼續配置之前，請務必閱讀我們的 [容器](../index.md) 指南。請務必檢視[免責宣告](../index.md#disclaimer)和[要求](../index.md#requirements)部分，以瞭解所有風險以及你可能需要執行的必要步驟。

在本指南釋出時，該映象僅適用於 Linux/**amd64** 作業系統/架構（可由 CHR 和 x86 裝置使用）。對於 arm64 裝置，你需要從 [FreeRADIUS 原始碼](https://github.com/FreeRADIUS/freeradius-server) 構建自己的容器。對於 arm64 和 arm32 裝置，你也可以使用 **[freeradius/freeradius-server-dev](https://hub.docker.com/r/freeradius/freeradius-dev)** 映象，**風險自負**（因為它是該映象的“實驗/開發”版本）。

為幫助你在 [Virtual Box](https://www.virtualbox.org/) 中設定 CHR，請檢視我們的 [YouTube 教程](https://www.youtube.com/watch?v=oHXkaHkSVVo)，或[製作你自己的 x86 路由器](https://www.youtube.com/watch?v=JpccW9tYOkQ)。

:::warning
本指南演示的是一個基本示例！測試是在本地環境中執行的！本指南僅用於基本的 RADIUS “測試”目的！並非所有 "freeradius" 功能都已測試！
:::

## 配置 {#configuration}

### 容器模式 {#container-mode}

啟用容器模式：

```ros
/system/device-mode/update container=yes
```

如果在 X86 上使用容器，則需要透過冷重啟確認 device-mode。

### 網路 {#networking}

為容器新增 veth 介面：

```ros
/interface/veth/add name=veth3 address=172.17.0.2/24 gateway=172.17.0.1
```

為容器建立網橋，為其分配 IP 網路，並將 veth 新增到網橋：

```ros
/interface/bridge/add name=dockerfreeradius
/ip/address/add address=172.17.0.1/24 interface=dockerfreeradius
/interface/bridge/port/add bridge=dockerfreeradius interface=veth3
```

如有需要，為出站流量設定 NAT：

```ros
/ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.17.0.0/24
```

### 獲取映象 {#getting-image}

為簡化配置，我們將從外部映象庫獲取映象，但你也可以透過 [.tar](../index.md#option-b-import-image-from-pc) 檔案匯入它。

確保已相應設定“Registry URL”，限制 RAM 使用量（如有必要），併為映象設定一個目錄：

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=pull
```

使用以下命令拉取映象：

```ros
/container/add remote-image=freeradius/freeradius-server:latest interface=veth3 root-dir=freeradius logging=yes cmd="-X"
```

其中 `cmd="-X"` 會啟用偵錯日誌記錄（依據 "freeradius" 文件）。

執行該命令後，RouterOS 應開始“解壓”軟體包。檢查“File System”中新建的資料夾，並使用命令 `/container/print` 監控容器狀態。

### 啟動容器 {#starting-the-container}

在使用 `/container/print` 確認容器已新增且狀態變為 `status=stopped` 後，即可啟動它：

```ros
/container/start 0
```

### 修改伺服器的配置檔案 {#altering-the-servers-configuration-files}

要訪問伺服器的配置檔案（**clients.conf** 和 **authorize**），我們需要使用 SFTP（基於 SSH 的檔案傳輸）協定，因此請確保已啟用 SSH [服務](../../system-information-and-utilities/services.md)。

開啟命令終端（Windows 使用者請以管理員身份開啟“CMD”，Linux 使用者開啟“Linux Shell 或命令終端”），並導航到你要下載配置檔案的目錄。例如，導航到“桌面”上的“radius”資料夾：

```powershell
C:\WINDOWS\system32>cd C:\Users\Administrator\Desktop\radius
 
C:\Users\Administrator\Desktop\radius>
```

透過裝置的 IP 地址發起 SFTP 連線：

```powershell
C:\Users\Administrator\Desktop\radius>sftp admin@10.55.8.53
admin@10.55.8.53's password:
Connected to 10.55.8.53.
sftp>
```

轉到伺服器的配置檔案資料夾（使用 `dir` 或 `ls` 命令檢視當前所在資料夾的內容，使用 `cd` 命令轉到我們選擇的資料夾）。

第一個檔案 "clients.conf" 允許你定義 RADIUS 用戶端。根據 "freeradius" 文件，它應位於 `/etc/freeradius` 目錄下……因此，導航到該目錄並使用 `get` 命令下載它：

```powershell
sftp> dir
freeradius          pub                     pull                    skins                   
sftp> cd freeradius/etc/freeradius
sftp> dir
README.rst          certs               clients.conf        dictionary          experimental.conf   hints               
huntgroups          mods-available      mods-config         mods-enabled        panic.gdb           policy.d            
proxy.conf          radiusd.conf        sites-available     sites-enabled       templates.conf      trigger.conf        
users
sftp> get clients.conf
Fetching /freeradius/etc/freeradius/clients.conf to clients.conf
/freeradius/etc/freeradius/clients.conf                                               100% 8323     1.2MB/s   00:00
```

使用你偏好的文字編輯器（Notepad 或任何其他編輯器）開啟“**clients.conf**”。你可以研究該檔案以檢視所有可用選項（此外，請檢視 [freeradius.org](https://wiki.freeradius.org/config/Configuration-files)）。本示例展示基本設定，因此我們將直接用下面顯示的行覆蓋整個檔案：

```text
client new {
    ipaddr = 0.0.0.0/0
    secret = client_password
}
```

其中我們指明我們的 RADIUS 用戶端可以使用任意可能的 IP 地址進行連線（**ipaddr=0.0.0.0/0** 可確保這一點，但如有需要，你也可以將其改為 RADIUS 用戶端的實際 IP 地址/掩碼），並且我們的 secret 為 "client\_password"（你可以將其改為任何其他 secret）。

儲存檔案/覆蓋它。

第二個檔案 "authorize" 允許你設定使用者。根據 "freeradius" 文件，它應位於 `/etc/freeradius/mods-config/files` 下。轉到那裡並使用 `get` 獲取該檔案：

```powershell
sftp> dir
freeradius          pub                     pull                    skins                    
sftp> cd freeradius/etc/freeradius/mods-config/files
sftp> dir
accounting  authorize   dhcp        pre-proxy
sftp> get authorize
Fetching /freeradius/etc/freeradius/mods-config/files/authorize to authorize
/freeradius/etc/freeradius/mods-config/files/authorize                                100% 6594     1.1MB/s   00:00
```

使用你偏好的文字編輯器（Notepad 或任何其他編輯器）開啟“**authorize**”。本示例展示基本設定，因此我們只需取消註釋（刪除 "#" 符號）下面顯示的行（其餘配置/行保持原樣）：

```text
bob	Cleartext-Password := "hello"
```

這會建立使用者名稱 "bob" 並將密碼設定為 "hello"（你可以更改使用者名稱和密碼）。

儲存檔案/覆蓋它。

使用 `put` 命令將兩個檔案上傳回去，以覆蓋預設檔案：

```powershell
sftp> dir
freeradius          pub                     pull                    skins      
sftp> cd freeradius/etc/freeradius
sftp> dir
README.rst          certs               clients.conf        dictionary          experimental.conf   hints               
huntgroups          mods-available      mods-config         mods-enabled        panic.gdb           policy.d            
proxy.conf          radiusd.conf        sites-available     sites-enabled       templates.conf      trigger.conf        
users
sftp> put clients.conf
Uploading clients.conf to /freeradius/etc/freeradius/clients.conf
clients.conf                                                                          100%   67    22.3KB/s   00:00
sftp> cd mods-config/files
sftp> dir
accounting  authorize   dhcp        pre-proxy
sftp> put authorize
Uploading authorize to /freeradius/etc/freeradius/mods-config/files/authorize
authorize                                                                             100% 6626     1.6MB/s   00:00
```

重啟容器：

```ros
/container/stop 0
/container/start 0
```

再次啟動容器之前，請確保等待容器停止（使用 `/container/print` 命令後應顯示 `status=stopped`）。

## 結果驗證 {#result-verification}

在 RouterOS 中，新增新的 RADIUS 用戶端配置：

```ros
/radius/add service=login address=172.17.0.2 secret="client_password"
```

其中 `address` 是 veth3 介面的 IP 地址，`secret` 是我們在 **clients.conf** 檔案中配置的 secret，`service` 是你希望使用的允許服務。

透過以下命令允許 RADIUS 使用者使用 "login"：

```ros
/user/aaa/set use-radius=yes
```

我們已為 RADIUS 允許 "login" 服務，並可以使用 ssh/winbox/webfig 連線進行測試。對於 SSH 測試，請執行以下命令（其中需要指明裝置的管理 IP，並在之後輸入 bob 的密碼 "hello"）：

```ros
/system/ssh 10.55.8.53 user=bob
```

你應該能夠驗證終端使用者已從 "admin@MikroTik" 變為 "bob@MikroTik"：

```ros
[admin@MikroTik] > /system/ssh 10.55.8.53 user=bob
password:hello                                                                                                                                                                 
 

  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

  MikroTik RouterOS 7.8alpha173 (c) 1999-2023       https://www.mikrotik.com/

Press F1 for help
  
[bob@MikroTik] > 
```

如果執行命令 `/user/active/print`：

```ros
/user/active/print
Flags: R - RADIUS
Columns: WHEN, NAME, ADDRESS, VIA
#   WHEN                  NAME   ADDRESS     VIA    
0   2023-02-16 16:31:21  admin  xx.xx.xx.xx  winbox 
1   2023-02-16 16:38:46  admin  xx.xx.xx.xx  console
2 R 2023-02-16 16:38:53  bob    10.55.8.53  ssh  
```

你將能夠驗證新使用者 "bob" 處於 "active" 狀態，並被分配了標誌 "R"，這表明該使用者是 RADIUS 使用者。
