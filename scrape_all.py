import json
from pathlib import Path

from scrapers.yvas import scrape_yvas

OUTPUT_PATH = Path("output/dogs.json")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

def main():
    dogs = []

    yvas_dogs = scrape_yvas()
    print(f"YVAS returned {len(yvas_dogs)} dogs")
    dogs += yvas_dogs

    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(dogs, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(dogs)} dogs to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
