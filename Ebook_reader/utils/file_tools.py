from pathlib import Path

def scan_directory_for_books(directory_path):

    path = Path(directory_path)
    if not path.exists():
        return []
    
    extension = ['*.epub','*.pdf']
    found_files = []

    for ext in extension:
        found_files.extend(path.rglob(ext)) 

    return found_files
