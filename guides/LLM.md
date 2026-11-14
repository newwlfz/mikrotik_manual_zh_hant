# LLM 配置（翻译）

`tools/translate` 会把仍是英文的文本块发到一个兼容 OpenAI chat-completions
的接口。接口地址、模型和密钥属于连接配置，不是仓库内容：它们从不入库，
`config/translation.yml` 也不再保存它们。

## 变量

| 名称 | 必填 | 默认值 | 含义 |
| --- | --- | --- | --- |
| `LLM_BASE_URL` | 是 | — | 兼容 OpenAI 的 API 基地址，例如 `https://opencode.ai/inference/go/v1`。以 `/v1` 结尾时自动补 `/chat/completions`；已经带 `/chat/completions` 的完整地址原样使用。尾部斜杠会被忽略；查询串和片段会被拒绝。 |
| `LLM_MODEL` | 是 | — | 精确的模型名，例如 `deepseek-v4.1-flash`。 |
| `LLM_API_KEY` | 是 | — | 服务商密钥。**只认这个变量名。** |
| `LLM_TIMEOUT_MS` | 否 | `120000` | 单次请求超时，毫秒。 |
| `LLM_MAX_RETRIES` | 否 | `3` | 可重试失败（`408`、`429`、`5xx`、超时、网络错误）后的重试次数；`0` 表示不重试。 |
| `LLM_EXTRA_HEADERS` | 否 | — | 额外请求头的 JSON 对象，例如 `{"X-Org":"team"}`；不得设置 `Authorization`。 |
| `LLM_SESSION_ID` | 否 | 每进程一个 UUID | Go 通道上 `x-opencode-session` 的值；仅在 `LLM_EXTRA_HEADERS` 没有显式给出该头时读取。 |

所有工具输出和日志里，`LLM_API_KEY` 只显示前 4 位和后 4 位（如
`oc_s…DKIc`），绝不打印完整值。

`OPENCODE_API_KEY` 已弃用，请改名（**deprecated, rename it to
`LLM_API_KEY`**）。检测到旧名时工具会打印警告。

## 通道：Go 与 zen

OpenCode 用两个端点提供同一批模型，规则不同：

| 通道 | `LLM_BASE_URL` | 要求 |
| --- | --- | --- |
| **Go** | `https://opencode.ai/inference/go/v1` | 每个请求都必须带 `x-opencode-session`；不带会得到 `400 MissingSessionID`。 |
| **zen** | `https://opencode.ai/zen/v1` | 按量付费（pay-as-you-go）：不需要 session 头，但**余额为 0 会返回 `402 payment_required`**。 |

只要 `LLM_BASE_URL` 的路径里含 `/inference/go`，`tools/translate` 就会自动补
session 头：

1. `LLM_EXTRA_HEADERS` 里显式写了 `x-opencode-session` → 以用户值为准（任何通道都如此）；
2. 否则用 `LLM_SESSION_ID`；
3. 都没有时，为当前进程生成一个随机 UUID 并复用（一个批次共用一个 session）。

其它端点（`zen`、普通服务商 URL）**不会**加这个头。`verify:llm` 会把它打印成
`session header : auto`（或用户值，或 `(not needed)`），这样 `400
MissingSessionID` 和密钥错误就能区分开。

## 取值顺序

按下面的顺序取第一个非空值：

1. `process.env`（CI 就是这样注入的）；
2. `<仓库根>/.env.local`；
3. `<工作区根>/.env.local`，即仓库的上一级目录。

文件不会覆盖 `process.env` 中已经存在的值。解析支持 `KEY=VALUE`、
`export KEY=VALUE`、`#` 注释行、单/双引号包裹和行尾空白。

## GitHub Actions 配置位置

在运行翻译的仓库（`mikrotik_manual_zh_hans`）里配置：

1. **Settings → Secrets and variables → Actions**；
2. **Variables** 页（非密钥，日志可见）：
   - `LLM_BASE_URL`
   - `LLM_MODEL`
   - 可选：`LLM_TIMEOUT_MS`、`LLM_MAX_RETRIES`、`LLM_EXTRA_HEADERS`、
     `LLM_SESSION_ID`
3. **Secrets** 页（打码）：
   - `LLM_API_KEY`

翻译工作流需要把它们映射进 job 环境，例如：

```yaml
env:
  LLM_BASE_URL: ${{ vars.LLM_BASE_URL }}
  LLM_MODEL: ${{ vars.LLM_MODEL }}
  LLM_API_KEY: ${{ secrets.LLM_API_KEY }}
  LLM_TIMEOUT_MS: ${{ vars.LLM_TIMEOUT_MS }}
  LLM_MAX_RETRIES: ${{ vars.LLM_MAX_RETRIES }}
```

变量为空时工具**不会**回退到默认 endpoint 或模型：
`verify:llm --dry-run` 和翻译任务都会直接报出缺哪个变量。

## 本地使用

```bash
cp .env.local.example .env.local
# 填入 LLM_BASE_URL、LLM_MODEL、LLM_API_KEY
node tools/translate/verify-llm.mjs --dry-run
node tools/translate/verify-llm.mjs
node tools/translate/verify-llm.mjs --quick   # CI 预检：max_tokens=8，只看额度/鉴权
```

`.env.local` 在两个仓库都已被 git 忽略。放在仓库根或工作区根都可以：
仓库根优先，`process.env` 优先于两者。

## 自检

`npm run verify:llm -- --dry-run`：只校验变量是否齐全、URL 是否合法、数值
是否有效，打印脱敏后的配置；成功 `exit 0`，失败 `exit 1` 并列出缺少的变量
和查找过的文件。

`npm run verify:llm`：发一个最小请求（`把 hello 翻译成中文`，
`max_tokens: 256`），打印脱敏后的 base URL、模型、session 头决策、HTTP
状态、耗时和返回文本；返回内容里应出现「你好」。

`max_tokens: 256`（而不是 32）是有意为之：推理模型会先吐 reasoning token
再给答案，32 时额度全被推理吃掉，`content` 会是空的。遇到这种情况工具会明确
提示「推理吃掉了额度」，打印 `reasoning_content` 前 120 字并 `exit 1`，而不是
笼统地说「没有 content」。

`npm run verify:llm -- --quick`：**CI 用的预检**。同一个请求，但
`max_tokens: 8`、超时压到 30 秒，只判断「key 能不能用、账户有没有钱」：

- **2xx 就算通过**（推理模型把 8 个 token 全用在 reasoning 上、`content` 为空也
  没关系，会打印 `OK: LLM preflight passed`）；
- 401/402/403/429 会额外打印一行 `llm_error=<code>`，供
  `.github/workflows/pages.yml` 的放行判断读取；其他失败（404、5xx、超时）没有这
  一行，因此永远不会被放行；
- `--max-tokens=<n>` 可以改预算；`--dry-run` 仍然什么都不发。

`translate` job 就是先跑这一条，再决定要不要开始批量翻译（见
[CI 指南](CI.md#llm-额度失效预检与-publish_on_llm_error)）。

| 结果 | 含义与处理 |
| --- | --- |
| `200` + 中文 | 连接正常。 |
| `400` `MissingSessionID` | Go 通道没收到 `x-opencode-session`。只要 `LLM_BASE_URL` 含 `/inference/go` 工具会自动补；先确认 URL 是 Go 通道，或设置 `LLM_SESSION_ID`。 |
| `401` | `LLM_API_KEY` 无效或已吊销，换新 key。 |
| `402` | key 有效但账户余额不足（`zen` 是按量付费通道），去服务商充值，或改用 Go 通道。 |
| `404` | 端点或模型名错：检查 `LLM_BASE_URL`（通常以 `/v1` 结尾）和精确的 `LLM_MODEL`。 |
| `429` | 被限流：稍后重试、减小批次，或调大 `LLM_MAX_RETRIES`。 |
| 超时 | 调大 `LLM_TIMEOUT_MS`，或检查到服务商的网络。 |
| `content` 空、`reasoning_content` 非空 | 推理吃掉了输出额度：调大 `max_tokens` 或换非推理模型（`--quick` 下这是**正常**的）。 |
| 缺变量 | 按报错列出的变量名，在环境变量、`<仓库>/.env.local` 或 `<工作区>/.env.local` 中补齐。 |

## 不需要配置 LLM 的仓库

只有运行 `tools/translate` 的仓库需要 `LLM_*`。**总管仓（hub/content 仓库）
和英文站构建都不调用 LLM，不需要任何变量或密钥**；密钥只放在翻译仓库。
