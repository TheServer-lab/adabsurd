import random
import os

IMAGE_DIR = "images"

PRODUCTS = ["AirCube", "Blorb", "NothingBurger", "Gravel+", "InfinitePDF"]
SUFFIXES = ["Pro", "Max", "Ultra", "Enterprise", "Cloud"]

FEATURES = [
    "AI-powered nonsense",
    "blockchain-enabled hydration",
    "synergy-driven innovation",
    "quantum-ready workflow",
    "now with 30% more abstraction"
]

PRICES = [
    "₹999/month",
    "₹6,999/month",
    "Free* (*not really)",
    "Pay per thought"
]

def get_random_image():
    try:
        files = os.listdir(IMAGE_DIR)
        images = [f for f in files if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]
        if not images:
            return None
        return "/images/" + random.choice(images)
    except:
        return None

def generate_ad(tone="corporate", chaos=50, format="300x250"):
    product = random.choice(PRODUCTS)
    suffix = random.choice(SUFFIXES)

    tagline = random.choice(FEATURES)
    price = random.choice(PRICES)

    if chaos > 70:
        tagline += " — now deprecated"

    if chaos > 90:
        product = "???"

    image = get_random_image()

    return {
        "title": f"{product} {suffix}",
        "tagline": tagline,
        "price": price,
        "bg_color": random.choice(["#111827", "#1f2937", "#0f172a"]),
        "image": image,
        "format": format
    }