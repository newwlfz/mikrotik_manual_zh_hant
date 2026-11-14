---
sidebar_key: "wireless/abgn/capsman/ap-controller-capsman"
sidebar_position: 1
title: "AP 控制器（CAPsMAN）"
sidebar_label: "AP 控制器"
description: "CAPsMAN（受控接入點系統管理器）透過允許 RouterOS 伺服器配置多個接入點、處理用戶端身份驗證和資料轉發，實現無線網路的集中管理。它支援無限數量的 CAP（受特定硬體限制），使用 DTLS 進行安全的管理連線，並提供集中式或本地資料轉發的選項。"
tags:
  - 'capsman'
  - 'wireless-management'
  - 'dtls'
source: https://manual.mikrotik.com/docs/7.25/wireless/abgn/capsman/ap-controller-capsman
captured_at: '2026-11-04T11:23:53+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
本頁介紹用於執行 `wireless` 軟體包（`/interface/wireless`）的裝置的舊版 CAPsMAN（`/caps-man`）。如果您的裝置使用 `/interface/wifi` 選單（`wifi-qcom` / `wifi-qcom-ac` 軟體包），請改為參閱 [WiFi CAPsMAN](../../wifi/capsman.md)。
:::

---

CAPsMAN 允許從中央配置介面向多臺 MikroTik AP 裝置應用無線設定。

更具體地說，Controlled Access Point system Manager（CAPsMAN）允許集中管理無線網路，並在必要時集中處理資料。使用 CAPsMAN 功能時，網路將由若干提供無線連線的“受控接入點”（CAP）以及一個管理 AP 配置的“系統管理器”（CAPsMAN）組成。它還負責用戶端認證，並可選擇負責資料轉發。

當 CAP 由 CAPsMAN 控制時，它只需要最低限度的配置即可與 CAPsMAN 建立連線。傳統上由 AP 執行的功能（如訪問控制、用戶端認證）現在由 CAPsMAN 執行。CAP 裝置現在只需提供無線鏈路層加密/解密。

根據配置，資料要麼轉發到 CAPsMAN 進行集中處理（*預設*），要麼在 CAP 本地轉發（本地轉發模式）。

## 要求 {#requirements}

- 任何 RouterOS 裝置只要至少具有 Level 4 RouterOS 許可證，都可以作為受控無線接入點（CAP）。
- CAPsMAN 伺服器可以安裝在任何 RouterOS 裝置上，即使該裝置本身沒有無線介面。
- CAPsMAN 支援無限數量的 CAP（接入點）。
- 每個 CAP 最多 32 個射頻。
- 每個主射頻介面最多 32 個虛擬介面。
- 不能使用 Nv2 和 NStreme 專有協定。

---

## CAPsMAN 系統的簡單設定 {#simple-setup-of-a-capsman-system}

![](/img/24386f7736bf211a.webp)

在深入探討 CAPsMAN 操作細節之前，讓我們快速說明如何設定最基本的系統：由一臺 MikroTik 路由器管理兩臺 MikroTik AP 裝置。CAPsMAN 的好處是 CAP 單元無需配置；所有設定都在 CAPsMAN 伺服器上完成。

CAPsMAN 設定包括定義配置模板，然後將這些模板推送到可控制的 AP 裝置（CAP）。假設您的主路由器已連線到網際網路且工作正常，可以按如下步驟操作。

在將作為 CAPsMAN 伺服器的中央裝置上，建立一個僅包含基本設定的新“Configuration”模板（網路名稱、國家/地區、本地 LAN 網橋介面、無線密碼）：

![](/img/7c8e743432e137ce.webp)新增新的配置模板：
![](/img/93fa941161ea2b1a.webp)
![](/img/78b31855d8f3b0d5.webp)

然後建立新的“Provisioning”規則，將已建立的配置模板分配給 CAP 裝置：

![](/img/b976b0971eb21c10.webp)

在 CAPsMAN 上剩下要做的就是啟用它：

![](/img/69dbb61f857cb034.webp)

大多數 MikroTik AP 裝置開箱即支援 CAP 模式，您只需確保它們與 CAPsMAN 位於同一網路，然後在按住復位按鈕的同時啟動它們。

例如，在 CAP 裝置關閉時將其連線到 CAPsMAN 裝置的某個 LAN 埠，然後按住復位按鈕，並給 CAP 裝置上電。繼續按住按鈕，直到 User LED 常亮，然後鬆開以開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（按住按鈕的總時間約為 10 秒）。

裝置現在將顯示在 CAPsMAN 的“Remote CAP”選單中，並會根據預配設定使用配置模板進行“預配”。有關如何手動調整所有設定的更多詳細資訊，請繼續閱讀本文件。

### CAP 到 CAPsMAN 的連線 {#cap-to-capsman-connection}

為使 CAPsMAN 系統正常執行並提供無線連線，CAP 必須與 CAPsMAN 建立管理連線。管理連線可以使用 MAC 或 IP 層協定建立，並使用“DTLS”進行保護。

CAP 也可以將用戶端資料連線傳遞給 Manager，但資料連線不受保護。如果認為有必要，則需要使用其他資料安全手段，例如 IPSec 或加密隧道。

CAP 到 CAPsMAN 的連線可以使用 2 種傳輸協定建立（透過 Layer 2 和 Layer 3）。

- MAC 層連線特性：
  - CAP 上無需 IP 配置。
  - CAP 和 CAPsMAN 必須位於同一 Layer 2 網段——物理或虛擬（透過 L2 隧道）。
- IP 層（UDP）連線特性：
  - 如有必要可以穿越 NAT。
  - CAP 必須能夠使用 IP 協定訪問 CAPsMAN。
  - 如果 CAP 與 CAPsMAN 不在同一 L2 網段，則必須為 CAP 預配 CAPsMAN IP 地址，因為基於 IP 組播的發現無法跨 Layer 3 工作。

為了與 CAPsMAN 建立連線，CAP 會執行發現過程。在發現期間，CAP 嘗試聯絡 CAPsMAN 並構建可用 CAPsMAN 列表。CAP 嘗試透過以下方式聯絡可用的 CAPsMAN：

- 已配置的 Manager IP 地址列表。
- 從 DHCP 伺服器獲取的 CAPsMAN IP 地址列表。
- 在已配置介面上使用 IP 和 MAC 層協定進行廣播。

構建可用 CAPsMAN 列表後，CAP 根據以下規則選擇 CAPsMAN：

- 如果 **caps-man-names** 引數指定了允許的 Manager 名稱（CAPsMAN 的 `/system/identity`），CAP 將優先選擇列表中靠前的 CAPsMAN；如果列表為空，它將連線到任何可用的 Manager。
- 具有 MAC 層連線的合適 Manager 優先於具有 IP 連線的 Manager。

選擇 Manager 後，CAP 嘗試建立 DTLS 連線。可能使用以下認證模式：

- CAP 和 CAPsMAN 上沒有證書——不進行認證。
- 僅 Manager 配置了證書——CAP 會檢查 CAPsMAN 證書，但如果沒有合適的受信任 CA 證書也不會失敗；為了與沒有證書的 CAP 建立連線，CAPsMAN 必須配置 **require-peer-certificate=no**。
- CAP 和 CAPsMAN 都配置了證書——雙向認證。

建立 DTLS 連線後，CAP 可以選擇檢查 CAPsMAN 提供的證書的 CommonName 欄位。**caps-man-certificate-common-names** 引數包含允許的 CommonName 值列表。如果此列表不為空，CAPsMAN 必須配置證書。如果此列表為空，CAP 不檢查 CommonName 欄位。

如果 CAPsMAN 或 CAP 與網路斷開連線，CAP 與 CAPsMAN 之間的連線丟失將在大約 10-20 秒內被檢測到。

#### CAP 自動鎖定到 CAPsMAN {#cap-auto-locking-to-capsman}

CAP 可以配置為自動鎖定到特定的 CAPsMAN 伺服器。鎖定透過記錄 CAP 所鎖定到的 CAPsMAN 證書 CommonName，並在所有後續連線中檢查此 CommonName 來實現。由於此功能使用證書 CommonName 實現，因此必須使用證書才能讓鎖定生效。

透過以下命令啟用鎖定：

```
[admin@CAP] > /interface/wireless/cap/set lock-to-caps-man=yes
```

一旦 CAP 連線到合適的 CAPsMAN 並鎖定到它，將如下所示：

```
[admin@wtp] > /interface/wireless/cap/print
...
        locked-caps-man-common-name: CAPsMAN-000C424C30F3
```

從現在起，CAP 將只連線到具有此 CommonName 的 CAPsMAN，直到透過設定 **lock-to-caps-man=no** 清除鎖定要求。如果需要強制 CAP 鎖定到另一個 CAPsMAN，則需要使用此方法——首先設定 **lock-to-caps-man=no**，然後設定 **lock-to-caps-man=yes**。

請注意，可以透過設定 **caps-man-certificate-common-names** 手動將 CAP“鎖定”到 CAPsMAN。

#### 自動證書 {#auto-certificates}

為在需要證書時（例如自動鎖定功能）簡化 CAPsMAN 和 CAP 配置，可以將 CAPsMAN 配置為自動生成必要的證書，並將 CAP 配置為向 CAPsMAN 請求證書。

**自動證書不提供完整的公鑰基礎設施**，僅適用於簡單設定。如果需要更復雜的 PKI——支援適當的證書有效期、多級 CA 證書、證書續期——則必須使用其他方式，例如手動分發證書或 SCEP。

CAPsMAN 具有以下證書設定：

- **certificate** - 這是 CAPsMAN 證書，此證書必須具有可用的私鑰。如果設定為 **none**，CAPsMAN 將以無證書模式執行，任何需要證書的功能都不會工作。如果設定為 **auto**，CAPsMAN 將嘗試使用 CA 證書（請參閱 **ca-certificate** 描述）向自己頒發證書。請注意，自動頒發證書的 CommonName 將為 `CAPsMAN-<mac address>`，有效期將與 CA 證書相同。
- **ca-certificate** - 這是 CA 證書，CAPsMAN 在必要時（請參閱 **certificate** 描述）為自己頒發證書以及簽署來自 CAP 的證書請求時將使用它。如果設定為 **none**，CAPsMAN 將無法為自己頒發證書或簽署來自 CAP 的證書請求。如果設定為 **auto**，CAPsMAN 將生成自簽名 CA 證書作為 CA 證書使用。此證書的 CommonName 格式為 `CAPsMAN-CA-<mac address>`，有效期將從 1970-01-01 到 2038-01-18。

當 CAPsMAN 自動生成證書時，將如下所示：

```
[admin@CM] /caps-man/manager> pr
                   enabled: yes
               certificate: auto
            ca-certificate: auto
  require-peer-certificate: no
     generated-certificate: CAPsMAN-000C424C30F3
  generated-ca-certificate: CAPsMAN-CA-000C424C30F3
```

以及證書：

```
[admin@CM] /certificate> print detail
Flags: K - private-key, D - dsa, L - crl, C - smart-card-key, 
A - authority, I - issued, R - revoked, E - expired, T - trusted 
 0 K   A T name="CAPsMAN-CA-000C424C30F3" common-name="CAPsMAN-CA-000C424C30F3" key-size=2048 
           days-valid=24854 trusted=yes 
           key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign 
           serial-number="1" fingerprint="69d77bbb45c50afd2d6c1785c2a3d72596b8a5f6" 
           invalid-before=1970-01-01 00:00:01 invalid-after=2038-01-18 03:14:07 

 1 K   I   name="CAPsMAN-000C424C30F3" common-name="CAPsMAN-000C424C30F3" key-size=2048 
           days-valid=24854 trusted=no key-usage=digital-signature,key-encipherment 
           ca=CAPsMAN-CA-000C424C30F3 serial-number="1" 
           fingerprint="e853ddb9d41fc139083a176ab164331bc24bc5ed" 
           invalid-before=1970-01-01 00:00:01 invalid-after=2038-01-18 03:14:07 
```

CAP 可以配置為向 CAPsMAN 請求證書。為此，CAP 必須配置 **certificate=request** 設定，並且 CAPsMAN 必須具有可用的 CA 證書（在 **ca-certificate** 設定中指定或自動生成）。

CAP 最初將生成私鑰和 CommonName 格式為 `CAP-<mac address>` 的證書請求。當 CAP 與 CAPsMAN 建立連線時，CAP 將請求 CAPsMAN 簽署其證書請求。如果成功，CAPsMAN 將向 CAP 傳送 CA 證書和新頒發的證書。CAP 將這些證書匯入其證書儲存：

```
[admin@CAP] > /interface/wireless/cap/print
...
              requested-certificate: cert_2
        locked-caps-man-common-name: CAPsMAN-000C424C30F3
[admin@CAP] > /certificate/print detail 
Flags: K - private-key, D - dsa, L - crl, C - smart-card-key, 
A - authority, I - issued, R - revoked, E - expired, T - trusted 
 0       T name="cert_1" issuer=CN=CAPsMAN-CA-000C424C30F3 common-name="CAPsMAN-CA-000C424C30F3" 
            key-size=2048 days-valid=24837 trusted=yes 
            key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign 
            serial-number="1" fingerprint="69d77bbb45c50afd2d6c1785c2a3d72596b8a5f6" 
            invalid-before=1970-01-01 00:00:01 invalid-after=2038-01-18 03:14:07 

 1 K     T name="cert_2" issuer=CN=CAPsMAN-CA-000C424C30F3 common-name="CAP-000C4200C032" 
            key-size=2048 days-valid=24837 trusted=yes 
            key-usage=digital-signature,key-encipherment serial-number="2" 
            fingerprint="2c85bf2fbc9fc0832e47cd2773a6f4b6af35ef65" 
            invalid-before=1970-01-01 00:00:01 invalid-after=2038-01-18 03:14:07 
```

在後續連線到 CAPsMAN 時，CAP 將使用生成的證書。

---

## CAP 配置 {#cap-configuration}

當 AP 配置為由 CAPsMAN 控制時，AP 上受管無線介面的配置將被忽略*（例外：antenna-gain、antenna-mode）*。相反，AP 從 CAPsMAN 接受受管介面的配置。

:::warning
由 CAPsMAN 管理且其流量被轉發到 CAPsMAN 的 CAP 無線介面（即它們不處於*本地轉發*模式）顯示為*停用*，並帶有註釋 **Managed by CAPsMAN**。那些處於*本地轉發*模式的介面（流量由 CAP 本地管理，僅管理由 CAPsMAN 完成）不會顯示為停用，但會顯示註釋 **Managed by CAPsMAN**
:::

AP 的 CAP 行為在 `/interface/wireless/cap` 選單中配置。在那裡您可以：

- 在裝置上停用或啟用 CAP 功能。
- 設定要由 Manager 控制的無線介面列表。
- 設定 CAP 應嘗試透過其發現 Manager 的介面列表。
- 設定 CAP 在發現期間將嘗試聯絡的 Manager IP 地址列表。
- 設定 CAP 將嘗試連線的 Manager 名稱列表。
- 設定 CAP 將連線的 Manager 證書 CommonName 列表。
- 設定使用本地轉發模式時應將介面新增到的網橋。

CAP 上由 CAPsMAN 控制的每個無線介面都會在 CAPsMAN 上顯示為虛擬介面。這在使用常規 RouterOS 功能（如路由、橋接、防火牆等）控制資料轉發時提供了最大的靈活性。

## CAPsMAN 配置概念 {#capsman-configuration-concepts}

許多無線介面設定可以分組到命名組（“模板”）中，以簡化配置複用——例如，可以在“配置模板”中配置通用設定，然後多個介面可以引用該模板。同時，為了獲得最大靈活性，任何模板設定都可以直接在介面配置中覆蓋。

目前有以下設定組：

- channel - 通道相關設定，例如頻率和寬度。
- datapath - 資料轉發相關設定，例如應將特定介面自動新增為埠的網橋。
- security - 安全相關設定，例如允許的認證型別或口令。
- configuration - 主無線設定組，包括 SSID 等設定，並另外將其他設定組繫結在一起——也就是說，配置模板可以引用 channel、security 等命名設定組。此外，任何設定都可以直接在配置模板中覆蓋。

介面設定將所有設定組繫結在一起，但此外任何設定都可以直接在介面設定中覆蓋。

透過設定組，配置以介面（配置的實際使用者）為根組織成層次結構。為了確定某個設定的有效值，會按照較高層級的設定值覆蓋較低層級值的方式查詢此結構。

例如，當需要查詢某個介面要使用的 WPA2 口令時，會按以下位置依次查詢，第一個配置了 WPA2 口令的位置決定有效口令。“->”表示引用設定模板（如果已配置）：

- 介面口令
- interface->security 口令
- interface->configuration 口令
- interface->configuration->security 口令

CAPsMAN 上有 2 種介面——“主”介面和“從”介面。主介面儲存實際無線介面（射頻）的配置，而從介面連結到主介面，旨在儲存 Virtual-AP（多 SSID 支援）的配置。有些設定僅對主介面有意義，即主要是與硬體設定相關的設定，例如射頻通道設定。請注意，為了讓射頻接受用戶端，其主介面需要啟用。從介面只有在啟用且主介面已啟用時才會進入工作狀態。

CAPsMAN 上的介面可以是靜態或動態的。靜態介面儲存在 RouterOS 配置中，並會在重啟後保留。動態介面僅在特定 CAP 連線到 CAPsMAN 時存在。

### CAPsMAN 全域性配置 {#capsman-global-configuration}

用於啟用 CAPsMAN 功能的設定位於 `/caps-man/manager` 選單中：

| 屬性 | 描述 |
| :-- | :-- |
| **enabled** (*yes \| no*；預設值：**no**) | 停用或啟用 CAPsMAN 功能 |
| **certificate** (*auto \| certificate name \| none*; Default: **none**) | 裝置證書 |
| **ca-certificate** (*auto \| certificate name \| none*；預設值：**none**) | 裝置 CA 證書 |
| **require-peer-certificate** (*yes \| no*；預設值：**no**) | 要求所有連線的 CAP 都具有有效證書 |
| **package-path** (*string \|*；預設值： ) | RouterOS 軟體包的資料夾位置。例如，使用 "/upgrade" 指定檔案部分中的 upgrade 資料夾。如果設定為空字串，CAPsMAN 可以使用內建 RouterOS 軟體包；請注意，在這種情況下，只有與 CAPsMAN 架構相同的 CAP 才會被升級。 |
| **upgrade-policy** (*none \| require-same-version \| suggest-same-version*; 預設：**none**) | 升級策略選項none - 不執行升級require-same-version - CAPsMAN 建議升級 CAP 的 RouterOS 版本，如果失敗，則不會預配該 CAP。（仍可手動預配）suggest-same-version - CAPsMAN 建議升級 CAP 的 RouterOS 版本，如果失敗，仍會進行預配 |

### 射頻預配 {#radio-provisioning}

CAPsMAN 根據識別符號區分 CAP。該識別符號根據以下規則生成：

- 如果 CAP 提供了證書，則識別符號設定為證書中的 Common Name 欄位。
- 否則，識別符號基於 CAP 提供的 Base-MAC，格式為：‘[XX:XX:XX:XX:XX:XX]’。

當與 CAP 的 DTLS 連線成功建立時（這意味著 CAP 識別符號已知且有效），CAPsMAN 會確保沒有使用相同識別符號的陳舊 CAP 連線。當前連線的 CAP 列在 `/caps-man/remote-cap` 選單中：

```
[admin@CM] /caps-man> remote-cap print
 # ADDRESS                                    IDENT           STATE               RADIOS
 0 00:0C:42:00:C0:32/27044                    MT-000C4200C032 Run                      1
```

CAPsMAN 根據實際無線介面（射頻）的內建 MAC 地址（radio-mac）區分它們。這意味著無法在一個 CAPsMAN 上管理兩個具有相同 MAC 地址的射頻。當前由 CAPsMAN 管理的射頻（由已連線的 CAP 提供）列在 `/caps-man/radio` 選單中：

```
[admin@CM] /caps-man> radio print
Flags: L - local, P - provisioned 
 #    RADIO-MAC         INTERFACE                               REMOTE-AP-IDENT
 0  P 00:03:7F:48:CC:07 cap1                                    MT-000C4200C032
```

當 CAP 連線時，CAPsMAN 首先嚐試根據 radio-mac 將每個 CAP 射頻繫結到 CAPsMAN 主介面。如果找到合適的介面，則使用主介面配置以及引用該特定主介面的從介面配置來設定射頻。此時，介面（主介面和從介面）被視為已繫結到射頻，並且射頻被視為已預配。

如果未找到與該射頻匹配的主介面，CAPsMAN 將執行“預配規則”。預配規則是一個有序規則列表，其中包含指定要匹配哪些射頻的設定，以及指定射頻匹配後採取何種操作的設定。

用於匹配射頻的預配規則在 `/caps-man/provisioning` 選單中配置：

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*create-disabled \| create-enabled \| create-dynamic-enabled \| none*; 預設：**none**) | 規則匹配時採取的操作，由以下設定指定：create-disabled - 為射頻建立停用的靜態介面。也就是說，介面將繫結到射頻，但在手動啟用介面之前射頻不會工作；create-enabled - 建立啟用的靜態介面。也就是說，介面將繫結到射頻，並且射頻將工作；create-dynamic-enabled - 建立啟用的動態介面。也就是說，介面將繫結到射頻，並且射頻將工作；none - 不執行任何操作，使射頻保持未預配狀態； |
| **comment** (*string*；預設值： ) | 預配規則的簡短描述 |
| **common-name-regexp** (*string*; 預設：) | 用於按 CommonName 匹配射頻的正則表示式 |
| **hw-supported-modes** (*a\|a-turbo\|ac\|an\|b\|g\|g-turbo\|gn*；預設值： ) | 按支援的無線模式匹配無線電 |
| **identity-regexp** (*string*；預設值： ) | 用於按路由器身份匹配無線電的正則表示式 |
| **ip-address-ranges** (*IpAddressRange[,IpAddressRanges] max 100x*；預設值：**""**) | 匹配 IP 位於所配置地址範圍內的 CAP。 |
| **master-configuration** (*string*; 預設：) | 如果 **action** 指定建立介面，則將建立一個新的主介面，其配置設定為此配置模板 |
| **name-format** (*cap \| identity \| prefix \| prefix-identity*; 預設：**cap**) | 指定 CAP 介面名稱建立的語法cap - 預設名稱；identity - CAP 板的 `/system/identity` 名稱；prefix - 來自 name-prefix 值的名稱；prefix-identity - 來自 name-prefix 值和 CAP 板的 `/system/identity` 名稱的名稱 |
| **name-prefix** (*string*；預設值： ) | 可在 name-format 中用於建立 CAP 介面名稱的名稱字首 |
| **radio-mac** (*MAC address*; 預設：**00:00:00:00:00:00**) | 要匹配的射頻 MAC 地址，空 MAC（00:00:00:00:00:00）表示匹配所有 MAC 地址 |
| **slave-configurations** (*string*; 預設：) | 如果 **action** 指定建立介面，則為該列表中的每個配置模板建立一個新的從介面。 |

:::warning
如果沒有規則匹配該射頻，則會執行一條隱式預設規則，其 action 為 **create-enabled**，且未設定任何配置。
:::

獲取活動的預配匹配器：

```
[admin@CM] /caps-man/provisioning> print
Flags: X - disabled 
 0   radio-mac=00:00:00:00:00:00 action=create-enabled master-configuration=main-cfg 
     slave-configurations=virtual-ap-cfg name-prefix=""
```

為方便使用者，有些命令可以重新執行某個射頻或某個 AP 提供的所有射頻的預配過程：

```
[admin@CM] > /caps-man/radio/provision 0
```

以及：

```
[admin@CM] > /caps-man/remote-cap/provision 0
```

### 介面配置 {#interface-configuration}

CAPsMAN 介面在 `/caps-man/interface` 選單中管理：

```
[admin@CM] > /caps-man/interface/print          
Flags: M - master, D - dynamic, B - bound, X - disabled, I - inactive, R - running 
 #      NAME                                 RADIO-MAC         MASTER-INTERFACE                               
 0 M BR cap2                                 00:0C:42:1B:4E:F5 none                                           
 1   B  cap3                                 00:00:00:00:00:00 cap2                   

```

### 主配置模板 {#master-configuration-profiles}

配置模板允許將預定義的“頂層”主設定應用到正在預配的 CAP 射頻。

配置模板在 `/caps-man/configuration` 選單中配置：

| 屬性 | 描述 |
| :-- | :-- |
| **channel** (*list*；預設值： ) | 從 Channel 名稱（`/caps-man/channels`）中獲取的使用者定義列表 |
| **channel.band** (*2ghz-b \| 2ghz-b/g \| 2ghz-b/g/n \| 2ghz-onlyg \| 2ghz-onlyn \| 5ghz-a \| 5ghz-a/n \| 5ghz-onlyn \| 5ghz-a/n/ac \| 5ghz-only-ac*；預設值： ) | 定義所用通道集合。 |
| **channel.control-channel-width** (*40mhz-turbo \| 20mhz \| 10mhz \| 5mhz*；預設值： ) | 定義所用通道寬度集合。 |
| **channel.extension-channel** (*Ce \| Ceee \| eC \| eCee \| eeCe \| eeeC \| xx \| xxxx \| disabled*；預設值： ) | 擴充套件通道配置。（例如 Ce = 擴充套件通道位於控制通道之上，eC = 擴充套件通道位於控制通道之下） |
| **channel.frequency** (*integer [0..4294967295]*; 預設：) | AP 工作時的通道頻率值，單位為 MHz。如果留空，CAPsMAN 將自動確定佔用最少的最佳頻率。 |
| **channel.reselect-interval** (*time [00:00:00]*; *[00:00:00..00:00:00];* 預設：) | 選擇佔用最少頻率的間隔，可以定義為隨機間隔，例如 "30m..60m"。僅在 **channel.frequency** 留空時有效。 |
| **channel.save-selected** (*yes \| no*; 預設：**no**) | 如果自動選擇通道頻率且使用了 **channel.reselect-interval**，則儲存最後選取的頻率。 |
| **channel.secondary-frequency** (*integer [0..4294967295]*；預設值：**auto**) | 指定用於 80+80MHz 配置的第二個頻率。將其設定為 **Disabled** 可停用 80+80MHz 能力。 |
| **channel.skip-dfs-channels** (*yes \| no*；預設值：**no**) | 如果 **channel.frequency** 留空，選擇時將跳過 DFS 通道 |
| **channel.tx-power** (*integer [-30..40]*；預設值： ) | CAP 介面的 TX Power（針對整個介面，而不是單個鏈），單位為 dBm。不能設定得高於國家法規或介面允許的值。預設情況下，使用國家或介面允許的最大值。 |
| **channel.width** (；預設值： ) | 設定通道寬度，單位為 MHz。 |
| **comment** (*string*；預設值： ) | 配置配置檔案的簡短描述 |
| **country** (*name of the country \| no\_country\_set*; 預設：**no\_country\_set**) | 限制可用頻段、頻率以及每個頻率的最大發射功率。還指定 **scan-list** 的預設值。值 *no\_country\_set* 是符合 FCC 的通道集合。 |
| **datapath** (*list*；預設值： ) | 從 Datapath 名稱（`/caps-man/datapath`）中獲取的使用者定義列表 |
| **datapath.bridge** (*list*; 預設：) | 應將特定介面自動新增為埠的網橋 |
| **datapath.bridge-cost** (*integer [1..*200000000*]*; 預設：) | 作為網橋埠新增時使用的網橋埠開銷 |
| **datapath.bridge-horizon** (*integer [0..4294967295]*；預設值： ) | 作為網橋埠新增時要使用的網橋 horizon |
| **datapath.client-to-client-forwarding** (*yes \| no*; 預設：**no**) | 控制是否允許連線到該介面的無線用戶端之間進行用戶端到用戶端轉發；在本地轉發模式下，此功能由 CAP 執行，否則由 CAPsMAN 執行 |
| **datapath.interface-list** (；預設值： ) |  |
| **datapath.l2mtu** (；預設值： ) | 設定二層 MTU 大小 |
| **datapath.local-forwarding** (*yes \| no*; 預設：**no**) | 控制轉發模式 |
| **datapath.mtu** (；預設值： ) | 設定 MTU 大小 |
| **datapath.openflow-switch** (；預設值： ) | 要將介面新增到的 OpenFlow 交換器埠（啟用時） |
| **datapath.vlan-id** (*integer [1..4095]*；預設值： ) | 如果 vlan-mode 啟用 VLAN 標記，則分配給介面的 VLAN ID |
| **datapath.vlan-mode** (*use-service-tag \| use-tag*；預設值： ) | 啟用並指定要分配給介面的 VLAN 標記型別（使所有接收到的資料都打上 VLAN 標記，並允許介面只發送帶有指定標記的資料） |
| **disconnect-timeout** (；預設值： ) |  |
| **distance** (；預設值： ) |  |
| **frame-lifetime** (；預設值： ) |  |
| **guard-interval** (*any \| long*；預設值：**any**) | 是否允許使用短保護間隔（請參閱 802.11n MCS 規範，瞭解這可能如何影響吞吐量）。"any" 將根據資料速率使用短或長保護間隔，"long" 將僅使用長保護間隔。 |
| **hide-ssid** (*yes \| no*; 預設：) | yes - AP 不在 Beacon 幀中包含 SSID，也不回覆具有廣播 SSID 的探測請求。no - AP 在 Beacon 幀中包含 SSID，並回復具有廣播 SSID 的探測請求。此屬性僅在 AP 模式下生效。將其設定為 *yes* 可能會從某些用戶端軟體顯示的無線網路列表中移除此網路。更改此設定不會提高無線網路的安全性，因為 SSID 包含在 AP 傳送的其他幀中。 |
| **hw-protection-mode** (；預設值： ) |  |
| **hw-retries** (；預設值： ) |  |
| **installation** (*any \| indoor \| outdoor*；預設值：**any**) |  |
| **keepalive-frames** (*enabled \| disabled*；預設值：**enabled**) |  |
| **load-balancing-group** (*string*；預設值： ) | 將介面標記到負載均衡組。要使用戶端連線到該組中的介面，該介面已連線的用戶端數量應與組中所有其他介面相同或更少。在多個 CAP 的覆蓋範圍大多重疊的部署中很有用。 |
| **max-sta-count** (*integer [1..2007]*；預設值： ) | 最大關聯用戶端數。 |
| **mode** (；預設值：**ap**) | 設定工作模式。目前僅支援 ap。 |
| **multicast-helper** (*default \| disabled \| full*; 預設：**default**) | 設定為 full 時，組播封包將使用單播目標 MAC 地址傳送，從而解決無線鏈路上的組播問題。此選項只應在接入點上啟用；用戶端應配置為 **station-bridge** 模式。disabled - 停用該助手，並使用組播目標 MAC 地址傳送組播封包full - 在傳送前將所有組播封包的 MAC 地址改為單播 MAC 地址default - 當前設定為 disabled 的預設選擇。該值可能會在未來的版本中更改。 |
| **name** (*string*；預設值： ) | Configuration Profile 的描述性名稱 |
| **rates** (；預設值： ) | 從 Rates 名稱（`/caps-man/rates`）中獲取的使用者定義列表 |
| **rates.basic** (*1Mbps \| 2Mbps \| 5.5Mbps \| 6Mbps \| 9Mbps \| 11Mbps \| 12Mbps \| 18Mbps \| 24Mbps \| 36Mbps \| 48Mbps \| 54Mbps*；預設值： ) |  |
| **rates.supported** (*1Mbps \| 2Mbps \| 5.5Mbps \| 6Mbps \| 9Mbps \| 11Mbps \| 12Mbps \| 18Mbps \| 24Mbps \| 36Mbps \| 48Mbps \| 54Mbps*；預設值： ) |  |
| **rates.ht-basic-mcs** (*list of (mcs-0 \| mcs-1 \| mcs-2 \| mcs-3 \| mcs-4 \| mcs-5 \| mcs-6 \| mcs-7 \| mcs-8 \| mcs-9 \| mcs-10 \| mcs-11 \| mcs-12 \| mcs-13 \| mcs-14 \| mcs-15 \| mcs-16 \| mcs-17 \| mcs-18 \| mcs-19 \| mcs-20 \| mcs-21 \| mcs-22 \| mcs-23)*；預設值：**mcs-0; mcs-1; mcs-2; mcs-3; mcs-4; mcs-5; mcs-6; mcs-7**) | 每個連線的用戶端都必須支援的 [調製與編碼方案](https://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates)。有關 MCS 規範，請參閱 802.11n。 |
| **rates.ht-supported-mcs** (*list of (mcs-0 \| mcs-1 \| mcs-2 \| mcs-3 \| mcs-4 \| mcs-5 \| mcs-6 \| mcs-7 \| mcs-8 \| mcs-9 \| mcs-10 \| mcs-11 \| mcs-12 \| mcs-13 \| mcs-14 \| mcs-15 \| mcs-16 \| mcs-17 \| mcs-18 \| mcs-19 \| mcs-20 \| mcs-21 \| mcs-22 \| mcs-23)*；預設值：**mcs-0; mcs-1; mcs-2; mcs-3; mcs-4; mcs-5; mcs-6; mcs-7; mcs-8; mcs-9; mcs-10; mcs-11; mcs-12; mcs-13; mcs-14; mcs-15; mcs-16; mcs-17; mcs-18; mcs-19; mcs-20; mcs-21; mcs-22; mcs-23**) | 此裝置宣告支援的 [調製與編碼方案](https://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates)。有關 MCS 規範，請參閱 802.11n。 |
| **rates.vht-basic-mcs** (*none \| MCS 0-7 \| MCS 0-8 \| MCS 0-9*；預設值：**none**) | 每個連線的用戶端都必須支援的 [調製與編碼方案](../../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)。有關 MCS 規範，請參閱 802.11ac。可以為每個空間流設定 MCS 區間：none - 將不使用所選空間流；MCS 0-7 - 用戶端必須支援 MCS-0 到 MCS-7；MCS 0-8 - 用戶端必須支援 MCS-0 到 MCS-8；MCS 0-9 - 用戶端必須支援 MCS-0 到 MCS-9 |
| **rates.vht-supported-mcs** (*none \| MCS 0-7 \| MCS 0-8 \| MCS 0-9*；預設值：**none**) | 此裝置宣告支援的 [調製與編碼方案](http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed)。有關 MCS 規範，請參閱 802.11ac。可以為每個空間流設定 MCS 區間：none - 將不使用所選空間流；MCS 0-7 - 裝置將宣告支援 MCS-0 到 MCS-7；MCS 0-8 - 裝置將宣告支援 MCS-0 到 MCS-8；MCS 0-9 - 裝置將宣告支援 MCS-0 到 MCS-9 |
| **rx-chains** (*list of integer [0..3]*；預設值：**0**) | 用於接收的天線。 |
| **security** (*string*；預設值：**none**) | 來自 `/caps-man/security` 的安全配置名稱 |
| **security.authentication-types** (*list of string*；預設值：**none**) | 指定認證型別，可選值為 **wpa-psk**、**wpa2-psk**、**wpa-eap** 或 **wpa2-eap** |
| **security.disable-pmkid** (；預設值： ) |  |
| **security.eap-methods** (*eap-tls \| passthrough*；預設值：**none**) | eap-tls - 使用內建 EAP TLS 認證。passthrough - 接入點會將認證過程中繼到 RADIUS 伺服器。 |
| **security.eap-radius-accounting** (; 預設：) |  |
| **security.encryption** (*aes-ccm \| tkip*；預設值： ) | 設定所使用的單播加密演算法型別 |
| **security.group-encryption** (*aes-ccm \| tkip*；預設值：**aes-ccm**) | 接入點會通告這些密碼之一，可以選擇多個值。接入點使用它來加密所有廣播和組播幀。用戶端只會嘗試連線到使用指定組密碼之一的接入點。tkip - Temporal Key Integrity Protocol - 加密協定，與舊版 WEP 裝置相容，但經過增強以修正一些 WEP 缺陷。aes-ccm - 更安全的 WPA 加密協定，基於可靠的 AES（Advanced Encryption Standard）。沒有 WEP 遺留問題的網路應只使用此密碼。 |
| **security.group-key-update** (*time: 30s..1h*；預設值：**5m**) | 控制接入點更新組金鑰的頻率。此金鑰用於加密所有廣播和組播幀。該屬性僅對 Access Point 生效。 |
| **security.passphrase** (*string*; 預設：) | WPA 或 WPA2 預共享金鑰 |
| **security.tls-certificate** (*none \| name*; 預設：) | 當 `security.tls-mode` 設定為 `no-certificates` 以外的值時，接入點始終需要證書。 |
| **security.tls-mode** (*verify-certificate \| dont-verify-certificate \| no-certificates \| verify-certificate-with-crl*; 預設：) | 此屬性僅在 **security.eap-methods** 包含 *eap-tls* 時生效。verify-certificate - 要求遠端裝置具有有效證書。檢查該證書是否由已知證書頒發機構簽名。不會進行額外的身份驗證。證書可能包含其有效時間段的資訊。如果路由器的時間與日期不正確，可能會因為路由器時鐘不在該時間段內而拒絕有效證書。另請參閱 Certificates 配置。dont-verify-certificate - 不檢查遠端裝置的證書。接入點不會要求用戶端提供證書。no-certificates - 不使用證書。TLS 會話使用 2048 位匿名 Diffie-Hellman 金鑰交換建立。verify-certificate-with-crl - 與 verify-certificate 相同，但還會透過檢查證書吊銷列表來檢查證書是否有效。 |
| **ssid** (*string (0..32 chars)*；預設值： ) | SSID（服務集識別符號）是在信標中廣播的名稱，用於標識無線網路。 |
| **tx-chains** (*list of integer [0..3]*; 預設：**0**) | 傳輸時使用哪些天線。 |

### 通道組 {#channel-groups}

通道組設定允許配置與射頻通道相關的設定列表，例如射頻頻段、頻率、傳送功率、擴充套件通道和寬度。

通道組設定在 Channels 模板選單 `/caps-man/channels` 中配置

| 屬性 | 描述 |
| :-- | :-- |
| **band** (*2ghz-b \| 2ghz-b/g \| 2ghz-b/g/n \| 2ghz-onlyg \| 2ghz-onlyn \| 5ghz-a \| 5ghz-a/n \| 5ghz-onlyn*; 預設：) | 定義工作射頻頻段和模式，取自無線網路卡的硬體能力 |
| **comment** (*string*; 預設：) | 通道組模板的簡短描述 |
| **extension-channel** (*Ce \| Ceee \| eC \| eCee \| eeCe \| eeeC \| disabled*; 預設：) | 擴充套件通道配置。（例如 Ce = 擴充套件通道位於控制通道之上，eC = 擴充套件通道位於控制通道之下） |
| **frequency** (*integer [0..4294967295]*; 預設：) | AP 工作時的通道頻率值，單位為 MHz。 |
| **name** (*string*; 預設：) | 通道組模板的描述性名稱 |
| **tx-power** (*integer [-30..40]*; 預設：) | CAP 介面的傳送功率（針對整個介面而非單個鏈）單位為 dBm。不能設定為高於國家法規或介面允許的值。預設使用國家或介面允許的最大值。 |
| **width** (; 預設：) | 設定通道寬度，單位為 MHz。（例如 20、40） |
| **save-selected** (; 預設：**yes**) | 為 CAP 射頻儲存所選通道 - 在 CAP 重新連線到 CAPsMAN 後將選擇此通道並使用它，直到為此 CAP 完成通道重新最佳化。 |

### Datapath 配置 {#datapath-configuration}

Datapath 設定控制與資料轉發相關的方面。在 CAPsMAN 上，datapath 設定可在 datapath 模板選單 `/caps-man/datapath` 中配置，也可直接在使用 **datapath.** 字首設定的配置模板或介面選單中配置。

有 2 種主要轉發模式：

- 本地轉發模式，其中 CAP 在本地向無線介面轉發資料以及從無線介面轉發資料。
- Manager 轉發模式，其中 CAP 將透過無線接收的所有資料傳送到 CAPsMAN，並且僅透過無線傳送從 CAPsMAN 接收的資料。在此模式下，甚至用戶端到用戶端轉發也由 CAPsMAN 控制和執行。

轉發模式按介面配置——因此，如果一個 CAP 提供 2 個射頻介面，一個可以配置為在本地轉發模式下執行，另一個可以配置為在 Manager 轉發模式下執行。這同樣適用於 Virtual-AP 介面——每個介面可以具有與主介面或其他 Virtual-AP 介面不同的轉發模式。

大多數 datapath 設定僅在 Manager 轉發模式下使用，因為在本地轉發模式下，CAPsMAN 無法控制資料轉發。

有以下 datapath 設定：

- bridge -- 啟用時要將介面作為網橋埠新增到的網橋介面。
- bridge-cost -- 作為網橋埠新增時使用的網橋埠開銷。
- bridge-horizon -- 作為網橋埠新增時使用的網橋 horizon。
- client-to-client-forwarding -- 控制是否允許連線到該介面的無線用戶端之間進行用戶端到用戶端轉發；在本地轉發模式下，此功能由 CAP 執行，否則由 CAPsMAN 執行。
- local-forwarding -- 控制轉發模式。
- openflow-switch -- 啟用時要將介面作為埠新增到的 OpenFlow 交換器。
- vlan-id -- 如果 vlan-mode 啟用 VLAN 標記，則分配給介面的 VLAN ID。
- vlan-mode -- VLAN 標記模式指定是否應為介面分配 VLAN 標記（使所有接收的資料都打上 VLAN 標記，並允許介面僅傳送帶有指定標記的資料）。

### 本地轉發模式 {#local-forwarding-mode}

在此模式下，CAP 上的無線介面像普通介面一樣工作，並參與正常的資料轉發。無線介面將接受資料/將資料傳遞到 CAP 上的網路棧。CAPsMAN 不參與資料轉發，也不處理任何資料幀。它只控制介面配置和用戶端關聯過程。

CAP 上的無線介面會將其配置改為“啟用”，其狀態和一些相關引數（例如 mac-address、arp、mtu）將反映 CAPsMAN 上的介面。請注意，無線相關配置**不會**反映 CAPsMAN 實際應用的介面配置：

```
[admin@CAP] /interface/wireless> pr
Flags: X - disabled, R - running 
 0  R ;;; managed by CAPsMAN
      ;;; channel: 5180/20-Ceee/ac, SSID: master, local forwarding
      name="wlan2" mtu=1500 mac-address=00:03:7F:48:CC:07 arp=enabled 
      interface-type=Atheros AR9888 mode=ap-bridge ssid="merlin" 
      frequency=5240 band=5ghz-a/n channel-width=20/40mhz-eC scan-list=default
      ...
```

本地轉發模式下的 Virtual-AP 介面將顯示為已啟用的動態 Virtual-AP 介面：

```
[admin@CAP] /interface> pr
Flags: D - dynamic, X - disabled, R - running, S - slave 
 #     NAME                                TYPE         MTU L2MTU  MAX-L2MTU
 ...
 2  RS ;;; managed by CAPsMAN
       ;;; channel: 5180/20-Ceee/ac, SSID: master, local forwarding
       wlan2                               wlan        1500  1600
 3 DRS ;;; managed by CAPsMAN
       ;;; SSID: slave, local forwarding
       wlan6                               wlan        1500  1600
 ...
[admin@CAP] /interface> wireless pr   
Flags: X - disabled, R - running 
 ...
 2  R ;;; managed by CAPsMAN
      ;;; SSID: slave, local forwarding
      name="wlan6" mtu=1500 mac-address=00:00:00:00:00:00 arp=enabled 
      interface-type=virtual-AP master-interface=wlan2 
```

Virtual-AP 介面以動態方式新增這一事實在一定程度上限制了 CAP 上用於資料轉發的靜態配置可能性，例如為 Virtual-AP 介面分配地址。這不適用於主無線介面。

為克服此問題，可以在 CAP 上使用 static-virtual 設定，這將建立靜態虛擬介面而不是動態介面，並允許為這些介面分配 IP 配置。在應用來自 CAPsMAN 的配置時，使用 MAC 地址來記住每個靜態介面。如果兩個或更多靜態介面具有相同的 MAC 地址，則配置可能會以隨機順序應用。

為便於資料轉發配置，可以將 CAP 配置一個網橋，當介面由 CAPsMAN 啟用時，介面會自動作為埠新增到該網橋。這可以在 `/interface/wireless/cap` 選單中完成。

### Manager 轉發模式 {#manager-forwarding-mode}

在此模式下，CAP 將透過無線接收的所有資料傳送到 CAPsMAN，並且僅透過無線傳送從 CAPsMAN 接收的資料。CAPsMAN 完全控制資料轉發，包括用戶端到用戶端轉發。CAP 上的無線介面被停用，不參與網路：

```
 ...
 1 X  ;;; managed by CAPsMAN
      ;;; channel: 5180/20-Ceee/ac, SSID: master, manager forwarding
      name="wlan2" mtu=1500 mac-address=00:03:7F:48:CC:07 arp=enabled 
      interface-type=Atheros AR9888 mode=ap-bridge ssid="merlin" 
 ...
```

Virtual-AP 介面也會建立為“停用”，並且不參與 CAP 上的資料轉發。

### 訪問列表 {#access-list}

CAPsMAN 上的訪問列表是一個有序規則列表，用於允許/拒絕用戶端連線到 CAPsMAN 控制下的任何 CAP。當用戶端嘗試連線到由 CAPsMAN 控制的 CAP 時，CAP 會將該請求轉發給 CAPsMAN。作為註冊過程的一部分，CAPsMAN 會查詢訪問列表，以確定是否應允許該用戶端連線。訪問列表的預設行為是允許連線。

訪問列表規則會逐條處理，直到找到匹配規則。然後執行匹配規則中的操作。如果操作指定應接受用戶端，則接受該用戶端，並可能用訪問列表規則中指定的引數覆蓋其預設連線引數。

訪問列表在 `/caps-man/access-list` 選單中配置。訪問列表規則有以下引數：

- 用戶端匹配引數：
  - address - 用戶端 MAC 地址（或者，如果指定了 mask，則僅按掩碼檢查那些部分，因此要匹配 "D8:1C:79:6E:1E:FE" 中的廠商 D8，只需輸入一個虛假條目，例如 "D8:00:00:00:00:00"，然後按下一行使用掩碼）。
  - mask - 比較用戶端地址時應用的 MAC 地址掩碼。例如，使用 FF:00:00:00:00:00 僅匹配指定 MAC 地址的第一個八位組。在上面的示例中，無論輸入的 MAC 是什麼，它都只匹配第一個八位組。同樣，輸入 00:00:00:00:00:FF 將僅匹配假設 MAC "D8:1C:79:6E:1E:FE" 的最後一個八位組（FE）。因此，在 mac 行中，如果您要使用這樣的掩碼，只需輸入 00:00:00:00:00:FE。
  - interface - 可選介面，用於與用戶端實際連線的介面進行比較。
  - time - 規則匹配的每日時間和星期。
  - signal-range - 用戶端訊號必須落入的範圍，規則才會匹配。
- 操作引數 - 指定用戶端匹配時採取的操作：
  - accept - 接受用戶端。
  - reject - 拒絕用戶端。
  - query-radius - 查詢 RADIUS 伺服器，確定是否允許特定用戶端連線。
- 連線引數：
  - ap-tx-limit - 朝向用戶端方向的傳送速率限制。
  - client-tx-limit - 朝向 AP 方向的傳送速率限制（僅適用於 RouterOS 用戶端）。
  - client-to-client-forwarding - 指定是否允許將此用戶端收到的資料轉發到連線到同一介面的其他用戶端。
  - private-passphrase - 如果使用某種 PSK 認證演算法，則為此用戶端使用的 PSK 口令。
  - radius-accounting - 指定如果為此用戶端進行 RADIUS 認證，是否應使用 RADIUS 流量計費。
  - vlan-mode - VLAN 標記模式指定來自用戶端的流量是否應打上標記（並在發往用戶端時取消標記）。
  - vlan-id - 進行 VLAN 標記時使用的 VLAN ID。

### 登錄檔 {#registration-table}

登錄檔包含連線到由 CAPsMAN 控制的射頻的用戶端列表，可在 `/caps-man/registration-table` 選單中檢視：

```
[admin@CM] /caps-man> registration-table print
 # INTERFACE                   MAC-ADDRESS       UPTIME                RX-SIGNAL
 0 cap1                        00:03:7F:48:CC:0B 1h38m9s210ms                -36
```

## 示例 {#examples}

### 使用主介面和從介面的基本配置 {#basic-configuration-with-master-and-slave-interface}

建立用於 WPA2 PSK 的安全模板，不指定口令：

```
[admin@CM] /caps-man/security>add name="wpa2psk" authentication-types=wpa2-psk encryption=aes-ccm
```

建立供主介面使用的配置模板：

- 在配置中指定 WPA2 口令。
- 在配置中指定通道設定。

```
[admin@CM] /caps-man/configuration> add name=master-cfg ssid=master security=wpa2psk
security.passphrase=12345678 channel.frequency=5180 channel.width=20 channel.band=5ghz-a
```

建立供虛擬 AP 介面使用的配置模板：

- 在配置中指定不同的 WPA2 口令。

```
[admin@CM] /caps-man/configuration> add name=slave-cfg ssid=slave security=wpa2psk
security.passphrase=87654321
```

建立一條預配規則，匹配任何射頻，並使用 master-cfg 和 slave-cfg 建立動態介面：

```
[admin@CM] /caps-man/provisioning> add action=create-dynamic-enabled master-configuration=master-cfg
slave-configurations=slave-cfg
```

現在，當某個 AP 連線並被預配時，將建立 2 個動態介面（一個主介面和一個從介面）：

```
[admin@CM] /caps-man/interface> print detail 
Flags: M - master, D - dynamic, B - bound, X - disabled, I - inactive, R - running 
 0 MDB  name="cap1" mtu=1500 l2mtu=2300 radio-mac=00:0C:42:1B:4E:F5 master-interface=none 
        configuration=master-cfg 

 1  DB  name="cap2" mtu=1500 l2mtu=2300 radio-mac=00:00:00:00:00:00 master-interface=cap1 
        configuration=slave-cfg 
```

假設有一個不支援所配置頻率的 AP 連線進來，並且無法進入工作狀態：

```
[admin@CM] /caps-man/interface> pr
Flags: M - master, D - dynamic, B - bound, X - disabled, I - inactive, R - running 
 #      NAME                                 RADIO-MAC         MASTER-INTERFACE                               
 0 MDB  ;;; unsupported band or channel
        cap3                                 00:0C:42:1B:4E:FF none    
 ...
```

我們可以在介面設定中覆蓋此特定射頻的通道設定，而不影響 master-cfg 模板：

```
[admin@CM] /caps-man/interface> set cap3 channel.frequency=2142 channel.band=2ghz-b/g
```

允許特定 MAC 地址範圍匹配訪問列表，例如匹配所有 Apple 裝置：

```
[admin@CM] /caps-man/access-list> add mac-address=18:34:51:00:00:00 mac-address-mask=FF:FF:FF:00:00:00 action=accept
```

配置 DHCP Server Option 138，以在 CAP 板上設定 CAPsMAN 地址

```
[admin@CM] /ip/dhcp-server/network/set <network-id> caps-manager=<capsman-server-ip>
```

DHCP 用戶端將在 `/ip/dhcp-client/print detail` 中看到此 CAPsMAN IP。

### 使用證書的配置 {#configuration-with-certificates}

您可能希望在 CAPsMAN 中配置證書，以使用 *Require Peer Certificate* 和 *Lock To Caps Man* 等選項。這些選項可提高 CAPsMAN 網路的安全性，並在某些情況下提高穩定性。沒有特定證書時，CAP 無法連線到 CAPsMAN，反之亦然。

#### 快速簡便配置 {#fast-and-easy-configuration}

這是在 CAPsMAN 設定中使用證書的基本配置。此示例假設您的 CAPsMAN 和 CAP 上已有基本配置。最好在不會持續增長的 CAPsMAN 網路中使用此配置。有關更多詳細資訊，請閱讀 [CAP 到 CAPsMAN 的連線](#cap-to-capsman-connection)。

**CAPsMAN 裝置：**

在 CAPsMAN Manager 選單中，將 *Certificate* 和 *CA Certificate* 設定為 *auto*：

```
/caps-man/manager
set ca-certificate=auto certificate=auto
```

列印輸出：

```
[admin@CAPsMAN] /caps-man/manager/print 
                   enabled: yes
               certificate: auto
            ca-certificate: auto
              package-path: 
            upgrade-policy: none
  require-peer-certificate: no
     generated-certificate: CAPsMAN-D4CA6D987C26
  generated-ca-certificate: CAPsMAN-CA-D4CA6D987C26
```

CAPsMAN 裝置將首先生成 *CA-Certificate*，然後生成依賴於 *CA-Certificate* 的 *Certificate*。

**CAP 裝置：**

在 CAP 配置中設定為 *request* 證書：

```
/interface/wireless/cap
set certificate=request
```

CAP 將連線到 CAPsMAN 並請求證書。CAP 將從 CAPsMAN 接收 *CA-Certificate*，並建立另一個證書供 CAP 使用。

**結果**

在 CAP 裝置的 CAP 選單中，*Requested Certificate* 已設定：

```
[admin@CAP] /interface/wireless/cap/print
                            enabled: yes
                         interfaces: wlan1
                        certificate: request
                   lock-to-caps-man: no
               discovery-interfaces: ether1
                 caps-man-addresses: 
                     caps-man-names: 
  caps-man-certificate-common-names: 
                             bridge: none
                     static-virtual: no
         -->  requested-certificate: CAP-D4CA6D7F45BA  <--
```

此外，還獲得兩個證書，可在 *Certificate* 選單中看到：

```
[admin@CAP] > /certificate/print 
Flags: K - private-key, D - dsa, L - crl, C - smart-card-key, A - authority, I - issued, R - revoked, E - expired, T - trusted 
 #          NAME              COMMON-NAME              SUBJECT-ALT-NAME                                           FINGERPRINT             
 0     A  T _0                CAPsMAN-CA-D4CA6D987C26                                                             383e63d7b...
 1 K        CAP-D4CA6D7F45BA  CAP-D4CA6D7F45BA                                                                    d495d1a94...
```

在 CAPsMAN 裝置的 Certificate 選單中會建立三個證書：CAPsMAN 和 CAPsMAN-CA 證書，以及頒發給 CAP 的證書：

```
[admin@CAPsMAN] > /certificate/print 
Flags: K - private-key, D - dsa, L - crl, C - smart-card-key, A - authority, I - issued, R - revoked, E - expired, T - trusted 
 #          NAME                     COMMON-NAME              SUBJECT-ALT-NAME                                    FINGERPRINT         
 0 K   A  T CAPsMAN-CA-D4CA6D987C26  CAPsMAN-CA-D4CA6D987C26                                                      383e63d7b...
 1 K    I   CAPsMAN-D4CA6D987C26     CAPsMAN-D4CA6D987C26                                                         02b0f7ff4...
 2      I   issued_1                 CAP-D4CA6D7F45BA                                                             d495d1a94...
```

**另外**

如果您希望僅允許具有有效證書的 CAP 連線到此 CAPsMAN，可以在 CAPsMAN 裝置上將 *Require Peer Certificate* 設定為 *yes*：

```
/caps-man/manager
set require-peer-certificate=yes
```

但是，當您想向 CAPsMAN 網路新增新的 CAP 裝置時，必須先將此選項設定為 *no*，然後在 CAP 獲得證書後再設回 *yes*。每次更改此選項時，CAPsMAN 都會丟棄所有動態介面，CAP 將再次嘗試連線。

如果您想將 CAP 鎖定到特定 CAPsMAN，並確保它不會連線到其他 CAPsMAN，應將 *Lock To CAPsMAN* 選項設定為 *yes*。此外，您可以透過在 CAP 裝置上設定 *CAPsMAN Certificate Common Names* 來指定要鎖定到的 CAPsMAN：

```
/interface/wireless/cap
set lock-to-caps-man=yes
set caps-man-certificate-common-names=CAPsMAN-D4CA6D987C26
```

#### 手動證書並使用 SCEP 簽發 {#manual-certificates-and-issuing-with-scep}

透過此示例，您可以為 CAPsMAN 建立自己的證書，並控制向 CAP 頒發證書的過程。此配置在大型且不斷增長的 CAPsMAN 網路中很有用。根據您的環境和需求，此示例的許多部分可以採用不同方式完成。此時，瞭解一些關於[證書](../../../authentication-authorization-accounting/certificates.md)及其[應用](../../../authentication-authorization-accounting/certificates.md#sign-certificate)的知識可能會有幫助。

**CAPsMAN 裝置：**

在 *Certificate* 選單中為 CA 證書和 CAPsMAN 伺服器證書新增證書模板：

```
/certificate
add name=CA-temp common-name=CA
add name=CAPsMAN-temp common-name=CAPsMAN
```

現在*簽署*證書模板。首先*簽署* CA 證書，並使用 CAPsMAN 裝置 IP 作為 *CA CRL Host*：

```
/certificate
sign CA-temp ca-crl-host=10.5.138.157 name=CA
sign CAPsMAN-temp ca=CA name=CAPsMAN
```

或者，前兩個步驟可以透過 CAPsMAN Manager 選單中 *Certificate* 和 *CA-Certificate* 選項的 auto 設定完成，請參閱[快速簡便配置](#fast-and-easy-configuration)。

*匯出* CA 證書。您將需要在 CAP 裝置上*匯入*它。您可以使用 *Download -> Drag&Drop* 到 CAP 裝置；在此示例中，稍後從 CAP 裝置使用 *fetch* 命令。建議使用較長的口令——如果口令落入錯誤的人手中，較長的口令需要更長時間才能破解：

```
/certificate
export-certificate CA export-passphrase=thelongerthebetterpassphrase
```

建立一個 *SCEP 伺服器*，用於向 CAP 裝置頒發和授予證書：

```
/certificate/scep-server
add ca-cert=CA path=/scep/CAPsMAN
```

在 CAPsMAN Manager 選單中設定證書，並將 *Require Peer Certificate* 設定為 yes：

```
/caps-man/manager
set ca-certificate=CA certificate=CAPsMAN
set require-peer-certificate=yes
```

此時，只有具有有效證書的 CAP 才能連線。

**CAP 裝置**

將 CAPsMAN 裝置上匯出的 CA 證書下載到 CAP 裝置。此示例中使用 *fetch*；不過還有許多其他方式：

```
/tool/fetch address=10.5.138.157 src-path=cert_export_CA.crt user=admin password="123" mode=ftp
```

在 *Certificate* 選單中匯入來自 CAPsMAN 裝置的 CA 證書：

```
/certificate> import file-name=cert_export_CA.crt passphrase=thelongerthebetterpassphrase
```

為 CAP 新增證書模板：

```
/certificate
add name=CAP1 common-name=CAP1
```

請求 CAPsMAN 裝置使用 SCEP 為此證書授予金鑰：

```
/certificate
add-scep template=CAP1 scep-url="https://10.5.138.157/scep/CAPsMAN"
```

您將需要返回 CAPsMAN 裝置為此證書授予金鑰。

在 CAP 選單中設定剛剛建立的證書：

```
/interface/wireless/cap
set certificate=CAP1
```

**CAPsMAN 裝置：**

返回 CAPsMAN 裝置，在 *Certificate Request* 選單中為 CAP 證書授予金鑰：

```
/certificate/scep-server/requests
grant numbers=0
```

**結果**

現在 CAP 應該能夠連線到 CAPsMAN。可在 *CAPsMAN interfaces* 中檢視它是否連線。在 CAPsMAN 裝置的 *Certificate* 選單中可以看到三個證書：CA、CAPsMAN，以及頒發給 CAP 的證書：

```
[admin@CAPsMAN] /certificate/print 
Flags: K - private-key, D - dsa, L - crl, C - smart-card-key, A - authority, I - issued, R - revoked, 
E - expired, T - trusted 
 #          NAME        COMMON-NAME      SUBJECT-ALT-NAME                                   FINGERPRINT     
 0 K L A  T CA          CA                                                                  752775b457a37...
 1 K   A    CAPsMAN     CAPsMAN                                                             12911ba445b3b...
 2      I   issued_1    CAP1                                                                5b9a52b6ce3fb...
```

在 CAP 裝置的 *Certificate* 選單中可以看到兩個已獲取的證書：

```
[admin@CAP1] /interface/wireless> /certificate/print 
Flags: K - private-key, D - dsa, L - crl, C - smart-card-key, A - authority, I - issued, R - revoked, 
E - expired, T - trusted 
 #          NAME        COMMON-NAME      SUBJECT-ALT-NAME                                   FINGERPRINT     
 0   L A  T cert_exp... CA                                                                  752775b457a37...
 1 K      T CAP1        CAP1                                                                5b9a52b6ce3fb...
```
