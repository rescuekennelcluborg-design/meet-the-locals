import requests
from bs4 import BeautifulSoup

def scrape_humane_society_western_mt():
    url = "https://www.myhswm.org/adoptable-dogs"
    dogs = []

    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "lxml")

        cards = soup.select(".animal-card")  # their site uses card elements

        for c in cards:
            name = c.select_one(".animal-name")
            breed = c.select_one(".animal-breed")
            link = c.select_one("a")
            img = c.select_one("img")

            dogs.append({
                "name": name.get_text(strip=True) if name else "",
                "breed": breed.get_text(strip=True) if breed else "",
                "url": link["href"] if link else url,
                "photo": img["src"] if img else "",
                "shelter": "Humane Society of Western Montana",
                "location": "Missoula, MT"
            })

    except Exception as e:
        print("Error scraping HSWM:", e)

    return dogs
