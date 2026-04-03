# Homepage Video + Copy Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a local video section between Stats and How It Works, and update all homepage copy to remove before/after photo language and sharpen the headline/sub/CTA.

**Architecture:** Pure static HTML/CSS edits to `index.html` and `css/styles.css`. No JavaScript needed. Video served via `<video>` tag pointing to `assets/VIDEO-2026-03-29-16-46-55.mov`. No new pages, no new dependencies.

**Tech Stack:** HTML5, CSS3, static file serving via `python server.py`

---

## Files

- Modify: `index.html` — video section HTML + all copy changes
- Modify: `css/styles.css` — new `.demo-video` section styles

---

### Task 1: Add video section styles to styles.css

**Files:**
- Modify: `css/styles.css`

- [ ] **Step 1: Open the local dev server to verify baseline**

```bash
cd "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice"
python server.py
```
Open http://localhost:8000 — confirm homepage loads correctly before making any changes. Stop server with Ctrl+C when done.

- [ ] **Step 2: Add `.demo-video` styles to styles.css**

Open `css/styles.css` and append the following block at the end of the file:

```css
/* ─── DEMO VIDEO ─────────────────────────────────────────── */
.demo-video {
  padding: 80px 0;
  background: var(--surface);
}

.demo-video__head {
  text-align: center;
  margin-bottom: 40px;
}

.demo-video__wrap {
  max-width: 900px;
  margin: 0 auto;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 40px rgba(0,0,0,0.18);
}

.demo-video__wrap video {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 16px;
}

@media (max-width: 768px) {
  .demo-video {
    padding: 48px 0;
  }

  .demo-video__wrap {
    border-radius: 10px;
  }

  .demo-video__wrap video {
    border-radius: 10px;
  }
}
```

- [ ] **Step 3: Verify styles load without errors**

Run `python server.py`, open http://localhost:8000, open browser DevTools → Console. Confirm no CSS errors. Stop server.

- [ ] **Step 4: Commit**

```bash
git add css/styles.css
git commit -m "feat: add demo-video section styles"
```

---

### Task 2: Add video section HTML to index.html

**Files:**
- Modify: `index.html`

The video section goes between the closing `</section>` of Stats and the opening `<section class="how"` of How It Works. In the current file this is around line 324–327.

- [ ] **Step 1: Insert the video section HTML**

Find this exact comment line in `index.html`:

```html
  <!-- ────────────────────── HOW IT WORKS ───────────────────────── -->
```

Insert the following block immediately before it:

```html
  <!-- ────────────────────── DEMO VIDEO ────────────────────────── -->
  <section class="demo-video">
    <div class="container">
      <div class="demo-video__head">
        <div class="section-label reveal">See It In Action</div>
        <h2 class="section-title reveal" style="transition-delay:0.1s">Watch how it works</h2>
      </div>
      <div class="demo-video__wrap reveal" style="transition-delay:0.2s">
        <video
          controls
          preload="metadata"
          width="100%"
          aria-label="CaptureNInvoice product demo"
        >
          <source src="assets/VIDEO-2026-03-29-16-46-55.mov" type="video/mp4">
          Your browser does not support the video tag.
        </video>
      </div>
    </div>
  </section>

```

- [ ] **Step 2: Verify video appears in browser**

Run `python server.py`, open http://localhost:8000. Scroll to the section between Stats and How It Works. Confirm:
- Section label "See It In Action" is visible
- Video player renders with controls
- Video plays when clicked
- No layout breakage above or below

Check on mobile width by resizing browser to under 768px — video should stay full-width and not overflow.

Stop server.

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add demo video section between stats and how-it-works"
```

---

### Task 3: Update hero copy

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Update hero headline**

Find:
```html
          <h1 class="hero__title reveal">
            Proof-of-Work<br>Invoicing for<br>
            <span>Service Businesses</span>
          </h1>
```

Replace with:
```html
          <h1 class="hero__title reveal">
            Invoice with proof.<br>
            <span>Get paid faster.</span>
          </h1>
```

- [ ] **Step 2: Update hero subheadline**

Find:
```html
          <p class="hero__sub reveal" style="transition-delay:0.1s">
            Document completed work, send professional invoices, get paid faster, and track revenue — all in one place built for the trades.
          </p>
```

Replace with:
```html
          <p class="hero__sub reveal" style="transition-delay:0.1s">
            Document every job, send invoices backed by proof, and collect payment — all from your phone.
          </p>
```

- [ ] **Step 3: Update primary CTA button**

Find:
```html
              Get Started Free
```
(inside the `<a href="https://app.captureninvoice.com/register" class="btn btn--primary">` in the hero actions div)

Replace with:
```html
              Start Invoicing Free
```

- [ ] **Step 4: Verify hero in browser**

Run `python server.py`, open http://localhost:8000. Confirm:
- Headline reads "Invoice with proof. Get paid faster."
- Subheadline is updated
- Primary CTA reads "Start Invoicing Free"
- Hero layout is unchanged on desktop and mobile

Stop server.

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: update hero headline, sub, and CTA copy"
```

---

### Task 4: Update How It Works, Why section, and Features copy

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Update How It Works — Step 01 description**

Find:
```html
          <p class="step-card__desc">Capture before and after photos, log job notes, and record completed tasks directly on-site. Build undeniable proof as you work.</p>
```

Replace with:
```html
          <p class="step-card__desc">Log the job on-site — notes, photos, and completed tasks. Build a clear record of what was done before you leave.</p>
```

- [ ] **Step 2: Update Why section — Benefit 1 body text**

Find:
```html
                Photos and documentation attached automatically — clients see exactly what was done.
```

Replace with:
```html
                Proof of work on every invoice — clients see exactly what was done before they pay.
```

- [ ] **Step 3: Update Features — Proof-of-Work Invoicing card description**

Find:
```html
          <p class="feat-card__desc">Attach before/after photos and job documentation directly to invoices. Let your work speak for itself and eliminate payment disputes.</p>
```

Replace with:
```html
          <p class="feat-card__desc">Attach job documentation and proof directly to every invoice. Let your work speak for itself and eliminate payment disputes.</p>
```

- [ ] **Step 4: Verify in browser**

Run `python server.py`, open http://localhost:8000. Scroll through:
- How It Works Step 01 — updated text visible
- Why section benefit 1 — updated text visible
- Features card — updated text visible

Stop server.

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: remove before/after photo language from how-it-works, why, and features sections"
```

---

### Task 5: Update Who It's For and Final CTA copy

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Update Who It's For — Cleaners card**

Find:
```html
            <div class="who-card__desc">Show before/after photos and charge confidently for deep cleans</div>
```

Replace with:
```html
            <div class="who-card__desc">Show documented proof of work and charge confidently for every clean</div>
```

- [ ] **Step 2: Update Who It's For — Painters card**

Find:
```html
            <div class="who-card__desc">Attach prep photos and finished shots — prove the full scope of work</div>
```

Replace with:
```html
            <div class="who-card__desc">Attach job documentation and prove the full scope of work</div>
```

- [ ] **Step 3: Update Final CTA subtext**

Find:
```html
        <p class="final-cta__sub reveal" style="transition-delay:0.2s">Document your work, invoice clients professionally, and get paid faster — all in one place built for the trades.</p>
```

Replace with:
```html
        <p class="final-cta__sub reveal" style="transition-delay:0.2s">Invoice with proof, get paid faster, and run your business with confidence — all in one place built for the trades.</p>
```

- [ ] **Step 4: Final full-page verification**

Run `python server.py`, open http://localhost:8000. Do a complete scroll from top to bottom and confirm:
- No remaining instances of "before/after" or "before and after" anywhere on the page (use browser Cmd+F to search)
- All updated sections read correctly
- No layout broken on desktop
- Resize to mobile (< 768px) — all sections still look correct
- Video plays correctly

Stop server.

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: update who-its-for and final CTA copy, complete proof language refactor"
```
