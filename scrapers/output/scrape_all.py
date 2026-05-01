import json
from breed_filter import is_bully_breed

def main():
    all_dogs = []

    # placeholder for incoming scraper results
    # each scraper will return a list of dicts like:
    # {"name": "...", "breed": "...", "url": "...", "photo": "...", "shelter": "...", "location": "..."}

    # Example structure:
    # all_dogs.extend(scrape_humane_society_western_mt())
    # all_dogs.extend(scrape_flathead_county())
    # etc.

    filtered = [dog for dog in all_dogs if is_bully_breed(dog.get("breed", ""))]

    with open("output/dogs.json", "w") as f:
        json.dump({"dogs": filtered}, f, indent=2)

    print(f"Saved {len(filtered)} bully‑type dogs to output/dogs.json")

if __name__ == "__main__":
    main()
import json
from breed_filter import is_bully_breed

def main():
    all_dogs = []

    # placeholder for incoming scraper results
    # each scraper will return a list of dicts like:
    # {"name": "...", "breed": "...", "url": "...", "photo": "...", "shelter": "...", "location": "..."}

    # Example structure:
    # all_dogs.extend(scrape_humane_society_western_mt())
    # all_dogs.extend(scrape_flathead_county())
    # etc.

    filtered = [dog for dog in all_dogs if is_bully_breed(dog.get("breed", ""))]

    with open("output/dogs.json", "w") as f:
        json.dump({"dogs": filtered}, f, indent=2)

    print(f"Saved {len(filtered)} bully‑type dogs to output/dogs.json")

if __name__ == "__main__":
    main()
