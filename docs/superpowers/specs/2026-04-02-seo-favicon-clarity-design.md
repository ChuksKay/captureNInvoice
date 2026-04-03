# SEO, Favicon & Analytics Design

**Date:** 2026-04-02
**Scope:** All 9 pages, `assets/`, `CLAUDE.md`

---

## Changes from v1 *(clearly marked below)*

- **REMOVED:** robots.txt task — sitemap already referenced, no change needed
- **REMOVED:** "add title + meta description per page" task — all 9 pages already have unique, correct titles and meta descriptions (verified by grep)
- **CHANGED:** OG image generation — replaced vague "use Playwright" with Playwright MCP browser tool (already available in session, zero installation required)
- **SIMPLIFIED:** Scope reduced from 14 files to 12 (removed robots.txt and title/meta work)

---

## Task 1 — OG Image

**Design (Style C — Clean White, 1200×630px):**
- White background `#FFFFFF`
- Gradient accent bar top: `linear-gradient(90deg, #FF6B35, #FFD23F)`, 6px tall
- Logo SVG + "CaptureNInvoice" wordmark, top-left
- Headline: "From job to payment — in one flow" — `#004E89`, weight 800, 48px
- Subheadline: "Get paid faster." — `#FF6B35`, weight 600, 24px
- Third line: "Built for service businesses" — `#6b7280`, 18px
- URL bottom-right: `captureninvoice.com` — `#9ca3af`, 14px

**Generation (no external dependencies):**
1. Write `assets/og-image-source.html` — full standalone HTML document, `<body>` sized to exactly 1200×630px with `overflow:hidden`
2. Use the **Playwright MCP browser tool** (`mcp__plugin_playwright`) — already available in-session, no npm/pip install needed — to navigate to the file and take a screenshot at 1200×630
3. Save as `assets/og-image.jpg`
4. Delete `assets/og-image-source.html` (build artifact, not needed in repo)

**Meta tags added to all 9 pages inside `<head>` after existing OG tags:**
```html
<meta property="og:image" content="https://captureninvoice.com/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

---

## Task 2 — Favicon

**Files to create:**
- `assets/favicon.svg` — two overlapping squares, matches nav logo exactly
- `assets/apple-touch-icon.png` — 180×180px, generated via Playwright MCP screenshot of the SVG at that size

**SVG spec** (matches existing inline nav logo):
```svg
<svg width="32" height="32" viewBox="0 0 50 50" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="fg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FF6B35"/>
      <stop offset="100%" style="stop-color:#FFD23F"/>
    </linearGradient>
  </defs>
  <rect x="2" y="2" width="30" height="30" rx="7" fill="url(#fg)"/>
  <rect x="18" y="18" width="30" height="30" rx="7" fill="#004E89"/>
</svg>
```

**Links added to all 9 pages inside `<head>`, after existing meta/canonical tags:**
```html
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
```

---

## Task 3 — Microsoft Clarity

**Snippet added to all 9 pages** immediately after the closing `</script>` of the GA4 block:

```html
<!-- Microsoft Clarity — replace YOUR_CLARITY_ID once you have a project at clarity.microsoft.com -->
<script type="text/javascript">
  (function(c,l,a,r,i,t,y){
    c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
    t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
    y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
  })(window, document, "clarity", "script", "YOUR_CLARITY_ID");
</script>
```

**To activate:** Go to clarity.microsoft.com → create a project → copy the project ID → replace `YOUR_CLARITY_ID` across all 9 files (one grep-replace).

---

## Task 4 — CLAUDE.md Updates

Add two notes:

1. **Search Console:** Steps to submit sitemap (user must do manually):
   - Go to search.google.com/search-console
   - Add property → `https://captureninvoice.com`
   - Verify ownership via DNS TXT record
   - Sitemaps → submit `https://captureninvoice.com/sitemap.xml`

2. **Clarity activation:** Note that `YOUR_CLARITY_ID` placeholder exists in all 9 pages and how to replace it.

---

## What Is Already Done (No Changes Needed)

| Item | Status |
|---|---|
| Unique `<title>` on all 9 pages | ✅ Done |
| Unique `<meta name="description">` on all 9 pages | ✅ Done |
| Sitemap referenced in `robots.txt` | ✅ Done |
| Canonical tags on all pages | ✅ Done |
| OG title + description + type + url on all pages | ✅ Done |

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
- `robots.txt` *(already correct)*
- `sitemap.xml`
