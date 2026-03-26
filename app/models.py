from pydantic import BaseModel

class Ad(BaseModel):
    title: str
    tagline: str
    price: str
    cta: str
    bg_color: str