from fastapi import FastAPI
from typing import Dict, List
from random import choice
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

images = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def generate_jsons() -> List[Dict[str, str]]:
    jsons = []
    for i in range(10):
        title = "Щтора " + str(choice(range(i+1)))
        description = "Гардина " + str(i+1)
        image = choice(images)
        jsons.append({"title": title, "description": description, "image": image})
    return jsons
