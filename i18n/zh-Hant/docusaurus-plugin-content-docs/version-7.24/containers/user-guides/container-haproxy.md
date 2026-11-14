---
sidebar_key: "containers/user-guides/container-haproxy"
sidebar_position: 2
title: "容器 - HAProxy"
sidebar_label: "容器 - HAProxy"
description: "本頁介紹如何在 MikroTik RouterOS 中將 HAProxy 配置為 Container，並提供使用 Certbot 設定支援 HTTPS 的反向代理和負載均衡的分步說明。"
tags:
  - 'haproxy'
  - 'container'
  - 'https'
source: https://manual.mikrotik.com/docs/7.24/containers/user-guides/container-haproxy
captured_at: '2026-11-04T11:27:39+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

HAProxy 是一個高效能的反向代理和負載均衡器，可作為 Container 使用。

為了獲得最佳安全性，強烈建議使用像 HAProxy 這樣的反向 HTTP/HTTPS 代理，作為外部使用者與內部服務之間的中介，而不是將 Container 直接暴露到網路。

## 配置 {#configuration}

要在您的 RouterOS 裝置上設定 HAProxy Container，請按照以下步驟操作。

:::info

在繼續之前，請確保已建立 [Container 網路](../index.md#networking-examples)。

:::

1. 建立 HAProxy Container 掛載點。  

   ```routeros
   /container/mounts/add list=haproxy_etc src=disk1/haproxy-etc dst=/usr/local/etc/haproxy
   ```

2. 建立 HAProxy Container。  

   ```routeros
   /container/add remote-image=haproxy:latest interface=veth1 root-dir=disk1/haproxy mountlists=haproxy_etc user=0:0 name=haproxy
   ```

3. 使用 SFTP 用戶端（例如，在 Microsoft Windows 上使用 WinSCP）連線到您的 RouterOS 裝置，並建立新檔案 `disk1/haproxy-etc/haproxy.cfg`，您可以將以下配置用作示例。  

```cfg
defaults
  mode http
  timeout client 10s
  timeout connect 10s
  timeout server 10s
  timeout http-request 10s

frontend http_synapse
  bind *:80
  use_backend synapse

backend synapse
  server server1 172.17.0.2:8008 maxconn 32
```

1. 啟動 HAProxy Container。  

   ```routeros
   /container/start [find where name=haproxy]
   ```

## 高階：HAProxy 與 Certbot {#advanced-haproxy-with-certbot}

本示例展示如何配置 HAProxy 來提供 HTTPS 流量服務，並透過使用 Certbot 和 RFC2136 自動續訂證書。

1. 建立 HAProxy Container：  

   ```routeros
   /container/mounts/add list=MOUNT_HAPROXY src=disk1/volumes/haproxy/config dst=/usr/local/etc/haproxy
   /container/add remote-image=haproxy:latest interface=veth1 root-dir=disk1/images/haproxy mountlists=MOUNT_HAPROXY name=haproxy start-on-boot=yes user=0:0 logging=yes
   ```

2. 在您的 PC 上建立名為 `haproxy.cfg` 的新檔案，並將其上傳到 `disk1/volumes/haproxy/config/`，然後根據您的需求調整配置：  

```cfg
global
  log stdout format raw local0 info
  stats socket :9999 level admin expose-fd listeners
  ssl-default-bind-ciphers EECDH+AESGCM:EDH+AESGCM
  ssl-default-server-ciphers EECDH+AESGCM:EDH+AESGCM
  ssl-default-bind-options ssl-min-ver TLSv1.2
  ssl-default-server-options ssl-min-ver TLSv1.2
  tune.ssl.default-dh-param 2048
  tune.bufsize 43768
  tune.ssl.cachesize 1000000
  nbthread 8

defaults
  log global
  timeout client 10s
  timeout connect 10s
  timeout server 10s
  timeout http-request 10s

frontend frontend_webapp
  mode http
  option httplog
  option http-server-close
  option forwardfor except 127.0.0.0/8
  stick-table type ipv6 size 100k expire 30s store http_req_rate(10s)
  http-request track-sc0 src
  http-request deny deny_status 429 if { sc_http_req_rate(0) gt 10000 }
  bind *:80
  bind *:443 ssl crt /usr/local/etc/haproxy/certs/
  http-request redirect scheme https unless { ssl_fc }
  http-request set-header X-Forwarded-Host %[req.hdr(host)]
  http-request set-header X-Forwarded-For %[src]
  use_backend backend_webapp

backend backend_webapp
  mode http
  balance roundrobin
  option http-server-close
  option forwardfor
  server server1 172.17.0.2:8080

```

1. 建立 Certbot Container：  

   ```routeros
   /container/mounts/add list=MOUNT_CERTBOT_CONFIG src=disk1/volumes/certbot/config dst=/etc/letsencrypt
   /container/mounts/add list=MOUNT_CERTBOT_DATA src=disk1/volumes/certbot/data dst=/var/lib/letsencrypt
   /container/mounts/add list=MOUNT_CERTBOT_LOG src=disk1/volumes/certbot/log dst=/var/log/letsencrypt
   /container/mounts/add list=MOUNT_CERTBOT_HAPROXY src=disk1/volumes/haproxy/config dst=/etc/haproxy
   /container/add remote-image=certbot/dns-rfc2136 cmd="certonly -n --agree-tos --dns-rfc2136 --dns-rfc2136-credentials /etc/letsencrypt/rfc2136.ini -m admin@<FQDN> --deploy-hook 'cat /etc/letsencrypt/li\
       ve/<FQDN>/fullchain.pem /etc/letsencrypt/live/<FQDN>/privkey.pem | tee /etc/haproxy/certs/<FQDN>.pem > /dev/null; echo -e \"set ssl cert /usr/local/e\
       tc/haproxy/certs/<FQDN>.pem <<\
       \n\$(cat /etc/haproxy/certs/<FQDN>.pem)\
       \n\" | nc 127.0.0.1:9999; echo \"commit ssl cert /usr/local/etc/haproxy/certs/<FQDN>.pem\" | nc 127.0.0.1:9999' -d <FQDN> --cert-name <FQDN>" \
       interface=veth1 logging=yes mountlists=MOUNT_CERTBOT_CONFIG,MOUNT_CERTBOT_DATA,MOUNT_CERTBOT_LOG,MOUNT_CERTBOT_HAPROXY name=certbot root-dir=\
       disk1/images/certbot start-on-boot=yes workdir=/opt/certbot

   ```

:::warning

請確保將上述示例中的所有 `<FQDN>` 佔位符替換為您的完全限定域名！

:::

1. 等待 Container 映象下載完成，然後啟動 Certbot Container：  

   ```routeros
   /container/start [find where name=certbot]
   ```

2. 檢查日誌，以確保您成功獲取了新證書：  

   ```routeros
   /log/print follow
   ```

3. 啟動 HAProxy Container：  

   ```routeros
   /container/start [find where name=haproxy]
   ```

4. 設定計劃任務，例如每天 06:30 檢查新證書：  

   ```routeros
   /system/scheduler
   add interval=1d name=SCHEDULE_RenewCertbot on-event=SCRIPT_RenewCertbot policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=\
       2025-03-10 start-time=06:30:00
   /system/script
   add dont-require-permissions=no name=SCRIPT_RenewCertbot owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=\
       "/container/start [find where name=\"certbot\"]"
   ```

5. 完成

證書將自動續訂並替換 HAProxy 中的舊證書，而無需重啟 Container。
