from ..core.database import LibraryDatabase

def test_db_creation_and_query():
    db = LibraryDatabase()
    count = LibraryDatabase.get_book_count(db)

    print(count)