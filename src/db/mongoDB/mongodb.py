from ..database import DatabaseAbstractFactory
# from dotenv import load_dotenv
from pymongo import MongoClient, errors 
# import os

MONGO_HOST = "localhost"
MONGO_PORT = "27017"
MONGO_TIMEOUT = 1000

class DatabaseMongoDB(DatabaseAbstractFactory):
    _instance = None
    _uri = None
    _timeout = None

    def __new__(cls):
        if cls._instance is None:
            print("First instance")
            cls._instance = super(DatabaseMongoDB, cls).__new__(cls)
            cls._uri = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"
            cls._timeout = MONGO_TIMEOUT

        return cls._instance

    def connect(self, db_name:str)->MongoClient:
        print(self._uri)
        try:
            client:MongoClient = MongoClient(self._uri, serverSelectionTimeoutMS = self._timeout)
            mongo_db = client["bookease"]
            print(f"Connected to {db_name}")
            return mongo_db
        except errors.ServerSelectionTimeoutError as error_tiemout:
            print(f"Error timeout: {error_tiemout}")
        except errors.ConnectionFailure as error_connection:
            print(f"Error connection: {error_connection}") 
