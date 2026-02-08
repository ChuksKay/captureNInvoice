---
name: captureninvoice-validation-site
description: Build and run a validation landing page for InvoiceKit (CaptureNInvoice) - an invoicing app for service professionals. This skill guides setting up a local development server, building the HTML/CSS/JS validation page, and preparing for email capture integration.
---

# CaptureNInvoice Validation Landing Page Skill

## Project Overview
Building a validation landing page for InvoiceKit - an invoicing tool that lets service professionals (cleaners, detailers, handymen, etc.) attach before/after photos to invoices, eliminating customer follow-ups and speeding up payment.

**Key Value Proposition:** Stop the "did you finish?" texts. Show your work, get paid faster.

**Target Audience:** Service professionals (cleaning services, pressure washers, car detailers, handymen, contractors, tutors)

**Project Location:** `/desktop/my apps projects/captureninvoice` (on user's local machine when using Claude Code)

## Project Structure

```
captureninvoice/
├── index.html              # Main validation landing page
├── css/
│   └── styles.css         # Separated styles (optional, can be inline)
├── js/
│   └── app.js             # Form handling and interactions
├── assets/
│   └── images/            # Any images/logos needed
├── README.md              # Project documentation
└── server.py              # Simple Python HTTP server for local testing
```

## Tech Stack for Validation Page

- **Frontend:** Pure HTML, CSS, JavaScript (no frameworks needed for validation)
- **Local Server:** Python's built-in HTTP server or Node's http-server
- **Future Integration:** Mailchimp, ConvertKit, Google Sheets, or Airtable for email capture

## Development Workflow

### Step 1: Initial Setup
1. Create project structure with all necessary folders
2. Set up a simple local server (Python or Node)
3. Create README with setup instructions

### Step 2: Build the Landing Page
1. Create the HTML structure based on the validation page design
2. Implement responsive CSS styling
3. Add JavaScript for:
   - Form validation
   - Success message display
   - Signup counter (localStorage)
   - Optional: subtle animations

### Step 3: Form Handling
For validation phase, use localStorage to store signups locally. Include comments showing how to integrate with:
- Mailchimp API
- ConvertKit API
- Google Sheets (via Apps Script)
- Airtable API
- Custom backend endpoint

### Step 4: Testing & Refinement
1. Test on different screen sizes
2. Verify form validation works
3. Test success states
4. Check browser compatibility

## Key Features to Implement

### 1. Email Capture Form
- Email input (required)
- Business type dropdown (required) - tracks which segment converts
- Name input (optional)
- Clear CTA button
- Privacy note

### 2. Social Proof Elements
- Dynamic signup counter (starts at 52, increments)
- "Coming Soon" badge
- Trust indicators

### 3. Value Proposition Sections
- Problem statement (the "did you finish?" texts)
- Solution highlight (photos in invoices)
- Feature list with icons
- Visual hierarchy guiding to signup

### 4. Responsive Design
- Mobile-first approach
- Works on tablets and desktop
- Touch-friendly buttons
- Readable typography at all sizes

## Design Principles

### Color Scheme
- Primary: #FF6B35 (Orange - energetic, action-oriented)
- Secondary: #004E89 (Blue - trustworthy, professional)
- Accent: #FFD23F (Yellow - highlighting)
- Dark: #1A1A2E
- Light: #F7F9FB

### Typography
- Headings: 'Bricolage Grotesque' (bold, distinctive)
- Body: 'DM Sans' (clean, readable)
- Load from Google Fonts

### Layout
- Single-column, centered layout
- Generous white space
- Clear visual hierarchy
- Prominent CTA

## Server Setup Instructions

### Option 1: Python (Recommended)
```python
# server.py
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.js': 'application/javascript',
})

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()
```

Run with: `python server.py`

### Option 2: Node.js
```bash
npm install -g http-server
http-server -p 8000
```

### Option 3: Python One-liner
```bash
python -m http.server 8000
```

## Email Integration (Future)

### Mailchimp Integration Template
```javascript
fetch('https://YOUR_DOMAIN.us1.list-manage.com/subscribe/post-json?u=XXX&id=XXX', {
  method: 'POST',
  mode: 'no-cors',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    EMAIL: email,
    FNAME: name,
    BUSINESS: businessType
  })
});
```

### Google Sheets Integration (via Apps Script)
1. Create Google Sheet
2. Create Apps Script webhook
3. POST signup data to webhook URL

## Validation Metrics to Track

**Success Indicators:**
- 10%+ conversion rate (visitors → signups)
- 100+ signups in first week
- Clear segment leader (which business type converts best)

**Data to Capture:**
- Email address
- Business type (dropdown selection)
- Name (optional)
- Timestamp
- Source (if running multiple ad variants)

## Code Quality Standards

1. **Clean, readable code** - other developers should understand it
2. **Comments** - explain why, not what
3. **Responsive** - mobile-first CSS
4. **Accessible** - proper labels, semantic HTML
5. **Performance** - minimize external dependencies

## Files to Create

### 1. index.html
Complete validation landing page with:
- Semantic HTML5 structure
- Meta tags for social sharing
- Embedded or linked CSS
- Form with proper validation

### 2. README.md
Should include:
- Project description
- Setup instructions
- How to run locally
- How to deploy
- Future integration steps

### 3. server.py (or server setup)
Simple local development server

### 4. .gitignore (optional)
If pushing to GitHub:
```
node_modules/
.DS_Store
*.log
```

## Deployment Options (Post-Validation)

When ready to go live:
1. **Netlify** - Drag & drop, instant deploy, free
2. **Vercel** - Similar to Netlify
3. **GitHub Pages** - Free hosting from repo
4. **Carrd.co** - No-code landing page builder

## Next Steps After Validation

If validation succeeds (10%+ conversion, 100+ signups):
1. Set up proper email service (Mailchimp/ConvertKit)
2. Add analytics (Google Analytics or Plausible)
3. Create Facebook ad campaigns
4. A/B test different headlines
5. Build the actual app

If validation fails (<5% conversion):
1. Review messaging - does it resonate?
2. Test different target audiences
3. Adjust value proposition
4. Consider interviewing signups to understand hesitation

## Important Notes

- Keep it SIMPLE - this is validation, not production
- Focus on collecting emails and business types
- Use localStorage for demo - real integration comes later
- Make it easy to update headline/copy for A/B testing
- Ensure fast loading - single page, minimal assets

## Common Issues & Solutions

**Issue:** Form submits but nothing happens
**Solution:** Check browser console, ensure preventDefault() is called

**Issue:** Styles not loading
**Solution:** Check file paths, ensure server is serving CSS files correctly

**Issue:** Counter not incrementing
**Solution:** Check localStorage permissions in browser

**Issue:** Mobile layout broken
**Solution:** Add viewport meta tag, test responsive CSS breakpoints
