---
sidebar_key: "cli-reference/system/package/local-update/download-all"
sidebar_position: 1
title: "download-all"
sidebar_label: 'download-all'
source: https://manual.mikrotik.com/docs/cli-reference/system/package/local-update/download-all
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/package/local-update/download-all {#systempackagelocal-updatedownload-all}
**型別：** 命令

下載本地軟體包伺服器上所有可用的相容（與裝置架構匹配）軟體包。下載的軟體包會儲存在根目錄中。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="download-beta" typ="bool">下載所有相容軟體包時是否包含 beta 軟體包。</ArgTableRow>
<ArgTableRow arg="reboot-after-download" typ="bool">所有軟體包下載完成後是否自動重新啟動裝置。</ArgTableRow>
</ArgTable>
