# PyCutee (The PyQt5 Framework) V0.0.1

# PROJECT IS NOW ON [PyPi](https://pypi.org/project/PyCutee/0.0.4/)

PyCutee is a lightweight and stylish framework for PyQt5, designed to simplify the creation of modern and visually appealing graphical user interfaces (GUIs) in Python.

## Features

- Customizable Widgets: PyCutee offers a variety of customizable buttons, labels, and other widgets to enhance the visual appeal of your application.
- Pre-defined Color Schemes: Easily apply stylish color schemes to your application components with minimal effort.
- Simple API: The framework provides a straightforward and user-friendly API for creating sleek and modern interfaces.
- Documentation: Comprehensive documentation to help you get started and make the most of PyCutee.

You can install PyCutee via pip:

```bash
pip install pycutee
```

## Example Usage

Here's an example of how to use PyCutee in your project:

```py
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
```

## License

PyCutee is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
