from PySide6.QtCore import QObject, Slot


class SecondWindowBackend(QObject):
    def __init__(self):
        super().__init__()

    @Slot()
    def do_something(self):
        print("Second Screen Backend: Action Triggered!")
