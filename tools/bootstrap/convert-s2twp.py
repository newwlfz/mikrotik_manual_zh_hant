#!/usr/bin/env python3
"""
ONE-OFF: Simplified→Traditional bootstrap only; not part of the generic locale pipeline.

This repository (`mikrotik_manual_zh_hant`) was seeded once from the Simplified
overlays of `mikrotik_manual_zh_hans`. This script is the tool that did it: it
copies `i18n/zh-Hans/**` to `i18n/zh-Hant/**` and converts the Chinese prose with
OpenCC's **s2twp** configuration (Taiwan standard + Taiwan phrase table).

It is deliberately **not** wired into `package.json`, `tools/translate/**`, the
hub's `locale:add` flow or CI. New content is translated by the normal (LLM)
pipeline in `tools/translate`; nothing re-runs a Simplified→Traditional pass.
Keep it here as a record of how the bootstrap was produced (and as the only
honest way to redo it if the overlay tree is ever rebuilt from scratch).

Requirements: Python 3.8+, the system OpenCC library (`libopencc1.1`) and its
data files (`/usr/share/opencc/s2twp.json`). No Python packages.

Usage (from the repository root):

    # overlays: ../repo_zh_hans/i18n/zh-Hans -> i18n/zh-Hant
    python3 tools/bootstrap/convert-s2twp.py \
        --source ../repo_zh_hans/i18n/zh-Hans \
        --target i18n/zh-Hant \
        --stats ../work/zh-hant-conversion.json

    # glossary and page patches, one file at a time:
    python3 tools/bootstrap/convert-s2twp.py --file ../repo_zh_hans/config/glossary/zh-Hans.yml \
        --out config/glossary/zh-Hant.yml

Structure is preserved: code fences, inline code, link destinations, absolute
URLs, HTML tags, HTML comments, MDX `{...}` expressions (including `{#anchors}`)
and the front-matter keys that carry identifiers are copied byte for byte. Only
the Chinese prose in between is converted, so `translate:verify` keeps passing.

Exit codes: 0 = converted, 1 = usage/config error, 2 = OpenCC unavailable.
"""

from __future__ import annotations

import argparse
import ctypes
import ctypes.util
import difflib
import json
import os
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

OPENCC_LIBRARY_CANDIDATES = (
    os.environ.get("OPENCC_LIBRARY", ""),
    "/usr/lib/x86_64-linux-gnu/libopencc.so.1.1",
    "/usr/lib/x86_64-linux-gnu/libopencc.so.1",
    "/usr/lib/libopencc.so.1",
    "/usr/local/lib/libopencc.so.1",
    ctypes.util.find_library("opencc"),
)
OPENCC_DATA_DIR = os.environ.get("OPENCC_DATA_DIR", "/usr/share/opencc")

# Front-matter keys whose values are identifiers, URLs or machine state: they
# must survive byte for byte. Everything else (`title`, `sidebar_label`,
# `description`) is prose and gets converted.
FRONTMATTER_KEEP = {
    "id",
    "slug",
    "sidebar_key",
    "sidebar_position",
    "sidebar_class_name",
    "displayed_sidebar",
    "tags",
    "keywords",
    "image",
    "draft",
    "source",
    "captured_at",
    "translated_at",
    "translation_provider",
    "translation_model",
    "translation_source_hash",
    "source_hash",
    "hide_table_of_contents",
    "pagination_next",
    "pagination_prev",
    "custom_edit_url",
    "format",
}

# CommonMark: an opening fence may carry an info string, a closing fence may not.
FENCE_OPEN = re.compile(r"^[ \t]*(`{3,}|~{3,})(.*)$")
FENCE_CLOSE = re.compile(r"^[ \t]*(`{3,}|~{3,})[ \t]*$")
HAN_RUN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]+")
FRONTMATTER_LINE = re.compile(r"^([A-Za-z0-9_-]+):(.*)$")

# Protected spans inside one line of prose. Every alternative is copied as-is;
# the gaps between matches are the only text OpenCC sees.
PROTECTED = re.compile(
    # Inline code: a backtick run closed by a run of the **same** length.
    r"(?P<code>(?P<ticks>`+).*?(?P=ticks))"
    # Link/image destination, or reference label.
    r"|(?P<dest>\](?:\((?:[^()\\]|\\.)*\)|\s*\[[^\]]*\]))"
    # HTML / JSX tag: quoted attribute values are prose (`<ArgTable c1="参数">`),
    # so only the quotes are protected here and the values are converted below.
    r"|(?P<html><[^>]*>)"
    # Absolute URL: ASCII only. A URL followed by Chinese prose used to swallow
    # the rest of the line because the negated class did not stop at CJK.
    r"|(?P<url>(?:https?|ftp)://[^\s<>\"'\u3000-\u303f\uff00-\uffef\u3400-\u9fff]+)"
    # MDX expression, including `{#anchors}` and JSX props.
    r"|(?P<brace>\{[^{}]*\})"
)

# `"..."` / `'...'` inside a link destination or a tag: the visible title or
# attribute text, which is prose even though its container is structural.
QUOTED = re.compile(r"([\"'])(.*?)\1")


class OpenCC:
    """Minimal binding to the OpenCC C API (`opencc_open`, `opencc_convert_utf8`)."""

    def __init__(self, config: str) -> None:
        path = next((candidate for candidate in OPENCC_LIBRARY_CANDIDATES if candidate), None)
        if not path or not os.path.exists(path):
            print(
                "OpenCC library not found; install libopencc1.1 or set OPENCC_LIBRARY",
                file=sys.stderr,
            )
            raise SystemExit(2)
        self.lib = ctypes.CDLL(path)
        self.lib.opencc_open.restype = ctypes.c_void_p
        self.lib.opencc_open.argtypes = [ctypes.c_char_p]
        self.lib.opencc_convert_utf8.restype = ctypes.c_void_p
        self.lib.opencc_convert_utf8.argtypes = [
            ctypes.c_void_p,
            ctypes.c_char_p,
            ctypes.c_size_t,
        ]
        self.lib.opencc_convert_utf8_free.argtypes = [ctypes.c_void_p]
        self.lib.opencc_close.argtypes = [ctypes.c_void_p]
        self.lib.opencc_error.restype = ctypes.c_char_p

        config_path = config if os.path.isabs(config) else os.path.join(OPENCC_DATA_DIR, config)
        self.handle = self.lib.opencc_open(config_path.encode())
        if self.handle in (None, ctypes.c_void_p(-1).value):
            print(f"OpenCC could not load {config_path}: {self._error()}", file=sys.stderr)
            raise SystemExit(2)

    def _error(self) -> str:
        message = self.lib.opencc_error()
        return message.decode(errors="replace") if message else "unknown error"

    def convert(self, text: str) -> str:
        if not text:
            return text
        raw = text.encode()
        pointer = self.lib.opencc_convert_utf8(self.handle, raw, len(raw))
        if not pointer:
            print(f"OpenCC conversion failed: {self._error()}", file=sys.stderr)
            raise SystemExit(2)
        try:
            return ctypes.string_at(pointer).decode()
        finally:
            self.lib.opencc_convert_utf8_free(pointer)

    def close(self) -> None:
        if self.handle:
            self.lib.opencc_close(self.handle)
            self.handle = None


@dataclass
class Stats:
    """Conversion ledger for the review report.

    Classification is measured per run of Han characters: a run is converted
    with `s2tw` (character/variant level) and with `s2twp` (adds the Taiwan
    phrase table). Whatever `s2tw` already explains is a character conversion;
    whatever only `s2twp` produces is a vocabulary replacement, recorded as
    "Simplified word -> Traditional word" for the review table.
    """

    files_converted: int = 0
    files_skipped: int = 0
    char_conversions: int = 0
    char_pairs: Counter = field(default_factory=Counter)
    phrase_conversions: int = 0
    phrase_pairs: Counter = field(default_factory=Counter)
    structural_edits: int = 0
    extra_passes: int = 0
    phrase_contexts: dict = field(default_factory=lambda: __import__("collections").defaultdict(Counter))
    unparseable: list = field(default_factory=list)

    def add(self, original: str, converted: str, tw, twp) -> None:
        for run in HAN_RUN.findall(original):
            traditional = tw(run)
            if len(traditional) != len(run):
                # Defensive: the character tables are 1:1, a length change here
                # would mean a phrase rewrite we cannot index back to the source.
                self.structural_edits += 1
                continue
            for source_char, target_char in zip(run, traditional):
                if source_char != target_char:
                    self.char_conversions += 1
                    self.char_pairs[(source_char, target_char)] += 1
            final = twp(run)
            if final == traditional:
                continue
            matcher = difflib.SequenceMatcher(None, traditional, final, autojunk=False)
            for tag, i1, i2, j1, j2 in matcher.get_opcodes():
                if tag == "equal":
                    continue
                if tag != "replace":
                    self.structural_edits += 1
                    continue
                key = (run[i1:i2], final[j1:j2])
                self.phrase_conversions += 1
                self.phrase_pairs[key] += 1
                # Minimal diffs are precise but unreadable alone ("置 -> 定");
                # keep a short sample of the surrounding word so the report can
                # show what the phrase table actually chose.
                left = traditional[max(0, i1 - 2) : i1]
                right = traditional[i2 : i2 + 2]
                left_final = final[max(0, j1 - 2) : j1]
                right_final = final[j2 : j2 + 2]
                context = f"{left}【{key[0]}】{right} → {left_final}【{key[1]}】{right_final}"
                self.phrase_contexts[key][context] += 1

    def as_dict(self) -> dict:
        return {
            "filesConverted": self.files_converted,
            "filesSkipped": self.files_skipped,
            "charConversions": self.char_conversions,
            "phraseConversions": self.phrase_conversions,
            "structuralEdits": self.structural_edits,
            "segmentsConvertedOnExtraPass": self.extra_passes,
            "charPairs": [
                {"from": pair[0], "to": pair[1], "count": count}
                for pair, count in self.char_pairs.most_common(50)
            ],
            "phrasePairs": [
                {
                    "from": pair[0],
                    "to": pair[1],
                    "count": count,
                    "samples": [
                        context
                        for context, _ in self.phrase_contexts.get(pair, Counter()).most_common(2)
                    ],
                }
                for pair, count in self.phrase_pairs.most_common()
            ],
            "unparseable": self.unparseable,
        }


class Converter:
    def __init__(self) -> None:
        self.twp = OpenCC("s2twp.json")
        self.tw = OpenCC("s2tw.json")
        self.stats = Stats()

    def close(self) -> None:
        self.twp.close()
        self.tw.close()

    # -- text -------------------------------------------------------------
    def convert_text(self, text: str) -> str:
        if not text.strip():
            return text
        # One OpenCC s2twp pass, deliberately. Running it to a fixpoint would
        # translate a few more words (the phrase step is applied per segmented
        # token), but the bootstrap is a starting point for human review, not a
        # word list to perfect: see `config/zh-hant-terms.yml` for the regional
        # wording layer that runs on build instead.
        converted = self.twp.convert(text)
        if converted != text:
            self.stats.add(text, converted, self.tw.convert, self.twp.convert)
        return converted

    def convert_line(self, line: str) -> str:
        """Convert the unprotected spans of one line."""
        pieces: list[str] = []
        cursor = 0
        for match in PROTECTED.finditer(line):
            if match.start() > cursor:
                pieces.append(self.convert_text(line[cursor : match.start()]))
            if match.group("html") or match.group("dest"):
                pieces.append(self.convert_quoted(match.group(0)))
            else:
                pieces.append(match.group(0))
            cursor = match.end()
        if cursor < len(line):
            pieces.append(self.convert_text(line[cursor:]))
        return "".join(pieces)

    def convert_quoted(self, text: str) -> str:
        """Convert only the quoted (visible) values inside a tag or link."""
        return QUOTED.sub(
            lambda match: match.group(1) + self.convert_text(match.group(2)) + match.group(1),
            text,
        )

    # -- markdown ---------------------------------------------------------
    def convert_markdown(self, text: str) -> str:
        front, body = split_front_matter(text)
        converted_front = self.convert_front_matter(front) if front else ""
        return converted_front + self.convert_body(body)

    def convert_body(self, body: str) -> str:
        out: list[str] = []
        fence_marker: str | None = None
        in_comment = False
        for line in body.split("\n"):
            closer = FENCE_CLOSE.match(line)
            if fence_marker is not None:
                # Inside a fence: bytes are code, never translate them. Only a
                # bare marker line (no info string) of the same character and at
                # least the opening length closes the block; a line like
                # "```ros" inside it is content (CommonMark).
                if (
                    closer
                    and closer.group(1)[0] == fence_marker[0]
                    and len(closer.group(1)) >= len(fence_marker)
                ):
                    fence_marker = None
                out.append(line)
                continue
            opener = FENCE_OPEN.match(line)
            if opener:
                fence_marker = opener.group(1)
                out.append(line)
                continue
            if in_comment:
                out.append(line)
                if "-->" in line:
                    in_comment = False
                continue
            start = line.find("<!--")
            if start != -1 and "-->" not in line[start:]:
                head, tail = line[:start], line[start:]
                out.append(self.convert_line(head) + tail)
                in_comment = True
                continue
            out.append(self.convert_line(line))
        return "\n".join(out)

    def convert_front_matter(self, block: str) -> str:
        if not block:
            return block
        out: list[str] = []
        current_key: str | None = None
        for line in block.split("\n"):
            match = FRONTMATTER_LINE.match(line)
            if match:
                current_key = match.group(1)
                if current_key in FRONTMATTER_KEEP:
                    out.append(line)
                else:
                    out.append(f"{current_key}:{self.convert_line(match.group(2))}")
                continue
            if current_key in FRONTMATTER_KEEP or not line.strip() or line.strip() == "---":
                out.append(line)
            else:
                out.append(self.convert_line(line))
        return "\n".join(out)

    # -- files ------------------------------------------------------------
    def convert_file(self, source: Path, target: Path) -> None:
        text = source.read_text(encoding="utf-8")
        if source.suffix == ".json":
            converted = self.convert_json(text, source)
        elif source.suffix in {".yml", ".yaml"}:
            converted = self.convert_yaml(text)
        else:
            converted = self.convert_markdown(text)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(converted, encoding="utf-8")
        self.stats.files_converted += 1

    def convert_yaml(self, text: str) -> str:
        """Glossary and page patches: convert prose, keep keys and English."""
        return "\n".join(self.convert_line(line) for line in text.split("\n"))

    def convert_json(self, text: str, source: Path) -> str:
        try:
            data = json.loads(text)
        except json.JSONDecodeError as error:
            self.stats.unparseable.append(f"{source}: {error}")
            return text

        def walk(value):
            if isinstance(value, str):
                return self.convert_text(value)
            if isinstance(value, list):
                return [walk(item) for item in value]
            if isinstance(value, dict):
                return {key: walk(item) for key, item in value.items()}
            return value

        return json.dumps(walk(data), ensure_ascii=False, indent=2) + "\n"


def merge_regions(regions, run_length: int, final_length: int):
    """Widen each changed region by one character and merge the overlaps."""
    widened = []
    for i1, i2, j1, j2 in regions:
        widened.append(
            (max(0, i1 - 1), min(run_length, i2 + 1), max(0, j1 - 1), min(final_length, j2 + 1))
        )
    widened.sort()
    merged = []
    for region in widened:
        if merged and region[0] <= merged[-1][1]:
            last = merged[-1]
            merged[-1] = (last[0], max(last[1], region[1]), last[2], max(last[3], region[3]))
        else:
            merged.append(region)
    return merged


def split_front_matter(text: str) -> tuple[str, str]:
    """Return (front-matter block including its delimiters, body)."""
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    return text[: end + 5], text[end + 5 :]


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix in {".md", ".mdx", ".json", ".yml", ".yaml"}:
            yield path


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="One-off s2twp bootstrap converter")
    parser.add_argument("--source", type=Path, help="i18n/zh-Hans directory to convert")
    parser.add_argument("--target", type=Path, help="i18n/zh-Hant directory to write")
    parser.add_argument("--file", type=Path, help="convert a single file (glossary/patches)")
    parser.add_argument("--out", type=Path, help="destination for --file")
    parser.add_argument("--stats", type=Path, help="write the conversion ledger as JSON")
    args = parser.parse_args(argv)

    converter = Converter()
    try:
        if args.file:
            if not args.out:
                parser.error("--file requires --out")
            converter.convert_file(args.file, args.out)
        else:
            if not args.source or not args.target:
                parser.error("--source and --target are required (or use --file/--out)")
            for path in iter_files(args.source):
                converter.convert_file(path, args.target / path.relative_to(args.source))
    finally:
        converter.close()

    summary = converter.stats.as_dict()
    if args.stats:
        args.stats.parent.mkdir(parents=True, exist_ok=True)
        args.stats.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    print(
        json.dumps(
            {
                "files": summary["filesConverted"],
                "charConversions": summary["charConversions"],
                "phraseConversions": summary["phraseConversions"],
                "structuralEdits": summary["structuralEdits"],
                "uniquePhrases": len(summary["phrasePairs"]),
            },
            ensure_ascii=False,
        ),
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
