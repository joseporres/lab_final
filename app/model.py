from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Movie(Base):
    __tablename__ = "movies"
    #title,genres
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    genres = Column(String)


class Rating(Base):
    __tablename__ = "ratings"
    #userId,movieId,rating,timestamp
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer)
    movieId = Column(Integer, ForeignKey("movies.id"))
    rating = Column(Integer)
    timestamp = Column(Integer)

class Tag(Base):
    __tablename__ = "tags"
    #userId,movieId,tag,timestamp
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer)
    movieId = Column(Integer, ForeignKey("movies.id"))
    tag = Column(String)
    timestamp = Column(Integer)