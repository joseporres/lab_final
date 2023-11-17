import csv
from . import models, schemas,crud
from .database import SessionLocal

def insert_movie_csv(): 
    movies = []
    with open('./data/movies.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movies.append(schemas.MovieSchema(**row))
    with SessionLocal() as db:
        crud.addChunkMovies(db,movies)
        return {"status": "success", "message": f"Success insert {len(movies)} data of movies.csv"}
    

def insert_rating_csv(): 
    ratings = []
    with open('data/ratings.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ratings.append(schemas.RatingSchema(**row))
    with SessionLocal() as db:
        crud.addChunkRatings(db,ratings)
        return {"status": "success", "message": f"Success insert {len(ratings)} data of ratings.csv"}

def insert_tag_csv():
    tags = []
    with open('data/tags.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tags.append(schemas.TagSchema(**row))
    with SessionLocal() as db:
        crud.addChunkTags(db,tags)
        return {"status": "success", "message": f"Success insert {len(tags)} data of tags.csv"}