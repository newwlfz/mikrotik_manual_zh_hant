---
sidebar_key: "containers/user-guides/container-matrix-synapse"
sidebar_position: 5
title: "容器 - Matrix (Synapse)"
sidebar_label: "容器 - Matrix"
description: "本頁面介紹如何在 MikroTik RouterOS 上將 Synapse Matrix 伺服器配置為容器，涵蓋容器網路配置和 PostgreSQL 環境設定等先決條件，以便在多個平臺之間實現安全的聯邦通訊。"
tags:
  - 'container'
  - 'synapse'
  - 'matrix'
source: https://manual.mikrotik.com/docs/containers/user-guides/container-matrix-synapse
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Matrix 是一種去中心化的通訊協定。每個 Matrix 伺服器獨立執行，維護自己的使用者集合，並定義自己的規則和策略。

### 託管自己的 Matrix 伺服器 {#hosting-your-own-matrix-server}

你可以使用容器直接在 RouterOS 裝置上託管自己的 Matrix 伺服器。這讓你能夠完全控制自己的通訊基礎設施。

### 聯邦 {#federation}

Matrix 伺服器可以透過聯邦連線，建立統一的通訊網路。這使不同 Matrix 伺服器上的使用者能夠安全地相互通訊，而無需中央權威機構。

### 橋接到其他平臺 {#bridging-to-other-platforms}

Matrix 支援透過橋接中繼來自其他聊天平臺的訊息，包括：

- WhatsApp
- Discord
- Signal
- Telegram
- 以及許多其他平臺

透過使用 Matrix 橋接，你可以將多個平臺的通訊整合到一個應用程式中，例如 [Element](https://element.io/)。這讓你能夠透過一個統一的介面與不同平臺的使用者通訊。

# 在 RouterOS 上設定 Synapse Matrix 伺服器 {#setting-up-a-synapse-matrix-server-on-routeros}

本指南說明如何使用容器在你的 MikroTik RouterOS 裝置上設定 Synapse，它是可用的幾種 Matrix 伺服器之一。

:::info

繼續操作之前，請確保你已經建立了容器網路。有關說明，請參閱[容器網路文件](../index.md#networking-examples)。

:::

---

## 先決條件 {#prerequisites}

- 一臺支援容器的 RouterOS 裝置
- 已配置現有容器網路
- 有足夠的儲存空間用於資料庫和 Synapse 資料

---

## 步驟 1：建立 PostgreSQL 容器環境變數 {#step-1-create-postgresql-container-environment-variables}

為 PostgreSQL 容器配置環境變數列表：

```routeros
/container/envs/add list=postgres_synapse_envs key=POSTGRES_DB value="synapse"
/container/envs/add list=postgres_synapse_envs key=POSTGRES_PASSWORD value="<POSTGRES_PASSWORD_HERE>"
/container/envs/add list=postgres_synapse_envs key=POSTGRES_USER value="synapse_user"
/container/envs/add list=postgres_synapse_envs key=PGDATA value="/var/lib/postgresql/data/pgdata"
/container/envs/add list=postgres_synapse_envs key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
/container/envs/add list=postgres_synapse_envs key=PGPORT value=5433
```

:::note

將 `<POSTGRES_PASSWORD_HERE>` 替換為你所需的 PostgreSQL 密碼。

:::

---

## 步驟 2：建立 PostgreSQL 容器掛載 {#step-2-create-postgresql-container-mount}

建立掛載點，以便在 RouterOS 裝置上持久儲存 PostgreSQL 資料：

```routeros
/container/mounts/add list=synapse_postgres_data src=disk1/synapse-postgres-data dst=/var/lib/postgresql/data
```

---

## 步驟 3：建立 PostgreSQL 容器 {#step-3-create-the-postgresql-container}

使用前面步驟中的配置啟動 PostgreSQL 容器：

```routeros
/container/add remote-image=postgres:17.2-alpine interface=veth1 root-dir=disk1/postgres-17.2-synapse mountlists=synapse_postgres_data envlists=postgres_synapse_envs name=postgresql_synapse
```

---

## 步驟 4：建立 Synapse 容器環境變數 {#step-4-create-synapse-container-environment-variables}

為 Synapse 容器配置環境變數：

```routeros
/container/envs/add list=synapse_envs key=SYNAPSE_CONFIG_DIR value="/data"
/container/envs/add list=synapse_envs key=SYNAPSE_CONFIG_PATH value="/data/homeserver.yaml"
/container/envs/add list=synapse_envs key=SYNAPSE_SERVER_NAME value="test.mt.lv"
/container/envs/add list=synapse_envs key=SYNAPSE_REPORT_STATS value="yes"
```

:::note

將 `test.mt.lv` 替換為你實際的伺服器域名。

:::

---

## 步驟 5：建立 Synapse 容器掛載 {#step-5-create-synapse-container-mount}

建立掛載點，以便在 RouterOS 裝置上持久儲存 Synapse 資料：

```routeros
/container/mounts/add list=synapse_data src=disk1/synapse-data dst=/data
```

---

## 步驟 6：生成初始 Synapse 配置 {#step-6-generate-initial-synapse-configuration}

建立並執行 Synapse 容器，以生成所需的配置檔案。該容器使用 `generate` 命令執行，以建立初始配置：

```routeros
/container/add remote-image=matrixdotorg/synapse:latest interface=veth1 cmd="generate" root-dir=disk1/synapse mountlists=synapse_data envlists=synapse_envs name=synapse
```

---

## 步驟 7：初始化配置檔案 {#step-7-initialize-configuration-files}

啟動然後停止 Synapse 容器，使其能夠生成必要的配置檔案：

```routeros
/container/start [find where name=synapse]
/container/stop [find where name=synapse]
```

---

## 步驟 8：移除 generate 命令 {#step-8-remove-the-generate-command}

清除 Synapse 容器中的命令引數，使其以正常模式執行：

```routeros
/container/set [find where name=synapse] cmd=""
```

---

## 步驟 9：配置資料庫連線 {#step-9-configure-database-connection}

使用 SFTP 用戶端（例如 Windows 上的 WinSCP）連線到你的 RouterOS 裝置，並編輯 `disk1/synapse-data/homeserver.yaml` 中生成的配置檔案。使用以下設定更新資料庫部分：

```yaml
database:
  name: psycopg2
  args:
    user: synapse_user
    password: <POSTGRES_PASSWORD_HERE>
    dbname: synapse
    host: 172.17.0.2
    port: 5433
    cp_min: 5
    cp_max: 10
    keepalives_idle: 10  # optional
    keepalives_interval: 10  # optional
    keepalives_count: 3     # optional
```

:::info

將 `<POSTGRES_PASSWORD_HERE>` 替換為你在步驟 1 中設定的密碼。

:::

---

## 步驟 10：啟動 PostgreSQL 容器 {#step-10-start-the-postgresql-container}

啟動 PostgreSQL 容器以準備資料庫：

```routeros
/container/start [find where name=postgresql_synapse]
```

---

## 步驟 11：啟動 Synapse 容器 {#step-11-start-the-synapse-container}

啟動 Synapse 容器以執行你的 Matrix 伺服器：

```routeros
/container/start [find where name=synapse]
```

---

## 步驟 12：註冊 Matrix 使用者 {#step-12-register-a-matrix-user}

進入 Synapse 容器的 shell 並註冊新使用者：

```routeros
/container/shell [find where name=synapse]
```

進入容器後，執行：

```
register_new_matrix_user -c /data/homeserver.yaml
```

按照提示建立你的管理員使用者賬戶。

---

## 步驟 13：訪問你的 Matrix 伺服器 {#step-13-access-your-matrix-server}

你的 Synapse Matrix 伺服器現在正在執行。使用你的 RouterOS 裝置的 IP 地址或域名訪問它。

---

:::warning

請始終查閱官方 Synapse 文件，以獲取最新的配置選項和最佳實踐，因為配置流程可能會隨著新版本而變化。

:::

### Discord 橋接 {#discord-bridge}

:::tip

下面的示例用於配置 Discord 橋接，但其他型別[橋接](https://matrix.org/ecosystem/bridges/)的流程非常相似。請檢視你所需[橋接](https://matrix.org/ecosystem/bridges/)的官方文件以獲取更多資訊。

:::

1. 建立 PostgreSQL Discord 橋接容器環境變數：  

   ```routeros
   /container/envs/add list=postgres_discord_envs key=POSTGRES_DB value="synapse-discord"
   /container/envs/add list=postgres_discord_envs key=POSTGRES_PASSWORD value="<POSTGRE_BRIDGE_PASSWORD_HERE>"
   /container/envs/add list=postgres_discord_envs key=POSTGRES_USER value="synapse_discord"
   /container/envs/add list=postgres_discord_envs key=PGDATA value="/var/lib/postgresql/data/pgdata"
   /container/envs/add list=postgres_discord_envs key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
    /container/envs/add list=postgres_discord_envs key=PGPORT value=5434
   ```

2. 建立 PostgreSQL Discord 橋接容器掛載：  

   ```routeros
   /container/mounts/add list=discord_postgres_data src=disk1/discord-postgres-data dst=/var/lib/postgresql/data
   ```

3. 為 Discord 橋接建立 PostgreSQL 容器：  

   ```routeros
   /container/add remote-image=postgres:17.2-alpine interface=veth1 root-dir=disk1/postgres-17.2-discord mountlists=discord_postgres_data envlists=postgres_discord_envs name=postgresql_discord
   ```

4. 按照 [容器 - HAProxy](./container-haproxy.md) 容器指南操作，併為埠 `8080` 設定反向代理
5. 建立 Discord 橋接容器掛載點：  

   ```routeros
   /container/mounts/add list=synapse_discord_data src=disk1/synapse-discord-data dst=/data
   ```

6. 建立 Discord 橋接容器：  

   ```routeros
   /container/add remote-image=litetex/mau.mautrix.discord:latest interface=veth1 root-dir=disk1/synapse-discord mountlists=synapse_discord_data name=synapse_discord
   ```

7. 啟動並停止 Discord 橋接容器以生成檔案：  

   ```routeros
   /container/start [find where name=synapse_discord]
   /container/stop [find where name=synapse_discord]
   ```

8. 使用 SFTP 用戶端（例如使用 Microsoft Windows 時的 WinSCP）連線到你的 RouterOS 裝置，並調整檔案 `disk1/synapse-discord/config.yaml`：  

   ```yaml
    homeserver
        address: http://172.17.0.2:8008
        domain: test.mt.lv
       software: standard
       async_media: true
       
   appservice
       address: leave default
       hostname: leave default
       port: leave default
       database:
           type: postgres
           uri: postgres://synapse_discord:<POSTGRE_DISCORD_PASSWORD_HERE>@172.17.0.2:5434/synapse-discord?sslmode=disable
   bridge:
       encryption:
           allow: true
       permissions:
           "*": relay
           "@your_admin_user1:test.mt.lv": admin
           "@your_admin_user2:test.mt.lv": admin
   ```

9. 再次啟動並停止 Discord 橋接容器：  

   ```routeros
   /container/start [find where name=synapse_discord]
   /container/stop [find where name=synapse_discord]
   ```

10. 下載檔案 `disk1/synapse-discord/registration.yaml`，並將其作為檔案 `disk1/synapse-data/mautrix-discord-registration.yaml` 上傳
11. 使用 SFTP 用戶端（例如使用 Microsoft Windows 時的 WinSCP）連線到你的 RouterOS 裝置，並將以下行新增到 `disk1/synapse-data/homeserver.yaml`：  

     ```yaml
     ...
     app_service_config_files:
     - /data/mautrix-discord-registration.yaml
     ```

12. 啟動 Synapse 和 Discord 橋接容器：  

     ```routeros
    /container/start [find where name=postgresql_discord]
    /container/start [find where name=synapse_discord]
    /container/start [find where name=postgresql_synapse]
    /container/start [find where name=synapse]
    ```

13. 你的 Matrix 伺服器現在應該有一個名為 "Discord bridge bot" 的新使用者。請按照官方文件建立橋接房間。
