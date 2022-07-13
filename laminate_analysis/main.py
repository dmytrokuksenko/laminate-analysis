"""
Main file for the laminate analysis project.

Author: Dmytro Kuksenko
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 300)
    w.move(300, 300)
    w.setWindowTitle("Composite Materials Analysis Tools")

    w.show()

    sys.exit(app.exec())