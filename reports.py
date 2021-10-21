from models import User, Book, BookShelf


def show_users():
    users = User.select()
    for user in users:
        # shelves_count = Shelf.select().where(Shelf.user == user).count()
        shelves_count = user.shelves.count()
        shelves = ', '.join([shelf.name for shelf in user.shelves])
        print(user.username, '\t', shelves, '\t', user.book_shelves.count())


def show_books():
    books = Book.select()
    for book in books:
        authors = ', '.join([book_author.author.name for book_author in book.authors])
        print(f"{book.name}({book.isbn})", '\t', authors)


def show_Book_shelves():
    book_shelves = BookShelf.select()
    for book_shelf in book_shelves:
        # authors = ', '.join([book for book in book_shelf.book])
        print(f"{book_shelf.book.name}({book_shelf.book.isbn})", '\t', book_shelf.user.username)
