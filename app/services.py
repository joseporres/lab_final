import csv
from app import models, schemas,crud
from app.database import SessionLocal
import pandas as pd
from app.chromadb import client,collection
# from chromadb.utils import embedding_functions
# from chromadb.config import Settings


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
    
def getMoviesByPront(prompt,n_results=1):
    results = collection.query(
    query_texts=[prompt],
    n_results=n_results
    )
    #traeme los documentos en merge por salto de linea 
    documents=  results['documents'][0]
    formated_documents = '\n'.join(documents)
    return formated_documents