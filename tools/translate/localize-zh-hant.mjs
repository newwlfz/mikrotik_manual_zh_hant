#!/usr/bin/env node
/**
 * Regional wording layer for the Traditional Chinese overlays.
 *
 * `i18n/zh-Hant/**` is Simplified→Traditional output from the one-off OpenCC
 * bootstrap (`tools/bootstrap/convert-s2twp.py`). OpenCC converts **characters
 * and a phrase table**; it cannot know that Taiwan writes 資料 instead of 数据,
 * 程式 instead of 程序, or 重設 instead of 重置. This tool applies that second,
 * purely local layer, driven by `config/zh-hant-terms.yml`.
 *
 * It is **zh-Hant-specific by design**: the hub's `locale:add` flow and the
 * generic translation pipeline know nothing about it, and they must not, because
 * every locale has its own regional wording. Reviewing a page and adding a pair
 * to the YAML is the whole workflow — no model call.
 *
 * Properties:
 *   - **idempotent**: a replaced term equals its target, so a second run is a
 *     no-op; `--check` therefore exits 0 on a clean tree.
 *   - **structure-safe**: fenced code, inline code, link destinations, URLs,
 *     `{#anchors}` and MDX `{...}` expressions are skipped; quoted link titles
 *     and HTML/JSX attribute values are converted (they are visible text).
 *   - **front matter**: only prose keys (`title`, `sidebar_label`,
 *     `description`) are touched; identifiers, URLs and machine state are not.
 *
 * Usage:
 *   npm run localize:hant            # --write: rewrite i18n/zh-Hant/**
 *   npm run localize:hant:check      # --check: report only, exit 1 on changes
 *   node tools/translate/localize-zh-hant.mjs --check --json
 */

import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import YAML from 'yaml';

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const OVERLAY_ROOT = path.join(REPO, 'i18n/zh-Hant');
const TERMS_FILE = path.join(REPO, 'config/zh-hant-terms.yml');

/** Front-matter keys that carry identifiers, URLs or machine state. */
const FRONTMATTER_KEEP = new Set([
  'id',
  'slug',
  'sidebar_key',
  'sidebar_position',
  'sidebar_class_name',
  'displayed_sidebar',
  'tags',
  'keywords',
  'image',
  'draft',
  'source',
  'captured_at',
  'translated_at',
  'translation_provider',
  'translation_model',
  'translation_source_hash',
  'source_hash',
  'hide_table_of_contents',
  'pagination_next',
  'pagination_prev',
  'custom_edit_url',
  'format',
]);

const FENCE_OPEN = /^[ \t]*(`{3,}|~{3,})(.*)$/;
const FENCE_CLOSE = /^[ \t]*(`{3,}|~{3,})[ \t]*$/;
const FRONTMATTER_LINE = /^([A-Za-z0-9_-]+):(.*)$/;

/**
 * Structural spans inside one line. Each match is copied; the gaps are prose.
 * Inline code is a backtick run closed by a run of the same length (CommonMark),
 * which is why the pattern uses a backreference instead of `.+?`.
 */
const PROTECTED =
  /(?<code>(?<ticks>`+).*?(?<=\k<ticks>))|(?<dest>\](?:\((?:[^()\\]|\\.)*\)|\s*\[[^\]]*\]))|(?<html><[^>]*>)|(?<url>(?:https?|ftp):\/\/[^\s<>"'，。；：、（）【】「」『』！？…\u3000-\u303f\uff00-\uffef\u3400-\u9fff]+)|(?<brace>\{[^{}]*\})/g;
const QUOTED = /(["'])(.*?)\1/g;

/** Read and validate `config/zh-hant-terms.yml`. */
export function loadTerms(file = TERMS_FILE) {
  if (!fs.existsSync(file)) return [];
  const parsed = YAML.parse(fs.readFileSync(file, 'utf8')) || {};
  const terms = [];
  for (const entry of parsed.terms || []) {
    const from = String(entry?.from ?? '').trim();
    const to = String(entry?.to ?? '').trim();
    if (!from || !to) continue;
    if (from === to) continue;
    if ([...from].length < 2) {
      // Single-character pairs belong to the character layer (OpenCC); allowing
      // them here would rewrite words the reviewer never looked at.
      process.stderr.write(
        `note: skipping single-character term "${from}" (character mappings belong to OpenCC)\n`,
      );
      continue;
    }
    terms.push({from, to, note: entry.note || null});
  }
  // Longest source first: `数据包` must win over `数据`.
  terms.sort((a, b) => b.from.length - a.from.length);
  return terms;
}

/** Replace terms in one piece of prose. */
function applyToText(text, terms, hits) {
  let out = text;
  for (const term of terms) {
    if (!out.includes(term.from)) continue;
    const count = out.split(term.from).length - 1;
    out = out.split(term.from).join(term.to);
    hits.set(term.from, (hits.get(term.from) || 0) + count);
  }
  return out;
}

function applyToQuoted(text, terms, hits) {
  return text.replace(QUOTED, (match, quote, value) => {
    const converted = applyToText(value, terms, hits);
    return converted === value ? match : `${quote}${converted}${quote}`;
  });
}

/** One line of prose, with structural spans protected. */
export function convertLine(line, terms, hits) {
  let out = '';
  let cursor = 0;
  for (const match of line.matchAll(PROTECTED)) {
    if (match.index > cursor) {
      out += applyToText(line.slice(cursor, match.index), terms, hits);
    }
    const groups = match.groups || {};
    if (groups.html || groups.dest) out += applyToQuoted(match[0], terms, hits);
    else out += match[0];
    cursor = match.index + match[0].length;
  }
  if (cursor < line.length) out += applyToText(line.slice(cursor), terms, hits);
  return out;
}

/** Front matter: prose values only. */
function convertFrontMatter(block, terms, hits) {
  let currentKey = null;
  return block
    .split('\n')
    .map((line) => {
      const match = FRONTMATTER_LINE.exec(line);
      if (match) {
        currentKey = match[1];
        if (FRONTMATTER_KEEP.has(currentKey)) return line;
        const converted = convertLine(match[2], terms, hits);
        return `${currentKey}:${converted}`;
      }
      if (currentKey === null || FRONTMATTER_KEEP.has(currentKey) || !line.trim()) return line;
      if (line.trim() === '---') return line;
      return convertLine(line, terms, hits);
    })
    .join('\n');
}

/** Convert a whole document; returns `{text, hits}`. */
export function convertDocument(source, terms) {
  const hits = new Map();
  let front = '';
  let body = source;
  if (source.startsWith('---\n')) {
    const end = source.indexOf('\n---\n', 4);
    if (end !== -1) {
      front = source.slice(0, end + 5);
      body = source.slice(end + 5);
    }
  }
  const convertedFront = front ? convertFrontMatter(front, terms, hits) : '';
  const lines = body.split('\n');
  const out = [];
  let fence = null;
  let inComment = false;
  for (const line of lines) {
    const closer = FENCE_CLOSE.exec(line);
    if (fence !== null) {
      if (closer && closer[1][0] === fence[0] && closer[1].length >= fence.length) fence = null;
      out.push(line);
      continue;
    }
    const opener = FENCE_OPEN.exec(line);
    if (opener) {
      fence = opener[1];
      out.push(line);
      continue;
    }
    if (inComment) {
      out.push(line);
      if (line.includes('-->')) inComment = false;
      continue;
    }
    const start = line.indexOf('<!--');
    if (start !== -1 && !line.slice(start).includes('-->')) {
      out.push(convertLine(line.slice(0, start), terms, hits) + line.slice(start));
      inComment = true;
      continue;
    }
    out.push(convertLine(line, terms, hits));
  }
  return {text: convertedFront + out.join('\n'), hits};
}

function* markdownFiles(root) {
  if (!fs.existsSync(root)) return;
  for (const entry of fs.readdirSync(root, {withFileTypes: true})) {
    if (entry.name.startsWith('.')) continue;
    const full = path.join(root, entry.name);
    if (entry.isDirectory()) yield* markdownFiles(full);
    else if (/\.mdx?$/.test(entry.name)) yield full;
  }
}

function main(argv) {
  const args = new Set(argv);
  const write = args.has('--write');
  const check = args.has('--check') || !write;
  const json = args.has('--json');
  const terms = loadTerms();
  const files = [];
  const totals = new Map();
  let occurrences = 0;

  for (const file of markdownFiles(OVERLAY_ROOT)) {
    const source = fs.readFileSync(file, 'utf8');
    const {text, hits} = convertDocument(source, terms);
    if (text === source) continue;
    const relative = path.relative(REPO, file).split(path.sep).join('/');
    let fileCount = 0;
    for (const [from, count] of hits) {
      totals.set(from, (totals.get(from) || 0) + count);
      fileCount += count;
    }
    occurrences += fileCount;
    files.push({file: relative, occurrences: fileCount, terms: [...hits.entries()]});
    if (write) fs.writeFileSync(file, text);
  }

  files.sort((a, b) => b.occurrences - a.occurrences);
  if (json) {
    process.stdout.write(
      `${JSON.stringify(
        {
          mode: write ? 'write' : 'check',
          terms: terms.length,
          files: files.length,
          occurrences,
          byTerm: [...totals.entries()]
            .sort((a, b) => b[1] - a[1])
            .map(([from, count]) => ({from, count})),
          changed: files,
        },
        null,
        2,
      )}\n`,
    );
  } else {
    for (const entry of files.slice(0, 15)) {
      process.stdout.write(
        `  ${String(entry.occurrences).padStart(4)}  ${entry.file}\n`,
      );
    }
    const top = [...totals.entries()].sort((a, b) => b[1] - a[1]).slice(0, 10);
    if (top.length) {
      process.stdout.write(
        `terms: ${top.map(([from, count]) => `${from}×${count}`).join(', ')}\n`,
      );
    }
    process.stdout.write(
      `[localize:hant] ${write ? 'rewrote' : 'would rewrite'} ${files.length} file(s), ` +
        `${occurrences} occurrence(s) with ${terms.length} term(s) from config/zh-hant-terms.yml\n`,
    );
  }

  if (check && files.length > 0 && !write) {
    process.stdout.write(
      '[localize:hant] the overlays do not match config/zh-hant-terms.yml; ' +
        'run `npm run localize:hant` and commit the result.\n',
    );
    process.exitCode = 1;
  }
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  main(process.argv.slice(2));
}
