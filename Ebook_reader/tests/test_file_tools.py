from ..utils.file_tools import scan_directory_for_books


def test_file_scan():
    success = scan_directory_for_books("../")
    assert success
