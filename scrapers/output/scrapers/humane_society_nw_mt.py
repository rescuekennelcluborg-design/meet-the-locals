import requests
from bs4 import BeautifulSoup

def scrape_humane_society_nw_mt():
    url = "https://www.humanesocietypets.com/adoptable-dogs"
    dogs = []

    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "lxml")

        # Their site uses "pet-card" style blocks
        cards = soup.select(".pet-card, .pet")  # flexible selector

        for c in cards:
            name = c.select_one(".pet-name, h3")
            breed = c.select_one(".pet-breed, .breed")
            link = c.select_one("a")
            img = c.select_one("img")

            dogs.append({
                "name": name.get_text(strip=True) if name else "",
                "breed": breed.get_text(strip=True) if breed else "",
                "url": link["href"] if link and link.has_attr("href") else url,
                "photo": img["src"] if img and img.has_attr("src") else "",
                "shelter": "Humane Society of Northwest Montana",
                "location": "Kalispell, MT"
            })

    except Exception as e:
        print("Error scraping HS Northwest MT:", e)

    return dogs
