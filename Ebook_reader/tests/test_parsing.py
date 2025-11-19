from Ebook_reader.parsing.epub_parser import epub_parser
from Ebook_reader.parsing.factory import create_parser

def test_epub_parser_can_read_file():
    test_file_path = "./Ebook_reader/tests/sample_files/pg100-images.epub"
    parser = create_parser(test_file_path)
    success = parser.read_ebook()
    # print(parser.get_chapter(2))
    
    

    assert success == True
    assert parser._meta
    assert parser._chapters
    