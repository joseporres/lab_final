from sqlalchemy.orm import  Session
from sqlalchemy.dialects.sqlite import insert
from app import models, schemas


def addChunkMovies(db:Session, movies: list[schemas.MovieSchema]):

    values = [movie.dict() for movie in movies]
      # Insertar o actualizar en lotes
    db.execute(
        insert(models.Movie)
        .values(values)
        .on_conflict_do_update(
            index_elements=['id'],
            set_={'title': insert(models.Movie).excluded.title, 'genres': insert(models.Movie).excluded.genres}
        )
    )

    db.commit()
    db.close()

def addChunkTags(db:Session, tags: list[schemas.TagSchema]):

    values = [tag.dict() for tag in tags]
      # Insertar o actualizar en lotes
    db.execute(
        insert(models.Tag)
        .values(values)
        .on_conflict_do_update(
            index_elements=['id'],
            set_={'userId': insert(models.Tag).excluded.userId, 'movieId': insert(models.Tag).excluded.movieId, 'tag': insert(models.Tag).excluded.tag, 'timestamp': insert(models.Tag).excluded.timestamp}
        )
    )

    db.commit()
    db.close()

def addChunkRatings(db:Session, ratings: list[schemas.RatingSchema]):

    values = [rating.dict() for rating in ratings]
      # Insertar o actualizar en lotes
    db.execute(
        insert(models.Rating)
        .values(values)
        .on_conflict_do_update(
            index_elements=['id'],
            set_={'userId': insert(models.Rating).excluded.userId, 'movieId': insert(models.Rating).excluded.movieId, 'rating': insert(models.Rating).excluded.rating, 'timestamp': insert(models.Rating).excluded.timestamp}
        )
    )

    db.commit()
    db.close()