import os
from pathlib import Path
from ..utils.file_tools import get_file_hash,scan_directory_for_books

class library_manager:
    def __init__(self, db, cover_dir = 'assets/covers'):
        self.db = db
        self.cover_dir = Path(cover_dir)
        self.cover_dir.mkdir(parents=True, exist_ok=True)
    
    def scan_library(self,books_dir):
        unlisted_books = []
        hashed_books = []
        books_dir = Path(books_dir)
        books = scan_directory_for_books(books_dir)
        
        for book in books:
            book_hash = get_file_hash(book)

            if not self.db.book_exist(book_hash):
                
        



