# SCAM SHIELD with SCAMSAVER (v6.3 Standardized Release)

Professional, senior-friendly threat defense and fraud verification web application powered by **Gemini AI Threat Intelligence**.

---

## Live Public Web Application
- **Production Tunnel URL:** [https://reservation-hometown-wilson-immunology.trycloudflare.com](https://reservation-hometown-wilson-immunology.trycloudflare.com)
- **Status:** Active & Responsive

---

## Repository & Project Architecture

All files follow standard Web, Python, and Git naming conventions and proper suffixes for clean deployment across GitHub and Vercel:

```text
scamsafe prototype v1/
├── index.html                   # Canonical Frontend Application (HTML5)
├── vercel.json                  # Vercel Serverless Routing Specification (JSON)
├── requirements.txt             # Pinned Serverless Python Dependencies (TXT)
├── .gitignore                   # Standard Git Ignore Specification
├── README.md                    # Project Architecture & Deployment Guide (Markdown)
├── api/
│   └── index.py                 # FastAPI Serverless Threat Engine (Python)
├── css/
│   └── style.css                # Standard Stylesheet (EB Garamond & Calibri, Pale Pink Light / Dark)
├── js/
│   ├── app.js                   # Client Application Engine (ES6+ Multimodal & Screen Capture)
│   └── mock_scams.js            # Known Threat Signatures & Database
├── public/                      # Static Mirror for Hosting Environments
│   ├── index.html
│   ├── css/style.css
│   └── js/
├── static/                      # Static Mirror for Framework Fallbacks
│   ├── index.html
│   ├── css/style.css
│   └── js/
├── .github/
│   └── workflows/
│       └── deploy.yml           # GitHub Actions CI Verification Pipeline (YAML)
├── server.py                    # Standalone Local Python Web Server (Python)
├── start_live.py                # Local Server & Resilient Cloudflare Tunnel Launcher (Python)
├── run.bat                      # Windows 1-Click Local Server Launcher (Batch)
├── start_live_demo.bat          # Windows 1-Click Live Public Demo Launcher (Batch)
├── auto_update_git.py           # Automated Git & Vercel Push Engine (Dulwich)
└── auto_update_github.bat       # Windows 1-Click GitHub & Vercel Auto-Deployment Launcher (Batch)
```

---

## Key Features & UI Specifications

1. **Default Dark Mode:**
   - Dark theme is enabled by default upon first visit (`theme-dark`).
   - Deep charcoal background (`#232722`) with warm alabaster text (`#FAFAF7`) for comfortable, eye-soothing night contrast.
   - Smooth 1-click toggle to Light Mode (pale pink background `#F6EAE7` with crisp `#FFFFFF` cards for Sectors 1 & 2).

2. **Default Language is English:**
   - The application defaults strictly to English (`"en"`).

3. **Searchable World Language Selector with Instant Re-Open:**
   - Real-time search bar to filter 30+ world languages (e.g., Hindi, Spanish, French, Mandarin, Arabic, Tamil, Telugu, etc.).
   - Clean toggle state: selecting a language updates the UI and results seamlessly, and the button can be re-opened at any time without locking up.

4. **Universal Full-Page Translation & Multilingual Forensic Results:**
   - Translates 100% of the webpage elements, inputs, and dialogs.
   - Safety reports generated in Sector 2 are automatically localized into the user's chosen language.

5. **Gemini AI Threat Intelligence & Live Screen Share:**
   - Multi-modal scam detection (Screen Share, URLs, Images, Documents, Audios, Messages).
   - Pure non-binding advisory recommendation tone.
   - Persistent SCAMSAVER AI companion in the left taskbar.
   - Zero emojis anywhere across the interface.

---

## How to Deploy to GitHub & Vercel

### Option 1: 1-Click Automated Batch Launcher
Run the following command in PowerShell or Command Prompt:
```powershell
.\auto_update_github.bat https://github.com/YOUR_USERNAME/YOUR_REPO.git
```
*If using a GitHub Personal Access Token (PAT):*
```powershell
.\auto_update_github.bat https://<TOKEN>@github.com/YOUR_USERNAME/YOUR_REPO.git
```

### Option 2: Direct Python Sync
```powershell
python auto_update_git.py https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

Once pushed, Vercel automatically detects the commit, provisions the Python runtime, and deploys the updated web application with zero manual configuration.

---

## How to Run Locally

### Start Local Server:
```powershell
.\run.bat
```
or:
```powershell
python server.py
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser.

### Start Live Public Demo Tunnel:
```powershell
.\start_live_demo.bat
```
or:
```powershell
python start_live.py
```
