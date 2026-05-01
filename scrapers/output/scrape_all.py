import json

# import the breed filter
from breed_filter import is_bully_breed

# import your first scraper
from scrapers.humane_society_western_mt import scrape_humane_society_western_mt


def main():
    all_dogs = []

    # --- RUN SCRAPERS ---
    all_dogs.extend(scrape_humane_society_western_mt())

    # --- FILTER FOR BULLY BREEDS ---
    filtered = [
        dog for dog in all_dogs
        if is_bully_breed(dog.get("breed", ""))
    ]

    # --- SAVE OUTPUT ---
    with open("output/dogs.json", "w") as f:
        json.dump({"dogs": filtered}, f, indent=2)

    print(f"Saved {len(filtered)} bully‑type dogs to output/dogs.json")


if __name__ == "__main__":
    main()
