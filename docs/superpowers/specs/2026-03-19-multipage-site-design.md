# Multi-Page Marketing Site — Design Spec
**Date:** 2026-03-19
**Project:** CaptureNInvoice marketing website
**Status:** Approved by user

---

## Goal

Convert the single-page `index.html` marketing site into a proper multi-page static site. Each top nav item links to a real, dedicated page. Visual style, brand, and layout direction are unchanged.

---

## Architecture

### Prerequisites
Both `css/` and `js/` directories already exist in the repo (empty). No mkdir needed.

### Approach
Extract shared CSS and nav JS from `index.html` into shared files. Each page is a standalone HTML file that links to those shared files.

### File Structure

```
captureninvoice/
├── css/
│   └── styles.css          ← extracted from index.html (~1,040 lines)
├── js/
│   └── nav.js              ← shared nav behaviours (see below)
├── index.html              ← updated: external CSS/JS, nav links → page paths
├── product.html            ← new
├── features.html           ← new
├── how-it-works.html       ← new
├── pricing.html            ← new
├── about.html              ← new
├── sitemap.xml             ← updated: all 6 URLs
├── robots.txt              ← unchanged
└── server.py               ← unchanged
```

### Nav link format — local dev compatibility
Nav `href` values use `.html` extensions (e.g. `product.html`, `features.html`). This is guaranteed to work on the Python `http.server` local dev server with no configuration changes. On Netlify/Vercel in production, both `/product` and `product.html` resolve correctly.

All internal nav, footer, and CTA links use this format consistently.

### Shared JS (`js/nav.js`)
Extracted from `index.html` script block. Contains exactly these four behaviours:
1. Scroll listener → toggles `.scrolled` on `#mainNav`
2. Hamburger click → toggles `.open` on `#mobileMenu`
3. Mobile menu link click → removes `.open` from `#mobileMenu`
4. Smooth-scroll handler for `a[href^="#"]` — kept in nav.js so `index.html` anchor links still work; harmless no-op on subpages that have no in-page anchors

**FAQ accordion JS** — kept inline on both `index.html` and `pricing.html` (the two pages with FAQ accordions). Not extracted to a shared file.

**Reveal-on-scroll IntersectionObserver** — kept inline on each page individually.

---

## Navigation

### Logo link
On all pages, the logo `href` is `/` (homepage). Clicking it always returns to the homepage.

### Desktop + Mobile Nav Links (all pages)
| Label | href |
|---|---|
| Product | product.html |
| Features | features.html |
| How It Works | how-it-works.html |
| Pricing | pricing.html |
| About | about.html |
| Sign In | https://app.captureninvoice.com/login |
| Get Started | https://app.captureninvoice.com/register |

### Footer Updates
- Product column: `features.html`, `how-it-works.html`, `pricing.html`
- Company column: `about.html` (live), Blog/Contact/Careers remain `#` (not built yet)
- No invented links added

### CTA href standard
All "Get Started Free" / "Get Started" CTA buttons across all pages use the absolute URL `https://app.captureninvoice.com/register`.

---

## Open Graph & Structured Data on Subpages

Each subpage includes minimal Open Graph meta tags (`og:title`, `og:description`, `og:type`, `og:url`). No JSON-LD structured data is added to subpages — the Organization and SoftwareApplication schemas on `index.html` are sufficient for the site as a whole.

**`index.html` structured data update:** The existing SoftwareApplication JSON-LD `offers` block currently references `"name": "Starter"` with `"price": "0"`. Update it to reflect the live pricing:
```json
"offers": {
  "@type": "Offer",
  "name": "Basic",
  "price": "9",
  "priceCurrency": "USD"
}
```

---

## Pages

### `/` — Homepage (`index.html`)
**Purpose:** Main marketing front door.

**Structure (unchanged):**
- Hero with primary CTA
- Logos bar ("Built for" industry strip)
- How It Works (3-step)
- Why CaptureNInvoice
- Features grid
- Who It's For
- Testimonials
- Pricing preview
- FAQ accordion (FAQ accordion JS stays inline here)
- Final CTA
- Footer

**Changes:** Nav anchor hrefs → `.html` page paths. Logo href → `/`. External `css/styles.css` and `js/nav.js` links replace embedded style block and inline nav JS. SoftwareApplication JSON-LD offer updated.

---

### `/product` — Product page (`product.html`)
**Purpose:** Explain what CaptureNInvoice is.

**`<title>`:** `What is CaptureNInvoice? — Proof-of-Work Invoicing`
**`<meta description>`:** `CaptureNInvoice is a proof-of-work invoicing platform for service businesses. Document jobs, attach photos, send invoices, and get paid faster.`
**Canonical:** `https://captureninvoice.com/product`
**OG tags:** og:title, og:description, og:type=website, og:url matching above.

**Sections:**
1. **Hero** — Pill: "The Product" / H1: "Proof-of-work invoicing built for real service work" / subhead: "CaptureNInvoice helps service professionals document completed jobs with photos and notes, attach that proof to invoices, and collect payment with more confidence."
2. **Why it exists** — paragraph: "Most invoicing tools were built for accountants and office workers. They let you send a bill — but they don't let you prove the work was done. For service businesses working in the field, that gap creates disputes, delayed payments, and lost trust. CaptureNInvoice closes that gap."
3. **Value grid** — 4 cards:
   - Document the Work: Capture photos, notes, and job details on-site before you leave.
   - Send the Invoice: Attach proof of work and send a professional invoice by shareable link.
   - Reduce Disputes: Clients see exactly what was completed before they pay — no guesswork.
   - Track Revenue: Monitor paid vs outstanding invoices and revenue growth over time.
4. **CTA** — "Get Started Free" → `https://app.captureninvoice.com/register`

---

### `/features` — Features page (`features.html`)
**Purpose:** Show product capabilities in detail.

**`<title>`:** `Features — CaptureNInvoice`
**`<meta description>`:** `See all CaptureNInvoice features: proof-of-work photo invoicing, online payments, revenue tracking, and client management for service businesses.`
**Canonical:** `https://captureninvoice.com/features`
**OG tags:** og:title, og:description, og:type=website, og:url matching above.

**Sections:**
1. **Hero** — H1: "Everything you need to document work, invoice clients, and get paid" / subhead: "Purpose-built features for job-based service businesses."
2. **Feature groups** — 5 groups, each with title + 3 bullet points:

   **A. Proof of Work**
   - Attach before/after photos to every invoice
   - Add job notes and work details
   - Show clients exactly what was completed

   **B. Professional Invoicing**
   - Create polished invoices in minutes
   - Add line items, notes, due dates, and branding
   - Send invoices by link or email

   **C. Payments**
   - Let clients pay online directly from the invoice
   - Supports Stripe and manual payment workflows
   - Track paid vs outstanding invoices

   **D. Revenue Visibility**
   - See total revenue at a glance
   - Monitor invoice status across all clients
   - Track payment activity over time

   **E. Client Management**
   - Store client details for reuse
   - Pull up client info when creating new invoices
   - Keep work history organised by customer

3. **CTA** — "Get Started Free" → `https://app.captureninvoice.com/register`

---

### `/how-it-works` — How It Works page (`how-it-works.html`)
**Purpose:** Explain the workflow simply.

**`<title>`:** `How It Works — CaptureNInvoice`
**`<meta description>`:** `See how CaptureNInvoice works: document the job, send a proof-of-work invoice, and get paid faster in three simple steps.`
**Canonical:** `https://captureninvoice.com/how-it-works`
**OG tags:** og:title, og:description, og:type=website, og:url matching above.

**Sections:**
1. **Hero** — H1: "From completed work to paid invoice" / subhead: "Three steps. One workflow. Less friction."
2. **3-step flow** (numbered):
   - Step 1 — Document the Work: Take photos, add notes, and record the completed job before you leave the site.
   - Step 2 — Send the Invoice: Create a professional invoice with your proof of work attached and send it to the client by link.
   - Step 3 — Get Paid Faster: Clients review the work, pay online or by approved payment method, and you track payment status inside CaptureNInvoice.
3. **Why this workflow matters** — 4-point list:
   - Reduces billing disputes — clients can see what was done
   - Improves professionalism — every invoice looks polished
   - Speeds up payment collection — less back-and-forth
   - Keeps records in one place — photos, notes, and invoices together
4. **CTA** — "Get Started Free" → `https://app.captureninvoice.com/register`

---

### `/pricing` — Pricing page (`pricing.html`)
**Purpose:** Present plans clearly and credibly.

**`<title>`:** `Pricing — CaptureNInvoice`
**`<meta description>`:** `Simple, transparent pricing for service businesses. Start free or upgrade for more control and workflow tools.`
**Canonical:** `https://captureninvoice.com/pricing`
**OG tags:** og:title, og:description, og:type=website, og:url matching above.

**Sections:**
1. **Hero** — H1: "Simple, transparent pricing" / subhead: "No hidden fees. No bloated tiers. Just the tools you need to invoice with proof."
2. **Plan cards:**

   **Basic — $9/month**
   For solo operators who want proof-of-work invoicing and a clean way to send invoices.
   Features (real only):
   - Proof-of-work photo invoices
   - Online payment collection
   - Revenue dashboard
   - Client management

   **Pro — $25/month**
   For growing service businesses that want more control, stronger workflow tools, and more advanced visibility.
   Features:
   - Everything in Basic
   - Advanced revenue reporting *(coming soon)*
   - Priority support *(coming soon)*
   - Team access *(coming soon)*

3. **Mini FAQ** — accordion with FAQ accordion JS inline. Full Q&A:

   Q: Do my clients need an account to pay?
   A: No. Clients receive a payment link and can pay directly — no account, no sign-up, no friction. They open the link, see your work, and pay.

   Q: Can I attach proof of work to invoices?
   A: Yes — that's the core of CaptureNInvoice. You can attach before/after photos, work logs, and job notes directly to each invoice. Clients see your proof when they open the payment link.

   Q: Is CaptureNInvoice good for small service businesses?
   A: Yes. It's designed specifically for solo operators and small teams in the trades — cleaners, landscapers, painters, handymen, and similar businesses.

   Q: Can I use Stripe or manual payment methods?
   A: Yes. CaptureNInvoice supports online payment collection via Stripe as well as manual payment workflows for clients who prefer to pay by other means.

   Q: Can I track paid and unpaid invoices?
   A: Yes. The revenue dashboard shows paid invoices, outstanding amounts, and your total earnings — so you always know where you stand.

4. **CTA** — "Get Started Free" → `https://app.captureninvoice.com/register`

---

### `/about` — About page (`about.html`)
**Purpose:** Mission and audience clarity.

**`<title>`:** `About — CaptureNInvoice`
**`<meta description>`:** `CaptureNInvoice was built for service professionals who complete real work on-site and need a better way to document it, invoice for it, and get paid faster.`
**Canonical:** `https://captureninvoice.com/about`
**OG tags:** og:title, og:description, og:type=website, og:url matching above.

**Sections:**
1. **Hero** — H1: "Built for service businesses that need proof, professionalism, and faster payment" / intro paragraph: "CaptureNInvoice was created for service professionals who complete real work on-site and need a better way to document it, invoice for it, and get paid with less friction. We built it because generic invoicing tools were never designed for the field."
2. **Audience list** — 6 business types with icons: Cleaners 🧹, Landscapers 🌿, Painters 🎨, Handymen 🔧, Maintenance Professionals 🏠, Field Service Businesses 🏗️
3. **Why generic tools fall short** — short section:
   - They let you invoice the work — but they don't prove the work was done
   - No photo documentation attached to invoices
   - No on-site job records
   - No protection when clients dispute what was completed
4. **Closing** — "CaptureNInvoice connects documentation, invoicing, and payment into one workflow designed for job-based businesses."
5. **CTA** — "Get Started Free" → `https://app.captureninvoice.com/register`

---

## Sitemap

Replace `sitemap.xml` content with all 6 URLs using correct `http://` namespace:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://captureninvoice.com/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://captureninvoice.com/product</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://captureninvoice.com/features</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://captureninvoice.com/how-it-works</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://captureninvoice.com/pricing</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://captureninvoice.com/about</loc>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>
```

---

## Constraints

- Do not touch authenticated routes at `app.captureninvoice.com`
- Do not invent features not yet built — use "coming soon" label only on Pro plan extras
- Do not add social links, support emails, or logos that do not exist
- All CTA links use absolute URL `https://app.captureninvoice.com/register`
- Footer placeholder links (Blog, Contact, Careers, Privacy, Terms) remain as `#`
