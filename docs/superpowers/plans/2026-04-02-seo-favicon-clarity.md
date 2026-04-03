# SEO, Favicon & Analytics Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add OG social share image, favicon, Apple touch icon, and Microsoft Clarity snippet to all 9 pages of the CaptureNInvoice marketing website.

**Architecture:** Pure static HTML edits — no build tools, no dependencies. OG image and Apple touch icon are generated once using the Playwright MCP browser tool (already available in-session). All 9 pages receive identical tag insertions at the same structural positions.

**Tech Stack:** HTML, CSS (inline for asset generation), Playwright MCP browser tool, sips (macOS, for JPEG conversion)

---

## File Map

| File | Action |
|---|---|
| `assets/og-image-source.html` | Create (temp) — rendered by Playwright, deleted after screenshot |
| `assets/og-image.jpg` | Create — 1200×630 OG social share image |
| `assets/favicon.svg` | Create — SVG favicon matching nav logo |
| `assets/apple-touch-icon.png` | Create — 180×180 PNG for iOS |
| `index.html` | Add OG image tags + favicon links + Clarity snippet |
| `product.html` | Add OG image tags + favicon links + Clarity snippet |
| `features.html` | Add OG image tags + favicon links + Clarity snippet |
| `how-it-works.html` | Add OG image tags + favicon links + Clarity snippet |
| `pricing.html` | Add OG image tags + favicon links + Clarity snippet |
| `about.html` | Add OG image tags + favicon links + Clarity snippet |
| `privacy.html` | Add OG image tags + favicon links + Clarity snippet |
| `terms.html` | Add OG image tags + favicon links + Clarity snippet |
| `security.html` | Add OG image tags + favicon links + Clarity snippet |
| `CLAUDE.md` | Add Search Console steps + Clarity activation note |

---

### Task 1: Generate OG image

**Files:**
- Create: `assets/og-image-source.html` (temp, deleted after use)
- Create: `assets/og-image.jpg`

- [ ] **Step 1: Write the OG image source HTML**

Create `assets/og-image-source.html` with this exact content:

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1200px;
    height: 630px;
    overflow: hidden;
    background: #FFFFFF;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    position: relative;
  }
  .accent-bar {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 6px;
    background: linear-gradient(90deg, #FF6B35, #FFD23F);
  }
  .inner {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    padding: 56px 80px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .logo-row {
    position: absolute;
    top: 40px; left: 80px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .logo-text {
    font-size: 18px;
    font-weight: 600;
    color: #004E89;
  }
  .headline {
    font-size: 52px;
    font-weight: 800;
    color: #004E89;
    line-height: 1.15;
    letter-spacing: -0.5px;
    margin-top: 20px;
  }
  .subheadline {
    font-size: 26px;
    font-weight: 600;
    color: #FF6B35;
    margin-top: 16px;
  }
  .tagline {
    font-size: 18px;
    color: #6b7280;
    margin-top: 10px;
  }
  .url {
    position: absolute;
    bottom: 40px; right: 80px;
    font-size: 15px;
    color: #9ca3af;
    font-weight: 500;
  }
</style>
</head>
<body>
  <div class="accent-bar"></div>
  <div class="logo-row">
    <svg width="32" height="32" viewBox="0 0 50 50" fill="none">
      <defs>
        <linearGradient id="fg" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:#FF6B35"/>
          <stop offset="100%" style="stop-color:#FFD23F"/>
        </linearGradient>
      </defs>
      <rect x="2" y="2" width="30" height="30" rx="7" fill="url(#fg)"/>
      <rect x="18" y="18" width="30" height="30" rx="7" fill="#004E89"/>
    </svg>
    <span class="logo-text">CaptureNInvoice</span>
  </div>
  <div class="inner">
    <div class="headline">From job to payment —<br>in one flow</div>
    <div class="subheadline">Get paid faster.</div>
    <div class="tagline">Built for service businesses</div>
  </div>
  <div class="url">captureninvoice.com</div>
</body>
</html>
```

- [ ] **Step 2: Verify the local server is running**

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8000
```

Expected: `200`. If not, run: `python3 -m http.server 8000` from the project root.

- [ ] **Step 3: Screenshot via Playwright MCP browser tool**

Using the Playwright MCP browser tool:
1. Navigate to `http://localhost:8000/assets/og-image-source.html`
2. Resize browser to 1200×630
3. Take a screenshot — save to `assets/og-image-screenshot.png`

- [ ] **Step 4: Convert PNG to JPEG**

```bash
sips -s format jpeg -s formatOptions 85 \
  "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice/assets/og-image-screenshot.png" \
  --out "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice/assets/og-image.jpg"
```

Expected output: `og-image.jpg` exists, size roughly 80–200KB.

- [ ] **Step 5: Clean up temp files**

```bash
rm "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice/assets/og-image-source.html"
rm "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice/assets/og-image-screenshot.png"
```

- [ ] **Step 6: Verify output**

```bash
ls -lh "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice/assets/og-image.jpg"
```

Expected: file exists, size between 50KB and 300KB.

- [ ] **Step 7: Commit**

```bash
cd "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice"
git add assets/og-image.jpg
git commit -m "feat: add OG social share image"
```

---

### Task 2: Create favicon and Apple touch icon

**Files:**
- Create: `assets/favicon.svg`
- Create: `assets/apple-touch-icon.png`

- [ ] **Step 1: Create favicon.svg**

Create `assets/favicon.svg` with this exact content:

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

- [ ] **Step 2: Generate Apple touch icon via Playwright MCP**

Write a temporary HTML file `assets/touch-icon-source.html`:

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; }
  body { width: 180px; height: 180px; background: #FFFFFF; display: flex; align-items: center; justify-content: center; }
</style>
</head>
<body>
  <svg width="120" height="120" viewBox="0 0 50 50" fill="none">
    <defs>
      <linearGradient id="fg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#FF6B35"/>
        <stop offset="100%" style="stop-color:#FFD23F"/>
      </linearGradient>
    </defs>
    <rect x="2" y="2" width="30" height="30" rx="7" fill="url(#fg)"/>
    <rect x="18" y="18" width="30" height="30" rx="7" fill="#004E89"/>
  </svg>
</body>
</html>
```

Using Playwright MCP: navigate to `http://localhost:8000/assets/touch-icon-source.html`, resize to 180×180, take screenshot — save to `assets/apple-touch-icon.png`.

- [ ] **Step 3: Clean up temp file**

```bash
rm "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice/assets/touch-icon-source.html"
```

- [ ] **Step 4: Verify both files exist**

```bash
ls -lh "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice/assets/favicon.svg"
ls -lh "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice/assets/apple-touch-icon.png"
```

Expected: both files present. `favicon.svg` under 1KB. `apple-touch-icon.png` under 50KB.

- [ ] **Step 5: Commit**

```bash
cd "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice"
git add assets/favicon.svg assets/apple-touch-icon.png
git commit -m "feat: add favicon and Apple touch icon"
```

---

### Task 3: Add tags to all 9 pages

**Files:**
- Modify: all 9 HTML files

Each page needs three insertions:

**A) OG image tags** — add after the existing `<meta property="og:url" ...>` line:
```html
  <meta property="og:image" content="https://captureninvoice.com/assets/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
```

**B) Favicon links** — add after the `<meta property="og:image:height" ...>` line just added:
```html
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
```

**C) Microsoft Clarity snippet** — add after the closing `</script>` of the GA4 block (the block that ends with `gtag('config', 'G-6WRXJRYEW0');`):
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

- [ ] **Step 1: Update index.html**

Apply all three insertions (A, B, C) to `index.html`.

In `index.html`, the existing OG block ends with:
```html
  <meta property="og:url" content="https://captureninvoice.com/">
```
Insert A + B immediately after this line.

The GA4 block ends with:
```html
    gtag('config', 'G-6WRXJRYEW0');
  </script>
```
Insert C immediately after the `</script>`.

- [ ] **Step 2: Update product.html**

Same three insertions. The OG url tag in this file is:
```html
  <meta property="og:url" content="https://captureninvoice.com/product">
```
Insert A + B after it. Insert C after the GA4 `</script>`.

- [ ] **Step 3: Update features.html**

Same. OG url tag:
```html
  <meta property="og:url" content="https://captureninvoice.com/features">
```

- [ ] **Step 4: Update how-it-works.html**

Same. OG url tag:
```html
  <meta property="og:url" content="https://captureninvoice.com/how-it-works">
```

- [ ] **Step 5: Update pricing.html**

Same. OG url tag:
```html
  <meta property="og:url" content="https://captureninvoice.com/pricing">
```

- [ ] **Step 6: Update about.html**

Same. OG url tag:
```html
  <meta property="og:url" content="https://captureninvoice.com/about">
```

- [ ] **Step 7: Update privacy.html**

Same. OG url tag:
```html
  <meta property="og:url" content="https://captureninvoice.com/privacy">
```

- [ ] **Step 8: Update terms.html**

Same. OG url tag:
```html
  <meta property="og:url" content="https://captureninvoice.com/terms">
```

- [ ] **Step 9: Update security.html**

Same. OG url tag:
```html
  <meta property="og:url" content="https://captureninvoice.com/security">
```

- [ ] **Step 10: Verify all 9 pages have the tags**

```bash
cd "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice"
grep -l 'og:image' index.html product.html features.html how-it-works.html pricing.html about.html privacy.html terms.html security.html | wc -l
```
Expected: `9`

```bash
grep -l 'favicon.svg' index.html product.html features.html how-it-works.html pricing.html about.html privacy.html terms.html security.html | wc -l
```
Expected: `9`

```bash
grep -l 'YOUR_CLARITY_ID' index.html product.html features.html how-it-works.html pricing.html about.html privacy.html terms.html security.html | wc -l
```
Expected: `9`

- [ ] **Step 11: Commit**

```bash
git add index.html product.html features.html how-it-works.html pricing.html about.html privacy.html terms.html security.html
git commit -m "feat: add OG image tags, favicon links, and Clarity snippet to all 9 pages"
```

---

### Task 4: Update CLAUDE.md

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add Search Console steps and Clarity activation note to CLAUDE.md**

Find the `## Next Steps (Pending)` section in `CLAUDE.md` and replace it with:

```markdown
## Google Search Console

To submit the sitemap (manual — requires your Google account):
1. Go to https://search.google.com/search-console
2. Add property → enter `https://captureninvoice.com`
3. Verify ownership via DNS TXT record with your domain registrar
4. Once verified: Sitemaps → submit `https://captureninvoice.com/sitemap.xml`

## Microsoft Clarity

All 9 pages have the Clarity snippet installed with a `YOUR_CLARITY_ID` placeholder.

To activate:
1. Go to https://clarity.microsoft.com
2. Create a new project for CaptureNInvoice
3. Copy your project ID (looks like `abc12345`)
4. Run this from the project root:
   ```bash
   grep -rl 'YOUR_CLARITY_ID' . --include="*.html" | xargs sed -i '' 's/YOUR_CLARITY_ID/YOUR_ACTUAL_ID/g'
   ```
5. Commit and push

## Next Steps (Pending)

1. Submit sitemap to Google Search Console (see above)
2. Activate Microsoft Clarity (see above — replace YOUR_CLARITY_ID)
3. Migrate demo video to Vimeo and replace `<video>` tag with embed
```

- [ ] **Step 2: Commit**

```bash
cd "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice"
git add CLAUDE.md
git commit -m "docs: add Search Console and Clarity activation steps to CLAUDE.md"
```
