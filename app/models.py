from sqlalchemy import Boolean,Float, Column, ForeignKey, Integer, PrimaryKeyConstraint, String
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
    id = Column(Integer)
    userId = Column(Integer)
    movieId = Column(Integer, ForeignKey("movies.movieId"))
    rating = Column(Float)
    timestamp = Column(Integer)
    movie = relationship("Movie", back_populates="ratings")
    __table_args__ = (
        PrimaryKeyConstraint('userId', 'movieId', 'rating'),
        {}
    )


class Tag(Base):
    __tablename__ = "tags"
    userId = Column(Integer)
    movieId = Column(Integer, ForeignKey("movies.movieId"))
    tag = Column(String)
    timestamp = Column(Integer)
    movie = relationship("Movie", back_populates="tags")
    __table_args__ = (
        PrimaryKeyConstraint('userId', 'movieId', 'tag'),
        {}
    )