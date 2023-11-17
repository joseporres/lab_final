from fastapi import FastAPI, Header, Response
from starlette.middleware.cors import CORSMiddleware
from app.config.settings import api_settings
import uvicorn
from fastapi.responses import JSONResponse
import app.services as services
import xml.etree.ElementTree as ET
from app.models import Movie, Rating, Tag
from app.database import Base, engine, SessionLocal


app = FastAPI(
    title=api_settings.TITLE,
    openapi_url=f'{api_settings.PREFIX}/openapi.json',
    docs_url=f'{api_settings.PREFIX}/docs',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# set prefix  all routes

app.router.prefix = api_settings.PREFIX

@app.get("/insert")
def insert():
    services.insert_movie_csv()
    services.insert_rating_csv()
    services.insert_tag_csv()
    return {"message": "Insert data to database"}

@app.get("/")
def root():
    return {"message": f"Welcome to {api_settings.TITLE}"}

def run():
    Movie.metadata.create_all(bind=engine)
    Rating.metadata.create_all(bind=engine)
    Tag.metadata.create_all(bind=engine)
    uvicorn.run(app,
                host=api_settings.HOST,
                port=api_settings.PORT,
                )
