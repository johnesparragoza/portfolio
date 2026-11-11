# John Esparragoza - Personal Portfolio

A containerized personal portfolio website built with Python and FastAPI, utilizing Jinja2 for server-side HTML rendering. The application is fully dockerized and configured for continuous deployment on the Render cloud platform.

## Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **Frontend:** HTML, CSS, Jinja2 Templates
* **Containerization:** Docker
* **Deployment:** Render (Platform-as-a-Service)
* **Version Control:** Git / GitHub

## Project Structure
```text
portfolio/
├── main.py              # FastAPI application routing and absolute path configurations
├── Dockerfile           # Docker image build instructions (Python 3.11-slim)
├── requirements.txt     # Python dependencies (FastAPI, Uvicorn, Jinja2, etc.)
├── templates/           # Jinja2 HTML templates (index.html)
└── static/              # Static assets (CSS, headshot images)
