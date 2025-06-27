# Resume Parser API

A FastAPI backend to extract structured data from resumes and save to MongoDB.

## Features
- Upload PDF resumes
- Extract key information (name, email, skills)
- Store data in MongoDB
- Built with FastAPI and Python

## Tech Stack
- Python
- FastAPI
- MongoDB

## How to Run
```bash
git clone https://github.com/yourusername/resume-parser-api.git
cd resume-parser-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload