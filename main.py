import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyCutee import Button_simple, Button_rounded

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('PyCutee Demo')

    layout = QVBoxLayout()

    regular_button = QPushButton("Regular QPushButton")
    layout.addWidget(regular_button)

    py_cutee_button = Button_simple()
    py_cutee_button("Click Me", "#95A5A6", "#95A5A6")
    layout.addWidget(py_cutee_button)

    py_cutee_button_rounded = Button_rounded()
    py_cutee_button_rounded("Click Me", "#95A5A6", "#95A5A6")
    layout.addWidget(py_cutee_button_rounded)

    window.setLayout(layout)

    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
