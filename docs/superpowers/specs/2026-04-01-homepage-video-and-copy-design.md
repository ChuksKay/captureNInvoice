# Homepage: Video + Copy Update Design

**Date:** 2026-04-01  
**Scope:** `index.html`, `css/styles.css`

---

## Overview

Three changes to the CaptureNInvoice homepage:

1. Add a video section (local `.mp4` file from `assets/`)
2. Replace all "before/after photo" language with "proof" language
3. Improve headline, subheadline, and CTA copy for conversion

---

## Task 1 — Video Section

**Placement:** Between the Stats section and the "How It Works" section.

**Rationale:** At this point in the page, the visitor has read the headline and seen credibility stats. They're primed to ask "what does this actually look like?" — the video answers that before the product walkthrough begins.

**Implementation:**
- New `<section class="demo-video">` inserted between `<!-- STATS -->` and `<!-- HOW IT WORKS -->`
- Section label: "See It In Action"
- `<video>` tag with `controls`, `preload="metadata"`, `width="100%"`
- `poster` attribute set to first-frame thumbnail (or omitted — browser handles it)
- Source: `assets/<filename>.mp4`
- Responsive styles in `styles.css`: `max-width: 900px`, centered, `border-radius`, subtle `box-shadow`
- No autoplay, no mute trick — user-initiated play only

---

## Task 2 — Recording / Analytics Status

**Status: No session recording tool installed.**

Only GA4 (`G-6WRXJRYEW0`) is present — aggregate analytics only, no session replays or heatmaps.

**Recommended addition (not in scope for this implementation):** Microsoft Clarity — free, one-line install, records sessions + heatmaps.

---

## Task 3 — Copy Changes

All changes are in `index.html` only.

### Hero
| Element | Before | After |
|---|---|---|
| Headline | "Proof-of-Work Invoicing for Service Businesses" | "Invoice with proof. Get paid faster." |
| Subheadline | "Document completed work, send professional invoices, get paid faster, and track revenue — all in one place built for the trades." | "Document every job, send invoices backed by proof, and collect payment — all from your phone." |
| Primary CTA | "Get Started Free" | "Start Invoicing Free" |

### How It Works — Step 01
| Element | Before | After |
|---|---|---|
| Description | "Capture before and after photos, log job notes, and record completed tasks directly on-site. Build undeniable proof as you work." | "Log the job on-site — notes, photos, and completed tasks. Build a clear record of what was done before you leave." |

### Why Section — Benefit 1
| Element | Before | After |
|---|---|---|
| Body | "Photos and documentation attached automatically — clients see exactly what was done." | "Proof of work on every invoice — clients see exactly what was done before they pay." |

### Features — Proof-of-Work Card
| Element | Before | After |
|---|---|---|
| Description | "Attach before/after photos and job documentation directly to invoices. Let your work speak for itself and eliminate payment disputes." | "Attach job documentation and proof directly to every invoice. Let your work speak for itself and eliminate payment disputes." |

### Who It's For — Cleaners
| Element | Before | After |
|---|---|---|
| Description | "Show before/after photos and charge confidently for deep cleans" | "Show documented proof of work and charge confidently for every clean" |

### Who It's For — Painters
| Element | Before | After |
|---|---|---|
| Description | "Attach prep photos and finished shots — prove the full scope of work" | "Attach job documentation and prove the full scope of work" |

### Final CTA
| Element | Before | After |
|---|---|---|
| Subtext | "Document your work, invoice clients professionally, and get paid faster — all in one place built for the trades." | "Invoice with proof, get paid faster, and run your business with confidence — all in one place built for the trades." |

---

## Files Changed

- `index.html` — copy changes + new video section HTML
- `css/styles.css` — new `.demo-video` section styles

## Files NOT Changed

- All other pages (copy changes are homepage-only)
- `sitemap.xml`, `robots.txt` (no new pages added)
