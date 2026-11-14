#!/usr/bin/env node
/**
 * Read the JSON batch summary that `npm run translate:batch -- --json` printed.
 *
 * The workflow wraps the translation in `| tee` so the job can commit progress
 * even when the batch failed; that leaves npm's own banner
 * (`> mikrotik-manual-mirror@0.1.0 translate:batch`) and the tool's progress
 * lines in the file. Only one line is machine-readable — the last one that
 * parses as the summary object — so this is the parser that decides what the
 * deploy gate sees.
 *
 * Output is a `key=value` block for `$GITHUB_OUTPUT`; every value is always
 * printed, because a missing `pending` must read as "not zero" rather than
 * letting the build job's `== '0'` comparison fail open.
 *
 * Usage:
 *   node scripts/ci/read-translate-summary.mjs --file "$RUNNER_TEMP/translate.json"
 *        >> "$GITHUB_OUTPUT"
 */

import fs from 'node:fs';

function parseArgs(argv) {
  const args = {file: null};
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--file') args.file = argv[++i];
    else if (argv[i].startsWith('--file=')) args.file = argv[i].slice('--file='.length);
  }
  return args;
}

/** The last complete summary line, or null when the run never got that far. */
export function readSummary(text) {
  const lines = String(text ?? '').split('\n');
  for (let i = lines.length - 1; i >= 0; i--) {
    const line = lines[i].trim();
    if (!line.startsWith('{')) continue;
    let value;
    try {
      value = JSON.parse(line);
    } catch {
      continue;
    }
    if (
      value &&
      typeof value === 'object' &&
      Number.isFinite(value.translated) &&
      Number.isFinite(value.pending) &&
      typeof value.stopped === 'string'
    ) {
      return value;
    }
  }
  return null;
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.file) {
    process.stderr.write('usage: node scripts/ci/read-translate-summary.mjs --file <json-log>\n');
    process.exitCode = 2;
    return;
  }
  const text = fs.existsSync(args.file) ? fs.readFileSync(args.file, 'utf8') : '';
  const summary = readSummary(text);
  if (!summary) {
    // The batch died before printing anything (missing LLM_* variables, a crash
    // in the plan). Empty pending keeps the build job from running.
    process.stderr.write('no JSON summary in the translation log; treating as "unknown, not done"\n');
    process.stdout.write('pending=\nstopped=unknown\ntranslated=0\n');
    return;
  }
  process.stdout.write(`pending=${summary.pending}\n`);
  process.stdout.write(`stopped=${summary.stopped}\n`);
  process.stdout.write(`translated=${summary.translated}\n`);
  const stepSummary = process.env.GITHUB_STEP_SUMMARY;
  if (stepSummary) {
    const limit = summary.limit ? `，触发上限 \`${summary.limit}\`` : '';
    const lines = [
      '### 中文站翻译批次',
      '',
      '| 指标 | 值 |',
      '| --- | ---: |',
      `| 本次翻译块数 | ${summary.translated} |`,
      `| 翻译标题数 | ${summary.titles ?? 0} |`,
      `| 剩余待译单位 | ${summary.pending} |`,
      `| 停止原因 | \`${summary.stopped}\`${limit} |`,
      '',
      summary.pending === 0
        ? '全部译完：继续构建并部署。'
        : '仍有待译内容：本次不构建，线上保持旧版；下一次 push 或手动触发继续。',
      '',
    ];
    fs.appendFileSync(stepSummary, `${lines.join('\n')}\n`);
  }
}

if (import.meta.url === `file://${process.argv[1]}`) main();
