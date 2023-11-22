import chromadb
from chromadb.config import Settings


client = chromadb.PersistentClient(path="./dbmovies_default",settings=Settings(allow_reset=True))
collection = client.get_or_create_collection(name="movies")
