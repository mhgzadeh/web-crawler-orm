from importer import UserImporter, BookImporter, AuthorImporter, BookAuthorImporter, ShelfImporter, BookShelfImporter
from models import database, User, Book, Author, Shelf, BookShelf, BookAuthor, BookTranslator, UserAuthorRelation, \
    UserRelation
from reports import show_users, show_books, show_Book_shelves


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
    show_user_data()
    # bs = BookShelf.get_by_id(2)
    # print(bs.shelf.name)
    # bs.change_to_read()
    # print(bs.shelf.name)
