# Multi-Page Marketing Site — Design Spec
**Date:** 2026-03-19
**Project:** CaptureNInvoice marketing website
**Status:** Approved by user

---

## Goal

Convert the single-page `index.html` marketing site into a proper multi-page static site. Each top nav item links to a real, dedicated page. Visual style, brand, and layout direction are unchanged.

---

## Architecture

### Approach
Extract shared CSS and nav JS from `index.html` into shared files. Each page is a standalone HTML file that links to those shared files.

### File Structure

```
captureninvoice/
├── css/
│   └── styles.css          ← extracted from index.html (~1,040 lines)
├── js/
│   └── nav.js              ← shared: scroll→scrolled, hamburger, mobile close
├── index.html              ← updated: external CSS/JS, nav links → /page paths
├── product.html            ← new
├── features.html           ← new
├── how-it-works.html       ← new
├── pricing.html            ← new
├── about.html              ← new
├── sitemap.xml             ← updated: all 6 URLs
├── robots.txt              ← unchanged
└── server.py               ← unchanged
```

### Shared JS (`js/nav.js`)
Extracted from `index.html` script block. Contains:
- Scroll listener → toggles `.scrolled` on `#mainNav`
- Hamburger click → toggles `.open` on `#mobileMenu`
- Mobile menu link click → removes `.open` from `#mobileMenu`

FAQ accordion JS stays inline on `/pricing` only (single-page use).
Reveal-on-scroll IntersectionObserver stays inline on each page.

---

## Navigation

### Desktop + Mobile Nav Links (all pages)
| Label | href |
|---|---|
| Product | /product |
| Features | /features |
| How It Works | /how-it-works |
| Pricing | /pricing |
| About | /about |
| Sign In | https://app.captureninvoice.com/login |
| Get Started | https://app.captureninvoice.com/register |

### Footer Updates
- Product column: `/features`, `/how-it-works`, `/pricing`
- Company column: `/about` (live), Blog/Contact/Careers remain `#` (not built yet)
- No invented links added

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
- FAQ accordion
- Final CTA
- Footer

**Nav update only:** anchor hrefs → page paths.

---

### `/product` — Product page (`product.html`)
**Purpose:** Explain what CaptureNInvoice is.

**`<title>`:** `What is CaptureNInvoice? — Proof-of-Work Invoicing`
**`<meta description>`:** `CaptureNInvoice is a proof-of-work invoicing platform for service businesses. Document jobs, attach photos, send invoices, and get paid faster.`
**Canonical:** `https://captureninvoice.com/product`

**Sections:**
1. **Hero** — Pill: "The Product" / H1: "Proof-of-work invoicing built for real service work" / subhead: "CaptureNInvoice helps service professionals document completed jobs with photos and notes, attach that proof to invoices, and collect payment with more confidence."
2. **Why it exists** — short paragraph: generic invoicing tools invoice the work but don't prove it was done; this creates disputes, slow payment, and lost trust
3. **Value grid** — 4 cards:
   - Document the Work: capture photos, notes, and job details on-site
   - Send the Invoice: attach proof and send a professional invoice by link
   - Reduce Disputes: clients see exactly what was done before they pay
   - Track Revenue: monitor paid vs outstanding and growth over time
4. **CTA** — "Get Started Free" → `/register`

---

### `/features` — Features page (`features.html`)
**Purpose:** Show product capabilities in detail.

**`<title>`:** `Features — CaptureNInvoice`
**`<meta description>`:** `See all CaptureNInvoice features: proof-of-work photo invoicing, online payments, revenue tracking, and client management for service businesses.`
**Canonical:** `https://captureninvoice.com/features`

**Sections:**
1. **Hero** — H1: "Everything you need to document work, invoice clients, and get paid" / subhead: "Purpose-built features for job-based service businesses."
2. **Feature groups** — 5 groups, each with title + 3 bullet points:

   **A. Proof of Work**
   - Attach before/after photos to invoices
   - Add job notes and work details
   - Show clients exactly what was completed

   **B. Professional Invoicing**
   - Create polished invoices quickly
   - Add line items, notes, due dates, and branding
   - Send invoices by link or email

   **C. Payments**
   - Let clients pay online
   - Support Stripe and manual payment workflows
   - Track paid vs outstanding invoices

   **D. Revenue Visibility**
   - See total revenue at a glance
   - Monitor invoice status
   - Track payment activity over time

   **E. Client Management**
   - Store client details
   - Reuse client info for future invoices
   - Keep work organized by customer

3. **CTA** — "Get Started Free"

---

### `/how-it-works` — How It Works page (`how-it-works.html`)
**Purpose:** Explain the workflow simply.

**`<title>`:** `How It Works — CaptureNInvoice`
**`<meta description>`:** `See how CaptureNInvoice works: document the job, send a proof-of-work invoice, and get paid faster in three simple steps.`
**Canonical:** `https://captureninvoice.com/how-it-works`

**Sections:**
1. **Hero** — H1: "From completed work to paid invoice" / subhead: "Three steps. One workflow. Less friction."
2. **3-step flow** (numbered):
   - Step 1 — Document the Work: Take photos, add notes, and record the completed job.
   - Step 2 — Send the Invoice: Create a professional invoice with proof of work attached and send it to the client.
   - Step 3 — Get Paid Faster: Clients review the work, pay online or by approved payment method, and you track status inside CaptureNInvoice.
3. **Why this workflow matters** — 4-point list:
   - Reduces billing disputes
   - Improves professionalism
   - Speeds up payment collection
   - Keeps records in one place
4. **CTA** — "Get Started Free"

---

### `/pricing` — Pricing page (`pricing.html`)
**Purpose:** Present plans clearly and credibly.

**`<title>`:** `Pricing — CaptureNInvoice`
**`<meta description>`:** `Simple, transparent pricing for service businesses. Start free or upgrade for more control and workflow tools.`
**Canonical:** `https://captureninvoice.com/pricing`

**Sections:**
1. **Hero** — H1: "Simple, transparent pricing" / subhead: "No hidden fees. No bloated tiers. Just the tools you need to invoice with proof."
2. **Plan cards:**

   **Basic — $9/month**
   For solo operators who want proof-of-work invoicing and a clean way to send invoices.
   Features listed (real only — no invented claims):
   - Proof-of-work photo invoices
   - Online payment collection
   - Revenue dashboard
   - Client management

   **Pro — $25/month**
   For growing service businesses that want more control, stronger workflow tools, and more advanced visibility.
   Features listed:
   - Everything in Basic
   - Advanced revenue reporting *(coming soon)*
   - Priority support *(coming soon)*
   - Team access *(coming soon)*

3. **Mini FAQ** — accordion, 5 questions:
   - Do my clients need an account to pay?
   - Can I attach proof of work to invoices?
   - Is CaptureNInvoice good for small service businesses?
   - Can I use Stripe or manual payment methods?
   - Can I track paid and unpaid invoices?
4. **CTA** — "Get Started Free"

---

### `/about` — About page (`about.html`)
**Purpose:** Mission and audience clarity.

**`<title>`:** `About — CaptureNInvoice`
**`<meta description>`:** `CaptureNInvoice was built for service professionals who complete real work on-site and need a better way to document it, invoice for it, and get paid faster.`
**Canonical:** `https://captureninvoice.com/about`

**Sections:**
1. **Hero** — H1: "Built for service businesses that need proof, professionalism, and faster payment" / intro paragraph from spec
2. **Audience list** — 6 business types with icons: Cleaners, Landscapers, Painters, Handymen, Maintenance Professionals, Field Service Businesses
3. **Why generic tools fall short** — short section: they invoice the work but don't prove it; no photo documentation, no job records, no dispute protection
4. **Closing** — "CaptureNInvoice connects documentation, invoicing, and payment into one workflow designed for job-based businesses."
5. **CTA** — "Get Started Free"

---

## Sitemap Updates

Add to `sitemap.xml`:
```xml
<url><loc>https://captureninvoice.com/product</loc><priority>0.8</priority></url>
<url><loc>https://captureninvoice.com/features</loc><priority>0.8</priority></url>
<url><loc>https://captureninvoice.com/how-it-works</loc><priority>0.8</priority></url>
<url><loc>https://captureninvoice.com/pricing</loc><priority>0.9</priority></url>
<url><loc>https://captureninvoice.com/about</loc><priority>0.7</priority></url>
```

---

## Constraints

- Do not touch authenticated routes at `app.captureninvoice.com`
- Do not invent features not yet built — use "coming soon" label only on Pro plan extras
- Do not add social links, support emails, or logos that do not exist
- Keep all existing Sign In / Get Started href values unchanged
- Footer placeholder links (Blog, Contact, Careers, Privacy, Terms) remain as `#`
