import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# tells FastAPI where to find the CSS and images
app.mount("/static", StaticFiles(directory="static"), name="static")

# tells FastAPI where to find the HTML files
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def serve_portfolio(request: Request):
    # This dictionary acts as your database for the static frontend.
    # Jinja2 will loop through the 'projects' list to build your HTML cards.
    portfolio_data = {
        "request": request,  # required (FastAPI)
        "name": "John Esparragoza",
        "email": "johnesparragoza@gmail.com",
        "github_url": "https://github.com/johnesparragoza",
        "linkedin_url": "https://linkedin.com/in/john-esparragoza",
        "projects": [
            {
                "title": "First Person Narratives for ASD Individuals AI Web App",
                "tools": "Python, Streamlit, Vision-Language Models",
                "description": "An interactive web application that generates personalized first-person narrative prompts from uploaded photographs. Evaluated latency constraints and lightweight architectures, resulting in a co-authored IEEE conference publication.",
                "link": "https://github.com/johnesparragoza"
            },
            {
                "title": "Houston Crime Relational Database System",
                "tools": "MySQL, Relational Schema Design, R",
                "description": "Cleaned and preprocessed 215,000+ public crime records using R. Designed and implemented a Third Normal Form (3NF) relational database schema in MySQL and developed optimized multi-table SQL queries to support crime trend analysis.",
                "link": "https://github.com/johnesparragoza/AI-for-Support-in-Conversations-for-ASD"
            },
            {
                "title": "One Piece Metadata Analytics",
                "tools": "R, REST API, R Markdown, GitHub",
                "description": "Retrieved and parsed JSON data from a REST API, transforming episode and character metadata into structured datasets. Performed data cleaning and preprocessing to analyze saga progression, episode distribution, and story arc duration trends.",
                "link": "https://github.com/johnesparragoza/one-piece-metadata-analytics"
            }
        ],
        "experience": [
            {
                "title": "Undergraduate Researcher",
                "company": "Texas State University",
                "dates": "June 2025 - August 2025; June 2026 - August 2026",
                "description": "Engineered an end-to-end multimodal pipeline leveraging computer vision and NLP architectures to extract features from unstructured image data. Optimized model inference by deploying interactive Streamlit applications on ZeroGPU, and architected modular code repositories."
            },
            {
                "title": "Tutor",
                "company": "Collaborative Learning Community Center, University of Houston-Downtown",
                "dates": "January 2026 - Present",
                "description": "Assist students with programming assignments, debugging strategies, and problem-solving techniques to improve technical proficiency and foster collaborative learning environments in STEM disciplines."
            },
            {
                "title": "Peer Mentor",
                "company": "Scholars Academy, University of Houston-Downtown",
                "dates": "January 2026 - Present",
                "description": "Mentored 11+ undergraduate students in academic planning, research involvement, and professional development while organizing biannual networking events to strengthen community engagement."
            }
        ]
    }
    
    return templates.TemplateResponse(request=request, name="index.html", context=portfolio_data)

@app.get("/api/resume")
async def get_resume_json():
    """Serves the portfolio resume data as a raw JSON response."""
    return {
        "name": "John Esparragoza",
        "contact": {
            "email": "johnesparragoza@gmail.com",
            "github": "https://github.com/johnesparragoza",
            "linkedin": "https://linkedin.com/in/john-esparragoza"
        },
        "education": {
            "university": "University of Houston-Downtown",
            "degree": "Bachelor of Science in Computer Science, Minor in Data Science",
            "graduation": "December 2026"
        },
        "skills": {
            "languages": ["Python", "C++", "SQL", "R"],
            "libraries": ["pandas", "NumPy", "Matplotlib", "PyTorch", "TensorFlow", "scikit-learn"],
            "tools": ["Github", "Linux/Unix", "FastAPI", "Docker"]
        }
    }