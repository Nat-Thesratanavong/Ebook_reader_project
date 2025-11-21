from pathlib import Path
import hashlib


def scan_directory_for_books(directory_path):

    path = Path(directory_path)
    if not path.exists():
        return []

    extension = ["*.epub", "*.pdf"]
    found_files = []

    for ext in extension:
        found_files.extend(path.rglob(ext))

    return found_files


def get_file_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256.update(byte_block)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None
