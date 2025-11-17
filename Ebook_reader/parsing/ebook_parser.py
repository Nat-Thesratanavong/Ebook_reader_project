from abc import ABC, abstractmethod
class ebook_parser(ABC):
    def __init__(self, file_path):
        self.file_path = file_path
        print(f"Parser created for file: {self.file_path}")
    
    @abstractmethod
    def read_ebook(self):
        pass
    @abstractmethod
    def get_meta(self):
        pass

    def validate_path(self):
        return bool(self.file_path)
    

