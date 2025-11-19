import ebooklib 
from ebooklib import epub
from .ebook_parser import ebook_parser

class epub_parser(ebook_parser):

    def __init__(self, file_path):
        super().__init__(file_path)

        self.book = None
        self._meta = None
        self._chapters = []

    def read_ebook(self):
        if not self.validate_path():
            return None
        
        try:
            book = epub.read_epub(self.file_path)

            self._book = book
            self._load_meta()
            self._load_chapters()
            

            return True
        except Exception as e:
            print(f"Error: could not read EPUB file at {self.file_path}. Details: {e}")
            self._book = None
        return False
    
    
    
    def _load_meta(self):
        if not self._book:
            return None
        
        try:
            meta = self._book.metadata
            self._meta = meta
            if not self._meta:
                return False
            return True
        except Exception as e:
            print(f"Error: oculd not read EPUB meta data at {self.file_path}. Details: {e}")
            self._meta = None
        return False
    
    def _load_chapters(self):
        for item in self._book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                self._chapters.append(item)
        return True
    def get_meta(self):
            if(self._meta):
                meta = self._meta
            else:
                meta = None
            return meta
    
    def get_chapter(self, target_chapter):
        if(target_chapter < 0 | target_chapter > len(self._chapters)):
            return None
        try:
            chapter = self._chapters[target_chapter]
            raw_data = chapter.get_content()
            html_string = raw_data.decode('utf-8')   
            return html_string
        except Exception as e:
            print(f"Error: oculd not read EPUB meta data at {self.file_path}. Details: {e}")
            return None