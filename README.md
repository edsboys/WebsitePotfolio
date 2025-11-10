# Mpho Matseka's Personal Portfolio

This repository contains the source code for my personal portfolio website. It showcases my skills, projects, and professional background as a software developer. The site is designed to be clean, modern, and fully responsive.

A key feature of this project is the Python script (`cv.py`) that programmatically generates my CV in PDF format using the `reportlab` library, ensuring the content is always up-to-date with the data defined in the script.

## ✨ Features

*   **Responsive Design**: Adapts to various screen sizes from mobile to desktop.
*   **Interactive UI**: Smooth scrolling, scroll-triggered animations, and a dynamic hamburger menu for mobile navigation.
*   **Dynamic CV Generation**: A Python script automatically creates the downloadable PDF version of my CV.
*   **Project Showcase**: A dedicated section to display my recent work with links to the corresponding GitHub repositories.
*   **Clear Navigation**: Includes sections for About, Skills, Projects, and Contact information.

## 🛠️ Technologies Used

*   **Frontend**: HTML5, CSS3, JavaScript
*   **CV Generation**: Python, `reportlab`

## 🚀 Getting Started

### Prerequisites

To generate the CV, you need Python and the `reportlab` library installed.

```sh
pip install reportlab
```

### Running the Project

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd WebsitePotfolio
    ```
3.  **Generate the CV (Optional):**
    If you need to regenerate the CV from the data in [`cv.py`](cv.py), run the script:
    ```sh
    python cv.py
    ```
    This will create or update the `Mpho_Matseka_CV_v2.pdf` file in the `assets` directory.

4.  **View the website:**
    Open the [`index.html`](index.html) file in your web browser to see the portfolio live.
