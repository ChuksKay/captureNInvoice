# CaptureNInvoice Marketing Website - Claude Code Instructions

## Project Overview

This is the public marketing website for [CaptureNInvoice](https://captureninvoice.com) — proof-of-work invoicing for service businesses. The live app is at [app.captureninvoice.com](https://app.captureninvoice.com).

The site is a static multi-page marketing site with shared CSS and JS.

## Project Structure

```
captureninvoice/
├── index.html           # Homepage
├── product.html         # Product page
├── features.html        # Features page
├── how-it-works.html    # How It Works page
├── pricing.html         # Pricing page
├── about.html           # About page
├── privacy.html         # Privacy Policy
├── terms.html           # Terms of Service
├── security.html        # Security page
├── css/
│   └── styles.css       # Shared styles (all pages)
├── js/
│   └── nav.js           # Shared nav behaviour (scroll, hamburger, smooth scroll)
├── robots.txt           # Crawler directives
├── sitemap.xml          # Sitemap for search engines
├── server.py            # Local dev server
└── assets/              # Images and static assets
```

## Pages

| Page | File | Purpose |
|---|---|---|
| Homepage | `index.html` | Main marketing front door |
| Product | `product.html` | What CaptureNInvoice is |
| Features | `features.html` | Full feature breakdown |
| How It Works | `how-it-works.html` | 3-step workflow |
| Pricing | `pricing.html` | Basic ($9/mo) and Pro ($25/mo) plans |
| About | `about.html` | Mission and audience |
| Privacy Policy | `privacy.html` | Data collection and user rights |
| Terms of Service | `terms.html` | Usage terms and conditions |
| Security | `security.html` | Data protection and payment security |

## Running Locally

```bash
cd "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice"
python server.py
# Open: http://localhost:8000
# Stop: Ctrl+C
```

Or: `python -m http.server 8000`

## Design System

**Colors:**
- Primary: #FF6B35 (orange)
- Secondary: #004E89 (blue)
- Accent: #FFD23F (yellow)
- Background gradient: linear-gradient from #004E89 to #002B4F

**Typography:**
- Headings: Bricolage Grotesque (800 weight)
- Body: DM Sans (400, 500, 700)
- Loaded from Google Fonts CDN

**Layout:**
- Max width: 1100px (marketing pages)
- Shared nav and footer on all pages
- Responsive — mobile breakpoint at 768px

## Shared Components

- **Nav** (`nav.js`) — scroll behaviour, hamburger menu, smooth scroll. Included on every page.
- **CSS** (`styles.css`) — all shared styles. Do not duplicate styles inline unless page-specific.

## Analytics

Google Analytics 4 is installed on all pages — Measurement ID: `G-6WRXJRYEW0`.
The gtag snippet must be placed immediately after the opening `<head>` tag (not before `</head>`).

## When Adding a New Page

1. Copy the structure of an existing page (e.g. `about.html`)
2. Update `<title>`, `<meta>` description, canonical URL, and Open Graph tags in `<head>`
3. The GA tag is already in the template — do not add it again
4. Add the page to `sitemap.xml`
5. Link to it from the footer (and nav if appropriate) on all other pages

## SEO Notes

- Structured data (Organization, SoftwareApplication, FAQPage) lives in `index.html`
- Every page has canonical tags and Open Graph meta tags
- `robots.txt` allows all crawlers and points to sitemap
- `sitemap.xml` covers all marketing pages

## Content Rules

- Do not add fake user counts, made-up metrics, or false social proof
- Pricing: Basic $9/mo, Pro $25/mo — do not change without confirmation
- App URL: `https://app.captureninvoice.com` — use this consistently

## Next Steps (Pending)

1. Submit sitemap to Google Search Console
2. Add `og:image` social share image
3. Add favicon
