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
python -m http.server 8000
```

Open: **http://localhost:8000** — stop with `Ctrl+C`.

## Project Structure

```
captureninvoice/
├── index.html       # Marketing page (HTML + CSS + JS)
├── robots.txt       # Crawler directives
├── sitemap.xml      # Sitemap for search engines
├── server.py        # Local dev server
├── README.md        # This file
├── css/             # Reserved for separated styles
├── js/              # Reserved for separated scripts
└── assets/images/   # Reserved for images/logos
```

## SEO

Structured data in `index.html` `<head>`:
- **Organization** — name, url, description
- **SoftwareApplication** — app category, pricing, description
- **FAQPage** — all 6 FAQ questions mapped to schema.org

Crawl infrastructure:
- `robots.txt` — allows all crawlers, points to sitemap
- `sitemap.xml` — single entry for `https://captureninvoice.com/`

## Next Steps

1. **Deploy** — push to Netlify, Vercel, or GitHub Pages and point `captureninvoice.com` to it
2. **Submit sitemap** — add `https://captureninvoice.com/sitemap.xml` to Google Search Console
3. **Add analytics** — Google Analytics or Plausible for visitor tracking
4. **Add og:image** — create a social share image and add to Open Graph tags
5. **Connect email capture** — replace localStorage with Mailchimp, ConvertKit, or a webhook
