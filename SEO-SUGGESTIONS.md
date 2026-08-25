# SEO Suggestions — Dante Troubleshooter

Principles kept in mind throughout: same voice, no jargon-stuffing, nothing on the page changes meaning. The site's tone is an asset — the goal is to make it *findable*, not louder.

---

## 1. Metadata (highest impact per minute spent)

### Title tag (~55 chars)
```
Dante Troubleshooter — Fix Dante Network Problems Fast
```
Keeps "panic button" energy without losing the two terms people search: *Dante* + *troubleshooting/problems*. Current title is good but "audio networks" is a phrase nobody types when panicking.

### Meta description (~155 chars)
```
Guided troubleshooting and real diagnostics for Dante networks. Find missing devices, fix clock sync and audio dropouts — 40 minutes before doors.
```
Swaps "zero condescension" (great line, wrong place — descriptions are for the query match) for symptom words: *missing devices, clock sync, audio dropouts*. Those three phrases mirror the top search queries in this niche.

### Canonical
```html
<link rel="canonical" href="https://dante.brandon-lopez.com/">
```
Prevents the github.io URL from splitting ranking credit.

### Open Graph + Twitter card
```html
<meta property="og:type" content="website">
<meta property="og:title" content="Dante Troubleshooter — The panic button for Dante networks">
<meta property="og:description" content="Find missing Dante devices, fix clock sync, stop audio dropouts. Real diagnostics plus field knowledge for Yamaha, Allen & Heath, DiGiCo, d&b and more.">
<meta property="og:url" content="https://dante.brandon-lopez.com/">
<meta property="og:image" content="https://dante.brandon-lopez.com/og-image.png">
<meta name="twitter:card" content="summary_large_image">
```
Needs one simple OG image (1200×630) — black background, sky-blue "DT", tagline. This is what shows when someone drops the link into a church-tech Facebook group or r/livesound comment. Currently those shares render as bare text.

### Structured data (JSON-LD)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Dante Troubleshooter",
  "applicationCategory": "MultimediaApplication",
  "operatingSystem": "macOS 12+",
  "description": "Guided troubleshooting and network diagnostics for Dante audio networks.",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
  "author": { "@type": "Person", "name": "Brandon Lopez" }
}
</script>
```
Adjust price/free as appropriate.

### robots.txt + sitemap.xml
Two tiny files:
```
# robots.txt
User-agent: *
Allow: /
Sitemap: https://dante.brandon-lopez.com/sitemap.xml
```

---

## 2. On-page copy tweaks (same voice, sharper query alignment)

Small edits only — every one of these already matches how the site talks:

1. **H1 alt text / hero sub:** work the phrase "Dante network problems" naturally into the first paragraph. It's already implied; make it literal once. E.g. append one sentence to the hero sub:
   > *"Missing devices, broken clocking, mystery dropouts — diagnosed in minutes."*
   That sentence is pure query-mirror, zero jargon inflation.

2. **"What's inside" section head side-note** currently reads *"Six failure modes. Forty-eight screens. Zero forum spelunking."* — keep it, but consider the h2 staying and adding one visible line under the grid intro using natural phrasing like **"the problems that actually take down a show."**

3. **Feature cell 01 list:** rename items to match search phrasing where it costs nothing:
   - "Can't see Dante devices" → keep (already perfect)
   - "Clock sync problems" → keep (perfect)
   - "Routing & audio dropouts" → keep

4. **Add a short FAQ section before Install** (see §3). Biggest on-page lever available.

5. **Footer:** add one plain-text line with the domain spelled out ("Dante Troubleshooter — dante.brandon-lopez.com") so crawlers see the canonical domain in body text.

---

## 3. New page: `/faq` (or `/#faq` if you'd rather not add a route)

A single FAQ page written entirely in the current voice. It captures long-tail symptom searches and each answer ends with a soft pointer to the app. Draft topics — these are literally the queries people type today:

- **Why can't I see my Dante devices in Dante Controller?**
  (IGMP snooping, VLANs, link-local addresses — then: "or run the subnet scan and stop guessing")
- **Why does my Dante audio drop out randomly?** (clock conflicts, flow control, Wi-Fi isolation)
- **Why is my Yamaha console fighting me on clocking?** (CL/QL defaults, Console IDs)
- **Can primary and secondary Dante networks share one switch?** (no — here's why)
- **Why don't my d&b amps show up on the network?** (DS100 failsafe LEDs)
- **Do I still need Dante Controller?** (yes — this app complements it, honest positioning)

Mark it up with `FAQPage` JSON-LD and it becomes eligible for rich results. Audinate has documentation for all of this but their answers read like IT manuals; there is a real gap for answers that talk like a system tech.

---

## 4. Off-page (where the actual ranking power comes from)

The site currently has essentially zero inbound links. On-page work alone won't outrank forum threads with years of accumulated authority. Highest-leverage moves:

1. **Reddit r/livesound & Gearspace** — share genuinely, as the developer, in Dante-horror-story threads. The site's voice will land well there.
2. **Church tech communities** — Facebook groups, Church Production magazine, church AV Discords. The audience section could name them explicitly (see §5).
3. **GitHub repo description/topics** — add `dante`, `audinate`, `audio-networking`, `av-professionals` topics; GitHub ranks well and links back.
4. **Release notes** — even a simple CHANGELOG on the site gives crawlers (and humans) proof of maintenance and another crawlable page.

---

## 5. Optional copy addition: name the audiences

The user research says corporate A1s, theatre, AVL installers, and church tech directors. The page gestures at this ("A1s and system techs…") but never says *corporate*, *theatre*, *church*, or *installation* — four real search modifiers. One added bullet in "For:", in the existing voice:

> **For:**
> - A1s and system techs who know what a subnet mask is but don't want to derive it under pressure
> - Church tech directors running a network one volunteer at a time *(new)*
> - The installer commissioning a room at 6 a.m. with the client watching *(new)*
> - …

This adds genuine relevance without a single stuffed keyword.

---

## Priority order

| # | Item | Effort | Impact |
|---|---|---|---|
| 1 | Metadata block: title, description, canonical, OG/Twitter | 30 min | High |
| 2 | OG image | 30 min | High (for shares, which drive links) |
| 3 | JSON-LD SoftwareApplication | 15 min | Medium |
| 4 | robots.txt + sitemap.xml | 10 min | Low-medium |
| 5 | Hero/copy micro-edits (§2, §5) | 45 min | Medium |
| 6 | FAQ page + FAQPage schema | Half day | **Highest long-term** |
| 7 | Community sharing / link building | Ongoing | **Highest overall** |
