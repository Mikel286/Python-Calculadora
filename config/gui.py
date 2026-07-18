from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton

class Window(QWidget):

    def __init__(self, position_x, position_y, width, height):
        
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(position_x, position_y, width, height)

        self.start_gui()

    def create_button(self, text, value):
        button = QPushButton(text)
        button.value = value
        button.clicked.connect(lambda: print(f"Soy el boton con el valor: {button.value}"))
        return button

    def create_row(self, row):
        button_row = QHBoxLayout()
        for element in row:
            button = self.create_button(text = element, value = element)
            button_row.addWidget(button)
        return button_row

    def create_matrix(self):

        calculator = QVBoxLayout()
        elements = [["7", "8", "9", "/"],
                    ["4", "5", "6", "*"],
                    ["1", "2", "3", "-"],
                    ["0", ".", "=", "+"]]
        
        for row in elements:
            button_row = self.create_row(row)
            calculator.addLayout(button_row)
        return calculator

    def start_gui(self):

        self.calculator = self.create_matrix()
        self.setLayout(self.calculator)
        self.show()
