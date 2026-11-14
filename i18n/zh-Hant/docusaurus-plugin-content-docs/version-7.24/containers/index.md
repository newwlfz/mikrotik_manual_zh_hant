---
sidebar_key: "containers/index"
sidebar_position: 3
title: "容器"
sidebar_label: "容器"
description: "本頁面介紹 MikroTik RouterOS 的 container 支援，涵蓋配置、虛擬介面、儲存和安全注意事項。頁面詳細說明了 restart interval、DNS 設定、CPU 分配和記憶體限制等屬性，用於執行容器化服務，同時警告存在安全風險。"
tags:
  - 'container'
  - 'security'
source: https://manual.mikrotik.com/docs/7.24/containers
captured_at: '2026-11-04T11:27:42+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 RouterOS 的容器支援，包括容器配置、虛擬乙太網介面、儲存以及應用示例。使用這些內容可以在 RouterOS 裝置上執行受支援的容器化服務。

<DocCardList />

**所需軟體包：** `container`

容器是 MikroTik 對 Linux 容器的實現，允許使用者在 RouterOS 內執行容器化環境。容器功能可在最新的 MikroTik RouterOS v7.x 版本中工作。容器相容來自 Docker Hub、GCR、Quay 或其他提供商的映象，也相容在其他裝置上構建的映象，使用這些提供商所支援的相同格式。雖然 RouterOS 使用的語法與 Docker 不同，但它仍能實現類似的功能。

## 免責宣告 {#disclaimer}

:::danger
你需要對 RouterOS 裝置擁有物理訪問許可權才能啟用容器功能支援；該功能預設處於停用狀態；

- 一旦啟用容器功能，容器就可以被遠端新增/配置/啟動/停止/刪除！
- 如果你的 RouterOS 裝置已被入侵，攻擊者可以輕易利用容器在你的 RouterOS 裝置中以及透過網路安裝惡意軟體；
- 你的 RouterOS 裝置的安全性取決於你在容器中執行的任何內容；
- 如果你執行容器，則沒有任何形式的安全保證；
- 在 RouterOS 裝置上執行第三方容器映象可能會開啟安全漏洞/攻擊途徑/攻擊面；
- 掌握漏洞利用構建知識的專家將能夠越獄/提升至 root 許可權；

:::

### 安全風險 {#security-risks}

- 當安全專家公佈其漏洞利用研究時——任何人都能運用此類漏洞利用。
- 有人可以構建一個既能利用該漏洞又能提供 Linux root shell 的容器映象。
- 透過使用 root shell，即使容器映象被刪除且容器功能被停用，他人也可能在你的 RouterOS 系統中留下永久的後門/漏洞。
- 如果漏洞被注入到主或備用 RouterBOOT（或廠商預載入程式）中，那麼即使 Netinstall 也可能無法修復。

## 要求 {#requirements}

容器軟體包相容 **arm、arm64** 和 **x86** 架構。使用 remote-image（類似於 docker pull）功能需要主記憶體中有大量可用空間，16MB SPI 快閃記憶體的板卡可以使用 USB 或其他磁碟介質上的預構建映象。

:::danger

- 建議使用至少支援 100MB/s 順序讀寫速度和 10K 隨機 iops 的外部磁碟。使用較慢的磁碟時，容器解壓時間可能會變長。
- 需要安裝 Container 軟體包
- 對於使用 EN7562CT CPU 的裝置（如 hEX Refresh），僅支援 [arm32v5](https://hub.docker.com/u/arm32v5) 容器映象，這意味著可執行的容器數量有限。

:::

**子選單：** `/container`

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **restart-interval** (*string*; 預設: ) | 指定 Container 在發生故障時的重啟間隔。示例：10s |
| **cmd** (*string*; 預設: ) | CMD 的主要用途是為正在執行的容器提供預設值。這些預設值可以包含可執行檔案，也可以省略可執行檔案；在這種情況下，還必須指定 ENTRYPOINT 指令。 |
| **comment** (*string*; 預設: ) | 簡短描述 |
| **dns** (*string*; 預設: ) | 如果容器需要不同的 DNS，可在此處配置 |
| **domain-name** (*string*；預設值：) |  |
| **entrypoint** (*string*; 預設: ) | ENTRYPOINT 允許指定啟動容器時要執行的可執行檔案。示例：`/bin/sh` |
| **envlist** (*string*; 預設: ) | 要與容器一起使用的環境變數列表（在 *`/container/envs`* 下配置） |
| **file** (*string*; 預設: ) | 如果容器是從檔案匯入的，則為容器 \*tar.gz 壓縮包 |
| **hostname** (*string*; 預設: ) | 為容器分配主機名有助於更輕鬆地識別和管理容器 |
| **interface** (*string*; 預設: ) | 要與容器一起使用的 veth 介面 |
| **logging** (*string*; 預設: ) | 如果設定為 yes，所有由容器生成的輸出都將顯示在 RouterOS 日誌中 |
| **start-on-boot** (*string*; 預設: ) | 如果設定為 yes，容器將在裝置啟動時自動啟動。 |
| **mountlists** (*string*; 預設: ) | 要與此容器一起使用的 /container/mounts/ 子選單中的掛載 |
| **mount** (*string*; 預設: ) | 指定要用作掛載的目錄 |
| **remote-image** (*string*; 預設: ) | 如果使用外部 registry，則為要安裝的容器映象名稱（在 `/container/config/set` registry-url=... 下配置） |
| **root-dir** (*string*; 預設: ) | 用於將容器儲存儲存到主記憶體之外 |
| **stop-signal** (*string*; 預設: 15) | 定義如果容器在 10 秒後仍在執行，則傳送哪個 Linux 訊號來終止容器。不同的訊號可能允許優雅關閉、立即終止或觸發特定於應用程式的操作 |
| **workdir** (*string*; 預設: ) | cmd entrypoint 的工作目錄 |
| **devices** (*string*; 預設: ) | 將物理裝置透傳給容器 |
| **cpu-list** (*string*; 預設: ) | 指定允許容器執行在哪些 CPU 核心上 |
| **user** (*string*; 預設: ) | 設定容器程式在執行前執行所用的使用者和組。 |
| **memory-high** (*int*；預設值：) | 特定容器的 RAM 使用上限（位元組） |
| **memory-max** (*int*；預設值：) | 每個容器的最大 RAM 使用上限（位元組）（如果 memory-max 值小於容器的 memory-current，則容器程式將被終止）；從 7.23 起，該引數不能設定為低於 1MB，以避免容器在啟動過程中過早被終止 |
| **stop-time** (*string*; 預設: ) | 在傳送 stop-signal 之前，容器優雅停止的時間限制。 |
| **tmpfs** (*string*; 預設: ) | 容器的臨時檔案系統掛載點。格式：`size@dir`，例如：`64M@/tmp`。 |
| **layer-dir** (*string*; 預設: ) | 用於儲存容器映象層的目錄，用於容器之間的共享層儲存。 |
| **shm-size** (*int*; 預設: ) | 容器的 `/dev/shm` 共享記憶體檔案系統大小（以位元組為單位）。 |
| **default-dns** (*string*; 預設: ) | 從系統 `/ip/dns` 配置繼承的預設 DNS 伺服器。 |
| **hosts** (*string*; 預設: ) | 容器的自定義主機名到 IP 地址對映。格式：`host=ip`。 |
| **restart-policy** (*string*; 預設: ) | 定義容器的重啟策略：`no`（從不重啟）、`on-failure`（僅在退出碼非零時重啟）或 `always`（始終重啟）。 |
| **restart-max-count** (*int*; 預設: ) | 在 restart-interval 時間範圍內允許的最大重啟嘗試次數。 |
| **stop-on-unhealthy** (*string*; 預設: ) | 如果設定為 `yes`，當 healthcheck 狀態變為 unhealthy 時，容器將自動停止。 |

:::warning
預設情況下，容器使用 `/ip/dns` 子選單中配置的相同 DNS。如果此處未配置 DNS，且未指定容器的 `dns` 引數，則容器將無法啟動！
:::

### 選單專用命令 {#menu-specific-commands}

| 屬性 | 描述 |
| :-- | :-- |
| **update** | 更新容器映象。自動從容器倉庫拉取並解壓，替換原始映象。 |
| **kill** | 終止指定的執行中容器。 |
| **restart** | 重新啟動指定的執行中容器。 |
| **repull** | 重新拉取/解壓容器映象。 |
| **shell** | 進入執行中容器的容器 shell。 |
| **run** | 啟動容器並進入其 shell。當容器執行後即退出時很有用。 |

## 容器配置 {#container-configuration}

**子選單：** `/container/config`

| 屬性 | 描述 |
| :-- | :-- |
| **registry-url** | 將從中下載容器的外部登錄檔 URL（預設：`https://lscr.io/`） |
| **tmpdir** | 容器解壓目錄 |
| **layer-dir** | 用於儲存容器映象層的目錄，用於在容器之間共享層儲存 |
| **memory-high** | RAM 使用上限（位元組）1 - 無限制 |
| **memory-max** | 每個容器的最大 RAM 使用上限（位元組）。如果 memory-max 值小於容器的 memory-current，則容器程式將被終止 |
| **username** | 指定用於身份驗證的使用者名稱（從 ROS 7.8 開始） |
| **password** *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 指定用於身份驗證的密碼（從 ROS 7.8 開始） |

### 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **assumed-registry-url** | 自動檢測到的登錄檔 URL。 |
| **memory-current** | 所有容器當前的總記憶體使用量（位元組）。 |

## 示例 {#examples}

### 執行 Pi-hole {#running-pi-hole}

#### 前置條件 {#prerequisites}

   1. 裝有 RouterOS v7.4beta 或更高版本的 RouterOS 裝置，並且**已安裝 Container 軟體包 -** [如何安裝軟體包](../getting-started/installation-and-upgrade/packages.md)
   2. 對裝置擁有物理訪問許可權以啟用容器模式 - 將在下文說明
   3. 已連線的 HDD、SSD 或 USB 儲存驅動器 - 已格式化為 RouterOS 支援的檔案系統 - [如何格式化/管理磁碟](../hardware/disks/index.md)

#### 執行 Pi-hole 的步驟 {#steps-to-run-pi-hole}

1. 啟用容器模式，並按照命令給出的說明操作（閱讀更多關於 [裝置模式](../system-information-and-utilities/device-mode.md) 的資訊）。你需要透過按下 [reset 按鈕](../getting-started/configuration-management/routeros-configuration-reset.md)或冷重啟（如果在 x86 上使用容器）來確認 device-mode：  

   ```routeros
   /system/device-mode/update container=yes 
   ```

   :::danger
   [裝置模式](../system-information-and-utilities/device-mode.md) 預設限制容器使用，在授予容器模式訪問許可權之前 - 請確保你的裝置已完全做好安全防護。
   :::
2. 建立一個新的 veth 介面，並分配一個在你的網路中唯一的 IP 地址段：  

   ```routeros
   /interface/veth/add name=veth1 address=172.17.0.2/24 gateway=172.17.0.1
   ```

   :::info
   以下配置等同於其他容器引擎（如 Docker）中的 "bridge" 網路模式。也可以建立等同於 "host" 的配置。

   **重要：** 一個 veth 介面可供多個容器使用。你可以建立多個 veth 介面，為不同的容器建立[隔離](./index.md#isolated-containers)的網路。
   :::
3. 建立一個將用於你的容器的新 [bridge](../bridging-and-switching/index.md)，並分配與 veth 介面閘道器相同的 IP 地址：  

   ```routeros
   /interface/bridge/add name=containers
   /ip/address/add address=172.17.0.1/24 interface=containers
   ```

4. 將 veth 介面新增到新建的 bridge 中：  

   ```routeros
   /interface/bridge/port/add bridge=containers interface=veth1
   ```

5. 為出站流量建立 NAT：  

   ```routeros
   /ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.17.0.0/24
   ```

6. 為容器建立環境變數：  

   ```routeros
   /container/envs/add list=ENV_PIHOLE key=TZ value="Europe/Riga"
   /container/envs/add list=ENV_PIHOLE key=FTLCONF_webserver_api_password value="mysecurepassword"
   /container/envs/add list=ENV_PIHOLE key=DNSMASQ_USER value="root"
   ```

7. 為容器建立掛載卷：  

   ```routeros
   /container/mounts/add list=MOUNT_PIHOLE_PIHOLE src=disk1/volumes/pihole/pihole dst=/etc/pihole
   /container/mounts/add list=MOUNT_PIHOLE_DNSMASQD src=disk1/volumes/pihole/dnsmasq.d dst=/etc/dnsmasq.d
   ```

   :::warning
   `src=` 指向 RouterOS 中的位置（例如，如果你決定將配置檔案放在外部 USB 介質上，也可以使用 `src=disk1/etc_pihole`），`dst=` 指向已定義的位置（請查閱容器手冊/wiki/github 瞭解應指向何處）。如果首次使用時 `src` 目錄不存在，則會用容器在 `dst` 位置中的內容來填充它。
   :::

   :::warning
   強烈建議將任何容器卷放在連線到 RouterOS 裝置的外部磁碟上。避免將容器卷放在內建儲存上。
   :::
8. 配置使用特定的容器倉庫，例如使用 Docker.io：  

   ```routeros
   /container/config/set registry-url=https://registry-1.docker.io tmpdir=disk1/tmp
   ```

9. 新增容器：  

   ```routeros
   /container/add remote-image=pihole/pihole interface=veth1 root-dir=disk1/images/pihole mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
   ```

   :::tip
   如果你希望在 `/log/print` 中看到容器輸出，則在建立容器時新增 `logging=yes`，root-dir 應指向外部驅動器。不建議將內部儲存用於容器。

   **重要：** 獲取容器映象有多種方式，如果你需要新增容器映象的其他方式，請檢視[新增容器映象](./index.md#adding-a-container-image)章節。

   **重要：** 新增容器將開始下載或解壓它，容器本身在新增後不會啟動，你需要在首次下載/解壓完成後手動啟動它。
   :::
10. 檢查容器狀態，等待下載/解壓完成且 `status=stopped`：  

    ```routeros
    /container/print
    ```

11. 啟動容器：  

    ```routeros
    /container/start pihole
    ```

12. 為容器建立埠轉發：  

    ```ros
    /ip/firewall/nat
    add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=80 protocol=tcp to-addresses=172.17.0.2 to-ports=80
    ```

13. 你應該可以透過在瀏覽器中訪問 `http://192.168.88.1/admin/` 來開啟 Pi-hole 的 Web 面板。
14. 要在你的裝置上開始使用 Pi-hole，請將其 DNS 配置改為使用 `192.168.88.1` 作為 DNS 伺服器。

### 新增容器映象 {#adding-a-container-image}

在 RouterOS 裝置上執行容器映象有多種方式。請檢視下面的示例。

#### 選項 A：從外部庫獲取映象 {#option-a-get-an-image-from-an-external-library}

設定 registry-url（用於從 Docker 登錄檔下載容器），並將解壓目錄（tmpdir）設定為已連線的 USB 介質：

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=disk1/tmp
```

拉取映象：

```ros
/container/add remote-image=pihole/pihole interface=veth1 root-dir=disk1/images/pihole mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
```

映象將被自動拉取並解壓到 root-dir。可以使用以下命令檢查狀態

```ros
/container/print
```

#### 選項 B：從 PC 匯入映象 {#option-b-import-image-from-pc}

你可以使用執行 Docker 或 Podman 的 PC 下載所需的容器映象並將其儲存為歸檔檔案。我們推薦使用 [Podman](https://podman.io/docs/installation)，因為使用 Podman 為特定架構構建和下載容器更加容易。

1. 根據你的 RouterOS 裝置的架構下載所需的映象。  

   ```routeros
   #对于 ARM64
   podman pull --arch=arm64 docker.io/pihole/pihole

   #对于 ARM
   podman pull --arch=arm docker.io/pihole/pihole

   #对于 AMD64
   podman pull --arch=amd64 docker.io/pihole/pihole
   ```

2. 將容器映象儲存為歸檔檔案。  

   ```routeros
   podman save pihole > pihole.tar
   ```

3. 將歸檔檔案上傳到你的 RouterOS 裝置，例如：  

   ```routeros
   rsync -av pihole.tar admin@192.168.88.1:/data/disk1/
   ```

   :::tip
   你也可以使用 Winbox 上傳檔案！
   :::
4. 使用上傳的容器映象歸檔檔案在你的 RouterOS 裝置上建立容器。  

   ```routeros
   /container/add file=disk1/pihole.tar interface=veth1 root-dir=disk1/pihole mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
   ```

#### 選項 C：在 PC 上構建映象 {#option-c-build-an-image-on-pc}

你可以構建自己的容器並在 RouterOS 裝置上使用它們。雖然可以使用 Docker 構建容器，但我們推薦使用 [Podman](https://podman.io/docs/installation)，因為使用 Podman 為特定架構構建容器更加容易。

1. 獲取所需容器映象的原始檔，例如使用 git。  

   ```routeros
   git clone https://github.com/pi-hole/docker-pi-hole.git
   cd docker-pi-hole
   ```

2. 透過指定 Dockerfile 或 Containerfile 以及目標架構來構建容器映象。  

   ```routeros
   #对于 ARM64
   podman build --platform linux/arm64 --tag pihole -f ./src/Dockerfile

   #对于 ARM
   podman build --platform linux/arm --tag pihole -f ./src/Dockerfile

   #对于 AMD64
   podman build --platform linux/amd64 --tag pihole -f ./src/Dockerfile
   ```

3. 將容器映象儲存為歸檔檔案。  

   ```routeros
   podman save pihole > pihole.tar
   ```

4. 將歸檔檔案上傳到你的 RouterOS 裝置，例如。  

   ```routeros
   rsync -av pihole.tar admin@192.168.88.1:/data/disk1/
   ```

   :::tip
   你也可以使用 Winbox 上傳檔案！
   :::
5. 使用上傳的容器映象歸檔檔案在你的 RouterOS 裝置上建立容器。  

   ```routeros
   /container/add file=disk1/pihole.tar interface=veth1 root-dir=disk1/pihole mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
   ```

##### 替代方案：使用 Docker 構建容器映象 {#alternative-using-docker-to-build-container-images}

要使用 Dockerfile 並製作你自己的 docker 軟體包 - 需要安裝 docker 以及 buildx 或其他構建工具包。

安裝後檢查是否有其他架構可用：

```bash
docker buildx ls
```

應返回：

```bash
NAME/NODE DRIVER/ENDPOINT STATUS  PLATFORMS
default * docker
  default default         running linux/amd64, linux/arm64, linux/riscv64, linux/ppc64le, linux/s390x, linux/386, linux/arm/v7, linux/arm/v6
```

如果沒有 - 安裝其他架構：

```bash
docker run --privileged --rm tonistiigi/binfmt --install all
```

拉取或建立包含 Dockerfile 的專案，並構建、匯出映象（如需要可調整 --platform）：

```bash
git clone https://github.com/pi-hole/docker-pi-hole.git
cd docker-pi-hole
docker buildx build  --no-cache --platform arm64 --output=type=docker -t pihole .
docker save pihole > pihole.tar
```

將 *pihole.tar* 上傳到你的 RouterOS 裝置。

Linux 系統上的映象和物件可以被 `pruned`

從 tar 映象建立容器

```ros
/container/add file=pihole.tar interface=veth1 mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
```

### 網路配置示例 {#networking-examples}

#### 帶 NAT 的 bridge {#bridge-with-nat}

在這種網路配置中，所有容器使用同一個 veth 介面，並且彼此通訊不受任何防火牆限制，但你需要轉發埠才能允許訪問容器的埠。

例如，資料庫容器需要與 Web 應用容器通訊；Web 應用需要將埠 `80` 對外暴露，而資料庫容器不需要對外暴露任何埠。

- 網路配置：  

  ```routeros
  /interface/veth/add name=veth1 address=172.17.0.2/24 gateway=172.17.0.1
  /interface/bridge/add name=containers
  /ip/address/add address=172.17.0.1/24 interface=containers
  /interface/bridge/port/add bridge=containers interface=veth1
  /ip/firewall/nat
  add chain=srcnat action=masquerade src-address=172.17.0.0/24
  add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=80 protocol=tcp to-addresses=172.17.0.2 to-ports=80
  ```

- 資料庫容器配置：  

  ```routeros
  /container/envs/add list=ENV_POSTGRES key=POSTGRES_DB value="webapp"
  /container/envs/add list=ENV_POSTGRES key=POSTGRES_PASSWORD value="<changeme>"
  /container/envs/add list=ENV_POSTGRES key=POSTGRES_USER value="webapp"
  /container/envs/add list=ENV_POSTGRES key=PGDATA value="/var/lib/postgresql/data/pgdata"
  /container/envs/add list=ENV_POSTGRES key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
  /container/mounts/add list=MOUNT_POSTGRES src=disk1/volumes/postgres/data dst=/var/lib/postgresql/data
  /container/add remote-image=postgres:15 interface=veth1 root-dir=disk1/images/postgres mountlists=MOUNT_POSTGRES envlist=ENV_POSTGRES name=postgres start-on-boot=yes logging=yes
  ```

- Web 應用容器配置：  

  ```routeros
  /container/add remote-image=dpage/pgadmin4 interface=veth1 root-dir=disk1/images/pgadmin name=pgadmin start-on-boot=yes logging=yes
  ```

在此示例中，`pgadmin` 的埠 80 對所有人可訪問，但 `postgres` 的埠 5432 並非對所有人可訪問；它只能透過 `pgadmin` 以 `127.0.0.1` 訪問，或透過執行該容器的 RouterOS 裝置以 `172.17.0.2` 訪問。

#### 隔離容器 {#isolated-containers}

在這種網路配置中，你有多個容器，並且希望確保其中一些容器之間的通訊不受防火牆限制，而另一些則需要與其他容器隔離。例如，你可能想建立兩個資料庫容器並將它們隔離。

- 網路配置。  

  ```routeros
  /interface/veth/add name=veth1 address=172.17.0.2/24 gateway=172.17.0.1
  /interface/veth/add name=veth2 address=172.18.0.2/24 gateway=172.18.0.1
  /interface/bridge/add name=containers1
  /interface/bridge/add name=containers2
  /ip/address/add address=172.17.0.1/24 interface=containers1
  /ip/address/add address=172.18.0.1/24 interface=containers2
  /interface/bridge/port/add bridge=containers1 interface=veth1
  /interface/bridge/port/add bridge=containers2 interface=veth2
  /ip/firewall/nat
  add chain=srcnat action=masquerade src-address=172.17.0.0/24
  add chain=srcnat action=masquerade src-address=172.18.0.0/24
  add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=81 protocol=tcp to-addresses=172.17.0.2 to-ports=80
  add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=82 protocol=tcp to-addresses=172.18.0.2 to-ports=80
  ```

- 第一個和第二個資料庫容器配置。  

  ```routeros
  /container/envs/add list=ENV_POSTGRES1 key=POSTGRES_DB value="webapp1"
  /container/envs/add list=ENV_POSTGRES1 key=POSTGRES_PASSWORD value="<changeme>"
  /container/envs/add list=ENV_POSTGRES1 key=POSTGRES_USER value="webapp1"
  /container/envs/add list=ENV_POSTGRES1 key=PGDATA value="/var/lib/postgresql/data/pgdata"
  /container/envs/add list=ENV_POSTGRES1 key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
  /container/mounts/add list=MOUNT_POSTGRES1 src=disk1/volumes/postgres1/data dst=/var/lib/postgresql/data
  /container/add remote-image=postgres:15 interface=veth1 root-dir=disk1/images/postgres1 mountlists=MOUNT_POSTGRES1 envlist=ENV_POSTGRES1 name=postgres1 start-on-boot=yes logging=yes
  ```

  ```routeros
  /container/envs/add list=ENV_POSTGRES2 key=POSTGRES_DB value="webapp2"
  /container/envs/add list=ENV_POSTGRES2 key=POSTGRES_PASSWORD value="<changeme>"
  /container/envs/add list=ENV_POSTGRES2 key=POSTGRES_USER value="webapp2"
  /container/envs/add list=ENV_POSTGRES2 key=PGDATA value="/var/lib/postgresql/data/pgdata"
  /container/envs/add list=ENV_POSTGRES2 key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
  /container/mounts/add list=MOUNT_POSTGRES2 src=disk1/volumes/postgres2/data dst=/var/lib/postgresql/data
  /container/add remote-image=postgres:15 interface=veth2 root-dir=disk1/images/postgres2 mountlists=MOUNT_POSTGRES2 envlist=ENV_POSTGRES2 name=postgres2 start-on-boot=yes logging=yes
  ```

- 第一個和第二個 Web 應用容器配置。  

  ```routeros
  /container/add remote-image=dpage/pgadmin4 interface=veth1 root-dir=disk1/images/pgadmin1 name=pgadmin1 start-on-boot=yes logging=yes
  ```

  ```routeros
  /container/add remote-image=dpage/pgadmin4 interface=veth2 root-dir=disk1/images/pgadmin2 name=pgadmin2 start-on-boot=yes logging=yes
  ```

在此示例中，`pgadmin1` 可以訪問 `postgres1`，但無法訪問 `postgres2`。同樣，`pgadmin2` 可以訪問 `postgres2`，但無法訪問 `postgres1`。

#### 位於二層網路中的容器 {#container-in-layer2-network}

在這種網路配置中，你的容器與其他物理網路裝置直接連線到同一個二層網路。這種網路配置等同於其他容器引擎（如 Docker）上的 "host" 網路模式。

:::danger
在這種網路配置中，容器上的所有埠都會暴露。這被認為是不安全的，但確實會略微提升容器的網路效能。
:::

- 網路配置。  

  ```routeros
  /interface/veth/add name=veth1 address=192.168.88.2/24 gateway=192.168.88.1
  /interface/bridge/port/add bridge=bridge interface=veth1
  ```

- 如果你的 RouterOS 裝置有服務執行在同一埠上，則需要停用它們。  

  ```routeros
  /ip/service/disable [find where name=www]
  ```

- Web 應用配置。  

  ```routeros
  /container/add remote-image=dpage/pgadmin4 interface=veth1 root-dir=disk1/images/pgadmin name=pgadmin start-on-boot=yes logging=yes
  ```

在此示例中，`pgadmin` 容器不需要埠轉發，但該容器所使用的所有其他埠現在對同一二層網路中的其他人可訪問。僅當你的應用要求容器在同二層網路中擁有 IP 地址時才應使用此類配置，例如使用廣播流量進行服務發現的應用（在大多數情況下，此類需求仍可透過使用 NAT 來規避）。

### 容器的 IPv4 和 IPv6 {#ipv4-and-ipv6-for-container}

在這種網路配置中，你的容器將能夠透過 IPv4 和 IPv6 通訊。該解決方案基於[帶 NAT 的 bridge](./index.md#bridge-with-nat)網路配置。

- 網路配置。  

  ```routeros
  /ip/address
  add address=172.17.0.1/24 interface=containers
  /ip/firewall/nat
  add action=masquerade chain=srcnat src-address=172.17.0.0/24
  add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=80 protocol=tcp to-addresses=172.17.0.2 to-ports=80
  /ipv6/address
  add address=fd8d:5ad2:24:2::1 interface=containers
  /ipv6/firewall/nat
  add action=masquerade chain=srcnat src-address=fd8d:5ad2:24:2::/64
  add action=dst-nat chain=dstnat dst-address=fd8d:5ad2:24:2::1 dst-port=80 protocol=tcp to-addresses=fd8d:5ad2:24:2::2 to-ports=80
  /interface/veth
  add address=172.17.0.2/24,fd8d:5ad2:24:2::2/64 gateway=172.17.0.1 gateway6=fd8d:5ad2:24:2::1 name=veth1
  /interface/bridge/port/add bridge=containers interface=veth1
  ```

- Web 應用容器配置。

  ```routeros
  /container/add remote-image=nginx interface=veth1 root-dir=disk1/images/nginx name=nginx start-on-boot=yes logging=yes
  ```

## 健康檢查 {#healthcheck}

從 RouterOS 7.23 開始，RouterOS 中已實現健康檢查支援。
健康檢查是一種幫助驗證容器內應用是否正常執行的一種機制。

健康檢查依賴標準退出碼。用於健康檢查的命令在應用健康時應返回 0，在應用不健康時應返回非零退出碼。

在大多數情況下，對於執行 Web 介面的容器，向 localhost 傳送一個簡單的 HTTP GET 請求就足以驗證應用是否正常響應。

| 屬性 | 描述 |
| :-- | :-- |
| **healthcheck-cmd** (*string*；*預設值*：)| 用於健康檢查的命令 |
| **healthcheck-interval** (*time*；*預設值*：00:00:30)| 時間間隔，格式為 HH:MM:SS |
| **healthcheck-retries** (*int*；*預設值*：3)| 檢查失敗時 - 在容器應用被視為不健康之前的重試次數 |
| **healthcheck-start-interval** (*time*；*預設值*：00:00:05)| 啟動期間健康檢查之間的時間間隔 |
| **healthcheck-start-period** (*time*；*預設值*：00:00:00) | 為容器啟動提供時間。啟動期間內的任何失敗都不會計入重試計數器 |
| **healthcheck-status** (*string*)| 容器當前的健康狀態。顯示容器內應用的當前狀態以及探針的輸出 |
| **healthcheck-timeout** (*time*；*預設值*：00:00:30)| 如果健康檢查探測耗時超過指定時間，該檢查將被計為失敗 |

### 健康檢查示例 {#healthcheck-example}

在本示例中，我們將設定一個 HomeAssistant 容器，併為其配置一個簡單的健康檢查。

有關設定 HomeAssistant 容器的指南，請參閱我們的 [HomeAssistant 設定指南](./user-guides/container-homeassistant.md)

要設定電子郵件工具。請參閱我們的[電子郵件文件頁面](../system-information-and-utilities/e-mail.md)

1. 檢查你的容器名稱

    ```ros
    [admin@ROSE] > container print 
    Flags: S - STOPPED, R - RUNNING
    Columns: NAME, ROOT-DIR, INTERFACE, MEMORY-CURRENT, CPU-USAGE, CONTAINER-SIZE, DATA-SIZE, TAG
    #   NAME                ROOT-DIR                                        INTERFACE                MEMORY-CURRENT  CPU-USAGE  CONTAINER-SIZE  DATA-SIZE  TAG                                                                   
    1 S home-assistant  /nvme1/apps/home-assistant/home-assistant_root  veth-home-assistant                          0  2201.9MiB       471.9KiB   docker.io/homeassistant/home-assistant:latest
    ```

2. 建立容器後，我們可以透過設定健康檢查命令來為其啟用健康檢查。對於這個特定容器，我們可以增大 healthcheck-interval，並指定 start-period，因為 HomeAssistant 是一個較重的容器，在某些裝置上啟動可能較慢。

    ```ros
    /container/set home-assistant healthcheck-cmd="curl -f http://localhost:8123" healthcheck-interval="00:01:00" healthcheck-start-period="00:02:00"
    ```

    如果成功且容器已啟動 - 你應該會看到容器以 "Healthy" 狀態執行。
    此外，healthcheck-status 欄位會填充容器的當前狀態以及 curl 命令的輸出。

    ```ros
    [admin@ROSE] > container print proplist=name,healthcheck-status
    Flags: S - STOPPED, R - RUNNING, H - HEALTHY
    Columns: NAME, HEALTHCHECK-STATUS
    #   NAME                HEALTHCHECK-STATUS                                                                           
    
     H home-assistant  good, output:   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                                              Dload  Upload   Total   Spent    Left  Speed     
    ```

作為額外步驟，你可以建立一個指令碼，輪詢容器狀態，並在健康檢查失敗時向你的電子郵件傳送通知，然後新增一個排程器定期執行該指令碼。

1. 建立指令碼：

    ```ros
    /system script
    add name=unhealthy-container-alert source="
    :global lastState\
        \n:local currentState \"\"\
        \n:local msg \"\"\
        \n:foreach i in=[/container find where unhealthy] do={\
        \n:local name [/container get \$i name]\
        \n:set currentState (\$currentState . \$name . \";\")\
        \n}\
        \n:if ([:len \$currentState] = 0) do={\
        \n:set lastState \"\"\
        \n} else={\
        \n:if (\$currentState != \$lastState) do={\
        \n:set lastState \$currentState\
        \n:foreach i in=[/container find where unhealthy] do={\
        \n:local name [/container get \$i name]\
        \n:set msg (\$msg . \$name . \" is UNHEALTHY\\n\")\
        \n}\
        \n/tool e-mail send to=\"admin@example.com\" subject=\"Unhealthy container(s)\" body=\$msg\
        \n}\
        \n}"
    ```

    :::warning
    請確保將 admin@example.com 替換為你的電子郵件地址。
    :::

2. 建立排程器：

    ```ros
    /system scheduler
    add interval=2m name=container-healthcheck-alert on-event="/system/script/run unhealthy-container-alert"
    ```

## 提示和技巧 {#tips-and-tricks}

- 容器會佔用大量磁碟空間。強烈建議使用 USB/SATA、NVMe 連線的介質。對於帶 USB 埠的裝置 - 可以將 USB 轉 SATA 介面卡與 2.5 英寸硬碟配合使用 - 以獲得額外儲存和更快的檔案操作。
- 可以透過以下方式限制 RAM 使用量：

```ros
/container/config/set memory-high=200M
```

這將軟限制 RAM 使用量 - 如果 RAM 使用量超過高邊界，cgroup 中的程式將被限流並承受較大的回收壓力。

- 要在路由器重啟後啟動容器，請使用 start-on-boot 選項（從 7.6beta6 開始）：

  ```ros
  /container/print
    0 name="2e679415-2edd-4300-8fab-a779ec267058" tag="test_arm64:latest" os="linux" arch="arm" interface=veth2 
      root-dir=disk1/alpine mountlists="" dns="" logging=yes start-on-boot=yes status=running 

  /container/set 0 start-on-boot=yes
  ```

- 可以進入**執行中**容器的 shell：

  ```ros
  /container/shell 0
  ```

- 可以以秒為單位設定容器超時時間，否則它將無限期保持開啟：

  ```ros
  /container/shell 0 timeout=120
  ```

- 啟用日誌記錄以獲取容器輸出：

  ```ros
  /container/set 0 logging=yes
  ```

- 某些容器需要額外的許可權才能正常執行：  

  ```routeros
  /container/set 0 user=0:0
  ```

- 你可以以特定使用者在容器內執行命令，而無需呼叫 `/bin/sh`：  

  ```routeros
  /container/shell nextcloud user=www-data cmd="php /var/www/html/cron.php" no-sh
  ```

- 從 7.11beta5 版本開始，可以新增多個地址和 IPv6 地址：

  ```ros
  /interface/veth/add address=172.17.0.3/16,fd8d:5ad2:24:2::2/64 gateway=172.17.0.1 gateway6=fd8d:5ad2:24:2::1
  ```

- 可供容器使用的活躍 /dev/ 節點：

  ```shell
  /dev/full	/dev/null	/dev/random		/dev/tty	/dev/urandom	/dev/zero	/dev/console	/dev/net/tun	/dev/kvm	/dev/fuse
  ```

- 使用 `Devices` 引數，可以將序列終端暴露給容器。

```ros
/container/set your-container devices=serial0:""
```

:::info
要允許容器使用序列控制檯埠，你必須先在 `/system/console` 下釋放 RouterOS 使用的序列控制檯
:::
