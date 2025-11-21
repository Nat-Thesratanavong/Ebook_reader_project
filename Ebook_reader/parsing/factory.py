from pathlib import Path

from .epub_parser import epub_parser

# from pdf_parser import pdf_parser


def create_parser(file_path):
    path_obj = Path(file_path)
    extension = path_obj.suffix.lower()
    if extension == ".epub":
        return epub_parser(file_path)
    elif extension == ".pdf":
        # return pdf_parser(file_path)
        pass
    print(f"Warning: No parser found for extension '{extension}'")
    return None
