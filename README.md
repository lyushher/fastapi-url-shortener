<h1 align="center">FastAPI URL Shortener</h1>

<p align="center">
URL Shortening API with persistent storage and automated deployment workflows.
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
  <img src="https://img.shields.io/github/v/release/lyushher/fastapi-url-shortener?color=success" alt="GitHub Release" />
</p>



## Overview
A URL shortening API that generates short links and redirects requests to their original destinations through a REST interface.

The service manages URL creation, short code mapping, and redirection workflows while maintaining persistent URL records for later retrieval.

---

## Tech Stack

| Layer                | Technology     |
| -------------------- | -------------- |
| API Framework        | FastAPI        |
| Database             | PostgreSQL     |
| Container Runtime    | Docker         |
| CI/CD Platform       | GitHub Actions |
| Cloud Infrastructure | AWS EC2        |
| Language             | Python 3.11    |


---

## URL Processing Flow

1. A long URL is submitted to the API.
2. A unique short code is generated or a custom code is validated.
3. The URL mapping is stored in PostgreSQL.
4. The API returns a shortened URL.
5. Requests to the short URL are redirected to the original destination.


---

## API Endpoints

You can use tools like Swagger UI or Postman to test these endpoints interactively.

| Method | Route         | Description                   |
|--------|---------------|-------------------------------|
| POST   | `/shorten`    | Shorten a long URL            |
| GET    | `/{shortcode}`| Redirect to original URL      |
| GET    | `/urls`       | (Optional) List all URLs      |
| DELETE | `/{shortcode}`| (Optional) Delete a short URL |


---

## Setup & Local Development

```bash
git clone https://github.com/lyushher/fastapi-url-shortener.git
cd fastapi-url-shortener

docker compose up --build
```


---


## Running with Docker

The project is available as a prebuilt Docker image and can be executed without cloning the repository.

### Pull the Image

```bash
docker pull firdevsakbayir/urlshortener:latest

docker run -d -p 8001:8001 firdevsakbayir/urlshortener:latest
```

### Access the API

Once the container is running, the API documentation is available at:

```text
http://localhost:8001/docs
```

---

## License

This project is open-source and available under the terms of the [MIT License](LICENSE).



