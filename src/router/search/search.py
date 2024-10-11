from src.router.router import RouterPrototype
from src.search.search import (
    search_all_strategy,
    search_title_strategy,
    search_author_strategy,
    search_isbn_strategy,
    search_editorial_strategy,
    search_price_strategy
    )

prototype_router = RouterPrototype(prefix="/router")
router = prototype_router.clone(new_prefix="/search")


@router.get("/")
def search_all():
    return search_all_strategy()

@router.get("/title/{title}")
def search_title(title: str):                                                                                                     
    return search_title_strategy(title)

@router.get("/autor/{author}")
def search_author(author: str):
    return search_author_strategy(author)

@router.get("/isbn/{isbn}")
def search_isbn(isbn: str):
    return search_isbn_strategy(isbn)

@router.get("/editorial/{editorial}")
def search_editorial(editorial: str):
    return search_editorial_strategy(editorial) 

@router.get("/price/{price}")
def search_price(price:str):
    return search_price_strategy(price)
