import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem,
    HRFlowable,
    Table,
    TableStyle,
)
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY


# --- CV DATA ---
cv_data = {
    "file_path": "./assets/Mpho_Matseka_CV_Professional.pdf",
    "name": "MPHO MATSEKA",
    "title": "Software Developer | AI/ML Engineer",
    "tagline": "Building intelligent solutions through code and data",
    "contact": {
        "Email": "ehlersdanlosboy@gmail.com",
        "LinkedIn": "linkedin.com/in/mphomatseka",
        "GitHub": "github.com/edsboys",
        "Website": "www.mphomatseka.dev",
        "Location": "South Africa",
    },
    "profile_summary": (
        "Final-year Software Development student with proven expertise in AI/ML implementation "
        "and full-stack development. Successfully deployed fraud detection systems processing 250K+ records "
        "with 80.6% recall. Competed in multiple prestigious hackathons including FNB App of the Year. "
        "Certified in Oracle Cloud AI, Azure AI, and Full-Stack Development. Passionate about leveraging "
        "AI to solve real-world problems through scalable, data-driven applications."
    ),
    "technical_skills": {
        "Languages & Frameworks": ["Python", "Java", "JavaScript", "React", "Flask", "Spring Boot"],
        "AI/ML & Data": ["Scikit-learn", "NLP", "Data Analytics", "Model Deployment", "Feature Engineering"],
        "Frontend Technologies": ["HTML5", "CSS3", "Tailwind CSS", "Material UI", "Responsive Design"],
        "Backend & Databases": ["SQL", "PostgreSQL", "RESTful APIs", "Database Design"],
        "Cloud & DevOps": ["Oracle Cloud Infrastructure", "Microsoft Azure", "Docker", "Git/GitHub"],
        "Methodologies": ["Agile/Scrum", "Problem-solving", "Debugging", "Code Review"],
    },
    "education": {
        "degree": "Diploma in Information Technology - Software Development",
        "university": "Vaal University of Technology",
        "location": "South Africa",
        "status": "Final Year - Expected Graduation 2025",
        "highlights": [
            "Specialized in Software Development & AI/ML",
            "Completed multiple industry certifications alongside degree",
        ],
    },
    "certifications": [
        {"name": "Oracle Cloud Infrastructure 2025 AI Foundations Associate", "org": "Oracle"},
        {"name": "Microsoft Azure AI Fundamentals (AI-900)", "org": "Microsoft"},
        {"name": "Full Stack Development Certificate", "org": "IT Varsity"},
        {"name": "IBM Data Fundamentals", "org": "IBM"},
        {"name": "CCNA v7: Introduction to Networks", "org": "Cisco"},
        {"name": "Introduction to Cybersecurity", "org": "Cisco"},
    ],
    "projects": [
        {
            "title": "Credit Card Fraud Detection System",
            "tech": "Python • Scikit-learn • Flask • Data Visualization",
            "achievements": [
                "Developed ML model achieving 80.6% recall rate for fraud detection",
                "Successfully processed and analyzed 250,000+ transaction records",
                "Implemented real-time anomaly detection with Flask REST API",
                "Created interactive dashboards for fraud pattern visualization",
            ],
        },
        {
            "title": "Pitch Perfect AI",
            "tech": "JavaScript • Google Gemini API • Web Audio API • Real-time Processing",
            "achievements": [
                "Built AI-powered public speaking coach with real-time speech analysis",
                "Integrated Google Gemini for intelligent feedback and improvement suggestions",
                "Designed intuitive UI for speech recording and instant performance metrics",
                "Implemented features for tone, pace, and clarity assessment",
            ],
        },
        {
            "title": "Student Records Management System",
            "tech": "Java • AWT • Data Structures • Object-Oriented Design",
            "achievements": [
                "Developed comprehensive GUI application for student data management",
                "Implemented efficient data structures (ArrayLists) for record handling",
                "Created CRUD operations with data validation and error handling",
                "Designed intuitive interface following OOP principles",
            ],
        },
    ],
    "achievements": [
        "Competed in FNB App of the Year Hackathon - National competition",
        "Participated in Intervarsity Hackathon - Multi-university competition",
        "Competed in VUT First Annual Internal Hackathon",
        "Earned 6 professional certifications in AI, Cloud, and Development",
        "Built 3 production-ready applications showcasing full-stack and AI capabilities",
    ],
}

# --- COLOR SCHEME ---
PRIMARY_COLOR = colors.HexColor("#0A4D68")  # Deep Professional Blue
ACCENT_COLOR = colors.HexColor("#088395")   # Vibrant Teal
TEXT_DARK = colors.HexColor("#1A1A1A")      # Almost Black
TEXT_MUTED = colors.HexColor("#666666")     # Medium Gray

# --- STYLES ---
def get_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="Name",
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=PRIMARY_COLOR,
        leading=26,
        spaceAfter=2,
        alignment=TA_LEFT,
    ))
    styles.add(ParagraphStyle(
        name="CvTitle",  # renamed to avoid clash with built-in 'Title'
        fontName="Helvetica",
        fontSize=11.5,
        textColor=ACCENT_COLOR,
        spaceAfter=2,
        alignment=TA_LEFT,
    ))
    styles.add(ParagraphStyle(
        name="Tagline",
        fontName="Helvetica-Oblique",
        fontSize=9.5,
        textColor=TEXT_MUTED,
        spaceAfter=6,
        alignment=TA_LEFT,
    ))
    styles.add(ParagraphStyle(
        name="Contact",
        fontName="Helvetica",
        fontSize=9,
        textColor=TEXT_MUTED,
        spaceAfter=8,
        alignment=TA_LEFT,
    ))
    styles.add(ParagraphStyle(
        name="SectionH",
        fontName="Helvetica-Bold",
        fontSize=12.5,
        textColor=PRIMARY_COLOR,
        spaceBefore=6,
        spaceAfter=6,
        underlineWidth=0.5,
    ))
    styles.add(ParagraphStyle(
        name="Body",
        fontName="Helvetica",
        fontSize=10,
        textColor=TEXT_DARK,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="Subhead",
        fontName="Helvetica-Bold",
        fontSize=10.5,
        textColor=TEXT_DARK,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name="Meta",
        fontName="Helvetica-Oblique",
        fontSize=9,
        textColor=TEXT_MUTED,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="BulletText",
        fontName="Helvetica",
        fontSize=10,
        textColor=TEXT_DARK,
        leading=14,
    ))
    styles.add(ParagraphStyle(
        name="Footer",
        fontName="Helvetica",
        fontSize=8.5,
        textColor=TEXT_MUTED,
        alignment=TA_CENTER,
    ))

    # Tweak built-ins for consistency
    styles["Normal"].fontName = "Helvetica"
    styles["Normal"].fontSize = 10
    styles["Normal"].leading = 14
    styles["Normal"].textColor = TEXT_DARK
    styles["Normal"].spaceAfter = 4

    return styles

# --- HELPERS ---
def ensure_url(u: str) -> str:
    if not u:
        return ""
    if u.startswith("http://") or u.startswith("https://"):
        return u
    return "https://" + u

def clean_text(s: str) -> str:
    # Remove common emoji that won't render with core PDF fonts
    if not s:
        return s
    for ch in ["🏆", "🎓", "💻", "•"]:
        s = s.replace(ch, "")
    return s.strip()

def bullets(items, styles) -> ListFlowable:
    return ListFlowable(
        [ListItem(Paragraph(clean_text(i), styles["BulletText"]), leftIndent=0) for i in items if i],
        bulletType="bullet",
        start=None,
        leftIndent=12,
        bulletFontName="Helvetica",
        bulletFontSize=9,
        bulletOffsetY=0,
    )

# --- DOCUMENT BUILDERS ---
def build_header(story, data, styles):
    story.append(Paragraph(data["name"], styles["Name"]))
    story.append(Paragraph(data["title"], styles["CvTitle"]))
    if data.get("tagline"):
        story.append(Paragraph(data["tagline"], styles["Tagline"]))

    email = data["contact"].get("Email", "")
    ln = ensure_url(data["contact"].get("LinkedIn", ""))
    gh = ensure_url(data["contact"].get("GitHub", ""))
    loc = data["contact"].get("Location", "")

    contact_parts = []
    if email:
        contact_parts.append(f"<link href='mailto:{email}'>{email}</link>")
    if ln:
        contact_parts.append(f"<link href='{ln}'>LinkedIn</link>")
    if gh:
        contact_parts.append(f"<link href='{gh}'>GitHub</link>")
    if data["contact"].get("Website", ""):
        web = ensure_url(data["contact"]["Website"])
        contact_parts.append(f"<link href='{web}'>Website</link>")
    if loc:
        contact_parts.append(loc)

    story.append(Paragraph(" | ".join(contact_parts), styles["Contact"]))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY_COLOR, spaceBefore=4, spaceAfter=8))

def build_profile(story, data, styles):
    story.append(Paragraph("Professional Summary", styles["SectionH"]))
    story.append(Paragraph(data["profile_summary"], styles["Body"]))

def build_skills(story, data, styles):
    story.append(Paragraph("Technical Skills", styles["SectionH"]))
    for category, items in data["technical_skills"].items():
        text = f"<b>{category}:</b> {', '.join(items)}"
        story.append(Paragraph(text, styles["Body"]))
    story.append(Spacer(1, 4))

def build_projects(story, data, styles):
    story.append(Paragraph("Projects", styles["SectionH"]))
    for proj in data["projects"]:
        story.append(Paragraph(proj["title"], styles["Subhead"]))
        if proj.get("tech"):
            story.append(Paragraph(proj["tech"], styles["Meta"]))
        if proj.get("achievements"):
            story.append(bullets(proj["achievements"], styles))
        story.append(Spacer(1, 4))

def build_education(story, data, styles):
    story.append(Paragraph("Education", styles["SectionH"]))
    edu = data["education"]
    degree_line = f"{edu['degree']}"
    meta_line = ", ".join([p for p in [edu.get("university"), edu.get("location"), edu.get("status")] if p])
    story.append(Paragraph(degree_line, styles["Subhead"]))
    if meta_line:
        story.append(Paragraph(meta_line, styles["Meta"]))
    if edu.get("highlights"):
        story.append(bullets(edu["highlights"], styles))

def build_certifications(story, data, styles):
    story.append(Paragraph("Certifications", styles["SectionH"]))
    cert_texts = [f"{c['name']} — {c.get('org','')}".strip(" —") for c in data["certifications"]]
    story.append(bullets(cert_texts, styles))

def build_achievements(story, data, styles):
    if not data.get("achievements"):
        return
    story.append(Paragraph("Achievements", styles["SectionH"]))
    story.append(bullets([clean_text(a) for a in data["achievements"]], styles))

# --- PAGE DECORATION ---
def on_page_footer(canvas, doc):
    canvas.saveState()
    width, height = doc.pagesize
    canvas.setStrokeColor(colors.HexColor("#DDDDDD"))
    canvas.setLineWidth(0.5)
    y = 1.4 * cm
    canvas.line(doc.leftMargin, y + 0.35 * cm, width - doc.rightMargin, y + 0.35 * cm)

    canvas.setFont("Helvetica", 8.5)
    canvas.setFillColor(TEXT_MUTED)
    footer_text = f"{cv_data['name']}    •    Page {doc.page}"
    canvas.drawCentredString(width / 2.0, y, footer_text)
    canvas.restoreState()

# --- MAIN ---
def create_cv():
    # Ensure output directory exists
    os.makedirs(os.path.dirname(cv_data["file_path"]) or ".", exist_ok=True)

    styles = get_styles()

    doc = SimpleDocTemplate(
        cv_data["file_path"],
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    story = []

    # Header (only as content on page 1 so it doesn't repeat)
    build_header(story, cv_data, styles)

    # Body sections
    build_profile(story, cv_data, styles)
    build_skills(story, cv_data, styles)
    build_projects(story, cv_data, styles)
    build_education(story, cv_data, styles)
    build_certifications(story, cv_data, styles)
    build_achievements(story, cv_data, styles)

    # Build with footer drawn on every page
    doc.build(story, onFirstPage=on_page_footer, onLaterPages=on_page_footer)

    print(f"Professional CV created at {cv_data['file_path']}")

if __name__ == "__main__":
    create_cv()