# from Ebook_reader.parsing.epub_parser import epub_parser
from Ebook_reader.parsing.factory import create_parser
from ..utils.file_tools import scan_directory_for_books

# from pathlib import Path
import os


def test_epub_parser_can_read_file():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    abs_test_file_path = os.path.join(base_dir, "sample_files", "pg100-images.epub")
    parser = create_parser(abs_test_file_path)
    parser.read_ebook()
    parser.load_chapters()
    file_content = parser.get_chapter(2)
    with open("my_file.html", "w", encoding="utf-8") as file:
        file.write(file_content)
    success = parser.read_ebook()

    assert success
    # assert parser.chapters


def test_epub_parser_interface_with_file_scan():
    test_file_path = "./"
    files = scan_directory_for_books(test_file_path)
    meta = []
    for f in files:
        parser = create_parser(f)
        parser.read_ebook()
        meta.extend(parser.get_meta())
    # print(meta)
