---
sidebar_key: "authentication-authorization-accounting/certificates"
sidebar_position: 1
title: "證書"
sidebar_label: "證書"
description: "本頁介紹 MikroTik RouterOS 中的 Certificate management 選單，涵蓋證書模板建立、金鑰大小和用途等配置屬性，以及包括 ACME 用戶端整合在內的證書管理。"
tags:
  - 'certificate'
  - 'crl'
  - 'trust-store'
  - 'letsencrypt'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/certificates
captured_at: '2026-11-04T11:27:02+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#overview}

**子選單：** `/certificate`

通用選單用於管理證書、新增模板、簽發證書，以及管理 CRL 和 SCEP 用戶端。

### 證書模板 {#certificate-template}

證書模板用於為簽發準備所需的證書。

證書籤發完成或執行證書請求命令後，證書模板會立即被刪除

```ros
/certificate
add name=CA-Template common-name=CAtemp key-usage=key-cert-sign,crl-sign
add name=Server common-name=server
add name=Client common-name=client
```

列印證書：

```ros
[admin@4k11] /certificate> print detail 
Flags: K - private-key; L - crl; C - smart-card-key; A - authority; I - issued, R - revoked; E - expired; T - trusted 
 0         name="CA-Template" key-type=rsa common-name="CAtemp" key-size=2048 subject-alt-name="" days-valid=365 key-usage=key-cert-sign,crl-sign 

 1         name="Server" key-type=rsa common-name="server" key-size=2048 subject-alt-name="" days-valid=365 
           key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client 

 2         name="Client" key-type=rsa common-name="client" key-size=2048 subject-alt-name="" days-valid=365 
           key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client 
```

#### 證書模板屬性 {#certificate-template-properties}

在建立證書模板的過程中，可以定義和配置多個引數以滿足特定需求。

| 屬性 | 描述 |
| :-- | :-- |
| **common-name** (*string*) | 證書通用名稱 |
| **copy-from**(*name*) | 從中複製通用設定的證書名稱 |
| **country** (*string*) | 證書頒發者國家 |
| **days-valid** (*days* Default: **365**) | 簽發後證書的有效天數 |
| **digest-algorithm** (*md5 \| sha1 \| sha256 \| sha384 \| sha512* Default: **sha256**) | 用於簽發證書的雜湊演算法。 |
| **key-size** (*1024* \| *1536* \| *2048* \| *4096* \| *8192* \| *prime256v1* \| *secp384r1* \| *secp521r1* Default: **2048**) | 證書公鑰大小 |
| **key-usage** (*code-sign* \| *crl-sign* \| *decipher-only* \| *dvcs* \| *encipher-only* \| *key-cert-sign* \| *ocsp-sign* \| *tls-client* \| *content-commitment* \| *data-encipherment* \| *digital-signature* \| *email-protect* \| *key-agreement* \| *key-encipherment* \| *timestamp* \| *tls-server* Default: **digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client)** | 證書用途 |
| **locality** (*string*) | 證書頒發者所在地 |
| **name** (*string*) | 證書名稱 |
| **organization** (*string*) | 證書頒發者組織 |
| **state** (*string*) | 證書頒發者州/省 |
| **subject-alt-name** (*DNS: \| IP: \| email:*) | 證書主題備用名稱 |
| **trusted** (*no \| yes*) | 是否信任證書。若為 *yes*，該證書將用於主機證書驗證。 |
| **trust-store**(*all* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging* Default: **all**) | 指定哪些服務可以使用特定證書進行證書驗證或信任鏈建立（www、sstp）。 |
| **unit** (*string*) | 證書頒發者組織單位 |

### 證書屬性 {#certificate-properties}

對於已簽發的證書，大多數屬性為只讀，但 *name*、*trusted* 和 *trust-store* 除外。

| 屬性 | 描述 |
| :-- | :-- |
| **acme-status** *(string)* | ACME 用戶端狀態 |
| **common-name** (*string*) | 證書通用名稱 |
| **copy-from**(*name*) | 從中複製通用設定的證書名稱 |
| **country** (*string*) | 證書頒發者國家 |
| **days-valid** (*days*) | 簽發後證書的有效天數 |
| **digest-algorithm** (*md5 \| sha1 \| sha256 \| sha384 \| sha512*) | 用於簽發證書的雜湊演算法 |
| **directory-url** *(string)* | ACME 用戶端目錄 URL |
| **domain-names** *(string)* | ACME 用戶端使用的域名 |
| **key-size** (*1024* \| *1536* \| *2048* \| *4096* \| *8192* \| *prime256v1* \| *secp384r1* \| *secp521r1*) | 證書公鑰大小 |
| **key-usage** (*code-sign* \| *crl-sign* \| *decipher-only* \| *dvcs* \| *encipher-only* \| *key-cert-sign* \| *ocsp-sign* \| *tls-client* \| *content-commitment* \| *data-encipherment* \| *digital-signature* \| *email-protect* \| *key-agreement* \| *key-encipherment* \| *timestamp* \| *tls-server*) | 證書用途 |
| **locality** (*string*) | 證書頒發者所在地 |
| **organization** (*string*) | 證書頒發者組織 |
| **revoked** *(date)* | 證書吊銷時間（僅適用於在特定裝置上籤發並吊銷的證書） |
| **state** (*string*) | 證書頒發者州/省 |
| **subject-alt-name** (*DNS \| IP \| email*) | 證書主題備用名稱 |
| **trusted** (*no \| yes*) | 是否信任證書。若為 *yes*，該證書將用於主機證書驗證。 |
| **trust-store**(*all* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging*) | 指定哪些服務可以使用特定證書進行證書驗證或信任鏈建立（www、sstp）。 |
| **unit** (*string*) | 證書頒發者組織單位 |
| **serial-number** (*string*) | 證書序列號 |
| **fingerprint** (*string*) | 證書指紋 |
| **akid** (*string*) | 證書頒發機構 ID |
| **skid** (*string*) | 證書主題 ID |
| **issuer** (*string*) | 證書頒發機構 |
| **invalid-before** *(date)* | 證書尚未生效的日期和時間（有效期開始日期）。 |
| **invalid-after** *(date)* | 證書不再有效的日期和時間（到期日期）。 |
| **expires-after** *(time)* | 距離到期剩餘時間 |
| **key-type** (*string*) | 私鑰型別 |
| **ca** *(string)* | CA 證書名稱（僅對在特定裝置上籤發的證書顯示） |

:::warning
如果刪除 CA 證書，鏈中所有已簽發的證書也會被刪除。
:::

### 簽發證書 {#sign-certificate}

證書應當被簽發。在以下示例中，我們將簽發證書，併為伺服器證書新增 CRL URL：

```ros
/certificate 
sign CA-Template 
sign Client      
sign Server ca-crl-host=192.168.88.1 name=ServerCA

```

檢查證書是否已簽發：

```ros
[admin@MikroTik] /certificate> print
Flags: K - private-key; L - crl; A - authority; T - trusted
Columns: NAME, COMMON-name, FINGERPRINT
#        NAME         COMMON  FINGERPRINT                                                     
0  K AT  CA-Template  CAtemp  0c7aaa7607a4dde1bbf33deaae6be7bac9fe4064ba47d64e8a73dcefad6cfc38
1  K AT  Client       client  b3ff25ecb166ea41e15733a7493003f3ea66310c10390c33e98fe32364c3659f
2  KLAT  ServerCA     server  152b88c9d81f4b765a59e2302e01efd1fbf11ceeed6e59f4974e87787a5bb980

```

影片示例請點選[此處。](http://youtube.com/watch?v=i2A3YIQKfwY)

:::warning
金鑰簽發過程所需的時間取決於特定證書的金鑰大小。當金鑰大小為 4k 或更大時，在效能較弱的 CPU 裝置上籤發該證書可能需要相當長的時間。
:::

### 匯出證書 {#export-certificate}

可以以兩種格式匯出帶金鑰的用戶端證書和 CA 證書 —— PEM 或 PKCS12。

| 屬性 | 描述 |
| :-- | :-- |
| **export-passphrase** (*string* Default: **none**) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於匯出證書私鑰加密的密碼短語。 |
| **file-name** (*string* Default: **cert\_export\_[certificate name].crt/key/pkcs12**) | 匯出的證書檔名。 |
| **type** (*pem \| pkcs12* Default: **pem**) | 匯出的證書型別。  若為 PEM，證書將以 CRT 副檔名匯出；如果指定了 export-passphrase，還會匯出一個加密的私鑰 KEY 檔案。  若為 PKCS12，證書將以 P12 副檔名匯出；如果指定了 export-passphrase，匯出的證書將包含加密的私鑰。PKCS12 檔案使用 AES 加密。 |

```ros
/certificate 
export-certificate CA-Template 
export-certificate ServerCA export-passphrase=yourpassphrase
export-certificate Client export-passphrase=yourpassphrase
```

匯出的證書可在 */file* 部分檢視：

```ros
[admin@MikroTik] > file print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME                         TYPE        SIZE  CREATION-TIME       
0  skins                        directory         2019-01-19 00:00:04
1  flash                        directory         2019-01-19 01:00:00
2  pub                          directory         2019-01-19 02:42:16
3  cert_export_CA-Template.crt  .crt file   1119  2019-01-19 04:15:21
4  cert_export_ServerCA.crt     .crt file   1229  2019-01-19 04:15:42
5  cert_export_ServerCA.key     .key file   1858  2019-01-19 04:15:42
6  cert_export_Client.crt       .crt file   1164  2019-01-19 04:15:55
7  cert_export_Client.key       .key file   1858  2019-01-19 04:15:55
```

:::warning
匯出證書需要 "sensitive" 使用者策略。
:::

### 匯入證書 {#import-certificate}

要匯入證書，必須使用某種檔案上傳方法將證書上傳到裝置。

證書必須作為檔案匯入。

支援 PEM、DER、CRT、PKCS12 格式。PKCS12 匯入支援 AES 和 3DES 解密。

| 屬性 | 描述 |
| :-- | :-- |
| **name** (*string* Default: **file-name\_number**) | 將在證書管理器中顯示的證書名稱 |
| **file-name** (*string*) | 將被匯入的檔名 |
| **passphrase** (*string* Default: **none**) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 檔案密碼短語（如果有） |
| **trusted** (*yes \| no* Default: yes) | 為匯入的證書新增 *trusted* 標誌 |
| **trust-store**(*all* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging*  Default: **all**) | 指定哪些服務可以使用特定證書進行證書驗證或信任鏈建立（www、sstp）。 |

```ros
[admin@MikroTik] > /certificate/import file-name=certificate_file_name name=name_example passphrase=file_passphrase
     certificates-imported: 2
     private-keys-imported: 1
            files-imported: 1
       decryption-failures: 0
  keys-with-no-certificate: 0

[admin@MikroTik] > /certificate/print 
Flags: K - PRIVATE-KEY; T - TRUSTED
Columns: NAME, COMMON-NAME
#    NAME            COMMON-NAME                                                  
0 KT name_example    cert    
1  T name_example_1  ca   
```

### CRL {#crl}

RouterOS 支援證書吊銷列表（CRL）檢查。

預設情況下不使用 CRL，也不會驗證證書的吊銷狀態。

在[證書設定](#settings)中啟用 `crl-use=yes`，可讓系統使用其 CRL 驗證鏈中的每個證書；設定 `crl-download=yes` 可讓 RouterOS 自動下載並更新 CRL。

可以透過提供 CRL URL 手動新增 CRL，也可以在匯入包含 CRL 分發點的證書時動態新增。

| 屬性 | 描述 |
| :-- | :-- |
| **akid** (*string*) | CRL 頒發機構 ID |
| **cert**(*string*) | 從中新增 CRL 分發點的證書（來自證書儲存） |
| **dynamic** (*flag*) | CRL 是否為動態新增 |
| **expired** (*flag*) | CRL 是否已過期 |
| **fingerprint** (*string*) | CRL 指紋 |
| **Invalid** (*flag*) | CRL 是否無效（未更新） |
| **last-update** (*date*) | 上次 CRL 更新的日期和時間 |
| **next-update** (*date*) | 下次 CRL 更新的日期和時間 |
| **num** (*integer*) | CRL 編號 |
| **removed** (*integer*) | 已吊銷證書的數量 |
| **signature** (*string*) | CRL 簽名 |
| **url** (*string*) | CRL 地址 |
| **num** (*integer*) | CRL 編號 |

### 設定 {#settings}

`/certificate/settings` 允許配置[證書吊銷列表](#crl)和[內建信任儲存](#built-in-trust-store-authorities)設定。

| 屬性 | 描述 |
| :-- | :-- |
| **builtin-trust-store** (*all* \| *default* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging* \| *untrusted* Default: **default**) | 可使用[內建信任儲存機構](#built-in-trust-store-authorities)進行證書驗證的服務。  當前預設值：fetchmqttemailnetwatchcontainerloradnswwwreverse-proxy |
| **crl-download** (*yes \| no* Default: **no**) | 是否自動下載/更新 CRL |
| **crl-store** (*ram \| system* Default: **ram**) | 儲存下載的 CRL 資訊的位置  對於 "trusted=yes" 的證書，將使用 http 協定每小時自動續訂 CRL（目前不支援 ldap 和 ftp） |
| **crl-use** (*yes \| no* Default: **no**) | 是否使用 CRL |

:::warning
如果將 *`/certificate/settings/set crl-use`* 設定為 *`yes`*，RouterOS 會檢查證書鏈中每個證書的 CRL，因此應將完整的證書鏈安裝到裝置中 —— 從根 CA、中間 CA（如果有）開始，一直到用於特定服務的證書。
:::

匯入根證書的[示例](http://youtube.com/watch?v=q9oMO3_jvBU)。

## ACME 用戶端 {#acme-client}

ACME 用戶端透過 ACME 自動獲取和續訂多個 TLS 證書。

要透過 CLI 新增新的 ACME 用戶端，請使用命令 `/certificate/add-acme`。

現有的 ACME 用戶端會顯示在證書檢視中，並標記為 `a`（acme-manage）標誌。

域名必須解析到路由器，且 TCP 埠 80 必須可從 WAN 訪問（使用 HTTP-01 質詢）。對於 IP Cloud 的 `<id>.sn.mynetname.net` 域名，則改用 DNS-01 質詢。

當證書有效期過去 80% 時，證書會自動續訂。

如果在初始設定期間未能獲取到證書，則必須新增一個新的 ACME 用戶端。

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **directory-url** (*string*) | ACME 目錄 URL |
| **domain-names** (*string*) | 以逗號分隔的域名列表 |
| **eab-hmac-key** (*string*) | 用於 ACME 外部賬戶繫結的 HMAC 金鑰 |
| **eab-kid** (*string*) | 金鑰識別符號 |
| **name** (*string*) | ACME 用戶端名稱 |

### 手動續訂 ACME {#manual-acme-renewal}

要手動觸發 ACME 證書續訂：

```ros
/certificate/acme-renew [name]
```

例如：

```ros
/certificate/acme-renew numbers=0
```

### Let's Encrypt 證書 {#lets-encrypt-certificate}

要獲取可自動續訂的 Let's Encrypt 證書，必須使用 `domain-names` 引數手動提供域名：

```ros
/certificate/add-acme domain-names=router.example.com
```

要為 [雲](../network-management/cloud/index.md#ddns) 名稱（例如 `example.sn.mynetname.net`）生成 Let's Encrypt 證書，請將 `/ip/cloud` 選單中的 `dns-name` 作為域名提供，或使用 `[/ip/cloud/get dns-name]` 內聯讀取：

```ros
/certificate/add-acme domain-names=[/ip/cloud/get dns-name]
```

:::info
如果未提供 `directory-url`，則使用 Let's Encrypt 目錄。
:::

:::note
當證書的更新正在進行時，無法刪除該證書。如果 ACME 證書續訂失敗並一直處於錯誤狀態，則 `remove` 命令會因 `cannot remove certificate while acme update is in progress` 而失敗。請重啟路由器，然後再刪除該證書。
:::

## SCEP {#scep}

SCEP 使用 HTTP 協定和 base64 編碼的 GET 請求。大多數請求不進行身份驗證和加密，但在必要時可以保護重要請求（使用收到的公鑰進行加密或簽名）。

RouterOS 中的 SCEP 用戶端將：

- 從 CA 伺服器或 RA（如果使用）獲取 CA 證書。
- 使用者應比較 CA 證書的指紋，或確認其來自正確的伺服器。
- 使用臨時金鑰生成自簽名證書。
- 向伺服器傳送證書請求。
- 如果伺服器以狀態 x 響應，用戶端會持續請求，直到伺服器傳送錯誤或批准。

SCEP 伺服器僅支援簽發一個證書。RouterOS 還支援 renew 和 next-ca 選項：

- renew - 可以使用同一 CA 自動續訂舊證書。
- next-ca - 可以將當前 CA 證書更換為新的 CA 證書。

用戶端會輪詢伺服器以獲取任何變更；如果伺服器通告 next-ca 可用，用戶端可以請求下一個 CA，或者等到當前 CA 即將過期時再請求 next-ca。

預設情況下，如果伺服器通告支援 POST、AES 和 SHA256，RouterOS 用戶端會嘗試使用這些方式。如果不支援上述演算法，則用戶端會嘗試使用 3DES、DES 以及 SHA1、MD5。

SCEP 證書在其有效期過去 3/4 時會被續訂。

## 內建信任儲存機構 {#built-in-trust-store-authorities}

RouterOS 包含一個內建根證書頒發機構列表，特定服務可以使用這些機構進行主機證書驗證。

SMIPS 裝置具有[精簡的內建 CA 信任儲存](#smips-built-in-cas)。

可使用內建根證書頒發機構的服務列表見[設定](#settings)部分。

可以在使用 [DoH](../network-management/dns.md) 的同時進行證書驗證，而無需手動匯入相關的根證書。

內建根證書頒發機構列表可在 System → Certificates → Built In CA 中訪問，也可透過 `/certificate/builtin/` 訪問。

### 內建 CA 列表 {#list-of-built-in-cas}

以下內建 CA 列表在所有架構上可用（SMIPS 除外）。

| 組織 | 通用名稱 | 主體 ID |
| :-- | :-- | :-- |
| Amazon | Amazon Root CA 1 | `8418CC8534ECBC0C94942E08599CC7B2104E0A08` |
| DigiCert Inc | DigiCert Assured ID Root CA | `45EBA2AFF492CB82312D518BA7A7219DF36DC80F` |
| DigiCert Inc | DigiCert Assured ID Root G2 | `CEC34AB99955F2B8DB60BFA97EBD56B59736A7D6` |
| DigiCert Inc | DigiCert Assured ID Root G3 | `CBD0BDA9E1980551A14D37A28379CE8D1D2AE484` |
| DigiCert Inc | DigiCert Global Root CA | `03DE503556D14CBB66F0A3E21B1BC397B23DD155` |
| DigiCert Inc | DigiCert Global Root G2 | `4E2254201895E6E36EE60FFAFAB912ED06178F39` |
| DigiCert Inc | DigiCert Global Root G3 | `B3DB48A4F9A1C5D8AE3641CC1163696229BC4BC6` |
| DigiCert Inc | DigiCert High Assurance EV Root CA | `B13EC36903F8BF4701D498261A0802EF63642BC3` |
| DigiCert, Inc. | DigiCert TLS ECC P384 Root G5 | `C151455059AB3EE72C5AFA2022120780887C116A` |
| DigiCert, Inc. | DigiCert TLS RSA4096 Root G5 | `51331CED3640AF17D325CD6968F2AF4E233EB341` |
| DigiCert Inc | DigiCert Trusted Root G4 | `ECD7E382D2715D644CDF2E673FE7BA98AE1C0F4F` |
| GlobalSign | GlobalSign | `3DE629489BEA07CA21444A26DE6EDED283D09F59` |
| GlobalSign nv-sa | GlobalSign Root CA | `607B661A450D97CA89502F7D04CD34A8FFFCFD4B` |
| GlobalSign | GlobalSign | `8FF04B7FA82E4524AE4D50FA639A8BDEE2DD1BBC` |
| GlobalSign | GlobalSign | `AE6C05A39313E2A2E7E2D71CD6C7F07FC86753A0` |
| GlobalSign nv-sa | GlobalSign Root E46 | `310A908FB6C69DD2444B80B5A2E61FB1124F1B95` |
| GlobalSign nv-sa | GlobalSign Root R46 | `035CAB738187A8CCB0A6D594E2369649FF05992C` |
| The Go Daddy Group, Inc. | | `D2C4B0D291D44C1171B361CB3DA1FEDDA86AD4E3` |
| GoDaddy.com, Inc. | Go Daddy Root Certificate Authority - G2 | `3A9A8507106728B6EFF6BD05416E20C194DA0FDE` |
| Sectigo Limited | Sectigo Public Server Authentication Root E46 | `D122DA4C59F14B5F2638AA9DD6EEEB0DC3FBA961` |
| Sectigo Limited | Sectigo Public Server Authentication Root R46 | `5673586495F9921AB0122A046279A14015882149` |
| The USERTRUST Network | USERTrust ECC Certification Authority | `3AE10986D4CF19C29676744976DCE035C663639A` |
| The USERTRUST Network | USERTrust RSA Certification Authority | `5379BF5AAA2B4ACF5480E1D89BC09DF2B20366CB` |
| 網際網路安全研究小組 | ISRG Root X1 | `79B459E67BB6E5E40173800888C81A58F6E99B6E` |
| 網際網路安全研究小組 | ISRG Root X2 | `7C4296AEDE4B483BFA92F89E8CCF6D8BA9723795` |
| ISRG | Root YE | `A3C8265A8EA14CD03563FC9B23C83AAE56F34F56` |
| ISRG | Root YR | `DEE75B60D0226D40287D3F0D01FEA4B552B45194` |

### SMIPS 內建 CA {#smips-built-in-cas}

SMIPS 裝置具有精簡的內建 CA 信任儲存：

| 組織 | 通用名稱 | 主體 ID |
| :-- | :-- | :-- |
| DigiCert Inc | DigiCert Global Root G2 | `4E2254201895E6E36EE60FFAFAB912ED06178F39` |
| 網際網路安全研究小組 | ISRG Root X1 | `79B459E67BB6E5E40173800888C81A58F6E99B6E` |
| 網際網路安全研究小組 | ISRG Root X2 | `7C4296AEDE4B483BFA92F89E8CCF6D8BA9723795` |
| ISRG | Root YE | `A3C8265A8EA14CD03563FC9B23C83AAE56F34F56` |
| ISRG | Root YR | `DEE75B60D0226D40287D3F0D01FEA4B552B45194` |
