import os
from pathlib import Path
from ..utils.file_tools import get_file_hash,scan_directory_for_books

class library_manager:
    def __init__(self, db, cover_dir = 'assets/covers'):
        self.db = db
        self.cover_dir = Path(cover_dir)
        self.cover_dir.mkdir(parents=True, exist_ok=True)
        


