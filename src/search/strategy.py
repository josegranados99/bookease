from abc import ABC, abstractmethod
from typing import Optional
from pydantic import BaseModel
from src.schema.book import (bookEntity, booksEntity)
from pymongo import MongoClient 

mongo_client = MongoClient()

class ModelBook(BaseModel):
    id: Optional[str]
    title: str
    author: str
    isbn: str
    editorial: str
    price: float
    amount: int

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