# MikroTik Manual Mirror · English hub repository

英文網站在此建置：<https://newwlfz.github.io/mikrotik_manual_i18n/>。它也是三個網站的唯一資料來源：內容會從 <https://manual.mikrotik.com/> 同步進來、修正後，再推送到簡體與繁體中文翻譯儲存庫。

簡體與繁體網站不在這個儲存庫中建置。兩者各有自己的儲存庫（`mikrotik_manual_zh_hans`、`mikrotik_manual_zh_hant`），只存放各自的翻譯。這個儲存庫根目錄的 `locales.json` 是三個網站共用的語言登錄檔：導覽列語言下拉式選單、每個頁面上的 `hreflang` 標籤，以及中文瀏覽器的首次造訪重新導向，都是從它產生的。

## 每天會發生什麼事

1. `.github/workflows/sync.yml` 每天在 03:00 UTC（11:00 Asia/Shanghai）先送出以 ETag 為基礎的條件式請求。如果官方網站沒有變更，該次執行會在沒有提交、也沒有建置的情況下結束。
2. 只有官方網站有變更時，才會執行同步（在 CI 中：`node tools/sync/index.mjs --update`；本機對等指令是 `npm run sync`）：它會擷取新內容、切換版本、重建側邊欄與 CLI 資料、將結果提交回 `main`，然後明確觸發 `pages.yml`。
3. `pages.yml` 會建置英文網站、執行 `npm run verify:deploy`，並發佈它。
4. 同一個工作流程中的 `publish-content` 工作會使用 `CROSS_REPO_TOKEN` 將內容推送到兩個語言儲存庫，並觸發 `content-fanout`；收到事件後，它們會進行翻譯、建置與部署。

同步失敗時不會提交任何內容，只會開啟一個 `sync failed:` issue；線上網站會停留在前一個版本。詳情請參閱 `guides/CI.md` 與 `guides/ARCHITECTURE-MULTISITE.md`。

## 哪些要編輯，哪些不要編輯

| 路徑 | 它是什麼 | 要怎麼做 |
| --- | --- | --- |
| `docs/`、`versioned_docs/`、`hardware/`、`blog/`、`changelog/`、`data/` | 同步輸出 | 不要手動編輯。下一次同步會取代整個目錄樹。若要進行變更，請編輯上游來源或 `tools/sync/`。 |
| `sidebars.ts`、`sidebars-hardware.ts`、`versioned_sidebars/`、`versions.json` | 同步輸出 | 同上；這些也會推送到語言儲存庫。 |
| `upstream/`、`build/`、`.docusaurus/` | 擷取快取與建置輸出 | 不要編輯或提交。 |
| `tools/`、`config/`、`src/`、`docusaurus.config.ts` | 流程與設定 | 真正的變更在這裡進行。同步規則位於 `config/mirror.yml`；網站外殼位於 `src/`。 |
| `.github/workflows/`、`guides/` | CI 與文件 | 變更工作流程時，請在這裡編輯。 |
| `locales.json` | 語言登錄檔 | 可編輯，但一次編輯會影響三個網站（請見下文）。 |

編輯 `locales.json` 是整個儲存庫層級的事件。hub 會將它發佈到兩個語言儲存庫；共用的索引欄位（`default`、每個語言的 `repo` / `baseUrl` / `site` / `available`）必須一致，而 `tagline` / `label` / `siteTitle` 則保留各網站的當地語系化內容，刻意不做逐位元組相同。每當 `available` 旗標從 `false` 切換為 `true`，或位址變更時，都必須重建 hub 與兩個網站，讓語言下拉式選單、`hreflang` 與重新導向中繼資料保持一致。編輯後，請依序執行 `npm run locales:check` 與 `npm run content:publish:dry`，確認計畫後，才執行 `npm run content:publish`。登錄檔的 `default` 必須是 `en`。

使用 `npm run locale:add` 新增語言。先查看計畫：

```bash
npm run locale:add -- --code ru-RU --label Русский --dry-run
```

它只會建立目錄骨架，並在 `locales.json` 中登錄該語言；不會建立 GitHub 儲存庫，也不會寫入任何秘密。之後你仍需要手動建立儲存庫、授予 `CROSS_REPO_TOKEN` 存取權、在新儲存庫中設定 LLM 變數，並再次執行 publish。命令參數請參閱 `--help`，決策理由請參閱 `guides/DECISIONS.md`（D7，以及 README 政策的 D9）。

若要從已發佈的 Release 而不是本機範本進行初始化，請在新的空白儲存庫內執行一個命令：

```bash
node <你的 hub checkout 路径>/templates/locale-repo/tools/bootstrap/from-release.mjs \
  --locale zh-Hant --label 繁體中文 --repo newwlfz/mikrotik_manual_zh_hant --slug zh_hant
```

將 `<你的 hub checkout 路径>` 換成 hub checkout 的實際絕對路徑；這台機器上的真實範例是 `/home/evan/mikrotik_manual_i18n/mikrotik_manual_i18n`（僅供範例，請勿照抄）。

從範本的 checkout 執行時，相同的命令是 `npm run bootstrap:from-release -- --locale ... --dir <empty target>`。它會下載 Release tarball 與資訊清單、驗證 `archive.sha256` 與每個檔案的 SHA-256、展開內容與路徑中的 11 個預留位置、再次確認沒有殘留，然後才寫入目錄樹並列印可複製的 `git init` / `add` / `commit` / `push` 命令。它不會提交、推送或變更憑證；`--dry-run` 只會驗證並列印計畫。仍需由人完成的先決條件包括：建立空白儲存庫、授予 `CROSS_REPO_TOKEN` 存取權、設定 LLM 變數／秘密與 Pages 來源，並在 `locales.json` 中登錄該語言。完整步驟請參閱 `guides/ONBOARDING.md`（zh-Hant 請參閱 `guides/ZH_HANT_RUNBOOK.md`）。

範本含有一份共用的英文 `README.md`。骨架產生程序一律會展開其中的 11 個預留位置，並將它寫成新儲存庫根目錄的 `README.md`；範本中沒有各語言專屬的 README 檔案。語言儲存庫自己的 README，是由該儲存庫的 `translate` 工作流程，從這個 hub 發佈的英文 `hub-docs/` 來源翻譯而來——它是翻譯產物，不是範本變體。維護者不應手動編輯骨架產生出來的 README，也不應在範本中加入語言專屬的 README 檔案。這個 hub 自己的 README 保持英文，且不含任何私人位址。

## 常用命令

```bash
npm ci                          # install dependencies first
npm run sync:probe              # only ask the official site "have you changed?", writes nothing
npm run build                   # CLI data -> Docusaurus -> Pagefind -> llms.txt
npm run verify:deploy           # verify the deploy shape
npm run serve                   # single-site Docusaurus preview (not the three-site server below)
npm run locales:check           # validate locales.json
npm run content:publish:dry     # print what would be pushed, write nothing remote
npm run content:publish         # real push; requires CROSS_REPO_TOKEN
```

請使用 `npm run build` 建置，不要直接執行 `npx docusaurus build`：npm 指令會在 Docusaurus 之後執行 Pagefind 與 llms 重寫，而導覽列搜尋依賴該步驟。

## 本機預覽（三個網站一起）

這三個儲存庫是並排放在同一個工作根目錄下的 checkout；每個都會產生一個 `build/`。請建置你想檢視的網站；尚未建置的網站會回傳 404。已部署的網站是公開的：

- English <https://newwlfz.github.io/mikrotik_manual_i18n/>
- Simplified Chinese <https://newwlfz.github.io/mikrotik_manual_zh_hans/>
- Traditional Chinese <https://newwlfz.github.io/mikrotik_manual_zh_hant/>

若要進行本機預覽，請從工作根目錄（包含三個 checkout 與 `work/` 的目錄）建置網站，然後執行共用的靜態伺服器：

```bash
(cd mikrotik_manual_i18n && npm ci && \
  SITE_LOCALE=en SITE_URL=https://newwlfz.github.io BASE_URL=/mikrotik_manual_i18n/ \
  ASSET_HOST=true npm run build)
(cd mikrotik_manual_zh_hans && npm ci && \
  SITE_LOCALE=zh-Hans SITE_URL=https://newwlfz.github.io BASE_URL=/mikrotik_manual_zh_hans/ \
  ASSET_ORIGIN=https://newwlfz.github.io/mikrotik_manual_i18n npm run build)
(cd mikrotik_manual_zh_hant && npm ci && \
  SITE_LOCALE=zh-Hant SITE_URL=https://newwlfz.github.io BASE_URL=/mikrotik_manual_zh_hant/ \
  ASSET_ORIGIN=https://newwlfz.github.io/mikrotik_manual_i18n npm run build)
node work/serve-multi-i18n.mjs
```

`work/serve-multi-i18n.mjs` 是純 Node 靜態伺服器，會掛載三個 `build/` 目錄樹。它預設監聽 `3030` 埠；設定 `PORT` 可改用其他埠。掛載路徑與目錄名稱都從 `locales.json` 讀取；`/` 會重新導向到英文網站。`npm run serve` 只是 Docusaurus 的單站預覽，不是這個共用伺服器。

使用的變數：

| 變數 | 範例中的值 | 意義 |
| --- | --- | --- |
| `SITE_URL` | `https://newwlfz.github.io` | 此網站的 origin，用於 canonical / hreflang |
| `BASE_URL` | `/mikrotik_manual_i18n/` 等 | 每個網站的路徑前綴，開頭與結尾都要有 `/` |
| `SITE_LOCALE` | `en` / `zh-Hans` / `zh-Hant` | 一次只建置一個語言 |
| `ASSET_ORIGIN` | `https://newwlfz.github.io/mikrotik_manual_i18n` | 中文網站從英文網站載入圖片、PDF 與影片；結尾不加斜線 |
| `ASSET_HOST` | `true` | 僅 hub 使用：在精簡建置中保留完整的 `build/img` |
| `BUILD_HEAP_MB` | 三個 CI 工作流程中皆為 `6144` | 在每個 `.github/workflows/pages.yml` 的 env 中設定的 Node heap（hub、簡體與繁體皆為 6144）；若未設定變數，裸工具在本機會回退到 4 GiB |

`CROSS_REPO_TOKEN` 是秘密的名稱，不是要寫進文件中的值：在本機，它來自環境變數或 `.env.local`；在 CI 中，則來自 GitHub Secrets（此儲存庫的 Settings → Secrets and variables → Actions）。缺少它時，publish 會以明確錯誤失敗；dry run 不需要它。

更多設計說明請參閱 `ARCHITECTURE.md`、`TRANSLATION.md` 與 `guides/`。
