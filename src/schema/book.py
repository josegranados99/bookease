def bookEntity(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "isbn": book["isbn"],
        "editorial": book["editorial"],
        "price": book["price"],
        "amoutn": book["amoutn"],
    }

def booksEntity(books) -> list:
    return [bookEntity(book) for book in books]