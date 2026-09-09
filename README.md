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

## Recruiter presentation

The page targets graduate software development opportunities, with Java/Python, APIs, testing and CI/CD as the core evidence. The grade calculator leads because it demonstrates Java web development and a documented CI Engineer/Git Lead role; IdentityGuard follows for API integration. Academic and team work are labelled explicitly. The user confirmed the Diploma in IT is completed and the Advanced Diploma is in progress; no dates, marks or availability are inferred.

The hero offers CV, email, LinkedIn and GitHub access. Project skill links and a two-column desktop layout support scanning, with a single column on phones. Skills link back to project evidence. The linked graduate CV is a new review draft; previous CV files are retained.

BET Software's graduate programme page was reviewed on 10 September 2026 for its emphasis on learning, collaboration and the SDLC. It still listed the 2026 intake and a 15 September 2025 closing date; no currently open intake was verified. The public portfolio does not imply an application, endorsement or employment relationship.

## Content maintenance

Keep the website aligned with the actual project repositories. IdentityGuard uses Python/FastAPI with a Java client. Credit Card Fraud Detection is a VUT team project; the linked repository credits Mpho as team lead.

Student Grade Calculator is a separate Java web and DevOps team assessment, linked to `edsboys/student-grade-calculator`. Its README credits Mpho as CI Engineer and Git Lead. The project card describes the checked-in tools and workflows without claiming all tests pass or attributing the entire team's implementation to one person. Its SVG is a project illustration, not an application screenshot.

Only show demo or credential buttons when there is an actual destination. Student Records currently offers an email enquiry because its specific source repository is not confirmed. Credential buttons require matching verification URLs; badge IDs alone are not used to invent links. The IBM entry remains marked in progress and links to the programme, not an earned credential.

Avoid self-rated percentage bars and unsupported totals. Update credential status only when completion is confirmed.

## Contact

The email buttons open the visitor's mail application. The site does not submit or store messages. Visitors can copy the visible email address; JavaScript adds a copy button with success and failure feedback when the Clipboard API is available.

## Images

The original assets are retained. The page uses `portrait-320.webp` and `portrait-640.webp` through `srcset`, `identityguard.webp`, and a 48-pixel `favicon.png`. Project images below the introduction load lazily. Every image declares dimensions to reserve layout space.

## CV maintenance

The website currently links to `assets/Mpho_Matseka_Graduate_CV.pdf`. The optional `cv.py` script uses ReportLab and writes `Mpho_Matseka_CV_2025.pdf` in the repository root. Generating that file does not automatically replace the linked CV. Review the generated document and deliberately update the website link or replace the linked file when publishing a new CV.

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

## Additional credentials (owner supplied, September 2026)

The portfolio includes 22 distinct certifications, specialisations, badges and courses from the supplied list. Six relevant credentials are featured; 16 are grouped in a native expandable section usable without JavaScript. Java specialisation and CCNA/CCNAv7 Introduction to Networks duplicates are consolidated. The Cisco entry describes introductory coursework, not full CCNA certification. AI Skills Fest is retained as additional learning without describing it as an exam certification. The Full Stack programme remains separately marked in progress.

The previous generic Oracle and Cisco entries were replaced by the supplied exact titles, issue dates and Oracle expiry dates. The old Oracle verification URL was removed because it could not be matched to these specific awards from the supplied information. No award was independently verified in this update.

Supplied credential IDs for future matching: Java specialisation `O5XT0C4JPPEW`; Yonsei IoT course `S2UH7GIFWUEP`; Cisco networking course `885dcc2d-b1d8-4c5b-ab16-2d8ac8bfb544`. Add real verification links when available.

## Motion

The introduction and content blocks use short, one-time Web Animations API reveals with a small stagger and decelerating easing. IntersectionObserver triggers sections as they enter the viewport. Desktop hover adds a subtle card lift and image scale; buttons have press feedback. The header uses a translucent backdrop where supported. The existing native smooth scrolling is retained; there is no scroll interception, continuous parallax or animation dependency.

Content is visible in the base HTML/CSS, including when JavaScript, IntersectionObserver or the animation API is unavailable. Reduced-motion preferences suppress CSS and JavaScript motion, including changes while the page is open. Keyboard focus cancels an ancestor's entrance animation so links can be used immediately. Native disclosure semantics remain intact for the menu and additional credentials.
