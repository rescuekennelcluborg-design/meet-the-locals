import requests
from bs4 import BeautifulSoup

YVAS_URL = "https://yvas.org/adopt/dogs/"  # e.g. https://yvas.org/adoptable-dogs

BULLY_KEYWORDS = ["pit", "bully", "stafford", "american bulldog", "american bull", "blockhead"]

def is_bully_type(text: str) -> bool:
    if not text:
        return False
    t = text.lower()
    return any(k in t for k in BULLY_KEYWORDS)

def scrape_yvas():
    resp = requests.get(YVAS_URL, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    dogs = []

    # This is a generic pattern; we’ll refine if needed
    cards = soup.find_all(["article", "div"], class_=lambda c: c and ("dog" in c.lower() or "pet" in c.lower() or "animal" in c.lower()))

    for card in cards:
        name = None
        breed = None
        age = None
        photo = None
        url = None

        # Name
        h = card.find(["h2", "h3", "h4"])
        if h:
            name = h.get_text(strip=True)

        # Link
        a = card.find("a", href=True)
        if a:
            url = a["href"]
            if url.startswith("/"):
                url = "https://yvas.org" + url

        # Image
        img = card.find("img")
        if img and img.get("src"):
            photo = img["src"]
            if photo.startswith("/"):
                photo = "https://yvas.org" + photo

        # Text blob for breed/age
        text = card.get_text(" ", strip=True)
        breed = text
        age = None

        if not name:
            continue

        if not is_bully_type(breed):
            continue

        dogs.append({
            "name": name,
            "breed": breed,
            "age": age,
            "shelter": "Yellowstone Valley Animal Shelter",
            "location": "Billings, MT",
            "url": url,
            "photo": photo
        })

    return dogs
