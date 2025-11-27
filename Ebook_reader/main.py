import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# Import both backends
from gui.main_window import MainWindow
from gui.second_window import SecondWindowBackend

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    main_backend = MainWindow()
    second_backend = SecondWindowBackend()

    engine.rootContext().setContextProperty("backend", main_backend)

    qml_file = Path(__file__).parent / "gui/qml/main_window.qml"
    engine.load(qml_file)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
