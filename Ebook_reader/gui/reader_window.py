from PySide6.QtCore import QObject, Slot


class ReaderWindow(QObject):
    def __init__(self):
        super().__init__()

    @Slot()
    def do_something(self):
        print("Reader Screen Backend: Action Triggered!")
