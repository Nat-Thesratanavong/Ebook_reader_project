import ebooklib
from ebooklib import epub
from .ebook_parser import ebook_parser


# TO-DO: This parser needs working on chapters definition, load_chapters, get_chapter method.
class epub_parser(ebook_parser):
    def __init__(self, file_path):
        super().__init__(file_path)

        self.book = None
        self.chapters = []

    def read_ebook(self):
        if not self.validate_path():
            return None

        try:
            book = epub.read_epub(self.file_path)

            self.book = book
            return True
        except Exception as e:
            print(f"Error: could not read EPUB file at {self.file_path}. Details: {e}")
            self.book = None
        return False

    def load_chapters(self):
        chapters = []
        if not self.book:
            return None
        try:
            for item in self.book.get_items():
                if item.get_type() == ebooklib.ITEM_DOCUMENT:
                    chapters.append(item)
            self.chapters = chapters
        except Exception as e:
            print(f"Error: could not get chapters from {self.file_path}. Details: {e}")

    def get_meta(self):
        if not self.book:
            return None
        try:
            meta = self.book.metadata
            return meta
        except Exception as e:
            print(
                f"Error: could not read EPUB meta data at {self.file_path}. Details: {e}"
            )
        return None

    def get_chapter(self, target_chapter):
        if not self.chapters:
            return None
        if target_chapter < 0 | target_chapter > len(self.chapters):
            return None
        try:
            chapter = self.chapters[target_chapter]
            raw_data = chapter.get_content()
            html_string = raw_data.decode("utf-8")
            return html_string
        except Exception as e:
            print(
                f"Error: could not read EPUB meta data at {self.file_path}. Details: {e}"
            )
            return None

    def get_cover(self):
        meta_tags = self.book.get_metadata("OPF", "meta")

        cover_id = None

        for tag in meta_tags:
            attributes = tag[1]

            if attributes.get("name") == "cover":
                cover_id = attributes.get("content")
                break

        if cover_id:
            cover_item = self.book.get_item_with_id(cover_id)
            if cover_item:
                return cover_item.get_content(), cover_item.media_type

        fallback_item = self.book.get_item_with_id("cover")
        if fallback_item:
            return fallback_item.get_content(), cover_item.get_media_type

        return None, None

    def get_images(self):
        images = {}
        for item in self.book.get_items_of_type(ebooklib.ITEM_IMAGE):
            images.update({item.get_name(): item.get_content()})
        return images
