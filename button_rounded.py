from PyQt5.QtWidgets import QPushButton

class PyCuteeButtonRounded(QPushButton):
    def __init__(self):
        super().__init__()

    def __call__(self, title, color, hover_color):
        self.set_color(title, color, hover_color)

    def set_color(self, title, color, hover_color):
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: {'black' if color == "#FFFFFF" else 'white'};
                padding: 10px 20px;
                font-size: 16px;
                border: 2px solid {color};
                border-radius: 20px; /* Set border radius */
            }}
            QPushButton:hover {{
                background-color: {hover_color};
                border-color: {hover_color};
            }}
            QPushButton:checked {{
                background-color: {hover_color};
                border-color: {hover_color};
            }}
        """)
        self.setText(title)
