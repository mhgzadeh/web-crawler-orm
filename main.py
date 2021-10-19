from importer import UserImporter, BookImporter, AuthorImporter, BookAuthorImporter, ShelfImporter, BookShelfImporter
from models import database, User, Book, Author, Shelf, BookShelf, BookAuthor, BookTranslator, UserAuthorRelation, \
    UserRelation
from reports import show_users, show_books


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


def show_data():
    print("#" * 79)
    show_users()
    print("#" * 79)
    print("#" * 79)
    show_books()
    print("#" * 79)


if __name__ == "__main__":
    # say_hi()
    # create_tables()
    # load_data()
    show_data()
