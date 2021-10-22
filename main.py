from importer import UserImporter, BookImporter, AuthorImporter, BookAuthorImporter, ShelfImporter, BookShelfImporter
from models import database, User, Book, Author, Shelf, BookShelf, BookAuthor, BookTranslator, UserAuthorRelation, \
    UserRelation
from reports import show_users, show_books, show_Book_shelves
from peewee import fn


def say_hi():
    print('Hey Mohammad')


def load_data():
    importer_classes = [
        UserImporter, BookImporter, AuthorImporter,
        BookAuthorImporter, ShelfImporter, BookShelfImporter
    ]
    for _class in importer_classes:
        _class.load()  # it uses to send data form json to database


def create_tables():
    database.create_tables(
        [User, Book, Author, Shelf, BookShelf,
         BookAuthor, BookTranslator, UserAuthorRelation,
         UserRelation]
    )


def show_user_data(username='hosein', password='654321'):
    user = User.authenticate(username, password)
    if user is None:
        print("User not found")
    # print(user.username, ', '.join([shelf.book.name for shelf in user.book_shelves]))
    print(f"username: {user.username}")
    print("Bookshelves")
    for shelf in user.shelves:
        print(f"\t{shelf.name} ({shelf.book_shelves.count()})")

    print("Books")
    for book_shelf_instance in user.book_shelves:
        print(f"\t{book_shelf_instance.book.name}")

    # book = Book.get_by_id(1)
    # read_shelf = user.shelves.where(Shelf.name == Shelf.CURRENTLY_READING)
    # new_book_shelf = BookShelf.create(
    #     user=user, book=book, shelf=read_shelf,
    #     start_date='2021-06-10', rate='2', comment='Very bad book'
    # )


def show_book_rates():
    query = BookShelf.select(
        BookShelf.book,
        fn.AVG(BookShelf.rate).alias('rates_avg'),
        fn.SUM(BookShelf.rate).alias('rates_sum'),
        fn.COUNT(BookShelf.rate).alias('rates_count')
    ).group_by(BookShelf.book)

    for q in query:
        print(q.book.id, q.rates_avg, q.rates_sum / q.rates_count)


def show_book_shelves():
    query = BookShelf.select(
        BookShelf.user,
        BookShelf.shelf,
        fn.COUNT(BookShelf.book).alias('books_count')
    ).group_by(BookShelf.shelf).order_by()

    for q in query:
        print(q.user.username, q.shelf.name, q.books_count)


def show_all_book_shelves():
    query = BookShelf.select()  # hit 1

    for q in query:
        print(q.rate)  # hit 2
        print(q.user.username)  # hit 3
        print(q.book.name)  # hit 4
        print('#' * 20)


def show_all_book_shelves_optimized():
    query = BookShelf.select().join(User) \
        .switch(BookShelf).join(Book) \
        .switch(BookShelf).join(Shelf)  # hit 1

    for q in query:
        print(q.rate)  # no hit
        print(q.user.username)  # no hit
        print(q.book.name)  # no hit 4
        print('#' * 20)


def show_data():
    print("#" * 79)
    show_users()
    print("#" * 79)
    show_books()
    print("#" * 79)
    show_Book_shelves()
    print("#" * 79)


if __name__ == "__main__":
    # say_hi()
    # create_tables()
    # load_data()
    # show_data()
    # show_user_data()
    # bs = BookShelf.get_by_id(2)
    # print(bs.shelf.name)
    # bs.change_to_read()
    # print(bs.shelf.name)
    # show_book_rates()
    show_book_shelves()
    # show_all_book_shelves()
    show_all_book_shelves_optimized()
