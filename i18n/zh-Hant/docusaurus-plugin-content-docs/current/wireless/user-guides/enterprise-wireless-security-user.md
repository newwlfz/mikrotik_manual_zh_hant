---
sidebar_key: "wireless/user-guides/enterprise-wireless-security-user"
sidebar_position: 1
title: "企業級無線安全與 User Manager v5"
sidebar_label: "企業級無線安全與 User Manager v5"
description: "本指南介紹如何將 MikroTik RouterOS User Manager v5 配置為企業無線網路的認證伺服器，內容涵蓋安裝、為 PEAP 和 EAP-TLS 等安全 EAP 方法生成 TLS 證書，以及使用基於證書的認證來設定接入點。"
tags:
  - 'user-authentication'
  - 'tls-certificates'
  - 'eap'
source: https://manual.mikrotik.com/docs/wireless/user-guides/enterprise-wireless-security-user
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

User Manager 版本 5（適用於 RouterOS v7）支援透過可擴充套件認證協定（EAP）進行使用者認證。

本指南將說明將 User Manager v5 配置為 MikroTik 無線接入點的認證伺服器所需的步驟，並向用戶提供 PEAP 和 EAP-TLS 認證方法。

本指南假設有一臺執行 User Manager 的獨立裝置，網路地址為 10.0.0.10，以及 2 個接入點——一個地址為 10.0.0.11，另一個為 10.0.0.12。

## 安裝 User Manager {#installing-user-manager}

User Manager v5 可在 [RouterOS v7 最新版本](https://mikrotik.com/download)的 'Extra packages' 歸檔中找到。

下載適用於相應 CPU 架構的歸檔，將其解壓，把 User Manager 軟體包上傳到路由器並重啟路由器。

## 生成 TLS 證書 {#generating-tls-certificates}

使用安全 EAP 方法時，用戶端裝置（請求方）會在向認證伺服器傳送自身憑據之前驗證認證伺服器的身份。  
為此，認證伺服器需要一張 TLS 證書。

該證書應：

1. 有效，並由用戶端裝置信任的證書頒發機構簽名。
2. 在 Common Name (CN) 和 Subject Alt Name 欄位中包含完全限定域名。
3. 具有 Extended Key Usage 屬性，表明其獲准用於認證 TLS 伺服器。
4. 有效期不超過 825 天。

EAP-TLS 方法要求用戶端裝置擁有 TLS 證書（而不是密碼）。

要被視為對 User Manager 有效，用戶端證書必須：

1. 有效，並由執行 User Manager 的裝置信任的機構簽名
2. 在 Subject Alt Name (SAN) 欄位中包含使用者名稱。為向後相容，也可以將其新增到 CN 欄位。更多資訊請參見：[https://datatracker.ietf.org/doc/html/rfc5216#section-5.2](https://datatracker.ietf.org/doc/html/rfc5216#section-5.2)

最後，WPA3 企業規範包含一種額外安全模式，可提供 192 位加密安全性。

此模式要求使用 EAP-TLS，並且證書必須：

1. 使用 P-384 橢圓曲線金鑰或長度至少為 3072 位的 RSA 金鑰。
2. 使用 SHA384 作為摘要（雜湊）演算法。

為簡潔起見（並展示 RouterOS 的更多功能），本指南將演示如何在執行 User Manager 的裝置上生成所有證書，但在大型企業環境中，認證伺服器和用戶端裝置會各自在本地生成私鑰和證書籤名請求，然後將 CSR 上傳到證書頒發機構進行簽名。

**在執行 User Manager 的裝置上執行的命令：**

```ros
# 生成证书颁发机构
/certificate
add name=radius-ca common-name="RADIUS CA" key-size=secp384r1 digest-algorithm=sha384 days-valid=1825 key-usage=key-cert-sign,crl-sign
sign radius-ca ca-crl-host=radius.mikrotik.test
# 为 User Manager 生成服务器证书
add name=userman-cert common-name=radius.mikrotik.test subject-alt-name=DNS:radius.mikrotik.test key-size=secp384r1 digest-algorithm=sha384 days-valid=800 key-usage=tls-server
sign userman-cert ca=radius-ca
# 生成客户端证书
add name=maija-client-cert common-name=maija@mikrotik.test subject-alt-name=email:maija@mikrotik.test key-usage=tls-client days-valid=800 key-size=secp384r1 digest-algorithm=sha384
sign maija-client-cert ca=radius-ca
# 导出 CA 的公钥以及生成的客户端私钥和证书，以便分发到客户端设备
export-certificate radius-ca file-name=radius-ca
# 导出时需要口令才能包含私钥
export-certificate maija-client-cert type=pkcs12 export-passphrase="true zebra capacitor ziptie"
```

## 配置 User Manager {#configuring-user-manager}

**在執行 User Manager 的裝置上執行的命令：**

```ros
# 启用 User Manager 并指定要使用的证书
/user-manager
set enabled=yes certificate=userman-cert
# 启用 CRL 检查，以避免接受已吊销的用户证书
/certificate/settings
set crl-download=yes crl-use=yes
# 添加接入点
/user-manager/router
add name=ap1 address=10.0.0.11 shared-secret="Use a secure password generator for this"
add name=ap2 address=10.0.0.12 shared-secret="Use a secure password generator for this too"
# 限制允许的认证方式
/user-manager/user/group
set [find where name=default] outer-auths=eap-tls,eap-peap
add name=certificate-authenticated outer-auths=eap-tls
# 添加用户
/user-manager/user
add name=maija@mikrotik.test group=certificate-authenticated
add name=paija@mikrotik.test group=default password="right mule accumulator nail"
```

:::info
使用 CAPsMAN 控制器配置 AP 時，可以使用下面所示的完全相同配置來預配 CAP。只需為 CAP 預配 SSID + wpa2-eap/wpa3-eap 認證型別。  
使用 CAPsMAN 時，CAPsMAN 應為 `/radius` 用戶端（而不是 AP，如下面的獨立設定示例所示）。
:::

## 配置接入點 {#configuring-access-points}

### 執行常規 wireless 軟體包的 AP {#ap-running-regular-wireless-package}

**在 ap1 上執行的命令：**

```ros
# 配置 radius 客户端
/radius
add address=10.0.0.10 secret="Use a secure password generator for this" service=wireless timeout=1s
/radius/incoming
set accept=yes
# 添加安全配置文件并将其应用到无线接口
/interface/wireless/security-profile
add name=radius mode=dynamic-keys authentication-types=wpa2-eap
/interface/wireless
set [find] security-profile=radius
```

### 執行 wifi-qcom 軟體包的 AP {#ap-running-wifi-qcom-package}

**在 ap2 上執行的命令：**

```ros
# 配置 radius 客户端
/radius
add address=10.0.0.10 secret="Use a secure password generator for this too" service=wireless timeout=1s
/radius/incoming
set accept=yes
# 配置启用的认证类型。也可以通过安全配置文件完成，但请注意，如果指定了接口属性，接口属性会覆盖配置文件属性
/interface/wifi/set [find] security.authentication-types=wpa2-eap,wpa3-eap
```

wifi-qcom AP 也可以配置為使用額外安全的 wpa3-eap-192 模式，但請注意，這要求所有用戶端裝置支援 GCMP-256 加密演算法並採用 EAP-TLS 認證。

## 用戶端裝置配置說明 {#notes-on-client-device-configuration}

### Windows {#windows}

在 Windows 中手動安裝 CA 時，請確保將其顯式放入 'Trusted Root Certification Authorities' 證書儲存中。它不會自動放入該儲存。

### Android {#android}

連線到使用 EAP 認證的網路時，Android 裝置會要求使用者指定一個 'domain'。這指的是 RADIUS 伺服器 TLS 證書中包含的主機名的預期域（在我們的示例中為 'mikrotik.test'）。

預設情況下，Android 裝置使用其內建根 CA 列表來驗證 RADIUS 伺服器的證書。使用你自己的 CA 時，需要在相應的下拉選單中選擇它。

### iOS {#ios}

Apple iOS 似乎實際上並不信任手動匯入的 CA 來認證 RADIUS 伺服器。除非使用 Apple 專有的 'Configurator' 工具或經批准的第三方 MDM 工具匯入 CA，否則伺服器證書會被標記為 'Not Trusted'。
