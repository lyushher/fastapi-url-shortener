import string
import random
from app.database import url_db  # veritabani gibi davranan dict

#kisa kod uretici
def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# url kaydetme
def save_url(short_code, long_url):
    url_db[short_code] = long_url

# url getirme (yonlendirme icin)
def get_url(short_code):
    return url_db.get(short_code)

