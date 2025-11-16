import ebooklib as eb
from ebooklib import epub
from .ebook_parser import ebook_parser

class epub_parser(ebook_parser):

    def read_ebook(self):
        if not self.validate_path():
            return None
        
        book = epub.read_epub(self.file_path)
        return book