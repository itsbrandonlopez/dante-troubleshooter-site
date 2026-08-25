# SEO Research — Dante Troubleshooter

Date: 2026-08-24 · Site: dante.brandon-lopez.com (single static page, GitHub Pages)

---

## 1. Current state of the site

**Stack:** Plain HTML (`index.html`), one page, no build system, no robots.txt, no sitemap.xml, CNAME → `dante.brandon-lopez.com`.

**Existing metadata inventory:**

| Element | Status | Current value |
|---|---|---|
| `<title>` | ✅ Present | "Dante Troubleshooter — The panic button for Dante audio networks" |
| Meta description | ✅ Present | "Guided troubleshooting and real diagnostics for Dante audio networks. Six scenarios, 48 screens, zero condescension. For when the show is on the line." |
| Canonical URL | ❌ Missing | — |
| Open Graph (og:title, og:description, og:image…) | ❌ Missing | Nothing shared-preview friendly when pasted in Slack/iMessage/Facebook groups — exactly where AV techs share links |
| Twitter card | ❌ Missing | — |
| JSON-LD structured data | ❌ Missing | No `SoftwareApplication`, `FAQPage`, or `Organization` schema |
| robots.txt | ❌ Missing | — |
| sitemap.xml | ❌ Missing | — |
| H1 | ✅ One only | "The panic button for *Dante* networks." |
| H2s | ✅ | "What's inside." / "Who it's for." / "Install." |

**Content/tone observations:** Dry, confident, field-tested humor ("zero forum spelunking," "like all the best touring crews"). Symptom-first framing. Names specific gear (Yamaha CL/QL, Allen & Heath, DiGiCo, d&b DS100, NEXO NXDT104) — this is a genuine SEO asset because people search by *gear model*, not by abstract terms. The "Not for:" section is unusual and on-brand; it should not be touched for SEO.

**Gaps that matter:**
1. No canonical tag → `dante.brandon-lopez.com` and the github.io URL can split ranking signals.
2. Zero social preview markup → poor presentation wherever AV folks actually share links.
3. No structured data → ineligible for rich results.
4. Page targets brand terms ("Dante Troubleshooter") but almost no *symptom* language that matches how people actually search (see §3).
5. Single page = single keyword cluster. There's nothing to rank for the dozens of high-intent problem queries in this niche.
6. Download link goes straight to a DMG with no release notes/changelog page — no crawlable proof of maintenance or version history.

---

## 2. Competitive landscape

**Who owns these searches today:**

| Player | What they rank with | Notes |
|---|---|---|
| **Audinate (getdante.com)** | Blog posts ("Nothing shows up"), support KB, dev docs, certification pages | Owns virtually every head term. Unbeatable on generic "what is Dante" and official-doc queries. Their content is corporate and exhaustive — slow, formal, written for IT managers. |
| **Manufacturer support pages** | QSC, Sennheiser, Symetrix, KanexPro, Aviom troubleshooting articles | Rank for product-specific symptoms ("QSC dante clicks and pops"). |
| **Third-party guides** | syntechav.com "Dante Device Not Showing Up? 7 Fixes That Actually Work", Sound & Video Contractor articles, manuals.plus FAQ copies | These prove third parties CAN rank on symptom queries. They are listicles/checklists — exactly what your site's tone already positions against. |
| **Forums** | Allen & Heath community, Reddit, Gearspace | Rank heavily on long-tail ("dante device wrong IP address sq5"). High engagement, low polish. |
| **Hardware competitors** | Nixer PD Dante (handheld Dante diagnostic/monitor box, ~$3k+ class) | Only real "tool" competitor found. Ranks via dealer/press pages. Your differentiator: software, affordable, Mac-native, guided fixes. |

**Key takeaway:** Don't fight Audinate on head terms. Win the long-tail symptom queries where the current results are either corporate documentation, low-effort listicles, or forum threads — content you can beat on both quality and voice.

---

## 3. Keyword & query landscape (how people actually search)

Organized by intent, roughly in order of opportunity:

### Symptom queries (highest intent, best fit for the product)
- "dante devices not showing up in dante controller"
- "dante controller can't see devices"
- "dante audio dropouts" / "dante clicks and pops"
- "dante clock sync problems" / "dante clock status red"
- "dante sample rate mismatch"
- "dvs audio dropouts" / "dante virtual soundcard not working"
- "dante redundant network same switch"
- "dante firmware update stuck"
- "why are my dante amps not showing up" (the d&b DS100 case)
- "dante subnet mismatch" / "169.254 link local dante"

### Tool/comparison queries (commercial intent)
- "dante troubleshooting tool"
- "dante network diagnostics software"
- "dante network scanner"
- "dante troubleshooter mac"
- "alternative to dante controller" (adjacent; Dante Controller is free, so position as *complement*, not replacement)
- "nixer pd dante alternative"

### Gear + problem queries (long-tail, low competition, very high fit)
- "yamaha cl5 dante clock" / "yamaha console id dante"
- "allen & heath dante card static ip" / "sq dante dropped audio"
- "digico dmi 96k dante" / "orange box dante"
- "db ds100 dante devices not showing"
- "nexo nxdt104 dante"

### Audience-context queries
- "church sound system dante problems"
- "dante for house of worship"
- "corporate av dante setup troubleshooting"
- "dante virtual soundcheck"

### Head terms to acknowledge but NOT chase
- "what is dante", "dante audio networking", "dante controller" — owned by Audinate.

---

## 4. What actually moves rankings for a one-page site like this

1. **Metadata completeness** (title/description/canonical/OG/Twitter) — table stakes, currently half done.
2. **Structured data** — `SoftwareApplication` schema makes the app eligible for richer listings; `FAQPage` schema can surface questions directly in search results.
3. **On-page symptom language** — the page says "Can't see Dante devices" once, buried in a list. Search engines need the phrasing people type, naturally woven into headings and copy.
4. **Content depth** — a second page (FAQ / knowledge highlights) is the single biggest lever. It captures symptom queries AND funnels to the download. It can be done entirely in the existing voice.
5. **Technical hygiene** — sitemap.xml, robots.txt, fast load (already fine — inline CSS, no JS frameworks), mobile rendering.
6. **Off-page reality check** — with zero inbound links, rankings will be limited regardless of on-page work. Realistic channels: Reddit r/livesound, Gearspace, church tech Facebook groups/Discord, Church Production magazine, AV trade newsletters, GitHub discovery. Every place this gets shared is where OG tags pay off.
