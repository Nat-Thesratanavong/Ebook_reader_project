from ..parsing.factory import create_parser

def test_get_images():
    test_file_path = "./tests/sample_files/pg100-images.epub"
    parser = create_parser(test_file_path)
    success = parser.read_ebook()
    print(parser.get_images().keys())

    assert success