import logging
from pathlib import Path
from .library_manager import LibraryManager
from .database import LibraryDatabase

logger = logging.getLogger(__name__)
class ReaderModel:
    def __init__(self, library_manager: LibraryManager):
        self.libray_manager = library_manager
        self.current_book = None
        self.current_chapter = 0
        self.current_progress = 0.0
        logger.info("ReaderModel initialize")
    
    def get_book_by_hash(self, book_hash):
        return self.libray_manager.get_book_by_hash(book_hash)

    