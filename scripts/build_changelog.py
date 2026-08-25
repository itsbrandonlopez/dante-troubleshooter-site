#!/usr/bin/env python3
"""Bake GitHub releases into changelog/index.html as static HTML.

Run manually:  python3 scripts/build_changelog.py
Or via GitHub Actions (see .github/workflows/changelog.yml).

No dependencies beyond the Python standard library.
"""

import json
import os
import re
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = "itsbrandonlopez/dante-troubleshooter-site"
API = f"https://api.github.com/repos/{REPO}/releases?per_page=30"
SITE_URL = "https://dante.brandon-lopez.com/changelog/"
OUT = Path(__file__).resolve().parent.parent / "changelog" / "index.html"

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
HEADING_RE = re.compile(r"#{1,6}\s+")


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def inline(s: str) -> str:
    s = esc(s)
    s = s.replace("\u2026", "&hellip;")
    s = LINK_RE.sub(r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def md(src: str) -> str:
    out = []
    in_list = False
    for raw in src.splitlines():
        line = raw.strip()
        is_bullet = line[:2] in ("- ", "* ", "+ ")
        if is_bullet and not in_list:
            out.append("<ul>")
            in_list = True
        if not is_bullet and in_list:
            out.append("</ul>")
            in_list = False
        if not line:
            continue
        if HEADING_RE.match(line):
            out.append(f"<h3>{inline(HEADING_RE.sub('', line).strip())}</h3>")
        elif is_bullet:
            out.append(f"<li>{inline(line[2:])}</li>")
        else:
            out.append(f"<p>{inline(line)}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def fmt_date(iso: str) -> str:
    if not iso:
        return ""
    dt = datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(timezone.utc)
    return dt.strftime("%b %-d, %Y")


def fetch_releases() -> list:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "changelog-builder",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        req = urllib.request.Request(API, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except (urllib.error.URLError, OSError):
        # Some local Python installs (macOS python.org builds) lack CA certs;
        # fall back to curl so the script still works locally.
        cmd = ["curl", "-sfSL"]
        if token:
            cmd += ["-H", f"Authorization: Bearer {token}"]
        cmd += ["-H", "Accept: application/vnd.github+json", API]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)


def render_release(r: dict) -> str:
    tag = esc(r.get("tag_name") or "")
    published = r.get("published_at") or ""
    body_src = (r.get("body") or "").strip() or "No notes for this release."
    return (
        '<article class="release">\n'
        '  <div class="release-head">'
        f"<h2>{tag}</h2>"
        f'<time datetime="{esc(published)}">{esc(fmt_date(published))}</time>'
        "</div>\n"
        f'  <div class="release-body">\n{md(body_src)}\n  </div>\n'
        "</article>"
    )


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Changelog — Dante Troubleshooter Release Notes</title>
<meta name="description" content="Every Dante Troubleshooter release, straight from GitHub: new walkthroughs, diagnostics, and gear knowledge base updates.">
<meta name="theme-color" content="#000000">
<link rel="canonical" href="https://dante.brandon-lopez.com/changelog/">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Dante Troubleshooter">
<meta property="og:title" content="Dante Troubleshooter Changelog">
<meta property="og:description" content="Every release, straight from GitHub. New walkthroughs, diagnostics, and gear knowledge with each version.">
<meta property="og:url" content="https://dante.brandon-lopez.com/changelog/">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Dante Troubleshooter Changelog">
<meta name="twitter:description" content="Every release, straight from GitHub.">

<style>
  :root {
    --bg: #000;
    --ink: #fff;
    --muted: rgba(255, 255, 255, 0.62);
    --faint: rgba(255, 255, 255, 0.4);
    --hairline: rgba(255, 255, 255, 0.28);
    --accent: #38bdf8;
    --mono: ui-monospace, "SF Mono", Menlo, Monaco, "Courier New", monospace;
    --sans: "Helvetica Neue", Helvetica, Arial, sans-serif;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--ink);
    font-family: var(--sans);
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
  }

  ::selection { background: var(--accent); color: #000; }
  a { color: inherit; text-decoration: none; -webkit-tap-highlight-color: transparent; }
  :focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }

  .wrap {
    width: min(100% - clamp(48px, 9vw, 160px), 1400px);
    margin-inline: auto;
  }

  .label {
    font-family: var(--mono);
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: var(--muted);
  }

  header.hero { min-height: 46svh; display: flex; flex-direction: column; padding-block: 28px 36px; }

  .topbar {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    flex-wrap: wrap;
    gap: 14px 24px;
  }
  .topbar nav { display: flex; align-items: center; gap: 24px; }
  .nav-divider { width: 1px; height: 14px; background: var(--hairline); }
  .topbar a:hover { color: var(--accent); }

  .hero h1 {
    margin: auto 0;
    font-size: clamp(2.4rem, 6vw, 5rem);
    font-weight: 500;
    letter-spacing: -0.05em;
    line-height: 0.95;
    max-width: 20ch;
  }
  .hero h1 em { font-style: normal; color: var(--accent); }
  .hero p.sub {
    max-width: 560px;
    margin-top: 28px;
    font-size: 1.05rem;
    line-height: 1.55;
    color: var(--muted);
  }

  .releases { border-top: 1px solid var(--hairline); margin-top: 48px; max-width: 900px; }

  .release { padding: 34px 20px; border-bottom: 1px solid var(--hairline); }

  .release-head {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 16px;
    flex-wrap: wrap;
    margin-bottom: 16px;
  }
  .release-head h2 {
    font-family: var(--mono);
    font-size: 1.1rem;
    font-weight: 600;
    letter-spacing: 0.02em;
    color: var(--accent);
  }
  .release-head time {
    font-family: var(--mono);
    font-size: 0.72rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--faint);
  }

  .release-body { font-size: 1rem; line-height: 1.6; color: var(--muted); }
  .release-body p { margin-bottom: 12px; }
  .release-body p:last-child { margin-bottom: 0; }
  .release-body strong { color: var(--ink); font-weight: 500; }
  .release-body code { font-family: var(--mono); font-size: 0.85em; color: var(--ink); }
  .release-body ul { list-style: none; }
  .release-body li {
    padding-left: 18px;
    position: relative;
    margin-bottom: 8px;
  }
  .release-body li::before { content: "\\2014"; position: absolute; left: 0; color: var(--faint); }
  .release-body h3 {
    font-size: 1.15rem;
    font-weight: 500;
    letter-spacing: -0.02em;
    color: var(--ink);
    margin: 18px 0 10px;
  }
  .release-body h3:first-child { margin-top: 0; }
  .release-body a:hover { color: var(--accent); }

  footer { padding-block: 64px 40px; }
  .foot-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 24px;
    padding-top: 20px;
    border-top: 1px solid var(--hairline);
    flex-wrap: wrap;
  }
  .foot-row .links { display: flex; gap: 24px; }
  .foot-row a:hover { color: var(--accent); }

  @media (max-width: 800px) {
    .topbar { flex-direction: column; align-items: flex-start; gap: 16px; }
    .release { padding: 26px 14px; }
  }
</style>
</head>
<body>

<header class="hero wrap">
  <div class="topbar">
    <a class="label" href="/">Dante Troubleshooter</a>
    <nav class="label">
      <a href="/gear/">Gear coverage</a>
      <a href="/faq/">FAQ</a>
      <span class="nav-divider"></span>
      <a href="https://itsbrandonlopez.github.io/personal-site/">Made by Brandon</a>
    </nav>
  </div>
  <h1>What's <em>new.</em></h1>
  <p class="sub">Every release, straight from the source. No marketing gloss — what shipped, what got fixed.</p>
</header>

<main class="wrap" aria-label="Release history">
  <div class="releases">
<!--RELEASES-->
  </div>
</main>

<footer class="wrap">
  <div class="foot-row">
    <span class="label">Dante Troubleshooter &middot; &copy; 2026 Brandon Lopez</span>
    <div class="links">
      <a class="label" href="https://buttondown.com/itsbrandonlopez">Release updates</a>
      <a class="label" href="mailto:hi@brandon-lopez.com?subject=Dante%20Troubleshooter">hi@brandon-lopez.com</a>
    </div>
  </div>
</footer>

</body>
</html>
"""


def main() -> None:
    releases = fetch_releases()
    rendered = "\n".join(render_release(r) for r in releases)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(TEMPLATE.replace("<!--RELEASES-->", rendered), encoding="utf-8")
    print(f"Wrote {OUT} ({len(releases)} releases)")


if __name__ == "__main__":
    main()
