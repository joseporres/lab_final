from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Movie(Base):
    __tablename__ = "movies"
    #title,genres
    movieId = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    genres = Column(String)
    ratings = relationship("Rating", back_populates="movie")
    tags = relationship("Tag", back_populates="movie")


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userId = Column(Integer)
    movieId = Column(Integer, ForeignKey("movies.movieId"))
    rating = Column(Integer)
    timestamp = Column(Integer)
    movie = relationship("Movie", back_populates="ratings")


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userId = Column(Integer)
    movieId = Column(Integer, ForeignKey("movies.movieId"))
    tag = Column(String)
    timestamp = Column(Integer)
    movie = relationship("Movie", back_populates="tags")