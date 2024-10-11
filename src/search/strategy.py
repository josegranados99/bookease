from abc import ABC, abstractmethod
from src.schema.book import (bookEntity, booksEntity)
from pymongo import MongoClient 

mongo_client = MongoClient()

class SearchStartegy(ABC):
    @abstractmethod
    def serch(key:str):
        pass

class SearchStrategyAll(SearchStartegy):
    def serch(key:str = None):
        return booksEntity(mongo_client.bookease.books.find())
    
class SearchStrategyTitle(SearchStartegy):
    def serch(key: str):
        return bookEntity(mongo_client.bookease.books.find_one({"title": key}))

class SearchStrategyAuthor(SearchStartegy):
    def serch(key: str):
        return booksEntity(mongo_client.bookease.books.find({"author": {"$regex":key, "$options": "i"}}))

class SearchStartegyISBN(SearchStartegy):
    def serch(key: str):
        return bookEntity(mongo_client.bookease.books.find_one({"isbn": key}))

class SearchStartegyEditorial(SearchStartegy):
    def serch(key: str):
        return booksEntity(mongo_client.bookease.books.find({"editorial": {"$regex":key, "$options": "i"}}))

class SearchStartegyPrice(SearchStartegy):
    def serch(key: str):
        return booksEntity(mongo_client.bookease.books.find({"price": float(key) }))