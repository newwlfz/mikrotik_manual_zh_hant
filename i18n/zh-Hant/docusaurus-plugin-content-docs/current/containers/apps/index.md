---
sidebar_key: "containers/apps"
title: "應用"
sidebar_label: "應用"
description: "使用 RouterOS Apps 選單安裝、管理和建立容器應用，包括設定嚮導和自定義 compose YAML 檔案。"
tags:
  - 'container'
  - 'apps'
  - 'security'
source: https://manual.mikrotik.com/docs/containers/apps
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Apps 選單提供了可在 RouterOS 上執行的應用程式目錄。一個應用可以包含一個或多個容器，RouterOS 會自動建立所需的容器配置、VETH 介面、網橋埠、防火牆規則和反向代理條目。該目錄由 MikroTik 維護，映象來源包括 Docker Hub、GCR、Quay 及其他映象倉庫。你可以在啟用應用之前編輯其配置，並隨時檢視其 YAML。

[可用 Apps 列表](./available-apps.md)展示了該目錄。目錄應用和自定義應用使用相同的 YAML 格式。

## 先決條件 {#prerequisites}

- 安裝 `container` 軟體包。
- 使用 arm64、arm32 或 x86 裝置。搭載 EN7562CT CPU 的裝置（如 hEX Refresh）只能執行 arm32v5 映象，因此只有 `supported-archs` 中列出 `arm_v5` 的應用才可用。
- 使用 `/system/device-mode/update container=yes` 啟用容器模式。這需要物理接觸並按下復位按鈕確認，或在 x86 上執行冷重啟。請參閱[裝置模式](../../system-information-and-utilities/device-mode.md)。
- 將儲存磁碟格式化為 ext4、btrfs 或 xfs，並將其掛載到 `/disk`。建議使用外部儲存。配備 16 MB SPI 快閃記憶體的裝置需要外部儲存來存放容器映象。
- 為容器提供足夠的 RAM。應用的當前記憶體使用量顯示在 `/app/print detail` 的 `memory-current` 中。
- 在 `/app/settings` 中或透過[設定嚮導](#setup-wizard)配置應用磁碟、路由器 IP 地址和 LAN 網橋。
- 對於 HTTPS 應用 URL，路由器需要來自雲服務的有效應用證書。

:::warning
執行第三方容器映象會使裝置面臨與這些映象本身相同的安全風險。被攻陷的路由器也可能利用容器安裝惡意軟體。在啟用容器模式之前，請先閱讀[容器](../index.md)。
:::

## 設定嚮導 {#setup-wizard}

在終端中執行 `/app/setup`，或在 WebFig 中選擇 Setup。該向導會將各項值寫入 `/app/settings`，之後你可以隨時更改。

### 選擇應用磁碟 {#select-the-app-disk}

該向導會列出已格式化並掛載的磁碟。在執行嚮導之前，請先在 `/disk` 中將磁碟格式化為 ext4、btrfs 或 xfs。

請使用順序讀寫速度至少為 100 MB/s、隨機 IOPS 至少為 10,000 的磁碟。使用 `/disk/test` 驗證磁碟。

嚮導將媒體路徑設定為 `<disk>/media`，將下載路徑設定為 `<disk>/media/downloads`。應用映象和資料儲存在 `<disk>/apps` 下。

### 選擇 LAN 網橋 {#select-the-lan-bridge}

選擇代表你的 LAN 的網橋。具有 `network=lan` 的應用會將其 VETH 介面連線到此網橋。某些應用使用 LAN 進行自動發現。

### 設定路由器 IP {#set-the-router-ip}

選擇用戶端訪問路由器時使用的 IP 地址。應用會在生成的 URL 和埠轉發規則中使用此地址，因此請在啟用應用之前設定它。在未設定該地址的情況下啟用的應用會保持為 `status=waiting for router ip to be configured`。

### 檢視設定 {#review-the-settings}

嚮導會將所選值儲存在 `/app/settings` 中。使用以下方式檢查它們：

```routeros
/app/settings/print
```

## 安裝並執行應用 {#install-and-run-an-app}

目錄應用已存在但已停用。在 WebFig 或終端中啟用應用：

```routeros
/app/print
/app/enable <app>
```

首次啟用會拉取並解壓映象，建立網路並啟動容器。使用以下命令檢查進度：

```routeros
/app/print detail where name="<app>"
```

應用啟動期間，`status` 會顯示 `downloading/extracting` 或 `starting`。應用執行時，`status` 為空，標誌 `R` 出現，並且 `ui-url` 包含訪問 URL。

使用 `use-https=yes` 時，RouterOS 會建立反向代理規則，並使用來自 `/app/settings` 的應用證書。URL 使用雲主機名。使用 `use-https=no` 時，URL 為 `http://<router-ip>:<port>`。帶有名為 `web` 的埠的應用會獲得一個 UI URL。有關反向代理的詳細資訊，請參閱[容器應用](../../network-management/proxy/reverse-proxy.md#container-apps)。

## 管理應用 {#manage-apps}

### 標誌和狀態 {#flags-and-status}

| 標誌 | 含義 |
| :-- | :-- |
| `X` | 應用已停用。 |
| `R` | 應用正在執行。 |
| `c` | 該應用是自定義應用。 |
| `s` | 該應用來自自定義應用商店。 |

`app print` 可以根據終端寬度顯示不同的列。使用 `print detail` 或 `proplist` 讀取特定欄位。

應用執行時，`status` 為空。在啟動期間或發生故障後，它可能會顯示諸如 `waiting for router ip to be configured`、`downloading/extracting` 或 `starting` 之類的值。

### 更新、重啟和停止應用 {#update-restart-and-stop-apps}

```routeros
/app/update <app>
/app/restart <app>
/app/disable <app>
/app/enable <app>
```

`/app/update` 會再次拉取應用映象，解壓它們，並重啟應用。`/app/restart` 會停止並啟動容器，但不會拉取映象。

在應用上設定 `auto-update=yes`，可在裝置重啟後應用啟動時檢查新映象。`/app/settings` 中的全域性 `auto-update` 設定為已安裝應用提供預設值。當映象未發生變化時，RouterOS 會跳過匯入並啟動現有映象。

### 移除應用 {#remove-apps}

`/app/cleanup` 會停止應用並移除其容器、資料和網路配置。應用條目會保留，但處於停用狀態。此操作無法撤銷：

```text
/app/cleanup <app>
App data will be lost, continue? [y/N]:
```

使用 `/app/remove` 刪除應用條目本身。請先執行 cleanup 以移除應用資料。

:::warning
清理會永久刪除應用資料、配置和狀態。在繼續之前，請備份您需要的任何資料。
:::

### 網路設定 {#network-settings}

- `network` 選擇應用網路。`internal` 將應用置於 NAT 之後，`lan` 將 VETH 介面連線到 LAN 網橋，`default` 使用應用的預設網路。
- `network-pvid` 設定應用網橋埠的 PVID。預設值為 `1`。
- `network-outgoing-access=no` 使用 mangle drop 規則阻止來自應用的出站連線。請記住，這可能會干擾您現有的防火牆。
- `use-https` 控制應用使用 HTTPS 反向代理和雲 URL，還是使用普通 HTTP 並將埠轉發到路由器 IP。

## 自定義應用 {#custom-apps}

當目錄中不包含你需要的服務，或者你需要不同的容器配置時，建立自定義應用。自定義應用使用與目錄應用相同的 compose YAML 格式，並標記為標誌 `c`。你也可以在自定義應用商店中釋出自定義應用。

### 建立空白應用 {#create-a-blank-app}

建立應用並將其分配到 LAN 網路：

```routeros
/app/add network=lan
```

該應用會以停用狀態建立，名稱為 `app`，且沒有服務容器。在終端中新增 YAML 配置：

```routeros
/app/edit app yaml
```

貼上 YAML，按 <kbd>Control</kbd>+<kbd>O</kbd> 儲存，然後啟用該應用。

### 匯入 YAML 檔案 {#import-a-yaml-file}

儲存 compose 檔案，將其上傳到裝置，並將其內容用作應用 YAML：

```routeros
/app/add yaml=[/file/get <filename> contents]
```

應用建立時處於停用狀態。檢查匯入的配置後再啟用它。

### 新增自定義應用商店 {#add-a-custom-app-store}

在 `/app/settings` 中設定一個或多個應用商店 URL：

```routeros
/app/settings/set app-store-urls="<url>"
```

每個 URL 必須返回一個 YAML 陣列，其中每個元素都是一個應用定義。從自定義商店載入的應用會帶有標誌 `s` 顯示。

### 為自定義應用編寫 YAML {#write-yaml-for-a-custom-app}

此示例從已包含 iperf3 的 openEuler 映象建立一個 iperf3 伺服器：

```yaml
name: openeuler-iperf
descr: openEuler container running iperf3 server
page: https://iperf.fr/
category: networking
default-credentials: none
services:
  iperf:
    image: docker.io/openeuler/iperf:latest
    ports:
      - 5201:5201:tcp
      - 5201:5201/udp:udp
    command: /bin/sh -c "iperf3 -s"
```

該映象已包含 `iperf3`，埠會轉發到路由器 IP，並且 `command` 會在容器啟動時啟動伺服器。

要在容器啟動時安裝 iperf3，請使用普通基礎映象：

```yaml
name: alpine-iperf
descr: Alpine Linux container running iperf3 server
page: https://iperf.fr/
category: networking
default-credentials: none
services:
  iperf:
    image: docker.io/alpine:latest
    command: /bin/sh -c "apk add --no-cache iperf3 && iperf3 -s"
networks:
  default:
    name: lan
    external: true
```

此示例安裝 iperf3，並在每次容器啟動時啟動它。容器需要訪問網際網路才能下載該軟體包。`networks` 部分會將應用直接置於 LAN 上，而不是轉發埠。

若要僅在軟體包缺失時才安裝它，請使用條件命令：

```yaml
command: /bin/sh -c "if ! command -v iperf3 >/dev/null 2>&1; then apk add --no-cache iperf3; fi; exec iperf3 -s"
```

### 對映埠 {#map-ports}

使用 `<router-port>:<container-port>` 或 `<router-port>:<container-port>:<name>`：

```yaml
ports:
  - 8080:80:web
  - 9000:9000:api
  - 6000:6000/udp:dns
```

除非新增 `/udp`，否則埠為 TCP。如果沒有名為 `web` 的埠，則第一個 TCP 埠會成為 Web 埠。名為 `web` 的埠會獲得反向代理條目和 UI URL。如果 `web` 埠在容器內部沒有監聽器，應用會保持在 `starting` 狀態，因此請顯式命名埠。

### 設定 URL 路徑 {#set-a-url-path}

使用 `url-path` 在生成的應用 URL 後追加路徑：

```yaml
url-path: /admin
```

此時 UI URL 以 `/admin` 結尾。

## YAML 參考 {#yaml-reference}

一個 YAML 文件定義一個應用。應用級部分包含元資料，而 `services` 部分包含一個或多個容器定義。

### 應用級欄位 {#app-level-fields}

| 欄位 | 型別 | 描述 |
| :-- | :-- | :-- |
| `name` | *字串* | 應用的唯一名稱。 |
| `descr` | *字串* | 應用的描述。 |
| `page` | *字串* | 專案頁面的 URL，顯示為 `project-page` 屬性。 |
| `category` | *字串* | 在應用列表中顯示的分類組。 |
| `default-credentials` | *字串* | 採用 `username:password` 格式的登入憑據。僅供參考。 |
| `icon` | *字串* | 在 WebFig 中顯示的圖示 URL。 |
| `url-path` | *字串* | 追加到應用 URL 的路徑，例如 `/login` 或 `/web`。 |
| `auto-update` | *布林值* | 有新映象可用時更新應用。 |
| `supported-archs` | *字串列表* | 支援的架構：`arm`、`arm64`、`arm_v5` 和 `x86`。目錄使用此列表為裝置選擇應用。 |
| `compatible-boards` | *字串列表* | 支援的板卡名稱，例如 `RDS2216`。接受 `*` 萬用字元。目錄使用此列表為裝置選擇應用。 |
| `services` | *對映* | 容器服務定義。至少需要一個服務。 |
| `volumes` | *對映* | 服務使用的命名卷宣告。 |
| `secrets` | *對映* | 在 `environment` 中透過 `[secret:name]` 引用的金鑰名稱。 |
| `configs` | *對映* | 掛載到服務中的配置檔案宣告。 |
| `networks` | *對映* | 服務使用的網路宣告。 |

即使自定義應用的 `supported-archs` 值與該裝置不匹配，它們仍會保持可見。

### 服務欄位 {#service-fields}

| 欄位 | 型別 | 描述 |
| :-- | :-- | :-- |
| `image` | *字串* | 用於容器的應用映象。必需。 |
| `container_name` | *字串* | 在 `/container` 中使用的容器名稱。 |
| `command` | *字串* | 在容器內執行的啟動命令。 |
| `entrypoint` | *字串* | 用作容器入口點的可執行檔案。 |
| `environment` | *列表或對映* | 傳遞給容器的環境變數。 |
| `volumes` | *列表* | 附加到容器的掛載點。 |
| `ports` | *列表* | 從路由器到容器的埠對映。 |
| `expose` | *列表* | 向其他容器公開但不在路由器上釋出的埠。 |
| `restart` | *字串* | 重啟策略：`unless-stopped`、`always` 或 `on-failure`。 |
| `depends_on` | *列表* | 必須在此服務之前啟動的服務名稱。 |
| `healthcheck` | *對映* | 檢查服務是否正在執行的探測。 |
| `shm_size` | *字串* | 共享記憶體大小，例如 `512mb` 或 `1gb`。 |
| `stop_grace_period` | *字串* 或 *整數* | 優雅關閉的超時時間，例如 `30s` 或 `0`。 |
| `devices` | *列表* | 透傳到容器的硬體裝置。 |
| `user` | *字串* | 容器執行所使用的 Linux 使用者或 UID。 |
| `hostname` | *字串* | 在容器中設定的主機名。 |
| `security_opt` | *列表* | 容器安全選項。 |
| `build` | *對映* | 本地構建映象的構建配置。 |
| `secrets` | *列表* | 此服務可在 `/run/secrets/<name>` 以檔案形式使用的金鑰名稱。 |
| `configs` | *列表* | 掛載到此服務的配置檔案。 |

### 健康檢查 {#healthcheck}

健康檢查會探測該服務，並在命令以程式碼 0 退出時將其視為健康。對於可執行檔案，請使用帶有獨立引數的 `CMD`：

```yaml
healthcheck:
  test: ["CMD", "wget", "-qO-", "http://localhost/"]
  interval: 30s
  retries: 3
  start_period: 30s
  timeout: 10s
```

當命令包含諸如 `||` 或管道之類的 shell 語法時，請使用 `CMD-SHELL`：

```yaml
healthcheck:
  test: ["CMD-SHELL", "wget -qO- http://localhost/ || exit 1"]
  interval: 30s
  retries: 3
  start_period: 30s
  timeout: 10s
```

使用 `CMD` 時，每個列表元素都會成為一個引數。放在單個 `CMD` 引數中的 shell 表示式會作為文字傳遞並失敗。

### 執行時佔位符 {#runtime-placeholders}

環境值和 `default-credentials` 可以包含 RouterOS 在應用執行時替換的佔位符。

| 佔位符 | 描述 |
| :-- | :-- |
| `[accessIP]` | 用於從外部訪問應用的 IP 地址或主機名。 |
| `[accessPort]` | 對映到應用 Web 介面的路由器埠。 |
| `[accessProto]` | 用於訪問應用的協定：`http` 或 `https`。 |
| `[containerIP]` | 分配給容器的 IP 地址。 |
| `[containerInterface]` | 容器內 VETH 介面的名稱。名稱限制為 15 個字元。 |
| `[routerIP]` | 來自 `/app/settings router-ip` 的路由器 IP 地址。 |
| `[networkRouterIP]` | 應用網路上的路由器 IP 地址。 |
| `[env:variable]` | 應用的環境變數值。 |
| `[env:service:variable]` | 指定服務的環境變數值。 |
| `[secret:name]` | 在應用級 `secrets` 部分宣告的機密值。 |

示例環境值：

```yaml
environment:
  - NEXTCLOUD_TRUSTED_DOMAINS=[accessIP]
  - APP_URL=[accessProto]://[accessIP]:[accessPort]
```

### 卷 {#volumes}

向服務新增持久化資料：

```yaml
services:
  app:
    image: docker.io/example/app:latest
    volumes:
      - data:/data
      - appdata/conf:/etc/app
```

`data` 是應用儲存中的命名卷。諸如 `appdata/conf` 的路徑是應用儲存的子目錄，並掛載到 `/etc/app`。

### 金鑰 {#secrets}

在應用級 `secrets` 部分宣告金鑰，並使用 `[secret:name]` 引用它們。RouterOS 在應用執行時生成該值：

```yaml
secrets:
  db_password:
  admin_password:
services:
  db:
    image: docker.io/postgres:17
    environment:
      POSTGRES_PASSWORD: "[secret:db_password]"
  server:
    image: docker.io/example/server:latest
    environment:
      ADMIN_PASSWORD: "[secret:admin_password]"
```

要將金鑰作為檔案掛載，請在服務下列出它。該檔案可在 `/run/secrets/<name>` 處使用：

```yaml
services:
  server:
    image: docker.io/example/server:latest
    environment:
      DB_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
```

### 配置 {#configs}

Configs 以文字形式向容器提供配置檔案。在應用級 `configs` 部分宣告內容，並使用 `source`、`target` 和可選的 `mode` 將其掛載到服務中：

```yaml
configs:
  mosquitto_conf:
    content: |
      listener 1883
      allow_anonymous true
services:
  mosquitto:
    image: docker.io/eclipse-mosquitto:latest
    configs:
      - source: mosquitto_conf
        target: /mosquitto/config/mosquitto.conf
        mode: 0644
```

`source` 是應用級 config 宣告的名稱，`target` 是容器內的路徑，`mode` 是檔案許可權。

### 網路 {#networks}

預設情況下，應用在 NAT 後的內部網路上執行，服務透過對映埠訪問。要將應用直接放到某個網路上，請使用外部網路定義預設網路：

```yaml
networks:
  default:
    name: lan
    external: true
```

然後，應用會將其 VETH 介面連線到 `/app/settings` 中的 LAN 網橋。

### 自定義應用商店 {#custom-app-store}

自定義應用商店是一個 YAML 陣列，其中每個元素都是一個應用定義。該檔案必須可由路由器訪問：

```yaml
- name: code-server
  descr: Code-server is VS Code running on a remote server, accessible through the browser.
  page: https://coder.com
  category: development
  icon: https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/code-server-logo.png
  default-credentials: <no_username>:password
  services:
    code-server:
      image: lscr.io/linuxserver/code-server:latest
      container_name: code-server
      user: "0:0"
      environment:
        PUID: 0
        PGID: 0
        PASSWORD: password
        PWA_APPNAME: code-server
      volumes:
        - config:/config
        - media:/data/media
      ports:
        - 8443:8443:web
```

新增更多列表項以釋出更多應用。

## 應用屬性 {#app-properties}

應用選單具有以下屬性。`/app/add` 建立的新應用處於停用狀態。

| 屬性 | 型別 | 預設值 | 描述 |
| :-- | :-- | :-- | :-- |
| **auto-update** | *yes* &#124; *no* | *no* | 在重啟後 app 啟動時檢查新映象。 |
| **check-certificate** | *yes* &#124; *no* | *yes* | 根據路由器證書儲存驗證登錄檔證書。 |
| **container-command-lines** | *string* | *(empty)* | 從 YAML 生成的容器命令。 |
| **devices** | *string* | *(empty)* | 傳遞給容器的額外硬體裝置。 |
| **disabled** | *yes* &#124; *no* | *yes* | app 是否被停用。新 app 建立時處於停用狀態。 |
| **environment** | *string* | *(empty)* | `service:key=value` 形式的環境變數。 |
| **extra-mounts** | *string* | *(empty)* | 附加到容器的額外掛載點。 |
| **firewall-redirects** | *string* | *(empty)* | `router-port:container-port:protocol:name` 形式的埠重定向。 |
| **network** | *default* &#124; *lan* &#124; *internal* | *default* | app 使用的網路。`default` 使用 app 的預設網路。 |
| **network-outgoing-access** | *yes* &#124; *no* | *yes* | 允許來自 app 的出站連線。設定為 `no` 時，RouterOS 會新增一條 mangle drop 規則。 |
| **network-pvid** | *integer* | *1* | app 橋接埠的 PVID。 |
| **required-hw-devices** | *string* | *(empty)* | app 啟動時必須存在的硬體裝置。 |
| **required-mounts** | *string* | *(empty)* | app 所需的掛載目錄。 |
| **use-https** | *yes* &#124; *no* | *yes* | 為 app URL 使用 HTTPS 和反向代理。 |
| **yaml** | *string* | *(empty)* | 定義 app 的 Compose YAML。 |

只讀值：

| 屬性 | 描述 |
| :-- | :-- |
| **app-size** | app 映象的大小，單位為 MiB。 |
| **app-store-url** | app 來源的自定義 app 商店的 URL。 |
| **data-size** | app 資料的大小。 |
| **default-credentials** | 來自 YAML 的預設登入憑據。 |
| **default-network** | 來自 YAML 的預設網路。 |
| **description** | 來自 YAML 的 app 描述。 |
| **interface** | app 使用的 VETH 介面。 |
| **ip-address** | 分配給 VETH 介面的 IP 地址。 |
| **memory-current** | app 當前的記憶體使用量。 |
| **name** | app 名稱。 |
| **project-page** | 來自 YAML 的專案頁面 URL。 |
| **status** | 當前啟動或錯誤狀態。app 執行期間為空。 |
| **ui-url** | 為 app Web 介面生成的 URL。 |
| **variables-to-use-in-environment** | 佔位符及其當前值。 |

`/app/settings` 引數在 CLI 參考中有說明。

## 技術細節 {#technical-details}

啟用的應用會建立以下物件：

- 名為 `veth-app-<app>` 的 VETH 介面。
- 內部網橋或 LAN 網橋上的一個網橋埠。
- 對於內部網路，還包括 `internal` 網橋、`172.18.0.1/24` 地址以及一條源 NAT 偽裝規則。
- 每個對映埠對應一條目標 NAT 規則。
- 當 `use-https=yes` 時，為 `web` 埠新增一條反向代理規則。
- 每個服務對應一個容器，命名為 `app-<app>-<service>`。

所選磁碟上的儲存路徑：

- `<disk>/apps/layers` 存放共享映象層。
- `<disk>/apps/<app>/<service>_root` 存放容器根目錄。
- `<disk>/apps/<app>/<volume>` 存放命名卷。
- `<disk>/apps/<app>/secret-<name>` 存放金鑰檔案。
- `<disk>/apps/<app>/config-<name>` 存放配置檔案。

在啟用應用之前先設定 `router-ip`，這樣其生成的 URL 和環境變數值就會使用最終地址。

## 相關主題 {#related-topics}

- [容器](../index.md)，用於手動配置容器。
- [VETH](../veth.md)，用於虛擬乙太網介面。
- [反向代理](../../network-management/proxy/reverse-proxy.md#container-apps)，用於 HTTPS 應用 URL。
- [證書](../../authentication-authorization-accounting/certificates.md)，用於證書管理。
- [可用應用列表](./available-apps.md)。
