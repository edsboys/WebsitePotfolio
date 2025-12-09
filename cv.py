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
    Table,
    TableStyle,
    KeepTogether
)
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

# --- CV DATA ---
cv_data = {
    "file_path": "Mpho_Matseka_CV_2025.pdf",
    "name": "MPHO MATSEKA",
    "title": "SOFTWARE DEVELOPER | FULL STACK",
    "tagline": "Building intelligent, people-centered solutions through code and data.",
    
    "contact_info": [
        ("Email", "ehlersdanlosboy@gmail.com", "mailto:ehlersdanlosboy@gmail.com"),
        ("LinkedIn", "linkedin.com/in/mphomatseka", "https://linkedin.com/in/mphomatseka"),
        ("GitHub", "github.com/edsboys", "https://github.com/edsboys"),
        ("Portfolio", "mphomatseka.dev", "https://www.mphomatseka.dev"),
        ("Location", "Gauteng, South Africa", None),
    ],

    "profile_summary": (
        "Final-year Software Development student with practical experience in <b>Full Stack Engineering</b> and <b>Data Analytics</b>. "
        "Skilled in building interactive dashboards, fraud detection algorithms, and chatbot interfaces. "
        "Currently finalizing an IBM Full Stack Professional Certificate. Seeking to leverage strong Python and Java skills "
        "to build scalable, intelligent software solutions."
    ),

    "technical_skills": [
        ("Core Languages", "Python, JavaScript (ES6+), Java, SQL"),
        ("Web & Frameworks", "React.js, Flask, Spring Boot, Tailwind CSS"),
        ("AI & Data", "Machine Learning (Scikit-learn), Data Visualization, Chatbots"),
        ("Cloud & Tools", "Azure AI, Oracle Cloud (OCI), Docker, Git/GitHub"),
        ("Systems Analysis", "User Dashboards, Process Automation, Data Integrity"),
    ],

    "education": {
        "degree": "Diploma in Information Technology (Software Development)",
        "university": "Vaal University of Technology",
        "status": "Final Year (Graduating soon)",
        "details": "Specialized in Systems Analysis and Software Engineering."
    },

    "certifications": [
        "<b>IBM</b> Full Stack Software Developer (In Progress)",
        "<b>IT Varsity</b> Full Stack Development Certificate",
        "<b>Oracle Cloud Infrastructure 2025</b> AI Foundations Associate",
        "<b>Microsoft Azure</b> AI Fundamentals (AI-900)",
        "<b>Cisco</b> CCNA v7: Introduction to Networks & Cybersecurity",
    ],

    "projects": [
        {
            "title": "Credit Card Fraud Detection System",
            "stack": "Python, Flask, Scikit-Learn, Data Visualization",
            "bullets": [
                "Developed a Machine Learning model achieving <b>80.6% recall</b> to identify fraudulent transactions.",
                "Built an interactive web dashboard (Flask) to visualize fraud patterns for non-technical users.",
                "Implemented data cleaning pipelines to process 250,000+ financial records, ensuring high data integrity.",
                "Demonstrated ability to bridge the gap between complex ML logic and user-friendly software."
            ],
        },
        {
            "title": "Student Records Management System",
            "stack": "Java, SQL, Object-Oriented Design",
            "bullets": [
                "Architected a secure backend system for managing sensitive student data.",
                "Designed a robust database schema with strict validation rules to prevent data corruption.",
                "Applied OOP principles to create modular, maintainable code for long-term scalability."
            ],
        },
        {
            "title": "HealthTrack.AI (In Progress)",
            "stack": "React Native, Mobile Architecture, AI Integration",
            "bullets": [
                "Designing a mobile-first architecture for patient vital monitoring.",
                "Planning the integration of a chatbot assistant for symptom checking.",
                "Focusing on secure, real-time data synchronization between mobile app and backend."
            ],
        },
    ],
    
    "achievements": [
        "<b>Finalist:</b> FNB App of the Year Hackathon & VUT Internal Hackathon.",
        "<b>Production Ready:</b> Built 3 applications demonstrating full system lifecycle (SDLC) competence.",
        "<b>Advocacy:</b> Active advocate for Ehlers-Danlos Syndrome awareness."
    ]
}

# --- VISUAL CONFIGURATION ---
COLORS = {
    "primary": colors.HexColor("#0F172A"),    # Slate 900
    "accent": colors.HexColor("#0EA5E9"),     # Sky 500
    "text": colors.HexColor("#334155"),       # Slate 700
    "light_text": colors.HexColor("#64748B"), # Slate 500
    "line": colors.HexColor("#E2E8F0"),       # Slate 200
}

def get_stylesheet():
    styles = getSampleStyleSheet()
    
    # Custom Styles - renamed to ensure NO collisions with default library styles
    styles.add(ParagraphStyle(name="HeaderName", fontName="Helvetica-Bold", fontSize=24, textColor=COLORS["primary"], alignment=TA_CENTER, spaceAfter=4))
    styles.add(ParagraphStyle(name="HeaderTitle", fontName="Helvetica", fontSize=11, textColor=COLORS["accent"], alignment=TA_CENTER, spaceAfter=10, spaceBefore=2, letterSpacing=1.5))
    styles.add(ParagraphStyle(name="HeaderTagline", fontName="Helvetica-Oblique", fontSize=9, textColor=COLORS["light_text"], alignment=TA_CENTER, spaceAfter=15))
    
    styles.add(ParagraphStyle(name="SectionTitle", fontName="Helvetica-Bold", fontSize=12, textColor=COLORS["primary"], spaceBefore=12, spaceAfter=6, textTransform='uppercase'))
    
    # Renamed to CVBody to avoid "BodyText" collision
    styles.add(ParagraphStyle(name="CVBody", fontName="Helvetica", fontSize=10, leading=14, textColor=COLORS["text"], alignment=TA_JUSTIFY))
    
    # Skill Table Styles
    styles.add(ParagraphStyle(name="SkillCategory", fontName="Helvetica-Bold", fontSize=9, textColor=COLORS["primary"], alignment=TA_RIGHT))
    styles.add(ParagraphStyle(name="SkillList", fontName="Helvetica", fontSize=9, textColor=COLORS["text"], alignment=TA_LEFT))
    
    # Project Styles
    styles.add(ParagraphStyle(name="ProjectTitle", fontName="Helvetica-Bold", fontSize=11, textColor=COLORS["primary"], spaceAfter=2))
    styles.add(ParagraphStyle(name="ProjectStack", fontName="Helvetica-Oblique", fontSize=9, textColor=COLORS["accent"], spaceAfter=4))
    
    # Renamed to CVBullet to avoid "Bullet" collision
    styles.add(ParagraphStyle(name="CVBullet", fontName="Helvetica", fontSize=10, leading=13, textColor=COLORS["text"], leftIndent=10, firstLineIndent=0, spaceAfter=2))

    return styles

# --- BUILDERS ---

def build_header(story, data, styles):
    story.append(Paragraph(data["name"], styles["HeaderName"]))
    story.append(Paragraph(data["title"], styles["HeaderTitle"]))
    story.append(Paragraph(data["tagline"], styles["HeaderTagline"]))
    
    # Contact Grid (Using Table for alignment)
    contact_data = []
    row = []
    for i, (label, val, link) in enumerate(data["contact_info"]):
        text = f'<a href="{link}" color="#0EA5E9">{val}</a>' if link else val
        display = f"<b>{label}:</b> {text}"
        row.append(Paragraph(display, styles["SkillList"])) 
        if len(row) == 3 or i == len(data["contact_info"]) - 1:
            contact_data.append(row)
            row = []
            
    c_table = Table(contact_data, colWidths=[180, 180, 180])
    c_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(c_table)
    
    story.append(Spacer(1, 10))
    story.append(Table([[""]], colWidths=['100%'], style=[('LINEBELOW', (0,0), (-1,-1), 1, COLORS["line"])]))
    story.append(Spacer(1, 10))

def build_skills_grid(story, data, styles):
    story.append(Paragraph("TECHNICAL SKILLS", styles["SectionTitle"]))
    
    table_data = []
    for category, items in data["technical_skills"]:
        table_data.append([
            Paragraph(category, styles["SkillCategory"]),
            Paragraph(items, styles["SkillList"])
        ])

    t = Table(table_data, colWidths=[3*cm, 13*cm])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, COLORS["line"]),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0, colors.white),
    ]))
    story.append(t)

def build_experience_projects(story, data, styles):
    story.append(Paragraph("FEATURED PROJECTS", styles["SectionTitle"]))
    
    for proj in data["projects"]:
        content = []
        content.append(Paragraph(proj["title"], styles["ProjectTitle"]))
        content.append(Paragraph(proj["stack"], styles["ProjectStack"]))
        
        for b in proj["bullets"]:
            content.append(Paragraph(f"• {b}", styles["CVBullet"]))
        
        content.append(Spacer(1, 8))
        story.append(KeepTogether(content))

def build_education_cert(story, data, styles):
    story.append(Paragraph("EDUCATION & CERTIFICATIONS", styles["SectionTitle"]))
    
    # Education
    edu = data["education"]
    story.append(Paragraph(f"{edu['degree']}", styles["ProjectTitle"]))
    story.append(Paragraph(f"{edu['university']} | {edu['status']}", styles["CVBody"]))
    story.append(Spacer(1, 6))
    
    # Certs
    for cert in data["certifications"]:
        story.append(Paragraph(f"• {cert}", styles["CVBullet"]))

def build_achievements(story, data, styles):
    if not data.get("achievements"): return
    story.append(Paragraph("ACHIEVEMENTS", styles["SectionTitle"]))
    for ach in data["achievements"]:
        story.append(Paragraph(f"• {ach}", styles["CVBullet"]))

# --- MAIN GENERATOR ---
def create_cv():
    # Ensure output directory exists
    os.makedirs(os.path.dirname(cv_data["file_path"]) or ".", exist_ok=True)

    doc = SimpleDocTemplate(
        cv_data["file_path"],
        pagesize=A4,
        rightMargin=2*cm, leftMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm
    )
    
    styles = get_stylesheet()
    story = []
    
    build_header(story, cv_data, styles)
    
    story.append(Paragraph("PROFESSIONAL PROFILE", styles["SectionTitle"]))
    story.append(Paragraph(cv_data["profile_summary"], styles["CVBody"]))
    story.append(Spacer(1, 6))
    
    build_skills_grid(story, cv_data, styles)
    build_experience_projects(story, cv_data, styles)
    build_education_cert(story, cv_data, styles)
    build_achievements(story, cv_data, styles)
    
    doc.build(story)
    print(f"CV Generated successfully: {os.path.abspath(cv_data['file_path'])}")

if __name__ == "__main__":
    create_cv()