import sys
from PyQt5.QtWidgets import QApplication

from db import inicializar_db
from screens import MainWindow


if __name__ == "__main__":
    inicializar_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
