import os
import logging
import re
from pathlib import Path
from ..utils.file_tools import get_file_hash,scan_directory_for_books
from ..parsing.factory import create_parser

logger = logging.getLogger(__name__)

class LibraryManager:
    def __init__(self, db, cover_dir = 'assets/covers'):
        self.db = db
        self.cover_dir = Path(cover_dir)
        self.cover_dir.mkdir(parents=True, exist_ok=True)

    def _sanitize_filename(self, filename: str) -> str:
        
        if not filename:
            logger.info("Failed to get title")
            return "unknown_book"
        s = filename.strip().replace(" ", "_")

        s = re.sub(r'[\\/*?:"<>|]', '', s)
        return s
        
    
    def scan_library(self,books_dir):

        books_path = Path(books_dir)
        found_books = scan_directory_for_books(books_path)
        
        for book_path in found_books:
            try:
                book_hash = get_file_hash(book_path)

                if not self.db.book_exist(book_hash):
                    book_parser = create_parser(book_path)
                    book_parser.read_ebook()

                    # Extract metadata
                    title = book_parser.get_title or book_path.stem
                    author = book_parser.get_author or "Unknown author"
                    
                    db_cover_path = None

                    cover_data, cover_ext = book_parser.get_cover()
                    
                    if cover_data and cover_ext:

                        safe_title = self._sanitize_filename(title)
                        cover_filename = f"{safe_title}{cover_ext}"
                        absolute_cover_path = self.cover_dir / cover_filename

                        with open(absolute_cover_path, 'wb') as cover_file:
                            cover_file.write(cover_data)
                        
                        db_cover_path = str(absolute_cover_path)
                        logger.info(f"Saved cover for {title} to {absolute_cover_path}")

                    self.db.add_book(
                        book_hash = book_hash,
                        file_path = str(book_path),
                        cover_path = db_cover_path,
                        title = title,
                        author = author
                    )
            except Exception:
                logger.exception(f"Failed to add bokk at {book_path}")
        


                
                
                
        
