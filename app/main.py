from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.schemas import URLRequest
from app.services import generate_short_code, save_url, get_url

app = FastAPI()

@app.post("/shorten")
def shorten_url(request: URLRequest):
    short_code = generate_short_code()
    save_url(short_code, request.long_url)
    return {"short_url": f"http://localhost:8001/{short_code}"}

@app.get("/{short_code}")
def redirect_url(short_code: str):
    long_url = get_url(short_code)
    if long_url:
        return RedirectResponse(url=long_url)
    return {"error": "URL not found"}
