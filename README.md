# CaptureNInvoice - Validation Landing Page

A validation landing page for CaptureNInvoice, an invoicing tool that lets service professionals attach before/after photos to invoices.

## How to Run Locally

### Option 1: Using server.py (Recommended)

```bash
cd "/Users/calebchukwu/Desktop/My Apps Projects/captureninvoice"
python server.py
```

### Option 2: Python one-liner

```bash
python -m http.server 8000
```

Then open your browser to: **http://localhost:8000**

To stop the server, press `Ctrl+C`.

## Viewing Signups

During validation, signups are stored in browser localStorage.

Open the browser console (F12 or Cmd+Shift+J) and run:

```javascript
// View all signups
JSON.parse(localStorage.getItem('captureninvoice_signups'))

// View signup count
localStorage.getItem('captureninvoice_counter')
```

## Project Structure

```
captureninvoice/
├── index.html       # Main landing page (HTML + CSS + JS)
├── server.py        # Local development server
├── README.md        # This file
├── css/             # (reserved for separated styles)
├── js/              # (reserved for separated scripts)
└── assets/images/   # (reserved for images/logos)
```

## Next Steps

1. **Connect email capture** - Replace localStorage with Mailchimp, ConvertKit, or Google Sheets
2. **Add analytics** - Google Analytics or Plausible for visitor tracking
3. **Deploy** - Push to Netlify, Vercel, or GitHub Pages for public access
4. **Run ads** - Facebook/Instagram ads targeting service professionals
5. **A/B test** - Try different headlines and CTAs to optimize conversion

## Success Metrics

- Target conversion rate: 10%+
- Track which business types convert best (from the dropdown)
- Goal: 100+ signups in the first week
