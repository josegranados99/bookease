from src.search.strategy import (
    SearchStartegy,
    SearchStrategyAll,
    SearchStrategyTitle,
    SearchStrategyAuthor,
    SearchStartegyISBN,
    SearchStartegyEditorial,
    SearchStartegyPrice
    )

class Search:
    def __init__(self, strategy:SearchStartegy) -> None:
        self._strategy:SearchStartegy = strategy
        
    def execute_search(self, key:str = None):
        if self._strategy:
            return self._strategy.serch(key)
        else:
            raise ValueError("Strategy not established")

def search_all_strategy():
    books = Search(SearchStrategyAll)
    return books.execute_search()

def search_title_strategy(key: str):
    book = Search(SearchStrategyTitle)
    return book.execute_search(key)

def search_author_strategy(key: str):
    books = Search(SearchStrategyAuthor)
    return books.execute_search(key)

def search_isbn_strategy(key: str):
    book = Search(SearchStartegyISBN)
    return book.execute_search(key)

def search_editorial_strategy(key: str):
    books = Search(SearchStartegyEditorial)
    return books.execute_search(key)

def search_price_strategy(key: str):
    books = Search(SearchStartegyPrice)
    return books.execute_search(key)