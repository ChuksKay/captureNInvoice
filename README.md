# CaptureNInvoice — Marketing Website

Public marketing website for [CaptureNInvoice](https://captureninvoice.com) — proof-of-work invoicing for service businesses.

The live app is at [app.captureninvoice.com](https://app.captureninvoice.com).

## Run Locally

```bash
cd "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice"
python server.py
```

Or:

```bash
python3 -m http.server 8000
```

Open: **http://localhost:8000** — stop with `Ctrl+C`.

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
├── sitemap.xml          # Sitemap for search engines (all 6 marketing pages)
├── server.py            # Local dev server
└── assets/              # Images and static assets
```

## Pages

| Page | Path | Purpose |
|---|---|---|
| Homepage | `/` | Main marketing front door |
| Product | `/product` | What CaptureNInvoice is |
| Features | `/features` | Full feature breakdown |
| How It Works | `/how-it-works` | 3-step workflow |
| Pricing | `/pricing` | Basic ($9/mo) and Pro ($25/mo) plans |
| About | `/about` | Mission and audience |
| Privacy Policy | `/privacy` | Data collection and user rights |
| Terms of Service | `/terms` | Usage terms and conditions |
| Security | `/security` | Data protection and payment security |

## SEO

Structured data in `index.html` `<head>`:
- **Organization** — name, url, description
- **SoftwareApplication** — app category, pricing (Basic $9/mo), description
- **FAQPage** — 6 FAQ questions mapped to schema.org

Each subpage includes canonical tags and Open Graph meta tags (`og:title`, `og:description`, `og:type`, `og:url`).

Crawl infrastructure:
- `robots.txt` — allows all crawlers, points to sitemap
- `sitemap.xml` — all 9 marketing pages with priority and changefreq

## Analytics

Google Analytics 4 (GA4) is installed on all 9 pages — Measurement ID: `G-6WRXJRYEW0`.
The tag is placed immediately after the `<head>` element on every page per Google's requirements.

## Demo Video

A product demo video is embedded on the homepage between the Stats and How It Works sections.

- File: `assets/demo.mp4` (H.264, served locally for now)
- Poster: `assets/demo-poster.jpg`
- Planned: migrate to YouTube/Vimeo for better performance

## Next Steps

1. **Submit sitemap** — add `https://captureninvoice.com/sitemap.xml` to Google Search Console
2. **Add og:image** — create a social share image and add to Open Graph tags
3. **Add favicon** — create and link a favicon for brand consistency
4. **Migrate video** — host on YouTube/Vimeo and replace `<video>` tag with embed
5. **Session recording** — add Microsoft Clarity for heatmaps and session replays
