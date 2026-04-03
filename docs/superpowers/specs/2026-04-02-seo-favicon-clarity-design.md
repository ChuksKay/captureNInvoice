# SEO, Favicon & Analytics Design

**Date:** 2026-04-02  
**Scope:** All 9 pages (`index.html`, `product.html`, `features.html`, `how-it-works.html`, `pricing.html`, `about.html`, `privacy.html`, `terms.html`, `security.html`), `assets/`

---

## Overview

Four tasks to complete the baseline marketing site setup:

1. Document Google Search Console sitemap submission (manual user action)
2. Generate and add OG social share image to all pages
3. Create and add favicon to all pages
4. Add Microsoft Clarity snippet (with placeholder ID) to all pages

---

## Task 1 — Google Search Console (Documentation Only)

No code changes. Add a note to `CLAUDE.md` with the steps for the user to follow:

1. Go to https://search.google.com/search-console
2. Add property → enter `https://captureninvoice.com`
3. Verify ownership via DNS TXT record with domain registrar
4. Once verified: Sitemaps → submit `https://captureninvoice.com/sitemap.xml`

---

## Task 2 — OG Image

**Design (Style C — Clean White):**
- 1200×630px
- White background (`#FFFFFF`)
- Gradient accent bar at top: `linear-gradient(90deg, #FF6B35, #FFD23F)`, 6px tall
- Logo (two overlapping squares SVG) + "CaptureNInvoice" wordmark top-left
- Headline: "From job to payment — in one flow" — color `#004E89`, font weight 800, ~48px
- Subheadline: "Get paid faster." — color `#FF6B35`, font weight 600, ~24px
- Third line: "Built for service businesses" — color `#6b7280`, ~18px
- URL bottom-right: `captureninvoice.com` — color `#9ca3af`, small

**Generation:**
- Write `assets/og-image-source.html` — standalone HTML file at 1200×630px rendering the design
- Use Playwright (`mcp__plugin_playwright`) to screenshot it at exactly 1200×630
- Save output as `assets/og-image.jpg`
- Delete `og-image-source.html` after generation (it's a build artifact)

**Meta tags added to every page (inside `<head>`):**
```html
<meta property="og:image" content="https://captureninvoice.com/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

Note: Each page already has `og:title`, `og:description`, `og:type`, and `og:url`. This adds only the image tags.

---

## Task 3 — Favicon

**Files to create:**
- `assets/favicon.svg` — SVG favicon, two overlapping squares matching the nav logo exactly
- `assets/apple-touch-icon.png` — 180×180px PNG, generated via Playwright screenshot of the SVG

**SVG design** (matches existing nav logo):
- Large square: top-left, 30×30, rx=7, orange-yellow gradient fill (`#FF6B35` → `#FFD23F`)
- Small square: bottom-right overlapping, 30×30, rx=7, blue fill `#004E89`
- Viewbox: `0 0 50 50`
- White background circle or transparent (transparent preferred)

**Links added to every page (inside `<head>`, after existing meta tags):**
```html
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
```

---

## Task 4 — Microsoft Clarity

**Snippet added to every page**, immediately after the GA4 snippet (after `</script>` closing the GA block):

```html
<!-- Microsoft Clarity — replace YOUR_CLARITY_ID with your project ID from clarity.microsoft.com -->
<script type="text/javascript">
  (function(c,l,a,r,i,t,y){
    c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
    t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
    y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
  })(window, document, "clarity", "script", "YOUR_CLARITY_ID");
</script>
```

**To activate:** Create a project at https://clarity.microsoft.com, get the project ID, and replace `YOUR_CLARITY_ID` across all 9 files.

---

## Files Changed

| File | Change |
|---|---|
| `assets/og-image.jpg` | Created — OG social share image |
| `assets/favicon.svg` | Created — SVG favicon |
| `assets/apple-touch-icon.png` | Created — iOS home screen icon |
| `CLAUDE.md` | Add Search Console steps + Clarity activation note |
| `index.html` | OG image tags + favicon links + Clarity snippet |
| `product.html` | OG image tags + favicon links + Clarity snippet |
| `features.html` | OG image tags + favicon links + Clarity snippet |
| `how-it-works.html` | OG image tags + favicon links + Clarity snippet |
| `pricing.html` | OG image tags + favicon links + Clarity snippet |
| `about.html` | OG image tags + favicon links + Clarity snippet |
| `privacy.html` | OG image tags + favicon links + Clarity snippet |
| `terms.html` | OG image tags + favicon links + Clarity snippet |
| `security.html` | OG image tags + favicon links + Clarity snippet |

## Files NOT Changed

- `css/styles.css`
- `js/nav.js`
- `sitemap.xml`
- `robots.txt`
