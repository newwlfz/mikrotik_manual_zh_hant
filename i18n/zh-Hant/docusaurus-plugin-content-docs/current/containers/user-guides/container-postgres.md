---
sidebar_key: "containers/user-guides/container-postgres"
sidebar_position: 7
title: "容器 - Postgres"
sidebar_label: "容器 - Postgres"
description: "本指南提供在 MikroTik RouterOS 上設定 PostgreSQL 和 pgAdmin 容器的分步說明，包括建立掛載點、配置環境變數以及啟動具有持久儲存的容器。"
tags:
  - 'postgresql'
  - 'docker'
  - 'container'
source: https://manual.mikrotik.com/docs/containers/user-guides/container-postgres
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

PostgreSQL 是一個強大且廣泛使用的 SQL 資料庫引擎，是眾多應用（從小型 Web 專案到企業級系統）的骨幹。本指南將引導你完成在 RouterOS 上啟動並執行 PostgreSQL 所需的基本步驟。此外，本指南還將提供設定 pgAdmin 所需的說明——pgAdmin 是一個功能豐富的基於 Web 的介面，可讓你輕鬆管理 PostgreSQL 資料庫。

## 配置 {#configuration}

本節提供在 MikroTik RouterOS 裝置上設定 PostgreSQL 容器的分步說明。PostgreSQL 是一個強大的開源關係型資料庫系統，支援 SQL 標準，並提供事務、子查詢和使用者定義型別等高階功能。繼續操作之前，請確保你已按照 [容器網路](../index.md#networking-examples) 文件建立了容器網路。

### 步驟 1：為 PostgreSQL 容器建立掛載點 {#step-1-create-mount-point-for-postgresql-container}

在建立容器之前，你需要建立一個持久化儲存位置，PostgreSQL 將在其中儲存其資料庫檔案。這可確保即使容器被重新建立或移除，你的資料仍會保留，從而保護你寶貴的資料庫資訊。

```routeros
/container/mounts/add list=MOUNT_POSTGRES src=disk1/volumes/postgres/data dst=/var/lib/postgresql/data
```

此掛載點會將你的本地資料目錄對映到容器的 `/var/lib/postgresql/data` 路徑，PostgreSQL 將在該路徑中儲存所有資料庫檔案、事務日誌和系統目錄。

### 步驟 2：為 PostgreSQL 容器配置環境變數 {#step-2-configure-environment-variables-for-postgresql-container}

環境變數提供 PostgreSQL 在啟動時所需的配置引數。這些變數定義初始資料庫名稱、使用者憑據和資料目錄位置。

```routeros
/container/envs/add list=ENV_POSTGRES key=POSTGRES_DB value="myapp"
/container/envs/add list=ENV_POSTGRES key=POSTGRES_PASSWORD value="<changeme>"
/container/envs/add list=ENV_POSTGRES key=POSTGRES_USER value="myapp"
/container/envs/add list=ENV_POSTGRES key=PGDATA value="/var/lib/postgresql/data/pgdata"
/container/envs/add list=ENV_POSTGRES key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
```

`POSTGRES_DB` 變數指定 PostgreSQL 首次啟動時將建立的初始資料庫名稱。`POSTGRES_USER` 和 `POSTGRES_PASSWORD` 變數定義你將用於連線和管理資料庫的超級使用者賬戶憑據。`PGDATA` 變數指示 PostgreSQL 在容器記憶體儲其資料檔案的位置。`POSTGRES_INITDB_ARGS` 變數提供額外的初始化引數，將資料庫編碼設定為 UTF8，並將區域設定設定為 C，以獲得一致的行為。

### 步驟 3：建立 PostgreSQL 容器 {#step-3-create-the-postgresql-container}

現在你可以建立並配置 PostgreSQL 容器例項了。此命令從遠端登錄檔拉取官方 PostgreSQL Docker 映象，並使用前面步驟中建立的環境變數和掛載點對其進行配置。

```routeros
/container/add remote-image=postgres:15 interface=veth1 root-dir=disk1/images/postgres mountlists=MOUNT_POSTGRES envlists=ENV_POSTGRES name=postgres start-on-boot=yes logging=yes
```

:::warning

你可以透過將 `postgres:15` 值更改為任何其他可用的 PostgreSQL 版本標籤，來指定不同的 PostgreSQL 版本。

:::

### 步驟 4：啟動 PostgreSQL 容器 {#step-4-start-the-postgresql-container}

所有配置完成後，你現在可以啟動 PostgreSQL 容器了。啟動容器將啟動 PostgreSQL 資料庫伺服器，它將準備好接受來自你的應用程式的連線。

```routeros
/container/start [find where name=postgres]
```

啟動後，PostgreSQL 將根據你配置的環境變數自動建立初始資料庫和使用者。如果你已如此配置，容器將在系統啟動時自動啟動。

## 高階：PostgreSQL 與 pgAdmin {#advanced-postgresql-with-pgadmin}

本指南演示如何將 pgAdmin（用於 PostgreSQL 資料庫的流行的基於 Web 的管理工具）作為容器配置並部署到你的 MikroTik RouterOS 裝置上。pgAdmin 提供直觀的圖形介面來管理你的 PostgreSQL 資料庫伺服器，使你能夠透過 Web 瀏覽器建立資料庫、執行查詢、管理使用者並執行各種管理任務。

### 步驟 1：為 pgAdmin 容器建立掛載點目錄 {#step-1-create-mount-points-directories-for-pgadmin-container}

在建立容器之前，你需要建立持久化儲存位置，pgAdmin 將在其中儲存其配置檔案、會話資料和伺服器連線設定。這可確保即使容器重啟或更新，你的設定和連線仍保持完好。

```routeros
/container/mounts/add list=MOUNT_PGADMIN_CONFIG src=disk1/volumes/pgadmin/config dst=/config
/container/mounts/add list=MOUNT_PGADMIN_DATA src=disk1/volumes/pgadmin/data dst=/var/lib/pgadmin
```

第一個掛載點會將你的本地配置目錄對映到容器的 `/config` 路徑，pgAdmin 將在其中儲存伺服器定義和使用者偏好設定。第二個掛載點會將你的本地資料目錄對映到容器的 `/var/lib/pgadmin` 路徑，該路徑用於存放會話資訊、日誌和執行時資料。

### 步驟 2：為 pgAdmin 容器配置環境變數 {#step-2-configure-environment-variables-for-pgadmin-container}

環境變數提供 pgAdmin 在啟動時所需的配置引數。這些變數定義應用程式行為、預設憑據和網路設定。

```routeros
/container/envs/add list=ENV_PGADMIN key=PGADMIN_LISTEN_PORT value=80
/container/envs/add list=ENV_PGADMIN key=PGADMIN_DEFAULT_EMAIL value="sysadmin@domain.com"
/container/envs/add list=ENV_PGADMIN key=PGADMIN_DEFAULT_PASSWORD value="<changeme>"
/container/envs/add list=ENV_PGADMIN key=PGADMIN_SERVER_JSON_FILE value="/config/servers.json"
/container/envs/add list=ENV_PGADMIN key=PGADMIN_PREFERENCES_JSON_FILE value="/config/preferences.json"
/container/envs/add list=ENV_PGADMIN key=PGPASS_FILE value="/config/pgpass"
/container/envs/add list=ENV_PGADMIN key=PGADMIN_DISABLE_POSTFIX value="True"
```

`PGADMIN_LISTEN_PORT` 變數指定 pgAdmin 將監聽哪個埠以接受傳入的 Web 連線——預設使用埠 80 進行標準 HTTP 訪問。`PGADMIN_DEFAULT_EMAIL` 和 `PGADMIN_DEFAULT_PASSWORD` 變數定義你首次登入 pgAdmin Web 介面時將使用的初始管理員憑據。其餘變數指定容器內的檔案路徑，pgAdmin 將在這些路徑中儲存和檢索伺服器連線配置、使用者偏好設定和密碼檔案資料。

### 步驟 3：建立 pgAdmin 容器 {#step-3-create-the-pgadmin-container}

現在你可以建立並配置 pgAdmin 容器例項了。此命令從遠端登錄檔拉取官方 dpage/pgadmin4 Docker 映象，並使用前面步驟中建立的環境變數和掛載點對其進行配置。

```routeros
/container/add remote-image=dpage/pgadmin4 envlists=ENV_PGADMIN mountlists=MOUNT_PGADMIN_CONFIG,MOUNT_PGADMIN_DATA interface=veth1 logging=yes name=pgadmin root-dir=disk1/images/pgadmin start-on-boot=yes user=0:0
```

此命令指定來自 Docker Hub 的官方 pgAdmin4 Docker 映象，應用你先前定義的環境變數列表和掛載點列表，將容器分配到 `veth1` 虛擬乙太網介面，啟用日誌記錄以便故障排查，將容器命名為 "pgadmin" 以便識別，將容器映象檔案儲存在指定的磁碟位置，配置容器在路由器每次啟動時自動啟動，並以 root 使用者許可權執行容器。

### 步驟 4：停用 Webfig 服務 {#step-4-disable-the-webfig-service}

由於 pgAdmin 作為基於 Web 的應用程式執行，並且預設監聽 HTTP 埠 80，因此它會與 RouterOS 內建的 WebFig Web 介面衝突，後者也使用埠 80。為避免此埠衝突並確保 pgAdmin 正常執行，你必須停用 WebFig 服務。

```routeros
/ip/service
set www disabled=yes
```

:::tip

如果你希望保持 WebFig 可訪問，還有一種替代方法：只需修改 `PGADMIN_LISTEN_PORT` 環境變數，使用不同的埠號——例如 8080 或 8888——而不是預設埠 80。這樣兩個服務就可以同時執行而不會衝突。

:::

### 步驟 5：啟動 pgAdmin 容器 {#step-5-start-the-pgadmin-container}

所有配置完成後，你現在可以啟動 pgAdmin 容器了。啟動容器將啟動 pgAdmin Web 應用程式，它將可透過你的 Web 瀏覽器訪問。

```routeros
/container/start [find where name=pgadmin]
```

啟動後，你可以透過在 Web 瀏覽器中導航到路由器的 IP 地址來訪問 pgAdmin Web 介面。使用你在步驟 2 中配置的電子郵件地址和密碼進行身份驗證，並開始管理你的 PostgreSQL 資料庫伺服器。
