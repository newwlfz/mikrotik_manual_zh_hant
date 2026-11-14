# MikroTik 手册 — 繁体中文镜像站

**本仓库只构建 `zh-Hant` 一个语种。** 英文站是另一个仓库
（`repo_en`）、另一个 GitHub Pages 站点；两个仓库共用**同一份**
`docusaurus.config.ts` 与仓库根的 `locales.json`（语种登记表，由总管仓推送），
站点之间的全部差异由登记表 + 环境变量提供（见 [部署变量](#部署变量)）。繁体站
不产生 `build/zh-Hant/` 子目录：`build/` 根就是繁体站。

## 引导来源：一次性的简→繁转换（不再重复）

本仓库的覆盖层不是逐页翻译出来的：它由**一次性**转换生成——把
`mikrotik_manual_zh_hans` 的 `i18n/zh-Hans/**` 复制过来，用 OpenCC 的
**`s2twp`**（台湾正体 + 台湾词汇表）转成繁体，并保留 Markdown 结构、代码块、
链接、锚点与 front matter 标识符不变。

- 转换脚本：`tools/bootstrap/convert-s2twp.py`。文件头写明
  `ONE-OFF: Simplified→Traditional bootstrap only`：它**没有**接进
  `package.json`、`tools/translate/**`、总管仓的 `locale:add` 或 CI，
  也不是「新语种」流程的一部分。
- 之后的**新增内容仍走正常翻译流程**（`tools/translate` + 模型），不要期待
  任何自动繁简转换：没有第二条转换链路，也不该有。
- 首次引导的统计（字符级/词汇级替换、高频对照表、待人工审阅的词）见
  提交说明与 `reports/zh-hant-conversion.md`。

## 地区用词层（`npm run localize:hant`）

OpenCC 换的是**字形**和它的词表；台湾用词（`数据`→`資料`、`程序`→`程式`、
`重置`→`重設`）是另一层。这一层由 `config/zh-hant-terms.yml` 驱动：

```bash
npm run localize:hant          # 幂等替换 i18n/zh-Hant/**，无差异时零改动
npm run localize:hant:check    # 只报告；有差异时 exit 1
```

- **这是 zh-Hant 专属的本地化层，不是通用机制**：不要搬进总管仓或
  `locale:add`，别的语种有自己的地区用词表。
- 审阅时发现新的词对，加进 YAML 再跑一次即可，不需要模型；`pages.yml` 在构建前
  会跑一次 `localize:hant`（幂等），所以「审阅 → 加词 → 重建」闭环。
- 词表里标 `# review` 的条目是「有把握但值得再看一眼」的，优先人工抽查。

## 仓库职责（本仓只管「中文怎么说」）

| 归属 | 内容 | 在哪 |
|---|---|---|
| **本仓库** | 译文覆盖层 `i18n/zh-Hant/**`（4,704 个文件，约 4.3 MB，唯一繁体真源） | 入库 |
| **本仓库** | 翻译策略：`config/translation.yml`、术语表 `config/glossary/`、`config/translation-patches/`、`config/english-only-blocks.yml`、`config/force-translate.yml` | 入库 |
| **本仓库** | 翻译进度：`work/translate/{keep-english,run,comment-memory}.json` + `state/translation-state.json` | 入库 |
| **本仓库** | 站点代码与站点级配置：`src/`、`tools/`、`docusaurus.config.ts`（`sidebars*.ts`、`versions.json`、`versioned_sidebars/`、`locales.json` 由总管仓推送） | 入库 |
| 总管仓 `mikrotik_manual_i18n` | 英文内容：`docs/`、`versioned_docs/`、`hardware/`、`blog/`、`changelog/`、`data/`、`sidebars.ts`、`sidebars-hardware.ts`、`versioned_sidebars/`、`versions.json`，以及 `locales.json`（`publish-content` job 用 git 推送进来） | **入库，由总管仓提交** |
| 总管仓 `mikrotik_manual_i18n` | 资源 `static/`（图片、PDF、视频） | **不在本仓库**（构建时引用英文站） |
| 两者共享 | 构建期把站内资源引用改写到 `ASSET_ORIGIN`（英文站基址） | — |

繁体站的**翻译流水线**（分批翻译 → 全部译完才构建发布）见
[guides/CI.md](guides/CI.md)。

- 文档源：<https://manual.mikrotik.com/> 的镜像内容（英文正文）+
  `i18n/zh-Hant/` 翻译覆盖层；
- **`static/` 不是本仓库的内容**：图片、PDF、视频、抓取页与 CLI 数据留在
  英文站（资源宿主），构建时把资源引用改写到 `ASSET_ORIGIN`（见
  [guides/CI.md 的「共享资源」](guides/CI.md#共享资源asset_origin)）；
- 产物：约 527 MB（23,249 个文件，含 pagefind 索引），全部路由在
  `build/` 根；`llms.txt`/`llms-full.txt` 只写中文，`pagefind` 索引
  6,079 个中文页（另有 1 个英文页是抓取下来的 WebFig 示例
  `assets/295239801_index2.html`，带 `lang="en"`）。

## 翻译流水线（一句话）

`.github/workflows/pages.yml` 在 push / 手动触发时先跑**一批**翻译
（`--budget-minutes=90`，可中断、可续跑），有进度就提交回 `main`；摘要里的
`pending` 归零才构建并部署，否则线上保持旧版。命令、断点文件与失败处理见
[guides/CI.md](guides/CI.md)。

```bash
npm run translate:pending -- --json          # 还剩多少待译单位
npm run translate:batch -- --budget-minutes=5 --json   # 本地跑一小批
npm run translate:verify                     # 覆盖层结构校验
```

## 手动跳过翻译（`skip_translate`）

手动触发（Actions → **Translate, build and deploy** → `Run workflow`）勾选
`skip_translate` 后，`translate` job 整块跳过，`build` 直接用已提交的
`i18n/zh-Hant/` 覆盖层构建并部署。

- **用途**：只改了站点代码 / 配置 / 样式，或刚在本地验证过覆盖层、想立刻上线，
  不想再花一轮翻译预算和 1–2 小时等待。
- **不会被跳过的校验**：`build` 仍断言全部内容根，并跑
  `npm run translate:verify`（文件对齐、代码围栏、图片、front matter、MDX
  结构校验）；任何一项坏了都不会发布，所以不会上线结构损坏的站。
- **风险**：跳过翻译意味着**本次不推进 `pending`**。未译的块仍保持英文，站点会
  带着英文段落上线；而正常（未勾选）的流水线在 `pending > 0` 时依旧不会构建。
  不要用它绕过 `pending` 门禁去“发布半翻译站”——它只适合内容已齐备、只是不想
  再跑翻译的场景，且跳过期间不会有新的译文入库。

## 快速开始

```bash
npm ci                        # 或本地复用英文仓的依赖：ln -s ../repo_en/node_modules node_modules
npm run content:fetch         # 本地预览用：从 ../repo_en 取内容（CI 直接用总管仓推送的内容根）
SITE_URL=http://127.0.0.1:3013 BASE_URL=/mikrotik_manual_zh_hant/ SITE_LOCALE=zh-Hant \
LOCALE_EN_URL=http://127.0.0.1:3013 LOCALE_EN_BASE_URL=/mikrotik_manual_i18n/ \
LOCALE_ZH_URL=http://127.0.0.1:3013 LOCALE_ZH_BASE_URL=/mikrotik_manual_zh_hant/ \
ASSET_ORIGIN=http://127.0.0.1:3013/mikrotik_manual_i18n \
BUILD_HEAP_MB=6144 npm run build
ASSET_ORIGIN=http://127.0.0.1:3013/mikrotik_manual_i18n npm run verify:deploy
```

`npm run build` 依次执行：CLI 数据生成 → `docusaurus build --locale
zh-Hant --out-dir build` → `pagefind` → `tools/build/llms.mjs`。

## 内容获取

内容（英文正文与构建数据）**不在这里维护**，由总管仓 `mikrotik_manual_i18n`
的 `publish-content` job 用 **git 推送**进来：

| 来源 | 内容根 | 本仓库怎么处理 |
|---|---|---|
| 总管仓 git 推送 | `docs/`、`versioned_docs/`、`hardware/`、`blog/`、`changelog/`、`data/`、`versioned_sidebars/` | 目录整体替换（总管仓删掉的页面这里也会消失） |
| 总管仓 git 推送 | `sidebars.ts`、`sidebars-hardware.ts`、`versions.json`、`locales.json` | 文件覆盖写 |
| 英文站（`ASSET_ORIGIN`） | `static/`（图片、PDF、视频） | **不在本仓库**；构建时把资源引用改写到英文站 |

这些路径都**必须被 git 跟踪**：`.gitignore` 忽略任一根时，总管仓的 publish 会在
**提交前**直接失败（`git check-ignore -v` 会指出具体规则），`pages.yml` 也会在
translate / build 前断言。清单的唯一真源是总管仓 `tools/content/publish.mjs`
的 `CONTENT_ROOTS`。

本地预览还可以用 `npm run content:fetch` 从兄弟仓 `../repo_en` 复制（这是
**本地替身**，CI 不调用）：

```bash
node tools/content/fetch-local.mjs                 # 从 ../repo_en 复制
node tools/content/fetch-local.mjs --source=../repo_en --only=docs,hardware
node tools/content/fetch-local.mjs --dry-run
```

它按文件复制，目标已存在且大小相同就跳过（第二次运行几乎零成本），并把
来源 commit、各 section 的文件数/字节数写进 `.content/fetch.json`。

`static/` **不取**：内容包里虽然带着它（英文站需要），但繁体站通过
`ASSET_ORIGIN` 引用英文站的资源。`--url` 模式解压时用 `tar --exclude`
跳过 `static/`，并删除可能残留的旧副本；本地复制模式发现遗留 `static/`
只打印警告（构建会忽略它）。

## 部署变量

所有语种仓库共用**同一份** `docusaurus.config.ts`，站点地址的默认值来自仓库根的
`locales.json`（由总管仓逐字节推送，**不要在这里改**）；下面的环境变量可以覆盖它，
`pages.yml` 里显式写了本仓的取值：

| 变量 | 缺省（`locales.json`） | 含义 |
| --- | --- | --- |
| `SITE_LOCALE` | `en` | 本次构建产出的语种；繁体站固定传 `zh-Hant` |
| `SITE_URL` | `https://newwlfz.github.io`（两个站点相同 origin） | 本站绝对域名（`canonical`/`hreflang`） |
| `BASE_URL` | 本语种的 `baseUrl`：`/mikrotik_manual_i18n/` 或 `/mikrotik_manual_zh_hant/` | 本站路径前缀 |
| `LOCALE_EN_URL` / `LOCALE_EN_BASE_URL` | 登记表里 `en` 的 `site` / `baseUrl` | 英文站地址 |
| `LOCALE_ZH_URL` / `LOCALE_ZH_BASE_URL` | 登记表里 `zh-Hant` 的 `site` / `baseUrl` | 繁体站地址 |
| `ASSET_ORIGIN` | 空（本地资源） | 共享资源源站：英文站基址，含路径前缀、不带尾斜杠。繁体站设为 `https://newwlfz.github.io/mikrotik_manual_i18n`，`/img/`、`/assets/`、`/videos/`、`/official/`、`/cli/` 全部改写到它 |
| `BUILD_HEAP_MB` | `10240` | Node 堆上限（`build:lowmem` 与 CI 都用 6144） |
| `LLM_BASE_URL` / `LLM_MODEL` / `LLM_API_KEY` | 无 | 翻译接口、模型与 key（仓库 Variable / Secret）；缺失时翻译 job 明确失败 |

`localeConfigs.en` / `localeConfigs['zh-Hant']` 由 `locales.json` 生成，带
`url`/`baseUrl`/`htmlLang`/`label`。这些显式值有两个作用：语言下拉与
`hreflang` 指向**另一个仓库的站点**，而不是本产物的 `/zh-Hant/` 子目录；
同时 Docusaurus 由 `baseUrl - siteConfig.baseUrl` 推导非默认语种的输出
目录，显式值让 `--locale zh-Hant` 也写到 `build/` 根。

`translate` 只对**本次构建的语种**打开（`siteLocale === 'zh-Hant'`）：在
Docusaurus 3.10 里它不只是“是否导出翻译清单”，还决定 docs 插件是否读
`i18n/<locale>/`、navbar/footer/sidebar 标签是否翻译。英文仓构建时该值
恒为 `false`，与本仓共用同一份配置而不受影响。

## 路由

| 内容 | 繁体站（本仓库） | 英文站（`repo_en`） |
| --- | --- | --- |
| RouterOS 当前版 | `/mikrotik_manual_zh_hant/docs/...` | `/mikrotik_manual_i18n/docs/...` |
| RouterOS 归档版 | `/mikrotik_manual_zh_hant/docs/<version>/...` | `/mikrotik_manual_i18n/docs/<version>/...` |
| 硬件指南 | `/mikrotik_manual_zh_hant/hardware/...` | `/mikrotik_manual_i18n/hardware/...` |
| 产品新闻 | `/mikrotik_manual_zh_hant/blog/...` | `/mikrotik_manual_i18n/blog/...` |
| 文档变更 | `/mikrotik_manual_zh_hant/changelog/...` | `/mikrotik_manual_i18n/changelog/...` |

当前文档版本是 7.26（`data/manifests/current-version.json`），归档版本是
7.25 与 7.24（`versions.json`）。

## 跨站语言入口

- 语言下拉：`localeDropdown` 直接使用两个 `localeConfigs` 的
  `url`+`baseUrl`，在中文页点「English」是整页跳转到英文站同一路径；
- `hreflang`：每页输出 `en`、`zh-Hant` 与 `x-default` 三条 `alternate`，
  分别指向两个站点的同一路径；`canonical` 指向繁体站自身；
- 首屏脚本：`<head>` 里的自动跳转脚本**只在 `SITE_LOCALE=en` 时注入**。
  繁体站已经是目标语种，不做「跳中文」逻辑（
  `src/clientModules/locale-detect.js` 也读
  `<meta name="docusaurus-site-locale">` 做同样的短路）。

## 目录

```text
repo_zh_hans/
├─ locales.json             # 语种登记表（总管仓逐字节推送，勿手改）
├─ config/                  # 翻译策略：translation.yml、glossary/、patches/、force-translate.yml
├─ i18n/zh-Hant/            # 中文翻译覆盖层（唯一的中文真源）
├─ src/                     # 主题、组件、客户端模块
├─ tools/                   # 构建 / 校验 / 翻译 / 内容获取
│  ├─ translate/            # 分批翻译（translate/pending/apply/verify）
│  ├─ ci/read-translate-summary.mjs   # 把 --json 摘要读成 workflow outputs
│  ├─ content/{locales.js,fetch-local.mjs}
│  └─ build/{index,slim,llms}.mjs
├─ docs/ versioned_docs/ hardware/ blog/ changelog/ data/ versioned_sidebars/
│                          # 内容，总管仓 git 推送 → 必须跟踪（不能忽略）
├─ sidebars.ts sidebars-hardware.ts versions.json   # 同理，由总管仓推送
│                          # （static/ 不在此列：资源在英文站，见 ASSET_ORIGIN）
├─ work/translate/          # 翻译状态：keep-english.json / run.json / comment-memory.json 入库，
│                          # 大块 TM 与模型记忆仍 git-ignored
└─ work/verify/             # 本地双站点联调脚本与报告，git-ignored
```

## 本地双站点联调

`work/verify/multisite-local.mjs` 在同一个端口上同时挂载两个产物：

```text
/mikrotik_manual_i18n/*      -> ../repo_en/build
/mikrotik_manual_zh_hant/*   -> build
/                            -> 302 英文站
```

它用 Playwright 走完整浏览器路径，验证英文入口、语言下拉互跳、
`hreflang`/`canonical`、归档版本路由与产物形状，输出逐条 JSON：

```bash
node work/verify/multisite-local.mjs          # 需要两个产物都已构建
node work/verify/multisite-local.mjs --json
```

## 已知未完成项

- **翻译记忆（TM）**：`work/translate/` 里只有**小状态**入库
  （`keep-english.json`、`run.json`、`comment-memory.json`，合计约 0.7 MB）；
  `model-memory.json`、`translation-memory.json`、`tm-global.*.json`
  （约 79 MB 的重建脚手架）仍不入库 —— 每个批次都会重写它们，入库等于每次
  往仓库里塞几十 MB。断点续跑不依赖它们：覆盖层 + keep-English 锁足够。
- **内容根已覆盖，站点级配置仍各自维护**：总管仓 `publish-content` 现在推送
  `CONTENT_ROOTS` 的十个根 + `locales.json`，`build` 的内容根断言不会再缺板块。
  `config/`（翻译策略、术语表、patches）、`docusaurus.config.ts`、`tools/`、
  `src/` 属于**语种仓自有**，不随内容发布，两边需要**人工同步**；如果将来要把
  语种专属配置也交给总管统一管理，需要单独设计（例如只发布 `config/` 的公共
  子集，保留语种覆盖层）。
- **pagefind 的 1 个英文页**：`assets/295239801_index2.html` 是抓取下来的
  WebFig 示例（自带 `lang="en"`），pagefind 因此报告 1 个英文页；如需
  严格“只索引中文”，在 `pagefind` 参数里加 `--exclude "assets/*.html"`。
- **`slim` 适配**：单语种产物下 `tools/build/slim.mjs` 只做
  `build/img` 剪枝；繁体站的 `build/img` 引用与英文站一致，但没有针对
  中文资源目录做额外裁剪。
