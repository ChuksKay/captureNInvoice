# CaptureNInvoice Validation Landing Page - Claude Code Instructions

## Project Goal
Build a validation landing page for InvoiceKit locally at `/desktop/my apps projects/captureninvoice` to test market interest before building the full app.

## Quick Start for Claude Code

When the user says "start building" or "let's begin", follow these steps:

### Step 1: Verify Project Location
```bash
# Check if directory exists
ls "/desktop/my apps projects/captureninvoice" 2>/dev/null || echo "Directory not found"
```

If directory doesn't exist:
```bash
mkdir -p "/desktop/my apps projects/captureninvoice"
cd "/desktop/my apps projects/captureninvoice"
```

### Step 2: Create Project Structure
```bash
mkdir -p css js assets/images
```

### Step 3: Create Files in Order

**Priority order:**
1. `index.html` - Main landing page
2. `server.py` - Local development server
3. `README.md` - Setup instructions
4. `css/styles.css` - Separated styles (optional)
5. `js/app.js` - Form handling (optional)

### Step 4: Start the Local Server
```bash
cd "/desktop/my apps projects/captureninvoice"
python server.py
```

Or if Python not available:
```bash
python -m http.server 8000
```

User can then visit: `http://localhost:8000`

## What to Build

### index.html - Complete Validation Page
Create a single HTML file with:

**Structure:**
- Header with logo
- Hero section with main headline
- Problem statement box
- Value proposition highlight
- Features list (6 features with icons)
- Email signup form
- Social proof (signup counter)
- Footer (minimal)

**Key Elements:**
- Embedded CSS (or link to styles.css)
- Embedded JavaScript for form handling
- Responsive design (mobile-first)
- Google Fonts (Bricolage Grotesque + DM Sans)

**Form Fields:**
- Email (required)
- Business type dropdown (required) - tracks segments
- Name (optional)
- Submit button
- Privacy note

**Form Behavior:**
- Validate inputs
- Store in localStorage (demo mode)
- Show success message
- Hide form after submit
- Increment signup counter

### server.py - Simple HTTP Server
```python
import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"✓ Server running at http://localhost:{PORT}")
    print(f"✓ Press Ctrl+C to stop")
    httpd.serve_forever()
```

### README.md - Setup Instructions
Include:
- Project description
- How to run locally
- How to view signups (localStorage)
- Next steps for email integration

## Design Specifications

**Colors:**
- Primary: #FF6B35 (orange)
- Secondary: #004E89 (blue)
- Accent: #FFD23F (yellow)
- Background gradient: Linear gradient from #004E89 to #002B4F

**Typography:**
- Headings: Bricolage Grotesque (800 weight)
- Body: DM Sans (400, 500, 700)
- Load from: Google Fonts CDN

**Layout:**
- Max width: 700px
- Centered card design
- White card on blue gradient background
- Rounded corners (24px)
- Generous padding (50-60px)

**Responsive Breakpoints:**
- Mobile: < 768px
- Tablet/Desktop: > 768px

## Features to Include

1. **Problem Box** - Red/orange background, showing customer follow-up text problem
2. **Value Prop Box** - Green background, showing the solution
3. **6 Feature Items** - Icon + title + description
4. **Signup Form** - 3 fields, prominent CTA button
5. **Social Proof** - Dynamic counter starting at 52
6. **Success State** - Green message after form submit

## Testing Checklist

Before marking complete:
- [ ] Server starts without errors
- [ ] Page loads at localhost:8000
- [ ] Form validates required fields
- [ ] Form submits successfully
- [ ] Success message displays
- [ ] Counter increments
- [ ] Responsive on mobile (< 768px)
- [ ] All fonts load correctly
- [ ] Colors match specification

## Commands for User

After building, tell user:

```bash
# Navigate to project
cd "/desktop/my apps projects/captureninvoice"

# Start server
python server.py

# Open browser to:
http://localhost:8000

# View signups (browser console):
localStorage.getItem('signups')

# Stop server:
Ctrl+C
```

## Troubleshooting

**Server won't start:**
- Try: `python3 server.py`
- Or: `python -m http.server 8000`

**Page won't load:**
- Check if port 8000 is already in use
- Try different port: `python -m http.server 3000`

**Styles not showing:**
- If using external CSS, check file path
- Consider embedding CSS in HTML for simplicity

## Future Integration Notes

Add comments in JavaScript showing how to integrate:
- Mailchimp API
- Google Sheets webhook
- Airtable API
- Custom backend endpoint

## Success Metrics

Tell user to track:
- Visitors (use analytics later)
- Signups (localStorage for now)
- Conversion rate target: 10%+
- Business type breakdown (which segment converts best)

## What NOT to Build Yet

Don't build these during validation:
- Backend server/database
- Payment processing
- User authentication
- The actual invoice app
- Complex animations
- Multiple pages

Keep it simple. One page. Email capture. That's it.
