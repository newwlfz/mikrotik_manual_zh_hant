# CI 与自动更新

本仓库只有**一个**工作流 `.github/workflows/pages.yml`，它把「翻译 → 构建 → 部署」
串成一条流水线：**先分批翻译，全部译完才构建发布**。

| 工作流 | 触发 | 作用 |
|---|---|---|
| `pages.yml` | push 到 `main`（`paths` 含内容根、`locales.json`、`config/**`、`i18n/**`、`work/translate/**`、`tools/translate/**`、`tools/ci/**` 等）/ 手动（可勾 `skip_translate`、`publish_on_llm_error`） | `translate` job 先预检、再跑一批翻译并提交进度 → `build` job（`pending == 0`，或 translate 被 `skip_translate` 跳过，或 LLM 失败且勾了 `publish_on_llm_error`）构建 + 部署门禁 → `deploy` job 部署 |

总管仓 `newwlfz/mikrotik_manual_i18n` 另有 `build`/`deploy` 与 `publish-content`
两个 job：它把 `CONTENT_ROOTS` 的十个内容根与 `locales.json` **用 git 推送**进
本仓库，本仓库不再下载 content release。见
[内容从哪来](#内容从哪来总管仓-git-推送)。

## 一条流水线，三道关

```text
push 内容根 / locales.json / i18n/** …  ──┐
Actions → Run workflow（可传预算 / 勾 skip_translate / 勾 publish_on_llm_error）
                                        ──┴─► translate（≤120 分钟；勾 skip_translate 时整块跳过）
                                               ├─ 预检 verify:llm --quick（1-2 秒：402/429 立即失败）
                                               │    └─ 失败 → 不翻、不写盘、不提交；只留 llm_error
                                               ├─ 有进度 → 提交 i18n/ + work/translate/ + state/
                                               └─ 输出 pending / llm_error
                                                     │
        pending == 0（或 translate 被跳过，或 llm_error 放行）──┴─── pending > 0 且不放行 ──► 跳过 build（线上保持旧版）
                          │
                          ▼
                        build（≤45 分钟）：内容根断言 → translate:verify
                          → npm run build → npm run verify:deploy → 上传制品
                          │
                          ▼
                        deploy：仅 build 成功（`!cancelled() && needs.build.result == 'success'`，永不 `always()`）
```

`translate` job 的 `timeout-minutes` 是 120，而 `--budget-minutes` 默认 90：预算到点
**优雅停止并落盘**，多出来的 30 分钟是计划、写盘、提交的余量；真被 runner 杀掉时，
已经原子写盘的页面仍然在磁盘上。

## 分批翻译（`translate` job）

### 命令与参数

```bash
# CI 里跑的就是这一条（package.json 的 translate:batch 已带 --apply）
npm run translate:batch -- --budget-minutes=90 --json

# 本地：先看还剩多少，再决定翻多少
npm run translate:pending -- --json
npm run translate:batch -- --budget-minutes=5 --max-blocks=20 --json
```

| 参数 | 含义 |
|---|---|
| `--budget-minutes=<n>` | 时间预算（分钟，可为小数）。到点**优雅停止**：当前这批已完成的块写盘，不再发新请求。`0` 表示「只检查、一块都不翻」 |
| `--max-blocks=<n>` | 本次最多处理的**翻译单位**数：一个块算 1，一个页面标题也算 1。调试/试水用；设了它就顺序执行（并发 1），保证不超 |
| `--json` | 进度写 stderr，**stdout 只有一行摘要**：`{"translated":N,"pending":M,"stopped":"budget\|done\|error",…}` |
| `--apply` | 「写盘」的同义开关（写盘本来就是默认；与 `--dry-run` 互斥） |
| `--dry-run` | 只列出本次计划（每页多少块、是否要翻标题），不请求、不写盘 |
| `--section=` / `--file=` / `--kinds=` | 局部修：只跑某个板块、某一页、只翻块或只翻标题 |
| `--limit=<n>` | 本次最多看多少**页**。默认：有预算/单位上限时**不限**（预算才是唯一的界），否则 20 页/板块 |

> 旧的 `--limit=20` 默认值会给「带预算的批次」多套一个 20 页/板块的盖子，所以
> 预算/`--max-blocks` 模式默认不再限制页数；要限制就显式传 `--limit`。

摘要里的三个键是 CI 契约，其余是附加信息（`titles`、`pending_blocks`、
`pending_titles`、`pages`、`limit`、`tokens`、`error`）：

| 键 | 含义 |
|---|---|
| `translated` | 本次写盘的**块数**（标题另计 `titles`） |
| `pending` | 跑完之后还剩多少**待译单位**（块 + 英文标题） |
| `stopped` | `budget`（预算/上限没跑完）、`done`（计划跑空）、`error`（LLM 402/401/429 等） |
| `limit` | 触发 `budget` 的具体上限：`budget-minutes`、`max-blocks` 或 `signal` |

`tools/ci/read-translate-summary.mjs` 负责从 `npm run` 的噪声日志里取出这一行
（取最后一条能解析的 JSON），并把 `pending/stopped/translated` 写成 step outputs；
**取不到时 `pending` 为空**，于是 `build` 的 `== '0'` 不成立 —— 失败是安全的一侧。

### `script_warning`：字形與地區用詞告警

譯文寫盤前會按目標語種做一次文字系統校驗（`tools/translate/lib/script-check.mjs`）：
`zh-Hant` 不允許出現簡體專用字或大陸用詞（`软件`、`网络`、`设置`、`用户`、`队列`…），
`zh-Hans` 反向檢查繁體字與臺灣用詞（`軟體`、`網路`、`設定`、`使用者`、`佇列`…）。

命中時**先帶回饋重試一次**（把命中的詞形回給模型）；仍然命中就保留這次譯文，記為
`script_warning`，不會靜默通過：

- `--json` 摘要多出 `script_warning`（數量）與 `script_warnings`（逐條 `file` /
  `kind` / `forms` / `sample`）；
- `work/translate/run.json` 同樣記錄，下一批能看到上一批留下的告警；
- `tools/ci/read-translate-summary.mjs` 把它們列在 job summary 的「中文站翻譯批次」
  表格下面，一行一條，並寫出 `script_warning=<數量>` 這個 step output。

告警不是失敗：頁面照常寫盤、照常提交，`pending` 也不受影響；它只是讓人看見「這一版
還有多少處簡體／繁體用詞沒轉乾淨」。

### 一次「增量翻译」到底做了什么

1. **计划**：对每个板块读英文源（`docs/` 等）与覆盖层（`i18n/zh-Hans/…`），
   找出覆盖层里仍是英文的块；被 `config/english-only-blocks.yml`、
   `config/translation-patches/`、keep-English 锁或 TM 判为「有意保留英文」的块跳过。
2. **请求**：按 `config/translation.yml` 的 `segmentation`（默认一次 8 块 / 8000 字符）
   分批发给 OpenAI 兼容接口；围栏代码原样保留，admonition 只翻标题与正文段落。
3. **落盘**：每完成一批就把这些块替换回页面当时的块位置，**整页原子写**
   （临时文件 + `rename`）；随后更新 `state/translation-state.json`、
   `work/translate/keep-english.json`（新发现的「保持英文」块），模型记忆最多每
   2 分钟落一次盘，停止时强制落盘。
4. **报告**：重新计划一遍得到 `pending`，写 `work/translate/run.json`，打印 JSON 摘要。
5. **提交**（workflow，不在 CLI 里）：`git add i18n work/translate state` → 有变化就
   `translate: batch (pending N) [skip ci]` 提交并 push。

### 断点续跑靠什么

| 状态 | 位置 | 作用 |
|---|---|---|
| 译文本身 | `i18n/zh-Hans/**` | **唯一真源**：已是中文的块不会被再次计划，所以「已翻过」天然续跑 |
| 保持英文的块 | `work/translate/keep-english.json`（约 640 KB，入库） | 没有它，模型会把「译不动」的技术记号每批重发一次，`pending` 永远到不了 0 |
| 页面级状态 | `state/translation-state.json`（入库） | 每页的 `status`/`pendingBlocks`；`npm run translate` 的 `status` 子命令可读 |
| 上次批次日志 | `work/translate/run.json`（入库） | 停止原因、`limit`、成本、跑完后的 `pending` |
| 代码围栏注释 | `work/translate/comment-memory.json`（入库） | 注释只翻一次 |
| 页面源指纹 | `state/translation-state.json` 的 `source_sha256` / `overlay_sha256` / `source_blocks` | 页面级 sha 判断「英文源是否变了」，块级指纹判断「哪几块变了」；只翻变化的块靠它 |
| 模型记忆 / 旧 TM | `work/translate/{model-memory,translation-memory}.json`（本仓**没有**，不入库） | 约 45 MB 的重建脚手架。本仓库没有这两份基线，所以 `translate --refresh-changed` 会**跳过并告警**（绝不把整页打回英文），批次仍按旧流程只翻覆盖层里的英文块 |
| 全局 TM 快照 | `work/translate/tm-global.*.json`（**不入库**） | 纯派生，只由 `npm run translate:tm` 手动生成 |

**本仓库为什么没有 TM 基线**：`translation-memory.json` 来自旧版语料，本仓从未有过；
`model-memory.json` 也没有入库。按「无 TM 时跳过 refresh 并告警」的规则，本仓的
`translate:batch` 带着 `--refresh-changed` 运行时只会打印一行告警，然后照常按覆盖层
规划、翻译，不会重建页面、不会把中文覆盖层打回英文。要启用「源变更只翻变化块」，
先把 `zh-Hans` 仓库的两份基线复制过来并改成语种自己的记忆（不能直接用简体译文），
或等本仓自己的 TM 基线入库。

`zh-Hans` 仓库已入库约 7.4 MB packed 的基线，并每批只追加 `shards/*.json`；
本仓的对应说明见 `tools/translate/lib/refresh.mjs` 顶部注释。

### `pending` 怎么算、怎么看

`pending` = 翻译计划的剩余单位数：**块 + 仍为英文的页面标题**。它和 `translate`
用的是同一个 `planSection`，因此它归零就意味着「下一批没有活可干」。

```bash
npm run translate:pending -- --json
# {"pending":960,"blocks":478,"titles":482,"pages":536,"sections":{...}}
```

注意区分三个「待译」：

| 口径 | 在哪 | 含义 |
|---|---|---|
| `pending`（门禁用） | `npm run translate:pending` / 批次摘要 | 计划里还剩多少单位（块 + 英文标题），**可以归零** |
| `page_list`（页面清单） | `npm run translate:pending -- --json --pages` | 同一个计划的**逐页**明细（`section`/`path`/`blocks`/`title`），job summary 用它列出「哪些页面仍是英文」 |
| `state.files[].pendingBlocks` | `state/translation-state.json` | 单页里仍是英文的块数（含被判为「有意保留英文」的块），只作参考，可能不归零 |
| `untranslatedBlocks` | `npm run translate:verify`（`lib/verify.mjs`） | 覆盖层里实际还是英文的**正文段落与警告**；它跳过以 `#`/`<`/`\|` 开头的行（标题、组件、表格），所以**比计划少**，不能当门禁 —— 本仓库它现在报 0，而计划里还有 475 块（多为标题/表格）待译 |

`verify` 报的是结构性问题（文件对齐、围栏、图片、front matter、MDX）。`build` 现在
**每次**都在 `npm run build` **之前**跑一遍 `npm run translate:verify`（约 50 秒）：
`skip_translate`、`publish_on_llm_error` 放行、正常译完三条路径都经过它。翻译完整性
由 `pending` 把关。

### 内容从哪来（总管仓 git 推送）

总管仓的 `publish-content` job 把它的 `CONTENT_ROOTS` **直接提交**进本仓库
（跨仓 fine-grained PAT `CROSS_REPO_TOKEN`）：

| 内容根 | 同步方式 |
|---|---|
| `docs/`、`versioned_docs/`、`hardware/`、`blog/`、`changelog/`、`data/`、`versioned_sidebars/` | 目录整体替换（总管仓删掉的页面这里也会消失） |
| `sidebars.ts`、`sidebars-hardware.ts`、`versions.json`、`locales.json` | 文件覆盖写 |

所以：

- `.gitignore` **不能**忽略其中任何一个。忽略 `docs/` 时翻译计划看到 0 个待译块、
  构建产出空站，属于「静默成功」，比失败更贵；忽略其它根会让对应板块整体消失。
  总管仓的 publish 会在**提交前**失败，并用 `git check-ignore -v` 打印具体规则。
- `translate` job 断言这些根不被忽略（缺根只告警，`docs/` 与 `locales.json` 缺失
  直接失败）；`build` job 的硬断言要求十个根 + `locales.json` **一个都不少**，缺失
  时打印「缺少 X；应由总管 publish 推送」。
- `static/` 不在清单里：资源来自 `ASSET_ORIGIN`（英文站），本仓库不取。

清单的唯一真源是总管仓 `tools/content/publish.mjs` 的 `CONTENT_ROOTS`。

## 跳过翻译（`skip_translate`）

`workflow_dispatch` 增加布尔输入 `skip_translate`（默认 `false`）：

```yaml
skip_translate:
  description: '跳过本轮翻译，直接用已提交的覆盖层构建（内容根断言与 translate:verify 仍会跑）'
  type: boolean
  default: false
```

- `translate` job 的 `if` 是 `${{ !inputs.skip_translate }}`；push 触发时 `inputs`
  为空，`!inputs.skip_translate` 为 true，照常翻译。
- `build` 的 `if` 接受三种放行：translate 正常跑完且 `pending == '0'`；translate
  被跳过（`needs.translate.result == 'skipped'`）；或 LLM 失败且勾了
  `publish_on_llm_error`（`llm_error` 非空，见[下一节](#llm-额度失效预检与-publish_on_llm_error)）。
  翻译失败（`result == 'failure'`）永不构建。表达式里带 `!cancelled()`：GitHub 在
  `if` 没有状态函数时会隐式套 `success()`，而它对**被跳过**的依赖 job 为 false，
  不加就进不了 skip 分支。
- 勾选后 `build` **仍然**做内容根断言，并显式跑 `npm run translate:verify`，所以
  文件不对齐、围栏/图片/front matter/MDX 坏掉的覆盖层不会被发布。

**用途**：只改站点代码 / 配置 / 样式；刚在本地验证过覆盖层、想立刻上线；或 LLM
接口暂时不可用但内容已经齐备。

**风险**：

1. 本次**不推进 `pending`**：未译块仍是英文，站点会带着英文段落上线；
2. 长期勾选会让翻译停摆，`pending` 永远不降；
3. 它只跳过「翻译」这一步，不跳过任何结构校验。不要用它绕过 `pending` 门禁去发布
   半翻译站 —— 正常（未勾选）流水线在 `pending > 0` 时依然不会构建。

只在需要“马上上线”时手动勾选一次，用完取消。

## LLM 额度/失效（预检与 `publish_on_llm_error`）

额度用完（402）、key 失效（401）、被限流（429）时**默认不动线上**：`translate` job
失败 → `build` 不跑 → 线上保持上一个成功版本。为了让这种失败**早发生**（而不是花钱
跑了 20 分钟才死），流水线在批量翻译之前先做一次预检。

### 预检：`verify:llm --quick`

```bash
npm run verify:llm -- --quick   # CI 里跑的就是这一条（约 1-2 秒）
```

- 发一个 `max_tokens=8` 的请求，只问「key 能不能用、账户有没有钱」：**2xx 就算通过**，
  推理模型把 8 个 token 全花在 `reasoning_content` 上、`content` 为空也没关系；
- 超时上限 30 秒（`--quick` 会把 `LLM_TIMEOUT_MS` 再压到 30 秒），正常 1-2 秒；
- 只有 401/402/403/429 会额外打印一行 `llm_error=<code>`，其他失败（404、5xx、超时、
  配置缺失）没有这一行；
- 预检失败 → **不启动批量翻译、不写盘、不提交任何东西**（不会产生
  `translate: batch` 提交，`i18n/`、`state/` 都不动）。

`--max-tokens=<n>` 可以改请求预算；`--dry-run` 仍然只校验配置、不发请求。

### 失败后的三种结局

| 失败类型 | `publish_on_llm_error` | `translate` job | `build` | 线上 |
| --- | --- | --- | --- | --- |
| 401/402/403/429（预检或批次中途） | `false`（默认） | 失败 | 跳过 | **保持上一个成功版本** |
| 401/402/403/429（预检或批次中途） | `true` | **成功** | 跑（`translate:verify` + 全部部署门禁） | **发布，未译内容为英文** |
| 超时 / 5xx / 网络 / 配置缺失 / 404 等 | 任意 | 失败 | 跳过 | 保持上一个成功版本 |

批量翻译**中途**失败（跑了一半才 402）走同一套判断：已完成的块**先提交**（提交步骤
的条件是「这一批真的跑了」，不是 `success()`），`pending` 保持为剩余数，然后由
`publish_on_llm_error` 决定是否继续 `build`。

### `publish_on_llm_error` 的适用场景与风险

手动触发（Actions → **Translate, build and deploy** → `Run workflow`）时勾选
`publish_on_llm_error`。`build` 的门禁是：

```text
!cancelled() && needs.translate.result != 'failure'
  && (needs.translate.result == 'skipped'          # 勾了 skip_translate
      || needs.translate.outputs.pending == '0'    # 正常译完
      || (needs.translate.outputs.llm_error != '' && inputs.publish_on_llm_error == true))
```

- `needs.translate.result != 'failure'`：没勾选时 gate 会把 job 判失败，这一条直接拦住；
- `needs.translate.outputs.llm_error != ''`：只有**带 HTTP 状态**的 LLM 失败才可能
  放行；超时、5xx、配置缺失不带状态码，**勾了也不会放行**；
- `inputs.publish_on_llm_error == true`：push 触发时 `inputs` 为空，永远为假 ——
  自动流水线不会因为「上次勾过」而放行。

**适用场景**：内容已更新（新页面、改过的示例、CLI 表格），翻译只差一部分，而额度要
过一阵才恢复。先让结构完整的新内容上线、未译段落暂时保持英文，比整站停在旧版更有用。

**风险（必须知道）**：

1. **会发布部分英文内容**：未译的正文段落、警告块，以及仍为英文的**页面标题**，都会
   以英文出现在中文站上；
2. `pending` 不会因此下降，这些单位会一直留着，直到额度恢复后再跑；
3. 它**不跳过任何结构校验**：`build` 依然跑内容根断言、`translate:verify` 与
   `verify:deploy`，坏掉的覆盖层不会被发布；
4. 不要把它设成默认值 —— 长期放行等于让翻译停摆。

### 恢复后怎么重跑

1. 充值 / 换 key / 解除限流（`LLM_BASE_URL` 是仓库 Variable，`LLM_API_KEY` 是
   Secret，见 [LLM 指南](LLM.md#github-actions-配置位置)）；
2. 本地先确认：`npm run verify:llm -- --quick` 应打印
   `OK: LLM preflight passed`（失败时日志里有 `llm_error=<code>`）；
3. Actions → **Translate, build and deploy** → `Run workflow`，**不要**勾
   `publish_on_llm_error`；
4. 批次从断点继续（已翻的块不会重发），`pending` 归零后自动 `build` + 部署；
5. 想立刻补上一轮放行留下的英文，用 `max-blocks` 分几次跑也行，每次结束都会提交进度。

### 在哪里看「哪些页面仍是英文」

`translate` job 的 summary 里有一节 **「中文站：LLM 预检与发布决策」**：`pending`、
`llm_error`、是否放行，以及 **仍为英文的页面清单**（前 15 页 + 总数，来自
`npm run translate:pending -- --json --pages`，与门禁用同一个计划）。放行发布时
`build` job 的 summary 还会再写一条「⚠️ 本次为放行发布：仍有英文内容」。

> 清单**不**读 `state/translation-state.json`：那里的 `pendingBlocks` 还包含「有意
> 保留英文」的块，永远不归零，会把几百个已经译完的页面也列进来。

## 手动触发与恢复

| 场景 | 做法 |
|---|---|
| 想立刻跑一批 | Actions → **Translate, build and deploy** → `Run workflow`。`budget-minutes` 默认 90；只想试水就填 `max-blocks`（例如 `20`） |
| 只想上线代码、不想跑翻译 | 同一个手动触发里勾选 `skip_translate`。translate 被跳过，但 `build` 仍断言内容根并跑 `translate:verify`；风险见[上一节](#跳过翻译skip_translate) |
| 预算用完还有 pending | 正常现象：job 成功、`pending>0`、跳过构建。再触发一次（或等下一次 push）继续，已翻的块不会重翻 |
| LLM 402/401/403/429 | 预检就会失败（不跑批量、不提交），job 失败、`build` 不跑；批次中途失败时**已完成的块先提交**。充值/换 key 后重跑即可；确实要带着英文上线，见 [LLM 额度/失效](#llm-额度失效预检与-publish_on_llm_error)里勾选 `publish_on_llm_error` 的那一节 |
| 想看哪些页面还是英文 | `npm run translate:pending -- --json --pages`，或直接看 `translate` job 的 summary |
| 想从头看还剩多少 | `npm run translate:pending -- --json`，或看最近一次提交的 `work/translate/run.json` |
| 某一页翻坏了 | `npm run translate:batch -- --section=docs --file=<rel> --max-blocks=50`，然后 `npm run translate:verify` |
| 想让某个块强制重翻 | 把它加进 `config/force-translate.yml`（该文件里的块不会被 keep-English 跳过） |
| 构建失败 | 不部署，线上保持旧版；本地用 `npm run verify:deploy` 复现 |

本地等价命令：

```bash
node tools/translate/index.mjs pending --json          # 还剩多少（不请求、不写盘）
node tools/translate/index.mjs pending --json --pages  # 还剩多少 + 逐页清单
npm run verify:llm -- --quick                          # 预检（max_tokens=8，约 1-2 秒）
node tools/translate/index.mjs translate --dry-run     # 本批会翻哪些块
npm run translate:batch -- --budget-minutes=10 --json  # 真跑一小批
npm run translate:verify                               # 结构校验（覆盖层）
node tools/pipeline/translate.mjs                      # 旧的离线重建路径（apply/derive）
npm run build && npm run verify:deploy                 # 构建 + 部署门禁
```

### 用假 LLM 验证分批与断点

接口是 OpenAI 兼容的（`POST <LLM_BASE_URL>/chat/completions`），所以本地可以用一个
几十行的 mock 端到端验证「分批 / 断点 / 预算」。mock 只要把每个输入块原样加上中文前缀
（保持块结构），并把每个请求体写进日志：

```js
// mock.mjs —— node mock.mjs 8931 requests.jsonl
import http from 'node:http';
import fs from 'node:fs';
const [port, log] = [Number(process.argv[2]), process.argv[3]];
http.createServer((req, res) => {
  let body = '';
  req.on('data', (c) => (body += c));
  req.on('end', () => {
    const user = JSON.parse(body).messages.find((m) => m.role === 'user').content;
    fs.appendFileSync(log, `${JSON.stringify({user})}\n`);
    const han = (text) => `中译：${text}`;
    const content = user.includes('page title')
      ? '中译标题'
      : user.includes('documentation description')
        ? '中译描述'
        : user.split(/\n[ \t]*\n/).map(han).join('\n\n');
    res.writeHead(200, {'content-type': 'application/json'});
    res.end(JSON.stringify({choices: [{message: {content}, finish_reason: 'stop'}]}));
  });
}).listen(port, '127.0.0.1');
```

```bash
node mock.mjs 8931 /tmp/requests.jsonl &
export LLM_BASE_URL=http://127.0.0.1:8931/v1 LLM_MODEL=mock LLM_API_KEY=test

# 翻两块：只发一页的两块，pending 减 2，覆盖层出现两段「中译：」
npm run translate:batch -- --section=docs --file=<rel> --max-blocks=2 --json
# 再跑一次：请求日志里只有剩下的块，前两块不会再发（断点续跑）
npm run translate:batch -- --section=docs --file=<rel> --max-blocks=2 --json
# 预算 0：translated=0、pending 不变、exit 0、零请求
npm run translate:batch -- --budget-minutes=0 --json
```

实测口径（2026-11-14，本仓库）：

| 场景 | `translated` | `pending` | `stopped` | `limit` | exit |
|---|---:|---:|---|---|---:|
| 首次 `--max-blocks=2`（该页 3 块） | 2 | 960 → 958 | `budget` | `max-blocks` | 0 |
| 续跑 `--max-blocks=2`（同页剩 1 块） | 1 | 958 → 957 | `done` | — | 0 |
| `--budget-minutes=0` | 0 | 957（不变） | `budget` | `budget-minutes` | 0 |
| LLM 402（首批标题成功后） | 0 | 957 → 956 | `error` | — | 1 |

「未开始就停」还有一条：`--budget-minutes=0` 时连覆盖层都不碰（`pages=0`），
不会为每个板块重写一个字节相同的文件。


## 地区用词层（`localize:hant`，zh-Hant 专属）

覆盖层里的繁体字来自一次性的 OpenCC `s2twp` 引导（见 README「引导来源」）。
OpenCC 只换字形和它自己的词表，**换不动地区用词**：台湾写 `資料` 不写 `数据`、
`程式` 不写 `程序`、`重設` 不写 `重置`。第二层由 `config/zh-hant-terms.yml`
驱动：

```bash
npm run localize:hant:check    # 只报告会改哪些文件/处数，有差异 exit 1
npm run localize:hant          # 幂等写回 i18n/zh-Hant/**
```

- **这是 zh-Hant 仓库自己的层，不是通用机制**：总管仓的 `locale:add` 与
  `tools/translate` 都不知道它，也不要接进去——每个语种都有自己的地区用词。
- 只替换正文：代码块、行内代码、链接地址、锚点、MDX 表达式跳过；链接标题与
  HTML/JSX 属性值是可见文本，会替换。
- `pages.yml` 的 build job 在构建前跑 `localize:hant`（幂等，无差异时零改动），
  所以「审阅发现新词 → 加进 YAML → 重建」就能闭环，不需要模型调用。
- 构建前还有一步 `localize:hant:check`（`continue-on-error: true`，只提示）：
  词表改了但忘记提交覆盖层时，CI 会打印提示并在构建前就地修好，不拦发布；
  想让它成为硬门禁时把 `continue-on-error` 去掉即可。
- 浏览器语言 → 目标语种（`zh-TW`/`zh-HK` → 繁体站、`zh-CN`/`zh-SG` → 简体站、
  其它语言不跳）由 `tools/content/locales.js` 的一张表决定，单测在
  `npm run test:redirect`；build job 会跑它。

## 部署门禁（`pages.yml`）

`build` job 的顺序是 `npm run build` → `npm run verify:deploy` → `configure-pages`
→ `upload-pages-artifact`。`verify:deploy` 先跑 `build:slim`，再跑四条断言；任何一个
非 0 就停在构建阶段，不产出 Pages 制品，`deploy` 不会执行：

| 步骤 | 断言内容 |
|---|---|
| `npm run verify:assets` | 产物与源 Markdown 里没有 locale 前缀资源引用、没有双哈希 PDF、没有指向不存在文件的引用 |
| `npm run verify:base-url` | 资源型根绝对引用（`img`/`video`/`link`/`og:image` 等）都在 `baseUrl` 之下 |
| `npm run verify:orphan-assets` | 站内 `/img/<file>` 引用都有对应文件（无 `static/` 时跳过本地存在性检查） |
| `npm run verify:llms` | `llms.txt` / `llms-full.txt` 里的站内链接都指向存在的产物文件 |

顺序不能反：`slim` 会删掉 `build/<locale>/{img,assets/images,assets/files}` 并把 URL
改回根副本，先断言只会报「产物里还有 locale 前缀」；`verify:deploy` 已经把顺序固定好
（`slim && asset-refs && base-url-refs && orphan-assets && llms-links`）。
`verify:llms`（`tools/verify/llms-links.mjs`）补的是别的断言看不见的一类断链：
`llms.txt` 里是绝对 URL 字符串而不是路由，`onBrokenLinks` 与浏览器检查都不管。

门禁与 `build` 必须看到同一组 `SITE_URL` / `BASE_URL` / `ASSET_ORIGIN`：它们来自
workflow 级 `env`（见下），`slim` 也按 `BASE_URL` 重写产物里的绝对 URL。

## 站点身份（`locales.json` + 环境变量）

站点地址的唯一事实源是仓库根的 **`locales.json`**（`docusaurus.config.ts` 由它生成
`i18n.locales` 与 `localeConfigs`；`tools/lib/site-config.mjs` 也用同一份）。本仓库的
`locales.json` 由总管仓逐字节推送，**不要在这里改**。

`pages.yml` 的 workflow 级 `env` 再把本仓的部署地址显式写一遍（值必须与
`locales.json` 的 `zh-Hans` 条目一致），并可用仓库 Variables 覆盖：

| 变量 | 本仓库取值 | 说明 |
|---|---|---|
| `SITE_LOCALE` | `zh-Hans` | 本次构建的语种；`tools/build/index.mjs` 据此只构建一个语种 |
| `SITE_URL` | `https://newwlfz.github.io` | origin（不带尾斜杠、不带仓库路径） |
| `BASE_URL` | `/mikrotik_manual_zh_hans/` | 站点子路径（首尾都要有 `/`） |
| `LOCALE_EN_*` / `LOCALE_ZH_*` | 两个站的 origin / 前缀 | 语言下拉与 `hreflang` 指到**另一个仓库的站点** |
| `ASSET_ORIGIN` | `https://newwlfz.github.io/mikrotik_manual_i18n` | 共享资源源站，见下一节 |
| `BUILD_HEAP_MB` | `6144` | 静态渲染峰值；本地 10 GiB 堆会 OOM |

翻译凭据是另一组，缺任何一个都会让 `translate` job 明确失败（不会静默跳过）：

| 变量 | 位置 | 含义 |
|---|---|---|
| `LLM_BASE_URL` / `LLM_MODEL` | Repository **Variable** | OpenAI 兼容接口与模型（见 [LLM.md](LLM.md)） |
| `LLM_API_KEY` | Repository **Secret** | 接口 key（旧名 `OPENCODE_API_KEY` 已弃用） |

`SITE_URL` / `BASE_URL` 写错不会报错，只会把整站 canonical / sitemap 指向错域名；
`BASE_URL` 还决定 `slim` 重写绝对 URL 的前缀，所以它与 `locales.json` 必须一致。

## 共享资源（`ASSET_ORIGIN`）

英文站是**资源宿主**。中文站不再保存 `static/`：图片、PDF、视频、抓取页与
CLI 数据都留在英文仓，构建时把资源引用改写到该源站。

| `ASSET_ORIGIN` | 行为 |
| --- | --- |
| 未设置（英文站） | 站内绝对引用加本站 `baseUrl`，与旧行为完全一致 |
| 设置（语种站） | `/img/`、`/assets/`、`/videos/`、`/official/`、`/cli/` 改写为 `${ASSET_ORIGIN}/…`；页面路由（`/docs/`、`/hardware/`、`/blog/`、`/changelog/`）仍走本站 |

值是英文站的**基址**（含仓库路径前缀、不带尾斜杠）：
`https://newwlfz.github.io/mikrotik_manual_i18n`。它只写在中文仓的
`pages.yml` 里；英文站构建不设置。

改写发生在（两个仓代码逐字节相同）：

- `tools/build/remark-prefix-root-refs.mjs`：raw HTML/JSX 属性 **以及**
  Markdown 图片/链接目标。它同时注册在 `beforeDefaultRemarkPlugins`，否则
  `transformImage` 会把 `![](/img/…)` 当成本地文件 `require()`，而没有
  `static/` 的语种仓会直接构建失败。
- `customFields.assetBaseUrl = ASSET_ORIGIN || baseUrl`：`<Img>`、导航 Logo、
  favicon 与 `og:image`。
- `tools/build/llms.mjs`：`llms-full.txt` 与插件生成的每页 `.md` 副本。
- `staticDirectories: []`：遗留的 `static/` 被**忽略**（构建会打印警告），
  不会发布。
- `tools/cli/build-all.mjs`：生成的 CLI 数据（约 7 MiB）写进 `work/cli/`
  而不是 `static/cli/`，语种仓构建不会再重新造出 `static/` 树。但
  `cli-compare.json` 仍发布在本站根：它由 `fetch()` 读取，需要 CORS，
  而资源宿主不返回 `Access-Control-Allow-Origin`。
- `tools/verify/asset-refs.mjs` 统计外链并跳过它们的本地存在性检查；
  `tools/verify/orphan-assets.mjs` 在无 `static/img` 时跳过孤儿扫描；
  `tools/build/slim.mjs` 只输出 `external assets: N refs`，不再剪枝。

仍然发布在本站的：pagefind 索引（`customFields.localAssetBaseUrl`）、
Webpack chunk/字体，以及每页 `docs/**/img` 目录里的图片。

### 英文站必须保留完整的 `/img` 树（`ASSET_HOST`）

英文站不只是给读者看的站点，它还是**语种站的资源宿主**，所以它的产物比
普通站点多一条约束：英文仓 `pages.yml` 里的 `ASSET_HOST=true` 会让 slim
保留完整的 `build/img`（约 99 MiB）。否则 slim 会按**英文页面**的引用剪枝，
而英文的 Markdown 图片走 `assets/images`，几乎整个 `/img` 都会被删掉——中文
页面要的正是这些 `/img/<name>`（404）。

多出的约 88 MiB 就是共享的代价；目前 Pages 站点仍在 1 GB 预算内。以后资源
迁到独立 CDN 时，托管完整 `static/` 树即可，这条约束自然消失。

**失效风险**：`ASSET_ORIGIN` 把所有语种站绑在英文站地址上。英文仓改名、
换域名或改路径前缀，会同时打断**所有**语种站的图片、PDF 与视频；任何这类
变更必须在同一次改动里更新每个语种仓 `pages.yml` 的 `ASSET_ORIGIN`。以后
换独立 CDN 不需要改代码：把 `ASSET_ORIGIN` 指向 CDN、把 `static/` 树同步
过去即可。

本地验证（英文资源在 3020 的 `/mikrotik_manual_i18n/` 下，中文站在 3021）：

```bash
# 英文仓：把 build/ 挂在 /mikrotik_manual_i18n/ 路径下提供静态服务
# 中文仓：对着它构建，再跑部署门禁
ASSET_ORIGIN=http://127.0.0.1:3020/mikrotik_manual_i18n \
SITE_URL=http://127.0.0.1:3021 BASE_URL=/mikrotik_manual_zh_hans/ \
SITE_LOCALE=zh-Hans npm run build
ASSET_ORIGIN=http://127.0.0.1:3020/mikrotik_manual_i18n npm run verify:deploy
```

外链模式下 `verify:deploy` 必须 exit 0：外链只统计数量，不查 `build/` 里
是否存在。

## 发布彩排（本地，不 push）

`pages.yml` 只有 push 之后才会跑，但它的每一步都能在本地原样复现。
`tools/build/rehearse-pages.mjs` 按 `pages.yml` 的顺序跑构建 → 瘦身 → 四条门禁，
再按 `actions/upload-pages-artifact@v3` 的方式打包（`tar --dereference
--hard-dereference`），最后起一个按 `baseUrl` 服务的静态服务器抽查 URL，
并把全部数字写进 `work/pages-rehearsal.json`（`work/` 已被 `.gitignore` 忽略，不入库）。

```bash
# 全流程：构建 + 瘦身 + 门禁 + 打包 + URL 抽查 + browser-check
SITE_URL=https://newwlfz.github.io BASE_URL=/mikrotik_manual_zh_hans/ \
ASSET_ORIGIN=https://newwlfz.github.io/mikrotik_manual_i18n SITE_LOCALE=zh-Hans \
  node tools/build/rehearse-pages.mjs

# 复用现有 build：只重量 tar/gzip、抽查 URL、跑浏览器检查
node tools/build/rehearse-pages.mjs --skip-build

# 没有 Chrome（vendor/browsers）时跳过最后一步
node tools/build/rehearse-pages.mjs --skip-browser
```

一次成功的彩排应当看到（下面是 commit `11cf24f1d`、2026-11-14 的实测值）：

| 项 | 期望 |
|---|---|
| `build:lowmem` | exit 0，约 13–14 分钟（6 GiB 堆） |
| `build:slim` | exit 0，约 10 秒 |
| 四条门禁 | 全部 exit 0（合计约 18 秒） |
| `du -sb build` | ≈ 1.15 GB（1.07 GiB） |
| tar（artifact 口径） | ≈ 1.19 GB（1.11 GiB），远低于 10 GB |
| `gzip -9` 体积 | ≈ 364 MB（347 MiB），只作上传参考 |
| 文件 / 目录 | ≈ 47,900 文件 / 12,400 目录 / 0 符号链接 |
| 抽查 URL | 13 条全部 200，且 `content-length` 与磁盘文件一致 |
| `node tools/verify/browser-check.mjs` | 29/29 |

tar 比 `du -sb` 大约 4,200 万字节，是 tar 的 512 字节块填充与目录项开销，不是产物变多。

### 本地彩排不能替代真实部署

- 本机若用 `build:lowmem`（6 GiB 堆），与 `pages.yml` 的 `BUILD_HEAP_MB=6144` 相同；
  若直接 `npm run build` 而不设 `BUILD_HEAP_MB`，wrapper 会退到 10 GiB 堆，本机
  15 GiB 内存会 OOM。产物相同，**构建耗时不可直接类比**。
- 没有跑 `npm ci`：用的是工作区已有的 `node_modules`。依赖树是否与
  `package-lock.json` 完全一致，只有真实 CI 能确认。
- 本地彩排**不会**跑 `translate` job：翻译进度是否完整只看 `pending`，而它由
  翻译 job 的摘要决定，本地只能用 `npm run translate:pending -- --json` 近似。
- 静态服务器只模拟 `baseUrl` 下的路径解析（`/`、`index.html`、`.html` 回退、404），
  不模拟 CDN、压缩、HTTP/2 与 Pages 的 404 回退细节。
- **1 GB 的 “published site” 上限是否硬性拒绝，本地无法证明。** GitHub 文档把它写成
  发布站点的上限（[GitHub Pages 限制](https://docs.github.com/zh/pages/getting-started-with-github-pages/github-pages-limits)），
  但上传侧只受 10 GB artifact 限制；超限究竟是拒绝部署、部分 404，还是仅告警，
  只有一次真实部署能定论。
- 仓库 Variables（`LLM_BASE_URL` / `LLM_MODEL`）、Secret（`LLM_API_KEY`）与
  总管仓的 `CROSS_REPO_TOKEN` 是否已经设置，本地看不到。缺 `LLM_*` 时翻译 job
  明确失败；缺 `CROSS_REPO_TOKEN` 时总管仓的 publish 明确失败（不会静默跳过）。

如果真实部署因为体积被拒，回退顺序（数字以彩排实测为准）：

1. 去掉一个归档版本（7.24 约 226 MiB → 剩约 872 MiB）；
2. 只留当前 7.26（去掉 7.24 + 7.25 → 约 642 MiB）；
3. 中英文拆成两个 Pages 站点（英文约 640 MiB、中文约 457 MiB）。

Pages 发布失败时会保留上一次成功的部署，站点不会因为一次超限立刻下线；
但新内容也就不会上线，所以体积问题要在合并前解决，而不是等部署时报错。

PDF 附件链接一律写成裸 HTML 锚点
（`<a href="/assets/files/<name>.pdf" target="_blank" rel="noopener">…</a>`）：
Markdown 链接会被 `mdx-loader` 的 `transformLinks` 改写成 `require()`，再由
`otherAssets` 加载器给已经带内容哈希的文件名**再加一个哈希**
（`<stem>-<sha>-<sha>.pdf`），产物因此翻倍（约 60 MB）。锚点不经过 `transformLinks`，
`href` 的 `baseUrl` 由 `tools/build/remark-prefix-root-refs.mjs` 补；转换由
`tools/sync/sync-pdfs.mjs` 与 `tools/translate/fix-asset-links.mjs` 调用
`tools/translate/lib/pdf-links.mjs` 完成，两者都是幂等的。
