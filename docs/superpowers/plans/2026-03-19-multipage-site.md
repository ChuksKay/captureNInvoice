# Multi-Page Marketing Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the single-page `index.html` marketing site into a proper 6-page static site with a shared CSS file, shared nav JS, and five new content pages.

**Architecture:** Extract the ~1,040-line embedded CSS to `css/styles.css` and the nav JS behaviours to `js/nav.js`. Each page is a standalone HTML file that links to those shared files. Pages use `.html` extensions in all internal links for compatibility with the Python local dev server.

**Tech Stack:** Static HTML, CSS, vanilla JS, Python HTTP server for local dev.

**Spec:** `docs/superpowers/specs/2026-03-19-multipage-site-design.md`

---

## Shared Template Reference

> Copy this nav/footer/script block into every new page. Do not modify it per-page except the `<head>` metadata.

### Shared Nav HTML
```html
<!-- ────────────────────── NAV ────────────────────────────────── -->
<nav class="nav" id="mainNav">
  <div class="nav__inner">
    <a href="/" class="nav__logo">
      <svg width="32" height="32" viewBox="0 0 50 50" fill="none" xmlns="http://www.w3.org/2000/svg" style="flex-shrink:0">
        <defs>
          <linearGradient id="navGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FF6B35;stop-opacity:1"/>
            <stop offset="100%" style="stop-color:#FFD23F;stop-opacity:1"/>
          </linearGradient>
        </defs>
        <rect x="2" y="2" width="30" height="30" rx="7" fill="url(#navGrad)"/>
        <rect x="18" y="18" width="30" height="30" rx="7" fill="#004E89" opacity="0.95"/>
      </svg>
      CaptureNInvoice
    </a>
    <div class="nav__links">
      <a href="product.html">Product</a>
      <a href="features.html">Features</a>
      <a href="how-it-works.html">How It Works</a>
      <a href="pricing.html">Pricing</a>
      <a href="about.html">About</a>
    </div>
    <div class="nav__actions">
      <a href="https://app.captureninvoice.com/login" class="btn btn--ghost btn--sm">Sign In</a>
      <a href="https://app.captureninvoice.com/register" class="btn btn--primary btn--sm">Get Started</a>
    </div>
    <button class="nav__hamburger" id="hamburger" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>

<!-- Mobile nav -->
<div class="nav__mobile" id="mobileMenu">
  <a href="product.html">Product</a>
  <a href="features.html">Features</a>
  <a href="how-it-works.html">How It Works</a>
  <a href="pricing.html">Pricing</a>
  <a href="about.html">About</a>
  <div class="nav__mobile-actions">
    <a href="https://app.captureninvoice.com/login" class="btn btn--ghost">Sign In</a>
    <a href="https://app.captureninvoice.com/register" class="btn btn--primary">Get Started →</a>
  </div>
</div>
```

### Shared Footer HTML
```html
<!-- ────────────────────── FOOTER ─────────────────────────────── -->
<footer class="footer">
  <div class="container">
    <div class="footer__top">
      <div class="footer__brand">
        <div class="footer__logo">
          <svg width="28" height="28" viewBox="0 0 50 50" fill="none" xmlns="http://www.w3.org/2000/svg" style="flex-shrink:0">
            <defs>
              <linearGradient id="footGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#FF6B35;stop-opacity:1"/>
                <stop offset="100%" style="stop-color:#FFD23F;stop-opacity:1"/>
              </linearGradient>
            </defs>
            <rect x="2" y="2" width="30" height="30" rx="7" fill="url(#footGrad)"/>
            <rect x="18" y="18" width="30" height="30" rx="7" fill="#004E89" opacity="0.95"/>
          </svg>
          CaptureNInvoice
        </div>
        <p class="footer__tagline">Proof-of-work invoicing for service businesses. Document the work. Send the invoice. Get paid faster.</p>
      </div>
      <div>
        <div class="footer__col-title">Product</div>
        <div class="footer__links">
          <a href="features.html">Features</a>
          <a href="how-it-works.html">How It Works</a>
          <a href="pricing.html">Pricing</a>
          <a href="#">Changelog</a>
        </div>
      </div>
      <div>
        <div class="footer__col-title">App</div>
        <div class="footer__links">
          <a href="https://app.captureninvoice.com">Open App</a>
          <a href="https://app.captureninvoice.com/login">Sign In</a>
          <a href="https://app.captureninvoice.com/register">Create Account</a>
        </div>
      </div>
      <div>
        <div class="footer__col-title">Company</div>
        <div class="footer__links">
          <a href="about.html">About</a>
          <a href="#">Blog</a>
          <a href="#">Contact</a>
          <a href="#">Careers</a>
        </div>
      </div>
      <div>
        <div class="footer__col-title">Legal</div>
        <div class="footer__links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
          <a href="#">Security</a>
        </div>
      </div>
    </div>
    <div class="footer__bottom">
      <div class="footer__copy">© 2026 CaptureNInvoice. All rights reserved.</div>
      <div class="footer__legal">
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
        <a href="#">Contact</a>
      </div>
    </div>
  </div>
</footer>
```

### Shared Script Block (non-pricing pages)
```html
<script src="js/nav.js"></script>
<script>
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));
</script>
```

### Shared Script Block (pricing.html — adds FAQ accordion)
```html
<script src="js/nav.js"></script>
<script>
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

  document.querySelectorAll('.faq-item__q').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.faq-item');
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!isOpen) item.classList.add('open');
    });
  });
</script>
```

### Standard Page `<head>` Template
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PAGE TITLE HERE</title>
  <meta name="description" content="META DESCRIPTION HERE">
  <link rel="canonical" href="CANONICAL URL HERE">
  <meta property="og:title" content="PAGE TITLE HERE">
  <meta property="og:description" content="META DESCRIPTION HERE">
  <meta property="og:type" content="website">
  <meta property="og:url" content="CANONICAL URL HERE">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,700;12..96,800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
```

---

## Task 1: Extract CSS to `css/styles.css`

**Files:**
- Create: `css/styles.css`
- Modify: `index.html` (lines 20–1062: replace `<style>` block with `<link>` tag)

- [ ] **Step 1: Copy the CSS block out of index.html**

  In `index.html`, the CSS lives between `<style>` (line 20) and `</style>` (line 1062). Copy everything between those tags (not the tags themselves) and write it to `css/styles.css`.

  Then append these new classes at the **end** of `css/styles.css`, before the closing of the file:

  ```css
  /* ─── INNER PAGE HERO ────────────────────────────────────────── */
  .page-hero {
    padding: calc(var(--nav-h) + 80px) 0 80px;
    text-align: center;
    border-bottom: 1px solid var(--border);
  }
  .page-hero .pill { margin: 0 auto 20px; }
  .page-hero__title {
    font-family: var(--font-display);
    font-size: clamp(28px, 4.5vw, 48px);
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -0.025em;
    margin-bottom: 20px;
  }
  .page-hero__sub {
    font-size: 18px;
    color: var(--text-2);
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.65;
  }

  /* ─── PAGE SECTION ───────────────────────────────────────────── */
  .page-section { padding: 80px 0; }
  .page-section + .page-section { border-top: 1px solid var(--border); }
  .page-section__head { text-align: center; margin-bottom: 56px; }

  /* ─── VALUE GRID (product page) ──────────────────────────────── */
  .value-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    max-width: 840px;
    margin: 0 auto;
  }
  .value-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 32px;
  }
  .value-card__icon { font-size: 28px; margin-bottom: 16px; }
  .value-card__title {
    font-family: var(--font-display);
    font-size: 17px; font-weight: 700;
    margin-bottom: 8px;
  }
  .value-card__desc { font-size: 14px; color: var(--text-2); line-height: 1.65; }

  /* ─── FEATURE GROUPS (features page) ─────────────────────────── */
  .feat-groups {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 40px;
    max-width: 880px;
    margin: 0 auto;
  }
  .feat-group__title {
    font-family: var(--font-display);
    font-size: 16px; font-weight: 700;
    margin-bottom: 16px;
    display: flex; align-items: center; gap: 10px;
  }
  .feat-group__title-icon {
    width: 32px; height: 32px;
    background: var(--orange-dim);
    border-radius: var(--radius-sm);
    display: flex; align-items: center; justify-content: center;
    font-size: 16px;
  }
  .feat-group__list { display: flex; flex-direction: column; gap: 10px; }
  .feat-group__list li {
    font-size: 14px; color: var(--text-2); line-height: 1.6;
    display: flex; align-items: flex-start; gap: 10px;
  }
  .feat-group__list li::before {
    content: '✓';
    color: var(--green);
    font-weight: 700;
    flex-shrink: 0;
    margin-top: 1px;
  }

  /* ─── STEP FLOW (how-it-works page) ──────────────────────────── */
  .step-flow {
    display: flex; flex-direction: column; gap: 24px;
    max-width: 640px; margin: 0 auto;
  }
  .step-item {
    display: flex; gap: 24px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 32px;
  }
  .step-num {
    width: 40px; height: 40px; flex-shrink: 0;
    background: var(--orange);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-family: var(--font-display);
    font-size: 16px; font-weight: 800; color: #fff;
  }
  .step-body__title {
    font-family: var(--font-display);
    font-size: 17px; font-weight: 700;
    margin-bottom: 8px;
  }
  .step-body__desc { font-size: 14px; color: var(--text-2); line-height: 1.65; }

  /* ─── WHY MATTERS / SHORTFALL BOX ────────────────────────────── */
  .info-box {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-xl);
    padding: 40px 48px;
    max-width: 640px;
    margin: 0 auto;
  }
  .info-box__title {
    font-family: var(--font-display);
    font-size: 18px; font-weight: 700;
    margin-bottom: 20px;
  }
  .info-box__list { display: flex; flex-direction: column; gap: 12px; }
  .info-box__list li {
    font-size: 15px; color: var(--text-2);
    display: flex; align-items: flex-start; gap: 10px;
  }
  .info-box__list.checks li::before { content: '→'; color: var(--orange); font-weight: 700; flex-shrink: 0; }
  .info-box__list.crosses li::before { content: '✕'; color: #DC2626; font-weight: 700; flex-shrink: 0; }

  /* ─── AUDIENCE GRID (about page) ─────────────────────────────── */
  .audience-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    max-width: 720px;
    margin: 0 auto;
  }
  .audience-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 24px;
    display: flex; align-items: center; gap: 14px;
  }
  .audience-card__icon { font-size: 24px; }
  .audience-card__name { font-family: var(--font-display); font-size: 15px; font-weight: 700; }

  /* ─── PAGE CTA ────────────────────────────────────────────────── */
  .page-cta {
    padding: 100px 0;
    text-align: center;
    border-top: 1px solid var(--border);
  }
  .page-cta__title {
    font-family: var(--font-display);
    font-size: clamp(24px, 3.5vw, 36px);
    font-weight: 800;
    margin-bottom: 12px;
  }
  .page-cta__sub {
    font-size: 16px; color: var(--text-2);
    max-width: 440px;
    margin: 0 auto 32px;
    line-height: 1.6;
  }
  .page-cta__actions { display: flex; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap; }

  /* ─── RESPONSIVE ADDITIONS ───────────────────────────────────── */
  @media (max-width: 768px) {
    .value-grid { grid-template-columns: 1fr; }
    .feat-groups { grid-template-columns: 1fr; }
    .audience-grid { grid-template-columns: repeat(2, 1fr); }
    .info-box { padding: 28px 24px; }
    .step-item { flex-direction: column; gap: 16px; }
  }
  @media (max-width: 480px) {
    .audience-grid { grid-template-columns: 1fr; }
  }
  ```

- [ ] **Step 2: Replace the `<style>` block in index.html with a `<link>` tag**

  In `index.html`, replace:
  ```html
    <style>
      [~1040 lines of CSS]
    </style>
  ```
  With:
  ```html
    <link rel="stylesheet" href="css/styles.css">
  ```

- [ ] **Step 3: Verify locally**

  Start the server: `python server.py`
  Open `http://localhost:8000` — page should look identical to before. Check fonts, colors, layout on both desktop and mobile viewport. If unstyled: confirm `css/styles.css` exists and the `<link>` href path is correct.

- [ ] **Step 4: Commit**

  ```bash
  git add css/styles.css index.html
  git commit -m "Extract CSS to css/styles.css, add inner-page component classes"
  ```

---

## Task 2: Extract nav JS to `js/nav.js` and update `index.html`

**Files:**
- Create: `js/nav.js`
- Modify: `index.html` (nav links, logo href, footer links, script block, JSON-LD)

- [ ] **Step 1: Create `js/nav.js`**

  Write this file exactly:

  ```javascript
  // ─── NAV scroll behavior ──────────────────────────────────────
  const nav = document.getElementById('mainNav');
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 20);
  }, { passive: true });

  // ─── Mobile menu ──────────────────────────────────────────────
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
  });
  mobileMenu.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => mobileMenu.classList.remove('open'));
  });

  // ─── Smooth scroll for anchor links ──────────────────────────
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href').slice(1);
      if (!id) return;
      const target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
  ```

- [ ] **Step 2: Update nav links in `index.html` (desktop nav, lines ~1084–1088)**

  Replace:
  ```html
        <a href="#product">Product</a>
        <a href="#features">Features</a>
        <a href="#how-it-works">How It Works</a>
        <a href="#pricing">Pricing</a>
        <a href="#about">About</a>
  ```
  With:
  ```html
        <a href="product.html">Product</a>
        <a href="features.html">Features</a>
        <a href="how-it-works.html">How It Works</a>
        <a href="pricing.html">Pricing</a>
        <a href="about.html">About</a>
  ```

- [ ] **Step 3: Update mobile nav links in `index.html` (lines ~1102–1106)**

  Replace:
  ```html
    <a href="#product">Product</a>
    <a href="#features">Features</a>
    <a href="#how-it-works">How It Works</a>
    <a href="#pricing">Pricing</a>
    <a href="#about">About</a>
  ```
  With:
  ```html
    <a href="product.html">Product</a>
    <a href="features.html">Features</a>
    <a href="how-it-works.html">How It Works</a>
    <a href="pricing.html">Pricing</a>
    <a href="about.html">About</a>
  ```

- [ ] **Step 4: Update logo href in `index.html` (line ~1070)**

  Replace:
  ```html
      <a href="#" class="nav__logo">
  ```
  With:
  ```html
      <a href="/" class="nav__logo">
  ```

- [ ] **Step 5: Update footer Product column links in `index.html` (lines ~1755–1757)**

  Replace:
  ```html
            <a href="#features">Features</a>
            <a href="#how-it-works">How It Works</a>
            <a href="#pricing">Pricing</a>
  ```
  With:
  ```html
            <a href="features.html">Features</a>
            <a href="how-it-works.html">How It Works</a>
            <a href="pricing.html">Pricing</a>
  ```

- [ ] **Step 6: Update footer Company column About link in `index.html` (line ~1774)**

  Replace:
  ```html
            <a href="#">About</a>
  ```
  With:
  ```html
            <a href="about.html">About</a>
  ```

- [ ] **Step 7: Update SoftwareApplication JSON-LD offer in `index.html` (lines ~41–44)**

  Replace:
  ```json
      "offers": {
        "@type": "Offer",
        "name": "Starter",
        "price": "0",
        "priceCurrency": "USD"
      }
  ```
  With:
  ```json
      "offers": {
        "@type": "Offer",
        "name": "Basic",
        "price": "9",
        "priceCurrency": "USD"
      }
  ```

- [ ] **Step 8: Replace the inline `<script>` block in `index.html` (lines ~1802–1855)**

  Replace the entire `<script>` block with:
  ```html
    <script src="js/nav.js"></script>
    <script>
      // ─── Reveal on scroll ─────────────────────────────────────────
      const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            revealObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
      document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

      // ─── FAQ accordion ────────────────────────────────────────────
      document.querySelectorAll('.faq-item__q').forEach(btn => {
        btn.addEventListener('click', () => {
          const item = btn.closest('.faq-item');
          const isOpen = item.classList.contains('open');
          document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
          if (!isOpen) item.classList.add('open');
        });
      });
    </script>
  ```

- [ ] **Step 9: Verify locally**

  Reload `http://localhost:8000`. Confirm:
  - Clicking a nav link navigates to the correct `.html` page (will 404 until pages are built — that's fine)
  - Logo click goes to `/`
  - Hamburger opens/closes mobile menu
  - FAQ accordion still works
  - Scroll still adds `.scrolled` to nav

- [ ] **Step 10: Commit**

  ```bash
  git add js/nav.js index.html
  git commit -m "Extract nav JS, update nav/footer links to .html pages, fix JSON-LD offer"
  ```

---

## Task 3: Create `product.html`

**Files:**
- Create: `product.html`

- [ ] **Step 1: Create the file with this exact content**

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>What is CaptureNInvoice? — Proof-of-Work Invoicing</title>
    <meta name="description" content="CaptureNInvoice is a proof-of-work invoicing platform for service businesses. Document jobs, attach photos, send invoices, and get paid faster.">
    <link rel="canonical" href="https://captureninvoice.com/product">
    <meta property="og:title" content="What is CaptureNInvoice? — Proof-of-Work Invoicing">
    <meta property="og:description" content="CaptureNInvoice is a proof-of-work invoicing platform for service businesses. Document jobs, attach photos, send invoices, and get paid faster.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://captureninvoice.com/product">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,700;12..96,800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
  </head>
  <body>

    [PASTE SHARED NAV HTML FROM TEMPLATE ABOVE]

    <!-- ────────────────────── HERO ───────────────────────────────── -->
    <section class="page-hero">
      <div class="container">
        <div class="pill pill--orange reveal" style="margin:0 auto 20px">
          <svg width="8" height="8" viewBox="0 0 8 8" fill="currentColor"><circle cx="4" cy="4" r="4"/></svg>
          The Product
        </div>
        <h1 class="page-hero__title reveal" style="transition-delay:0.1s">Proof-of-work invoicing built<br>for real service work</h1>
        <p class="page-hero__sub reveal" style="transition-delay:0.2s">CaptureNInvoice helps service professionals document completed jobs with photos and notes, attach that proof to invoices, and collect payment with more confidence.</p>
      </div>
    </section>

    <!-- ────────────────────── WHY IT EXISTS ─────────────────────── -->
    <section class="page-section">
      <div class="container">
        <div class="page-section__head">
          <div class="section-label reveal">Why It Exists</div>
          <h2 class="section-title reveal" style="transition-delay:0.1s">The gap in generic invoicing tools</h2>
          <p class="section-sub reveal" style="transition-delay:0.2s">Most invoicing tools were built for accountants and office workers. They let you send a bill — but they don't let you prove the work was done. For service businesses working in the field, that gap creates disputes, delayed payments, and lost trust. CaptureNInvoice closes that gap.</p>
        </div>
      </div>
    </section>

    <!-- ────────────────────── VALUE GRID ────────────────────────── -->
    <section class="page-section">
      <div class="container">
        <div class="page-section__head">
          <div class="section-label reveal">What It Does</div>
          <h2 class="section-title reveal" style="transition-delay:0.1s">One workflow. Four outcomes.</h2>
        </div>
        <div class="value-grid">
          <div class="value-card reveal">
            <div class="value-card__icon">📷</div>
            <div class="value-card__title">Document the Work</div>
            <div class="value-card__desc">Capture before/after photos, notes, and job details on-site before you leave.</div>
          </div>
          <div class="value-card reveal" style="transition-delay:0.08s">
            <div class="value-card__icon">📄</div>
            <div class="value-card__title">Send the Invoice</div>
            <div class="value-card__desc">Attach proof of work and send a professional invoice to the client by shareable link.</div>
          </div>
          <div class="value-card reveal" style="transition-delay:0.16s">
            <div class="value-card__icon">🛡️</div>
            <div class="value-card__title">Reduce Disputes</div>
            <div class="value-card__desc">Clients see exactly what was completed before they pay — no guesswork, no back-and-forth.</div>
          </div>
          <div class="value-card reveal" style="transition-delay:0.24s">
            <div class="value-card__icon">📈</div>
            <div class="value-card__title">Track Revenue</div>
            <div class="value-card__desc">Monitor paid vs outstanding invoices and watch your revenue grow over time.</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ────────────────────── PAGE CTA ──────────────────────────── -->
    <section class="page-cta">
      <div class="container">
        <h2 class="page-cta__title reveal">Ready to invoice with proof?</h2>
        <p class="page-cta__sub reveal" style="transition-delay:0.1s">Join service professionals already using CaptureNInvoice to document their work and get paid faster.</p>
        <div class="page-cta__actions reveal" style="transition-delay:0.2s">
          <a href="https://app.captureninvoice.com/register" class="btn btn--primary">
            Get Started Free
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 7h8M7 3l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="https://app.captureninvoice.com/login" class="btn btn--ghost">Sign In</a>
        </div>
      </div>
    </section>

    [PASTE SHARED FOOTER HTML FROM TEMPLATE ABOVE]

    [PASTE SHARED SCRIPT BLOCK (non-pricing) FROM TEMPLATE ABOVE]

  </body>
  </html>
  ```

- [ ] **Step 2: Verify locally**

  Open `http://localhost:8000/product.html` — confirm nav renders, fonts load, value grid shows 4 cards, CTA button is orange, footer renders correctly.

- [ ] **Step 3: Commit**

  ```bash
  git add product.html
  git commit -m "Add /product page"
  ```

---

## Task 4: Create `features.html`

**Files:**
- Create: `features.html`

- [ ] **Step 1: Create the file**

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Features — CaptureNInvoice</title>
    <meta name="description" content="See all CaptureNInvoice features: proof-of-work photo invoicing, online payments, revenue tracking, and client management for service businesses.">
    <link rel="canonical" href="https://captureninvoice.com/features">
    <meta property="og:title" content="Features — CaptureNInvoice">
    <meta property="og:description" content="See all CaptureNInvoice features: proof-of-work photo invoicing, online payments, revenue tracking, and client management for service businesses.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://captureninvoice.com/features">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,700;12..96,800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
  </head>
  <body>

    [PASTE SHARED NAV HTML]

    <!-- ────────────────────── HERO ───────────────────────────────── -->
    <section class="page-hero">
      <div class="container">
        <div class="section-label reveal" style="margin:0 auto 20px">Features</div>
        <h1 class="page-hero__title reveal" style="transition-delay:0.1s">Everything you need to document work,<br>invoice clients, and get paid</h1>
        <p class="page-hero__sub reveal" style="transition-delay:0.2s">Purpose-built features for job-based service businesses.</p>
      </div>
    </section>

    <!-- ────────────────────── FEATURE GROUPS ────────────────────── -->
    <section class="page-section">
      <div class="container">
        <div class="feat-groups">

          <div class="feat-group reveal">
            <div class="feat-group__title">
              <div class="feat-group__title-icon">📷</div>
              Proof of Work
            </div>
            <ul class="feat-group__list">
              <li>Attach before/after photos to every invoice</li>
              <li>Add job notes and work details</li>
              <li>Show clients exactly what was completed</li>
            </ul>
          </div>

          <div class="feat-group reveal" style="transition-delay:0.08s">
            <div class="feat-group__title">
              <div class="feat-group__title-icon">📄</div>
              Professional Invoicing
            </div>
            <ul class="feat-group__list">
              <li>Create polished invoices in minutes</li>
              <li>Add line items, notes, due dates, and branding</li>
              <li>Send invoices by link or email</li>
            </ul>
          </div>

          <div class="feat-group reveal" style="transition-delay:0.16s">
            <div class="feat-group__title">
              <div class="feat-group__title-icon">💳</div>
              Payments
            </div>
            <ul class="feat-group__list">
              <li>Let clients pay online directly from the invoice</li>
              <li>Supports Stripe and manual payment workflows</li>
              <li>Track paid vs outstanding invoices</li>
            </ul>
          </div>

          <div class="feat-group reveal" style="transition-delay:0.08s">
            <div class="feat-group__title">
              <div class="feat-group__title-icon">📈</div>
              Revenue Visibility
            </div>
            <ul class="feat-group__list">
              <li>See total revenue at a glance</li>
              <li>Monitor invoice status across all clients</li>
              <li>Track payment activity over time</li>
            </ul>
          </div>

          <div class="feat-group reveal" style="transition-delay:0.16s">
            <div class="feat-group__title">
              <div class="feat-group__title-icon">👥</div>
              Client Management
            </div>
            <ul class="feat-group__list">
              <li>Store client details for reuse</li>
              <li>Pull up client info when creating new invoices</li>
              <li>Keep work history organised by customer</li>
            </ul>
          </div>

        </div>
      </div>
    </section>

    <!-- ────────────────────── PAGE CTA ──────────────────────────── -->
    <section class="page-cta">
      <div class="container">
        <h2 class="page-cta__title reveal">Start using these features today</h2>
        <p class="page-cta__sub reveal" style="transition-delay:0.1s">Everything above is available now. No complex setup. Takes 2 minutes to get started.</p>
        <div class="page-cta__actions reveal" style="transition-delay:0.2s">
          <a href="https://app.captureninvoice.com/register" class="btn btn--primary">
            Get Started Free
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 7h8M7 3l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="https://app.captureninvoice.com/login" class="btn btn--ghost">Sign In</a>
        </div>
      </div>
    </section>

    [PASTE SHARED FOOTER HTML]

    [PASTE SHARED SCRIPT BLOCK (non-pricing)]

  </body>
  </html>
  ```

- [ ] **Step 2: Verify locally**

  Open `http://localhost:8000/features.html` — confirm 5 feature groups render in a 2-column grid, checkmarks are green, nav and footer work.

- [ ] **Step 3: Commit**

  ```bash
  git add features.html
  git commit -m "Add /features page"
  ```

---

## Task 5: Create `how-it-works.html`

**Files:**
- Create: `how-it-works.html`

- [ ] **Step 1: Create the file**

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>How It Works — CaptureNInvoice</title>
    <meta name="description" content="See how CaptureNInvoice works: document the job, send a proof-of-work invoice, and get paid faster in three simple steps.">
    <link rel="canonical" href="https://captureninvoice.com/how-it-works">
    <meta property="og:title" content="How It Works — CaptureNInvoice">
    <meta property="og:description" content="See how CaptureNInvoice works: document the job, send a proof-of-work invoice, and get paid faster in three simple steps.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://captureninvoice.com/how-it-works">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,700;12..96,800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
  </head>
  <body>

    [PASTE SHARED NAV HTML]

    <!-- ────────────────────── HERO ───────────────────────────────── -->
    <section class="page-hero">
      <div class="container">
        <div class="section-label reveal" style="margin:0 auto 20px">How It Works</div>
        <h1 class="page-hero__title reveal" style="transition-delay:0.1s">From completed work<br>to paid invoice</h1>
        <p class="page-hero__sub reveal" style="transition-delay:0.2s">Three steps. One workflow. Less friction.</p>
      </div>
    </section>

    <!-- ────────────────────── STEPS ─────────────────────────────── -->
    <section class="page-section">
      <div class="container">
        <div class="step-flow">

          <div class="step-item reveal">
            <div class="step-num">1</div>
            <div class="step-body">
              <div class="step-body__title">Document the Work</div>
              <div class="step-body__desc">Take photos, add notes, and record the completed job before you leave the site. Everything is attached to the invoice automatically.</div>
            </div>
          </div>

          <div class="step-item reveal" style="transition-delay:0.1s">
            <div class="step-num">2</div>
            <div class="step-body">
              <div class="step-body__title">Send the Invoice</div>
              <div class="step-body__desc">Create a professional invoice with your proof of work attached and send it to the client by shareable link — no app required on their end.</div>
            </div>
          </div>

          <div class="step-item reveal" style="transition-delay:0.2s">
            <div class="step-num">3</div>
            <div class="step-body">
              <div class="step-body__title">Get Paid Faster</div>
              <div class="step-body__desc">Clients review the work, pay online or by approved payment method, and you track payment status inside CaptureNInvoice.</div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ────────────────────── WHY THIS MATTERS ──────────────────── -->
    <section class="page-section">
      <div class="container">
        <div class="page-section__head">
          <div class="section-label reveal">Why It Matters</div>
          <h2 class="section-title reveal" style="transition-delay:0.1s">Why this workflow changes things</h2>
        </div>
        <div class="info-box reveal">
          <ul class="info-box__list checks">
            <li>Reduces billing disputes — clients can see exactly what was done</li>
            <li>Improves professionalism — every invoice looks polished and credible</li>
            <li>Speeds up payment collection — less back-and-forth before you get paid</li>
            <li>Keeps records in one place — photos, notes, and invoices together</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- ────────────────────── PAGE CTA ──────────────────────────── -->
    <section class="page-cta">
      <div class="container">
        <h2 class="page-cta__title reveal">Try the workflow yourself</h2>
        <p class="page-cta__sub reveal" style="transition-delay:0.1s">Create your account and send your first proof-of-work invoice in minutes.</p>
        <div class="page-cta__actions reveal" style="transition-delay:0.2s">
          <a href="https://app.captureninvoice.com/register" class="btn btn--primary">
            Get Started Free
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 7h8M7 3l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="https://app.captureninvoice.com/login" class="btn btn--ghost">Sign In</a>
        </div>
      </div>
    </section>

    [PASTE SHARED FOOTER HTML]

    [PASTE SHARED SCRIPT BLOCK (non-pricing)]

  </body>
  </html>
  ```

- [ ] **Step 2: Verify locally**

  Open `http://localhost:8000/how-it-works.html` — confirm 3 numbered steps render, orange step numbers, info box with arrow bullets, CTA works.

- [ ] **Step 3: Commit**

  ```bash
  git add how-it-works.html
  git commit -m "Add /how-it-works page"
  ```

---

## Task 6: Create `pricing.html`

**Files:**
- Create: `pricing.html`

- [ ] **Step 1: Create the file**

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pricing — CaptureNInvoice</title>
    <meta name="description" content="Simple, transparent pricing for service businesses. Start free or upgrade for more control and workflow tools.">
    <link rel="canonical" href="https://captureninvoice.com/pricing">
    <meta property="og:title" content="Pricing — CaptureNInvoice">
    <meta property="og:description" content="Simple, transparent pricing for service businesses. Start free or upgrade for more control and workflow tools.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://captureninvoice.com/pricing">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,700;12..96,800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
  </head>
  <body>

    [PASTE SHARED NAV HTML]

    <!-- ────────────────────── HERO ───────────────────────────────── -->
    <section class="page-hero">
      <div class="container">
        <div class="section-label reveal" style="margin:0 auto 20px">Pricing</div>
        <h1 class="page-hero__title reveal" style="transition-delay:0.1s">Simple, transparent pricing</h1>
        <p class="page-hero__sub reveal" style="transition-delay:0.2s">No hidden fees. No bloated tiers. Just the tools you need to invoice with proof.</p>
      </div>
    </section>

    <!-- ────────────────────── PLANS ─────────────────────────────── -->
    <section class="page-section">
      <div class="container">
        <div class="pricing__grid" style="max-width:700px; margin:0 auto">

          <div class="pricing-card reveal">
            <div class="pricing-card__badge">Basic</div>
            <div class="pricing-card__price">
              <span class="pricing-card__amount">$9</span>
              <span class="pricing-card__period">/ month</span>
            </div>
            <div class="pricing-card__desc">For solo operators who want proof-of-work invoicing and a clean way to send invoices.</div>
            <ul class="pricing-card__features">
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8l3.5 3.5L13 5" stroke="#16A34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Proof-of-work photo invoices
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8l3.5 3.5L13 5" stroke="#16A34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Online payment collection
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8l3.5 3.5L13 5" stroke="#16A34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Revenue dashboard
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8l3.5 3.5L13 5" stroke="#16A34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Client management
              </li>
            </ul>
            <a href="https://app.captureninvoice.com/register" class="btn btn--primary" style="width:100%; justify-content:center">Get Started</a>
          </div>

          <div class="pricing-card pricing-card--featured reveal" style="transition-delay:0.1s">
            <div class="pricing-card__badge">Pro</div>
            <div class="pricing-card__price">
              <span class="pricing-card__amount">$25</span>
              <span class="pricing-card__period">/ month</span>
            </div>
            <div class="pricing-card__desc">For growing service businesses that want more control, stronger workflow tools, and more advanced visibility.</div>
            <ul class="pricing-card__features">
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8l3.5 3.5L13 5" stroke="#16A34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Everything in Basic
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8l3.5 3.5L13 5" stroke="#FF5C1A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Advanced revenue reporting <span style="font-size:11px;color:var(--text-3);font-weight:600;text-transform:uppercase;letter-spacing:0.04em">coming soon</span>
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8l3.5 3.5L13 5" stroke="#FF5C1A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Priority support <span style="font-size:11px;color:var(--text-3);font-weight:600;text-transform:uppercase;letter-spacing:0.04em">coming soon</span>
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8l3.5 3.5L13 5" stroke="#FF5C1A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Team access <span style="font-size:11px;color:var(--text-3);font-weight:600;text-transform:uppercase;letter-spacing:0.04em">coming soon</span>
              </li>
            </ul>
            <a href="https://app.captureninvoice.com/register" class="btn btn--primary" style="width:100%; justify-content:center">Get Started</a>
          </div>

        </div>
      </div>
    </section>

    <!-- ────────────────────── FAQ ────────────────────────────────── -->
    <section class="faq" style="padding-top:0">
      <div class="container">
        <div class="faq__head">
          <div class="section-label reveal">FAQ</div>
          <h2 class="section-title reveal" style="transition-delay:0.1s">Common questions</h2>
        </div>
        <div class="faq__list">

          <div class="faq-item reveal">
            <button class="faq-item__q">
              Do my clients need an account to pay?
              <div class="faq-item__arrow">▼</div>
            </button>
            <div class="faq-item__a">
              <div class="faq-item__a-inner">No. Clients receive a payment link and can pay directly — no account, no sign-up, no friction. They open the link, see your work, and pay.</div>
            </div>
          </div>

          <div class="faq-item reveal" style="transition-delay:0.05s">
            <button class="faq-item__q">
              Can I attach proof of work to invoices?
              <div class="faq-item__arrow">▼</div>
            </button>
            <div class="faq-item__a">
              <div class="faq-item__a-inner">Yes — that's the core of CaptureNInvoice. You can attach before/after photos, work logs, and job notes directly to each invoice. Clients see your proof when they open the payment link.</div>
            </div>
          </div>

          <div class="faq-item reveal" style="transition-delay:0.1s">
            <button class="faq-item__q">
              Is CaptureNInvoice good for small service businesses?
              <div class="faq-item__arrow">▼</div>
            </button>
            <div class="faq-item__a">
              <div class="faq-item__a-inner">Yes. It's designed specifically for solo operators and small teams in the trades — cleaners, landscapers, painters, handymen, and similar businesses.</div>
            </div>
          </div>

          <div class="faq-item reveal" style="transition-delay:0.15s">
            <button class="faq-item__q">
              Can I use Stripe or manual payment methods?
              <div class="faq-item__arrow">▼</div>
            </button>
            <div class="faq-item__a">
              <div class="faq-item__a-inner">Yes. CaptureNInvoice supports online payment collection via Stripe as well as manual payment workflows for clients who prefer to pay by other means.</div>
            </div>
          </div>

          <div class="faq-item reveal" style="transition-delay:0.2s">
            <button class="faq-item__q">
              Can I track paid and unpaid invoices?
              <div class="faq-item__arrow">▼</div>
            </button>
            <div class="faq-item__a">
              <div class="faq-item__a-inner">Yes. The revenue dashboard shows paid invoices, outstanding amounts, and your total earnings — so you always know where you stand.</div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ────────────────────── PAGE CTA ──────────────────────────── -->
    <section class="page-cta">
      <div class="container">
        <h2 class="page-cta__title reveal">Start with Basic today</h2>
        <p class="page-cta__sub reveal" style="transition-delay:0.1s">No credit card required. Takes 2 minutes to set up.</p>
        <div class="page-cta__actions reveal" style="transition-delay:0.2s">
          <a href="https://app.captureninvoice.com/register" class="btn btn--primary">
            Get Started Free
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 7h8M7 3l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="https://app.captureninvoice.com/login" class="btn btn--ghost">Sign In</a>
        </div>
      </div>
    </section>

    [PASTE SHARED FOOTER HTML]

    [PASTE SHARED SCRIPT BLOCK (pricing version — includes FAQ accordion)]

  </body>
  </html>
  ```

- [ ] **Step 2: Verify locally**

  Open `http://localhost:8000/pricing.html` — confirm 2 plan cards render side by side, "coming soon" labels are visible, FAQ accordion opens/closes, CTA works.

- [ ] **Step 3: Commit**

  ```bash
  git add pricing.html
  git commit -m "Add /pricing page"
  ```

---

## Task 7: Create `about.html`

**Files:**
- Create: `about.html`

- [ ] **Step 1: Create the file**

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About — CaptureNInvoice</title>
    <meta name="description" content="CaptureNInvoice was built for service professionals who complete real work on-site and need a better way to document it, invoice for it, and get paid faster.">
    <link rel="canonical" href="https://captureninvoice.com/about">
    <meta property="og:title" content="About — CaptureNInvoice">
    <meta property="og:description" content="CaptureNInvoice was built for service professionals who complete real work on-site and need a better way to document it, invoice for it, and get paid faster.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://captureninvoice.com/about">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,700;12..96,800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
  </head>
  <body>

    [PASTE SHARED NAV HTML]

    <!-- ────────────────────── HERO ───────────────────────────────── -->
    <section class="page-hero">
      <div class="container">
        <div class="section-label reveal" style="margin:0 auto 20px">About</div>
        <h1 class="page-hero__title reveal" style="transition-delay:0.1s">Built for service businesses that need proof, professionalism, and faster payment</h1>
        <p class="page-hero__sub reveal" style="transition-delay:0.2s">CaptureNInvoice was created for service professionals who complete real work on-site and need a better way to document it, invoice for it, and get paid with less friction. We built it because generic invoicing tools were never designed for the field.</p>
      </div>
    </section>

    <!-- ────────────────────── AUDIENCE ──────────────────────────── -->
    <section class="page-section">
      <div class="container">
        <div class="page-section__head">
          <div class="section-label reveal">Who It's For</div>
          <h2 class="section-title reveal" style="transition-delay:0.1s">Built for the people who do the work</h2>
        </div>
        <div class="audience-grid">
          <div class="audience-card reveal">
            <div class="audience-card__icon">🧹</div>
            <div class="audience-card__name">Cleaners</div>
          </div>
          <div class="audience-card reveal" style="transition-delay:0.05s">
            <div class="audience-card__icon">🌿</div>
            <div class="audience-card__name">Landscapers</div>
          </div>
          <div class="audience-card reveal" style="transition-delay:0.1s">
            <div class="audience-card__icon">🎨</div>
            <div class="audience-card__name">Painters</div>
          </div>
          <div class="audience-card reveal" style="transition-delay:0.05s">
            <div class="audience-card__icon">🔧</div>
            <div class="audience-card__name">Handymen</div>
          </div>
          <div class="audience-card reveal" style="transition-delay:0.1s">
            <div class="audience-card__icon">🏠</div>
            <div class="audience-card__name">Maintenance Pros</div>
          </div>
          <div class="audience-card reveal" style="transition-delay:0.15s">
            <div class="audience-card__icon">🏗️</div>
            <div class="audience-card__name">Field Service Businesses</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ────────────────────── WHY GENERIC TOOLS FALL SHORT ──────── -->
    <section class="page-section">
      <div class="container">
        <div class="page-section__head">
          <div class="section-label reveal">The Problem</div>
          <h2 class="section-title reveal" style="transition-delay:0.1s">Why generic invoicing tools fall short</h2>
        </div>
        <div class="info-box reveal">
          <ul class="info-box__list crosses">
            <li>They let you invoice the work — but they don't prove the work was done</li>
            <li>No photo documentation attached to invoices</li>
            <li>No on-site job records</li>
            <li>No protection when clients dispute what was completed</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- ────────────────────── CLOSING ───────────────────────────── -->
    <section class="page-section">
      <div class="container">
        <div style="max-width:640px; margin:0 auto; text-align:center;">
          <p class="section-sub reveal" style="font-size:20px; color:var(--text);">CaptureNInvoice connects documentation, invoicing, and payment into one workflow designed for job-based businesses.</p>
        </div>
      </div>
    </section>

    <!-- ────────────────────── PAGE CTA ──────────────────────────── -->
    <section class="page-cta">
      <div class="container">
        <h2 class="page-cta__title reveal">Start documenting your work today</h2>
        <p class="page-cta__sub reveal" style="transition-delay:0.1s">Create your account free. No credit card required.</p>
        <div class="page-cta__actions reveal" style="transition-delay:0.2s">
          <a href="https://app.captureninvoice.com/register" class="btn btn--primary">
            Get Started Free
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 7h8M7 3l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="https://app.captureninvoice.com/login" class="btn btn--ghost">Sign In</a>
        </div>
      </div>
    </section>

    [PASTE SHARED FOOTER HTML]

    [PASTE SHARED SCRIPT BLOCK (non-pricing)]

  </body>
  </html>
  ```

- [ ] **Step 2: Verify locally**

  Open `http://localhost:8000/about.html` — confirm audience grid renders 6 cards in 3 columns, shortfall list shows red ✕ marks, closing paragraph is centered, CTA works.

- [ ] **Step 3: Commit**

  ```bash
  git add about.html
  git commit -m "Add /about page"
  ```

---

## Task 8: Update `sitemap.xml`

**Files:**
- Modify: `sitemap.xml`

- [ ] **Step 1: Replace sitemap.xml with all 6 URLs**

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

  Note: namespace uses `http://` (not `https://`) — this is the sitemaps.org standard.

- [ ] **Step 2: Commit**

  ```bash
  git add sitemap.xml
  git commit -m "Update sitemap.xml with all 6 public pages"
  ```

---

## Task 9: Final verification and push

- [ ] **Step 1: Full navigation smoke test**

  Start the server: `python server.py`

  Test every link:
  - Homepage (`/`) loads correctly
  - Nav: Product → `product.html` ✓
  - Nav: Features → `features.html` ✓
  - Nav: How It Works → `how-it-works.html` ✓
  - Nav: Pricing → `pricing.html` ✓
  - Nav: About → `about.html` ✓
  - Logo on each page → back to `/` ✓
  - Sign In → `https://app.captureninvoice.com/login` ✓
  - Get Started → `https://app.captureninvoice.com/register` ✓
  - Footer Product column links → correct pages ✓
  - Footer Company → `about.html` ✓
  - Mobile hamburger opens/closes on each page ✓
  - FAQ accordion works on `index.html` and `pricing.html` ✓
  - Scroll reveals animate on all pages ✓

- [ ] **Step 2: Push to remote**

  ```bash
  git push origin main
  ```
