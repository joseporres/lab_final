from pydantic import BaseModel
from typing import List


class MovieSchema(BaseModel):
    id: int
    title: str
    genres: str

    class Config:
        orm_mode = True

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "genres": self.genres
        }


class RatingSchema(BaseModel):
    id: int
    userId: int
    movieId: int
    rating: int
    timestamp: int

    class Config:
        orm_mode = True

    def serialize(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "movieId": self.movieId,
            "rating": self.rating,
            "timestamp": self.timestamp
        }


class TagSchema(BaseModel):
    id: int
    userId: int
    movieId: int
    tag: str
    timestamp: int

    class Config:
        orm_mode = True

    def serialize(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "movieId": self.movieId,
            "tag": self.tag,
            "timestamp": self.timestamp
        }
