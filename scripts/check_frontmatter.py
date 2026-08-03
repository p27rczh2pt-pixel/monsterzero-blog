#!/usr/bin/env python3
"""Check Hugo post front matter for common mistakes, especially timestamp bugs.

Usage:
    python3 scripts/check_frontmatter.py [content_dir]

Exits non-zero if any errors are found (warnings alone exit 0), so it can be
wired into a pre-commit hook or CI.
"""
import sys
import re
from datetime import datetime, date
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    import tomllib
except ImportError:
    print("error: needs Python 3.11+ for tomllib", file=sys.stderr)
    sys.exit(2)

SITE_TZ = ZoneInfo("America/Chicago")  # matches this blog's -05:00/-06:00 posts
TOML_DELIM = "+++"
YAML_DELIM = "---"


def extract_frontmatter(text: str):
    """Return (format, raw_block) or (None, None) if no front matter found."""
    lines = text.splitlines()
    if not lines:
        return None, None
    first = lines[0].strip()
    delim = None
    if first == TOML_DELIM:
        delim = TOML_DELIM
    elif first == YAML_DELIM:
        delim = YAML_DELIM
    else:
        return None, None
    for i in range(1, len(lines)):
        if lines[i].strip() == delim:
            return ("toml" if delim == TOML_DELIM else "yaml"), "\n".join(lines[1:i])
    return None, None


def parse_frontmatter(fmt: str, raw: str):
    if fmt == "toml":
        return tomllib.loads(raw)
    else:
        import yaml  # only needed if a post ever uses YAML front matter
        return yaml.safe_load(raw)


def expected_offset(dt: datetime) -> str:
    """What the UTC offset should be for this local wall-clock time in SITE_TZ."""
    localized = dt.replace(tzinfo=SITE_TZ)
    offset = localized.utcoffset()
    total_minutes = int(offset.total_seconds() // 60)
    sign = "+" if total_minutes >= 0 else "-"
    total_minutes = abs(total_minutes)
    return f"{sign}{total_minutes // 60:02d}:{total_minutes % 60:02d}"


def check_file(path: Path, seen_dates: dict) -> list:
    issues = []  # list of (level, message)
    text = path.read_text(encoding="utf-8")
    fmt, raw = extract_frontmatter(text)

    if fmt is None:
        issues.append(("error", "no TOML/YAML front matter block found"))
        return issues

    try:
        fm = parse_frontmatter(fmt, raw)
    except Exception as e:
        issues.append(("error", f"front matter failed to parse: {e}"))
        return issues

    # --- title ---
    title = fm.get("title")
    if not title or not str(title).strip():
        issues.append(("error", "missing or empty title"))

    # --- draft ---
    if "draft" not in fm:
        issues.append(("warn", "missing draft field"))

    # --- date ---
    raw_date = fm.get("date")
    dt = None
    if raw_date is None:
        issues.append(("error", "missing date field"))
    else:
        if isinstance(raw_date, datetime):
            dt = raw_date
        elif isinstance(raw_date, date):
            issues.append(("error", f"date '{raw_date}' has no time-of-day component"))
        elif isinstance(raw_date, str):
            try:
                dt = datetime.fromisoformat(raw_date)
            except ValueError:
                issues.append(("error", f"date '{raw_date}' is not valid ISO 8601"))
        else:
            issues.append(("error", f"date field has unexpected type: {type(raw_date).__name__}"))

        if dt is not None:
            if dt.tzinfo is None:
                issues.append(("error", "date has no UTC offset (Hugo will assume server/local time)"))
            else:
                want = expected_offset(dt.replace(tzinfo=None))
                have_offset = dt.utcoffset()
                have_total = int(have_offset.total_seconds() // 60)
                have = f"{'+' if have_total >= 0 else '-'}{abs(have_total)//60:02d}:{abs(have_total)%60:02d}"
                if have != want:
                    issues.append((
                        "error",
                        f"date offset {have} looks wrong for {dt.date()} in America/Chicago "
                        f"(expected {want} — check for a stale DST offset)",
                    ))

            if dt.tzinfo is not None:
                now = datetime.now(dt.tzinfo)
            else:
                now = datetime.now()
            if dt > now:
                issues.append(("warn", f"date is in the future ({dt.isoformat()}) — buildFuture=false locally, won't render until then"))

            key = dt.isoformat()
            if key in seen_dates:
                issues.append(("warn", f"date/time identical to {seen_dates[key].name} — looks like a copy-paste that wasn't updated"))
            else:
                seen_dates[key] = path

    # --- lastmod ---
    raw_lastmod = fm.get("lastmod")
    if raw_lastmod is not None and dt is not None:
        lm = None
        if isinstance(raw_lastmod, datetime):
            lm = raw_lastmod
        elif isinstance(raw_lastmod, str):
            try:
                lm = datetime.fromisoformat(raw_lastmod)
            except ValueError:
                issues.append(("error", f"lastmod '{raw_lastmod}' is not valid ISO 8601"))

        if lm is not None:
            if lm.tzinfo is None:
                issues.append(("error", "lastmod has no UTC offset"))
            elif dt.tzinfo is not None and lm < dt:
                issues.append(("error", f"lastmod ({lm.isoformat()}) is earlier than date ({dt.isoformat()})"))

    return issues


def main():
    content_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("content/posts")
    if not content_dir.exists():
        print(f"error: {content_dir} does not exist", file=sys.stderr)
        sys.exit(2)

    files = sorted(content_dir.rglob("*.md"))
    if not files:
        print(f"no .md files found under {content_dir}", file=sys.stderr)
        sys.exit(2)

    seen_dates: dict = {}
    had_error = False
    had_warn = False

    for path in files:
        issues = check_file(path, seen_dates)
        if not issues:
            continue
        print(f"\n{path}")
        for level, msg in issues:
            marker = "ERROR" if level == "error" else "warn "
            print(f"  [{marker}] {msg}")
            if level == "error":
                had_error = True
            else:
                had_warn = True

    print()
    if not had_error and not had_warn:
        print(f"checked {len(files)} posts, no issues found")
    else:
        print(f"checked {len(files)} posts")

    sys.exit(1 if had_error else 0)


if __name__ == "__main__":
    main()
