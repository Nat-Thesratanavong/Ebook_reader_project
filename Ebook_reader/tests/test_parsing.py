from Ebook_reader.parsing.epub_parser import epub_parser

def test_epub_parser_can_read_file():
    test_file_path = "./Ebook_reader/tests/sample_files/pg100-images.epub"
    parser = epub_parser(test_file_path)
    success = parser.read_ebook()
    print(parser.meta)

    assert success == True
    assert parser.meta