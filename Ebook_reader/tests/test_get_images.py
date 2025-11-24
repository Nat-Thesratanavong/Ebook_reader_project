from ..parsing.factory import create_parser
import os


def test_get_images():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    abs_test_file_path = os.path.join(base_dir, 'sample_files', 'pg100-images.epub')
    # test_file_path = "./tests/sample_files/pg100-images.epub"
    parser = create_parser(abs_test_file_path)
    success = parser.read_ebook()
    print(parser.get_images().keys())
    # print(parser.meta)

    assert success
