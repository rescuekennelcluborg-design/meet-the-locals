BULLY_KEYWORDS = [
    "pit", "pittie", "pitbull", "pit bull",
    "american pit bull", "apbt",
    "staffordshire", "staffy", "amstaff",
    "bully", "bully mix",
    "american bulldog",
    "mastiff", "mastiff mix",
    "boxer mix"
]

def is_bully_breed(breed_text: str) -> bool:
    if not breed_text:
        return False
    text = breed_text.lower()
    return any(keyword in text for keyword in BULLY_KEYWORDS)
