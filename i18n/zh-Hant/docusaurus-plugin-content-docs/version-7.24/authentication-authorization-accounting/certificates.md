---
title: "憑證"
description: "本頁說明 MikroTik RouterOS 中的 Certificate 管理選單，涵蓋憑證範本建立、金鑰大小與用途等設定屬性，以及包含 ACME 用戶端整合在內的憑證管理。"
tags:
  - 'certificate'
  - 'crl'
  - 'trust-store'
  - 'letsencrypt'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/certificates
captured_at: '2026-11-28T10:19:39.818Z'
pagination_prev: "authentication-authorization-accounting"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

## 概觀 {#overview}

**子選單：** `/certificate`

一般選單用於管理憑證、新增範本、簽發憑證，以及管理 CRL 與 SCEP Clients。

### 憑證範本 {#certificate-template}

憑證範本用於準備要簽署的所需憑證。

憑證範本會在憑證簽署完成或執行 certificate request 指令後立即刪除。

```ros
/certificate
add name=CA-Template common-name=CAtemp key-usage=key-cert-sign,crl-sign
add name=Server common-name=server
add name=Client common-name=client
```

若要列印憑證：

```ros
[admin@4k11] /certificate> print detail 
Flags: K - private-key; L - crl; C - smart-card-key; A - authority; I - issued, R - revoked; E - expired; T - trusted 
 0         name="CA-Template" key-type=rsa common-name="CAtemp" key-size=2048 subject-alt-name="" days-valid=365 key-usage=key-cert-sign,crl-sign 

 1         name="Server" key-type=rsa common-name="server" key-size=2048 subject-alt-name="" days-valid=365 
           key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client 

 2         name="Client" key-type=rsa common-name="client" key-size=2048 subject-alt-name="" days-valid=365 
           key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client 
```

#### 憑證範本屬性 {#certificate-template-properties}

在憑證範本建立過程中，可以定義並設定多個參數，以符合特定需求。

| Property | Description |
| :-- | :-- |
| **common-name** (*string*) | 憑證通用名稱 |
| **copy-from**(*name*) | 要從中複製一般設定的憑證名稱 |
| **country** (*string*) | 憑證簽發者國家 |
| **days-valid** (*days* Default: **365**) | 憑證簽署後有效的天數 |
| **digest-algorithm** (*md5 \| sha1 \| sha256 \| sha384 \| sha512* Default: **sha256**) | 用於簽署憑證的雜湊演算法。 |
| **key-size** (*1024* \| *1536* \| *2048* \| *4096* \| *8192* \| *prime256v1* \| *secp384r1* \| *secp521r1* Default: **2048**) | 憑證公鑰大小 |
| **key-usage** (*code-sign* \| *crl-sign* \| *decipher-only* \| *dvcs* \| *encipher-only* \| *key-cert-sign* \| *ocsp-sign* \| *tls-client* \| *content-commitment* \| *data-encipherment* \| *digital-signature* \| *email-protect* \| *key-agreement* \| *key-encipherment* \| *timestamp* \| *tls-server* Default: **digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client)** | 憑證用途 |
| **locality** (*string*) | 憑證簽發者所在地 |
| **name** (*string*) | 憑證名稱 |
| **organization** (*string*) | 憑證簽發者組織 |
| **state** (*string*) | 憑證簽發者州別 |
| **subject-alt-name** (*DNS: \| IP: \| email:*) | 憑證主體替代名稱 |
| **trusted** (*no \| yes*) | 是否信任憑證。若為 *yes*，憑證將用於主機憑證驗證。 |
| **trust-store**(*all* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging* Default: **all**) | 指定可使用特定憑證進行憑證驗證或信任鏈建立服務（www、sstp）。 |
| **unit** (*string*) | 憑證簽發者組織單位 |

### 憑證屬性 {#certificate-properties}

對於已簽署的憑證，大多數屬性為唯讀，但 *name*、*trusted* 與 *trust-store* 除外。

| Property | Description |
| :-- | :-- |
| **acme-status** *(string)* | ACME 用戶端狀態 |
| **common-name** (*string*) | 憑證通用名稱 |
| **copy-from**(*name*) | 要從中複製一般設定的憑證名稱 |
| **country** (*string*) | 憑證簽發者國家 |
| **days-valid** (*days*) | 憑證簽署後有效的天數 |
| **digest-algorithm** (*md5 \| sha1 \| sha256 \| sha384 \| sha512*) | 用於簽署憑證的雜湊演算法 |
| **directory-url** *(string)* | ACME 用戶端目錄 URL |
| **domain-names** *(string)* | ACME 用戶端使用的網域名稱 |
| **key-size** (*1024* \| *1536* \| *2048* \| *4096* \| *8192* \| *prime256v1* \| *secp384r1* \| *secp521r1*) | 憑證公鑰大小 |
| **key-usage** (*code-sign* \| *crl-sign* \| *decipher-only* \| *dvcs* \| *encipher-only* \| *key-cert-sign* \| *ocsp-sign* \| *tls-client* \| *content-commitment* \| *data-encipherment* \| *digital-signature* \| *email-protect* \| *key-agreement* \| *key-encipherment* \| *timestamp* \| *tls-server*) | 憑證用途 |
| **locality** (*string*) | 憑證簽發者所在地 |
| **organization** (*string*) | 憑證簽發者組織 |
| **revoked** *(date)* | 憑證撤銷時間（僅適用於在特定設備中簽署並撤銷的憑證） |
| **state** (*string*) | 憑證簽發者州別 |
| **subject-alt-name** (*DNS \| IP \| email*) | 憑證主體替代名稱 |
| **trusted** (*no \| yes*) | 是否信任憑證。若為 *yes*，憑證將用於主機憑證驗證。 |
| **trust-store**(*all* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging*) | 指定可使用特定憑證進行憑證驗證或信任鏈建立的服務（www、sstp）。 |
| **unit** (*string*) | 憑證簽發者組織單位 |
| **serial-number** (*string*) | 憑證序號 |
| **fingerprint** (*string*) | 憑證指紋 |
| **akid** (*string*) | 憑證授權單位 ID |
| **skid** (*string*) | 憑證主體 ID |
| **issuer** (*string*) | 憑證授權單位 |
| **invalid-before** *(date)* | 憑證尚未生效的日期與時間（有效期開始日期）。 |
| **invalid-after** *(date)* | 憑證不再有效的日期與時間（到期日）。 |
| **expires-after** *(time)* | 到期前剩餘時間 |
| **key-type** (*string*) | 私密金鑰類型 |
| **ca** *(string)* | CA 憑證名稱（僅顯示於在特定設備中簽署的憑證） |

:::warning
如果移除 CA 憑證，鏈中的所有已簽發憑證也會一併移除。
:::

### 簽署憑證 {#sign-certificate}

憑證應進行簽署。在下列範例中，我們將簽署憑證，並為伺服器憑證新增 CRL URL：

```ros
/certificate 
sign CA-Template 
sign Client      
sign Server ca-crl-host=192.168.88.1 name=ServerCA

```

讓我們檢查憑證是否已簽署：

```ros
[admin@MikroTik] /certificate> print
Flags: K - private-key; L - crl; A - authority; T - trusted
Columns: NAME, COMMON-name, FINGERPRINT
#        NAME         COMMON  FINGERPRINT                                                     
0  K AT  CA-Template  CAtemp  0c7aaa7607a4dde1bbf33deaae6be7bac9fe4064ba47d64e8a73dcefad6cfc38
1  K AT  Client       client  b3ff25ecb166ea41e15733a7493003f3ea66310c10390c33e98fe32364c3659f
2  KLAT  ServerCA     server  152b88c9d81f4b765a59e2302e01efd1fbf11ceeed6e59f4974e87787a5bb980

```

如需影片範例，請按[這裡。](http://youtube.com/watch?v=i2A3YIQKfwY)

:::warning
金鑰簽署程序的時間取決於特定憑證的金鑰大小。若使用 4k 或更高的值，在 CPU 效能較低的裝置上，簽署該特定憑證可能需要相當長的時間。
:::

### 匯出憑證 {#export-certificate}

可以匯出用戶端憑證（含金鑰）與 CA 憑證，格式有兩種：PEM 或 PKCS12。

| 屬性 | 說明 |
| :-- | :-- |
| **export-passphrase** (*string* 預設：**none**) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 將用於匯出憑證私密金鑰加密的密碼片語。 |
| **file-name** (*string* 預設：**cert\_export\_[certificate name].crt/key/pkcs12**) | 匯出的憑證檔案名稱。 |
| **type** (*pem \| pkcs12* 預設：**pem**) | 匯出的憑證類型。 <br/> 若為 PEM，憑證會以 CRT 副檔名匯出；若指定 export-passphrase，也會匯出加密的私密 KEY 檔案。 <br/> 若為 PKCS12，憑證會以 P12 副檔名匯出；若指定 export-passphrase，匯出的憑證會包含加密的私密金鑰。PKCS12 檔案使用 AES 加密。 |

```ros
/certificate 
export-certificate CA-Template 
export-certificate ServerCA export-passphrase=yourpassphrase
export-certificate Client export-passphrase=yourpassphrase
```

匯出的憑證可在 */file* 區段下取得：

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
匯出憑證需要「sensitive」使用者政策。
:::

### 匯入憑證 {#import-certificate}

若要匯入憑證，必須使用其中一種檔案上傳方法，將憑證上傳至設備。

憑證必須以檔案形式匯入。

支援 PEM、DER、CRT、PKCS12 格式。PKCS12 匯入支援 AES 與 3DES 解密。

| Property | Description |
| :-- | :-- |
| **name** (*string* Default: **file-name\_number**) | 將顯示在憑證管理員中的憑證名稱 |
| **file-name** (*string*) | 將要匯入的檔案名稱 |
| **passphrase** (*string* Default: **none**) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 檔案的通行碼（若有） |
| **trusted** (*yes \| no* Default: yes) | 為匯入的憑證新增 *trusted* 旗標 |
| **trust-store**(*all* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging*  Default: **all**) | 指定可使用特定憑證進行憑證驗證或信任鏈建立（www、sstp）的服務。 |

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

### CRL

RouterOS 支援憑證撤銷清單（Certificate Revocation List，CRL）檢查。

預設不會使用 CRL，也不會驗證憑證的撤銷狀態。

在 [certificate setting](#settings) 中啟用 `crl-use=yes`，讓系統根據 CRL 驗證鏈中的每個憑證，並設定 `crl-download=yes`，讓 RouterOS 自動下載與更新 CRL。

CRL 可透過提供 CRL URL 手動新增，或在匯入包含 CRL Distribution Point 的憑證時動態新增。

| Property | Description |
| :-- | :-- |
| **akid** (*string*) | CRL 授權 ID |
| **cert**(*string*) | 新增 CRL Distribution Point 的來源憑證（來自憑證存放區） |
| **dynamic** (*flag*) | CRL 是否為動態新增 |
| **expired** (*flag*) | CRL 是否已過期 |
| **fingerprint** (*string*) | CRL 指紋 |
| **Invalid** (*flag*) | CRL 是否無效（未更新） |
| **last-update** (*date*) | 上次 CRL 更新的日期與時間 |
| **next-update** (*date*) | 下次 CRL 更新的日期與時間 |
| **num** (*integer*) | CRL 編號 |
| **removed** (*integer*) | 已撤銷憑證的數量 |
| **signature** (*string*) | CRL 簽章 |
| **url** (*string*) | CRL URL |
| **num** (*integer*) | CRL 編號 |

### 設定 {#settings}

`/certificate/settings` 可設定 [Certificate Revocation List](#crl) 與 [built-in trust store](#built-in-trust-store-authorities) 設定。

| Property | Description |
| :-- | :-- |
| **builtin-trust-store** (*all* \| *default* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging* \| *untrusted* Default: **default**) | 可使用 <a href="#built-in-trust-store-authorities">built-in trust store authorities</a> 進行憑證驗證的服務。 <br/> 目前的預設值： <ul><li>fetch</li><li>mqtt</li><li>email</li><li>netwatch</li><li>container</li><li>lora</li><li>dns</li><li>www</li><li>reverse-proxy</li></ul> |
| **crl-download** (*yes \| no* Default: **no**) | 是否自動下載／更新 CRL |
| **crl-store** (*ram \| system* Default: **ram**) | 儲存已下載 CRL 資訊的位置 <br/> 對於使用 http 通訊協定且 "trusted=yes" 的憑證，CRL 將每小時自動更新一次（目前不支援 ldap 與 ftp） |
| **crl-use** (*yes \| no* Default: **no**) | 是否使用 CRL |

:::warning
如果 *`/certificate/settings/set crl-use`* 設為 *`yes`*，RouterOS 會檢查憑證鏈中每個憑證的 CRL，因此，整個憑證鏈都應安裝到設備中，從 Root CA、中繼 CA（若有），以及用於特定服務的憑證開始。
:::

匯入根憑證的[範例](http://youtube.com/watch?v=q9oMO3_jvBU)。

## ACME 用戶端 {#acme-client}

ACME 用戶端會透過 ACME 自動取得與更新多個 TLS 憑證。

若要透過 CLI 新增 ACME 用戶端，請使用指令 `/certificate/add-acme`。

現有的 ACME 用戶端會顯示在 Certificates 檢視中，並標示 `a` (`acme-manage`) 旗標。

網域名稱必須解析至路由器，且 TCP 埠 80 必須可從 WAN 存取（使用 HTTP-01 challenge）。對於 IP Cloud `<id>.sn.mynetname.net` 網域名稱，則改用 DNS-01 challenge。

憑證會在有效期間經過 80% 時自動更新。

如果在初始設定期間未取得憑證，則必須新增 ACME 用戶端。

### 屬性 {#properties}

| Property | Description |
| :-- | :-- |
| **directory-url** (*string*) | ACME directory URL |
| **domain-names** (*string*) | 以逗號分隔的網域名稱清單 |
| **eab-hmac-key** (*string*) | ACME External Account Binding 的 HMAC 金鑰 |
| **eab-kid** (*string*) | 金鑰識別碼 |
| **name** (*string*) | ACME 用戶端名稱 |

### 手動更新 ACME {#manual-acme-renewal}

若要手動觸發 ACME 憑證更新：

```ros
/certificate/acme-renew [name]
```

例如：

```ros
/certificate/acme-renew numbers=0
```

### Let's Encrypt 憑證 {#lets-encrypt-certificate}

若要取得 Let's Encrypt 憑證並自動更新憑證，必須使用 `domain-names` 參數手動提供網域名稱：

```ros
/certificate/add-acme domain-names=router.example.com
```

若要為 [IP Cloud](/docs/network-management/cloud#ddns) 名稱產生 Let's Encrypt 憑證（例如 `example.sn.mynetname.net`），請將 `/ip/cloud` 選單中的 `dns-name` 作為網域名稱提供，或使用 `[/ip/cloud/get dns-name]` 直接讀取：

```ros
/certificate/add-acme domain-names=[/ip/cloud/get dns-name]
```

:::info
若未提供 `directory-url`，則會使用 Let's Encrypt 目錄。
:::

:::note
憑證更新期間無法移除憑證。若 ACME 憑證更新失敗並保持在錯誤狀態，`remove` 指令會失敗並顯示 `cannot remove certificate while acme update is in progress`。請重新啟動路由器，然後再移除憑證。
:::

## SCEP

SCEP 使用 HTTP 通訊協定與 base64 編碼的 GET 請求。大多數請求不含驗證與加密，不過重要的請求可在需要時加以保護（使用接收到的公鑰進行加密或簽署）。

RouterOS 中的 SCEP 用戶端將會：

- 從 CA 伺服器或 RA（如有使用）取得 CA 憑證。
- 使用者應比對 CA 憑證的指紋，或確認其是否來自正確的伺服器。
- 產生具有暫時金鑰的自簽憑證。
- 傳送憑證要求給伺服器。
- 如果伺服器回應狀態 x，則用戶端會持續要求，直到伺服器傳送錯誤或核准為止。

SCEP 伺服器僅支援核發單一憑證。RouterOS 也支援 renew 與 next-ca 選項：

- renew - 自動向相同 CA 更新舊憑證的能力。
- next-ca - 將目前 CA 憑證變更為新憑證的能力。

用戶端會輪詢伺服器是否有任何變更，如果伺服器公告 next-ca 可用，則用戶端可以要求下一個 CA，或等待 CA 幾乎到期後再要求 next-ca。

如果伺服器公告支援，RouterOS 用戶端預設會嘗試使用 POST、AES 與 SHA256。如果不支援上述演算法，則用戶端會嘗試使用 3DES、DES 與 SHA1、MD5。

SCEP 憑證會在有效期限經過 3/4 後更新。

## 內建信任存放區憑證授權單位 {#built-in-trust-store-authorities}

RouterOS 包含一份內建根憑證授權單位清單，特定服務可使用該清單驗證主機憑證。

SMIPS 設備具有[精簡的內建 CA 信任存放區](#smips-built-in-cas)。

可使用內建根憑證授權單位的服務清單，請參閱[設定](#settings)一節。

可以搭配憑證驗證使用 [DoH](/docs/network-management/dns)，而不需要手動匯入相關的根憑證。

內建根憑證授權單位清單可在 System → Certificates → Built In CA 或 `/certificate/builtin/` 中存取。

### 內建 CA 清單 {#list-of-built-in-cas}

下列內建 CA 清單適用於除 SMIPS 以外的所有架構。

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
| Internet Security Research Group | ISRG Root X1 | `79B459E67BB6E5E40173800888C81A58F6E99B6E` |
| Internet Security Research Group | ISRG Root X2 | `7C4296AEDE4B483BFA92F89E8CCF6D8BA9723795` |
| ISRG | Root YE | `A3C8265A8EA14CD03563FC9B23C83AAE56F34F56` |
| ISRG | Root YR | `DEE75B60D0226D40287D3F0D01FEA4B552B45194` |

### SMIPS 內建 CA {#smips-built-in-cas}

SMIPS 設備的內建 CA 信任存放區較精簡：

| 組織 | 通用名稱 | 主體 ID |
| :-- | :-- | :-- |
| DigiCert Inc | DigiCert Global Root G2 | `4E2254201895E6E36EE60FFAFAB912ED06178F39` |
| Internet Security Research Group | ISRG Root X1 | `79B459E67BB6E5E40173800888C81A58F6E99B6E` |
| Internet Security Research Group | ISRG Root X2 | `7C4296AEDE4B483BFA92F89E8CCF6D8BA9723795` |
| ISRG | Root YE | `A3C8265A8EA14CD03563FC9B23C83AAE56F34F56` |
| ISRG | Root YR | `DEE75B60D0226D40287D3F0D01FEA4B552B45194` |
