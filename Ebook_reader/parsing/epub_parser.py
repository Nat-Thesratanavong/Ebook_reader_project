from ebooklib import epub
from .ebook_parser import ebook_parser

class epub_parser(ebook_parser):

    def __init__(self, file_path):
        super().__init__(file_path)

        self.book = None
        self.meta = None

    def read_ebook(self):
        if not self.validate_path():
            return None
        
        try:
            book = epub.read_epub(self.file_path)

            self.book = book
            self.get_meta()

            return True
        except Exception as e:
            print(f"Error: could not read EPUB file at {self.file_path}. Details: {e}")
            self.book = None
        return False
    
    def get_meta(self):
        if not self.book:
            return None
        
        try:
            meta = self.book.metadata
            self.meta = meta
            if not self.meta:
                return False
            return True
        except Exception as e:
            print(f"Error: oculd not read EPUB meta data at {self.file_path}. Details: {e}")
            self.meta = None
        return False