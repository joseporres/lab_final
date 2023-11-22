from pydantic import BaseModel
from typing import List


class MovieSchema(BaseModel):
    movieId: int
    title: str
    genres: str

    class Config:
        from_attributes = True

    def serialize(self):
        return {
            "movieId": self.movieId,
            "title": self.title,
            "genres": self.genres
        }


class RatingSchema(BaseModel):
    userId: int
    movieId: int
    rating: float
    timestamp: int

    class Config:
        from_attributes = True

    def serialize(self):
        return {
            "userId": self.userId,
            "movieId": self.movieId,
            "rating": self.rating,
            "timestamp": self.timestamp
        }


class TagSchema(BaseModel):
    userId: int
    movieId: int
    tag: str
    timestamp: int

    class Config:
        from_attributes = True

    def serialize(self):
        return {
            "userId": self.userId,
            "movieId": self.movieId,
            "tag": self.tag,
            "timestamp": self.timestamp
        }
