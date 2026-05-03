import requests
from bs4 import BeautifulSoup
import json

URL = "https://yvas.org/adopt/dogs/"

# Keywords that count as pit bull–type dogs
BULLY_KEYWORDS = [
    "pit", "staffordshire", "american bully", "bully", "amstaff",
    "american pit bull", "staffy"
]

def is_bully(breed_text):
    breed_lower = breed_text.lower()
    return any(keyword in breed_lower for keyword in BULLY_KEYWORDS)

def scrape_yvas():
    r = requests.get(URL, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    dogs = []

    listings = soup.find_all("div", class_="sabai-entity")
    for listing in listings:
        # IMAGE
        img_tag = listing.find("img")
        image = img_tag["src"] if img_tag else None

        # NAME + DETAIL PAGE
        name_tag = listing.find("a", class_="sabai-entity-permalink")
        if not name_tag:
            continue
        name = name_tag.text.strip()
        link = name_tag["href"]

        # CUSTOM FIELDS
        fields = listing.find_all("div", class_="sabai-directory-field")
        data = {}
        for field in fields:
            label = field.find("span", class_="sabai-field-label")
            value = field.find("span", class_="sabai-field-value")
            if label and value:
                key = label.text.replace(":", "").strip().lower()
                data[key] = value.text.strip()

        breed = data.get("breed", "")
        sex = data.get("sex", "")
        age = data.get("age", "")
        status = data.get("current status", "")
        color = data.get("color", "")
        arms_id = data.get("arms id", "")

        # FILTER: Only pit bull–type dogs
        if not is_bully(breed):
            continue

        dogs.append({
            "name": name,
            "image": image,
            "link": link,
            "breed": breed,
            "sex": sex,
            "age": age,
            "status": status,
            "color": color,
            "arms_id": arms_id
        })

    return dogs

if __name__ == "__main__":
    dogs = scrape_yvas()
    with open("yvas_pitbulls.json", "w", encoding="utf-8") as f:
        json.dump(dogs, f, indent=4)
    print(f"Saved {len(dogs)} pit bull–type dogs to yvas_pitbulls.json")
