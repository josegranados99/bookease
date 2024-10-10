import pandas as pd
from ..db.mongoDB.mongodb import DatabaseMongoDB

class SeedSingleton:
    _intance = None
    _up_seed  = None

    def __new__(cls, path: str):
        if cls._intance is None:
            print("Seed instance")
            cls.path = path
            cls._intance = super(SeedSingleton, cls).__new__(cls)
        return cls._intance

    def seed(self):
        if self._up_seed is None:
            books_excel = pd.read_excel(self.path)
            mongo_client = DatabaseMongoDB()
            mongo_db = mongo_client.connect("bookease")
            mongo_db_collection = mongo_db["books"]

            for index,row in books_excel.iterrows():
                book = {
                "title": row['Title'],
                "author": row['Author'],
                "isbn": row['ISBN'],
                "editorial": row['Editorial'],
                "price": row['Price'],
                "amoutn": row['Amount'],
                }

                mongo_db_collection.insert_one(book)
            self._up_seed = True       
            print("Seed upp")

seed:SeedSingleton = SeedSingleton("../books.xlsx")
seed.seed()