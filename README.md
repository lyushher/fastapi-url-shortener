<h1 align="center">🔗 FastAPI URL Shortener</h1>

<p align="center">
A high-performance, Dockerized URL Shortener API built with <strong>FastAPI</strong>, <strong>PostgreSQL</strong>, and <strong>Docker</strong>, deployed using <strong>GitHub Actions</strong> and <strong>AWS EC2</strong> with full CI/CD automation.
</p>

---

<p align="center">
  <img src="https://github.com/lyushher/fastapi-url-shortener/actions/workflows/deploy.yml/badge.svg" />
  <img src="https://img.shields.io/badge/FastAPI-⚡-green" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" />
  <img src="https://img.shields.io/badge/platform-ubuntu-lightgrey" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Dockerized-Yes-blue?logo=docker" />
  <img src="https://img.shields.io/badge/python-3.11+-blue" />
  <img src="https://img.shields.io/docker/image-size/firdevsakbayir/urlshortener/latest" />
</p>
<p align="center">
  <img src="https://img.shields.io/github/license/lyushher/fastapi-url-shortener?color=yellow" />
</p>

---

## 🌐 Project Overview

This is a production-ready **URL Shortener API** designed for performance and scalability.  
It allows users to:

- Convert long URLs into short, shareable links
- Redirect users to original destinations using the short code
- Easily integrate into frontend apps, internal tools, or public services

Whether you're building a microservice architecture or a personal project,  
this API is optimized for **speed, modularity, and real-world deployment**.

---

## 🛠️ Tech Stack

This project is built using modern and scalable technologies to ensure high performance, reliability, and maintainability:

- **🚀 Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/) – A modern, high-performance web framework for building APIs with Python 3.11+ based on standard Python type hints.
- **🐘 Database:** [PostgreSQL](https://www.postgresql.org/) – A powerful, production-grade relational database system used for persistent URL storage.
- **🐳 Containerization:** [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/) – For building, packaging, and running the app in isolated environments, ensuring platform consistency.
- **⚙️ CI/CD Automation:** [GitHub Actions](https://github.com/features/actions) – Automated build, test, and deployment pipeline triggered on code push to `main`.
- **☁️ Deployment Target:** [AWS EC2 (Ubuntu 22.04)](https://aws.amazon.com/ec2/) – Cloud infrastructure hosting the application, with port `8000` publicly exposed for API access.
- **🔐 Secure Access:** SSH key-based authentication ensures safe and authorized deployments to the cloud server.
- **📦 Package Management:** `pip` with a clean `requirements.txt` for dependency management.

---

## 📈 Features

- ✅ Shortens long URLs with customizable short codes
- ✅ Redirects to original URL using short code
- ✅ Generates random short codes if none is provided
- ✅ Fully Dockerized for consistent builds
- ✅ PostgreSQL for persistent, scalable storage
- ✅ Clean, modular architecture for maintainability
- ✅ One-click deployment to AWS via GitHub Actions

## 🔐 Security & Authentication

> ℹ️ Note: This project does not implement authentication or rate limiting.  
If deployed in a public environment, consider adding access control or usage limits to prevent abuse.

---

## 📡 API Endpoints

| Method | Route         | Description                   |
|--------|---------------|-------------------------------|
| POST   | `/shorten`    | Shorten a long URL            |
| GET    | `/{shortcode}`| Redirect to original URL      |
| GET    | `/urls`       | (Optional) List all URLs      |
| DELETE | `/{shortcode}`| (Optional) Delete a short URL |


### Swagger UI Preview

You can explore the live API docs here:  
👉 [http://16.171.2.202:8001/docs](http://16.171.2.202:8001/docs)

---

## ⚙️ Setup & Local Development

```bash
# Clone repository
git clone https://github.com/lyushher/fastapi-url-shortener.git
cd fastapi-url-shortener

# Start services locally
docker compose up --build

```

---

## 🔁 CI/CD Pipeline

This project follows a fully automated CI/CD process using GitHub Actions:

1. **Push to `main`**: Every code change merged into the main branch triggers the pipeline.
2. **Build & Test**: GitHub Actions builds the Docker image and runs tests to ensure stability.
3. **SSH into EC2**: Secure connection is established to the production EC2 instance.
4. **Pull Latest Code**: The latest codebase is pulled from the GitHub repository.
5. **Rebuild Docker Container**: The container is rebuilt to reflect the new changes.
6. **Restart Application**: The old container is gracefully stopped and replaced with the new version.

---

## ⚠️ Known Limitations

Even though the service is production-ready, the current version includes the following constraints:

- ❌ No user authentication or API key validation  
- ❌ No analytics or click tracking system  
- ❌ No expiration or time-to-live (TTL) feature for short URLs  
- ❌ No support for custom domains (e.g., yourdomain.com/xyz)  
- ❌ No frontend interface – this is a pure backend API

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

