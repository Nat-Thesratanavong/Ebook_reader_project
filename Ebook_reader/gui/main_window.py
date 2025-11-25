from PySide6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QWidget
# from .book_list_view import BookListView
# from .book_details_view import BookDetailsView

class MainWindow(QMainWindow):
    def __init__(self, library_manager):
        super().__init__()
        self.library_manager = library_manager
        self.setWindowTitle("E-Reader")
        self.setGeometry(100, 100, 800, 600)

        