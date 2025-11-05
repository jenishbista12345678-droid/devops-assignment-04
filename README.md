# 🐍 Flask App — Dockerized with GitHub Actions & Dependabot

This project is a **Python Flask web application** containerized using **Docker** and automated with **GitHub Actions**.  
It demonstrates key DevOps concepts including CI/CD, environment variable management, and dependency automation.

---

## 🚀 Features

- Flask app served through **Gunicorn**
- Two HTML endpoints:
  - `/` → Displays a custom message from environment variable `APP_MESSAGE`
  - `/health` → Displays the app’s health status from environment variable `APP_HEALTH`
- Dockerized for easy local and cloud deployment
- Automated build & test pipeline via **GitHub Actions**
- **Dependabot** configured for automatic dependency updates (Python, Docker, GitHub Actions)

---

## 🧩 File Structure
```sh
flask-docker-github-actions-assignment/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
├── README.md
└── .github
    └── dependabot.yml
    └── workflows
       └── ci.yml

````
---

## ⚙️ Environment Variables

| Variable | Description | Example Value |
|-----------|--------------|----------------|
| `APP_MESSAGE` | Message displayed on `/` | `"Hello from Flask!"` |
| `APP_HEALTH` | Health status shown on `/health` | `"OK"` |
| `FLASK_ENV` | Flask environment | `"production"` |
