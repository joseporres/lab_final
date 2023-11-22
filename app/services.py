import csv
from . import models, schemas,crud
from .database import SessionLocal
import pandas as pd

CHUNK_SIZE = 1000  # Adjust the chunk size as needed

def insert_movie_csv():
    with SessionLocal() as db:
        for chunk in pd.read_csv('./data/movies.csv', chunksize=CHUNK_SIZE):
            movies = [schemas.MovieSchema(**row) for _, row in chunk.iterrows()]
            crud.addChunkMovies(db, movies)
        return {"status": "success", "message": "Successfully inserted data from movies.csv"}

def insert_rating_csv():
    with SessionLocal() as db:
        for chunk in pd.read_csv('./data/ratings.csv', chunksize=CHUNK_SIZE):
            ratings = [schemas.RatingSchema(**row) for _, row in chunk.iterrows()]
            crud.addChunkRatings(db, ratings)
        return {"status": "success", "message": "Successfully inserted data from ratings.csv"}

def insert_tag_csv():
    with SessionLocal() as db:
        for chunk in pd.read_csv('./data/tags.csv', chunksize=CHUNK_SIZE):
            tags = [schemas.TagSchema(**row) for _, row in chunk.iterrows()]
            crud.addChunkTags(db, tags)
        return {"status": "success", "message": "Successfully inserted data from tags.csv"}