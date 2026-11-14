---
sidebar_key: "getting-started/installation-and-upgrade/install/chr-installation/aws"
sidebar_position: 1
title: "CHR：AWS 安裝"
sidebar_label: "CHR：AWS 安裝"
description: "本頁指導使用者透過將原始磁碟映像匯入為 AMI 並啟動 EC2 例項，在 Amazon Web Services (AWS) 上部署 MikroTik CHR。"
tags:
  - 'chr'
  - 'aws'
source: https://manual.mikrotik.com/docs/7.24/getting-started/installation-and-upgrade/install/chr-installation/aws
captured_at: '2026-11-04T11:28:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Amazon Web Services (AWS) 並未在 Marketplace 中直接提供 MikroTik CHR。要在 AWS 上部署 CHR，需要先將原始磁碟映象匯入為 Amazon Machine Image (AMI)，然後用它啟動 EC2 例項。

## 先決條件 {#prerequisites}

- 一個具有使用 EC2、S3 和 VM Import/Export 服務許可權的 AWS 賬戶。
- 已在本機安裝並配置好 [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)。
- 一個用於上傳 CHR 磁碟映象的 S3 儲存桶。

:::info
IAM 使用者或角色必須配置好 `vmimport` 服務角色。所需許可權和信任策略請參閱 [AWS VM Import/Export 文件](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html)。
:::

## 步驟 1：下載 CHR 原始磁碟映象 {#step-1-download-the-chr-raw-disk-image}

1. 訪問 [MikroTik 下載頁面](https://mikrotik.com/download)。
2. 找到適用於目標架構的最新 Stable 版 **CHR raw disk image**（`.img` 檔案）。
3. 下載並解壓該歸檔檔案。

## 步驟 2：將映象上傳到 S3 {#step-2-upload-the-image-to-s3}

將原始 `.img` 檔案上傳到你的 S3 儲存桶：

```bash
aws s3 cp chr-x.x.x.img s3://YOUR-BUCKET-NAME/chr-x.x.x.img
```

將 `YOUR-BUCKET-NAME` 替換為實際的 S3 儲存桶名稱，將 `x.x.x` 替換為 RouterOS 版本。

## 步驟 3：建立匯入清單 {#step-3-create-the-import-manifest}

建立一個 JSON 檔案（例如 `containers.json`），用於描述匯入過程所需的磁碟映象：

```json
{
  "Description": "MikroTik RouterOS CHR",
  "Format": "raw",
  "UserBucket": {
    "S3Bucket": "YOUR-BUCKET-NAME",
    "S3Key": "chr-x.x.x.img"
  }
}
```

## 步驟 4：匯入快照 {#step-4-import-the-snapshot}

啟動快照匯入並記錄任務 ID：

```bash
aws ec2 import-snapshot \
  --description "MikroTik RouterOS CHR" \
  --disk-container file://containers.json
```

輸出中會包含 `ImportTaskId`。用它來監控進度：

```bash
aws ec2 describe-import-snapshot-tasks \
  --import-task-ids import-snap-xxxxxxxxxxxxxxxxx
```

等待狀態顯示為 `completed`。輸出中會包含 `SnapshotId`。

## 步驟 5：註冊 AMI {#step-5-register-the-ami}

將匯入的快照註冊為 AMI：

```bash
aws ec2 register-image \
  --name "MikroTik RouterOS CHR" \
  --description "MikroTik RouterOS CHR" \
  --architecture x86_64 \
  --virtualization-type hvm \
  --ena-support \
  --root-device-name "/dev/sda1" \
  --block-device-mappings "[{\"DeviceName\": \"/dev/sda1\", \"Ebs\": { \"SnapshotId\": \"snap-xxxxxxxxxxxxxxxxx\"}}]"
```

將 `SnapshotId` 替換為上一步得到的值。輸出中會包含 `ImageId` —— 這就是你新建的 AMI。

## 步驟 6：啟動 EC2 例項 {#step-6-launch-an-ec2-instance}

1. 開啟 [EC2 控制檯](https://console.aws.amazon.com/ec2/)。
2. 進入 **Images > AMIs**，找到你新建的 CHR AMI。
3. 選中它並選擇 **Launch**。
4. 選擇例項型別（例如用於測試的 `t3.micro`）。
5. 根據需要配置網路、安全組和金鑰對。
6. 啟動例項。

:::warning
確保安全組僅允許你的管理 IP 訪問 SSH（埠 22）和 WinBox（埠 8291）。首次登入後應立即加固路由器 —— 參見[保護你的路由器](../../../securing-your-router.md)。
:::

## 步驟 7：連線到 CHR {#step-7-connect-to-chr}

1. 使用例項的公網 IP 透過 SSH 連線：

   ```ros
   ssh admin@INSTANCE_PUBLIC_IP
   ```

2. 首次登入時，請檢視軟體許可並設定強密碼。
3. 然後繼續配置。生產環境搭建指南請參閱[首次配置](../../../first-time-configuration.md)。

:::tip
AWS 預設不分配公網 IP。請確保例項已關聯公網 IP 或 Elastic IP，並且安全組允許入站 SSH。
:::
