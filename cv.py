import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# --- 1. CV Data (All your content in one place) ---
# Edit this dictionary to update your CV
cv_data = {
    "file_path": "./html-css-js-portfolio-tutorial-2/assets/Mpho_Matseka_CV_v2.pdf",
    "name": "Mpho Matseka",

    "title": "Software Developer | Aspiring Full Stack Engineer",
    "contact": {
        "Email": "ehlersdanlosboy@gmail.com",
        "LinkedIn": "linkedin.com/in/mphomatseka/",
        "GitHub": "github.com/edsboys",
        "Location": "South Africa"
    },
    "skills": {
        "Frontend": "HTML, CSS, JavaScript, React, Tailwind CSS, Material UI",
        "Backend": "Java, Python, Flask, Spring Boot",
        "Databases": "SQL, PostgreSQL",
        "AI/ML": "Python, Scikit-learn, basic NLP, data analytics",
        "Cloud & Tools": "Oracle Cloud, Microsoft Azure, Git/GitHub, Docker",
        "Other": "Agile/Scrum, problem-solving, debugging"
    },
    "profile_summary": (
        "Final-year IT student at VUT specializing in Software Development. "
        "Passionate about building data-driven applications and AI solutions. "
        "Completed certifications in AI, cloud computing, cybersecurity, and full-stack development. "
        "Seeking opportunities in software engineering and AI integration projects."
    ),
    "education": {
        "degree": "Diploma in Information Technology (Software Development)",
        "university": "Vaal University of Technology, South Africa (Final Year)"
    },
    "certifications": [
        "Oracle Cloud Infrastructure 2025 Certified AI Foundations Associate",
        "Microsoft Azure AI Fundamentals (AI-900)",
        "IBM Data Fundamentals",
        "CCNA v7: Introduction to Networks (Cisco)",
        "Introduction to Cybersecurity (Cisco)",
        "Full Stack Development Certificate (IT Varsity)"
    ],
    "projects": [
        {
            "title": "Credit Card Fraud Detection",
            "desc": "Python, Scikit-learn, Flask, visualization. AI model for anomaly detection in financial data."
        },
        {
            "title": "Student Records Management System",
            "desc": "Java GUI app using AWT and ArrayLists for student record management."
        },
        {
            "title": "Pitch Perfect AI",
            "desc": "Web app using Google Gemini for real-time speech analysis and feedback for public speaking improvement."
        }
    ]
}

# --- 2. Layout Constants (Easy to tweak layout) ---
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_LEFT = 2.5 * cm
MARGIN_RIGHT = 2.5 * cm
MARGIN_TOP = 2.0 * cm
MARGIN_BOTTOM = 2.0 * cm
COLUMN_GAP = 1.5 * cm
LEFT_COLUMN_WIDTH = 7 * cm
RIGHT_COLUMN_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT - LEFT_COLUMN_WIDTH - COLUMN_GAP
LEFT_X = MARGIN_LEFT
RIGHT_X = MARGIN_LEFT + LEFT_COLUMN_WIDTH + COLUMN_GAP

# --- 3. Style Definitions ---
def get_styles():
    """Defines ParagraphStyle objects for the CV."""
    styles = getSampleStyleSheet()
    
    # Define custom colors
    primary_color = colors.HexColor("#1f4e79") # Dark Blue
    secondary_color = colors.HexColor("#0a0a0a") # Near Black
    accent_color = colors.HexColor("#555555") # Gray
    
    # Base style for all normal text
    base_style = ParagraphStyle(
        'Base',
        fontName='Helvetica',
        fontSize=10,
        textColor=secondary_color,
        leading=14,
        alignment=TA_LEFT
    )

    # Add custom styles
    styles.add(ParagraphStyle(
        name='Name',
        fontSize=26,
        fontName='Helvetica-Bold',
        textColor=primary_color,
        spaceAfter=6,
        alignment=TA_CENTER
     ))
    
    # Modify the existing 'Title' style instead of adding a new one
    styles['Title'].parent = base_style
    styles['Title'].fontSize = 12
    styles['Title'].textColor = accent_color
    styles['Title'].spaceAfter = 10
    styles['Title'].alignment = TA_CENTER
    
    styles.add(ParagraphStyle(
        name='SectionHead',
        fontSize=12,
        fontName='Helvetica-Bold',
        textColor=primary_color,
        spaceAfter=8,
        borderPadding=5
    ))
    styles.add(ParagraphStyle(
        name='JobTitle',
        parent=base_style,
        fontName='Helvetica-Bold',
        spaceAfter=1
    ))
    styles.add(ParagraphStyle(
        name='Footer',
        parent=base_style,
        fontSize=8,
        textColor=accent_color,
        alignment=TA_LEFT
    ))
    styles.add(ParagraphStyle(
        name='SkillCategory',
        parent=base_style,
        fontName='Helvetica-Bold',
        spaceAfter=2
    ))
    styles.add(ParagraphStyle(
        name='SkillList',
        parent=base_style,
        leftIndent=14,
        spaceAfter=6
    ))

    # Modify existing styles
    styles['Normal'].fontName = 'Helvetica'
    styles['Normal'].fontSize = 10
    styles['Normal'].textColor = secondary_color
    styles['Normal'].leading = 14
    styles['Normal'].spaceAfter = 4
    styles['Normal'].alignment = TA_LEFT

    styles['Bullet'].parent = styles['Normal']
    styles['Bullet'].leftIndent = 14
    styles['Bullet'].spaceAfter = 2
    styles['Bullet'].bulletIndent = 0
    styles['Bullet'].bulletText = '•'
    
    return styles

# --- 4. Helper Drawing Function ---
def draw_flowable(canvas, x, y, width, flowable):
    """
    Draws a ReportLab flowable (like a Paragraph) on the canvas.
    It automatically calculates the height and returns the new Y coordinate.
    """
    # wrapOn tells the flowable to calculate its size given the constraints
    w, h = flowable.wrapOn(canvas, width, PAGE_HEIGHT) 
    
    # drawOn places the flowable on the canvas
    flowable.drawOn(canvas, x, y - h)
    
    # Return the new y-coordinate for the next element
    return y - h

# --- 5. Drawing Functions ---
def draw_header(c, y_start, styles, data):
    """Draws the main header with name and title."""
    y = y_start
    
    # 1. Draw Name
    name_p = Paragraph(data['name'], styles['Name'])
    y = draw_flowable(c, MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT, name_p)
    
    # 2. Add a line below the header
    y -= 24  # Small padding above the line
    c.setStrokeColor(colors.HexColor("#1f4e79"))
    c.setLineWidth(1)
    c.line(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y)
    y -= 5  # Small padding below the line
    
    # 3. Draw Title (now below the line)
    title_p = Paragraph(data['title'], styles['Title'])
    y = draw_flowable(c, MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT, title_p)
    
    return y - 10 # Return new y-position with extra space

def draw_left_column(c, y_start, styles, data):
    """Draws the entire left column (Contact and Skills)."""
    y = y_start
    
    # --- Contact Info ---
    y = draw_flowable(c, LEFT_X, y, LEFT_COLUMN_WIDTH, Paragraph("Contact Info", styles['SectionHead']))
    
    # Create hyperlinks for contact info
    contact_details = {
        "Email": f"<link href='mailto:{data['contact']['Email']}'>{data['contact']['Email']}</link>",
        "LinkedIn": f"<link href='https://{data['contact']['LinkedIn']}'>{data['contact']['LinkedIn']}</link>",
        "GitHub": f"<link href='https://{data['contact']['GitHub']}'>{data['contact']['GitHub']}</link>",
        "Location": data['contact']['Location']
    }

    for key, value in contact_details.items():
        text = f"<b>{key}:</b> {value}"
        y = draw_flowable(c, LEFT_X, y, LEFT_COLUMN_WIDTH, Paragraph(text, styles['Normal']))
        y -= 2 # Small gap between contact items
    
    y -= 10 # Gap before next section

    # --- Technical Skills ---
    y = draw_flowable(c, LEFT_X, y, LEFT_COLUMN_WIDTH, Paragraph("Technical Skills", styles['SectionHead']))
    for category, skills in data['skills'].items():
        y = draw_flowable(c, LEFT_X, y, LEFT_COLUMN_WIDTH, Paragraph(category, styles['SkillCategory']))
        y = draw_flowable(c, LEFT_X, y, LEFT_COLUMN_WIDTH, Paragraph(skills, styles['SkillList']))

def draw_right_column(c, y_start, styles, data):
    """Draws the entire right column (Profile, Education, etc.)."""
    y = y_start
    
    # --- Profile Summary ---
    y = draw_flowable(c, RIGHT_X, y, RIGHT_COLUMN_WIDTH, Paragraph("Profile Summary", styles['SectionHead']))
    y = draw_flowable(c, RIGHT_X, y, RIGHT_COLUMN_WIDTH, Paragraph(data['profile_summary'], styles['Normal']))
    
    y -= 10 # Gap before next section

    # --- Education ---
    y = draw_flowable(c, RIGHT_X, y, RIGHT_COLUMN_WIDTH, Paragraph("Education", styles['SectionHead']))
    y = draw_flowable(c, RIGHT_X, y, RIGHT_COLUMN_WIDTH, Paragraph(data['education']['degree'], styles['JobTitle']))
    y = draw_flowable(c, RIGHT_X, y, RIGHT_COLUMN_WIDTH, Paragraph(data['education']['university'], styles['Normal']))
    
    y -= 10

    # --- Certifications ---
    y = draw_flowable(c, RIGHT_X, y, RIGHT_COLUMN_WIDTH, Paragraph("Certifications", styles['SectionHead']))
    for cert in data['certifications']:
        y = draw_flowable(c, RIGHT_X, y, RIGHT_COLUMN_WIDTH, Paragraph(cert, styles['Bullet']))

    y -= 10

    # --- Projects ---
    y = draw_flowable(c, RIGHT_X, y, RIGHT_COLUMN_WIDTH, Paragraph("Projects", styles['SectionHead']))
    for project in data['projects']:
        y = draw_flowable(c, RIGHT_X, y, RIGHT_COLUMN_WIDTH, Paragraph(project['title'], styles['JobTitle']))
        y = draw_flowable(c, RIGHT_X, y, RIGHT_COLUMN_WIDTH, Paragraph(project['desc'], styles['Bullet']))
        y -= 5 # Gap between projects

def draw_footer(c, styles):
    """Draws the footer line and text."""
    c.setStrokeColor(colors.HexColor("#1f4e79"))
    c.setLineWidth(1)
    c.line(MARGIN_LEFT, MARGIN_BOTTOM, PAGE_WIDTH - MARGIN_RIGHT, MARGIN_BOTTOM)
    
    draw_flowable(
        c, 
        MARGIN_LEFT, 
        MARGIN_BOTTOM - 5, 
        PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT, 
        Paragraph("Generated using Python | Mpho Matseka", styles['Footer'])
    )

# --- 6. Main execution ---
def create_cv():
    # Ensure the assets folder exists
    os.makedirs("./assets", exist_ok=True)
    
    # Get data and styles
    data = cv_data
    styles = get_styles()
    
    # Create canvas
    c = canvas.Canvas(data['file_path'], pagesize=A4)
    
    # Draw Header
    current_y = PAGE_HEIGHT - MARGIN_TOP
    current_y = draw_header(c, current_y, styles, data)
    
    # Set starting Y for the two columns
    column_y_start = current_y - (0.5 * cm)
    
    # Draw Columns
    # We draw them independently from the same starting Y
    draw_left_column(c, column_y_start, styles, data)
    draw_right_column(c, column_y_start, styles, data)
    
    # Draw Footer
    draw_footer(c, styles)
    
    # Save the PDF
    c.save()
    print(f"Modern tech CV (v2) created at {data['file_path']}")

if __name__ == "__main__":
    create_cv()