import string
import random
from app.database import url_db

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def save_url(short_code, long_url):
    url_db[short_code] = long_url

def get_url(short_code):
    return url_db.get(short_code)

