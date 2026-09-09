# Mpho Matseka's portfolio

A static HTML, CSS and JavaScript portfolio, hosted at https://www.mphomatseka.dev.

## Run locally

No build step or production dependencies are required.

```sh
git clone https://github.com/edsboys/WebsitePotfolio.git
cd WebsitePotfolio
python -m http.server 8000
```

Open http://localhost:8000. Use a local server rather than opening the HTML file directly so browser features such as clipboard access can work.

## Structure

- `index.html`: semantic page content, project descriptions and links.
- `style.css`: shared colours, responsive layouts and reduced-motion preferences.
- `script.js`: mobile navigation, email-copy feedback and the copyright year.
- `assets/`: project images, responsive portrait versions, favicon and CV files.
- `tests/check_site.py`: dependency-free checks for local links, assets, IDs, landmarks and image budgets.

The primary reading and contact flows work without JavaScript. The mobile menu is a non-modal disclosure; it supports Escape, closes on outside click or focus leaving the navigation, and resets at the desktop breakpoint. Selecting a section transfers keyboard focus to the destination.

## Content maintenance

Keep the website aligned with the actual project repositories. IdentityGuard uses Python/FastAPI with a Java client. Credit Card Fraud Detection is a VUT team project; the linked repository credits Mpho as team lead.

Only show demo or credential buttons when there is an actual destination. Student Records currently offers an email enquiry because its specific source repository is not confirmed. The Cisco entry has no credential button until a verification URL is supplied. The IBM entry remains marked in progress and links to the programme, not an earned credential.

Avoid self-rated percentage bars and unsupported totals. Update credential status only when completion is confirmed.

## Contact

The email buttons open the visitor's mail application. The site does not submit or store messages. Visitors can copy the visible email address; JavaScript adds a copy button with success and failure feedback when the Clipboard API is available.

## Images

The original assets are retained. The page uses `portrait-320.webp` and `portrait-640.webp` through `srcset`, `identityguard.webp`, and a 48-pixel `favicon.png`. Project images below the introduction load lazily. Every image declares dimensions to reserve layout space.

## CV maintenance

The website currently links to `assets/Mpho_Matseka_CV_Professional.pdf`. The optional `cv.py` script uses ReportLab and writes `Mpho_Matseka_CV_2025.pdf` in the repository root. Generating that file does not automatically replace the linked CV. Review the generated document and deliberately update the website link or replace the linked file when publishing a new CV.

## Validation

```sh
python tests/check_site.py
node --check script.js
```

Before publishing, also check the page in a browser:

- 320, 375, 390, 768, 1024 and 1440-pixel widths, including long contact text.
- Menu open/close, Escape, keyboard Tab navigation, outside click and resizing across 900 pixels.
- Skip-to-content, section destinations and visible focus.
- Email-copy success/failure feedback and CV access.
- Reduced motion, 200% text enlargement and JavaScript disabled.
- All sections and loaded project images.

The site retains its GitHub Pages structure and `CNAME`. No external form account, new framework or hosting migration is required.
