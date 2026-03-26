from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.generator import generate_ad

app = FastAPI(title="AdAbsurd API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")

@app.get("/")
def root():
    return {"message": "AdAbsurd API is running"}

@app.get("/ad")
def get_ad(tone: str = "corporate", chaos: int = 50, format: str = "300x250"):
    return generate_ad(tone=tone, chaos=chaos, format=format)