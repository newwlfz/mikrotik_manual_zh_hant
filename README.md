# MikroTik RouterOS Manual — 繁體中文 (zh-Hant)

**This repository builds the `zh-Hant` site only.** The English site is a
different repository ([`newwlfz/mikrotik_manual_i18n`](https://github.com/newwlfz/mikrotik_manual_i18n)) and a
different GitHub Pages deployment; both share the same `docusaurus.config.ts`
and the same root `locales.json` (the locale registry, pushed here by the hub).
Everything that differs between the sites comes from the registry plus
environment variables — no site address is written into the config.

Repository <https://github.com/newwlfz/mikrotik_manual_zh_hant> · deployed at <https://newwlfz.github.io/mikrotik_manual_zh_hant/>.

## What this repository owns

| Owner | Content | Where |
| --- | --- | --- |
| **This repository** | Translation overlays `i18n/zh-Hant/**` (the only copy of the `繁體中文` wording) | committed |
| **This repository** | Translation policy: `config/translation.yml`, `config/glossary/`, `config/translation-patches/`, `config/english-only-blocks.yml` | committed |
| **This repository** | Translation progress: `work/translate/*.json` and `state/translation-state.json` | committed |
| **This repository** | Site code and site-level configuration: `src/`, `tools/`, `docusaurus.config.ts`, `.github/workflows/pages.yml` | committed |
| Hub `newwlfz/mikrotik_manual_i18n` | English content: `docs/`, `versioned_docs/`, `hardware/`, `blog/`, `changelog/`, `data/`, `sidebars.ts`, `sidebars-hardware.ts`, `versioned_sidebars/`, `versions.json`, and `locales.json` | **committed here, written by the hub's `publish-content` job** |
| Hub `newwlfz/mikrotik_manual_i18n` | Assets `static/` (images, PDFs, video) | **not in this repository** (referenced from the hub at build time) |
| Shared | Build-time rewrite of asset references to `ASSET_ORIGIN` (the hub's base address) | — |

Never edit a content root by hand: the hub replaces those trees wholesale on the
next publish, and a hand edit is lost without a warning. Wording belongs in
`i18n/zh-Hant/` (generated) or in `config/`.

The locale profile (`config/locale-profiles/<locale>.md`) and glossary
(`config/glossary/<locale>.yml`) are contributed by each language maintainer
through a PR. A change only guides *new* translation output; existing wording
stays as committed until a refresh (`--refresh-changed`) runs.

## Translation pipeline

`.github/workflows/pages.yml` runs one translate batch per push (or on manual
dispatch, with a time budget), commits its progress back to `main`, and only
builds and deploys when `pending` reaches 0. A failed batch leaves the previous
deployment live. The endpoint, model and API key are **not** in this repository:

| Kind | Name | Purpose |
| --- | --- | --- |
| Actions variable | `LLM_BASE_URL` | OpenAI-compatible endpoint |
| Actions variable | `LLM_MODEL` | model name |
| Actions secret | `LLM_API_KEY` | API key |

Set them under *Settings → Secrets and variables → Actions*. Without them the
translate job fails fast on its preflight request and nothing is published.

```bash
npm ci
npm run translate:pending -- --json     # how many units are left
npm run verify:llm -- --quick           # preflight (max_tokens=8)
npm run translate:batch -- --budget-minutes=5 --json   # one short local batch
npm run translate:verify                # overlay structure check
npm run build                           # CLI model + Docusaurus + Pagefind
```

The pipeline in depth is documented in [`TRANSLATION.md`](TRANSLATION.md); the
tools in [`tools/README.md`](tools/README.md).

## Deployment variables

`pages.yml` sets these; the defaults below are what a new site starts from.

| Variable | Value | Meaning |
| --- | --- | --- |
| `SITE_LOCALE` | `zh-Hant` | The single locale this build produces |
| `SITE_URL` | `https://newwlfz.github.io` | This site's origin (`canonical`, `hreflang`) |
| `BASE_URL` | `/mikrotik_manual_zh_hant/` | This site's path prefix |
| `ASSET_ORIGIN` | `https://newwlfz.github.io/mikrotik_manual_i18n` | Shared asset origin (the hub's base address, no trailing slash) |
| `BUILD_HEAP_MB` | `4096` | Node heap for the build |

The other locales' addresses come from `locales.json`; do not hardcode them.
`LOCALE_<PRIMARY_SUBTAG>_URL` / `_BASE_URL` exist for local previews only
(`zh-Hant` → `ZH`).

## First run

The repository is scaffolded by the hub's `npm run locale:add` and contains no
content yet. Until the hub publishes for the first time, `pages.yml` stops at
its "verify content roots" step (there is no `docs/` yet); that is expected.
Run the hub's publish (`npm run content:publish -- --only=zh-Hant`) and the
next run has content to translate and build.
