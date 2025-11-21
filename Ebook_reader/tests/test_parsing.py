from Ebook_reader.parsing.epub_parser import epub_parser
from Ebook_reader.parsing.factory import create_parser
from ..utils.file_tools import scan_directory_for_books
from pathlib import Path


def test_epub_parser_can_read_file():
    test_file_path = "./tests/sample_files/pg100-images.epub"
    parser = create_parser(test_file_path)
    success = parser.read_ebook()

    assert success == True
    assert parser._meta
    assert parser._chapters
    assert parser._cover


def test_epub_parser_interface_with_file_scan():
    test_file_path = "./"
    files = scan_directory_for_books(test_file_path)
    meta = []
    for f in files:
        parser = create_parser(f)
        parser.read_ebook()
        meta.extend(parser.get_meta())
    # print(meta)
