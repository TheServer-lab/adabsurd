import random

PRODUCTS = ["AirCube", "Blorb", "NothingBurger", "Gravel+", "InfinitePDF"]
SUFFIXES = ["Pro", "Max", "Ultra", "Enterprise", "Cloud"]
CTAS = ["Buy Now", "Subscribe", "Upgrade Today", "Experience Nothing"]

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

def generate_ad(tone="corporate", chaos=50):
    product = random.choice(PRODUCTS)
    suffix = random.choice(SUFFIXES)

    tagline = random.choice(FEATURES)
    price = random.choice(PRICES)
    cta = random.choice(CTAS)

    if chaos > 70:
        tagline += " — now deprecated"

    if chaos > 90:
        product = "???"

    return {
        "title": f"{product} {suffix}",
        "tagline": tagline,
        "price": price,
        "cta": cta,
        "bg_color": random.choice(["#111827", "#1f2937", "#0f172a"])
    }